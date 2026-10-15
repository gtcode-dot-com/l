---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T00:08:12.301770+00:00'
exported_at: '2026-10-15T00:08:16.842783+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn
structured_data:
  about: []
  author: ''
  description: Ivanti has patched CVE-2026-104935, a Connect Secure (ICS) zero-day
    exploit that allows unauthenticated remote code execution.
  headline: Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN
updated_at: '2026-10-15T00:08:12.301770+00:00'
url_hash: 831b9777c044b6da75b6abb2d7fb57ab82362de0
---

### [Vulnerabilities](https://www.securityweek.com/category/vulnerabilities/)

# Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN

CVE-2026-104935 affects Ivanti Connect Secure and it can be exploited for unauthenticated remote code execution with elevated privileges.

![](https://www.securityweek.com/wp-content/uploads/2023/11/Ed-Kovacs.jpg)

By

[Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

|


October 13, 2026 (2:43 PM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)
  [+ Whatsapp](whatsapp://send?text=Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)
  [+ Email](/cdn-cgi/l/email-protection#d1eea2a4b3bbb4b2a5ec98a7b0bfa5b8f18bb4a3befc95b0a8f192b9b0b8bff196b0a7b4f190a5a5b0b2bab4a3a2f183bebea5f190b2b2b4a2a2f1a5bef197a4bdbda8f181b0a5b2b9b4b5f187819ff7b0bca1ea939e9588ec98f1b7bea4bfb5f1a5b9b8a2f1b0a3a5b8b2bdb4f1b8bfa5b4a3b4a2a5b8bfb6f1b0bfb5f1a5b9bea4b6b9a5f1beb7f1a2b9b0a3b8bfb6f1b8a5f1a6b8a5b9f1a8bea4fff192b9b4b2baf1b8a5f1bea4a5ebf1b9a5a5a1a2ebfefea6a6a6ffa2b4b2a4a3b8a5a8a6b4b4baffb2bebcfeb8a7b0bfa5b8fcabb4a3befcb5b0a8fcb2b9b0b8bffcb6b0a7b4fcb0a5a5b0b2bab4a3a2fca3bebea5fcb0b2b2b4a2a2fca5befcb7a4bdbda8fca1b0a5b2b9b4b5fca7a1bffe)

![Ivanti vulnerability exploited](https://www.securityweek.com/wp-content/uploads/2024/02/Ivanti-Risks-Exploits.jpg)

**Ivanti on Tuesday warned customers that a zero-day vulnerability in its Connect Secure (ICS) VPN appliances has been exploited in the wild.**

Tracked as
[CVE-2026-104935](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US)
and rated high severity, the issue is an authentication bypass that lets a remote, unauthenticated attacker execute arbitrary commands. Ivanti says it’s aware of exploitation affecting a limited number of customers.

Volexity discovered the in-the-wild exploitation while investigating an incident at one of its customers. A previously undocumented threat actor it tracks as UTA0576 had chained three zero-days to gain unauthenticated, root-level code execution on a fully patched ICS appliance.

According to Volexity, CVE-2026-104935 covers two of the flaws: an authentication bypass and a remote code execution bug. Ivanti has patched these vulnerabilities with the release of ICS versions 22.8R2.5, 25.1.1.2, 25.1.3.0, and 25.1.3.1.

The third vulnerability, a privilege escalation issue, remains unpatched, and the vendor plans to fix it over the coming weeks.

Volexity, which found evidence of exploitation starting on October 3, says UTA0576 focused primarily on credential theft, data exfiltration, network reconnaissance, and log tampering.

Advertisement. Scroll to continue reading.

The attackers stole domain credentials stored on the appliance and exfiltrated limited Active Directory metadata. Using a custom tool, they searched Active Directory for LAPS passwords and BitLocker recovery keys.

They also ran password-spraying attacks, tested credentials with a custom Kerberos tool, and tried to extract credentials from captured network traffic. They also scanned the network, collected the appliance’s configuration data, and parsed authentication logs to identify valid usernames. Volexity found no backdoor or web shell on the device.

The operation was detected and disrupted before the attackers’ ultimate goals became clear. Volexity believes with high confidence that their actions pointed to preparation for lateral movement and a wider compromise of the network.

“Volexity assesses with low confidence that UTA0576 has criminal, rather than espionage, motivations based on the target of this activity,” the company
[says](https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/)
.

“As with many other threat actor operations Volexity has investigated in 2026, Volexity assesses with medium confidence that UTA0576 makes use of large language models (LLMs) for exploit development and post-exploitation activity,” it added.

**Related**
:
[Critical SonicWall Vulnerability Exploited Days After Disclosure](https://www.securityweek.com/critical-sonicwall-vulnerability-exploited-days-after-disclosure/)

**Related**
:
[Unpatched AhsayCBS Vulnerabilities Exploited in the Wild](https://www.securityweek.com/unpatched-ahsaycbs-vulnerabilities-exploited-in-the-wild/)

**Related**
:
[Citrix Urges Immediate Patching of Critical NetScaler Vulnerability](https://www.securityweek.com/citrix-urges-immediate-patching-of-critical-netscaler-vulnerability/)

![](https://www.securityweek.com/wp-content/uploads/2023/11/Ed-Kovacs.jpg)

Written By

[Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

Eduard Kovacs (@EduardKovacs) is senior managing editor at SecurityWeek. He worked as a high school IT teacher before starting a career in journalism in 2011. Eduard holds a bachelor’s degree in industrial informatics and a master’s degree in computer techniques applied in electrical engineering.

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.

## More from [Eduard Kovacs](https://www.securityweek.com/contributors/eduard-kovacs/)

* [Microsoft Patches Record 1,413 Vulnerabilities, Including Exploited Windows Zero-Day](https://www.securityweek.com/microsoft-patches-record-1413-vulnerabilities-including-exploited-windows-zero-day/)
* [Adobe Patches 176 Vulnerabilities Across 11 Products](https://www.securityweek.com/adobe-patches-140-vulnerabilities-across-10-products/)
* [Google Partially Reverses Chrome Bug Bounty Cuts](https://www.securityweek.com/google-partially-reverses-chrome-bug-bounty-cuts/)
* [Meta Says Hackers Took Code, Personal Data of 1,500 in GitHub Breach](https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/)
* [Small AI Models Could Soon Self-Replicate on IoT Devices, Anthropic Warns](https://www.securityweek.com/small-ai-models-may-soon-be-able-to-self-replicate-on-iot-devices-anthropic-warns/)
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
  [+ Whatsapp](https://web.whatsapp.com/send?text=Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)
  [+ Whatsapp](whatsapp://send?text=Ivanti Zero-Day Chain Gave Attackers Root Access to Fully Patched VPN https://www.securityweek.com/ivanti-zero-day-chain-gave-attackers-root-access-to-fully-patched-vpn/)
  [+ Email](/cdn-cgi/l/email-protection#86b9f5f3e4ece3e5f2bbcff0e7e8f2efa6dce3f4e9abc2e7ffa6c5eee7efe8a6c1e7f0e3a6c7f2f2e7e5ede3f4f5a6d4e9e9f2a6c7e5e5e3f5f5a6f2e9a6c0f3eaeaffa6d6e7f2e5eee3e2a6d0d6c8a0e7ebf6bdc4c9c2dfbbcfa6e0e9f3e8e2a6f2eeeff5a6e7f4f2efe5eae3a6efe8f2e3f4e3f5f2efe8e1a6e7e8e2a6f2eee9f3e1eef2a6e9e0a6f5eee7f4efe8e1a6eff2a6f1eff2eea6ffe9f3a8a6c5eee3e5eda6eff2a6e9f3f2bca6eef2f2f6f5bca9a9f1f1f1a8f5e3e5f3f4eff2fff1e3e3eda8e5e9eba9eff0e7e8f2efabfce3f4e9abe2e7ffabe5eee7efe8abe1e7f0e3abe7f2f2e7e5ede3f4f5abf4e9e9f2abe7e5e5e3f5f5abf2e9abe0f3eaeaffabf6e7f2e5eee3e2abf0f6e8a9)



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