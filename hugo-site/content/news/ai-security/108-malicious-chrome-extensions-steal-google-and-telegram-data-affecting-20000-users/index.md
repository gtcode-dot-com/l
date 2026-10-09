---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T10:15:14.493266+00:00'
exported_at: '2026-04-14T10:15:16.734395+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html
structured_data:
  about: []
  author: ''
  description: 108 Chrome extensions routed stolen Google and Telegram data to shared
    C2 infrastructure, impacting 20,000 users.
  headline: 108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting
    20,000 Users
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 108 Malicious Chrome Extensions Steal Google and Telegram Data, Affecting 20,000
  Users
updated_at: '2026-04-14T10:15:14.493266+00:00'
url_hash: c4ac1963135e5f8e1bf6ad7aa3ceb9c7e127f7ef
---

**

Ravie Lakshmanan
**

Apr 14, 2026

Data Theft / Browser Security

Cybersecurity researchers have discovered a new campaign in which a cluster of 108 Google Chrome extensions has been found to communicate with the same command-and-control (C2) infrastructure with the goal of collecting user data and enabling browser-level abuse by injecting ads and arbitrary JavaScript code into every web page visited.

According to Socket, the extensions are published under five distinct publisher identities – Yana Project, GameGen, SideGames, Rodeo Games, and InterAlt – and have collectively amassed about 20,000 installs in the Chrome Web Store.

"All 108 route stolen credentials, user identities, and browsing data to servers controlled by the same operator," security researcher Kush Pandya
[said](https://socket.dev/blog/108-chrome-ext-linked-to-data-exfil-session-theft-shared-c2)
in an analysis.

Of these, 54 add-ons steal Google account identity via OAuth2, 45 extensions contain a universal backdoor that opens arbitrary URLs as soon as the browser is started, and the remaining ones engage in a variety of malicious behaviors -

* Exfiltrate Telegram Web sessions every 15 seconds
* Strip YouTube and TikTok security headers (i.e., Content Security Policy, X-Frame-Options, and CORS) and inject gambling overlays and ads
* Inject content scripts into every page the user visits
* Proxy all translation requests through the threat actor's server

In an attempt to lend a veneer of legitimacy, the identified extensions masquerade as Telegram sidebar clients, slot machine and Keno games, YouTube and TikTok enhancers, text translation tools, and page utilities. The advertised functionality is diverse, aiming to cast a wide net, while sharing the same backend.

Unbeknownst to the users, however, malicious code running in the background captures session information, injects arbitrary scripts, and opens URLs of the attacker's choosing.

Some of the identified extensions are listed below -

* Telegram Multi-account (ID: obifanppcpchlehkjipahhphbcbjekfa), which extracts the user\_auth token used by Telegram Web and exfiltrates the data to a remote server. It can also overwrite localStorage with threat actor-supplied session data and force-load the messaging application, effectively replacing the victim's active Telegram session with the threat actor's chosen session.
* Web Client for Telegram - Teleside (ID: mdcfennpfgkngnibjbpnpaafcjnhcjno), which strips Telegram's security headers and injects scripts to steal Telegram sessions.
* Formula Rush Racing Game (ID: akebbllmckjphjiojeioooidhnddnplj), which steals the user's Google account identity the first time the victim clicks the sign-in button. This includes details like email, full name, profile picture URL, and Google account identifier.

"Five extensions use Chrome's declarativeNetRequest API to strip security headers from target sites before the page loads," Socket said. "All 108 malicious extensions share the same backend, hosted at 144.126.135[.]238."

It's currently not known who is behind the policy-violating extensions. However, an analysis of source code has uncovered Russian language comments across several add-ons.

Users who have installed any of the extensions are advised to remove them with immediate effect and log out of all Telegram Web sessions from the Telegram mobile app.