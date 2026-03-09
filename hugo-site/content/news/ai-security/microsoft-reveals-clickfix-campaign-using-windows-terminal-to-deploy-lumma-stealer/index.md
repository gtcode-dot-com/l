---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-09T23:40:00.998362+00:00'
exported_at: '2026-03-09T23:40:02.585856+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/microsoft-reveals-clickfix-campaign.html
structured_data:
  about: []
  author: ''
  description: Microsoft reveals ClickFix campaign abusing Windows Terminal to deliver
    Lumma Stealer and steal browser credentials.
  headline: Microsoft Reveals ClickFix Campaign Using Windows Terminal to Deploy Lumma
    Stealer
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/microsoft-reveals-clickfix-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Reveals ClickFix Campaign Using Windows Terminal to Deploy Lumma
  Stealer
updated_at: '2026-03-09T23:40:00.998362+00:00'
url_hash: dff65c3e89fb7085b58e9132cbd00441bbd3ba23
---

**

Ravie Lakshmanan
**

Mar 06, 2026

Endpoint Security / Browser Security

Microsoft on Thursday disclosed details of a new widespread
[ClickFix](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)
social engineering campaign that has leveraged the
[Windows Terminal app](https://en.wikipedia.org/wiki/Windows_Terminal)
as a way to activate a sophisticated attack chain and deploy the
[Lumma Stealer](https://thehackernews.com/2024/06/beware-fake-browser-updates-deliver.html)
malware.

The activity, observed in February 2026, makes use of the terminal emulator program instead of instructing users to launch the Windows Run dialog and paste a command into it.

"This campaign instructs targets to use the Windows + X → I shortcut to launch Windows Terminal (wt.exe) directly, guiding users into a privileged command execution environment that blends into legitimate administrative workflows and appears more trustworthy to users," the Microsoft Threat Intelligence team
[said](https://x.com/MsftSecIntel/status/2029692925118992473)
in a series of posts on X.

What makes the latest variant notable is that it bypasses detections specifically designed to flag Run dialog abuse, not to mention take advantage of the legitimacy of Windows Terminal to trick unsuspecting users into running malicious commands delivered via bogus CAPTCHA pages, troubleshooting prompts, or other verification-style lures.

The post-compromise attack chain is also unique: when the user pastes a hex-encoded, XOR-compressed command copied from the ClickFix lure page into a Windows Terminal session, it spans additional Terminal/PowerShell instances to ultimately invoke a PowerShell process responsible for decoding the script.

This, in turn, leads to the download of a ZIP payload and a legitimate but renamed 7-Zip binary, the latter of which is saved to disk with a randomized file name. The utility then proceeds to extract the contents of the ZIP file, triggering a multi-stage attack chain that involves the following steps -

* Retrieving more payloads
* Setting up persistence via scheduled tasks
* Configuring Microsoft Defender exclusions
* Exfiltrating machine and network data
* Deploying Lumma Stealer using a technique called
  [QueueUserAPC()](https://nyameeeain.medium.com/queueuserapc-process-injection-6f31fcb89410)
  by injecting the malware into "chrome.exe" and "msedge.exe" processes

"The stealer targets high-value browser artifacts, including Web Data and Login Data, harvesting stored credentials and exfiltrating them to attacker-controlled infrastructure," Microsoft said.

The Windows maker said it also detected a second attack pathway, as part of which, when the compressed command is pasted into Windows Terminal, it downloads a randomly named batch script to the "AppData\Local" folder by means of "cmd.exe" in order to write a Visual Basic Script to the Temp folder (aka %TEMP%).

"The batch script is then executed via cmd.exe with the /launched command-line argument. The same batch script is then executed through MSBuild.exe, resulting in LOLBin abuse," it added. "The script connects to Crypto Blockchain RPC endpoints, indicating an etherhiding technique. It also performs QueueUserAPC()-based code injection into chrome.exe and msedge.exe processes to harvest Web Data and Login Data."