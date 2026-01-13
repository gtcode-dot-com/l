---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-13T12:15:13.871731+00:00'
exported_at: '2026-01-13T12:15:16.796963+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/servicenow-patches-critical-ai-platform.html
structured_data:
  about: []
  author: ''
  description: ServiceNow fixed CVE-2025-12420, a critical flaw that let unauthenticated
    attackers impersonate users on its AI Platform.
  headline: ServiceNow Patches Critical AI Platform Flaw Allowing Unauthenticated
    User Impersonation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/servicenow-patches-critical-ai-platform.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: ServiceNow Patches Critical AI Platform Flaw Allowing Unauthenticated User
  Impersonation
updated_at: '2026-01-13T12:15:13.871731+00:00'
url_hash: 5a6563984e6f0e55af5f0591e5d503a44e42d26f
---

**

Jan 13, 2026
**

Ravie Lakshmanan

Vulnerability / SaaS Security

ServiceNow has disclosed details of a now-patched critical security flaw impacting its ServiceNow AI Platform that could enable an unauthenticated user to impersonate another user and perform arbitrary actions as that user.

The vulnerability, tracked as
**[CVE-2025-12420](https://www.cve.org/CVERecord?id=CVE-2025-12420)**
, carries a CVSS score of 9.3 out of 10.0

"This issue [...] could enable an unauthenticated user to impersonate another user and perform the operations that the impersonated user is entitled to perform," the company
[said](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2587329)
in an advisory released Monday.

The shortcoming was addressed by ServiceNow on October 30, 2025, by deploying a security update to the majority of hosted instances, with the company also sharing the patches with ServiceNow partners and self-hosted customers.

The following versions include a fix for CVE-2025-12420 -

* Now Assist AI Agents (sn\_aia) - 5.1.18 or later and 5.2.19 or later
* Virtual Agent API (sn\_va\_as\_service) - 3.15.2 or later and 4.0.4 or later

ServiceNow credited Aaron Costello, chief of SaaS Security Research at AppOmni, with discovering and reporting the flaw in October 2025. While there is no evidence that the vulnerability has been exploited in the wild, users are advised to apply an appropriate security update as soon as possible to mitigate potential threats.

The disclosure comes nearly two months after AppOmni
[revealed](https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html)
that malicious actors can exploit default configurations in ServiceNow's Now Assist generative artificial intelligence (AI) platform and leverage its agentic capabilities to conduct second-order prompt injection attacks.

The issue could then be weaponized to execute unauthorized actions, enabling attackers to copy and exfiltrate sensitive corporate data, modify records, and escalate privileges.