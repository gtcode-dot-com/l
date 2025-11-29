#!/bin/bash
# Generate Hugo content pages for all repositories

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HUGO_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$HUGO_ROOT"

echo "==================================="
echo "Repo Pages Generator"
echo "==================================="
echo ""
echo "This script generates Hugo content pages from data/repos.yaml"
echo ""

PS3='Select an option: '
options=(
    "Generate new pages only (skip existing)"
    "Regenerate all pages (overwrite)"
    "Exit"
)

select opt in "${options[@]}"
do
    case $opt in
        "Generate new pages only (skip existing)")
            echo ""
            echo "Generating new repo pages..."
            python3 scripts/generate_repo_pages.py --skip-existing
            break
            ;;
        "Regenerate all pages (overwrite)")
            echo ""
            echo "Regenerating all repo pages..."
            python3 scripts/generate_repo_pages.py --overwrite
            break
            ;;
        "Exit")
            echo "Exiting."
            exit 0
            ;;
        *) echo "Invalid option $REPLY";;
    esac
done

echo ""
echo "Done! You can now:"
echo "  1. Run 'hugo server' to preview the site"
echo "  2. Visit http://localhost:1313/repos/{repo-slug}/ to view individual repo pages"
