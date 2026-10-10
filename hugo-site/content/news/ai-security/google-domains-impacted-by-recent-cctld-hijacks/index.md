---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-10T20:20:43.662137+00:00'
exported_at: '2026-10-10T20:20:50.651658+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks
structured_data:
  about: []
  author: ''
  description: Google says threat actors hijacked the .gh, .sl, and .as ccTLDs and
    obtained HTTPS certificates for several of its domains.
  headline: Google Domains Impacted by Recent ccTLD Hijacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Domains Impacted by Recent ccTLD Hijacks
updated_at: '2026-10-10T20:20:43.662137+00:00'
url_hash: 10536d791f018466542e1e2d37749b2dc603174a
---

### [Cybercrime](https://www.securityweek.com/category/cybercrime/)

# Google Domains Impacted by Recent ccTLD Hijacks

Hackers hijacked the .gh, .sl, and .as ccTLDs and obtained HTTPS certificates for several Google domains.

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

|


October 9, 2026 (7:43 AM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=Google Domains Impacted by Recent ccTLD Hijacks https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
  [+ Whatsapp](whatsapp://send?text=Google Domains Impacted by Recent ccTLD Hijacks https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
  [+ Email](/cdn-cgi/l/email-protection#d4eba7a1b6beb1b7a0e993bbbbb3b8b1f490bbb9b5bdbaa7f49db9a4b5b7a0b1b0f4b6adf486b1b7b1baa0f4b7b7809890f49cbdbeb5b7bfa7f2b5b9a4ef969b908de99df4b2bba1bab0f4a0bcbda7f4b5a6a0bdb7b8b1f4bdbaa0b1a6b1a7a0bdbab3f4b5bab0f4a0bcbba1b3bca0f4bbb2f4a7bcb5a6bdbab3f4bda0f4a3bda0bcf4adbba1faf497bcb1b7bff4bda0f4bba1a0eef4bca0a0a4a7eefbfba3a3a3faa7b1b7a1a6bda0ada3b1b1bffab7bbb9fbb3bbbbb3b8b1f9b0bbb9b5bdbaa7f9bdb9a4b5b7a0b1b0f9b6adf9a6b1b7b1baa0f9b7b7a0b8b0f9b0bbb9b5bdbaf9bcbdbeb5b7bfa7fb)

![DNS domain hijack](https://www.securityweek.com/wp-content/uploads/2026/05/Underminr-DNS-vulnerability.jpg)

**Google has disclosed that several of its domains were affected by a recent hijack of third-party country-code top-level domains (ccTLDs).**

The incident occurred last week and targeted the .gh (Ghana), .sl (Sierra Leone), and .as (American Samoa) ccTLDs, putting all domains with those suffixes at risk.

“During these hijacks, attackers modified authoritative DNS records and obtained unauthorized HTTPS certificates covering several Google domains, as well as domains belonging to other organizations,” the internet giant
[says](https://blog.google/security/chromes-response-to-recent-cctld-registry-hijacks/)
.

According to Google, the Certification Authorities (CAs) that issued the certificates are not to be blamed, given the nature of the attacks.

Immediately after learning of the incident, Google blocked the unauthorized certificates for its domains in Chrome and worked with the issuing CAs to revoke them.

Analysis of Certificate Transparency (CT) log data revealed that multiple other organizations, including global brands and popular online services, have been affected.

Advertisement. Scroll to continue reading.

“To ensure users of those sites were kept safe as soon as possible, we proactively blocked these certificates in Chrome. Where possible, we reached out to impacted organizations to alert them to our findings and actions,” Google says.

The internet giant notes that, while it took steps to identify and block the unauthorized certificates, certain domains might still be affected.

Google encourages domain owners to monitor CT logs for all their domains, especially for those in .gh, .sl, or .as, and to publish restrictive CAA DNS records to ensure safeguards after DNS control has been restored.

“Because CAs are permitted to cache and reuse completed domain control validation (DCV) checks for subsequent issuance, restoring a restrictive CAA policy, especially one that restricts issuance to specific authorized accounts and validation methods, prevents an attacker from using cached validation state to mint new certificates after a hijack ends,” Google notes.

**Related:**
[Chrome 155 Update Patches 247 Vulnerabilities](https://www.securityweek.com/chrome-155-update-patches-247-vulnerabilities/)

**Related:**
[Zero Trust Creator Says Model Holds Firm Against AI-Assisted Attacks](https://www.securityweek.com/zero-trust-creator-says-model-holds-firm-against-ai-assisted-attacks/)

**Related:**
[Anthropic Fast-Tracks AI Bug Reports to OSS Maintainers, Taps 11 Firms for OT Security](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/)

**Related:**
[Long-Running NPM Malware Campaign Accumulates 40,000 Downloads](https://www.securityweek.com/long-running-npm-malware-campaign-accumulates-40000-downloads/)

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

* [OpenAI Fires 3 Safety Researchers in Dispute Over AI Risks](https://www.securityweek.com/openai-fires-3-safety-researchers-in-dispute-over-ai-risks/)
* [In Other News: AI Used in Korean Bank Breaches, Poem-Guided Botnet, Empire Admin Gets 40 Years](https://www.securityweek.com/in-other-news-ai-used-in-korean-bank-breaches-poem-guided-botnet-empire-admin-gets-40-years/)
* [Unpatched AhsayCBS Vulnerabilities Exploited in the Wild](https://www.securityweek.com/unpatched-ahsaycbs-vulnerabilities-exploited-in-the-wild/)
* [Pre-Baked Firmware Malware Hits Budget Android Devices in 150+ Countries](https://www.securityweek.com/pre-baked-firmware-malware-hits-budget-android-devices-in-150-countries/)
* [US Disrupts Chinese State-Sponsored Hacking Tools](https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
* [Anthropic Fast-Tracks AI Bug Reports to OSS Maintainers, Taps 11 Firms for OT Security](https://www.securityweek.com/anthropic-fast-tracks-ai-bug-reports-to-oss-maintainers-taps-11-firms-for-ot-security/)
* [Citrix Urges Immediate Patching of Critical NetScaler Vulnerability](https://www.securityweek.com/citrix-urges-immediate-patching-of-critical-netscaler-vulnerability/)
* [Google Pixel 10 Exploits Earned Hackers $560,000 at Pwn2Own](https://www.securityweek.com/google-pixel-10-exploits-earned-hackers-560000-at-pwn2own/)

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
  [+ Whatsapp](https://web.whatsapp.com/send?text=Google Domains Impacted by Recent ccTLD Hijacks https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
  [+ Whatsapp](whatsapp://send?text=Google Domains Impacted by Recent ccTLD Hijacks https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
  [+ Email](/cdn-cgi/l/email-protection#f2cd81879098979186cfb59d9d959e97d2b69d9f939b9c81d2bb9f829391869796d2908bd2a09791979c86d29191a6beb6d2ba9b9893919981d4939f82c9b0bdb6abcfbbd2949d879c96d2869a9b81d29380869b919e97d29b9c8697809781869b9c95d2939c96d2869a9d87959a86d29d94d2819a93809b9c95d29b86d2859b869ad28b9d87dcd2b19a979199d29b86d29d8786c8d29a86868281c8dddd858585dc81979187809b868b85979799dc919d9fdd959d9d959e97df969d9f939b9c81df9b9f829391869796df908bdf809791979c86df9191869e96df969d9f939b9cdf9a9b9893919981dd)



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