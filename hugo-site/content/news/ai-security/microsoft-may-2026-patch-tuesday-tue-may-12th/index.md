---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:16:49.298126+00:00'
exported_at: '2026-05-14T21:16:53.810662+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32980
structured_data:
  about: []
  author: ''
  description: 'Microsoft May 2026 Patch Tuesday, Author: Johannes Ullrich'
  headline: Microsoft May 2026 Patch Tuesday, (Tue, May 12th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32980
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft May 2026 Patch Tuesday, (Tue, May 12th)
updated_at: '2026-05-14T21:16:49.298126+00:00'
url_hash: 972e412bdddbb530ea4d69400f6aec9db4e88dfb
---

# [Microsoft May 2026 Patch Tuesday](/forums/diary/Microsoft+May+2026+Patch+Tuesday/32980/)

**Published**
: 2026-05-12.
**Last Updated**
: 2026-05-12 18:29:36 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Microsoft+May+2026+Patch+Tuesday/32980/#comments)

Today's Microsoft patch Tuesday fixes 137 different vulnerabilities. In addition, the update addresses 137 Chromium-related issues affecting Microsoft Edge.

There are no already disclosed or already exploited vulnerabilities included in today's patches. I removed the Chromium issues from the table below and included only the 137 Microsoft issues to make it more readable.

Note that issues related to Microsoft Azure are labeled as "no customer action required.

Significant Vulnerabilities of interest:

CVE-2026-41103: This vulnerability affects the Microsoft SSO Plugin for Jira & Confluence. Exploitation could lead to an elevation of privileges. With ongoing supply chain attacks, development and CI/CD tools like Jira and Confluence are popular targets.

CVE-2026-41089: A preauthentication remote code execution vulnerability in the Netlogon service will always be a juicy target, worth some AI tokens to write an exploit for.

Other critical vulnerabilities include the usual Word and Microsoft Office issues.

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Core Tampering Vulnerability | | | | | | | |
| [CVE-2026-32175](/vuln.html?cve=2026-32175) | No | No | - | - | Important | 4.3 | 3.8 |
| .NET Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32177](/vuln.html?cve=2026-32177) | No | No | - | - | Important | 7.3 | 6.4 |
| [CVE-2026-35433](/vuln.html?cve=2026-35433) | No | No | - | - | Important | 7.3 | 6.4 |
| ASP.NET Core Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-42899](/vuln.html?cve=2026-42899) | No | No | - | - | Important | 7.5 | 6.5 |
| Azure AI Foundry Elevation of Privilege Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-35435](/vuln.html?cve=2026-35435) | No | No | - | - | Critical | 8.6 | 7.5 |
| Azure Cloud Shell Spoofing Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-35428](/vuln.html?cve=2026-35428) | No | No | - | - | Critical | 9.6 | 8.3 |
| Azure Connected Machine Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40381](/vuln.html?cve=2026-40381) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure DevOps Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-42826](/vuln.html?cve=2026-42826) | No | No | - | - | Critical | 10.0 | 8.7 |
| Azure Logic Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42823](/vuln.html?cve=2026-42823) | No | No | - | - | Important | 9.9 | 8.6 |
| Azure Machine Learning Notebook Spoofing Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-32207](/vuln.html?cve=2026-32207) | No | No | - | - | Critical | 8.8 | 7.7 |
| [CVE-2026-33833](/vuln.html?cve=2026-33833) | No | No | - | - | Important | 8.2 | 7.1 |
| Azure Managed Instance for Apache Cassandra Remote Code Execution Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-33109](/vuln.html?cve=2026-33109) | No | No | - | - | Critical | 9.9 | 8.6 |
| [CVE-2026-33844](/vuln.html?cve=2026-33844) | No | No | - | - | Critical | 9.0 | 7.8 |
| Azure Monitor Action Group Notification System Elevation of Privilege Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-41105](/vuln.html?cve=2026-41105) | No | No | - | - | Critical | 8.1 | 7.1 |
| Azure Monitor Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32204](/vuln.html?cve=2026-32204) | No | No | - | - | Important | 7.8 | 6.8 |
| Azure Monitor Agent Metrics Extension Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42830](/vuln.html?cve=2026-42830) | No | No | - | - | Important | 6.5 | 5.7 |
| Azure SDK for Java Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-33117](/vuln.html?cve=2026-33117) | No | No | - | - | Important | 9.1 | 7.9 |
| Copilot Chat (Microsoft Edge) Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-33111](/vuln.html?cve=2026-33111) | No | No | - | - | Critical | 7.5 | 6.5 |
| Data Deduplication Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41095](/vuln.html?cve=2026-41095) | No | No | - | - | Important | 7.8 | 6.8 |
| GitHub Copilot and Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-41109](/vuln.html?cve=2026-41109) | No | No | - | - | Important | 8.8 | 7.7 |
| Internet Key Exchange (IKE) Protocol Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-35424](/vuln.html?cve=2026-35424) | No | No | - | - | Important | 7.5 | 6.5 |
| M365 Copilot Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-26129](/vuln.html?cve=2026-26129) | No | No | - | - | Critical | 7.5 | 6.5 |
| [CVE-2026-26164](/vuln.html?cve=2026-26164) | No | No | - | - | Critical | 7.5 | 6.5 |
| M365 Copilot for Desktop Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41614](/vuln.html?cve=2026-41614) | No | No | - | - | Important | 6.2 | 5.4 |
| Microsoft 365 Copilot for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41100](/vuln.html?cve=2026-41100) | No | No | - | - | Important | 4.4 | 3.9 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40377](/vuln.html?cve=2026-40377) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Data Formulator Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-41094](/vuln.html?cve=2026-41094) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Dynamics 365 Business Central Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40417](/vuln.html?cve=2026-40417) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Dynamics 365 Customer Insights Elevation of Privilege Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-33821](/vuln.html?cve=2026-33821) | No | No | - | - | Critical | 7.7 | 6.7 |
| Microsoft Dynamics 365 On-Premises Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-42898](/vuln.html?cve=2026-42898) | No | No | - | - | Critical | 9.9 | 8.6 |
| [CVE-2026-42833](/vuln.html?cve=2026-42833) | No | No | - | - | Important | 9.1 | 7.9 |
| Microsoft Edge (Chromium-based) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42838](/vuln.html?cve=2026-42838) | No | No | - | - | Important | 5.4 | 4.7 |
| Microsoft Edge (Chromium-based) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-41107](/vuln.html?cve=2026-41107) | No | No | - | - | Moderate | 7.4 | 6.4 |
| Microsoft Edge (Chromium-based) for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-42891](/vuln.html?cve=2026-42891) | No | No | - | - | Moderate | 6.5 | 5.7 |
| [CVE-2026-35429](/vuln.html?cve=2026-35429) | No | No | - | - | Moderate | 4.3 | 3.9 |
| [CVE-2026-40416](/vuln.html?cve=2026-40416) | No | No | - | - | Low | 4.3 | 3.8 |
| Microsoft Enterprise Security Token Service (ESTS) Spoofing Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-40379](/vuln.html?cve=2026-40379) | No | No | - | - | Critical | 9.3 | 8.1 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-40360](/vuln.html?cve=2026-40360) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40359](/vuln.html?cve=2026-40359) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40362](/vuln.html?cve=2026-40362) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Message Queuing (MSMQ) Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-34329](/vuln.html?cve=2026-34329) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Click-To-Run Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40419](/vuln.html?cve=2026-40419) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40418](/vuln.html?cve=2026-40418) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-35436](/vuln.html?cve=2026-35436) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-40420](/vuln.html?cve=2026-40420) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40363](/vuln.html?cve=2026-40363) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-42831](/vuln.html?cve=2026-42831) | No | No | - | - | Critical | 7.8 | 6.8 |
| [CVE-2026-40358](/vuln.html?cve=2026-40358) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Office Spoofing Vulnerability | | | | | | | |
| [CVE-2026-42832](/vuln.html?cve=2026-42832) | No | No | - | - | Important | 7.7 | 6.7 |
| Microsoft Outlook for iOS Tampering Vulnerability | | | | | | | |
| [CVE-2026-42893](/vuln.html?cve=2026-42893) | No | No | - | - | Important | 7.4 | 6.4 |
| Microsoft Partner Center Spoofing Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-34327](/vuln.html?cve=2026-34327) | No | No | - | - | Critical | 8.2 | 7.1 |
| Microsoft Power Automate Desktop Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-40374](/vuln.html?cve=2026-40374) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft PowerPoint for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41102](/vuln.html?cve=2026-41102) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft SSO Plugin for Jira & Confluence Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41103](/vuln.html?cve=2026-41103) | No | No | - | - | Critical | 9.1 | 7.9 |
| Microsoft SharePoint Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-35439](/vuln.html?cve=2026-35439) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-40368](/vuln.html?cve=2026-40368) | No | No | - | - | Important | 8.0 | 7.0 |
| [CVE-2026-33110](/vuln.html?cve=2026-33110) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-33112](/vuln.html?cve=2026-33112) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-40357](/vuln.html?cve=2026-40357) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-40365](/vuln.html?cve=2026-40365) | No | No | - | - | Critical | 8.8 | 7.7 |
| Microsoft Team Events Portal Information Disclosure Vulnerability   (no customer action required) | | | | | | | |
| [CVE-2026-33823](/vuln.html?cve=2026-33823) | No | No | - | - | Critical | 9.6 | 8.3 |
| Microsoft Teams Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32185](/vuln.html?cve=2026-32185) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Word Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-35440](/vuln.html?cve=2026-35440) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-40421](/vuln.html?cve=2026-40421) | No | No | - | - | Important | 4.3 | 3.8 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40364](/vuln.html?cve=2026-40364) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-40366](/vuln.html?cve=2026-40366) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-40361](/vuln.html?cve=2026-40361) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-40367](/vuln.html?cve=2026-40367) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Word for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-41101](/vuln.html?cve=2026-41101) | No | No | - | - | Important | 7.1 | 6.2 |
| SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40370](/vuln.html?cve=2026-40370) | No | No | - | - | Important | 8.8 | 7.7 |
| Secure Boot Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-41097](/vuln.html?cve=2026-41097) | No | No | - | - | Important | 6.7 | 5.8 |
| Visual Studio Code Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41613](/vuln.html?cve=2026-41613) | No | No | - | - | Important | 8.8 | 7.7 |
| Visual Studio Code Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-41612](/vuln.html?cve=2026-41612) | No | No | - | - | Important | 5.5 | 4.8 |
| Visual Studio Code Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-41611](/vuln.html?cve=2026-41611) | No | No | - | - | Important | 7.8 | 6.8 |
| Visual Studio Code Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-41610](/vuln.html?cve=2026-41610) | No | No | - | - | Important | 6.3 | 5.5 |
| Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33839](/vuln.html?cve=2026-33839) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-33840](/vuln.html?cve=2026-33840) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34330](/vuln.html?cve=2026-34330) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34331](/vuln.html?cve=2026-34331) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows 11 Telnet Client Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-35423](/vuln.html?cve=2026-35423) | No | No | - | - | Important | 5.4 | 4.7 |
| Windows Admin Center Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-35438](/vuln.html?cve=2026-35438) | No | No | - | - | Important | 8.3 | 7.2 |
| Windows Admin Center in Azure Portal Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-41086](/vuln.html?cve=2026-41086) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34344](/vuln.html?cve=2026-34344) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34345](/vuln.html?cve=2026-34345) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-35416](/vuln.html?cve=2026-35416) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-41088](/vuln.html?cve=2026-41088) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Application Identity (AppID) Subsystem Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34343](/vuln.html?cve=2026-34343) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-35418](/vuln.html?cve=2026-35418) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-33835](/vuln.html?cve=2026-33835) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34337](/vuln.html?cve=2026-34337) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40407](/vuln.html?cve=2026-40407) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40397](/vuln.html?cve=2026-40397) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DNS Client Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-41096](/vuln.html?cve=2026-41096) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows DWM Core Library Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42896](/vuln.html?cve=2026-42896) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows DWM Core Library Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-35419](/vuln.html?cve=2026-35419) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-34336](/vuln.html?cve=2026-34336) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Event Logging Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33834](/vuln.html?cve=2026-33834) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Filtering Platform (WFP) Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-32209](/vuln.html?cve=2026-32209) | No | No | - | - | Important | 4.4 | 3.9 |
| Windows GDI Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-35421](/vuln.html?cve=2026-35421) | No | No | - | - | Critical | 7.8 | 6.8 |
| Windows Graphics Component Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40403](/vuln.html?cve=2026-40403) | No | No | - | - | Critical | 8.8 | 7.7 |
| Windows Hyper-V Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40402](/vuln.html?cve=2026-40402) | No | No | - | - | Critical | 9.3 | 8.1 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33841](/vuln.html?cve=2026-33841) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-35420](/vuln.html?cve=2026-35420) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40369](/vuln.html?cve=2026-40369) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kernel-Mode Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-34332](/vuln.html?cve=2026-34332) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows Lightweight Directory Access Protocol (LDAP) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-34339](/vuln.html?cve=2026-34339) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Link-Layer Discovery Protocol (LLDP) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34341](/vuln.html?cve=2026-34341) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Message Queuing (MSMQ) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33838](/vuln.html?cve=2026-33838) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Native WiFi Miniport Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32161](/vuln.html?cve=2026-32161) | No | No | - | - | Critical | 7.5 | 6.5 |
| Windows Netlogon Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-41089](/vuln.html?cve=2026-41089) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows Print Spooler Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34342](/vuln.html?cve=2026-34342) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34340](/vuln.html?cve=2026-34340) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Remote Desktop Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40398](/vuln.html?cve=2026-40398) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Rich Text Edit Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-21530](/vuln.html?cve=2026-21530) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-32170](/vuln.html?cve=2026-32170) | No | No | - | - | Important | 6.7 | 5.8 |
| Windows SMB Client Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40410](/vuln.html?cve=2026-40410) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Storage Spaces Controller Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-35415](/vuln.html?cve=2026-35415) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Storport Miniport Driver Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-34350](/vuln.html?cve=2026-34350) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows TCP/IP Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-40405](/vuln.html?cve=2026-40405) | No | No | - | - | Important | 7.5 | 6.5 |
| [CVE-2026-40414](/vuln.html?cve=2026-40414) | No | No | - | - | Important | 7.4 | 6.4 |
| [CVE-2026-40401](/vuln.html?cve=2026-40401) | No | No | - | - | Important | 7.1 | 6.2 |
| [CVE-2026-40413](/vuln.html?cve=2026-40413) | No | No | - | - | Important | 7.4 | 6.4 |
| Windows TCP/IP Driver Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-35422](/vuln.html?cve=2026-35422) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows TCP/IP Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34351](/vuln.html?cve=2026-34351) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40399](/vuln.html?cve=2026-40399) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34334](/vuln.html?cve=2026-34334) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows TCP/IP Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-40406](/vuln.html?cve=2026-40406) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows TCP/IP Local Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33837](/vuln.html?cve=2026-33837) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows TCP/IP Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40415](/vuln.html?cve=2026-40415) | No | No | - | - | Important | 8.1 | 7.1 |
| Windows Telephony Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-42825](/vuln.html?cve=2026-42825) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-34338](/vuln.html?cve=2026-34338) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-40382](/vuln.html?cve=2026-40382) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Volume Manager Extension Driver Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-40380](/vuln.html?cve=2026-40380) | No | No | - | - | Important | 6.2 | 5.4 |
| Windows WAN ARP Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-40408](/vuln.html?cve=2026-40408) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-34333](/vuln.html?cve=2026-34333) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-34347](/vuln.html?cve=2026-34347) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-35417](/vuln.html?cve=2026-35417) | No | No | - | - | Important | 7.8 | 6.8 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[microsoft patch Tuesday](/tag.html?tag=microsoft patch Tuesday)

[0 comment(s)](/diary/Microsoft+May+2026+Patch+Tuesday/32980/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32976)
* [next](/diary/32982)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)