---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-11T12:15:14.636913+00:00'
exported_at: '2026-01-11T12:15:16.801534+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32616
structured_data:
  about: []
  author: ''
  description: 'YARA-X 1.11.0 Release: Hash Function Warnings, Author: Didier Stevens'
  headline: 'YARA-X 1.11.0 Release: Hash Function Warnings, (Sun, Jan 11th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32616
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'YARA-X 1.11.0 Release: Hash Function Warnings, (Sun, Jan 11th)'
updated_at: '2026-01-11T12:15:14.636913+00:00'
url_hash: e964d92e211e145050aa0c6051901b6921cbaab8
---

[YARA-X's 1.11.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.11.0)
release brings a new feature: hash function warnings.

When you write a YARA rule to match a cryptographic hash (either the full file content or a part of it), what's actually going on are string comparisons:

![](https://isc.sans.edu/diaryimages/images/20260111-120140.png)

Function hash.sha256 returns a string (the hexadecimal SHA256 hash it calculated) and that is compared to a literal string that is the hash you want to find.

If you make a mistake in your literal string hash (for example: unintentionally add an extra space), then the match will fail.

But YARA-X will now show a warning like this:

![](https://isc.sans.edu/diaryimages/images/20260111-120202.png)

Another example is where you mixup hashes: you provide a SHA1 literal string hash, and it should be a SHA256.

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)