---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-21T06:12:18.305805+00:00'
exported_at: '2026-02-21T06:12:21.918668+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html
structured_data:
  about: []
  author: ''
  description: 'Malicious Chrome Extensions Caught Stealing Business Data, Emails,
    and Browsing History | Read more hacking news on The Hacker News cybersecurity
    news website and learn how to protect against cyberattacks and software vulnerabilities. '
  headline: Malicious Chrome Extensions Caught Stealing Business Data, Emails, and
    Browsing History
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Malicious Chrome Extensions Caught Stealing Business Data, Emails, and Browsing
  History
updated_at: '2026-02-21T06:12:18.305805+00:00'
url_hash: e0d7bac6a08ab6387add3a1be792a327bc92f229
---

Cybersecurity researchers have discovered a malicious Google Chrome extension that's designed to steal data associated with Meta Business Suite and Facebook Business Manager.

The extension, named CL Suite by @CLMasters (ID: jkphinfhmfkckkcnifhjiplhfoiefffl), is marketed as a way to scrape Meta Business Suite data, remove verification pop-ups, and generate two-factor authentication (2FA) codes. The extension has 33 users as of writing. It was first uploaded to the Chrome Web Store on March 1, 2025.

However, the browser add-on also exfiltrates TOTP codes for Facebook and Meta Business accounts, Business Manager contact lists, and analytics data to infrastructure controlled by the threat actor, Socket said.

"The extension requests broad access to meta.com and facebook.com and claims in its privacy policy that 2FA secrets and Business Manager data remain local," security researcher Kirill Boychenko
[said](https://socket.dev/blog/malicious-chrome-extension-steals-meta-business-manager-exports-and-totp-2fa-seeds)
.

"In practice, the code transmits TOTP seeds and current one-time security codes, Meta Business 'People' CSV exports, and Business Manager analytics data to a backend at getauth[.]pro, with an option to forward the same payloads to a Telegram channel controlled by the threat actor."

By targeting users of Meta Business Suite and Facebook Business Manager, the threat actor behind the operation has leveraged the extension to conduct data collection and exfiltration without users' knowledge or consent.

While the extension does not have capabilities to steal password-related information, the attacker could obtain such information beforehand from other sources, such as infostealer logs or credential dumps, and then use the stolen codes to gain unauthorized access to victims' accounts.

The full scope of the malicious add-on's capabilities is listed below -

* Steal TOTP seed (a unique, alphanumeric code that's used to generate time-based one-time passwords) and 2FA code
* Target Business Manager "People" view by navigating to facebook[.]com and meta[.]com and build a CSV file with names, email addresses, roles and permissions, and their status and access details.
* Enumerate Business Manager-level entities and their linked assets and build a CSV file of Business Manager IDs and names, attached ad accounts, connected pages and assets, and billing and payment configuration details.

Socket warned that despite the low number of installs, the extension gives the threat actor enough information to identify high-value targets and mount follow-on attacks.

"CL Suite by @CLMasters shows how a narrow browser extension can repackage data scraping as a 'tool' for Meta Business Suite and Facebook Business Manager," Boychenko said.

"Its people extraction, Business Manager analytics, popup suppression, and in-browser 2FA generation are not neutral productivity features, they are purpose-built scrapers for high-value Meta surfaces that collect contact lists, access metadata, and 2FA material straight from authenticated pages."

## Chrome Extensions Hijack VKontakte Accounts

The disclosure comes as Koi Security
[found](https://www.koi.ai/blog/vk-styles-500k-users-infected-by-chrome-extensions-that-hijack-vkontakte-accounts)
that about 500,000 VKontakte users have had their accounts silently hijacked through Chrome extensions masquerading as VK customization tools. The large-scale campaign has been codenamed
**VK Styles**
.

The malware embedded in the extensions is designed to engage in active account manipulation by automatically subscribing users to the attacker's VK groups, resetting account settings every 30 days to override user preferences, manipulating Cross-Site Request Forgery (CSRF) tokens to bypass VK's security protections, and maintaining persistent control.

The activity has been traced to a threat actor operating under the GitHub username 2vk, who has relied on VK's own social network to distribute malicious payloads and build a follower base through forced subscriptions. The names of the extensions are listed below -

* VK Styles - Themes for vk.com (ID: ceibjdigmfbbgcpkkdpmjokkokklodmc)
* VK Music - audio saver (ID: mflibpdjoodmoppignjhciadahapkoch)
* Music Downloader - VKsaver (ID: lgakkahjfibfgmacigibnhcgepajgfdb)
* vksaver - music saver vk (ID: bndkfmmbidllaiccmpnbdonijmicaafn)
* VKfeed - Download Music and Video from VK (ID: pcdgkgbadeggbnodegejccjffnoakcoh)

One of the defining traits of the campaign is the use of a VK profile's ("vk[.]com/m0nda") HTML metadata tags as a dead drop resolver to conceal the next-stage payload URLs and, therefore, evade detection. The next-stage payload is hosted in a public repository named "-" that's associated with 2vk. Present in the payload is obfuscated JavaScript that's injected into every VK page the victim visits.

The repository is still accessible as of writing, with the file, simply named "C," receiving a total of 17 commits between June 2025 and January 2026, as the operator refined and added new functionality.

"Each commit shows deliberate refinement," security researcher Ariel Cohen said. "This isn't sloppy malware - it's a maintained software project with version control, testing, and iterative improvements."

VK Styles has primarily affected Russian-speaking users, who are VK's main demographic, as well as users across Eastern Europe, Central Asia, and Russian diaspora communities globally. The campaign is assessed to be active since at least June 22, 2025, when the initial version of the payload was pushed to the "-" repository.

## Fake AI Chrome Extensions Steal Credentials, Emails

The findings also coincide with the discovery of another coordinated campaign dubbed
**AiFrame**
, where a cluster of 32 browser add-ons advertised as artificial intelligence (AI) assistants for summarization, chat, writing, and Gmail assistance are being used to siphon sensitive data. These extensions have been collectively installed by more than 260,000 users.

"While these tools appear legitimate on the surface, they hide a dangerous architecture: instead of implementing core functionality locally, they embed remote, server-controlled interfaces inside extension-controlled surfaces and act as privileged proxies, granting remote infrastructure access to sensitive browser capabilities," LayerX researcher Natalie Zargarov
[said](https://layerxsecurity.com/blog/aiframe-fake-ai-assistant-extensions-targeting-260000-chrome-users-via-injected-iframes/)
.

The names of the malicious extensions are as follows -

* AI Assistant (ID: nlhpidbjmmffhoogcennoiopekbiglbp)
* Llama (ID: gcfianbpjcfkafpiadmheejkokcmdkjl)
* Gemini AI Sidebar (ID: fppbiomdkfbhgjjdmojlogeceejinadg)
* AI Sidebar (ID: djhjckkfgancelbmgcamjimgphaphjdl)
* ChatGPT Sidebar (ID: llojfncgbabajmdglnkbhmiebiinohek)
* AI Sidebar (ID: gghdfkafnhfpaooiolhncejnlgglhkhe)
* Grok (ID: cgmmcoandmabammnhfnjcakdeejbfimn)
* Asking Chat Gpt (ID: phiphcloddhmndjbdedgfbglhpkjcffh)
* ChatGBT (ID: pgfibniplgcnccdnkhblpmmlfodijppg)
* Chat Bot GPT (ID: nkgbfengofophpmonladgaldioelckbe)
* Grok Chatbot (ID: gcdfailafdfjbailcdcbjmeginhncjkb)
* Chat With Gemini (ID: ebmmjmakencgmgoijdfnbailknaaiffh)
* XAI (ID: baonbjckakcpgliaafcodddkoednpjgf)
* Google Gemini (ID: fdlagfnfaheppaigholhoojabfaapnhb)
* Ask Gemini (ID: gnaekhndaddbimfllbgmecjijbbfpabc)
* AI Letter Generator (ID: hgnjolbjpjmhepcbjgeeallnamkjnfgi)
* AI Message Generator (ID: lodlcpnbppgipaimgbjgniokjcnpiiad)
* AI Translator (ID: cmpmhhjahlioglkleiofbjodhhiejhei)
* AI For Translation (ID: bilfflcophfehljhpnklmcelkoiffapb)
* AI Cover Letter Generator (ID: cicjlpmjmimeoempffghfglndokjihhn)
* AI Image Generator Chat GPT (ID: ckneindgfbjnbbiggcmnjeofelhflhaj)
* Ai Wallpaper Generator (ID: dbclhjpifdfkofnmjfpheiondafpkoed)
* Ai Picture Generator (ID: ecikmpoikkcelnakpgaeplcjoickgacj)
* DeepSeek Download (ID: kepibgehhljlecgaeihhnmibnmikbnga)
* AI Email Writer (ID: ckicoadchmmndbakbokhapncehanaeni)
* Email Generator AI (ID: fnjinbdmidgjkpmlihcginjipjaoapol)
* DeepSeek Chat (ID: gohgeedemmaohocbaccllpkabadoogpl)
* ChatGPT Picture Generator (ID: flnecpdpbhdblkpnegekobahlijbmfok)
* ChatGPT Translate (ID: acaeafediijmccnjlokgcdiojiljfpbe)
* AI GPT (ID: kblengdlefjpjkekanpoidgoghdngdgl)
* ChatGPT Translation (ID: idhknpoceajhnjokpnbicildeoligdgh)
* Chat GPT for Gmail (ID: fpmkabpaklbhbhegegapfkenkmpipick)

Once installed, these extensions render a full-screen iframe overlay pointing to a remote domain ("claude.tapnetic[.]pro"), allowing the attackers to remotely introduce new capabilities without requiring a Chrome Web Store update. When instructed by the iframe, the add-ons query the active browser tab and invoke a content script to extract readable article content using Mozilla's Readability library.

The malware also supports the capability to start speech recognition and exfiltrate the resulting transcript to the remote page. What's more, a smaller set of the extensions contain functionality to specifically target Gmail by reading visible email content directly from the document object model (DOM) when a victim visits mail.google[.]com.

"When Gmail-related features such as AI-assisted replies or summaries are invoked, the extracted email content is passed into the extension's logic and transmitted to third-party backend infrastructure controlled by the extension operator," LayerX said. "As a result, email message text and related contextual data may be sent off-device, outside of Gmail’s security boundary, to remote servers."

## 287 Chrome Extensions Exfiltrate Browsing History

The developments show how web browser extensions are
[increasingly being abused](https://thehackernews.com/2026/01/researchers-uncover-chrome-extensions.html)
by bad actors to harvest and exfiltrate sensitive data by passing them off as seemingly legitimate tools and utilities.

A report published by Q Continuum last week found a huge collection of 287 Chrome extensions that exfiltrate browsing history to data brokers. These extensions have 37.4 million installations, representing roughly 1% of the global Chrome userbase.

"It was shown in the past that Chrome extensions are used to exfiltrate user browser history that is then collected by data brokers such as Similarweb and Alexa," the researcher
[said](https://github.com/qcontinuum1/spying-extensions)
.

Given the risks involved, users are
[recommended](https://seraphicsecurity.com/learn/browser-security/top-5-browser-extension-security-risks-and-5-ways-to-prevent-them/)
to adopt a minimalist approach by only installing necessary, well-reviewed tools from official stores. It's also essential to periodically audit installed extensions for any signs of malicious behavior or excessive permission requests.

Other ways that users and organizations can ensure greater security include using separate browser profiles for sensitive tasks and implementing extension allowlisting to block those that are malicious or non-compliant.