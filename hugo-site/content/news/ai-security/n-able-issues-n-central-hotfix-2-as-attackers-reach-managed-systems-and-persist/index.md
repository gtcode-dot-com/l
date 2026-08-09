---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-09T09:50:05.628268+00:00'
exported_at: '2026-08-09T09:50:08.419393+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
structured_data:
  about: []
  author: ''
  description: N-able releases N-central Hotfix 2 amid CVE-2026-18577 exploitation
    that gave attackers admin access and persistent access to managed systems.
  headline: N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and
    Persist
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/n-central-attackers-reach-managed.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: N-able Issues N-central Hotfix 2 as Attackers Reach Managed Systems and Persist
updated_at: '2026-08-09T09:50:05.628268+00:00'
url_hash: 5dcfe0f4cb8f44086d25328eb6497df333c303a6
---

**

Ravie Lakshmanan
**

Aug 08, 2026

Vulnerability / Enterprise Security

N-able has
[released](https://www.n-able.com/blog/n-central-security-update-august-6-2026)
a fresh round of hotfixes for N‑central as part of its investigation into ongoing exploitation of a recently disclosed security flaw in the Remote Monitoring and Management (RMM) product.

"We are proactively expanding protections in response to ongoing monitoring of threat actors as they evolve their attack techniques," the company said.

"This is not a duplicate of our previous communication.
[Hotfix 2](https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/)
is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1 with additional hardening measures to further protect you and your customers."

The disclosure comes as N-able acknowledged that it detected unusual activity within a customer's environment on July 31, 2026, leading to the discovery of unknown threat actors exploiting a then-zero-day flaw in the N‑central server (CVE-2026-18577, CVSS score: 8.2). It impacts all versions prior to 2026.3.1.7.

It's worth noting that CVE-2026-18577 relates to an incomplete fix for CVE-2026-18556 (CVSS score: 8.2). Both vulnerabilities, which allow authentication bypass and account takeover in susceptible versions, have been
[flagged](https://thehackernews.com/2026/08/cisa-adds-exploited-n-able-n-central.html)
as
[actively exploited](https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html)
by the U.S. Cybersecurity and Infrastructure Security Agency (CISA).

In the attacks observed by N-able, the vulnerability allowed the attackers to obtain administrative access remotely and then leverage the Take Control feature to connect to systems within the N‑central managed environment. Upon gaining access to those devices, the threat actors registered a new service for a Cloudflare Tunnel, enabling persistence even after access to the N‑central server was revoked.

N-able has confirmed that a limited number of customers have been affected by the exploitation activity. Customers running an on-premise version are advised to update their instances to 026.3.1.10 immediately. The company has also shared an expanded set of IP addresses as indicators of compromise (IoCs) -

* 173.249.252[.]176
* 173.249.252[.]200
* 185.156.46[.]150
* 23.234.94[.]43
* 37.153.90[.]88
* 37.19.210[.]32
* 68.235.46[.]214
* 68.235.46[.]235
* 87.249.138[.]34
* 92.118.112[.]181

In addition, N-able has released a
[custom service template](https://developer.n-able.com/n-central/recipes/cve-2026-18577-detection)
that offers an automated way to check for known IoCs against Windows device endpoints in N‑central.

"A clean result should not be interpreted as a guarantee that your environment has not been impacted," it said. "Our investigation is ongoing and additional indicators may be identified over time. We strongly recommend this be used as one layer of your assessment, alongside a thorough review of your environment, logs, and account activity."