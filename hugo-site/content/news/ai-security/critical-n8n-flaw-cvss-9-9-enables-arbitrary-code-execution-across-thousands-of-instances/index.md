---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-23T12:03:10.789828+00:00'
exported_at: '2025-12-23T12:03:13.151694+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html
structured_data:
  about: []
  author: ''
  description: Critical n8n flaw CVE-2025-68613 (CVSS 9.9) lets authenticated users
    run arbitrary code; versions 0.211.0–1.120.4 affected, patched in newer releases.
  headline: Critical n8n Flaw (CVSS 9.9) Enables Arbitrary Code Execution Across Thousands
    of Instances
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Critical n8n Flaw (CVSS 9.9) Enables Arbitrary Code Execution Across Thousands
  of Instances
updated_at: '2025-12-23T12:03:10.789828+00:00'
url_hash: 434bd30d33ce55d138c76c047f4928077e7ad824
---

**

Dec 23, 2025
**

Ravie Lakshmanan

Vulnerability / Workflow Automation

A critical security vulnerability has been disclosed in the
[n8n](https://www.npmjs.com/package/n8n)
workflow automation platform that, if successfully exploited, could result in arbitrary code execution under certain circumstances.

The vulnerability, tracked as
**[CVE-2025-68613](https://nvd.nist.gov/vuln/detail/CVE-2025-68613)**
, carries a CVSS score of 9.9 out of a maximum of 10.0. The package has about 57,000 weekly downloads, according to statistics on npm.

"Under certain conditions, expressions supplied by authenticated users during workflow configuration may be evaluated in an execution context that is not sufficiently isolated from the underlying runtime," the maintainers of the npm package
[said](https://github.com/n8n-io/n8n/security/advisories/GHSA-v98v-ff95-f3cp)
.

"An authenticated attacker could abuse this behavior to execute arbitrary code with the privileges of the n8n process. Successful exploitation may lead to full compromise of the affected instance, including unauthorized access to sensitive data, modification of workflows, and execution of system-level operations."

The issue, which affects all versions including and higher than 0.211.0 and below 1.120.4, has been patched in 1.120.4, 1.121.1, and 1.122.0. Per the attack surface management platform Censys, there are
[103,476 potentially vulnerable instances](https://censys.com/advisory/cve-2025-68613)
as of December 22, 2025. A majority of the instances are located in the U.S., Germany, France, Brazil, and Singapore.

In light of the criticality of the flaw, users are advised to apply the updates as soon as possible. If immediate patching is not an option, it's advised to limit workflow creation and editing permissions to trusted users and deploy n8n in a hardened environment with restricted operating system privileges and network access to mitigate the risk.