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
MAX_FILES_PER_REPO=1000

# Set to "true" to prevent the script from deleting existing content.
# If "false", the script will remove and replace the content for each repo.
NO_DELETE_MODE=false

# --- Script Globals ---
# These are set in _main()
TEMP_DIR=""
FULL_CONTENT_PATH=""

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

trap _cleanup EXIT SIGHUP SIGINT SIGTERM


# --- Repository Processing Function ---
# This function handles the logic for a single repository.
# It's designed to be called from the main loop. `set -e` will cause it to
# exit on failure, which the main loop will catch.
#
_process_repo() {
  local repo_string="$1"

  # Parse repository and branch from the configuration string
  local repo_owner_name
  repo_owner_name=$(echo "$repo_string" | cut -d'@' -f1)
  local repo_name
  repo_name=$(basename "$repo_owner_name")
  local branch
  branch=$(echo "$repo_string" | awk -F'@' '{if (NF>1) print $2; else print "main"}')
  local target_repo_path="${FULL_CONTENT_PATH}/${repo_name}"
  local temp_repo_clone_path="${TEMP_DIR}/${repo_name}"

  _msg "\n\033[1;36mProcessing repository: ${repo_owner_name} (branch: ${branch})\033[0m"

  if [[ "$NO_DELETE_MODE" == "false" && -d "$target_repo_path" ]]; then
    _msg "🔥 Deleting existing content at ${target_repo_path}"
    rm -rf "$target_repo_path"
  fi
  mkdir -p "$target_repo_path"

  _msg "📥 Cloning repository..."
  # The entire script will no longer exit here if the clone fails.
  git clone --depth 1 --branch "$branch" "https://github.com/${repo_owner_name}.git" "$temp_repo_clone_path"

  _msg "🔍 Searching for markdown files..."
  local markdown_files
  # Sort files for predictable weighting
  mapfile -t markdown_files < <(find "$temp_repo_clone_path" -type f -name "*.md" -not -path "*/.git/*" | sort | head -n "$MAX_FILES_PER_REPO")

  local file_count=${#markdown_files[@]}
  if [[ $file_count -eq 0 ]]; then
    _msg "🟡 No markdown files found in this repository."
    return 0 # Success, nothing to do
  fi

  _msg "✅ Found ${file_count} files. Prepending front matter and copying to Hugo site..."

  local file_weight_counter=0
  for file_path in "${markdown_files[@]}"; do
    ((file_weight_counter++))

    local relative_path
    relative_path=${file_path#${temp_repo_clone_path}/}
    local dest_path="${target_repo_path}/${relative_path}"
    mkdir -p "$(dirname "$dest_path")"

    # --- Generate Front Matter ---
    local filename
    filename=$(basename "$file_path")
    local filename_no_ext
    filename_no_ext="${filename%.md}"

    local title
    title="${filename_no_ext//-/ }"
    title="${title//_/ }"
    title="$(tr '[:lower:]' '[:upper:]' <<< "${title:0:1}")${title:1}"

    local description="$title"

    local lastmod
    lastmod=$(cd "$temp_repo_clone_path" && git log -1 --pretty="format:%cs" -- "$relative_path" || date +%Y-%m-%d)

    # Use a temporary file to build the new content to avoid race conditions
    local temp_file
    temp_file=$(mktemp)
    (
      echo "---"
      echo "title: \"${title}\""
      echo "description: \"${description}\""
      echo "weight: ${file_weight_counter}"
      echo "lastmod: \"${lastmod}\""
      echo "sitemap:"
      echo "  changefreq: monthly"
      echo "  priority: 0.5"
      echo "  filename: sitemap.xml"
      echo "---"
      echo ""
      cat "$file_path"
    ) > "$temp_file"
    
    # Move the completed file into place
    mv "$temp_file" "$dest_path"
  done
}


# --- Main Script Execution ---

_main() {
  _msg "\n\033[1;34mStarting Hugo Documentation Importer\033[0m"

  # Validate configuration
  if [[ "$HUGO_SITE_ROOT" == "/path/to/your/hugo/site" || ! -d "$HUGO_SITE_ROOT" ]]; then
    _error "HUGO_SITE_ROOT is not configured or does not exist. Please edit the script."
  fi

  if [[ ${#REPOS_TO_PROCESS[@]} -eq 0 ]]; then
    _error "The REPOS_TO_PROCESS array is empty. Please add repositories to process."
  fi

  FULL_CONTENT_PATH="${HUGO_SITE_ROOT}/${HUGO_CONTENT_PATH}"
  mkdir -p "$FULL_CONTENT_PATH"

  TEMP_DIR=$(mktemp -d)
  _msg "📁 Created temporary directory at: $TEMP_DIR"

  for repo_string in "${REPOS_TO_PROCESS[@]}"; do
    # Call the processing function for each repo.
    # If the function fails (returns non-zero), catch the error, print a
    # warning, and continue to the next iteration of the loop.
    _process_repo "$repo_string" || _msg "\033[0;33m⚠️  Skipped repository '${repo_string}' due to an error. Please check the repo name, branch, and permissions.\033[0m"
  done

  _msg "\n\033[1;32m🎉 Documentation import process completed!\033[0m"
}

# Run the main function
_main
