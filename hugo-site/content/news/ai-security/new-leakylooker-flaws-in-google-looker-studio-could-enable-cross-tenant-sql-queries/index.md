---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T14:15:15.765440+00:00'
exported_at: '2026-03-10T14:15:18.009625+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/new-leakylooker-flaws-in-google-looker.html
structured_data:
  about: []
  author: ''
  description: Nine “LeakyLooker” flaws in Google Looker Studio allowed cross-tenant
    SQL access across GCP services before being patched.
  headline: New "LeakyLooker" Flaws in Google Looker Studio Could Enable Cross-Tenant
    SQL Queries
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/new-leakylooker-flaws-in-google-looker.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New "LeakyLooker" Flaws in Google Looker Studio Could Enable Cross-Tenant SQL
  Queries
updated_at: '2026-03-10T14:15:15.765440+00:00'
url_hash: 29990152051cb445379db1f8d711e158bba734df
---

**

Ravie Lakshmanan
**

Mar 10, 2026

Database Security / Vulnerability

Cybersecurity researchers have disclosed nine cross-tenant vulnerabilities in Google Looker Studio that could have permitted attackers to run arbitrary SQL queries on victims' databases and exfiltrate sensitive data within organizations' Google Cloud environments.

The shortcomings have been collectively named
**LeakyLooker**
by Tenable. There is no evidence that the vulnerabilities were exploited in the wild. Following responsible disclosure in June 2025, the issues have been addressed by Google.

The list of security flaws is as follows -

"The vulnerabilities broke fundamental design assumptions, revealed a new attack class, and could have allowed attackers to exfiltrate, insert, and delete data in victims' services and Google Cloud environment," security researcher Liv Matan
[said](https://www.tenable.com/blog/leakylooker-google-cloud-looker-studio-vulnerabilities)
in a report shared with The Hacker News.

"These vulnerabilities exposed sensitive data across Google Cloud Platform (GCP) environments, potentially affecting any organization using Google Sheets, BigQuery, Spanner, PostgreSQL, MySQL, Cloud Storage, and almost any other Looker Studio data connector."

Successful exploitation of the cross-tenant flaws could enable threat actors to gain access to entire datasets and projects across different cloud tenants.

Attackers could scan for public Looker Studio reports or obtain access to private ones that use these connectors (e.g., BigQuery) and seize control of the databases, allowing them to run arbitrary SQL queries across the owner's entire GCP project.

Alternatively, a victim creates a report as public or shares it with a specific recipient, and uses a JDBC-connected data source such as PostgreSQL. In this scenario, the attacker can take advantage of a logic flaw in the copy report feature that makes it possible to clone reports while retaining the original owner's credentials, enabling them to delete or modify tables.

Another high-impact path detailed by the cybersecurity company involved one-click data exfiltration, where sharing a specially crafted report forces a victim's browser to execute malicious code that contacts an attacker-controlled project to reconstruct entire databases from logs.

"The vulnerabilities broke the fundamental promise that a 'Viewer' should never be able to control the data they are viewing," Matan said, adding they "could have let attackers exfiltrate or modify data across Google services like BigQuery and Google Sheets."