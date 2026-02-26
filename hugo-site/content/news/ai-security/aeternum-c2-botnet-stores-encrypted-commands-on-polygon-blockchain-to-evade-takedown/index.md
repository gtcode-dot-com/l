---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-26T20:15:13.591824+00:00'
exported_at: '2026-02-26T20:15:15.791252+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/aeternum-c2-botnet-stores-encrypted.html
structured_data:
  about: []
  author: ''
  description: Researchers detail Aeternum C2 storing botnet commands on Polygon blockchain,
    while DSLRoot operates 300 residential proxy devices across U.S.
  headline: Aeternum C2 Botnet Stores Encrypted Commands on Polygon Blockchain to
    Evade Takedown
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/aeternum-c2-botnet-stores-encrypted.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Aeternum C2 Botnet Stores Encrypted Commands on Polygon Blockchain to Evade
  Takedown
updated_at: '2026-02-26T20:15:13.591824+00:00'
url_hash: f19c319fe3c605f5c7c8fe69764e0089b3b15198
---

Cybersecurity researchers have disclosed details of a new botnet loader called
**Aeternum C2**
that uses a blockchain-based command-and-control (C2) infrastructure to make it resilient to takedown efforts.

"Instead of relying on traditional servers or domains for command-and-control, Aeternum stores its instructions on the public Polygon blockchain," Qrator Labs
[said](https://qrator.net/blog/details/Exploring-Aeternum-C2/)
in a report shared with The Hacker News.

"This network is widely used by decentralized applications, including Polymarket, the world's largest prediction market. This approach makes Aeternum's C2 infrastructure effectively permanent and resistant to traditional takedown methods."

This is not the first time botnets have been found relying on blockchain for C2. In 2021, Google said it took steps to disrupt a botnet known as
[Glupteba](https://thehackernews.com/2024/02/glupteba-botnet-evades-detection-with.html)
that uses the Bitcoin blockchain as a backup C2 mechanism to fetch the actual C2 server address.

Details of Aeternum C2 first emerged in December 2025, when Outpost24's KrakenLabs
[revealed](https://x.com/KrakenLabs_Team/status/1998330973461622894)
that a threat actor by the name of LenAI was advertising the malware on underground forums for $200 that grants customers access to a panel and a configured build. For $4,000, customers were allegedly promised the entire C++ codebase along with updates.

A native C++ loader available in both x32 and x64 builds, the malware works by writing commands to be issued to the infected host to smart contracts on the Polygon blockchain. The bots then read those commands by querying public remote procedure call (RPC) endpoints.

All of this is managed via the web-based panel, from where customers can select a smart contract, choose a command type, specify a payload URL and update it. The command, which can target all endpoints or a specific one, is written into the blockchain as a transaction, after which it becomes available to every compromised device that's polling the network.

"Once a command is confirmed, it cannot be altered or removed by anyone other than the wallet holder," Qrator Labs said. "The operator can manage multiple smart contracts simultaneously, each one potentially serving a different payload or function, such as a clipper, a stealer, a RAT, or a miner."

According to a
[two-part research](https://ctrlaltintel.com/threat%20research/Aeternum-Part-1/)
published by
[Ctrl Alt Intel](https://ctrlaltintel.com/threat%20research/Aeternum-Part-2/)
earlier this month, the C2 panel is implemented as a Next.js web application that allows operators to deploy smart contracts to the Polygon blockchain. The smart contracts contain a function that, when called by the malware via the Polygon RPC, causes it to return the encrypted command that's subsequently decoded and run on the victim machines.

Besides using the blockchain to turn it into a takedown-resistant botnet, the malware packs in various anti-analysis features to extend the lifespan of infections. This includes checks to detect virtualized environments, in addition to equipping customers with the ability to scan their builds via
[Kleenscan](https://kleenscan.com/index)
to ensure that they are not flagged by antivirus vendors.

"The operational costs are negligible: $1 worth of MATIC, the native token of the Polygon network, is enough for 100 to 150 command transactions," the Czechian cybersecurity vendor said. "The operator doesn't need to rent servers, register domains, or maintain any infrastructure beyond a crypto wallet and a local copy of the panel."

The threat actor has since
[attempted to sell the entire toolkit](https://x.com/KrakenLabs_Team/status/2024872751266148544)
for an asking price of $10,000, claiming a lack of time for support and their involvement in another project. "I will sell the entire project to one person with permission for resale and commercial use, with all 'rights,'" LenAI said. "I will also give useful tips/notes on development that I did not have time to implement."

It's worth noting that LenAI is also behind a second crimeware solution called
[ErrTraffic](https://thehackernews.com/2026/01/threatsday-bulletin-ghostad-drain-macos.html#fake-glitch-scam-toolkit-exposed)
that enables threat actors to automate ClickFix attacks by generating fake glitches on compromised websites to induce a false sense of urgency and deceive users into following malicious instructions.

The disclosure comes as Infrawatch published details of an underground service that deploys dedicated laptop hardware into American homes to co-opt the devices into a residential proxy network named DSLRoot that redirects malicious traffic through them.

The hardware is designed to run a Delphi-based program called DSLPylon that's equipped with capabilities to enumerate supported modems on the network, as well as remotely control the residential networking equipment and Android devices via an Android Debug Bridge (
[ADB](https://thehackernews.com/2026/01/kimwolf-android-botnet-infects-over-2.html)
) integration.

"Attribution analysis identifies the operator as a Belarusian national with residential presence in Minsk and Moscow," Infrawatch
[said](https://infrawatch.com/blog/dslroot-us-proxy-investigation)
. "DSLRoot is estimated to operate roughly 300 active hardware devices across 20+ U.S. states."

The operator has been identified as Andrei Holas (aka Andre Holas and Andrei Golas), with the service promoted on BlackHatWorld by a user operating under the alias GlobalSolutions, claiming to offer physical residential ADSL proxies for sale for $190 per month for unrestricted access. It is also available for $990 for six months and $1,750 for annual subscriptions.

"DSLRoot's custom software provides automated remote management of consumer modems (ARRIS/Motorola, Belkin, D-Link, ASUS) and Android devices via ADB, enabling IP address rotation and connectivity control," the company noted. "The network operates without authentication, allowing clients to route traffic anonymously through U.S. residential IPs."