---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-28T14:15:14.659973+00:00'
exported_at: '2026-01-28T14:15:17.121689+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html
structured_data:
  about: []
  author: ''
  description: Researchers disclosed two n8n vulnerabilities that let authenticated
    users bypass JavaScript and Python sandboxes to run arbitrary code.
  headline: Two High-Severity n8n Flaws Allow Authenticated Remote Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Two High-Severity n8n Flaws Allow Authenticated Remote Code Execution
updated_at: '2026-01-28T14:15:14.659973+00:00'
url_hash: 0c6855fb11fed77bb68f10de8ecc2dafe59b8627
---

**

Ravie Lakshmanan
**

Jan 28, 2026

Vulnerability / Workflow Automation

Cybersecurity researchers have
[disclosed](https://research.jfrog.com/post/achieving-remote-code-execution-on-n8n-via-sandbox-escape/)
two new security flaws in the n8n workflow automation platform, including a crucial vulnerability that could result in remote code execution.

The weaknesses, discovered by the JFrog Security Research team, are listed below -

* **[CVE-2026-1470](https://nvd.nist.gov/vuln/detail/CVE-2026-1470)**
  (CVSS score: 9.9) - An
  [eval injection vulnerability](https://cwe.mitre.org/data/definitions/95.html)
  that could allow an authenticated user to bypass the
  [Expression sandbox mechanism](https://docs.n8n.io/code/expressions/)
  and achieve full remote code execution on n8n's main node by passing specially crafted JavaScript code
* **[CVE-2026-0863](https://nvd.nist.gov/vuln/detail/CVE-2026-0863)**
  (CVSS score: 8.5) - An eval injection vulnerability that could allow an authenticated user to bypass n8n's python-task-executor sandbox restrictions and run arbitrary Python code on the underlying operating system

Successful exploitation of the flaws could permit an attacker to hijack an entire n8n instance, including under scenarios where it's operating under "internal" execution mode. In its documentation, n8n
[notes](https://docs.n8n.io/hosting/configuration/task-runners/)
that using internal mode in production environments can pose a security risk, urging users to switch to external mode to ensure proper isolation between n8n and task runner processes.

"As n8n spans an entire organization to automate AI workflows, it holds the keys to core tools, functions, and data from infrastructure, including LLM APIs, sales data, and internal IAM systems, among others," JFrog said in a statement shared with The Hacker News. "This results in escapes giving a hacker an effective "skeleton key" to the entire corporation."

To address the flaws, users are advised to update to the following versions -

* **CVE-2026-1470**
  - 1.123.17, 2.4.5, or 2.5.1
* **CVE-2026-0863**
  - 1.123.14, 2.3.5, or 2.4.2

The development comes merely weeks after Cyera Research Labs detailed a maximum-severity security flaw in n8n (
[CVE-2026-21858](https://thehackernews.com/2026/01/critical-n8n-vulnerability-cvss-100.html)
aka Ni8mare) that allows an unauthenticated remote attacker to gain complete control over susceptible instances.

"These vulnerabilities highlight how difficult it is to safely sandbox dynamic, high‑level languages such as JavaScript and Python," researcher Nathan Nehorai said. "Even with multiple validation layers, deny lists, and AST‑based controls in place, subtle language features and runtime behaviors can be leveraged to bypass security assumptions."

"In this case, deprecated or rarely used constructs, combined with interpreter changes and exception handling behavior, were enough to break out of otherwise restrictive sandboxes and achieve remote code execution."