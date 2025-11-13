---
title: "Robots.txt - Web Crawler Policy"
description: "Robots.txt configuration for web crawlers and search engines"
date: 2025-11-12
version: "1.0"
type: "policies"
outputs: ["HTML", "plaintextrobots"]
---

# Robots.txt Configuration

This file controls how web crawlers and search engines access GTCode.com.

## General Access

```
User-agent: *
Allow: /
```

All crawlers are welcome to access all content on this site.

## AI Crawler Specific Rules

We explicitly allow and welcome AI crawlers:

- **GPTBot** (OpenAI)
- **ChatGPT-User** (OpenAI)
- **CCBot** (Common Crawl)
- **anthropic-ai** (Anthropic)
- **Claude-Web** (Anthropic)

All AI crawlers have full access to the site.

## Sitemaps

Primary sitemaps for discovery:
- Main sitemap: https://gtcode.com/sitemap.xml
- News sitemap: https://gtcode.com/news-sitemap.xml

## Crawl Behavior

**Crawl-delay:** 1 second

We request a 1-second delay between requests to ensure site performance for all visitors.

---

For AI-specific access policies, see:
- `/agent.txt` - AI agent guidelines
- `/llm.txt` - LLM usage policy
- `/ai.txt` - AI ethics guidelines
