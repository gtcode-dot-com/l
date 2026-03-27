---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-27T00:15:16.683365+00:00'
exported_at: '2026-03-27T00:15:19.762766+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32810
structured_data:
  about: []
  author: ''
  description: 'Interesting Message Stored in Cowrie Logs, Author: Guy Bruneau'
  headline: Interesting Message Stored in Cowrie Logs, (Wed, Mar 18th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32810
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Interesting Message Stored in Cowrie Logs, (Wed, Mar 18th)
updated_at: '2026-03-27T00:15:16.683365+00:00'
url_hash: db3959ca2031ad34be6ab78b008cef50ea4e08d6
---

This activity was found and reported by BACS student Adam Thorman as part of one of his assignments which I posted his final paper [
[1](https://isc.sans.edu/diary/32788)
] last week. This activity appeared to only have occurred on the 19 Feb 2026 where at least 2 sensors detected on the same day by DShield sensor in the cowrie logs an echo command that included: "
MAGIC\_PAYLOAD\_KILLER\_HERE\_OR\_LEAVE\_EMPTY\_iranbot\_was\_here
". My DShield sensor captured activity from source IP
[64.89.161.198](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-02-19&ip=64.89.161.198)
between 30 Jan - 22 Feb 2026 that included portscans, a successful login via Telnet (TCP/23) and web access that included all the activity listed below captured by the DShield sensor (cowrie, webhoneypot & iptables logs).

![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic1.png)

Bot successfully logged in twice into the sensor on the 15 and 19 Feb 2026 via Telnet. The bot activity of interest was a shell script uploaded on the 19 Feb 2026 in an attempt to exploit IoTs and 64-bit Linux systems.

Using Adam [1] grep command, I found in my logs the same script uploaded to the DShield sensor:

ubuntu@vps-711a413c:~/downloads$ sudo cat
f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715

**Script Content**

![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic2.png)

**Cowrie Log**

![](https://isc.sans.edu/diaryimages/images/64_89_161_198_pic3.png)

**Indicators**

64.89.161.198

188.214.30.5

http[:]//188.214.30.5/r.sh

f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715

If you detected the same type of activity, we also appreciate feedback and suggestions about what tool might be used to perform these scans. Please use our
[contact](https://isc.sans.edu/contact.html)
page to provide feedback.

[1] https://isc.sans.edu/diary/32788

[2] https://www.virustotal.com/gui/file/f1c0e109640d154246d27ff05074365740e994f142ef9846634bec7b18e3b715/detection

[3] https://www.linkedin.com/in/adam-thorman/

[4] https://isc.sans.edu/ipinfo/64.89.161.198

[5] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-02-19&ip=64.89.161.198

[6] https://isc.sans.edu/ipinfo/188.214.30.5

[7] https://www.shodan.io/host/64.89.161.198

[8] https://www.virustotal.com/gui/ip-address/64.89.161.198/detection

[9] https://github.com/DShield-ISC/dshield

[10] https://github.com/bruneaug/DShield-SIEM/tree/main

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu