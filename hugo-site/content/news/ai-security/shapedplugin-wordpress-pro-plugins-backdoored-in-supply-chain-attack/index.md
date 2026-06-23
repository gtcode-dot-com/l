---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:51:07.850834+00:00'
exported_at: '2026-06-23T03:51:10.708038+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html
structured_data:
  about: []
  author: ''
  description: Attackers backdoored ShapedPlugin Pro updates, stealing credentials,
    2FA codes, wp-config.php data, and WooCommerce order details.
  headline: ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/shapedplugin-wordpress-pro-plugins.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: ShapedPlugin WordPress Pro Plugins Backdoored in Supply Chain Attack
updated_at: '2026-06-23T03:51:07.850834+00:00'
url_hash: 68d2130f31731c5f8f0c2242c7894189ac8dcce9
---

**

Ravie Lakshmanan
**

Jun 22, 2026

Supply Chain Attack / Malware

Multiple WordPress plugins from
[ShapedPlugin](https://shapedplugin.com/)
were compromised in a supply chain attack after unknown threat actors managed to tamper with the official release channels and push backdoor code.

"Attackers compromised the vendor's build and distribution pipeline, injecting backdoor code into Pro plugin releases distributed through official licensed update channels," Wordfence
[said](https://www.wordfence.com/blog/2026/06/psa-supply-chain-compromise-targets-shapedplugin-backdoored-pro-plugins-distributed-via-official-channels/)
in an analysis published last week.

The incident affects the following plugins -

* Product Slider Pro for WooCommerce (versions before 3.5.4)
* Real Testimonials Pro (version 3.2.5)
* Smart Post Show Pro (versions before 4.0.2)

As mentioned above, it's worth emphasizing that the compromise only affects Pro plugin builds distributed through the vendor's Easy Digital Downloads (EDD) infrastructure via account.shapedplugin[.]com. The free versions of the plugins on WordPress.org are not impacted.

The supply chain compromise associated with Product Slider Pro for WooCommerce has been assigned the CVE identifier
[CVE-2026-49777](https://www.cve.org/CVERecord?id=CVE-2026-49777)
, along with a CVSS score of 10.0, indicating maximum severity.
[CVE-2026-10735](https://www.cve.org/CVERecord?id=CVE-2026-10735)
(CVSS score: 9.8) is the CVE identifier for the entire incident.

The WordPress security company said the compromised versions of the plugins incorporate a loader that's triggered on every admin page, causing it to fetch a payload from a remote server ("194.76.217[.]28:2871"), install it, and activate it as a fake plugin.

Once it's activated, the malware reports the victim domain back to the server and erases itself to cover up the tracks and complicate incident response efforts. The counterfeit plugin, for its part, hides itself from the WordPress admin plugin list and is capable of capturing credentials in plaintext and two-factor authentication (2FA) codes.

It also establishes multiple persistence methods that enable arbitrary file writes via a custom REST endpoint when provided a specific authentication token, as well as drop a web shell with command execution features. Lastly, it makes use of a PHP file named "install-persistent.php," which is bundled as part of the plugin, to extract the below data -

* Full contents of wp-config.php, including database credentials, authentication keys, and debug settings
* All administrator accounts with registration dates
* Mail plugin credentials from WP Mail SMTP, Post SMTP, and Easy WP SMTP
* WooCommerce order data from the last 3 months with payment method breakdown

Once this information is displayed, the file is deleted. Evidence indicates that the attack could be a compromise of the build pipeline, as opposed to a direct poisoning of the packages.

What's particularly dangerous about this attack is that it exposes site owners who purchased legitimate licenses and installed updates directly from the vendor's official update system to malware.

Upon being notified of the issue, ShapedPlugin has confirmed the incident, adding that it's reviewing the distribution and release processes to ensure the integrity of its products going forward. New versions of the impacted plugins are expected to be released pending comprehensive security reviews and validation tests.

Site owners who have installed the malicious versions are recommended to reset all passwords, revoke and regenerate 2FA secrets for all users, review administrator accounts for unauthorized additions, and check mail plugin configurations for modified SMTP credentials.