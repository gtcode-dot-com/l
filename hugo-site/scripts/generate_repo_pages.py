#!/usr/bin/env python3
"""
Generate minimal Hugo content stubs for repositories from data/repos.yaml

Each stub contains only title and description in front matter. All other
metadata is read from data/repos.yaml at build time by the Hugo template.

Usage:
    python generate_repo_pages.py [--dry-run] [--prune]

Options:
    --dry-run   Show what would be done without writing files
    --prune     Remove .md files that have no matching slug in repos.yaml
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
    """Generate minimal stub content for a repo"""
    title = repo.get('name', repo.get('slug', 'Unknown'))
    desc = repo.get('summary', '')
    # Escape quotes for YAML safety
    title_escaped = title.replace('"', '\\"')
    desc_escaped = desc.replace('"', '\\"')
    return f'---\ntitle: "{title_escaped}"\ndescription: "{desc_escaped}"\n---\n'


def main():
    parser = argparse.ArgumentParser(
        description='Generate minimal Hugo content stubs from data/repos.yaml'
    )
    parser.add_argument('--dry-run', action='store_true',
                        help='Show what would be done without writing files')
    parser.add_argument('--prune', action='store_true',
                        help='Remove .md files with no matching slug in repos.yaml')
    args = parser.parse_args()

    repos = load_repos()
    if not repos:
        print("No repositories found in data file.")
        return 1

    print(f"Found {len(repos)} repositories in {DATA_FILE}")
    CONTENT_DIR.mkdir(parents=True, exist_ok=True)

    slugs = set()
    created = 0
    updated = 0
    unchanged = 0

    for repo in repos:
        slug = repo.get('slug', '')
        if not slug:
            continue
        slugs.add(slug)
        content_file = CONTENT_DIR / f"{slug}.md"
        new_content = stub_content(repo)

        if content_file.exists():
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

    print(f"\nSummary: {created} created, {updated} updated, "
          f"{unchanged} unchanged, {pruned} pruned")
    return 0


if __name__ == '__main__':
    sys.exit(main())
