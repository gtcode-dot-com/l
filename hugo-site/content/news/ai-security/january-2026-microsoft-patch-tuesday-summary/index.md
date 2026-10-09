---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-13T20:15:14.628777+00:00'
exported_at: '2026-01-13T20:15:16.897832+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32624
structured_data:
  about: []
  author: ''
  description: 'January 2026 Microsoft Patch Tuesday Summary, Author: Johannes Ullrich'
  headline: January 2026 Microsoft Patch Tuesday Summary, (Tue, Jan 13th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32624
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: January 2026 Microsoft Patch Tuesday Summary, (Tue, Jan 13th)
updated_at: '2026-01-13T20:15:14.628777+00:00'
url_hash: b0aae9510927ae0f0ad0f4fbfc40a79651b46dc4
---

# [January 2026 Microsoft Patch Tuesday Summary](/forums/diary/January+2026+Microsoft+Patch+Tuesday+Summary/32624/)

**Published**
: 2026-01-13.
**Last Updated**
: 2026-01-13 19:05:41 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/January+2026+Microsoft+Patch+Tuesday+Summary/32624/#comments)

Today, Microsoft released patches for 113 vulnerabilities. One of these vulnerabilities affected the Edge browser and was patched upstream by Chromium.

Eight of the vulnerabilities are rated critical. One has been disclosed before today, and one is already being exploited. Five of the critical vulnerabilities affect Microsoft Office components.

**Noteworthy Vulnerabilities**

**[CVE-2026-20854](/vuln.html?cve=2026-20854)**
: A remote code execution vulnerability in LSASS. This brings back memories from hallmark Windows security events like the Blaster worm. However, in this case, the attacker must be authenticated. But the attacker does not need elevated privileges. Microsoft considers exploitation less likely.

**[CVE-2026-20805](/vuln.html?cve=2026-20805)
:**
This is an information disclosure vulnerability in the Desktop Windows Manager, and it is already being exploited. The vulnerability can be used to identify the section address from a remote ALPC port.

**[CVE-2026-21265](/vuln.html?cve=2026-21265)
:**
Secure boot may not recognize an expired certificate. This problem was already disclosed, but so far hasn't been exploited.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21224](/vuln.html?cve=2026-21224) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Core shared client library for Python Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21226](/vuln.html?cve=2026-21226) | No | No | - | - | Important | 7.5 | 6.5 |
| Capability Access Management Service (camsvc) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20815](/vuln.html?cve=2026-20815) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-20830](/vuln.html?cve=2026-20830) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-21221](/vuln.html?cve=2026-21221) | No | No | - | - | Important | 7.0 | 6.1 |
| Capability Access Management Service (camsvc) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20835](/vuln.html?cve=2026-20835) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20851](/vuln.html?cve=2026-20851) | No | No | - | - | Important | 6.2 | 5.4 |
| Chromium: CVE-2026-0628 Insufficient policy enforcement in WebView tag | | | | | | | |
| [CVE-2026-0628](/vuln.html?cve=2026-0628) | No | No | - | - | - |  |  |
| Desktop Window Manager Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20805](/vuln.html?cve=2026-20805) | No | Yes | - | - | Important | 5.5 | 4.8 |
| Desktop Windows Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20871](/vuln.html?cve=2026-20871) | No | No | - | - | Important | 7.8 | 6.8 |
| DirectX Graphics Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20814](/vuln.html?cve=2026-20814) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-20836](/vuln.html?cve=2026-20836) | No | No | - | - | Important | 7.0 | 6.1 |
| Dynamic Root of Trust for Measurement (DRTM) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20962](/vuln.html?cve=2026-20962) | No | No | - | - | Important | 4.4 | 3.9 |
| Host Process for Windows Tasks Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20941](/vuln.html?cve=2026-20941) | No | No | - | - | Important | 7.8 | 6.8 |
| Inbox COM Objects (Global Memory) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21219](/vuln.html?cve=2026-21219) | No | No | - | - | Important | 7.0 | 6.1 |
| LDAPTampering Vulnerability | | | | | | | |
| [CVE-2026-20812](/vuln.html?cve=2026-20812) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20842](/vuln.html?cve=2026-20842) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20946](/vuln.html?cve=2026-20946) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20955](/vuln.html?cve=2026-20955) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-20956](/vuln.html?cve=2026-20956) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20950](/vuln.html?cve=2026-20950) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20957](/vuln.html?cve=2026-20957) | No | No | - | - | Critical | 7.8 | 6.8 |
| Microsoft Excel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-20949](/vuln.html?cve=2026-20949) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Click-To-Run Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20943](/vuln.html?cve=2026-20943) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20953](/vuln.html?cve=2026-20953) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-20952](/vuln.html?cve=2026-20952) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20803](/vuln.html?cve=2026-20803) | No | No | - | - | Important | 7.2 | 6.3 |
| Microsoft SharePoint Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20958](/vuln.html?cve=2026-20958) | No | No | - | - | Important | 5.4 | 4.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20963](/vuln.html?cve=2026-20963) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20951](/vuln.html?cve=2026-20951) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20947](/vuln.html?cve=2026-20947) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20959](/vuln.html?cve=2026-20959) | No | No | - | - | Important | 4.6 | 4.0 |
| Microsoft Windows File Explorer Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20847](/vuln.html?cve=2026-20847) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20944](/vuln.html?cve=2026-20944) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-20948](/vuln.html?cve=2026-20948) | No | No | - | - | Important | 7.8 | 6.8 |
| NTLM Hash Disclosure Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20925](/vuln.html?cve=2026-20925) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-20872](/vuln.html?cve=2026-20872) | No | No | - | - | Important | 6.5 | 5.7 |
| Remote Procedure Call Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20821](/vuln.html?cve=2026-20821) | No | No | - | - | Important | 6.2 | 5.4 |
| Secure Boot Certificate Expiration Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-21265](/vuln.html?cve=2026-21265) | Yes | No | - | - | Important | 6.4 | 5.6 |
| TPM Trustlet Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20829](/vuln.html?cve=2026-20829) | No | No | - | - | Important | 5.5 | 4.8 |
| Tablet Windows User Interface (TWINUI) Subsystem Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20826](/vuln.html?cve=2026-20826) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20827](/vuln.html?cve=2026-20827) | No | No | - | - | Important | 5.5 | 4.8 |
| Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20811](/vuln.html?cve=2026-20811) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20920](/vuln.html?cve=2026-20920) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20863](/vuln.html?cve=2026-20863) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Admin Center Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20965](/vuln.html?cve=2026-20965) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20810](/vuln.html?cve=2026-20810) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20831](/vuln.html?cve=2026-20831) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20860](/vuln.html?cve=2026-20860) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Client-Side Caching (CSC) Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20839](/vuln.html?cve=2026-20839) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Clipboard Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20844](/vuln.html?cve=2026-20844) | No | No | - | - | Important | 7.4 | 6.4 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20857](/vuln.html?cve=2026-20857) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20940](/vuln.html?cve=2026-20940) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20820](/vuln.html?cve=2026-20820) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Connected Devices Platform Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20864](/vuln.html?cve=2026-20864) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Deployment Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-0386](/vuln.html?cve=2026-0386) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Error Reporting Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20817](/vuln.html?cve=2026-20817) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows File Explorer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20808](/vuln.html?cve=2026-20808) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows File Explorer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20823](/vuln.html?cve=2026-20823) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20932](/vuln.html?cve=2026-20932) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20937](/vuln.html?cve=2026-20937) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20939](/vuln.html?cve=2026-20939) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Graphics Component Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20822](/vuln.html?cve=2026-20822) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows HTTP.sys Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20929](/vuln.html?cve=2026-20929) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Hello Tampering Vulnerability | | | | | | | |
| [CVE-2026-20804](/vuln.html?cve=2026-20804) | No | No | - | - | Important | 7.7 | 6.7 |
| [CVE-2026-20852](/vuln.html?cve=2026-20852) | No | No | - | - | Important | 7.7 | 6.7 |
| Windows Hyper-V Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20825](/vuln.html?cve=2026-20825) | No | No | - | - | Important | 4.4 | 3.9 |
| Windows Installer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20816](/vuln.html?cve=2026-20816) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kerberos Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20849](/vuln.html?cve=2026-20849) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Kerberos Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20833](/vuln.html?cve=2026-20833) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Kernel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20818](/vuln.html?cve=2026-20818) | No | No | - | - | Important | 6.2 | 5.4 |
| [CVE-2026-20838](/vuln.html?cve=2026-20838) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Kernel Memory Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20809](/vuln.html?cve=2026-20809) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kernel-Mode Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20859](/vuln.html?cve=2026-20859) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Local Security Authority Subsystem Service (LSASS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-20875](/vuln.html?cve=2026-20875) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Local Security Authority Subsystem Service (LSASS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20854](/vuln.html?cve=2026-20854) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows Local Session Manager (LSM) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20869](/vuln.html?cve=2026-20869) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Management Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20858](/vuln.html?cve=2026-20858) | No | No | - | - | Important | 7.8 | 6.9 |
| [CVE-2026-20865](/vuln.html?cve=2026-20865) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20877](/vuln.html?cve=2026-20877) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20918](/vuln.html?cve=2026-20918) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20923](/vuln.html?cve=2026-20923) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20924](/vuln.html?cve=2026-20924) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20861](/vuln.html?cve=2026-20861) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20866](/vuln.html?cve=2026-20866) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20867](/vuln.html?cve=2026-20867) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20873](/vuln.html?cve=2026-20873) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20874](/vuln.html?cve=2026-20874) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Management Services Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20862](/vuln.html?cve=2026-20862) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Media Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20837](/vuln.html?cve=2026-20837) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows NDIS Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20936](/vuln.html?cve=2026-20936) | No | No | - | - | Important | 4.3 | 3.8 |
| Windows NTFS Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20840](/vuln.html?cve=2026-20840) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-20922](/vuln.html?cve=2026-20922) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Assistance Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-20824](/vuln.html?cve=2026-20824) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Remote Procedure Call Interface Definition Language (IDL) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20832](/vuln.html?cve=2026-20832) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Routing and Remote Access Service (RRAS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20843](/vuln.html?cve=2026-20843) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Routing and Remote Access Service (RRAS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20868](/vuln.html?cve=2026-20868) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows SMB Server Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-20927](/vuln.html?cve=2026-20927) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows SMB Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20919](/vuln.html?cve=2026-20919) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-20921](/vuln.html?cve=2026-20921) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-20926](/vuln.html?cve=2026-20926) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-20934](/vuln.html?cve=2026-20934) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-20848](/vuln.html?cve=2026-20848) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Server Update Service (WSUS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-20856](/vuln.html?cve=2026-20856) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20834](/vuln.html?cve=2026-20834) | No | No | - | - | Important | 4.6 | 4.0 |
| Windows Telephony Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20931](/vuln.html?cve=2026-20931) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows Virtualization-Based Security (VBS) Enclave Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20876](/vuln.html?cve=2026-20876) | No | No | - | - | Critical | 6.7 | 5.8 |
| [CVE-2026-20938](/vuln.html?cve=2026-20938) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Virtualization-Based Security (VBS) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20819](/vuln.html?cve=2026-20819) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-20935](/vuln.html?cve=2026-20935) | No | No | - | - | Important | 6.2 | 5.4 |
| Windows WalletService Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20853](/vuln.html?cve=2026-20853) | No | No | - | - | Important | 7.4 | 6.4 |
| Windows Win32 Kernel Subsystem Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20870](/vuln.html?cve=2026-20870) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows rndismp6.sys Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20828](/vuln.html?cve=2026-20828) | No | No | - | - | Important | 4.6 | 4.0 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[microsoft](/tag.html?tag=microsoft)
[patch](/tag.html?tag=patch)
[Tuesday](/tag.html?tag=Tuesday)

[0 comment(s)](/diary/January+2026+Microsoft+Patch+Tuesday+Summary/32624/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32616)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)