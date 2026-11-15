---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:47:11.152447+00:00'
exported_at: '2026-11-15T07:47:12.479435+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33518
structured_data:
  about: []
  author: ''
  description: 'Macfinger ClickFix campaign sends DownTheDRAIN infostealer for macOS,
    Author: Brad Duncan'
  headline: Macfinger ClickFix campaign sends DownTheDRAIN infostealer for macOS,
    (Fri, Nov 13th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33518
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Macfinger ClickFix campaign sends DownTheDRAIN infostealer for macOS, (Fri,
  Nov 13th)
updated_at: '2026-11-15T07:47:11.152447+00:00'
url_hash: 6b2047aad824de08c437f8a2680812a6733f3eb4
---

***Introduction***

In this diary, I've given a nickname to the macOS infostealer we've been seeing from the Macfinger ClickFix campaign. Based on
[the analysis of an example](https://www.huntress.com/blog/mac-crypto-draining-malware)
posted on the Huntress Cybersecurity Blog, I'm calling this macOS malware
***DownTheDRAIN infostealer***
.

This diary reviews an example of DownTheDRAIN infostealer distributed through the Macfinger ClickFix campaign on Wednesday, 2026-11-11.

Of note, my mac mini running macOS 26.7.3 blocked and moved the malware to Trash before it could exfiltrate any sensitive data.

[![](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-01a.png)

*Shown above: DownTheDRAIN infostealer blocked and moved to Trash.*

***Background***

I first wrote about the Macfinger ClickFix campaign on
[2026-09-22](https://isc.sans.edu/diary/33360)
, and I took a closer look at the malware on
[2026-09-25](https://isc.sans.edu/diary/33368)
. It didn't match the profile of any macOS infostealers I usually run across. Since I couldn't find any unique characteristics in my analysis, I waited for someone to name it.

I didn't see that anyone had named this infostealer yet, but the Huntress analysis of a sample provided a somewhat unique aspect that could be used for a nickname.

***The DRAIN function***

The
[Huntress analysis](https://www.huntress.com/blog/mac-crypto-draining-malware)
from one of the samples revealed a
DRAIN
function that "
*...identifies various cryptocurrency wallet addresses and can redirect the contents to a wallet controlled by the threat actor.*
" For more information on this function and the associated code, read the full
[August 2026 post by Andrew Brandt](https://www.huntress.com/blog/mac-crypto-draining-malware)
.

***Images***

[![](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-02.png)](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-02a.png)

*Shown above: Fake CAPTCHA page from the Macfinger ClickFix campaign.*

[![](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-03.png)](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-03a.png)

*Shown above: Fake CAPTCHA page showing the ClickFix instructions.*

[![](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-04.png)](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-04a.png)

*Shown above: ClickFix text pasted into a Terminal window.*

[![](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-05.png)](https://isc.sans.edu/diaryimages/images/2026-11-13-ISC-diary-image-05a.png)

*Shown above: Traffic from the infection filtered in Wireshark.*

***Indicators***

Macfinger domain for the fake CAPTCHA page:

Infection traffic for DownTheDRAIN infostealer:

* hxxp[:]//45.150.32[.]130/37339606cba4522a?force=1
* hxxp[:]//45.150.32[.]130/4be1066a49e75?force=1
* hxxp[:]//171.22.131[.]24:8133/api/t
  &lt;-- HTTP POST request, generated 4 times before the malware was blocked

Files from the infection:

SHA-256 hash:
[58e503cc2e6aacc6bdba54f40a7edebf7a5362bef0a9039769baaba8c472c4db](https://www.virustotal.com/gui/file/58e503cc2e6aacc6bdba54f40a7edebf7a5362bef0a9039769baaba8c472c4db)

* File size: 5,011 bytes
* File type: Bourne-Again shell script text executable, ASCII text, with very long lines
* File location:
  hxxp[:]//45.150.32[.]130/37339606cba4522a?force=1
* File description: Retrieved by command in ClickFix text, this shell script installs DownTheDRAIN infostealer

SHA-256 hash:
[8b5026d841aa93758ec3cb55c276f84d3ec1cf459810e0d9aa5624e2776f2fcd](https://www.virustotal.com/gui/file/8b5026d841aa93758ec3cb55c276f84d3ec1cf459810e0d9aa5624e2776f2fcd)

* File size: 35,143,984 bytes
* File type: Mach-O 64-bit executable arm64
* File location:
  hxxp[:]//45.150.32[.]130/4be1066a49e75?force=1
* File description: DownTheDRAIN infostealer binary retrieved by the above shell script

SHA-256 hash:
[c34cc30cb1cff5c47d77e62a3ba63e9a183989ec1ccdf7929beb1bcae0d41f23](https://www.virustotal.com/gui/file/c34cc30cb1cff5c47d77e62a3ba63e9a183989ec1ccdf7929beb1bcae0d41f23)

* File size: 34,957,760 bytes
* File type: Mach-O 64-bit executable arm64
* File location:
  $HOME/Library/Caches/com.apple.update
* File description: DownTheDRAIN infostealer saved to the infected host, then blocked and moved to Trash by macOS

--

Bradley Duncan

brad [at] malware-traffic-analysis.net