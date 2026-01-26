---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-26T10:15:12.194125+00:00'
exported_at: '2026-01-26T10:15:14.435927+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html
structured_data:
  about: []
  author: ''
  description: North Korean group Konni uses AI-assisted PowerShell malware and phishing
    via Google ads and Discord to breach blockchain development environments.
  headline: Konni Hackers Deploy AI-Generated PowerShell Backdoor Against Blockchain
    Developers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/konni-hackers-deploy-ai-generated.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Konni Hackers Deploy AI-Generated PowerShell Backdoor Against Blockchain Developers
updated_at: '2026-01-26T10:15:12.194125+00:00'
url_hash: 5919fadbcd1968235f1ca461f2396609258c0463
---

**

Ravie Lakshmanan
**

Jan 26, 2026

Malware / Endpoint Security

The North Korean threat actor known as
**Konni**
has been observed using PowerShell malware generated using artificial intelligence (AI) tools to target developers and engineering teams in the blockchain sector.

The phishing campaign has targeted Japan, Australia, and India, highlighting the adversary's expansion of the targeting scope beyond
[South Korea](https://thehackernews.com/2022/01/north-korean-hackers-return-with.html)
,
[Russia](https://thehackernews.com/2023/11/konni-group-using-russian-language.html)
,
[Ukraine](https://thehackernews.com/2025/05/north-korean-konni-apt-targets-ukraine.html)
, and
[European nations](https://thehackernews.com/2022/07/north-korean-hackers-using-malicious.html)
, Check Point Research
[said](https://research.checkpoint.com/2026/konni-targets-developers-with-ai-malware/)
in a technical report published last week.

Active since at least 2014, Konni is primarily known for its targeting of organizations and individuals in South Korea. It's also tracked as Earth Imp, Opal Sleet, Osmium, TA406, and Vedalia.

In November 2025, the Genians Security Center (GSC)
[detailed](https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html)
the hacking group's targeting of Android devices by exploiting Google's asset tracking service, Find Hub, to remotely reset victim devices and erase personal data from them, signaling a new escalation of their tradecraft.

As recently as this month, Konni has been observed distributing spear-phishing emails containing malicious links that are disguised as harmless advertising URLs associated with Google and Naver's advertising platforms to bypass security filters and deliver a remote access trojan codenamed EndRAT.

The campaign has been codenamed Operation Poseidon by the GSC, with the attacks impersonating North Korean human rights organizations and financial institutions in South Korea. The attacks are also characterized by the use of improperly secured WordPress websites to distribute malware and for command-and-control (C2) infrastructure.

The email messages have been found to masquerade as financial notices, such as transaction confirmations or wire transfer requests, to trick recipients into downloading ZIP archives hosted on WordPress sites. The ZIP file comes with a Windows shortcut (LNK) that's designed to execute an AutoIt script disguised as a PDF document. The AutoIt script is a known Konni malware called EndRAT (aka EndClient RAT).

"This attack is analyzed as a case that effectively bypassed email security filtering and user vigilance through a spear-phishing attack vector that exploited the ad click redirection mechanism used within the Google advertising ecosystem," the South Korean security outfit
[said](https://www.genians.co.kr/en/blog/threat_intelligence/spear-phishing)
.

"It was confirmed that the attacker utilized the redirection URL structure of a domain used for legitimate ad click tracking (ad.doubleclick[.]net) to incrementally direct users to external infrastructure where actual malicious files were hosted."

The latest campaign documented by Check Point leverages ZIP files mimicking project requirements-themed documents and hosted on Discord's content delivery network (CDN) to unleash a multi-stage attack chain that performs the following sequence of actions. The exact initial access vector used in the attacks is unknown.

* The ZIP archive contains a PDF decoy and an LNK file
* The shortcut file launches an embedded PowerShell loader which extracts two additional files, a Microsoft Word lure document and a CAB archive, and displays as the Word document as a distraction mechanism
* The shortcut file extracts the contents of the CAB archive, which contains a PowerShell Backdoor, two batch scripts, and an executable used for User Account Control (UAC) bypass
* The first batch script is used to prepare the environment, establish persistence using a scheduled task, stage the backdoor and execute it, following which it deletes itself from disk to reduce forensic visibility
* The PowerShell backdoor carries out a string of anti-analysis and sandbox-evasion checks, and then proceeds to profile the system and attempts to elevate privileges using the
  [FodHelper UAC bypass](https://thehackernews.com/2023/08/new-nodestealer-targeting-facebook.html)
  technique
* The backdoor performs cleanup of the previously dropped UAC bypass executable, configures Microsoft Defender exclusion for "C:\ProgramData," and runs the second batch script to replace the previously created scheduled task with a new one that's capable of running with elevated privileges
* The backdoor proceeds to drop SimpleHelp, a legitimate Remote Monitoring and Management (RMM) tool for persistent remote access, and communicates with a C2 server that's safeguarded by an encryption gate intended to block non-browser traffic to periodically send host metadata and execute PowerShell code returned by the server

The cybersecurity company said there are indications that the PowerShell backdoor was created with the assistance of an AI tool, citing its modular structure, human-readable documentation, and the presence of source code comments like "# <– your permanent project UUID."

"Instead of focusing on individual end-users, the campaign goal seems to be to establish a foothold in development environments, where compromise can provide broader downstream access across multiple projects and services," Check Point said. "The introduction of AI-assisted tooling suggests an effort to accelerate development and standardize code while continuing to rely on proven delivery methods and social engineering."

The findings coincide with the discovery of multiple North Korea-led campaigns that facilitate remote control and data theft -

* A spear-phishing campaign that
  [uses](https://www.darktrace.com/blog/darktrace-identifies-campaign-targeting-south-korea-leveraging-vs-code-for-remote-access)
  JavaScript Encoded (JSE) scripts mimicking Hangul Word Processor (HWPX) documents and government-themed decoy files to deploy a
  [Visual Studio Code (VS Code) tunnel](https://thehackernews.com/2024/12/hackers-weaponize-visual-studio-code.html)
  to establish remote access
* A phishing campaign that distributes
  [LNK files](https://sect.iij.ad.jp/blog/2026/01/dprk-moonpeak-executed-via-malicious-lnk-file/)
  masquerading as PDF documents to launch a PowerShell script that detects virtual and malware analysis environments and delivers a remote access trojan called
  [MoonPeak](https://thehackernews.com/2025/08/north-korea-uses-github-in-diplomat.html)
* A set of two cyber attacks, assessed to be conducted by
  [Andariel](https://labs.withsecure.com/publications/andariel-2025)
  in 2025, that targeted an unnamed European entity belonging to the legal sector to deliver
  [TigerRAT](https://thehackernews.com/2024/10/andariel-hacker-group-shifts-focus-to.html)
  , as well as compromised a South Korean Enterprise Resource Planning (ERP) software vendor's update mechanism to distribute three new trojans to downstream victims, including StarshellRAT, JelusRAT, and GopherRAT

According to Finnish cybersecurity company WithSecure, the ERP vendor's software has been the target of
[similar supply chain compromises](https://thehackernews.com/2024/07/south-korean-erp-vendors-server-hacked.html)
twice in the past – in 2017 and again in 2024 – to deploy malware families like HotCroissant and Xctdoor.

While JelusRAT is written in C++ and supports capabilities to retrieve plugins from the C2 server, StarshellRAT is developed in C# and supports command execution, file upload/download, and screenshot capture. GopherRAT, on the other hand, is based on Golang and features the ability to run commands or binaries, exfiltrate files, and enumerate the file system.

"Their targeting and objectives have varied over time; some campaigns have pursued financial gain, while others have focused on stealing information aligned with the regime's priority intelligence needs," WithSecure researcher Mohammad Kazem Hassan Nejad said. "This variability underscores the group's flexibility and its ability to support broader strategic goals as those priorities change over time."