---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-03T00:03:08.083172+00:00'
exported_at: '2025-12-03T00:03:10.835393+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html
structured_data:
  about: []
  author: ''
  description: GlassWorm spreads again using 24 fake extensions across Visual Studio
    Marketplace and Open VSX, hiding Rust implants & Solana-based C2 to target devs.
  headline: GlassWorm Returns with 24 Malicious Extensions Impersonating Popular Developer
    Tools
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: GlassWorm Returns with 24 Malicious Extensions Impersonating Popular Developer
  Tools
updated_at: '2025-12-03T00:03:08.083172+00:00'
url_hash: 68d996d9e85d44c195383eca3e3a699cb0d2b0af
---

**

Dec 02, 2025
**

Ravie Lakshmanan

Malware / Blockchain

The supply chain campaign known as
[GlassWorm](https://secureannex.com/blog/glassworm-continued/)
has once again reared its head, infiltrating both Microsoft Visual Studio Marketplace and Open VSX with 24 extensions impersonating popular developer tools and frameworks like Flutter, React, Tailwind, Vim, and Vue.

GlassWorm was
[first documented](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html)
in October 2025, detailing its use of the Solana blockchain for command-and-control (C2) and harvest npm, Open VSX, GitHub, and Git credentials, drain cryptocurrency assets from dozens of wallets, and turn developer machines into attacker-controlled nodes for other criminal activities.

The most crucial aspect of the campaign is the abuse of the stolen credentials to compromise additional packages and extensions, thereby spreading the malware like a worm. Despite
[continued efforts](https://thehackernews.com/2025/10/eclipse-foundation-revokes-leaked-open.html)
of Microsoft and Open VSX, the malware
[resurfaced](https://thehackernews.com/2025/11/glassworm-malware-discovered-in-three.html)
a second time last month, and the attackers were
[observed](https://thehackernews.com/2025/11/weekly-recap-lazarus-hits-web3-intelamd.html#:~:text=12%20Malicious%20VS%20Code%20Extensions%20Flagged)
targeting GitHub repositories.

The latest wave of the GlassWorm campaign, spotted by Secure Annex's John Tuckner, involves a total of 24 extensions spanning both repositories. The list of identified extensions is below -

VS Code Marketplace:

* iconkieftwo.icon-theme-materiall
* prisma-inc.prisma-studio-assistance (
  [removed](https://github.com/microsoft/vsmarketplace/blob/main/RemovedPackages.md)
  as of December 1, 2025)
* prettier-vsc.vsce-prettier
* flutcode.flutter-extension
* csvmech.csvrainbow
* codevsce.codelddb-vscode
* saoudrizvsce.claude-devsce
* clangdcode.clangd-vsce
* cweijamysq.sync-settings-vscode
* bphpburnsus.iconesvscode
* klustfix.kluster-code-verify
* vims-vsce.vscode-vim
* yamlcode.yaml-vscode-extension
* solblanco.svetle-vsce
* vsceue.volar-vscode
* redmat.vscode-quarkus-pro
* msjsdreact.react-native-vsce

Open VSX:

* bphpburn.icons-vscode
* tailwind-nuxt.tailwindcss-for-react
* flutcode.flutter-extension
* yamlcode.yaml-vscode-extension
* saoudrizvsce.claude-dev
* saoudrizvsce.claude-devsce
* vitalik.solidity

The attackers have been found to artificially inflate the download counts to make the extensions appear trustworthy and cause them to prominently appear in search results, often in close proximity to the actual projects they impersonate to deceive developers into installing them.

"Once the extension has been approved initially, the attacker seems to easily be able to update code with a new malicious version and easily evade filters," Tuckner said. "Many code extensions begin with an 'activate' context, and the malicious code is slipped in right after the activation occurs."

The new iteration, while still relying on the invisible Unicode trick, is characterized by the use of Rust-based implants that are packaged inside the extensions. In an
[analysis](https://www.nextron-systems.com/2025/11/28/malicious-vs-code-extension-impersonating-material-icon-theme-found-in-marketplace/)
of the "icon-theme-materiall" extension, Nextron Systems said it comes with
[two Rust implants](https://www.nextron-systems.com/2025/11/29/analysis-of-the-rust-implants-found-in-the-malicious-vs-code-extension/)
that are capable of targeting Windows and macOS systems -

* A Windows DLL named os.node
* A macOS dynamic library named darwin.node

As observed in the previous GlassWorm infections, the implants are designed to fetch details of the C2 server from a Solana blockchain wallet address and use it to download the next-stage payload, an encrypted JavaScript file. As a backup, they can parse a Google Calendar event to fetch the C2 address.

"Rarely does an attacker publish 20+ malicious extensions across both of the most popular marketplaces in a week," Tuckner said in a statement. "Many developers could easily be fooled by these extensions and are just one click away from compromise."