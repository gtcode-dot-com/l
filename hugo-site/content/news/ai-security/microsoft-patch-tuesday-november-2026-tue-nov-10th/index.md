---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:49:08.153849+00:00'
exported_at: '2026-11-15T06:49:09.959921+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33508
structured_data:
  about: []
  author: ''
  description: 'Microsoft Patch Tuesday November 2026, Author: Johannes Ullrich'
  headline: Microsoft Patch Tuesday November 2026, (Tue, Nov 10th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33508
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patch Tuesday November 2026, (Tue, Nov 10th)
updated_at: '2026-11-15T06:49:08.153849+00:00'
url_hash: 6da26adf46a9e43c948956ddbd5f1d8de540aa1d
---

# [Microsoft Patch Tuesday November 2026](/forums/diary/Microsoft+Patch+Tuesday+November+2026/33508/)

**Published**
: 2026-11-10.
**Last Updated**
: 2026-11-11 18:28:43 UTC

**by**
[Johannes Ullrich](https://isc.sans.edu/handler_list.html#johannes-ullrich)
(Version: 1)

[6 comment(s)](/diary/Microsoft+Patch+Tuesday+November+2026/33508/#comments)

Microsoft continues its AI-induced patch surge, addressing 1,260 different vulnerabilities this month. 68 of these vulnerabilities are considered critical. 167 of the vulnerabilities are Chromium issues affecting Microsoft Edge.

One of the vulnerabilities, CVE-2026-124194, a spoofing vulnerability in Outlook, is already being exploited.

Other vulnerabilities of note:

* CVE-2026-119958: A critical RCE vulnerability in Microsoft LDAP.
* CVE-2026-109459, CVE-2026-119967, CVE-2026-116710, CVE-2026-119963, CVE-2026-119964: Several critical vulnerabilities in Microsoft Queuing and Queue Manager.
* CVE-2026-113859: Windows TCP/IP Remote Code Execution Vulnerability. CVSS score is only 7.5.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-109475](/vuln.html?cve=2026-109475) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118747](/vuln.html?cve=2026-118747) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-120796](/vuln.html?cve=2026-120796) | No | No | - | - | Important | 5.3 | 4.6 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105544](/vuln.html?cve=2026-105544) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-114155](/vuln.html?cve=2026-114155) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-118746](/vuln.html?cve=2026-118746) | No | No | - | - | Important | 6.8 | 5.9 |
| AMD Zen Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-84004](/vuln.html?cve=2026-84004) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-84005](/vuln.html?cve=2026-84005) | No | No | - | - | Important | 5.5 | 4.8 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-109478](/vuln.html?cve=2026-109478) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-114147](/vuln.html?cve=2026-114147) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-114149](/vuln.html?cve=2026-114149) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-114154](/vuln.html?cve=2026-114154) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118748](/vuln.html?cve=2026-118748) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118749](/vuln.html?cve=2026-118749) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118750](/vuln.html?cve=2026-118750) | No | No | - | - | Important | 7.5 | 6.5 |
| ASP.NET Core Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-109481](/vuln.html?cve=2026-109481) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-114146](/vuln.html?cve=2026-114146) | No | No | - | - | Important | 9.0 | 7.8 |
| [CVE-2026-118741](/vuln.html?cve=2026-118741) | No | No | - | - | Important | 8.1 | 7.1 |
| ASP.NET Core Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-109476](/vuln.html?cve=2026-109476) | No | No | - | - | Important | 6.1 | 5.3 |
| [CVE-2026-114150](/vuln.html?cve=2026-114150) | No | No | - | - | Important | 5.9 | 5.2 |
| ASP.NET Core Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-114156](/vuln.html?cve=2026-114156) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-114157](/vuln.html?cve=2026-114157) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Domain Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118148](/vuln.html?cve=2026-118148) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-118735](/vuln.html?cve=2026-118735) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-123387](/vuln.html?cve=2026-123387) | No | No | - | - | Important | 8.0 | 7.0 |
| ActiveSyncProvider Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119889](/vuln.html?cve=2026-119889) | No | No | - | - | Important | 6.5 | 5.7 |
| Aspire Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-120006](/vuln.html?cve=2026-120006) | No | No | - | - | Important |  |  |
| [CVE-2026-120778](/vuln.html?cve=2026-120778) | No | No | - | - | Important | 7.3 | 6.4 |
| Aspire Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-120792](/vuln.html?cve=2026-120792) | No | No | - | - | Important | 7.3 | 6.4 |
| Aspire Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-118740](/vuln.html?cve=2026-118740) | No | No | - | - | Important | 9.1 | 7.9 |
| Azure CLI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109457](/vuln.html?cve=2026-109457) | No | No | - | - | Important | 8.0 | 7.0 |
| Azure Confidential Clean Rooms Tampering Vulnerability | | | | | | | |
| [CVE-2026-121668](/vuln.html?cve=2026-121668) | No | No | - | - | Important |  |  |
| Azure CycleCloud Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-102224](/vuln.html?cve=2026-102224) | No | No | - | - | Important | 8.4 | 7.3 |
| [CVE-2026-113822](/vuln.html?cve=2026-113822) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-114161](/vuln.html?cve=2026-114161) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure CycleCloud Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-113823](/vuln.html?cve=2026-113823) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure DevOps Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-120783](/vuln.html?cve=2026-120783) | No | No | - | - | Important | 6.4 | 5.8 |
| [CVE-2026-85923](/vuln.html?cve=2026-85923) | No | No | - | - | Important | 8.8 | 7.7 |
| Azure DevOps Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112745](/vuln.html?cve=2026-112745) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure DevOps Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109467](/vuln.html?cve=2026-109467) | No | No | - | - | Important | 9.9 | 8.6 |
| Azure Firmware Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-109462](/vuln.html?cve=2026-109462) | No | No | - | - | Important | 4.4 | 3.9 |
| Azure Front Door Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118742](/vuln.html?cve=2026-118742) | No | No | - | - | Important | 8.6 | 7.5 |
| Azure Local Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105734](/vuln.html?cve=2026-105734) | No | No | - | - | Important | 7.0 | 6.1 |
| Azure Managed Grafana Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-114160](/vuln.html?cve=2026-114160) | No | No | - | - | Critical |  |  |
| Azure NFS mount helper (aznfs) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105494](/vuln.html?cve=2026-105494) | No | No | - | - | Important |  |  |
| Azure OpenAI Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119990](/vuln.html?cve=2026-119990) | No | No | - | - | Critical | 9.8 | 8.5 |
| Azure Pipelines Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119989](/vuln.html?cve=2026-119989) | No | No | - | - | Important | 8.2 | 7.1 |
| Chromium CVE-2026-118309: Incorrect reference resolution | | | | | | | |
| [CVE-2026-118309](/vuln.html?cve=2026-118309) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-118314: Incorrect reference resolution | | | | | | | |
| [CVE-2026-118314](/vuln.html?cve=2026-118314) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-118321: Use after free | | | | | | | |
| [CVE-2026-118321](/vuln.html?cve=2026-118321) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-119260: Use after free | | | | | | | |
| [CVE-2026-119260](/vuln.html?cve=2026-119260) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119261: Improper input validation | | | | | | | |
| [CVE-2026-119261](/vuln.html?cve=2026-119261) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-119262: Improper input validation | | | | | | | |
| [CVE-2026-119262](/vuln.html?cve=2026-119262) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119263: Memory corruption | | | | | | | |
| [CVE-2026-119263](/vuln.html?cve=2026-119263) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-119264: Memory corruption | | | | | | | |
| [CVE-2026-119264](/vuln.html?cve=2026-119264) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119265: Memory corruption | | | | | | | |
| [CVE-2026-119265](/vuln.html?cve=2026-119265) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119266: Use after free | | | | | | | |
| [CVE-2026-119266](/vuln.html?cve=2026-119266) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119267: Memory corruption | | | | | | | |
| [CVE-2026-119267](/vuln.html?cve=2026-119267) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119268: Integer overflow | | | | | | | |
| [CVE-2026-119268](/vuln.html?cve=2026-119268) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119269: Use after free | | | | | | | |
| [CVE-2026-119269](/vuln.html?cve=2026-119269) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119270: Improper input validation | | | | | | | |
| [CVE-2026-119270](/vuln.html?cve=2026-119270) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119271: Use after free | | | | | | | |
| [CVE-2026-119271](/vuln.html?cve=2026-119271) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-119272: Out of bounds read | | | | | | | |
| [CVE-2026-119272](/vuln.html?cve=2026-119272) | No | No | - | - | Moderate | 4.3 | 4.3 |
| Chromium CVE-2026-120930: Incorrect authorization | | | | | | | |
| [CVE-2026-120930](/vuln.html?cve=2026-120930) | No | No | - | - | Important | 5.4 | 5.4 |
| Chromium CVE-2026-121029: Incorrect authorization | | | | | | | |
| [CVE-2026-121029](/vuln.html?cve=2026-121029) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121030: Incorrect authorization | | | | | | | |
| [CVE-2026-121030](/vuln.html?cve=2026-121030) | No | No | - | - | Moderate | 9.6 | 9.6 |
| Chromium CVE-2026-121031: Missing authorization | | | | | | | |
| [CVE-2026-121031](/vuln.html?cve=2026-121031) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121032: Out of bounds read | | | | | | | |
| [CVE-2026-121032](/vuln.html?cve=2026-121032) | No | No | - | - | Important |  |  |
| Chromium CVE-2026-121034: Use after free | | | | | | | |
| [CVE-2026-121034](/vuln.html?cve=2026-121034) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121035: Use after free | | | | | | | |
| [CVE-2026-121035](/vuln.html?cve=2026-121035) | No | No | - | - | Critical | 9.6 | 9.6 |
| Chromium CVE-2026-121036: Use after free | | | | | | | |
| [CVE-2026-121036](/vuln.html?cve=2026-121036) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121037: Out of bounds write | | | | | | | |
| [CVE-2026-121037](/vuln.html?cve=2026-121037) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121038: Information leak | | | | | | | |
| [CVE-2026-121038](/vuln.html?cve=2026-121038) | No | No | - | - | Important | 6.5 | 6.5 |
| Chromium CVE-2026-121039: Incorrect authorization | | | | | | | |
| [CVE-2026-121039](/vuln.html?cve=2026-121039) | No | No | - | - | Moderate | 5.3 | 5.3 |
| Chromium CVE-2026-121050: Race condition | | | | | | | |
| [CVE-2026-121050](/vuln.html?cve=2026-121050) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121078: Type confusion | | | | | | | |
| [CVE-2026-121078](/vuln.html?cve=2026-121078) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121079: Race condition | | | | | | | |
| [CVE-2026-121079](/vuln.html?cve=2026-121079) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121080: Use after free | | | | | | | |
| [CVE-2026-121080](/vuln.html?cve=2026-121080) | No | No | - | - | Important | 4.3 | 4.3 |
| Chromium CVE-2026-121081: UI misrepresentation | | | | | | | |
| [CVE-2026-121081](/vuln.html?cve=2026-121081) | No | No | - | - | Low | 5.9 | 5.9 |
| Chromium CVE-2026-121082: Type confusion | | | | | | | |
| [CVE-2026-121082](/vuln.html?cve=2026-121082) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121083: Use after free | | | | | | | |
| [CVE-2026-121083](/vuln.html?cve=2026-121083) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121084: Out of bounds read | | | | | | | |
| [CVE-2026-121084](/vuln.html?cve=2026-121084) | No | No | - | - | Important | 8.3 | 8.3 |
| Chromium CVE-2026-121085: Incorrect authorization | | | | | | | |
| [CVE-2026-121085](/vuln.html?cve=2026-121085) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121086: Buffer overflow | | | | | | | |
| [CVE-2026-121086](/vuln.html?cve=2026-121086) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121087: Improper input validation | | | | | | | |
| [CVE-2026-121087](/vuln.html?cve=2026-121087) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121088: Missing authorization | | | | | | | |
| [CVE-2026-121088](/vuln.html?cve=2026-121088) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121089: Use after free | | | | | | | |
| [CVE-2026-121089](/vuln.html?cve=2026-121089) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121091: Incorrect authorization | | | | | | | |
| [CVE-2026-121091](/vuln.html?cve=2026-121091) | No | No | - | - | Moderate | 5.3 | 5.3 |
| Chromium CVE-2026-121092: Uncontrolled recursion | | | | | | | |
| [CVE-2026-121092](/vuln.html?cve=2026-121092) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121093: Out of bounds read | | | | | | | |
| [CVE-2026-121093](/vuln.html?cve=2026-121093) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121094: Type confusion | | | | | | | |
| [CVE-2026-121094](/vuln.html?cve=2026-121094) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121095: Uninitialized resource | | | | | | | |
| [CVE-2026-121095](/vuln.html?cve=2026-121095) | No | No | - | - | Important |  |  |
| Chromium CVE-2026-121096: Incomplete cleanup | | | | | | | |
| [CVE-2026-121096](/vuln.html?cve=2026-121096) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121097: Use after free | | | | | | | |
| [CVE-2026-121097](/vuln.html?cve=2026-121097) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121098: Improper state validation | | | | | | | |
| [CVE-2026-121098](/vuln.html?cve=2026-121098) | No | No | - | - | Important | 8.3 | 8.3 |
| Chromium CVE-2026-121099: Information leak | | | | | | | |
| [CVE-2026-121099](/vuln.html?cve=2026-121099) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121100: Use after free | | | | | | | |
| [CVE-2026-121100](/vuln.html?cve=2026-121100) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121101: Missing authorization | | | | | | | |
| [CVE-2026-121101](/vuln.html?cve=2026-121101) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121102: Missing authorization | | | | | | | |
| [CVE-2026-121102](/vuln.html?cve=2026-121102) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121103: Incorrect authorization | | | | | | | |
| [CVE-2026-121103](/vuln.html?cve=2026-121103) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121104: Incorrect authorization | | | | | | | |
| [CVE-2026-121104](/vuln.html?cve=2026-121104) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121105: Information leak | | | | | | | |
| [CVE-2026-121105](/vuln.html?cve=2026-121105) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121107: Incorrect authorization | | | | | | | |
| [CVE-2026-121107](/vuln.html?cve=2026-121107) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121108: Confused deputy | | | | | | | |
| [CVE-2026-121108](/vuln.html?cve=2026-121108) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121109: Inadequate encryption strength | | | | | | | |
| [CVE-2026-121109](/vuln.html?cve=2026-121109) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121111: Incorrect authorization | | | | | | | |
| [CVE-2026-121111](/vuln.html?cve=2026-121111) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121113: Buffer overflow | | | | | | | |
| [CVE-2026-121113](/vuln.html?cve=2026-121113) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121114: Use after free | | | | | | | |
| [CVE-2026-121114](/vuln.html?cve=2026-121114) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121115: Improper input validation | | | | | | | |
| [CVE-2026-121115](/vuln.html?cve=2026-121115) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121117: Use after free | | | | | | | |
| [CVE-2026-121117](/vuln.html?cve=2026-121117) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121118: Use after free | | | | | | | |
| [CVE-2026-121118](/vuln.html?cve=2026-121118) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121119: Use after free | | | | | | | |
| [CVE-2026-121119](/vuln.html?cve=2026-121119) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121120: Improper input validation | | | | | | | |
| [CVE-2026-121120](/vuln.html?cve=2026-121120) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121121: UI misrepresentation | | | | | | | |
| [CVE-2026-121121](/vuln.html?cve=2026-121121) | No | No | - | - | Low | 5.4 | 5.4 |
| Chromium CVE-2026-121122: UI misrepresentation | | | | | | | |
| [CVE-2026-121122](/vuln.html?cve=2026-121122) | No | No | - | - | Moderate | 5.4 | 5.4 |
| Chromium CVE-2026-121123: Use after free | | | | | | | |
| [CVE-2026-121123](/vuln.html?cve=2026-121123) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121124: Improper adherence to coding standards | | | | | | | |
| [CVE-2026-121124](/vuln.html?cve=2026-121124) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121125: Information leak | | | | | | | |
| [CVE-2026-121125](/vuln.html?cve=2026-121125) | No | No | - | - | Low | 5.3 | 5.3 |
| Chromium CVE-2026-121126: Use after free | | | | | | | |
| [CVE-2026-121126](/vuln.html?cve=2026-121126) | No | No | - | - | Critical | 9.6 | 9.6 |
| Chromium CVE-2026-121127: Use after free | | | | | | | |
| [CVE-2026-121127](/vuln.html?cve=2026-121127) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121128: Use after free | | | | | | | |
| [CVE-2026-121128](/vuln.html?cve=2026-121128) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121129: Use after free | | | | | | | |
| [CVE-2026-121129](/vuln.html?cve=2026-121129) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121130: Observable discrepancy | | | | | | | |
| [CVE-2026-121130](/vuln.html?cve=2026-121130) | No | No | - | - | Low | 5.3 | 5.3 |
| Chromium CVE-2026-121131: Use after free | | | | | | | |
| [CVE-2026-121131](/vuln.html?cve=2026-121131) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121132: Information leak | | | | | | | |
| [CVE-2026-121132](/vuln.html?cve=2026-121132) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121133: Incorrect reference resolution | | | | | | | |
| [CVE-2026-121133](/vuln.html?cve=2026-121133) | No | No | - | - | Important | 8.1 | 8.1 |
| Chromium CVE-2026-121134: Information loss | | | | | | | |
| [CVE-2026-121134](/vuln.html?cve=2026-121134) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121135: Security issue | | | | | | | |
| [CVE-2026-121135](/vuln.html?cve=2026-121135) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121136: Missing authorization | | | | | | | |
| [CVE-2026-121136](/vuln.html?cve=2026-121136) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121137: Type confusion | | | | | | | |
| [CVE-2026-121137](/vuln.html?cve=2026-121137) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121138: Observable discrepancy | | | | | | | |
| [CVE-2026-121138](/vuln.html?cve=2026-121138) | No | No | - | - | Low | 6.5 | 6.5 |
| Chromium CVE-2026-121174: Missing authorization | | | | | | | |
| [CVE-2026-121174](/vuln.html?cve=2026-121174) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121175: Improper resource exposure | | | | | | | |
| [CVE-2026-121175](/vuln.html?cve=2026-121175) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121176: Uninitialized resource | | | | | | | |
| [CVE-2026-121176](/vuln.html?cve=2026-121176) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121178: Use after free | | | | | | | |
| [CVE-2026-121178](/vuln.html?cve=2026-121178) | No | No | - | - | Important | 8.3 | 8.3 |
| Chromium CVE-2026-121179: Use after free | | | | | | | |
| [CVE-2026-121179](/vuln.html?cve=2026-121179) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121180: Buffer overflow | | | | | | | |
| [CVE-2026-121180](/vuln.html?cve=2026-121180) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121181: Use after free | | | | | | | |
| [CVE-2026-121181](/vuln.html?cve=2026-121181) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121182: Use after free | | | | | | | |
| [CVE-2026-121182](/vuln.html?cve=2026-121182) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121183: Incorrect authorization | | | | | | | |
| [CVE-2026-121183](/vuln.html?cve=2026-121183) | No | No | - | - | Moderate | 8.3 | 8.3 |
| Chromium CVE-2026-121184: Out of bounds read | | | | | | | |
| [CVE-2026-121184](/vuln.html?cve=2026-121184) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121185: Use after free | | | | | | | |
| [CVE-2026-121185](/vuln.html?cve=2026-121185) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121187: Observable discrepancy | | | | | | | |
| [CVE-2026-121187](/vuln.html?cve=2026-121187) | No | No | - | - | Moderate | 5.3 | 5.3 |
| Chromium CVE-2026-121188: Use after free | | | | | | | |
| [CVE-2026-121188](/vuln.html?cve=2026-121188) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121189: Use after free | | | | | | | |
| [CVE-2026-121189](/vuln.html?cve=2026-121189) | No | No | - | - | Low | 9.6 | 9.6 |
| Chromium CVE-2026-121190: UI misrepresentation | | | | | | | |
| [CVE-2026-121190](/vuln.html?cve=2026-121190) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121193: Incorrect authorization | | | | | | | |
| [CVE-2026-121193](/vuln.html?cve=2026-121193) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121194: Missing authorization | | | | | | | |
| [CVE-2026-121194](/vuln.html?cve=2026-121194) | No | No | - | - | Moderate | 5.3 | 5.3 |
| Chromium CVE-2026-121195: Incorrect authorization | | | | | | | |
| [CVE-2026-121195](/vuln.html?cve=2026-121195) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121197: Out of bounds read | | | | | | | |
| [CVE-2026-121197](/vuln.html?cve=2026-121197) | No | No | - | - | Important |  |  |
| Chromium CVE-2026-121198: Confused deputy | | | | | | | |
| [CVE-2026-121198](/vuln.html?cve=2026-121198) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121199: Missing authorization | | | | | | | |
| [CVE-2026-121199](/vuln.html?cve=2026-121199) | No | No | - | - | Moderate | 5.5 | 5.5 |
| Chromium CVE-2026-121200: Incorrect reference resolution | | | | | | | |
| [CVE-2026-121200](/vuln.html?cve=2026-121200) | No | No | - | - | Moderate | 9.6 | 9.6 |
| Chromium CVE-2026-121201: Use after free | | | | | | | |
| [CVE-2026-121201](/vuln.html?cve=2026-121201) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121202: Use after free | | | | | | | |
| [CVE-2026-121202](/vuln.html?cve=2026-121202) | No | No | - | - | Moderate | 9.6 | 9.6 |
| Chromium CVE-2026-121203: Use after free | | | | | | | |
| [CVE-2026-121203](/vuln.html?cve=2026-121203) | No | No | - | - | Critical | 8.8 | 8.8 |
| Chromium CVE-2026-121204: Incomplete cleanup | | | | | | | |
| [CVE-2026-121204](/vuln.html?cve=2026-121204) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121205: Incorrect authorization | | | | | | | |
| [CVE-2026-121205](/vuln.html?cve=2026-121205) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121206: UI misrepresentation | | | | | | | |
| [CVE-2026-121206](/vuln.html?cve=2026-121206) | No | No | - | - | Low | 5.4 | 5.4 |
| Chromium CVE-2026-121207: Uninitialized resource | | | | | | | |
| [CVE-2026-121207](/vuln.html?cve=2026-121207) | No | No | - | - | Important |  |  |
| Chromium CVE-2026-121208: Out of bounds read | | | | | | | |
| [CVE-2026-121208](/vuln.html?cve=2026-121208) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121209: UI misrepresentation | | | | | | | |
| [CVE-2026-121209](/vuln.html?cve=2026-121209) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121210: Type confusion | | | | | | | |
| [CVE-2026-121210](/vuln.html?cve=2026-121210) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121211: Use after free | | | | | | | |
| [CVE-2026-121211](/vuln.html?cve=2026-121211) | No | No | - | - | Important | 8.3 | 8.3 |
| Chromium CVE-2026-121212: Incorrect authorization | | | | | | | |
| [CVE-2026-121212](/vuln.html?cve=2026-121212) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121213: Uninitialized resource | | | | | | | |
| [CVE-2026-121213](/vuln.html?cve=2026-121213) | No | No | - | - | Important | 6.5 | 6.5 |
| Chromium CVE-2026-121214: Use after free | | | | | | | |
| [CVE-2026-121214](/vuln.html?cve=2026-121214) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121215: UI misrepresentation | | | | | | | |
| [CVE-2026-121215](/vuln.html?cve=2026-121215) | No | No | - | - | Moderate | 5.4 | 5.4 |
| Chromium CVE-2026-121216: UI misrepresentation | | | | | | | |
| [CVE-2026-121216](/vuln.html?cve=2026-121216) | No | No | - | - | Moderate | 5.4 | 5.4 |
| Chromium CVE-2026-121217: Use after free | | | | | | | |
| [CVE-2026-121217](/vuln.html?cve=2026-121217) | No | No | - | - | Low | 7.5 | 7.5 |
| Chromium CVE-2026-121218: Type confusion | | | | | | | |
| [CVE-2026-121218](/vuln.html?cve=2026-121218) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121219: Integer overflow | | | | | | | |
| [CVE-2026-121219](/vuln.html?cve=2026-121219) | No | No | - | - | Moderate | 8.3 | 8.3 |
| Chromium CVE-2026-121220: Incorrect authorization | | | | | | | |
| [CVE-2026-121220](/vuln.html?cve=2026-121220) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121221: Type confusion | | | | | | | |
| [CVE-2026-121221](/vuln.html?cve=2026-121221) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121222: Incorrect authorization | | | | | | | |
| [CVE-2026-121222](/vuln.html?cve=2026-121222) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121223: Observable discrepancy | | | | | | | |
| [CVE-2026-121223](/vuln.html?cve=2026-121223) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121224: Security issue | | | | | | | |
| [CVE-2026-121224](/vuln.html?cve=2026-121224) | No | No | - | - | Important | 8.1 | 8.1 |
| Chromium CVE-2026-121226: Type confusion | | | | | | | |
| [CVE-2026-121226](/vuln.html?cve=2026-121226) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121227: Uninitialized resource | | | | | | | |
| [CVE-2026-121227](/vuln.html?cve=2026-121227) | No | No | - | - | Important |  |  |
| Chromium CVE-2026-121228: Type confusion | | | | | | | |
| [CVE-2026-121228](/vuln.html?cve=2026-121228) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121230: Race condition | | | | | | | |
| [CVE-2026-121230](/vuln.html?cve=2026-121230) | No | No | - | - | Low | 8.3 | 8.3 |
| Chromium CVE-2026-121231: Incorrect authorization | | | | | | | |
| [CVE-2026-121231](/vuln.html?cve=2026-121231) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121232: Incorrect authorization | | | | | | | |
| [CVE-2026-121232](/vuln.html?cve=2026-121232) | No | No | - | - | Low | 5.1 | 5.1 |
| Chromium CVE-2026-121233: Type confusion | | | | | | | |
| [CVE-2026-121233](/vuln.html?cve=2026-121233) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-121235: Information leak | | | | | | | |
| [CVE-2026-121235](/vuln.html?cve=2026-121235) | No | No | - | - | Low | 6.5 | 6.5 |
| Chromium CVE-2026-121236: Improper input validation | | | | | | | |
| [CVE-2026-121236](/vuln.html?cve=2026-121236) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121237: Improper state validation | | | | | | | |
| [CVE-2026-121237](/vuln.html?cve=2026-121237) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121238: Use after free | | | | | | | |
| [CVE-2026-121238](/vuln.html?cve=2026-121238) | No | No | - | - | Moderate | 8.8 | 8.8 |
| Chromium CVE-2026-121239: Information leak | | | | | | | |
| [CVE-2026-121239](/vuln.html?cve=2026-121239) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121240: Improper input validation | | | | | | | |
| [CVE-2026-121240](/vuln.html?cve=2026-121240) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121242: Improper input validation | | | | | | | |
| [CVE-2026-121242](/vuln.html?cve=2026-121242) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121243: Information leak | | | | | | | |
| [CVE-2026-121243](/vuln.html?cve=2026-121243) | No | No | - | - | Low | 6.5 | 6.5 |
| Chromium CVE-2026-121244: UI misrepresentation | | | | | | | |
| [CVE-2026-121244](/vuln.html?cve=2026-121244) | No | No | - | - | Moderate | 5.4 | 5.4 |
| Chromium CVE-2026-121245: Race condition | | | | | | | |
| [CVE-2026-121245](/vuln.html?cve=2026-121245) | No | No | - | - | Moderate | 5.3 | 5.3 |
| Chromium CVE-2026-121248: Incorrect authorization | | | | | | | |
| [CVE-2026-121248](/vuln.html?cve=2026-121248) | No | No | - | - | Moderate |  |  |
| Chromium CVE-2026-121249: Buffer overflow | | | | | | | |
| [CVE-2026-121249](/vuln.html?cve=2026-121249) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121250: Use after free | | | | | | | |
| [CVE-2026-121250](/vuln.html?cve=2026-121250) | No | No | - | - | Important | 9.6 | 9.6 |
| Chromium CVE-2026-121251: Missing authorization | | | | | | | |
| [CVE-2026-121251](/vuln.html?cve=2026-121251) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121252: Incorrect authorization | | | | | | | |
| [CVE-2026-121252](/vuln.html?cve=2026-121252) | No | No | - | - | Low | 8.8 | 8.8 |
| Chromium CVE-2026-121253: Missing authorization | | | | | | | |
| [CVE-2026-121253](/vuln.html?cve=2026-121253) | No | No | - | - | Low |  |  |
| Chromium CVE-2026-121254: Information leak | | | | | | | |
| [CVE-2026-121254](/vuln.html?cve=2026-121254) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121255: Incorrect authorization | | | | | | | |
| [CVE-2026-121255](/vuln.html?cve=2026-121255) | No | No | - | - | Moderate | 6.5 | 6.5 |
| Chromium CVE-2026-121256: Use of released resource | | | | | | | |
| [CVE-2026-121256](/vuln.html?cve=2026-121256) | No | No | - | - | Moderate | 8.3 | 8.3 |
| Chromium CVE-2026-121257: Use after free | | | | | | | |
| [CVE-2026-121257](/vuln.html?cve=2026-121257) | No | No | - | - | Moderate | 9.6 | 9.6 |
| Chromium CVE-2026-76024: Memory corruption | | | | | | | |
| [CVE-2026-76024](/vuln.html?cve=2026-76024) | No | No | - | - | Critical | 6.5 | 6.5 |
| Chromium CVE-2026-76025: Use after free | | | | | | | |
| [CVE-2026-76025](/vuln.html?cve=2026-76025) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-76026: Memory corruption | | | | | | | |
| [CVE-2026-76026](/vuln.html?cve=2026-76026) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-76027: Memory corruption | | | | | | | |
| [CVE-2026-76027](/vuln.html?cve=2026-76027) | No | No | - | - | Important | 4.3 | 4.3 |
| Chromium CVE-2026-76028: Use after free | | | | | | | |
| [CVE-2026-76028](/vuln.html?cve=2026-76028) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-76029: Memory corruption | | | | | | | |
| [CVE-2026-76029](/vuln.html?cve=2026-76029) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-76030: Memory corruption | | | | | | | |
| [CVE-2026-76030](/vuln.html?cve=2026-76030) | No | No | - | - | Important | 8.8 | 8.8 |
| Chromium CVE-2026-76031: Use after free | | | | | | | |
| [CVE-2026-76031](/vuln.html?cve=2026-76031) | No | No | - | - | Important | 8.8 | 8.8 |
| Connected Devices Platform Service (Cdpsvc) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96007](/vuln.html?cve=2026-96007) | No | No | - | - | Important | 7.0 | 6.1 |
| Data Deduplication Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-119883](/vuln.html?cve=2026-119883) | No | No | - | - | Important | 3.3 | 2.9 |
| Data Sharing Service Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95963](/vuln.html?cve=2026-95963) | No | No | - | - | Important | 7.8 | 6.8 |
| Desktop Window Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105528](/vuln.html?cve=2026-105528) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105581](/vuln.html?cve=2026-105581) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-113819](/vuln.html?cve=2026-113819) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96103](/vuln.html?cve=2026-96103) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96172](/vuln.html?cve=2026-96172) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96174](/vuln.html?cve=2026-96174) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96175](/vuln.html?cve=2026-96175) | No | No | - | - | Important | 7.8 | 6.8 |
| DirectX Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-94507](/vuln.html?cve=2026-94507) | No | No | - | - | Important | 7.8 | 6.8 |
| Entra Device Registration Elevation of Privilege Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-109469](/vuln.html?cve=2026-109469) | No | No | - | - | Critical | 10.0 | 8.7 |
| GitHub Copilot for Jetbrains Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-83953](/vuln.html?cve=2026-83953) | No | No | - | - | Important | 5.5 | 4.8 |
| Graphic Fonts Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96084](/vuln.html?cve=2026-96084) | No | No | - | - | Important | 7.8 | 6.8 |
| Graphic Fonts Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-88211](/vuln.html?cve=2026-88211) | No | No | - | - | Important | 5.7 | 5.0 |
| Graphic Fonts Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119969](/vuln.html?cve=2026-119969) | No | No | - | - | Critical | 8.8 | 7.7 |
| HEIF Image Extensions Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-100204](/vuln.html?cve=2026-100204) | No | No | - | - | Important | 7.0 | 6.1 |
| HEVC Video Extensions Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-114164](/vuln.html?cve=2026-114164) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-114165](/vuln.html?cve=2026-114165) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-114167](/vuln.html?cve=2026-114167) | No | No | - | - | Important | 7.8 | 6.8 |
| HID Parser Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122173](/vuln.html?cve=2026-122173) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-125135](/vuln.html?cve=2026-125135) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-96010](/vuln.html?cve=2026-96010) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96974](/vuln.html?cve=2026-96974) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-96979](/vuln.html?cve=2026-96979) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-96982](/vuln.html?cve=2026-96982) | No | No | - | - | Important | 6.8 | 5.9 |
| HID class driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96059](/vuln.html?cve=2026-96059) | No | No | - | - | Important | 5.5 | 4.8 |
| HTTP.sys Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119942](/vuln.html?cve=2026-119942) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-119946](/vuln.html?cve=2026-119946) | No | No | - | - | Important | 5.9 | 5.2 |
| JDBC Driver for SQL Server Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-70003](/vuln.html?cve=2026-70003) | No | No | - | - | Important | 8.7 | 7.6 |
| Kernel Streaming Service Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119937](/vuln.html?cve=2026-119937) | No | No | - | - | Important | 6.6 | 5.8 |
| Mailslot File System Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105537](/vuln.html?cve=2026-105537) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft 365 Agents SDK Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-109485](/vuln.html?cve=2026-109485) | No | No | - | - | Important | 6.3 | 5.5 |
| Microsoft Account Tampering Vulnerability | | | | | | | |
| [CVE-2026-112974](/vuln.html?cve=2026-112974) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-112982](/vuln.html?cve=2026-112982) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft ActiveX Installer Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96158](/vuln.html?cve=2026-96158) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Authentication Library (MSAL) for Node.js Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108470](/vuln.html?cve=2026-108470) | No | No | - | - | Important |  |  |
| Microsoft Authentication Library for JavaScript Spoofing Vulnerability | | | | | | | |
| [CVE-2026-108469](/vuln.html?cve=2026-108469) | No | No | - | - | Important | 6.8 | 5.9 |
| Microsoft Azure File Sync Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118288](/vuln.html?cve=2026-118288) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Azure Kubernetes Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122986](/vuln.html?cve=2026-122986) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Bluetooth Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-70120](/vuln.html?cve=2026-70120) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-85929](/vuln.html?cve=2026-85929) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Color Management Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-96054](/vuln.html?cve=2026-96054) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96067](/vuln.html?cve=2026-96067) | No | No | - | - | Important | 9.8 | 8.5 |
| [CVE-2026-96078](/vuln.html?cve=2026-96078) | No | No | - | - | Important | 9.8 | 8.5 |
| Microsoft Configuration Manager Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119991](/vuln.html?cve=2026-119991) | No | No | - | - | Important | 5.9 | 5.2 |
| Microsoft Defender Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-122194](/vuln.html?cve=2026-122194) | No | No | - | - | Critical | 8.8 | 7.7 |
| Microsoft DirectMusic Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-95882](/vuln.html?cve=2026-95882) | No | No | - | - | Important | 9.8 | 8.5 |
| [CVE-2026-95891](/vuln.html?cve=2026-95891) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95896](/vuln.html?cve=2026-95896) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95901](/vuln.html?cve=2026-95901) | No | No | - | - | Important | 9.8 | 8.5 |
| Microsoft Dynamics 365 (on-premises) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-122196](/vuln.html?cve=2026-122196) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Edge (Chromium-based) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-122518](/vuln.html?cve=2026-122518) | No | No | - | - | Moderate | 6.5 | 5.7 |
| Microsoft Entra Private Network Connector Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-109460](/vuln.html?cve=2026-109460) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Exchange Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-118153](/vuln.html?cve=2026-118153) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118150](/vuln.html?cve=2026-118150) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118151](/vuln.html?cve=2026-118151) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-118154](/vuln.html?cve=2026-118154) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118157](/vuln.html?cve=2026-118157) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft Exchange Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-118149](/vuln.html?cve=2026-118149) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118207](/vuln.html?cve=2026-118207) | No | No | - | - | Critical | 8.8 | 7.7 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-118152](/vuln.html?cve=2026-118152) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118208](/vuln.html?cve=2026-118208) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft Graph Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-114162](/vuln.html?cve=2026-114162) | No | No | - | - | Important | 9.1 | 7.9 |
| Microsoft Graphics Component Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112754](/vuln.html?cve=2026-112754) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft High Performance Computing (HPC) Pack Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122987](/vuln.html?cve=2026-122987) | No | No | - | - | Important | 5.9 | 5.2 |
| Microsoft Input Method Editor (IME) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105505](/vuln.html?cve=2026-105505) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft JScript Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105578](/vuln.html?cve=2026-105578) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft MCP Gateway Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-109492](/vuln.html?cve=2026-109492) | No | No | - | - | Important |  |  |
| Microsoft ODBC Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-108411](/vuln.html?cve=2026-108411) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Access Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109493](/vuln.html?cve=2026-109493) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109498](/vuln.html?cve=2026-109498) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-110058](/vuln.html?cve=2026-110058) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110059](/vuln.html?cve=2026-110059) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110060](/vuln.html?cve=2026-110060) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111301](/vuln.html?cve=2026-111301) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111305](/vuln.html?cve=2026-111305) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Excel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118715](/vuln.html?cve=2026-118715) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118725](/vuln.html?cve=2026-118725) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-111292](/vuln.html?cve=2026-111292) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118300](/vuln.html?cve=2026-118300) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118727](/vuln.html?cve=2026-118727) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118728](/vuln.html?cve=2026-118728) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-119999](/vuln.html?cve=2026-119999) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-123395](/vuln.html?cve=2026-123395) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-124178](/vuln.html?cve=2026-124178) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-124179](/vuln.html?cve=2026-124179) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-124183](/vuln.html?cve=2026-124183) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116927](/vuln.html?cve=2026-116927) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118292](/vuln.html?cve=2026-118292) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118293](/vuln.html?cve=2026-118293) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118294](/vuln.html?cve=2026-118294) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118295](/vuln.html?cve=2026-118295) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118296](/vuln.html?cve=2026-118296) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118297](/vuln.html?cve=2026-118297) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118298](/vuln.html?cve=2026-118298) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118299](/vuln.html?cve=2026-118299) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118301](/vuln.html?cve=2026-118301) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118302](/vuln.html?cve=2026-118302) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118700](/vuln.html?cve=2026-118700) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118701](/vuln.html?cve=2026-118701) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118702](/vuln.html?cve=2026-118702) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118703](/vuln.html?cve=2026-118703) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118704](/vuln.html?cve=2026-118704) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118705](/vuln.html?cve=2026-118705) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118706](/vuln.html?cve=2026-118706) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118707](/vuln.html?cve=2026-118707) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118708](/vuln.html?cve=2026-118708) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118709](/vuln.html?cve=2026-118709) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118710](/vuln.html?cve=2026-118710) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118711](/vuln.html?cve=2026-118711) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118712](/vuln.html?cve=2026-118712) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118713](/vuln.html?cve=2026-118713) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118714](/vuln.html?cve=2026-118714) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118716](/vuln.html?cve=2026-118716) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118717](/vuln.html?cve=2026-118717) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118718](/vuln.html?cve=2026-118718) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118719](/vuln.html?cve=2026-118719) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118720](/vuln.html?cve=2026-118720) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118721](/vuln.html?cve=2026-118721) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118722](/vuln.html?cve=2026-118722) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118723](/vuln.html?cve=2026-118723) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118724](/vuln.html?cve=2026-118724) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118726](/vuln.html?cve=2026-118726) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118729](/vuln.html?cve=2026-118729) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118730](/vuln.html?cve=2026-118730) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-118731](/vuln.html?cve=2026-118731) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118732](/vuln.html?cve=2026-118732) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119986](/vuln.html?cve=2026-119986) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120785](/vuln.html?cve=2026-120785) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120786](/vuln.html?cve=2026-120786) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-120788](/vuln.html?cve=2026-120788) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-120789](/vuln.html?cve=2026-120789) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-120790](/vuln.html?cve=2026-120790) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120791](/vuln.html?cve=2026-120791) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123385](/vuln.html?cve=2026-123385) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124170](/vuln.html?cve=2026-124170) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-124174](/vuln.html?cve=2026-124174) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124176](/vuln.html?cve=2026-124176) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124187](/vuln.html?cve=2026-124187) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124229](/vuln.html?cve=2026-124229) | No | No | - | - | Important | 6.6 | 5.8 |
| Microsoft Office Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-111291](/vuln.html?cve=2026-111291) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-111293](/vuln.html?cve=2026-111293) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-112731](/vuln.html?cve=2026-112731) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office Outlook Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119993](/vuln.html?cve=2026-119993) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office Outlook Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-110043](/vuln.html?cve=2026-110043) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-110068](/vuln.html?cve=2026-110068) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-111309](/vuln.html?cve=2026-111309) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-119995](/vuln.html?cve=2026-119995) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119996](/vuln.html?cve=2026-119996) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119997](/vuln.html?cve=2026-119997) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-123375](/vuln.html?cve=2026-123375) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123376](/vuln.html?cve=2026-123376) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123377](/vuln.html?cve=2026-123377) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123378](/vuln.html?cve=2026-123378) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-123379](/vuln.html?cve=2026-123379) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-123380](/vuln.html?cve=2026-123380) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123381](/vuln.html?cve=2026-123381) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123382](/vuln.html?cve=2026-123382) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123383](/vuln.html?cve=2026-123383) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123384](/vuln.html?cve=2026-123384) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124227](/vuln.html?cve=2026-124227) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-124228](/vuln.html?cve=2026-124228) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office PowerPoint Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112738](/vuln.html?cve=2026-112738) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-116922](/vuln.html?cve=2026-116922) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office PowerPoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-112734](/vuln.html?cve=2026-112734) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112737](/vuln.html?cve=2026-112737) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120001](/vuln.html?cve=2026-120001) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-111286](/vuln.html?cve=2026-111286) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-111289](/vuln.html?cve=2026-111289) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-116717](/vuln.html?cve=2026-116717) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120003](/vuln.html?cve=2026-120003) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-122198](/vuln.html?cve=2026-122198) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-119998](/vuln.html?cve=2026-119998) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office SharePoint Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-109466](/vuln.html?cve=2026-109466) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-109495](/vuln.html?cve=2026-109495) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-109502](/vuln.html?cve=2026-109502) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111296](/vuln.html?cve=2026-111296) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-123391](/vuln.html?cve=2026-123391) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-80095](/vuln.html?cve=2026-80095) | No | No | - | - | Important | 9.0 | 7.8 |
| [CVE-2026-88176](/vuln.html?cve=2026-88176) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office SharePoint Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-109455](/vuln.html?cve=2026-109455) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-110057](/vuln.html?cve=2026-110057) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-124210](/vuln.html?cve=2026-124210) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109464](/vuln.html?cve=2026-109464) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109472](/vuln.html?cve=2026-109472) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109499](/vuln.html?cve=2026-109499) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110044](/vuln.html?cve=2026-110044) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120000](/vuln.html?cve=2026-120000) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-123390](/vuln.html?cve=2026-123390) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office SharePoint Spoofing Vulnerability | | | | | | | |
| [CVE-2026-109454](/vuln.html?cve=2026-109454) | No | No | - | - | Important | 9.0 | 7.8 |
| [CVE-2026-109456](/vuln.html?cve=2026-109456) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-109497](/vuln.html?cve=2026-109497) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-109504](/vuln.html?cve=2026-109504) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-110045](/vuln.html?cve=2026-110045) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-110065](/vuln.html?cve=2026-110065) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-111297](/vuln.html?cve=2026-111297) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-111300](/vuln.html?cve=2026-111300) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-111303](/vuln.html?cve=2026-111303) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-112736](/vuln.html?cve=2026-112736) | No | No | - | - | Important | 5.3 | 4.6 |
| Microsoft Office Visio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109494](/vuln.html?cve=2026-109494) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109496](/vuln.html?cve=2026-109496) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Word Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-110046](/vuln.html?cve=2026-110046) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-110051](/vuln.html?cve=2026-110051) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-110066](/vuln.html?cve=2026-110066) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-111288](/vuln.html?cve=2026-111288) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-112720](/vuln.html?cve=2026-112720) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-116721](/vuln.html?cve=2026-116721) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-124233](/vuln.html?cve=2026-124233) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Office Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109491](/vuln.html?cve=2026-109491) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-109500](/vuln.html?cve=2026-109500) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-109501](/vuln.html?cve=2026-109501) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109503](/vuln.html?cve=2026-109503) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-109505](/vuln.html?cve=2026-109505) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110047](/vuln.html?cve=2026-110047) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-110050](/vuln.html?cve=2026-110050) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110052](/vuln.html?cve=2026-110052) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-110053](/vuln.html?cve=2026-110053) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-110054](/vuln.html?cve=2026-110054) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110056](/vuln.html?cve=2026-110056) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-110061](/vuln.html?cve=2026-110061) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110062](/vuln.html?cve=2026-110062) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110064](/vuln.html?cve=2026-110064) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110067](/vuln.html?cve=2026-110067) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-111285](/vuln.html?cve=2026-111285) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-111287](/vuln.html?cve=2026-111287) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-111290](/vuln.html?cve=2026-111290) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111294](/vuln.html?cve=2026-111294) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111295](/vuln.html?cve=2026-111295) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111298](/vuln.html?cve=2026-111298) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111299](/vuln.html?cve=2026-111299) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111302](/vuln.html?cve=2026-111302) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-111304](/vuln.html?cve=2026-111304) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111306](/vuln.html?cve=2026-111306) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111307](/vuln.html?cve=2026-111307) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111308](/vuln.html?cve=2026-111308) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-111310](/vuln.html?cve=2026-111310) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112714](/vuln.html?cve=2026-112714) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112715](/vuln.html?cve=2026-112715) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112716](/vuln.html?cve=2026-112716) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112717](/vuln.html?cve=2026-112717) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112718](/vuln.html?cve=2026-112718) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112719](/vuln.html?cve=2026-112719) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112721](/vuln.html?cve=2026-112721) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112722](/vuln.html?cve=2026-112722) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112723](/vuln.html?cve=2026-112723) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112724](/vuln.html?cve=2026-112724) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112726](/vuln.html?cve=2026-112726) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112728](/vuln.html?cve=2026-112728) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112729](/vuln.html?cve=2026-112729) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112730](/vuln.html?cve=2026-112730) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112733](/vuln.html?cve=2026-112733) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112735](/vuln.html?cve=2026-112735) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112739](/vuln.html?cve=2026-112739) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112741](/vuln.html?cve=2026-112741) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116718](/vuln.html?cve=2026-116718) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116719](/vuln.html?cve=2026-116719) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116720](/vuln.html?cve=2026-116720) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116722](/vuln.html?cve=2026-116722) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116923](/vuln.html?cve=2026-116923) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116925](/vuln.html?cve=2026-116925) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-123394](/vuln.html?cve=2026-123394) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-124185](/vuln.html?cve=2026-124185) | No | No | - | - | Critical | 7.5 | 6.5 |
| Microsoft Outlook Spoofing Vulnerability | | | | | | | |
| [CVE-2026-124194](/vuln.html?cve=2026-124194) | No | Yes | - | - | Moderate | 6.5 | 5.7 |
| Microsoft PowerPoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109487](/vuln.html?cve=2026-109487) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-120005](/vuln.html?cve=2026-120005) | No | No | - | - | Critical | 8.8 | 7.7 |
| Microsoft PowerShell Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-122985](/vuln.html?cve=2026-122985) | No | No | - | - | Important | 6.1 | 5.3 |
| Microsoft PowerShell Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-113815](/vuln.html?cve=2026-113815) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-124226](/vuln.html?cve=2026-124226) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft QUIC Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105512](/vuln.html?cve=2026-105512) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-88236](/vuln.html?cve=2026-88236) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Raw Image Extension Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-114166](/vuln.html?cve=2026-114166) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Remote Registry Service Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105492](/vuln.html?cve=2026-105492) | No | No | - | - | Important | 5.3 | 4.6 |
| Microsoft SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-116929](/vuln.html?cve=2026-116929) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116934](/vuln.html?cve=2026-116934) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116944](/vuln.html?cve=2026-116944) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-118105](/vuln.html?cve=2026-118105) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118108](/vuln.html?cve=2026-118108) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118109](/vuln.html?cve=2026-118109) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118110](/vuln.html?cve=2026-118110) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118111](/vuln.html?cve=2026-118111) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118112](/vuln.html?cve=2026-118112) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118113](/vuln.html?cve=2026-118113) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118114](/vuln.html?cve=2026-118114) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118115](/vuln.html?cve=2026-118115) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118116](/vuln.html?cve=2026-118116) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-118117](/vuln.html?cve=2026-118117) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118118](/vuln.html?cve=2026-118118) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118119](/vuln.html?cve=2026-118119) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-118120](/vuln.html?cve=2026-118120) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-66813](/vuln.html?cve=2026-66813) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-67375](/vuln.html?cve=2026-67375) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67387](/vuln.html?cve=2026-67387) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-84010](/vuln.html?cve=2026-84010) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-94513](/vuln.html?cve=2026-94513) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft SQL Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-116932](/vuln.html?cve=2026-116932) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-116935](/vuln.html?cve=2026-116935) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-116939](/vuln.html?cve=2026-116939) | No | No | - | - | Important | 5.7 | 5.0 |
| [CVE-2026-116940](/vuln.html?cve=2026-116940) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-116943](/vuln.html?cve=2026-116943) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118102](/vuln.html?cve=2026-118102) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-118103](/vuln.html?cve=2026-118103) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118104](/vuln.html?cve=2026-118104) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-67382](/vuln.html?cve=2026-67382) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-68783](/vuln.html?cve=2026-68783) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116930](/vuln.html?cve=2026-116930) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116931](/vuln.html?cve=2026-116931) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116933](/vuln.html?cve=2026-116933) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-116936](/vuln.html?cve=2026-116936) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-116937](/vuln.html?cve=2026-116937) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116938](/vuln.html?cve=2026-116938) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116941](/vuln.html?cve=2026-116941) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116942](/vuln.html?cve=2026-116942) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116945](/vuln.html?cve=2026-116945) | No | No | - | - | Important | 9.8 | 8.5 |
| [CVE-2026-116946](/vuln.html?cve=2026-116946) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-116947](/vuln.html?cve=2026-116947) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-118106](/vuln.html?cve=2026-118106) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-67372](/vuln.html?cve=2026-67372) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67374](/vuln.html?cve=2026-67374) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67391](/vuln.html?cve=2026-67391) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67632](/vuln.html?cve=2026-67632) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67637](/vuln.html?cve=2026-67637) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-67646](/vuln.html?cve=2026-67646) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-120002](/vuln.html?cve=2026-120002) | No | No | - | - | Important | 9.9 | 8.6 |
| Microsoft Teams Spoofing Vulnerability | | | | | | | |
| [CVE-2026-116926](/vuln.html?cve=2026-116926) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Teams for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-122979](/vuln.html?cve=2026-122979) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-69901](/vuln.html?cve=2026-69901) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Trace Data Helper Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-121681](/vuln.html?cve=2026-121681) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-122172](/vuln.html?cve=2026-122172) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft WDAC OLE DB provider for SQL Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116698](/vuln.html?cve=2026-116698) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-116699](/vuln.html?cve=2026-116699) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-85838](/vuln.html?cve=2026-85838) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-85839](/vuln.html?cve=2026-85839) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-88222](/vuln.html?cve=2026-88222) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Windows App Store Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119987](/vuln.html?cve=2026-119987) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Windows Codecs Library Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96150](/vuln.html?cve=2026-96150) | No | No | - | - | Important | 5.6 | 4.9 |
| Microsoft Windows Codecs Library Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113749](/vuln.html?cve=2026-113749) | No | No | - | - | Critical | 7.5 | 6.5 |
| Microsoft Windows Media Foundation Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122168](/vuln.html?cve=2026-122168) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Windows Media Foundation Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-96157](/vuln.html?cve=2026-96157) | No | No | - | - | Important | 9.8 | 8.5 |
| Microsoft Windows SCSI Class System File Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105586](/vuln.html?cve=2026-105586) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Windows SCSI Class System File Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-113821](/vuln.html?cve=2026-113821) | No | No | - | - | Important | 4.1 | 3.6 |
| Microsoft Windows Search Component Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119943](/vuln.html?cve=2026-119943) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119954](/vuln.html?cve=2026-119954) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Windows Speech Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119904](/vuln.html?cve=2026-119904) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Windows VMSwitch Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-97002](/vuln.html?cve=2026-97002) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-110048](/vuln.html?cve=2026-110048) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-110049](/vuln.html?cve=2026-110049) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-110055](/vuln.html?cve=2026-110055) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-113759](/vuln.html?cve=2026-113759) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft XPS Document Converter Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119881](/vuln.html?cve=2026-119881) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft XPS Document Converter Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119880](/vuln.html?cve=2026-119880) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-122171](/vuln.html?cve=2026-122171) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Xbox Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-66801](/vuln.html?cve=2026-66801) | No | No | - | - | Important |  |  |
| Microsoft.Data.SqlClient Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-62903](/vuln.html?cve=2026-62903) | No | No | - | - | Important |  |  |
| PowerShell Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-124224](/vuln.html?cve=2026-124224) | No | No | - | - | Important | 7.0 | 6.1 |
| PowerShell Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-121669](/vuln.html?cve=2026-121669) | No | No | - | - | Important | 6.1 | 5.3 |
| [CVE-2026-121674](/vuln.html?cve=2026-121674) | No | No | - | - | Important | 6.1 | 5.3 |
| [CVE-2026-121675](/vuln.html?cve=2026-121675) | No | No | - | - | Important | 6.1 | 5.3 |
| Quality Windows Audio/Video Experience (QWAVE) service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119387](/vuln.html?cve=2026-119387) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119388](/vuln.html?cve=2026-119388) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-123389](/vuln.html?cve=2026-123389) | No | No | - | - | Important | 7.0 | 6.1 |
| RPC Runtime Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-83894](/vuln.html?cve=2026-83894) | No | No | - | - | Important | 7.0 | 6.1 |
| Reliable Multicast Transport Driver (RMCAST) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-116697](/vuln.html?cve=2026-116697) | No | No | - | - | Important | 5.9 | 5.2 |
| Remote Access API Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119853](/vuln.html?cve=2026-119853) | No | No | - | - | Important | 7.8 | 6.8 |
| Remote Desktop Client Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119390](/vuln.html?cve=2026-119390) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119858](/vuln.html?cve=2026-119858) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119934](/vuln.html?cve=2026-119934) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-95964](/vuln.html?cve=2026-95964) | No | No | - | - | Important | 7.5 | 6.5 |
| Remote Desktop Client Tampering Vulnerability | | | | | | | |
| [CVE-2026-119824](/vuln.html?cve=2026-119824) | No | No | - | - | Important | 8.8 | 7.7 |
| Remote Desktop Gateway Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-80094](/vuln.html?cve=2026-80094) | No | No | - | - | Important | 7.5 | 6.5 |
| Remote Desktop Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-108401](/vuln.html?cve=2026-108401) | No | No | - | - | Important | 8.8 | 7.7 |
| Remote Procedure Call Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119972](/vuln.html?cve=2026-119972) | No | No | - | - | Important | 5.9 | 5.2 |
| Remote Procedure Call Runtime Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-118737](/vuln.html?cve=2026-118737) | No | No | - | - | Critical | 8.1 | 7.1 |
| Role: DNS Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-96017](/vuln.html?cve=2026-96017) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96975](/vuln.html?cve=2026-96975) | No | No | - | - | Important | 5.9 | 5.2 |
| SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-88111](/vuln.html?cve=2026-88111) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-94511](/vuln.html?cve=2026-94511) | No | No | - | - | Important | 8.8 | 7.7 |
| Secondary Logon Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96989](/vuln.html?cve=2026-96989) | No | No | - | - | Important | 5.5 | 4.8 |
| Server for NFS Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-118140](/vuln.html?cve=2026-118140) | No | No | - | - | Important | 5.5 | 4.8 |
| Servicing Stack Updates Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88235](/vuln.html?cve=2026-88235) | No | No | - | - | Important | 7.8 | 6.8 |
| Software Protection Platform (SPP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113748](/vuln.html?cve=2026-113748) | No | No | - | - | Important | 7.8 | 6.8 |
| Storport.sys Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119395](/vuln.html?cve=2026-119395) | No | No | - | - | Important | 4.0 | 3.5 |
| Virtual Hard Disk (VHD) Miniport Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119849](/vuln.html?cve=2026-119849) | No | No | - | - | Important | 7.0 | 6.1 |
| Visual Studio Code Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119981](/vuln.html?cve=2026-119981) | No | No | - | - | Important | 7.0 | 6.1 |
| Visual Studio Code GitHub Pull Requests and Issues Extension Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119976](/vuln.html?cve=2026-119976) | No | No | - | - | Important | 6.5 | 5.7 |
| Visual Studio Code Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-102230](/vuln.html?cve=2026-102230) | No | No | - | - | Important | 7.4 | 6.4 |
| Visual Studio Code Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119975](/vuln.html?cve=2026-119975) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119985](/vuln.html?cve=2026-119985) | No | No | - | - | Important | 8.3 | 7.2 |
| [CVE-2026-120779](/vuln.html?cve=2026-120779) | No | No | - | - | Important | 9.6 | 8.3 |
| [CVE-2026-120780](/vuln.html?cve=2026-120780) | No | No | - | - | Important | 8.3 | 7.2 |
| [CVE-2026-121662](/vuln.html?cve=2026-121662) | No | No | - | - | Important | 8.6 | 7.5 |
| [CVE-2026-121664](/vuln.html?cve=2026-121664) | No | No | - | - | Important | 8.3 | 7.2 |
| [CVE-2026-70094](/vuln.html?cve=2026-70094) | No | No | - | - | Important | 8.8 | 7.7 |
| Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-102236](/vuln.html?cve=2026-102236) | No | No | - | - | Important | 8.6 | 7.5 |
| [CVE-2026-114171](/vuln.html?cve=2026-114171) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119982](/vuln.html?cve=2026-119982) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-119983](/vuln.html?cve=2026-119983) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-120782](/vuln.html?cve=2026-120782) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-121660](/vuln.html?cve=2026-121660) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-121661](/vuln.html?cve=2026-121661) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-121663](/vuln.html?cve=2026-121663) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-121665](/vuln.html?cve=2026-121665) | No | No | - | - | Important | 8.8 | 7.7 |
| Visual Studio Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-114151](/vuln.html?cve=2026-114151) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-114152](/vuln.html?cve=2026-114152) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-114158](/vuln.html?cve=2026-114158) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-114159](/vuln.html?cve=2026-114159) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118745](/vuln.html?cve=2026-118745) | No | No | - | - | Important | 8.8 | 7.7 |
| Volume Shadow Copy Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105017](/vuln.html?cve=2026-105017) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119941](/vuln.html?cve=2026-119941) | No | No | - | - | Important | 7.8 | 6.8 |
| Win32k Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119825](/vuln.html?cve=2026-119825) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-119856](/vuln.html?cve=2026-119856) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-119910](/vuln.html?cve=2026-119910) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-95893](/vuln.html?cve=2026-95893) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Domain Name Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-112727](/vuln.html?cve=2026-112727) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96002](/vuln.html?cve=2026-96002) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96020](/vuln.html?cve=2026-96020) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96064](/vuln.html?cve=2026-96064) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-96092](/vuln.html?cve=2026-96092) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-96177](/vuln.html?cve=2026-96177) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Active Directory Certificate Services Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-95884](/vuln.html?cve=2026-95884) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Active Directory Certificate Services Security Feature Bypass | | | | | | | |
| [CVE-2026-105590](/vuln.html?cve=2026-105590) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Active Directory Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105559](/vuln.html?cve=2026-105559) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Active Directory Domain Services Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105568](/vuln.html?cve=2026-105568) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Active Directory Domain Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-118146](/vuln.html?cve=2026-118146) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows Active Directory Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119948](/vuln.html?cve=2026-119948) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Admin Center Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122988](/vuln.html?cve=2026-122988) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows Advanced Rasterization Platform Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105020](/vuln.html?cve=2026-105020) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105021](/vuln.html?cve=2026-105021) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105022](/vuln.html?cve=2026-105022) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105023](/vuln.html?cve=2026-105023) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105025](/vuln.html?cve=2026-105025) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105026](/vuln.html?cve=2026-105026) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105490](/vuln.html?cve=2026-105490) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105491](/vuln.html?cve=2026-105491) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105493](/vuln.html?cve=2026-105493) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105495](/vuln.html?cve=2026-105495) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105496](/vuln.html?cve=2026-105496) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105497](/vuln.html?cve=2026-105497) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105498](/vuln.html?cve=2026-105498) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-105499](/vuln.html?cve=2026-105499) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118215](/vuln.html?cve=2026-118215) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118216](/vuln.html?cve=2026-118216) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118217](/vuln.html?cve=2026-118217) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118218](/vuln.html?cve=2026-118218) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118219](/vuln.html?cve=2026-118219) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118221](/vuln.html?cve=2026-118221) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118222](/vuln.html?cve=2026-118222) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118223](/vuln.html?cve=2026-118223) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118224](/vuln.html?cve=2026-118224) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118225](/vuln.html?cve=2026-118225) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118226](/vuln.html?cve=2026-118226) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118227](/vuln.html?cve=2026-118227) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118228](/vuln.html?cve=2026-118228) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118229](/vuln.html?cve=2026-118229) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118232](/vuln.html?cve=2026-118232) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118277](/vuln.html?cve=2026-118277) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118278](/vuln.html?cve=2026-118278) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118279](/vuln.html?cve=2026-118279) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-118280](/vuln.html?cve=2026-118280) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118283](/vuln.html?cve=2026-118283) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-94515](/vuln.html?cve=2026-94515) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95960](/vuln.html?cve=2026-95960) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Advanced Rasterization Platform Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-118214](/vuln.html?cve=2026-118214) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88242](/vuln.html?cve=2026-88242) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows App Readiness Service Tampering Vulnerability | | | | | | | |
| [CVE-2026-95944](/vuln.html?cve=2026-95944) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows AppContainer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96018](/vuln.html?cve=2026-96018) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows AppX Deployment Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-116714](/vuln.html?cve=2026-116714) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88224](/vuln.html?cve=2026-88224) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows AppX Package Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96074](/vuln.html?cve=2026-96074) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Audio Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105541](/vuln.html?cve=2026-105541) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119888](/vuln.html?cve=2026-119888) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119893](/vuln.html?cve=2026-119893) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119894](/vuln.html?cve=2026-119894) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119895](/vuln.html?cve=2026-119895) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-121671](/vuln.html?cve=2026-121671) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96038](/vuln.html?cve=2026-96038) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96155](/vuln.html?cve=2026-96155) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Autopilot Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122175](/vuln.html?cve=2026-122175) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Background Intelligent Transfer Service (BITS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105554](/vuln.html?cve=2026-105554) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Backup Engine Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119405](/vuln.html?cve=2026-119405) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Bind Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-70182](/vuln.html?cve=2026-70182) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Biometric Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88239](/vuln.html?cve=2026-88239) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95877](/vuln.html?cve=2026-95877) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96127](/vuln.html?cve=2026-96127) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-119832](/vuln.html?cve=2026-119832) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-97015](/vuln.html?cve=2026-97015) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows Bluetooth A2DP driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88187](/vuln.html?cve=2026-88187) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows Bluetooth Port Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95996](/vuln.html?cve=2026-95996) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Bluetooth Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88213](/vuln.html?cve=2026-88213) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Bluetooth Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96001](/vuln.html?cve=2026-96001) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Broadcast DVR User Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112761](/vuln.html?cve=2026-112761) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-113762](/vuln.html?cve=2026-113762) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119401](/vuln.html?cve=2026-119401) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119402](/vuln.html?cve=2026-119402) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119403](/vuln.html?cve=2026-119403) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-88221](/vuln.html?cve=2026-88221) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-94529](/vuln.html?cve=2026-94529) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95871](/vuln.html?cve=2026-95871) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Broker Infrastructure Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96156](/vuln.html?cve=2026-96156) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88245](/vuln.html?cve=2026-88245) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95979](/vuln.html?cve=2026-95979) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96097](/vuln.html?cve=2026-96097) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows CD-ROM Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108405](/vuln.html?cve=2026-108405) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows CD-ROM Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-108404](/vuln.html?cve=2026-108404) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows CNG Key Isolation Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-103571](/vuln.html?cve=2026-103571) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows COM Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105533](/vuln.html?cve=2026-105533) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112968](/vuln.html?cve=2026-112968) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-94531](/vuln.html?cve=2026-94531) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows COM+ Event System Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113767](/vuln.html?cve=2026-113767) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-113769](/vuln.html?cve=2026-113769) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows COM+ Event System Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119855](/vuln.html?cve=2026-119855) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Camera Frame Server Monitor Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-85942](/vuln.html?cve=2026-85942) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88232](/vuln.html?cve=2026-88232) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88238](/vuln.html?cve=2026-88238) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Client for NFS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118138](/vuln.html?cve=2026-118138) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-122165](/vuln.html?cve=2026-122165) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95885](/vuln.html?cve=2026-95885) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Client for NFS Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-118141](/vuln.html?cve=2026-118141) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-88249](/vuln.html?cve=2026-88249) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Client for NFS Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-119404](/vuln.html?cve=2026-119404) | No | No | - | - | Important | 5.9 | 5.2 |
| Windows Clipboard Virtual Channel Extension Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96162](/vuln.html?cve=2026-96162) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105569](/vuln.html?cve=2026-105569) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112763](/vuln.html?cve=2026-112763) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112810](/vuln.html?cve=2026-112810) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119974](/vuln.html?cve=2026-119974) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Cloud Files Mini Filter Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112803](/vuln.html?cve=2026-112803) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Composite Image File System Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112809](/vuln.html?cve=2026-112809) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Connected User Experiences and Telemetry Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96072](/vuln.html?cve=2026-96072) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96088](/vuln.html?cve=2026-96088) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Connected User Experiences and Telemetry Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96101](/vuln.html?cve=2026-96101) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Connection Manager Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96042](/vuln.html?cve=2026-96042) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96043](/vuln.html?cve=2026-96043) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Container Isolation FS Filter Driver (unionfs.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112753](/vuln.html?cve=2026-112753) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-113761](/vuln.html?cve=2026-113761) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-113771](/vuln.html?cve=2026-113771) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Container Manager Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105562](/vuln.html?cve=2026-105562) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows CredSSP Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119962](/vuln.html?cve=2026-119962) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Credential Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119393](/vuln.html?cve=2026-119393) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Credential User Interface Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96978](/vuln.html?cve=2026-96978) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows DHCP Client Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-118739](/vuln.html?cve=2026-118739) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows DHCP Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113863](/vuln.html?cve=2026-113863) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-88240](/vuln.html?cve=2026-88240) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-96115](/vuln.html?cve=2026-96115) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows DHCP Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119890](/vuln.html?cve=2026-119890) | No | No | - | - | Important | 5.3 | 4.6 |
| [CVE-2026-96134](/vuln.html?cve=2026-96134) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows DHCP Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105588](/vuln.html?cve=2026-105588) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows DHCP Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105557](/vuln.html?cve=2026-105557) | No | No | - | - | Important | 5.9 | 5.2 |
| Windows DHCP Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105560](/vuln.html?cve=2026-105560) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-72998](/vuln.html?cve=2026-72998) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-88216](/vuln.html?cve=2026-88216) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-88243](/vuln.html?cve=2026-88243) | No | No | - | - | Important | 9.8 | 8.5 |
| Windows DHCP Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-113773](/vuln.html?cve=2026-113773) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows DIAL Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96076](/vuln.html?cve=2026-96076) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DNS Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-96176](/vuln.html?cve=2026-96176) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96983](/vuln.html?cve=2026-96983) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows DNS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105520](/vuln.html?cve=2026-105520) | No | No | - | - | Important | 7.2 | 6.3 |
| [CVE-2026-119953](/vuln.html?cve=2026-119953) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96179](/vuln.html?cve=2026-96179) | No | No | - | - | Important | 6.7 | 5.8 |
| Windows DNS Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105579](/vuln.html?cve=2026-105579) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-108425](/vuln.html?cve=2026-108425) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-119970](/vuln.html?cve=2026-119970) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96970](/vuln.html?cve=2026-96970) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96976](/vuln.html?cve=2026-96976) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96980](/vuln.html?cve=2026-96980) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96984](/vuln.html?cve=2026-96984) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96985](/vuln.html?cve=2026-96985) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96986](/vuln.html?cve=2026-96986) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96987](/vuln.html?cve=2026-96987) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96988](/vuln.html?cve=2026-96988) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-97006](/vuln.html?cve=2026-97006) | No | No | - | - | Important | 4.9 | 4.3 |
| Windows DNS Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109463](/vuln.html?cve=2026-109463) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-113855](/vuln.html?cve=2026-113855) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-88218](/vuln.html?cve=2026-88218) | No | No | - | - | Important | 9.8 | 8.5 |
| Windows DNS Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119971](/vuln.html?cve=2026-119971) | No | No | - | - | Important | 4.9 | 4.3 |
| [CVE-2026-96112](/vuln.html?cve=2026-96112) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-96972](/vuln.html?cve=2026-96972) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows DNS Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-81384](/vuln.html?cve=2026-81384) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows DNS Spoofing Vulnerability | | | | | | | |
| [CVE-2026-119905](/vuln.html?cve=2026-119905) | No | No | - | - | Important | 4.9 | 4.3 |
| Windows DPAPI (Data Protection Application Programming Interface) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113763](/vuln.html?cve=2026-113763) | No | No | - | - | Important | 6.3 | 5.5 |
| Windows DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105575](/vuln.html?cve=2026-105575) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105582](/vuln.html?cve=2026-105582) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-105583](/vuln.html?cve=2026-105583) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112986](/vuln.html?cve=2026-112986) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Defender Firewall Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112758](/vuln.html?cve=2026-112758) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Deployment Services Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112977](/vuln.html?cve=2026-112977) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-113818](/vuln.html?cve=2026-113818) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-118213](/vuln.html?cve=2026-118213) | No | No | - | - | Important | 5.9 | 5.2 |
| Windows Deployment Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105558](/vuln.html?cve=2026-105558) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119951](/vuln.html?cve=2026-119951) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Desktop Window Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112988](/vuln.html?cve=2026-112988) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-113758](/vuln.html?cve=2026-113758) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Device Association Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112743](/vuln.html?cve=2026-112743) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119844](/vuln.html?cve=2026-119844) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119866](/vuln.html?cve=2026-119866) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119874](/vuln.html?cve=2026-119874) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Device Inventory Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113750](/vuln.html?cve=2026-113750) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Devices Human Interface Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113817](/vuln.html?cve=2026-113817) | No | No | - | - | Important | 6.6 | 5.8 |
| Windows Diagnostic Policy Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112800](/vuln.html?cve=2026-112800) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95934](/vuln.html?cve=2026-95934) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95976](/vuln.html?cve=2026-95976) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Distributed File System (DFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118142](/vuln.html?cve=2026-118142) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Distributed Transaction Coordinator Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119917](/vuln.html?cve=2026-119917) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119919](/vuln.html?cve=2026-119919) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Encrypting File System (EFS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105527](/vuln.html?cve=2026-105527) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Encrypting File System (EFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96973](/vuln.html?cve=2026-96973) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Enhanced Storage Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119394](/vuln.html?cve=2026-119394) | No | No | - | - | Important | 6.6 | 5.8 |
| Windows Error Reporting Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105540](/vuln.html?cve=2026-105540) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-85862](/vuln.html?cve=2026-85862) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-94525](/vuln.html?cve=2026-94525) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95947](/vuln.html?cve=2026-95947) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96153](/vuln.html?cve=2026-96153) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Event Collector Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112793](/vuln.html?cve=2026-112793) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-112796](/vuln.html?cve=2026-112796) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Event Logging Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95997](/vuln.html?cve=2026-95997) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Event Viewer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-95977](/vuln.html?cve=2026-95977) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows FTP Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118137](/vuln.html?cve=2026-118137) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Failover Cluster Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119869](/vuln.html?cve=2026-119869) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows Fast FAT Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113751](/vuln.html?cve=2026-113751) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Feedback Hub Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96075](/vuln.html?cve=2026-96075) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows File Server Resource Management Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108415](/vuln.html?cve=2026-108415) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-108416](/vuln.html?cve=2026-108416) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-108421](/vuln.html?cve=2026-108421) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-113765](/vuln.html?cve=2026-113765) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows FileCrypt Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-113754](/vuln.html?cve=2026-113754) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-113757](/vuln.html?cve=2026-113757) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows FileCrypt Driver Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-113756](/vuln.html?cve=2026-113756) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Filter Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113755](/vuln.html?cve=2026-113755) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-121673](/vuln.html?cve=2026-121673) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Filtering Platform (WFP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105553](/vuln.html?cve=2026-105553) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112756](/vuln.html?cve=2026-112756) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-88215](/vuln.html?cve=2026-88215) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows Function Discovery Resource Publication Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119907](/vuln.html?cve=2026-119907) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Function Discovery Resource Publication Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-125134](/vuln.html?cve=2026-125134) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows Function Discovery SSDP Provider Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-118145](/vuln.html?cve=2026-118145) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows GDI Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108407](/vuln.html?cve=2026-108407) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-94527](/vuln.html?cve=2026-94527) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows GDI Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108424](/vuln.html?cve=2026-108424) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119966](/vuln.html?cve=2026-119966) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-125137](/vuln.html?cve=2026-125137) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-94519](/vuln.html?cve=2026-94519) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95879](/vuln.html?cve=2026-95879) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95888](/vuln.html?cve=2026-95888) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95895](/vuln.html?cve=2026-95895) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95906](/vuln.html?cve=2026-95906) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95909](/vuln.html?cve=2026-95909) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95922](/vuln.html?cve=2026-95922) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95932](/vuln.html?cve=2026-95932) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95935](/vuln.html?cve=2026-95935) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95938](/vuln.html?cve=2026-95938) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95942](/vuln.html?cve=2026-95942) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95948](/vuln.html?cve=2026-95948) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95950](/vuln.html?cve=2026-95950) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95953](/vuln.html?cve=2026-95953) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95966](/vuln.html?cve=2026-95966) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95971](/vuln.html?cve=2026-95971) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95973](/vuln.html?cve=2026-95973) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95974](/vuln.html?cve=2026-95974) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95983](/vuln.html?cve=2026-95983) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95991](/vuln.html?cve=2026-95991) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96122](/vuln.html?cve=2026-96122) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96124](/vuln.html?cve=2026-96124) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96126](/vuln.html?cve=2026-96126) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96160](/vuln.html?cve=2026-96160) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96168](/vuln.html?cve=2026-96168) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96171](/vuln.html?cve=2026-96171) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Graphics Kernel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119841](/vuln.html?cve=2026-119841) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-88217](/vuln.html?cve=2026-88217) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-95946](/vuln.html?cve=2026-95946) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-96048](/vuln.html?cve=2026-96048) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-96133](/vuln.html?cve=2026-96133) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-96137](/vuln.html?cve=2026-96137) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-96144](/vuln.html?cve=2026-96144) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows HTTP.sys Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119992](/vuln.html?cve=2026-119992) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95923](/vuln.html?cve=2026-95923) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Hyper-V Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119385](/vuln.html?cve=2026-119385) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-119955](/vuln.html?cve=2026-119955) | No | No | - | - | Important | 6.0 | 5.2 |
| [CVE-2026-95913](/vuln.html?cve=2026-95913) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-96965](/vuln.html?cve=2026-96965) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Hyper-V Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113753](/vuln.html?cve=2026-113753) | No | No | - | - | Critical | 8.2 | 7.1 |
| [CVE-2026-113856](/vuln.html?cve=2026-113856) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-113860](/vuln.html?cve=2026-113860) | No | No | - | - | Critical | 7.0 | 6.1 |
| [CVE-2026-113861](/vuln.html?cve=2026-113861) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-113864](/vuln.html?cve=2026-113864) | No | No | - | - | Critical | 6.4 | 5.6 |
| [CVE-2026-113865](/vuln.html?cve=2026-113865) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-119391](/vuln.html?cve=2026-119391) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119826](/vuln.html?cve=2026-119826) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119947](/vuln.html?cve=2026-119947) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-119960](/vuln.html?cve=2026-119960) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows Hyper-V Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-95910](/vuln.html?cve=2026-95910) | No | No | - | - | Important | 6.7 | 5.8 |
| Windows Hyper-V Spoofing Vulnerability | | | | | | | |
| [CVE-2026-119959](/vuln.html?cve=2026-119959) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows IKE Extension Spoofing Vulnerability | | | | | | | |
| [CVE-2026-122169](/vuln.html?cve=2026-122169) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows IP Translation Configuration Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119871](/vuln.html?cve=2026-119871) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows Image Acquisition Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-122163](/vuln.html?cve=2026-122163) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Imaging Component Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-96164](/vuln.html?cve=2026-96164) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Input System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119862](/vuln.html?cve=2026-119862) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119916](/vuln.html?cve=2026-119916) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Installer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105501](/vuln.html?cve=2026-105501) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105507](/vuln.html?cve=2026-105507) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105532](/vuln.html?cve=2026-105532) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105543](/vuln.html?cve=2026-105543) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105545](/vuln.html?cve=2026-105545) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-113847](/vuln.html?cve=2026-113847) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119398](/vuln.html?cve=2026-119398) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119399](/vuln.html?cve=2026-119399) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119831](/vuln.html?cve=2026-119831) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119852](/vuln.html?cve=2026-119852) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-119865](/vuln.html?cve=2026-119865) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119892](/vuln.html?cve=2026-119892) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119903](/vuln.html?cve=2026-119903) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119929](/vuln.html?cve=2026-119929) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95951](/vuln.html?cve=2026-95951) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96004](/vuln.html?cve=2026-96004) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96008](/vuln.html?cve=2026-96008) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96019](/vuln.html?cve=2026-96019) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96026](/vuln.html?cve=2026-96026) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96027](/vuln.html?cve=2026-96027) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96028](/vuln.html?cve=2026-96028) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96029](/vuln.html?cve=2026-96029) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96035](/vuln.html?cve=2026-96035) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96036](/vuln.html?cve=2026-96036) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96046](/vuln.html?cve=2026-96046) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96047](/vuln.html?cve=2026-96047) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96060](/vuln.html?cve=2026-96060) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96061](/vuln.html?cve=2026-96061) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96062](/vuln.html?cve=2026-96062) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96073](/vuln.html?cve=2026-96073) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96085](/vuln.html?cve=2026-96085) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96152](/vuln.html?cve=2026-96152) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Installer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112789](/vuln.html?cve=2026-112789) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-119838](/vuln.html?cve=2026-119838) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-119887](/vuln.html?cve=2026-119887) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Installer Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-119867](/vuln.html?cve=2026-119867) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Internet (wininet.dll) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96093](/vuln.html?cve=2026-96093) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows Internet Connection Sharing (ICS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118124](/vuln.html?cve=2026-118124) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119859](/vuln.html?cve=2026-119859) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119860](/vuln.html?cve=2026-119860) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119861](/vuln.html?cve=2026-119861) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-122179](/vuln.html?cve=2026-122179) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Internet Information Services Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119909](/vuln.html?cve=2026-119909) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-119936](/vuln.html?cve=2026-119936) | No | No | - | - | Important | 5.9 | 5.2 |
| Windows Internet Information Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119961](/vuln.html?cve=2026-119961) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Inventory Backup Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105584](/vuln.html?cve=2026-105584) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows JScript Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-112985](/vuln.html?cve=2026-112985) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Kerberos Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119940](/vuln.html?cve=2026-119940) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-70240](/vuln.html?cve=2026-70240) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-96082](/vuln.html?cve=2026-96082) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Kerberos Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119847](/vuln.html?cve=2026-119847) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-122164](/vuln.html?cve=2026-122164) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-85844](/vuln.html?cve=2026-85844) | No | No | - | - | Important | 9.8 | 8.5 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105504](/vuln.html?cve=2026-105504) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-105513](/vuln.html?cve=2026-105513) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-105566](/vuln.html?cve=2026-105566) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-108403](/vuln.html?cve=2026-108403) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-109473](/vuln.html?cve=2026-109473) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112790](/vuln.html?cve=2026-112790) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112802](/vuln.html?cve=2026-112802) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112805](/vuln.html?cve=2026-112805) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112969](/vuln.html?cve=2026-112969) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-114170](/vuln.html?cve=2026-114170) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118143](/vuln.html?cve=2026-118143) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-119868](/vuln.html?cve=2026-119868) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119884](/vuln.html?cve=2026-119884) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-119912](/vuln.html?cve=2026-119912) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-119918](/vuln.html?cve=2026-119918) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-119935](/vuln.html?cve=2026-119935) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-119965](/vuln.html?cve=2026-119965) | No | No | - | - | Important | 6.4 | 5.6 |
| [CVE-2026-122183](/vuln.html?cve=2026-122183) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-94514](/vuln.html?cve=2026-94514) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95905](/vuln.html?cve=2026-95905) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-95988](/vuln.html?cve=2026-95988) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96031](/vuln.html?cve=2026-96031) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96052](/vuln.html?cve=2026-96052) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96129](/vuln.html?cve=2026-96129) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kernel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105552](/vuln.html?cve=2026-105552) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-119857](/vuln.html?cve=2026-119857) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-96058](/vuln.html?cve=2026-96058) | No | No | - | - | Important | 4.6 | 4.0 |
| Windows Kernel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-112973](/vuln.html?cve=2026-112973) | No | No | - | - | Important | 7.1 | 6.2 |
| Windows Kernel Transaction Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119397](/vuln.html?cve=2026-119397) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-94522](/vuln.html?cve=2026-94522) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Kernel Transaction Manager Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-122297](/vuln.html?cve=2026-122297) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-94517](/vuln.html?cve=2026-94517) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Kernel-Mode Drivers Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96139](/vuln.html?cve=2026-96139) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows LDAP - Lightweight Directory Access Protocol Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119958](/vuln.html?cve=2026-119958) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows LUA File Virtualization Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88230](/vuln.html?cve=2026-88230) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96117](/vuln.html?cve=2026-96117) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Language Experience Service Tampering Vulnerability | | | | | | | |
| [CVE-2026-113766](/vuln.html?cve=2026-113766) | No | No | - | - | Important | 3.3 | 2.9 |
| Windows Layer-2 Bridge Network Driver Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-108402](/vuln.html?cve=2026-108402) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Link Layer Topology Discovery Protocol Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-116707](/vuln.html?cve=2026-116707) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Link Layer Topology Discovery Protocol Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116706](/vuln.html?cve=2026-116706) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-88244](/vuln.html?cve=2026-88244) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Link-Layer Discovery Protocol (LLDP) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-112975](/vuln.html?cve=2026-112975) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Link-Layer Discovery Protocol (LLDP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113816](/vuln.html?cve=2026-113816) | No | No | - | - | Important | 4.1 | 3.6 |
| Windows Local Security Authority Subsystem Service (LSASS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-112807](/vuln.html?cve=2026-112807) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Local Security Authority Subsystem Service (LSASS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-70231](/vuln.html?cve=2026-70231) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-85801](/vuln.html?cve=2026-85801) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88227](/vuln.html?cve=2026-88227) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88228](/vuln.html?cve=2026-88228) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96016](/vuln.html?cve=2026-96016) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96066](/vuln.html?cve=2026-96066) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Local Session Manager (LSM) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95876](/vuln.html?cve=2026-95876) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows MIDI Service Module Elevation of Privileges Vulnerability | | | | | | | |
| [CVE-2026-105565](/vuln.html?cve=2026-105565) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-105574](/vuln.html?cve=2026-105574) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119901](/vuln.html?cve=2026-119901) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows Management Instrumentation Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105503](/vuln.html?cve=2026-105503) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105524](/vuln.html?cve=2026-105524) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-105546](/vuln.html?cve=2026-105546) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112814](/vuln.html?cve=2026-112814) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-95920](/vuln.html?cve=2026-95920) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Management Instrumentation Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108410](/vuln.html?cve=2026-108410) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-112965](/vuln.html?cve=2026-112965) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Management Instrumentation Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105580](/vuln.html?cve=2026-105580) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Management Services Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119836](/vuln.html?cve=2026-119836) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows Maps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122182](/vuln.html?cve=2026-122182) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Media Player Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-88229](/vuln.html?cve=2026-88229) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Message Queuing Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105515](/vuln.html?cve=2026-105515) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119848](/vuln.html?cve=2026-119848) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Message Queuing Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118125](/vuln.html?cve=2026-118125) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-118126](/vuln.html?cve=2026-118126) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119833](/vuln.html?cve=2026-119833) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Message Queuing Queue Manager Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-109459](/vuln.html?cve=2026-109459) | No | No | - | - | Critical | 8.1 | 7.1 |
| [CVE-2026-119967](/vuln.html?cve=2026-119967) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Message Queuing Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116710](/vuln.html?cve=2026-116710) | No | No | - | - | Critical | 8.1 | 7.1 |
| [CVE-2026-119963](/vuln.html?cve=2026-119963) | No | No | - | - | Critical | 8.1 | 7.1 |
| [CVE-2026-119964](/vuln.html?cve=2026-119964) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Microsoft Account Sign-in Assistant Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119816](/vuln.html?cve=2026-119816) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119921](/vuln.html?cve=2026-119921) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Mobile Device Management Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119944](/vuln.html?cve=2026-119944) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Modern Device Management (MDM) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112987](/vuln.html?cve=2026-112987) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-113820](/vuln.html?cve=2026-113820) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96184](/vuln.html?cve=2026-96184) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Modern Device Management (MDM) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-102219](/vuln.html?cve=2026-102219) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-119945](/vuln.html?cve=2026-119945) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Multiple Provider Router Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-118220](/vuln.html?cve=2026-118220) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows NTFS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-100223](/vuln.html?cve=2026-100223) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119900](/vuln.html?cve=2026-119900) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-119933](/vuln.html?cve=2026-119933) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows NTFS Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105542](/vuln.html?cve=2026-105542) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-113848](/vuln.html?cve=2026-113848) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows NTFS Tampering Vulnerability | | | | | | | |
| [CVE-2026-102200](/vuln.html?cve=2026-102200) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-113844](/vuln.html?cve=2026-113844) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows NTLM Spoofing Vulnerability | | | | | | | |
| [CVE-2026-121680](/vuln.html?cve=2026-121680) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows NetBIOS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105551](/vuln.html?cve=2026-105551) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-112798](/vuln.html?cve=2026-112798) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119873](/vuln.html?cve=2026-119873) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96971](/vuln.html?cve=2026-96971) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Network Address Translation (NAT) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113862](/vuln.html?cve=2026-113862) | No | No | - | - | Critical | 8.1 | 7.1 |
| [CVE-2026-88212](/vuln.html?cve=2026-88212) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Network Connected Devices Auto-Setup Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-125136](/vuln.html?cve=2026-125136) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows Network Connection Broker Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105525](/vuln.html?cve=2026-105525) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-108406](/vuln.html?cve=2026-108406) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119821](/vuln.html?cve=2026-119821) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Network File System Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-118736](/vuln.html?cve=2026-118736) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows OLE DB Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105587](/vuln.html?cve=2026-105587) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows OLE Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95933](/vuln.html?cve=2026-95933) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows OLE Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96110](/vuln.html?cve=2026-96110) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Overlay Filter Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112760](/vuln.html?cve=2026-112760) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112813](/vuln.html?cve=2026-112813) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-119822](/vuln.html?cve=2026-119822) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-121670](/vuln.html?cve=2026-121670) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Overlay Filter Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108409](/vuln.html?cve=2026-108409) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-112750](/vuln.html?cve=2026-112750) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows PCI Bus Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96981](/vuln.html?cve=2026-96981) | No | No | - | - | Important | 6.4 | 5.6 |
| [CVE-2026-96992](/vuln.html?cve=2026-96992) | No | No | - | - | Important | 6.4 | 5.6 |
| Windows Partition Management Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105018](/vuln.html?cve=2026-105018) | No | No | - | - | Important | 6.6 | 5.8 |
| Windows Performance Counters Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-88220](/vuln.html?cve=2026-88220) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Performance Counters Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113768](/vuln.html?cve=2026-113768) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-95975](/vuln.html?cve=2026-95975) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Performance Monitor Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-96993](/vuln.html?cve=2026-96993) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Phone Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96107](/vuln.html?cve=2026-96107) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Point-to-Point Protocol over Ethernet (PPPoE) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105511](/vuln.html?cve=2026-105511) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-118123](/vuln.html?cve=2026-118123) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows PowerShell Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-124225](/vuln.html?cve=2026-124225) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Print Spooler Components Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105567](/vuln.html?cve=2026-105567) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112752](/vuln.html?cve=2026-112752) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112762](/vuln.html?cve=2026-112762) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-112765](/vuln.html?cve=2026-112765) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112791](/vuln.html?cve=2026-112791) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112792](/vuln.html?cve=2026-112792) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112797](/vuln.html?cve=2026-112797) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112811](/vuln.html?cve=2026-112811) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112976](/vuln.html?cve=2026-112976) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112978](/vuln.html?cve=2026-112978) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-112980](/vuln.html?cve=2026-112980) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-112981](/vuln.html?cve=2026-112981) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-113770](/vuln.html?cve=2026-113770) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119913](/vuln.html?cve=2026-119913) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119939](/vuln.html?cve=2026-119939) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119950](/vuln.html?cve=2026-119950) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Print Spooler Components Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105531](/vuln.html?cve=2026-105531) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-112806](/vuln.html?cve=2026-112806) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-112808](/vuln.html?cve=2026-112808) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Print Spooler Components Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113752](/vuln.html?cve=2026-113752) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows PrintWorkflowUserSvc Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119898](/vuln.html?cve=2026-119898) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119928](/vuln.html?cve=2026-119928) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Program Compatibility Assistant Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-123388](/vuln.html?cve=2026-123388) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Program Compatibility Assistant Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-88247](/vuln.html?cve=2026-88247) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112799](/vuln.html?cve=2026-112799) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Projected File System Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108414](/vuln.html?cve=2026-108414) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Projected File System Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-113764](/vuln.html?cve=2026-113764) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows Push Notification Core Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96023](/vuln.html?cve=2026-96023) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Push Notifications Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95881](/vuln.html?cve=2026-95881) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows RNDIS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112755](/vuln.html?cve=2026-112755) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows Raw Image Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-114169](/vuln.html?cve=2026-114169) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows Redirected Drive Buffering Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-113772](/vuln.html?cve=2026-113772) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows Redirected Drive Buffering System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108412](/vuln.html?cve=2026-108412) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Access API Tampering Vulnerability | | | | | | | |
| [CVE-2026-119396](/vuln.html?cve=2026-119396) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Remote Access Connection Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113843](/vuln.html?cve=2026-113843) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Assistance Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112751](/vuln.html?cve=2026-112751) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Desktop Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119839](/vuln.html?cve=2026-119839) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Remote Desktop Client Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108417](/vuln.html?cve=2026-108417) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-108418](/vuln.html?cve=2026-108418) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-108419](/vuln.html?cve=2026-108419) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-121677](/vuln.html?cve=2026-121677) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-121678](/vuln.html?cve=2026-121678) | No | No | - | - | Important | 5.3 | 4.6 |
| [CVE-2026-95908](/vuln.html?cve=2026-95908) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Remote Desktop Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-119932](/vuln.html?cve=2026-119932) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Remote Desktop Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119957](/vuln.html?cve=2026-119957) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-122166](/vuln.html?cve=2026-122166) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Desktop Services Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119882](/vuln.html?cve=2026-119882) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Remote Desktop Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-69327](/vuln.html?cve=2026-69327) | No | No | - | - | Important | 7.4 | 6.4 |
| [CVE-2026-69565](/vuln.html?cve=2026-69565) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Resilient File System (ReFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105509](/vuln.html?cve=2026-105509) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119386](/vuln.html?cve=2026-119386) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Rich Text Edit Control Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-96081](/vuln.html?cve=2026-96081) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows SMB Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112812](/vuln.html?cve=2026-112812) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112970](/vuln.html?cve=2026-112970) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112971](/vuln.html?cve=2026-112971) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119870](/vuln.html?cve=2026-119870) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows SMB Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119988](/vuln.html?cve=2026-119988) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2026-122176](/vuln.html?cve=2026-122176) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows SMB Server Network Transport Driver (srvnet.sys) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113825](/vuln.html?cve=2026-113825) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows SMBv3 Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-112972](/vuln.html?cve=2026-112972) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Sandbox Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119906](/vuln.html?cve=2026-119906) | No | No | - | - | Important |  |  |
| Windows Schannel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119952](/vuln.html?cve=2026-119952) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Search Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-116928](/vuln.html?cve=2026-116928) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows Secure Kernel Mode Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-112757](/vuln.html?cve=2026-112757) | No | No | - | - | Important | 6.0 | 5.2 |
| Windows Secure Socket Tunneling Protocol (SSTP) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-105561](/vuln.html?cve=2026-105561) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Secure Socket Tunneling Protocol (SSTP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105510](/vuln.html?cve=2026-105510) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Security Account Manager Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-112795](/vuln.html?cve=2026-112795) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-112966](/vuln.html?cve=2026-112966) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Security Account Manager Remote Protocol Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-122474](/vuln.html?cve=2026-122474) | No | No | - | - | Important | 5.9 | 5.2 |
| Windows Security Center Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113842](/vuln.html?cve=2026-113842) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Sensor Data Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-88241](/vuln.html?cve=2026-88241) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Servicing Stack Updates Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112989](/vuln.html?cve=2026-112989) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Setup and Deployment Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105547](/vuln.html?cve=2026-105547) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119914](/vuln.html?cve=2026-119914) | No | No | - | - | Important | 6.7 | 5.8 |
| Windows Shell Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119817](/vuln.html?cve=2026-119817) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-97013](/vuln.html?cve=2026-97013) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Shell Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-102868](/vuln.html?cve=2026-102868) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-105506](/vuln.html?cve=2026-105506) | No | No | - | - | Important | 5.0 | 4.4 |
| Windows Shell Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119938](/vuln.html?cve=2026-119938) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Simple Search and Discovery Protocol (SSDP) Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-85907](/vuln.html?cve=2026-85907) | No | No | - | - | Important | 4.4 | 3.9 |
| Windows Smart Card Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112794](/vuln.html?cve=2026-112794) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-118144](/vuln.html?cve=2026-118144) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-119383](/vuln.html?cve=2026-119383) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-119835](/vuln.html?cve=2026-119835) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95968](/vuln.html?cve=2026-95968) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Smart Card Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105549](/vuln.html?cve=2026-105549) | No | No | - | - | Important | 4.3 | 3.8 |
| Windows State Repository Service Tampering Vulnerability | | | | | | | |
| [CVE-2026-112979](/vuln.html?cve=2026-112979) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows StateRepository API Tampering Vulnerability | | | | | | | |
| [CVE-2026-95998](/vuln.html?cve=2026-95998) | No | No | - | - | Important | 4.4 | 3.9 |
| Windows Storage Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105529](/vuln.html?cve=2026-105529) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119389](/vuln.html?cve=2026-119389) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95889](/vuln.html?cve=2026-95889) | No | No | - | - | Important | 6.6 | 5.8 |
| Windows Storage Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105534](/vuln.html?cve=2026-105534) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Storage Spaces Controller Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105024](/vuln.html?cve=2026-105024) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119392](/vuln.html?cve=2026-119392) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119851](/vuln.html?cve=2026-119851) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Storage Spaces Controller Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113814](/vuln.html?cve=2026-113814) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119908](/vuln.html?cve=2026-119908) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-122475](/vuln.html?cve=2026-122475) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Storport Miniport Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119830](/vuln.html?cve=2026-119830) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-119885](/vuln.html?cve=2026-119885) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows Storport Miniport Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-119875](/vuln.html?cve=2026-119875) | No | No | - | - | Important | 4.0 | 3.5 |
| Windows Storport Miniport Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-119823](/vuln.html?cve=2026-119823) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows Subsystem for Linux Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119834](/vuln.html?cve=2026-119834) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119846](/vuln.html?cve=2026-119846) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-88237](/vuln.html?cve=2026-88237) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows System Events Broker Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-105530](/vuln.html?cve=2026-105530) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows TCP/IP Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-96077](/vuln.html?cve=2026-96077) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows TCP/IP Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-96102](/vuln.html?cve=2026-96102) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96969](/vuln.html?cve=2026-96969) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows TCP/IP Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-113859](/vuln.html?cve=2026-113859) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows TPM Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119382](/vuln.html?cve=2026-119382) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows Task Scheduler Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112759](/vuln.html?cve=2026-112759) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-122174](/vuln.html?cve=2026-122174) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-88233](/vuln.html?cve=2026-88233) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95894](/vuln.html?cve=2026-95894) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96053](/vuln.html?cve=2026-96053) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96845](/vuln.html?cve=2026-96845) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Telephony Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-108413](/vuln.html?cve=2026-108413) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-116700](/vuln.html?cve=2026-116700) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-119886](/vuln.html?cve=2026-119886) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Telephony Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108408](/vuln.html?cve=2026-108408) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Text Services Framework Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119818](/vuln.html?cve=2026-119818) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119925](/vuln.html?cve=2026-119925) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-119931](/vuln.html?cve=2026-119931) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Text Services Framework Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96022](/vuln.html?cve=2026-96022) | No | No | - | - | Important | 5.6 | 4.9 |
| Windows USB Audio Class driver (usbaudio.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119829](/vuln.html?cve=2026-119829) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows USB Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112764](/vuln.html?cve=2026-112764) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119872](/vuln.html?cve=2026-119872) | No | No | - | - | Important | 6.4 | 5.6 |
| [CVE-2026-122167](/vuln.html?cve=2026-122167) | No | No | - | - | Important | 6.8 | 5.9 |
| [CVE-2026-95872](/vuln.html?cve=2026-95872) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96005](/vuln.html?cve=2026-96005) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96051](/vuln.html?cve=2026-96051) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96055](/vuln.html?cve=2026-96055) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96056](/vuln.html?cve=2026-96056) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-96057](/vuln.html?cve=2026-96057) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows USB Hub Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95902](/vuln.html?cve=2026-95902) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-95999](/vuln.html?cve=2026-95999) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows USB Hub Driver Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-96041](/vuln.html?cve=2026-96041) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows USB Scanner Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119876](/vuln.html?cve=2026-119876) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows USB Video Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112984](/vuln.html?cve=2026-112984) | No | No | - | - | Important | 6.6 | 5.8 |
| [CVE-2026-112990](/vuln.html?cve=2026-112990) | No | No | - | - | Important | 4.7 | 4.1 |
| [CVE-2026-95961](/vuln.html?cve=2026-95961) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-95965](/vuln.html?cve=2026-95965) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows USM Communication Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-97000](/vuln.html?cve=2026-97000) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Universal Disk Format File System Driver (UDFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-119837](/vuln.html?cve=2026-119837) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-119840](/vuln.html?cve=2026-119840) | No | No | - | - | Important | 6.3 | 5.5 |
| [CVE-2026-122984](/vuln.html?cve=2026-122984) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Update Stack Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-122162](/vuln.html?cve=2026-122162) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows User Manager Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95987](/vuln.html?cve=2026-95987) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96037](/vuln.html?cve=2026-96037) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Virtual Filtering Platform (VFP) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-95962](/vuln.html?cve=2026-95962) | No | No | - | - | Important | 9.0 | 7.8 |
| Windows WLAN Service Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-96086](/vuln.html?cve=2026-96086) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105028](/vuln.html?cve=2026-105028) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-119827](/vuln.html?cve=2026-119827) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-119899](/vuln.html?cve=2026-119899) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-122170](/vuln.html?cve=2026-122170) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows WinHTTP Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-108423](/vuln.html?cve=2026-108423) | No | No | - | - | Important | 4.7 | 4.1 |
| Windows Wireless Networking Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105589](/vuln.html?cve=2026-105589) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows XWizard Framework Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-113760](/vuln.html?cve=2026-113760) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Xbox Live Networking Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-112967](/vuln.html?cve=2026-112967) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows eSCL Scanner Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112801](/vuln.html?cve=2026-112801) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows eSCL Scanner Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-95956](/vuln.html?cve=2026-95956) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows exFAT File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-112766](/vuln.html?cve=2026-112766) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-112804](/vuln.html?cve=2026-112804) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows iSCSI Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-122177](/vuln.html?cve=2026-122177) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-95898](/vuln.html?cve=2026-95898) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows iSCSI Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-88231](/vuln.html?cve=2026-88231) | No | No | - | - | Important | 5.7 | 5.0 |
| Windows iSCSI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-105518](/vuln.html?cve=2026-105518) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-88234](/vuln.html?cve=2026-88234) | No | No | - | - | Important | 9.8 | 8.5 |
| Windows iSCSI Target Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-83684](/vuln.html?cve=2026-83684) | No | No | - | - | Important | 7.5 | 6.5 |
| Winlogon Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105522](/vuln.html?cve=2026-105522) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-83563](/vuln.html?cve=2026-83563) | No | No | - | - | Important | 7.8 | 6.8 |
| Winsock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-105526](/vuln.html?cve=2026-105526) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-96994](/vuln.html?cve=2026-96994) | No | No | - | - | Important | 7.0 | 6.1 |
| Xbox Gaming Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95874](/vuln.html?cve=2026-95874) | No | No | - | - | Important | 7.8 | 6.8 |
| vhdmp.sys Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-95989](/vuln.html?cve=2026-95989) | No | No | - | - | Important | 7.0 | 6.1 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[patches](/tag.html?tag=patches)
[microsoft](/tag.html?tag=microsoft)

[6 comment(s)](/diary/Microsoft+Patch+Tuesday+November+2026/33508/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33506)
* [next](/diary/33514)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)