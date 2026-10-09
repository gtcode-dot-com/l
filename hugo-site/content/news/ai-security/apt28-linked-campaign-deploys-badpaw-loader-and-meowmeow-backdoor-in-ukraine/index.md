---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-06T20:36:05.157522+00:00'
exported_at: '2026-03-06T20:36:08.159530+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html
structured_data:
  about: []
  author: ''
  description: Researchers uncover APT28-linked phishing attacks against Ukrainian
    targets deploying BadPaw loader and MeowMeow backdoor for remote system control.
  headline: APT28-Linked Campaign Deploys BadPaw Loader and MeowMeow Backdoor in Ukraine
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: APT28-Linked Campaign Deploys BadPaw Loader and MeowMeow Backdoor in Ukraine
updated_at: '2026-03-06T20:36:05.157522+00:00'
url_hash: c7c69b7a3f172cb3eb7e21855c93f5c08c8071b9
---

**

Ravie Lakshmanan
**

Mar 05, 2026

Cyber Espionage / Threat Intelligence

Cybersecurity researchers have disclosed details of a new Russian cyber campaign that has targeted Ukrainian entities with two previously undocumented malware families named
**BadPaw**
and
**MeowMeow**
.

"The attack chain initiates with a phishing email containing a link to a ZIP archive. Once extracted, an initial HTA file displays a lure document written in Ukrainian concerning border crossing appeals to deceive the victim," ClearSky
[said](https://www.clearskysec.com/russian-campaign-targeting-ukraine-badpaw-and-meowmeow/)
in a report published this week.

In parallel, the attack chain leads to the deployment of a .NET-based loader called BadPaw, which then establishes communication with a remote server to fetch and deploy a sophisticated backdoor called MeowMeow.

The campaign has been attributed with moderate confidence to the Russian state-sponsored threat actor known as
[APT28](https://thehackernews.com/2026/03/apt28-tied-to-cve-2026-21513-mshtml-0.html)
, based on the targeting footprint, the geopolitical nature of the lures used, and overlaps with techniques observed in previous Russian cyber operations.

The starting point of the attack sequence is a phishing email sent from ukr[.]net, likely in an attempt to establish credibility and secure the trust of targeted victims. Present in the message is a link to a purported ZIP file, causing the user to be redirected to a URL that loads an "exceptionally small image," effectively acting as a tracking pixel to signal the operators that the link was clicked.

Once this step is complete, the victim is redirected to a secondary URL from where the archive is downloaded. The ZIP file includes an HTML Application (HTA) that, once launched, drops a decoy document as a distraction mechanism, while it executes follow-on stages in the background.

"The dropped decoy document serves as a social engineering tactic, presenting a confirmation of receipt for a government appeal regarding a Ukrainian border crossing," ClearSky said. "This lure is intended to maintain the veneer of legitimacy."

The HTA file also carries out checks to avoid running within sandbox environments. It does this by querying the Windows Registry key "KLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\InstallDate" to estimate the "age" of the operating system. The malware is designed to abort execution if the system was installed less than ten days prior.

Should the system meet the environment criteria, the malware locates the downloaded ZIP archive and extracts two files from it – a Visual Basic Script (VBScript) and a PNG image – and saves them to disk under different names. It also creates a scheduled task to execute the VBScript as a way of ensuring persistence on the infected system.

The primary responsibility of the VBScript is to extract malicious code embedded within the PNG image, an obfuscated loader referred to as BadPaw that's capable of contacting a command-and-control (C2) server to download additional components, including an executable named MeowMeow.

"Consistent with the 'BadPaw' tradecraft, if this file is executed independently of the full attack chain, it initiates a dummy code sequence," the Israeli cybersecurity company explained. "This decoy execution displays a graphical user interface (GUI) featuring a picture of a cat, aligning with the visual theme of the initial image file from which the primary malware was extracted."

"When the 'MeowMeow' button within the decoy GUI is clicked, the application simply displays a 'Meow Meow Meow' message, performing no further malicious actions. This serves as a secondary functional decoy to mislead manual analysis."

The backdoor's malicious code is activated only when it's executed with a certain parameter ("-v") that's provided by the initial infection chain, and after checking that it's running on an actual endpoint as opposed to a sandbox, and no forensic and monitoring tools like Wireshark, Procmon, Ollydbg, and Fiddler are running in the background.

At its core, MeowMeow is equipped to remotely execute PowerShell commands on the compromised host and support file system operations, such as the ability to read, write, and delete data. ClearSky said it identified Russian language strings in the source code, reinforcing the assessment that the activity is the work of a Russian-speaking threat actor.

"The presence of these Russian-language strings suggests two possibilities: the threat actor committed an operational security (OPSEC) error by failing to localize the code for the Ukrainian target environment, or they inadvertently left Russian development artifacts within the code during the malware's production phase," it said.