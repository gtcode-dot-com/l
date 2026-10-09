---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T16:27:06.138387+00:00'
exported_at: '2026-10-08T16:27:07.802075+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html
structured_data:
  about: []
  author: ''
  description: Sixteen malicious Firefox extensions imitate Rabby and OKX wallets
    to intercept recovery phrases and private keys during wallet imports.
  headline: 16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal
    Recovery Phrases
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/16-malicious-firefox-extensions-pose-as.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 16 Malicious Firefox Extensions Pose as Rabby and OKX Wallets to Steal Recovery
  Phrases
updated_at: '2026-10-08T16:27:06.138387+00:00'
url_hash: f31e2f0411cadf2bd49b85518adafc83145e942c
---

**

Ravie Lakshmanan
**

Oct 08, 2026

Browser Security / Malware

Cybersecurity researchers have discovered a cluster of 16 malicious Mozilla Firefox extensions that are capable of stealing cryptocurrency wallet recovery phrases and private keys.

"The extensions masquerade as wallet portals, desktop utilities, and browser tools, but their code intercepts recovery phrases and private keys during wallet import flows and attempts to send those secrets to attacker-controlled Cloudflare Workers," Socket researcher Joseph Edwards
[said](https://socket.dev/blog/firefox-crypto-wallet-stealers)
in an analysis.

The names of the extensions are below -

* view-focus-bright@webtools.co@6.12.2
* quick-track-nest@tabtools.co@8.1.18
* vibe-kit-tool@fasttools.co@9.21.9
* edge-hub-snap@protools.net@4.12.24
* core-hub-peak@neattools.example@8.24.21
* sipoo-grozza@browserweb.com@2.1
* mozart-seo@webtools.com@1.4
* clean-file-bar@neattools.com@4.21.8
* clean-net-timer@plugify.example@4.17.1
* manager-square@webtools.com@1.4
* manager-course@webtools.com@1.4
* val-andrew@browserweb.com@1.4
* manager-team@browserweb.com@1.4
* valory-andrew@browserweb.com@1.4
* franklin-uk@browserweb.com@1.4
* franklin-uro@browserweb.com@1.4

Four of these extensions are clones of Rabby Wallet, while the rest are targeted clones of OKX Wallet. All the identified add-ons barring one have been found to contact the "\*.icy-star-f45c.workers[.]dev" domain. The end goal is to collect mnemonic phrases and private keys and exfiltrate them to the Cloudflare Workers domain.

The activity is assessed to be a continuation of an
[earlier wave](https://thehackernews.com/2026/08/40-malicious-firefox-extensions-pose-as.html)
that the application security company documented in August 2026. The findings suggest that the threat actors are rotating package names, versions, extension IDs, descriptions, and the presentation layer, while reusing the same wallet interfaces, credential-handling logic, and network infrastructure.

As of October 5, 2026, all the extensions have been removed. Users who have installed any of the aforementioned extensions and entered a real recovery phrase or private key into the fake wallet interfaces should assume compromise, create a new wallet from a clean system, and move their assets.

The findings coincide with the discovery of several malicious or sketchy extensions for Firefox, Google Chrome, and Microsoft Edge in recent months -

* A Firefox extension called "
  [ID- Pay](https://socket.dev/blog/firefox-google-account-takeover)
  " (pdf-para-texto@extensao.local) that poses as a utility for identity verification before opening protected PDF documents, but harbors functionality to fetch a remote payload from attacker-controlled infrastructure and inject JavaScript into the legitimate "accounts.google[.]com" domain to steal session cookies.
* A
  [cluster of 32 malicious browser extensions](https://www.akamai.com/blog/security-research/when-productivity-extensions-become-attack-platforms)
  across the Chrome Web Store and Microsoft Edge Add-ons Store that masquerades as benign productivity utilities, but harvest data, monitor user browsing habits, and stealthily replace the active tab with a destination URL specified in a remotely-retrieved configuration. The campaign has been active since March 2025 and attributed to a Korean-speaking threat actor.
* A
  [cluster of about 30 malicious browser extensions](https://www.akamai.com/blog/security-research/crypto-scam-extensions-masquerade-high-profile-investors)
  that masquerade as productivity tools, privacy utilities, and cryptocurrency-related services published under the names of legitimate, high-profile financial personalities with the goal of redirecting victims to cryptocurrency wallet phishing pages designed to steal recovery phrases, while skipping English-speaking users and analysis environments.
* A
  [cluster of 31 Russian-language Chrome extensions](https://riskyplugins.com/threat-library/russian-vpn-proxy-farm)
  that are advertised as VPNs for a specific blocked service in the country (e.g., Anthropic Claude, Facebook, Google Gemini, LinkedIn, Netflix, Notion, OpenAI ChatGPT, Spotify, Telegram, Threads, Wikipedia, X, and YouTube) but routes browser traffic through a proxy whose server list is fetched from a GitHub Pages URL (or Blogger, Google Docs, and Telegram for redundancy) post-installation.
* A Chrome Web Store extension named
  [Stylish](https://amibeingpwned.com/extensions/stylish)
  that
  [intercepts](https://amibeingpwned.com/blog/ai-chat-scraper-wall-of-shame)
  every ChatGPT, Gemini, Claude, Perplexity, Character.AI, and GitHub Copilot conversation and forwards the full response text to its operator.
* A Chrome Web Store extension named "
  [Urban VPN](https://amibeingpwned.com/blog/anatomy-of-a-malicious-extension)
  " that includes an "anti-phishing" feature designed to warn users before visiting any harmful sites, but never returns a phishing warning and silently transmits visited URLs to servers operated by BIScience. Urban VPN was
  [previously accused](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)
  of capturing user conversations with AI chatbots. However, the extension developers
  [clarified](https://www.urban-vpn.com/blog/setting-the-record-straight-how-urban-vpns-ai-protection-feature-actually-works/)
  that AI-related processing only occurs after the "AI Protection" feature was explicitly enabled. Earlier this May, the add-on developers also
  [addressed](https://amibeingpwned.com/blog/urban-vpn-postmessage-command-injection)
  a high-severity security vulnerability that allowed any website to send arbitrary commands to the extension without origin verification.
* A Chrome Web Store extension named "
  [Pop up blocker for Chrome™ - Poper Blocker](https://amibeingpwned.com/extensions/poper-blocker)
  " that's marketed as an ad blocker but
  [ships an interpreter](https://amibeingpwned.com/blog/poper-blocker-the-adblocker-that-spies-on-you)
  that downloads and interprets instructions from a command-and-control (C2) server, circumventing Google's
  [Manifest V3 rules](https://developer.chrome.com/docs/webstore/program-policies/mv3-requirements#:~:text=Building%20an%20interpreter%20to%20run%20complex%20commands%20fetched%20from%20a%20remote%20source%2C%20even%20if%20those%20commands%20are%20fetched%20as%20data)
  banning this behavior. The commands allow it to collect browser fingerprints, browsing history, social media profile information, and AI chatbot interactions.

To counter the threat associated with malicious extensions, users are advised to review the browser extensions installed in their environment, and remove those that are no longer needed. Organizations are recommended to audit extensions within managed environments, adopt runtime monitoring approaches, and deploy behavior-based extension monitoring technologies to detect suspicious activity.