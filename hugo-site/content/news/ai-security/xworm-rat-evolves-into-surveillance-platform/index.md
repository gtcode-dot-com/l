---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T00:13:22.054719+00:00'
exported_at: '2026-10-15T00:13:29.731040+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform
structured_data:
  about: []
  author: ''
  description: Expanded plugin count allows the malware to monitor users’ location,
    stream live audio, and interact with authenticated browser sessions.
  headline: XWorm RAT Evolves Into Surveillance Platform
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform
  publisher:
    logo: /favicon.ico
    name: GTCode
title: XWorm RAT Evolves Into Surveillance Platform
updated_at: '2026-10-15T00:13:22.054719+00:00'
url_hash: fc404d9151bf834b209f034c1d2482e8dca14fc8
---

### [Malware &amp; Threats](https://www.securityweek.com/category/malware-cyber-threats/)

# XWorm RAT Evolves Into Surveillance Platform

Expanded plugin count allows the malware to monitor users’ location, stream live audio, and interact with authenticated browser sessions.

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

|


October 13, 2026 (7:13 AM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=XWorm RAT Evolves Into Surveillance Platform https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/)
  [+ Whatsapp](whatsapp://send?text=XWorm RAT Evolves Into Surveillance Platform https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/)
  [+ Email](/cdn-cgi/l/email-protection#4a75393f28202f293e77121d2538276a180b1e6a0f3c25263c2f396a03243e256a193f383c2f2326262b24292f6a1a262b3e2c2538276c2b273a7108050e1377036a2c253f242e6a3e2223396a2b383e2329262f6a23243e2f382f393e23242d6a2b242e6a3e22253f2d223e6a252c6a39222b3823242d6a233e6a3d233e226a33253f646a09222f29216a233e6a253f3e706a223e3e3a397065653d3d3d64392f293f38233e333d2f2f216429252765323d25382767382b3e672f3c25263c2f396723243e2567393f383c2f2326262b24292f673a262b3e2c25382765)

![Malware](https://www.securityweek.com/wp-content/uploads/2026/08/malware-infection.webp)

**The XWorm RAT developers have expanded the malware’s capabilities with fresh plugins that turn it into a surveillance platform, cybersecurity firm Netskope reports.**

A sophisticated, multi-functional Windows RAT first observed in 2022, XWorm provides attackers with full control over the infected systems, offering keylogging, screenshot capture, webcam access, and payload execution capabilities.

The malware’s developers have been constantly updating its codebase and adding new functionality, and the threat has remained highly active, with Netskope observing over 1,200 incidents across 100 organizations during the third quarter of the year.

Alongside new variants, the developers have also increased the number of plugins XWorm supports, from 35 in July 2025 to 46 in October 2026.

Some of these have been clearly designed for surveillance: enabling location tracking, live audio streaming, webcam capture, and interactive control over authenticated browser sessions.

“The Maps plugin provides victims’ GPS location without a user prompt. The Microphone plugin streams live audio from the victim’s device. HBrowser hijacks authenticated browser sessions without touching credentials, bypassing MFA entirely. Webcam capture is also available on demand,”
[Netskope says](https://threatlabs.netskope.com/blog/2026/09/xworm-reborn)
.

Advertisement. Scroll to continue reading.

According to the cybersecurity company, the activity surrounding XWorm has increased since a cracked version of its builder was released publicly in June 2025, and the source code for RAT’s 6.4 version was leaked in August 2025.

With the addition of the HBrowser plugin, the RAT moves beyond harvesting credentials and user data from browsers: it provides the operator with a real-time view of the browser and can relay attacker inputs to the browser.

Operator’s interactions are encoded as command-and-control (C&amp;C) commands, transmitted over the standard XWorm AES-encrypted communication channel, and executed on the victim’s system.

“The victim machine receives them and executes the corresponding input on the active browser window. The operator receives a continuous stream of screenshots. From the operator’s perspective, it is a full remote browser session. Every authenticated tab is accessible, bypassing the need for logging in and dealing with MFA,” the company explains.

The Maps and Microphone
plugins allow operators to monitor the victim’s location and to capture audio without privilege escalation and without a user warning.

“XWorm continues to evolve and has now added surveillance capabilities. Since its builder and source code were leaked, we expect continued upgrades and use of this toolkit,” Netskope notes.

**Related:**
[Pre-Baked Firmware Malware Hits Budget Android Devices in 150+ Countries](https://www.securityweek.com/pre-baked-firmware-malware-hits-budget-android-devices-in-150-countries/)

**Related:**
[US Disrupts Chinese State-Sponsored Hacking Tools](https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)

**Related:**
[Linux Backdoor Abuses STUN Protocol, Exploits Dozens of Flaws](https://www.securityweek.com/linux-backdoor-abuses-stun-protocol-exploits-dozens-of-flaws/)

**Related:**
[macOS Users Targeted by Fake Zoom Installer Carrying CloudSyncD Backdoor](https://www.securityweek.com/macos-users-targeted-by-fake-zoom-installer-carrying-cloudsyncd-backdoor/)

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

Written By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

Ionut Arghire is an international correspondent for SecurityWeek.

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.

## More from [Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

* [SAP Patches Critical NetWeaver, S/4HANA Vulnerabilities](https://www.securityweek.com/sap-patches-critical-netweaver-s-4hana-vulnerabilities/)
* [$86 Million Crypto Heist Linked to Ledger Signer Hardware Implant](https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/)
* [Cyberattack Prompts Grocery Giant Ahold Delhaize to Disconnect Systems](https://www.securityweek.com/cyberattack-prompts-ahold-delhaize-to-disconnect-systems/)
* [Refrigeration Controller Hack Spoils Food Across European Supermarkets](https://www.securityweek.com/refrigeration-controller-hack-spoils-food-across-european-supermarkets/)
* [Mastermind of 15,000-Mule Cybercrime Laundering Network Pleads Guilty in US](https://www.securityweek.com/mastermind-of-15000-mule-cybercrime-laundering-network-pleads-guilty-in-us/)
* [iRhythm Data Breach Impacts at Least 360,000 People](https://www.securityweek.com/irhythm-data-breach-impacts-over-360000-people/)
* [Critical SonicWall Vulnerability Exploited Days After Disclosure](https://www.securityweek.com/critical-sonicwall-vulnerability-exploited-days-after-disclosure/)
* [Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch](https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch/)

## Latest News

* [AI Agents Navigate Unfamiliar OT Systems and Move Equipment in Minutes, Booz Allen Finds](https://www.securityweek.com/ai-agents-navigate-unfamiliar-ot-systems-and-move-equipment-in-minutes-booz-allen-finds/)
* [ICS Patch Tuesday: Siemens Issues 17 Advisories, Rockwell Fixes ArmorBlock Takeover Flaw](https://www.securityweek.com/ics-patch-tuesday-siemens-issues-17-advisories-rockwell-fixes-armorblock-takeover-flaw/)
* [Harmonic Security Raises $50 Million for Workforce AI Protection](https://www.securityweek.com/harmonic-security-raises-50-million-for-workforce-ai-protection/)
* [Virtual Event Today: Zero Trust Strategies Summit](https://www.securityweek.com/virtual-event-today-zero-trust-strategies-summit-2/)
* [Microsoft Disrupts Chinese-Language Phishing Market Behind 1B+ Messages](https://www.securityweek.com/microsoft-disrupts-chinese-language-phishing-market-behind-1b-messages/)
* [US Arrests Two in Crackdown on North Korean IT Worker Laptop Farms](https://www.securityweek.com/us-arrests-two-in-crackdown-on-north-korean-it-worker-laptop-farms/)
* [Chrome, Firefox Updates Patch 114 Flaws as Mozilla Unveils Firefox Enterprise](https://www.securityweek.com/chrome-firefox-updates-patch-114-flaws-as-mozilla-unveils-firefox-enterprise/)
* [Citrix, Fortinet, Ivanti Patch 29 Vulnerabilities Across Their Products](https://www.securityweek.com/citrix-fortinet-ivanti-patch-29-vulnerabilities-across-their-products/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark.png)

#### Trending

## [iRhythm Data Breach Impacts at Least 360,000 People](https://www.securityweek.com/irhythm-data-breach-impacts-over-360000-people/)

## [Meta Says Hackers Took Code, Personal Data of 1,500 in GitHub Breach](https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/)

## [Cyberattack Prompts Grocery Giant Ahold Delhaize to Disconnect Systems](https://www.securityweek.com/cyberattack-prompts-ahold-delhaize-to-disconnect-systems/)

## [Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns](https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)

## [US Seeks Alleged Chinese Hafnium Hacker With $10 Million Reward](https://www.securityweek.com/us-seeks-alleged-chinese-hafnium-hacker-with-10-million-reward/)

## [Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day](https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/)

## [Adobe Patches 176 Vulnerabilities Across 11 Products](https://www.securityweek.com/adobe-patches-140-vulnerabilities-across-10-products/)

## [Ransomware Response Expert Arrested in ShinyHunters FBI Hack Probe](https://www.securityweek.com/ransomware-response-expert-arrested-in-shinyhunters-fbi-hack-probe/)

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts.

[## Webinar: The AI Access Risk Already in Your Google Workspace](https://event.on24.com/wcc/r/5521433/0D49F418CC4E7B4F3B4901B44C13F604?partnerref=awidget)

October 19, 2026

AI tools connected to Google Workspace can access millions of sensitive emails and files. Join this session to uncover your organization’s risk and learn a framework to manage AI access.

[Register](https://event.on24.com/wcc/r/5521433/0D49F418CC4E7B4F3B4901B44C13F604?partnerref=awidget)

[## Virtual Event: Zero Trust &amp; Identity Strategies Summit 2026](https://register.securityweek.com/zero-trust-summit)

October 14, 2026

Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit trust and continuously validating every stage of a digital interaction.

[Register](https://register.securityweek.com/zero-trust-summit)

#### People on the Move

Adam Zolle has joined Nike as CISO.

Jeff Hackett has been appointed CFO at internet intelligence provider Censys.

Accenture Federal Services has named Nathaniel Parker as CISO.

[More People On The Move](/industry-moves)

#### Expert Insights

[## AI Has Changed Attack Speed, Not Security Fundamentals](https://www.securityweek.com/ai-has-changed-attack-speed-not-security-fundamentals/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/Josh-Goldfarb-F5.jpeg)

As AI accelerates vulnerability discovery and exploitation, so-called virtual patching still comes down to defense-in-depth and strong application security fundamentals.
[(Joshua Goldfarb)](https://www.securityweek.com/contributors/joshua-goldfarb/)

[## Four Cyber Threats Harboring Big Plans for the Future](https://www.securityweek.com/four-cyber-threats-harboring-big-plans-for-the-future/)

![](https://www.securityweek.com/wp-content/uploads/2025/10/Steve_Durbin-ISF.jpg)

- AI, supply-chain exposure, quantum computing and geopolitical conflict are testing security programs. Preparing for disruption must become part of day-to-day operations.
[(Steve Durbin)](https://www.securityweek.com/contributors/stevedurbin/)

[## Begin at the End: How to Enable Agentic Remediation](https://www.securityweek.com/begin-at-the-end-how-to-enable-agentic-remediation/)

![](https://www.securityweek.com/wp-content/uploads/2025/12/Nadir_Izrael_Armis.jpg)

Agentic remediation is not an act of faith. We are talking about fixing known problems, not judgment calls about unfamiliar risk.
[(Nadir Izrael)](https://www.securityweek.com/contributors/nadir-izrael/)

[## “We Think the Security Control Is Working” Is No Longer Good Enough](https://www.securityweek.com/we-think-the-security-control-is-working-is-no-longer-good-enough/)

![](https://www.securityweek.com/wp-content/uploads/2026/08/Sravish-Sridhar_TrustCloud.jpeg)

Point-in-time audits and sampled assessments offer only snapshots; continuous control monitoring provides evidence that security controls are working today.
[(Sravish Sridhar)](https://www.securityweek.com/contributors/sravish-sridhar/)

[## This Key Will Self-Destruct: An Open Standard for Revocable API Keys](https://www.securityweek.com/this-key-will-self-destruct-an-open-standard-for-revocable-api-keys/)

![](https://www.securityweek.com/wp-content/uploads/2023/05/Matt-Honea.jpg)

Every leaked credential should be dead, or dying, within sixty seconds of being found. Here's a proposal to make that the default.
[(Matt Honea)](https://www.securityweek.com/contributors/matt-honea/)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=XWorm RAT Evolves Into Surveillance Platform https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/)
  [+ Whatsapp](whatsapp://send?text=XWorm RAT Evolves Into Surveillance Platform https://www.securityweek.com/xworm-rat-evolves-into-surveillance-platform/)
  [+ Email](/cdn-cgi/l/email-protection#67581412050d0204135a3f3008150a47352633472211080b110214472e0913084734121511020e0b0b0609040247370b06130108150a41060a175c2528233e5a2e47010812090347130f0e14470615130e040b02470e091302150214130e09004706090347130f0812000f1347080147140f06150e0900470e1347100e130f471e08124947240f02040c470e13470812135d470f131317145d48481010104914020412150e131e1002020c4904080a481f1008150a4a1506134a0211080b1102144a0e0913084a14121511020e0b0b060904024a170b06130108150a48)



[![SecurityWeek](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark@2x.png)](https://www.securityweek.com/)

### Popular Topics

* [Cybersecurity News](https://www.securityweek.com/)
* [Industrial Cybersecurity](https://www.icscybersecurityconference.com/)

### Security Community

* [Virtual Cybersecurity Events](https://www.securitysummits.com)
* [Webcast Library](https://gateway.on24.com/wcc/eh/1220486/securityweek-webcast-library)
* [CISO Forum](https://www.cisoforum.com/)
* [AI Risk Summit](https://www.airisksummit.com/?utm_source=securityweek)
* [ICS Cybersecurity Conference](https://www.icscybersecurityconference.com/)
* [Cybersecurity Newsletters](https://www.securityweek.com/subscribe/)

### Stay Intouch

* [Cyber Weapon Discussion Group](https://www.linkedin.com/groups?mostPopular=&amp;gid=3551517)
* [RSS Feed](/feed)
* [Security Intelligence Group](https://www.linkedin.com/groups/?gid=4439585)
* [Follow SecurityWeek on LinkedIn](https://www.linkedin.com/company/securityweek/)

### About SecurityWeek

* [Advertising](https://advertise.securityweek.com/info)
* [Event Sponsorships](https://advertise.securityweek.com/events)
* [Writing Opportunities](https://advertise.securityweek.com/contact-securityweek)
* [Feedback/Contact Us](https://advertise.securityweek.com/contact-securityweek)
* [Privacy Policy](https://www.securityweek.com/privacy-policy/)

### News Tips

Got a confidential news tip? We want to hear from you.

[Submit Tip](/submit-tip)

### Advertising

Reach a large audience of enterprise cybersecurity professionals

[Contact Us](https://advertise.securityweek.com/info)

### Daily Briefing Newsletter

Subscribe to the SecurityWeek Daily Briefing and get the latest content delivered to your inbox.

* [Privacy Policy](https://www.securityweek.com/privacy-policy/)

Copyright © 2026 SecurityWeek ®, a Wired Business Media Publication. All Rights Reserved.