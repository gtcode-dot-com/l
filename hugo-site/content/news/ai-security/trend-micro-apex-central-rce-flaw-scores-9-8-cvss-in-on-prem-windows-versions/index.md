---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-09T10:15:14.643457+00:00'
exported_at: '2026-01-09T10:15:17.021520+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/trend-micro-apex-central-rce-flaw.html
structured_data:
  about: []
  author: ''
  description: Trend Micro patched a critical Apex Central on-prem Windows flaw (CVE-2025-69258)
    with CVSS 9.8 that allows remote code execution if access exists.
  headline: Trend Micro Apex Central RCE Flaw Scores 9.8 CVSS in On-Prem Windows Versions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/trend-micro-apex-central-rce-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Trend Micro Apex Central RCE Flaw Scores 9.8 CVSS in On-Prem Windows Versions
updated_at: '2026-01-09T10:15:14.643457+00:00'
url_hash: a22671d10e4544927ff1d91ca8eb84f0e7ef9635
---

**

Jan 09, 2026
**

Ravie Lakshmanan

Vulnerability / Endpoint Security

Trend Micro has
[released](https://success.trendmicro.com/en-US/solution/KA-0022071)
security updates to address multiple security vulnerabilities impacting on-premise versions of Apex Central for Windows, including a critical bug that could result in arbitrary code execution.

The vulnerability, tracked as
**CVE-2025-69258**
, carries a CVSS score of 9.8 out of a maximum of 10.0. The vulnerability has been described as a case of remote code execution affecting LoadLibraryEX.

"A LoadLibraryEX vulnerability in Trend Micro Apex Central could allow an unauthenticated remote attacker to load an attacker-controlled DLL into a key executable, leading to execution of attacker-supplied code under the context of SYSTEM on affected installations," the cybersecurity company said.

Also patched by Trend Micro are two other flaws -

* **CVE-2025-69259**
  (CVSS score: 7.5) - A message unchecked NULL return value vulnerability in Trend Micro Apex Central could allow a remote, unauthenticated attacker to create a denial-of-service condition on affected installations
* **CVE-2025-69260**
  (CVSS score: 7.5) - A message out-of-bounds read vulnerability in Trend Micro Apex Central could allow a remote, unauthenticated attacker to create a denial-of-service condition on affected installations

Tenable, which is credited with identifying and reporting all three flaws in August 2025,
[said](https://www.tenable.com/security/research/tra-2026-01)
an attacker can exploit CVE-2025-69258 by sending a message "0x0a8d" ("SC\_INSTALL\_HANDLER\_REQUEST") to the MsgReceiver.exe component, causing a DLL under their control to be loaded into the binary, resulting in code execution with elevated privileges.

Similarly, CVE-2025-69259 and CVE-2025-69260 can also be triggered by sending a specially crafted message "0x1b5b" ("SC\_CMD\_CGI\_LOG\_REQUEST") to the MsgReceiver.exe process, which listens on the default TCP port 20001.

The issues impact Apex Central on-premise versions below Build 7190. Trend Micro noted that successful exploitation hinges on an attacker already having physical or remote access to a vulnerable endpoint.

"In addition to timely application of patches and updated solutions, customers are also advised to review remote access to critical systems and ensure policies and perimeter security are up-to-date," it added.