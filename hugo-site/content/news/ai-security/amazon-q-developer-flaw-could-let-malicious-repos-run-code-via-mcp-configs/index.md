---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T03:24:17.419066+00:00'
exported_at: '2026-06-27T03:24:18.656784+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
structured_data:
  about: []
  author: ''
  description: Amazon patched CVE-2026-12957, a high-severity Amazon Q Developer flaw
    that let malicious MCP config run commands and steal AWS credentials.
  headline: Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/amazon-q-developer-flaw-could-let.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Amazon Q Developer Flaw Could Let Malicious Repos Run Code via MCP Configs
updated_at: '2026-06-27T03:24:17.419066+00:00'
url_hash: b1b6db37ba8fea46a9d264b0e6f1d62a64765bbc
---

**

Swati Khandelwal
**

Jun 26, 2026

AI Security / Vulnerability

A high-severity flaw in Amazon Q Developer let a malicious repository run commands and steal a developer's cloud credentials. The path was short: a developer opens the repo, trusts the workspace, and Amazon Q does the rest. Amazon has patched it.

Tracked as
[CVE-2026-12957](https://www.cve.org/cverecord?id=CVE-2026-12957)
(CVSS 8.5), the bug sat in how Amazon's AI coding assistant handled Model Context Protocol (MCP) servers.

Wiz Research, which found and reported it, showed that a single config file dropped in a repo was enough to go from git clone to cloud compromise.

## How the attack worked

Amazon Q read an MCP configuration file, .amazonq/mcp.json, from the open workspace and launched the servers it defined. MCP servers are local processes that an AI assistant can spawn to reach databases, APIs, or build tools, so starting one means running commands on the machine.

Those processes inherited the developer's full environment. That usually means AWS keys, cloud CLI tokens, API secrets, and SSH agent sockets.

Put the two together, and a file sitting in a cloned repo could run arbitrary code with the developer's live cloud session attached. No password, no second sign-in.

In its
[proof of concept](https://www.wiz.io/blog/amazon-q-vulnerability)
, Wiz had the file run aws sts get-caller-identity and ship the output to an attacker server, capturing the active AWS session. What comes next depends on that developer's cloud permissions: backdoor an IAM user for persistence, reach internal services, or pivot toward production.

AWS and Wiz frame the consent step differently. Amazon's
[advisory](https://github.com/aws/language-servers/security/advisories/GHSA-xhcr-j4j9-3gh7)
says the user has to trust the workspace when prompted, and CVSS rates the user interaction as passive.

Wiz reported there was no separate consent step for the MCP servers themselves before the fix. The patch closes that gap: Amazon Q now flags an untrusted MCP server and lets the developer reject the command before it runs.

The flaw lives in
[Language Servers for AWS](https://github.com/aws/language-servers)
, the runtime that powers Amazon Q across VS Code, JetBrains, Eclipse, and Visual Studio. All four plugins bundle it, so all four were exposed by versions that shipped an older copy.

## What to do

Update. CVE-2026-12957 is fixed in Language Servers for AWS 1.65.0, but AWS's
[bulletin](https://aws.amazon.com/security/security-bulletins/2026-047-aws/)
tells customers to move to 1.69.0.

That build also closes a second issue,
[CVE-2026-12958](https://www.cve.org/cverecord?id=CVE-2026-12958)
, a missing symlink check that could allow arbitrary file writes outside the workspace trust boundary.

The patched plugin minimums:

* VS Code: 2.20 or later
* JetBrains: 4.3 or later
* Eclipse: 2.7.4 or later
* Visual Studio toolkit: 1.94.0.0 or later

The language server auto-updates unless the network blocks it, and reloading the IDE pulls the latest build.

There is no known public exploitation; CISA's ADP entry for CVE-2026-12957 lists it as none. Wiz found the flaw through research and disclosed it in coordination with Amazon, reporting it on April 20 and seeing a fix on May 12, ahead of the June 26 public write-up.

## A pattern, not a one-off

Amazon Q is not the first coding assistant to trip over MCP trust. The bugs are not identical, but they rhyme: project configuration turns into executable behavior, and the trust checks around that handoff keep failing.

[Claude Code](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html)
(CVE-2025-59536) and
[Cursor](https://thehackernews.com/2025/08/cursor-ai-code-editor-vulnerability.html)
(CVE-2025-54136) both had project-level MCP config that led to command execution.
[Windsurf](https://www.ox.security/blog/mcp-supply-chain-advisory-rce-vulnerabilities-across-the-ai-ecosystem/)
(CVE-2026-30615) reached the same end by a different path, with attacker-controlled content rewriting the local MCP config to register a malicious server.

The convenience of letting a project folder configure an AI agent is also the attack surface. Repo-carried config is untrusted input. Turning it into a running process should take an explicit yes.