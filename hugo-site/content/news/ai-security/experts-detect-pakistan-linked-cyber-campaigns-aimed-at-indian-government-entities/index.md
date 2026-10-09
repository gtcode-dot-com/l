---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-27T18:15:13.528129+00:00'
exported_at: '2026-01-27T18:15:15.809457+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html
structured_data:
  about: []
  author: ''
  description: Pakistan-linked hackers targeted Indian government entities using phishing,
    Google services, Golang malware, and GitHub-based command-and-control.
  headline: Experts Detect Pakistan-Linked Cyber Campaigns Aimed at Indian Government
    Entities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/experts-detect-pakistan-linked-cyber.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Experts Detect Pakistan-Linked Cyber Campaigns Aimed at Indian Government Entities
updated_at: '2026-01-27T18:15:13.528129+00:00'
url_hash: 19bf10bb1e4bd55c3bb620dd04435ecae7d135e9
---

**

Ravie Lakshmanan
**

Jan 27, 2026

Threat Intelligence / Cyber Espionage

Indian government entities have been targeted in two campaigns undertaken by a threat actor that operates in Pakistan using previously undocumented tradecraft.

The campaigns have been codenamed
**Gopher Strike**
and
**Sheet Attack**
by Zscaler ThreatLabz, which identified them in September 2025.

"While these campaigns share some similarities with the Pakistan-linked Advanced Persistent Threat (APT) group,
[APT36](https://thehackernews.com/2025/10/apt36-targets-indian-government-with.html)
, we assess with medium confidence that the activity identified during this analysis might originate from a new subgroup or another Pakistan-linked group operating in parallel," researchers Sudeep Singh and Yin Hong Chang
[said](https://www.zscaler.com/blogs/security-research/apt-attacks-target-indian-government-using-gogitter-gitshellpad-and-goshell)
.

Sheet Attack gets its name from the use of legitimate services like Google Sheets, Firebase, and email for command-and-control (C2). On the other hand, Gopher Strike is assessed to have leveraged phishing emails as a starting point to deliver PDF documents containing a blurred image that's superimposed by a seemingly harmless pop-up instructing the recipient to download an update for Adobe Acrobat Reader DC.

The main purpose of the image is to give the users an impression that it's necessary to install the update in order to access the document's contents. Clicking the "Download and Install" button in the fake update dialog triggers the download of an ISO image file only when the requests originate from IP addresses located in India and the
[User-Agent string](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent)
corresponds to Windows.

"These server-side checks prevent automated URL analysis tools from fetching the ISO file, ensuring that the malicious file is only delivered to intended targets," Zscaler said.

The malicious payload embedded within the ISO image is a Golang-based downloader dubbed GOGITTER that's responsible for creating a Visual Basic Script (VBScript) file if it does not already exist in the following locations: "C:\Users\Public\Downloads," "C:\Users\Public\Pictures," and "%APPDATA%." The script is designed to fetch VBScript commands every 30 seconds from two pre-configured C2 servers.

GOGITTER also sets up persistence using a scheduled task that's configured to run the aforementioned VBScript file every 50 minutes. In addition, it ascertains the presence of another file named "adobe\_update.zip" in the same three folders. If the ZIP file is not present, it pulls the archive from a private GitHub repository ("github[.]com/jaishankai/sockv6"). The GitHub account was created on June 7, 2025.

Once the download is successful, the attack chain sends an HTTP GET request to the domain "adobe-acrobat[.]in" likely to signal the threat actors that the endpoint has been infected. GOGITTER then extracts and executes "edgehost.exe" from the ZIP file. A lightweight Golang-based backdoor, GITSHELLPAD, leverages threat actor-controlled private GitHub repositories for C2.

Specifically, it polls the C2 server every 15 seconds by means of a GET request to access the contents of a file named "command.txt." It supports six different commands -

* **cd ..**
  , to change working directory to the parent directory
* **cd**
  , to change directory to the specified path
* **run**
  , to run a command in the background without capturing the output
* **upload**
  , to upload a local file specified by the path to the GitHub repository
* **download**
  , to download a file to the specified path
* **default case**
  , to run a command using cmd /c and capture the output

The results of the command execution are stored in a file called "result.txt" and uploaded to the GitHub account via an HTTP PUT request. The "command.txt" is then deleted from the GitHub repository once the command is successfully executed.

Zscaler said it observed the threat actor also downloading RAR archives using cURL commands after gaining access to the victim's machine. The archives include utilities to gather system information and drop GOSHELL, a bespoke Golang-based loader used to deliver Cobalt Strike Beacon after multiple rounds of decoding. The tools are wiped from the machine after use.

"GOSHELL's size was artificially inflated to approximately 1 gigabyte by adding junk bytes to the Portable Executable (PE) overlay, likely to evade detection by antivirus software," the cybersecurity company said. "GOSHELL only executes on specific hostnames by comparing the victim's hostname against a hard-coded list."