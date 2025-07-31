#!/usr/bin/env bash

#===============================================================================
# Hugo Docs Importer v2.0
#
# A script to fetch markdown documentation from specified GitHub repositories
# and organize them into a Hugo website structure. It intelligently creates
# directories and _index.md files only for paths that contain markdown files,
# ensuring a clean and efficient content structure.
#===============================================================================

# --- Robust Scripting Settings ---
set -o errexit
set -o nounset
set -o pipefail

# --- Configuration ---

# The absolute path to the root of your Hugo website repository.
HUGO_SITE_ROOT="./hugo-site"

# The path within your Hugo site where the repository content will be placed.
HUGO_CONTENT_PATH="content/repos"

# An array of repositories to process.
# Format: "owner/repo" or "owner/repo@branch"
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
NO_DELETE_MODE=false

# --- Script Globals ---
TEMP_DIR=""
FULL_CONTENT_PATH=""

# --- Script Logic ---

_msg() {
  echo -e "$@"
}

_error() {
  echo -e "\033[0;31mError: $1\033[0m" >&2
  exit 1
}

_generate_title() {
  local input_name="$1"
  local title
  title="${input_name//-/ }"
  title="${title//_/ }"
  title="$(tr '[:lower:]' '[:upper:]' <<< "${title:0:1}")${title:1}"
  echo "$title"
}

_cleanup() {
  if [[ -n "${TEMP_DIR-}" && -d "$TEMP_DIR" ]]; then
    rm -rf "$TEMP_DIR"
    _msg "\n🧹 Cleaned up temporary directory."
  fi
}

trap _cleanup EXIT SIGHUP SIGINT SIGTERM

# --- Repository Processing Function ---

_process_repo() {
  local repo_string="$1"

  # Parse repository and branch details
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
  git clone --depth 1 --branch "$branch" "https://github.com/${repo_owner_name}.git" "$temp_repo_clone_path"

  _msg "🔍 Searching for markdown files..."
  local markdown_files
  mapfile -t markdown_files < <(find "$temp_repo_clone_path" -type f \( -name "*.md" -o -name "*.markdown" \) -not -path "*/.git/*" | sort | head -n "$MAX_FILES_PER_REPO")

  local file_count=${#markdown_files[@]}
  if [[ $file_count -eq 0 ]]; then
    _msg "🟡 No markdown files found in this repository."
    # Clean up the empty repo directory we created
    rmdir "$target_repo_path"
    return 0
  fi

  _msg "✅ Found ${file_count} files. Copying and creating indexes as needed..."

  # Associative array to track which directories have had an index created.
  # This prevents redundant work.
  declare -A created_indexes

  # --- [REVISED] Create _index.md for the repo root first ---
  local repo_title
  repo_title=$(_generate_title "$repo_name")
  (
    echo "---"
    echo "title: \"${repo_title}\""
    echo "description: \"Browse the contents of the ${repo_title} repository.\""
    echo "---"
  ) > "${target_repo_path}/_index.md"
  created_indexes["$target_repo_path"]=1


  local file_weight_counter=0
  for file_path in "${markdown_files[@]}"; do
    ((file_weight_counter++))

    local relative_path
    relative_path=${file_path#${temp_repo_clone_path}/}
    local dest_path="${target_repo_path}/${relative_path}"
    local dest_dir
    dest_dir=$(dirname "$dest_path")

    # Create the destination directory for the markdown file
    mkdir -p "$dest_dir"

    # --- [REVISED] Intelligent Index Creation ---
    # Walk up the directory tree from the file's location to the repo root,
    # creating _index.md files for any directory that doesn't have one yet.
    local current_check_dir="$dest_dir"
    while [[ "$current_check_dir" > "$target_repo_path" ]]; do
      if [[ -z "${created_indexes[$current_check_dir]-}" ]]; then
        local dir_name
        dir_name=$(basename "$current_check_dir")
        local dir_title
        dir_title=$(_generate_title "$dir_name")
        (
          echo "---"
          echo "title: \"${dir_title}\""
          echo "description: \"Contents of the ${dir_title} directory.\""
          echo "---"
        ) > "${current_check_dir}/_index.md"
        created_indexes["$current_check_dir"]=1
      fi
      current_check_dir=$(dirname "$current_check_dir")
    done
    # --- End of revised logic ---

    # --- Generate Front Matter and copy file ---
    local filename
    filename=$(basename "$file_path")
    local filename_no_ext="${filename%.*}"

    local title
    title=$(_generate_title "$filename_no_ext")
    local description="Documentation for ${filename_no_ext} from the ${repo_title} repository."

    local lastmod
    lastmod=$(cd "$temp_repo_clone_path" && git log -1 --pretty="format:%cs" -- "$relative_path" || date +%Y-%m-%d)

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

    mv "$temp_file" "$dest_path"
  done
}

# --- Main Script Execution ---

_main() {
  _msg "\n\033[1;34mStarting Hugo Documentation Importer v2.0\033[0m"

  # Validate configuration
  if [[ ! -d "$HUGO_SITE_ROOT" ]]; then
    _error "HUGO_SITE_ROOT directory does not exist. Please check the path."
  fi

  if [[ ${#REPOS_TO_PROCESS[@]} -eq 0 ]]; then
    _error "The REPOS_TO_PROCESS array is empty. Please add repositories to process."
  fi

  FULL_CONTENT_PATH="${HUGO_SITE_ROOT}/${HUGO_CONTENT_PATH}"
  mkdir -p "$FULL_CONTENT_PATH"

  # --- [NEW] Create a single top-level _index.md for the /repos/ section ---
  if [ ! -f "${FULL_CONTENT_PATH}/_index.md" ]; then
    _msg "📝 Creating top-level index for the '${HUGO_CONTENT_PATH}' section..."
    local section_title
    section_title=$(_generate_title "$(basename "$HUGO_CONTENT_PATH")")
    (
      echo "---"
      echo "title: \"${section_title}\""
      echo "description: \"A collection of documentation from various code repositories.\""
      echo "---"
    ) > "${FULL_CONTENT_PATH}/_index.md"
  fi

  TEMP_DIR=$(mktemp -d)
  _msg "📁 Created temporary directory at: $TEMP_DIR"

  for repo_string in "${REPOS_TO_PROCESS[@]}"; do
    _process_repo "$repo_string" || _msg "\033[0;33m⚠️  Skipped repository '${repo_string}' due to an error. Please check the repo name, branch, and permissions.\033[0m"
  done

  _msg "\n\033[1;32m🎉 Documentation import process completed!\033[0m"
}

# Run the main function
_main
