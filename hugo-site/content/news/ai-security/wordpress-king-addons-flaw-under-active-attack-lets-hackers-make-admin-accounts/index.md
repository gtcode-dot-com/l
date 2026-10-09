---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-04T00:03:08.188539+00:00'
exported_at: '2025-12-04T00:03:10.711306+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/wordpress-king-addons-flaw-under-active.html
structured_data:
  about: []
  author: ''
  description: Severe King Addons flaw lets attackers register admin accounts; update
    to the patched version to stay secure.
  headline: WordPress King Addons Flaw Under Active Attack Lets Hackers Make Admin
    Accounts
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/wordpress-king-addons-flaw-under-active.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: WordPress King Addons Flaw Under Active Attack Lets Hackers Make Admin Accounts
updated_at: '2025-12-04T00:03:08.188539+00:00'
url_hash: 0e87e1af4880a616a63b01808b04bd1dcaa0a79f
---

**

Dec 03, 2025
**

Ravie Lakshmanan

Vulnerability / Website Security

A critical security flaw impacting a WordPress plugin known as King Addons for Elementor has come under active exploitation in the wild.

The vulnerability,
**[CVE-2025-8489](https://www.cve.org/CVERecord?id=CVE-2025-8489)**
(CVSS score: 9.8), is a case of privilege escalation that allows unauthenticated attackers to grant themselves administrative privileges by simply specifying the administrator user role during registration.

It affects versions from 24.12.92 through 51.1.14. It was patched by the maintainers in version 51.1.35 released on September 25, 2025. Security researcher Peter Thaleikis has been credited with discovering and reporting the flaw. The plugin has over 10,000 active installs.

"This is due to the plugin not properly restricting the roles that users can register with," Wordfence
[said](https://www.wordfence.com/blog/2025/12/attackers-actively-exploiting-critical-vulnerability-in-king-addons-for-elementor-plugin/)
in an alert. "This makes it possible for unauthenticated attackers to register with administrator-level user accounts."

Specifically, the issue is rooted in the "handle\_register\_ajax()" function that's invoked during user registration. But an insecure implementation of the function meant that unauthenticated attackers can specify their role as "administrator" in a crafted HTTP request to the "/wp-admin/admin-ajax.php" endpoint, allowing them to obtain elevated privileges.

Successful exploitation of the vulnerability could enable a bad actor to seize control of a susceptible site that has installed the plugin, and weaponize the access to upload malicious code that can deliver malware, redirect site visitors to sketchy sites, or inject spam.

Wordfence said it has blocked over 48,400 exploit attempts since the flaw was publicly disclosed in late October 2025, with 75 attempts thwarted in the last 24 hours alone. The attacks have originated from the following IP addresses -

* 45.61.157.120
* 182.8.226.228
* 138.199.21.230
* 206.238.221.25
* 2602:fa59:3:424::1

"Attackers may have started actively targeting this vulnerability as early as October 31, 2025, with mass exploitation starting on November 9, 2025," the WordPress security company said.

Site administrators are advised to ensure that they are running the latest version of the plugin, audit their environments for any suspicious admin users, and monitor for any signs of abnormal activity.