---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-16T12:03:12.118134+00:00'
exported_at: '2025-12-16T12:03:14.870992+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/freepbx-authentication-bypass-exposed.html
structured_data:
  about: []
  author: ''
  description: FreePBX patched 2025 flaws allowing SQL injection, file upload attacks,
    and an auth bypass only when webserver AUTHTYPE was enabled.
  headline: FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws
    Enabling RCE
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/freepbx-authentication-bypass-exposed.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: FreePBX Patches Critical SQLi, File-Upload, and AUTHTYPE Bypass Flaws Enabling
  RCE
updated_at: '2025-12-16T12:03:12.118134+00:00'
url_hash: a484395c2856313bb7be7f69a7276014f7148e74
---

**

Dec 15, 2025
**

Ravie Lakshmanan

Vulnerability / Software Security

Multiple security vulnerabilities have been
[disclosed](https://horizon3.ai/attack-research/the-freepbx-rabbit-hole-cve-2025-66039-and-others/)
in the open-source private branch exchange (PBX) platform FreePBX, including a critical flaw that could result in an authentication bypass under certain configurations.

The shortcomings, discovered by Horizon3.ai and reported to the project maintainers on September 15, 2025, are listed below -

* **[CVE-2025-61675](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-292p-rj6h-54cp)**
  (CVSS score: 8.6) - Numerous authenticated SQL injection vulnerabilities impacting four unique endpoints (basestation, model, firmware, and custom extension) and 11 affected parameters that enable read and write access to the underlying SQL database
* **[CVE-2025-61678](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-7p8x-8m3m-58j9)**
  (CVSS score: 8.6) - An authenticated arbitrary file upload vulnerability that allows an attacker to exploit the firmware upload endpoint to upload a PHP web shell after obtaining a valid PHPSESSID and run arbitrary commands to leak the contents of sensitive files (e.g., "/etc/passwd")
* **[CVE-2025-66039](https://github.com/FreePBX/security-reporting/security/advisories/GHSA-9jvh-mv6x-w698)**
  (CVSS score: 9.3) - An authentication bypass vulnerability that occurs when the "Authorization Type" (aka AUTHTYPE) is set to "webserver," allowing an attacker to log in to the Administrator Control Panel via a forged Authorization header

[![Cybersecurity](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://thehackernews.uk/rat-d)

It's worth mentioning here that the authentication bypass is not vulnerable in the default configuration of FreePBX, given that the "Authorization Type" option is only displayed when the three following values in the Advanced Settings Details are set to "Yes":

* Display Friendly Name
* Display Readonly Settings, and
* Override Readonly Settings

However, once the prerequisite is met, an attacker could send crafted HTTP requests to sidestep authentication and insert a malicious user into the "ampusers" database table, effectively accomplishing something similar to
[CVE-2025-57819](https://thehackernews.com/2025/08/freepbx-servers-targeted-by-zero-day.html)
, another flaw in FreePBX that was disclosed as having been actively exploited in the wild in September 2025.

"These vulnerabilities are easily exploitable and enable authenticated/unauthenticated remote attackers to achieve remote code execution on vulnerable FreePBX instances," Horizon3.ai security researcher Noah King said in a report published last week.

The issues have been addressed in the following versions -

* **CVE-2025-61675**
  and
  **CVE-2025-61678**
  - 16.0.92 and 17.0.6 (Fixed on October 14, 2025)
* **CVE-2025-66039**
  - 16.0.44 and 17.0.23 (Fixed on December 9, 2025)

In addition, the option to choose an authentication provider has now been removed from Advanced Settings and requires users to set it manually through the command-line using fwconsole. As temporary mitigations, FreePBX has recommended that users set "Authorization Type" to "usermanager," set "Override Readonly Settings" to "No," apply the new configuration, and reboot the system to disconnect any rogue sessions.

"If you did find that web server AUTHTYPE was enabled inadvertently, then you should fully analyze your system for signs of any potential compromise," it said.

Users are also displayed a warning on the dashboard, stating "webserver" may offer reduced security compared to "usermanager." For optimal protection, it's advised to avoid using this authentication type.

"It's important to note that the underlying vulnerable code is still present and relies on authentication layers in front to provide security and access to the FreePBX instance," King said. "It still requires passing an Authorization header with a basic Base64-encoded username:password."

"Depending on the endpoint, we noticed a valid username was required. In other cases, such as the file upload shared above, a valid username is not required, and you can achieve remote code execution with a few steps, as outlined. It is best practice not to use the authentication type webserver as it appears to be legacy code."