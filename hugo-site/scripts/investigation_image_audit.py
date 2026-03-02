#!/usr/bin/env python3
"""Audit investigation image metadata and local static image coverage."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    tomllib = None


IMAGE_FIELDS = ("og_image", "twitter_image", "hero_image")
REQUIRED_FIELDS = ("og_image", "twitter_image")
RASTER_EXTS = {".jpg", ".jpeg", ".png", ".webp"}


@dataclass
class PageRecord:
    file_name: str
    title: str
    fields: dict[str, str]


def parse_front_matter(md_path: Path) -> dict[str, str]:
    raw = md_path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        return {}

    end = raw.find("\n---", 4)
    if end == -1:
        return {}

    fm = raw[4:end]
    data: dict[str, str] = {}
    for line in fm.splitlines():
        if not line or line.startswith(" ") or line.startswith("\t"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        key = key.strip()
        value = value.strip()
        if not value:
            continue
        if value[0] in {"'", '"'} and value[-1] == value[0]:
            value = value[1:-1]
        data[key] = value
    return data


def normalize_image_ref(raw_value: str) -> tuple[str | None, str | None]:
    if not raw_value:
        return None, None
    if raw_value.startswith(("http://", "https://")):
        parsed = urlsplit(raw_value)
        return parsed.netloc.lower(), parsed.path
    return None, raw_value


def load_base_host(config_path: Path) -> str | None:
    if tomllib is None or not config_path.exists():
        return None
    with config_path.open("rb") as fh:
        cfg = tomllib.load(fh)
    base_url = cfg.get("baseURL") or cfg.get("baseUrl") or cfg.get("baseurl")
    if not isinstance(base_url, str) or not base_url:
        return None
    return urlsplit(base_url).netloc.lower() or None


def collect_pages(content_dir: Path) -> list[PageRecord]:
    pages: list[PageRecord] = []
    for md_path in sorted(content_dir.glob("*.md")):
        fm = parse_front_matter(md_path)
        fields = {field: fm.get(field, "").strip() for field in IMAGE_FIELDS if fm.get(field)}
        pages.append(PageRecord(file_name=md_path.name, title=fm.get("title", md_path.stem), fields=fields))
    return pages


def run_audit(
    pages: list[PageRecord],
    static_dir: Path,
    allowed_host: str | None = None,
) -> dict:
    missing_fields = {field: [] for field in REQUIRED_FIELDS}
    missing_hero: list[str] = []
    missing_og_and_hero: list[str] = []
    missing_refs: list[dict[str, str]] = []
    host_mismatch: list[dict[str, str]] = []
    variant_gaps: list[dict[str, str]] = []

    seen_variant_keys: set[tuple[str, str]] = set()

    for page in pages:
        for field in REQUIRED_FIELDS:
            if field not in page.fields:
                missing_fields[field].append(page.file_name)
        if "hero_image" not in page.fields:
            missing_hero.append(page.file_name)
        if "og_image" not in page.fields and "hero_image" not in page.fields:
            missing_og_and_hero.append(page.file_name)

        for field, raw_value in page.fields.items():
            host, image_path = normalize_image_ref(raw_value)
            if host and allowed_host and host != allowed_host:
                host_mismatch.append(
                    {"page": page.file_name, "field": field, "host": host, "allowed_host": allowed_host}
                )
            if not image_path or not image_path.startswith("/"):
                continue

            local_path = static_dir / image_path.lstrip("/")
            if not local_path.exists():
                missing_refs.append(
                    {
                        "page": page.file_name,
                        "field": field,
                        "value": raw_value,
                        "expected_file": str(local_path),
                    }
                )
                continue

            ext = local_path.suffix.lower()
            if ext not in RASTER_EXTS:
                continue

            if ext in {".jpg", ".jpeg", ".png"}:
                webp_path = local_path.with_suffix(".webp")
                key = (str(local_path), str(webp_path))
                if not webp_path.exists() and key not in seen_variant_keys:
                    seen_variant_keys.add(key)
                    variant_gaps.append(
                        {
                            "page": page.file_name,
                            "field": field,
                            "source": str(local_path),
                            "missing_variant": str(webp_path),
                            "variant_type": "webp_pair",
                        }
                    )
            else:  # .webp
                jpg_path = local_path.with_suffix(".jpg")
                png_path = local_path.with_suffix(".png")
                jpeg_path = local_path.with_suffix(".jpeg")
                key = (str(local_path), str(jpg_path))
                if not jpg_path.exists() and not png_path.exists() and not jpeg_path.exists() and key not in seen_variant_keys:
                    seen_variant_keys.add(key)
                    variant_gaps.append(
                        {
                            "page": page.file_name,
                            "field": field,
                            "source": str(local_path),
                            "missing_variant": f"{jpg_path} | {png_path} | {jpeg_path}",
                            "variant_type": "raster_pair",
                        }
                    )

            if field != "hero_image":
                continue
            # When hero naming follows -hero-<size>, enforce baseline webp set.
            hero_match = re.match(r"^(?P<prefix>.+-hero-)(?P<size>\d+)(?P<ext>\.[^.]+)$", local_path.name)
            if not hero_match:
                continue
            prefix = hero_match.group("prefix")
            for size in ("960", "1600", "2400"):
                expected = local_path.with_name(f"{prefix}{size}.webp")
                key = (str(local_path), str(expected))
                if not expected.exists() and key not in seen_variant_keys:
                    seen_variant_keys.add(key)
                    variant_gaps.append(
                        {
                            "page": page.file_name,
                            "field": field,
                            "source": str(local_path),
                            "missing_variant": str(expected),
                            "variant_type": "hero_size_webp",
                        }
                    )

    return {
        "summary": {
            "pages_scanned": len(pages),
            "missing_required_field_count": sum(len(v) for v in missing_fields.values()),
            "missing_hero_field_count": len(missing_hero),
            "missing_og_and_hero_count": len(missing_og_and_hero),
            "missing_static_reference_count": len(missing_refs),
            "variant_gap_count": len(variant_gaps),
            "host_mismatch_count": len(host_mismatch),
        },
        "missing_fields": missing_fields,
        "missing_hero_image": missing_hero,
        "missing_og_and_hero": missing_og_and_hero,
        "missing_static_references": missing_refs,
        "variant_gaps": variant_gaps,
        "host_mismatch": host_mismatch,
    }


def maybe_generate_webp_variants(audit: dict) -> int:
    """Generate missing webp pairs when source raster exists and cwebp is available."""
    variant_gaps = audit.get("variant_gaps", [])
    candidates = [v for v in variant_gaps if v.get("variant_type") == "webp_pair"]
    if not candidates:
        return 0

    cwebp_path = shutil.which("cwebp")
    if not cwebp_path:
        return 0

    generated = 0
    for item in candidates:
        source = Path(item["source"])
        target = Path(item["missing_variant"])
        if not source.exists() or target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        proc = subprocess.run(
            [cwebp_path, "-quiet", "-q", "82", str(source), "-o", str(target)],
            capture_output=True,
            text=True,
        )
        if proc.returncode == 0 and target.exists():
            generated += 1
    return generated


def print_report(report: dict) -> None:
    summary = report["summary"]
    print("[investigation-image-audit] Summary")
    print(f"  pages scanned: {summary['pages_scanned']}")
    print(f"  missing required fields: {summary['missing_required_field_count']}")
    print(f"  missing og+hero entirely: {summary['missing_og_and_hero_count']}")
    print(f"  missing static references: {summary['missing_static_reference_count']}")
    print(f"  variant gaps: {summary['variant_gap_count']}")
    print(f"  host mismatches: {summary['host_mismatch_count']}")
    print(f"  pages without explicit hero_image: {summary['missing_hero_field_count']}")

    if report["missing_og_and_hero"]:
        print("  pages missing both og_image and hero_image:")
        for page in report["missing_og_and_hero"]:
            print(f"    - {page}")
    if report["missing_static_references"]:
        print("  missing static references:")
        for item in report["missing_static_references"]:
            print(f"    - {item['page']} :: {item['field']} -> {item['expected_file']}")
    if report["variant_gaps"]:
        print("  variant gaps:")
        for item in report["variant_gaps"]:
            print(f"    - {item['page']} :: {item['missing_variant']}")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--content-dir",
        default=str(repo_root / "content" / "investigation"),
        help="Path to investigation markdown content directory.",
    )
    parser.add_argument(
        "--static-dir",
        default=str(repo_root / "static"),
        help="Path to Hugo static directory.",
    )
    parser.add_argument(
        "--config",
        default=str(repo_root / "config.toml"),
        help="Path to Hugo config.toml for baseURL host checks.",
    )
    parser.add_argument("--report-json", default="", help="Optional path to write JSON report.")
    parser.add_argument(
        "--strict-variants",
        action="store_true",
        help="Fail when variant gaps are present.",
    )
    parser.add_argument(
        "--fix-webp",
        action="store_true",
        help="Generate missing .webp variants for referenced jpg/jpeg/png assets when possible.",
    )
    args = parser.parse_args()

    content_dir = Path(args.content_dir).resolve()
    static_dir = Path(args.static_dir).resolve()
    config_path = Path(args.config).resolve()

    if not content_dir.exists():
        print(f"[investigation-image-audit] ERROR: missing content dir {content_dir}", file=sys.stderr)
        return 2
    if not static_dir.exists():
        print(f"[investigation-image-audit] ERROR: missing static dir {static_dir}", file=sys.stderr)
        return 2

    allowed_host = load_base_host(config_path)
    pages = collect_pages(content_dir)
    report = run_audit(pages, static_dir, allowed_host=allowed_host)

    generated = 0
    if args.fix_webp:
        generated = maybe_generate_webp_variants(report)
        if generated:
            report = run_audit(pages, static_dir, allowed_host=allowed_host)
            report["summary"]["generated_webp_variants"] = generated

    if args.report_json:
        report_path = Path(args.report_json)
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    print_report(report)
    if generated:
        print(f"[investigation-image-audit] Generated webp variants: {generated}")

    summary = report["summary"]
    has_errors = summary["missing_required_field_count"] > 0 or summary["missing_static_reference_count"] > 0
    if args.strict_variants and summary["variant_gap_count"] > 0:
        has_errors = True
    return 1 if has_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
