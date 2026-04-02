---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:03:22.225690+00:00'
exported_at: '2026-04-02T04:03:24.670905+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html
structured_data:
  about: []
  author: ''
  description: WebRTC skimmer exploits PolyShell flaw since March 19, hitting 56.7%
    stores, enabling stealth data theft bypassing CSP.
  headline: WebRTC Skimmer Bypasses CSP to Steal Payment Data from E-Commerce Sites
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: WebRTC Skimmer Bypasses CSP to Steal Payment Data from E-Commerce Sites
updated_at: '2026-04-02T04:03:22.225690+00:00'
url_hash: d77751784568b0c148e8e918ee870cbd32b16f47
---

**

Ravie Lakshmanan
**

Mar 26, 2026

Malware / Web Security

Cybersecurity researchers have discovered a new
[payment skimmer](https://thehackernews.com/2026/01/long-running-web-skimming-campaign.html)
that uses
[WebRTC data channels](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API/Using_data_channels)
as a means to receive payloads and exfiltrate data, effectively bypassing security controls.

"Instead of the usual HTTP requests or image beacons, this malware uses WebRTC data channels to load its payload and exfiltrate stolen payment data," Sansec
[said](https://sansec.io/research/webrtc-skimmer)
in a report published this week.

The attack, which targeted a car maker's e-commerce website, is said to have been facilitated by
[PolyShell](https://thehackernews.com/2026/03/magento-polyshell-flaw-enables.html)
, a new vulnerability impacting Magento Open Source and Adobe Commerce that allows unauthenticated attackers to upload arbitrary executables via the REST API and achieve code execution.

Notably, the vulnerability has since come under mass exploitation since March 19, 2026, with more than 50 IP addresses participating in the scanning activity. The Dutch security company said it has found PolyShell attacks on 56.7% of all vulnerable stores.

The skimmer is designed as a self-executing script that establishes a WebRTC peer connection to a hard-coded IP address ("202.181.177[.]177") over UDP port 3479 and retrieves JavaScript code that's subsequently injected into the web page for stealing payment information.

The use of WebRTC marks a significant evolution in skimmer attacks, as it bypasses Content Security Policy (
[CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
) directives.

"A store with a strict CSP that blocks all unauthorized HTTP connections is still wide open to WebRTC-based exfiltration," Sansec noted. "The traffic itself is also harder to detect. WebRTC DataChannels run over DTLS-encrypted UDP, not HTTP. Network security tools that inspect HTTP traffic will never see the stolen data leave."

Adobe released a fix for PolyShell in
[version 2.4.9-beta1](https://experienceleague.adobe.com/en/docs/commerce-operations/release/notes/adobe-commerce/2-4-9?lang=en#highlights-in-v249-beta1)
released on March 10, 2026. But the patch has yet to reach the production versions.

As mitigations, site owners are recommended to block access to the "pub/media/custom\_options/" directory and scan the stores for web shells, backdoors, and other malware.

### More Details About PolyShell Emerge

The development comes as Searchlight Cyber's Assetnote team
[shared](https://slcyber.io/research-center/magento-polyshell-unauthenticated-file-upload-to-rce-in-magento-apsb25-94/)
additional details of the PolyShell vulnerability, stating it's rooted in a function named ImageProcessor::processImageContent(), which accepts any "valid" image as input and move the file to destination folder (i.e., "pub/media/custom\_options/quote/<FIRST\_CHAR>/<SECOND\_CHAR>/<FILE\_NAME>").

As for what constitutes a valid image, the code checks that it's not empty, has a size, has a valid MIME type, and does not have blocked characters in its file name. In other words, there is no validation to ensure that the file extension actually matches the MIME type.

This allows an attacker to upload a polyglot shell via an HTTP POST request to the "/rest/default/V1/guest-carts/{cart\_id}/items" endpoint and invoke that file to achieve code execution. An important caveat here is that the uploaded file is only accessible if the web server is misconfigured; any attempt to access it will result in a 404 error message.

"If you're using Adobe’s suggested Nginx/Apache configurations, then the files are inaccessible and not executable," security researcher Tomais Williamson said. "However, any deviations from this configuration (or missing .htaccess files) may lead to instances being impacted."

"For Nginx instances, Magento ships with an example configuration file that should block access to the folders and any uploaded PHP files. Deviations from this configuration that remove the deny all clauses locations affecting the pub/media/custom\_options path can lead to XSS, and removing .php execution restrictions will lead to those files being executable."

*(The story was updated after publication to include insights from Searchlight Cyber about PolyShell.)*