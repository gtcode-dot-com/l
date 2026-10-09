---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-17T06:18:59.848013+00:00'
exported_at: '2026-09-17T06:19:02.071624+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/operation-quicsilver-targets-myanmar.html
structured_data:
  about: []
  author: ''
  description: Operation QUICSILVER targets Myanmar government and IT sectors with
    graduation lures that deploy the Go-based QUICAgent backdoor.
  headline: Operation QUICSILVER Targets Myanmar Government and IT with QUICAgent
    Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/operation-quicsilver-targets-myanmar.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Operation QUICSILVER Targets Myanmar Government and IT with QUICAgent Backdoor
updated_at: '2026-09-17T06:18:59.848013+00:00'
url_hash: 7113f16252a4678fcbf35dd50ff7d5331f9d84da
---

**

Ravie Lakshmanan
**

Aug 24, 2026

Cyber Espionage / Cyber Attack

Cybersecurity researchers have flagged a cyber espionage campaign targeting Myanmar that uses graduation ceremony invitation lures to deliver a Go backdoor called QUICAgent.

The campaign, codenamed
**[Operation QUICSILVER](https://www.seqrite.com/blog/operation-quicsilver-china-nexus-actor-targets-myanmar-diplomats-via-vhd-delivered-go-backdoor/)**
, has been found to target government and information technology sectors, per Seqrite Labs. The activity is assessed to be the work of a China-nexus threat actor with moderate confidence.

It was first observed in April 2026, when the attack was observed delivering a file named "HolidayNotice.pdf.exe" along with a lure that was a fabricated Belgian–Myanmar public holiday calendar. Two subsequent artifacts, each detected in June and July 2026, make use of a Virtual Hard Disk (VHD) file that activates the infection chain.

Present within the VHD file is a Windows Shortcut (LNK) that mimics a PDF document. Opening the document displays a decoy PDF to the victim, an official graduation ceremony invitation that's written in Burmese and purports to be from the Information Technology and Cyber Security Department (ITCSD), which operates under Myanmar's Ministry of Transport and Communications.

The "announcement" serves as a distraction while the shortcut file stealthily launches "ftp.exe," a legitimate Microsoft-signed Windows binary, and abuses its "-s" option to run commands stored in a local script file.

"While the decoy is presented on the victim's screen, the script searches for two document files, header.doc and body.doc, stored inside the hidden \_rels directory," security researchers Priya Patel and Kartik Jivani said. "It then combines these two files using the native Windows copy /b command to reconstruct the next-stage payload."

The payload is a Golang-based implant dubbed QUICAgent that performs sandbox evasion techniques before connecting to a command-and-control (C2) server. Specifically, it incorporates a random delay of 100-600 milliseconds and executes 1,000 iterations of SHA-256 hashing operations to exhaust automated sandbox execution time limits.

The backend C2 server address is retrieved dynamically by sending an HTTP GET request to two Cloudflare Workers domains. Once the C2 address is obtained ("104.64.211[.]22"), it suffixes port 443 to the domain and constructs the final destination. The malware uses QUIC over UDP port 443 to communicate with the C2 server.

The initial beacon to the server also includes basic information about the compromised host. The beacon is transmitted every five seconds, with each infected machine assigned a unique X-Agent-ID to identify the victim. QUICAgent is fairly basic in that it supports five commands to execute commands, transfer files, browse directories, and modify the beacon interval.

Persistence is achieved by setting up an LNK file in the current user's Windows Startup folder so that it's automatically executed the next time the user logs in to the system.

"The campaign uses a multi-stage infection chain that begins with a malicious LNK file, abuses ftp.exe as a LOLBAS to execute the next stage, reconstructs the payload from two fake document files, and finally deploys a custom Go-based backdoor that we have named QUICAgent," the Indian cybersecurity company said.

The disclosure comes as the China-linked Mustang Panda actor has been observed using an updated version of a known backdoor called
[COOLCLIENT](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html)
that can deploy a signed kernel-mode driver ("Msagent.sys"), similar to the kernel-mode enhancements identified in
[TONESHELL](https://thehackernews.com/2025/12/mustang-panda-uses-signed-kernel-driver.html)
. The backdoor is assessed to be deployed via PlugX using DLL sideloading, a technique extensively abused by the hacking group.

COOLCLIENT supports such a wide array of capabilities as keylogging, clipboard theft, credential harvesting, file management, system reconnaissance, and plugin-based extensions. It was first detected in the wild in 2022.

"The driver enhances the malware's stealth by hiding the COOLCLIENT process, protecting related files and registry entries, and preventing them from being inspected or modified," Kaspersky
[said](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)
, adding it detected the updated variant and its accompanying driver in intrusions across Myanmar, Mongolia, Pakistan, and Russia.

"While the overall execution flow remains consistent with previously documented COOLCLIENT variants, this sample introduces a previously undocumented kernel-mode driver that significantly expands the malware's stealth capabilities."