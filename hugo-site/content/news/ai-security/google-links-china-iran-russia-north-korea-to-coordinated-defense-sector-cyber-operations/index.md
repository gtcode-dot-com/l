---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-19T04:26:10.364170+00:00'
exported_at: '2026-02-19T04:26:12.420471+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/google-links-china-iran-russia-north.html
structured_data:
  about: []
  author: ''
  description: State-backed hackers from China, Russia, Iran, and North Korea target
    defense contractors using espionage, malware, hiring scams, and edge exploits.
  headline: Google Links China, Iran, Russia, North Korea to Coordinated Defense Sector
    Cyber Operations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/google-links-china-iran-russia-north.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Links China, Iran, Russia, North Korea to Coordinated Defense Sector
  Cyber Operations
updated_at: '2026-02-19T04:26:10.364170+00:00'
url_hash: a64aae078076e9525e4dd543c20cb2963f5dab80
---

**

Ravie Lakshmanan
**

Feb 13, 2026

Malware / Critical Infrastructure

Several state-sponsored actors, hacktivist entities, and criminal groups from China, Iran, North Korea, and Russia have trained their sights on the defense industrial base (DIB) sector, according to findings from Google Threat Intelligence Group (GTIG).

The tech giant's threat intelligence division said the adversarial targeting of the sector is centered around four key themes: striking defense entities deploying technologies on the battlefield in the Russia-Ukraine War, directly approaching employees and exploitation of the hiring process by North Korean and Iranian actors, use of edge devices and appliances as initial access pathways for China-nexus groups, and supply chain risk stemming from the breach of the manufacturing sector.

"Many of the chief state-sponsors of cyber espionage and hacktivist actors have shown an interest in autonomous vehicles and drones, as these platforms play an increasing role in modern warfare," GTIG
[said](https://cloud.google.com/blog/topics/threat-intelligence/threats-to-defense-industrial-base)
. "Further, the 'evasion of detection' trend [...] continues, as actors focus on single endpoints and individuals, or carry out intrusions in a manner that seeks to avoid endpoint detection and response (EDR) tools altogether."

Some of the notable threat actors that have participated in the activity include -

* **[APT44 (aka Sandworm)](https://thehackernews.com/2025/12/amazon-exposes-years-long-gru-cyber.html)**
  has attempted to exfiltrate information from Telegram and Signal encrypted messaging applications, likely after securing physical access to devices obtained during on-ground operations in Ukraine. This includes the use of a Windows batch script called WAVESIGN to decrypt and exfiltrate data from Signal's desktop app.
* **[TEMP.Vermin (aka UAC-0020)](https://thehackernews.com/2024/06/spectr-malware-targets-ukraine-defense.html)**
  has used malware like VERMONSTER, SPECTRUM (aka SPECTR), and FIRMACHAGENT using lure content revolving around drone production and development, anti-drone defense systems, and video surveillance security systems.
* **[UNC5125 (aka FlyingYeti and UAC-0149)](https://thehackernews.com/2024/05/flyingyeti-exploits-winrar.html)**
  has conducted highly targeted campaigns focusing on frontline drone units. It has used a questionnaire hosted on Google Forms to conduct reconnaissance against prospective drone operators, and distributed via messaging apps malware like MESSYFORK (aka COOKBOX) to an Unmanned Aerial Vehicle (UAV) operator based in Ukraine.
* **UNC5125**
  is also said to have leveraged an Android malware called GREYBATTLE, a bespoke version of the
  [Hydra](https://thehackernews.com/2021/11/4-android-banking-trojan-campaigns.html)
  banking trojan, to steal credentials and data by distributing it via a website spoofing a Ukrainian military artificial intelligence company.
* **[UNC5792 (aka UAC-0195)](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html)**
  has exploited secure messaging apps to target Ukrainian military and government entities, as well as individuals and organizations in Moldova, Georgia, France, and the U.S. The threat actor is notable for weaponizing Signal's device linking feature to hijack victim accounts.
* **[UNC4221 (aka UAC-0185)](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html)**
  has also targeted secure messaging apps used by Ukrainian military personnel, using tactics similar to UNC5792. The threat actor has also leveraged an Android malware called STALECOOKIE that mimics Ukraine's battlefield management platform
  [DELTA](https://thehackernews.com/2022/12/ukraines-delta-military-system-users.html)
  to steal browser cookies. Another tactic employed by the group is the use of
  [ClickFix](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)
  to deliver the TINYWHALE downloader that, in turn, drops the
  [MeshAgent](https://thehackernews.com/2024/12/cert-ua-warns-of-phishing-attacks.html)
  remote management software.
* **UNC5976**
  , a Russian espionage cluster that has conducted a phishing campaign delivering malicious RDP connection files that are configured to communicate with actor-controlled domains mimicking a Ukrainian telecommunications company.
* **UNC6096**
  , a Russian espionage cluster that has conducted malware delivery operations via WhatsApp using DELTA-related themes to deliver a malicious LNK shortcut within an archive file that downloads a secondary payload. Attacks aimed at Android devices have been found to deliver malware called GALLGRAB that collects locally stored files, contact information, and potentially encrypted user data from specialized battlefield applications.
* **UNC5114**
  , a suspected Russian espionage cluster that has delivered a variant of an off-the-shelf Android malware called
  [CraxsRAT](https://thehackernews.com/2024/10/russian-espionage-group-targets.html)
  by masquerading it as an update for
  [Kropyva](https://united24media.com/war-in-ukraine/ukraines-secret-weapon-kropyva-software-4026)
  , a combat control system used in Ukraine.
* **[APT45 (aka Andariel)](https://thehackernews.com/2024/07/us-doj-indicts-north-korean-hacker-for.html)**
  has targeted South Korean defense, semiconductor, and automotive manufacturing entities with
  [SmallTiger](https://asec.ahnlab.com/en/74039/)
  malware.
* **[APT43 (aka Kimsuky)](https://thehackernews.com/2025/02/north-korean-apt43-uses-powershell-and.html)**
  has likely leveraged infrastructure mimicking German and U.S. defense-related entities to deploy a backdoor called THINWAVE.
* **[UNC2970 (aka Lazarus Group)](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html)**
  has conducted the Operation Dream Job campaign to target aerospace, defense, and energy sectors, in addition to relying on artificial intelligence (AI) tools to conduct reconnaissance on its targets.
* **[UNC1549 (aka Nimbus Manticore)](https://thehackernews.com/2025/11/iranian-hackers-use-deeproot-and.html)**
  has targeted aerospace, aviation, and defense industries in the Middle East with malware families like MINIBIKE, TWOSTROKE, DEEPROOT, and CRASHPAD. The group is known to orchestrate Lazarus Group-style
  [Dream Job campaigns](https://thehackernews.com/2025/09/unc1549-hacks-34-devices-in-11-telecom.html)
  to trick users into executing malware or giving up credentials under the guise of legitimate employment opportunities.
* **UNC6446**
  , an Iranian-nexus threat actor that has used resume builder and personality test applications to distribute custom malware to targets in the aerospace and defense vertical across the U.S. and the Middle East.
* **[APT5 (aka Keyhole Panda and Mulberry Typhoon)](https://thehackernews.com/2022/12/hackers-actively-exploiting-citrix-adc.html)**
  has targeted current and former employees of major aerospace and defense contractors with tailored phishing lures.
* **[UNC3236 (aka Volt Typhoon)](https://thehackernews.com/2024/02/chinese-hackers-operate-undetected-in.html)**
  has conducted reconnaissance activity against publicly hosted login portals of North American military and defense contractors, while using the ARCMAZE obfuscation framework to conceal its origin.
* **UNC6508**
  , a China-nexus threat cluster that targeted a U.S.-based research institution in late 2023 by leveraging a REDCap exploit to drop a custom malware named INFINITERED that's capable of persistent remote access and credential theft after intercepting the application's software upgrade process.

In addition, Google said it has also observed China-nexus threat groups utilizing
[operational relay box (ORB) networks](https://www.team-cymru.com/post/tracking-orbs-on-singapores-telecommunications-networks)
for reconnaissance against defense industrial targets, thereby complicating detection and attribution efforts.

ORBs confer several advantages to threat actors, allowing them to route their traffic through home or commercial networks, blend with regular network traffic, circumvent geofencing security controls, and pre-position themselves to a target's perimeter ahead of a cyber attack. ORBs are also resilient to takedown attempts, as attackers managing them can scale these networks to add more devices, even if some nodes are discovered and blocked.

"While specific risks vary by geographic footprint and sub-sector specialization, the broader trend is clear: the defense industrial base is under a state of constant, multi-vector siege," Google said. "Financially motivated actors carry out extortion against this sector and the broader manufacturing base, like many of the other verticals they target for monetary gain."

"The campaigns against defense contractors in Ukraine, threats to or exploitation of defense personnel, the persistent volume of intrusions by China-nexus actors, and the hack, leak, and disruption of the manufacturing base are some of the leading threats to this industry today."