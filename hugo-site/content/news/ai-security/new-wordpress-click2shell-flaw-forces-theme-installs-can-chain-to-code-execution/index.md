---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T05:00:45.520727+00:00'
exported_at: '2026-10-03T05:00:47.579629+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html
structured_data:
  about: []
  author: ''
  description: WordPress 7.1.1 fixes Click2Shell, which can force theme installs from
    crafted links and was chained with a theme flaw for code execution.
  headline: New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/new-wordpress-click2shell-flaw-forces.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New WordPress Click2Shell Flaw Forces Theme Installs, Can Chain to Code Execution
updated_at: '2026-10-03T05:00:45.520727+00:00'
url_hash: f7a8a3c8b9b3189884c09a46c52db7a3afc426e9
---

**

Swati Khandelwal
**

Sep 18, 2026

Vulnerability / Web Security

WordPress today released patches to fix a new set of vulnerabilities in its core software, one of which could allow a crafted web link, opened by a logged-in administrator, to install a theme from the official WordPress.org directory without anyone clicking Install.

The security firm
[pwn.ai](https://pwn.ai/blog/click2shell)
, whose researchers reported the flaw, calls the attack chain
**Click2Shell**
. On its own the flaw only installs a real theme that the attacker picks, but the security research team showed it could be combined with a separate weakness in a theme to run the attacker's own code on the server.

The fix shipped on September 17 in
[WordPress 7.1.1](https://wordpress.org/news/2026/09/wordpress-7-1-1-maintenance-and-security-release/)
. Because this is a security release, WordPress advises updating right away. There is no sign the flaw has been used in real attacks.

The installed theme stays switched off, so the site's own appearance does not change and nothing looks wrong. Reaching code execution needed a second, separate flaw in the theme that was installed. As pwn.ai wrote of the core bug alone, "The Core bug does not accept an arbitrary theme ZIP by itself."

The flaw works because two parts of WordPress read the same link differently. The WordPress.org directory treats the value in the link as an ordinary theme name and returns a real theme, but the administrator's browser reuses the original text, punctuation and all, inside code meant to pick out an item on the page. Characters the attacker adds to the link send that code to the Install button, and WordPress's own script clicks it.

Because the administrator is already logged in, their session supplies the permission and the security token the install needs, so the attacker supplies neither.

An installed theme is not always idle. When WordPress builds a preview in its Customizer tool, it can load a theme's PHP code even before the theme is switched on.

The theme pwn.ai used, Mobile Repair Zone, carried a second flaw: a background handler that fetched a web address from the request, downloaded a package, and ran its code, with no check on the visitor's permission or a security token. Chained after the forced install, that handler ran the attacker's code on the server.

The researchers rated the forced-install flaw on its own as high severity, with a CVSS score of 7.1, and the full chain to code execution as critical, at 9.6. WordPress has not published a severity rating of its own, and in its release it described the issue this way: "Specially crafted URLs can automatically install and preview an inactive theme from WordPress.org." No CVE identifier has been assigned yet, though pwn.ai says WordPress plans to add one.

WordPress fixed the flaw in 7.1.1, part of a security release whose fixes reach supported branches back to 4.7. Its
[notes](https://wordpress.org/documentation/wordpress-version/version-7-1-1/)
confirm this flaw from version 6.0 up through the releases just before the fix. Site owners should install 7.1.1, or the matching update for whichever branch they run, and sites set to update automatically will receive it on their own.

If you cannot update at once, note that neither WordPress nor pwn.ai offered a separate workaround, and that the attack still needs a logged-in administrator to open the attacker's link. Updating WordPress core closes the demonstrated attack whatever theme a site runs.

Click2Shell is not the firm's first WordPress core flaw in recent weeks. In August, WordPress fixed
[a similar flaw](https://thehackernews.com/2026/08/new-wordpress-pre-auth-xss-could-lead.html)
pwn.ai found in the login screen and also chained to code execution, and there too WordPress described the risk more narrowly than the researchers did.

A
[different WordPress core flaw](https://thehackernews.com/2026/07/new-wp2shell-wordpress-core-flaw-lets.html)
disclosed in July, called wp2shell, is not connected to pwn.ai's work. That flaw needs no login and no click, and the U.S. cybersecurity agency CISA has listed it as exploited in real attacks, which Click2Shell has not been.