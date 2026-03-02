#!/usr/bin/env python3
"""Deterministic SEO + build-pipeline audit for Hugo output.

This script audits built HTML output under `public/` and exits non-zero when
strict checks fail. It is designed to run locally, in full-publish flows, and
in CI/CD.
"""

from __future__ import annotations

import argparse
import json
import posixpath
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit
import xml.etree.ElementTree as ET

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


DEFAULT_BASE_URL = "https://gtcode.com/"
DEFAULT_NEWS_WINDOW_DAYS = 2
DATE_KEYS = {"datePublished", "dateModified", "dateCreated", "uploadDate"}
HTML_TAG_RE = re.compile(r"<[^>]+>")
PLACEHOLDER_RE = re.compile(r"(?i)(<nil>|\\bnil\\b|0000-00-00|0001-01-01|1970-01-01)")
WORKFLOW_FALLBACK_RE = re.compile(r'HUGO_VERSION\\s*=\\s*"([0-9]+\\.[0-9]+\\.[0-9]+)"')


@dataclass
class PageRecord:
    file_path: str
    rel_path: str
    rel_url: str
    expected_url: str
    title: str = ""
    meta_description: str = ""
    robots: str = ""
    canonical: str = ""
    og_title: str = ""
    og_description: str = ""
    twitter_title: str = ""
    twitter_description: str = ""
    h1_list: list[str] = field(default_factory=list)
    image_count: int = 0
    missing_alt_images: list[str] = field(default_factory=list)
    time_datetimes: list[str] = field(default_factory=list)
    jsonld_scripts: list[str] = field(default_factory=list)
    jsonld_types: set[str] = field(default_factory=set)
    jsonld_invalid_errors: list[str] = field(default_factory=list)
    jsonld_desc_html_hits: list[str] = field(default_factory=list)
    jsonld_placeholder_hits: list[str] = field(default_factory=list)
    jsonld_dates: list[str] = field(default_factory=list)

    @property
    def title_len(self) -> int:
        return len(self.title)

    @property
    def description_len(self) -> int:
        return len(self.meta_description.strip())

    @property
    def h1_count(self) -> int:
        return len(self.h1_list)

    @property
    def missing_alt_count(self) -> int:
        return len(self.missing_alt_images)

    @property
    def indexable(self) -> bool:
        if self.rel_url == "/404.html":
            return False
        return "noindex" not in self.robots.lower()

    def is_news_article(self) -> bool:
        parts = split_url_parts(self.rel_url)
        if len(parts) < 3:
            return False
        return parts[0] == "news"

    def is_news_section_index(self) -> bool:
        parts = split_url_parts(self.rel_url)
        if not parts:
            return False
        return parts[0] == "news" and len(parts) <= 2

    def is_repo_detail(self) -> bool:
        parts = split_url_parts(self.rel_url)
        return len(parts) >= 2 and parts[0] == "repos"


@dataclass
class RedirectRule:
    line_no: int
    source: str
    destination: str
    status: str = ""


class PageHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_chunks: list[str] = []
        self.in_title = False

        self.in_h1 = False
        self.current_h1_chunks: list[str] = []
        self.h1_list: list[str] = []

        self.in_jsonld_script = False
        self.current_jsonld_chunks: list[str] = []
        self.jsonld_scripts: list[str] = []

        self.meta_description = ""
        self.robots = ""
        self.canonical = ""
        self.og_title = ""
        self.og_description = ""
        self.twitter_title = ""
        self.twitter_description = ""

        self.image_count = 0
        self.missing_alt_images: list[str] = []
        self.time_datetimes: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr_map = {k.lower(): (v or "") for k, v in attrs}
        tag = tag.lower()

        if tag == "title":
            self.in_title = True
            return

        if tag == "h1":
            self.in_h1 = True
            self.current_h1_chunks = []
            return

        if tag == "meta":
            name = attr_map.get("name", "").strip().lower()
            prop = attr_map.get("property", "").strip().lower()
            content = attr_map.get("content", "").strip()

            if name == "description" and not self.meta_description:
                self.meta_description = content
            elif name == "robots" and not self.robots:
                self.robots = content
            elif name == "twitter:title" and not self.twitter_title:
                self.twitter_title = content
            elif name == "twitter:description" and not self.twitter_description:
                self.twitter_description = content
            elif prop == "og:title" and not self.og_title:
                self.og_title = content
            elif prop == "og:description" and not self.og_description:
                self.og_description = content
            return

        if tag == "link":
            rel = attr_map.get("rel", "")
            rel_tokens = [token.strip().lower() for token in rel.split() if token.strip()]
            if "canonical" in rel_tokens and not self.canonical:
                self.canonical = attr_map.get("href", "").strip()
            return

        if tag == "img":
            self.image_count += 1
            alt = attr_map.get("alt")
            if alt is None:
                self.missing_alt_images.append(attr_map.get("src", ""))
            return

        if tag == "time":
            dt = attr_map.get("datetime", "").strip()
            if dt:
                self.time_datetimes.append(dt)
            return

        if tag == "script":
            script_type = attr_map.get("type", "").lower()
            if "ld+json" in script_type:
                self.in_jsonld_script = True
                self.current_jsonld_chunks = []
            return

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
            return
        if tag == "h1":
            self.in_h1 = False
            text = normalize_whitespace("".join(self.current_h1_chunks))
            if text:
                self.h1_list.append(text)
            self.current_h1_chunks = []
            return
        if tag == "script" and self.in_jsonld_script:
            self.in_jsonld_script = False
            raw = "".join(self.current_jsonld_chunks).strip()
            if raw:
                self.jsonld_scripts.append(raw)
            self.current_jsonld_chunks = []
            return

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_chunks.append(data)
        if self.in_h1:
            self.current_h1_chunks.append(data)
        if self.in_jsonld_script:
            self.current_jsonld_chunks.append(data)

    def parsed_title(self) -> str:
        return normalize_whitespace("".join(self.title_chunks))


def normalize_whitespace(value: str) -> str:
    return re.sub(r"\\s+", " ", value or "").strip()


def split_url_parts(rel_url: str) -> list[str]:
    return [p for p in rel_url.strip("/").split("/") if p]


def normalize_url(url: str) -> str:
    if not url:
        return ""
    parts = urlsplit(url.strip())
    scheme = parts.scheme.lower()
    netloc = parts.netloc.lower()
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if not path.startswith("/"):
        path = f"/{path}"
    if parts.path.endswith("/") and not path.endswith("/"):
        path = f"{path}/"
    return urlunsplit((scheme, netloc, path, "", ""))


def build_expected_abs_url(base_url: str, rel_url: str) -> str:
    base = urlsplit(base_url.strip())
    scheme = (base.scheme or "https").lower()
    netloc = base.netloc.lower()
    base_path = base.path or "/"
    if not base_path.startswith("/"):
        base_path = f"/{base_path}"
    if not base_path.endswith("/"):
        base_path = f"{base_path}/"

    if rel_url == "/":
        joined_path = base_path
    else:
        rel = rel_url.lstrip("/")
        joined_path = posixpath.normpath(f"{base_path}{rel}")
        joined_path = re.sub(r"/{2,}", "/", joined_path)
        if rel_url.endswith("/") and not joined_path.endswith("/"):
            joined_path = f"{joined_path}/"
        if not joined_path.startswith("/"):
            joined_path = f"/{joined_path}"

    return normalize_url(urlunsplit((scheme, netloc, joined_path, "", "")))


def page_url_from_rel_path(rel_path: str) -> str:
    if rel_path == "index.html":
        return "/"
    if rel_path.endswith("/index.html"):
        base = rel_path[: -len("index.html")].rstrip("/")
        if not base:
            return "/"
        return f"/{base}/"
    return f"/{rel_path}"


def walk_json(node: Any, callback) -> None:
    if isinstance(node, dict):
        callback(node)
        for value in node.values():
            walk_json(value, callback)
    elif isinstance(node, list):
        for value in node:
            walk_json(value, callback)


def parse_jsonld_signals(raw_scripts: list[str]) -> tuple[set[str], list[str], list[str], list[str], list[str]]:
    types: set[str] = set()
    invalid_errors: list[str] = []
    desc_html_hits: list[str] = []
    placeholder_hits: list[str] = []
    dates: list[str] = []

    for raw in raw_scripts:
        try:
            payload = json.loads(raw)
        except Exception as exc:
            invalid_errors.append(str(exc))
            continue

        def callback(node: dict[str, Any]) -> None:
            value = node.get("@type")
            if isinstance(value, str):
                types.add(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str):
                        types.add(item)

            desc = node.get("description")
            if isinstance(desc, str) and HTML_TAG_RE.search(desc):
                desc_html_hits.append(desc)

            for key, value in node.items():
                if isinstance(value, str) and PLACEHOLDER_RE.search(value):
                    placeholder_hits.append(f"{key}={value}")
                if key in DATE_KEYS and isinstance(value, str) and value.strip():
                    dates.append(value.strip())

        walk_json(payload, callback)

    return types, invalid_errors, desc_html_hits, placeholder_hits, dates


def parse_iso_datetime(raw: str) -> datetime | None:
    value = (raw or "").strip()
    if not value:
        return None
    if value.endswith("Z"):
        value = f"{value[:-1]}+00:00"
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        try:
            dt = datetime.fromisoformat(f"{value}T00:00:00+00:00")
        except ValueError:
            return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def load_site_config(config_path: Path) -> tuple[str, dict[str, Any], list[str]]:
    warnings: list[str] = []
    if not config_path.exists():
        warnings.append(f"Config file not found: {config_path}")
        return DEFAULT_BASE_URL, {}, warnings
    if tomllib is None:
        warnings.append("tomllib unavailable; using default config values")
        return DEFAULT_BASE_URL, {}, warnings

    try:
        with config_path.open("rb") as handle:
            cfg = tomllib.load(handle)
    except Exception as exc:
        warnings.append(f"Unable to parse config TOML: {exc}")
        return DEFAULT_BASE_URL, {}, warnings

    base_url = cfg.get("baseURL") or DEFAULT_BASE_URL
    params = cfg.get("params") or {}
    if not isinstance(params, dict):
        params = {}
    return str(base_url), params, warnings


def parse_html_pages(public_dir: Path, base_url: str) -> list[PageRecord]:
    pages: list[PageRecord] = []
    for path in sorted(public_dir.rglob("*.html")):
        rel_path = path.relative_to(public_dir).as_posix()
        if rel_path.startswith("sources/"):
            continue
        rel_url = page_url_from_rel_path(rel_path)
        expected_url = build_expected_abs_url(base_url, rel_url)

        parser = PageHTMLParser()
        html = path.read_text(encoding="utf-8", errors="ignore")
        parser.feed(html)
        parser.close()

        types, invalid, desc_html, placeholders, dates = parse_jsonld_signals(parser.jsonld_scripts)

        record = PageRecord(
            file_path=str(path),
            rel_path=rel_path,
            rel_url=rel_url,
            expected_url=expected_url,
            title=parser.parsed_title(),
            meta_description=parser.meta_description,
            robots=parser.robots,
            canonical=parser.canonical,
            og_title=parser.og_title,
            og_description=parser.og_description,
            twitter_title=parser.twitter_title,
            twitter_description=parser.twitter_description,
            h1_list=parser.h1_list,
            image_count=parser.image_count,
            missing_alt_images=parser.missing_alt_images,
            time_datetimes=parser.time_datetimes,
            jsonld_scripts=parser.jsonld_scripts,
            jsonld_types=types,
            jsonld_invalid_errors=invalid,
            jsonld_desc_html_hits=desc_html,
            jsonld_placeholder_hits=placeholders,
            jsonld_dates=dates,
        )
        pages.append(record)
    return pages


def parse_sitemap_locs(path: Path) -> tuple[set[str], str | None]:
    if not path.exists():
        return set(), f"Missing sitemap file: {path}"
    try:
        root = ET.parse(path).getroot()
    except Exception as exc:
        return set(), f"Failed to parse XML {path}: {exc}"
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = set()
    for elem in root.findall(".//sm:url/sm:loc", ns):
        if elem.text:
            locs.add(normalize_url(elem.text.strip()))
    return locs, None


def parse_robots_crawl_delay(robots_path: Path) -> tuple[list[str], str | None]:
    if not robots_path.exists():
        return [], f"Missing robots.txt at {robots_path}"
    lines = robots_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    values: list[str] = []
    for raw in lines:
        line = raw.strip()
        if not line:
            continue
        match = re.match(r"(?i)^crawl-delay\\s*:\\s*(.+?)\\s*$", line)
        if match:
            values.append(match.group(1))
    return values, None


def parse_redirect_rules(path: Path) -> tuple[list[RedirectRule], str | None]:
    if not path.exists():
        return [], f"Missing redirects file: {path}"
    rules: list[RedirectRule] = []
    for idx, raw in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        source = parts[0]
        destination = parts[1]
        status = parts[2] if len(parts) >= 3 else ""
        rules.append(RedirectRule(line_no=idx, source=source, destination=destination, status=status))
    return rules, None


def redirect_pattern_matches_path(source_pattern: str, candidate_path: str) -> bool:
    pattern = source_pattern.strip()
    if not pattern.startswith("/"):
        return False

    regex_parts: list[str] = []
    index = 0
    while index < len(pattern):
        char = pattern[index]
        if char == "*":
            regex_parts.append(".*")
            index += 1
            continue
        if char == ":":
            end = index + 1
            while end < len(pattern) and (pattern[end].isalnum() or pattern[end] == "_"):
                end += 1
            token = pattern[index + 1 : end]
            if token:
                regex_parts.append(".*" if token.lower() == "splat" else "[^/]+")
                index = end
                continue
        regex_parts.append(re.escape(char))
        index += 1

    regex = f"^{''.join(regex_parts)}$"
    return re.match(regex, candidate_path) is not None


def redirect_rule_matches_repos(source_pattern: str) -> bool:
    candidates = ("/repos", "/repos/", "/repos/example", "/repos/example/")
    return any(redirect_pattern_matches_path(source_pattern, candidate) for candidate in candidates)


def check_workflow_alignment(
    workflow_path: Path | None,
    hugo_version_file: Path | None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    if workflow_path is None:
        checks.append(
            {
                "key": "workflow_alignment",
                "status": "WARN",
                "count": 1,
                "details": "Workflow path not provided; skipped version-drift checks",
                "examples": [],
            }
        )
        return checks

    if not workflow_path.exists():
        checks.append(
            {
                "key": "workflow_alignment",
                "status": "WARN",
                "count": 1,
                "details": f"Workflow file not found: {workflow_path}",
                "examples": [],
            }
        )
        return checks

    workflow_text = workflow_path.read_text(encoding="utf-8", errors="ignore")
    required_version = ""
    if hugo_version_file and hugo_version_file.exists():
        required_version = hugo_version_file.read_text(encoding="utf-8", errors="ignore").strip()

    fallback_match = WORKFLOW_FALLBACK_RE.search(workflow_text)
    fallback_version = fallback_match.group(1) if fallback_match else ""
    has_hugo_version_resolve = ".hugo-version" in workflow_text
    has_baseurl_override = "--baseURL" in workflow_text

    missing_hugo_version_ref = 0 if has_hugo_version_resolve else 1
    checks.append(
        {
            "key": "workflow_uses_hugo_version_file",
            "status": "PASS" if missing_hugo_version_ref == 0 else "FAIL",
            "count": missing_hugo_version_ref,
            "details": "Workflow should resolve Hugo version from .hugo-version",
            "examples": [str(workflow_path)] if missing_hugo_version_ref else [],
        }
    )

    fallback_mismatch = 0
    examples: list[str] = []
    if required_version and fallback_version and required_version != fallback_version:
        fallback_mismatch = 1
        examples.append(f"required={required_version}, workflow_fallback={fallback_version}")
    checks.append(
        {
            "key": "workflow_hugo_fallback_matches_required",
            "status": "PASS" if fallback_mismatch == 0 else "FAIL",
            "count": fallback_mismatch,
            "details": "Workflow fallback Hugo version should match .hugo-version",
            "examples": examples,
        }
    )

    baseurl_override_count = 1 if has_baseurl_override else 0
    checks.append(
        {
            "key": "workflow_avoids_baseurl_override",
            "status": "PASS" if baseurl_override_count == 0 else "FAIL",
            "count": baseurl_override_count,
            "details": "Workflow should not override canonical baseURL at build time",
            "examples": [str(workflow_path)] if baseurl_override_count else [],
        }
    )

    return checks


def add_check(
    checks: list[dict[str, Any]],
    key: str,
    count: int,
    details: str,
    examples: list[str] | None = None,
    warn_only: bool = False,
) -> None:
    examples = examples or []
    if count == 0:
        status = "PASS"
    elif warn_only:
        status = "WARN"
    else:
        status = "FAIL"
    checks.append(
        {
            "key": key,
            "status": status,
            "count": count,
            "details": details,
            "examples": examples[:20],
        }
    )


def run_audit(args: argparse.Namespace) -> tuple[dict[str, Any], int]:
    public_dir = Path(args.public_dir).resolve()
    config_path = Path(args.config).resolve()
    workflow_path = Path(args.workflow_path).resolve() if args.workflow_path else None
    hugo_version_file = Path(args.hugo_version_file).resolve() if args.hugo_version_file else None

    config_base_url, params, config_warnings = load_site_config(config_path)
    expected_base_url = args.base_url or config_base_url or DEFAULT_BASE_URL
    expected_base_url = normalize_url(expected_base_url)

    checks: list[dict[str, Any]] = []
    notes: list[str] = []
    notes.extend(config_warnings)

    if not public_dir.exists():
        report = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "strict_mode": args.strict,
            "base_url": expected_base_url,
            "summary": {"total_pages": 0, "indexable_pages": 0, "failed_checks": 1, "warn_checks": 0},
            "checks": [
                {
                    "key": "public_dir_exists",
                    "status": "FAIL",
                    "count": 1,
                    "details": f"Public directory not found: {public_dir}",
                    "examples": [],
                }
            ],
            "notes": notes,
        }
        return report, 1

    pages = parse_html_pages(public_dir, expected_base_url)
    indexable_pages = [page for page in pages if page.indexable]

    long_titles = [page for page in indexable_pages if page.title_len > args.max_title]
    long_descriptions = [page for page in indexable_pages if page.description_len > args.max_description]
    duplicate_h1 = [page for page in indexable_pages if page.h1_count > 1]
    missing_alt = [page for page in indexable_pages if page.missing_alt_count > 0]
    invalid_jsonld = [page for page in indexable_pages if page.jsonld_invalid_errors]
    jsonld_desc_html = [page for page in indexable_pages if page.jsonld_desc_html_hits]

    add_check(
        checks,
        "required.title_len_gt_65",
        len(long_titles),
        f"Indexable pages with title length > {args.max_title}",
        [page.rel_url for page in long_titles],
    )
    add_check(
        checks,
        "required.meta_description_len_gt_160",
        len(long_descriptions),
        f"Indexable pages with meta description length > {args.max_description}",
        [page.rel_url for page in long_descriptions],
    )
    add_check(
        checks,
        "required.duplicate_h1",
        len(duplicate_h1),
        "Indexable pages with multiple H1 elements",
        [page.rel_url for page in duplicate_h1],
    )
    add_check(
        checks,
        "required.missing_image_alt",
        len(missing_alt),
        "Indexable pages with missing/empty image alt text",
        [page.rel_url for page in missing_alt],
    )
    add_check(
        checks,
        "required.invalid_jsonld",
        len(invalid_jsonld),
        "Indexable pages with invalid JSON-LD scripts",
        [page.rel_url for page in invalid_jsonld],
    )
    add_check(
        checks,
        "required.jsonld_description_contains_html",
        len(jsonld_desc_html),
        "Indexable pages with JSON-LD description containing HTML tags",
        [page.rel_url for page in jsonld_desc_html],
    )

    robots_crawl_delay_values, robots_err = parse_robots_crawl_delay(public_dir / "robots.txt")
    if robots_err:
        add_check(
            checks,
            "required.robots_crawl_delay_policy",
            1,
            robots_err,
        )
    else:
        crawl_enabled = bool(params.get("robots_crawl_delay_enabled", False))
        crawl_seconds = int(params.get("robots_crawl_delay_seconds", 1))
        crawl_policy_failures = 0
        examples: list[str] = []
        if crawl_enabled:
            if len(robots_crawl_delay_values) != 1:
                crawl_policy_failures += 1
                examples.append(f"expected 1 Crawl-delay line, found {len(robots_crawl_delay_values)}")
            else:
                value = robots_crawl_delay_values[0]
                if not value.isdigit() or int(value) <= 0:
                    crawl_policy_failures += 1
                    examples.append(f"invalid Crawl-delay value: {value}")
                elif int(value) != crawl_seconds:
                    crawl_policy_failures += 1
                    examples.append(f"Crawl-delay mismatch: expected {crawl_seconds}, found {value}")
        else:
            if robots_crawl_delay_values:
                crawl_policy_failures += 1
                examples.append(f"unexpected Crawl-delay lines: {robots_crawl_delay_values}")
        add_check(
            checks,
            "required.robots_crawl_delay_policy",
            crawl_policy_failures,
            "robots.txt Crawl-delay must match config policy",
            examples,
        )

    redirects_path = public_dir / "_redirects"
    redirect_rules, redirects_error = parse_redirect_rules(redirects_path)
    repos_redirect_conflicts: list[str] = []
    if redirects_error:
        repos_redirect_conflicts.append(redirects_error)
    else:
        for rule in redirect_rules:
            source_lower = rule.source.lower()
            if source_lower == "/repos" or source_lower.startswith("/repos/"):
                repos_redirect_conflicts.append(
                    f"line {rule.line_no}: direct /repos rule ({rule.source} -> {rule.destination})"
                )
                continue
            if redirect_rule_matches_repos(rule.source):
                repos_redirect_conflicts.append(
                    f"line {rule.line_no}: wildcard can match /repos/ ({rule.source} -> {rule.destination})"
                )
    add_check(
        checks,
        "required.repos_redirect_conflicts",
        len(repos_redirect_conflicts),
        "Redirect rules must not rewrite first-party /repos/ URLs (including wildcard patterns)",
        repos_redirect_conflicts,
    )

    canonical_missing = [page for page in indexable_pages if not page.canonical]
    canonical_non_https = [page for page in indexable_pages if page.canonical and not page.canonical.startswith("https://")]
    canonical_mismatch = [
        page
        for page in indexable_pages
        if page.canonical and normalize_url(page.canonical) != normalize_url(page.expected_url)
    ]
    add_check(
        checks,
        "canonical.present",
        len(canonical_missing),
        "Indexable pages must include rel=canonical",
        [page.rel_url for page in canonical_missing],
    )
    add_check(
        checks,
        "canonical.https",
        len(canonical_non_https),
        "Canonical URLs must use HTTPS",
        [page.rel_url for page in canonical_non_https],
    )
    add_check(
        checks,
        "canonical.matches_expected_url",
        len(canonical_mismatch),
        "Canonical URLs on indexable pages must match expected page URL",
        [page.rel_url for page in canonical_mismatch],
    )

    social_missing = [
        page
        for page in indexable_pages
        if not page.og_title or not page.twitter_title or not page.og_description or not page.twitter_description
    ]
    social_title_mismatch = [
        page
        for page in indexable_pages
        if page.og_title and page.twitter_title and normalize_whitespace(page.og_title) != normalize_whitespace(page.twitter_title)
    ]
    social_desc_mismatch = [
        page
        for page in indexable_pages
        if page.og_description
        and page.twitter_description
        and normalize_whitespace(page.og_description) != normalize_whitespace(page.twitter_description)
    ]
    add_check(
        checks,
        "social.tags_present",
        len(social_missing),
        "OG/Twitter title and description tags must be present on indexable pages",
        [page.rel_url for page in social_missing],
    )
    add_check(
        checks,
        "social.title_parity",
        len(social_title_mismatch),
        "OG and Twitter titles should match",
        [page.rel_url for page in social_title_mismatch],
    )
    add_check(
        checks,
        "social.description_parity",
        len(social_desc_mismatch),
        "OG and Twitter descriptions should match",
        [page.rel_url for page in social_desc_mismatch],
    )

    sitemap_urls, sitemap_error = parse_sitemap_locs(public_dir / "sitemap.xml")
    if sitemap_error:
        add_check(checks, "sitemap.main_present_and_valid", 1, sitemap_error)
        sitemap_urls = set()
    else:
        add_check(checks, "sitemap.main_present_and_valid", 0, "sitemap.xml is present and parseable")

    news_sitemap_path = public_dir / "news-sitemap.xml"
    if news_sitemap_path.exists():
        news_sitemap_urls, news_sitemap_error = parse_sitemap_locs(news_sitemap_path)
        if news_sitemap_error:
            add_check(checks, "sitemap.news_present_and_valid", 1, news_sitemap_error)
            news_sitemap_urls = set()
        else:
            add_check(checks, "sitemap.news_present_and_valid", 0, "news-sitemap.xml is present and parseable")
    else:
        news_sitemap_urls = set()
        add_check(checks, "sitemap.news_present_and_valid", 0, "news-sitemap.xml not generated (skipped)")

    indexable_url_set = {normalize_url(page.expected_url) for page in indexable_pages}
    all_html_url_set = {normalize_url(page.expected_url) for page in pages}

    sitemap_missing_indexable = sorted(indexable_url_set - sitemap_urls)
    sitemap_html_non_indexable = sorted((sitemap_urls & all_html_url_set) - indexable_url_set)
    sitemap_non_html_entries = sorted(sitemap_urls - all_html_url_set)

    add_check(
        checks,
        "sitemap.indexable_parity",
        len(sitemap_missing_indexable),
        "Indexable HTML pages must exist in sitemap.xml",
        sitemap_missing_indexable,
    )
    add_check(
        checks,
        "sitemap.excludes_nonindex_html",
        len(sitemap_html_non_indexable),
        "sitemap.xml should not include non-indexable HTML pages",
        sitemap_html_non_indexable,
    )
    add_check(
        checks,
        "sitemap.non_html_entries",
        len(sitemap_non_html_entries),
        "sitemap.xml includes non-HTML entries (informational)",
        sitemap_non_html_entries,
        warn_only=True,
    )

    news_window_days = int(params.get("news_sitemap_window_days", DEFAULT_NEWS_WINDOW_DAYS))
    if news_window_days < 1:
        news_window_days = DEFAULT_NEWS_WINDOW_DAYS
    cutoff = datetime.now(timezone.utc) - timedelta(days=news_window_days)

    expected_news_recent: set[str] = set()
    news_missing_date: list[str] = []
    for page in indexable_pages:
        if not page.is_news_article():
            continue
        candidate_dates = page.jsonld_dates + page.time_datetimes
        parsed_dt: datetime | None = None
        for raw in candidate_dates:
            parsed_dt = parse_iso_datetime(raw)
            if parsed_dt:
                break
        if parsed_dt is None:
            news_missing_date.append(page.rel_url)
            continue
        if parsed_dt >= cutoff:
            expected_news_recent.add(normalize_url(page.expected_url))

    news_missing_expected = sorted(expected_news_recent - news_sitemap_urls)
    news_non_indexable = sorted(news_sitemap_urls - indexable_url_set)
    news_extra_indexable = sorted((news_sitemap_urls & indexable_url_set) - expected_news_recent)

    add_check(
        checks,
        "news_sitemap.expected_recent_indexable_present",
        len(news_missing_expected),
        "Recent indexable news articles should be present in news-sitemap.xml",
        news_missing_expected,
    )
    add_check(
        checks,
        "news_sitemap.excludes_non_indexable",
        len(news_non_indexable),
        "news-sitemap.xml should not include non-indexable URLs",
        news_non_indexable,
    )
    add_check(
        checks,
        "news_sitemap.extra_indexable_entries",
        len(news_extra_indexable),
        "news-sitemap.xml includes indexable URLs outside expected recency window",
        news_extra_indexable,
        warn_only=True,
    )
    add_check(
        checks,
        "news_sitemap.indexable_news_missing_dates",
        len(news_missing_date),
        "Indexable news articles without parseable date fields",
        news_missing_date,
        warn_only=True,
    )

    jsonld_placeholders = [page for page in indexable_pages if page.jsonld_placeholder_hits]
    add_check(
        checks,
        "jsonld.placeholder_values",
        len(jsonld_placeholders),
        "Indexable pages should not emit JSON-LD placeholder values (<nil>, zero dates, etc.)",
        [page.rel_url for page in jsonld_placeholders],
    )

    repo_missing_type = [
        page
        for page in indexable_pages
        if page.is_repo_detail() and page.rel_url != "/repos/" and "softwaresourcecode" not in {t.lower() for t in page.jsonld_types}
    ]
    news_article_missing_type = [
        page
        for page in indexable_pages
        if page.is_news_article() and not ({"newsarticle", "article"} & {t.lower() for t in page.jsonld_types})
    ]
    news_section_missing_collection = [
        page
        for page in indexable_pages
        if page.is_news_section_index() and "collectionpage" not in {t.lower() for t in page.jsonld_types}
    ]
    add_check(
        checks,
        "structured_data.repo_detail_type",
        len(repo_missing_type),
        "Indexable repo detail pages should include SoftwareSourceCode JSON-LD",
        [page.rel_url for page in repo_missing_type],
    )
    add_check(
        checks,
        "structured_data.news_article_type",
        len(news_article_missing_type),
        "Indexable news articles should include NewsArticle/Article JSON-LD",
        [page.rel_url for page in news_article_missing_type],
    )
    add_check(
        checks,
        "structured_data.news_section_type",
        len(news_section_missing_collection),
        "Indexable news section pages should include CollectionPage JSON-LD",
        [page.rel_url for page in news_section_missing_collection],
    )

    checks.extend(check_workflow_alignment(workflow_path, hugo_version_file))

    failed_checks = sum(1 for check in checks if check["status"] == "FAIL")
    warn_checks = sum(1 for check in checks if check["status"] == "WARN")

    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "strict_mode": args.strict,
        "base_url": expected_base_url,
        "config_path": str(config_path),
        "public_dir": str(public_dir),
        "summary": {
            "total_pages": len(pages),
            "indexable_pages": len(indexable_pages),
            "failed_checks": failed_checks,
            "warn_checks": warn_checks,
        },
        "counts": {
            "total_html_pages": len(pages),
            "indexable_pages": len(indexable_pages),
            "title_gt_65": len(long_titles),
            "meta_description_gt_160": len(long_descriptions),
            "duplicate_h1": len(duplicate_h1),
            "missing_alt": len(missing_alt),
            "invalid_jsonld": len(invalid_jsonld),
            "jsonld_description_contains_html": len(jsonld_desc_html),
            "sitemap_urls": len(sitemap_urls),
            "news_sitemap_urls": len(news_sitemap_urls),
            "expected_recent_news_urls": len(expected_news_recent),
        },
        "checks": checks,
        "notes": notes,
    }

    exit_code = 1 if args.strict and failed_checks > 0 else 0
    return report, exit_code


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Audit built Hugo output for SEO + pipeline regressions.")
    parser.add_argument("--public-dir", default="public", help="Path to Hugo public output directory")
    parser.add_argument("--config", default="config.toml", help="Path to Hugo config.toml")
    parser.add_argument("--base-url", default="", help="Expected canonical base URL override")
    parser.add_argument("--workflow-path", default="", help="Optional CI workflow file for drift checks")
    parser.add_argument("--hugo-version-file", default=".hugo-version", help="Path to .hugo-version file")
    parser.add_argument("--max-title", type=int, default=65, help="Max title length for required check")
    parser.add_argument("--max-description", type=int, default=160, help="Max meta description length for required check")
    parser.add_argument("--report-json", default="", help="Optional path to write JSON report")
    parser.add_argument("--strict", dest="strict", action="store_true", help="Fail with non-zero exit code on check failures")
    parser.add_argument("--no-strict", dest="strict", action="store_false", help="Always exit zero")
    parser.set_defaults(strict=True)
    return parser.parse_args(argv)


def print_summary(report: dict[str, Any]) -> None:
    summary = report["summary"]
    print("[seo-audit] Total HTML pages:", summary["total_pages"])
    print("[seo-audit] Indexable pages:", summary["indexable_pages"])
    print("[seo-audit] Failed checks:", summary["failed_checks"])
    print("[seo-audit] Warn checks:", summary["warn_checks"])
    for check in report["checks"]:
        status = check["status"]
        print(f"[seo-audit] {status:<4} {check['key']} (count={check['count']})")
        if status in {"FAIL", "WARN"} and check["examples"]:
            for example in check["examples"][:5]:
                print(f"[seo-audit]       - {example}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    report, exit_code = run_audit(args)

    if args.report_json:
        output_path = Path(args.report_json).resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"[seo-audit] JSON report written: {output_path}")

    print_summary(report)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
