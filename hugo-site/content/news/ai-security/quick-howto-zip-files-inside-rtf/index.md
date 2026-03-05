---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-05T22:15:16.553277+00:00'
exported_at: '2026-03-05T22:15:20.713448+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32696
structured_data:
  about: []
  author: ''
  description: 'Quick Howto: ZIP Files Inside RTF, Author: Didier Stevens'
  headline: 'Quick Howto: ZIP Files Inside RTF, (Mon, Mar 2nd)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32696
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Quick Howto: ZIP Files Inside RTF, (Mon, Mar 2nd)'
updated_at: '2026-03-05T22:15:16.553277+00:00'
url_hash: 8ab2372ff0452e9db7c0451e60ff96caab6a16f3
---

In diary entry "
[Quick Howto: Extract URLs from RTF files](https://isc.sans.edu/diary/Quick%20Howto%3A%20Extract%20URLs%20from%20RTF%20files/32692)
" I mentioned ZIP files.

There are OLE objects inside this RTF file:

![](https://isc.sans.edu/diaryimages/images/20260209-124939.png)

![](https://isc.sans.edu/diaryimages/images/20260209-124956.png)

![](https://isc.sans.edu/diaryimages/images/20260209-125102.png)

They can be analyzed with
[oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py)
like this:

![](https://isc.sans.edu/diaryimages/images/20260209-125403.png)

Options --storages and -E %CLSID% are used to show the abused CLSID.

![](https://isc.sans.edu/diaryimages/images/20260209-125518.png)

Stream CONTENTS contains the URL:

![](https://isc.sans.edu/diaryimages/images/20260209-125609.png)

We extracted this URL with the method described in my previous diary entry "
[Quick Howto: Extract URLs from RTF files](https://isc.sans.edu/diary/Quick%20Howto%3A%20Extract%20URLs%20from%20RTF%20files/32692)
".

But this OLE object contains a .docx file.

![](https://isc.sans.edu/diaryimages/images/20260209-125740.png)

![](https://isc.sans.edu/diaryimages/images/20260209-125928.png)

A .docx file is a ZIP container, and thus the URLs it contains are inside compressed files, and will not be extracted with the technique I explained.

But this file can be looked into with
[zipdump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/zipdump.py)
:

![](https://isc.sans.edu/diaryimages/images/20260209-130005.png)

It is possible to search for ZIP files embedded inside RTF files: 50 4B 03 04 -> hex sequence of magic number header for file record in ZIP file.

![](https://isc.sans.edu/diaryimages/images/20260209-130139.png)

Search for all embedded ZIP files:

![](https://isc.sans.edu/diaryimages/images/20260209-130412.png)

Extract URLs:

![](https://isc.sans.edu/diaryimages/images/20260209-130600.png)

![](https://isc.sans.edu/diaryimages/images/20260209-130636.png)

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)