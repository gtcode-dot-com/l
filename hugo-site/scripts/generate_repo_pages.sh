#!/bin/bash
# Generate minimal Hugo content stubs for all repositories from data/repos.yaml
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HUGO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$HUGO_ROOT"

echo "Generating repo content stubs from data/repos.yaml..."
python3 scripts/generate_repo_pages.py "$@"
