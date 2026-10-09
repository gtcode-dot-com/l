---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-10T12:15:13.149377+00:00'
exported_at: '2026-01-10T12:15:15.467038+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html
structured_data:
  about: []
  author: ''
  description: MuddyWater launched RustyWater, a Rust-based RAT, via spear-phishing
    Word macros targeting Middle East organizations.
  headline: MuddyWater Launches RustyWater RAT via Spear-Phishing Across Middle East
    Sectors
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/muddywater-launches-rustywater-rat-via.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MuddyWater Launches RustyWater RAT via Spear-Phishing Across Middle East Sectors
updated_at: '2026-01-10T12:15:13.149377+00:00'
url_hash: 4e5c388d082c3736fb2190f74712356ba66b4927
---

**

Jan 10, 2026
**

Ravie Lakshmanan

Cyber Espionage / Malware

The Iranian threat actor known as
[MuddyWater](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html)
has been attributed to a spear-phishing campaign targeting diplomatic, maritime, financial, and telecom entities in the Middle East with a Rust-based implant codenamed
**RustyWater**
.

"The campaign uses icon spoofing and malicious Word documents to deliver Rust based implants capable of asynchronous C2, anti-analysis, registry persistence, and modular post-compromise capability expansion," CloudSEK resetter Prajwal Awasthi
[said](https://www.cloudsek.com/blog/reborn-in-rust-muddywater-evolves-tooling-with-rustywater-implant)
in a report published this week.

The latest development reflects continued evolution of MuddyWater's tradecraft, which has gradually-but-steadily
[reduced its reliance](https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html#iranian-group-evolves)
on legitimate remote access software as a post-exploitation tool in favor of diverse malware arsenal comprising tools like
[Phoenix, UDPGangster](https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html)
,
[BugSleep (aka MuddyRot), and MuddyViper](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html)
.

Also tracked as Mango Sandstorm, Static Kitten, and TA450, the hacking group is assessed to be affiliated with Iran's Ministry of Intelligence and Security (MOIS). It's been operational since at least 2017.

Attack chains distributing RustyWater are fairly straightforward: spear-phishing emails masquerading as cybersecurity guidelines come attacked with a Microsoft Word document that, when opened, instructs the victim to "
[Enable content](https://thehackernews.com/2024/06/hackers-use-ms-excel-macro-to-launch.html)
" so as to activate the execution of a malicious VBA macro that's responsible for deploying the Rust implant binary.

Also referred to as Archer RAT and RUSTRIC, RustyWater gathers victim machine information, detects installed security software, sets up persistence by means of a Windows Registry key, and establishes contact with a command-and-control (C2) server ("nomercys.it[.]com") to facilitate file operations and command execution.

It's worth noting that use of RUSTRIC was
[flagged](https://thehackernews.com/2025/12/threatsday-bulletin-stealth-loaders-ai.html#israel-targeted-phishing)
by Seqrite Labs late last month as part of attacks targeting Information Technology (IT), Managed Service Providers (MSPs), human resources, and software development companies in Israel. The activity is being tracked by the cybersecurity company under the names UNG0801 and Operation IconCat.

"Historically, MuddyWater has relied on PowerShell and VBS loaders for initial access and post-compromise operations," CloudSEK said. "The introduction of Rust-based implants represents a notable tooling evolution toward more structured, modular, and low noise RAT capabilities."