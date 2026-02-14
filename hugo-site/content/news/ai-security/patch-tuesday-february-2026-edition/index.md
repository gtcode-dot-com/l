---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-14T23:10:30.697234+00:00'
exported_at: '2026-02-14T23:10:35.590858+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition
structured_data:
  about: []
  author: ''
  description: Patch Tuesday, February 2026 Edition
  headline: Patch Tuesday, February 2026 Edition
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/02/patch-tuesday-february-2026-edition
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Patch Tuesday, February 2026 Edition
updated_at: '2026-02-14T23:10:30.697234+00:00'
url_hash: 742a6972155a7eaac533c94edbecf71a1a74c21a
---

**Microsoft**
today released updates to fix more than 50 security holes in its
**Windows**
operating systems and other software, including patches for a whopping six “zero-day” vulnerabilities that attackers are already exploiting in the wild.

![](https://krebsonsecurity.com/wp-content/uploads/2022/07/winupdatedate.png)

Zero-day #1 this month is
[CVE-2026-21510](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21510)
, a security feature bypass vulnerability in
**Windows Shell**
wherein a single click on a malicious link can quietly bypass Windows protections and run attacker-controlled content without warning or consent dialogs. CVE-2026-21510 affects all currently supported versions of Windows.

The zero-day flaw
[CVE-2026-21513](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21513)
is a security bypass bug targeting
**MSHTML**
, the proprietary engine of the default Web browser in Windows.
[CVE-2026-21514](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21514)
is a related security feature bypass in
**Microsoft Word.**

The zero-day
[CVE-2026-21533](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21533)
allows local attackers to elevate their user privileges to “SYSTEM” level access in
**Windows Remote Desktop Services**
.
[CVE-2026-21519](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21519)
is a zero-day elevation of privilege flaw in the
**Desktop Window Manager**
(DWM), a key component of Windows that organizes windows on a user’s screen. Microsoft fixed a different zero-day in DWM
[just last month](https://krebsonsecurity.com/2026/01/patch-tuesday-january-2026-edition/)
.

The sixth zero-day is
[CVE-2026-21525](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-21525)
, a potentially disruptive denial-of-service vulnerability in the
**Windows Remote Access Connection Manager**
, the service responsible for maintaining VPN connections to corporate networks.

**Chris Goettl**
at
**Ivanti**
reminds us Microsoft has issued several out-of-band security updates since January’s Patch Tuesday. On January 17, Microsoft pushed a fix that resolved a credential prompt failure when attempting remote desktop or remote application connections. On January 26, Microsoft patched a zero-day security feature bypass vulnerability (
[CVE-2026-21509](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21509)
) in
**Microsoft Office**
.

**Kev Breen**
at
**Immersive**
notes that this month’s Patch Tuesday includes several fixes for remote code execution vulnerabilities affecting
**GitHub Copilot**
and multiple integrated development environments (IDEs), including
**VS Code**
,
**Visual Studio**
, and
**JetBrains**
products. The relevant CVEs are
[CVE-2026-21516](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21516)
,
[CVE-2026-21523](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21523)
, and
[CVE-2026-21256](https://msrc.microsoft.com/update-guide/en-US/advisory/CVE-2026-21256)
.

Breen said the AI vulnerabilities Microsoft patched this month stem from a command injection flaw that can be triggered through prompt injection, or tricking the AI agent into doing something it shouldn’t — like executing malicious code or commands.

“Developers are high-value targets for threat actors, as they often have access to sensitive data such as API keys and secrets that function as keys to critical infrastructure, including privileged AWS or Azure API keys,” Breen said. “When organizations enable developers and automation pipelines to use LLMs and agentic AI, a malicious prompt can have significant impact. This does not mean organizations should stop using AI. It does mean developers should understand the risks, teams should clearly identify which systems and workflows have access to AI agents, and least-privilege principles should be applied to limit the blast radius if developer secrets are compromised.”

The
**SANS Internet Storm Center**
has a
[clickable breakdown](https://isc.sans.edu/diary/Microsoft%20Patch%20Tuesday%20-%20February%202026/32700)
of each individual fix this month from Microsoft, indexed by severity and CVSS score. Enterprise Windows admins involved in testing patches before rolling them out should keep an eye on
[askwoody.com](https://www.askwoody.com/2026/february-2026-security-updates/)
, which often has the skinny on wonky updates. Please don’t neglect to back up your data if it has been a while since you’ve done that, and feel free to sound off in the comments if you experience problems installing any of these fixes.