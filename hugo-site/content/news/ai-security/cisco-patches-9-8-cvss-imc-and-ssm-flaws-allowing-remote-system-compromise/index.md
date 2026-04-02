---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T18:15:14.508592+00:00'
exported_at: '2026-04-02T18:15:16.871624+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/cisco-patches-98-cvss-imc-and-ssm-flaws.html
structured_data:
  about: []
  author: ''
  description: Cisco patches two 9.8 CVSS flaws (CVE-2026-20093, CVE-2026-20160),
    preventing authentication bypass and root access.
  headline: Cisco Patches 9.8 CVSS IMC and SSM Flaws Allowing Remote System Compromise
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/cisco-patches-98-cvss-imc-and-ssm-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cisco Patches 9.8 CVSS IMC and SSM Flaws Allowing Remote System Compromise
updated_at: '2026-04-02T18:15:14.508592+00:00'
url_hash: 943198ee6773883b8ef5fc7b99853c2064531bd6
---

**

Ravie Lakshmanan
**

Apr 02, 2026

Network Security / Vulnerability

Cisco has released updates to address a critical security flaw in the Integrated Management Controller (IMC) that, if successfully exploited, could allow an unauthenticated, remote attacker to bypass authentication and gain access to the system with elevated privileges.

The vulnerability, tracked as CVE-2026-20093, carries a CVSS score of 9.8 out of a maximum of 10.0.

"This vulnerability is due to incorrect handling of password change requests," Cisco
[said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-auth-bypass-AgG2BxTn)
in an advisory released Wednesday. "An attacker could exploit this vulnerability by sending a crafted HTTP request to an affected device."

"A successful exploit could allow the attacker to bypass authentication, alter the passwords of any user on the system, including an Admin user, and gain access to the system as that user."

Security researcher "jyh" has been credited with discovering and reporting the vulnerability. The shortcoming affects the following products regardless of the device configuration -

* 5000 Series Enterprise Network Compute Systems (ENCS) - Fixed in 4.15.5
* Catalyst 8300 Series Edge uCPE - Fixed in 4.18.3
* UCS C-Series M5 and M6 Rack Servers in standalone mode - Fixed in 4.3(2.260007), 4.3(6.260017), and 6.0(1.250174)
* UCS E-Series Servers M3 - Fixed in 3.2.17
* UCS E-Series Servers M6 - Fixed in 4.15.3

Another critical vulnerability patched by Cisco impacts Smart Software Manager On-Prem (SSM On-Prem), which could enable an unauthenticated, remote attacker to execute arbitrary commands on the underlying operating system. The vulnerability, CVE-2026-20160 (CVSS score: 9.8), stems from an unintentional exposure of an internal service.

"An attacker could exploit this vulnerability by sending a crafted request to the API of the exposed service," Cisco
[said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ssm-cli-execution-cHUcWuNr)
. "A successful exploit could allow the attacker to execute commands on the underlying operating system with root-level privileges."

Patches for the flaw have been released in Cisco SSM On-Prem version 9-202601. Cisco said the vulnerability was discovered internally during the resolution of a Cisco Technical Assistance Center (TAC) support case.

While neither of the vulnerabilities has been exploited in the wild, a number of
[recently](https://thehackernews.com/2026/02/cisco-sd-wan-zero-day-cve-2026-20127.html)
[disclosed](https://thehackernews.com/2026/03/cisco-confirms-active-exploitation-of.html)
security flaws in Cisco products have been weaponized by threat actors. In the absence of a workaround, customers are recommended to update to the fixed version for optimal protection.