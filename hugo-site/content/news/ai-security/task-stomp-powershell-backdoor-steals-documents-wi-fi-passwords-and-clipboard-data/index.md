---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:28:48.904317+00:00'
exported_at: '2026-10-03T23:28:50.995146+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html
structured_data:
  about: []
  author: ''
  description: TASK#STOMP deploys a PowerShell backdoor that steals documents and
    Wi-Fi passwords, monitors files, and executes remote commands.
  headline: TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and
    Clipboard Data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/taskstomp-powershell-backdoor-steals.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: TASK#STOMP PowerShell Backdoor Steals Documents, Wi-Fi Passwords, and Clipboard
  Data
updated_at: '2026-10-03T23:28:48.904317+00:00'
url_hash: 1554d5146d5bf901446579111c7386c2cb160a8b
---

**

Ravie Lakshmanan
**

Sep 21, 2026

Endpoint Security / Malware

Cybersecurity researchers have disclosed details of a new campaign dubbed
**TASK#STOMP**
that delivers a PowerShell backdoor designed to harvest sensitive data from compromised hosts.

The backdoor "automatically harvests and exfiltrates business documents, watches the filesystem for new files in real time, steals Wi-Fi passwords and clipboard contents, takes screenshots, and accepts arbitrary remote commands through two redundant, token-authenticated C2 servers," Securonix researchers Akshay Gaikwad and Aaron Beardslee
[said](https://www.securonix.com/blog/task-stomp-powershell-backdoor-document-theft-remote-access)
in a report shared with The Hacker News.

The starting point of the infection chain is the use of "wscript.exe" to execute an encoded Visual Basic Script (VBScript) file staged on the victim's desktop ("95c9050t66.vbs"). The exact initial access pathway used to deliver the payload is unclear, although it's possible that it may have been via email-based phishing or social engineering.

By giving it a completely random file name, it's suspected that the intention may have been to evade file name-based detection mechanisms. The VBScript functions as the orchestrator for establishing persistence on the host using scheduled tasks and launching subsequent stages.

The tasks are given the names Local Credential Manager, Network Audio Service, Windows Display Manager, and Device Credential Handler so as to blend in with regular operating system activity and avoid raising any red flags.

The VBScript installer also sets up a backup persistence method that uses the Windows Startup folder to launch another script payload ("msdiag.vbs") every time the user logs in to the system. In the next phase, the malware executes PowerShell commands to forcibly terminate previously running instances and ensure there exists only one active session

These strategies, paired with deliberate timestamp modification (aka timestomping), hidden execution, and cleanup behavior, suggest a deliberate effort to get around superficial administrative reviews and complicate forensic analysis. The use of redundant persistence methods guarantees continued execution even if one of them fails or is detected and removed.

The next phase involves running a pair of hidden PowerShell commands -

* sys\_loader.ps1, which decodes "diag\_pack.dat" and initiates the document-stealing, surveillance, and remote-access payload to steal system metadata, business documents, Wi-Fi passwords, and clipboard content, monitor for newly modified files, take screenshots, and execute arbitrary PowerShell commands win\_conn.ps1, which decodes "win\_conn\_cfg.dat" and sets up a secondary, persistent C2 channel with command execution and collection capabilities

"Running the modules as separate processes provides functional separation and operational redundancy: failure or termination of one branch does not immediately remove the other," Securonix said.

Both the modules communicate with the same C2 infrastructure ("corecloudfileshare[.]xyz" or "attachmentsharingdrive[.]xyz"). Interestingly, the two components incorporate a mutual-watchdog relationship in which "diag\_pack.dat" checks if "win\_conn.ps1" is running, and restart it if not, and vice versa.

The end goal of the attack is to provide a pathway for continuous document collection, credential and clipboard theft, screenshot capture, redundant C2 communications, and arbitrary code execution, while leveraging an array of techniques to fly under the radar.

In the final stage, the VBScript orchestrator opens Google Chrome in a maximized window and opens a specific URL from "irantenders[.]com," which hosts a searchable database of all tenders and contracts issued by government departments and local authorities in Iran. The purpose behind this user-facing web action is unknown.

Also launched is a batch script ("purge.bat") that invokes a two-second delay and likely performs a clean-up to erase traces of the malicious activity. That said, what this batch script does is unknown as its contents have not been recovered.

"Threat actors routinely abuse Windows Script Host, PowerShell, Task Scheduler, and the .NET toolchain to blend malicious execution with legitimate administrative activity," the researchers said.

"TASK#STOMP demonstrates this approach through a VBS-controlled framework that installs multiple persistence anchors and delegates follow-on functionality to PowerShell and dynamically compiled C# code. By relying almost entirely on native Windows components, the operation reduces its dependence on conventional executable payloads and makes individual events more difficult to distinguish from benign system activity."