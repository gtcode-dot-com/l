---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-30T02:37:53.553586+00:00'
exported_at: '2026-09-30T02:37:55.472778+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33324
structured_data:
  about: []
  author: ''
  description: 'Scans for Proxmox Servers, Author: Johannes Ullrich'
  headline: Scans for Proxmox Servers, (Wed, Sep 9th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33324
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scans for Proxmox Servers, (Wed, Sep 9th)
updated_at: '2026-09-30T02:37:53.553586+00:00'
url_hash: 29987adf12fb95bf7a88cc9c8ded6ef1011fcbd2
---

About a week ago, Proxmox published an advisory revealing a vulnerability in older versions of Proxmox VE, its flagship Virtual Environment product. The vulnerability only affects version 7, which has not been supported for a couple of years now.

But it appears that the vulnerability may have caught the attention of some attackers and researchers. We do see a bump in scans for port 8006, and also some additional brute force traffic. For example, brute force requests like:

&gt; `POST /api2/json/access/ticket HTTP/1.1
&gt;
&gt; Host: [redacted]:8006
&gt;
&gt; User-Agent: Go-http-client/1.1
&gt;
&gt; Content-Length: 37
&gt;
&gt; Content-Type: application/x-www-form-urlencoded
&gt;
&gt; Accept-Encoding: gzip`
&gt;
&gt; `password=Ww778899&amp;username=root%40pam`

The PVE proxy log will log failed login attempts with a 401 status code:

&gt; `::ffff:62.60.130.193 - - [09/09/2026:15:26:14 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:28:04 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:28:08 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:29:49 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:29:52 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:31:33 +0000] "POST /api2/json/access/ticket HTTP/1.1" 308 18
&gt;
&gt; ::ffff:62.60.130.193 - - [09/09/2026:15:31:36 +0000] "POST /api2/json/access/ticket HTTP/1.1" 401 50`

You may also see the less commonly used 308 status code if the attacker does not use TLS on their first attempt and instead sends a POST request (as shown above). A 308 access code allows a client to change the request method after following the redirect. 301 and 302 status codes require the same method for the follow-up request.

Other scans I have seen:

Classic Fingerprinting

&gt; `/pve2/images/logo-128.png???????`

And a POST request to
`/api2/extjs/access/ticket`
. This endpoint behaves differently from the prior endpoint. It always returns 200, but the JSON payload will contain the login failed messages. These are trickier to analyze because the proxy log does not indicate the outcome of authentication. A return payload size of 77 bytes should indicate failure.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|