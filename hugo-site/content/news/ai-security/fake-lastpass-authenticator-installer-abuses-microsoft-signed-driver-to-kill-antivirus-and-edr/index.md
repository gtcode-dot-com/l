---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:18:31.481275+00:00'
exported_at: '2026-10-03T23:18:33.405148+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html
structured_data:
  about: []
  author: ''
  description: A fake LastPass Authenticator installer uses a signed kernel driver
    to kill security tools before a stealer collects passwords and wallet files.
  headline: Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to
    Kill Antivirus and EDR
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/fake-lastpass-authenticator-installer.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake LastPass Authenticator Installer Abuses Microsoft-Signed Driver to Kill
  Antivirus and EDR
updated_at: '2026-10-03T23:18:31.481275+00:00'
url_hash: 98fe946df30dd12793a090c43f3dd871a7a7ad71
---

A fake LastPass Authenticator installer offered on GitHub installs a Windows kernel driver that shuts off antivirus and other security software before a password stealer runs if a victim downloads and runs it, researchers at LastPass and Delphos Labs said on September 17.

Microsoft's own hardware-compatibility program signs the driver, scored zero detections on VirusTotal when researchers checked it in August, and was not on Microsoft's list of blocked drivers. LastPass says none of its own systems, services, or customer vaults were touched, and that the attackers only borrowed its name.

The lure is a fake GitHub page (github.com/LastPass-Authenticator) that ranks in search results for terms like "LastPass Authenticator download" and looks like a real LastPass product page.

Clicking the download button sends the visitor through several GitHub pages to an attacker server, which serves a large ZIP file. The real LastPass Authenticator comes from lastpass.com and the official app stores, not GitHub.

Inside the ZIP is a renamed copy of a real Microsoft debugging tool, vsdbg.exe, placed next to a malicious file named vsdbg.dll. When the fake installer runs, Windows loads the attacker's DLL from the same folder, a trick called DLL side-loading. The loader then tries three ways to gain administrator rights, reaches SYSTEM, the highest level on a Windows machine, and installs the kernel driver as a service.

The archives seen were 148 MB and 127.9 MB, padded with junk files so that scanners with size limits skip them.

## What the driver does, and why Windows trusts it

A kernel driver runs below the level where antivirus and endpoint detection and response (EDR) tools operate. This one, which the researchers named Alinubx.sys, carries a list of 145 antivirus and security process names and terminates each one it finds running.

It does this from the kernel, below the level where security software runs, so those user-mode tools cannot block or see the kill. Loading a legitimately signed but abusable driver to gain that access is a known technique called bring your own vulnerable driver, or BYOVD, which
[The Hacker News has covered before](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html)
.

The driver is signed through the Microsoft Windows Hardware Compatibility Publisher chain, with a signing date of March 2023, years before this campaign. As the
[researchers](https://blog.lastpass.com/posts/lastpass-delphos-report-rapuncel-infostealer)
put it, "Microsoft attestation proves a driver passed through a trust pipeline. It does not prove the driver is safe."

The kill list is the only part of the driver that ran here. Its code can also hide files, inject into other programs, and reroute web traffic, but those need a configuration file the attackers did not include, so they stayed off.

What it did do is enough. With security software down, the stealer collected saved passwords from more than two dozen browsers, cryptocurrency wallet files, and login sessions for Discord, Steam, and Telegram, along with the contents of Windows Credential Manager and files named like "password," "seed," or "recovery."

For Chrome and Edge, which use Google's app-bound encryption to stop exactly this, the stealer injects code into the browser and asks the browser's own service to decrypt the passwords. The data is packed into a ZIP and sent to an attacker server.

## Why nothing caught it

The driver is a renamed copy of CcProtect.sys, a driver from the Chinese disk-encryption product CnCrypt that is
[already listed on the LOLDrivers catalog](https://www.loldrivers.io/drivers/3e3067b0-3d74-46fe-9f57-1ae3a0293958/)
as a process killer, with public proof-of-concept code. The two share the same product name, version, and submitter; only the file name and description changed.

That change dropped the file's antivirus detections: the known original showed 7 of about 70 engines flagging it in August, while the renamed driver showed zero.

The blocklist is a different matter. Microsoft's
[vulnerable driver blocklist](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/app-control-for-business/design/microsoft-recommended-driver-block-rules)
, on by default since the Windows 11 2022 update, stops listed drivers from loading. Delphos checked it on August 20 and found neither the renamed driver nor the known original on it. The rename did not slip past the blocklist, because the original was never on it either.

The blocklist matches known file hashes, and a renamed or recompiled driver produces a new hash that the list does not carry. At the September 17 report, Alinubx.sys was still not on the blocklist.

Delphos reported the driver to Microsoft on August 19. Microsoft responded that the behavior does not meet its definition of a security vulnerability, because the driver is not a Microsoft component, and pointed the researchers to the separate channel that considers drivers for the blocklist. Delphos resubmitted there the same day.

## If you ran the fake installer

Treat every password saved in the browser on that machine as stolen, along with any cryptocurrency wallet files, Discord, Steam, and Telegram sessions, and anything in Windows Credential Manager. The stealer copies these out before the driver work begins.

Change those passwords from a separate, clean device, not the affected one, and review account activity for anything you did not do. The driver stays loaded, re-kills security tools, and re-runs the stealer on every reboot, defeating the tools that would normally clean it up.

A machine that ran this payload should be treated as a kernel-level compromise and, where possible, given a kernel-level forensic check or rebuilt.

## What defenders can hunt for

The researchers say to hunt for the driver's lineage and behavior rather than one file name, because the operators can change the name again as they did here. Signs to watch for:

* **Service:**
  a service created as NvFsFilter
* **File:**
  a driver written to C:\Windows\System32\drivers\nvfsflt64.sys
* **Signer:**
  a driver whose signing details name Henan Dafeng Software or contain "CnCrypt"
* **Device:**
  the path \\.\Alinubx
* **Behavior:**
  a driver load followed by security processes being killed

A community detection for the exact driver is
[published on LOLDrivers](https://www.loldrivers.io/drivers/84a3007a-de5e-4622-bfc5-f05d927c3618/)
, though it matches by hash and so shares the same weakness once the file changes. Full indicators are in the joint report.

## Where it came from

The LastPass page was one of many lures. The attacker server was serving impersonation pages for at least 40 brands, LastPass said, and a near-identical second fake page for a "macOS LastPass" product was taken down before the team could examine it.

Fake GitHub repositories delivering this family of stealer are not new: Trend Micro documented the
[BoryptGrab stealer](https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html#github-seo-malware)
spread this way in March, and Arctic Wolf reported
[a separate wave of nearly 300 such repositories](https://thehackernews.com/2026/07/threatsday-game-cheat-spyware-24-hour.html)
in July.

Delphos assesses with high confidence that the loader was built with the
[Cruciferra crypter](https://thehackernews.com/2026/07/cruciferra-crypter-uses-byovd-and.html)
, a paid tool whose default kill list also holds 145 names and whose driver is interchangeable, and with moderate confidence that the stealer, which LastPass calls Rapuncel, is a relative of BoryptGrab rather than the same build. How many people were infected is unknown; the report provides no victim count.