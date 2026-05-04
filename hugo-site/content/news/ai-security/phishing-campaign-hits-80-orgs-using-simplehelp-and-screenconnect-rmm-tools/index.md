---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-04T18:15:13.733586+00:00'
exported_at: '2026-05-04T18:15:16.997318+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
structured_data:
  about: []
  author: ''
  description: VENOMOUS#HELPER phishing campaign active since April 2025 has impacted
    80+ organizations, mainly in the U.S., using SSA-themed lures.
  headline: Phishing Campaign Hits 80+ Orgs Using SimpleHelp and ScreenConnect RMM
    Tools
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/phishing-campaign-hits-80-orgs-using.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Phishing Campaign Hits 80+ Orgs Using SimpleHelp and ScreenConnect RMM Tools
updated_at: '2026-05-04T18:15:13.733586+00:00'
url_hash: 423da35cd9d46b1ac89dd99dc6f3fe095c08520a
---

**

Ravie Lakshmanan
**

May 04, 2026

Network Security / Endpoint Security

An active phishing campaign has been observed targeting multiple vectors since at least April 2025, with legitimate Remote Monitoring and Management (RMM) software as a way to establish persistent remote access to compromised hosts.

The activity, codenamed
**VENOMOUS#HELPER**
, has impacted over 80 organizations, most of which are in the U.S., according to Securonix. It shares overlaps with clusters previously tracked by
[Red Canary](https://redcanary.com/blog/threat-intelligence/phishing-rmm-tools/)
and Sophos, the latter of which has given it the moniker
[STAC6405](https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html#saas-platforms-abused-for-phishing-delivery)
. While it's not clear who is behind the campaign, the cybersecurity company said it aligns with a financially motivated Initial Access Broker (IAB) or a ransomware precursor operation.

"In this case, a customized SimpleHelp and ScreenConnect RMMs are used to bypass defenses as they are legitimately installed by the unsuspecting victim," researchers Akshay Gaikwad, Shikha Sangwan, and Aaron Beardslee
[said](https://www.securonix.com/blog/venomous-helper-phishing-campaign)
in a report shared with The Hacker News.

Setting aside the fact that the use of legitimate RMM tools can evade detection, the deployment of both SimpleHelp and ScreenConnect indicates an attempt to create a "redundant dual-channel access architecture" that enables continued operations even when either of them is detected and blocked.

It all begins with a phishing email impersonating the U.S. Social Security Administration (SSA), where the recipient is instructed to verify their email address and download a purported SSA statement by clicking on a link embedded in the message. The link points to a legitimate-but-compromised Mexican business website ("gruta.com[.]mx"), indicating a deliberate strategy to evade email spam filters.

The "SSA statement" is then downloaded from a second attacker-controlled domain ("server.cubatiendaalimentos.com[.]mx"), an executable that's responsible for delivering the SimpleHelp RMM tool. It's believed that the attacker gained access to a single cPanel user account on the legitimate hosting server to stage the binary.

As soon as the victim opens the JWrapper-packaged Windows executable, thinking it's a document, the malware installs itself as a Windows service with Safe Mode persistence, makes sure it's running by means of a "self-healing watchdog" that automatically restarts it when killed, and periodically enumerates registered security products using the root\SecurityCenter2 WMI namespace every 67 seconds, and polls user presence every 23 seconds.

To facilitate fully interactive desktop access, the SimpleHelp remote access client acquires SeDebugPrivilege via
[AdjustTokenPrivileges](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges)
, while "elev\_win.exe" – a legitimate executable file associated with the software – is used to gain SYSTEM-level privileges. This, in turn, allows the operator to read the screen, inject keystrokes, and access user-context resources.

This elevated remote access is then abused to download and install ConnectWise ScreenConnect, offering a fallback communication mechanism if the SimpleHelp channel is taken down.

"The deployed SimpleHelp version (5.0.1) provides a comprehensive remote administration capability set," the researchers said. "The victim organization is left in a state where the attacker can return at any time, execute commands silently in the user’s desktop session, transfer files bidirectionally, and pivot to adjacent systems, while standard antivirus and signature-based controls see nothing but legitimately signed software from a reputable U.K. vendor."