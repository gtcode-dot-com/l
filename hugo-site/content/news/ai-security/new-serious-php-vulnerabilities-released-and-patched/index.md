---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-08T05:49:49.374357+00:00'
exported_at: '2026-11-08T05:49:50.374770+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html
structured_data:
  about: []
  author: ''
  description: 'PHP maintainers have released fixes for two critical vulnerabilities:
    PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can
    allow unauthenticated remote code execution. All PHP users are strongly encouraged
    to update immediately. Who is at risk: all PHP installations serving web requests,
    i...'
  headline: New Serious PHP Vulnerabilities Released and Patched
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Serious PHP Vulnerabilities Released and Patched
updated_at: '2026-11-08T05:49:49.374357+00:00'
url_hash: ab875104cf1640af9cf9b7bb654865af58f6430b
---

## New Serious PHP Vulnerabilities Released and Patched

PHP maintainers have
[released](https://www.php.net/archive/2026.php#2026-10-20-1)
fixes for two critical vulnerabilities:

&gt; PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately.
&gt;
&gt; Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with mod\_php, php-cgi, FrankenPHP and LiteSpeed. We consider the risk highest for mod\_php, with a demonstrated exploit where an unauthenticated request can trigger the attack before any application code runs.
&gt;
&gt; The vulnerabilities:
&gt;
&gt; * RCE via OOM corruption, CVE-2026-109618 (
&gt;   [GHSA-w8hw-w9fx-j79w](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w)
&gt;   ): out-of-memory handling can interrupt PHP while internal request data is only partially initialized. Request cleanup may then treat the invalid data as valid.
&gt; * RCE via stale global state, CVE-2026-109619 (
&gt;   [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
&gt;   ): request-owned internal state can survive after its backing memory has been freed. A later request handled by the same worker may use that stale state before normal initialization resets it.

Updating PHP is the only way to regain security. Do it now.

More
[news](https://thehackernews.com/2026/10/php2shell-two-unpatched-critical-php.html)
.

[Good](https://www.wired.com/story/this-is-not-a-drill-2-php-vulnerabilities-are-setting-the-internet-on-fire/)
[explanations](https://www.recordedfuture.com/blog/php2shell-vulnerability-exploitation)
.

Tags:
[patching](https://www.schneier.com/tag/patching/)
,
[vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on October 22, 2026 at 9:26 AM](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html)
•
[15 Comments](https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.