#!/usr/bin/env bash

#===============================================================================
# Hugo Docs Importer
#
# A script to fetch markdown documentation from specified GitHub repositories
# and organize them into a Hugo website structure.
#
#===============================================================================

# --- Robust Scripting Settings ---
# Exit immediately if a command exits with a non-zero status.
set -o errexit
# Treat unset variables as an error when substituting.
set -o nounset
# Pipelines return the exit status of the last command to exit with a non-zero
# status, or zero if no command exited with a non-zero status.
set -o pipefail

# --- Configuration ---

# The absolute path to the root of your Hugo website repository.
# Example: HUGO_SITE_ROOT="/Users/your-user/projects/my-hugo-site"
HUGO_SITE_ROOT="./hugo-site"

# The path within your Hugo site where the content pages should be placed.
# This is typically 'content/docs' or similar.
# The script will create subdirectories for each repository here.
HUGO_CONTENT_PATH="content/repos"

# An array of repositories to process.
# Format: "owner/repo" or "owner/repo@branch"
# If no branch is specified, 'main' is used as the default.
REPOS_TO_PROCESS=(
  "nshkrdotcom/ds_ex"
  "nshkrdotcom/pipeline_ex"
  "nshkrdotcom/json_remedy"
  "nshkrdotcom/foundation"
  "nshkrdotcom/dspex"
)

# A safety limit on the number of markdown files to process per repository.
# This prevents issues with repositories containing a very large number of markdown files.
MAX_FILES_PER_REPO=1000

# Set to "true" to prevent the script from deleting existing content in the target directory.
# If "false", the script will remove and replace the content for each processed repo.
NO_DELETE_MODE=false

# --- Script Logic ---

# Function to display colored messages
_msg() {
  echo -e "$@"
}

# Function to display error messages and exit
_error() {
  echo -e "\033[0;31mError: $1\033[0m" >&2
  exit 1
}

# Function for cleaning up the temporary directory on exit
_cleanup() {
  if [[ -n "${TEMP_DIR-}" && -d "$TEMP_DIR" ]]; then
    rm -rf "$TEMP_DIR"
    _msg "\n🧹 Cleaned up temporary directory."
  fi
}

# Trap signals to ensure cleanup runs
trap _cleanup EXIT SIGHUP SIGINT SIGTERM

# --- Main Script ---

_main() {
  _msg "\n\033[1;34mStarting Hugo Documentation Importer\033[0m"

  # Validate configuration
  if [[ "$HUGO_SITE_ROOT" == "/path/to/your/hugo/site" || ! -d "$HUGO_SITE_ROOT" ]]; then
    _error "HUGO_SITE_ROOT is not configured or does not exist. Please edit the script."
  fi

  if [[ ${#REPOS_TO_PROCESS[@]} -eq 0 ]]; then
    _error "The REPOS_TO_PROCESS array is empty. Please add repositories to process."
  fi

  local full_content_path="${HUGO_SITE_ROOT}/${HUGO_CONTENT_PATH}"
  mkdir -p "$full_content_path"

  # Create a secure temporary directory for cloning repositories
  TEMP_DIR=$(mktemp -d)
  _msg "📁 Created temporary directory at: $TEMP_DIR"

  for repo_string in "${REPOS_TO_PROCESS[@]}"; do
    # Parse repository and branch from the configuration string
    local repo_owner_name
    repo_owner_name=$(echo "$repo_string" | cut -d'@' -f1)
    local repo_name
    repo_name=$(basename "$repo_owner_name")
    local branch
    branch=$(echo "$repo_string" | awk -F'@' '{if (NF>1) print $2; else print "main"}')

    local target_repo_path="${full_content_path}/${repo_name}"

    _msg "\n\033[1;36mProcessing repository: ${repo_owner_name} (branch: ${branch})\033[0m"

    # Handle the no-delete option
    if [[ "$NO_DELETE_MODE" == "false" && -d "$target_repo_path" ]]; then
      _msg "🔥 Deleting existing content at ${target_repo_path}"
      rm -rf "$target_repo_path"
    fi
    mkdir -p "$target_repo_path"

    # Clone the specific branch of the repository into the temporary directory
    _msg "📥 Cloning repository..."
    git clone --depth 1 --branch "$branch" "https://github.com/${repo_owner_name}.git" "${TEMP_DIR}/${repo_name}"

    # Find markdown files, excluding certain paths like .git
    _msg "🔍 Searching for markdown files..."
    local markdown_files
    mapfile -t markdown_files < <(find "${TEMP_DIR}/${repo_name}" -type f -name "*.md" -not -path "*/.git/*" | head -n "$MAX_FILES_PER_REPO")

    local file_count=${#markdown_files[@]}
    if [[ $file_count -eq 0 ]]; then
      _msg "🟡 No markdown files found in this repository."
      continue
    fi

    _msg "✅ Found ${file_count} markdown files. Copying to Hugo site..."

    for file_path in "${markdown_files[@]}"; do
      local relative_path
      relative_path=${file_path#${TEMP_DIR}/${repo_name}/}
      local dest_path="${target_repo_path}/${relative_path}"

      mkdir -p "$(dirname "$dest_path")"
      cp "$file_path" "$dest_path"
    done
  done

  _msg "\n\033[1;32m🎉 Documentation import process completed successfully!\033[0m"
}

# Run the main function
_main
