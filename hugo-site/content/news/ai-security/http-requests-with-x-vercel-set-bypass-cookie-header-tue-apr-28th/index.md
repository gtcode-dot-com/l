---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-28T14:15:14.158964+00:00'
exported_at: '2026-04-28T14:15:16.326306+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32930
structured_data:
  about: []
  author: ''
  description: 'HTTP Requests with X-Vercel-Set-Bypass-Cookie Header, Author: Johannes
    Ullrich'
  headline: HTTP Requests with X-Vercel-Set-Bypass-Cookie Header, (Tue, Apr 28th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32930
  publisher:
    logo: /favicon.ico
    name: GTCode
title: HTTP Requests with X-Vercel-Set-Bypass-Cookie Header, (Tue, Apr 28th)
updated_at: '2026-04-28T14:15:14.158964+00:00'
url_hash: 2ea983e73d3ca5e818006595428a41dd296ddb6f
---

This weekend, we saw a few requests to our honeypot that included an "X-Vercel-Set-Bypass-Cookie" header. A sample request:

> GET / HTTP/1.1
>
> User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
>
> Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,\*/ \*;q=0.8
>
> Accept-Language: en-US,en;q=0.5
>
> Accept-Encoding: gzip, deflate, br
>
> Cache-Control: no-cache
>
> Pragma: no-cache
>
> Connection: keep-alive
>
> X-Vercel-Set-Bypass-Cookie: samesite-none-secure
>
> Upgrade-Insecure-Requests: 1
>
> X-Forwarded-From: 21.235.92.139
>
> X-Real-Iphone: 21.235.92.139
>
> Referer: [redacted, same as "Host" header]
>
> Host: [redacted]

Vercel documents the "x-vercel-protection-bypass" header(note: no "Cookie" part) as a secret that can be configured to disable certain protections during testing. This type of bypass feature is common in various platforms. In particular, web application firewall features often need to be disabled to allow higher request rates during CI/CD pipeline operations. The value set in the header is a user-configurable secret[1].

The X-Vercel-Set-Bypass-Cookie allows testing in browsers and maintains the bypass by having the server set a cookie to indicate the bypass. There are two options according to Vercel's documentation:

1. True: enables the cookie
2. samesitenone: enables the cookie, and set the same-site property to none.

I did not see the "
samesite-none-secure
" documented by Vercel.

The most likely intention of the header is to relax security settings, maybe even steal secrets, should Vercel expose them in the cookie. I have not had a chance to test the request against a Vercel website. Any input as to the intent is welcome.

The request was also set via an open proxy, likely to protect the attacker's identity, but it failed due to the configured proxy headers.

[1] https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|