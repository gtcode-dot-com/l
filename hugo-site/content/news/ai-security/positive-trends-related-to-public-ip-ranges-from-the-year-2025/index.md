---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-19T12:03:14.016485+00:00'
exported_at: '2025-12-19T12:03:16.248023+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32584
structured_data:
  about: []
  author: ''
  description: 'Positive trends related to public IP ranges from the year 2025, Author:
    Jan Kopriva'
  headline: Positive trends related to public IP ranges from the year 2025, (Thu,
    Dec 18th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32584
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Positive trends related to public IP ranges from the year 2025, (Thu, Dec 18th)
updated_at: '2025-12-19T12:03:14.016485+00:00'
url_hash: abbb699b8db31a8a7c32313030e4669830b84bf4
---

Since the end of the year is quickly approaching, it is undoubtedly a good time to look back at what the past twelve months have brought to us… And given that the entire cyber security profession is about protecting various systems from “bad things” (and we’ve all correspondingly seen more than our share of the “bad”), I thought that it might be pleasant to look at a few positive background trends that have accompanied us throughout the year, without us necessarily noticing…

It should be mentioned that all the following charts are based on data gathered from
[Shodan](https://www.shodan.io/)
using my
[TriOp tool](https://untrustednetwork.net/en/triop/)
, which means that they are certainly not exact. Nevertheless, the data is undoubtedly good enough to show us the general trends.

The first positive trend that deserves a mention is the overall decrease in the number of industrial control systems accessible from the global internet. Although, based on Shodan data, there still appear to be more than 100 thousand public IP addresses that expose a system that may be classified as ICS on one or more ports, the number has fallen by more than 10% since the beginning of the year…

[![](https://isc.sans.edu/diaryimages/images/25-12-18-ics.png)](https://isc.sans.edu/diaryimages/images/25-12-18-ics.png)

Two other positive trends worth mentioning are related to the support of SSLv2 and SSLv3 on port 443.

While, at the beginning of the year, there were almost 2 million web servers that supported SSLv3, at the time of writing there seem to be only a little more than 1 million of them still left on the public internet.

[![](https://isc.sans.edu/diaryimages/images/25-12-18-ssl3.png)](https://isc.sans.edu/diaryimages/images/25-12-18-ssl3.png)

The situation has similarly improved in terms of public IP addresses exposing web servers that still support SSLv2. In January, there were more than 320 thousand such servers, while now only about 145 thousand of them seem to remain in December (unsurprisingly, a significant percentage of these servers seem to be located in Kazakhstan, which is something we’ve discussed previously[
[1](https://isc.sans.edu/diary/29988)
]).

[![](https://isc.sans.edu/diaryimages/images/25-12-18-ssl2.png)](https://isc.sans.edu/diaryimages/images/25-12-18-ssl2.png)

Although, as cyber security professionals, we have to – by necessity – focus mostly on unpleasant trends (such as those related to rising numbers of zero-day vulnerabilities discovered each year, or the continuously increasing impacts of attacks), it is good to notice from time to time that "in the background", some things are getting better... Even if the improvements are only small, they do still count in the long run.

-----------

Jan Kopriva

[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)

[Nettles Consulting](https://www.nettles.cz/)