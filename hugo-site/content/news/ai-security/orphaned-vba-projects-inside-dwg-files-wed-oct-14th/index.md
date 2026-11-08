---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-08T05:23:07.629137+00:00'
exported_at: '2026-11-08T05:23:08.635508+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33420
structured_data:
  about: []
  author: ''
  description: 'Orphaned VBA Projects Inside DWG Files, Author: Didier Stevens'
  headline: Orphaned VBA Projects Inside DWG Files, (Wed, Oct 14th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33420
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Orphaned VBA Projects Inside DWG Files, (Wed, Oct 14th)
updated_at: '2026-11-08T05:23:07.629137+00:00'
url_hash: 6a1ad96a7af92813bcafe9e6dc429cdceb8104ea
---

Years ago I wrote
[diary](https://isc.sans.edu/diary/Malicious+DWG+Files/25612)
[entries](https://isc.sans.edu/diary/Extracting+VBA+Macros+From+DWG+Files/25634)
about VBA code stored inside AutoCAD drawing files (.dwg).

In a nutshell: the VBA code is stored inside an OLE file, that is embedded inside the DWG file. You can do a brute-force search for the embedded OLE file, or you can follow a pointer inside the header of the DWG file.

I wrote a small Python script (
[autocad.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/autocad.py)
) for this second case. It looks at a 32-bit pointer at position 0x24 inside the DWG file. This points to a 16-byte long header, followed by the embedded file. This 16-byte long header contains the length of the embedded file. You use the script together with my tool
[cut-bytes.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/cut-bytes.py)
, like this:

&gt; cut-bytes.py -S autocad.py -P AutoCAD : 461ed52aeb75384133a8238b2eb481ae5d505d4961effa622673d65a889c8218.vir.zip | oledump.py

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-49-50.png)

This command carves the DWG file (inside the ZIP file) and extracts the embedded OLE file, and pipes it into
[oledump.py](https://github.com/DidierStevens/DidierStevensSuite/blob/master/oledump.py)
for analysis.

When the pointer is zero, there is no embedded OLE file, and cut-bytes.py returns nothing.

Recently, I discovered 2 DWG files that are an exception: their pointer to the embedded OLE file is zero, but if you do a brute-force search, you will find an embedded OLE file with a VBA project.

For example
[this DWG file](https://www.virustotal.com/gui/file/09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8)
.

Its pointer to the embedded VBA project is zero:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-57-23.png)

But it contains an embedded OLE file:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_17-58-05.png)

And right in front of the embedded OLE file, there is the 16-byte long header that contains the lenght of the embedded file.

Using the AutoCAD script to extract the file gives nothing:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_18-02-46.png)

But oledump.py can find the embedded OLE file and analyze it:

![](https://isc.sans.edu/diaryimages/images/2026-10-13_18-04-26.png)

So while using oledump.py to analyze DWG files you find a VBA project embedded inside a DWG file, then also verify if it is not orphaned: verify that the pointer at 0x24 is not zero (or use the autocad.py script).

Because when a DWG file contains an orphaned VBA project, the VBA code can not have executed when someone opened the DWG file with AutoCAD. AutoCAD "does not see" orphaned VBA projects.

Notice that a default installation of AutoCAD does not support VBA. VBA for AutoCAD is a
[separate install](https://www.autodesk.com/support/technical/article/caas/tsarticles/ts/3kxk0RyvfWTfSfAIrcmsLQ.html)
.

I don't know how orphaning happens, but I did find an
[AutoLISP command to remove a VBA project from a DWG file](https://forums.autodesk.com/t5/autocad-forum/need-to-remove-old-vba-from-2020-dwg/td-p/11235044)
:

&gt; (dictremove (namedobjdict) "ACAD\_VBA")

Maybe this dictremove command clears the pointer, but does not remove the embedded OLE file.

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)