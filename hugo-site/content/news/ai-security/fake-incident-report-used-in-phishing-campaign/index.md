---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-02T02:38:53.631316+00:00'
exported_at: '2026-03-02T02:38:54.832251+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32722
structured_data:
  about: []
  author: ''
  description: 'Fake Incident Report Used in Phishing Campaign, Author: Xavier Mertens'
  headline: Fake Incident Report Used in Phishing Campaign, (Tue, Feb 17th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32722
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake Incident Report Used in Phishing Campaign, (Tue, Feb 17th)
updated_at: '2026-03-02T02:38:53.631316+00:00'
url_hash: cbad33acdab8b4d591a903d52fc449cc7ce34940
---

This morning, I received an interesting phishing email. I’ve a “love & hate” relation with such emails because I always have the impression to lose time when reviewing them but sometimes it’s a win because you spot interesting “TTPs” (“tools, techniques &  procedures”). Maybe one day, I'll try to automate this process!

Today's email targets Metamask[
[1](https://metamask.io)
] users. It’s a popular software crypto wallet available as a browser extension and mobile app. The mail asks the victim to enable 2FA:

![](https://isc.sans.edu/diaryimages/images/isc-20260217-1.png)

The link points to an AWS server: hxxps://access-authority-2fa7abff0e[.]s3.us-east-1[.]amazonaws[.]com/index.html

But it you look carefully at the screenshots, you see that there is a file attached to the message: “Security\_Reports.pdf”. It contains a fake security incident report about an unusual login activity:

![](https://isc.sans.edu/diaryimages/images/isc-20260217-2.png)

The goal is simple: To make the victim scary and ready to “increase” his/her security by enabled 2FA.

I had a look at the PDF content. It’s not malicious. Interesting, it has been generated through ReportLab[
[2](http://www.reportlab.com)
], an online service that allows you to create nice PDF documents!

```
6 0 obj
<<
/Author (\(anonymous\)) /CreationDate (D:20260211234209+00'00') /Creator (\(unspecified\)) /Keywords () /ModDate (D:20260211234209+00'00') /Producer (ReportLab PDF Library - www.reportlab.com)
  /Subject (\(unspecified\)) /Title (\(anonymous\)) /Trapped /False
>>
endobj
```

They also provide a Python library to create documents:

```
pip install reportlab
```

The PDF file is the SHA256 hash 2486253ddc186e9f4a061670765ad0730c8945164a3fc83d7b22963950d6dcd1.

Besides the idea to use a fake incident report, this campaign remains at a low quality level because the "From" is not spoofed, the PDF is not "branded" with at least the victim's email. If you can automate the creation of a PDF file, why not customize it?

[1]
<https://metamask.io>

???????[2]
<http://www.reportlab.com>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)