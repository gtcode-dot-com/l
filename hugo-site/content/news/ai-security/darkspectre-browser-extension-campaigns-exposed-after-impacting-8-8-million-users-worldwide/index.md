---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-01T00:15:14.237949+00:00'
exported_at: '2026-01-01T00:15:16.923509+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html
structured_data:
  about: []
  author: ''
  description: A China-linked threat actor used malicious browser extensions over
    seven years to steal data and corporate intelligence from Chrome, Edge, and Firefox
  headline: DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million
    Users Worldwide
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/darkspectre-browser-extension-campaigns.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: DarkSpectre Browser Extension Campaigns Exposed After Impacting 8.8 Million
  Users Worldwide
updated_at: '2026-01-01T00:15:14.237949+00:00'
url_hash: d676ea9291db580f5608bd249ec79912227ab281
---

The threat actor behind two malicious browser extension campaigns,
[ShadyPanda](https://thehackernews.com/2025/12/shadypanda-turns-popular-browser.html)
and
[GhostPoster](https://thehackernews.com/2025/12/ghostposter-malware-found-in-17-firefox.html)
, has been attributed to a third attack campaign codenamed DarkSpectre that has impacted 2.2 million users of Google Chrome, Microsoft Edge, and Mozilla Firefox.

The activity is
[assessed](https://www.koi.ai/blog/darkspectre-unmasking-the-threat-actor-behind-7-8-million-infected-browsers)
to be the work of a Chinese threat actor that Koi Security is tracking under the moniker
**DarkSpectre**
. In all, the campaigns have collectively affected over 8.8 million users spanning a period of more than seven years.

ShadyPanda was first unmasked by the cybersecurity company earlier this month as targeting all three browser users to facilitate data theft, search query hijacking, and affiliate fraud. It has been found to affect 5.6 million users, including 1.3 newly identified victims stemming from over 100 extensions flagged as connected to the same cluster.

This also includes an Edge add-on named "New Tab - Customized Dashboard" that features a logic bomb that waits for three days prior to triggering its malicious behavior. The time-delayed activation is an attempt to give the impression that it's legitimate during the review period and get it approved.

Nine of these extensions are currently active, with an additional 85 "dormant sleepers" that are benign and meant to attract a user base before they are weaponized via malicious updates. Koi said the updates were introduced after more than five years in some cases.

The second campaign, GhostPoster, is mostly focused on Firefox users, targeting them with seemingly harmless utilities and VPN tools to serve malicious JavaScript code designed to hijack affiliate links, inject tracking code, and commit click and ad fraud. Further investigation into the activity has unearthed more browser add-ons, including a Google Translate (developer "charliesmithbons") extension for Opera with nearly one million installs.

The third campaign mounted by DarkSpectre is The Zoom Stealer, which involves a set of 18 extensions across Chrome, Edge, and Firefox that are geared towards corporate meeting intelligence by collecting online meeting-related data like meeting URLs with embedded passwords, meeting IDs, topics, descriptions, scheduled times, and registration status.

The list of identified extensions and their corresponding IDs is below -

Google Chrome -

* Chrome Audio Capture (kfokdmfpdnokpmpbjhjbcabgligoelgp)
* ZED: Zoom Easy Downloader (pdadlkbckhinonakkfkdaadceojbekep)
* X (Twitter) Video Downloader (akmdionenlnfcipmdhbhcnkighafmdha)
* Google Meet Auto Admit (pabkjoplheapcclldpknfpcepheldbga)
* Zoom.us Always Show "Join From Web" (aedgpiecagcpmehhelbibfbgpfiafdkm)
* Timer for Google Meet (dpdgjbnanmmlikideilnpfjjdbmneanf)
* CVR: Chrome Video Recorder (kabbfhmcaaodobkfbnnehopcghicgffo)
* GoToWebinar & GoToMeeting Download Recordings (cphibdhgbdoekmkkcbbaoogedpfibeme)
* Meet auto admit (ceofheakaalaecnecdkdanhejojkpeai)
* Google Meet Tweak (Emojis, Text, Cam Effects) (dakebdbeofhmlnmjlmhjdmmjmfohiicn)
* Mute All on Meet (adjoknoacleghaejlggocbakidkoifle)
* Google Meet Push-To-Talk (pgpidfocdapogajplhjofamgeboonmmj)
* Photo Downloader for Facebook, Instagram, + (ifklcpoenaammhnoddgedlapnodfcjpn)
* Zoomcoder Extension (ebhomdageggjbmomenipfbhcjamfkmbl)
* Auto-join for Google Meet (ajfokipknlmjhcioemgnofkpmdnbaldi)

Microsoft Edge -

* Edge Audio Capture (mhjdjckeljinofckdibjiojbdpapoecj)

Mozilla Firefox -

* Twiter X Video Downloader ({7536027f-96fb-4762-9e02-fdfaedd3bfb5}, published by "invaliddejavu")
* x-video-downloader (xtwitterdownloader@benimaddonum.com, published by "invaliddejavu")

As is evident by the names of the extensions, a majority of them are engineered to mimic tools for enterprise-oriented videoconferencing applications like Google Meet, Zoom, and GoTo Webinar to exfiltrate meeting links, credentials, and participant lists over a WebSocket connection in real-time.

It's also capable of harvesting details about webinar speakers and hosts, such as names, titles, bios, profile photos, and company affiliations, along with logos, promotional graphics, and session metadata, every time a user visits a webinar registration page via the browser with one of the extensions installed.

These add-ons have been found to request access to more than 28 video conferencing platforms, including Cisco WebEx, Google Meet, GoTo Webinar, Microsoft Teams, and Zoom, among others, regardless of whether they required access to them in the first place.

"This isn't consumer fraud - this is corporate espionage infrastructure," researchers Tuval Admoni and Gal Hachamov said. "The Zoom Stealer represents something more targeted: systematic collection of corporate meeting intelligence. Users got what was advertised. The extensions earned trust and positive reviews. Meanwhile, surveillance ran silently in the background."

The cybersecurity company said the gathered information could be used to fuel corporate espionage by selling the data to other bad actors, and enable social engineering and large-scale impersonation operations.

The Chinese links to the operation are based on several clues: consistent use of command-and-control (C2) servers hosted on Alibaba Cloud, Internet Content Provider (ICP) registrations linked to Chinese provinces like Hubei, code artifacts containing Chinese-language strings and comments, and fraud schemes specifically aimed at Chinese e-commerce platforms such as JD.com and Taobao.

"DarkSpectre likely has more infrastructure in place right now - extensions that look completely legitimate because they are legitimate, for now," Koi said. "They're still in the trust-building phase, accumulating users, earning badges, waiting."