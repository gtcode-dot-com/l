---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-11T10:15:14.053045+00:00'
exported_at: '2026-03-11T10:15:17.053031+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html
structured_data:
  about: []
  author: ''
  description: Microsoft patches 84 vulnerabilities, including two public zero-days,
    strengthening defenses against privilege escalation and cloud token theft.
  headline: Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public
    Zero-Days
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches 84 Flaws in March Patch Tuesday, Including Two Public Zero-Days
updated_at: '2026-03-11T10:15:14.053045+00:00'
url_hash: 3f56503341ddbce895bdbbacfac0c8ce6af017bc
---

Microsoft on Tuesday released patches for a set of
[84 new security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2026-mar)
affecting various software components, including two that have been listed as publicly known.

Of these, eight are rated Critical, and 76 are rated Important in severity. Forty-six of the patched vulnerabilities relate to privilege escalation, followed by 18 remote code execution, 10 information disclosure, four spoofing, four denial-of-service, and two security feature bypass flaws.

The fixes are in addition to
[10 vulnerabilities](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
that have been addressed in its Chromium-based Edge browser since the release of the
[February 2026 Patch Tuesday update](https://thehackernews.com/2026/02/microsoft-patches-59-vulnerabilities.html)
.

The two publicly disclosed zero-days are
[CVE-2026-26127](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26127)
(CVSS score: 7.5), a denial-of-service vulnerability in .NET, and
[CVE-2026-21262](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21262)
(CVSS score: 8.8), an elevation of privilege vulnerability in SQL Server.

The vulnerability with the highest CVSS score in this month's update is a critical remote code execution flaw in the Microsoft Devices Pricing Program.
[CVE-2026-21536](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-21536)
(CVSS score: 9.8), per Microsoft, has been fully mitigated, and no action is required from users. Artificial intelligence (AI)-powered autonomous vulnerability discovery platform XBOW has been credited with discovering and reporting the issue.

"This month, over half (55%) of all Patch Tuesday CVEs were privilege escalation bugs, and of those, six were rated exploitation more likely across Windows Graphics Component, Windows Accessibility Infrastructure, Windows Kernel, Windows SMB Server, and Winlogon," Satnam Narang, senior staff research engineer at Tenable, said.

"We know these bugs are typically used by threat actors as part of post-compromise activity, once they get onto systems through other means (social engineering, exploitation of another vulnerability)."

The Winlogon privilege escalation flaw (
[CVE-2026-25187](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-25187)
, CVSS score: 7.8), in particular, leverages improper link resolution to obtain SYSTEM privileges. Google Project Zero researcher James Forshaw has been acknowledged for reporting the vulnerability.

"The flaw allows a locally authenticated attacker with low privileges to exploit a link-following condition in the Winlogon process and escalate to SYSTEM privileges," Jacob Ashdown, cybersecurity engineer at Immersive, said. "The vulnerability requires no user interaction and has low attack complexity, making it a straightforward target once an attacker gains a foothold."

Another vulnerability of note is
[CVE-2026-26118](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26118)
(CVSS score: 8.8), a server-side request forgery bug in the Azure Model Context Protocol (MCP) server that could allow an authorized attacker to elevate privileges over a network.

"An attacker could exploit this issue by sending specially crafted input to an Azure Model Context Protocol (MCP) Server tool that accepts user‑provided parameters," Microsoft said.

"If the attacker can interact with the MCP‑backed agent, they can submit a malicious URL in place of a normal Azure resource identifier. The MCP Server then sends an outbound request to that URL and, in doing so, may include its managed identity token. This allows the attacker to capture that token without requiring administrative access."

Successful exploitation of the vulnerability could permit an attacker to obtain the permissions associated with the MCP Server's managed identity. The attacker could then leverage this behavior to access or perform actions on any resources that the managed identity is authorized to reach.

Among the Critical-severity bugs resolved by Microsoft is an information disclosure flaw in Excel. Tracked as
[CVE-2026-26144](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-26144)
(CVSS score of 7.5), it has been described as a case of cross-site scripting that occurs as a result of improper neutralization of input during web page generation.

The Windows maker said an attacker who exploited the shortcoming could potentially cause Copilot Agent mode to exfiltrate data as part of a zero-click attack.

"Information disclosure vulnerabilities are especially dangerous in corporate environments where Excel files often contain financial data, intellectual property, or operational records," Alex Vovk, CEO and co-founder of Action1, said in a statement.

"If exploited, attackers could silently extract confidential information from internal systems without triggering obvious alerts. Organizations using AI-assisted productivity features may face increased exposure, as automated agents could unintentionally transmit sensitive data outside corporate boundaries."

The patches come as Microsoft said it's changing the default behavior of Windows Autopatch by enabling hotpatch security updates to help secure devices at a faster pace.

"This change in default behavior comes to all eligible devices in Microsoft Intune and those accessing the service via Microsoft Graph API starting with the May 2026 Windows security update," Redmond
[said](https://techcommunity.microsoft.com/blog/windows-itpro-blog/securing-devices-faster-with-hotpatch-updates-on-by-default/4500066)
. "Applying security fixes without waiting for a restart can get organizations to 90% compliance in half the time, while you remain in control."