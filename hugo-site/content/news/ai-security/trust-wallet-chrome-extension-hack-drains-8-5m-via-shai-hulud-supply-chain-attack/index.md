---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-01T00:15:14.091698+00:00'
exported_at: '2026-01-01T00:15:16.925091+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html
structured_data:
  about: []
  author: ''
  description: Trust Wallet confirmed a supply chain attack let hackers push a malicious
    Chrome extension update, draining $8.5 million from 2,520 wallets.
  headline: Trust Wallet Chrome Extension Hack Drains $8.5M via Shai-Hulud Supply
    Chain Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-hack.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Trust Wallet Chrome Extension Hack Drains $8.5M via Shai-Hulud Supply Chain
  Attack
updated_at: '2026-01-01T00:15:14.091698+00:00'
url_hash: 4adaacd96fc80ba0cc89a8b3d39c1bdafca14ca2
---

**

Dec 31, 2026
**

Ravie Lakshmanan

Software Security / Data Breach

Trust Wallet on Tuesday revealed that the second iteration of the
[Shai-Hulud](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html)
(aka Sha1-Hulud) supply chain outbreak in November 2025 was likely responsible for the hack of its Google Chrome extension, ultimately resulting in the theft of approximately $8.5 million in assets.

"Our Developer GitHub secrets were exposed in the attack, which gave the attacker access to our browser extension source code and the Chrome Web Store (CWS) API key," the company
[said](https://trustwallet.com/blog/announcements/trust-wallet-browser-extension-v268-incident-community-update)
in a post-mortem published Tuesday.

"The attacker obtained full CWS API access via the leaked key, allowing builds to be uploaded directly without Trust Wallet's standard release process, which requires internal approval/manual review."

Subsequently, the attacker is said to have registered the domain "metrics-trustwallet[.]com" and pushed a trojanized version of the extension with a backdoor that's capable of harvesting users' wallet mnemonic phrases to the sub-domain "api.metrics-trustwallet[.]com."

The disclosure comes days after Trust Wallet
[urged](https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html)
about one million users of its Chrome extension to update to version 2.69 after a malicious update (version 2.68) was pushed by unknown threat actors on December 24, 2025, to the browser's extension marketplace.

The security incident ultimately led to $8.5 million in cryptocurrency assets being drained from 2,520 wallet addresses to no less than 17 wallet addresses controlled by the attacker. The first wallet-draining activity was publicly reported a day after the malicious update.

Trust Wallet has since initiated a reimbursement claim process for impacted victims. The company noted that reviews of submitted claims are ongoing and are being handled on a case-by-case basis. It also stressed that processing times may vary with each case due to the need to distinguish between victims and bad actors, and further protect against fraud.

To prevent such breaches from occurring again, Trust Wallet said it has implemented additional monitoring capabilities and controls related to its release processes.

"Sha1-Hulud was an industry-wide software supply chain attack that affected companies across multiple sectors, including but not limited to crypto," the company said. "It involved malicious code being introduced and distributed through commonly-used developer tooling. This allowed attackers to gain access through trusted software dependencies rather than directly targeting individual organizations."

Trust Wallet's disclosure coincides with the
[emergence of Shai-Hulud 3.0](https://thehackernews.com/2025/12/researchers-spot-modified-shai-hulud.html)
with increased obfuscation and reliability improvements, while still remaining laser-focused on stealing secrets from developer machines.

"The primary difference lies in string obfuscation, error handling, and Windows compatibility, all aimed at increasing campaign longevity rather than introducing novel exploitation techniques," Upwind researchers Guy Gilad and Moshe Hassan
[said](https://www.upwind.io/feed/shai-hulud-3-npm-supply-chain-worm)
.