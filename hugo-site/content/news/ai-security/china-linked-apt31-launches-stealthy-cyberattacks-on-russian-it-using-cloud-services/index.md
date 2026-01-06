---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-23T00:00:08.080167+00:00'
exported_at: '2025-11-23T00:00:10.308008+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html
structured_data:
  about: []
  author: ''
  description: APT31 secretly targeted Russian IT from 2022–2025 using cloud services,
    social media commands, and CloudyLoader malware to steal sensitive data.
  headline: China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using
    Cloud Services
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/china-linked-apt31-launches-stealthy.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: China-Linked APT31 Launches Stealthy Cyberattacks on Russian IT Using Cloud
  Services
updated_at: '2025-11-23T00:00:08.080167+00:00'
url_hash: 697e79ab41a1ac396ac6130fc99108bba3181157
---

**

Nov 22, 2025
**

Ravie Lakshmanan

Cyber Espionage / Cloud Security

The China-linked advanced persistent threat (APT) group known as
**APT31**
has been attributed to cyber attacks targeting the Russian information technology (IT) sector between 2024 and 2025 while staying undetected for extended periods of time.

"In the period from 2024 to 2025, the Russian IT sector, especially companies working as contractors and integrators of solutions for government agencies, faced a series of targeted computer attacks," Positive Technologies researchers Daniil Grigoryan and Varvara Koloskova
[said](https://ptsecurity.com/research/pt-esc-threat-intelligence/striking-panda-attacks-apt31-today/)
in a technical report.

APT31, also known as Altaire, Bronze Vinewood, Judgement Panda, PerplexedGoblin, RedBravo, Red Keres, and Violet Typhoon (formerly Zirconium), is assessed to be active since at least 2010. It has a track record of striking a wide range of sectors, including governments, financial, and aerospace and defense, high tech, construction and engineering, telecommunications, media, and insurance.

The cyber espionage group is primarily focused on gathering intelligence that can provide Beijing and state-owned enterprises with political, economic, and military advantages. In May 2025, the hacking crew was
[blamed](https://thehackernews.com/2025/05/czech-republic-blames-china-linked.html)
by the Czech Republic for targeting its Ministry of Foreign Affairs.

The attacks aimed at Russia are characterized by the use of legitimate cloud services, mainly those prevalent in the country, like Yandex Cloud, for command-and-control (C2) and data exfiltration in an attempt to blend in with normal traffic and escape detection.

The adversary is also said to have staged encrypted commands and payloads in social media profiles, both domestic and foreign, while also conducting their attacks during weekends and holidays. In at least one attack targeting an IT company, APT31 breached its network as far back as late 2022, before escalating the activity coinciding with the 2023 New Year holidays.

In another intrusion detected in December 2024, the threat actors sent a spear-phishing email containing a RAR archive that, in turn, included a Windows Shortcut (LNK) responsible for launching a Cobalt Strike loader dubbed CloudyLoader via DLL side-loading. Details of this activity were
[previously documented](https://securelist.ru/cobalt-strike-attacks-using-quora-github-social-media/113139/)
by Kaspersky in July 2025, while identifying some overlaps with a threat cluster known as
[EastWind](https://thehackernews.com/2024/08/russian-government-hit-by-eastwind.html)
.

The Russian cybersecurity company also said it identified a ZIP archive lure that masqueraded as a report from the Ministry of Foreign Affairs of Peru to ultimately deploy CloudyLoader.

To facilitate subsequent stages of the attack cycle, APT31 has leveraged an extensive set of publicly available and custom tools. Persistence is achieved by setting up scheduled tasks that mimic legitimate applications, such as Yandex Disk and Google Chrome. Some of them are listed below -

* [SharpADUserIP](https://github.com/evilashz/SharpADUserIP)
  , a C# utility for reconnaissance and discovery
* [SharpChrome.exe](https://github.com/GhostPack/SharpDPAPI)
  , to extract passwords and cookies from Google Chrome and Microsoft Edge browsers
* [SharpDir](https://github.com/jnqpblc/SharpDir)
  , to search files
* [StickyNotesExtract.exe](https://github.com/V1V1/SharpScribbles)
  , to extract data from the Windows Sticky Notes database
* Tailscale VPN, to create an encrypted tunnel and set up a peer-to-peer (P2P) network between the compromised host and their infrastructure
* [Microsoft dev tunnels](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/overview)
  , to tunnel traffic
* [Owawa](https://thehackernews.com/2021/12/hackers-using-malicious-iis-server.html)
  , a malicious IIS module for credential theft
* AufTime, a Linux backdoor that uses the wolfSSL library to communicate with C2
* COFFProxy, a Golang backdoor that supports commands for tunneling traffic, executing commands, managing files, and delivering additional payloads
* VtChatter, a tool that uses Base64-encoded comments to a
  [text file hosted on VirusTotal](https://www.virustotal.com/gui/file/adc9bf081e1e9da2fbec962ae11212808e642096a9788159ac0acef879fd31e8/community)
  as a two-way C2 channel every two hours
* OneDriveDoor, a backdoor that uses Microsoft OneDrive as C2
* [LocalPlugX](https://rt-solar.ru/solar-4rays/blog/3829/)
  , a variant of
  [PlugX](https://thehackernews.com/2025/01/fbi-deletes-plugx-malware-from-4250.html)
  that's used to spread within the local network, rather than to communicate with C2
* [CloudSorcerer](https://thehackernews.com/2024/07/new-apt-group-cloudsorcerer-targets.html)
  , a backdoor that used cloud services as C2
* YaLeak, a .NET tool to upload information to Yandex Cloud

"APT31 is constantly replenishing its arsenal: although they continue to use some of their old tools," Positive Technologies said. "As C2, attackers actively use cloud services, in particular, Yandex and Microsoft OneDrive services. Many tools are also configured to work in server mode, waiting for attackers to connect to an infected host."

"In addition, the grouping exfiltrates data through Yandex's cloud storage. These tools and techniques allowed APT31 to stay unnoticed in the infrastructure of victims for years. At the same time, attackers downloaded files and collected confidential information from devices, including passwords from mailboxes and internal services of victims."