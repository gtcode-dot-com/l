---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-21T20:15:13.999464+00:00'
exported_at: '2026-04-21T20:15:16.207456+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/systembc-c2-server-reveals-1570-victims.html
structured_data:
  about: []
  author: ''
  description: SystemBC C2 exposed 1,570+ victims tied to The Gentlemen since July
    2025, revealing expanding ransomware scale.
  headline: SystemBC C2 Server Reveals 1,570+ Victims in The Gentlemen Ransomware
    Operation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/systembc-c2-server-reveals-1570-victims.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SystemBC C2 Server Reveals 1,570+ Victims in The Gentlemen Ransomware Operation
updated_at: '2026-04-21T20:15:13.999464+00:00'
url_hash: 5b0c6ed719bb687e8effa8b96edce777b436d484
---

Threat actors associated with The Gentlemen ransomware‑as‑a‑service (RaaS) operation have been observed attempting to deploy a known proxy malware called
[SystemBC](https://thehackernews.com/2024/01/systembc-malwares-c2-server-analysis.html)
.

According to
[new research](https://research.checkpoint.com/2026/dfir-report-the-gentlemen/)
published by Check Point, the command-and-control (C2 or C&C) server linked to SystemBC has led to the discovery of a botnet of more than 1,570 victims.

"SystemBC establishes SOCKS5 network tunnels within the victim’s environment and connects to its C&C server using a custom RC4‑encrypted protocol," Check Point said. It can also download and execute additional malware, with payloads either written to disk or injected directly into memory.

Since its emergence in July 2025, The Gentlemen has quickly established itself as one of the most prolific ransomware groups, claiming more than 320 victims on its data leak site. Operating under a classic double-extortion model, the group is versatile as it's sophisticated, exhibiting capabilities to target Windows, Linux, NAS, and BSD systems with a Go-based locker as well as employing
[legitimate drivers](https://securelist.com/av-killer-exploiting-throttlestop-sys/117026/)
and custom malicious tools to subvert defenses.

Exactly how the threat actors obtain initial access is unclear, although evidence suggests that internet-facing services or compromised credentials are being abused to establish an initial foothold, followed by engaging in discovery, lateral movement, payload staging (i.e., Cobalt Strike, SystemBC, and the encryptor), defense evasion, and ransomware deployment. A notable aspect of the attacks is the abuse of Group Policy Objects (GPOs) to facilitate domain-wide compromise.

"By tailoring their tactics against specific security vendors, The Gentlemen have demonstrated an acute awareness of their targets' environments and a willingness to engage in in-depth reconnaissance and tool modification throughout the course of their operation," security vendor Trend Micro
[noted](https://www.trendmicro.com/en_us/research/25/i/unmasking-the-gentlemen-ransomware.html)
in an analysis of the group's tradecraft in September 2025.

The latest findings from Check Point show that an affiliate of The Gentlemen RaaS deployed SystemBC on a compromised host, with the C2 server linked to the proxy malware commandeering hundreds of victims across the globe, including the U.S., the U.K., Germany, Australia, and Romania.

While SystemBC has been
[used in ransomware operations](https://thehackernews.com/2020/12/ransomware-attackers-using-systembc.html)
as far back as 2020, the exact nature of the connection between the malware and The Gentlemen e-crime scheme remains unclear, such as whether it's part of the attack playbook or if it's something deployed by a specific affiliate for data exfiltration and remote access.

"During lateral movement, the ransomware makes an attempt to blind Windows Defender on each reachable remote host by pushing a PowerShell script that disables real-time monitoring, adds broad exclusions for the drive, staging share, and its own process, shuts down the firewall, re-enables SMB1, and loosens LSA anonymous access controls, all before deploying and executing the ransomware binary on that host," Check Point said.

The ESXi variant incorporates fewer functionalities than the Windows variant, but is equipped to shut down virtual machines to enhance the effectiveness of the attack, adds persistence via crontab, and inhibits recovery before the ransomware binary is deployed.

"Most ransomware groups make noise when they launch and then disappear. The Gentlemen are different," Eli Smadja, group manager at Check Point Research, said in a statement shared with The Hacker News.

"They've cracked the affiliate recruitment problem by offering a better deal than anyone else in the criminal ecosystem. When we got inside one of their operator's servers, we found over 1,570 compromised corporate networks that hadn't even made the news yet. The real scale of this operation is significantly larger than what's publicly known, and it's still growing."

The findings come as Rapid7 highlighted the inner workings of another relatively new ransomware family called
[Kyber](https://www.watchguard.com/wgrd-security-hub/ransomware-tracker/kyber)
that surfaced in September 2025, targeting Windows and VMware ESXi infrastructures using encryptors developed in Rust and C++, respectively.

"The ESXi variant is specifically built for VMware environments, with capabilities for datastore encryption, optional virtual machine termination, and defacement of management interfaces," the cybersecurity company
[said](https://www.rapid7.com/blog/post/tr-kyber-ransomware-double-trouble-windows-esxi-attacks-explained/)
. "The Windows variant, written in Rust, includes a self-described 'experimental' feature for targeting Hyper-V."

"Kyber ransomware isn't a masterpiece of complex code, but it is highly effective at causing destruction. It reflects a shift toward specialization over sophistication."

According to data compiled by ZeroFox, at least 2,059 separate ransomware and digital extortion (R&DE) incidents have been observed in Q1 2026, with March accounting for no less than 747 incidents. The most active groups during the time period were Qilin (338), Akira (197), The Gentlemen (192), INC Ransom, and Cl0p.

"Notably, North America-based victims accounted for approximately 20 percent of The Gentlemen's attacks in Q3 2025, 2% in Q4 2025, and 13% in Q1 2026," ZeroFox
[said](https://www.zerofox.com/advisories/39483/)
. "This largely goes against typical regional targeting trends by other R&DE collectives, at least 50 percent of whose victims are North America-based."

### The Shifting Velocity of Ransomware Attacks

Cybersecurity company Halcyon, in its
[2025 Ransomware Evolution Report](https://www.halcyon.ai/ransomware-research-reports/2025-ransomware-evolution-report)
, revealed that the threat continues to mature into something more disciplined and a business-driven criminal enterprise, even as ransomware attacks targeting the automotive industry
[more than doubled in 2025](https://www.halcyon.ai/ransomware-research-reports/forty-four-percent-ransomware-automotive-industry)
, taking up 44% of all cyber incidents across the sector.

Other significant trends include attempts to impair security Endpoint Detection and Response (EDR) tools, use of the Bring Your Own Vulnerable Driver (
[BYOVD](https://thehackernews.com/2026/03/54-edr-killers-use-byovd-to-exploit-34.html)
) attack technique to escalate privileges and disable security solutions, blurring of nation-state and
[criminal ransomware campaigns](https://thehackernews.com/2025/07/storm-2603-exploits-sharepoint-flaws-to.html)
, and increased targeting of small and mid-sized organizations and operational technology (OT) environments.

"Ransomware continued to grow as a durable, industrialized ecosystem built on specialization, shared infrastructure, and rapid regeneration rather than any single brand," it said. "Law enforcement pressure and infrastructure seizures disrupted major operations, driving fragmentation, rebranding, and intensified competition across a more fluid landscape."

Ransomware operations are increasingly fast-moving, with dwell times collapsing from days to hours. About 69% of observed attack attempts have been found to be deliberately staged during nights and weekends to outpace defender response.

For instance, attacks involving Akira ransomware have
[demonstrated](https://www.halcyon.ai/ransomware-research-reports/akira-ransomware-attacks-in-under-an-hour)
an unusual swiftness, rapidly escalating from initial foothold to full encryption within an hour in some cases without detection, highlighting a well-oiled attack engine designed to maximize impact.

"Akira's combination of rapid compromise capabilities, disciplined operational tempo, and investment in reliable decryption infrastructure sets it apart from many ransomware operators," Halcyon said. "Defenders should treat Akira not as an opportunistic threat, but as a capable, persistent adversary that will exploit every available weakness to reach its objective."