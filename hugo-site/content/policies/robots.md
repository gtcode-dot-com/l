---
title: "Robots.txt - Web Crawler Policy"
description: "Robots.txt configuration for web crawlers and search engines"
date: 2025-11-12
version: "1.0"
type: "policies"
outputs: ["HTML", "Markdown", "plaintextrobots"]
---

User-agent: *
Allow: /
Allow: /agent.txt
Allow: /agents.txt
Allow: /llm.txt
Allow: /llms.txt
Allow: /ai.txt
Allow: /humans.txt

User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: CCBot
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: Claude-Web
Allow: /

Sitemap: https://gtcode.com/sitemap.xml
Sitemap: https://gtcode.com/news-sitemap.xml

Crawl-delay: 1
