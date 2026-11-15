---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:32:27.611133+00:00'
exported_at: '2026-11-15T07:32:29.230890+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/apify-confirms-customer-data-accessed-in-cyberattack
structured_data:
  about: []
  author: ''
  description: Apify confirms a cyberattack involving compromised credentials and
    unauthorized access to customer accounts and data.
  headline: Apify Confirms Customer Data Accessed in Cyberattack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/apify-confirms-customer-data-accessed-in-cyberattack
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apify Confirms Customer Data Accessed in Cyberattack
updated_at: '2026-11-15T07:32:27.611133+00:00'
url_hash: 5177075a13cb0048cc71dff5741657d792bd0af6
---

**Web scraping and automation company Apify has confirmed that customer data was accessed in a cyberattack that compromised internal systems and customer accounts.**

The Czech company provides a cloud platform for collecting information from websites and automating online tasks. It says it has 91,000 customers worldwide.

The intrusion took place on November 9 and 10 and was discovered on November 11, when Apify blocked the attacker’s access and launched an investigation.

According to the company, the attacker used a compromised credential to obtain additional credentials and gain access to related Apify accounts.

On November 12,
[Apify confirmed](https://status.apify.com/incidents/sxd1dj5j6749)
that some customers had their personal information or stored data accessed during the attack.

The company has contacted customers whose information was exposed. Those who have not received a notification have not been identified as affected so far, although the investigation is continuing. Apify has not disclosed the number of compromised customer accounts.

Advertisement. Scroll to continue reading.

According to an Apify customer who shared a
[breach notification](https://www.reddit.com/r/apify/comments/1xv1rvs/more_details_about_the_security_incident/)
on Reddit, the exposed information included names, email addresses, billing details, account activity, and IP addresses.

More importantly, the notification listed salted password hashes, 2FA recovery codes and phone numbers, and authentication tokens associated with Google and GitHub sign-ins among the compromised data.

The notification also indicated that payment card information was limited to cardholder names, expiration dates, and the last four digits of card numbers. Full card numbers and security codes were not exposed.

The company has implemented additional monitoring, changed critical internal secrets, and revoked some OAuth connections to third-party services, including GitHub.

Apify said its investigation had not found that the OAuth connections could have been used as an attack vector. Customers building Apify Actors from private GitHub repositories have been instructed to reconnect their GitHub integrations.

**Related**
:
[Notion Customer Data Compromised in Fireworks AI Hack](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/)

**Related**
:
[Maersk Confirms Data Theft Amid $5 Million Extortion Attempt](https://www.securityweek.com/maersk-confirms-data-theft-amid-5-million-extortion-attempt/)

**Related**
:
[Over 3 Million People Hit by Frontline Education Data Breach](https://www.securityweek.com/3-million-people-hit-by-frontline-education-data-breach/)