---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T20:05:05.820925+00:00'
exported_at: '2026-09-26T20:05:07.864436+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html
structured_data:
  about: []
  author: ''
  description: Attackers are scanning for two miniOrange SAML flaws, including CVE-2026-15981,
    that can bypass login and grant WordPress admin access.
  headline: Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin
    Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/attackers-target-miniorange-saml-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attackers Target miniOrange SAML Flaws That Can Grant WordPress Admin Access
updated_at: '2026-09-26T20:05:05.820925+00:00'
url_hash: aefc8810292db5cb23fd059f57e2eb9ffca9f249
---

**

Ravie Lakshmanan
**

Aug 25, 2026

Vulnerability / Web Security

Bad actors are attempting to exploit two severe unauthenticated authentication bypasses in the Xecurify miniOrange SAML 2.0 Single Sign On plugin that make it possible for an attacker to sign in as any WordPress user, including administrators.

The vulnerabilities, as disclosed by
[Patchstack](https://patchstack.com/articles/one-slug-seven-editions-the-miniorange-saml-sso-bug-that-let-anyone-log-in-as-your-wordpress-admin/)
, are listed below -

* **[CVE-2026-61979](https://www.cve.org/CVERecord?id=CVE-2026-61979)**
  (CVSS score: 8.1) - An unauthenticated privilege escalation vulnerability stemming from signature algorithm confusion (Fixed in version 17.0.5 for the Standard edition)
* **[CVE-2026-15981](https://www.cve.org/CVERecord?id=CVE-2026-15981)**
  (CVSS score: 9.8) - An authentication bypass vulnerability stemming from accepting malformed signatures as valid (Fixed in version 17.0.6 for the Standard edition)

"This is due to the mo\_saml\_validate\_signature() function performing a loose boolean check on the raw tri-state integer returned by PHP's openssl\_verify(), causing an error return value of -1 to be evaluated as truthy and therefore treated as a successful signature verification," according to a description of CVE-2026-15981 on CVE.org.

"This makes it possible for unauthenticated attackers to log in as any existing WordPress user, including administrators, by submitting a crafted SAMLResponse containing an attacker-controlled NameID and a deliberately malformed signature value that triggers an OpenSSL processing error — bypassing verification entirely and resulting in wp\_set\_auth\_cookie() being called for the targeted account."

The WordPress security company, which credited the DigitalOcean security team for reporting the issues, said an attacker can craft a SAML response with a malformed signature and send it to the plugin, causing it to treat it as valid.

The cloud infrastructure provider is said to have discovered the vulnerabilities after observing an anomalous WordPress administrator session attempt from outside their trusted network. "The attacker had already used the bypass to obtain a WordPress admin session cookie, but was stalled because the admin panel operations themselves sat restricted behind the trusted network," Patchstack said.

The scanning activity has been recorded from the following IP addresses -

* 207.211.214.41
* 79.127.224.14
* 102.91.71.83
* 162.243.116.148
* 84.201.6.54
* 64.225.25.188

"The spread suggests opportunistic scanning rather than a targeted campaign," Patchstack added. "Whoever is running this appears to be throwing the exploit at every site with the plugin installed without checking which edition or version is behind it."

WordPress site owners are advised to apply the latest fixes to stay protected, especially given the availability of a proof-of-concept (PoC) code that allows attackers to chain the flaws to obtain admin privileges and take control of susceptible sites.