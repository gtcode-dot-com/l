---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-30T08:15:12.772795+00:00'
exported_at: '2026-01-30T08:15:15.188996+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/smartermail-fixes-critical.html
structured_data:
  about: []
  author: ''
  description: SmarterTools fixed critical SmarterMail flaws, including CVSS 9.3 unauthenticated
    RCE and NTLM relay bugs, urging users to update immediately.
  headline: SmarterMail Fixes Critical Unauthenticated RCE Flaw with CVSS 9.3 Score
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/smartermail-fixes-critical.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: SmarterMail Fixes Critical Unauthenticated RCE Flaw with CVSS 9.3 Score
updated_at: '2026-01-30T08:15:12.772795+00:00'
url_hash: 416eddc900c5da296e97bc81ed6cd4a70ba0580d
---

**

Ravie Lakshmanan
**

Jan 30, 2026

Vulnerability / Email Security

SmarterTools has addressed two more security flaws in SmarterMail email software, including one critical security flaw that could result in arbitrary code execution.

The vulnerability, tracked as
**CVE-2026-24423**
, carries a CVSS score of 9.3 out of 10.0.

"SmarterTools SmarterMail versions prior to build 9511 contain an unauthenticated remote code execution vulnerability in the ConnectToHub API method," according to a
[description of the flaw](https://www.cve.org/CVERecord?id=CVE-2026-24423)
in CVE.org.

"The attacker could point the SmarterMail to the malicious HTTP server, which serves the malicious OS [operating system] command. This command will be executed by the vulnerable application."

watchTowr researchers Sina Kheirkhah and Piotr Bazydlo,
[CODE WHITE GmbH's Markus Wulftange](https://code-white.com/public-vulnerability-list/)
, and
[VulnCheck's Cale Black](https://www.vulncheck.com/advisories/smartertools-smartermail-unauthenticated-rce-via-connecttohub-api)
have been credited with discovering and reporting the vulnerability.

The security hole has been addressed in version Build 9511, released on January 15, 2026. The same build also patches another critical flaw (
[CVE-2026-23760](https://thehackernews.com/2026/01/smartermail-auth-bypass-exploited-in.html)
, CVSS score: 9.3) that has since come under active exploitation in the wild.

In addition, SmarterTools has shipped fixes to plug a medium-severity security vulnerability (CVE-2026-25067, CVSS score: 6.9) that could allow an attacker to facilitate NTLM relay attacks and unauthorized network authentication.

It has been described as a case of unauthenticated path coercion affecting the background-of-the-day preview endpoint.

"The application base64-decodes attacker-supplied input and uses it as a filesystem path without validation," VulnCheck
[noted](https://www.vulncheck.com/advisories/smartertools-smartermail-unauthenticated-background-of-the-day-path-coercion)
in an alert.

"On Windows systems, this allows UNC [Universal Naming Convention] paths to be resolved, causing the SmarterMail service to initiate outbound SMB authentication attempts to attacker-controlled hosts. This can be abused for credential coercion, NTLM relay attacks, and unauthorized network authentication."

The vulnerability has been
[patched](https://www.smartertools.com/smartermail/release-notes/current)
in Build 9518, released on January 22, 2026. With two vulnerabilities in SmarterMail coming under active exploitation over the past week, it's essential that users update to the latest version as soon as possible.