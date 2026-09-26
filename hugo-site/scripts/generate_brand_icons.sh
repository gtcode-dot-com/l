#!/usr/bin/env bash
# Regenerate the six raster/ICO brand assets and their manifest versions.
# Usage: bash hugo-site/scripts/generate_brand_icons.sh
# Requires librsvg (rsvg-convert), ImageMagick (convert), and Node.js.
set -euo pipefail

site_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
static_dir="$site_dir/static"
for tool in rsvg-convert convert node; do
  command -v "$tool" >/dev/null || { printf 'Missing required tool: %s\n' "$tool" >&2; exit 1; }
done

icon_tmp="$(mktemp -d)"
trap 'rm -f -- "$icon_tmp/badge.png" "$icon_tmp/favicon-48x48.png"; rmdir -- "$icon_tmp"' EXIT

# Use the journalism background for opaque installed-app tiles.
app_background="$(node -e '
  const fs = require("fs");
  const css = fs.readFileSync(process.argv[1], "utf8");
  const color = css.match(/--theme-bg:\s*(#[0-9a-f]{6})/i);
  if (!color) throw new Error("Missing journalism background token");
  process.stdout.write(color[1]);
' "$site_dir/assets/css/oahu-underground.css")"

rsvg-convert --width 1024 --height 1024 "$static_dir/img/gtcode-badge.svg" --output "$icon_tmp/badge.png"

for size in 16 32; do
  convert "$icon_tmp/badge.png" -filter Lanczos -resize "${size}x${size}" \
    -strip -define png:exclude-chunks=date,time "PNG32:$static_dir/favicon-${size}x${size}.png"
done
convert "$icon_tmp/badge.png" -filter Lanczos -resize 48x48 -strip "PNG32:$icon_tmp/favicon-48x48.png"
convert "$static_dir/favicon-16x16.png" "$static_dir/favicon-32x32.png" \
  "$icon_tmp/favicon-48x48.png" "$static_dir/favicon.ico"

for size in 180 192 512; do
  if [ "$size" = 180 ]; then
    output="$static_dir/apple-touch-icon.png"
  else
    output="$static_dir/android-chrome-${size}x${size}.png"
  fi
  inset_size=$((size * 4 / 5))
  convert "$icon_tmp/badge.png" -filter Lanczos -resize "${inset_size}x${inset_size}" \
    -background "$app_background" -alpha remove -alpha off -gravity center \
    -extent "${size}x${size}" -strip -define png:exclude-chunks=date,time "PNG24:$output"
done

node - "$static_dir" "$app_background" <<'JS'
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const [staticDir, background] = process.argv.slice(2);
const manifestPath = path.join(staticDir, 'site.webmanifest');
const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
for (const icon of manifest.icons) {
  const pathname = icon.src.split('?')[0];
  const data = fs.readFileSync(path.join(staticDir, pathname));
  const hash = crypto.createHash('sha256').update(data).digest('hex').slice(0, 12);
  icon.src = `${pathname}?v=${hash}`;
}
manifest.theme_color = background;
manifest.background_color = background;
fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2) + '\n');
JS

printf 'Regenerated six icons from gtcode-badge.svg and refreshed the manifest.\n'
