---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-23T08:15:15.564146+00:00'
exported_at: '2026-02-23T08:15:17.805964+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html
structured_data:
  about: []
  author: ''
  description: MuddyWater’s Operation Olalampo targets MENA with GhostFetch, CHAR,
    HTTP_VIP, and AI-assisted malware since Jan 26, 2026.
  headline: MuddyWater Targets MENA Organizations with GhostFetch, CHAR, and HTTP_VIP
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MuddyWater Targets MENA Organizations with GhostFetch, CHAR, and HTTP_VIP
updated_at: '2026-02-23T08:15:15.564146+00:00'
url_hash: 4312da15650d3de3a5174efba6a58c39f40eeaf1
---

**

Ravie Lakshmanan
**

Feb 23, 2026

Threat Intelligence / Artificial Intelligence

The Iranian hacking group known as
[MuddyWater](https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html)
(aka Earth Vetala, Mango Sandstorm, and MUDDYCOAST) has targeted several organizations and individuals mainly located across the Middle East and North Africa (MENA) region as part of a new campaign codenamed
**Operation Olalampo**
.

The activity, first observed on January 26, 2026, has resulted in the deployment of new malware families that share overlapping samples previously identified as used by the threat actor, according to a report published by Group-IB. These include downloaders like GhostFetch and HTTP\_VIP, along with a Rust backdoor called CHAR and an advanced implant codenamed GhostBackDoor that's dropped by GhostFetch.

"These attacks follow similar patterns and align with the killchains previously observed in MuddyWater attacks; starting with a phishing email with a Microsoft Office document attached to it that contains malicious macro code that decodes the embedded payload and drops it on the system and executes it, providing the adversary with remote control of the system," the company
[said](https://www.group-ib.com/blog/muddywater-operation-olalampo/)
.

One such attack chain employing a malicious Microsoft Excel document prompts users to enable macros in order to activate the infection and ultimately drop CHAR. Another variant of the same attack has been found to lead to the deployment of the GhostFetch downloader, which then downloads GhostBackDoor.

A third version of the attack leverages themes such as flight tickets and reports, in contrast to using lures mimicking an energy and marine services company in the Middle East, to distribute the HTTP\_VIP downloader that subsequently deploys the AnyDesk remote desktop software.

A brief description of the four tools is as follows -

* **GhostFetch**
  , a first-stage downloader that profiles the system, validates mouse movements and checks screen resolution, checks for the presence of debuggers, virtual machine artifacts, and antivirus software, and fetches and executes secondary payloads directly in memory.
* **GhostBackDoor**
  , a second-stage backdoor delivered by GhostFetch that supports an interactive shell, file read/write, and re-run GhostFetch.
* **HTTP\_VIP**
  , a native downloader that conducts system reconnaissance, connects to an external server ("codefusiontech[.]org") to authenticate and deploy AnyDesk from the C2 server. A new variant of the malware also adds the ability to retrieve victim information and retrieve instructions to start an interactive shell, download/upload files, capture clipboard contents, and update the sleep/beaconing interval.
* **CHAR**
  , a Rust backdoor that's controlled by a Telegram bot (whose first name is "Olalampo" and username is "stager\_51\_bot") to change directory and execute a cmd.exe or PowerShell command.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9codiElaXflP03LdRbTq-nazzyJg9afA33hoJJJYw6SEgccvJ3Mb801nozDT8dzpn6WnkEWlnTvHH5ZNGPIIvLsX32d2lga5MUukWPeZ3MQl2_gJdF5a7shBN1c1YUp-clQD-JvVck2t8az-B0JimfGW5BvZZQPkydZoW2thBVF9Su75pVtwGCNU_cvHy/s1600/killchain.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9codiElaXflP03LdRbTq-nazzyJg9afA33hoJJJYw6SEgccvJ3Mb801nozDT8dzpn6WnkEWlnTvHH5ZNGPIIvLsX32d2lga5MUukWPeZ3MQl2_gJdF5a7shBN1c1YUp-clQD-JvVck2t8az-B0JimfGW5BvZZQPkydZoW2thBVF9Su75pVtwGCNU_cvHy/s1600/killchain.jpg)

The PowerShell command is designed to execute a SOCKS5 reverse proxy or another backdoor named Kalim, upload data stolen from web browsers, and run unknown executables referred to as "sh.exe" and "gshdoc\_release\_X64\_GUI.exe."

Group-IB's analysis of CHAR's source code has revealed signs of artificial intelligence (AI)-assisted development owing to the presence of emojis in debug strings, a finding that's consistent with
[Google's revelations](https://thehackernews.com/2025/11/google-uncovers-promptflux-malware-that.html)
last year that the threat actor is experimenting with generative AI tools to support the development of custom malware to support file transfer and remote execution.

Another notable aspect is that CHAR shares a similar structure and development environment as the Rust-based malware
[BlackBeard](https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html)
(aka Archer RAT and RUSTRIC), which was flagged by CloudSEK and Seqrite Labs as put to use by the threat actor to target various entities in the Middle East.

MuddyWater has also been observed exploiting recently disclosed vulnerabilities on public-facing servers as a way to obtain initial access to target networks.

"The MuddyWater APT group remains an active threat within the META region, with this operation primarily targeting organizations in the MENA region," Group-IB concluded. "The group's continued adoption of AI technology, combined with continued development of custom malware and tooling and diversified command-and-control (C2) infrastructures, underscores their dedication and intent to expand their operations."