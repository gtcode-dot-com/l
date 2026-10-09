---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T00:50:02.337183+00:00'
exported_at: '2025-11-13T00:50:03.626684+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html
structured_data:
  about: []
  author: ''
  description: Konni and Lazarus launch new North Korea-linked attacks using RATs,
    fake lures, and Google exploits.
  headline: Konni Hackers Turn Google’s Find Hub into a Remote Data-Wiping Weapon
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/konni-hackers-turn-googles-find-hub.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Konni Hackers Turn Google’s Find Hub into a Remote Data-Wiping Weapon
updated_at: '2025-11-13T00:50:02.337183+00:00'
url_hash: a782d1e22822e09837f0b083e86e5a0c7391c719
---

The North Korea-affiliated threat actor known as
**[Konni](https://thehackernews.com/2025/05/north-korean-konni-apt-targets-ukraine.html)**
(aka Earth Imp, Opal Sleet, Osmium, TA406, and Vedalia) has been attributed to a new set of attacks targeting both Android and Windows devices for data theft and remote control.

"Attackers impersonated psychological counselors and North Korean human rights activists, distributing malware disguised as stress-relief programs," the Genians Security Center (GSC)
[said](https://www.genians.co.kr/en/blog/threat_intelligence/android)
in a technical report.

What's notable about the attacks targeting Android devices is also the destructive ability of the threat actors to exploit Google's asset tracking services Find Hub (formerly Find My Device) to remotely reset victim devices, thereby leading to the unauthorized deletion of personal data. The activity was detected in early September 2025.

The development marks the first time the
[hacking group](https://www.genians.co.kr/blog/threat_intelligence/konni_disguise)
has weaponized legitimate management functions to remotely reset mobile devices. The activity is also preceded by an attack chain in which the attackers approach targets via spear-phishing emails to obtain access to their computers, and leverage their logged-in KakaoTalk chat app sessions to distribute the malicious payloads to their contacts in the form of a ZIP archive.

The spear-phishing emails are said to mimic legitimate entities like the National Tax Service to deceive recipients into opening malicious attachments to deliver remote access trojans like
[Lilith RAT](https://thehackernews.com/2024/09/developers-beware-lazarus-group-uses.html)
that can remotely commandeer compromised machines and deliver additional payloads.

|  |
| --- |
|  |
| Konni Attack Flow |

"The threat actor stayed hidden in the compromised computer for over a year, spying via the webcam and operating the system when the user was absent," GSC noted. "In this process, the access obtained during the initial intrusion enables system control and additional information collection, while evasion tactics allow long-term concealment."

The deployed malware on the victim's computer allows the threat actors to carry out internal reconnaissance and monitoring, as well as exfiltrate victims' Google and Naver account credentials. The stolen Google credentials are then used to log in to Google's Find Hub and initiate a remote wipe of their devices.

In one case, the attackers have been found to sign into a recovery email account registered under Naver, delete security alert emails from Google, and empty the inbox's trash folder to cover up traces of the nefarious activity.

The ZIP file propagated via the messaging app contains a malicious Microsoft Installer (MSI) package ("Stress Clear.msi"), which abuses a valid signature issued to a Chinese company to give the application an illusion of legitimacy. Once launched, it invokes a batch script to perform initial setup and proceeds to run a Visual Basic Script (VB Script) that displays a fake error message about a language pack compatibility issue, while the malicious commands are executed in the background.

This includes launching an AutoIt script that's configured to run every minute by means of a scheduled task in order to execute additional commands received from an external server ("116.202.99[.]218"). While the malware shares some similarities with Lilith RAT, it has been codenamed EndRAT (also referred to as
[EndClient RAT](https://www.0x0v1.com/endclientrat/)
by security researcher Ovi Liber) due to the differences observed.

The list of supported commands is as follows -

* **shellStart**
  , to start a remote shell session
* **shellStop**
  , to stop remote shell
* **refresh**
  , to send system information
* **list**
  , to list drives or root directory
* **goUp**
  , to move up one directory
* **download**
  , to exfiltrate a file
* **upload**
  , to receive a file
* **run**
  , to execute a program on host
* **delete**
  , to delete a file on host

Genians said the Konni APT actors have also utilized an AutoIt script to launch Remcos RAT version 7.0.4, which was
[released](https://breakingsecurity.net/remcos/changelog/)
by its maintainers, Breaking Security, on September 10, 2025, indicating that the adversary is actively using newer versions of the trojan in its attacks. Also observed on victim devices are Quasar RAT and
[RftRAT](https://thehackernews.com/2023/12/lazarus-group-using-log4j-exploits-to.html)
, another trojan previously put to use by Kimsuky in 2023.

"This suggests that the malware is tailored to Korea-focused operations and that obtaining relevant data and conducting in-depth analysis requires substantial effort," the South Korean cybersecurity company said.

In a statement shared with The Hacker News, a Google spokesperson said the attack does not exploit any security flaw in Android or Find Hub, urging users to enable
[2-Step Verification](https://support.google.com/accounts/answer/185839?hl=en&co=GENIE.Platform%3DAndroid)
or
[passkeys](https://www.google.com/account/about/passkeys/)
to safeguard against credential theft. Users at an elevated risk of targeted attacks because of who they are or what they do are recommended to enroll in Google's
[Advanced Protection Program](https://landing.google.com/intl/en_in/advancedprotection/)
for improved account security.

“This attack did not exploit any security flaw in Android or Find Hub. The report indicates this targeted attack required PC malware to be present in order to steal Google account credentials and abuse legitimate functions in Find Hub,” the spokesperson added.

### Lazarus Group's New Comebacker Variant Detailed

The disclosure comes as ENKI detailed the
[Lazarus Group's](https://thehackernews.com/2025/11/new-httptroy-backdoor-poses-as-vpn.html)
use of an updated version of the Comebacker malware in attacks aimed at aerospace and defense organizations using tailored Microsoft Word document lures consistent with an espionage campaign. The lures impersonate Airbus, Edge Group, and the Indian Institute of Technology Kanpur.

The infection chain kicks off when victims open the file and enable macros, causing the embedded VBA code to execute and deliver a decoy document that's displayed to the user, along with a loader component that's responsible for launching Comebacker in memory.

The malware, for its part, establishes communication with a command-and-control (C2) server over HTTPS and enters into a loop to poll for new commands or download an encrypted payload and execute it.

"The actor's use of highly specific lure documents indicates that this is a targeted spear phishing campaign," ENKI
[said](https://www.enki.co.kr/en/media-center/blog/lazarus-group-targets-aerospace-and-defense-with-new-comebacker-variant)
in a technical report. "Although there are no reports of victims so far, the C2 infrastructure remains active at the time of this publication."

### Kimsuky Uses a New JavaScript Dropper

The findings also coincide with the discovery of a new JavaScript-based malware dropper that has been employed by
[Kimsuky](https://thehackernews.com/2025/04/kimsuky-exploits-bluekeep-rdp.html)
in its recent operations, demonstrating the actor's continued refinement of its malware arsenal. The initial access mechanism by which the JavaScript malware is distributed is currently not known.

|  |
| --- |
|  |
| Kimsuky JavaScript Dropper Flow |

The starting point of the attack is an initial JavaScript file ("themes.js") that contacts an adversary-controlled infrastructure to fetch more JavaScript code that's capable of executing commands, exfiltrating data, and retrieving a third-stage JavaScript payload to create a scheduled task to launch the first JavaScript file every minute and launch an empty Word document, likely as a decoy.

"Since the Word document is empty and does not run any macros in the background, it may be a lure," the Pulsedive Threat Research
[said](https://blog.pulsedive.com/dissecting-the-infection-chain-technical-analysis-of-the-kimsuky-javascript-dropper/)
in an analysis published last week.