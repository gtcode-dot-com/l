---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T04:42:51.124443+00:00'
exported_at: '2026-10-03T04:42:55.918953+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33344
structured_data:
  about: []
  author: ''
  description: 'Scans Targeting Hospitality Applications, Author: Johannes Ullrich'
  headline: Scans Targeting Hospitality Applications, (Wed, Sep 16th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33344
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scans Targeting Hospitality Applications, (Wed, Sep 16th)
updated_at: '2026-10-03T04:42:51.124443+00:00'
url_hash: 942c41f9fa7ac1edd0b630f2817857500534f6eb
---

Earlier today, I noted an odd request showing up in our "First Seen" report:

```
GET /PIAF-HMS/ HTTP/1.1
Host: [redacted]
User-Agent: Farez-Sorter/1.0
Accept-Encoding: gzip
```

This request is linked to a rather old application, a "PBX in a Flash Hospitality Management System" [1]. The last update, the addition of a license file, happened 10 years ago, and I would consider the project abandoned. However, I also noted a new vulnerability reported a couple of months ago: An SQL injection issue. A quick scan of the code shows many more, and the author does not believe in input validation at all. I am also not seeing any authentication and access control, but I have a suspicion that this code may never have been used, and may be intended more as a lab/experiment to test some Asterix PBX integration. With that, I was about to move on.

However, looking at the somewhat odd user agent, I found a few other similar requests:

&gt; `/admin/
&gt;
&gt; /admin/config.php
&gt;
&gt; /ucp/
&gt;
&gt; /hms/
&gt;
&gt; /hotel/`

The scans started yesterday and have been continuing today. The only source IP for the scans is
[94.102.49.125](/ipinfo.html?ip=94.102.49.125)
. This IP address is associated with IP Volume ( AS202425), which is often considered a bulletproof hoster. Hotels are often "soft targets" for attackers seeking to steal valuable personal data. In some cases, they have been compromised to launch MitM attacks against guests. The focus on PBX systems is interesting, and maybe there are some tricks that could be played on guests if an attacker can appear to call from "inside" the property.

Please let me know if you have some insight as to what is going on here.

[1] https://github.com/claudiopizzillo/PIAF-HMS

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|