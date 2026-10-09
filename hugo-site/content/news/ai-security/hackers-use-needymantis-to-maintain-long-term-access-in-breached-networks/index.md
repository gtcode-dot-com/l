---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T21:50:20.661040+00:00'
exported_at: '2026-10-06T21:50:22.948551+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html
structured_data:
  about: []
  author: ''
  description: NeedyMantis maintains long-term access in targeted intrusions, using
    DLL sideloading and HTTPS-to-WebSocket command-and-control.
  headline: Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hackers Use NeedyMantis to Maintain Long-Term Access in Breached Networks
updated_at: '2026-10-06T21:50:20.661040+00:00'
url_hash: e7f8e7a928b1f9222f28e79c25b416c1d6339fb3
---

Hackers have used a malware family called
**NeedyMantis**
to maintain long-term access to networks they had already breached, Microsoft said in a technical analysis.

The malware has been seen in a small number of targeted intrusions at telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors. Its use goes back to at least October 2025.

Microsoft found
[NeedyMantis](https://www.microsoft.com/en-us/security/blog/2026/09/28/needymantis-unpacking-a-post-compromise-malware-family-used-in-targeted-operations/)
while following up on indicators from Kaspersky's investigation into the
[supply chain attack on DAEMON Tools](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html)
. In that attack, official, signed installers for the DAEMON Tools Lite disk image program carried malicious code from April 8, 2026. The developer replaced them with a clean version on May 5.

Microsoft tracks the activity tied to that attack as Storm-3069. It says Storm-3069 is one group that uses NeedyMantis, though it has not seen the malware itself spread through a supply chain attack. Defenders can check their networks using the file hashes, domains, file paths, and hunting queries that Microsoft published and listed below.

### How NeedyMantis Runs

In the cases Microsoft examined, NeedyMantis arrived as a bundle of three parts: a copy of a legitimate program, a malicious DLL named after a file that program loads, and an encrypted archive with the same name as the DLL. When the program starts, it loads the malicious DLL. This is called DLL sideloading.

The legitimate programs used this way include the Poedit translation tool, curl, the Vim text editor, and the TightVNC remote access tool. The malware has also posed as DLL files from Microsoft Office, Broadcom, Intel, and NVIDIA.

In the sample Microsoft analyzed in detail, the malicious file replaced WinSparkle.dll, the update component that Poedit uses.

In one intrusion, an operator who was already inside the network used the Impacket toolkit to copy the bundle from a network share and run it on a target machine. How attackers initially gain access to a network may differ from one intrusion to the next.

Once loaded, the DLL unpacks the next stage from the encrypted archive and runs it. That stage decodes the malware's main component. The main component connects to a command-and-control (C2) server over HTTPS and then switches to a WebSocket connection.

Through that connection, operators can load and unload extra modules and send data to them. Microsoft has not confirmed what those modules do.

An older version, seen in October 2025, included a persistence module that uses Windows services. Microsoft did not describe how the newer version it analyzed stays on a machine.

### Who Is Behind It

Storm-3069 is a temporary name. Microsoft
[gives "Storm" names](https://learn.microsoft.com/en-us/defender-xdr/microsoft-threat-actor-naming)
to new or developing groups until it is confident about who is behind them or where they come from.

Microsoft has also seen NeedyMantis outside Storm-3069's activity in the DAEMON Tools campaign, and it says more than one group may be using the malware. It has not determined whether all the activity comes from a single actor, nor has it explained what links Storm-3069 to NeedyMantis.

Storm-3069's activity appears to originate in China, Microsoft assesses, but the company has not tied the group to a Chinese nation-state actor. All the NeedyMantis activity Microsoft has seen so far fits the pattern of groups it links to China. Examples include targets that align with Chinese interests and the malware's use against only a few selected organizations.

When Kaspersky disclosed the DAEMON Tools attack in May, it found Chinese-language text in the malware but did not attribute it to any particular group.

Google Threat Intelligence Group
[tracks the actor](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise)
behind the DAEMON Tools campaign as UNC6863. In June,
[Mandiant described UNC6863](https://security.googlecloudcommunity.com/security-validation-5/validation-content-update-june-24-2026-7779)
as "a suspected China-nexus actor" that used the DAEMON Tools compromise to deploy malware. It is unclear whether UNC6863 and Storm-3069 belong to the same group.

### How to Check for NeedyMantis

Microsoft published these indicators of compromise:

* **SHA-256**
  : e842dd7642c8e04b5ec20b6393848a9c904e4832930950c16664fe7800ba382e (first-stage loader WinSparkle.dll, first seen May 21, 2026)
* **SHA-256**
  : 9cb68f986043a576e19d32184c583b7d8f571c7219d8dc0065dced1c13f077ef (encrypted archive named WinSparkle, first seen May 23, 2026)
* **SHA-256**
  : c82520eb03c084226be4eafbff46f56dca0aa8804a2a7f23a085a96afe71ef77 (encrypted archive named libcurl, older version, first seen October 3, 2025)
* **Domain**
  : corp.tripswithengine[.]com (C2 server, port 443)
* **User agent**
  : firefox/21.0 (hard-coded in the malware's communications DLL)

These are some of the file paths used by the malicious DLLs:

* %ProgramFiles%\Poedit\WinSparkle.dll
* %ProgramData%\USOShared\libcurl.dll
* %ProgramData%\VIM\vim64.dll
* %ProgramData%\TightVNC\VIM\vim64.dll
* %ProgramData%\office\dbghelp.dll
* %ProgramData%\broadcom\dbghelp.dll
* %ProgramData%\Intel\jli.dll
* %ProgramFiles%\modifiable\nvml.dll
* %ProgramData%\ics\nvml.dll

Microsoft Defender Antivirus detects the malware as TrojanDropper:Win64/NeedyMantis and Behavior:Win64/NeedyMantis. Microsoft also published hunting queries that look for these paths in Defender XDR, and for the C2 domain and user agent in both Defender XDR and Microsoft Sentinel.

Each query looks back only seven days. Microsoft has not said whether NeedyMantis is still in use, and the files it dated were first seen in October 2025 and May 2026. If run unchanged, the queries would not find events from those months.

A hit on the Poedit path alone does not prove an infection. WinSparkle.dll is also a normal part of Poedit, so compare any file found there with the published hash.

Microsoft recommends several Defender settings: cloud-delivered protection, block at first sight, EDR in block mode, network protection, automatic attack disruption, and two attack surface reduction rules. It also advises checking outbound traffic for connections to the C2 domain, a step that does not need Defender.

Microsoft has not seen NeedyMantis arrive through the tampered DAEMON Tools installers. For those installers,
[the developer has advised](https://thehackernews.com/2026/05/daemon-tools-supply-chain-attack.html)
that anyone who downloaded or installed the free DAEMON Tools Lite 12.5.1 during the affected period should uninstall it, run a full system scan, and download version 12.6 from the official website.