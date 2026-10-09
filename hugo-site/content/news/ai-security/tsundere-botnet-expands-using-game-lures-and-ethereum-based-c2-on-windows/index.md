---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-21T00:00:08.075094+00:00'
exported_at: '2025-11-21T00:00:10.886316+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html
structured_data:
  about: []
  author: ''
  description: Tsundere botnet spreads via MSI and PowerShell installers, using Ethereum-based
    C2 rotation and game-themed lures to target Windows users.
  headline: Tsundere Botnet Expands Using Game Lures and Ethereum-Based C2 on Windows
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Tsundere Botnet Expands Using Game Lures and Ethereum-Based C2 on Windows
updated_at: '2025-11-21T00:00:08.075094+00:00'
url_hash: 10305ca438e0a675b47842d00244728936aa9124
---

Cybersecurity researchers have warned of an actively expanding botnet dubbed
**Tsundere**
that's targeting Windows users.

Active since mid-2025, the threat is
[designed](https://securelist.com/tsundere-node-js-botnet-uses-ethereum-blockchain/117979/)
to execute arbitrary JavaScript code retrieved from a command-and-control (C2) server, Kaspersky researcher Lisandro Ubiedo said in an analysis published today.

There are currently no details on how the botnet malware is propagated; however, in at least one case, the threat actors behind the operation are said to have leveraged a legitimate Remote Monitoring and Management (RMM) tool as a conduit to download an MSI installer file from a compromised site.

The names given to the malware artifacts – Valorant, r6x (Rainbow Six Siege X), and cs2 (Counter-Strike 2) – also suggest that the implant is likely being disseminated using lures for games. It's possible that users searching for pirated versions of these games are the target.

Regardless of the method used, the fake MSI installer is designed to install Node.js and launch a loader script that's responsible for decrypting and executing the main botnet-related payload. It also prepares the environment by downloading three legitimate libraries, namely, ws, ethers, and pm2, using an "npm install" command.

"The pm2 package is installed to ensure the Tsundere bot remains active and used to launch the bot," Ubiedo explained. "Additionally, pm2 helps achieve persistence on the system by writing to the registry and configuring itself to restart the process upon login."

Kaspersky's analysis of the C2 panel has revealed that the malware is also propagated in the form of a PowerShell script, which performs a similar sequence of actions by deploying Node.js on the compromised host and downloading ws and ethers as dependencies.

While the PowerShell infector doesn't make use of pm2, it carries out the same actions observed in the MSI installer by creating a registry key value that ensures the bot is executed on each login by spawning a new instance of itself.

The Tsundere botnet makes
[use of the Ethereum blockchain](https://thehackernews.com/2025/10/hackers-abuse-blockchain-smart.html)
to
[fetch details](https://thehackernews.com/2025/11/malicious-vsx-extension-sleepyduck-uses.html)
of the WebSocket C2 server (e.g., ws://193.24.123[.]68:3011 or ws://185.28.119[.]179:1234), creating a resilient mechanism that allows the attackers to
[rotate the infrastructure](https://etherscan.io/tx/0x834769584d0305b7517aea4f17d3382e68e86b535c190bba51d56981c83a4705)
simply by employing a
[smart contract](https://etherscan.io/address/0xa1b40044EBc2794f207D45143Bd82a1B86156c6b)
. The contract was created on September 23, 2024, and has had 26 transactions to date.

Once the C2 address is retrieved, it checks to ensure it is a valid WebSocket URL, and then proceeds to establish a WebSocket connection with the specific address and receive JavaScript code sent by the server. Kaspersky said it did not observe any follow-up commands from the server during the observation period.

"The ability to evaluate code makes the Tsundere bot relatively simple, but it also provides flexibility and dynamism, allowing the botnet administrators to adapt it to a wide range of actions," Kaspersky said.

The botnet operations are facilitated by a control panel that allows logged-in users to build new artifacts using MSI or PowerShell, manage administrative functions, view the number of bots at any given point of time, turn their bots into a proxy for routing malicious traffic, and even browse and purchase botnets via a dedicated marketplace.

Exactly who is behind Tsundere is not known, but the presence of the Russian language in the source code for logging purposes alludes to a threat actor who is Russian-speaking. The activity is assessed to share functional overlaps with a malicious npm campaign
[documented](https://thehackernews.com/2024/11/malware-campaign-uses-ethereum-smart.html)
by Checkmarx, Phylum, and Socket in November 2024.

What's more, the same server has been identified as hosting the C2 panel associated with an information stealer known as 123 Stealer, which is available on a subscription basis for $120 per month. It was first advertised by a threat actor named "koneko" on a dark web forum on June 17, 2025, per
[Outpost24's KrakenLabs Team](https://x.com/KrakenLabs_Team/status/1940756956156666349)
.

Another clue that points to its Russian origins is that the customers are forbidden from using the stealer to target Russia and the Commonwealth of Independent States (CIS) countries. "Violation of this rule will result in the immediate blocking of your account without explanation," Koneko said in the post at the time.

"Infections can occur through MSI and PowerShell files, which provide flexibility in terms of disguising installers, using phishing as a point of entry, or integrating with other attack mechanisms, making it an even more formidable threat," Kaspersky said.