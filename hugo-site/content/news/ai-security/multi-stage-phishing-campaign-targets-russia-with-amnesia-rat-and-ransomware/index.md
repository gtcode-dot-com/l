---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-24T12:15:12.675975+00:00'
exported_at: '2026-01-24T12:15:15.161655+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/multi-stage-phishing-campaign-targets.html
structured_data:
  about: []
  author: ''
  description: A multi-stage phishing campaign targeting Russia abuses GitHub and
    Dropbox to disable Microsoft Defender and deploy Amnesia RAT and ransomware.
  headline: Multi-Stage Phishing Campaign Targets Russia with Amnesia RAT and Ransomware
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/multi-stage-phishing-campaign-targets.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Multi-Stage Phishing Campaign Targets Russia with Amnesia RAT and Ransomware
updated_at: '2026-01-24T12:15:12.675975+00:00'
url_hash: 10010c34e87febe7b835d199c760e81f26f99d1a
---

A new multi-stage phishing campaign has been observed targeting users in Russia with ransomware and a remote access trojan called Amnesia RAT.

"The attack begins with social engineering lures delivered via business-themed documents crafted to appear routine and benign," Fortinet FortiGuard Labs researcher Cara Lin
[said](https://www.fortinet.com/blog/threat-research/inside-a-multi-stage-windows-malware-campaign)
in a technical breakdown published this week. "These documents and accompanying scripts serve as visual distractions, diverting victims to fake tasks or status messages while malicious activity runs silently in the background."

The campaign stands out for a couple of reasons. First, it uses multiple public cloud services to distribute different kinds of payloads. While GitHub is mainly used to distribute scripts, binary payloads are staged on Dropbox. This separation complicates takedown efforts, effectively improving resilience.

Another "defining characteristic" of the campaign, per Fortinet, is the operational abuse of
[defendnot](https://thehackernews.com/2025/05/weekly-recap-zero-day-exploits-insider.html#:~:text=New%20%22defendnot%22%20Tool%20Can%20Disable%20Windows%20Defender)
to disable Microsoft Defender.
[Defendnot](https://binarydefense.com/resources/blog/defendnot-turning-windows-defender-against-itself)
was
[released](https://www.huntress.com/blog/defendnot-detecting-malicious-security-product-bypass-techniques)
last year by a security researcher who goes by the online alias es3n1n as a way to trick the security program into believing another antivirus product has already installed on the Windows host.

The campaign leverages social engineering to distribute compressed archives, which contain multiple decoy documents and a malicious Windows shortcut (LNK) with Russian-language filenames. The LNK file uses a double extension ("Задание\_для\_бухгалтера\_02отдела.txt.lnk") to give the impression that it's a text file.

When executed, it runs a PowerShell command to retrieve the next-stage PowerShell script hosted on a GitHub repository ("github[.]com/Mafin111/MafinREP111"), which then serves as a first-stage loader to establish a foothold, readies the system to hide evidence of malicious activity, and hands off control flow to subsequent stages.

"The script first suppresses visible execution by programmatically hiding the PowerShell console window," Fortinet said. "This removes any immediate visual indicators that a script is running. It then generates a decoy text document in the user's local application data directory. Once written to disk, the decoy document is automatically opened."

Once the document is displayed to the victim to keep up the ruse, the script sends a message to the attacker using the
[Telegram Bot API](https://core.telegram.org/bots/api)
, informing the operator that the first stage has been successfully executed. A deliberately-introduced 444 second delay later, the PowerShell script runs a Visual Basic Script ("SCRRC4ryuk.vbe") hosted at the same repository location.

This offers two crucial advantages in that it keeps the loader lightweight and allows the threat actors to update or replace the payload's functionality on the fly without having to introduce any changes to the attack chain itself.

The Visual Basic Script is highly obfuscated and acts as the controller that assembles the next-stage payload directly in memory, thereby avoiding leaving any artifacts on disk. The final-stage script checks if it's running with elevated privileges, and, if not, repeatedly displays a User Account Control (
[UAC](https://thehackernews.com/2026/01/fake-booking-emails-redirect-hotel.html)
) prompt to force the victim to grant it the necessary permissions. The script pauses for 3,000 milliseconds between attempts.

In the next phase, the malware initiates a series of actions to suppress visibility, neutralize endpoint protection mechanisms, conduct reconnaissance, inhibit recovery, and ultimately deploy the main payloads -

* Configure Microsoft Defender exclusions to prevent the program from scanning ProgramData, Program Files, Desktop, Downloads, and the system temporary directory
* Use PowerShell to turn off additional Defender protection components
* Deploy defendnot to register a fake antivirus product with the Windows Security Center interface and cause Microsoft Defender to disable itself to avoid potential conflicts
* Conduct environment reconnaissance and surveillance via screenshot capture by means of a dedicated .NET module downloaded from the GitHub repository that takes a screengrab every 30 seconds, save it as a PNG image, and exfiltrates the data using a Telegram bot
* Disable Windows administrative and diagnostic tools by tampering with the Registry-based policy controls
* Implement a file association hijacking mechanism such that opening files with certain predefined extensions causes a message to be displayed to the victim, instructing them to contact the threat actor via Telegram

One of the final payloads deployed after successfully disarming security controls and recovery mechanisms is Amnesia RAT ("svchost.scr"), which is retrieved from Dropbox and is capable of broad data theft and remote control. It's designed to pilfer information stored in web browsers, cryptocurrency wallets, Discord, Steam, and Telegram, along with system metadata, screenshots, webcam images, microphone audio, clipboard, and active window title.

"The RAT enables full remote interaction, including process enumeration and termination, shell command execution, arbitrary payload deployment, and execution of additional malware," Fortinet said. "Exfiltration is primarily performed over HTTPS using Telegram Bot APIs. Larger datasets may be uploaded to third-party file-hosting services such as GoFile, with download links relayed to the attacker via Telegram."

In all, Amnesia RAT facilitates credential theft, session hijacking, financial fraud, and real-time data gathering, turning it into a comprehensive tool for account takeover and follow-on attacks.

The second payload delivered by the script is a ransomware that's derived from the Hakuna Matata ransomware family and is configured to encrypt documents, archives, images, media, source code, and application assets on the infected endpoint, but not before terminating any process that could interfere with its functioning.

In addition, the ransomware keeps tabs on clipboard contents and silently modifies cryptocurrency wallet addresses with attacker-controlled wallets to reroute transactions. The infection sequence ends with the script deploying WinLocker to restrict user interaction.

"This attack chain demonstrates how modern malware campaigns can achieve full system compromise without exploiting software vulnerabilities," Lin concluded. "By systematically abusing native Windows features, administrative tools, and policy enforcement mechanisms, the attacker disables endpoint defenses before deploying persistent surveillance tooling and destructive payloads."

To counter defendnot's abuse of the Windows Security Center API, Microsoft
[recommends](https://learn.microsoft.com/en-us/answers/questions/2286851/microsoft-defender-vs-defendnot)
that users enable Tamper Protection to prevent unauthorized changes to Defender settings and monitor for suspicious API calls or Defender service changes.

The development comes as human resources, payroll, and internal administrative departments belonging to Russian corporate entities have been targeted by a threat actor UNG0902 to deliver an unknown implant dubbed DUPERUNNER that's responsible for loading
[AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
, a command-and-control (C2) framework. The spear-phishing campaign, codenamed Operation DupeHike, has been ongoing since November 2025.

Seqrite Labs
[said](https://www.seqrite.com/blog/operation-dupehike-ung0902-targets-russian-employees-with-duperunner-and-adaptixc2/)
the attacks involve the use of decoy documents centered around themes related to employee bonuses and internal financial policies to convince recipients into opening a malicious LNK file within ZIP archives that leads to the execution of DUPERUNNER.

The implant reaches out to an external server to fetch and display a decoy PDF document, while system profiling and the download of the AdaptixC2
[beacon](https://adaptix-framework.gitbook.io/adaptix-framework/extenders/agents/beacon)
are carried out in the background.

In recent months, Russian organizations have also been likely targeted by another threat actor tracked as
[Paper Werewolf](https://thehackernews.com/2025/04/paper-werewolf-deploys-powermodul.html)
(aka GOFFEE), which has employed artificial intelligence (AI)-generated decoys and DLL files compiled as
[Excel XLL add-ins](https://thehackernews.com/2025/10/ukraine-warns-of-cabinetrat-backdoor.html)
to deliver a backdoor referred to as EchoGather.

"Once launched, the backdoor collects system information, communicates with a hardcoded command-and-control (C2) server, and supports command execution and file transfer operations," Intezer security researcher Nicole Fishbein
[said](https://intezer.com/blog/tracing-a-paper-werewolf-campaign-through-ai-generated-decoys-and-excel-xlls/)
. It "communicates with the C2 over HTTP(S) using the WinHTTP API."