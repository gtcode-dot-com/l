---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-05T22:15:14.783286+00:00'
exported_at: '2026-03-05T22:15:20.716840+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32762
structured_data:
  about: []
  author: ''
  description: 'Bruteforce Scans for CrushFTP , Author: Johannes Ullrich'
  headline: Bruteforce Scans for CrushFTP , (Tue, Mar 3rd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32762
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Bruteforce Scans for CrushFTP , (Tue, Mar 3rd)
updated_at: '2026-03-05T22:15:14.783286+00:00'
url_hash: 0e7cccf0b38e61505f9072242d8976c66b67ab70
---

CrushFTP is a Java-based open source file transfer system. It is offered for multiple operating systems. If you run a CrushFTP instance, you may remember that the software has had some serious vulnerabilities: CVE-2024-4040 (the template-injection flaw that let unauthenticated attackers escape the VFS sandbox and achieve RCE), CVE-2025-31161 (the auth-bypass that handed over the crushadmin account on a silver platter), and the July 2025 zero-day CVE-2025-54309 that was actively exploited in the wild.

But what we are seeing now is not an exploit of a specific vulnerability, but rather simple brute-forcing, looking for lazily configured systems.

The requests we are seeing right now:

> `POST /WebInterface/function/?command=login&username=crushadmin&password=crushadmin HTTP/1.1
>
> Host: [redacted]
>
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.137 Safari/537.36
>
> Content-Length: 0
>
> Accept-Encoding: gzip
>
> Connection: close`

Note that these are POST requests, but the username and password are passed as GET parameters. The body of the request is empty.

During setup, CrushFTP requires that the user configure an admin user. The username is not fixed, but "crushadmin" is one of the suggested usernames. Others are "root" and "admin". There is no default or suggested password. The attacker relies on lazy administrators who use "crushadmin" as both a username and a password.

These attacks originate from 5.189.139.225, a French IP address with a history of exploit attempts targeting simple vulnerabilities. We have seen this IP acting up since around February.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|