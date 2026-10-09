---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-03T19:51:56.925435+00:00'
exported_at: '2026-03-03T19:51:59.027461+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/900-sangoma-freepbx-instances.html
structured_data:
  about: []
  author: ''
  description: Over 900 FreePBX systems remain infected after CVE-2025-64328 exploitation,
    now listed in CISA KEV amid active attacks.
  headline: 900+ Sangoma FreePBX Instances Compromised in Ongoing Web Shell Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/900-sangoma-freepbx-instances.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 900+ Sangoma FreePBX Instances Compromised in Ongoing Web Shell Attacks
updated_at: '2026-03-03T19:51:56.925435+00:00'
url_hash: ed14668691e6b309ca65c278be655b134c35b853
---

**

Ravie Lakshmanan
**

Feb 27, 2026

Network Security / Vulnerability

The Shadowserver Foundation has
[revealed](https://bsky.app/profile/shadowserver.bsky.social/post/3mfmv4o433k2b)
that over 900 Sangoma FreePBX instances still remain infected with web shells as part of attacks that exploited a command injection vulnerability starting in December 2025.

Of these,
[401 instances](https://dashboard.shadowserver.org/statistics/combined/tree/?date_range=1&source=compromised_iot&source=compromised_website&source=compromised_website6&tag=freepbx-compromised%2B&data_set=count&scale=log&auto_update=on)
are located in the U.S., followed by 51 in Brazil, 43 in Canada, 40 in Germany, and 36 in France.

The non-profit entity said the compromises are likely accomplished via the exploitation of CVE-2025-64328 (CVSS score: 8.6), a high-severity security flaw that could enable post-authentication command injection.

"The impact is that any user with access to the FreePBX Administration panel could leverage this vulnerability to execute arbitrary shell commands on the underlying host," FreePBX
[said](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-vm9p-46mv-5xvw)
in an advisory for the flaw in November 2025. "An attacker could leverage this to obtain remote access to the system as the asterisk user."

The vulnerability affects FreePBX versions higher than and including 17.0.2.36. It was resolved in version 17.0.3. As mitigations, it's advised to add security controls to ensure that only authorized users have access to the FreePBX Administrator Control Panel (ACP), restrict access from hostile networks to the ACP, and update the filestore module to the latest version.

The vulnerability has since come under active exploitation in the wild, prompting the U.S. Cybersecurity and Infrastructure Security Agency (CISA) to
[add](https://thehackernews.com/2026/02/cisa-adds-actively-exploited-solarwinds.html)
it to its Known Exploited Vulnerabilities (KEV) catalog earlier this month.

|  |
| --- |
|  |
| Source: The Shadowserver Foundation |

In a report published late last month, Fortinet FortiGuard Labs revealed that the threat actor behind the cyber fraud operation codenamed INJ3CTOR3 has been exploiting CVE-2025-64328 starting early December 2025 to deliver a web shell codenamed EncystPHP.

"By leveraging Elastix and FreePBX administrative contexts, the web shell operates with elevated privileges, enabling arbitrary command execution on the compromised host and initiating outbound call activity through the PBX environment," the cybersecurity company noted.

FreePBX users are recommended to update their FreePBX deployments to the latest version as soon as possible to counter active threats.