---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T01:52:46.518394+00:00'
exported_at: '2026-06-11T01:52:48.601179+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33064
structured_data:
  about: []
  author: ''
  description: 'Microsoft June 2026 Patch Tuesday, Author: Johannes Ullrich'
  headline: Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33064
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft June 2026 Patch Tuesday, (Tue, Jun 9th)
updated_at: '2026-06-11T01:52:46.518394+00:00'
url_hash: 0a0a68e8701018e9d35cdf6dceb75d755ade8915
---

# [Microsoft June 2026 Patch Tuesday](/forums/diary/Microsoft+June+2026+Patch+Tuesday/33064/)

**Published**
: 2026-06-09.
**Last Updated**
: 2026-06-09 17:34:29 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Microsoft+June+2026+Patch+Tuesday/33064/#comments)

Microsoft today released patches for 204 vulnerabilities. 38 of these vulnerabilities are considered critical, and three have been disclosed before today. Six of the vulnerabilities affect Microsoft cloud solutions and do not require any user action. In addition, Microsoft incorporated 360 different vulnerabilities affecting Chromium into its Edge browser.

This is certainly a busier-than-usual patch Tuesday. In particular, the large number of patched Chromium/Edge vulnerabilities underscores the impact of AI tools on vulnerability discovery.

Some noteworthy vulnerabilities:

**CVE-2026-49160**
: This vulnerability was made public a week ago. As implemented, the "HPACK" compression algorithm in HTTP/2 and HTTP/3 can lead to a "compression bomb" that consumes excessive resources. Many HTTP/2 implementations are vulnerable. Microsoft addressed this issue by adding a "MaxHeadersCount" registry setting that limits the amount of allocated resources.

**CVE-2026-47291**
: Affecting the Microsoft web server engine http.sys, just like CVE-2026-49160, this vulnerability is rated critical and allows for remote code execution. The integer overflow requires an oversized request to trigger it. Microsoft recommends restricting the "MaxRequestBytes" to prevent exploitation until the patch can be rolled out.

CVE-2026-45648: A stack-based buffer overflow in Active Directory Domain Services. A successful attack requires authentication, and Microsoft considers exploit development as "unlikely".

Microsoft fixed three different BitLocker security feature bypass vulnerabilities. One of the vulnerabilities was already publicly known. An "anonymous" researcher is credited with the discovery, but I assume it is one of the "Nightmare Eclipse" vulnerabilities.

Several critical vulnerabilities affect Microsoft Office, Outlook, and Word.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET SDK Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45490](/vuln.html?cve=2026-45490) | No | No | - | - | Important | 7.8 | 6.8 |
| .NET Tampering Vulnerability | | | | | | | |
| [CVE-2026-45491](/vuln.html?cve=2026-45491) | No | No | - | - | Important | 6.2 | 5.4 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-45591](/vuln.html?cve=2026-45591) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure HorizonDB Elevation of Privilege Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-48567](/vuln.html?cve=2026-48567) | No | No | - | - | Critical | 10.0 | 8.7 |
| Azure Kubernetes Service (AKS) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32193](/vuln.html?cve=2026-32193) | No | No | - | - | Critical | 8.8 | 7.7 |
| Azure Stack Edge Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47643](/vuln.html?cve=2026-47643) | No | No | - | - | Important | 9.8 | 8.5 |
| Azure Stack Edge Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41098](/vuln.html?cve=2026-41098) | No | No | - | - | Important | 8.4 | 7.3 |
| Copilot Chat (Microsoft Edge) Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-47644](/vuln.html?cve=2026-47644) | No | No | - | - | Critical | 6.5 | 5.7 |
| DHCP Client Service Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-44815](/vuln.html?cve=2026-44815) | No | No | - | - | Critical | 9.8 | 8.5 |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-49160](/vuln.html?cve=2026-49160) | Yes | No | - | - | Important | 7.5 | 6.5 |
| HTTP.sys Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47291](/vuln.html?cve=2026-47291) | No | No | - | - | Critical | 9.8 | 8.5 |
| M365 Copilot Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-42824](/vuln.html?cve=2026-42824) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Azure Attestation service and Device Health Attestation Service Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45642](/vuln.html?cve=2026-45642) | No | No | - | - | Important | 3.9 | 3.4 |
| Microsoft Azure Network Adapter Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45476](/vuln.html?cve=2026-45476) | No | No | - | - | Critical | 8.2 | 7.1 |
| Microsoft Bing Search Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45650](/vuln.html?cve=2026-45650) | No | No | - | - | Important | 4.3 | 3.8 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-44810](/vuln.html?cve=2026-44810) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45637](/vuln.html?cve=2026-45637) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Defender for Endpoint for Mac Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45647](/vuln.html?cve=2026-45647) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Dynamics 365 (on-premises) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40371](/vuln.html?cve=2026-40371) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-44822](/vuln.html?cve=2026-44822) | No | No | - | - | Important | 8.2 | 7.1 |
| [CVE-2026-45455](/vuln.html?cve=2026-45455) | No | No | - | - | Important | 3.3 | 2.9 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45469](/vuln.html?cve=2026-45469) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44817](/vuln.html?cve=2026-44817) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44818](/vuln.html?cve=2026-44818) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-44820](/vuln.html?cve=2026-44820) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44823](/vuln.html?cve=2026-44823) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Excel Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45459](/vuln.html?cve=2026-45459) | No | No | - | - | Important | 3.3 | 2.9 |
| Microsoft Exchange Online Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-48579](/vuln.html?cve=2026-48579) | No | No | - | - | Critical | 9.1 | 7.9 |
| Microsoft Exchange Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45504](/vuln.html?cve=2026-45504) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Exchange Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45502](/vuln.html?cve=2026-45502) | No | No | - | - | Important | 5.0 | 4.4 |
| [CVE-2026-45503](/vuln.html?cve=2026-45503) | No | No | - | - | Important | 8.1 | 7.1 |
| Microsoft Exchange Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45583](/vuln.html?cve=2026-45583) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Exchange Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45500](/vuln.html?cve=2026-45500) | No | No | - | - | Important | 6.1 | 5.3 |
| [CVE-2026-45501](/vuln.html?cve=2026-45501) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-47631](/vuln.html?cve=2026-47631) | No | No | - | - | Important | 8.1 | 7.1 |
| Microsoft Graph Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-47655](/vuln.html?cve=2026-47655) | No | No | - | - | Critical | 6.5 | 5.7 |
| Microsoft Graphics Component Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42986](/vuln.html?cve=2026-42986) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Kinect Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41092](/vuln.html?cve=2026-41092) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Live Share Canvas SDK Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45644](/vuln.html?cve=2026-45644) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft M365 Copilot Remote Code Execution Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-45497](/vuln.html?cve=2026-45497) | No | No | - | - | Critical | 7.7 | 6.7 |
| Microsoft Office Click-To-Run Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-47293](/vuln.html?cve=2026-47293) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Office Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45485](/vuln.html?cve=2026-45485) | No | No | - | - | Important | 3.3 | 2.9 |
| [CVE-2026-44821](/vuln.html?cve=2026-44821) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-45460](/vuln.html?cve=2026-45460) | No | No | - | - | Critical | 4.7 | 4.1 |
| Microsoft Office Project Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45483](/vuln.html?cve=2026-45483) | No | No | - | - | Important | 4.6 | 4.0 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45475](/vuln.html?cve=2026-45475) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45472](/vuln.html?cve=2026-45472) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-45474](/vuln.html?cve=2026-45474) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-44819](/vuln.html?cve=2026-44819) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44824](/vuln.html?cve=2026-44824) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45461](/vuln.html?cve=2026-45461) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-45645](/vuln.html?cve=2026-45645) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45463](/vuln.html?cve=2026-45463) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Outlook and Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45456](/vuln.html?cve=2026-45456) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-45458](/vuln.html?cve=2026-45458) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-47635](/vuln.html?cve=2026-47635) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft PC Manager Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-49161](/vuln.html?cve=2026-49161) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft PowerToys Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42902](/vuln.html?cve=2026-42902) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft SharePoint Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45484](/vuln.html?cve=2026-45484) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45454](/vuln.html?cve=2026-45454) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47298](/vuln.html?cve=2026-47298) | No | No | - | - | Important | 8.0 | 7.0 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45467](/vuln.html?cve=2026-45467) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-45468](/vuln.html?cve=2026-45468) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-45479](/vuln.html?cve=2026-45479) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-45453](/vuln.html?cve=2026-45453) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-47636](/vuln.html?cve=2026-47636) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-47637](/vuln.html?cve=2026-47637) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-47638](/vuln.html?cve=2026-47638) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-47639](/vuln.html?cve=2026-47639) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-47641](/vuln.html?cve=2026-47641) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-33113](/vuln.html?cve=2026-33113) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-45462](/vuln.html?cve=2026-45462) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-45464](/vuln.html?cve=2026-45464) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-45465](/vuln.html?cve=2026-45465) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-47634](/vuln.html?cve=2026-47634) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-47640](/vuln.html?cve=2026-47640) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-45481](/vuln.html?cve=2026-45481) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-48560](/vuln.html?cve=2026-48560) | No | No | - | - | Important | 5.4 | 4.7 |
| [CVE-2026-48562](/vuln.html?cve=2026-48562) | No | No | - | - | Important | 4.6 | 4.0 |
| Microsoft Teams for Android Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-42835](/vuln.html?cve=2026-42835) | No | No | - | - | Important | 8.1 | 7.1 |
| Microsoft UxTheme Library (uxtheme.dll) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-45606](/vuln.html?cve=2026-45606) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Visual Studio Code CoPilot Chat Extension Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45482](/vuln.html?cve=2026-45482) | No | No | - | - | Important | 8.4 | 7.3 |
| Microsoft Word Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45466](/vuln.html?cve=2026-45466) | No | No | - | - | Important | 3.3 | 2.9 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45471](/vuln.html?cve=2026-45471) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45486](/vuln.html?cve=2026-45486) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45643](/vuln.html?cve=2026-45643) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45457](/vuln.html?cve=2026-45457) | No | No | - | - | Important | 7.8 | 6.8 |
| NT OS Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42980](/vuln.html?cve=2026-42980) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42916](/vuln.html?cve=2026-42916) | No | No | - | - | Important | 7.8 | 6.8 |
| Nuance PowerScribe Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-26142](/vuln.html?cve=2026-26142) | No | No | - | - | Critical | 9.8 | 8.5 |
| Office for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-45649](/vuln.html?cve=2026-45649) | No | No | - | - | Important | 7.1 | 6.2 |
| Remote Desktop Client Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47289](/vuln.html?cve=2026-47289) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-47653](/vuln.html?cve=2026-47653) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-47654](/vuln.html?cve=2026-47654) | No | No | - | - | Critical | 7.5 | 6.6 |
| [CVE-2026-48563](/vuln.html?cve=2026-48563) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-42909](/vuln.html?cve=2026-42909) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-42913](/vuln.html?cve=2026-42913) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-42992](/vuln.html?cve=2026-42992) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-44799](/vuln.html?cve=2026-44799) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-44801](/vuln.html?cve=2026-44801) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-42985](/vuln.html?cve=2026-42985) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-42993](/vuln.html?cve=2026-42993) | No | No | - | - | Important | 7.5 | 6.5 |
| Secure Boot Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45588](/vuln.html?cve=2026-45588) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-48568](/vuln.html?cve=2026-48568) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-48570](/vuln.html?cve=2026-48570) | No | No | - | - | Important | 7.9 | 7.1 |
| [CVE-2026-48573](/vuln.html?cve=2026-48573) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-48575](/vuln.html?cve=2026-48575) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-48576](/vuln.html?cve=2026-48576) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-48578](/vuln.html?cve=2026-48578) | No | No | - | - | Important | 7.9 | 6.9 |
| [CVE-2026-45654](/vuln.html?cve=2026-45654) | No | No | - | - | Important | 7.9 | 6.9 |
| UEFI Secure Boot Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45656](/vuln.html?cve=2026-45656) | No | No | - | - | Important | 7.8 | 6.8 |
| Visual Studio Code Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40376](/vuln.html?cve=2026-40376) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-47281](/vuln.html?cve=2026-47281) | No | No | - | - | Important | 9.6 | 8.3 |
| Visual Studio Code Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-47284](/vuln.html?cve=2026-47284) | No | No | - | - | Important | 6.5 | 5.7 |
| Visual Studio Code MSSQL Extension Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-47292](/vuln.html?cve=2026-47292) | No | No | - | - | Important | 7.8 | 6.8 |
| Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-48569](/vuln.html?cve=2026-48569) | No | No | - | - | Important | 7.1 | 6.2 |
| Visual Studio Code Tampering Vulnerability | | | | | | | |
| [CVE-2026-47287](/vuln.html?cve=2026-47287) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Active Directory Domain Services Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45648](/vuln.html?cve=2026-45648) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows Administrator Protection Secure Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-42829](/vuln.html?cve=2026-42829) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34335](/vuln.html?cve=2026-34335) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-45601](/vuln.html?cve=2026-45601) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-45598](/vuln.html?cve=2026-45598) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-45596](/vuln.html?cve=2026-45596) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-45638](/vuln.html?cve=2026-45638) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45603](/vuln.html?cve=2026-45603) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-42911](/vuln.html?cve=2026-42911) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Application Identity (AppID) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45594](/vuln.html?cve=2026-45594) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45655](/vuln.html?cve=2026-45655) | No | No | - | - | Important | 5.3 | 4.6 |
| [CVE-2026-45658](/vuln.html?cve=2026-45658) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-50507](/vuln.html?cve=2026-50507) | Yes | No | - | - | Important | 6.8 | 6.1 |
| Windows Bluetooth Port Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45640](/vuln.html?cve=2026-45640) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Bluetooth Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45605](/vuln.html?cve=2026-45605) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Boot Manager Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-47656](/vuln.html?cve=2026-47656) | No | No | - | - | Important | 7.9 | 6.9 |
| Windows Collaborative Translation Framework (CTFMON) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45586](/vuln.html?cve=2026-45586) | Yes | No | - | - | Important | 7.8 | 6.8 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-44809](/vuln.html?cve=2026-44809) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DHCP Client Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45634](/vuln.html?cve=2026-45634) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-45608](/vuln.html?cve=2026-45608) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows DNS Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41108](/vuln.html?cve=2026-41108) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42905](/vuln.html?cve=2026-42905) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44811](/vuln.html?cve=2026-44811) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44808](/vuln.html?cve=2026-44808) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44807](/vuln.html?cve=2026-44807) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42983](/vuln.html?cve=2026-42983) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44802](/vuln.html?cve=2026-44802) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44813](/vuln.html?cve=2026-44813) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-44804](/vuln.html?cve=2026-44804) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DWM Core Library Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-48566](/vuln.html?cve=2026-48566) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-44814](/vuln.html?cve=2026-44814) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Deployment Services (WDS) Remote Code Execution | | | | | | | |
| [CVE-2026-42987](/vuln.html?cve=2026-42987) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows Device Health Attestation (DHA) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33828](/vuln.html?cve=2026-33828) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows Dynamic Host Configuration Protocol (DHCP) Tampering Vulnerability | | | | | | | |
| [CVE-2026-45602](/vuln.html?cve=2026-45602) | No | No | - | - | Important | 9.1 | 7.9 |
| Windows Function Discovery Service (fdwsd.dll) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42836](/vuln.html?cve=2026-42836) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Graphics Component Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-44803](/vuln.html?cve=2026-44803) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-44812](/vuln.html?cve=2026-44812) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows Hotpatch Monitoring Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42910](/vuln.html?cve=2026-42910) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Hyper-V Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-42972](/vuln.html?cve=2026-42972) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Hyper-V Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45607](/vuln.html?cve=2026-45607) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-45641](/vuln.html?cve=2026-45641) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-47652](/vuln.html?cve=2026-47652) | No | No | - | - | Critical | 8.2 | 7.1 |
| Windows Internet (wininet.dll) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45592](/vuln.html?cve=2026-45592) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kerberos Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-42903](/vuln.html?cve=2026-42903) | No | No | - | - | Important | 6.5 | 5.7 |
| [CVE-2026-42914](/vuln.html?cve=2026-42914) | No | No | - | - | Important | 5.3 | 4.6 |
| Windows Kerberos Key Distribution Center (KDC) Remote Code Execution | | | | | | | |
| [CVE-2026-47288](/vuln.html?cve=2026-47288) | No | No | - | - | Critical | 7.1 | 6.2 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-48583](/vuln.html?cve=2026-48583) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-45653](/vuln.html?cve=2026-45653) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-42984](/vuln.html?cve=2026-42984) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Kernel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45657](/vuln.html?cve=2026-45657) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows Kernel-Mode Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45600](/vuln.html?cve=2026-45600) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Managed Installer Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45604](/vuln.html?cve=2026-45604) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Mark of the Web Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-45595](/vuln.html?cve=2026-45595) | No | No | - | - | Important | 5.4 | 4.7 |
| Windows Media Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-48574](/vuln.html?cve=2026-48574) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows NTFS Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45636](/vuln.html?cve=2026-45636) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows NTLM Spoofing Vulnerability | | | | | | | |
| [CVE-2026-50508](/vuln.html?cve=2026-50508) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Narrator Braille Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-48565](/vuln.html?cve=2026-48565) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Network Controller (NC) Host Agent Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-44805](/vuln.html?cve=2026-44805) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Performance Monitor Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-42981](/vuln.html?cve=2026-42981) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-42974](/vuln.html?cve=2026-42974) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Program Compatibility Assistant Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45487](/vuln.html?cve=2026-45487) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42828](/vuln.html?cve=2026-42828) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42837](/vuln.html?cve=2026-42837) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Push Notification Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-42969](/vuln.html?cve=2026-42969) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-42971](/vuln.html?cve=2026-42971) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-42970](/vuln.html?cve=2026-42970) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-42973](/vuln.html?cve=2026-42973) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Push Notifications Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42978](/vuln.html?cve=2026-42978) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42977](/vuln.html?cve=2026-42977) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42979](/vuln.html?cve=2026-42979) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-42991](/vuln.html?cve=2026-42991) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Remote Desktop Protocol (RDP) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-45639](/vuln.html?cve=2026-45639) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-42908](/vuln.html?cve=2026-42908) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows SDK Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45593](/vuln.html?cve=2026-45593) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Shell Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-42906](/vuln.html?cve=2026-42906) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-42907](/vuln.html?cve=2026-42907) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Storage Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-47648](/vuln.html?cve=2026-47648) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows TCP/IP Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-42915](/vuln.html?cve=2026-42915) | No | No | - | - | Important | 5.7 | 5.0 |
| Windows TCP/IP Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42904](/vuln.html?cve=2026-42904) | No | No | - | - | Important | 9.6 | 8.3 |
| Windows Telephony Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-42968](/vuln.html?cve=2026-42968) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Telephony Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42912](/vuln.html?cve=2026-42912) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows UI Automation Manager (uiamanager.dll) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-45597](/vuln.html?cve=2026-45597) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows UPnP Device Host Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-45599](/vuln.html?cve=2026-45599) | No | No | - | - | Important | 8.1 | 7.1 |
| [CVE-2026-45635](/vuln.html?cve=2026-45635) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Universal Disk Format File System Driver (UDFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40409](/vuln.html?cve=2026-40409) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40404](/vuln.html?cve=2026-40404) | No | No | - | - | Important | 7.8 | 6.8 |
| Winlogon Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42989](/vuln.html?cve=2026-42989) | No | No | - | - | Important | 7.8 | 6.8 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[microsoft patch tuesday patches](/tag.html?tag=microsoft patch tuesday patches)

[0 comment(s)](/diary/Microsoft+June+2026+Patch+Tuesday/33064/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33060)
* [next](/diary/33068)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)