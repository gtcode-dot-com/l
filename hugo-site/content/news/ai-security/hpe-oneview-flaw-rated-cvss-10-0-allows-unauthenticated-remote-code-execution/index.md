---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-20T00:03:12.849205+00:00'
exported_at: '2025-12-20T00:03:15.587849+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/hpe-oneview-flaw-rated-cvss-100-allows.html
structured_data:
  about: []
  author: ''
  description: HPE patched a critical OneView vulnerability with CVSS 10.0 that could
    allow unauthenticated remote code execution in versions before 11.00.
  headline: HPE OneView Flaw Rated CVSS 10.0 Allows Unauthenticated Remote Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/hpe-oneview-flaw-rated-cvss-100-allows.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: HPE OneView Flaw Rated CVSS 10.0 Allows Unauthenticated Remote Code Execution
updated_at: '2025-12-20T00:03:12.849205+00:00'
url_hash: 105add5a6f7d9d13d38ba1a0b870e6b89840a77f
---

**

Dec 18, 2025
**

Ravie Lakshmanan

Vulnerability / Enterprise Security

Hewlett Packard Enterprise (HPE) has resolved a maximum-severity security flaw in OneView Software that, if successfully exploited, could result in remote code execution.

The critical vulnerability, assigned the CVE identifier
**[CVE-2025-37164](https://nvd.nist.gov/vuln/detail/CVE-2025-37164)**
, carries a CVSS score of 10.0. HPE
[OneView](https://www.hpe.com/us/en/software/oneview.html)
is an IT infrastructure management software that streamlines IT operations and controls all systems via a centralized dashboard interface.

"A potential security vulnerability has been identified in Hewlett Packard Enterprise OneView Software. This vulnerability could be exploited, allowing a remote unauthenticated user to perform remote code execution," HPE
[said](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbgn04985en_us&docLocale=en_US#vulnerability-summary-1)
in an advisory issued this week.

It affects all versions of the software prior to
[version 11.00](https://support.hpe.com/hpesc/public/docDisplay?docId=sd00006817en_us&page=GUID-EE158266-5CA2-4EF6-BDEF-BD4945C38EDA.html)
, which addresses the flaw. The company has also made available a hotfix that can be applied to OneView versions 5.20 through 10.20.

It's worth noting that the hotfix must be reapplied after upgrading from version 6.60 or later to version 7.00.00, or after any HPE Synergy Composer reimaging operations. Separate hotfixes are available for the OneView virtual appliance and Synergy Composer2.

Although HPE makes no mention of the flaw being exploited in the wild, it's essential that users apply the patches as soon as possible for optimal protection.

Earlier this June, the company also
[released](https://thehackernews.com/2025/06/hpe-issues-security-patch-for-storeonce.html)
updates to fix eight vulnerabilities in its StoreOnce data backup and deduplication solution that could result in an authentication bypass and remote code execution. It also shipped OneView version 10.00 to remediate a number of known flaws in third-party components, such as Apache Tomcat and Apache HTTP Server.