---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-07T00:03:07.411869+00:00'
exported_at: '2025-12-07T00:03:09.635258+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
structured_data:
  about: []
  author: ''
  description: More than 30 security flaws in AI-powered IDEs allow data leaks and
    remote code execution, showing major risks in modern coding tools.
  headline: Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and
    RCE Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Uncover 30+ Flaws in AI Coding Tools Enabling Data Theft and RCE
  Attacks
updated_at: '2025-12-07T00:03:07.411869+00:00'
url_hash: 06769c58e2f3b0d731256114cba39c3875860b96
---

**

Dec 06, 2025
**

Ravie Lakshmanan

AI Security / Vulnerability

Over 30 security vulnerabilities have been disclosed in various artificial intelligence (AI)-powered Integrated Development Environments (IDEs) that combine
[prompt injection primitives](https://thehackernews.com/2025/11/researchers-find-chatgpt.html)
with legitimate features to achieve data exfiltration and remote code execution.

The security shortcomings have been collectively named
**[IDEsaster](https://maccarita.com/posts/idesaster/)**
by security researcher Ari Marzouk (MaccariTA). They affect popular IDEs and extensions such as Cursor, Windsurf, Kiro.dev, GitHub Copilot, Zed.dev, Roo Code, Junie, and Cline, among others. Of these, 24 have been assigned CVE identifiers.

"I think the fact that multiple universal attack chains affected each and every AI IDE tested is the most surprising finding of this research," Marzouk told The Hacker News.

"All AI IDEs (and coding assistants that integrate with them) effectively ignore the base software (IDE) in their threat model. They treat their features as inherently safe because they've been there for years. However, once you add AI agents that can act autonomously, the same features can be weaponized into data exfiltration and RCE primitives."

At its core, these issues chain three different vectors that are common to AI-driven IDEs -

* Bypass a large language model's (LLM) guardrails to hijack the context and perform the attacker's bidding (aka prompt injection)
* Perform certain actions without requiring any user interaction via an AI agent's auto-approved tool calls
* Trigger an IDE's legitimate features that allow an attacker to break out of the security boundary to leak sensitive data or execute arbitrary commands

The highlighted issues are different from prior attack chains that have leveraged prompt injections in conjunction with vulnerable tools (or abusing legitimate tools to perform read or write actions) to modify an AI agent's configuration to achieve code execution or other unintended behavior.

What makes IDEsaster notable is that it takes prompt injection primitives and an agent's tools, using them to activate legitimate features of the IDE to result in information leakage or command execution.

Context hijacking can be pulled off in myriad ways, including through user-added context references that can take the form of pasted URLs or text with hidden characters that are not visible to the human eye, but can be parsed by the LLM. Alternatively, the context can be polluted by using a Model Context Protocol (MCP) server through
[tool poisoning](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html)
or
[rug pulls](https://thehackernews.com/2025/09/two-critical-flaws-uncovered-in.html)
, or when a legitimate MCP server parses attacker-controlled input from an external source.

Some of the identified attacks made possible by the new exploit chain is as follows -

* **[CVE-2025-49150](https://www.cve.org/CVERecord?id=CVE-2025-49150)
  (Cursor),
  [CVE-2025-53097](https://www.cve.org/CVERecord?id=CVE-2025-53097)
  (Roo Code),
  [CVE-2025-58335](https://www.cve.org/CVERecord?id=CVE-2025-58335)
  (JetBrains Junie), GitHub Copilot (no CVE), Kiro.dev (no CVE), and Claude Code (addressed with a
  [security warning](https://code.claude.com/docs/en/vs-code#security-considerations)
  )**
  - Using a prompt injection to read a sensitive file using either a legitimate ("read\_file") or vulnerable tool ("search\_files" or "search\_project") and writing a JSON file via a legitimate tool ("write\_file" or "edit\_file)) with a remote JSON schema hosted on an attacker-controlled domain, causing the data to be leaked when the IDE makes a GET request
* **[CVE-2025-53773](https://www.cve.org/CVERecord?id=CVE-2025-53773)
  (GitHub Copilot),
  [CVE-2025-54130](https://www.cve.org/CVERecord?id=CVE-2025-54130)
  (Cursor),
  [CVE-2025-53536](https://www.cve.org/CVERecord?id=CVE-2025-53536)
  (Roo Code),
  [CVE-2025-55012](https://www.cve.org/CVERecord?id=CVE-2025-55012)
  (Zed.dev), and Claude Code (addressed with a
  [security warning](https://code.claude.com/docs/en/vs-code#security-considerations)
  )**
  - Using a prompt injection to edit IDE settings files (".vscode/settings.json" or ".idea/workspace.xml") to achieve code execution by setting "php.validate.executablePath" or "PATH\_TO\_GIT" to the path of an executable file containing malicious code
* **[CVE-2025-64660](https://www.cve.org/CVERecord?id=CVE-2025-64660)
  (GitHub Copilot),
  [CVE-2025-61590](https://www.cve.org/CVERecord?id=CVE-2025-61590)
  (Cursor), and
  [CVE-2025-58372](https://www.cve.org/CVERecord?id=CVE-2025-58372)
  (Roo Code)**
  - Using a prompt injection to edit workspace configuration files (\*.code-workspace) and override
  [multi-root workspace](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces)
  settings to achieve code execution

It's worth noting that the last two examples hinge on an AI agent being configured to auto-approve file writes, which subsequently allows an attacker with the ability to influence prompts to cause malicious workspace settings to be written. But given that this behavior is auto-approved by default for in-workspace files, it leads to arbitrary code execution without any user interaction or the need to reopen the workspace.

With prompt injections and jailbreaks acting as the first step for the attack chain, Marzouk offers the following recommendations -

* *Only use AI IDEs (and AI agents) with trusted projects and files. Malicious rule files, instructions hidden inside source code or other files (README), and even file names can become prompt injection vectors.*
* *Only connect to trusted MCP servers and continuously monitor these servers for changes (even a trusted server can be breached). Review and understand the data flow of MCP tools (e.g., a legitimate MCP tool might pull information from attacker controlled source, such as a GitHub PR)*
* *Manually review sources you add (such as via URLs) for hidden instructions (comments in HTML / css-hidden text / invisible unicode characters, etc.)*

Developers of AI agents and AI IDEs are advised to apply the principle of least privilege to LLM tools, minimize prompt injection vectors, harden the system prompt, use sandboxing to run commands, perform security testing for path traversal, information leakage, and command injection.

The disclosure coincides with the discovery of several vulnerabilities in AI coding tools that could have a wide range of impacts -

* A command injection flaw in OpenAI Codex CLI (
  [CVE-2025-61260](https://research.checkpoint.com/2025/openai-codex-cli-command-injection-vulnerability/)
  ) that takes advantage of the fact that the program implicitly trusts commands configured via MCP server entries and executes them at startup without seeking a user's permission. This could lead to arbitrary command execution when a malicious actor can tamper with the repository's ".env" and "./.codex/config.toml" files.
* An
  [indirect prompt injection](https://www.promptarmor.com/resources/google-antigravity-exfiltrates-data)
  in Google Antigravity using a poisoned web source that can be used to manipulate Gemini into harvesting credentials and sensitive code from a user's IDE and exfiltrating the information using a browser subagent to browse to a malicious site.
* Multiple vulnerabilities in Google Antigravity that could result in
  [data exfiltration and remote command execution](https://embracethered.com/blog/posts/2025/security-keeps-google-antigravity-grounded/)
  via indirect prompt injections, as well as leverage a
  [malicious trusted workspace](https://mindgard.ai/blog/google-antigravity-persistent-code-execution-vulnerability)
  to embed a persistent backdoor to execute arbitrary code every time the application is launched in the future.
* A new class of vulnerability named
  [PromptPwnd](https://www.aikido.dev/blog/promptpwnd-github-actions-ai-agents)
  that targets AI agents connected to vulnerable GitHub Actions (or GitLab CI/CD pipelines) with prompt injections to trick them into executing built-in privileged tools that lead to information leak or code execution.

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/zscaler-ai-event-d)

As agentic AI tools are becoming increasingly popular in enterprise environments, these findings demonstrate how AI tools expand the attack surface of development machines, often by leveraging an LLM's inability to distinguish between instructions provided by a user to complete a task and content that it may ingest from an external source, which, in turn, can contain an embedded malicious prompt.

"Any repository using AI for issue triage, PR labeling, code suggestions, or automated replies is at risk of prompt injection, command injection, secret exfiltration, repository compromise and upstream supply chain compromise," Aikido researcher Rein Daelman said.

Marzouk also said the discoveries emphasized the importance of "Secure for AI," which is a new paradigm that has been coined by the researcher to tackle security challenges introduced by AI features, thereby ensuring that products are not only secure by default and secure by design, but are also conceived keeping in mind how AI components can be abused over time.

"This is another example of why the 'Secure for AI' principle is needed," Marzouk said. "Connecting AI agents to existing applications (in my case IDE, in their case GitHub Actions) creates new emerging risks."