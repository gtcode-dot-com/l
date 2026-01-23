---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-23T14:15:12.622703+00:00'
exported_at: '2026-01-23T14:15:14.818088+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/fortinet-confirms-active-forticloud-sso.html
structured_data:
  about: []
  author: ''
  description: Fortinet confirms active exploitation of a FortiCloud SSO authentication
    bypass affecting fully patched FortiGate devices via SAML abuse.
  headline: Fortinet Confirms Active FortiCloud SSO Bypass on Fully Patched FortiGate
    Firewalls
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/fortinet-confirms-active-forticloud-sso.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fortinet Confirms Active FortiCloud SSO Bypass on Fully Patched FortiGate Firewalls
updated_at: '2026-01-23T14:15:12.622703+00:00'
url_hash: b0d16df7969255adec0a059727a7240f073f0cea
---

**

Ravie Lakshmanan
**

Jan 23, 2026

Network Security / Vulnerability

Fortinet has officially confirmed that it's working to completely plug a FortiCloud SSO authentication bypass vulnerability following reports of fresh exploitation activity on fully-patched firewalls.

"In the last 24 hours, we have identified a number of cases where the exploit was to a device that had been fully upgraded to the latest release at the time of the attack, which suggested a new attack path," Fortinet Chief Information Security Officer (CISO) Carl Windsor
[said](https://www.fortinet.com/blog/psirt-blogs/analysis-of-sso-abuse-on-fortios)
in a Thursday post.

The activity essentially mounts to a bypass for patches put in place by the network security vendor to address
[CVE-2025-59718 and CVE-2025-59719](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html)
, which could allow unauthenticated bypass of SSO login authentication via crafted SAML messages if the FortiCloud SSO feature is enabled on affected devices. The issues were originally addressed by Fortinet last month.

However, earlier this week, reports
[emerged](https://thehackernews.com/2026/01/automated-fortigate-attacks-exploit.html)
of renewed activity in which malicious SSO logins on FortiGate appliances were recorded against the admin account on devices that had been patched against the twin vulnerabilities. The activity is similar to
[incidents](https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html)
observed in December, shortly after the disclosure of the CVE-2025-59718 and CVE-2025-59719.

The activity involves the creation of generic accounts for persistence, making configuration changes granting VPN access to those accounts, and the exfiltration of firewall configurations to different IP addresses. The threat actor has been observed logging in with accounts named "cloud-noc@mail.io" and "cloud-init@mail.io."

As mitigations, the company is urging the following actions -

* Restrict administrative access of edge network device via the internet by applying a local-in policy
* Disable FortiCloud SSO logins by disabling "admin-forticloud-sso-login"

"It is important to note that while, at this time, only exploitation of FortiCloud SSO has been observed, this issue is applicable to all SAML SSO implementations," Fortinet said.