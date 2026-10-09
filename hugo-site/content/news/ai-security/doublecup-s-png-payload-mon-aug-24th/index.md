---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-22T04:26:05.976698+00:00'
exported_at: '2026-09-22T04:26:08.982438+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33274
structured_data:
  about: []
  author: ''
  description: 'DOUBLECUP''s PNG Payload, Author: Didier Stevens'
  headline: DOUBLECUP's PNG Payload, (Mon, Aug 24th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33274
  publisher:
    logo: /favicon.ico
    name: GTCode
title: DOUBLECUP's PNG Payload, (Mon, Aug 24th)
updated_at: '2026-09-22T04:26:05.976698+00:00'
url_hash: dc0e6dc1e99160343bb6ba7b83c7ffcbcd4977b6
---

New malware that uses steganography always gets my attention, but I was disappointed when I looked at the latest
[DOUBLECUP write-up](https://socradar.io/blog/doublecup-clickfix-loader-devicemanager-rats/)
. It doesn't use real steganography:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-01-09.png)

You can see the PowerShell payload as cleartext: it has not been encoded into the pixels of the image.

It's even not embedded in the image (like inside the metadata), it's just appended after the PNG file:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-01-43.png)

Yet there is a clever little trick:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-02-58.png)

The PowerShell script starts with 0x0D 0x0A, Carriage-Return + Newline: that terminates a line of text in Windows.

That makes that you don't need a custom payload extractor, you can just use the FINDSTR command (Windows' grep) with a unique identifier to extract the script:

![](https://isc.sans.edu/diaryimages/images/2026-08-23_10-03-40.png)

And then pipe it into the PowerShell interpreter.

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)