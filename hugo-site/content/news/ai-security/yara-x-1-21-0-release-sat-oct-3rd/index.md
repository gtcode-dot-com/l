---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:29:51.322462+00:00'
exported_at: '2026-10-07T04:29:54.566803+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33392
structured_data:
  about: []
  author: ''
  description: 'YARA-X 1.21.0 Release, Author: Didier Stevens'
  headline: YARA-X 1.21.0 Release, (Sat, Oct 3rd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33392
  publisher:
    logo: /favicon.ico
    name: GTCode
title: YARA-X 1.21.0 Release, (Sat, Oct 3rd)
updated_at: '2026-10-07T04:29:51.322462+00:00'
url_hash: 2b6adb625a29b35c4f5b853d7ec4a44d93f57b40
---

# [YARA-X 1.21.0 Release](/forums/diary/YARAX+1210+Release/33392/)

**Published**
: 2026-10-03.
**Last Updated**
: 2026-10-03 14:40:21 UTC

**by**
[Didier Stevens](/handler_list.html#didier-stevens)
(Version: 1)

[0 comment(s)](/diary/YARAX+1210+Release/33392/#comments)

[YARA-X's 1.21.0](https://github.com/VirusTotal/yara-x/releases/tag/v1.21.0)
release brings 5 improvements and 4 bugfixes.

One improvement is allowing stdin for CLI option --scan-list.

This allows one to generate a list of folders to scan, and pass it via a pipe. Like this example (Windows) to scan all folders with "sample" in their name:

```
dir /s /b /a:d c:\*samples* | yr.exe scan --scan-list - rules.yara
```

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)

Keywords:

[0 comment(s)](/diary/YARAX+1210+Release/33392/#comments)

Click
HERE
to learn more about classes Didier is teaching for SANS

* [previous](/diary/33388)
* [next](/diary/33394)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)