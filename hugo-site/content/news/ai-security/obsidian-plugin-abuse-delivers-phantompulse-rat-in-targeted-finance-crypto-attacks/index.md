---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-16T12:15:14.293422+00:00'
exported_at: '2026-04-16T12:15:16.732067+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html
structured_data:
  about: []
  author: ''
  description: PHANTOMPULSE spreads via Obsidian plugin abuse in REF6598 campaign,
    targeting finance and crypto users, bypassing AV controls.
  headline: Obsidian Plugin Abuse Delivers PHANTOMPULSE RAT in Targeted Finance, Crypto
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Obsidian Plugin Abuse Delivers PHANTOMPULSE RAT in Targeted Finance, Crypto
  Attacks
updated_at: '2026-04-16T12:15:14.293422+00:00'
url_hash: bcce6c30998012f84673b616a6c220cccaa0ca17
---

**

Ravie Lakshmanan
**

Apr 16, 2026

Application Security / Threat Intelligence

A "novel" social engineering campaign has been observed abusing Obsidian, a cross-platform note-taking application, as an initial access vector to distribute a previously undocumented Windows remote access trojan called PHANTOMPULSE in attacks targeting individuals in the financial and cryptocurrency sectors.

Dubbed
[**REF6598**](https://www.elastic.co/security-labs/phantom-in-the-vault)
by Elastic Security Labs, the activity has been found to leverage elaborate social engineering tactics through LinkedIn and Telegram to breach both Windows and macOS systems, approaching prospective individuals under the guise of a venture capital firm and then moving the conversation to a Telegram group where several purported partners are present.

The Telegram group chat is engineered to lend the operation a smidgen of credibility, with the members discussing topics related to financial services and cryptocurrency liquidity solutions. The target is then instructed to use Obsidian to access what appears to be a shared dashboard by connecting to a
[cloud-hosted vault](https://obsidian.md/help/vault)
using the credentials provided to them.

It's this vault that triggers the infection sequence. As soon as the vault is opened in the note-taking application, the target is asked to enable "Installed community plugins" sync, effectively causing malicious code to be executed.

"The threat actors abuse Obsidian's legitimate community plugin ecosystem, specifically the
[Shell Commands](https://github.com/Taitava/obsidian-shellcommands)
and
[Hider](https://github.com/kepano/obsidian-hider)
plugins, to silently execute code when a victim opens a shared cloud vault," researchers Salim Bitam, Samir Bousseaden, and Daniel Stepanic said in a technical breakdown of the campaign.

Given that the option is disabled by default and cannot be remotely turned on, the attacker must convince the target to manually toggle the community plugin sync on their device so that the malicious vault configuration can trigger the execution of commands through the Shell Commands plugin. Also used in conjunction with Shell Commands is another plugin named Hider to hide certain user interface elements of Obsidian, such as status bar, scrollbar, tooltips, and others.

"While this attack requires social engineering to cross the community plugin sync boundary, the technique remains notable: it abuses a legitimate application feature as a persistence and command execution channel, the payload lives entirely within JSON configuration files that are unlikely to trigger traditional AV [antivirus] signatures, and execution is handed off by a signed, trusted Electron application, making parent-process-based detection the critical layer," the researchers said.

Dedicated execution paths are activated depending on the operating system. On Windows, the commands are used to invoke a PowerShell script to drop an intermediate loader codenamed PHANTOMPULL that decrypts and launches PHANTOMPULSE in memory.

PHANTOMPULSE is an artificial intelligence (AI)-generated backdoor that uses the Ethereum blockchain for resolving its command-and-control (C2) server by fetching the
[latest transaction](https://etherscan.io/tx/0x4ad9923ede3ba2dab91cd37a733c01a08d91caaa4a867b77a3597acb28d40c31)
associated with a
[hard-coded wallet address](https://etherscan.io/address/0xc117688c530b660e15085bF3A2B664117d8672aA)
. Upon obtaining the C2 address, the malware uses WinHTTP for communications, allowing it to send system telemetry data, fetch commands and transmit the execution results, upload files or screenshots, and capture keystrokes.

The supported commands are designed to facilitate comprehensive remote access -

* **inject**
  , to inject shellcode/DLL/EXE into target process
* **drop**
  , to drop a file to disk and execute it
* **screenshot**
  , to capture and upload a screenshot
* **keylog**
  , to start/stop a keylogger
* **uninstall**
  , to initiate removal of persistence and perform cleanup
* **elevate**
  , to escalate privileges to SYSTEM via the
  [COM elevation moniker](https://learn.microsoft.com/en-us/windows/win32/com/the-com-elevation-moniker)
* **downgrade**
  , to transition from SYSTEM to elevated admin

On macOS, the Shell Commands plugin delivers an obfuscated AppleScript dropper that iterates over a hard-coded domain list, while employing Telegram as a dead drop resolver for fallback C2 resolution. This approach also offers added flexibility as it makes it possible to easily rotate C2 infrastructure, rendering domain-based blocking insufficient.

In the final step, the dropper script contacts the C2 domain to download and execute a second-stage payload via osascript. The exact nature of this payload remains unknown given that the C2 servers are currently offline. The intrusion was ultimately unsuccessful, as the attack was detected and blocked before the adversary could accomplish their goals on the infected machine.

"REF6598 demonstrates how threat actors continue to find creative initial access vectors by abusing trusted applications and employing targeted social engineering," Elastic said. "By abusing Obsidian's community plugin ecosystem rather than exploiting a software vulnerability, the attackers bypass traditional security controls entirely, relying on the application's intended functionality to execute arbitrary code."