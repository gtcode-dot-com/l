---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-26T12:00:08.243825+00:00'
exported_at: '2025-11-26T12:00:10.746363+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/chrome-extension-caught-injecting.html
structured_data:
  about: []
  author: ''
  description: esearchers uncover Crypto Copilot, a Chrome extension that injects
    secret Solana transfer fees into Raydium swaps.
  headline: Chrome Extension Caught Injecting Hidden Solana Transfer Fees Into Raydium
    Swaps
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/chrome-extension-caught-injecting.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Chrome Extension Caught Injecting Hidden Solana Transfer Fees Into Raydium
  Swaps
updated_at: '2025-11-26T12:00:08.243825+00:00'
url_hash: 1085708230d0413afd7613feef7d9104b17f4594
---

**

Nov 26, 2025
**

Ravie Lakshmanan

Browser Security / Cryptocurrency

Cybersecurity researchers have discovered a new malicious extension on the Chrome Web Store that's capable of injecting a stealthy Solana transfer into a swap transaction and transferring the funds to an attacker-controlled cryptocurrency wallet.

The extension, named
[Crypto Copilot](https://chromewebstore.google.com/detail/crypto-copilot/iaemdpdnmdkaphnmcogmcgcmhhafcifd)
, was
[first published](https://dex.koi.security/reports/chrome/iaemdpdnmdkaphnmcogmcgcmhhafcifd/1.1.0)
by a user named "sjclark76" on May 7, 2024. The developer describes the browser add-on as offering the ability to "trade crypto directly on X with real-time insights and seamless execution." The extension has 12 installs and remains available for download as of writing.

"Behind the interface, the extension injects an extra transfer into every Solana swap, siphoning a minimum of 0.0013 SOL or 0.05% of the trade amount to a hardcoded attacker-controlled wallet," Socket security researcher Kush Pandya
[said](https://socket.dev/blog/malicious-chrome-extension-injects-hidden-sol-fees-into-solana-swaps)
in a Tuesday report.

Specifically, the extension incorporates obfuscated code that comes to life when a user performs a Raydium swap, manipulating it to inject an undisclosed SOL transfer into the same signed transaction. Raydium is a decentralized exchange (DEX) and automated market maker (AMM) built on the Solana blockchain.

It works by appending a hidden
[SystemProgram.transfer](https://solana-foundation.github.io/solana-web3.js/classes/SystemProgram.html#transfer)
util method to each swap before the user's signature is requested, and sends the fee to a
[hard-coded wallet](https://solscan.io/account/Bjeida13AjgPaUEU9xrh1iQMwxZC7QDdvSfg73oxQff7)
embedded in the code. The fee is calculated based on the amount traded, charging a minimum of 0.0013 SOL for trades and 2.6 SOL and 0.05% of the swap amount if it's more than 2.6 SOL. To avoid detection, the malicious behavior is concealed using techniques like
[minification](https://en.wikipedia.org/wiki/Minification_(programming))
and variable renaming.

The extension also communicates with a backend hosted on the domain "crypto-coplilot-dashboard.vercel[.]app" to register connected wallets, fetch points and referral data, and report user activity. The domain, along with "cryptocopilot[.]app," does not host any real product.

What's notable about the attack is that users are completely kept in the dark about the hidden platform fee, and the user interface only shows details of the swap. Furthermore, Crypto Copilot makes use of legitimate services like DexScreener and Helius RPC to lend it a veneer of trust.

"Because this transfer is added silently and sent to a personal wallet rather than a protocol treasury, most users will never notice it unless they inspect each instruction before signing," Pandya said. "The surrounding infrastructure appears designed only to pass Chrome Web Store review and provide a veneer of legitimacy while siphoning fees in the background."