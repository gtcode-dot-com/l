---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-10T14:15:13.688869+00:00'
exported_at: '2026-04-10T14:15:16.082362+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html
structured_data:
  about: []
  author: ''
  description: GlassWorm uses a fake WakaTime VS Code extension to infect IDEs, deploy
    RATs, and steal data, prompting urgent credential rotation.
  headline: GlassWorm Campaign Uses Zig Dropper to Infect Multiple Developer IDEs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/glassworm-campaign-uses-zig-dropper-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: GlassWorm Campaign Uses Zig Dropper to Infect Multiple Developer IDEs
updated_at: '2026-04-10T14:15:13.688869+00:00'
url_hash: 84122a9348d67268a18fbb29145afd3cf00c5b98
---

**

Ravie Lakshmanan
**

Apr 10, 2026

Malware / Blockchain

Cybersecurity researchers have flagged yet another evolution of the ongoing
**[GlassWorm](https://thehackernews.com/2026/03/glassworm-malware-uses-solana-dead.html)**
campaign, which employs a new Zig dropper that's designed to stealthily infect all integrated development environments (IDEs) on a developer's machine.

The technique has been discovered in an Open VSX extension named "
[specstudio.code-wakatime-activity-tracker](https://open-vsx.org/extension/specstudio/code-wakatime-activity-tracker)
," which masquerades as WakaTime, a popular tool that measures the time programmers spend inside their IDE. The extension is no longer available for download.

"The extension [...] ships a Zig-compiled native binary alongside its JavaScript code," Aikido Security researcher Ilyas Makari
[said](https://www.aikido.dev/blog/glassworm-zig-dropper-infects-every-ide-on-your-machine)
in an analysis published this week.

"This is not the first time
[GlassWorm](https://thehackernews.com/2025/12/glassworm-returns-with-24-malicious.html)
has resorted to using
[native compiled code](https://www.koi.ai/blog/glassworm-goes-native-same-infrastructure-hardened-delivery)
in extensions. However, rather than using the binary as the payload directly, it is used as a stealthy indirection for the known GlassWorm dropper, which now secretly infects all other IDEs it can find on your system."

The newly identified Microsoft Visual Studio Code (VS Code) extension is a near replica of WakaTime, save for a change introduced in a function named "activate()." The extension installs a binary named "win.node" on Windows systems and "mac.node," a universal Mach-O binary if the system is running Apple macOS.

These Node.js native addons are compiled shared libraries that are written in Zig and load directly into Node's runtime and execute outside the JavaScript sandbox with full operating system-level access.

Once loaded, the primary goal of the binary is to find every IDE on the system that supports VS Code extensions. This includes Microsoft VS Code and VS Code Insiders, as well as forks like VSCodium, Positron, and a number of artificial intelligence (AI)-powered coding tools like Cursor and Windsurf.

The binary then downloads a malicious VS Code extension (.VSIX) from an attacker-controlled
[GitHub account](https://github.com/ColossusQuailPray)
. The extension – called "floktokbok.autoimport" – impersonates "
[steoates.autoimport](https://marketplace.visualstudio.com/items?itemName=steoates.autoimport)
," a legitimate extension with more than 5 million installs on the official Visual Studio Marketplace.

In the final step, the downloaded .VSIX file is written to a temporary path and silently installed into every IDE using each editor's CLI installer. The second-stage VS Code extension
[acts as a dropper](https://thehackernews.com/2026/03/glassworm-malware-uses-solana-dead.html)
that avoids execution on Russian systems, talks to the Solana blockchain to fetch the command-and-control (C2) server, exfiltrates sensitive data, and installs a remote access trojan (RAT), which ultimately deploys an information-stealing Google Chrome extension.

Users who have installed "specstudio.code-wakatime-activity-tracker" or "floktokbok.autoimport" are advised to assume compromise and rotate all secrets.