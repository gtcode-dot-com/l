---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-22T00:00:07.351438+00:00'
exported_at: '2025-11-22T00:00:10.287912+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/grafana-patches-cvss-100-scim-flaw.html
structured_data:
  about: []
  author: ''
  description: Grafana fixes CVSS 10.0 SCIM flaw that enabled user impersonation and
    privilege escalation in versions 12.x.
  headline: Grafana Patches CVSS 10.0 SCIM Flaw Enabling Impersonation and Privilege
    Escalation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/grafana-patches-cvss-100-scim-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Grafana Patches CVSS 10.0 SCIM Flaw Enabling Impersonation and Privilege Escalation
updated_at: '2025-11-22T00:00:07.351438+00:00'
url_hash: 66f00a9f49683b7f799493264e26c99435c128f8
---

**

Nov 21, 2025
**

Ravie Lakshmanan

Vulnerability / Threat Mitigation

Grafana has released security updates to address a maximum severity security flaw that could allow privilege escalation or user impersonation under certain configurations.

The vulnerability, tracked as
**CVE-2025-41115**
, carries a CVSS score of 10.0. It resides in the System for Cross-domain Identity Management (
[SCIM](https://grafana.com/docs/grafana/latest/setup-grafana/configure-access/configure-scim-provisioning/)
) component that allows automated user provisioning and management. First
[introduced](https://grafana.com/blog/2025/05/14/introducing-scim-provisioning-in-grafana-enterprise-grade-user-management-made-simple/)
in April 2025, it's currently in public preview.

"In Grafana versions 12.x where SCIM provisioning is enabled and configured, a vulnerability in user identity handling allows a malicious or compromised SCIM client to provision a user with a numeric externalId, which in turn could allow for overriding internal user IDs and lead to impersonation or privilege escalation," Grafana's Vardan Torosyan
[said](https://grafana.com/blog/2025/11/19/grafana-enterprise-security-update-critical-severity-security-fix-for-cve-2025-41115/)
.

That said, successful exploitation hinges on both conditions being met -

* enableSCIM feature flag is set to true
* user\_sync\_enabled config option in the [auth.scim] block is set to true

The shortcoming affects Grafana Enterprise versions from 12.0.0 to 12.2.1. It has been addressed in the following versions of the software -

* Grafana Enterprise 12.0.6+security-01
* Grafana Enterprise 12.1.3+security-01
* Grafana Enterprise 12.2.1+security-01
* Grafana Enterprise 12.3.0

"Grafana maps the SCIM externalId directly to the internal user.uid; therefore, numeric values (e.g. '1') may be interpreted as internal numeric user IDs," Torosyan said. "In specific cases this could allow the newly provisioned user to be treated as an existing internal account, such as the Admin, leading to potential impersonation or privilege escalation."

The analytics and observability platform said the vulnerability was discovered internally on November 4, 2025, during an audit and testing. Given the severity of the issue, users are advised to apply the patches as soon as possible to mitigate potential risks.