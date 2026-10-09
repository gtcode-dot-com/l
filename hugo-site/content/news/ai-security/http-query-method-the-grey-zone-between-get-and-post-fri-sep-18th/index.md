---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T22:19:28.179697+00:00'
exported_at: '2026-10-03T22:19:30.137521+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33352
structured_data:
  about: []
  author: ''
  description: 'HTTP QUERY Method: The Grey Zone Between GET And POST., Author: Xavier
    Mertens'
  headline: 'HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33352
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'HTTP QUERY Method: The Grey Zone Between GET And POST., (Fri, Sep 18th)'
updated_at: '2026-10-03T22:19:28.179697+00:00'
url_hash: 7c704cae3839d0ec7004b79d0dd1038a8feb6842
---

In June 2026 the IETF published RFC 10008[
[1](https://www.rfc-editor.org/info/rfc10008/)
], defining a new HTTP method: "QUERY". The HTTP protocol faced already by changes (HTTP/2, HTTP/3) but it’s the first new standard HTTP verb since "PATCH" in 2010!

This new method sits between “GET” and “POST” and can be resumed like this: “QUERY is a GET with a body
**”.**
It's safe and idempotent: the request is processed without state change and can be automatically repeated or restarted without concern for partial state changes. The query itself lives in the request body instead of the URL, and it's explicitly cacheable. Servers advertise the body formats they'll accept via a new “Accept-Query” response header.

If you defend web infrastructure, the interesting part isn't the RFC. The risk is that every control you own that pattern-matches on HTTP methods was written before "QUERY" existed.
WAF rules, API-gateway allowlists, CSRF middleware, cache keying, load-balancer method handling is written in terms of a known verb set: GET, POST, PUT, DELETE, PATCH.  Drop a sixth verb that behaves like a hybrid of the first two into that world and each control now has to make a
*deliberate*
decision about it. Most of them currently make an accidental one.

And the behaviour in the wild is genuinely inconsistent. Researchers found that nginx's limit\_except pattern and Django's View class reject QUERY outright, while curl, FastAPI's explicit routes, Caddy and Traefik pass it through untouched. On caching, one researcher built a QUERY-only API and found nginx forwards it happily and caches it never[
[2](https://dev.to/alexgeorgiev17/nginxs-limitexcept-block-silently-rejects-the-new-http-query-method-1gcg)
].

Think about this HTTP request:

```
curl -X QUERY https://target.com/api/search \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "q=' OR 1=1--" -v
```

If your WAF signatures (SQLi, XSS, command injection) are bound to "POST" bodies but never taught that "QUERY" also carries a body, you get a clean inspection bypass. The test is trivial: send the same malicious payload over "POST" and over "QUERY" and diff the outcome. If the "QUERY" version sails through where the "POST" version gets blocked, that's a live gap, not a theoretical one.

Because "QUERY" is cacheable and safe by spec, caches that don't key on the full request body can be poisoned into serving one user's malicious payload to the next, and CSRF middleware hardcoded to the classic state-changing verbs will wave through any "QUERY" endpoint that carries an unintended side effect.

The new method is not popular yet, here is an overview of what I found:

| Layer | Component | Status |
| --- | --- | --- |
| Clients | curl | Works today via "-x query" |
|  | Node.js / fetch (server-side), Python (httpx/requests), Go net/http, Rust reqwest | Already let you send arbitrary method strings, so QUERY works between your own services right now |
|  | Browser fetch() / XHR | Can send it, but QUERY is not CORS-safelisted → always triggers an OPTIONS preflight; browser HTTP cache should not be assumed to cache QUERY responses yet |
|  | .NET 10 | First-class support out of the box |
|  | HTTP.jl (Julia) | Merged June 2026 — client + server, retries, redirect handling, Accept-Query |
| Servers / proxies | nginx | Proxies it, never caches it. Four identical QUERY requests hit the backend four times; four POSTs hit it once. Also, the limit-except pattern silently rejects QUERY. |
|  | Caddy, Traefik | Pass it through untouched |
|  | Apache | Needs config adjustment to recognize the method and handle OPTIONS/CORS |
| Frameworks | Fast API | Explicit routes pass it through |
|  | Django | The `View` class rejects it outright |
|  | Spring (Java) | Maintainers deliberately scoping it down to "teach the framework QUERY exists" and waiting on adoption feedback before expanding |
| CDN | Cloudflare, Akamai | Co-authored the RFC, so edge/CDN support is expected to lead framework support, but reliable at-scale QUERY caching isn't there yet |

What can you actually do?

Update your rules/regexes to support the new verb:

```
http.method in ("GET","POST", "QUERY")
```

I searched across my HTTP-related logs and found no occurrence of QUERY request but it’s for sure a question of time.

And from a malware point of view? Is there a risk? Most of what a modern SOC actually relies on to catch C2 is behavioral, and behavioral detection doesn't care about the verb:

* Beaconing analysis (RITA/AC-Hunter-style connection-count and interval work), jitter/timing, volume, and flow shape are all method-agnostic. A "QUERY" beacon beacons exactly like a "POST" beacon.
* JA3/JA4 and TLS fingerprinting sit below the HTTP method entirely.
* For HTTPS C2 — which is nearly everything now — the method is inside  the TLS tunnel. A network sensor without interception never sees "GET" vs "POST" vs "QUERY" in the first place, so "QUERY" changes nothing unless you're decrypting.

[1]
&lt;https://www.rfc-editor.org/info/rfc10008/&gt;

[2]
&lt;https://dev.to/alexgeorgiev17/nginxs-limitexcept-block-silently-rejects-the-new-http-query-method-1gcg&gt;

Xavier Mertens (@xme)

Senior ISC Handler | SANS Principal Instructor | Freelance Consultant

[Xameco](https://xameco.be)
|
[PGP Key](https://xameco.be/pgpkey.txt)