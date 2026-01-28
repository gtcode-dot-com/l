---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-28T14:15:14.962599+00:00'
exported_at: '2026-01-28T14:15:17.117111+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html
structured_data:
  about: []
  author: ''
  description: China-linked Mustang Panda used updated COOLCLIENT malware in 2025
    espionage to steal data from government and telecom targets across Asia and Russia.
  headline: Mustang Panda Deploys Updated COOLCLIENT Backdoor in Government Cyber
    Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Mustang Panda Deploys Updated COOLCLIENT Backdoor in Government Cyber Attacks
updated_at: '2026-01-28T14:15:14.962599+00:00'
url_hash: 92c85b9b3d82925a88ccb3f46bacb7d1c4070bd2
---

Threat actors with ties to China have been observed using an updated version of a backdoor called COOLCLIENT in cyber espionage attacks in 2025 to facilitate comprehensive data theft from infected endpoints.

The activity has been attributed to
**[Mustang Panda](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html)**
(aka Earth Preta, Fireant, HoneyMyte, Polaris, and Twill Typhoon) with the intrusions primarily directed against government entities located across campaigns across Myanmar, Mongolia, Malaysia, and Russia.

Kaspersky, which disclosed details of the updated malware, said it's deployed as a secondary backdoor along with
[PlugX](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)
and
[LuminousMoth](https://thehackernews.com/2021/07/chinas-cyberspies-targeting-southeast.html)
infections.

"COOLCLIENT was typically delivered alongside encrypted loader files containing encrypted configuration data, shellcode, and in-memory next-stage DLL modules," the Russian cybersecurity company
[said](https://securelist.com/honeymyte-updates-coolclient-uses-browser-stealers-and-scripts/118664/)
. "These modules relied on DLL side-loading as their primary execution method, which required a legitimate signed executable to load a malicious DLL."

Between 2021 and 2025, Mustang Panda is said to have leveraged signed binaries from various software products, including Bitdefender ("qutppy.exe"), VLC Media Player ("vlc.exe" renamed as "googleupdate.exe"), Ulead PhotoImpact ("olreg.exe"), and Sangfor ("sang.exe") for this purpose.

Campaigns observed in 2024 and 2025 have been found to abuse legitimate software developed by Sangfor, with one such wave targeting Pakistan and Myanmar using it to deliver a COOLCLIENT variant that drops and executes a previously unseen rootkit.

COOLCLIENT was
[first documented](https://www.sophos.com/en-us/blog/family-tree-dll-sideloading-cases-may-be-related)
by Sophos in November 2022 in a report detailing the widespread use of DLL side-loading by China-based APT groups. A subsequent analysis from Trend Micro officially
[attributed](https://thehackernews.com/2023/03/researchers-uncover-chinese-nation.html)
the backdoor to Mustang Panda and highlighted its ability to read/delete files, as well as monitor the clipboard and active windows.

The malware has also been put to use in attacks targeting multiple telecom operators in a single Asian country in a long-running espionage campaign that may have commenced in 2021, Broadcom's Symantec and Carbon Black Threat Hunter Team
[revealed](https://thehackernews.com/2024/06/chinese-cyber-espionage-targets-telecom.html)
in June 2024.

COOLCLIENT is designed for collecting system and user information, such as keystrokes, clipboard contents, files, and HTTP proxy credentials from the host's HTTP traffic packets based on instructions sent from a command-and-control (C2) server over TCP. It can also set up a reverse tunnel or proxy, and receive and execute additional plugins in memory.

Some of the supported plugins are listed below -

* ServiceMgrS.dll, a service management plugin to oversee all services on the victim host
* FileMgrS.dll, a file management plugin to enumerate, create, move, read, compress, search, or delete files and folders
* RemoteShellS.dll, a remote shell plugin that spawns a "cmd.exe" process to allow the operator to issue commands and capture the resulting output

Mustang Panda has also been observed deploying three different stealer programs in order to extract saved login credentials from Google Chrome, Microsoft Edge, and other Chromium-based browsers. In at least one case, the adversary ran a cURL command to exfiltrate the Mozilla Firefox browser cookie file ("cookies.sqlite") to Google Drive.

These stealers, detected in attacks against the government sector in Myanmar, Malaysia, and Thailand, are suspected to be used as part of broader post-exploitation efforts.

Furthermore, the attacks are characterized by the use of a known malware called
[TONESHELL](https://thehackernews.com/2022/11/chinese-mustang-panda-hackers-actively.html)
(aka TOnePipeShell), which has been employed with varying levels of capabilities to establish persistence and drop additional payloads like
[QReverse](https://hitcon.org/2024/CMT/agenda/5e788b7a-f9e1-4f0c-b772-f7fe9b0140ec/)
, a remote access trojan with remote shell, file management, screenshot capture, and information gathering features, and a USB worm codenamed
[TONEDISK](https://thehackernews.com/2025/09/mustang-panda-deploys-snakedisk-usb.html)
.

Kaspersky's analysis of the browser credential stealer has also uncovered code-level similarities with a cookie stealer used by LuminousMoth, suggesting some level of tool sharing between the two clusters. On top of that, Mustang Panda has been identified as using batch and PowerShell scripts to gather system information, conduct document theft activities, and steal browser login data.

"With capabilities such as keylogging, clipboard monitoring, proxy credential theft, document exfiltration, browser credential harvesting, and large-scale file theft, HoneyMyte's campaigns appear to go far beyond traditional espionage goals like document theft and persistence," the company said.

"These tools indicate a shift toward the active surveillance of user activity that includes capturing keystrokes, collecting clipboard data, and harvesting proxy credentials."