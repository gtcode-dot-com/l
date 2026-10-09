---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-13T20:21:01.673839+00:00'
exported_at: '2025-11-13T20:21:04.182737+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/cisa-flags-critical-watchguard-fireware.html
structured_data:
  about: []
  author: ''
  description: CISA warns 54K+ WatchGuard firewalls risk remote exploits via CVE-2025-9242;
    patches due by Dec 3.
  headline: CISA Flags Critical WatchGuard Fireware Flaw Exposing 54,000 Fireboxes
    to No-Login Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/cisa-flags-critical-watchguard-fireware.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: CISA Flags Critical WatchGuard Fireware Flaw Exposing 54,000 Fireboxes to No-Login
  Attacks
updated_at: '2025-11-13T20:21:01.673839+00:00'
url_hash: ead199b854711dc443d75d9dab97ecb2db3aab26
---

**

Nov 13, 2025
**

Ravie Lakshmanan

Vulnerability / Network Security

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Wednesday
[added](https://www.cisa.gov/news-events/alerts/2025/11/12/cisa-adds-three-known-exploited-vulnerabilities-catalog)
a critical security flaw impacting
**WatchGuard Fireware**
to its Known Exploited Vulnerabilities (
[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
) catalog, based on evidence of active exploitation.

The vulnerability in question is CVE-2025-9242 (CVSS score: 9.3), an out-of-bounds write vulnerability affecting Fireware OS 11.10.2 up to and including 11.12.4\_Update1, 12.0 up to and including 12.11.3 and 2025.1. It was patched by WatchGuard in September.

"WatchGuard Firebox contains an out-of-bounds write vulnerability in the OS iked process that may allow a remote unauthenticated attacker to execute arbitrary code," CISA said in an advisory.

Details of the vulnerability were
[shared](https://thehackernews.com/2025/10/researchers-uncover-watchguard-vpn-bug.html)
by watchTowr Labs last month, with the cybersecurity company stating that the issue stems from a missing length check on an identification buffer used during the IKE handshake process.

"The server does attempt certificate validation, but that validation happens after the vulnerable code runs, allowing our vulnerable code path to be reachable pre-authentication," security researcher McCaulay Hudson noted.

In an
[update to its advisory](https://www.watchguard.com/wgrd-psirt/advisory/wgsa-2025-00015)
on October 21, 2025, WatchGuard said it has evidence suggesting active exploitation of the flaw, sharing three indicators of compromise (IoCs) associated with the activity -

* An IKE\_AUTH request log message with an abnormally large IKE\_AUTH request IDi payload greater than 100 bytes
* During a successful exploit, the iked process will hang, interrupting VPN connections
* After a failed or successful exploit, the iked process will crash and generate a fault report on the Firebox

According to
[data](https://dashboard.shadowserver.org/statistics/combined/time-series/?date_range=30&source=isakmp_vulnerable&source=isakmp_vulnerable6&tag=cve-2025-9242%2B&dataset=unique_ips&limit=100&group_by=geo&stacking=stacked&auto_update=on)
from the Shadowserver Foundation, more than 54,300 Firebox instances remain vulnerable to the critical bug as of November 12, 2025, down from a high of 75,955 on October 19.

|  |
| --- |
|  |
| Number of exposed WatchGuard Firebox instances |

Roughly 18,500 of these devices are in the U.S., the scans reveal. Italy (5,400), the U.K. (4,000), Germany (3,600), and Canada (3,000) round up the top five. Federal Civilian Executive Branch (FCEB) agencies are advised to apply WatchGuard's patches by December 3, 2025.

The development comes as CISA also added
[CVE-2025-62215](https://thehackernews.com/2025/11/microsoft-fixes-63-security-flaws.html)
(CVSS score: 7.0), a recently disclosed flaw in Windows kernel, and
[CVE-2025-12480](https://thehackernews.com/2025/11/hackers-exploiting-triofox-flaw-to.html)
(CVSS score: 9.1), an improper access control vulnerability in Gladinet Triofox, to the KEV catalog. Google's Mandiant Threat Defense team has attributed the exploitation of CVE-2025-12480 to a threat actor it tracks as UNC6485.

*(The story was updated after publication to include information from WatchGuard confirming active exploitation efforts.)*