---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-29T14:15:14.438021+00:00'
exported_at: '2026-04-29T14:15:16.660491+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32934
structured_data:
  about: []
  author: ''
  description: 'Today''s Odd Web Requests, Author: Johannes Ullrich'
  headline: Today's Odd Web Requests, (Wed, Apr 29th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32934
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Today's Odd Web Requests, (Wed, Apr 29th)
updated_at: '2026-04-29T14:15:14.438021+00:00'
url_hash: 7d096dbd5daba0dc4ac34e4efc182f816700e9f6
---

Today, two different "new" requests hit our honeypots. Both appear to be recon requests and not associated with specific vulnerabilities. But as always, please let me know if you have additional information

1 - Broadcom API Gateway

> GET /bam/restart/if/required
>
> Host: [redacted]:8080
>
> Connection: close

This request is targeting a Broadcom API Gateway endpoint. As is, the request should not cause any problems, but the response may indicate if a Broadcom API Gateway is used, and it could lead to follow-up attacks.

2 - ESP32

> `GET /esps/
>
> host: [redcated]:8080
>
> user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
>
> connection: close
>
> accept: */*
>
> accept-language: en
>
> accept-encoding: gzip`

The path "/esps/" is associated with ESP32 devices. The ESP32 platform is a low-cost system-on-a-chip (SOC) device that is frequently used in IoT devices or even in various home automation projects. The URL '/esps/' may be associated with uploading firmware, but I have not yet seen any follow-up attacks.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|