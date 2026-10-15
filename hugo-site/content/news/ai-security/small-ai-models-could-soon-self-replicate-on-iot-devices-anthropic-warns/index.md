---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T00:08:15.619333+00:00'
exported_at: '2026-10-15T00:08:16.802351+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns
structured_data:
  about: []
  author: ''
  description: Anthropic’s red team says AI worms built on small models may soon be
    able to spread across poorly secured IoT devices.
  headline: Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns
updated_at: '2026-10-15T00:08:15.619333+00:00'
url_hash: d9fddc7b2a461483552ea2ddd5f94df3662ee41d
---

### [Artificial Intelligence](https://www.securityweek.com/category/artificial-intelligence/)

# Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns

Experiments show cheap TV boxes can run capable AI models, and small models may soon be able to spread across such devices on their own.

![](https://www.securityweek.com/wp-content/uploads/2023/11/Ed-Kovacs.jpg)

By

[Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

|


October 13, 2026 (7:58 AM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)
  [+ Whatsapp](whatsapp://send?text=Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)
  [+ Email](/cdn-cgi/l/email-protection#caf5b9bfa8a0afa9bef799a7aba6a6ea8b83ea87a5aeafa6b9ea89a5bfa6aeea99a5a5a4ea99afa6ace798afbaa6a3a9abbeafeaa5a4ea83a59eea8eafbca3a9afb9e6ea8ba4bea2b8a5baa3a9ea9dabb8a4b9ecaba7baf188858e93f783eaaca5bfa4aeeabea2a3b9eaabb8bea3a9a6afeaa3a4beafb8afb9bea3a4adeaaba4aeeabea2a5bfada2beeaa5aceab9a2abb8a3a4adeaa3beeabda3bea2eab3a5bfe4ea89a2afa9a1eaa3beeaa5bfbef0eaa2bebebab9f0e5e5bdbdbde4b9afa9bfb8a3beb3bdafafa1e4a9a5a7e5b9a7aba6a6e7aba3e7a7a5aeafa6b9e7a7abb3e7b9a5a5a4e7a8afe7aba8a6afe7bea5e7b9afa6ace7b8afbaa6a3a9abbeafe7a5a4e7a3a5bee7aeafbca3a9afb9e7aba4bea2b8a5baa3a9e7bdabb8a4b9e5)

![Botnet](https://www.securityweek.com/wp-content/uploads/2025/12/botnet.jpeg)

**Small AI models may be only months away from being able to self-replicate across commercial IoT devices, without needing a data center, according to research from Anthropic’s Frontier Red Team.**

The study looks at AI worms that run their own model directly on the devices they compromise. Such malware would be hard to shut down because it has no central point to switch off, though it would likely spread slowly.

The researchers bought 15 off-brand Android-based TV boxes for about $55 each. A 26-billion-parameter open-weight model split across them ran at 0.39 tokens per second.

Rather than exploitation, which prior studies have
[already examined](https://www.securityweek.com/widened-scan-turns-up-fourth-rogue-claude-cyber-incident/)
, the team focused on whether models could get AI inference running on unfamiliar hardware. A 9-billion-parameter model did so on eight of the nine hardware types tested.

The researchers then tested the full replication cycle on a closed network of eight emulated Android devices, with the hacking step deliberately kept trivial. Of the open-weight models tested, only GLM-5.2 completed it, reaching all eight devices in four of five runs.

[Anthropic](https://www.securityweek.com/topics/anthropic/)
considers the results an upper bound for real-world success, but notes that past IoT botnets such as Mirai spread simply by trying default manufacturer credentials.

Advertisement. Scroll to continue reading.

Models with 30 billion parameters or fewer can already complete many of the individual steps but make mistakes when chaining them together. If they keep improving at their historical rate, Anthropic expects them to reach GLM-5.2’s level by the end of 2026.

“Small weight-based replicators may be possible soon after,” the company
[says](https://www.anthropic.com/research/self-replicating-ai)
.

Anthropic also looked at a botnet as large as
[Kimwolf](https://www.securityweek.com/aisuru-and-kimwolf-ddos-botnets-disrupted-in-international-operation/)
, which infected more than two million devices. If every 15 TV boxes ran one copy of the 26-billion-parameter model, such a botnet would host roughly 133,000 copies. Their combined compute would be worth at most about 40 Nvidia H100 GPUs, and each replication would take more than a day.

**[ Read:**
[AI Turns Familiar Cyberattacks Into a Race Against Time](https://www.securityweek.com/ai-turns-familiar-cyberattacks-into-a-race-against-time/)
**]**

Unlike traditional botnets built for specific devices, an AI worm could work out unfamiliar hardware on its own, Anthropic says. Defenders, however, still have some advantages.

Large model transfers and sustained traffic between devices that don’t normally communicate would stand out in ISP monitoring. In addition, moving manufacturers to more secure defaults, such as eliminating default passwords, would also shrink the target pool.

There is no full rogue replicator yet, Anthropic says, but models are getting better at each step in the chain and at passing what they learn on to their copies.

**Related**
:
[OpenAI Fires 3 Safety Researchers in Dispute Over AI Risks](https://www.securityweek.com/openai-fires-3-safety-researchers-in-dispute-over-ai-risks/)

**Related**
:
[Anthropic Fast-Tracks AI Bug Reports to OSS Maintainers, Taps 11 Firms for OT Security](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/)

**Related**
:
[Formula Predicts When AI Chatbots Are at Risk of Turning Bad](https://www.securityweek.com/formula-predicts-when-ai-chatbots-are-at-risk-of-turning-bad/)

![](https://www.securityweek.com/wp-content/uploads/2023/11/Ed-Kovacs.jpg)

Written By

[Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering.

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.

## More from [Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

* [Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day](https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/)
* [Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN](https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)
* [Adobe Patches 176 Vulnerabilities Across 11 Products](https://www.securityweek.com/adobe-patches-140-vulnerabilities-across-10-products/)
* [Google Partially Reverses Chrome Bug Bounty Cuts](https://www.securityweek.com/google-partially-reverses-chrome-bug-bounty-cuts/)
* [Meta Says Hackers Took Code, Personal Data of 1,500 in GitHub Breach](https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/)
* [Bricksforge WordPress Plugin Vulnerability Exploited in the Wild](https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/)
* [Canonical Websites Disrupted in Second DDoS Attack This Year](https://www.securityweek.com/canonical-websites-disrupted-in-second-ddos-attack-this-year/)
* [Ransomware Response Expert Arrested in ShinyHunters FBI Hack Probe](https://www.securityweek.com/ransomware-response-expert-arrested-in-shinyhunters-fbi-hack-probe/)

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
  [+ Whatsapp](https://web.whatsapp.com/send?text=Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)
  [+ Whatsapp](whatsapp://send?text=Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)
  [+ Email](/cdn-cgi/l/email-protection#5a65292f38303f392e6709373b36367a1b137a17353e3f36297a19352f363e7a093535347a093f363c77083f2a3633393b2e3f7a35347a13350e7a1e3f2c33393f29767a1b342e3228352a33397a0d3b2834297c3b372a6118151e0367137a3c352f343e7a2e3233297a3b282e3339363f7a33342e3f283f292e33343d7a3b343e7a2e32352f3d322e7a353c7a29323b2833343d7a332e7a2d332e327a23352f747a19323f39317a332e7a352f2e607a322e2e2a296075752d2d2d74293f392f28332e232d3f3f31743935377529373b3636773b337737353e3f362977373b23772935353477383f773b38363f772e3577293f363c77283f2a3633393b2e3f7735347733352e773e3f2c33393f29773b342e3228352a3339772d3b28342975)



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