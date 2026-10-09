---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:21:30.664914+00:00'
exported_at: '2026-05-14T21:21:32.359330+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html
structured_data:
  about: []
  author: ''
  description: Microsoft patched 138 flaws, including 30 Critical bugs, as AI discovery
    expands Patch Tuesday risk.
  headline: Microsoft Patches 138 Vulnerabilities, Including DNS and Netlogon RCE
    Flaws
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/microsoft-patches-138-vulnerabilities.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches 138 Vulnerabilities, Including DNS and Netlogon RCE Flaws
updated_at: '2026-05-14T21:21:30.664914+00:00'
url_hash: 3f0b5f448234ff148bb10e5fa83e5f621b6043c5
---

Microsoft on Tuesday released patches for
[138 security vulnerabilities](https://msrc.microsoft.com/update-guide/releaseNote/2026-May)
spanning its product portfolio, although none of them have been listed as publicly known or under active attack.

Of the 138 flaws, 30 are rated Critical, 104 are rated Important, three are rated Moderate, and one is rated Low in severity. As many as 61 vulnerabilities are classified as privilege escalation bugs, followed by 32 remote code execution, 15 information disclosure, 14 spoofing, eight denial-of-service, six security feature bypass, and two tampering flaws.

The update list also includes a vulnerability that was patched by AMD (
[CVE-2025-54518](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7052.html)
, CVSS score: 7.3) this month. It relates to a case of improper isolation of shared resources within the CPU operation cache on Zen 2-based products that could allow an attacker to corrupt instructions executed at a different privilege level, potentially resulting in privilege escalation.

The patches are also in addition to
[127 security flaws](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnotes-security)
that Google has addressed in Chromium, which forms the basis for Microsoft's Edge browser.

One of the most severe vulnerabilities patched by Redmond is
[CVE-2026-41096](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41096)
(CVSS score: 9.8), a heap-based buffer overflow flaw impacting Windows DNS that could allow an unauthorized attacker to execute code over a network.

"An attacker could exploit this vulnerability by sending a specially crafted DNS response to a vulnerable Windows system, causing the DNS Client to incorrectly process the response and corrupt memory," Microsoft said. "In certain configurations, this could allow the attacker to run code remotely on the affected system without authentication."

Also fixed by Microsoft are several Critical- and Important-rated flaws -

* [**CVE-2026-42826**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42826)
  (CVSS score: 10.0) - An exposure of sensitive information to an unauthorized actor in Azure DevOps that allows an unauthorized attacker to disclose information over a network. (Requires no customer action)
* **[CVE-2026-33109](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33109)**
  (CVSS score: 9.9) - An improper access control in Azure Managed Instance for Apache Cassandra that allows an authorized attacker to execute code over a network. (Requires no customer action)
* **[CVE-2026-42898](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42898)**
  (CVSS score: 9.9) - A code injection vulnerability in Microsoft Dynamics 365 (on-premises) that allows an authorized attacker to execute code over a network.
* **[CVE-2026-42823](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42823)**
  (CVSS score: 9.9) - An improper access control in Azure Logic Apps that allows an authorized attacker to elevate privileges over a network.
* **[CVE-2026-41089](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41089)**
  (CVSS score: 9.8) - A stack-based buffer overflow in Windows Netlogon that allows an unauthorized attacker to execute code over a network without needing to sign in or have prior access by sending a specially crafted network request to a Windows server that is acting as a domain controller.
* **[CVE-2026-33823](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33823)**
  (CVSS score: 9.6) - An improper authorization in Microsoft Teams that allows an authorized attacker to disclose information over a network. (Requires no customer action)
* **[CVE-2026-35428](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-35428)**
  (CVSS score: 9.6) - A command injection vulnerability in Azure Cloud Shell that allows an unauthorized attacker to perform spoofing over a network. (Requires no customer action)
* **[CVE-2026-40379](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-40379)**
  (CVSS score: 9.3) - An exposure of sensitive information to an unauthorized actor in Azure Entra ID that allows an unauthorized attacker to perform spoofing over a network. (Requires no customer action)
* **[CVE-2026-40402](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-40402)**
  (CVSS score: 9.3) - A user-after-free in Windows Hyper-V that allows an unauthorized attacker to gain SYSTEM privileges and access the Hyper-V host environment.
* **[CVE-2026-41103](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-41103)**
  (CVSS score: 9.1) - An incorrect implementation of authentication algorithm in Microsoft SSO Plugin for Jira & Confluence that allows an unauthorized attacker to gain unauthorized access to Jira or Confluence as a valid user and perform actions with the same permissions as the compromised account.
* **[CVE-2026-33117](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33117)**
  (CVSS score: 9.1) - An improper authentication in Azure SDK that allows an unauthorized attacker to bypass a security feature over a network.
* **[CVE-2026-42833](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-42833)**
  (CVSS score: 9.1) - An execution with unnecessary privileges in Microsoft Dynamics 365 (on-premises) that allows an authorized attacker to execute code over a network and gain the ability to interact with other tenant’s applications and content.
* **[CVE-2026-33844](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33844)**
  (CVSS score: 9.0) - An improper input validation in Azure Managed Instance for Apache Cassandra that allows an authorized attacker to execute code over a network. (Requires no customer action)
* [**CVE-2026-40361**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-40361)
  (CVSS score: 8.4) - A use-after-free vulnerability in Microsoft Office Word that allows an unauthorized attacker to execute code locally without requiring user interaction.
* [**CVE-2026-40364**](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-40364)
  (CVSS score: 8.4) - A type confusion vulnerability in Microsoft Office Word that allows an unauthorized attacker to execute code locally without requiring user interaction.

"This critical elevation of privilege vulnerability allows an unauthorized attacker to impersonate an existing user by presenting forged credentials, thus bypassing Entra ID," Adam Barnett, lead software engineer at Rapid7, said about CVE-2026-41103.

Jack Bicer, director of vulnerability research at Action1,
[described](https://www.action1.com/patch-tuesday/patch-tuesday-may-2026/)
CVE-2026-42898 as a critical flaw that allows an authenticated attacker with low privileges to run arbitrary code over the network by manipulating process session data within Dynamics CRM.

"With no user interaction required, and the potential to impact systems beyond the vulnerable component's original security scope, this vulnerability poses serious enterprise risk: an attacker with only basic access could turn a business application server into a remote execution platform," Bicer said.

"Compromise of Dynamics 365 infrastructure can expose customer records, operational workflows, financial information, and integrated business systems. Since CRM environments often connect with identity services, databases, and enterprise applications, successful exploitation could lead to broader organizational compromise and operational disruption."

Organizations are also advised to
[update Windows Secure Boot certificates](https://thehackernews.com/2026/01/microsoft-fixes-114-windows-flaws-in.html)
to their 2023 counterparts ahead of next month, when the 2011-issued certificates are set to expire. Microsoft first announced the change in November 2025.

"The most critical non-CVE update involves the mandatory rollout of updated Secure Boot certificates," Rain Baker, senior incident response specialist at Nightwing, said. "Devices failing to receive these updates before the June 26 deadline face 'catastrophic boot-level security failures' or degraded security states. Ensure your entire fleet successfully rotates to the new trust anchors before the June 26, 2026, deadline."

## Over 500 CVEs in 2026 So Far

According to Satnam Narang, senior staff research engineer at Tenable, Microsoft has already patched over 500 CVEs five months into the year. This large volume of fixes reflects a broader industry trend where vulnerability discovery has scaled new highs, with a chunk of them flagged via artificial intelligence (AI)-powered approaches.

Microsoft, in a report published Tuesday, said AI-assisted vulnerability discovery is expected to increase the scale of Patch Tuesday releases in the coming months, adding 16 of the flaws fixed this month across the Windows networking and authentication stack were identified through its new multi-model AI-driven vulnerability discovery system, codenamed
[MDASH](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)
(short for
**m**
ulti-mo
**d**
el
**a**
gentic
**s**
canning
**h**
arness).

"In this month's release, a greater share of the issues addressed were discovered by Microsoft, compared to prior months," Tom Gallagher, vice president of engineering at Microsoft Security Response Center,
[said](https://www.microsoft.com/en-us/msrc/blog/2026/05/a-note-on-patch-tuesday)
. "Many of these were surfaced through AI investments and investigations across our engineering and research teams, including the use of Microsoft's new multi-model AI-driven scanning harness."

Microsoft also emphasized that the scale and speed of vulnerability discovery brought about by AI can raise operational demands and requires a consistent, disciplined approach to risk management in order to ensure that issues are mitigated quickly and fixed in a timely fashion.

"Stay current on supported operating systems, products, and patches, and revisit the speed and consistency of your patching cadence," Gallagher said. "Triage by exposure and impact, not raw count."

Other recommendations outlined by Microsoft include reducing unnecessary internet exposure, improving configuration hygiene, removing legacy authentication, enabling multi-factor authentication (MFA), enforcing strong access controls, segmenting environments to contain incidents, and investing in detection and response.

"The work of finding and fixing vulnerabilities continues to get faster, broader, and more rigorous across the industry," the tech giant said. "What we encourage in turn is a thoughtful look at whether the practices that worked well for the patching landscape of a few years ago are still well matched to where the landscape is heading."

"The fundamentals have not changed. The pace at which they need to be applied is changing, and the organizations that adjust with it will be the ones best positioned for what comes next."