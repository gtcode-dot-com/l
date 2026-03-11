---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-11T16:15:14.015636+00:00'
exported_at: '2026-03-11T16:15:16.312649+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html
structured_data:
  about: []
  author: ''
  description: Two critical n8n flaws (CVSS 9.4, 9.5) enable RCE via expression sandbox
    escape and public forms, risking credential exposure.
  headline: Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored
    Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Critical n8n Flaws Allow Remote Code Execution and Exposure of Stored Credentials
updated_at: '2026-03-11T16:15:14.015636+00:00'
url_hash: b433948027c711a24ee5ff4362fe007da5109a8b
---

**

Ravie Lakshmanan
**

Mar 11, 2026

Vulnerability / Application Security

Cybersecurity researchers have disclosed details of two now-patched security flaws in the
[n8n](https://thehackernews.com/2026/02/critical-n8n-flaw-cve-2026-25049.html)
workflow automation platform, including two critical bugs that could result in arbitrary command execution.

The vulnerabilities are listed below -

* **[CVE-2026-27577](https://github.com/n8n-io/n8n/security/advisories/GHSA-vpcf-gvg4-6qwr)**
  (CVSS score: 9.4) - Expression sandbox escape leading to remote code execution (RCE)
* **[CVE-2026-27493](https://github.com/n8n-io/n8n/security/advisories/GHSA-75g8-rv7v-32f7)**
  (CVSS score: 9.5) - Unauthenticated expression evaluation via n8n's Form nodes

"CVE-2026-27577 is a sandbox escape in the expression compiler: a missing case in the AST rewriter lets process slip through untransformed, giving any authenticated expression full RCE," Pillar Security researcher Eilon Cohen, who discovered and reported the issues,
[said](https://www.pillar.security/blog/zero-click-unauthenticated-rce-in-n8n-a-contact-form-that-executes-shell-commands)
in a report shared with The Hacker News.

The cybersecurity company described CVE-2026-27493 as a "double-evaluation bug" in n8n's Form nodes that could be abused for expression injection by taking advantage of the fact that the form endpoints are public by design and require neither authentication nor an n8n account.

All it takes for successful exploitation is to leverage a public "Contact Us" form to execute arbitrary shell commands by simply providing a payload as input into the Name field.

In an advisory released late last month, n8n said CVE-2026-27577 could be weaponized by an authenticated user with permission to create or modify workflows to trigger unintended system command execution on the host running n8n via crafted expressions in workflow parameters.

N8n also noted that CVE-2026-27493, when chained with an expression sandbox escape like CVE-2026-27577, could "escalate to remote code execution on the n8n host." Both vulnerabilities affect the self-hosted and cloud deployments of n8n -

* < 1.123.22, >= 2.0.0 < 2.9.3, and >= 2.10.0 < 2.10.1 - Fixed in versions 2.10.1, 2.9.3, and 1.123.22

If immediate patching of CVE-2026-27577 is not an option, users are advised to limit workflow creation and editing permissions to fully trusted users and deploy n8n in a hardened environment with restricted operating system privileges and network access.

As for CVE-2026-27493, n8n recommends the following mitigations -

* Review the usage of form nodes manually for the above-mentioned preconditions.
* Disable the Form node by adding n8n-nodes-base.form to the NODES\_EXCLUDE environment variable.
* Disable the Form Trigger node by adding n8n-nodes-base.formTrigger to the NODES\_EXCLUDE environment variable.

"These workarounds do not fully remediate the risk and should only be used as short-term mitigation measures," the maintainers cautioned.

Pillar Security said an attacker could exploit these flaws to read the N8N\_ENCRYPTION\_KEY environment variable and use it to decrypt every credential stored in n8n's database, including AWS keys, database passwords, OAuth tokens, and API keys.

N8n versions 2.10.1, 2.9.3, and 1.123.22 also resolve two more critical vulnerabilities that could also be abused to achieve arbitrary code execution -

* **[CVE-2026-27495](https://github.com/n8n-io/n8n/security/advisories/GHSA-jjpj-p2wh-qf23)**
  (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could exploit a code injection vulnerability in the JavaScript Task Runner sandbox to execute arbitrary code outside the sandbox boundary.
* **[CVE-2026-27497](https://github.com/n8n-io/n8n/security/advisories/GHSA-wxx7-mcgf-j869)**
  (CVSS score: 9.4) - An authenticated user with permission to create or modify workflows could leverage the Merge node's SQL query mode to execute arbitrary code and write arbitrary files on the n8n server.

Besides limiting workflow creation and editing permissions to trusted users, n8n has outlined the workarounds below for each flaw -

* **CVE-2026-27495**
  - Use external runner mode (N8N\_RUNNERS\_MODE=external) to limit the blast radius.
* **CVE-2026-27497**
  - Disable the Merge node by adding n8n-nodes-base.merge to the NODES\_EXCLUDE environment variable.

While n8n makes no mention of any of these vulnerabilities being exploited in the wild, users are advised to keep their installations up-to-date for optimal protection.