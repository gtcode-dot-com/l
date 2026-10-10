---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-10T20:20:47.723198+00:00'
exported_at: '2026-10-10T20:20:50.639927+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools
structured_data:
  about: []
  author: ''
  description: The US has seized MicroScan and FishHub, tools used by Flax Typhoon
    and other Chinese APTs in critical infrastructure intrusions.
  headline: US Disrupts Chinese State-Sponsored Hacking Tools
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools
  publisher:
    logo: /favicon.ico
    name: GTCode
title: US Disrupts Chinese State-Sponsored Hacking Tools
updated_at: '2026-10-10T20:20:47.723198+00:00'
url_hash: cbefaa94bc091355765764763150c97ff8363dfb
---

### [Government](https://www.securityweek.com/category/government-cybersecurity/)

# US Disrupts Chinese State-Sponsored Hacking Tools

Flax Typhoon and other APTs used MicroScan and FishHub to scan and hack US and foreign critical infrastructure.

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

|


October 9, 2026 (4:36 AM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=US Disrupts Chinese State-Sponsored Hacking Tools https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
  [+ Whatsapp](whatsapp://send?text=US Disrupts Chinese State-Sponsored Hacking Tools https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
  [+ Email](/cdn-cgi/l/email-protection#0c337f796e66696f7831595f2c48657f7e797c787f2c4f646562697f692c5f786d7869215f7c63627f637e69682c446d6f6765626b2c586363607f2a6d617c374e43485531452c6a637962682c7864657f2c6d7e78656f60692c656278697e697f7865626b2c6d62682c786463796b64782c636a2c7f646d7e65626b2c65782c7b6578642c756379222c4f64696f672c65782c637978362c6478787c7f3623237b7b7b227f696f797e6578757b696967226f636123797f2168657f7e797c787f216f646562697f69217f786d7869217f7c63627f637e696821646d6f6765626b21786363607f23)

![Chinese hacking tools disrupted by US](https://www.securityweek.com/wp-content/uploads/2026/10/Flax-Typhoon-disrupted.jpg)

**The United States on Thursday announced the disruption of two hacking tools used by Chinese state-sponsored threat actors in attacks against US and foreign critical infrastructure.**

Built by Integrity Technology Group (Integrity Tech), MicroScan has been used for vulnerability scanning, while FishHub has enabled network intrusions via spear phishing.

Integrity Tech, the US says, used a Mirai malware variant to build an IoT botnet that facilitated MicroScan’s use for reconnaissance against victims’ networks, including a US power company, NGOs, Japanese and Polish airports, and Taiwanese critical infrastructure entities and universities.

FishHub enabled Integrity Tech’s clients to access victim networks remotely, search for specific files, and exfiltrate them. The tool has been used in attacks against at least 20 universities in Taiwan.

The US seized the domains the threat actors were using to access MicroScan and FishHub, including c0cc[.]cc, 98aicai[.]com, 98aicode[.]com, outlook3650[.]com, youtubecard[.]com, and linkedinns[.]net.

In 2024, the US disrupted Integrity Tech’s
[Raptor Train botnet](https://www.securityweek.com/us-disrupts-raptor-train-botnet-of-chinese-apt-flax-typhoon/)
, and in 2025
[sanctioned it](https://www.securityweek.com/us-sanctions-chinese-firm-linked-to-flax-typhoon-attacks-on-critical-infrastructure/)
for providing cybersecurity products to Chinese state-sponsored APTs such as Flax Typhoon. The European Union
[sanctioned the company](https://www.securityweek.com/eu-sanctions-chinese-iranian-firms-supporting-hacking-operations/)
in March 2026.

Advertisement. Scroll to continue reading.

A new
[joint advisory](https://www.ic3.gov/CSA/2026/261008.pdf)
(PDF) from government agencies in the US, UK, Australia, Canada, Japan, New Zealand, and Spain shows that MicroScan has been active since at least 2017, targeting Apache Struts, Juniper ScreenOS, Jenkins, OpenSSL, Oracle, Rejetto HFS, WebLogic Server, WordPress, and other services.

“This Python-based web application contains over 1,300 penetration testing scripts written to scan websites for specific vulnerabilities,” the advisory reads.

The tool was mainly associated with Flax Typhoon (also known as Ethereal Panda, Red Juliett, Storm-0919, and UNC5007) activity, but Integrity Tech is believed to have been working with other Chinese APTs as well.

Flax Typhoon was also seen using BBScan, dirsearch, Fscan, ksubdomain, masscan, Nmap, OneForAll, ShuiZe, and WPScan for reconnaissance, and command-line exploit utilities and the EBurst Microsoft Exchange password spraying tool for initial access.

The threat actors deployed VPN tools such as SoftEther for persistence and downloaded databases or manually extracted data from victims’ email addresses. They also used the PHP script Curlc4.txt and command-line utility office-cli for email exfiltration, and DC.ex to extract sensitive data from Active Directory.

“The threat actors collect account credentials and exfiltrate victim email data from on-premises systems and cloud-based services. Observed victims of email data theft included government organizations, law enforcement agencies, healthcare systems, and religious institutions located in Southeast Asia. In some instances, the threat actors restricted access to the exfiltrated data to only IP addresses from Xiamen, China,” the advisory reads.

**Related:**
[US Seeks Alleged Chinese Hafnium Hacker With $10 Million Reward](https://www.securityweek.com/us-seeks-alleged-chinese-hafnium-hacker-with-10-million-reward/)

**Related:**
[Recent ZyXEL Switch Vulnerability Exploited by Chinese Hackers](https://www.securityweek.com/recent-zyxel-switch-vulnerability-exploited-by-chinese-hackers/)

**Related:**
[Chinese Hackers Exploit Critical Tencent Software Flaw for One-Click Code Execution](https://www.securityweek.com/chinese-hackers-exploit-critical-tencent-software-flaw-for-one-click-code-execution/)

**Related:**
[US Disrupts Chinese Hacking Platform Used in Military and Critical Infrastructure Attacks](https://www.securityweek.com/us-disrupts-chinese-hacking-platform-used-in-military-and-critical-infrastructure-attacks/)

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

Written By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

Ionut Arghire is an international correspondent for SecurityWeek.

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.

## More from [Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

* [Cisco Patches a Dozen Critical Vulnerabilities](https://www.securityweek.com/cisco-patches-a-dozen-critical-vulnerabilities/)
* [SonicWall and Splunk Patch Critical Vulnerabilities](https://www.securityweek.com/sonicwall-and-splunk-patch-critical-vulnerabilities/)
* [Rein Security Raises $25 Million to Guard AI Agents at Runtime](https://www.securityweek.com/rein-security-raises-25-million-to-guard-ai-agents-at-runtime/)
* [Fake Decryption Tools Masked $11M Markup in Ransomware Recovery Scheme](https://www.securityweek.com/fake-decryption-tools-masked-11m-markup-in-ransomware-recovery-scheme/)
* [FortiBleed Attackers Locking Victims Out of Fortinet Devices](https://www.securityweek.com/fortibleed-attackers-locking-victims-out-of-fortinet-devices/)
* [Qilin Ransomware Suspect Arrested in Japan, Extradited to Germany](https://www.securityweek.com/qilin-ransomware-suspect-arrested-in-japan-extradited-to-germany/)
* [Chrome 155 Update Patches 247 Vulnerabilities](https://www.securityweek.com/chrome-155-update-patches-247-vulnerabilities/)
* [ASOS Confirms Cyberattack, Data Breach](https://www.securityweek.com/asos-confirms-cyberattack-data-breach/)

## Latest News

* [Insider Cyber Extortion Plot Against Industrial Firm Lands Engineer in Prison](https://www.securityweek.com/insider-cyber-extortion-plot-against-industrial-firm-lands-engineer-in-prison/)
* [OpenAI Fires 3 Safety Researchers in Dispute Over AI Risks](https://www.securityweek.com/openai-fires-3-safety-researchers-in-dispute-over-ai-risks/)
* [In Other News: AI Used in Korean Bank Breaches, Poem-Guided Botnet, Empire Admin Gets 40 Years](https://www.securityweek.com/in-other-news-ai-used-in-korean-bank-breaches-poem-guided-botnet-empire-admin-gets-40-years/)
* [Google Domains Impacted by Recent ccTLD Hijacks](https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
* [Unpatched AhsayCBS Vulnerabilities Exploited in the Wild](https://www.securityweek.com/unpatched-ahsaycbs-vulnerabilities-exploited-in-the-wild/)
* [Pre-Baked Firmware Malware Hits Budget Android Devices in 150+ Countries](https://www.securityweek.com/pre-baked-firmware-malware-hits-budget-android-devices-in-150-countries/)
* [Anthropic Fast-Tracks AI Bug Reports to OSS Maintainers, Taps 11 Firms for OT Security](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/)
* [Citrix Urges Immediate Patching of Critical NetScaler Vulnerability](https://www.securityweek.com/citrix-urges-immediate-patching-of-critical-netscaler-vulnerability/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark.png)

#### Trending

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing to stay informed on the latest threats, trends, and technology, along with insightful columns from industry experts.

[## Webinar: AI Is Accelerating Risk. Can Your IT Operations Keep Up?](https://event.on24.com/wcc/r/5514549/02C48E5F6F13A20EA4A5702D2392FD21?partnerref=awidget)

October 14, 2026

Learn about Frontier Pace Governance: a practical approach to helping IT operations move at AI speed without sacrificing security, accountability, or operational discipline.

[Register](https://event.on24.com/wcc/r/5514549/02C48E5F6F13A20EA4A5702D2392FD21?partnerref=awidget)

[## Virtual Event: Zero Trust &amp; Identity Strategies Summit 2026](https://register.securityweek.com/zero-trust-summit)

October 14, 2026

Join as we decipher the world of zero trust and share war stories on securing an organization by eliminating implicit trust and continuously validating every stage of a digital interaction.

[Register](https://register.securityweek.com/zero-trust-summit)

#### People on the Move

Rapid7 has named Rik Ferguson as VP of Security Intelligence.

Cytactic has appointed Tim Brown as CSO.

Scott Simkin has joined Vega as CMO.

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
  [+ Whatsapp](https://web.whatsapp.com/send?text=US Disrupts Chinese State-Sponsored Hacking Tools https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
  [+ Whatsapp](whatsapp://send?text=US Disrupts Chinese State-Sponsored Hacking Tools https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
  [+ Email](/cdn-cgi/l/email-protection#9ba4e8eef9f1fef8efa6cec8bbdff2e8e9eeebefe8bbd8f3f2f5fee8febbc8effaeffeb6c8ebf4f5e8f4e9feffbbd3faf8f0f2f5fcbbcff4f4f7e8bdfaf6eba0d9d4dfc2a6d2bbfdf4eef5ffbbeff3f2e8bbfae9eff2f8f7febbf2f5effee9fee8eff2f5fcbbfaf5ffbbeff3f4eefcf3efbbf4fdbbe8f3fae9f2f5fcbbf2efbbecf2eff3bbe2f4eeb5bbd8f3fef8f0bbf2efbbf4eeefa1bbf3efefebe8a1b4b4ecececb5e8fef8eee9f2efe2ecfefef0b5f8f4f6b4eee8b6fff2e8e9eeebefe8b6f8f3f2f5fee8feb6e8effaeffeb6e8ebf4f5e8f4e9feffb6f3faf8f0f2f5fcb6eff4f4f7e8b4)



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