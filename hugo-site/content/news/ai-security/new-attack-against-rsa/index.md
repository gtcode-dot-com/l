---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T00:49:30.418345+00:00'
exported_at: '2026-10-06T00:49:33.955919+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html
structured_data:
  about: []
  author: ''
  description: ArsTechnica is reporting on a “new” attack against RSA, one that bypasses
    factoring. First, this attack isn’t new. The original research is from 2007. What
    is new is the implementation. Second, it is a forgery attack. It allows an attacker
    to forge digital signatures. It does not recover the private key from the pub...
  headline: New Attack Against RSA
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Attack Against RSA
updated_at: '2026-10-06T00:49:30.418345+00:00'
url_hash: 390ed4fb33d34dc67c8130fad26a40fe3ac42570
---

## New Attack Against RSA

ArsTechnica is
[reporting](https://arstechnica.com/security/2026/09/theres-a-new-way-to-break-rsa-thats-faster-than-anything-weve-seen-before/)
on a “new” attack against RSA, one that bypasses factoring.

First, this attack isn’t new. The original research is from
[2007](https://eprint.iacr.org/2007/424)
. What is new is the implementation.

Second, it is a forgery attack. It allows an attacker to forge digital signatures. It does not recover the private key from the public key.

Third, the attack only works against pure signatures. That is, signatures without any formatting or padding. This is not generally how we use RSA in practice.

Fourth, speed is all relative. This is not a polynomial-time algorithm; it’s a subexponential-time algorithm. But it is somewhat faster than factoring. The authors were able to forge messages for 1024-bit RSA with 1380 CPU core-years (over five real-world months).

The authors have a
[webpage](https://github.com/ucsd-hacc/NSNFSSSFSFN)
that explains the context much better than the article. And here’s the
[paper](https://eprint.iacr.org/2026/2131.pdf)
.

EDITED TO ADD: Slashdot
[thread](https://it.slashdot.org/story/26/09/24/1652228/theres-a-new-way-to-break-rsa-encryption)
.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[cryptography](https://www.schneier.com/tag/cryptography/)
,
[forgery](https://www.schneier.com/tag/forgery/)
,
[RSA](https://www.schneier.com/tag/rsa/)

[Posted on September 28, 2026 at 7:02 AM](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html)
•
[13 Comments](https://www.schneier.com/blog/archives/2026/09/new-attack-against-rsa.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.