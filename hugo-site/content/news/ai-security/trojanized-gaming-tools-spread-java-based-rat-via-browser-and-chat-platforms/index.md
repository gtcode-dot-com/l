---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-27T12:15:14.046990+00:00'
exported_at: '2026-02-27T12:15:16.668204+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html
structured_data:
  about: []
  author: ''
  description: Trojanized gaming tools and new Windows RATs like Steaelite enable
    data theft, ransomware, and persistent remote control.
  headline: Trojanized Gaming Tools Spread Java-Based RAT via Browser and Chat Platforms
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/trojanized-gaming-tools-spread-java.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Trojanized Gaming Tools Spread Java-Based RAT via Browser and Chat Platforms
updated_at: '2026-02-27T12:15:14.046990+00:00'
url_hash: c487c939a70f63c73fb3b54144225684a60bb94b
---

**

Ravie Lakshmanan
**

Feb 27, 2026

Endpoint Security / Windows Security

Threat actors are luring unsuspecting users into running trojanized gaming utilities that are distributed via browsers and chat platforms to distribute a remote access trojan (RAT).

"A malicious downloader staged a portable Java runtime and executed a malicious Java archive (JAR) file named jd-gui.jar," the Microsoft Threat Intelligence team
[said](https://x.com/MsftSecIntel/status/2027070355487997998)
in a post on X. "This downloader used PowerShell and living-off-the-land binaries (LOLBins) like cmstp.exe for stealthy execution."

The attack chain is also designed to evade detection by deleting the initial downloader and by configuring Microsoft Defender exclusions for the RAT components.

Persistence is achieved by means of a scheduled task and Windows startup script named "world.vbs," before the final payload is deployed on the compromised host. The malware, per Microsoft, is a "multi-purpose malware" that acts as a loader, runner, downloader, and RAT.

Once launched, it connects to an external server at "79.110.49[.]15" for command-and-control (C2) communications, allowing it to exfiltrate data and deploy additional payloads.

As ways to defend against the threat, users are advised to audit Microsoft Defender exclusions and scheduled tasks, remove malicious tasks and startup scripts, isolate affected endpoints, and reset credentials for users active on compromised hosts.

The disclosure comes as BlackFog disclosed details of a new Windows RAT malware family called Steaelite that was first advertised on criminal forums in November 2025 as a "best Windows RAT" with "fully undetectable" (FUD) capabilities. It's compatible with both Windows 10 and 11.

Unlike other off-the-shelf RATs sold to criminal actors, Steaelite bundles together data theft and ransomware, packaging them into one web panel, with an Android ransomware module on the way. The panel also incorporates various developer tools to facilitate keylogging, client-to-victim chat, file searching, USB spreading, wallpaper modification, UAC bypass, and
[clipper functionality](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)
.

Other notable features include removing competing malware, disabling Microsoft Defender, or configuring exclusions, and installing persistence methods.

As for its main capabilities, Steaelite RAT supports remote code execution, file management, live streaming, webcam and microphone access, process management, clipboard monitoring, password theft, installed program enumeration, location tracking, arbitrary file execution, URL opening, DDoS attacks, and VB.NET payload compilation.

"The tool gives operators browser-based control over infected Windows machines, covering remote code execution, credential theft, live surveillance, file exfiltration, and ransomware deployment from a single dashboard," security researcher Wendy McCague
[said](https://www.blackfog.com/steaelite-rat-double-extortion-from-single-panel/)
.

"A single threat actor can browse files, exfiltrate documents, harvest credentials, and deploy ransomware from the same dashboard. This enables complete double extortion from one tool."

In recent weeks, threat hunters have also discovered two new RAT families tracked as
[DesckVB RAT](https://github.com/ShadowOpCode/DesckVB-RAT)
and
[KazakRAT](https://ctrlaltintel.com/threat%20research/KazakRAT/)
that enable comprehensive remote control over infected hosts and even selectively deploy capabilities post-compromise. According to Ctrl Alt Intel, KazakRAT is suspected to be the work of a suspected state-affiliated cluster targeting Kazakh and Afghan entities as part of a persistent campaign ongoing since at least August 2022.