---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T23:19:05.045835+00:00'
exported_at: '2026-10-04T23:19:06.362119+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33366
structured_data:
  about: []
  author: ''
  description: 'One URL, Three Different Tricks, Author: Xavier Mertens'
  headline: One URL, Three Different Tricks, (Thu, Sep 24th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33366
  publisher:
    logo: /favicon.ico
    name: GTCode
title: One URL, Three Different Tricks, (Thu, Sep 24th)
updated_at: '2026-10-04T23:19:05.045835+00:00'
url_hash: 0e4bd9fbb923a7f786486e8869b488dd18096df4
---

Yesterday, we received a phishing email with an interesting link. At first sight, it looks like garbage, but every piece of it has been carefully crafted to confuse basic security controls. Here is the defanged link:

```
hxxps://YKZjqa7A@gynd--[.]koncar-hr[.]com/[email protected]
```

Let's break it down...

The first trick is the old "userinfo" field. According to RFC 3986[
[1](https://www.rfc-editor.org/info/rfc3986/)
], everything between the scheme and an "@" inside the authority is treated as credentials ("user:password@host"). Browsers silently ignore it, but it has two advantages for the attacker. The random string ("YKZjqa7A") makes every URL unique, which defeats exact-match blocklists and URL reputation lookups. It probably also acts as a tracking token per victim or campaign. As a side effect, the whole thing now looks like an email address to any tool that doesn't parse URLs strictly.

The second trick is the hostname itself: "gynd--.koncar-hr.com". Per the classic hostname rules (RFC 952/1123[
[2](https://www.rfc-editor.org/info/rfc952/)
]), a label can't start or end with a hyphen. DNS doesn't care, and browsers happily resolve and visit it. However, strict validators, regex-based URL extractors, and some link-rewriting or sandboxing solutions may consider it invalid and simply skip it. A URL that is never extracted is never scanned. The random subdomain also suggests wildcard DNS, so each victim gets a brand-new hostname that no blocklist knows. The parent domain is a lookalike of the legitimate "koncar.hr" (a Croatian industrial group), with the ccTLD turned into a hyphenated ".com".

The last trick is the victim's email address, appended in the path. This is common with phishing kits: the page reads the path, pre-fills the login form with the victim's address, and sometimes adapts the branding to the email domain. There is another benefit, though. A poorly written parser that splits the string on the
*last*
"@" will conclude that the host is "isc.sans.edu", the recipient's own trusted domain! Per the WHATWG[
[3](https://url.spec.whatwg.org)
] URL standard, the authority ends at the first "/", so the browser correctly connects to the attacker's server.

The result is a single string that tells three different stories. A naive filter sees two email addresses or a link to your own domain. A strict validator sees an invalid hostname and drops it. The browser sees a perfectly valid URL and takes the victim straight to the phishing page. Attackers aren't exploiting a vulnerability here but the differences between parsers.

Tip: If you want to hunt for this kind of link, look for URLs with more than one "@", hostname labels starting or ending with a hyphen, and paths containing the recipient's own email address.

[1]
&lt;https://www.rfc-editor.org/info/rfc3986/&gt;

[2]
&lt;https://www.rfc-editor.org/info/rfc952/&gt;

[3]
&lt;https://url.spec.whatwg.org&gt;

Xavier Mertens (@xme)

Senior ISC Handler | SANS Principal Instructor | Freelance Consultant

[Xameco](https://xameco.be)
|
[PGP Key](https://xameco.be/pgpkey.txt)