---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T02:04:13.347064+00:00'
exported_at: '2026-11-15T02:04:14.148510+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/digicert-data-breach-impacts-business-customer-information
structured_data:
  about: []
  author: ''
  description: DigiCert says hackers accessed archived data containing business contact
    information, including names, emails, and phone numbers.
  headline: DigiCert Data Breach Impacts Business Customer Information
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/digicert-data-breach-impacts-business-customer-information
  publisher:
    logo: /favicon.ico
    name: GTCode
title: DigiCert Data Breach Impacts Business Customer Information
updated_at: '2026-11-15T02:04:13.347064+00:00'
url_hash: fa3f0d293e67cff42e9d6187376df6ea42abd156
---

**DigiCert has disclosed a data breach impacting its business customers’ contact information, including names and email addresses.**

The incident involved an internal business system used for archiving customer information, which was moved to a different network segment in February 2025, inadvertently becoming exposed to the internet.

Attackers abused a self-registration feature in the system’s account manager, built for other purposes and not requiring MFA, to create a read-only account that had access to archived data between June 27 and July 2.

DigiCert blocked the unauthorized account on July 2, and determined in October that the account was used to access archived customer contact information, including names, email addresses, phone numbers, and business addresses.

In some cases, driver’s licenses, passports, utility bills, and other documents containing a name and address that its customers provided were also compromised.

“The access could not write records, act as a validation approver, or issue certificates,”
[DigiCert says](https://bugzilla.mozilla.org/show_bug.cgi?id=2084460)
. “The CA systems operate on their own secure network segments and were not affected by this external access.”

Advertisement. Scroll to continue reading.

According to the company, the incident was initially investigated and remediated as an account-creation event. On October 12, however, it started suspecting that the unauthorized account may have accessed archived data, and launched an investigation.

Since mid-October, the company also implemented additional monitoring and alerting, verified or removed remaining non-DigiCert accounts, reset passwords for all business system users, deactivated the feature that enabled users to self-register, and verified the ownership of the business system and the enforcement of permission policies.

DigiCert did not say how many customers might have been affected.
*SecurityWeek*
has emailed the company for information on the matter and will update this article if it responds.

**Related:**
[Malicious cPGuard Updates Served in OpsShield Supply Chain Attack](https://www.securityweek.com/malicious-cpguard-updates-served-in-opsshield-supply-chain-attack/)

**Related:**
[Frontline Education Data Breach Impacts Over 1.3 Million](https://www.securityweek.com/frontline-education-data-breach-impacts-over-1-3-million/)

**Related:**
[Florida Student Aid Website Hack Puts Data of 4.9 Million People at Risk](https://www.securityweek.com/florida-student-aid-website-hack-puts-data-of-4-9-million-people-at-risk/)

**Related:**
[Revolve Data Breach Impacts at Least 200,000 People](https://www.securityweek.com/revolve-data-breach-impacts-at-least-180000-people/)