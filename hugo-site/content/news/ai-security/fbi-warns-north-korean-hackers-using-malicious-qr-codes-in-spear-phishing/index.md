---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-09T08:15:13.301332+00:00'
exported_at: '2026-01-09T08:15:16.285950+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/fbi-warns-north-korean-hackers-using.html
structured_data:
  about: []
  author: ''
  description: FBI warns Kimsuky hackers linked to North Korea are using malicious
    QR codes to bypass MFA, steal session tokens, and hijack cloud accounts.
  headline: FBI Warns North Korean Hackers Using Malicious QR Codes in Spear-Phishing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/fbi-warns-north-korean-hackers-using.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: FBI Warns North Korean Hackers Using Malicious QR Codes in Spear-Phishing
updated_at: '2026-01-09T08:15:13.301332+00:00'
url_hash: 6dffe25b52c042edf1ac1529fd1204a01c493815
---

**

Jan 09, 2026
**

Ravie Lakshmanan

Mobile Security / Email Security

The U.S. Federal Bureau of Investigation (FBI) on Thursday released an advisory warning of North Korean state-sponsored threat actors leveraging malicious QR codes in spear-phishing campaigns targeting entities in the country.

"As of 2025, Kimsuky actors have targeted think tanks, academic institutions, and both U.S. and foreign government entities with embedded malicious Quick Response (QR) codes in spear-phishing campaigns," the FBI
[said](https://www.ic3.gov/CSA/2026/260108.pdf)
in the flash alert. "This type of spear-phishing attack is referred to as quishing."

The use of QR codes for phishing is a tactic that forces victims to shift from a machine that's secured by enterprise policies to a mobile device that may not offer the same level of protection, effectively allowing threat actors to bypass traditional defenses.

Kimsuky, also tracked as APT43, Black Banshee, Emerald Sleet, Springtail, TA427, and Velvet Chollima, is a threat group that's assessed to be affiliated with North Korea's Reconnaissance General Bureau (RGB). It has a long history of orchestrating spear-phishing campaigns that are specifically designed to subvert email authentication protocols.

In a bulletin released in May 2024, the U.S. government
[called out](https://thehackernews.com/2024/05/nsa-fbi-alert-on-n-korean-hackers.html)
the hacking crew for exploiting improperly configured Domain-based Message Authentication, Reporting, and Conformance (DMARC) record policies to send emails that look like they've come from a legitimate domain.

The FBI said it observed the Kimsuky actors utilizing malicious QR codes as part of targeted phishing efforts several times in May and June 2025 -

* Spoofing a foreign advisor in emails requesting insight from a think tank leader regarding recent developments on the Korean Peninsula by scanning a QR code to
  [access a questionnaire](https://thehackernews.com/2025/04/state-sponsored-hackers-weaponize.html)
* Spoofing an embassy employee in emails requesting input from a senior fellow at a think tank about North Korean human rights issues, along with a QR code that claimed to provide access to a secure drive
* Spoofing a think tank employee in emails with a QR code that's designed to take the victim to infrastructure under their control for follow-on activity
* Sending emails to a strategic advisory firm, inviting them to a non-existent conference by urging the recipients to scan a QR code to redirect them to a registration landing page that's designed to harvest their Google account credentials by using a fake login page

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/attack-surface-insight-d)

The disclosure comes less than a month after ENKI
[revealed](https://thehackernews.com/2025/12/kimsuky-spreads-docswap-android-malware.html)
details of a QR code campaign conducted by Kimsuky to distribute a new variant of Android malware called DocSwap in phishing emails mimicking a Seoul-based logistics firm.

"Quishing operations frequently end with session token theft and replay, enabling attackers to bypass multi-factor authentication and hijack cloud identities without triggering typical 'MFA failed' alerts," the FBI said. "Adversaries then establish persistence in the organization [and propagate secondary spear-phishing from the compromised mailbox."

"Because the compromise path originates on unmanaged mobile devices outside normal Endpoint Detection and Response (EDR) and network inspection boundaries, Quishing is now considered a high-confidence, MFA-resilient identity intrusion vector in enterprise environments."