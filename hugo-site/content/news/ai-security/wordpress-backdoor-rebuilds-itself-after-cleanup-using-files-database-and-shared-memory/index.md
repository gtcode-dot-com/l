---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:55:25.608805+00:00'
exported_at: '2026-10-07T01:55:28.273748+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html
structured_data:
  about: []
  author: ''
  description: SC WordPress malware rebuilds its backdoor from files, the database,
    and shared memory; fewer than 20 wpForo exploit attempts were seen since July
    3.
  headline: WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database,
    and Shared Memory
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/wordpress-backdoor-rebuilds-itself.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: WordPress Backdoor Rebuilds Itself After Cleanup Using Files, Database, and
  Shared Memory
updated_at: '2026-10-07T01:55:25.608805+00:00'
url_hash: e0da2450b1b9314ca48dac1b82cae5078ef9535d
---

**

Ravie Lakshmanan
**

Oct 01, 2026

Vulnerability / Web Security

Cybersecurity researchers have shed light on a WordPress compromise in which threat actors deployed multiple persistence mechanisms to ensure that the final payload kept returning without having to infect the site again.

The backdoor has been codenamed
**SC**
after the "SC\_" markers present in the injected content. Sucuri has described the malware as a "self-healing mesh" that's blockchain-controlled.

"The payload lives in at least eight places at once, spread across files, the database, and shared memory, and every one of those places can rebuild all the others," security researcher Gabriel Barbosa
[said](https://blog.sucuri.net/2026/09/sc-wordpress-malware-a-self-healing-mesh-of-loaders-drop-ins-and-a-blockchain-controlled-backdoor.html)
.

"Delete the plugin and a drop-in rewrites it. Delete the drop-in and the theme rewrites it. Clean every file on disk, and the next page load restores the whole set from the database or from a shared-memory segment. The result is a circular system with no single point you can remove to stop it."

According to Sucuri, the malware does not have any readable function names, instead employing a decoder to unscramble the code using a substitution cipher. A summary of the eight components is as follows -

* .user.ini, which sets "
  [auto\_prepend\_file](https://www.php.net/manual/en/ini.core.php#ini.auto-prepend-file)
  " to run a loader before every PHP request in that directory tree.
* wp-content/c1b12371.php, the loader that includes a hidden dot-prefixed file if it exists in the same location.
* wp-content/.c1b12371.php, the hidden dot-prefixed file which acts as the first-stage loader to locate a fake plugin and rebuilds it in mu-plugins from three sources: an existing copy in the plugins folder, an encoded stub in the cache directory, and a ZIP restore bundle with a random hex name.
* wp-content/db.php, which is loaded during bootstrap and carries the entire backdoor payload in compressed, Base64-encoded format. It decodes and re-deploys the plugin whenever it's missing or too small.
* wp-content/advanced-cache.php, which is loaded by WordPress before ordinary plugins when caching is enabled, and rebuilds the plugin from five independent sources: an existing mu-plugin, an existing plugin copy, a System V shared-memory segment holding PHP, a ZIP bundle, and the database. It then hooks plugins\_loaded and includes it.
* wp-content/themes/khorshidi/functions.php, a theme-resident twin of db.php that features the same backdoor and rewrites the plugin every time it is not present.
* wp-content/mu-plugins/hyper-engine-kit.php, the actual malware that's installed as both a must-use plugin and a normal plugin.
* wp-content/plugins/hyper-engine-kit/hyper-engine-kit.php, a duplicate of the same backdoor payload for redundancy.

Regardless of the method used to launch the backdoor, it carries out a number of actions, including hiding itself from the admin plugins screen or in update checks, communicating with a command-and-control (C2) server using the Ethereum blockchain, fingerprinting the infected site and retrieving additional payloads, creating a hidden administrator account, and running the reinfection loop.

The backdoor's capabilities allow the operator to take control of the WordPress site, fetch arbitrary JavaScript to inject and target site visitors with skimmers (or other malware), run PHP code, and deactivate or delete specific plugins.

"On servers that support System V shared memory, the payload is written into a segment identified by a fixed numeric key," Sucuri said. "That segment lives in RAM, so it survives file deletion and database cleanup alike, and on shared hosting it can even be owned by a different account."

"The infection registers cron hooks, including randomized names alongside a known fetch hook. System cron runs the WordPress cron file, not visitor traffic, then triggers redeployment on schedule."

It's currently not known how the malware was delivered to the WordPress site. However, typical initial access vectors include known security flaws in WordPress, plugins, and themes; weak login credentials; software supply chain attacks targeting popular plugins; and the exploitation of insecure media or form upload features to push PHP web shells into server directories.

"SC is a reminder that a modern WordPress infection can be a system rather than a file," Sucuri said. "This toolkit spreads identical copies of one backdoor across drop-ins, the theme, a fake plugin in two locations, the database, and shared memory, hides its command channel inside legitimate blockchain infrastructure, and rewrites itself from any surviving copy on the very next request."

### wpForo Forum WordPress Plugin Flaw Exploited

The disclosure comes as a high-severity unauthenticated SQL injection flaw in the wpForo Forum WordPress plugin (
[CVE-2026-1581](https://www.cve.org/CVERecord?id=CVE-2026-1581)
, CVSS score: 7.5) has come under active exploitation. The issue affects all versions of the plugin up to, and including, 2.4.14.

According to
[telemetry data from Previdian](https://previdian.com/CVE-2026-1581)
, fewer than 20 exploitation attempts targeting the vulnerability have been observed since July 3, 2026. The activity has originated from five unique attacker IP addresses located in Bulgaria, Switzerland, France, the U.S., and Yemen.