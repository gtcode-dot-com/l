---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-17T00:03:12.048621+00:00'
exported_at: '2025-12-17T00:03:14.773377+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html
structured_data:
  about: []
  author: ''
  description: Attackers are exploiting two CVSS 9.8 FortiGate SSO authentication
    bypass flaws days after disclosure; Fortinet urges immediate patching.
  headline: Fortinet FortiGate Under Active Attack Through SAML SSO Authentication
    Bypass
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/fortinet-fortigate-under-active-attack.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Fortinet FortiGate Under Active Attack Through SAML SSO Authentication Bypass
updated_at: '2025-12-17T00:03:12.048621+00:00'
url_hash: fa56b589583ab2e1e38701f080401ced87f468dd
---

**

Dec 16, 2025
**

Ravie Lakshmanan

Network Security / Vulnerability

Threat actors have begun to exploit two newly disclosed security flaws in Fortinet FortiGate devices, less than a week after public disclosure.

Cybersecurity company Arctic Wolf said it observed active intrusions involving malicious single sign-on (SSO) logins on FortiGate appliances on December 12, 2025. The attacks exploit
[two critical authentication bypasses](https://thehackernews.com/2025/12/fortinet-ivanti-and-sap-issue-urgent.html)
(CVE-2025-59718 and CVE-2025-59719, CVSS scores: 9.8). Patches for the flaws were released by Fortinet last week for FortiOS, FortiWeb, FortiProxy, and FortiSwitchManager.

"These vulnerabilities allow unauthenticated bypass of SSO login authentication via crafted SAML messages, if the FortiCloud SSO feature is enabled on affected devices," Arctic Wolf Labs
[said](https://arcticwolf.com/resources/blog/arctic-wolf-observes-malicious-sso-logins-following-disclosure-cve-2025-59718-cve-2025-59719/)
in a new bulletin.

It's worth noting that while FortiCloud SSO is disabled by default, it is automatically enabled during FortiCare registration unless administrators explicitly turn it off using the "Allow administrative login using FortiCloud SSO" setting in the registration page.

In the malicious activity observed by Arctic Wolf, IP addresses associated with a limited set of hosting providers, such as The Constant Company llc, Bl Networks, and Kaopu Cloud Hk Limited, were used to carry out malicious SSO logins against the "admin" account.

Following the logins, the attackers have been found to export device configurations via the GUI to the same IP addresses.

In light of ongoing exploitation activity, organizations are advised to apply the patches as soon as possible. As mitigations, it's essential to disable FortiCloud SSO until the instances are updated to the latest version and limit access to management interfaces of firewalls and VPNs to trusted internal users.

"Although credentials are typically hashed in network appliance configurations, threat actors are known to crack hashes offline, especially if credentials are weak and susceptible to dictionary attacks," Arctic Wolf said.

Fortinet customers who find indicators of compromise (IoCs) consistent with the campaign are recommended to assume compromise and reset hashed firewall credentials stored in the exfiltrated configurations.