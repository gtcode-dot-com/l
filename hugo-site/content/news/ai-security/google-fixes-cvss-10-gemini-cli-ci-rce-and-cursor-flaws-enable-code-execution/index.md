---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-30T08:15:15.433566+00:00'
exported_at: '2026-04-30T08:15:17.646845+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
structured_data:
  about: []
  author: ''
  description: Gemini CLI CVSS 10.0 flaw in versions below 0.39.1 enabled RCE in CI
    workflows, forcing Google to mandate explicit workspace trust.
  headline: Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Fixes CVSS 10 Gemini CLI CI RCE and Cursor Flaws Enable Code Execution
updated_at: '2026-04-30T08:15:15.433566+00:00'
url_hash: 15a54f0c111de7f3a4dcb6fbcc04043d02a7d4ef
---

Google has addressed a maximum severity security flaw in Gemini CLI -- the "@google/gemini-cli" npm package and the "google-github-actions/run-gemini-cli" GitHub Actions workflow -- that could have allowed attackers to execute arbitrary commands on host systems.

"The vulnerability allowed an unprivileged external attacker to force their own malicious content to load as Gemini configuration," Novee Security
[said](https://novee.security/blog/google-gemini-cli-rce-vulnerability-cvss-10-critical-security-advisory/)
in a Wednesday report. "This triggered command execution directly on the host system, bypassing security before the agent’s sandbox even initialized."

The shortcoming, which does not have a CVE identifier, carries a CVSS score of 10.0. It affects the following versions -

* @google/gemini-cli < 0.39.1
* @google/gemini-cli < 0.40.0-preview.3
* google-github-actions/run-gemini-cli < 0.1.22

In its advisory
[published](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g)
last week, Google said the impact is limited to workflows using Gemini CLI in headless mode, adding that any use of the tool in headless mode without folder trust will require manual review to configure this trust mechanism.

"In previous versions, Gemini CLI running in CI environments (headless mode) automatically trusted workspace folders for the purpose of loading configuration and environment variables," it said.

"This is potentially risky in situations where Gemini CLI runs on untrusted folders in headless mode (e.g., CI workflows that review user-submitted pull requests). If used with untrusted directory contents, this could lead to remote code execution via malicious environment variables in the local .gemini/ directory."

This automatic trust of the current workspace folder meant that the tool could load any agent configuration it found without review, sandboxing, or explicit user consent. An attacker could weaponize this behavior by planting a specially crafted configuration that could pave the way for code execution on the host running the agent, effectively turning CI/CD pipelines into supply-chain attack paths.

The update addresses the problem by requiring folders to be explicitly trusted before configuration files can be accessed. To that end, users are being urged to review their workflows and adopt one of two approaches -

* If the workflow runs on trusted inputs (e.g., reviewing pull requests from trusted collaborators), set GEMINI\_TRUST\_WORKSPACE: 'true' in the workflow.
* If the workflow runs on untrusted inputs, review Google's guidance in
  [google-github-actions/run-gemini-cli](https://github.com/google-github-actions/run-gemini-cli)
  to harden the workflow against malicious content, and set the environment variable.

The tech giant also noted that it's taking steps to harden tool allowlisting when Gemini CLI is configured to run in --yolo mode to prevent scenarios where untrusted inputs (e.g., user-submitted GitHub issues) could lead to remote code execution via prompt injection by taking advantage of the fact that the auto-approve mode would ignore any allowlist in "~/.gemini/settings.json" and run all tool calls automatically (including "run\_shell\_command") without requiring user confirmation.

"In version 0.39.1, the Gemini CLI policy engine now evaluates tool allowlisting under --yolo mode, which is useful for CI workflows that allowlist a few safe commands to run when processing untrusted inputs," Google said. "As a result, some workflows that previously depended on this behavior may fail silently unless tool allowlists are modified to fit the task."

### Cursor Bug Leads to Code Execution

The disclosure comes as Novee Security also highlighted a high-severity vulnerability in the AI-powered development tool Cursor prior to version 2.5 (CVE-2026-26268, CVSS score: 8.1) that could also lead to arbitrary code execution by means of a prompt injection.

Cursor, in an alert
[released](https://github.com/cursor/cursor/security/advisories/GHSA-8pcm-8jpx-hv8r)
in February 2026, described it as a case of sandbox escape through .git configurations, allowing a rogue agent to set up a bare repository (".git") with a malicious
[Git hook](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks)
that's automatically fired every time a commit operation runs within the embedded repository context without requiring any user interaction.

The end result is auto-approved arbitrary code execution on the victim's machine through the following sequence of actions -

* User clones a public GitHub repository with the embedded bare repository containing a malicious post-checkout hook
* User opens the repository in CursorIDE
* Users ask an innocuous prompt to "explain the codebase"
* Cursor agent parses the
  [AGENTS.md](https://agents.md/)
  that instructs it to navigate to the bare repository and performs a "git checkout" of the master branch
* The post-checkout hook inside the bare repository is triggered, leading to code execution.

"The root cause is not a flaw in Cursor's core product logic, but rather a consequence of a feature interaction in Git, one that becomes exploitable the moment an AI agent starts autonomously executing Git operations inside a repository it doesn't control," security researcher Assaf Levkovich
[said](https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/)
.

"When the agent runs git checkout as part of fulfilling a routine request, it is not doing anything the user didn't implicitly authorize. But neither the user nor the agent has visibility into what the repository's Cursor Rules have set in motion. A malicious pre-commit hook embedded in a nested bare repository executes silently, outside the agent's reasoning chain and outside the user’s field of view."

The findings also coincide with the discovery of another high-severity access control vulnerability in the IDE (CVSS score: 8.2) that could allow any installed extension to access sensitive API keys and credentials stored locally in an SQLite database, enabling account takeover, data exposure, and financial loss stemming from unauthorized API usage. The issue, codenamed
[CursorJacking](https://layerxsecurity.com/blog/cursorjacking-every-cursor-user-is-vulnerable-to-api-key-theft-by-rogue-extensions/)
by LayerX, remains unpatched.

"Cursor does not enforce access control boundaries between extensions and this database," LayerX researcher Roy Paz said. "Exploitation of this vulnerability can lead to exposure of session tokens and API keys, unauthorized access to Cursor backend services, and data theft via user impersonation."

Cursor has maintained that the access is limited to the local machine where the user has already installed and granted permissions to the extension, meaning any rogue extension with local file system access could potentially extract valuable information from various application data stores. To counter the threat, it's essential that users stick to downloading trusted extensions.