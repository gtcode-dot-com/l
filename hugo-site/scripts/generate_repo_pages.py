#!/usr/bin/env python3
"""Generate Hugo content stubs for repositories from data/repos.yaml.

Each stub contains only title and description in front matter. All other
metadata is read from data/repos.yaml at build time by Hugo templates.

Default behavior is conservative: create missing files only.
"""

import sys
import yaml
import argparse
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
HUGO_ROOT = SCRIPT_DIR.parent
DATA_FILE = HUGO_ROOT / "data" / "repos.yaml"
CONTENT_DIR = HUGO_ROOT / "content" / "repos"


def load_repos():
    """Load repository data from YAML file"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) or []


def stub_content(repo):
    """Generate minimal YAML-front-matter stub content for a repo."""
    title = repo.get('name', repo.get('slug', 'Unknown'))
    desc = repo.get('summary', '')
    front_matter = {
        "title": str(title),
        "description": str(desc),
    }
    yaml_text = yaml.safe_dump(
        front_matter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    )
    return f"---\n{yaml_text}---\n"


def main():
    parser = argparse.ArgumentParser(
        description='Generate Hugo repo content stubs from data/repos.yaml'
    )
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without writing files')
    parser.add_argument('--prune', action='store_true',
                        help='Remove .md files with no matching slug in repos.yaml')
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument('--skip-existing', action='store_true',
                            help='Create only missing files (default behavior)')
    mode_group.add_argument('--overwrite', action='store_true',
                            help='Overwrite existing files in addition to creating missing files')
    parser.add_argument('--force', action='store_true',
                        help='Required with --overwrite to avoid accidental mass rewrites')
    args = parser.parse_args()

    if args.overwrite and not args.force:
        parser.error('--overwrite requires --force')

    repos = load_repos()
    if not repos:
        print("No repositories found in data file.")
        return 1

    print(f"Found {len(repos)} repositories in {DATA_FILE}")
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    slugs = set()
    created = 0
    updated = 0
    skipped = 0
    unchanged = 0

    for repo in repos:
        slug = repo.get('slug', '')
        if not slug:
            continue
        slugs.add(slug)
        content_file = CONTENT_DIR / f"{slug}.md"
        new_content = stub_content(repo)

        if content_file.exists():
            if not args.overwrite:
                skipped += 1
                continue
            existing = content_file.read_text(encoding='utf-8')
            if existing == new_content:
                unchanged += 1
                continue
            status = 'update'
            updated += 1
        else:
            status = 'create'
            created += 1

        if args.dry_run:
            print(f"  [DRY RUN] Would {status}: {content_file.name}")
        else:
            content_file.write_text(new_content, encoding='utf-8')
            print(f"  {status}: {content_file.name}")

    # Prune orphaned files
    pruned = 0
    if args.prune:
        for md_file in CONTENT_DIR.glob("*.md"):
            if md_file.name == "_index.md":
                continue
            file_slug = md_file.stem
            if file_slug not in slugs:
                pruned += 1
                if args.dry_run:
                    print(f"  [DRY RUN] Would prune: {md_file.name}")
                else:
                    md_file.unlink()
                    print(f"  pruned: {md_file.name}")

    print(f"\nSummary: {created} created, {updated} updated, {skipped} skipped, "
          f"{unchanged} unchanged, {pruned} pruned")
    return 0


if __name__ == '__main__':
    sys.exit(main())
