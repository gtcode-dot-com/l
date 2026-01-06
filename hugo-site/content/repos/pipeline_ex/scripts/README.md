---
title: "README"
description: "Documentation for README from the Pipeline ex repository."
weight: 172
lastmod: "2025-07-19"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

# CI Scripts

## credo_ci.sh

This script runs Credo for CI/CD pipelines while excluding refactoring opportunities.

### Purpose

- **Local Development**: `mix credo --strict` shows all issues including refactoring opportunities
- **CI/CD**: `./scripts/credo_ci.sh` only fails on critical issues (Software Design & Code Readability)

### What it checks

✅ **Software Design issues** - Critical architectural problems  
✅ **Code Readability issues** - Code style and readability violations  
❌ **Refactoring Opportunities** - Suggestions shown locally but don't fail CI

### Usage

```bash
# Local development (shows all issues)
mix credo --strict

# CI/CD (excludes refactoring opportunities) 
./scripts/credo_ci.sh
```

This approach ensures that:
1. Developers see helpful refactoring suggestions during development
2. CI doesn't fail on complex functions that are intentionally complex (like test mocks)
3. Critical code quality issues still block deployment