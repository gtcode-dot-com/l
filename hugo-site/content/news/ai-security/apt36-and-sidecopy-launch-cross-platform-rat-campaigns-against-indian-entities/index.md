---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-12T19:33:52.952771+00:00'
exported_at: '2026-02-12T19:33:56.046185+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/apt36-and-sidecopy-launch-cross.html
structured_data:
  about: []
  author: ''
  description: Pakistan-aligned APT36 and SideCopy target Indian defense and government
    entities using phishing-delivered RAT malware across Windows and Linux system
  headline: APT36 and SideCopy Launch Cross-Platform RAT Campaigns Against Indian
    Entities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/apt36-and-sidecopy-launch-cross.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: APT36 and SideCopy Launch Cross-Platform RAT Campaigns Against Indian Entities
updated_at: '2026-02-12T19:33:52.952771+00:00'
url_hash: 0ee558d66fbfe4796d0d26d291175152544dabed
---

**

Ravie Lakshmanan
**

Feb 11, 2026

Cyber Espionage / Threat Intelligence

Indian defense sector and government-aligned organizations have been targeted by multiple campaigns that are designed to compromise Windows and Linux environments with remote access trojans capable of stealing sensitive data and ensuring continued access to infected machines.

The campaigns are characterized by the use of malware families like
[Geta RAT](https://thehackernews.com/2025/04/pakistan-linked-hackers-expand-targets.html)
,
[Ares RAT](https://thehackernews.com/2025/07/tag-140-deploys-drat-v2-rat-targeting.html)
, and
[DeskRAT](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)
, which are often attributed to Pakistan-aligned threat clusters tracked as SideCopy and APT36 (aka Transparent Tribe). SideCopy, active since at least 2019, is assessed to operate as a subdivision of Transparent Tribe.

"Taken together, these campaigns reinforce a familiar but evolving narrative," Aditya K. Sood, vice president of Security Engineering and AI Strategy at Aryaka,
[said](https://www.aryaka.com/blog/espionage-without-noise-apt36-enduring-campaigns/)
. "Transparent Tribe and SideCopy are not reinventing espionage – they are refining it."

"By expanding cross-platform coverage, leaning into memory-resident techniques, and experimenting with new delivery vectors, this ecosystem continues to operate below the noise floor while maintaining strategic focus."

Common to all the campaigns is the use of phishing emails containing malicious attachments or embedded download links that lead prospective targets to attacker-controlled infrastructure. These initial access mechanisms serve as a conduit for Windows shortcuts (LNK), ELF binaries, and PowerPoint Add-In files that, when opened, launch a multi-stage process to drop the trojans.

The malware families are designed to provide persistent remote access, enable system reconnaissance, collect data, execute commands, and facilitate long-term post-compromise operations across both Windows and Linux environments.

One of the attack chains is as follows: a malicious LNK file invokes "mshta.exe" to execute an HTML Application (HTA) file hosted on compromised legitimate domains. The HTA payload contains JavaScript to decrypt an embedded DLL payload, which, in turn, processes an embedded data blob to write a decoy PDF to disk, connects to a hard-coded command-and-control (C2) server, and displays the saved decoy file.

After the lure document is displayed, the malware checks for installed security products and adapts its persistence method accordingly prior to deploying Geta RAT on the compromised host. It's worth noting this attack chain was detailed by
[CYFIRMA](https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html)
and Seqrite Labs researcher
[Sathwik Ram Prakki](https://x.com/PrakkiSathwik/status/2007457956636590184)
in late December 2025.

Geta RAT supports various commands to collect system information, enumerate running processes, terminate a specified process, list installed apps, gather credentials, retrieve and replace clipboard contents with attacker-supplied data, capture screenshots, perform file operations, run arbitrary shell commands, and harvest data from connected USB devices.

Running parallel to this Windows-focused campaign is a Linux variant that employs a Go binary as a starting point to drop a Python-based Ares RAT by means of a shell script downloaded from an external server. Like Geta RAT, Ares RAT can also run a wide range of commands to harvest sensitive data and run Python scripts or commands issued by the threat actor.

Aryaka said it also observed another campaign where the Golang malware, DeskRAT, is delivered via a rogue PowerPoint Add-In file that runs embedded macro to establish outbound communication with a remote server to fetch the malware. APT36's use of DeskRAT was
[documented](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)
by Sekoia and QiAnXin XLab in October 2025.

"These campaigns demonstrate a well-resourced, espionage-focused threat actor deliberately targeting Indian defense, government, and strategic sectors through defense-themed lures, impersonated official documents, and regionally trusted infrastructure," the company said. "The activity extends beyond defense to policy, research, critical infrastructure, and defense-adjacent organizations operating within the same trusted ecosystem."

"The deployment of DeskRAT, alongside Geta RAT and Ares RAT, underscores an evolving toolkit optimized for stealth, persistence, and long-term access."