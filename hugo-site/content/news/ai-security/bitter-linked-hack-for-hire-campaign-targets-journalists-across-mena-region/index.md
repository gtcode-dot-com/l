---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-09T12:15:15.029597+00:00'
exported_at: '2026-04-09T12:15:17.925953+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/bitter-linked-hack-for-hire-campaign.html
structured_data:
  about: []
  author: ''
  description: Hack-for-hire phishing tied to Bitter targeted MENA journalists from
    2023–2025, compromising an Apple account and enabling regional surveillance.
  headline: Bitter-Linked Hack-for-Hire Campaign Targets Journalists Across MENA Region
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/bitter-linked-hack-for-hire-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Bitter-Linked Hack-for-Hire Campaign Targets Journalists Across MENA Region
updated_at: '2026-04-09T12:15:15.029597+00:00'
url_hash: 783bddb299566221af5388927d188e355076819b
---

An apparent hack-for-hire campaign likely orchestrated by a threat actor with suspected ties to the Indian government targeted journalists, activists, and government officials across the Middle East and North Africa (MENA), according to findings from
[Access Now](https://www.accessnow.org/mena-phishing-2026/)
,
[Lookout](https://www.lookout.com/threat-intelligence/article/bitter-hack-for-hire)
, and
[SMEX](https://smex.org/smex-may2025/)
.

Two of the targets included prominent Egyptian journalists and government critics, Mostafa Al-A'sar and Ahmed Eltantawy, who were at the receiving end of a series of spear-phishing attacks that sought to compromise their Apple and Google accounts in October 2023 and January 2024 by directing them to fake pages that tricked them into entering their credentials and two-factor authentication (2FA) codes.

"The attacks were carried out from 2023 to 2024, and both targets are prominent critics of the Egyptian government who have previously faced political imprisonment; one of them was previously targeted with
[spyware](https://thehackernews.com/2023/09/latest-apple-zero-days-used-to-hack.html)
," Access Now's Digital Security Helpline said.

Also singled out as part of these efforts was an anonymous Lebanese journalist, who received phishing messages in May 2025 through the Apple Messages app and WhatsApp containing malicious links that, when clicked, tricked users into entering their account credentials as part of a supposed verification step from Apple.

"The phishing campaign included persistent attacks via iMessage/Apple Messenger and WhatsApp app, [...] impersonating Apple Support," SMEX, a digital rights non-profit in the West Asia and North Africa (WANA) region, said. "While the main focus of this campaign appears to be Apple services, evidence suggests that other messaging platforms, namely Telegram and Signal, were also targeted."

In the case of Al-A'sar, the spear-phishing attack aimed at compromising his Google account began with a LinkedIn message from a sock puppet persona named "Haifa Kareem," who approached him with a job opportunity. After the journalist shared their mobile number and email address with the LinkedIn user, he received an email from the latter on January 24, 2024, instructing him to join a Zoom call by clicking on a link shortened using Rebrandly.

The URL is assessed to be a consent-based phishing attack that leverages Google's OAuth 2.0 to grant the attacker unauthorized access to the victim's account through a malicious web application named "en-account.info."

"Unlike the previous attack, where the attacker impersonated an Apple account login and used a fake domain, this attack employs OAuth consent to leverage legitimate Google assets to deceive targets into providing their credentials," Access Now said.

"If the targeted user is not logged in to Google, they are prompted to enter their credentials (username and password). More commonly, if the user is already logged in, they are prompted to grant permission to an application that the attacker controls, using a third-party sign-in feature that is familiar to most Google users."

Some of the domains used in these phishing attacks are listed below -

* signin-apple.com-en-uk[.]co
* id-apple.com-en[.]io
* facetime.com-en[.]io
* secure-signal.com-en[.]io
* telegram.com-en[.]io
* verify-apple.com-ae[.]net
* join-facetime.com-ae[.]net
* android.com-ae[.]net
* encryption-plug-in-signal.com-ae[.]net

Interestingly, the use of the domain "com-ae[.]net" overlaps with an Android spyware campaign that Slovakian cybersecurity company ESET documented in October 2025, highlighting the use of deceptive websites impersonating Signal, ToTok, and Botim to deploy
[ProSpy and ToSpy](https://thehackernews.com/2025/10/warning-beware-of-android-spyware.html)
to unspecified targets in the U.A.E.

Specifically, the domain "encryption-plug-in-signal.com-ae[.]net" was used as an initial access vector for ProSpy by claiming to be a non-existent encryption plugin for Signal.The spyware comes fitted with capabilities to exfiltrate sensitive data like contacts, SMS messages, device metadata, and local files.

Neither of the Egyptian journalists' accounts was ultimately infiltrated. However, SMEX revealed that the initial attack that targeted the Lebanese journalist on May 19, 2025, completely compromised their Apple Account and resulted in the addition of a virtual device to the account to gain persistent access to the victim's data. The second wave of attacks was unsuccessful.

While there is no evidence that the three journalists were targeted with spyware, the evidence shows that threat actors can use the methods and infrastructure associated with the attacks to deliver malicious payloads and exfiltrate sensitive data.

"This suggests that the operation we identified may be part of a broader regional surveillance effort aimed at monitoring communications and harvesting personal data," Access Now said.

Lookout, in its own analysis of these campaigns, attributed the disparate efforts to a hack-for-hire operation with ties to
[Bitter](https://thehackernews.com/2025/06/bitter-hacker-group-expands-cyber.html)
, a threat cluster that's assessed to be tasked with intelligence gathering efforts in the interests of the Indian government. The espionage campaign has been operational since at least 2022.

Based on the phishing domains observed and ProSpy malware lures, the campaign has likely targeted victims in Bahrain, the U.A.E., Saudi Arabia, the U.K., Egypt, and potentially the U.S., or alumni of U.S. universities, indicating the attacks go beyond members of Egyptian and Lebanese civil society.

"The operation features a combination of targeted spear-phishing delivered through fake social media accounts and messaging applications leveraging persistent social engineering efforts, which may result in the delivery of Android spyware depending on the target’s device," the cybersecurity company said.

The campaign's links to Bitter stem from
[infrastructure connections](https://pastebin.com/WE7bjsat)
between "
[com-ae[.]net](https://www.virustotal.com/gui/domain/com-ae.net/details)
" and "
[youtubepremiumapp[.]com](https://www.virustotal.com/gui/domain/youtubepremiumapp.com/details)
," a domain flagged by
[Cyble](https://blog.cyble.com/2022/08/09/bitter-apt-group-using-dracarys-android-spyware/)
and
[Meta](https://thehackernews.com/2022/08/meta-cracks-down-on-cyber-espionage.html)
in August 2022 as linked to Bitter in relation to an espionage effort that used fake sites mimicking trusted services like YouTube, Signal, Telegram, and WhatsApp to distribute an Android malware dubbed Dracarys.

Lookout's analysis has also uncovered similarities between Dracarys and ProSpy, despite the latter being developed years later using Kotlin instead of Java. "Both families use worker logic to handle tasks, and they name the worker classes similarly. They also both use numbered C2 commands," the company added. "While ProSpy exfiltrates data to server endpoints starting with 'v3,' Dracarys exfiltrates data to server endpoints starting with 'r3.'"

These connections notwithstanding, what makes the campaign unusual is that Bitter has never been attributed to espionage campaigns targeting civil society members. This has raised two possibilities: either it's the work of a hack-for-hire operation with ties to Bitter or the threat actor itself is behind it, in which case it could indicate an expansion of its targeting scope.

"We do not know whether this represents an expansion of Bitter's role, or if it is an indication of overlap between Bitter and an unknown hack-for-hire group," Lookout added. "What we do know is that mobile malware continues to be a primary means of spying on civil society, whether it is purchased through a commercial surveillance vendor, outsourced to a hack-for-hire organization, or deployed directly by a nation state."