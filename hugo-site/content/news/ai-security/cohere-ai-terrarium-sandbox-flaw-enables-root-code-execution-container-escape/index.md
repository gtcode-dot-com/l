---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-22T10:15:14.148770+00:00'
exported_at: '2026-04-22T10:15:16.405871+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/cohere-ai-terrarium-sandbox-flaw.html
structured_data:
  about: []
  author: ''
  description: CVE-2026-5752 CVSS 9.3 flaw in Terrarium enables root code execution
    via Pyodide prototype traversal, risking container escape.
  headline: Cohere AI Terrarium Sandbox Flaw Enables Root Code Execution, Container
    Escape
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/cohere-ai-terrarium-sandbox-flaw.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cohere AI Terrarium Sandbox Flaw Enables Root Code Execution, Container Escape
updated_at: '2026-04-22T10:15:14.148770+00:00'
url_hash: 5e19ddcc18e130ab2c5517450737ac6c2b19014b
---

**

Ravie Lakshmanan
**

Apr 22, 2026

Vulnerability / Container Security

A critical security vulnerability has been disclosed in a Python-based sandbox called
[Terrarium](https://github.com/cohere-ai/cohere-terrarium)
that could result in arbitrary code execution.

The vulnerability, tracked as
**CVE-2026-5752**
, is rated 9.3 on the CVSS scoring system.

"Sandbox escape vulnerability in Terrarium allows arbitrary code execution with root privileges on a host process via JavaScript prototype chain traversal," according to a
[description](https://www.cve.org/CVERecord?id=CVE-2026-5752)
of the flaw in CVE.org.

Developed by Cohere AI as an open-source project, Terrarium is a Python sandbox that's used as a Docker-deployed container for running untrusted code written by users or generated with assistance from a large language model (LLM).

Notably, Terrarium runs on Pyodide, a Python distribution for the browser and Node.js, enabling it to support standard Python packages.  The project has been forked 56 times and starred 312 times.

According to the CERT Coordination Center (CERT/CC), the root cause
[relates](https://kb.cert.org/vuls/id/414811)
to a JavaScript prototype chain traversal in the
[Pyodide](https://thehackernews.com/2026/01/critical-grist-core-vulnerability.html)
WebAssembly environment that enables code execution with elevated privileges on the host Node.js process.

Successful exploitation of the vulnerability can allow an attacker to break out of the confines of the sandbox and execute arbitrary system commands as root within the container.

In addition, it can permit unauthorized access to sensitive files, such as "/etc/passwd," reach other services on the container's network, and even possibly escape the container and escalate privileges further.

It bears noting that the attack requires local access to the system but does not require any user interaction or special privileges to exploit.

Security researcher Jeremy Brown has been credited with discovering and reporting the flaw. Given that the project is no longer actively maintained, the vulnerability is unlikely to be patched.

As mitigations, CERT/CC is advising users to take the following steps -

* Disable features that allow users to submit code to the sandbox, if possible.
* Segment the network to limit the attack surface and prevent lateral movement.
* Deploy a Web Application Firewall to detect and block suspicious traffic, including attempts to exploit the vulnerability.
* Monitor container activity for signs of suspicious behavior.
* Limit access to the container and its resources to authorized personnel only.
* Use a secure container orchestration tool to manage and secure containers.
* Ensure that dependencies are up-to-date and patched.

"The sandbox fails to adequately prevent access to parent or global object prototypes, allowing sandboxed code to reference and manipulate objects in the host environment," SentinelOne
[said](https://www.sentinelone.com/vulnerability-database/cve-2026-5752/)
. "This prototype pollution or traversal technique bypasses the intended security boundaries of the sandbox."