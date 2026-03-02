#!/usr/bin/env python3
"""Site-wide image normalization audit and variant generator.

This script enforces the responsive image conventions used by template partials:
- Local raster images referenced from content/layouts must exist in static/.
- WebP responsive variants (`-<width>w.webp`) must exist for configured slot widths.
- Key templates must not bypass the shared responsive image partial with raw <img> tags.
- Markdown content should avoid raw HTML raster <img> tags (use Markdown image syntax/render hooks).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit


RASTER_EXTS = {".jpg", ".jpeg", ".png", ".webp"}
FRONT_MATTER_FIELDS = ("og_image", "twitter_image", "hero_image", "image")
LOCAL_IMAGE_PREFIXES = ("/img/", "/articles/")

MARKDOWN_IMAGE_RE = re.compile(r"!\[[^\]]*]\(([^)\s]+)")
HTML_IMG_RE = re.compile(r"<img\b[^>]*>", re.IGNORECASE)
HTML_SRC_RE = re.compile(r"""\bsrc\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
WIDTHS_RE = re.compile(r"widths:\s*\[([^\]]+)\]")

TEMPLATE_BYPASS_FILES = (
    "layouts/index.html",
    "layouts/investigation/list.html",
    "layouts/investigation/single.html",
    "layouts/investigation/series.html",
)


@dataclass(frozen=True)
class Ref:
    source_file: str
    source_kind: str
    raw_value: str
    normalized_path: str


def parse_front_matter(md_path: Path) -> dict[str, str]:
    text = md_path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    fm = text[4:end]
    out: dict[str, str] = {}
    for line in fm.splitlines():
        if not line or line.startswith((" ", "\t")):
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
        out[key] = value
    return out


def normalize_local_raster_path(raw: str) -> str | None:
    raw = raw.strip()
    if not raw:
        return None
    if raw.startswith(("http://", "https://")):
        parsed = urlsplit(raw)
        path = parsed.path
    else:
        path = raw
    if not path.startswith("/"):
        return None
    if not any(path.startswith(prefix) for prefix in LOCAL_IMAGE_PREFIXES):
        return None
    ext = Path(path).suffix.lower()
    if ext not in RASTER_EXTS:
        return None
    return path


def load_slot_widths(repo_root: Path) -> list[int]:
    slots_file = repo_root / "data" / "media_slots.yaml"
    defaults = [320, 360, 480, 600, 640, 760, 900, 920, 960, 1200, 1536, 1600, 2400]
    if not slots_file.exists():
        return defaults
    text = slots_file.read_text(encoding="utf-8", errors="replace")
    widths: set[int] = set()
    for match in WIDTHS_RE.finditer(text):
        for token in match.group(1).split(","):
            token = token.strip()
            if not token:
                continue
            try:
                widths.add(int(token))
            except ValueError:
                continue
    if not widths:
        return defaults
    return sorted(widths)


def collect_references(repo_root: Path) -> list[Ref]:
    refs: list[Ref] = []
    content_root = repo_root / "content"
    layouts_root = repo_root / "layouts"

    for md_path in sorted(content_root.rglob("*.md")):
        rel = md_path.relative_to(repo_root).as_posix()
        is_news_content = rel.startswith("content/news/")
        fm = parse_front_matter(md_path)
        for field in FRONT_MATTER_FIELDS:
            value = fm.get(field, "").strip()
            normalized = normalize_local_raster_path(value)
            if normalized:
                refs.append(Ref(rel, f"frontmatter:{field}", value, normalized))

        if not is_news_content:
            body = md_path.read_text(encoding="utf-8", errors="replace")
            for match in MARKDOWN_IMAGE_RE.finditer(body):
                raw_value = match.group(1).strip()
                normalized = normalize_local_raster_path(raw_value)
                if normalized:
                    refs.append(Ref(rel, "markdown-image", raw_value, normalized))

            for tag in HTML_IMG_RE.findall(body):
                src_match = HTML_SRC_RE.search(tag)
                if not src_match:
                    continue
                raw_value = src_match.group(1).strip()
                normalized = normalize_local_raster_path(raw_value)
                if normalized:
                    refs.append(Ref(rel, "raw-html-image", raw_value, normalized))

    for tpl_path in sorted(layouts_root.rglob("*.html")):
        rel = tpl_path.relative_to(repo_root).as_posix()
        text = tpl_path.read_text(encoding="utf-8", errors="replace")
        for tag in HTML_IMG_RE.findall(text):
            src_match = HTML_SRC_RE.search(tag)
            if not src_match:
                continue
            raw_value = src_match.group(1).strip()
            normalized = normalize_local_raster_path(raw_value)
            if normalized:
                refs.append(Ref(rel, "template-static-image", raw_value, normalized))

    dedup: dict[tuple[str, str], Ref] = {}
    for ref in refs:
        dedup[(ref.normalized_path, ref.source_file)] = ref
    return sorted(dedup.values(), key=lambda r: (r.normalized_path, r.source_file, r.source_kind))


def image_dimensions(img_path: Path) -> tuple[int, int]:
    proc = subprocess.run(
        ["identify", "-format", "%w %h", str(img_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return 0, 0
    parts = proc.stdout.strip().split()
    if len(parts) != 2:
        return 0, 0
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return 0, 0


def expected_widths(intrinsic_width: int, configured_widths: list[int]) -> list[int]:
    if intrinsic_width <= 0:
        return []
    return [w for w in configured_widths if 320 <= w <= intrinsic_width]


def generate_webp_variant(source: Path, target: Path, width: int) -> bool:
    target.parent.mkdir(parents=True, exist_ok=True)

    cwebp = shutil.which("cwebp")
    if cwebp:
        proc = subprocess.run(
            [cwebp, "-quiet", "-q", "82", "-resize", str(width), "0", str(source), "-o", str(target)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and target.exists():
            return True

    convert = shutil.which("convert")
    if convert:
        proc = subprocess.run(
            [convert, str(source), "-resize", f"{width}x", "-quality", "82", str(target)],
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode == 0 and target.exists():
            return True

    return False


def scan_template_bypass(repo_root: Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for rel_path in TEMPLATE_BYPASS_FILES:
        path = repo_root / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for tag in HTML_IMG_RE.findall(text):
            src_match = HTML_SRC_RE.search(tag)
            if not src_match:
                continue
            src = src_match.group(1).strip()
            if "{{" in src:
                violations.append({"file": rel_path, "reason": "dynamic-img-src", "tag": tag.strip()[:180]})
                continue
            if src.startswith("/") and Path(src).suffix.lower() in RASTER_EXTS:
                violations.append({"file": rel_path, "reason": "raw-raster-img-tag", "tag": tag.strip()[:180]})
    return violations


def scan_raw_html_raster_content(repo_root: Path) -> list[dict[str, str]]:
    violations: list[dict[str, str]] = []
    for md_path in sorted((repo_root / "content").rglob("*.md")):
        rel = md_path.relative_to(repo_root).as_posix()
        text = md_path.read_text(encoding="utf-8", errors="replace")
        for tag in HTML_IMG_RE.findall(text):
            src_match = HTML_SRC_RE.search(tag)
            if not src_match:
                continue
            src = src_match.group(1).strip()
            normalized = normalize_local_raster_path(src)
            if normalized:
                violations.append({"file": rel, "src": normalized, "tag": tag.strip()[:180]})
    return violations


def run_audit(repo_root: Path, fix_variants: bool) -> tuple[dict, int]:
    refs = collect_references(repo_root)
    slot_widths = load_slot_widths(repo_root)
    static_root = repo_root / "static"

    unique_paths = sorted({ref.normalized_path for ref in refs})
    missing_files: list[dict[str, str]] = []
    missing_variants: list[dict[str, str | int]] = []
    generated = 0

    for rel_path in unique_paths:
        disk_path = static_root / rel_path.lstrip("/")
        if not disk_path.exists() and rel_path.startswith("/articles/"):
            content_candidate = repo_root / "content" / rel_path.lstrip("/")
            if content_candidate.exists():
                disk_path = content_candidate

        if not disk_path.exists():
            referenced_by = [r for r in refs if r.normalized_path == rel_path]
            for ref in referenced_by:
                missing_files.append(
                    {
                        "path": rel_path,
                        "source_file": ref.source_file,
                        "source_kind": ref.source_kind,
                        "raw_value": ref.raw_value,
                    }
                )
            continue

        if rel_path.startswith("/img/"):
            width, _ = image_dimensions(disk_path)
            for target_width in expected_widths(width, slot_widths):
                variant_rel = f"{rel_path.rsplit('.', 1)[0]}-{target_width}w.webp"
                variant_disk = static_root / variant_rel.lstrip("/")
                if not variant_disk.exists():
                    if fix_variants and generate_webp_variant(disk_path, variant_disk, target_width):
                        generated += 1
                        continue
                    missing_variants.append(
                        {
                            "source": rel_path,
                            "missing_variant": variant_rel,
                            "target_width": target_width,
                            "intrinsic_width": width,
                        }
                    )

    if fix_variants and missing_variants:
        # Re-evaluate after attempted generation.
        still_missing: list[dict[str, str | int]] = []
        for item in missing_variants:
            variant_disk = static_root / str(item["missing_variant"]).lstrip("/")
            if not variant_disk.exists():
                still_missing.append(item)
        missing_variants = still_missing

    template_bypass = scan_template_bypass(repo_root)
    raw_html_raster = scan_raw_html_raster_content(repo_root)

    report = {
        "summary": {
            "references_scanned": len(refs),
            "unique_local_raster_paths": len(unique_paths),
            "missing_file_count": len(missing_files),
            "missing_variant_count": len(missing_variants),
            "template_bypass_count": len(template_bypass),
            "raw_html_raster_count": len(raw_html_raster),
            "generated_variant_count": generated,
        },
        "missing_files": missing_files,
        "missing_variants": missing_variants,
        "template_bypass": template_bypass,
        "raw_html_raster": raw_html_raster,
        "slot_widths": slot_widths,
    }

    has_errors = any(
        (
            report["summary"]["missing_file_count"] > 0,
            report["summary"]["missing_variant_count"] > 0,
            report["summary"]["template_bypass_count"] > 0,
            report["summary"]["raw_html_raster_count"] > 0,
        )
    )
    return report, (1 if has_errors else 0)


def print_report(report: dict) -> None:
    summary = report["summary"]
    print("[site-image-audit] Summary")
    print(f"  references scanned: {summary['references_scanned']}")
    print(f"  unique local raster paths: {summary['unique_local_raster_paths']}")
    print(f"  missing files: {summary['missing_file_count']}")
    print(f"  missing variants: {summary['missing_variant_count']}")
    print(f"  template bypass violations: {summary['template_bypass_count']}")
    print(f"  raw-html raster image violations: {summary['raw_html_raster_count']}")
    print(f"  generated variants: {summary['generated_variant_count']}")

    if report["missing_files"]:
        print("  missing files:")
        for item in report["missing_files"][:25]:
            print(f"    - {item['path']} ({item['source_file']} :: {item['source_kind']})")
    if report["missing_variants"]:
        print("  missing variants:")
        for item in report["missing_variants"][:40]:
            print(f"    - {item['missing_variant']} (from {item['source']})")
    if report["template_bypass"]:
        print("  template bypass violations:")
        for item in report["template_bypass"][:40]:
            print(f"    - {item['file']} :: {item['reason']}")
    if report["raw_html_raster"]:
        print("  raw-html raster violations:")
        for item in report["raw_html_raster"][:40]:
            print(f"    - {item['file']} :: {item['src']}")


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report-json",
        default="",
        help="Optional path to write full JSON report.",
    )
    parser.add_argument(
        "--fix-variants",
        action="store_true",
        help="Generate missing `-<width>w.webp` variants for referenced local raster images.",
    )
    args = parser.parse_args()

    report, exit_code = run_audit(repo_root, fix_variants=args.fix_variants)
    print_report(report)

    if args.report_json:
        out_path = Path(args.report_json)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
