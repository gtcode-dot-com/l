---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-24T00:03:12.893231+00:00'
exported_at: '2025-12-24T00:03:15.082688+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/two-chrome-extensions-caught-secretly.html
structured_data:
  about: []
  author: ''
  description: 'Two Chrome Extensions Caught Secretly Stealing Credentials from Over
    170 Sites | Read more hacking news on The Hacker News cybersecurity news website
    and learn how to protect against cyberattacks and software vulnerabilities. '
  headline: Two Chrome Extensions Caught Secretly Stealing Credentials from Over 170
    Sites
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/two-chrome-extensions-caught-secretly.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Two Chrome Extensions Caught Secretly Stealing Credentials from Over 170 Sites
updated_at: '2025-12-24T00:03:12.893231+00:00'
url_hash: 853a9e3dc18ad645f816b1983f20246f11b4c18a
---

Cybersecurity researchers have
[discovered](https://socket.dev/blog/malicious-chrome-extensions-phantom-shuttle)
two malicious Google Chrome extensions with the same name and published by the same developer that come with capabilities to intercept traffic and capture user credentials.

The extensions are advertised as a "multi-location network speed test plug-in" for developers and foreign trade personnel. Both the browser add-ons are available for download as of writing. The details of the extensions are as follows -

* Phantom Shuttle (ID: fbfldogmkadejddihifklefknmikncaj) - 2,000 users (Published on November 26, 2017)
* Phantom Shuttle (ID: ocpcmfmiidofonkbodpdhgddhlcmcofd) - 180 users (Published on April 27, 2023)

"Users pay subscriptions ranging from ¥9.9 to ¥95.9 CNY ($1.40 to $13.50 USD), believing they're purchasing a legitimate VPN service, but both variants perform identical malicious operations," Socket security researcher Kush Pandya said.

"Behind the subscription facade, the extensions execute complete traffic interception through authentication credential injection, operate as man-in-the-middle proxies, and continuously exfiltrate user data to the threat actor's C2 [command-and-control] server."

Once unsuspecting users make the payment, they receive VIP status and the extensions auto-enable "smarty" proxy mode, which routes traffic from over 170 targeted domains through the C2 infrastructure.

The extensions work as advertised to reinforce the illusion of a functional product. They perform actual latency tests on proxy servers and display connection status, while keeping users in the dark about their main goal, which is to intercept network traffic and steal credentials.

This involves malicious modifications prepended to two JavaScript libraries, namely, jquery-1.12.2.min.js and scripts.js, that come bundled with the extensions. The code is designed to automatically inject hard-coded proxy credentials (topfany / 963852wei) into every HTTP authentication challenge across all websites by registering a listener on chrome.webRequest.onAuthRequired.

"When any website or service requests HTTP authentication (Basic Auth, Digest Auth, or proxy authentication), this listener fires before the browser displays a credential prompt," Pandya explained. "It immediately responds with the hardcoded proxy credentials, completely transparent to the user. The asyncBlocking mode ensures synchronous credential injection, preventing any user interaction."

Once users authenticate to a proxy server, the extension configures Chrome's proxy settings using a Proxy Auto-Configuration (
[PAC](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Proxy_servers_and_tunneling/Proxy_Auto-Configuration_PAC_file)
) script to implement three modes -

* close, which disables the proxy feature
* always, which routes all web traffic through the proxy
* smarty, which routes a hard-coded list of more than 170 high-value domains through the proxy

The list of domains includes developer platforms (GitHub, Stack Overflow, Docker), cloud services (Amazon Web Services, Digital Ocean, Microsoft Azure), enterprise solutions (Cisco, IBM, VMware), social media (Facebook, Instagram, Twitter), and adult content sites. The inclusion of pornographic sites is likely an attempt to blackmail victims, Socket theorized.

The net result of this behavior is that user web traffic is routed through threat actor-controlled proxies while the extension maintains a 60-second heartbeat to its C2 server at phantomshuttle[.]space, a domain that remains operational. It also grants the attacker a "man-in-the-middle" (MitM) position to capture traffic, manipulate responses, and inject arbitrary payloads.

More importantly, the heartbeat message transmits a VIP user's email, password in plaintext, and version number to an external server via an HTTP GET request every five minutes for continuous credential exfiltration and session monitoring.

"The combination of heartbeat exfiltration (credentials and metadata) plus proxy MitM (real-time traffic capture) provides comprehensive data theft capabilities operating continuously while the extension remains active," Socket said.

Put differently, the extension captures passwords, credit card numbers, authentication cookies, browsing history, form data, API keys, and access tokens from users accessing the targeted domains while VIP mode is active. What's more, the theft of developer secrets could pave the way for supply chain attacks.

It's currently not known who is behind the eight-year-old operation, but the use of Chinese language in the extension description, the presence of Alipay/WeChat Pay integration to make payments, and the use of Alibaba Cloud to host the C2 domain points to a China-based operation.

"The subscription model creates victim retention while generating revenue, and the professional infrastructure with payment integration presents a facade of legitimacy," Socket said. "Users believe they're
[purchasing a VPN service](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)
while unknowingly enabling complete traffic compromise."

The findings highlight how browser-based extensions are becoming an unmanaged risk layer for enterprises. Users who have installed the extensions are advised to remove them as soon as possible. For security teams, it's essential to deploy extension allowlisting, monitor for extensions with subscription payment systems combined with proxy permissions, and implement network monitoring for suspicious proxy authentication attempts.