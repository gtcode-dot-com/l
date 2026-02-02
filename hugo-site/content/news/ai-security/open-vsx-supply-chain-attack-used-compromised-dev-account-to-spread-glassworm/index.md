---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T06:15:14.933351+00:00'
exported_at: '2026-02-02T06:15:17.169071+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html
structured_data:
  about: []
  author: ''
  description: Open VSX supply chain attack hijacked VS Code extensions delivered
    GlassWorm malware stealing macOS, crypto, and developer data.
  headline: Open VSX Supply Chain Attack Used Compromised Dev Account to Spread GlassWorm
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/open-vsx-supply-chain-attack-used.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Open VSX Supply Chain Attack Used Compromised Dev Account to Spread GlassWorm
updated_at: '2026-02-02T06:15:14.933351+00:00'
url_hash: 7b98d71d8c17c3a09f33f416aca1fe9faedb9799
---

**

Ravie Lakshmanan
**

Feb 02, 2026

Developer Tools / Malware

Cybersecurity researchers have disclosed details of a supply chain attack targeting the Open VSX Registry in which unidentified threat actors compromised a legitimate developer's resources to push malicious updates to downstream users.

"On January 30, 2026, four established Open VSX extensions published by the oorzc author had malicious versions published to Open VSX that embed the GlassWorm malware loader," Socket security researcher Kirill Boychenko
[said](https://socket.dev/blog/glassworm-loader-hits-open-vsx-via-suspected-developer-account-compromise)
in a Saturday report.

"These extensions had previously been presented as legitimate developer utilities (some first published more than two years ago) and collectively accumulated over 22,000 Open VSX downloads prior to the malicious releases."

The supply chain security company
[said](https://github.com/oorzc/vscode_sync_tool/issues/25)
that the supply chain attack involved the compromise of the developer's publishing credentials, with the Open VSX security team assessing the incident as involving the use of either a leaked token or other unauthorized access. The malicious versions have since been removed from the Open VSX.

The list of identified extensions is below -

* FTP/SFTP/SSH Sync Tool (oorzc.ssh-tools — version 0.5.1)
* I18n Tools (oorzc.i18n-tools-plus — version 1.6.8)
* vscode mindmap (oorzc.mind-map — version 1.0.61)
* scss to css (oorzc.scss-to-css-compile — version 1.3.4)

The poisoned versions, Socket noted, are designed to deliver a loader malware associated with a known campaign called
[GlassWorm](https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html)
. The loader is equipped to decrypt and run embedded at runtime, uses an increasingly weaponized technique called EtherHiding to fetch command-and-control (C2) endpoints, and ultimately run code designed to steal Apple macOS credentials and cryptocurrency wallet data.

At the same time, the malware is detonated only after the compromised machine has been profiled, and it has been determined that it does not correspond to a Russian locale, a pattern commonly observed in malicious programs originating from or affiliated with Russian-speaking threat actors to avoid domestic prosecution.

The kinds of information harvested by the malware include -

* Data from Mozilla Firefox and Chromium-based browsers (logins, cookies, internet history, and wallet extensions like MetaMask)
* Cryptocurrency wallet files (Electrum, Exodus, Atomic, Ledger Live, Trezor Suite, Binance, and TonKeeper)
* iCloud Keychain database
* Safari cookies
* Data from Apple Notes
* user documents from Desktop, Documents, and Downloads folders
* FortiClient VPN configuration files
* Developer credentials (e.g., ~/.aws and ~/.ssh)

The targeting of developer information poses severe risks as it exposes enterprise environments to potential cloud account compromise and lateral movement attacks.

"The payload includes routines to locate and extract authentication material used in common workflows, including inspecting npm configuration for \_authToken and referencing GitHub authentication artifacts, which can provide access to private repositories, CI secrets, and release automation," Boychenko said.

A significant aspect of the attack is that it diverges from previously observed GlassWorm indicators in that it makes use of a compromised account belonging to a legitimate developer to distribute the malware. In prior instances, the threat actors behind the campaign have leveraged typosquatting and brandjacking to upload fraudulent extensions for subsequent propagation.

"The threat actor blends into normal developer workflows, hides execution behind encrypted, runtime-decrypted loaders, and uses Solana memos as a dynamic dead drop to rotate staging infrastructure without republishing extensions," Socket said. "These design choices reduce the value of static indicators and shift defender advantage toward behavioral detection and rapid response."