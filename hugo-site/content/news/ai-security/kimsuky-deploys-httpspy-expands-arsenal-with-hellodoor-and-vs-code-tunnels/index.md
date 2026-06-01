---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-01T01:10:12.129504+00:00'
exported_at: '2026-06-01T01:10:13.492129+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
structured_data:
  about: []
  author: ''
  description: Kimsuky used fake security tools and Webex pages in March-April 2026
    to deploy HTTPSpy, enabling persistent espionage and data theft.
  headline: Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/kimsuky-deploys-httpspy-expands-arsenal.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Kimsuky Deploys HTTPSpy, Expands Arsenal with HelloDoor and VS Code Tunnels
updated_at: '2026-06-01T01:10:12.129504+00:00'
url_hash: 9fc7eeb6b2bd31e2ab634c0f1841cf545639ff34
---

The North Korean state-sponsored threat actor known as
**[Kimsuky](https://thehackernews.com/2026/01/fbi-warns-north-korean-hackers-using.html)**
(aka Velvet Chollima) has been attributed to a fresh set of cyber attacks targeting South Korean military and corporate entities through March and April 2026.

"Kimsuky employed a range of tailored social engineering tactics, such as spoofing security software installation pages and crafting a fake Webex meeting page that leveraged a legitimate meeting schedule," ENKI
[said](https://www.enki.co.kr/en/media-center/blog/kimsuky-s-advanced-attack-techniques-jsonping-webex-spoofing-and-a-new-httpspy-variant)
in an analysis published this week.

The attacks have been found to deliver a variant of a known malware family dubbed
**HTTPSpy**
by disguising it as installers from South Korean security software, a tactic the
[threat actor](https://www.estsecurity.com/public/security-center/notice/view/542031?category-id=)
has
[consistently](https://asec.ahnlab.com/ko/61666/)
[adopted](https://blog.alyac.co.kr/5564)
since 2023.

In the latest campaign observed in March 2026, the adversary has been found to propagate malicious payloads through a bogus web page impersonating the security software installation page of a South Korean B2B messaging service. Given the nature of the lure, it's suspected that the activity may have been specifically designed to single out messaging administrators within corporate environments.

The page claims to offer two security tools: a firewall and a keyboard security program. Once unsuspecting users initiate the download, it results in the download of either of the two executables - "nos-setup.exe" and "astx-setup.exe" - that masquerade as nProtect Online Security and AhnLab Safe Transaction (ASTx). Despite the differences in the name, the malicious behavior embedded in them is identical.

The primary responsibility of the binaries is to launch a second-stage DLL payload ("MemLoader.dll") via "regsvr32.exe," after which a batch script is run to delete themselves from disk. The DLL establishes persistence on the host using a scheduled task and contacts a command-and-control (C2) server to retrieve an as-yet-unknown payload.

"The attacker likely monitored the recurring GET requests from the malware and selectively delivered payloads to specific victims," ENKI said.

In another campaign observed in April 2026, a counterfeit web page mimicking Cisco Webex is said to have been used to display a pop-up message urging the victim to download and run a script to address issues with accessing the camera. Doing so results in the retrieval of a ZIP archive containing an encrypted JavaScript (JSE) file ("fix-camera.jse").

The execution of the JSE file results in the deployment of an intermediate downloader ("mTSTCv8.mdxm") using PowerShell, which then runs anti-analysis checks and contacts a C2 server to fetch the next-stage malware ("engine.dat" or "spyInster.dll"). In the final stage, the DLL drops a loader component ("cacheMon.dat") that, in turn, executes HTTPSpy on the compromised system.

HTTPSpy is a full-featured remote access trojan that supports a wide range of capabilities to run shell commands, upload/download files, execute processes, capture screenshots, inject DLL paths into specified PID processes, and erase itself from the endpoint.

This is not the first time Kimsuky has deployed HTTPSpy. In its 2025 European Threat Landscape Report, CrowdStrike
[said](https://www.crowdstrike.com/en-us/resources/reports/2025-european-threat-landscape-report/)
the hacking group likely targeted a German defense manufacturer's employees via a credential phishing campaign deploying the malware between May 2024 and at least September 2024. The first use of HTTPSpy dates back to 2022.

Simultaneously, the malware also drops and opens an HTML file named "meeting.html," which immediately redirects the victim to a Webex meeting room. Accessing the URL opens a legitimate Webex meeting room associated with an actual scheduled event that took place around the same time.

"This indicates that the attacker likely compromised a service member's device or account to obtain the meeting schedule, then crafted a fake meeting page to distribute malware to the other attendees," the cybersecurity company said.

ENKI said it also discovered additional fake web pages that query a local server set up by the malware on the victim's machine via JSONP (JSON with Padding) to verify malware execution status and display an installation prompt if it's not running. The technique has been codenamed JSONPing. However, the exact nature of the downloaded malware remains unknown as the URL is currently inactive.

"Kimsuky went beyond simple malware distribution, introducing sophisticated mechanisms to maximize delivery success, including real-time infection verification via JSONPing and crafting a fake page using a stolen meeting schedule," ENKI said.

### Kimsuky Evolves with HelloDoor and HttpMalice

The disclosure comes as Kaspersky detailed the threat actor's use of Microsoft Visual Studio Code (VS Code) tunneling, Cloudflare Quick Tunnels, DWAgent, large language models (LLMs), and the Rust programming language in its latest campaigns, highlighting its continued adaptation and evolution.

"Specifically, Kimsuky leveraged legitimate VS Code tunneling mechanisms to establish persistence and distributed the open-source DWAgent remote monitoring and management tool for post-exploitation activities," the Russian cybersecurity company
[said](https://securelist.com/kimsuky-appleseed-pebbledash-campaigns/119785/)
. "These activities affected various sectors in South Korea, impacting both public and private entities."

Attack chains have been found to rely on a variety of droppers written in JSE, PIF, SCR, and EXE to deliver two broad malware families:
[PebbleDash](https://thehackernews.com/2020/05/fbi-north-korean-malware.html)
and
[AppleSeed](https://thehackernews.com/2023/12/kimsuky-hackers-deploying-appleseed.html)
. While PebbleDash attacks have also been recorded against defense organizations in Brazil and Germany, the AppleSeed cluster has mainly targeted government organizations.

Some of the key malware families delivered by the droppers are as follows -

* **HelloDoor**
  , a Rust-based PebbleDash variant first identified in August 2025 and likely developed using an LLM. It supports basic functionality to set the current directory, sleep for a specific time interval, and run commands.
* **HttpMalice**
  , the latest backdoor variant of PebbleDash, emerged no later than December 2025. It comes with capabilities to gather information about the compromised system, set up persistence, perform reconnaissance using native Windows commands, capture screenshots, load downloaded payloads into memory, run commands, and exfiltrate the execution output.
* **[HttpTroy](https://thehackernews.com/2025/11/new-httptroy-backdoor-poses-as-vpn.html)**
  , a backdoor delivered via a loader named MemLoad that allows file upload/download, screenshot capture, command execution, in-memory loading of executables, reverse shell, process termination, and trace removal.
* **AppleSeed**
  , which comes in two variants: Dropper and Spy. The Dropper is responsible for downloading additional malware and executing commands received from its C2 server. The Spy version gathers sensitive information such as documents, screenshots, keystrokes, and lists of USB drives. This also includes harvesting data from the C:\GPKI directory, mirroring a similar feature implemented in
  [Troll Stealer](https://thehackernews.com/2024/02/kimsukys-new-golang-stealer-troll-and.html)
  .
* **[HappyDoor](https://thehackernews.com/2024/07/south-korean-erp-vendors-server-hacked.html)**
  , an advanced version of AppleSeed that
  [first surfaced in 2021](https://asec.ahnlab.com/en/76800/)
  .

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNWuAcO7nYTNC6bUzLqFozm7H2phW6X4ZhRhyphenhyphenXSdtBeE5i_-cm_hK-iZ_ugafujh9yBl7p9LPv70siQDHGNako1kweY0g6Iky6YGE4gFncBs-IjqA5uz3-2PGM6qr0cnQR9T205siBmOu6-uaCiNqu__IsOm8p37F5v-63mQX6MX5yP7ORj-bHMmgKgfFu/s1600/http.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNWuAcO7nYTNC6bUzLqFozm7H2phW6X4ZhRhyphenhyphenXSdtBeE5i_-cm_hK-iZ_ugafujh9yBl7p9LPv70siQDHGNako1kweY0g6Iky6YGE4gFncBs-IjqA5uz3-2PGM6qr0cnQR9T205siBmOu6-uaCiNqu__IsOm8p37F5v-63mQX6MX5yP7ORj-bHMmgKgfFu/s1600/http.png)

Another notable tactical shift involves the abuse of the legitimate VS Code Remote Tunneling feature to establish covert remote access to the victim's device, thereby eliminating the need for traditional malware-based C2 channels. This approach has also been highlighted by
[Darktrace](https://www.darktrace.com/blog/darktrace-identifies-campaign-targeting-south-korea-leveraging-vs-code-for-remote-access)
and
[Logpresso](https://logpresso.com/ko/blog/2026-05-15-1Q-Kimsuky-report)
.

"Our analysis shows that the actor retains access to the original source code of the malware clusters and the ability to modify it," Kaspersky researcher Sojun Ryu said. "Two clusters have overlapping target sectors that span the defense, military, government, medical, machinery, and energy industries."

"The AppleSeed cluster is shifting its focus to data exfiltration, and GPKI certificate extraction has become a signature capability. Meanwhile, the PebbleDash cluster demonstrates advanced remote control capabilities and an expanding set of targets."