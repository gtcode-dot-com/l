---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-11T12:03:08.049685+00:00'
exported_at: '2025-12-11T12:03:10.744712+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/wirte-leverages-ashenloader-sideloading.html
structured_data:
  about: []
  author: ''
  description: WIRTE expands AshTag espionage operations, using phishing & DLL sideloading
    to target Middle East govts with persistent intelligence-gathering attacks
  headline: WIRTE Leverages AshenLoader Sideloading to Install the AshTag Espionage
    Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/wirte-leverages-ashenloader-sideloading.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: WIRTE Leverages AshenLoader Sideloading to Install the AshTag Espionage Backdoor
updated_at: '2025-12-11T12:03:08.049685+00:00'
url_hash: cf1e2d4212920ef94975a53a7e5f9e33634f0f92
---

**

Dec 11, 2025
**

Ravie Lakshmanan

Cyberwarfare / Threat Intelligence

An advanced persistent threat (APT) known as
**WIRTE**
has been attributed to attacks targeting government and diplomatic entities across the Middle East with a previously undocumented malware suite dubbed AshTag
[since 2020](https://thehackernews.com/2021/06/molerats-hackers-return-with-new.html)
.

Palo Alto Networks is tracking the activity cluster under the name
**Ashen Lepus**
. Artifacts uploaded to the VirusTotal platform show that the threat actor has trained its sights on Oman and Morocco, indicating an expansion in operational scope beyond the Palestinian Authority, Jordan, Iraq, Saudi Arabia, and Egypt.

"Ashen Lepus remained persistently active throughout the Israel-Hamas conflict, distinguishing it from other affiliated groups whose activities decreased over the same period," the cybersecurity company said in a
[report](https://unit42.paloaltonetworks.com/hamas-affiliate-ashen-lepus-uses-new-malware-suite-ashtag/)
shared with The Hacker News. "Ashen Lepus continued with its campaign even after the October 2025 Gaza ceasefire, deploying newly developed malware variants and engaging in hands-on activity within victim environments."

WIRTE, which overlaps with an Arabic-speaking, politically motivated cluster known as
[Gaza Cyber Gang](https://thehackernews.com/2023/11/new-campaign-targets-middle-east.html)
(aka Blackstem, Extreme Jackal, Molerats, or TA402), is
[assessed](https://thehackernews.com/2024/11/hamas-affiliated-wirte-employs-samecoin.html)
to be active since at least 2018. According to a report from Cybereason, both Molerats and
[APT-C-23](https://thehackernews.com/2022/04/hamas-linked-hackers-targeting-high.html)
(aka
[Arid Viper](https://blog.sekoia.io/aridviper-an-intrusion-set-allegedly-associated-with-hamas/)
, Desert Varnish, or Renegade Jackal) are two main sub-groups of the Hamas cyberwarfare division.

It's primarily driven by espionage and intelligence collection, targeting government entities in the Middle East to meet its strategic objectives.

In a report published in November 2024, Check Point
[attributed](https://thehackernews.com/2024/11/hamas-affiliated-wirte-employs-samecoin.html)
the hacking crew to destructive attacks exclusively aimed at Israeli entities to infect them with a custom wiper malware referred to as SameCoin, highlighting their ability to adapt and carry out both espionage and sabotage.

The long-running, elusive campaign detailed by Unit 42, going all the way back to 2018, has been found to leverage phishing emails with lures related to geopolitical affairs in the region. A recent increase in lures related to Turkey – e.g., "Partnership agreement between Morocco and Turkey" or "Draft resolutions concerning the State of Palestine" – suggests that entities in the country may be a new area of focus.

The attack chains commence with a harmless PDF decoy that tricks recipients into downloading a RAR archive from a file-sharing service. Opening the archive triggers a chain of events that results in the deployment of AshTag.

This involves using a renamed benign binary to sideload a malicious DLL dubbed AshenLoader that, in addition to opening a decoy PDF file to keep up the ruse, contacts an external server to drop two more components, a legitimate executable and a DLL payload called AshenStager (aka stagerx64) that's again sideloaded to launch the malware suite in memory to minimize forensic artifacts.

AshTag is a modular .NET backdoor that's designed to facilitate persistence and remote command execution, while masquerading as a legitimate VisualServer utility to fly under the radar. Internally, its features are realized by means of an AshenOrchestrator to enable communications and to run additional payloads in memory.

These payloads serve different purposes -

* Persistence and process management
* Update and removal
* Screen capture
* File explorer and management
* System fingerprinting

In one case, Unit 42 said it observed the threat actor accessing a compromised machine to conduct hands-on data theft by staging documents of interest in the C:\Users\Public folder. These files are said to have been downloaded from a victim's email inbox, their end goal being the theft of diplomacy-related documents. The documents were then exfiltrated to an attacker-controlled server using the Rclone utility.

"Ashen Lepus remains a persistent espionage actor, demonstrating a clear intent to continue its operations throughout the recent regional conflict -- unlike other affiliated threat groups, whose activity significantly decreased," the company concluded. "The threat actors' activities throughout the last two years in particular highlight their commitment to constant intelligence collection."