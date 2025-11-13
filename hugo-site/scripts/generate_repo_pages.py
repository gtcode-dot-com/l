#!/usr/bin/env python3
"""
Generate Hugo content pages for repositories from data/repos.yaml

Usage:
    python generate_repo_pages.py [--overwrite] [--skip-existing]

Options:
    --overwrite      Overwrite all existing repo pages
    --skip-existing  Skip repos that already have content pages (default)
    --force         Force overwrite without prompting
"""

import os
import sys
import yaml
import argparse
from pathlib import Path
from datetime import datetime

# Paths
SCRIPT_DIR = Path(__file__).parent
HUGO_ROOT = SCRIPT_DIR.parent
DATA_FILE = HUGO_ROOT / "data" / "repos.yaml"
CONTENT_DIR = HUGO_ROOT / "content" / "repos"


def load_repos():
    """Load repository data from YAML file"""
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def create_repo_content(repo, overwrite=False):
    """Create a Hugo content file for a repository"""
    slug = repo.get('slug', '')
    content_file = CONTENT_DIR / f"{slug}.md"

    # Check if file exists
    if content_file.exists() and not overwrite:
        return 'skipped'

    # Prepare front matter
    front_matter = {
        'title': repo.get('name', slug),
        'description': repo.get('summary', ''),
        'date': datetime.now().strftime('%Y-%m-%d'),
        'slug': slug,
        'stage': repo.get('stage', 'Active'),
        'version': repo.get('version', '0.0.0'),
        'highlights': repo.get('highlights', []),
        'tags': repo.get('tags', []),
        'hex_url': repo.get('hex_url', ''),
        'docs_url': repo.get('docs_url', ''),
        'repo_url': repo.get('repo_url', ''),
    }

    # Generate content file
    content = "---\n"
    content += yaml.dump(front_matter, default_flow_style=False, allow_unicode=True)
    content += "---\n\n"
    content += f"## About {repo.get('name', slug)}\n\n"
    content += f"{repo.get('summary', '')}\n\n"

    if repo.get('highlights'):
        content += "## Package Information\n\n"
        for highlight in repo.get('highlights'):
            content += f"- {highlight}\n"
        content += "\n"

    content += "## Installation\n\n"
    content += f"Add `{slug}` to your list of dependencies in `mix.exs`:\n\n"
    content += "```elixir\n"
    content += "def deps do\n"
    content += "  [\n"
    content += f"    {{{slug!r}, \"~> {repo.get('version', '0.0.0')}\"}}\\n"
    content += "  ]\n"
    content += "end\n"
    content += "```\n\n"
    content += "Then run:\n\n"
    content += "```bash\n"
    content += "mix deps.get\n"
    content += "```\n\n"
    content += "## Documentation\n\n"

    if repo.get('docs_url'):
        content += f"Full documentation is available at [{repo.get('docs_url')}]({repo.get('docs_url')}).\n\n"

    if repo.get('repo_url'):
        content += f"## Source Code\n\n"
        content += f"The source code is available on GitHub: [{repo.get('repo_url')}]({repo.get('repo_url')}).\n\n"

    # Write file
    content_file.parent.mkdir(parents=True, exist_ok=True)
    with open(content_file, 'w', encoding='utf-8') as f:
        f.write(content)

    return 'created' if not content_file.exists() else 'updated'


def main():
    parser = argparse.ArgumentParser(
        description='Generate Hugo content pages for repositories from data/repos.yaml'
    )
    parser.add_argument(
        '--overwrite',
        action='store_true',
        help='Overwrite all existing repo pages'
    )
    parser.add_argument(
        '--skip-existing',
        action='store_true',
        default=True,
        help='Skip repos that already have content pages (default)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force overwrite without prompting'
    )

    args = parser.parse_args()

    # Load repos
    print(f"Loading repositories from {DATA_FILE}...")
    repos = load_repos()

    if not repos:
        print("No repositories found in data file.")
        return 1

    print(f"Found {len(repos)} repositories.")

    # Confirm overwrite if requested
    if args.overwrite and not args.force:
        response = input(f"\nThis will overwrite existing repo pages. Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Aborted.")
            return 0

    # Process each repo
    stats = {'created': 0, 'updated': 0, 'skipped': 0}

    print(f"\nProcessing repositories...")
    print("-" * 60)

    for repo in repos:
        slug = repo.get('slug', 'unknown')
        status = create_repo_content(repo, overwrite=args.overwrite)
        stats[status] = stats.get(status, 0) + 1

        status_icon = {
            'created': '✓',
            'updated': '↻',
            'skipped': '○'
        }.get(status, '?')

        print(f"{status_icon} {slug:<30} {status}")

    # Summary
    print("-" * 60)
    print(f"\nSummary:")
    print(f"  Created:  {stats['created']}")
    print(f"  Updated:  {stats['updated']}")
    print(f"  Skipped:  {stats['skipped']}")
    print(f"  Total:    {len(repos)}")

    return 0


if __name__ == '__main__':
    sys.exit(main())
