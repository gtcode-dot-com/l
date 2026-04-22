---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-22T16:15:14.090238+00:00'
exported_at: '2026-04-22T16:15:16.259958+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html
structured_data:
  about: []
  author: ''
  description: Harvester deploys Linux GoGra via Microsoft Graph API in South Asia,
    targeting India and Afghanistan since 2021, enabling covert espionage
  headline: Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph
    API
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/harvester-deploys-linux-gogra-backdoor.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Harvester Deploys Linux GoGra Backdoor in South Asia Using Microsoft Graph
  API
updated_at: '2026-04-22T16:15:14.090238+00:00'
url_hash: 0772643485d90db65af50e83a9f498af51e514f5
---

**

Ravie Lakshmanan
**

Apr 22, 2026

Cyber Espionage / Malware

The threat actor known as
**Harvester**
has been attributed to a new Linux version of its
**GoGra**
backdoor deployed as part of attacks likely targeting entities in South Asia.

"The malware uses the legitimate Microsoft Graph API and Outlook mailboxes as a covert command-and-control (C2) channel, allowing it to bypass traditional perimeter network defenses," the Symantec and Carbon Black Threat Hunter Team
[said](https://www.security.com/threat-intelligence/harvester-new-linux-backdoor-gogra)
in a report shared with The Hacker News.

The cybersecurity company said it identified artifacts uploaded to the VirusTotal platform from India and Afghanistan, suggesting that the two countries may be the target of the espionage activity.

Harvester was first
[publicly documented](https://thehackernews.com/2021/10/lightbasin-hackers-breach-at-least-13.html)
by Symantec in late 2021, linking it to an information-stealing campaign aimed at telecommunications, government, and information technology sectors in South Asia since June 2021, using a bespoke implant called Graphon that used the Microsoft Graph API for C2.

Subsequent activity flagged in August 2024
[connected](https://thehackernews.com/2024/08/new-go-based-backdoor-gogra-targets.html)
the hacking group to an attack targeting an unnamed media organization in South Asia with a never-before-seen Go-based backdoor called GoGra. The latest findings suggest that the adversary is continuing to expand its toolset beyond Windows and infecting Linux machines with a new variant of the same backdoor.

The attacks employ social engineering to trick victims into opening ELF binaries disguised as PDF documents. The dropper then proceeds to display a lure document while stealthily running the backdoor.

Like its Windows counterpart, the Linux version of GoGra abuses Microsoft's cloud infrastructure to contact a specific Outlook mailbox folder named "Zomato Pizza" every two seconds using Open Data Protocol (OData) queries. The backdoor scans the inbox for incoming email messages with a subject line starting with the word "Input."

Once an email matching the criteria is received, it decrypts the Base64-encoded message body and executes it as shell commands using "/bin/bash." The results of the execution are sent back to the operator in an email message with the subject line "Output." After the exfiltration step is complete, the implant wipes the original tasking message to cover up the tracks.

"Despite using different deployment architectures and operating systems, the underlying C2 logic remains unchanged," Symantec and Carbon Black said, adding the teams "also identified several matching, hard-coded spelling errors across both platforms, which points towards the same developer being behind both tools."

"The use of a new Linux backdoor shows that Harvester is continuing to expand its toolset and actively develop new tooling in order to go after a wider range of victims and machines."