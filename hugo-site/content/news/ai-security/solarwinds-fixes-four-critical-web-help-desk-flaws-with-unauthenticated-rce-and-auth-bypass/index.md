---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T10:15:12.586394+00:00'
exported_at: '2026-01-29T10:15:14.838580+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html
structured_data:
  about: []
  author: ''
  description: SolarWinds fixed six Web Help Desk vulnerabilities, including four
    critical flaws that allow unauthenticated remote code execution.
  headline: SolarWinds Fixes Four Critical Web Help Desk Flaws With Unauthenticated
    RCE and Auth Bypass
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: SolarWinds Fixes Four Critical Web Help Desk Flaws With Unauthenticated RCE
  and Auth Bypass
updated_at: '2026-01-29T10:15:12.586394+00:00'
url_hash: aa2428b991cc169f586c67bf240e738ad9a78865
---

**

Ravie Lakshmanan
**

Jan 29, 2026

Vulnerability / Software Security

SolarWinds has
[released](https://www.solarwinds.com/trust-center/security-advisories)
security updates to address multiple security vulnerabilities impacting SolarWinds Web Help Desk, including four critical vulnerabilities that could result in authentication bypass and remote code execution (RCE).

The list of vulnerabilities is as follows -

* **CVE-2025-40536**
  (CVSS score: 8.1) - A security control bypass vulnerability that could allow an unauthenticated attacker to gain access to certain restricted functionality
* **CVE-2025-40537**
  (CVSS score: 7.5) - A hard-coded credentials vulnerability that could allow access to administrative functions using the "client" user account
* **CVE-2025-40551**
  (CVSS score: 9.8) - An untrusted data deserialization vulnerability that could lead to remote code execution, which would allow an unauthenticated attacker to run commands on the host machine
* **CVE-2025-40552**
  (CVSS score: 9.8) - An authentication bypass vulnerability that could allow an unauthenticated attacker to execute actions and methods
* **CVE-2025-40553**
  (CVSS score: 9.8) - An untrusted data deserialization vulnerability that could lead to remote code execution, which would allow an unauthenticated attacker to run commands on the host machine
* **CVE-2025-40554**
  (CVSS score: 9.8) - An authentication bypass vulnerability that could allow an attacker to invoke specific actions within Web Help Desk

While Jimi Sebree from Horizon3.ai has been credited with discovering and reporting the first three vulnerabilities, watchTowr's Piotr Bazydlo has been acknowledged for the remaining three flaws. All the issues have been addressed in
[WHD 2026.1](https://documentation.solarwinds.com/en/success_center/whd/content/release_notes/whd_2026-1_release_notes.htm)
.

"Both CVE-2025-40551 and CVE-2025-40553 are critical deserialization of untrusted data vulnerabilities that allow a remote unauthenticated attacker to achieve RCE on a target system and execute payloads such as arbitrary OS command execution," Rapid7
[said](https://www.rapid7.com/blog/post/etr-multiple-critical-solarwinds-web-help-desk-vulnerabilities-cve-2025-40551-40552-40553-40554/)
.

"RCE via deserialization is a highly reliable vector for attackers to leverage, and as these vulnerabilities are exploitable without authentication, the impact of either of these two vulnerabilities is significant."

While CVE-2025-40552 and CVE-2025-40554 have been described as authentication bypasses, they could also be leveraged to obtain RCE and achieve the same impact as the other two RCE deserialization vulnerabilities, the cybersecurity company added.

In recent years, SolarWinds has released fixes to resolve several flaws in its Web Help Desk software, including
[CVE-2024-28986](https://thehackernews.com/2024/08/solarwinds-releases-patch-for-critical.html)
,
[CVE-2024-28987](https://thehackernews.com/2024/08/hardcoded-credential-vulnerability.html)
,
[CVE-2024-28988, and CVE-2025-26399](https://thehackernews.com/2025/09/solarwinds-releases-hotfix-for-critical.html)
. It's worth noting that CVE-2025-26399 addresses a patch bypass for CVE-2024-28988, which, in turn, is a
[patch bypass](https://www.solarwinds.com/trust-center/security-advisories/cve-2024-28988)
of CVE-2024-28986.

In late 2024, the U.S. Cybersecurity and Infrastructure Security Agency (CISA)
[added](https://thehackernews.com/2024/10/cisa-warns-of-active-exploitation-in.html)
CVE-2024-28986 and CVE-2024-28987 to its Known Exploited Vulnerabilities (KEV) catalog, citing evidence of active exploitation.

In a post explaining CVE-2025-40551, Horizon3.ai's Sebree
[described](https://horizon3.ai/attack-research/cve-2025-40551-another-solarwinds-web-help-desk-deserialization-issue/)
it as yet another deserialization vulnerability stemming from the AjaxProxy functionality that could result in remote code execution. To achieve RCE, an attacker needs to carry out the following series of actions -

* Establish a valid session and extract key values
* Create a LoginPref component
* Set the state of the LoginPref component to allow us to access the file upload
* Use the JSONRPC bridge to create some malicious Java objects behind the scenes
* Trigger these malicious Java objects

With flaws in Web Help Desk having been weaponized in the past, it's essential that customers move quickly to update to the latest version of the help desk and IT service management platform.