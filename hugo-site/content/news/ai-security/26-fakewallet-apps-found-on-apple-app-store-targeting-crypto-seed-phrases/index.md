---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-24T12:15:13.792713+00:00'
exported_at: '2026-04-24T12:15:16.037773+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/26-fakewallet-apps-found-on-apple-app.html
structured_data:
  about: []
  author: ''
  description: 26 FakeWallet apps since fall 2025 hijack crypto recovery phrases via
    Apple App Store China accounts, enabling wallet theft.
  headline: 26 FakeWallet Apps Found on Apple App Store Targeting Crypto Seed Phrases
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/26-fakewallet-apps-found-on-apple-app.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 26 FakeWallet Apps Found on Apple App Store Targeting Crypto Seed Phrases
updated_at: '2026-04-24T12:15:13.792713+00:00'
url_hash: 6ee8755e381c48729887d6e3baee2f8c6c7e4a6e
---

Cybersecurity researchers have discovered a set of malicious apps on the Apple App Store that impersonate popular cryptocurrency wallets in an attempt to steal recovery phrases and private keys since at least fall 2025.

"Once launched, these apps redirect users to browser pages designed to look similar to the App Store and distribute trojanized versions of legitimate wallets," Kaspersky researcher Sergey Puzan
[said](https://securelist.com/fakewallet-cryptostealer-ios-app-store/119474/)
. "The infected apps are specifically engineered to hijack recovery phrases and private keys."

The 26 apps, collectively dubbed
**FakeWallet**
, mimic various popular wallets like Bitpie, Coinbase, imToken, Ledger, MetaMask, TokenPocket, and Trust Wallet. Many of these apps have since been taken down by Apple following disclosure. There is no evidence that these apps were distributed via the Google Play Store.

While malicious cryptocurrency wallets
[distributed in the past](https://thehackernews.com/2022/03/experts-uncover-campaign-stealing.html)
via bogus websites have abused iOS provisioning profiles to get users to install them, the latest crypto-theft scheme is an improvement in several ways. For starters, the apps are directly available for download from Apple's App Store if a user has their Apple account set to China.

These apps have icons that mirror the original but have intentional typos in their names (e.g., LeddgerNew) so as to trick unsuspecting users into downloading them. In some cases, the app names and icons have no connection to cryptocurrency. Instead, they are used as placeholders to direct users to download the official wallet app through them, claiming they are "unavailable in the App Store" due to regulatory reasons.

Kaspersky said it also identified several similar apps likely linked to the same threat actor that do not have the malicious features enabled, but have been found to mimic a benign service, such as a game, a calculator, or a task planner. Once launched, these apps open a link on the web browser and leverage enterprise provisioning profiles to install the wallet app on the victim's device.

"The attackers have churned out a wide variety of malicious modules, each tailored to a specific wallet," Puzan said. "In most cases, the malware is delivered via a malicious library injection, though we've also come across builds where the app's original source code was modified."

The end goal of these infections is to look for mnemonic phrases from both hot and cold wallets, and exfiltrate them to an external server, allowing the operators to seize control of victims' wallets and drain cryptocurrency assets or initiate fraudulent transactions.

The seed phrases are captured either by hooking the code that's responsible for the screen where the user enters their recovery phrase or serving a phishing page that instructs the victim to enter their mnemonics as part of a supposed verification step.

It's suspected the campaign could be the work of threat actors linked to the
[SparkKitty trojan campaign](https://thehackernews.com/2025/07/mobile-security-alert-352-iconads-fraud.html)
last year, given that some of the infected apps also come with a module to steal wallet recovery phrases using optical character recognition (OCR), and that both the campaigns appear to be the work of native Chinese speakers and specifically target cryptocurrency assets.

"The FakeWallet campaign is gaining momentum by employing new tactics, ranging from delivering payloads via phishing apps published in the App Store to embedding themselves into cold wallet apps and using sophisticated phishing notifications to trick users into revealing their mnemonics," Kaspersky said.

### MiningDropper Android Malware Framework Emerges

The discovery comes as Cyble sheds light on a sophisticated Android malware delivery framework known as
**MiningDropper**
(aka BeatBanker) that combines cryptocurrency mining with information theft, remote access, and banking malware in attacks targeting users in India, as well as in Latin America, Europe, and Asia as part of a
[BTMOB RAT](https://thehackernews.com/2026/03/six-android-malware-families-target-pix.html)
campaign.

MiningDropper has been distributed via a trojanized version of the open-source Android application project
[Lumolight](https://github.com/BitMavrick/Lumolight)
, with the campaigns using fake websites impersonating banking institutions and regional transport offices to propagate the malware. Once launched, it activates a multi-stage sequence to extract the miner and the trojan payloads from an encrypted assets archive present within the package.

"MiningDropper employs a multi-stage payload delivery architecture that combines XOR-based native obfuscation, AES-encrypted payload staging, dynamic DEX loading, and anti-emulation techniques," Cyble
[said](https://cyble.com/blog/miningdropper-global-modular-android-malware/)
. "MiningDropper employs a multi-stage payload delivery architecture that combines XOR-based native obfuscation, AES-encrypted payload staging, dynamic DEX loading, and anti-emulation techniques."

"MiningDropper demonstrates a layered, modular Android malware architecture designed to make static analysis difficult while giving threat actors flexibility in final payload delivery. This design allows the threat actor to reuse the same distribution and installation framework across hundreds of samples while adapting the final monetization objective to operational needs."