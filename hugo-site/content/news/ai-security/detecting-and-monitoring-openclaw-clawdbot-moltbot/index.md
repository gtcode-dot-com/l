---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-03T14:15:14.744439+00:00'
exported_at: '2026-02-03T14:15:16.993106+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32678
structured_data:
  about: []
  author: ''
  description: 'Detecting and Monitoring OpenClaw (clawdbot, moltbot), Author: Johannes
    Ullrich'
  headline: Detecting and Monitoring OpenClaw (clawdbot, moltbot), (Tue, Feb 3rd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32678
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Detecting and Monitoring OpenClaw (clawdbot, moltbot), (Tue, Feb 3rd)
updated_at: '2026-02-03T14:15:14.744439+00:00'
url_hash: c0a923bf45a50e8a009686312865bacf89d36227
---

Last week, a new AI agent framework was introduced to automate "live". It targets office work in particular, focusing on messaging and interacting with systems. The tool has gone viral not so much because of its features, which are similar to those of other agent frameworks, but because of a stream of security oversights in its design.

If you are looking to detect the use of OpenClaw in your environment, Knostic has created scripts to detect It, and, if you do want to use OpenClaw, to collect telemetry about its use.

This script searches the system for filenames commonly associated with OpenClaw. For example, the presence of the state directory ~/.openclaw or for a Docker container running openclaw. If you have decent endpoint monitoring, this tool may not be needed, but it can give you some hints on which files to look for.

If you do run OpenClaw, openclaw-detect will add additional meaningful logging. The tool captures "every tool call, LLM request, and agent session — with built-in redaction, tamper-proof hash chains, syslog/SIEM forwarding, and rate limiting". It is an OpenClaw plugin and installs like any other OpenClaw plugin

In addition, there are a few additional security tools and tips:

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|