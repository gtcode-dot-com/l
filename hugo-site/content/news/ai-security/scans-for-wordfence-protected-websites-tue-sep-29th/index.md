---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:31:18.225011+00:00'
exported_at: '2026-10-07T01:31:21.116058+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33382
structured_data:
  about: []
  author: ''
  description: 'Scans for Wordfence Protected Websites, Author: Johannes Ullrich'
  headline: Scans for Wordfence Protected Websites, (Tue, Sep 29th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33382
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scans for Wordfence Protected Websites, (Tue, Sep 29th)
updated_at: '2026-10-07T01:31:18.225011+00:00'
url_hash: eefc3c7ca91579173d05289539bfb54a1d6805a0
---

Starting yesterday, our sensors picked up a small number of scans for "wordfence-waf.php". This particular script is used by Wordfence, a solution to protect WordPress sites. During the Wordfence install, the wordpress-waf.php file will be created in the site's root directory [1].

The requests themselves are unremarkable, not including any headers like User-Agent. Just the bare minimum "Host" header, which is the IP address of the targeted site.

The file does not include any secrets or configuration parameters, but it includes other scripts intended to run before any WordPress code to assist with Wordfence's integration. My best guess is that attackers may attempt to enumerate Wordfence-protected sites to limit detection. Wordfence collects intelligence from the sites it protects and often publishes information about newly detected attacks. This, in turn, "burns" exploit techniques, as other sites will not be able to protect themselves as well.

Another possible option is that these scans attempt to bypass Wordfence. By using the IP address instead of the hostname, the attacker may attempt to identify Wordfence-protected sites that are directly reachable. This could be used to bypass Wordfence protection and expose sites that rely on it to delays in patching. Web application firewalls and "virtual patching" are only temporary fixes; please follow Wordfence's guidance on preventing the bypassing of its protection. But wordfence-waf.php is part of the "Extended Protection" feature, which is designed to help prevent this type of bypass.

[1] https://www.wordfence.com/help/firewall/optimizing-the-firewall/

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|