---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-13T06:15:14.892109+00:00'
exported_at: '2026-03-13T06:15:17.100535+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html
structured_data:
  about: []
  author: ''
  description: Veeam fixes 7 Backup & Replication flaws, including CVSS 9.9 RCE bugs,
    warning attackers may exploit unpatched systems.
  headline: Veeam Patches 7 Critical Backup & Replication Flaws Allowing Remote Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Veeam Patches 7 Critical Backup & Replication Flaws Allowing Remote Code Execution
updated_at: '2026-03-13T06:15:14.892109+00:00'
url_hash: f34b9cdd4d88e7512e8850ce453c973b855fff2a
---

**

Ravie Lakshmanan
**

Mar 13, 2026

Vulnerability / Enterprise Security

Veeam has released security updates to address multiple critical vulnerabilities in its Backup & Replication software that, if successfully exploited, could result in remote code execution.

The
[vulnerabilities](https://www.veeam.com/kb4830)
are as follows -

* **CVE-2026-21666**
  (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21667**
  (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21668**
  (CVSS score: 8.8) - A vulnerability that allows an authenticated domain user to bypass restrictions and manipulate arbitrary files on a Backup Repository.
* **CVE-2026-21672**
  (CVSS score: 8.8) - A vulnerability that allows local privilege escalation on Windows-based Veeam Backup & Replication servers.
* **CVE-2026-21708**
  (CVSS score: 9.9) - A vulnerability that allows a Backup Viewer to perform remote code execution as the postgres user.

The shortcomings, which affect Veeam Backup & Replication 12.3.2.4165 and all earlier version 12 builds, have been addressed in
[version 12.3.2.4465](https://www.veeam.com/kb4696)
. CVE-2026-21672 and CVE-2026-21708 have also been fixed in
[Backup & Replication 13.0.1.2067](https://www.veeam.com/kb4738)
, along with
[two more critical security flaws](https://www.veeam.com/kb4831)
-

* **CVE-2026-21669**
  (CVSS score: 9.9) - A vulnerability that allows an authenticated domain user to perform remote code execution on the Backup Server.
* **CVE-2026-21671**
  (CVSS score: 9.1) - A vulnerability that allows an authenticated user with the Backup Administrator role to perform remote code execution in high availability (HA) deployments of Veeam Backup & Replication.

"It's important to note that once a vulnerability and its associated patch are disclosed, attackers will likely attempt to reverse-engineer the patch to exploit unpatched deployments of Veeam software," the company said in its advisory.

With vulnerabilities in Veeam software having been
[repeatedly](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html)
[exploited](https://thehackernews.com/2024/11/cisa-alert-active-exploitation-of.html)
by
[threat actors](https://thehackernews.com/2026/01/veeam-patches-critical-rce.html)
to carry out ransomware attacks in the past, it's essential that users update their instances to the latest version to safeguard against any potential threat.