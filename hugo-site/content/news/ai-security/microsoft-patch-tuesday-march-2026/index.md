---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T18:15:16.223737+00:00'
exported_at: '2026-03-10T18:15:18.545867+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32782
structured_data:
  about: []
  author: ''
  description: 'Microsoft Patch Tuesday March 2026, Author: Johannes Ullrich'
  headline: Microsoft Patch Tuesday March 2026, (Tue, Mar 10th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32782
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patch Tuesday March 2026, (Tue, Mar 10th)
updated_at: '2026-03-10T18:15:16.223737+00:00'
url_hash: 293025f10ee23859e92612121ac5e60421514c30
---

# [Microsoft Patch Tuesday March 2026](/forums/diary/Microsoft+Patch+Tuesday+March+2026/32782/)

**Published**
: 2026-03-10.
**Last Updated**
: 2026-03-10 17:33:47 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Microsoft+Patch+Tuesday+March+2026/32782/#comments)

Microsoft today released patches for 93 vulnerabilities, including 9 vulnerabilities in Chromium affecting Microsoft Edge. 8 of the vulnerabilities are rated critical. 2 were disclosed prior to today but have not yet been exploited. This update addresses no already-exploited vulnerabilities.

Disclose vulnerabilities:

**CVE-2026-26127**
: A denial of service vulnerability in .Net. Microsoft considers exploitation unlikely. The issue arises from an out-of-bounds read and can be exploited across the network. No authentication is required.

**CVE-2026-21262**
: A privilege escalation in SQL Server. An authenticated user may be able to escalate privileges to sysadmin.

Critical Vulnerabilities:

**CVE-2026-21536**
: The vulnerability in Microsoft's Devices Pricing Program allows remote code execution. But this product is only offered as a cloud service, and Microsoft has already deployed the patch. Microsoft credits the AI vulnerability scanning platform XBOW with discovering this vulnerability.

**CVE-2026-26125**
: Similar to the above vulnerability, this elevation-of-privilege vulnerability in Microsoft's Payment Orchestrator service has been mitigated by Microsoft.

**CVE-2026-26113, CVE-2026-26110, CVE-2026-26144**
: These vulnerabilities affect Excel and Office.

**CVE-2026-23651, CVE-2026-26124, CVE-2026-26122**
: These vulnerabilities affect Microsoft ACI Confidential Containers. No customer action is required. Microsoft already patched these issues.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26127](/vuln.html?cve=2026-26127) | Yes | No | - | - | Important | 7.5 | 6.5 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26131](/vuln.html?cve=2026-26131) | No | No | - | - | Important | 7.8 | 6.8 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26130](/vuln.html?cve=2026-26130) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Domain Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25177](/vuln.html?cve=2026-25177) | No | No | - | - | Important | 8.8 | 7.7 |
| Arc Enabled Servers - Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26117](/vuln.html?cve=2026-26117) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure IOT Explorer Spoofing Vulnerability | | | | | | | |
| [CVE-2026-26121](/vuln.html?cve=2026-26121) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure IoT Explorer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-23664](/vuln.html?cve=2026-23664) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-23661](/vuln.html?cve=2026-23661) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-23662](/vuln.html?cve=2026-23662) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure MCP Server Tools Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26118](/vuln.html?cve=2026-26118) | No | No | - | - | Important | 8.8 | 7.7 |
| Broadcast DVR Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23667](/vuln.html?cve=2026-23667) | No | No | - | - | Important | 7.0 | 6.1 |
| Chromium: CVE-2026-3536 Integer overflow in ANGLE | | | | | | | |
| [CVE-2026-3536](/vuln.html?cve=2026-3536) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3538 Integer overflow in Skia | | | | | | | |
| [CVE-2026-3538](/vuln.html?cve=2026-3538) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3539 Object lifecycle issue in DevTools | | | | | | | |
| [CVE-2026-3539](/vuln.html?cve=2026-3539) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3540 Inappropriate implementation in WebAudio | | | | | | | |
| [CVE-2026-3540](/vuln.html?cve=2026-3540) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3541 Inappropriate implementation in CSS | | | | | | | |
| [CVE-2026-3541](/vuln.html?cve=2026-3541) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3542 Inappropriate implementation in WebAssembly | | | | | | | |
| [CVE-2026-3542](/vuln.html?cve=2026-3542) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3543 Inappropriate implementation in V8 | | | | | | | |
| [CVE-2026-3543](/vuln.html?cve=2026-3543) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3544 Heap buffer overflow in WebCodecs | | | | | | | |
| [CVE-2026-3544](/vuln.html?cve=2026-3544) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-3545 Insufficient data validation in Navigation | | | | | | | |
| [CVE-2026-3545](/vuln.html?cve=2026-3545) | No | No | - | - | - |  |  |
| GDI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-25190](/vuln.html?cve=2026-25190) | No | No | - | - | Important | 7.8 | 6.8 |
| GDI+ Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-25181](/vuln.html?cve=2026-25181) | No | No | - | - | Important | 7.5 | 6.5 |
| GitHub: CVE-2026-26030 Microsoft Semantic Kernel InMemoryVectorStore filter functionality vulnerable | | | | | | | |
| [CVE-2026-26030](/vuln.html?cve=2026-26030) | No | No | - | - | Important | 9.9 | 8.6 |
| GitHub: Zero Shot SCFoundation Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-23654](/vuln.html?cve=2026-23654) | No | No | - | - | Important | 8.8 | 7.7 |
| Hybrid Worker Extension (Arc?enabled Windows VMs) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26141](/vuln.html?cve=2026-26141) | No | No | - | - | Important | 7.8 | 6.8 |
| Linux Azure Diagnostic extension (LAD) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23665](/vuln.html?cve=2026-23665) | No | No | - | - | Important | 7.8 | 6.8 |
| MapUrlToZone Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-23674](/vuln.html?cve=2026-23674) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft ACI Confidential Containers Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23651](/vuln.html?cve=2026-23651) | No | No | - | - | Critical | 6.7 | 6.0 |
| [CVE-2026-26124](/vuln.html?cve=2026-26124) | No | No | - | - | Critical | 6.7 | 6.0 |
| Microsoft ACI Confidential Containers Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26122](/vuln.html?cve=2026-26122) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Authenticator Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26123](/vuln.html?cve=2026-26123) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Azure AD SSH Login extension for Linux Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26148](/vuln.html?cve=2026-26148) | No | No | - | - | Important | 8.1 | 7.3 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25167](/vuln.html?cve=2026-25167) | No | No | - | - | Important | 7.4 | 6.4 |
| Microsoft Devices Pricing Program Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-21536](/vuln.html?cve=2026-21536) | No | No | - | - | Critical | 9.8 | 8.5 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26144](/vuln.html?cve=2026-26144) | No | No | - | - | Critical | 7.5 | 6.5 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-26112](/vuln.html?cve=2026-26112) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26107](/vuln.html?cve=2026-26107) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26108](/vuln.html?cve=2026-26108) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26109](/vuln.html?cve=2026-26109) | No | No | - | - | Important | 8.4 | 7.3 |
| Microsoft Office Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26134](/vuln.html?cve=2026-26134) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-26113](/vuln.html?cve=2026-26113) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-26110](/vuln.html?cve=2026-26110) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-26114](/vuln.html?cve=2026-26114) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-26106](/vuln.html?cve=2026-26106) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-26105](/vuln.html?cve=2026-26105) | No | No | - | - | Important | 8.1 | 7.1 |
| Multiple UNC Provider Kernel Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24283](/vuln.html?cve=2026-24283) | No | No | - | - | Important | 8.8 | 7.7 |
| Payment Orchestrator Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26125](/vuln.html?cve=2026-26125) | No | No | - | - | Critical | 8.6 | 7.7 |
| Performance Counters for Windows Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25165](/vuln.html?cve=2026-25165) | No | No | - | - | Important | 7.8 | 6.8 |
| Push message Routing Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24282](/vuln.html?cve=2026-24282) | No | No | - | - | Important | 5.5 | 4.8 |
| SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21262](/vuln.html?cve=2026-21262) | Yes | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-26115](/vuln.html?cve=2026-26115) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-26116](/vuln.html?cve=2026-26116) | No | No | - | - | Important | 8.8 | 7.7 |
| System Center Operations Manager (SCOM) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20967](/vuln.html?cve=2026-20967) | No | No | - | - | Important | 8.8 | 7.7 |
| Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24285](/vuln.html?cve=2026-24285) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Accessibility Infrastructure (ATBroker.exe) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24291](/vuln.html?cve=2026-24291) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Accessibility Infrastructure (ATBroker.exe) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-25186](/vuln.html?cve=2026-25186) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Admin Center in Azure Portal Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23660](/vuln.html?cve=2026-23660) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24293](/vuln.html?cve=2026-24293) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-25176](/vuln.html?cve=2026-25176) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-25178](/vuln.html?cve=2026-25178) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-25179](/vuln.html?cve=2026-25179) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows App Installer Spoofing Vulnerability | | | | | | | |
| [CVE-2026-23656](/vuln.html?cve=2026-23656) | No | No | - | - | Important |  |  |
| Windows Authentication Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25171](/vuln.html?cve=2026-25171) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Bluetooth RFCOM Protocol Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23671](/vuln.html?cve=2026-23671) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Connected Devices Platform Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24292](/vuln.html?cve=2026-24292) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25189](/vuln.html?cve=2026-25189) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Device Association Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24295](/vuln.html?cve=2026-24295) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-24296](/vuln.html?cve=2026-24296) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Extensible File Allocation Table Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25174](/vuln.html?cve=2026-25174) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Graphics Component Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-25168](/vuln.html?cve=2026-25168) | No | No | - | - | Important | 6.2 | 5.4 |
| [CVE-2026-25169](/vuln.html?cve=2026-25169) | No | No | - | - | Important | 6.2 | 5.4 |
| Windows Graphics Component Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23668](/vuln.html?cve=2026-23668) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Graphics Component Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-25180](/vuln.html?cve=2026-25180) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Hyper-V Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25170](/vuln.html?cve=2026-25170) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Kerberos Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-24297](/vuln.html?cve=2026-24297) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24287](/vuln.html?cve=2026-24287) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-24289](/vuln.html?cve=2026-24289) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26132](/vuln.html?cve=2026-26132) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Mobile Broadband Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-24288](/vuln.html?cve=2026-24288) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows NTFS Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25175](/vuln.html?cve=2026-25175) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Print Spooler Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-23669](/vuln.html?cve=2026-23669) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24290](/vuln.html?cve=2026-24290) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Resilient File System (ReFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23673](/vuln.html?cve=2026-23673) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Routing and Remote Access Service (RRAS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-25172](/vuln.html?cve=2026-25172) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-25173](/vuln.html?cve=2026-25173) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-26111](/vuln.html?cve=2026-26111) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows SMB Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-24294](/vuln.html?cve=2026-24294) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26128](/vuln.html?cve=2026-26128) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Shell Link Processing Spoofing Vulnerability | | | | | | | |
| [CVE-2026-25185](/vuln.html?cve=2026-25185) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows System Image Manager Assessment and Deployment Kit (ADK) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-25166](/vuln.html?cve=2026-25166) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Telephony Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25188](/vuln.html?cve=2026-25188) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Universal Disk Format File System Driver (UDFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-23672](/vuln.html?cve=2026-23672) | No | No | - | - | Important | 7.8 | 6.8 |
| Winlogon Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25187](/vuln.html?cve=2026-25187) | No | No | - | - | Important | 7.8 | 6.8 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[patch Tuesday](/tag.html?tag=patch Tuesday)
[Microsoft](/tag.html?tag=Microsoft)

[0 comment(s)](/diary/Microsoft+Patch+Tuesday+March+2026/32782/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32778)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)