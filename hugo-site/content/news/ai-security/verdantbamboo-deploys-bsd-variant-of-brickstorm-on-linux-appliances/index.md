---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T03:42:17.203431+00:00'
exported_at: '2026-06-10T03:42:20.340167+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html
structured_data:
  about: []
  author: ''
  description: VerdantBamboo used BRICKSTORM, PLENET, and AGENTPSD after an 18-month
    breach, enabling stealthy Linux appliance access.
  headline: VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/verdantbamboo-deploys-bsd-variant-of.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: VerdantBamboo Deploys BSD Variant of BRICKSTORM on Linux Appliances
updated_at: '2026-06-10T03:42:17.203431+00:00'
url_hash: 2a43a7eb423b1d352e0da114b5b6d8bc6a725bcb
---

**

Ravie Lakshmanan
**

Jun 08, 2026

Cyber Espionage / Malware

A China-nexus cyber espionage group has been observed deploying a BSD variant of a known backdoor called BRICKSTORM, as well as two other malware families codenamed PLENET (aka
[GRIMBOLT](https://thehackernews.com/2026/02/dell-recoverpoint-for-vms-zero-day-cve.html)
) and AGENTPSD to target Linux systems.

The activity has been attributed by Volexity to a threat cluster it tracks as
**[VerdantBamboo](https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/)**
, which it said
[overlaps](https://thehackernews.com/2025/12/cisa-reports-prc-hackers-using.html)
with hacking groups known as Clay Typhoon (Microsoft), UNC5221 (Google), and Warp Panda (CrowdStrike).

The cybersecurity company said it discovered the intrusion during an incident response engagement in September 2025, when it emerged that the adversary had compromised an unnamed victim's Egnyte Storage Sync system by exploiting a local privilege escalation flaw to deploy BRICKSTORM. The issue was addressed in Storage Sync
[version 13.13](https://helpdesk.egnyte.com/hc/en-us/articles/43855328739469-Storage-Sync-V-13-13-Miscellaneous-Improvements)
, released in March 2026.

"The appliance had periodically been accessed by VerdantBamboo via IP addresses assigned through the victim organization's web SSL VPN," researchers Damien Cash, Paul Rascagneres, Steven Adair, and Tom Lancaster said in a technical report published last week.

"The threat actor used the malware's proxying capabilities deployed on the Storage Sync system, along with compromised credentials, to access the victim's Microsoft 365 (M365) environment."

It's assessed that these steps were undertaken to blend in with legitimate network traffic and evade Conditional Access policies, with the initial compromise occurring at least 18 months before.

Following the initial remediation, VerdantBamboo is said to have staged a return, breaching the same organization by using stolen administrative credentials to connect to the firewall, and then abusing that access to configure web SSL VPN access to the device, connect to other systems, and deploy additional malware to a Synology Network Attached Storage (NAS) appliance.

Further investigation has since uncovered that the threat actor had in fact compromised the victim organization's Managed Services Provider (MSP), specifically infecting its MSP's pfSense firewall with a BSD variant of BRICKSTORM around the same time the victim's Storage Sync system was also breached.

It's believed that the victim was compromised through the threat actor's breach of the MSP. The two malware families deployed to the NAS appliance over SSH are as follows -

* PLENET (aka GRIMBOLT), a cross-platform backdoor developed in .NET Core and a new version of BRICKSTORM compiled using native ahead-of-time (AOT) compilation. It supports interactive shell, remote command execution, file manipulation, and command-and-control (C2) server switching.
* AGENTPSD, a Python-based reverse shell that likely functions as a fallback in case the primary implant ceases to function

It's worth noting that the use of PLENET in the wild was reported by Google earlier this February in connection with attacks mounted by a suspected China-nexus threat cluster dubbed UNC6201 that exploited a vulnerability in Dell RecoverPoint for Virtual Machines (CVE-2026-22769, CVSS score: 10.0) as a zero-day since mid-2024.

"VerdantBamboo is a highly sophisticated threat actor that seeks to leverage a combination of living-off-the-land techniques and malware deployment on systems that traditionally do not or cannot run EDR software," Volexity said.

"This threat actor appears to have good knowledge of proprietary appliances, allowing them to deploy malware with customized persistence mechanisms. They also appear to have operational security discipline aimed at leveraging a limited number of domains and IP addresses per victim and setting up customized implant naming and persistence on a per-device basis."