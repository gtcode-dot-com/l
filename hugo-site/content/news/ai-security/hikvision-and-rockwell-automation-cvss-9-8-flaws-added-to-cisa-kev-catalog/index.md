---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-07T04:00:07.221751+00:00'
exported_at: '2026-03-07T04:00:09.833259+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html
structured_data:
  about: []
  author: ''
  description: CISA adds Hikvision flaw CVE-2017-7921 and Rockwell Automation CVE-2021-22681
    to KEV, urging agencies to patch by March 26, 2026.
  headline: Hikvision and Rockwell Automation CVSS 9.8 Flaws Added to CISA KEV Catalog
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/hikvision-and-rockwell-automation-cvss.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hikvision and Rockwell Automation CVSS 9.8 Flaws Added to CISA KEV Catalog
updated_at: '2026-03-07T04:00:07.221751+00:00'
url_hash: 398bc6a49eb76c896015fb355afd0003f8e2c79d
---

**

Ravie Lakshmanan
**

Mar 06, 2026

Vulnerability / Network Security

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Thursday
[added](https://www.cisa.gov/news-events/alerts/2026/03/05/cisa-adds-five-known-exploited-vulnerabilities-catalog)
two security flaws impacting Hikvision and Rockwell Automation products to its Known Exploited Vulnerabilities (
[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
) catalog, citing evidence of active exploitation.

The critical-severity vulnerabilities are listed below -

* **[CVE-2017-7921](https://www.cve.org/CVERecord?id=CVE-2017-7921)**
  (CVSS score: 9.8) - An improper authentication vulnerability affecting multiple Hikvision products that could allow a malicious user to escalate privileges on the system and gain access to sensitive information.
* **[CVE-2021-22681](https://www.cve.org/CVERecord?id=CVE-2021-22681)**
  (CVSS score: 9.8) - An insufficiently protected credentials vulnerability affecting multiple Rockwell Automation Studio 5000 Logix Designer, RSLogix 5000, and Logix Controllers that could allow an unauthorized user with network access to the controller to bypass the verification mechanism and authenticate with it, as well as alter its configuration and/or application code.

The addition of CVE-2017-7921 to the KEV catalog comes more than four months after the SANS Internet Storm Center
[disclosed](https://thehackernews.com/2025/10/threatsday-bulletin-carplay-exploit.html#scan-waves-hint-pre-exploit-staging)
that it had detected exploit attempts against Hikvision cameras susceptible to the flaw. However, there appears to be no public report describing attacks involving
[CVE-2021-22681](https://thehackernews.com/2024/05/rockwell-advises-disconnecting-internet.html)
.

In light of active exploitation, Federal Civilian Executive Branch (FCEB) agencies are recommended to update to the latest supported software versions by March 26, 2026, as part of
[Binding Operational Directive (BOD) 22-01](https://www.cisa.gov/binding-operational-directive-22-01)
.

"These types of vulnerabilities are frequent attack vectors for malicious cyber actors and pose significant risks to the federal enterprise," CISA said.

"Although BOD 22-01 only applies to FCEB agencies, CISA strongly urges all organizations to reduce their exposure to cyberattacks by prioritizing timely remediation of KEV Catalog vulnerabilities as part of their vulnerability management practice."