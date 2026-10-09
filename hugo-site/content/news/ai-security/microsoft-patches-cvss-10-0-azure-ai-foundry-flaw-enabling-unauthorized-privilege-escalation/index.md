---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T05:00:46.190233+00:00'
exported_at: '2026-10-03T05:00:47.568453+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
structured_data:
  about: []
  author: ''
  description: Microsoft fixes a CVSS 10.0 Azure AI Foundry flaw enabling network
    privilege escalation; no exploitation has been observed.
  headline: Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized
    Privilege Escalation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/microsoft-patches-cvss-100-azure-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Patches CVSS 10.0 Azure AI Foundry Flaw Enabling Unauthorized Privilege
  Escalation
updated_at: '2026-10-03T05:00:46.190233+00:00'
url_hash: d12dd718a0ca78aa68bf388b2b5ffbc0d8aca992
---

**

Ravie Lakshmanan
**

Sep 18, 2026

Vulnerability / Cloud Security

Microsoft has released fixes for a maximum-severity security flaw in Azure AI Foundry that could be exploited to achieve privilege escalation. No customer action is required.

The vulnerability, tracked as
**CVE-2026-85889**
, carries a CVSS score of 10.0.

"Missing authentication for critical function in Azure AI Foundry allows an unauthorized attacker to elevate privileges over a network," Microsoft
[said](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85889)
in a Thursday advisory.

Azure AI Foundry, also called Microsoft Foundry, is an
[enterprise platform](https://azure.microsoft.com/en-us/products/ai-foundry)
designed to build, deploy, and manage generative artificial intelligence (AI) applications and agents.

The Windows maker credited security researcher Rémy Marot (@R\_Marot) for discovering and reporting the flaw. There is no evidence that the issue has been exploited in the wild.

Also patched by Microsoft in recent days are a number of other critical flaws -

* **[CVE-2026-85885](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85885)**
  (CVSS score: 9.9) - A command injection vulnerability in Microsoft 365 Copilot that could allow an authorized attacker to elevate privileges over a network
* **[CVE-2026-85878](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85878)**
  (CVSS score: 9.9) - An improper authorization in Azure Database for PostgreSQL that could allow an authorized attacker to elevate privileges over a network
* **[CVE-2026-87701](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-87701)**
  (CVSS score: 9.6) - An improper neutralization vulnerability in Azure Cosmos DB that could allow an authorized attacker to elevate privileges over a network

As is typically the case with cloud-based CVEs, Microsoft said the vulnerabilities have already been fully mitigated, and that they require no action for users to take.

Separately, Microsoft has shipped updates for two other vulnerabilities, one of which was originally disclosed last month.

* **[CVE-2026-62721](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62721)**
  (CVSS score: 7.8) - An insufficient granularity of access control in Windows User-Mode Power Service (UMPS) that could allow an authorized attacker to elevate privileges locally and gain SYSTEM privileges.
* **[CVE-2026-85921](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-85921)**
  (CVSS score: 8.2) - A double free vulnerability in Windows Secure Kernel Mode that could allow an authorized attacker to elevate privileges locally and gain Virtual Trust Level 1 (VTL1) privileges.

Both flaws have been addressed as part of an
[out-of-band update](https://support.microsoft.com/en-us/servicing/os/windows-11/2026/09/kb5129194-windows-11-26h1-security-update)
for Windows 11, version 26H1 -

* 2026-09 Cumulative Update for Windows 11, version 26H1 for arm64-based Systems (KB5129194) (28000.2956)
* 2026-09 Cumulative Update for Windows 11, version 26H1 for x64-based Systems (KB5129194) (28000.2956)

The disclosure comes as Microsoft patched a
[record 974 vulnerabilities](https://thehackernews.com/2026/09/microsoft-patches-record-974-flaws.html)
spanning its software portfolio earlier last week. Two of those defects impacting Windows Advanced Local Procedure Call (ALPC) and the Windows Update Stack have come under active exploitation.

According to reports from
[Proofpoint](https://thehackernews.com/2026/09/four-spy-groups-used-same-chrome-and.html)
and
[Volexity](https://thehackernews.com/2026/09/china-linked-hackers-exploit-chrome.html)
, the ALPC vulnerability has been chained along with two Google Chrome flaws to develop an exploit kit called BlueMoon that has been weaponized by multiple espionage-aligned threat actors to deliver malicious payloads.