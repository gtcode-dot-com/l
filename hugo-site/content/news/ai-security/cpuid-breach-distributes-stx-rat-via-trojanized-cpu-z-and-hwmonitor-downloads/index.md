---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-12T06:15:14.733663+00:00'
exported_at: '2026-04-12T06:15:17.150489+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
structured_data:
  about: []
  author: ''
  description: CPUID breach served STX RAT via trojanized CPU-Z downloads on April
    9–10, impacting 150+ victims and multiple industries.
  headline: CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: CPUID Breach Distributes STX RAT via Trojanized CPU-Z and HWMonitor Downloads
updated_at: '2026-04-12T06:15:14.733663+00:00'
url_hash: ffa933ee628e21774546b1946efb1fe2ef9e3cc1
---

**

Ravie Lakshmanan
**

Apr 12, 2026

Malware / Threat Intelligence

Unknown threat actors compromised CPUID ("cpuid[.]com"), a website that hosts popular hardware monitoring tools like CPU-Z, HWMonitor, HWMonitor Pro, and PerfMonitor, for less than 24 hours to serve malicious executables for the software and deploy a remote access trojan called STX RAT.

The incident lasted from approximately April 9, 15:00 UTC, to about April 10, 10:00 UTC, with the download URLs for CPU-Z and HWMonitor installers replaced with links to malicious websites.

In a
[post](https://x.com/d0cTB/status/2042520961824559150)
shared on X, CPUID confirmed the breach, attributing it to a compromise of a "secondary feature (basically a side API)" that caused the main site to randomly display malicious links. It's worth noting that the attack did not impact its signed original files.

According to
[Kaspersky](https://securelist.com/tr/cpu-z/119365/)
, the names of the rogue websites are as follows -

* cahayailmukreatif.web[.]id
* pub-45c2577dbd174292a02137c18e7b1b5a.r2[.]dev
* transitopalermo[.]com
* vatrobran[.]hr

"The trojanized software was distributed both as ZIP archives and as standalone installers for the aforementioned products," the Russian cybersecurity company said. "These files contain a legitimate signed executable for the corresponding product and a malicious DLL, which is named 'CRYPTBASE.dll' to leverage the DLL side-loading technique."

The malicious DLL, for its part, contacts an external server and executes additional payloads, but not before performing anti-sandbox checks to sidestep detection. The end goal of the campaign is to deploy
[STX RAT](https://www.esentire.com/blog/stx-rat-a-new-rat-in-2026-with-infostealer-capabilities)
, a RAT with HVNC and broad infostealer capabilities.

STX RAT "exposes a broad command set for remote control, follow-on payload execution, and post-exploitation actions (e.g., in-memory execution of EXE/DLL/PowerShell/shellcode, reverse proxy/tunneling, desktop interaction)," eSentire said in an analysis of the malware last week.

The command-and-control (C2) server address and the connection configuration have been reused from a
[prior campaign](https://www.malwarebytes.com/blog/threat-intel/2026/03/a-fake-filezilla-site-hosts-a-malicious-download)
that leveraged trojanized
[FileZilla installers](https://www.malwarebytes.com/blog/threat-intel/2026/02/fake-7-zip-downloads-are-turning-home-pcs-into-proxy-nodes)
hosted on bogus sites to deploy the same RAT malware. The activity was documented by Malwarebytes early last month.

Kaspersky said it has identified more than 150 victims, mostly individuals who were affected by the incident. However, organizations in retail, manufacturing, consulting, telecommunications, and agriculture have also been impacted. Most of the infections are located in Brazil, Russia, and China.

"The gravest mistake attackers made was to reuse the same infection chain involving STX RAT, and the same domain names for C2 communication, from the previous attack related to fake FileZilla installers," Kaspersky said. "The overall malware development/deployment and operational security capabilities of the threat actor behind this attack are quite low, which, in turn, made it possible to detect the watering hole compromise as soon as it started."