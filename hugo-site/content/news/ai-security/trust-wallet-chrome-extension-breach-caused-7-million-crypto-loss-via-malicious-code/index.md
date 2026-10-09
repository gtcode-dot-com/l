---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-27T00:03:14.176673+00:00'
exported_at: '2025-12-27T00:03:16.752949+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html
structured_data:
  about: []
  author: ''
  description: Trust Wallet says a security incident in its Chrome extension v2.68
    caused about $7M in crypto losses and urges users to update to v2.69.
  headline: Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via
    Malicious Code
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/trust-wallet-chrome-extension-bug.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Trust Wallet Chrome Extension Breach Caused $7 Million Crypto Loss via Malicious
  Code
updated_at: '2025-12-27T00:03:14.176673+00:00'
url_hash: 75635303250f722882936da943d1cf54ca02bd7d
---

**

Dec 26, 2025
**

Ravie Lakshmanan

Cryptocurrency / Incident Response

Trust Wallet is
[urging](https://x.com/TrustWallet/status/2004475085168795941)
users to update its Google Chrome extension to the latest version following what it described as a "security incident" that led to the loss of approximately $7 million.

The issue, the multi‑chain, non‑custodial cryptocurrency wallet service said, impacts version 2.68. The extension has about one million users, according to the Chrome Web Store listing. Users are advised to update to
[version 2.69](https://chromewebstore.google.com/detail/trust-wallet/egjidjbpglichdcondbcbdnbeeppgdph)
as soon as possible.

"We've confirmed that approximately $7M has been impacted and we will ensure all affected users are refunded," Trust Wallet said in a post on X. "Supporting affected users is our top priority, and we are actively finalizing the process to refund the impacted users."

Trust Wallet is also urging users to refrain from interacting with any messages that do not come from its official channels. Mobile-only users and all other browser extension versions are not affected.

According to details shared by SlowMist, version 2.68 introduced malicious code that's designed to iterate through all wallets stored in the extension and trigger a mnemonic phrase request for each wallet.

"The encrypted mnemonic is then decrypted using the password or passkeyPassword entered during wallet unlock," the blockchain security firm
[said](https://x.com/SlowMist_Team/status/2004505094646345905)
. "Once decrypted, the mnemonic phrase is sent to the attacker's server api.metrics-trustwallet[.]com."

The domain "metrics-trustwallet[.]com" was registered on December 8, 2025, with the first request to "api.metrics-trustwallet[.]com" commencing on December 21, 2025.

Further analysis has revealed that the attacker has leveraged an open‑source full‑chain analytics library named posthog-js to harvest wallet user information.

The digital assets drained so far include about $3 million in Bitcoin, $431 in Solana, and more than $3 million in Ethereum. The stolen funds have been
[moved through](https://x.com/PeckShieldAlert/status/2004382831158714735)
centralized exchanges and cross-chain bridges for laundering and swapping. According to an update shared by blockchain investigator ZachXBT, the incident has
[claimed](https://t.me/investigations/297)
hundreds of victims.

"While ~$2.8 million of the stolen funds remain in the hacker's wallets (Bitcoin/ EVM/ Solana), the bulk – >$4M in cryptos – has been sent to CEXs [centralized exchanges]: ~$3.3 million to ChangeNOW, ~$340,000 to FixedFloat, and ~$447,000 to KuCoin," PeckShield
[said](https://x.com/PeckShieldAlert/status/2004382831158714735)
.

"This backdoor incident originated from malicious source code modification within the internal Trust Wallet extension codebase (analytics logic), rather than an injected compromised third‑party dependency (e.g., malicious npm package)," SlowMist said.

"The attacker directly tampered with the application's own code, then leveraged the legitimate PostHog analytics library as the data‑exfiltration channel, redirecting analytic traffic to an attacker‑controlled server."

The company said there is a possibility that it's the work of a nation-state actor, adding the attackers may have gained control of Trust Wallet‑related developer devices or obtained deployment permissions prior to December 8, 2025.

Changpeng Zhao, a co-founder of crypto exchange Binance, which owns the utility,
[hinted that](https://x.com/cz_binance/status/2004398433285894432)
the exploit was "most likely" carried out by an insider, although no further evidence was provided to support the theory.