---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-11T18:15:14.634677+00:00'
exported_at: '2026-03-11T18:15:16.907279+00:00'
feed: https://krebsonsecurity.com/feed/
language: en
source_url: https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker
structured_data:
  about: []
  author: ''
  description: Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker
  headline: Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://krebsonsecurity.com/2026/03/iran-backed-hackers-claim-wiper-attack-on-medtech-firm-stryker
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Iran-Backed Hackers Claim Wiper Attack on Medtech Firm Stryker
updated_at: '2026-03-11T18:15:14.634677+00:00'
url_hash: f7487a74cbe55f9818c507abd9f77c748eefbc67
---

A hacktivist group with links to Iran’s intelligence agencies is claiming responsibility for a data-wiping attack against
**Stryker**
, a global medical technology company based in Michigan. News reports out of Ireland, Stryker’s largest hub outside of the United States, said the company sent home more than 5,000 workers there today. Meanwhile, a voicemail message at Stryker’s main U.S. headquarters says the company is currently experiencing a building emergency.

In a lengthy statement posted to Telegram, an Iranian hacktivist group known as
**Handala**
(a.k.a. Handala Hack Team) claimed that Stryker’s offices in 79 countries have been forced to shut down after the group erased data from more than 200,000 systems, servers and mobile devices.

![A manifesto posted by the Iran-backed hacktivist group Handala, claiming a mass data-wiping attack against medical technology maker Stryker.](https://krebsonsecurity.com/wp-content/uploads/2026/03/handala-stryker.png)

A manifesto posted by the Iran-backed hacktivist group Handala, claiming a mass data-wiping attack against medical technology maker Stryker.

“All the acquired data is now in the hands of the free people of the world, ready to be used for the true advancement of humanity and the exposure of injustice and corruption,” a portion of the Handala statement reads.

The group said the wiper attack was in retaliation for a Feb. 28 missile strike that hit an Iranian school and killed at least 175 people, most of them children.
**The New York Times**
[reports](https://www.nytimes.com/2026/03/11/us/politics/iran-school-missile-strike.html)
today that an ongoing military investigation has determined the United States is responsible for the deadly Tomahawk missile strike.

Handala was one of several Iran-linked hacker groups recently
[profiled](https://unit42.paloaltonetworks.com/iranian-cyberattacks-2026/)
by
**Palo Alto Networks**
, which links it to Iran’s
**Ministry of Intelligence and Security**
(MOIS). Palo Alto says Handala surfaced in late 2023 and is assessed as one of several online personas maintained by
[Void Manticore](https://malpedia.caad.fkie.fraunhofer.de/actor/void_manticore)
, a MOIS-affiliated actor.

Stryker’s website says the company has 56,000 employees in 61 countries. A phone call placed Wednesday morning to the media line at Stryker’s Michigan headquarters sent this author to a voicemail message that stated, “We are currently experiencing a building emergency. Please try your call again later.”

A
[report](https://www.irishexaminer.com/news/munster/arid-41808308.html)
Wednesday morning from the
**Irish Examiner**
said Stryker staff are now communicating via WhatsApp for any updates on when they can return to work. The story quoted an unnamed employee saying anything connected to the network is down, and that “anyone with Microsoft Outlook on their personal phones had their devices wiped.”

“Multiple sources have said that systems in the Cork headquarters have been ‘shut down’ and that Stryker devices held by employees have been wiped out,” the Examiner reported. “The login pages coming up on these devices have been defaced with the Handala logo.”

Wiper attacks usually involve malicious software designed to overwrite any existing data on infected devices. But a trusted source with knowledge of the attack who spoke on condition of anonymity told KrebsOnSecurity the perpetrators in this case appear to have used a Microsoft service called
**Microsoft Intune**
to issue a ‘remote wipe’ command against all connected devices.

Intune is a cloud-based solution built for IT teams to enforce security and data compliance policies, and it provides a single, web-based administrative console to monitor and control devices regardless of location. The Intune connection is supported by
[this Reddit discussion](https://www.reddit.com/r/cybersecurity/comments/1rqopq0/stryker_hit_by_handala_intune_managed_devices/)
on the Stryker outage, where several users who claimed to be Stryker employees said they were told to uninstall Intune urgently.

Palo Alto says Handala’s hack-and-leak activity is primarily focused on Israel, with occasional targeting outside that scope when it serves a specific agenda. The security firm said Handala also has taken credit for recent attacks against fuel systems in Jordan and an Israeli energy exploration company.

“Recent observed activities are opportunistic and ‘quick and dirty,’ with a noticeable focus on supply-chain footholds (e.g., IT/service providers) to reach downstream victims, followed by ‘proof’ posts to amplify credibility and intimidate targets,” Palo Alto researchers wrote.

The Handala manifesto posted to Telegram referred to Stryker as a “Zionist-rooted corporation,” which may be a reference to the company’s 2019 acquisition of the Israeli company OrthoSpace.

This is a developing story. Updates will be noted with a timestamp.