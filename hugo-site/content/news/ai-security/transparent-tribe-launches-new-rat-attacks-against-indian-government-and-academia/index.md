---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-03T00:15:14.122454+00:00'
exported_at: '2026-01-03T00:15:17.783856+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html
structured_data:
  about: []
  author: ''
  description: 'Transparent Tribe (APT36) is linked to new cyber-espionage attacks
    using malicious LNK files, adaptive RATs, and long-term persistence against Indian '
  headline: Transparent Tribe Launches New RAT Attacks Against Indian Government and
    Academia
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/transparent-tribe-launches-new-rat.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Transparent Tribe Launches New RAT Attacks Against Indian Government and Academia
updated_at: '2026-01-03T00:15:14.122454+00:00'
url_hash: 213da710e699a769eaeb83ccff5c0a6a275af2f3
---

The threat actor known as Transparent Tribe has been attributed to a fresh set of attacks targeting Indian governmental, academic, and strategic entities with a remote access trojan (RAT) that grants them persistent control over compromised hosts.

"The campaign employs deceptive delivery techniques, including a weaponized Windows shortcut (LNK) file masquerading as a legitimate PDF document and embedded with full PDF content to evade user suspicion," CYFIRMA
[said](https://www.cyfirma.com/research/apt36-multi-stage-lnk-malware-campaign-targeting-indian-government-entities/)
in a technical report.

Transparent Tribe, also called APT36, is a hacking group that's known for mounting cyber espionage campaigns against Indian organizations. Assessed to be of Indian origin, the state-sponsored adversary has been active since at least 2013.

The threat actor boasts of an ever-evolving arsenal of RATs to realize its goals. Some of the trojans put to use by Transparent Tribe in recent years include
[CapraRAT](https://thehackernews.com/2023/09/transparent-tribe-uses-fake-youtube.html)
,
[Crimson RAT](https://thehackernews.com/2023/04/pakistan-based-transparent-tribe.html)
,
[ElizaRAT](https://thehackernews.com/2024/11/icepeony-and-transparent-tribe-target.html)
, and
[DeskRAT](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)
.

The latest set of attacks began with a spear-phishing email containing a ZIP archive with a LNK file disguised as a PDF. Opening the file triggers the execution of a remote HTML Application (HTA) script using "mshta.exe" that decrypts and loads the final RAT payload directly in memory. In tandem, the HTA downloads and opens a decoy PDF document so as not to arouse users' suspicion.

"After decoding logic is established, the HTA leverages ActiveX objects, particularly WScript.Shell, to interact with the Windows environment," CYFIRMA noted. "This behavior demonstrates environment profiling and runtime manipulation, ensuring compatibility with the target system and increasing execution reliability techniques commonly observed in malware abusing 'mshta.exe.'"

A noteworthy aspect of the malware is its ability to adapt its persistence method based on the antivirus solutions installed on the infected machine -

* If Kapsersky is detected, it creates a working directory under "C:\Users\Public\core\," writes an obfuscated HTA payload to disk, and establishes persistence by dropping a LNK file in the Windows Startup folder that, in turn, launches the HTA script using "mshta.exe"
* If Quick Heal is detected, it establishes persistence by creating a batch file and a malicious LNK file in the Windows Startup folder, writing the HTA payload to disk, and then calling it using the batch script
* If Avast, AVG, or Avira are detected, it works by directly copying the payload into the Startup directory and executing it
* If no recognized antivirus solution is detected, it falls back to a combination of batch file execution, registry based persistence, and payload deployment prior to launching the batch script

The second HTA file includes a DLL named "iinneldc.dll" that functions as a fully-featured RAT, supporting remote system control, file management, data exfiltration, screenshot capture, clipboard manipulation, and process control.

"APT36 (Transparent Tribe) remains a highly persistent and strategically driven cyber-espionage threat, with a sustained focus on intelligence collection targeting Indian government entities, educational institutions, and other strategically relevant sectors," the cybersecurity company said.

In recent weeks, APT36 has also been linked to another campaign that leverages a malicious shortcut file disguised as a government advisory PDF ("NCERT-Whatsapp-Advisory.pdf.lnk") to deliver a .NET-based loader, which then drops additional executables and malicious DLLs to establish remote command execution, system reconnaissance, and long-term access.

The shortcut is designed to execute an obfuscated command using cmd.exe to retrieve an MSI installer ("nikmights.msi") from a remote server ("aeroclubofindia.co[.]in"), which is responsible for initiating a series of actions -

* Extract and display a decoy PDF document to the victim
* Decode and write DLL files to "C:\ProgramData\PcDirvs\pdf.dll" and "C:\ProgramData\PcDirvs\wininet.dll"
* Drop "PcDirvs.exe" to the same the same location and execute it after a delay of 10 seconds
* Establish persistence by creating "PcDirvs.hta" that contains Visual Basic Script to make Registry modifications to launch "PcDirvs.exe" every time after system startup

It's worth pointing out that the lure PDF displayed is a
[legitimate advisory](https://web.archive.org/web/20240808195321/https://pkcert.gov.pk/advisory/24-12.pdf)
issued by the National Cyber Emergency Response Team of Pakistan (PKCERT) in 2024 about a fraudulent WhatsApp message campaign targeting government entities in Pakistan with a malicious WinRAR file that infects systems with malware.

The DLL "wininet.dll" connects to a hard-coded command-and-control (C2) infrastructure hosted at dns.wmiprovider[.]com. It was registered in mid-April 2025. The C2 associated with the activity is currently inactive, but the Windows Registry-based persistence ensures that the threat can be resurrected at any time in the future.

"The DLL implements multiple HTTP GET–based endpoints to establish communication with the C2 server, perform updates, and retrieve attacker-issued commands," CYFIRMA
[said](https://www.cyfirma.com/research/apt36-lnk-based-malware-campaign-leveraging-msi-payload-delivery/)
. "To evade static string detection, the endpoint characters are intentionally stored in reversed order."

The list of endpoints is as follows -

* /retsiger (register), to register the infected system with the C2 server
* /taebtraeh (heartbeat), to beacon its presence to the C2 server
* /dnammoc\_teg (get\_command), to run arbitrary commands via "cmd.exe"
* /dnammocmvitna (antivmcommand), to query or set an anti-VM status and likely adjust behavior

The DLL also queries installed antivirus products on the victim system, turning it into a potent tool capable of conducting reconnaissance and gathering sensitive information.

### Patchwork Linked to New StreamSpy Trojan

The disclosure comes weeks after
[Patchwork](https://thehackernews.com/2025/07/patchwork-targets-turkish-defense-firms.html)
(aka
[Dropping Elephant or Maha Grass](https://ti.qianxin.com/apt/detail/5aa10b90d70a3f2810c4d3c5?name=Hangover&type=list)
), a hacking group believed to be of Indian origin, was linked to attacks targeting Pakistan's defense sector with a Python-based backdoor that's distributed via phishing emails containing ZIP files,
[according](https://www.linkedin.com/posts/idan-tarab-7a9057200_india-backdoor-msbuild-activity-7397661496421470208-ltCf/)
to security researcher Idan Tarab.

Present within the archive is an MSBuild project that, when executed via "msbuild.exe," deploys a dropper to ultimately install and launch the Python RAT. The malware is equipped to contact a C2 server and run remote Python modules, execute commands, and upload/download files.

"This campaign represents a modernized, highly obfuscated Patchwork APT toolkit blending MSBuild
[LOLBin](https://www.huntress.com/blog/detecting-malicious-use-of-lolbins)
loaders, PyInstaller‑modified Python runtimes, marshalled bytecode implants, geofencing, randomized PHP C2 endpoints, [and] realistic persistence mechanisms," Tarab said.

As of December 2025, Patchwork has also been
[associated](https://ti.qianxin.com/blog/articles/analysis-of-streamspy-a-new-trojan-using-websocket-by-patchwork-en/)
with a previously undocumented trojan named StreamSpy, which uses WebSocket and HTTP protocols for C2 communication. While the WebSocket channel is used to receive instructions and transmit the execution results, HTTP is leveraged for file transfers.

StreamSpy's links to Patchwork, per QiAnXin, stem from its similarities to
[Spyder](https://ti.qianxin.com/blog/articles/Patchwork-Group-Utilizing-WarHawk-Backdoor-Variant-Spyder-for-Espionage-against-Multiple-Countries-EN/)
, a variant of another backdoor named
[WarHawk](https://thehackernews.com/2024/09/cloudflare-warns-of-india-linked.html)
that's attributed to
[SideWinder](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)
. Patchwork's use of Spider dates all the way back to 2023.

Distributed via ZIP archives ("OPS-VII-SIR.zip") hosted on "firebasescloudemail[.]com," the malware ("
[Annexure.exe](https://www.virustotal.com/gui/file/3a4f47c60edf1e00adb3ca60a7643062657fe2c6dd85ace9dfd8fdec47078d4e)
") can harvest system information, establish persistence via Windows Registry, scheduled task, or via a LNK file in the Startup folder, communicate with the C2 server using HTTP and WebSocket. The list of support commands is below -

* F1A5C3, to download a file and open it using ShellExecuteExW
* B8C1D2, to set the shell for command execution to cmd
* E4F5A6, to set the shell for command execution to PowerShell
* FL\_SH1, to close all shells
* C9E3D4, E7F8A9, H1K4R8, C0V3RT, to download encrypted zip files from the C2 server, extract them, and open them using ShellExecuteExW
* F2B3C4, to gather information about the file system and all disks connected to the device
* D5E6F7, to perform file upload and download
* A8B9C0, to perform file upload
* D1E2F3, to delete a file
* A4B5C6, to rename a file
* D7E8F9, to enumerate a specific folder

QinAnXin said the StreamSpy download site also hosts Spyder variants with extensive data collection features, adding the malware's digital signature exhibits correlations with a different
[Windows RAT](https://www.virustotal.com/gui/file/dc297aded70b0692ad0a24509e7bbec210bc0a1c7a105e99e1a8f76e3861ad34)
called
[ShadowAgent](https://x.com/malwrhunterteam/status/1985321347279626438)
[attributed](https://x.com/malwrhunterteam/status/1986334542123159792)
to the
[DoNot Team](https://thehackernews.com/2025/07/donot-apt-expands-operations-targets.html)
(aka Brainworm). Interestingly, 360 Threat Intelligence Center
[flagged](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247507603&idx=1&sn=af41be456f6393a24771846328e8d7f2&poc_token=HFXIV2mjHDf6vRChlY5yx20OepiqSApAHaYOo067)
the same "Annexure.exe" executable as ShadowAgent in November 2025.

"The emergence of the StreamSpy Trojan and Spyder variants from the Maha Grass group indicates that the group is continuously iterating its arsenal of attack tools," the Chinese security vendor said.

"In the StreamSpy trojan, attackers attempt to use WebSocket channels for command issuance and result feedback to evade detection and censorship of HTTP traffic. Additionally, the correlated samples further confirm that the Maha Grass and
[DoNot](https://ti.qianxin.com/blog/articles/analysis-of-the-attack-activity-of-the-apt-q-38-using-pdf-document-decoys-cn/)
attack groups have some connections in terms of resource sharing."