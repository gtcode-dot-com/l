---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-01T12:03:07.899032+00:00'
exported_at: '2025-12-01T12:03:10.139616+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/tomiris-shifts-to-public-service.html
structured_data:
  about: []
  author: ''
  description: Tomiris is using public-service C2 implants and new phishing chains
    to stealthily deploy multi-language malware across targeted government networks.
  headline: Tomiris Shifts to Public-Service Implants for Stealthier C2 in Attacks
    on Government Targets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/tomiris-shifts-to-public-service.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Tomiris Shifts to Public-Service Implants for Stealthier C2 in Attacks on Government
  Targets
updated_at: '2025-12-01T12:03:07.899032+00:00'
url_hash: eded0b7ee00a85405c77ea29284e5283862647f6
---

**

Dec 01, 2025
**

Ravie Lakshmanan

Malware / Threat Intelligence

The threat actor known as
**[Tomiris](https://thehackernews.com/2023/04/russian-hackers-tomiris-targeting.html)**
has been attributed to attacks targeting foreign ministries, intergovernmental organizations, and government entities in Russia with an aim to establish remote access and deploy additional tools.

"These attacks highlight a notable shift in Tomiris's tactics, namely the increased use of implants that leverage public services (e.g., Telegram and Discord) as command-and-control (C2) servers," Kaspersky researchers Oleg Kupreev and Artem Ushkov
[said](https://securelist.com/tomiris-new-tools/118143/)
in an analysis. "This approach likely aims to blend malicious traffic with legitimate service activity to evade detection by security tools."

The cybersecurity company said more than 50% of the spear-phishing emails and decoy files used in the campaign used Russian names and contained Russian text, indicating that Russian-speaking users or entities were the primary focus. The spear-phishing emails have also targeted Turkmenistan, Kyrgyzstan, Tajikistan, and Uzbekistan using tailored content written in their respective national languages.

The attacks aimed at high-value political and diplomatic infrastructure have leveraged a combination of reverse shells, custom implants, and open-source C2 frameworks like Havoc and AdaptixC2 to facilitate post-exploitation.

Details of Tomiris
[first emerged](https://thehackernews.com/2021/09/new-tomiris-backdoor-found-linked-to.html)
in September 2021 when Kaspersky shed light on the inner workings of a backdoor of the same name, pinpointing its links with SUNSHUTTLE (aka GoldMax), a malware used by the Russian APT29 hackers behind the SolarWinds supply chain attack, and Kazuar, a .NET-based espionage backdoor used by Turla.

Despite these overlaps, Tomiris is assessed to be a different threat actor that mainly focuses on intelligence gathering in Central Asia. Microsoft, in a report
[published](https://thehackernews.com/2024/12/russia-linked-turla-exploits-pakistani.html)
in December 2024, connected the Tomiris backdoor to a Kazakhstan-based threat actor it tracks as Storm-0473.

Subsequent reports from
[Cisco Talos](https://thehackernews.com/2023/10/yorotrooper-researchers-warn-of.html)
,
[Seqrite Labs](https://thehackernews.com/2025/02/silent-lynx-using-powershell-golang-and.html)
,
[Group-IB](https://thehackernews.com/2025/08/shadowsilk-hits-36-government-targets.html)
, and
[BI.ZONE](https://thehackernews.com/2025/10/new-cavalry-werewolf-attack-hits.html)
have strengthened this hypothesis, with the analyses identifying overlaps with clusters referred to as Cavalry Werewolf, ShadowSilk,
[Silent Lynx](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html#silent-lynx-exploits-diplomacy-themes-to-breach-targets)
, SturgeonPhisher, and YoroTrooper.

The latest activity documented by Kaspersky begins with phishing emails containing malicious password-protected RAR files. The password to open the archive is included in the text of the email. Present within the file is an executable masquerading as a Microsoft Word document (\*.doc.exe) that, when launched, drops a C/C++ reverse shell that's responsible for gathering system information and contacting a C2 server to fetch AdaptixC2.

The reverse shell also makes Windows Registry modifications to ensure persistence for the downloaded payload. Three different versions of the malware have been detected this year alone.

Alternatively, the RAR archives propagated via the emails have been found to deliver other malware families, which, in turn, trigger their own infection sequences -

* A Rust-based downloader that collects system information and sends it to a Discord webhook; creates Visual Basic Script (VBScript) and PowerShell script files; and launches the VBScript using cscript, which runs the PowerShell script to fetch a ZIP file containing an executable associated with Havoc.
* A Python-based reverse shell that uses Discord as C2 to receive commands, execute them, and exfiltrate the results back to the server; conducts reconnaissance; and downloads next-stage implants, including AdaptixC2 and a Python-based FileGrabber that harvests files matching jpg, .png, .pdf, .txt, .docx, and .doc. extensions.
* A Python-based backdoor dubbed Distopia that's based on the open-source
  [dystopia-c2](https://github.com/3ct0s/dystopia-c2)
  project and uses Discord as C2 to execute console commands and download additional payloads, including a Python-based reverse shell that uses Telegram for C2 to run commands on the host and send the output back to the server.

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/ai-security-insights-d)

Tomiris' malware arsenal also comprises a number of reverse shells and implants written in different programming languages -

* A C# reverse shell that employs Telegram to receive commands
* A Rust-based malware named JLORAT that can run commands and take screenshots
* A Rust-based reverse shell that uses PowerShell as the shell rather than "cmd.exe"
* A Go-based reverse shell that establishes a TCP connection to run commands via "cmd.exe"
* A PowerShell backdoor that uses Telegram to execute commands and download an arbitrary file to the "C:\Users\Public\Libraries\" location
* A C# reverse shell that uses establishes a TCP connection to run commands via "cmd.exe"
* A reverse SOCKS proxy written in C++ that modifies the open-source
  [Reverse-SOCKS5](https://github.com/Neosama/Reverse-SOCKS5)
  project to remove debugging messages and hide the console window
* A reverse SOCKS proxy written in Golang that modifies the open-source
  [ReverseSocks5](https://github.com/Acebond/ReverseSocks5)
  project to remove debugging messages and hide the console window

"The Tomiris 2025 campaign leverages multi-language malware modules to enhance operational flexibility and evade detection by appearing less suspicious," Kaspersky said. "The evolution in tactics underscores the threat actor's focus on stealth, long-term persistence, and the strategic targeting of government and intergovernmental organizations."