---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-23T00:03:17.716114+00:00'
exported_at: '2025-12-23T00:03:20.626415+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html
structured_data:
  about: []
  author: ''
  description: A malicious npm package posing as a WhatsApp API intercepts messages,
    steals credentials, and links attacker devices after 56,000 downloads.
  headline: Fake WhatsApp API Package on npm Steals Messages, Contacts, and Login
    Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/fake-whatsapp-api-package-on-npm-steals.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fake WhatsApp API Package on npm Steals Messages, Contacts, and Login Tokens
updated_at: '2025-12-23T00:03:17.716114+00:00'
url_hash: 09b34a526d4412f8220074cddf8438c608381d02
---

Cybersecurity researchers have disclosed details of a new malicious package on the npm repository that works as a fully functional WhatsApp API, but also contains the ability to intercept every message and link the attacker's device to a victim's WhatsApp account.

The package, named "
[lotusbail](https://www.npmjs.com/package/lotusbail)
," has been downloaded
[over 56,000 times](https://npm-stat.com/charts.html?package=lotusbail)
since it was first uploaded to the registry by a user named "seiren\_primrose" in May 2025. Of these, 711 downloads took place over the last week. The library is still available for download as of writing.

Under the cover of a functional tool, the malware "steals your WhatsApp credentials, intercepts every message, harvests your contacts, installs a persistent backdoor, and encrypts everything before sending it to the threat actor's server," Koi Security researcher Tuval Admoni
[said](https://www.koi.ai/blog/npm-package-with-56k-downloads-malware-stealing-whatsapp-messages)
in a report published over the weekend.

Specifically, it's equipped to capture authentication tokens and session keys, message history, contact lists with phone numbers, as well as media files and documents. More significantly, the library is inspired by
[@whiskeysockets/baileys](https://www.npmjs.com/package/@whiskeysockets/baileys)
, a legitimate WebSockets-based TypeScript library for interacting with the WhatsApp Web API.

This is accomplished by means of a malicious WebSocket wrapper through which authentication information and messages are routed, thereby allowing it to capture credentials and chats. The stolen data is transmitted to an attacker-controlled URL in encrypted form.

The attack doesn't stop there, for the package also harbors covert functionality to create persistent access to the victim's WhatsApp account by hijacking the
[device linking process](https://thehackernews.com/2025/12/threatsday-bulletin-whatsapp-hijacks.html#whatsapp-hijack-campaign)
by using a hard-coded pairing code.

"When you use this library to authenticate, you're not just linking your application -- you're also linking the threat actor's device," Admoni said. "They have complete, persistent access to your WhatsApp account, and you have no idea they're there."

By linking their device to the target's WhatsApp, it not only allows continued access to their contacts and conversations but also enables persistent access even after the package is uninstalled from the system, given the threat actor's device remains linked to the WhatsApp account until it's unlinked by navigating to the app's settings.

Koi Security's Idan Dardikman told The Hacker News that the malicious activity is triggered when the developer uses the library to connect to WhatsApp.

"The malware wraps the WebSocket client, so once you authenticate and start sending/receiving messages, the interception kicks in," Dardikman said. "No special function needed beyond normal usage of the API. The backdoor pairing code also activates during the authentication flow – so the attacker's device gets linked the moment you connect your app to WhatsApp."

Furthermore, "lotusbail" comes fitted with anti-debugging capabilities that cause it to enter into an infinite loop trap when debugging tools are detected, causing it to freeze execution.

"Supply chain attacks aren't slowing down – they're getting better," Koi said. "Traditional security doesn't catch this. Static analysis sees working WhatsApp code and approves it. Reputation systems have seen 56,000 downloads, and trust it. The malware hides in the gap between 'this code works' and 'this code only does what it claims.'"

### Malicious NuGet Packages Target the Crypto Ecosystem

The disclosure comes as ReversingLabs
[shared](https://www.reversinglabs.com/blog/nuget-malware-crypto-oauth-tokens)
details of 14 malicious NuGet packages that impersonate Nethereum, a .NET integration library for the Ethereum decentralized blockchain, and other cryptocurrency-related tools to redirect transaction funds to attacker-controlled wallets when the transfer amount exceeded $100 or exfiltrate private keys and seed phrases.

The names of the packages, published from eight different accounts, are listed below -

* binance.csharp
* bitcoincore
* bybitapi.net
* coinbase.net.api
* googleads.api
* nbitcoin.unified
* nethereumnet
* nethereumunified
* netherеum.all
* solananet
* solnetall
* solnetall.net
* solnetplus
* solnetunified

The packages have leveraged several techniques to lull users into a false sense of trust in security, including inflating download counts and publishing dozens of new versions in a short amount of time to give the impression that it's being actively maintained. The campaign dates all the way back to July 2025.

The malicious functionality is injected such that it's only triggered when the packages are installed by developers and specific functions are embedded into other applications. Notable among the packages is GoogleAds.API, which focuses on stealing Google Ads OAuth information instead of exfiltrating wallet data secrets.

"These values are highly sensitive, because they allow full programmatic access to a Google Ads account and, if leaked, attackers can impersonate the victim's advertising client, read all campaign and performance data, create or modify ads, and even spend unlimited funds on a malicious or fraudulent campaign," ReversingLabs said.