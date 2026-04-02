---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T05:34:57.341987+00:00'
exported_at: '2026-04-02T05:34:59.540949+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/casbaneiro-phishing-targets-latin.html
structured_data:
  about: []
  author: ''
  description: Augmented Marauder targets Latin America and Europe since 2020, using
    dynamic PDF phishing to spread Casbaneiro via Horabot.
  headline: Casbaneiro Phishing Targets Latin America and Europe Using Dynamic PDF
    Lures
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/casbaneiro-phishing-targets-latin.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Casbaneiro Phishing Targets Latin America and Europe Using Dynamic PDF Lures
updated_at: '2026-04-02T05:34:57.341987+00:00'
url_hash: ff83746d73bb4a32e7eb1aabc971941e2f96025b
---

**

Ravie Lakshmanan
**

Apr 01, 2026

Malware / Windows Security

A multi-pronged phishing campaign is targeting Spanish-speaking users in organizations across Latin America and Europe to deliver Windows banking trojans like
[Casbaneiro](https://thehackernews.com/2023/07/casbaneiro-banking-malware-goes-under.html)
(aka Metamorfo) via another malware called
[Horabot](https://thehackernews.com/2025/05/horabot-malware-targets-6-latin.html)
.

The activity has been attributed to a Brazilian cybercrime threat actor tracked as
[Augmented Marauder and Water Saci](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html)
. The e-crime group was
[first documented](https://thehackernews.com/2025/11/whatsapp-malware-maverick-hijacks.html)
by Trend Micro in October 2025.

"This threat group employs a wider-ranging attack model focused on a bespoke delivery and propagation mechanism that includes WhatsApp,
[ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
techniques, and email-centric phishing," BlueVoyant security researchers Thomas Elkins and Joshua Green
[said](https://www.bluevoyant.com/blog/augmented-marauders-multi-pronged-casbaneiro-campaigns)
in a technical breakdown published Tuesday.

"It is now evident that while these Brazil-based operators heavily leverage script-based WhatsApp automation to compromise retail and consumer users in Latin America, they concurrently maintain and deploy an advanced, email-hijacking engine to penetrate enterprise perimeters there and Europe as well."

The starting point of the campaign is a phishing email that employs court summons-themed messages to deceive recipients into opening a password-protected PDF attachment. Clicking on an embedded link in the document directs the victim to a malicious link and initiates an automatic download of a ZIP archive, which, in turn, leads to the execution of interim HTML Application (HTA) and VBS payloads.

The VBS script is designed to carry out environment and anti-analysis checks similar to those found in Horabot artifacts, including checks for Avast antivirus software, and proceeds to retrieve next-stage payloads from a remote server. Among the downloaded files are AutoIt-based loaders, each of which extracts and runs encrypted payload files with ".ia" or ".at" extensions to eventually launch two malware families: Casbaneiro ("staticdata.dll") and Horabot ("at.dll").

While Casbaneiro is the primary payload, Horabot is used as a propagation mechanism for the malware. Casbaneiro's Delphi DLL module contacts a command-and-control (C2) server to fetch a PowerShell script that employs Horabot to distribute the malware via phishing emails to harvested contacts from Microsoft Outlook.

"Rather than distributing a static file or hardcoded link as seen in older Horabot campaigns, this script initiates an HTTP POST request to a remote PHP API (hxxps://tt.grupobedfs[.]com/.../gera\_pdf.php), passing a randomly generated four-digit PIN," BlueVoyant said.

"The server dynamically forges a bespoke, password-protected PDF impersonating a Spanish judicial summons, which is returned to the infected host. The script then iterates over the filtered email list, utilizing the compromised user's own email account to send a tailored phishing email with the newly generated PDF attached."

Also used in tandem is a secondary Horabot-related DLL ("at.dll") that functions as a spam and account hijacking tool targeting Yahoo, Live, and Gmail accounts to send phishing emails via Outlook. Horabot is
[assessed](https://thehackernews.com/2023/06/new-botnet-malware-horabot-targets.html)
to be put to use in attacks targeting Latin America since at least November 2020.

Water Saci has a history of using WhatsApp Web as a distribution vector for disseminating banking trojans like Maverick and Casbaneiro in a worm-like manner. However, recent campaigns highlighted by Kaspersky have
[leveraged](https://securelist.com/horabot-campaign/119033/)
the ClickFix social engineering tactic to dupe users into running malicious HTA files with the end goal of deploying Casbaneiro and the Horabot spreader.

"Taken together, the integration of ClickFix social engineering, alongside dynamic PDF generation and WhatsApp automation, demonstrates an agile adversary that is continually innovating and executing diverse attack paths to bypass modern security controls," the researchers concluded.

"This adversary is maintaining a bifurcated, multi-pronged attack infrastructure, dynamically deploying the WhatsApp-centric Maverick chain and concurrently utilizing both ClickFix and email-based Horabot attack paths."