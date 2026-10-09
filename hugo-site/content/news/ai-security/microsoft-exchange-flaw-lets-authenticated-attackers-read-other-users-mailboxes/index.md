---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:41:28.405617+00:00'
exported_at: '2026-10-07T04:41:31.023065+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
structured_data:
  about: []
  author: ''
  description: Microsoft patches CVE-2026-96940, which lets authenticated attackers
    read other users' Exchange mailboxes within the same organization.
  headline: Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users'
    Mailboxes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/microsoft-exchange-flaw-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Exchange Flaw Lets Authenticated Attackers Read Other Users' Mailboxes
updated_at: '2026-10-07T04:41:28.405617+00:00'
url_hash: cb207012cadc4c9d5a75e9548cfb84b6316e69e4
---

**

Ravie Lakshmanan
**

Oct 05, 2026

Vulnerability / Email Security

Microsoft has released out-of-band security updates to address a high-severity flaw in Microsoft Exchange Server that could allow an attacker to escalate privileges under certain conditions.

The vulnerability, tracked as
**[CVE-2026-96940](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-96940)**
, is rated 8.8 on the CVSS scoring system.

"Weak authorization in Microsoft Exchange Server allows an authenticated attacker to elevate privileges over a network," Microsoft said in an advisory released on October 2, 2026.

The Windows maker said an authenticated attacker can exploit this flaw to gain unauthorized access to other users' mailboxes within the same organization and read email messages and attachments. However, the vulnerability does not allow cross-tenant access.

Microsoft has already deployed a "related service-side fix" to Exchange Online to address the issue. As a result, Exchange Online customers are not required to take any action.

Users of affected on-premises Microsoft Exchange Server products are advised to install the updates to stay protected. The following versions are impacted -

* Microsoft Exchange Server Subscription Edition RTM
* Microsoft Exchange Server 2016 Cumulative Update 23
* Microsoft Exchange Server 2019 Cumulative Update 15
* Microsoft Exchange Server 2019 Cumulative Update 14

Redmond has credited Microsoft researcher Jan Mitchell with discovering and reporting the flaw. Although there is no evidence of the flaw being weaponized in the wild, Microsoft has tagged it with an Exploitability assessment of "Exploitation More Likely," making it essential that users move quickly to apply the fixes.

The disclosure comes days after Broadcom-owned Symantec
[warned](https://thehackernews.com/2026/10/warlock-exploits-sharepoint-flaws-to.html)
that the China-linked Warlock actor is exploiting multiple vulnerabilities in Microsoft SharePoint to deploy its namesake ransomware in attacks targeting organizations in Portuguese- and Spanish-speaking countries.