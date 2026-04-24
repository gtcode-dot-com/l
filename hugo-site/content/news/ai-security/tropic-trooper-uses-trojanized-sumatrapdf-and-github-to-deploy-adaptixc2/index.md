---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-24T10:15:13.696771+00:00'
exported_at: '2026-04-24T10:15:15.879400+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/tropic-trooper-uses-trojanized.html
structured_data:
  about: []
  author: ''
  description: Tropic Trooper used trojanized SumatraPDF and GitHub C2 in 2024 to
    deploy AdaptixC2, enabling covert VS Code tunnel access.
  headline: Tropic Trooper Uses Trojanized SumatraPDF and GitHub to Deploy AdaptixC2
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/tropic-trooper-uses-trojanized.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Tropic Trooper Uses Trojanized SumatraPDF and GitHub to Deploy AdaptixC2
updated_at: '2026-04-24T10:15:13.696771+00:00'
url_hash: fa963107a978ef5bfa45ddea99b89f9c39b4e5b2
---

**

Ravie Lakshmanan
**

Apr 24, 2026

Malware / Threat Intelligence

Chinese-speaking individuals are the target of a new campaign that uses a trojanized version of SumatraPDF reader to deploy the
[AdaptixC2](https://unit42.paloaltonetworks.com/adaptixc2-post-exploitation-framework/)
Beacon post-exploitation agent and ultimately facilitate the abuse of Microsoft Visual Studio Code (VS Code) tunnels for remote access.

Zscaler ThreatLabz, which discovered the campaign last month, has attributed it with high confidence to
**[Tropic Trooper](https://thehackernews.com/2024/09/chinese-speaking-hacker-group-targets.html)**
(aka APT23, Earth Centaur, KeyBoy, and Pirate Panda), a hacking group known for its targeting of various entities in Taiwan, Hong Kong, and the Philippines. It's assessed to be active since at least 2011.

"The threat actors created a custom AdaptixC2 Beacon listener, leveraging GitHub as their command-and-control (C2) platform," security researcher Yin Hong Chang
[said](https://www.zscaler.com/blogs/security-research/tropic-trooper-pivots-adaptixc2-and-custom-beacon-listener)
in an analysis.

It's believed that Chinese-speaking individuals in Taiwan, and individuals in South Korea and Japan, are the targets of the campaign. The starting point of the attack is a ZIP archive containing military-themed document lures to launch the rogue version of SumatraPDF, which is then used to display a decoy PDF document, while simultaneously retrieving encrypted shellcode from a staging server to launch AdaptixC2 Beacon.

To accomplish this, the backdoored SumatraPDF executable launches a slightly modified version of a loader codenamed
[TOSHIS](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html)
, which is a variant of Xiangoop, a malware linked to Tropic Trooper, and has been used in the past to fetch next-stage payloads like Cobalt Strike Beacon or Merlin agent for the Mythic framework.

The loader is responsible for activating the multi-stage attack, dropping both the lure document as a distraction mechanism and the AdaptixC2 Beacon agent in the background.The agent employs GitHub for C2, beaconing out to the attacker-controlled infrastructure to fetch tasks to be executed on the compromised host.

The attack moves to the next stage only when the victim is deemed valuable, at which point the threat actor deploys VS Code and sets up
[VS Code tunnels](https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html)
for remote access. On select machines, the threat actor has been found to install alternative, trojanized applications, likely in an attemptto better camouflage their actions.

What's more, the staging server involved in the intrusion ("158.247.193[.]100") has been observed hosting a Cobalt Strike Beacon and a custom backdoor called
[EntryShell](https://hitcon.org/2024/CMT/slides/Pirates_of_The_Nang_Hai_Follow_the_Artifacts_of_Tropic_Trooper,_No_One_Knows.pdf)
, both of which have been put to use by Tropic Trooper in the past.

"Similar to the
[TAOTH campaign](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html)
, publicly available backdoors are used as payloads," Zscaler said. "While Cobalt Strike Beacon and Mythic Merlin were previously used, the threat actor has now shifted to AdaptixC2."