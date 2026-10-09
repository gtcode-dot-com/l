---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T22:15:18.450237+00:00'
exported_at: '2026-06-10T22:15:20.177067+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html
structured_data:
  about: []
  author: ''
  description: Veeam fixes CVE-2026-44963 RCE in 12 builds, blocking authenticated
    domain users from attacking backup servers.
  headline: Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/veeam-backup-replication-rce-flaw-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Veeam Backup & Replication RCE Flaw Lets Domain Users Run Remote Code
updated_at: '2026-06-10T22:15:18.450237+00:00'
url_hash: 02c4490a9341cc3aead808d661cf3f5b670465c3
---

**

Ravie Lakshmanan
**

Jun 09, 2026

Vulnerability / Backup Software

Veeam has released security patches to address a critical flaw in its Backup &amp; Replication software that could result in remote code execution.

Tracked as
**CVE-2026-44963**
, the vulnerability carries a CVSS score of 9.4 out of a maximum of 10.0.

"A vulnerability allowing remote code execution (RCE) on the Backup Server by an authenticated domain user," Veeam
[said](https://www.veeam.com/kb4869)
in a Tuesday advisory.

It credited watchTowr researcher Sina Kheirkhah for responsibly discovering and reporting the issue. It impacts Veeam Backup &amp; Replication 12.3.2.4465 and all earlier versions of 12 builds.

Veeam has noted that the vulnerability does not affect any version 13.x build of the backup software due to architectural changes introduced in version 13.

The shortcoming has been addressed in Veeam Backup &amp; Replication version 12.3.2.4854.

In March 2026, Veeam
[resolved](https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html)
multiple critical vulnerabilities in Backup &amp; Replication software that, if successfully exploited, could result in remote code execution.

It's essential that users update to the latest version for optimal version, particularly given that prior vulnerabilities in the program have been exploited by bad actors, including ransomware groups.