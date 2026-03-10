---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-10T02:15:15.194061+00:00'
exported_at: '2026-03-10T02:15:18.691010+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html
structured_data:
  about: []
  author: ''
  description: 'It’s called AirSnitch: Unlike previous Wi-Fi attacks, AirSnitch exploits
    core features in Layers 1 and 2 and the failure to bind and synchronize a client
    across these and higher layers, other nodes, and other network names such as SSIDs
    (Service Set Identifiers). This cross-layer identity desynchronization is the
    ke...'
  headline: New Attack Against Wi-Fi
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Attack Against Wi-Fi
updated_at: '2026-03-10T02:15:15.194061+00:00'
url_hash: 0da3f226fa06f8493b76d66b3ffc34599839d0f5
---

## New Attack Against Wi-Fi

It’s called
[AirSnitch](https://arstechnica.com/security/2026/02/new-airsnitch-attack-breaks-wi-fi-encryption-in-homes-offices-and-enterprises/)
:

> Unlike previous Wi-Fi attacks, AirSnitch exploits core features in Layers 1 and 2 and the failure to bind and synchronize a client across these and higher layers, other nodes, and other network names such as SSIDs (Service Set Identifiers). This cross-layer identity desynchronization is the key driver of AirSnitch attacks.
>
> The most powerful such attack is a full, bidirectional
> [machine-in-the-middle (MitM) attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)
> , meaning the attacker can view and modify data before it makes its way to the intended recipient. The attacker can be on the same SSID, a separate one, or even a separate network segment tied to the same AP. It works against small Wi-Fi networks in both homes and offices and large networks in enterprises.
>
> With the ability to intercept all link-layer traffic (that is, the traffic as it passes between Layers 1 and 2), an attacker can perform other attacks on higher layers. The most dire consequence occurs when an Internet connection isn’t encrypted­—something that Google
> [recently estimated](https://transparencyreport.google.com/https/overview)
> occurred when as much as 6 percent and 20 percent of pages loaded on Windows and Linux, respectively. In these cases, the attacker can view and modify all traffic in the clear and steal authentication cookies, passwords, payment card details, and any other sensitive data. Since many company intranets are sent in plaintext, traffic from them can also be intercepted.
>
> Even when HTTPS is in place, an attacker can still intercept domain look-up traffic and use DNS cache poisoning to corrupt tables stored by the target’s operating system. The AirSnitch MitM also puts the attacker in the position to wage attacks against vulnerabilities that may not be patched. Attackers can also see the external IP addresses hosting webpages being visited and often correlate them with the precise URL.

Here’s the
[paper](https://www.ndss-symposium.org/ndss-paper/airsnitch-demystifying-and-breaking-client-isolation-in-wi-fi-networks/)
.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)
,
[man-in-the-middle attacks](https://www.schneier.com/tag/man-in-the-middle-attacks/)
,
[Wi-Fi](https://www.schneier.com/tag/wi-fi/)

[Posted on March 9, 2026 at 6:57 AM](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html)
•
[8 Comments](https://www.schneier.com/blog/archives/2026/03/new-attack-against-wi-fi.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.