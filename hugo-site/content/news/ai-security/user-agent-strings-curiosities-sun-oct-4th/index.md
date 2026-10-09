---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:29:52.721054+00:00'
exported_at: '2026-10-07T04:29:54.558906+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33394
structured_data:
  about: []
  author: ''
  description: 'User Agent Strings Curiosities, Author: Didier Stevens'
  headline: User Agent Strings Curiosities, (Sun, Oct 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33394
  publisher:
    logo: /favicon.ico
    name: GTCode
title: User Agent Strings Curiosities, (Sun, Oct 4th)
updated_at: '2026-10-07T04:29:52.721054+00:00'
url_hash: c45b408e21ef0dad2ddf0abfb66d0e56216d3652
---

Sometimes I have to smile, or my interest is triggered, when I review new User Agent Strings in the honeypot logs.

Like when I see an "authorized" scan:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-45-29.png)

Or when I'm owned for the umpteenth time:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-43-50.png)

I regularly see URLs or email addresses for when you want to know more, or get in touch, with the persons behind a scanner:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-50-13.png)

(around the end of this list, you'll see the Belarus email address we
[wrote about recently](https://isc.sans.edu/diary/HELPMEESCAPEFROMBELARUSPLEASE+Guest+Diary/33130)
)

Many variants of masscan:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-54-10.png)

Even a KGB variant.

As you can guess, "scan" is a popular word to include in your UAS:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_16-57-47.png)

And some wordplays are thrown in:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-03-28.png)

And they do not shy away from discrediting:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-01-45.png)

Sometime complete lists of User Agent Strings are used: the scanner will select a new UAS for each request. They don't always sanitize these list, as you can see with these weird "User Agent Strings":

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-07-45.png)

These lines actually appear in
[this repository of User Agent Strings](https://gist.github.com/alexanderldavis/93e5c8dc779dfb27b835ec98bebca0cd)
, to separate them in groups:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-12-18.png)

And because of a lack of quality control, these separator lines also get used as UAS in a request.

Of course, there are also attempts to exploit the parsing of a User Agent String. Shellshock may be more than 10 years old, I still see it in User Agent Strings:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-15-14.png)

And sometimes I think: "Huh, are they scanning for this too?". Like the last one:

![](https://isc.sans.edu/diaryimages/images/2026-10-03_17-21-26.png)

Scanning for servers that stream GPS correction data via the
[NTRIP protocol](https://en.wikipedia.org/wiki/Networked_Transport_of_RTCM_via_Internet_Protocol)
(a NTRIP header was also included in this request).

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)