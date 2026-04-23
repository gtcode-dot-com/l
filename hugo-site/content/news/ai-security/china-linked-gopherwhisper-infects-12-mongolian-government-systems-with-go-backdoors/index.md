---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T10:15:14.162055+00:00'
exported_at: '2026-04-23T10:15:16.790352+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/china-linked-gopherwhisper-infects-12.html
structured_data:
  about: []
  author: ''
  description: GopherWhisper infected 12 Mongolian government systems in January 2025,
    abusing Slack and Discord for C2, exposing wider espionage risks.
  headline: China-Linked GopherWhisper Infects 12 Mongolian Government Systems with
    Go Backdoors
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/china-linked-gopherwhisper-infects-12.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked GopherWhisper Infects 12 Mongolian Government Systems with Go
  Backdoors
updated_at: '2026-04-23T10:15:14.162055+00:00'
url_hash: 5171ff98ef351e5e12cac06d86b6e978c3b87d55
---

**

Ravie Lakshmanan
**

Apr 23, 2026

Threat Intelligence / Malware

Mongolian governmental institutions have emerged as the target of a previously undocumented China-aligned advanced persistent threat (APT) group tracked as
**GopherWhisper**
.

"The group wields a wide array of tools mostly written in Go, using injectors and loaders to deploy and execute various backdoors in its arsenal," Slovakian cybersecurity company ESET
[said](https://www.welivesecurity.com/en/eset-research/gopherwhisper-burrow-full-malware/)
in a report shared with The Hacker News. "GopherWhisper abuses legitimate services, notably Discord, Slack, Microsoft 365 Outlook, and file.io for command-and-control (C&C) communication and exfiltration."

The group was first discovered in January 2025 following the discovery of a never-before-seen backdoor codenamed LaxGopher on a system belonging to a Mongolian governmental entity. Also discovered as part of the threat actor's arsenal are a number of other malware families, mostly developed using Golang to receive instructions from the C&C server, execute them, and send the results back.

Also used by the threat actor is a file collection tool to gather files of interest and exfiltrate them in compressed format to the file[.]io file sharing service and a C++ backdoor that offers remote control over compromised hosts.

Telemetry data from ESET shows that about 12 systems associated with the Mongolian governmental institution were infected by the backdoors, with C&C traffic from the attacker-controlled Discord and Slack servers indicating dozens of other victims.

Exactly how GopherWhisper obtains initial access to the target networks is currently not known. But a successful foothold is followed by attempts to deploy a wide range of tools and implants -

* **JabGopher**
  , an injector that executes the LaxGopher ("whisper.dll") backdoor.
* **LaxGopher**
  , a Go-based backdoor that uses Slack for C2 to execute commands via "cmd.exe" and publish the results back to the Slack channel, as well as download additional malware.
* **CompactGopher**
  , a Go-based file collection utility dropped by LaxGopher to filter files of interest by extensions (.doc, .docx, .jpg, .xls, .xlsx, .txt, .pdf, .ppt, and .pptx.), compress them into ZIP files, encrypt the archives using AES-CFB-128, and exfiltrate them to file[.]io.
* **RatGopher**
  , a Go-based backdoor that uses a private Discord server to receive C&C messages, execute commands, and publish the results back to the configured Discord channel, as well as upload and download files from file[.]io.
* **SSLORDoor**
  , a C++-based backdoor that uses OpenSSL BIO for communication via raw sockets on port 443 to enumerate drives, perform file operations, and run commands based on C&C input via "cmd.exe."
* **FriendDelivery**
  , a malicious DLL that serves as a loader and injector for BoxOfFriends.
* **BoxOfFriends**
  , a Go-based backdoor that uses the Microsoft Graph API to craft draft emails for C2 using hard-coded credentials, with the earliest Outlook account created for this purpose ("barrantaya.1010@outlook[.]com") created on July 11, 2024.

"Timestamp inspection of the Slack and Discord messages showed us that the bulk of them were being sent during working hours, i.e., between 8 a.m. and 5 p.m., which aligns with China Standard Time," ESET researcher Eric Howard said. "Furthermore, the locale for the configured user in Slack metadata was also set to this time zone. We therefore believe that GopherWhisper is a China-aligned group."