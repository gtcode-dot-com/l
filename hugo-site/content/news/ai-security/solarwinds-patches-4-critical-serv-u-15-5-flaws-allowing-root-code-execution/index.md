---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T06:15:15.328726+00:00'
exported_at: '2026-02-26T06:15:18.541515+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/solarwinds-patches-4-critical-serv-u.html
structured_data:
  about: []
  author: ''
  description: SolarWinds fixes four critical CVSS 9.1 vulnerabilities in Serv-U 15.5
    that could allow root code execution with administrative privileges.
  headline: SolarWinds Patches 4 Critical Serv-U 15.5 Flaws Allowing Root Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/solarwinds-patches-4-critical-serv-u.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: SolarWinds Patches 4 Critical Serv-U 15.5 Flaws Allowing Root Code Execution
updated_at: '2026-02-26T06:15:15.328726+00:00'
url_hash: 98f4716b515eeaaf232a94736012a84d2f35b66b
---

**

Ravie Lakshmanan
**

Feb 25, 2026

Vulnerability / Windows Security

SolarWinds has
[released updates](https://documentation.solarwinds.com/en/success_center/servu/content/release_notes/servu_15-5-4_release_notes.htm)
to address four critical security flaws in its Serv-U file transfer software that, if successfully exploited, could result in remote code execution.

The vulnerabilities, all rated 9.1 on the CVSS scoring system, are listed below -

* **[CVE-2025-40538](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40538)**
  - A broken access control vulnerability that allows an attacker to create a system admin user and execute arbitrary code as root via domain admin or group admin privileges.
* **[CVE-2025-40539](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40539)**
  - A type confusion vulnerability that allows an attacker to execute arbitrary native code as root.
* **[CVE-2025-40540](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40540)**
  - A type confusion vulnerability that allows an attacker to execute arbitrary native code as root.
* **[CVE-2025-40541](https://www.solarwinds.com/trust-center/security-advisories/cve-2025-40541)**
  - An insecure direct object reference (IDOR) vulnerability that allows an attacker to execute native code as root.

SolarWinds noted that the vulnerabilities require administrative privileges for successful exploitation. It also said that they carry a medium security risk on Windows deployments as the services "frequently run under less-privileged service accounts by default."

The four shortcomings affect SolarWinds Serv-U version 15.5. They have been addressed in SolarWinds Serv-U version 15.5.4.

While SolarWinds makes no mention of the security flaws being exploited in the wild, prior vulnerabilities in the software (
[CVE-2021-35211](https://thehackernews.com/2021/09/microsoft-says-chinese-hackers-were.html)
,
[CVE-2021-35247](https://thehackernews.com/2022/01/microsoft-hackers-exploiting-new.html)
, and
[CVE-2024-28995](https://thehackernews.com/2024/06/solarwinds-serv-u-vulnerability-under.html)
) have been exploited by malicious actors, including by a China-based hacking group tracked as Storm-0322 (formerly DEV-0322).