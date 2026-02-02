---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T18:15:14.318201+00:00'
exported_at: '2026-02-02T18:15:16.572804+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html
structured_data:
  about: []
  author: ''
  description: A high-severity OpenClaw flaw allows one-click remote code execution
    via token theft and WebSocket hijacking; patched in v2026.1.29.
  headline: OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link
updated_at: '2026-02-02T18:15:14.318201+00:00'
url_hash: c486437de41e15f62523c21a636af1b7c2ce2ede
---

**

Ravie Lakshmanan
**

Feb 02, 2026

Vulnerability / Artificial Intelligence

A high-severity security flaw has been disclosed in
[OpenClaw](https://github.com/openclaw/openclaw)
(formerly referred to as Clawdbot and Moltbot) that could allow remote code execution (RCE) through a crafted malicious link.

The issue, which is tracked as
**[CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253)**
(CVSS score: 8.8), has been addressed in
[version 2026.1.29](https://github.com/openclaw/openclaw/releases/tag/v2026.1.29)
released on January 30, 2026. It has been described as a token exfiltration vulnerability that leads to full gateway compromise.

"The Control UI trusts gatewayUrl from the query string without validation and auto-connects on load, sending the stored gateway token in the WebSocket connect payload," OpenClaw's creator and maintainer Peter Steinberger
[said](https://github.com/openclaw/openclaw/security/advisories/GHSA-g8p2-7wf7-98mq)
in an advisory.

"Clicking a crafted link or visiting a malicious site can send the token to an attacker-controlled server. The attacker can then connect to the victim's local gateway, modify config (sandbox, tool policies), and invoke privileged actions, achieving 1-click RCE."

OpenClaw is an open-source autonomous artificial intelligence (AI) personal assistant that runs locally on user devices and integrates with a wide range of messaging platforms. Although initially released in November 2025, the project has gained rapid popularity in recent weeks, with its GitHub repository crossing 149,000 stars as of writing.

"OpenClaw is an open agent platform that runs on your machine and works from the chat apps you already use," Steinberger
[said](https://openclaw.ai/blog/introducing-openclaw)
. "Unlike SaaS assistants where your data lives on someone else's servers, OpenClaw runs where you choose – laptop, homelab, or VPS. Your infrastructure. Your keys. Your data."

Mav Levin, founding security researcher at depthfirst who is credited with discovering the shortcoming,
[said](https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys)
it can be exploited to create a one-click RCE exploit chain that takes only milliseconds after a victim visits a single malicious web page.

The problem is that clicking on the link to that web page is enough to trigger a cross-site WebSocket hijacking attack because OpenClaw's server doesn't validate the WebSocket origin header. This causes the server to accept requests from any website, effectively getting around localhost network restrictions.

A malicious web page can take advantage of the issue to execute client-side JavaScript on the victim's browser that can retrieve an authentication token, establish a WebSocket connection to the server, and use the stolen token to bypass authentication and log in to the victim's OpenClaw instance.

To make matters worse, by leveraging the token's privileged operator.admin and operator.approvals scopes, the attacker can use the API to disable user confirmation by setting "exec.approvals.set" to "off" and escape the container used to run shell tools by setting "tools.exec.host" to "gateway."

"This forces the agent to run commands directly on the host machine, not inside a Docker container," Levin said. "Finally, to achieve arbitrary command execution, the attacker JavaScript executes a node.invoke request."

When asked whether OpenClaw's use of the API to manage the safety features constitutes an architectural limitation, Levin told The Hacker News in an emailed response that, "I would say the problem is those defenses (sandbox and safety guardrails) were designed to contain malicious actions of an LLM, as a result of prompt injection, for example. And users might think these defenses would protect from this vulnerability (or limit the blast radius), but they don't."

Steinberger noted in the advisory that "the vulnerability is exploitable even on instances configured to listen on loopback only, since the victim's browser initiates the outbound connection."

"It impacts any Moltbot deployment where a user has authenticated to the Control UI. The attacker gains operator-level access to the gateway API, enabling arbitrary config changes and code execution on the gateway host. The attack works even when the gateway binds to loopback because the victim's browser acts as the bridge."