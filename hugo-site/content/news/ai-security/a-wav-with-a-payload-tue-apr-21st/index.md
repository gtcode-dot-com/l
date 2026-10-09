---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-21T08:15:14.704900+00:00'
exported_at: '2026-04-21T08:15:17.198482+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32910
structured_data:
  about: []
  author: ''
  description: 'A .WAV With A Payload, Author: Didier Stevens'
  headline: A .WAV With A Payload, (Tue, Apr 21st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32910
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A .WAV With A Payload, (Tue, Apr 21st)
updated_at: '2026-04-21T08:15:14.704900+00:00'
url_hash: 436c873f95338c6d12374ccc7f7285a8d36b787d
---

There have been reports of threat actors using a
[.wav file as a vector for malware](https://www.bleepingcomputer.com/news/security/backdoored-telnyx-pypi-package-pushes-malware-hidden-in-wav-audio/)
.

It's a proper .wav file, but they didn't use staganography. The .wav file will play, but you'll just hear noise:

![](https://isc.sans.edu/diaryimages/images/20260419-100007.png)

That's because the TAs have just replaced the bytes that encode the sound with the BASE64 representation of their payload:

![](https://isc.sans.edu/diaryimages/images/20260419-100220.png)

Thus I don't need a .wav parser to extract the encoded payload, I can just use my
[base64dump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/base64dump.py)
tool:

![](https://isc.sans.edu/diaryimages/images/20260419-100408.png)

The BASE64-decoded payload is an XOR-encoded PE file. So I don't need to make a custom decoder, I can just perform a known-plaintext attack looking for the DOS header with my
[xor-kpa.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/xor-kpa.py)
tool:

![](https://isc.sans.edu/diaryimages/images/20260419-100857.png)

The XOR key was found. Thus we can easily dump the decoded PE file and see the MZ header at position 0x08 and a bit further down the DOS header we used in the known-plaintext-attack:

![](https://isc.sans.edu/diaryimages/images/20260419-102311.png)

And my tool
[pecheck.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/pecheck.py)
can extract an analyse the
[sample](https://www.virustotal.com/gui/file/a0a8857e8a65c05778cf6068ad4c05ec9b6808990ae1427e932d2989754c59a4/detection)
:

![](https://isc.sans.edu/diaryimages/images/20260419-101916.png)

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)