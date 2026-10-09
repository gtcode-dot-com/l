---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-01T00:15:14.416293+00:00'
exported_at: '2026-01-01T00:15:16.922176+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/ibm-warns-of-critical-api-connect-bug.html
structured_data:
  about: []
  author: ''
  description: IBM disclosed a critical CVSS 9.8 authentication bypass in IBM API
    Connect that could allow remote access; patches are now available.
  headline: IBM Warns of Critical API Connect Bug Allowing Remote Authentication Bypass
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/ibm-warns-of-critical-api-connect-bug.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: IBM Warns of Critical API Connect Bug Allowing Remote Authentication Bypass
updated_at: '2026-01-01T00:15:14.416293+00:00'
url_hash: 8092869e6f08e7f7452b643d8780c05cade2c31d
---

**

Dec 31, 2026
**

Ravie Lakshmanan

API Security / Vulnerability

IBM has disclosed details of a critical security flaw in
[API Connect](https://www.ibm.com/products/api-connect)
that could allow attackers to gain remote access to the application.

The vulnerability, tracked as
**[CVE-2025-13915](https://www.cve.org/CVERecord?id=CVE-2025-13915)**
, is rated 9.8 out of a maximum of 10.0 on the CVSS scoring system. It has been described as an authentication bypass flaw.

"IBM API Connect could allow a remote attacker to bypass authentication mechanisms and gain unauthorized access to the application," the tech giant
[said](https://www.ibm.com/support/pages/node/7255149)
in a bulletin.

The shortcoming affects the following versions of IBM API Connect -

* 10.0.8.0 through 10.0.8.5
* 10.0.11.0

Customers are advised to
[follow the steps](https://www.ibm.com/support/pages/node/7255318)
outlined below -

* Download the fix from Fix Central
* Extract the files: Readme.md and ibm-apiconnect-<version>-ifix.13195.tar.gz
* Apply the fix based on the appropriate API Connect version

"Customers unable to install the interim fix should disable self-service sign-up on their Developer Portal if enabled, which will help minimise their exposure to this vulnerability," the company added.

[API Connect](https://www.ibm.com/docs/en/api-connect/software/12.1.0?topic=api-connect-overview)
is an end-to-end application programming interface (API) solution that allows organizations to create, test, manage, and secure APIs located on cloud and on-premises. It's used by companies like Axis Bank, Bankart, Etihad Airways, Finologee, IBS Bulgaria, State Bank of India, Tata Consultancy Services, and TINE.

While there is no evidence of the vulnerability being exploited in the wild, users are advised to apply the fixes as soon as possible for optimal protection.