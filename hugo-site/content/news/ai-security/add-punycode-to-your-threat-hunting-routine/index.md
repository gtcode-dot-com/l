---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-20T10:15:13.452510+00:00'
exported_at: '2026-01-20T10:15:15.681865+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32640
structured_data:
  about: []
  author: ''
  description: 'Add Punycode to your Threat Hunting Routine, Author: Xavier Mertens'
  headline: Add Punycode to your Threat Hunting Routine, (Tue, Jan 20th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32640
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Add Punycode to your Threat Hunting Routine, (Tue, Jan 20th)
updated_at: '2026-01-20T10:15:13.452510+00:00'
url_hash: a007b012b69d05785ab2f67e76f823ed468f04eb
---

IDNs or “International Domain Names” have been with us for a while now (see RFC3490[
[1](https://datatracker.ietf.org/doc/html/rfc3490)
]). They are (ab)used in many attack scenarios because.. it works! Who can immediately spot the difference between:

```
https://youtube.com/
```

And:

```
https://youtube.com/
```

The magic is to replace classic characters by others that look almost the same. In the example above, the letter “o” has been replaced by Greek character “o”.

If they are very efficient for attackers, they remain below the radar in many organizations. To avoid issues when printing unusual characters, Punycode[
[2](https://en.wikipedia.org/wiki/Punycode)
] helps to encode them in plain characters. The example above will be encoded as:

```
xn--yutube-wqf.com
```

This format is based on:

* “xn--“ : the common prefix for all IDNs requests.
* “yutube.com”: The normal ASCII characters
* “wqf” : The Punycode encoded version of the Unicode character

Python can decode them easily:

```
$ python3
Python 3.12.3 (main, Jan  8 2026, 11:30:50) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> domain = "xn--yutube-wqf.com"
>>> decoded = domain.encode("ascii").decode("idna")
>>> print(decoded)
y?utube.com
>>> for c in decoded:
...     print(f"{c} -> {ord(c)}")
...
y -> 121
? -> 1086
u -> 117
t -> 116
u -> 117
b -> 98
e -> 101
. -> 46
c -> 99
o -> 111
m -> 109
>>>
```

You can see the value of “o” is not “usual” (not in the ASCII range). They are plenty of online tools that can (de|en)code Punycode[
[3](https://regery.com/en/domains/tools/punycode-decoder)
].

If not all IDNs are suspicious, they are not very common and deserve some searches in your logs. If you already collect your DNS resolver logs (I hope you do!), it’s easy to search for such domains:

```
$ grep "xn--" queries.log*
queries.log:19-Jan-2026 19:54:38.399 queries: info: client @0x999999999999 192.168.255.13#47099 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log:20-Jan-2026 04:38:25.877 queries: info: client @0x999999999999 192.168.255.13#49850 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 15:22:11.741 queries: info: client @0x9999999999 192.168.255.13#60763 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 17:27:23.127 queries: info: client @0x99999999999 192.168.255.13#44141 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
queries.log.0:18-Jan-2026 22:54:36.841 queries: info: client @0x99999999999 192.168.255.13#35963 (in.xn--b1akcbzf.xn--90amc.xn--p1acf): query: in.xn--b1akcbzf.xn--90amc.xn--p1acf IN A +E(0) (192.168.254.8)
```

The detected Punycode domain is decoded to:

![](https://isc.sans.edu/diaryimages/images/isc-20260120-1.png)

Another good proof that DNS is a goldmine for threat hunting!

[1]
<https://datatracker.ietf.org/doc/html/rfc3490>

[2]
<https://en.wikipedia.org/wiki/Punycode>

[3]
<https://regery.com/en/domains/tools/punycode-decoder>

Xavier Mertens (@xme)

Xameco

Senior ISC Handler - Freelance Cyber Security Consultant

[PGP Key](https://keybase.io/xme/key.asc)