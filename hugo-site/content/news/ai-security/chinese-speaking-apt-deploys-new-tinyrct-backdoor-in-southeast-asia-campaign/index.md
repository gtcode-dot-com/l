---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T03:24:16.729760+00:00'
exported_at: '2026-06-27T03:24:18.669982+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html
structured_data:
  about: []
  author: ''
  description: Unit 42 links CL-STA-1062 to TinyRCT, a custom .NET backdoor used against
    government and energy targets in Southeast Asia.
  headline: Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/chinese-speaking-apt-deploys-new.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Chinese-Speaking APT Deploys New TinyRCT Backdoor in Southeast Asia Campaign
updated_at: '2026-06-27T03:24:16.729760+00:00'
url_hash: 216b1b46491c69d2cbcde65daafe85d2eefd9a5e
---

A Chinese-speaking advanced persistent threat (APT) actor has been linked to a new custom backdoor called TinyRCT as part of cyber attacks aimed at government entities and critical infrastructure in Southeast Asia.

The activity, particularly aimed at state-owned enterprises in the energy and government sectors, has been attributed to a threat actor called
**CL-STA-1062**
, which Palo Alto Networks Unit 42 said shares overlaps with
[UAT-7237](https://thehackernews.com/2025/08/taiwan-web-servers-breached-by-uat-7237.html)
, a hacking group that was first flagged by Cisco Talos in August 2025 in relation to a campaign directed against web infrastructure entities in Taiwan.

Unit 42 said it also observed CL-STA-1062 campaigns in prior operations targeting strategic sectors in East Asia since March 2022, suggesting a broader but sustained focus in the region.

"From a technical standpoint, the attackers behind CL-STA-1062 rely on a hybrid toolkit," Unit 42
[said](https://unit42.paloaltonetworks.com/cl-sta-1062-tinyrct-backdoor/)
in a technical report. "While they frequently use common open-source tools such as SoftEther VPN, Mimikatz, and VNT, they have recently introduced TinyRCT, a bespoke, previously undocumented backdoor."

TinyRCT is equipped to run arbitrary commands, enumerate files and exfiltrate them, capture the device's screen, and delete itself from the compromised host.

In one campaign detected in September 2025, the threat actor is said to have infiltrated a Southeast Asian government entity and deployed a web shell to exfiltrate data from an MS SQL server. During the same attack, the threat actors have been found to conduct network reconnaissance on a separate government entity in the same country.

"This suggests an effort to identify lateral movement opportunities and broaden their access. In one case, we observed the attacker staging and exfiltrating an entire directory of web server source code from the government entity," Unit 42 said, adding it detected the breach of at least 10 different organizations in Southeast Asia between October and December 2025.

Since at least mid-2025, CL-STA-1062 has trained its sights on the critical infrastructure, with the adversary scanning multiple entities in the region for vulnerabilities and then establishing a foothold via ASPX web shells that facilitate initial reconnaissance and outbound requests from the infected networks to attacker-controlled infrastructure, leading to the deployment of additional payloads.

This includes SoftEther VPN components and RAR archives containing the group's toolset, including open-source utilities such as
[Yuze](https://github.com/P001water/yuze)
(a SOCKS5 proxy) and
[VNT](https://github.com/vnt-dev/vnt)
(a VPN), often disguising them as VMware executables or an XDR agent (e.g., "XDRAgent.exe," "vmtools.exe," and "vmwared.exe").

Further analysis of the campaign's infrastructure has led to the discovery of a previously undocumented .NET backdoor dubbed TinyRCT ("PerfWatson2.exe"), a lightweight remote access trojan that enables system reconnaissance, command execution, file uploads, screenshot capture, remote control, and wipe traces of itself, while taking steps to avoid running in sandboxed environments.

It establishes a persistent communication channel with a remote server ("45.32.113[.]172") over HTTP, but encrypts the exchanged data using AES-128 encryption in CBC mode.

"The malware operates on a beaconing model, with a default 10-second sleep interval between requests," Unit 42 explained. "It polls the C2 server for instructions using GET requests, while it sends exfiltrated data via POST requests."

As for how TinyRCT is delivered, it takes the form of a malicious archive named "chrome\_setup.zip" containing a legitimate executable ("chrome\_setup.exe"), a configuration file ("chrome\_setup.exe.config"), and a rogue DLL ("MyAppDomainManager.dll") that's used to trigger an
[AppDomainManager injection](https://attack.mitre.org/techniques/T1574/014/)
attack to load the malicious DLL, which functions as a downloader by contacting "139.180.134[.]221" to retrieve "PerfWatson2.exe."

"The combination of tools observed in this activity cluster reflects a pragmatic approach to tool selection and attack capabilities," Unit 42 concluded. "The attackers behind this cluster continue to leverage common open-source tools such as SoftEther VPN and VNT to facilitate lateral movement."

"Our discovery of the TinyRCT backdoor in the attackers' infrastructure underscores their ability to customize tools to gain specific capabilities. The combination of targeting critical infrastructure and the development of custom malware suggests that CL-STA-1062 activity will continue to pose a threat to the region."