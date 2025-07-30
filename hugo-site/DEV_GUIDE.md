# Hugo Site Development Guide

This guide explains how to build and deploy the Hugo-based site locally and configure GitHub Pages for static hosting.

## Prerequisites

- Hugo Extended (version 0.100.0 or higher)
- Git
- GitHub repository with Pages enabled

## Local Development Setup

### 1. Install Hugo Extended

**macOS (using Homebrew):**
```bash
brew install hugo
```

**Windows (using Chocolatey):**
```bash
choco install hugo-extended
```

**Linux (using Snap):**
```bash
sudo snap install hugo --channel=extended
```

**Manual Installation:**
Download from [Hugo Releases](https://github.com/gohugoio/hugo/releases) - ensure you get the "extended" version.

### 2. Clone and Setup

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 3. Local Development Server

Start the development server:
```bash
hugo server --bind=0.0.0.0 --port=5000 --baseURL=http://localhost:5000
```

The site will be available at `http://localhost:5000`

**Development Server Features:**
- Live reload on file changes
- Draft content rendering
- Fast rebuild times

## Building for Production

### 1. Build Static Site

Generate the complete static site:
```bash
hugo --minify --gc --baseURL=https://yourdomain.com
```

**Build Options:**
- `--minify`: Minifies HTML, CSS, JS, JSON, XML, and SVG
- `--gc`: Runs garbage collection after build
- `--baseURL`: Sets the base URL for absolute links

### 2. Output Location

Hugo generates the static site in the `public/` directory by default.

**File Structure After Build:**
```
public/
├── index.html                    # Homepage (Paul Lowndes static page)
├── guides/
│   └── building-cns-2.0-developers-guide/
│       ├── index.html            # CNS Guide homepage
│       ├── chapter-1-introduction/
│       ├── chapter-2-sno-foundations/
│       └── ...
├── for-agents/
│   └── conspiracy-of-silence/
│       └── index.html            # Static agents page
├── investigation/
│   └── hawaii-justice-system-wilson-loo/
│       └── index.html            # Static investigation page
├── css/
├── js/
├── img/
└── styles/
```

## GitHub Pages Configuration

### Option 1: Deploy from Root (Recommended)

1. **Build locally:**
   ```bash
   hugo --minify --gc --baseURL=https://yourusername.github.io/your-repo-name
   ```

2. **Copy public contents to root:**
   ```bash
   cp -r public/* .
   git add .
   git commit -m "Deploy static site"
   git push origin main
   ```

3. **Configure GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `main` / `(root)`

### Option 2: Deploy from Subdirectory

If you prefer to keep Hugo source separate:

1. **Create deployment structure:**
   ```bash
   mkdir -p hugo-site/static
   hugo --minify --gc --destination=hugo-site/static --baseURL=https://yourusername.github.io/your-repo-name
   ```

2. **Configure GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: "Deploy from a branch"
   - Branch: `main` / `/hugo-site/static`

3. **Deploy:**
   ```bash
   git add hugo-site/static
   git commit -m "Deploy to hugo-site/static"
   git push origin main
   ```

## Site Architecture

### Static Pages (No Hugo Processing)
- `/` - Paul Lowndes homepage
- `/for-agents/conspiracy-of-silence/` - Agents directive page
- `/investigation/hawaii-justice-system-wilson-loo/` - Investigation report

### Hugo-Generated Pages
- `/guides/building-cns-2.0-developers-guide/` - CNS educational content
- All chapter pages under `/guides/building-cns-2.0-developers-guide/chapter-*/`

## Configuration Files

### config.yaml
Key settings for production:
```yaml
baseURL: 'https://yourdomain.com'
languageCode: 'en-us'
title: 'Building CNS 2.0: A Developer\'s Guide'

staticDir: 'static'
disableKinds: ['home', 'taxonomy', 'term']

publishDir: 'public'
```

### Content Organization
```
content/
└── guides/
    └── building-cns-2.0-developers-guide/
        ├── _index.md              # Guide homepage
        ├── chapter-1-introduction/
        ├── chapter-2-sno-foundations/
        └── ...

static/
├── index.html                     # Static homepage
├── for-agents/conspiracy-of-silence/index.html
├── investigation/hawaii-justice-system-wilson-loo/index.html
├── css/
├── js/
└── img/
```

## Deployment Workflow

### 1. Development Cycle
```bash
# 1. Make changes to content or layouts
# 2. Test locally
hugo server

# 3. Build for production
hugo --minify --gc --baseURL=https://yourdomain.com

# 4. Deploy
git add .
git commit -m "Update site content"
git push origin main
```

### 2. Content Updates

**Static Pages:** Edit files directly in `static/` directory
**Hugo Pages:** Edit markdown files in `content/` directory
**Styling:** Modify `static/css/style.css`
**Layouts:** Update files in `layouts/` directory

## Troubleshooting

### Common Issues

1. **CSS/JS not loading:**
   - Ensure `baseURL` matches your domain
   - Check that assets use absolute paths (`/css/style.css`)

2. **Static pages not serving:**
   - Verify files exist in `static/` directory
   - Check Hugo isn't generating conflicting content

3. **GitHub Pages not updating:**
   - Check repository Settings → Pages configuration
   - Ensure branch and directory are correct
   - Allow 5-10 minutes for changes to propagate

### Verification

After deployment, verify:
- [ ] Homepage loads Paul Lowndes content
- [ ] CNS guide accessible at `/guides/building-cns-2.0-developers-guide/`
- [ ] All chapter pages load with proper styling
- [ ] Static investigation page loads at correct URL
- [ ] Navigation links work between all sections

## Performance Optimization

Hugo's built-in optimizations:
- Minification with `--minify`
- Asset bundling and fingerprinting
- Garbage collection with `--gc`
- Static file serving

Additional optimizations:
- Images are served from `static/img/`
- CSS is minified and cached
- JavaScript is minimal and optimized

## Domain Configuration

For custom domains:
1. Add `CNAME` file to `static/` directory containing your domain
2. Configure DNS with your domain provider
3. Update `baseURL` in `config.yaml`
4. Rebuild and deploy

Example `static/CNAME`:
```
yourdomain.com
```

This guide ensures you can develop locally and deploy to GitHub Pages with full control over the static build process.