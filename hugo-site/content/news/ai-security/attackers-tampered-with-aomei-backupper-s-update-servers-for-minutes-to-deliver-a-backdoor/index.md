---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-17T22:16:29.450562+00:00'
exported_at: '2026-10-17T22:16:31.180930+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html
structured_data:
  about: []
  author: ''
  description: Attackers altered AOMEI Backupper update files for 5 to 10 minutes
    at a time, delivering SHINYROAD to systems that checked for updates
  headline: Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to
    Deliver a Backdoor
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/attackers-tampered-with-aomei.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attackers Tampered with AOMEI Backupper's Update Servers for Minutes to Deliver
  a Backdoor
updated_at: '2026-10-17T22:16:29.450562+00:00'
url_hash: 2f6312b7767d6c547ac84e86b76922a35d16c11a
---

Attackers repeatedly changed the files that AOMEI Backupper fetches from the vendor's own update servers, in windows of five to ten minutes at a time between May and July 2026, so that any copy of the Windows backup program that checked for an update during one of those windows would download and run a backdoor.

[Google Threat Intelligence Group, Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)
, and
[ManageEngine's Threat Analysis Lab](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)
, which disclosed the campaign this week, say AOMEI has reported fixing its servers, but that fix does not remove the backdoor from machines that were already hit.

AOMEI Backupper is Windows backup and disk-cloning software made by AOMEI Technology, a vendor registered in Hong Kong. Like the company's remote-desktop tool AnyViewer, it runs background services that regularly check AOMEI's servers over HTTPS for software updates and promotional pop-ups.

Two files drive that check. One, down\_html.ini, names the update package to download and the checksum the program uses to verify it. The other, Notifycfg.ini, tells the pop-up service what to display and what to run.

The program does not cryptographically verify either file, and the checksum that is supposed to prove the download is genuine sits inside the same unsigned file that names it.

Nothing in the software was exploited. There was no vulnerability, and no user action was needed beyond having the program installed and running, according to ManageEngine's lab. The attacker only had to change two text files on the server for a few minutes.

A copy of Backupper that checked in during a window pulled the attacker's package into its own folder, and the notification file then made it run. It ran with the privileges of the AOMEI process that launched it.

On the machines the lab examined, that was enough to install software across the whole system, though it said the elevation depended on how the AOMEI service was running.

### Three Windows, Eleven Countries

GTIG and Mandiant confirmed three tampering windows, and said more probably happened that they did not see:

* May 28, 2026: a 10-minute window, 05:40 to 05:50 UTC
* July 16, 2026: a 6-minute window, 08:33 to 08:39 UTC
* July 20, 2026: a 5-minute window, 10:35 to 10:40 UTC

Only copies that checked for an update during a window were affected. A copy that checked before or after got clean, genuine files, which is what makes the attack hard to catch. GTIG described the targeting as opportunistic, hitting whatever system happened to poll during those minutes.

From its own telemetry, GTIG identified affected organizations in IT services, telecommunications and higher education across 11 countries: Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye and the United States. It gave no total and said the real number is likely higher.

GTIG named AnyViewer, AOMEI's remote-desktop tool, as using the same update flow, but the detections it describes involve Backupper. Neither report lists which Backupper versions are affected, and the lab examined version 8.3.0.

GTIG tracks the group behind the campaign as UNC7017 and names no country or known actor. It said this is the first supply chain compromise it has encountered built on Windows this short, "effectively evading traditional point-in-time triage and automated file scanning."

### What Landed on the Machine

On a machine that pulled the package, a downloader that GTIG calls CROSSROAD unpacked a bundle into a local Radmin folder, created a scheduled task set to run every three hours, and then deleted itself from disk.

The bundle included a genuine, signed copy of Radmin, a commercial remote-administration tool. ManageEngine's lab found it staged but never switched on, with no listener, no configuration, and no new account. The remote control came instead from a separate implant that reached out to the attacker.

The scheduled task runs the signed Radmin program, which loads an attacker-built DLL placed beside it, which in turn loads the SHINYROAD implant. The implant gives a remote shell and can fetch and run new code on command. It talks to a single hard-coded address with no backup, so blocking that one address cuts off the attacker's control.

CROSSROAD runs only in some places. It checks the machine's location and stops if it is in China, and ManageEngine added that it also stops if it finds particular security agents on the host. On machines that passed those checks, GTIG later saw a second tool pushed down on top of SHINYROAD, the open-source
[Adaptix C2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
framework, disguised as Nitro PDF software.

### A July 20 Change That Needed No Code to Run

The July 20 window included a second trick that did not require running any program. GTIG found that the notification file had been changed to open an invisible, one-pixel pop-up pointing to a file on an attacker's server via WebDAV, a way to access a remote file as if it were on the local disk.

Rendering that pop-up can make Windows send the logged-in user's NetNTLMv2 authentication response, a token an attacker can try to crack offline or reuse, to the attacker's address with nothing visible to the user. Because no program had to run, a machine with the backdoor blocked could still have leaked that token.

### What AOMEI Was Told, and When

ManageEngine's lab said its endpoint software first caught the activity on May 28, when it recorded AOMEI Backupper installing Radmin on two unrelated customers in different countries. A customer raised it on June 7, and the lab notified AOMEI the same day. AOMEI's first explanation was that the content had been intercepted and changed in transit.

The lab said the evidence did not support that explanation. Both machines had fetched the files over HTTPS from AOMEI's own servers, across different countries and networks, and the program had pulled the package in through its normal update steps. In mid-July, its own monitors caught one of the windows as it happened, confirming the change was being served from AOMEI's side.

Mandiant notified AOMEI on July 17 and shared indicators. AOMEI told Mandiant on July 29 that it had taken corrective action to secure its servers. ManageEngine's lab said that, as of publication, it had not independently confirmed that the compromise had been contained.

Neither report says how the attacker gained the ability to change files on AOMEI's servers. AOMEI's published
[changelog](https://www.ubackup.com/changelog.html)
for Backupper, checked by The Hacker News on October 16, lists no change to how the program verifies updates through the current release, 8.5.0, from October 9. Neither report points to a version that closes the gap.

### What to Check Now

A fixed server does not clean a machine that was hit. The downloader set up its scheduled task and then restored the local update file to its genuine contents, so an infected machine can look normal while the vendor's download page also looks clean. GTIG and ManageEngine both urge organizations running AOMEI software to hunt across the whole April-to-July period.

"Organizations running AOMEI software cannot assume they are protected solely because the vendor took corrective server-side action," GTIG and Mandiant said.

Do not judge an alert by checking the vendor's download page now. Because the files changed back within minutes, that page serves genuine content almost all the time, which has led analysts to dismiss real detections as false alarms. Preserve the files cached in the program's own folders, and check network logs for what was served at the exact time the alert fired.

On the endpoint, hunt for:

* **Scheduled task**
  : RadminComponentRuntime, or NitroRuntime for the follow-on tool
* **File**
  : an unsigned upgrade-now.exe that carries AOMEI's publisher details, or any program running from Backupper's html pop-up folder
* **Folder**
  : attacker files staged under the local Radmin application-data folder

On the network, block the attacker infrastructure named in both reports, and block outbound SMB (TCP 445) and WebDAV to external addresses to stop the credential trick:

* **Domain**
  : storage-data[.]com, promotion.storage-data[.]com, aomei.storage-data[.]com
* **IP**
  : 8.210.84[.]56, 8.218.65[.]184, 47.239.60[.]117

GTIG and ManageEngine each published detection rules with their reports, YARA rules from GTIG and Sigma rules from the lab. Both sets are the researchers' own and have not been tested by The Hacker News.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.