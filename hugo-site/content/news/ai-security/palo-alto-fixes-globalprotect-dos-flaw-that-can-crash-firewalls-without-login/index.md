---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-15T10:15:12.877229+00:00'
exported_at: '2026-01-15T10:15:15.123998+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/palo-alto-fixes-globalprotect-dos-flaw.html
structured_data:
  about: []
  author: ''
  description: Palo Alto Networks fixed CVE-2026-0227, new GlobalProtect flaw that
    lets unauthenticated attackers trigger firewall DoS &  maintenance mode.
  headline: Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without
    Login
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/palo-alto-fixes-globalprotect-dos-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Palo Alto Fixes GlobalProtect DoS Flaw That Can Crash Firewalls Without Login
updated_at: '2026-01-15T10:15:12.877229+00:00'
url_hash: 0bbd61031bce641af5f12aab137602c9d58323fa
---

**

Jan 15, 2026
**

Ravie Lakshmanan

Network Security / Vulnerability

Palo Alto Networks has released security updates for a high-severity security flaw impacting GlobalProtect Gateway and Portal, for which it said there exists a proof-of-concept (PoC) exploit.

The vulnerability, tracked as
**CVE-2026-0227**
(CVSS score: 7.7), has been described as a denial-of-service (DoS) condition impacting GlobalProtect PAN-OS software arising as a result of an improper check for exceptional conditions (
[CWE-754](https://cwe.mitre.org/data/definitions/754)
)

"A vulnerability in Palo Alto Networks PAN-OS software enables an unauthenticated attacker to cause a denial-of-service (DoS) to the firewall," the company
[said](https://security.paloaltonetworks.com/CVE-2026-0227)
in an advisory released Wednesday. "Repeated attempts to trigger this issue result in the firewall entering into maintenance mode."

The issue, discovered and reported by an unnamed external researcher, affects the following versions -

* PAN-OS 12.1 < 12.1.3-h3, < 12.1.4
* PAN-OS 11.2 < 11.2.4-h15, < 11.2.7-h8, < 11.2.10-h2
* PAN-OS 11.1 < 11.1.4-h27, < 11.1.6-h23, < 11.1.10-h9, < 11.1.13
* PAN-OS 10.2 < 10.2.7-h32, < 10.2.10-h30, < 10.2.13-h18, < 10.2.16-h6, < 10.2.18-h1
* PAN-OS 10.1 < 10.1.14-h20
* Prisma Access 11.2 < 11.2.7-h8
* Prisma Access 10.2 < 10.2.10-h29

Palo Alto Networks also clarified that the vulnerability is applicable only to PAN-OS NGFW or Prisma Access configurations with an enabled GlobalProtect gateway or portal. The company's Cloud Next-Generation Firewall (NGFW) is not impacted. There are no workarounds to mitigate the flaw.

While there is no evidence that the vulnerability has been exploited in the wild, it's essential to keep the devices up-to-date, especially given that exposed GlobalProtect gateways have
[witnessed](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)
repeated
[scanning activity](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#globalprotect-scans-spike)
over the
[past year](https://thehackernews.com/2025/12/cisco-warns-of-active-attacks.html)
.