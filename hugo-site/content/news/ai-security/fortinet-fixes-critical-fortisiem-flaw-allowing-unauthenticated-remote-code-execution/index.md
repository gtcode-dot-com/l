---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-14T12:15:13.980346+00:00'
exported_at: '2026-01-14T12:15:17.217031+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html
structured_data:
  about: []
  author: ''
  description: Fortinet patches a critical FortiSIEM vulnerability (CVE-2025-64155)
    that allows unauthenticated remote code execution via exposed phMonitor service.
  headline: Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote
    Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/fortinet-fixes-critical-fortisiem-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fortinet Fixes Critical FortiSIEM Flaw Allowing Unauthenticated Remote Code
  Execution
updated_at: '2026-01-14T12:15:13.980346+00:00'
url_hash: 55d09ea0344bd46e74cdb4d8bb28a962e748f29b
---

**

Jan 14, 2026
**

Ravie Lakshmanan

Vulnerability / Patch Management

Fortinet has released updates to fix a critical security flaw impacting FortiSIEM that could allow an unauthenticated attacker to achieve code execution on susceptible instances.

The operating system (OS) injection vulnerability, tracked as
**CVE-2025-64155**
, is rated 9.4 out of 10.0 on the CVSS scoring system.

"An improper neutralization of special elements used in an OS command ('OS command injection') vulnerability [CWE-78] in FortiSIEM may allow an unauthenticated attacker to execute unauthorized code or commands via crafted TCP requests," the company
[said](https://www.fortiguard.com/psirt/FG-IR-25-772)
in a Tuesday bulletin.

Fortinet said the vulnerability affects only Super and Worker nodes, and that it has been addressed in the following versions -

* FortiSIEM 6.7.0 through 6.7.10 (Migrate to a fixed release)
* FortiSIEM 7.0.0 through 7.0.4 (Migrate to a fixed release)
* FortiSIEM 7.1.0 through 7.1.8 (Upgrade to 7.1.9 or above)
* FortiSIEM 7.2.0 through 7.2.6 (Upgrade to 7.2.7 or above)
* FortiSIEM 7.3.0 through 7.3.4 (Upgrade to 7.3.5 or above)
* FortiSIEM 7.4.0 (Upgrade to 7.4.1 or above)
* FortiSIEM 7.5 (Not affected)
* FortiSIEM Cloud (Not affected)

Horizon3.ai security researcher Zach Hanley, who is credited with discovering and reporting the flaw on August 14, 2025,
[said](https://horizon3.ai/attack-research/disclosures/cve-2025-64155-three-years-of-remotely-rooting-the-fortinet-fortisiem/)
it comprises two moving parts -

* An unauthenticated argument injection vulnerability that leads to arbitrary file write, allowing for remote code execution as the admin user
* A file overwrite privilege escalation vulnerability that leads to root access and completely compromises the appliance

Specifically, the problem has to do with how FortiSIEM's
[phMonitor](https://thehackernews.com/2025/08/fortinet-warns-about-fortisiem.html)
service – a crucial backend process
[responsible](https://docs.fortinet.com/document/fortisiem/7.5.0/user-guide/174517/viewing-cloud-health)
for health monitoring, task distribution, and inter-node communication via TCP port 7900 – handles incoming requests related to logging security events to Elasticsearch.

This, in turn, invokes a shell script with user-controlled parameters, thereby opening the door to argument injection via curl and achieving arbitrary file writes to the disk in the context of the admin user.

This limited file write can be weaponized to achieve full system takeover weaponizing the curl argument injection to write a reverse shell to "/opt/charting/redishb.sh," a file that's writable by an admin user and is executed every minute by the appliance by means of a cron job that runs with root-level permissions.

In other words, writing a reverse shell to this file enables privilege escalation from admin to root, granting the attacker unfettered access to the FortiSIEM appliance. The most important aspect of the attack is that the phMonitor service exposes several command handlers that do not require authentication. This makes it easy for an attacker to invoke these functions simply by obtaining network access to port 7900.

Fortinet has also shipped fixes for another
[critical security vulnerability](https://www.fortiguard.com/psirt/FG-IR-25-260)
in FortiFone (CVE-2025-47855, CVSS score: 9.3) that could allow an unauthenticated attacker to obtain device configuration via a specially crafted HTTP(S) request to the Web Portal page. It impacts the following versions of the enterprise communications platform -

* FortiFone 3.0.13 through 3.0.23 (Upgrade to 3.0.24 or above)
* FortiFone 7.0.0 through 7.0.1 (Upgrade to 7.0.2 or above)
* FortiFone 7.2 (Not affected)

Users are advised to update to the latest versions for optimal protection. As workarounds for CVE-2025-64155, Fortinet is recommending that customers limit access to the phMonitor port (7900).