---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-10T08:15:14.107773+00:00'
exported_at: '2026-04-10T08:15:16.917065+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/backdoored-smart-slider-3-pro-update.html
structured_data:
  about: []
  author: ''
  description: Backdoored Smart Slider 3 Pro v3.5.1.35 update distributed for 6 hours
    via compromised infrastructure, enabling RCE and data theft.
  headline: Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend
    Servers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/backdoored-smart-slider-3-pro-update.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Backdoored Smart Slider 3 Pro Update Distributed via Compromised Nextend Servers
updated_at: '2026-04-10T08:15:14.107773+00:00'
url_hash: c76edc83b74a4f99d16a7a251b7c33438b2824c7
---

**

Ravie Lakshmanan
**

Apr 10, 2026

Malware / Website Security

Unknown threat actors have hijacked the update system for the Smart Slider 3 Pro plugin for WordPress and Joomla to push a poisoned version containing a backdoor.

The incident impacts Smart Slider 3 Pro version 3.5.1.35 for WordPress, per WordPress security company Patchstack. Smart Slider 3 is a popular WordPress slider plugin with more than 800,000 active installations across its free and Pro editions.

"An unauthorized party gained access to Nextend’s update infrastructure and distributed a fully attacker-authored build through the official update channel," the company
[said](https://patchstack.com/articles/critical-supply-chain-compromise-in-smart-slider-3-pro-full-malware-analysis/)
. "Any site that updated to 3.5.1.35 between its release on April 7, 2026, and its detection approximately 6 hours later received a fully weaponized remote access toolkit."

Nextend, which maintains the plugin,
[said](https://wordpress.org/support/topic/smart-slider-3-pro-update/#post-18873519)
an unauthorized party gained unauthorized access to its update system and pushed a malicious version (3.5.1.35 Pro) that remained accessible for approximately six hours, before it was detected and pulled.

The trojanized update includes the ability to create rogue administrator accounts, as well as drop backdoors that execute system commands remotely via HTTP headers and run arbitrary PHP code via hidden request parameters. According to Patchstack, the malware comes with the following capabilities -

* Achieve pre-authenticated remote code execution via custom HTTP headers like X-Cache-Status and X-Cache-Key, the latter of which contains the code that's passed to "shell\_exec()."
* A backdoor that supports dual execution modes, enabling the attacker to execute arbitrary PHP code and operating system commands on the server.
* Create a hidden administrator account (e.g., "wpsvc\_a3f1") for persistent access and make it invisible to legitimate administrators by tampering with the "pre\_user\_query" and "views\_users" filters.
* Use three custom WordPress options that are set with the "autoload" setting disabled to reduce their visibility in option dumps: \_wpc\_ak (a secret authentication key), \_wpc\_uid (user ID of the hidden administrator account), and \_wpc\_uinfo (Base64-encoded JSON containing the plaintext username, password, and email of the rogue account).
* Install persistence in three locations for redundancy: create a
  [must-use plugin](https://thehackernews.com/2025/07/hackers-deploy-stealth-backdoor-in.html)
  with the filename "object-cache-helper.php" to make it look like a legitimate caching component, append the backdoor component to the active theme's "functions.php" file, and drop a file named "class-wp-locale-helper.php" in the WordPress "wp-includes" directory.
* Exfiltrate data containing site URL, secret backdoor key, hostname, Smart Slider 3 version, WordPress version, and PHP version, WordPress admin email address, WordPress database name, plaintext username and password of the administrator account, and a list of all installed persistence methods to the command-and-control (C2) domain "wpjs1[.]com."

"The malware operates in several stages, each designed to ensure deep, persistent, and redundant access to the compromised site," Patchstack said.

"The sophistication of the payload is notable: rather than a simple webshell, the attacker deployed a multi-layered persistence toolkit with several independent, redundant re-entry points, user concealment, resilient command execution with fallback chains, and automatic C2 registration with full credential exfiltration.

It's worth noting that the free version of the WordPress plugin is not affected. To contain the issue, Nextend shut down its update servers, removed the malicious version, and launched a full investigation into the incident.

Users who have the trojanized version installed are advised to update to version 3.5.1.36. In addition, users who have installed the rogue version are recommended to perform the
[following cleanup steps](https://smartslider.helpscoutdocs.com/article/2144-wordpress-security-advisory-smart-slider-3-pro-3-5-1-35-compromise)
-

* Check for any suspicious or unknown admin accounts and remove them.
* Remove Smart Slider 3 Pro version 3.5.1.35 if installed.
* Reinstall a clean version of the plugin.
* Remove all persistence files that allow the backdoor to persist on the site.
* Delete malicious WordPress options from the "wp\_options" table: \_wpc\_ak, \_wpc\_uid, \_wpc\_uinfo, \_perf\_toolkit\_source, and wp\_page\_for\_privacy\_policy\_cache.
* Clean up the "wp-config.php" file, including removing "define('WP\_CACHE\_SALT', '<token>');" if it exists.
* Remove the line "# WPCacheSalt <token>" from the ".htaccess" file located in the WordPress root folder.
* Reset the administrator and WordPress database user passwords.
* Change FTP/SSH and hosting account credentials.
* Review the website and logs for any unauthorized changes and unusual POST requests.
* Enable two-factor authentication (2FA) for admins and disable PHP execution in the uploads folder.

"This incident is a textbook supply chain compromise, the kind that renders traditional perimeter defenses irrelevant," Patchstack said. "Generic firewall rules, nonce verification,role-based access controls,none of them apply when the malicious code is delivered through the trusted update channel. The plugin is the malware."