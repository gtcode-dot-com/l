---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T04:30:34.081405+00:00'
exported_at: '2026-06-23T04:30:36.790457+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33090
structured_data:
  about: []
  author: ''
  description: 'eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, Author:
    Xavier Mertens'
  headline: eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun
    19th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33090
  publisher:
    logo: /favicon.ico
    name: GTCode
title: eBanking Phishing Delivered Through IPv4-Mapped IPv6 Address, (Fri, Jun 19th)
updated_at: '2026-06-23T04:30:34.081405+00:00'
url_hash: 6864c9b0e75d6b598801371f9a88247ec2fa2fe6
---

I detected an interesting phishing email this morning. It targets a major Belgian bank:

![](https://isc.sans.edu/diaryimages/images/isc-20260618-1.png)

The phishing in itself is a classic one, not relevant but the malicious link is interesting:

```
hxxp://[::ffff:5511:74be]/kWC5PHA1
```

The technique used by the attacker is to bypass simple security controls trying to extract domain names and IP addresses via simple regular expressions. The notation “[…]” tells the URL parser that what's inside is a literal IPv6 address. But it’s not a real IPv6 address. What’s the magic?

The started “::” in the address means that it can be expanded to this address:

```
0000:0000:0000:0000:0000:ffff:5511:74be
```

The trick is the fifth group (::ffff:) means that we are facing a IPv4-mapped IPv6 address. This is defined in RFC 4291[
[1](https://www.rfc-editor.org/info/rfc4291/)
]:

![](https://isc.sans.edu/diaryimages/images/isc-20260618-2.png)

In the URL above, the two trailing 16-bit hex groups “5511” and “74be” are just the four IPv4 octets written in hex.

| Hex | Dec |
| --- | --- |
| 0x55 | 85 |
| 0x11 | 17 |
| 0x74 | 116 |
| 0xBE | 190 |

The real URL is therefore:

```
hxxp://85[.]17[.]116[.]190/kWC5PHA1
```

Another good news from the attacker’s point of view, there is no DNS record!

When visited, this URL redirects to another link where the real phishing kit is hosted:

```
hxxps://3439-aanmelden[.]verificatie[.]qzz[.]io/mon-belfius
```

[1]
&lt;https://www.rfc-editor.org/info/rfc4291/&gt;

**Xavier Mertens (@xme)**

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://raw.githubusercontent.com/xme/pgp/refs/heads/main/public.key)