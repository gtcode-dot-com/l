---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-13T04:39:48.198644+00:00'
exported_at: '2026-10-13T04:39:49.496723+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch
structured_data:
  about: []
  author: ''
  description: Starting February 2027, Let’s Encrypt will move to 64-day certificate
    lifetimes by default, ahead of 45-day lifetimes in 2028.
  headline: Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day
    Switch
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day
  Switch
updated_at: '2026-10-13T04:39:48.198644+00:00'
url_hash: 8a123394a7319723b1d5a98f346d73f43ba7ce33
---

### [Data Protection](https://www.securityweek.com/category/data-protection/)

# Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch

Beginning February 2027, all newly issued certificates will have a 64-day validity period by default.

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

|


October 12, 2026 (3:53 AM ET)

* [+ Flipboard](# "Share on Flipboard")
  [+ Reddit](# "Share on Reddit")
  [+ Whatsapp](https://web.whatsapp.com/send?text=Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch/)
  [+ Whatsapp](whatsapp://send?text=Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch/)
  [+ Email](/cdn-cgi/l/email-protection#4d723e382f27282e3970012839afcdd43e6d08232e3f343d396d0e38393e6d09282b2c3821396d0e283f39242b242e2c39286d1b2c2124292439346d39226d7b796d092c343e6d0c25282c296d222b6d797860092c346d1e3a24392e256b2c203d760f02091470046d2b223823296d3925243e6d2c3f39242e21286d242339283f283e3924232a6d2c23296d392522382a25396d222b6d3e252c3f24232a6d24396d3a2439256d342238636d0e25282e266d24396d223839776d2539393d3e7762623a3a3a633e282e383f2439343a282826632e2220622128393e6028232e3f343d39602e38393e6029282b2c382139602e283f39242b242e2c3928603b2c212429243934603922607b7960292c343e602c25282c2960222b60797860292c34603e3a24392e2562)

![TLS certificate lifespan](https://www.securityweek.com/wp-content/uploads/2024/09/internet-routing-bgp.jpeg)

**Open Certificate Authority (CA) Let’s Encrypt is taking the first step towards reducing the validity period of the certificates it issues.**

Beginning February 10, 2027, it will issue certificates with 64-day lifetimes by default, in preparation for 45-day lifetimes planned for 2028.

In line with the CA/Browser Forum Baseline Requirements, the shorter certificate validity period is expected to improve security on the web by making revocation more efficient and limiting the scope of compromise.

All publicly trusted CAs will make similar changes, Let’s Encrypt
[noted](https://letsencrypt.org/2025/12/02/from-90-to-45)
in a December 2025 blog, when it revealed the planned timeline for switching to 45-day certificates.

Last week, the CA
[announced](https://letsencrypt.org/2026/10/07/64-day-certs.html)
that, after February 10, 2027, all newly issued or renewed certificates will have a 64-day validity period, with the last 90-day certificate expected to expire on May 11, 2027.

This week, Let’s Encrypt will start issuing 64-day certificates in its staging environment for testing purposes, and recommends that all customers perform similar tests before the change enters production.

Advertisement. Scroll to continue reading.

“If your renewals are automated and your client supports ACME Renewal Info (ARI), you should be all set since ARI allows Let’s Encrypt to tell your client when to renew (you can review your ACME client’s documentation to determine if ARI is implemented),” Let’s Encrypt notes.

For certificates with renewals hardcoded to a specific date from expiration, the CA recommends setting the date to approximately two-thirds of the certificate lifetime.

Let’s Encrypt will also reduce the authorization reuse period to 10 days next year, and further reduce it to seven hours in 2028.

“We are making this change to comply with a 2029 reduction in maximum validation reuse periods, and to remove the need for ‘CAA rechecking’, where we have to repeat part of the validation process if the validation data is more than 7 hours old,” it explains.

According to Let’s Encrypt, the change will not affect ACME endpoints, its issuance chains, or rate limits.

**Related:**
[Google Domains Impacted by Recent ccTLD Hijacks](https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)

**Related:**
[DigiCert Revokes Certificates After Support Portal Hack](https://www.securityweek.com/digicert-revokes-certificates-after-support-portal-hack/)

**Related:**
[Google Working Towards Quantum-Safe Chrome HTTPS Certificates](https://www.securityweek.com/google-working-towards-quantum-safe-chrome-https-certificates/)

**Related:**
[Zero Trust Creator Says Model Holds Firm Against AI-Assisted Attacks](https://www.securityweek.com/zero-trust-creator-says-model-holds-firm-against-ai-assisted-attacks/)

![](https://www.securityweek.com/wp-content/uploads/2023/10/Iounut-SecurityWeek.jpg)

Written By

[Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

Ionut Arghire is an international correspondent for SecurityWeek.

## Daily Briefing Newsletter

Subscribe to the SecurityWeek Email Briefing for the latest cybersecurity threats, trends, and expert
insights.

## More from [Ionut Arghire](https://www.securityweek.com/contributors/ionut-arghire/)

* [Google Domains Impacted by Recent ccTLD Hijacks](https://www.securityweek.com/google-domains-impacted-by-recent-cctld-domain-hijacks/)
* [Unpatched AhsayCBS Vulnerabilities Exploited in the Wild](https://www.securityweek.com/unpatched-ahsaycbs-vulnerabilities-exploited-in-the-wild/)
* [US Disrupts Chinese State-Sponsored Hacking Tools](https://www.securityweek.com/us-disrupts-chinese-state-sponsored-hacking-tools/)
* [Citrix Urges Immediate Patching of Critical NetScaler Vulnerability](https://www.securityweek.com/citrix-urges-immediate-patching-of-critical-netscaler-vulnerability/)
* [Cisco Patches a Dozen Critical Vulnerabilities](https://www.securityweek.com/cisco-patches-a-dozen-critical-vulnerabilities/)
* [SonicWall and Splunk Patch Critical Vulnerabilities](https://www.securityweek.com/sonicwall-and-splunk-patch-critical-vulnerabilities/)
* [Rein Security Raises $25 Million to Guard AI Agents at Runtime](https://www.securityweek.com/rein-security-raises-25-million-to-guard-ai-agents-at-runtime/)
* [Fake Decryption Tools Masked $11M Markup in Ransomware Recovery Scheme](https://www.securityweek.com/fake-decryption-tools-masked-11m-markup-in-ransomware-recovery-scheme/)

## Latest News

* [IonQ to Acquire Zero Trust Firm Elisity for Up to $1.3 Billion](https://www.securityweek.com/ionq-to-acquire-zero-trust-firm-elisity-for-up-to-1-3-billion/)
* [Bricksforge WordPress Plugin Vulnerability Exploited in the Wild](https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/)
* [Canonical Websites Disrupted in Second DDoS Attack This Year](https://www.securityweek.com/canonical-websites-disrupted-in-second-ddos-attack-this-year/)
* [Mastermind of 15,000-Mule Cybercrime Laundering Network Pleads Guilty in US](https://www.securityweek.com/mastermind-of-15000-mule-cybercrime-laundering-network-pleads-guilty-in-us/)
* [iRhythm Data Breach Impacts at Least 360,000 People](https://www.securityweek.com/irhythm-data-breach-impacts-over-360000-people/)
* [Ransomware Response Expert Arrested in ShinyHunters FBI Hack Probe](https://www.securityweek.com/ransomware-response-expert-arrested-in-shinyhunters-fbi-hack-probe/)
* [Critical SonicWall Vulnerability Exploited Days After Disclosure](https://www.securityweek.com/critical-sonicwall-vulnerability-exploited-days-after-disclosure/)
* [Insider Cyber Extortion Plot Against Industrial Firm Lands Engineer in Prison](https://www.securityweek.com/insider-cyber-extortion-plot-against-industrial-firm-lands-engineer-in-prison/)

![](https://www.securityweek.com/wp-content/uploads/2022/04/SecurityWeek-Small-Dark.png)

#### Trending

## [Ransomware Response Expert Arrested in ShinyHunters FBI Hack Probe](https://www.securityweek.com/ransomware-response-expert-arrested-in-shinyhunters-fbi-hack-probe/)

## [Critical SonicWall Vulnerability Exploited Days After Disclosure](https://www.securityweek.com/critical-sonicwall-vulnerability-exploited-days-after-disclosure/)

## [Insider Cyber Extortion Plot Against Industrial Firm Lands Engineer in Prison](https://www.securityweek.com/insider-cyber-extortion-plot-against-industrial-firm-lands-engineer-in-prison/)

## [iRhythm Data Breach Impacts at Least 360,000 People](https://www.securityweek.com/irhythm-data-breach-impacts-over-360000-people/)

## [Mastermind of 15,000-Mule Cybercrime Laundering Network Pleads Guilty in US](https://www.securityweek.com/mastermind-of-15000-mule-cybercrime-laundering-network-pleads-guilty-in-us/)

## [Security Awareness Training Isn’t Dead, but It Needs a Rethink](https://www.securityweek.com/security-awareness-training-isnt-dead-but-it-needs-a-rethink/)

## [Canonical Websites Disrupted in Second DDoS Attack This Year](https://www.securityweek.com/canonical-websites-disrupted-in-second-ddos-attack-this-year/)

## [Bricksforge WordPress Plugin Vulnerability Exploited in the Wild](https://www.securityweek.com/bricksforge-wordpress-plugin-vulnerability-exploited-in-the-wild/)

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
  [+ Whatsapp](https://web.whatsapp.com/send?text=Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch/)
  [+ Whatsapp](whatsapp://send?text=Let’s Encrypt Cuts Default Certificate Validity to 64 Days Ahead of 45-Day Switch https://www.securityweek.com/lets-encrypt-cuts-default-certificate-validity-to-64-days-ahead-of-45-day-switch/)
  [+ Email](/cdn-cgi/l/email-protection#cef1bdbbaca4abadbaf382abba2c4e57bdee8ba0adbcb7bebaee8dbbbabdee8aaba8afbba2baee8dabbcbaa7a8a7adafbaabee98afa2a7aaa7bab7eebaa1eef8faee8aafb7bdee8fa6abafaaeea1a8eefafbe38aafb7ee9db9a7baada6e8afa3bef58c818a97f387eea8a1bba0aaeebaa6a7bdeeafbcbaa7ada2abeea7a0baabbcabbdbaa7a0a9eeafa0aaeebaa6a1bba9a6baeea1a8eebda6afbca7a0a9eea7baeeb9a7baa6eeb7a1bbe0ee8da6abada5eea7baeea1bbbaf4eea6bababebdf4e1e1b9b9b9e0bdabadbbbca7bab7b9ababa5e0ada1a3e1a2abbabde3aba0adbcb7bebae3adbbbabde3aaaba8afbba2bae3adabbcbaa7a8a7adafbaabe3b8afa2a7aaa7bab7e3baa1e3f8fae3aaafb7bde3afa6abafaae3a1a8e3fafbe3aaafb7e3bdb9a7baada6e1)



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