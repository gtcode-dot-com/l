---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-18T22:15:16.845931+00:00'
exported_at: '2026-03-18T22:15:20.317411+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32800
structured_data:
  about: []
  author: ''
  description: '/proxy/ URL scans with IP addresses, Author: Johannes Ullrich'
  headline: /proxy/ URL scans with IP addresses, (Mon, Mar 16th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32800
  publisher:
    logo: /favicon.ico
    name: GTCode
title: /proxy/ URL scans with IP addresses, (Mon, Mar 16th)
updated_at: '2026-03-18T22:15:16.845931+00:00'
url_hash: 2cabb10a499091cf92d7dc45f03fcee429530c63
---

Attempts to find proxy servers are among the most common scans our honeypots detect. Most of the time, the attacker attempts to use a host header or include the hostname in the URL to trigger the proxy server forwarding the request. In some cases, common URL prefixes like "/proxy/" are used. This weekend, I noticed a slightly different pattern in our logs:

| First Seen | Last Seen | Count | Path |
| --- | --- | --- | --- |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/http:/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/http:/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/absolute/169.254.169.254/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/dynamic/instance-identity/document |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[0:0:0:0:0:ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[::ffff:a9fe:a9fe]/latest/dynamic/instance-identity/document |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/[::ffff:a9fe:a9fe]/latest/meta-data/iam/security-credentials/ |
| 2026-03-15 | 2026-03-16 | 2 | /proxy/169.254.169.254/latest/dynamic/instance-identity/document |
| 2026-03-16 | 2026-03-16 | 1 | /proxy/2852039166/latest/meta-data/iam/security-credentials/ |

The intent of these requests is to reach the cloud metadata service, which is typically listening on 169.254.169.254, a non-routable link-local address. The "security-credentials" directory should list entities with access to the service, and can then lead to requests for key material used for authentication.

The attacker does not just use the IPv4 address, but attempts to bypasspass some filters by using the IPv4 mapped IPv6 address. The prefix ::ffff/96, followed by the IPv4 address, is used to express IPv4 addresses in IPv6. Note that these addresses are not intended to be routable, but just like 169.254.169.254 they may work on the host itself. In addition, the attacker is used the "less apprviated" form by specifying the first few bytes with 0:0:0:0. Finally, the long unsigned integer form of the IP address is used.

The meta data service is often exploited using SSRF vulenrabilities. However, the more modern "version 2" of the meta data service is attempting to prevent simple SSRF attacks by requiring two requests with different methods and specific custom headers. SSRF vulnerabilities are just like a less functional open proxy. In this case, the attacker assumes a full proxy, and an attack may not be prevented by the more modern meta data service implementation.

Modern web applications use proxies in many different forms. For example you may have API gateways, load balancers, web application firewalls or even still some proxies to bypass CORS constraints. Any of these cases is potentially vulenrable if badly configured. The above list of URLs may make a good starting point to test the implementation of your proxy.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|