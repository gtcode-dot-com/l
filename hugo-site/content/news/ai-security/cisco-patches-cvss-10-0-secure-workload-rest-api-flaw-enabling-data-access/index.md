---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-23T03:18:48.120338+00:00'
exported_at: '2026-05-23T03:18:50.544056+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
structured_data:
  about: []
  author: ''
  description: Cisco patches critical CVSS 10.0 flaw in Secure Workload — unauthenticated
    attackers can steal data & escalate privileges across tenants.
  headline: Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Enabling Data Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/cisco-patches-cvss-100-secure-workload.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cisco Patches CVSS 10.0 Secure Workload REST API Flaw Enabling Data Access
updated_at: '2026-05-23T03:18:48.120338+00:00'
url_hash: 289e87ac70a4b68cbb3474a891db70688ab53adb
---

**

Ravie Lakshmanan
**

May 22, 2026

Vulnerability / Network Security

Cisco has rolled out updates for a maximum-severity security flaw impacting Secure Workload that could allow an unauthenticated, remote attacker to access sensitive data.

Tracked as
**CVE-2026-20223**
(CVSS score: 10.0), the vulnerability arises from insufficient validation and authentication when accessing REST API endpoints.

"An attacker could exploit this vulnerability if they are able to send a crafted API request to an affected endpoint," Cisco
[said](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-csw-pnbsa-g8WEnuy)
. "A successful exploit could allow the attacker to read sensitive information and make configuration changes across tenant boundaries with the privileges of the Site Admin user."

The shortcoming impacts Cisco Secure Workload Cluster Software on SaaS and on-prem deployments, regardless of device configuration. Cisco said there are no workarounds that address the vulnerability.

The issue has been addressed in the following versions -

* Cisco Secure Workload Release 3.9 and earlier (Migrate to a fixed release)
* Cisco Secure Workload Release 3.10 (Fixed in 3.10.8.3)
* Cisco Secure Workload Release 4.0 (Fixed in 4.0.3.17)

The networking equipment major said it found the vulnerability during internal security testing and that there is no evidence of it being exploited in the wild.

The disclosure comes a week after Cisco revealed that another maximum-severity authentication bypass flaw in Catalyst SD-WAN Controller (
[CVE-2026-20182](https://thehackernews.com/2026/05/cisa-adds-cisco-sd-wan-cve-2026-20182.html)
, CVSS score: 10.0) has been exploited by a threat actor known as UAT-8616 to gain unauthorized access to SD-WAN systems.