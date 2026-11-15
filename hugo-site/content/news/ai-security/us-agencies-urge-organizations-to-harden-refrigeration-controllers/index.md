---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T02:41:04.916003+00:00'
exported_at: '2026-11-15T02:41:06.800783+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/us-agencies-urge-organizations-to-harden-refrigeration-controllers
structured_data:
  about: []
  author: ''
  description: The US urges refrigeration monitoring system hardening amid attacks
    against European supermarkets and blood banks.
  headline: US Agencies Urge Organizations to Harden Refrigeration Controllers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/us-agencies-urge-organizations-to-harden-refrigeration-controllers
  publisher:
    logo: /favicon.ico
    name: GTCode
title: US Agencies Urge Organizations to Harden Refrigeration Controllers
updated_at: '2026-11-15T02:41:04.916003+00:00'
url_hash: fcfddf9c6246224f8331819453f4c65b8d841b2e
---

**The US government is urging healthcare, chemical, food, and transportation organizations to harden their industrial refrigeration and cold chain monitoring systems.**

Over the past weeks, threat actors have been hacking monitoring systems to tamper with fridges and freezers in supermarkets and blood banks across Europe, causing millions in losses.

[Hundreds of supermarkets](https://www.securityweek.com/refrigeration-controller-hack-spoils-food-across-european-supermarkets/)
were hit on October 11, when the attackers turned the temperatures in fridges to 50 degrees Celsius (122 degrees Fahrenheit) and set freezers to defrost, spoiling food and, in some cases, causing fires.

A second wave of attacks hit
[more than 100 supermarkets](https://www.securityweek.com/over-100-european-stores-hit-as-supermarket-fridge-attacks-resume/)
and a
[blood bank](https://www.securityweek.com/cyberattack-hits-french-blood-bank-site-but-no-blood-products-are-compromised/)
this week, but only supermarkets suffered losses. Quick action from staff prevented the compromise of blood products and samples, the French Blood Establishment (EFS) said.

Russian hacktivist groups such as Noname057(16) and Z-Pentest Alliance reportedly claimed hacking Danfoss, leading to speculation that they mounted the supermarket attacks. However, nothing has been confirmed, and Iranian hacktivists or state-sponsored hackers may also be responsible, BBC
[notes](https://www.bbc.com/news/articles/c8vgxyvz6y9ro)
.

CISA, the FBI, HHS, USDA, and DoT say they “are aware of malicious cyber actors targeting electronic temperature controllers and commercial refrigeration controllers in retail grocery and cold storage facilities.”

Advertisement. Scroll to continue reading.

“The actors may exploit vulnerabilities or weaknesses in unpatched or internet-accessible controllers to remotely alter settings and force units into continuous heating and defrost cycles, which can cause widespread inventory loss and equipment hazards,” the agencies
[note](https://www.ic3.gov/CSA/2026/261105.pdf)
(PDF).

Hackers may exploit authentication bypasses, code injection, and weak configurations to access the management systems and tamper with refrigerator and cold storage systems’ temperature or cause denial-of-view conditions, the agencies say.

According to internet intelligence firm Censys, out of 6,695 internet-exposed refrigeration controllers identified on October 9, only 3,124 (or 47%) remain accessible from the web as of November 5.

The company’s
[analysis](https://censys.com/blog/european-refrigeration-controller-exposure-sitrep)
covers the widely used Copeland/Dixell XWEB and Danfoss StoreView controllers: XWEB exposure dropped 35% (3,708 to 2,420), while StoreView dropped 76% (3,004 to 708).

Per the US government’s recommendations, taking the control systems off the internet is the best action organizations can take to prevent attacks. If web access is necessary, these systems should be protected by a firewall or edge device.

Organizations should also isolate OT devices, restrict access to trusted identities, enforce strong password policies and phishing-resistant multifactor authentication, keep systems updated, maintain backups offsite, and enable logging and monitoring.

**Related:**
[OpenSSH Rushes Patches for ‘SSHole’ Authentication Bypass](https://www.securityweek.com/openssh-rushes-patches-for-sshole-authentication-bypass/)

**Related:**
[Critical Node-RED Flaw Exploited in Attacks](https://www.securityweek.com/critical-node-red-flaw-exploited-in-attacks/)

**Related:**
[Barracuda ESG Authentication Bypass Flaw Opens Path to Root](https://www.securityweek.com/barracuda-email-security-gateway-authentication-bypass-opens-path-to-root/)

**Related:**
[Google Introduces $250,000 Root-in-Cloud Bug Bounty Reward](https://www.securityweek.com/google-introduces-250000-root-in-cloud-bug-bounty-reward/)