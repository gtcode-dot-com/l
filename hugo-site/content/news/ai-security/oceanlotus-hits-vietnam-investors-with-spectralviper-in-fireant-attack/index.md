---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:33:10.242522+00:00'
exported_at: '2026-06-12T21:33:12.845676+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
structured_data:
  about: []
  author: ''
  description: OceanLotus used SPECTRALVIPER in 2025–2026 Vietnam campaigns, hitting
    investors and transport infrastructure via espionage.
  headline: OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/oceanlotus-hits-vietnam-investors-with.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OceanLotus Hits Vietnam Investors With SPECTRALVIPER in FireAnt Attack
updated_at: '2026-06-12T21:33:10.242522+00:00'
url_hash: 320366b279760fbcf683a575129538aefff0e95f
---

The Vietnam-aligned threat actor known as
**[OceanLotus](https://thehackernews.com/2024/08/vietnamese-human-rights-group-targeted.html)**
has been attributed to two distinct campaigns that targeted domestic entities and stock investors with a backdoor known as SPECTRALVIPER.

The campaigns involve a prolonged cyber espionage operation aimed at a Vietnamese infrastructure and transport construction corporation between mid-2024 and February 2026, as well as a supply chain attack leveraging FireAnt Metakit, a popular software platform used by stock investors in Vietnam. The second activity cluster took place from October 2025 to March 2026.

The two sets of attacks represent a shift in operational focus, per ESET, with the threat actor placing an increasing emphasis on domestic espionage rather than external targets. The group, active since 2012, also has a history of
[targeting China](https://thehackernews.com/2020/12/facebook-tracks-apt32-oceanlotus.html)
.

"Whether the shift represents a temporary adjustment or a long-term strategic change remains unclear; however, this 15-year-old APT group continues to demonstrate aggressive tactics and a level of craftiness in its tooling," the Slovakian cybersecurity company
[said](https://www.welivesecurity.com/en/eset-research/oceanlotus-external-espionage-domestic-targeting/)
in a report shared with The Hacker News.

Prior attacks orchestrated by the adversarial collective have
[leveraged](https://www.volexity.com/blog/2017/11/06/oceanlotus-blossoms-mass-digital-surveillance-and-exploitation-of-asean-nations-the-media-human-rights-and-civil-society/)
watering holes to
[digitally profile site visitors](https://www.welivesecurity.com/2018/11/20/oceanlotus-new-watering-hole-attack-southeast-asia/)
, with a specific focus on hundreds of individuals and organizations tied to media, human rights, and civil society causes in 2017 and 2018. Other campaigns have
[singled out](https://interaktiv.br.de/ocean-lotus/en/)
Vietnamese
[human rights defenders and dissidents](https://www.amnesty.org/en/latest/research/2021/02/click-and-bait-vietnamese-human-rights-defenders-targeted-with-spyware-attacks/)
.

In December 2020, Meta
[linked](https://thehackernews.com/2020/12/facebook-tracks-apt32-oceanlotus.html)
OceanLotus' activities with a Vietnamese IT company named CyberOne Group, which is also known as CyberOne Security, CyberOne Technologies, and Hành Tinh Company Limited. Although the company denied the allegations, the public exposure led to the group going off the grid for nearly three years.

Some of the key tools in its arsenal include
[SOUNDBITE](https://securelist.com/use-of-dns-tunneling-for-cc-communications/78203/)
(aka Denis),
[PHOREAL](https://malpedia.caad.fkie.fraunhofer.de/details/win.phoreal)
(aka Rizzo),
[WINDSHIELD](https://malpedia.caad.fkie.fraunhofer.de/details/win.remy)
(aka Remy), and, more recently,
[SPECTRALVIPER](https://thehackernews.com/2023/06/new-spectralviper-backdoor-targeting.html)
, which was first documented by Elastic Security Labs in June 2023 when the threat actor resurfaced in connection with a campaign targeting Vietnamese public companies.

As recently as last month, Kaspersky
[said](https://thehackernews.com/2026/05/pypi-packages-deliver-zichatbot-malware.html)
it discovered
[three malicious packages](https://thehackernews.com/2025/08/malicious-pypi-and-npm-packages.html)
on the Python Package Index (PyPI) repository designed to deliver a previously unknown malware family called ZiChatBot on Windows and Linux systems. The Russian cybersecurity company noted that the dropper used to deliver the malware shares a "64% similarity" to another dropper used by OceanLotus.

### The FireAnt Metakit Supply Chain Attack

The latest findings from ESET show that the FireAnt Metakit supply chain attack likely began around October 2, 2025, and lasted until March 2026. The attack is said to have leveraged the software's legitimate update URL to serve SPECTRALVIPER to a small subset of stock investors, indicating a more selective approach.

The use of the FireAnt update server to directly distribute malicious payloads notwithstanding, the update configuration file located at "metakit.fireant[.]vn/Software/version.xml" lacks an integrity validation mechanism to ensure that the update binary ("setup.exe") has not been tampered with.

"Due to the absence of signature validation, Metakit.exe executed the malicious downloader as a legitimate update," ESET said. "Once launched, the downloader performed basic host reconnaissance and transmitted the collected information via an HTTP POST request to a staging server, requesting the next-stage payload."

The payload is a DLL side-loading chain that employs a legitimate binary to launch a rogue DLL ("DtlCrashCatch.dll"), which then injects itself into the OneDrive.Sync.Service.exe process to trigger the execution of SPECTRALVIPER. The backdoor subsequently contacts a command-and-control (C2) server ("financemachinelearning[.]com") to send encrypted host information.

ESET said it has not observed any further malicious updates being distributed through the compromised channel since March 9, 2026, raising the possibility that the threat actors concluded their campaign.

### Vietnamese Transport Construction Corporation Targeted

OceanLotus has also been found targeting an unnamed Vietnamese infrastructure and transport construction firm starting as far back as November 2024, covertly retaining access to the entity until February 2026. Although the exact initial access pathway used by the threat actor is unclear, it's suspected to have involved the exploitation of remote code execution vulnerabilities in a public-facing Microsoft SQL server.

The attacks, as before, paves the way for the deployment of the SPECTRALVIPER backdoor using DLL side-loading. Three different variants have been identified across multiple compromised hosts on the same network. The malware contacts the C2 server ("gatewayrvcenter[.]com") to transmit host-profiling data and receive instructions from the operator.

SPECTRALVIPER also facilitates lateral movement and functions as a loader by injecting additional binaries or shellcode retrieved from the C2 server into target processes.

"Overall, the available evidence points to a potential shift in OceanLotus's operational patterns," ESET said. "Since the exposure of its physical front company in 2020, the group appears to have adopted a more selective approach to foreign espionage while placing increasing emphasis on domestic targets."