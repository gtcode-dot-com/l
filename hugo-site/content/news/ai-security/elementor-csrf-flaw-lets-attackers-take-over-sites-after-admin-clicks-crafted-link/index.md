---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-05T04:00:21.241511+00:00'
exported_at: '2026-10-05T04:00:23.364407+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html
structured_data:
  about: []
  author: ''
  description: Elementor 4.3.0 and 4.3.1 contain a CSRF flaw that can create an admin
    account when a logged-in administrator opens a crafted link.
  headline: Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks
    Crafted Link
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/elementor-csrf-flaw-lets-attackers-take.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Elementor CSRF Flaw Lets Attackers Take Over Sites After Admin Clicks Crafted
  Link
updated_at: '2026-10-05T04:00:21.241511+00:00'
url_hash: 06ab9a4d91a46080af41bfa93b3e61e5dc1727c6
---

**

Ravie Lakshmanan
**

Sep 26, 2026

Vulnerability / Web Security

Details have emerged about a high-severity security flaw in the Elementor Website Builder WordPress plugin that could be exploited by an unauthenticated attacker to create rogue administrator accounts and take control of a site.

The cross-site request forgery (CSRF) vulnerability, which has yet to be assigned a CVE identifier, carries a CVSS score of 8.8 out of 10.0. It only affects versions 4.3.0 and 4.3.1 of the plugin, which is active on over 10 million WordPress sites. Statistics from WordPress.org
[show](https://wordpress.org/plugins/elementor/advanced/)
that the two impacted versions alone have been installed on more than 2 million sites.

"One link, opened by a logged-in WordPress user, makes that user carry out any REST API action their account is permitted to perform," Patchstack
[said](https://patchstack.com/articles/cross-site-request-forgery-in-elementor-plugin-affecting-2-million-sites/)
. "On a stock installation, an administrator clicking the link creates a second administrator account for the attacker."

The WordPress security company said the attack does not hinge on any prerequisite, such as JavaScript, a submitted form, or a web page under the threat actor's control. The link can even be a plain anchor tag embedded in an email, a chat message, or a comment.

Following responsible disclosure, the issue has been addressed in
[version 4.3.2](https://elementor.com/pro/changelog/)
released earlier this week. A security researcher going by the alias "Saggre" has been credited with discovering and reporting the bug.

Patchstack said the vulnerability stems from the Editor Events module skipping CSRF protection for cookie-authenticated REST API requests every time the literal string "elementor/v1/events/" appears anywhere in the request URI.

"Because the request URI includes the query string, and the query string is written by whoever composes the link, any REST request can opt itself out of that protection by appending a harmless-looking parameter," it added.

The bypass applies to the entire REST API surface of a site, including WordPress core routes and the routes of every other plugin installed on it. An attacker could exploit this loophole to create an administrator account through "/wp/v2/users" using a request like below -

```
https://example.com/wp-json/wp/v2/users
?_method=POST
&amp;username=csrfadmin
&amp;email=csrfadmin%40example.test
&amp;password=...
&amp;roles%5B%5D=administrator
&amp;x=elementor/v1/events/
```

Because Elementor releases before 4.3.0 do not ship the Editor Events proxy, they are not affected by the flaw. Users of the plugin are advised to apply the latest update as soon as possible to counter any potential threat.