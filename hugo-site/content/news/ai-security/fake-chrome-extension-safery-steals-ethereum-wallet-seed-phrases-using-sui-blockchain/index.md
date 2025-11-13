---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T20:21:02.069123+00:00'
exported_at: '2025-11-13T20:21:04.180723+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/fake-chrome-extension-safery-steals.html
structured_data:
  about: []
  author: ''
  description: A fake Chrome wallet “Safery” is stealing Ethereum seed phrases using
    hidden Sui blockchain transactions.
  headline: Fake Chrome Extension “Safery” Steals Ethereum Wallet Seed Phrases Using
    Sui Blockchain
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/fake-chrome-extension-safery-steals.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fake Chrome Extension “Safery” Steals Ethereum Wallet Seed Phrases Using Sui
  Blockchain
updated_at: '2025-11-13T20:21:02.069123+00:00'
url_hash: 67cf8454d36dd3c0fc08562a8c05ef7ae7e43290
---

**

Nov 13, 2025
**

Ravie Lakshmanan

Browser Security / Threat Intelligence

Cybersecurity researchers have uncovered a malicious Chrome extension that poses as a legitimate Ethereum wallet but harbors functionality to exfiltrate users' seed phrases.

The name of the extension is "Safery: Ethereum Wallet," with the threat actor describing it as a "secure wallet for managing Ethereum cryptocurrency with flexible settings." It was uploaded to the Chrome Web Store on September 29, 2025, and was updated as recently as November 12. It's still
[available for download](https://chromewebstore.google.com/detail/safery-ethereum-wallet/fibemlnkopkeenmmgcfohhcdbkhgbolo)
as of writing.

"Marketed as a simple, secure Ethereum (ETH) wallet, it contains a backdoor that exfiltrates seed phrases by encoding them into Sui addresses and broadcasting microtransactions from a threat actor-controlled Sui wallet," Socket security researcher Kirill Boychenko
[said](https://socket.dev/blog/malicious-chrome-extension-exfiltrates-seed-phrases)
.

Specifically, the malware present within the browser add-on is designed to steal wallet mnemonic phrases by encoding them as fake Sui wallet addresses and then using micro-transactions to send 0.000001 SUI to those wallets from a hard-coded threat actor-controlled wallet.

The end goal of the malware is to smuggle the seed phrase inside normal looking blockchain transactions without the need for setting up a command-and-control (C2) server to receive the information. Once the transactions are complete, the threat actor can decode the recipient addresses to reconstruct the original seed phrase and ultimately drain assets from it.

"This extension steals wallet seed phrases by encoding them as fake Sui addresses and sending micro-transactions to them from an attacker-controlled wallet, allowing the attacker to monitor the blockchain, decode the addresses back to seed phrases, and drain victims' funds," Koi Security
[notes](https://dex.koi.security/reports/chrome/fibemlnkopkeenmmgcfohhcdbkhgbolo/1.6)
in an analysis.

To counter the risk posed by the threat, users are advised to stick to trusted wallet extensions. Defenders are recommended to scan extensions for mnemonic encoders, synthetic address generators, and hard-coded seed phrases, as well as block those that write on the chain during wallet import or creation.

"This technique lets threat actors switch chains and RPC endpoints with little effort, so detections that rely on domains, URLs, or specific extension IDs will miss it," Boychenko said. "Treat unexpected blockchain RPC calls from the browser as high signal, especially when the product claims to be single chain."