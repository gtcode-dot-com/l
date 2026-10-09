---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-14T18:15:15.303601+00:00'
exported_at: '2026-04-14T18:15:19.403025+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html
structured_data:
  about: []
  author: ''
  description: Two Composer flaws (CVE-2026-40176, CVE-2026-40261) allow command execution
    via Perforce configurations, prompting urgent updates.
  headline: New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New PHP Composer Flaws Enable Arbitrary Command Execution — Patches Released
updated_at: '2026-04-14T18:15:15.303601+00:00'
url_hash: 9225f25604b479d5fd8e7c30d1702f88d6732953
---

**

Ravie Lakshmanan
**

Apr 14, 2026

Vulnerability / DevSecOps

Two high-severity security vulnerabilities have been
[disclosed](https://blog.packagist.com/composer-2-9-6-perforce-driver-command-injection-vulnerabilities/)
in Composer, a package manager for PHP, that, if successfully exploited, could result in arbitrary command execution.

The vulnerabilities have been described as command injection flaws affecting the Perforce VCS (version control software) driver. Details of the two flaws are below -

* **[CVE-2026-40176](https://github.com/composer/composer/security/advisories/GHSA-wg36-wvj6-r67p)**
  (CVSS score: 7.8) - An improper input validation vulnerability that could allow an attacker controlling a repository configuration in a malicious composer.json declaring a Perforce VCS repository to inject arbitrary commands, resulting in command execution in the context of the user running Composer.
* **[CVE-2026-40261](https://github.com/composer/composer/security/advisories/GHSA-gqw4-4w2p-838q)**
  (CVSS score: 8.8) - An improper input validation vulnerability stemming from inadequate
  [escaping](https://en.wikipedia.org/wiki/Escape_sequence)
  that could allow an attacker to inject arbitrary commands through a crafted source reference containing shell metacharacters.

In both cases, Composer would execute these injected commands even if Perforce VCS is not installed, the maintainers noted in an advisory.

The vulnerabilities affect the following versions -

* >= 2.3, < 2.9.6 (Fixed in version 2.9.6)
* >= 2.0, < 2.2.27 (Fixed in version 2.2.27)

If immediate patching is not an option, it's advised to inspect composer.json files before running Composer and verify that Perforce-related fields contain valid values. It's also recommended to only use trusted Composer repositories, run Composer commands on projects from trusted sources, and avoid installing dependencies using the "--prefer-dist" or the "preferred-install: dist" configuration setting.

Composer said it scanned Packagist.org and did not find any evidence of the aforementioned vulnerabilities being exploited by threat actors by publishing packages with malicious Perforce information. A new release is expected to be shipped for Private Packagist Self-Hosted customers.

"As a precaution, publication of Perforce source metadata has been disabled on Packagist.org since Friday, April 10th, 2026," it said. "Composer installations should be updated immediately regardless."