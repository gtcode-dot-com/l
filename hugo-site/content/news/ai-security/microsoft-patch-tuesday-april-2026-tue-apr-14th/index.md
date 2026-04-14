---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T18:15:17.084563+00:00'
exported_at: '2026-04-14T18:15:19.396865+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32898
structured_data:
  about: []
  author: ''
  description: 'Microsoft Patch Tuesday April 2026., Author: Johannes Ullrich'
  headline: Microsoft Patch Tuesday April 2026., (Tue, Apr 14th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32898
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patch Tuesday April 2026., (Tue, Apr 14th)
updated_at: '2026-04-14T18:15:17.084563+00:00'
url_hash: 9e609ccde5b1f245b2fd9976a7653a9a5a4dae0a
---

# [Microsoft Patch Tuesday April 2026.](/forums/diary/Microsoft+Patch+Tuesday+April+2026/32898/)

**Published**
: 2026-04-14.
**Last Updated**
: 2026-04-14 17:46:09 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Microsoft+Patch+Tuesday+April+2026/32898/#comments)

This month's Microsoft Patch Tuesday looks like a record one, but let's look at it a bit closer to understand what is happening

The update patches a total of 243 vulnerabilities. However, 78 of them are Chromium issues affecting Microsoft Edge. Patches for Edge were released earlier. This leaves 165 vulnerabilities that are not Edge-related. Of these, 8 are rated critical, and 154 are important. One vulnerability has already been exploited, and another was made public before today but has not yet been seen in the wild.

Noteworthy Vulnerabilities:

CVE-2026-33827 (Windows TCP/IP Remote Code Execution Vulnerability): As a packet nerd, I love these types of vulnerabilities. Need to know more to really figure out the impact. Microsoft describes this as a race condition, allowing attackers to execute arbitrary code over the network. Exploitation is likely tricky, but never underestimate the creativity of an AI aided attacker.

CVE-2026-33825 (Microsoft Defender Elevation of Privilege Vulnerability): This vulnerability has already been disclosed.

CVE-2026-32201 (Microsoft SharePoint Server Spoofing Vulnerability): Two similar SharePoint server spoofing vulnerabilities were patched this month. Both are rated important, and this particular one is already being exploited.

CVE-2026-33826 (Windows Active Directory Remote Code Execution Vulnerability): CVSS score of "only" 8.0, but critical according to Microsoft.

CVE-2026-32190 (Microsoft Office Remote Code Execution Vulnerability): Standard fair for every monthly patch Tuesday. These are often the more worrisome vulnerabilities. Two additional critical RCE vulnerabilities affect Word (CVE-2026-33114, CVE-2026-33115).

CVE-2026-32157 (Remote Desktop Client Remote Code Execution Vulnerability): Typically, these vulnerabilities require a user to connect to a malicious RDP server, but connections may be initiated by clicking on an "rdp:" link.

CVE-2026-33824 (Windows Internet Key Exchange (IKE) Service Extensions Remote Code Execution Vulnerability): IKE, part of IPSEC, is usually not enabled by default. It isn't clear yet what the exact exploitation requirements are (will update once MSFT's page responds again)

CVE-2026-23666 (.NET Framework Denial of Service Vulnerability): Just a denial of service. Not sure why this deserved "critical".

| Description | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CVE | Disclosed | Exploited | Exploitability (old versions) | current version | Severity | CVSS Base (AVG) | CVSS Temporal (AVG) |
| .NET Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-26171](/vuln.html?cve=2026-26171) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET Framework Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32226](/vuln.html?cve=2026-32226) | No | No | - | - | Important | 5.9 | 5.2 |
| [CVE-2026-23666](/vuln.html?cve=2026-23666) | No | No | - | - | Critical | 7.5 | 6.7 |
| .NET Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32178](/vuln.html?cve=2026-32178) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32203](/vuln.html?cve=2026-32203) | No | No | - | - | Important | 7.5 | 6.5 |
| .NET, .NET Framework, and Visual Studio Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-33116](/vuln.html?cve=2026-33116) | No | No | - | - | Important | 7.5 | 6.5 |
| Active Directory Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32072](/vuln.html?cve=2026-32072) | No | No | - | - | Important | 6.2 | 5.4 |
| Applocker Filter Driver (applockerfltr.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-25184](/vuln.html?cve=2026-25184) | No | No | - | - | Important | 7.0 | 6.1 |
| Azure Logic Apps Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32171](/vuln.html?cve=2026-32171) | No | No | - | - | Important | 8.8 | 7.7 |
| Azure Monitor Agent Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32168](/vuln.html?cve=2026-32168) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32192](/vuln.html?cve=2026-32192) | No | No | - | - | Important | 7.8 | 6.8 |
| Chromium: CVE-2026-5272 Heap buffer overflow in GPU | | | | | | | |
| [CVE-2026-5272](/vuln.html?cve=2026-5272) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5273 Use after free in CSS | | | | | | | |
| [CVE-2026-5273](/vuln.html?cve=2026-5273) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5274 Integer overflow in Codecs | | | | | | | |
| [CVE-2026-5274](/vuln.html?cve=2026-5274) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5275 Heap buffer overflow in ANGLE | | | | | | | |
| [CVE-2026-5275](/vuln.html?cve=2026-5275) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5276 Insufficient policy enforcement in WebUSB | | | | | | | |
| [CVE-2026-5276](/vuln.html?cve=2026-5276) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5277 Integer overflow in ANGLE | | | | | | | |
| [CVE-2026-5277](/vuln.html?cve=2026-5277) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5279 Object corruption in V8 | | | | | | | |
| [CVE-2026-5279](/vuln.html?cve=2026-5279) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5280 Use after free in WebCodecs | | | | | | | |
| [CVE-2026-5280](/vuln.html?cve=2026-5280) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5281 Use after free in Dawn | | | | | | | |
| [CVE-2026-5281](/vuln.html?cve=2026-5281) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5283 Inappropriate implementation in ANGLE | | | | | | | |
| [CVE-2026-5283](/vuln.html?cve=2026-5283) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5284 Use after free in Dawn | | | | | | | |
| [CVE-2026-5284](/vuln.html?cve=2026-5284) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5285 Use after free in WebGL | | | | | | | |
| [CVE-2026-5285](/vuln.html?cve=2026-5285) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5286 Use after free in Dawn | | | | | | | |
| [CVE-2026-5286](/vuln.html?cve=2026-5286) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5287 Use after free in PDF | | | | | | | |
| [CVE-2026-5287](/vuln.html?cve=2026-5287) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5289 Use after free in Navigation | | | | | | | |
| [CVE-2026-5289](/vuln.html?cve=2026-5289) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5290 Use after free in Compositing | | | | | | | |
| [CVE-2026-5290](/vuln.html?cve=2026-5290) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5291 Inappropriate implementation in WebGL | | | | | | | |
| [CVE-2026-5291](/vuln.html?cve=2026-5291) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5292 Out of bounds read in WebCodecs | | | | | | | |
| [CVE-2026-5292](/vuln.html?cve=2026-5292) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5858 Heap buffer overflow in WebML | | | | | | | |
| [CVE-2026-5858](/vuln.html?cve=2026-5858) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5859 Integer overflow in WebML | | | | | | | |
| [CVE-2026-5859](/vuln.html?cve=2026-5859) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5860 Use after free in WebRTC | | | | | | | |
| [CVE-2026-5860](/vuln.html?cve=2026-5860) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5861 Use after free in V8 | | | | | | | |
| [CVE-2026-5861](/vuln.html?cve=2026-5861) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5862 Inappropriate implementation in V8 | | | | | | | |
| [CVE-2026-5862](/vuln.html?cve=2026-5862) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5863 Inappropriate implementation in V8 | | | | | | | |
| [CVE-2026-5863](/vuln.html?cve=2026-5863) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5864 Heap buffer overflow in WebAudio | | | | | | | |
| [CVE-2026-5864](/vuln.html?cve=2026-5864) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5865 Type Confusion in V8 | | | | | | | |
| [CVE-2026-5865](/vuln.html?cve=2026-5865) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5866 Use after free in Media | | | | | | | |
| [CVE-2026-5866](/vuln.html?cve=2026-5866) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5867 Heap buffer overflow in WebML | | | | | | | |
| [CVE-2026-5867](/vuln.html?cve=2026-5867) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5868 Heap buffer overflow in ANGLE | | | | | | | |
| [CVE-2026-5868](/vuln.html?cve=2026-5868) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5869 Heap buffer overflow in WebML | | | | | | | |
| [CVE-2026-5869](/vuln.html?cve=2026-5869) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5870 Integer overflow in Skia | | | | | | | |
| [CVE-2026-5870](/vuln.html?cve=2026-5870) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5871 Type Confusion in V8 | | | | | | | |
| [CVE-2026-5871](/vuln.html?cve=2026-5871) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5872 Use after free in Blink | | | | | | | |
| [CVE-2026-5872](/vuln.html?cve=2026-5872) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5873 Out of bounds read and write in V8 | | | | | | | |
| [CVE-2026-5873](/vuln.html?cve=2026-5873) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5874 Use after free in PrivateAI | | | | | | | |
| [CVE-2026-5874](/vuln.html?cve=2026-5874) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5875 Policy bypass in Blink | | | | | | | |
| [CVE-2026-5875](/vuln.html?cve=2026-5875) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5876 Side-channel information leakage in Navigation | | | | | | | |
| [CVE-2026-5876](/vuln.html?cve=2026-5876) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5877 Use after free in Navigation | | | | | | | |
| [CVE-2026-5877](/vuln.html?cve=2026-5877) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5878 Incorrect security UI in Blink | | | | | | | |
| [CVE-2026-5878](/vuln.html?cve=2026-5878) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5879 Insufficient validation of untrusted input in ANGLE | | | | | | | |
| [CVE-2026-5879](/vuln.html?cve=2026-5879) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5880 Incorrect security UI in browser UI | | | | | | | |
| [CVE-2026-5880](/vuln.html?cve=2026-5880) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5881 Policy bypass in LocalNetworkAccess | | | | | | | |
| [CVE-2026-5881](/vuln.html?cve=2026-5881) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5882 Incorrect security UI in Fullscreen | | | | | | | |
| [CVE-2026-5882](/vuln.html?cve=2026-5882) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5883 Use after free in Media | | | | | | | |
| [CVE-2026-5883](/vuln.html?cve=2026-5883) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5884 Insufficient validation of untrusted input in Media | | | | | | | |
| [CVE-2026-5884](/vuln.html?cve=2026-5884) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5885 Insufficient validation of untrusted input in WebML | | | | | | | |
| [CVE-2026-5885](/vuln.html?cve=2026-5885) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5886 Out of bounds read in WebAudio | | | | | | | |
| [CVE-2026-5886](/vuln.html?cve=2026-5886) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5887 Insufficient validation of untrusted input in Downloads | | | | | | | |
| [CVE-2026-5887](/vuln.html?cve=2026-5887) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5888 Uninitialized Use in WebCodecs | | | | | | | |
| [CVE-2026-5888](/vuln.html?cve=2026-5888) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5889 Cryptographic Flaw in PDFium | | | | | | | |
| [CVE-2026-5889](/vuln.html?cve=2026-5889) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5890 Race in WebCodecs | | | | | | | |
| [CVE-2026-5890](/vuln.html?cve=2026-5890) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5891 Insufficient policy enforcement in browser UI | | | | | | | |
| [CVE-2026-5891](/vuln.html?cve=2026-5891) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5892 Insufficient policy enforcement in PWAs | | | | | | | |
| [CVE-2026-5892](/vuln.html?cve=2026-5892) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5893 Race in V8 | | | | | | | |
| [CVE-2026-5893](/vuln.html?cve=2026-5893) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5894 Inappropriate implementation in PDF | | | | | | | |
| [CVE-2026-5894](/vuln.html?cve=2026-5894) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5895 Incorrect security UI in Omnibox | | | | | | | |
| [CVE-2026-5895](/vuln.html?cve=2026-5895) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5896 Policy bypass in Audio | | | | | | | |
| [CVE-2026-5896](/vuln.html?cve=2026-5896) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5897 Incorrect security UI in Downloads | | | | | | | |
| [CVE-2026-5897](/vuln.html?cve=2026-5897) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5898 Incorrect security UI in Omnibox | | | | | | | |
| [CVE-2026-5898](/vuln.html?cve=2026-5898) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5899 Incorrect security UI in History Navigation | | | | | | | |
| [CVE-2026-5899](/vuln.html?cve=2026-5899) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5900 Policy bypass in Downloads | | | | | | | |
| [CVE-2026-5900](/vuln.html?cve=2026-5900) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5901 Policy bypass in DevTools | | | | | | | |
| [CVE-2026-5901](/vuln.html?cve=2026-5901) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5902 Race in Media | | | | | | | |
| [CVE-2026-5902](/vuln.html?cve=2026-5902) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5903 Policy bypass in IFrameSandbox | | | | | | | |
| [CVE-2026-5903](/vuln.html?cve=2026-5903) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5904 Use after free in V8 | | | | | | | |
| [CVE-2026-5904](/vuln.html?cve=2026-5904) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5905 Incorrect security UI in Permissions | | | | | | | |
| [CVE-2026-5905](/vuln.html?cve=2026-5905) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5906 Incorrect security UI in Omnibox | | | | | | | |
| [CVE-2026-5906](/vuln.html?cve=2026-5906) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5907 Insufficient data validation in Media | | | | | | | |
| [CVE-2026-5907](/vuln.html?cve=2026-5907) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5908 Integer overflow in Media | | | | | | | |
| [CVE-2026-5908](/vuln.html?cve=2026-5908) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5909 Integer overflow in Media | | | | | | | |
| [CVE-2026-5909](/vuln.html?cve=2026-5909) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5910 Integer overflow in Media | | | | | | | |
| [CVE-2026-5910](/vuln.html?cve=2026-5910) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5911 Policy bypass in ServiceWorkers | | | | | | | |
| [CVE-2026-5911](/vuln.html?cve=2026-5911) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5912 Integer overflow in WebRTC | | | | | | | |
| [CVE-2026-5912](/vuln.html?cve=2026-5912) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5913 Out of bounds read in Blink | | | | | | | |
| [CVE-2026-5913](/vuln.html?cve=2026-5913) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5914 Type Confusion in CSS | | | | | | | |
| [CVE-2026-5914](/vuln.html?cve=2026-5914) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5915 Insufficient validation of untrusted input in WebML | | | | | | | |
| [CVE-2026-5915](/vuln.html?cve=2026-5915) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5918 Inappropriate implementation in Navigation | | | | | | | |
| [CVE-2026-5918](/vuln.html?cve=2026-5918) | No | No | - | - | - |  |  |
| Chromium: CVE-2026-5919 Insufficient validation of untrusted input in WebSockets | | | | | | | |
| [CVE-2026-5919](/vuln.html?cve=2026-5919) | No | No | - | - | - |  |  |
| Connected User Experiences and Telemetry Service Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32181](/vuln.html?cve=2026-32181) | No | No | - | - | Important | 5.5 | 4.8 |
| Desktop Window Manager Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27924](/vuln.html?cve=2026-27924) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32152](/vuln.html?cve=2026-32152) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32154](/vuln.html?cve=2026-32154) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-27923](/vuln.html?cve=2026-27923) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32155](/vuln.html?cve=2026-32155) | No | No | - | - | Important | 7.8 | 6.8 |
| GitHub Copilot and Visual Studio Code Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-23653](/vuln.html?cve=2026-23653) | No | No | - | - | Important | 5.7 | 5.0 |
| HTTP.sys Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-33096](/vuln.html?cve=2026-33096) | No | No | - | - | Important | 7.5 | 6.5 |
| Microsoft Brokering File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26181](/vuln.html?cve=2026-26181) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32219](/vuln.html?cve=2026-32219) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32091](/vuln.html?cve=2026-32091) | No | No | - | - | Important | 8.4 | 7.3 |
| Microsoft Cryptographic Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26152](/vuln.html?cve=2026-26152) | No | No | - | - | Important | 7.0 | 6.1 |
| Microsoft Defender Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33825](/vuln.html?cve=2026-33825) | Yes | No | - | - | Important | 7.8 | 7.0 |
| Microsoft Dynamics 365 (On-Premises) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-33103](/vuln.html?cve=2026-33103) | No | No | - | - | Important | 5.5 | 4.8 |
| Microsoft Edge (Chromium-based) Spoofing Vulnerability | | | | | | | |
| [CVE-2026-33118](/vuln.html?cve=2026-33118) | No | No | - | - | Low | 4.3 | 3.8 |
| Microsoft Edge (Chromium-based) for Android Spoofing Vulnerability | | | | | | | |
| [CVE-2026-33119](/vuln.html?cve=2026-33119) | No | No | - | - | Moderate | 5.4 | 4.7 |
| Microsoft Excel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32188](/vuln.html?cve=2026-32188) | No | No | - | - | Important | 7.1 | 6.2 |
| Microsoft Excel Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32189](/vuln.html?cve=2026-32189) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32197](/vuln.html?cve=2026-32197) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32198](/vuln.html?cve=2026-32198) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32199](/vuln.html?cve=2026-32199) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft High Performance Compute (HPC) Pack Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32184](/vuln.html?cve=2026-32184) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Local Security Authority Subsystem Service Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26155](/vuln.html?cve=2026-26155) | No | No | - | - | Important | 6.5 | 5.7 |
| Microsoft Management Console Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27914](/vuln.html?cve=2026-27914) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft Office Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32190](/vuln.html?cve=2026-32190) | No | No | - | - | Critical | 8.4 | 7.3 |
| Microsoft Power Apps Security Feature Bypass | | | | | | | |
| [CVE-2026-26149](/vuln.html?cve=2026-26149) | No | No | - | - | Important | 9.0 | 7.9 |
| Microsoft PowerPoint Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32200](/vuln.html?cve=2026-32200) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft PowerShell Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-26143](/vuln.html?cve=2026-26143) | No | No | - | - | Important | 7.8 | 6.8 |
| Microsoft SQL Server Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-33120](/vuln.html?cve=2026-33120) | No | No | - | - | Important | 8.8 | 7.7 |
| Microsoft SharePoint Server Spoofing Vulnerability | | | | | | | |
| [CVE-2026-20945](/vuln.html?cve=2026-20945) | No | No | - | - | Important | 4.6 | 4.0 |
| [CVE-2026-32201](/vuln.html?cve=2026-32201) | No | Yes | - | - | Important | 6.5 | 6.0 |
| Microsoft Word Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-33822](/vuln.html?cve=2026-33822) | No | No | - | - | Important | 6.1 | 5.3 |
| Microsoft Word Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-33095](/vuln.html?cve=2026-33095) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-23657](/vuln.html?cve=2026-23657) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-33114](/vuln.html?cve=2026-33114) | No | No | - | - | Critical | 8.4 | 7.3 |
| [CVE-2026-33115](/vuln.html?cve=2026-33115) | No | No | - | - | Critical | 8.4 | 7.3 |
| Package Catalog Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32081](/vuln.html?cve=2026-32081) | No | No | - | - | Important | 5.5 | 4.8 |
| PowerShell Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26170](/vuln.html?cve=2026-26170) | No | No | - | - | Important | 7.8 | 6.8 |
| Remote Access Management service/API (RPC server) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26183](/vuln.html?cve=2026-26183) | No | No | - | - | Important | 7.8 | 6.8 |
| Remote Desktop Client Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32157](/vuln.html?cve=2026-32157) | No | No | - | - | Critical | 8.8 | 7.7 |
| Remote Desktop Licensing Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26160](/vuln.html?cve=2026-26160) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26159](/vuln.html?cve=2026-26159) | No | No | - | - | Important | 7.8 | 6.8 |
| Remote Desktop Spoofing Vulnerability | | | | | | | |
| [CVE-2026-26151](/vuln.html?cve=2026-26151) | No | No | - | - | Important | 7.1 | 6.2 |
| Remote Procedure Call Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32085](/vuln.html?cve=2026-32085) | No | No | - | - | Important | 5.5 | 4.8 |
| SQL Server Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32167](/vuln.html?cve=2026-32167) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-32176](/vuln.html?cve=2026-32176) | No | No | - | - | Important | 6.7 | 5.8 |
| UEFI Secure Boot Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-0390](/vuln.html?cve=2026-0390) | No | No | - | - | Important | 6.7 | 5.8 |
| [CVE-2026-32220](/vuln.html?cve=2026-32220) | No | No | - | - | Important | 4.4 | 3.9 |
| Universal Plug and Play (upnp.dll) Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32212](/vuln.html?cve=2026-32212) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-32214](/vuln.html?cve=2026-32214) | No | No | - | - | Important | 5.5 | 4.8 |
| Web Account Manager Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32079](/vuln.html?cve=2026-32079) | No | No | - | - | Important | 5.5 | 4.8 |
| Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33104](/vuln.html?cve=2026-33104) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Active Directory Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-33826](/vuln.html?cve=2026-33826) | No | No | - | - | Critical | 8.0 | 7.0 |
| Windows Admin Center Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32196](/vuln.html?cve=2026-32196) | No | No | - | - | Important | 6.1 | 5.3 |
| Windows Advanced Rasterization Platform Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26178](/vuln.html?cve=2026-26178) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Ancillary Function Driver for WinSock Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32073](/vuln.html?cve=2026-32073) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-26168](/vuln.html?cve=2026-26168) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26173](/vuln.html?cve=2026-26173) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-26177](/vuln.html?cve=2026-26177) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-26182](/vuln.html?cve=2026-26182) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-27922](/vuln.html?cve=2026-27922) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-33099](/vuln.html?cve=2026-33099) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-33100](/vuln.html?cve=2026-33100) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Biometric Service Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-32088](/vuln.html?cve=2026-32088) | No | No | - | - | Important | 6.1 | 5.3 |
| Windows BitLocker Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-27913](/vuln.html?cve=2026-27913) | No | No | - | - | Important | 7.7 | 6.7 |
| Windows Boot Manager Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-26175](/vuln.html?cve=2026-26175) | No | No | - | - | Important | 4.6 | 4.0 |
| Windows COM Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32162](/vuln.html?cve=2026-32162) | No | No | - | - | Important | 8.4 | 7.3 |
| Windows COM Server Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-20806](/vuln.html?cve=2026-20806) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Client Side Caching driver (csc.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26176](/vuln.html?cve=2026-26176) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Cloud Files Mini Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27926](/vuln.html?cve=2026-27926) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Common Log File System Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32070](/vuln.html?cve=2026-32070) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Container Isolation FS Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33098](/vuln.html?cve=2026-33098) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Encrypted File System (EFS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26153](/vuln.html?cve=2026-26153) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Function Discovery Service (fdwsd.dll) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32087](/vuln.html?cve=2026-32087) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32093](/vuln.html?cve=2026-32093) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32086](/vuln.html?cve=2026-32086) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32150](/vuln.html?cve=2026-32150) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows GDI Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-27931](/vuln.html?cve=2026-27931) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-27930](/vuln.html?cve=2026-27930) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Graphics Component Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32221](/vuln.html?cve=2026-32221) | No | No | - | - | Important | 8.4 | 7.3 |
| Windows Hello Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-27906](/vuln.html?cve=2026-27906) | No | No | - | - | Important | 4.4 | 3.9 |
| [CVE-2026-27928](/vuln.html?cve=2026-27928) | No | No | - | - | Important | 8.7 | 7.6 |
| Windows Hyper-V Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-26156](/vuln.html?cve=2026-26156) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32149](/vuln.html?cve=2026-32149) | No | No | - | - | Important | 7.3 | 6.4 |
| Windows Installer Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27910](/vuln.html?cve=2026-27910) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Internet Key Exchange (IKE) Service Extensions Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-33824](/vuln.html?cve=2026-33824) | No | No | - | - | Critical | 9.8 | 8.5 |
| Windows Kerberos Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27912](/vuln.html?cve=2026-27912) | No | No | - | - | Important | 8.0 | 7.0 |
| Windows Kernel Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26179](/vuln.html?cve=2026-26179) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26180](/vuln.html?cve=2026-26180) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32195](/vuln.html?cve=2026-32195) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-26163](/vuln.html?cve=2026-26163) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Kernel Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32215](/vuln.html?cve=2026-32215) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-32217](/vuln.html?cve=2026-32217) | No | No | - | - | Important | 5.5 | 4.8 |
| [CVE-2026-32218](/vuln.html?cve=2026-32218) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Kernel Memory Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-26169](/vuln.html?cve=2026-26169) | No | No | - | - | Important | 6.1 | 5.3 |
| Windows LUA File Virtualization Filter Driver Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27929](/vuln.html?cve=2026-27929) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Local Security Authority Subsystem Service (LSASS) Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32071](/vuln.html?cve=2026-32071) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Management Services Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-20930](/vuln.html?cve=2026-20930) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows OLE Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26162](/vuln.html?cve=2026-26162) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Print Spooler Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-33101](/vuln.html?cve=2026-33101) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Print Spooler Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32084](/vuln.html?cve=2026-32084) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Projected File System Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27927](/vuln.html?cve=2026-27927) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26184](/vuln.html?cve=2026-26184) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32069](/vuln.html?cve=2026-32069) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32074](/vuln.html?cve=2026-32074) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32078](/vuln.html?cve=2026-32078) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Push Notifications Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26167](/vuln.html?cve=2026-26167) | No | No | - | - | Important | 8.8 | 7.7 |
| [CVE-2026-32158](/vuln.html?cve=2026-32158) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32159](/vuln.html?cve=2026-32159) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32160](/vuln.html?cve=2026-32160) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-26172](/vuln.html?cve=2026-26172) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Recovery Environment Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-20928](/vuln.html?cve=2026-20928) | No | No | - | - | Important | 4.6 | 4.0 |
| Windows Redirected Drive Buffering System Denial of Service Vulnerability | | | | | | | |
| [CVE-2026-32216](/vuln.html?cve=2026-32216) | No | No | - | - | Important | 5.5 | 4.8 |
| Windows Search Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27909](/vuln.html?cve=2026-27909) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Sensor Data Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26161](/vuln.html?cve=2026-26161) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Server Update Service (WSUS) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26174](/vuln.html?cve=2026-26174) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32224](/vuln.html?cve=2026-32224) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Server Update Service (WSUS) Tampering Vulnerability | | | | | | | |
| [CVE-2026-26154](/vuln.html?cve=2026-26154) | No | No | - | - | Important | 7.5 | 6.5 |
| Windows Shell Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-26165](/vuln.html?cve=2026-26165) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-26166](/vuln.html?cve=2026-26166) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-27918](/vuln.html?cve=2026-27918) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Shell Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-32151](/vuln.html?cve=2026-32151) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows Shell Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-32225](/vuln.html?cve=2026-32225) | No | No | - | - | Important | 8.8 | 7.7 |
| Windows Shell Spoofing Vulnerability | | | | | | | |
| [CVE-2026-32202](/vuln.html?cve=2026-32202) | No | No | - | - | Important | 4.3 | 3.8 |
| Windows Simple Search and Discovery Protocol (SSDP) Service Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32082](/vuln.html?cve=2026-32082) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32083](/vuln.html?cve=2026-32083) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-32068](/vuln.html?cve=2026-32068) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Snipping Tool Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32183](/vuln.html?cve=2026-32183) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Snipping Tool Spoofing Vulnerability | | | | | | | |
| [CVE-2026-33829](/vuln.html?cve=2026-33829) | No | No | - | - | Moderate | 4.3 | 3.8 |
| Windows Speech Brokered Api Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32089](/vuln.html?cve=2026-32089) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32090](/vuln.html?cve=2026-32090) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Speech Runtime Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32153](/vuln.html?cve=2026-32153) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Storage Spaces Controller Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27907](/vuln.html?cve=2026-27907) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32076](/vuln.html?cve=2026-32076) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows TCP/IP Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-33827](/vuln.html?cve=2026-33827) | No | No | - | - | Critical | 8.1 | 7.1 |
| Windows TDI Translation Driver (tdx.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27908](/vuln.html?cve=2026-27908) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-27921](/vuln.html?cve=2026-27921) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows UPnP Device Host Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27915](/vuln.html?cve=2026-27915) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-27919](/vuln.html?cve=2026-27919) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32075](/vuln.html?cve=2026-32075) | No | No | - | - | Important | 7.0 | 6.1 |
| [CVE-2026-27916](/vuln.html?cve=2026-27916) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-27920](/vuln.html?cve=2026-27920) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32077](/vuln.html?cve=2026-32077) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows UPnP Device Host Information Disclosure Vulnerability | | | | | | | |
| [CVE-2026-27925](/vuln.html?cve=2026-27925) | No | No | - | - | Important | 6.5 | 5.7 |
| Windows UPnP Device Host Remote Code Execution Vulnerability | | | | | | | |
| [CVE-2026-32156](/vuln.html?cve=2026-32156) | No | No | - | - | Important | 7.4 | 6.4 |
| Windows USB Printing Stack (usbprint.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32223](/vuln.html?cve=2026-32223) | No | No | - | - | Important | 6.8 | 5.9 |
| Windows User Interface Core Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32165](/vuln.html?cve=2026-32165) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-27911](/vuln.html?cve=2026-27911) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32163](/vuln.html?cve=2026-32163) | No | No | - | - | Important | 7.8 | 6.8 |
| [CVE-2026-32164](/vuln.html?cve=2026-32164) | No | No | - | - | Important | 7.8 | 6.8 |
| Windows Virtualization-Based Security (VBS) Security Feature Bypass Vulnerability | | | | | | | |
| [CVE-2026-23670](/vuln.html?cve=2026-23670) | No | No | - | - | Important | 5.7 | 5.0 |
| Windows WFP NDIS Lightweight Filter Driver (wfplwfs.sys) Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-27917](/vuln.html?cve=2026-27917) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows WalletService Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32080](/vuln.html?cve=2026-32080) | No | No | - | - | Important | 7.0 | 6.1 |
| Windows Win32k Elevation of Privilege Vulnerability | | | | | | | |
| [CVE-2026-32222](/vuln.html?cve=2026-32222) | No | No | - | - | Important | 7.8 | 6.8 |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[microsoft patch Tuesday](/tag.html?tag=microsoft patch Tuesday)

[0 comment(s)](/diary/Microsoft+Patch+Tuesday+April+2026/32898/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32892)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)