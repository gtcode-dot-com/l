---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-20T12:15:13.130347+00:00'
exported_at: '2026-01-20T12:15:15.668927+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/cloudflare-fixes-acme-validation-bug.html
structured_data:
  about: []
  author: ''
  description: Cloudflare patched an ACME HTTP-01 validation flaw that disabled WAF
    protections and let unauthorized requests reach origin servers.
  headline: Cloudflare Fixes ACME Validation Bug Allowing WAF Bypass to Origin Servers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/cloudflare-fixes-acme-validation-bug.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Cloudflare Fixes ACME Validation Bug Allowing WAF Bypass to Origin Servers
updated_at: '2026-01-20T12:15:13.130347+00:00'
url_hash: dfb9f676f429a311a318f2a4de71a923cebe7daf
---

**

Ravie Lakshmanan
**

Jan 20, 2026

Web Security / Vulnerability

Cloudflare has
[addressed](https://blog.cloudflare.com/acme-path-vulnerability/)
a security vulnerability impacting its Automatic Certificate Management Environment (
[ACME](https://en.wikipedia.org/wiki/Automatic_Certificate_Management_Environment)
) validation logic that made it possible to bypass security controls and access
[origin servers](https://developers.cloudflare.com/fundamentals/security/protect-your-origin-server/)
.

"The vulnerability was rooted in how our edge network processed requests destined for the ACME HTTP-01 challenge path (/.well-known/acme-challenge/\*)," the web infrastructure company's Hrushikesh Deshpande, Andrew Mitchell, and Leland Garofalo said.

The web infrastructure company said it found no evidence that the vulnerability was ever exploited in a malicious context.

ACME is a communications protocol (
[RFC 8555](https://www.rfc-editor.org/rfc/rfc8555)
) that facilitates automatic issuance, renewal, and revocation of SSL/TLS certificates. Every certificate provisioned to a website by a certificate authority (CA) is validated using challenges to prove domain ownership.

This process is typically achieved using an ACME client like
[Certbot](https://letsencrypt.org/docs/client-options/)
that proves domain ownership via an
[HTTP-01](https://letsencrypt.org/docs/challenge-types/)
(or DNS-01) challenge and manages the certificate lifecycle. The HTTP-01 challenge checks for a validation token and a key fingerprint located in the web server at "https://<YOUR\_DOMAIN>/.well-known/acme-challenge/<TOKEN>" over HTTP port 80.

The CA's server makes an HTTP GET request to that exact URL to retrieve the file. Once the verification succeeds, the certificate is issued and the CA marks the ACME account (i.e., the registered entity on its server) as authorized to manage that specific domain.

In the event the challenge is used by a certificate order managed by Cloudflare, then Cloudflare will respond on the aforementioned path and provide the token provided by the CA to the caller. But if it does not correlate to a Cloudflare-managed order, the request is routed to the customer origin, which may be using a different system for domain validation.

The vulnerability,
[discovered and reported](https://fearsoff.org/research/cloudflare-acme)
by FearsOff in October 2025, has to do with a flawed implementation of the ACME validation process that causes certain challenge requests to the URL to disable web application firewall (WAF) rules and allow it to reach the origin server when it should have been ideally blocked.

In other words, the logic failed to verify whether the token in the request actually matched an active challenge for that specific hostname, effectively permitting an attacker to send arbitrary requests to the ACME path and circumvent WAF protections entirely, granting them the ability to reach the origin server.

"Previously, when Cloudflare was serving an HTTP-01 challenge token, if the path requested by the caller matched a token for an active challenge in our system, the logic serving an ACME challenge token would disable WAF features, since Cloudflare would be directly serving the response," the company explained.

"This is done because those features can interfere with the CA's ability to validate the token values and would cause failures with automated certificate orders and renewals. However, in the scenario that the token used was associated with a different zone and not directly managed by Cloudflare, the request would be allowed to proceed onto the customer origin without further processing by WAF rulesets."

Kirill Firsov, founder and CEO of FearsOff, said the vulnerability could be exploited by a malicious user to obtain a deterministic, long‑lived token and access sensitive files on the origin server across all Cloudflare hosts, opening the door to reconnaissance.

The vulnerability was addressed by Cloudflare on October 27, 2025, with a code change that serves the response and disables WAF features only when the request matches a valid ACME HTTP-01 challenge token for that hostname.