---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T06:15:14.706468+00:00'
exported_at: '2026-04-08T06:15:16.982269+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html
structured_data:
  about: []
  author: ''
  description: Iran-linked actors target U.S. PLCs using Dropbear and SSH access,
    disrupting OT systems across sectors and escalating cyber conflict.
  headline: Iran-Linked Hackers Disrupt U.S. Critical Infrastructure by Targeting
    Internet-Exposed PLCs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Iran-Linked Hackers Disrupt U.S. Critical Infrastructure by Targeting Internet-Exposed
  PLCs
updated_at: '2026-04-08T06:15:14.706468+00:00'
url_hash: e633537c3796f4d33e0b9f4d1d1676cffd4bcd32
---

Iran-affiliated cyber actors are targeting internet-facing operational technology (OT) devices across critical infrastructures in the U.S., including programmable logic controllers (PLCs), cybersecurity and intelligence agencies
[warned](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)
Tuesday.

"These attacks have led to diminished PLC functionality, manipulation of display data and, in some cases, operational disruption and financial loss," the U.S. Federal Bureau of Investigation (FBI)
[said](https://x.com/FBICyberDiv/status/2041566548691660897)
in a post on X.

The agencies said the
[campaign](https://thehackernews.com/2025/06/us-agencies-warn-of-rising-iranian.html)
is part of a
[recent escalation](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
in cyber attacks orchestrated by Iranian hacking groups against U.S. organizations in response to the ongoing conflict between Iran and the U.S. and Israel.

Specifically, the activity has led to PLC disruptions across several U.S. critical infrastructure sectors via what the authoring agencies described as malicious interactions with the project file and manipulation of data on human-machine interface (HMI) and supervisory control and data acquisition (SCADA) displays.

These attacks have singled out Rockwell Automation and Allen-Bradley PLCs deployed in government services and facilities, Water and Wastewater Systems (WWS), and energy sectors.

"The actors used leased, third-party hosted infrastructure with configuration software, such as Rockwell Automation's Studio 5000 Logix Designer software, to create an accepted connection to the victim's PLC," the advisory said. "Targeted devices include CompactLogix and Micro850 PLC devices."

Upon obtaining initial access, the threat actors established command-and-control by deploying Dropbear, a Secure Shell (SSH) software, on victim endpoints to enable remote access through port 22 and facilitate the extraction of the device's project file and data manipulation on HMI and SCADA displays.

To combat the threat, organizations are advised to avoid exposing the PLC to the internet, take steps to prevent remote modification either via a physical or software switch, implement multi-factor authentication (MFA), and erect a firewall or network proxy in front of the PLC to control network access, keep PLC devices up-to-date, disable any unused authentication features, and monitor for unusual traffic.

This is not the first time Iranian threat actors have targeted OT networks and PLCs. In late 2023, Cyber Av3ngers (aka Hydro Kitten, Shahid Kaveh Group, and UNC5691) was
[linked](https://thehackernews.com/2023/11/iranian-hackers-exploit-plcs-in-attack.html)
to the active exploitation of Unitronics PLCs to target the Municipal Water Authority of Aliquippa in western Pennsylvania. These attacks compromised at least 75 devices.

"This advisory confirms what we've observed for months: Iran's cyber escalation follows a known playbook. Iranian threat actors are now moving faster and broader and targeting both IT and OT infrastructure," Sergey Shykevich, threat intelligence group manager at Check Point Research, said in a statement shared with The Hacker News.

"We documented identical targeting patterns against Israeli PLCs in March. It is not the first time Iranian actors are targeting operational technology in the US for disruption purposes, so organizations shouldn't treat this as a new threat, but as an accelerating one."

The development comes amid a
[new-found surge](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
in distributed denial-of-service (DDoS) attacks and claims of hack-and-leak operations carried out by cyber proxy groups and hacktivists targeting Western and Israeli entities, according to Flashpoint.

In a report published this week, DomainTools Investigations (DTI) described activity attributed to Homeland Justice, Karma/KarmaBelow80, and Handala Hack as a "single, coordinated cyber influence ecosystem" aligned with Iran's Ministry of Intelligence and Security (MOIS) rather than a set of distinct hacktivist groups.

"These personas function as interchangeable operational veneers applied to a consistent underlying capability," DTI
[said](https://dti.domaintools.com/research/handala-mois-linked-cyber-influence-ecosystem-threat-intelligence-assessment)
. "Their purpose is not to reflect organizational separation, but to enable segmentation of messaging, targeting, and attribution while preserving continuity of infrastructure and tradecraft."

Public-facing domains and Telegram channels serve as the primary dissemination and amplification hub, with the messaging platform also playing a huge role in command-and-control (C2) operations by allowing the malware to communicate with threat actor-controlled bots, reduce infrastructure overhead, and blend in with normal operations.

"This ecosystem represents a state-directed instrument of cyber-enabled influence, in which technical operations are tightly integrated with narrative manipulation and media amplification dynamics to achieve coercive and strategic effects," DTI added.

### MuddyWater aș a CastleRAT Affiliate

The development comes as JUMPSEC detailed MuddyWater ties with the criminal ecosystem, stating that the Iranian state-sponsored threat actor operates at least two CastleRAT builds against Israeli targets. It's worth noting that CastleRAT is a remote access trojan that's part of the
[CastleLoader framework](https://thehackernews.com/2025/12/four-threat-clusters-using-castleloader.html)
attributed by Recorded Future to a group it tracks under the moniker GrayBravo (aka TAG-150).

Central to the operations is a PowerShell deployer ("reset.ps1") that deploys a previously undocumented JavaScript-based malware called ChainShell, which then contacts a smart contract on the Ethereum blockchain to retrieve a C2 address and use it to fetch next-stage JavaScript code for execution on compromised hosts.

Some aspects of these connections between MOIS and the cybercrime ecosystem were also flagged by
[Ctrl-Alt-Intel](https://thehackernews.com/2026/03/weekly-recap-qualcomm-0-day-ios-exploit.html#:~:text=MuddyWater%20Evolves%20Its%20Tactics)
,
[Broadcom](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)
, and
[Check Point](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
, highlighting the growing engagement as evidence of a growing reliance on off-the-shelf tools to support state objectives and complicate attribution efforts.

The same PowerShell loader has also been found to deliver a botnet malware referred to as Tsundere (aka Dindoor). According to JUMPSEC, both ChainShell and Tsundere are separate TAG-150 platform components that are deployed along with CastleRAT.

"The adoption of a Russian criminal MaaS by an Iranian state actor has direct implications for defenders," JUMPSEC said in a report shared with The Hacker News. "Organizations targeted by MuddyWater, especially in the defence, aerospace, energy, and government sectors, now face threats that combine state-level targeting with commercially developed offensive tools."