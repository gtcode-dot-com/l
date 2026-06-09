---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T04:29:09.868536+00:00'
exported_at: '2026-06-09T04:29:13.906303+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33044
structured_data:
  about: []
  author: ''
  description: 'Continuing Scans for swagger.json, Author: Johannes Ullrich'
  headline: Continuing Scans for swagger.json, (Wed, Jun 3rd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33044
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Continuing Scans for swagger.json, (Wed, Jun 3rd)
updated_at: '2026-06-09T04:29:09.868536+00:00'
url_hash: 0d192925454263f19e292f1bb5cd1dc54502bbd1
---

Enterprise applications often still use complex standards like SOAP for web services. The big advantage of SOAP is its tight and extensive standards, which enable interoperability across an enterprise governed by web services. The disadvantage of SOAP: First, while it is de facto usually used over HTTP, it does not leverage HTTP, leading to unnecessary complexity. Secondly, kids don't RTFM, and developers these days tend not to appreciate the art of careful system design; they rather throw code at an IDE to see what sticks, if they don't vibe code it anyway.

So the answer to all of the calls for a simpler standard is the non-standard REST. REST is more a "living standard" defined by commonly used libraries that happen to be popular right now. One of these standards is Swagger, or OpenAPI [1]. A very popular part of Swagger is "swagger.json", a file that defines how to use an API. Some people here may remember "WSDL"s, or good old ".h" files in C/C++. Same idea, but now with more JSON.

From a web application security perspective, swagger.json is like a directory listing for an API. It is not that they are inherently evil or insecure. They are often necessary to allow developers to connect to an API efficiently. But on the other hand, they are also a great roadmap for attackers. So it's no surprise that attackers are looking for them. Not only do they provide a list of API features, but metadata in the description will usually identify the underlying application. It is a great way to find vulnerable applications.

Here are some of the top URLs attackers are scanning recently:

| URL | First Seen | Last Seen | # of Requests |
| --- | --- | --- | --- |
| /swagger.json | 2020-12-28 | 2026-06-03 | 32,499 |
| /api/v2/swagger.json | 2021-01-03 | 2026-06-02 | 14,536 |
| /swagger/v1/swagger.json | 2020-12-28 | 2026-06-03 | 13,791 |
| /api/swagger.json | 2020-12-28 | 2026-06-03 | 11,100 |
| /api-docs/swagger.json | 2020-12-28 | 2026-06-03 | 8,693 |
| /v1/swagger.json | 2021-01-03 | 2026-06-02 | 7,482 |
| /apidocs/swagger.json | 2021-01-03 | 2026-04-26 | 6,517 |
| /api/v1/swagger.json | 2021-03-03 | 2026-06-02 | 6,495 |
| /v2/swagger.json | 2021-08-07 | 2026-06-03 | 1,026 |
| /api/api-docs/swagger.json | 2020-12-28 | 2026-05-12 | 945 |

And some that started showing up more recently:

| URL | First Seen | Last Seen | Number of Requests |
| --- | --- | --- | --- |
| /%2Fswagger.json | 2026-04-03 | 2026-04-22 | 20 |
| /swagger/v2/api-docs/service/swagger.json | 2026-02-27 | 2026-05-24 | 17 |
| /swagger/v3/api-docs/service/swagger.json | 2026-02-27 | 2026-05-24 | 17 |
| /26-166/api-docs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /73/api/apidocs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /hsd1/api/swagger-ui/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /69/api/api-docs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /166/api-docs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /c/api-docs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |
| /26-166/api/api-docs/swagger.json | 2026-01-21 | 2026-04-18 | 2 |

The number of requests is continuously high, but there are spikes and slow times:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-06-03%20at%209_30_47%E2%80%AFAM.png)

But the continuing interest shows that attackers see value here.

What's the lesson? Should you stop using swagger.json? Probably not. Your developers need it. On the other hand, you should be scanning for swagger.json files preemptively in your environment to identify inappropriately published swagger.json files. My intro remarks about REST, while obviously an attempt to finally get someone to read these posts, also point out that with REST, some important design decisions are left up to you, and with lots of freedom comes lots of possibilities to mess things up.

Any comments on good tools to do so? (yes, more engagement farming. But maybe it will cause me to fix the comment system for this site.

[1] https://swagger.io/specification/

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|