---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-03T06:15:14.432933+00:00'
exported_at: '2026-02-03T06:15:16.640145+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/notepad-hosting-breach-attributed-to.html
structured_data:
  about: []
  author: ''
  description: Rapid7 links China-linked Lotus Blossom to a 2025 Notepad++ hosting
    breach that delivered the Chrysalis backdoor via hijacked updates, fixed in v8.8.9
  headline: Notepad++ Hosting Breach Attributed to China-Linked Lotus Blossom Hacking
    Group
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/notepad-hosting-breach-attributed-to.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Notepad++ Hosting Breach Attributed to China-Linked Lotus Blossom Hacking Group
updated_at: '2026-02-03T06:15:14.432933+00:00'
url_hash: 424ac9ba3f3281697544b5b5e3c7248beed2132c
---

**

Ravie Lakshmanan
**

Feb 03, 2026

Malware / Open Source

A China-linked threat actor known as
**[Lotus Blossom](https://thehackernews.com/2025/03/chinese-apt-lotus-panda-targets.html)**
has been attributed with medium confidence to the recently discovered compromise of the infrastructure hosting Notepad++.

The attack enabled the state-sponsored hacking group to deliver a previously undocumented backdoor codenamed
**Chrysalis**
to users of the open-source editor, according to
[new findings](https://www.rapid7.com/blog/post/tr-chrysalis-backdoor-dive-into-lotus-blossoms-toolkit/)
from Rapid7.

The development comes shortly after Notepad++ maintainer Don Ho
[said](https://thehackernews.com/2026/02/notepad-official-update-mechanism.html)
that a compromise at the hosting provider level allowed threat actors to hijack update traffic starting June 2025 and selectively redirect such requests from certain users to malicious servers to serve a tampered update by exploiting insufficient update verification controls that existed in older versions of the utility.

The weakness was plugged in December 2025 with the release of version 8.8.9. It has since emerged that the hosting provider for the software was breached to perform targeted traffic redirections until December 2, 2025, when the attacker's access was terminated. Notepad++ has since migrated to a new hosting provider with stronger security and rotated all credentials.

Rapid7's analysis of the incident has uncovered no evidence or artifacts to suggest that the updater-related mechanism was exploited to distribute malware.

"The only confirmed behavior is that execution of 'notepad++.exe' and subsequently 'GUP.exe' preceded the execution of a suspicious process 'update.exe' which was downloaded from 95.179.213.0," security researcher Ivan Feigl said.

"Update.exe" is a Nullsoft Scriptable Install System (NSIS) installer that contains multiple files -

* An NSIS installation script
* BluetoothService.exe, a renamed version of Bitdefender Submission Wizard that's used for DLL side-loading (a technique widely used by Chinese hacking groups)
* BluetoothService, encrypted shellcode (aka Chrysalis)
* log.dll, a malicious DLL that's sideloaded to decrypt and execute the shellcode

Chrysalis is a bespoke, feature-rich implant that gathers system information and contacts an external server ("api.skycloudcenter[.]com") to likely receive additional commands for execution on the infected host.

The command-and-control (C2) server is currently offline. However, a deeper examination of the obfuscated artifact has revealed that it's capable of processing incoming HTTP responses to spawn an interactive shell, create processes, perform file operations, upload/download files, and uninstall itself.

"Overall, the sample looks like something that has been actively developed over time," Rapid7 said, adding it also identified a file named "conf.c" that's designed to retrieve a Cobalt Strike beacon by means of a custom loader that embeds
[Metasploit block API](https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x86/src/block/block_api.asm)
shellcode.

One such loader, "ConsoleApplication2.exe" is noteworthy for its use of
[Microsoft Warbird](https://websec.net/blog/a-deep-dive-into-microsoft-warbird-mss-kernel-mode-dynamic-packer-68ee2c87b251081f55ec8c31)
, an undocumented internal code protection and obfuscation framework, to execute shellcode. The threat actor has been found to copy and modify an already existing proof-of-concept (PoC)
[published](https://cirosec.de/en/news/abusing-microsoft-warbird-for-shellcode-execution/)
by German cybersecurity company Cirosec in September 2024.

Rapid7's attribution of Chrysalis to Lotus Blossom (aka Billbug, Bronze Elgin, Lotus Blossom, Raspberry Typhoon, Spring Dragon, and Thrip) based on similarities with prior campaigns undertaken by the threat actor, including one
[documented](https://thehackernews.com/2025/04/lotus-panda-hacks-se-asian-governments.html)
by Broadcom-owned Symantec in April 2025 that involved the use of legitimate executables from Trend Micro and Bitdefender to sideload malicious DLLs.

"While the group continues to rely on proven techniques like DLL side-loading and service persistence, their multi-layered shellcode loader and integration of undocumented system calls (NtQuerySystemInformation) mark a clear shift toward more resilient and stealth tradecraft," the company said.

"What stands out is the mix of tools: the deployment of custom malware (Chrysalis) alongside commodity frameworks like Metasploit and Cobalt Strike, together with the rapid adaptation of public research (specifically the abuse of Microsoft Warbird). This demonstrates that Billbug is actively updating its playbook to stay ahead of modern detection."