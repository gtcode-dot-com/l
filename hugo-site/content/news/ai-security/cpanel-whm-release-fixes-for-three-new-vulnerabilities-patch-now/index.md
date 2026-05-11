---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-11T02:28:45.854818+00:00'
exported_at: '2026-05-11T02:28:47.458258+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
structured_data:
  about: []
  author: ''
  description: cPanel patched three vulnerabilities, including two 8.8 CVSS flaws,
    reducing risks of code execution and privilege escalation.
  headline: cPanel, WHM Release Fixes for Three New Vulnerabilities — Patch Now
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/cpanel-whm-patch-3-new-vulnerabilities.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: cPanel, WHM Release Fixes for Three New Vulnerabilities — Patch Now
updated_at: '2026-05-11T02:28:45.854818+00:00'
url_hash: aa67df4b71869bbb597849462d34fac18560f251
---

**

Ravie Lakshmanan
**

May 09, 2026

Vulnerability / Web Hosting

cPanel has released updates to address three vulnerabilities in cPanel and Web Host Manager (WHM) that could be exploited to achieve privilege escalation, code execution, and denial-of-service.

The list of vulnerabilities is as follows -

* **[CVE-2026-29201](https://support.cpanel.net/hc/en-us/articles/40311033698327-Security-CVE-2026-29201-cPanel-WHM-WP2-Security-Update-May-08-2026)**
  (CVSS score: 4.3) - An insufficient input validation of the feature file name in the "feature::LOADFEATUREFILE" adminbin call that could result in an arbitrary file read.
* **[CVE-2026-29202](https://support.cpanel.net/hc/en-us/articles/40311426610327-Security-CVE-2026-29202-cPanel-WHM-WP2-Security-Update-May-08-2026)**
  (CVSS score: 8.8) - An insufficient input validation of the "plugin" parameter in the "create\_user API" call that could result in arbitrary Perl code execution on behalf of the already authenticated account's system user.
* **[CVE-2026-29203](https://support.cpanel.net/hc/en-us/articles/40311543760407-Security-CVE-2026-29203-cPanel-WHM-WP2-Security-Update-May-08-2026)**
  (CVSS score: 8.8) - An unsafe symlink handling vulnerability that allows a user to modify access permissions of an arbitrary file using chmod, resulting in denial-of-service or possible privilege escalation.

The shortcomings have been patched in the following versions -

* cPanel and WHM -
  + 11.136.0.9 and higher
  + 11.134.0.25 and higher
  + 11.132.0.31 and higher
  + 11.130.0.22 and higher
  + 11.126.0.58 and higher
  + 11.124.0.37 and higher
  + 11.118.0.66 and higher
  + 11.110.0.116 and higher
  + 11.110.0.117 and higher
  + 11.102.0.41 and higher
  + 11.94.0.30 and higher
  + 11.86.0.43 and higher
* WP Squared -

cPanel has released 110.0.114 as a direct update for customers who are still on CentOS 6 or CloudLinux 6. Users are advised to update to the latest versions for optimal protection.

While there is no evidence that the vulnerabilities have been exploited in the wild, the disclosure comes days after another critical flaw in the product (
[CVE-2026-41940](https://thehackernews.com/2026/05/critical-cpanel-vulnerability.html)
) has been weaponized by threat actors as a zero-day to deliver Mirai botnet variants and a ransomware strain called Sorry.