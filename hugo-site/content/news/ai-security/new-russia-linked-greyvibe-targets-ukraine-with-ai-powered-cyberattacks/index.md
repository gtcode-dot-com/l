---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-01T01:10:11.037582+00:00'
exported_at: '2026-06-01T01:10:13.517144+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html
structured_data:
  about: []
  author: ''
  description: GREYVIBE targeted Ukraine since August 2025 using AI-assisted malware
    campaigns, increasing espionage capabilities and attribution challenges.
  headline: New Russia-Linked GREYVIBE Targets Ukraine with AI-Powered Cyberattacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/new-russian-linked-greyvibe-targets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Russia-Linked GREYVIBE Targets Ukraine with AI-Powered Cyberattacks
updated_at: '2026-06-01T01:10:11.037582+00:00'
url_hash: 46fc71566ca0b384deb11626173fc8270bc331c8
---

**

Ravie Lakshmanan
**

May 29, 2026

Cyber Espionage / Artificial Intelligence

A previously undocumented threat actor dubbed
**GREYVIBE**
has been attributed to ongoing and persistent attacks targeting Ukraine and Ukraine-related entities since at least August 2025.

GREYVIBE, per WithSecure, is assessed to be a Russian-speaking group operating broadly in the Russian time zone, with the activities aligning with Kremlin state interests, specifically when it comes to intelligence gathering efforts aimed at Ukraine in the context of the ongoing Russo-Ukrainian war.

"The group has leveraged multiple attack vectors, including spear-phishing e-mails, fake captcha pages, and fraudulent Ukrainian adult club websites, to deliver malware to a diverse set of victims," WithSecure researcher Mohammad Kazem Hassan Nejad
[said](https://labs.withsecure.com/publications/greyvibe)
in an analysis. "Across these campaigns, the group has relied on custom-developed obfuscators, loaders, and malware."

The victimology footprint spans military, government, civilian, and business-related organizations. GREYVIBE, its nation-state-affiliated activity notwithstanding, also shares ties to the broader Russian cybercrime ecosystem through some of its members who are believed to be current or former cybercriminal actors.

In addition, there is evidence indicating that the adversary is relying on generative artificial intelligence (GenAI) and large language models (LLMs) to supercharge its operations. Taken together, WithSecure paints the picture of a "low-to-moderately sophisticated group" that suffers from operational security blunders and employs AI-assisted tooling to augment its malware development efforts.

GREYVIBE has been observed using multiple attack chains against its targets -

* **PhantomMail**
  , which uses spear-phishing emails to distribute links pointing to malicious ZIP or RAR archives hosted on Google Drive and 4sync that contain JavaScript-based loaders to launch a decoy document, and PhantomRelay, a PowerShell-based remote access trojan (RAT) designed to profile the host and run PowerShell scripts and Windows commands.
* **PhantomClick**
  , which uses
  [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
  -style fake CAPTCHA pages on bogus domains masquerading as Zoom and LAPAS to trick users into running commands that initiate a PhantomRelay infection chain.
* **PrincessClub**
  , which uses fake Ukrainian adult-club websites to deliver FallSpy on Android and PhantomRelayV1 or LegionRelay on Windows, with subsequent iterations of the lure sites introducing a WebRTC-based live call feature to capture victim audio and video. While FallSpy is an Android spyware capable of harvesting sensitive data from the compromised device, LegionRelay is a lightweight PowerShell-based RAT that supports file enumeration, file exfiltration, screenshot capture, browser data theft, Telegram and WhatsApp data exfiltration, and RDP access setup. PhantomRelayV1 is a variant of PhantomRelay with a custom watchdog persistence mechanism.
* **DroneLink**
  , which uses websites masquerading as charitable foundations supporting the Armed Forces of Ukraine to deliver WireGuard and LegionRelay.
* **Nebo**
  , which uses a FallSpy sample that mimics a Russian-language login screen, likely in an attempt to deceive Ukrainian military personnel into thinking they were accessing a Russian military terminal.

The variety of delivery vectors and tools used in the attacks likely stems from the use of AI platforms, including Ideogram AI, OpenAI ChatGPT, and Google Gemini, to assist with generating images and developing LegionRelay, as well as obfuscation and loader scripts, backend infrastructure, and post-compromise commands.

The cybersecurity company said GREYVIBE's usage of AI serves multiple advantages, including bridging gaps in technical expertise, accelerating the development lifecycle, and reducing reliance on previously known malware or tools that could aid in attribution efforts.

"If an actor can frequently generate, refactor, or replace components of its operational footprint with AI assistance, traditional clustering methods based on stable technical artifacts may become less reliable over time," Nejad said.

That said, the use of AI has also had the side effect of introducing design flaws into LegionRelay, exposing the malware's backend functionality. This is another sign suggesting GREYVIBE may not be a pure nation-state actor, as sophisticated adversaries are unlikely to make such mistakes.

The hacking group's links to the cybercriminal ecosystem are based on multiple factors -

* Possible access to and use of an ISO builder with suspected ties to the TrickBot gang and
  [UAC-0098](https://thehackernews.com/2022/09/some-members-of-conti-group-targeting.html)
* Presence of PhantomRelay variants across seemingly unrelated cybercrime activity clusters, such as a
  [Microsoft](https://fieldeffect.com/blog/quick-you-need-assistance)
  Teams
  [voice](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html)
  [phishing](https://fieldeffect.com/blog/quick-you-need-assistance)
  [campaign](https://www.nccgroup.com/research/rapid-breach-social-engineering-to-remote-access-in-300-seconds/)
  between July 2025 and February 2026, and a
  [KongTuke](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html)
  delivery chain between late February and late March 2026 that used ClickFix to distribute the malware.
* The upload of early development and test samples to VirusTotal
* Use of internet slang terms like "letsrollboyos," "totallyunsus," and "cuteuwu" as naming conventions for development artifacts.
* The deployment of XMRig miner on a small number of LegionRelay-infected machines

"Taken together, we assess with moderate confidence that the group has ties to the broader cybercrime ecosystem, and with low-to-moderate confidence that it involves current or former cybercriminal members," WithSecure said. "The exact nature of their relationship to the Russian state remains unclear, whether such members have been absorbed into a state-backed group, operate independently under state-directed tasking, or have formed a hybrid team."

"The group occupies a grey area between cybercrime and state-affiliated activity, complicating attribution efforts and blurring traditional distinctions between these categories."