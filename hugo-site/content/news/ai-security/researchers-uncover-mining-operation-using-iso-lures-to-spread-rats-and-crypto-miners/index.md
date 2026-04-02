---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T14:15:14.317043+00:00'
exported_at: '2026-04-02T14:15:17.325644+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/researchers-uncover-mining-operation.html
structured_data:
  about: []
  author: ''
  description: REF1695 spreads RATs and miners since Nov 2023 via ISO lures, earning
    27.88 XMR across four wallets through cryptomining and CPA fraud.
  headline: Researchers Uncover Mining Operation Using ISO Lures to Spread RATs and
    Crypto Miners
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/researchers-uncover-mining-operation.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers Uncover Mining Operation Using ISO Lures to Spread RATs and Crypto
  Miners
updated_at: '2026-04-02T14:15:14.317043+00:00'
url_hash: f4c5ebc931fc54a25d4d608f85fcec327cade31d
---

**

Ravie Lakshmanan
**

Apr 02, 2026

Cryptomining / Malware

A financially motivated operation codenamed
**REF1695**
has been observed leveraging fake installers to deploy remote access trojans (RATs) and cryptocurrency miners since November 2023.

"Beyond cryptomining, the threat actor monetizes infections through CPA (Cost Per Action) fraud, directing victims to content locker pages under the guise of software registration," Elastic Security Labs researchers Jia Yu Chan, Cyril François, and Remco Sprooten
[said](https://www.elastic.co/security-labs/fake-installers-to-monero)
in an analysis published this week.

Recent iterations of the campaign have also been found to deliver a previously undocumented .NET implant codenamed CNB Bot. These attacks leverage an ISO file as the infection vector to deliver a .NET Reactor-protected loader and a text file with explicit instructions to the user to bypass Microsoft Defender SmartScreen protections against running unrecognized applications by clicking on "More info" and "Run anyway."

The loader is designed to invoke PowerShell, which is responsible for configuring broad Microsoft Defender Antivirus exclusions to fly under the radar and launch CNB Bot in the background. At the same time, the user is displayed an error message: "Unable to launch the application. Your system may not meet the required specifications. Please contact support."

CNB Bot functions as a loader with capabilities to download and execute additional payloads, update itself, and uninstall and perform cleanup actions to cover up the tracks. It communicates with a command-and-control (C2) server using HTTP POST requests.

Other campaigns mounted by the threat actor have leveraged similar ISO lures to deploy
[PureRAT](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html)
,
[PureMiner](https://thehackernews.com/2025/09/researchers-expose-svg-and-purerat.html)
, and a bespoke .NET-based XMRig loader, the last of which reaches out to a hard-coded URL to extract the mining configuration and launch the miner payload.

As recently observed in the
[FAUX#ELEVATE](https://thehackernews.com/2026/03/hackers-use-fake-resumes-to-steal.html)
campaign, "WinRing0x64.sys," a legitimate, signed, and vulnerable Windows kernel driver, is abused to obtain kernel-level hardware access and modify CPU settings to boost hash rates, thereby enabling performance improvement. The
[use of the driver](https://www.sophos.com/en-us/blog/mrbminer-cryptojacking-to-bypass-international-sanctions)
has been
[observed](https://www.morphisec.com/blog/proxyshellminer-campaign/)
in many
[cryptojacking campaigns](https://www.trellix.com/blogs/research/technical-deep-dive-the-monero-mining-campaign/)
over the years. The functionality was
[added to XMRig miners](https://github.com/xmrig/xmrig/blob/master/bin/WinRing0/WinRing0x64.sys)
in December 2019.

Elastic said it also identified another campaign that leads to the deployment of
[SilentCryptoMiner](https://thehackernews.com/2025/03/silentcryptominer-infects-2000-russian.html)
. The miner, besides using direct system calls to evade detection, takes steps to disable Windows Sleep and Hibernate modes, set up persistence via a scheduled task, and uses the "Winring0.sys" driver to fine-tune the CPU for mining operations.

Another notable component of the attack is a watchdog process that ensures the malicious artifacts and persistence mechanisms are restored in the event they are deleted. The campaign is estimated to have accrued 27.88 XMR ($9,392) across four tracked wallets, indicating that the operation is yielding consistent financial returns to the attacker.

"Beyond the C2 infrastructure, the threat actor abuses GitHub as a payload delivery CDN, hosting staged binaries across two identified accounts," Elastic said. "This technique shifts the download-and-execute step away from operator-controlled infrastructure to a trusted platform, reducing detection friction."