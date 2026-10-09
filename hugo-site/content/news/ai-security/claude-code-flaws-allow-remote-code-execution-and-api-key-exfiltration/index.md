---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T06:07:52.432861+00:00'
exported_at: '2026-02-26T06:07:55.644593+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html
structured_data:
  about: []
  author: ''
  description: Claude Code flaws allow remote code execution and API key theft via
    untrusted repositories; three bugs fixed across 2025–2026 releases.
  headline: Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration
updated_at: '2026-02-26T06:07:52.432861+00:00'
url_hash: 2455f356beab65e18afdcd0fadc33be59d385018
---

**

Ravie Lakshmanan
**

Feb 25, 2026

Artificial Intelligence / Vulnerability

Cybersecurity researchers have
[disclosed](https://blog.checkpoint.com/research/check-point-researchers-expose-critical-claude-code-flaws/)
multiple security vulnerabilities in Anthropic's Claude Code, an artificial intelligence (AI)-powered coding assistant, that could result in remote code execution and theft of API credentials.

"The vulnerabilities exploit various configuration mechanisms, including Hooks, Model Context Protocol (MCP) servers, and environment variables – executing arbitrary shell commands and exfiltrating Anthropic API keys when users clone and open untrusted repositories," Check Point researchers Aviv Donenfeld and Oded Vanunu
[said](https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/)
in a report shared with The Hacker News.

The identified shortcomings fall under three broad categories -

* **[No CVE](https://github.com/anthropics/claude-code/security/advisories/GHSA-ph6w-f82w-28w6)**
  (CVSS score: 8.7) - A code injection vulnerability stemming from a user consent bypass when starting Claude Code in a new directory that could result in arbitrary code execution without additional confirmation via untrusted
  [project hooks](https://code.claude.com/docs/en/hooks-guide)
  defined in .claude/settings.json. (Fixed in version 1.0.87 in September 2025)
* **[CVE-2025-59536](https://github.com/anthropics/claude-code/security/advisories/GHSA-4fgq-fpq9-mr3g)**
  (CVSS score: 8.7) - A code injection vulnerability that allows execution of arbitrary shell commands automatically upon tool initialization when a user starts Claude Code in an untrusted directory. (Fixed in version 1.0.111 in October 2025)
* **[CVE-2026-21852](https://github.com/anthropics/claude-code/security/advisories/GHSA-jh7p-qr78-84p7)**
  (CVSS score: 5.3) - An information disclosure vulnerability in Claude Code's project-load flow that allows a malicious repository to exfiltrate data, including Anthropic API keys. (Fixed in version 2.0.65 in January 2026)

"If a user started Claude Code in an attacker-controller repository, and the repository included a settings file that set ANTHROPIC\_BASE\_URL to an attacker-controlled endpoint, Claude Code would issue API requests before showing the trust prompt, including potentially leaking the user's API keys," Anthropic said in an advisory for CVE-2026-21852.

In other words, simply opening a crafted repository is enough to exfiltrate a developer's active API key, redirect authenticated API traffic to external infrastructure, and capture credentials. This, in turn, can permit the attacker to burrow deeper into the victim's AI infrastructure.

VIDEO

This could potentially involve accessing shared project files, modifying/deleting cloud-stored data, uploading malicious content, and even generating unexpected API costs.

Successful exploitation of the first vulnerability could trigger stealthy execution on a developer's machine without any additional interaction beyond launching the project.

VIDEO

CVE-2025-59536 also achieves a similar goal, the main difference being that repository-defined configurations defined through .mcp.json and claude/settings.json file could be exploited by an attacker to override explicit user approval prior to interacting with external tools and services through the Model Context Protocol (MCP). This is achieved by setting the "
[enableAllProjectMcpServers](https://code.claude.com/docs/en/settings)
" option to true.

"As AI-powered tools gain the ability to execute commands, initialize external integrations, and initiate network communication autonomously, configuration files effectively become part of the execution layer," Check Point said. "What was once considered operational context now directly influences system behavior."

"This fundamentally alters the threat model. The risk is no longer limited to running untrusted code – it now extends to opening untrusted projects. In AI-driven development environments, the supply chain begins not only with source code, but with the automation layers surrounding it."