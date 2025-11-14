---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-14T16:15:53.189514+00:00'
exported_at: '2025-11-14T16:15:55.480592+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/iranian-hackers-launch-spearspecter-spy.html
structured_data:
  about: []
  author: ''
  description: Iran’s APT42 launches SpearSpecter campaign using TAMECAT malware,
    targeting defense and government officials.
  headline: Iranian Hackers Launch ‘SpearSpecter’ Spy Operation on Defense & Government
    Targets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/iranian-hackers-launch-spearspecter-spy.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Iranian Hackers Launch ‘SpearSpecter’ Spy Operation on Defense & Government
  Targets
updated_at: '2025-11-14T16:15:53.189514+00:00'
url_hash: 39be7eb8afb20a66d10aece10cd127759a3360d8
---

The Iranian state-sponsored threat actor known as
[APT42](https://thehackernews.com/2022/09/iranian-apt42-launched-over-30.html)
has been observed targeting individuals and organizations that are of interest to the Islamic Revolutionary Guard Corps (IRGC) as part of a new espionage-focused campaign.

The activity, detected in early September 2025 and assessed to be ongoing, has been codenamed
**[SpearSpecter](https://govextra.gov.il/national-digital-agency/cyber/research/spearspecter/)**
by the Israel National Digital Agency (INDA).

"The campaign has systematically targeted high-value senior defense and government officials using personalized social engineering tactics," INDA researchers Shimi Cohen, Adi Pick, Idan Beit-Yosef, Hila David, and Yaniv Goldman said. "These include inviting targets to prestigious conferences or arranging significant meetings."

What's notable about the effort is that it also extends to the targets' family members, creating a broader attack surface that exerts more pressure on the primary targets.

APT42 was first publicly documented in late 2022 by Google Mandiant, detailing its overlaps with another
[IRGC threat cluster](https://thehackernews.com/2023/04/iranian-hackers-launch-sophisticated.html)
tracked as APT35, CALANQUE, Charming Kitten, CharmingCypress, Cobalt Illusion, Educated Manticore, GreenCharlie, ITG18, Magic Hound, Mint Sandstorm (formerly Phosphorus), TA453, and Yellow Garuda.

One of the group's hallmarks is its ability to mount convincing social engineering campaigns that can run for days or weeks in an effort build trust with the targets, in some cases masquerading as known contacts to create an illusion of authenticity, before sending a malicious payload or tricking them into clicking on booby-trapped links.

As recently as June 2025, Check Point
[detailed](https://thehackernews.com/2025/06/iranian-apt35-hackers-targeting-israeli.html)
an attack wave in which the threat actors approached Israeli technology and cyber security professionals by posing as technology executives or researchers in emails and WhatsApp messages.

Goldman told The Hacker News that SpearSpecter and the June 2025 campaign are distinct and have been undertaken by two different sub-groups within APT42.

"While our campaign was carried out by cluster D of APT42 (which focuses more on malware-based operations), the campaign detailed by Check Point was carried out by cluster B of the same group (which focuses more on credential harvesting)," Goldman added.

INDA said SpearSpecter is flexible in that the adversary tweaks its approach based on the value of the target and operational objectives. In one set of attacks, victims are redirected to bogus meeting pages that are designed to capture their credentials. On the other hand, if the end goal is persistent long-term access, the attacks lead to the deployment of a known PowerShell backdoor dubbed TAMECAT that has been
[repeatedly](https://thehackernews.com/2024/05/apt42-hackers-pose-as-journalists-to.html)
put to use in
[recent years](https://thehackernews.com/2024/08/iranian-hackers-set-up-new-network-to.html)
.

To that end, the attack chains involve impersonating trusted WhatsApp contacts to send a malicious link to a supposed required document for an upcoming meeting or conference. When the link is clicked, it initiates a redirect chain to serve a WebDAV-hosted Windows shortcut (LNK) masquerading as a PDF file by
[taking advantage](https://thehackernews.com/2024/06/cybercriminals-exploit-free-software.html)
of the "search-ms:" protocol handler.

The LNK file, for its part, establishes contact with a
[Cloudflare Workers subdomain](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/)
to retrieve a batch script that functions as a loader for TAMECAT, which, in turn, employs various modular components to facilitate data exfiltration and remote control.

The PowerShell framework uses three distinct channels, viz., HTTPS, Discord, and Telegram, for command-and-control (C2), suggesting the threat actor's goal of maintaining persistent access to compromised hosts even if one pathway gets detected and blocked.

For Telegram-based C2, TAMECAT listens for incoming commands from an attacker-controlled Telegram bot, based on which it fetches and executes additional PowerShell code from different Cloudflare Workers subdomains. In the case of Discord, a webhook URL is used to send basic system information and get commands in return from a hard-coded channel.

"Analysis of accounts recovered from the actor's Discord server suggests the command lookup logic relies on messages from a specific user, allowing the actor to deliver unique commands to individual infected hosts while using the same channel to coordinate multiple attacks, effectively creating a collaborative workspace on a single infrastructure," INDA researchers said.

Furthermore, TAMECAT comes equipped with features to conduct reconnaissance, harvest files matching a certain extensions, steal data from web browsers like Google Chrome and Microsoft Edge, collect Outlook mailboxes, and take screenshots at 15-second intervals. The data is exfiltrated over HTTPS or FTP.

It also adopts a variety of stealthy techniques to evade detection and resist analysis efforts. These include encrypting telemetry and controller payloads, source code obfuscation, using living-off-the-land binaries (LOLBins) to hide malicious activities, and operating mostly in memory, thereby leaving little traces on disk.

"The SpearSpecter campaign's infrastructure reflects a sophisticated blend of agility, stealth, and operational security designed to sustain prolonged espionage against high-value targets," INDA said. "operators leverage a multifaceted infrastructure that combines legitimate cloud services with attacker-controlled resources, enabling seamless initial access, persistent command-and-control (C2), and covert data exfiltration."