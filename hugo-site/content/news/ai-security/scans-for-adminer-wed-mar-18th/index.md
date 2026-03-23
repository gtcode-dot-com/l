---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-23T05:47:36.737568+00:00'
exported_at: '2026-03-23T05:47:39.692096+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32808
structured_data:
  about: []
  author: ''
  description: 'Scans for "adminer", Author: Johannes Ullrich'
  headline: Scans for "adminer", (Wed, Mar 18th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32808
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scans for "adminer", (Wed, Mar 18th)
updated_at: '2026-03-23T05:47:36.737568+00:00'
url_hash: d992412ced346d3d0cc347ac4103094f24ec9482
---

A very popular target of attackers scanning our honeypots is "phpmyadmin". phpMyAdmin is a script first released in the late 90s, before many security concepts had been discovered. It's rich history of vulnerabilities made it a favorite target. Its alternative, "adminer", began appearing about a decade later (https://www.adminer.org). One of its main "selling" points was simplicity. Adminer is just a single PHP file. It requires no configuration. Copy it to your server, and you are ready to go. "adminer" has a much better security record and claims to prioritize security in its development.

So how does it deal with configurations for database connection parameters? The simple answer: It does not. Instead of using its own authentication or access control, Adminer simply asks the user to enter the SQL username and password they want to use to connect to the database. This is certainly not a terrible idea. Let the database deal with it! SQL databases have robust access controls, so there is no need to reinvent the wheel. Not having to store database credentials in a secrets file also removes several security headaches.

But... these credentials are, of course, still subject to brute-forcing. Adminer thought about that, and only allows 30 login attempts in 30 minutes. One may argue that this is "generous", but they thought about it. The main weakness likely represents users using weak passwords and relying on SQL authentication; there is no easy way to implement two-factor authentication. Adminer mitigates some of these issues with security plugins that implement OTP protection and other security features.

This likely explains why attackers are scanning for it, and they have been scanning quite aggressively lately:

![Graph of adminer scan volume](https://isc.sans.edu/diaryimages/images/Screenshot%202026-03-18%20at%208_56_32%E2%80%AFAM.png)

The increase in the number of URLs scanned is noteworthy. In phpMyAdmin scans, attackers often attempt to find obfuscated URLs used to host phpMyAdmin, such as "/pma/". For Adminer, attackers are scanning for different versions of the file. The filename released by Adminer includes the version number and the language or database type. For example, "adminer-5.4.2-mysql-en.php" is the English version for MySQL.

In short: Do not forget to read the security advice provided by Adminer, and you probably do not want to open Adminer to the internet.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|