---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T16:15:15.503925+00:00'
exported_at: '2026-02-02T16:15:18.150446+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32674
structured_data:
  about: []
  author: ''
  description: 'Scanning for exposed Anthropic Models, Author: Johannes Ullrich'
  headline: Scanning for exposed Anthropic Models, (Mon, Feb 2nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32674
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Scanning for exposed Anthropic Models, (Mon, Feb 2nd)
updated_at: '2026-02-02T16:15:15.503925+00:00'
url_hash: c068eb246ffb4f032eaf69d6468630039f732179
---

Yesterday, a single IP address (
[204.76.203.210](/ipinfo.html?ip=204.76.203.210)
) scanned a number of our sensors for what looks like an anthropic API node. The IP address is known to be a Tor exit node.

The requests are pretty simple:

> `GET /anthropic/v1/models
>
> Host: 67.171.182.193:8000
>
> X-Api-Key: password
>
> Anthropic-Version: 2023-06-01`

It looks like this is scanning for locally hosted Anthropic models, but it is not clear to me if this would be successful. If anyone has any insights, please let me know. The API Key is a commonly used key in documentation, and not a key that anybody would expect to work.

At the same time, we are also seeing a small increase in requests for "/v1/messages". These requests have been more common in the past, but the URL may be associated with Anthropic (it is, however, somewhat generic, and it is likely other APIs use the same endpoint. These requests originate from
[154.83.103.179](/ipinfo.html?ip=154.83.103.179)
, an IP address with a bit a complex geolocation and routing footprint.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|