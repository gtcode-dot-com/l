# Pilgrimage Mode Documentation

## Overview

Pilgrimage Mode is a temporary maintenance mode that replaces the entire site with a humorous "expedition dashboard" landing page. All existing URLs redirect to the homepage.

## How It Works

When `pilgrimage_mode = true` in the site configuration:

1. The homepage displays the "Great Sustenance Pilgrimage" expedition dashboard
2. All other pages (investigations, articles, news, etc.) redirect to the homepage
3. Redirects use meta refresh and JavaScript (client-side, suitable for static hosting)
4. No content is deleted - the normal site remains intact underneath

**Note:** Client-side redirects return HTTP 200 then redirect via meta/JS. This is standard for static sites (GitHub Pages, etc.) and search engines handle it correctly for temporary maintenance.

## Enabling/Disabling

Edit `config.toml`:

```toml
[params]
  # Set to true for pilgrimage mode, false for normal operation
  pilgrimage_mode = true
```

After changing the value, rebuild the site:

```bash
hugo --gc --minify
```

## Files Modified

1. **config.toml** - Added `pilgrimage_mode` parameter

2. **layouts/index.html** - Added pilgrimage mode check at top of file
   - Wraps pilgrimage partial in conditional
   - Falls back to normal homepage when mode is disabled

3. **layouts/partials/pilgrimage-homepage.html** - NEW
   - Self-contained expedition dashboard HTML/CSS
   - Includes:
     - Breaking news banner
     - Hero section with headline
     - Rotating status messages (15+ variants)
     - Expedition metrics dashboard
     - Route visualization
     - Mission timeline
     - Footer

4. **layouts/_default/baseof.html** - Added redirect logic
   - Checks pilgrimage_mode param
   - Returns redirect HTML for non-home pages when enabled

5. **layouts/investigation/baseof.html** - Added redirect logic
   - Same redirect behavior for investigation pages

6. **layouts/ou-article/baseof.html** - Added redirect logic
   - Same redirect behavior for article pages

## SEO Considerations

- All redirected pages return `noindex,follow` robots meta tag
- No existing content is deleted or modified
- Original URLs remain valid (just redirect)
- Easy to disable and restore full site instantly

## Design Features

- Dark mode by default with light mode support
- Mobile responsive
- Accessible (semantic HTML, ARIA labels, proper heading hierarchy)
- No external dependencies (all CSS inlined)
- Rotating status messages change daily
- Expedition aesthetic: mission control, NASA, field reports

## To Disable Pilgrimage Mode

1. Open `config.toml`
2. Find `pilgrimage_mode = true`
3. Change to `pilgrimage_mode = false`
4. Rebuild: `hugo --gc --minify`
5. The normal site will be fully restored
