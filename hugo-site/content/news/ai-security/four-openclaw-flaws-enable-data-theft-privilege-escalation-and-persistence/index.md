---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-15T17:19:50.123978+00:00'
exported_at: '2026-05-15T17:19:53.938318+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html
structured_data:
  about: []
  author: ''
  description: Claw Chain flaws in OpenClaw 2026.4.22 enable data theft, privilege
    escalation, and persistence when chained.
  headline: Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/four-openclaw-flaws-enable-data-theft.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Four OpenClaw Flaws Enable Data Theft, Privilege Escalation, and Persistence
updated_at: '2026-05-15T17:19:50.123978+00:00'
url_hash: 3d84935ad4c5753cca4a91d11f5b2a6e6ee2e364
---

**

Ravie Lakshmanan
**

May 15, 2026

Vulnerability / AI Security

Cybersecurity researchers have disclosed a set of four security flaws in OpenClaw that could be chained to achieve data theft, privilege escalation, and persistence.

The vulnerabilities, collectively dubbed
**[Claw Chain](https://www.cyera.com/blog/claw-chain-cyera-research-unveil-four-chainable-vulnerabilities-in-openclaw)**
by Cyera, can permit an attacker to establish a foothold, expose sensitive data, and plant backdoors. A brief description of the flaws is below -

* **[CVE-2026-44112](https://nvd.nist.gov/vuln/detail/CVE-2026-44112)**
  (CVSS score: 9.6/6.3) - A time-of-check/time-of-use (TOCTOU) race condition vulnerability in the
  [OpenShell](https://docs.openclaw.ai/gateway/openshell)
  managed sandbox backend that allows attackers to bypass sandbox restrictions and redirect writes outside the intended mount root.
* **[CVE-2026-44113](https://nvd.nist.gov/vuln/detail/CVE-2026-44113)**
  (CVSS score: 7.7/6.3) - A TOCTOU race condition vulnerability in OpenShell that allows attackers to bypass sandbox restrictions and read files outside the intended mount root.
* **[CVE-2026-44115](https://nvd.nist.gov/vuln/detail/CVE-2026-44115)**
  (CVSS score: 8.8) - An incomplete list of disallowed inputs vulnerability that allows attackers to bypass allowlist validation by embedding shell expansion tokens in a
  [here document](https://en.wikipedia.org/wiki/Here_document)
  (heredoc) body to execute unapproved commands at runtime.
* **[CVE-2026-44118](https://nvd.nist.gov/vuln/detail/CVE-2026-44118)**
  (CVSS score: 7.8) - An improper access control vulnerability that could allow non-owner loopback clients to impersonate an owner to elevate their privileges and gain control over gateway configuration, cron scheduling, and execution environment management.

Cyera said successful exploitation of CVE-2026-44112 could allow an attacker to tamper with configuration, plant backdoors, and establish persistent control over the compromised host, whereas CVE-2026-44113 could be weaponized to read system files, credentials, and internal artifacts.

The exploitation chain unfolds over four steps -

* A malicious plugin, prompt injection, or compromised external input gains code execution inside the OpenShell sandbox.
* Leverage CVE-2026-44113 and CVE-2026-44115 to expose credentials, secrets, and sensitive files.
* Exploit CVE-2026-44118 to obtain owner-level control of the agent runtime.
* Use CVE-2026-44112 to plant backdoors or make configuration changes and set up persistence.

The root cause for CVE-2026-44118, per the cybersecurity company, stems from the fact that OpenClaw trusts a client-controlled ownership flag called senderIsOwner, which signals whether the caller is authorized for owner-only tools, without validating it against the authenticated session.

"The MCP loopback runtime now issues separate owner and non-owner bearer tokens and derives senderIsOwner exclusively from which token authenticated the request," OpenClaw detailed the fixes in an advisory for the flaw. "The spoofable sender-owner header is no longer emitted or trusted."

Following responsible disclosure, all four vulnerabilities have been addressed in OpenClaw version 2026.4.22. Security researcher Vladimir Tokarev has been credited with discovering and reporting the issues. Users are advised to update to the latest version to stay protected against potential threats.

"By weaponizing the agent's own privileges, an adversary moves through data access, privilege escalation, and persistence -- using the agent as their hands inside the environment," Cyera said. "Each step looks like normal agent behavior to traditional controls, broadening blast radius and making detection significantly harder."