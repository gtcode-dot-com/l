---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-13T00:21:37.883023+00:00'
exported_at: '2026-11-13T00:21:39.582582+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33434
structured_data:
  about: []
  author: ''
  description: 'Orphaned VBA Projects Inside DWG Files: YARA Rule, Author: Didier
    Stevens'
  headline: 'Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33434
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Orphaned VBA Projects Inside DWG Files: YARA Rule, (Sun, Oct 18th)'
updated_at: '2026-11-13T00:21:37.883023+00:00'
url_hash: d33178f3f117c66b94687fca70636034254188a8
---

Here is the YARA rule I used to detect "
[Orphaned VBA Projects Inside DWG Files](https://dshield.org/diary/Orphaned%20VBA%20Projects%20Inside%20DWG%20Files/33420)
".

&gt; rule
&gt;
&gt; autocad\_orphaned\_vba\_project
&gt;
&gt; {
&gt;
&gt; strings
&gt;
&gt; : $a =
&gt;
&gt; "AC10"
&gt;
&gt; $b = {
&gt;
&gt; D0
&gt;
&gt; CF
&gt;
&gt; 11
&gt;
&gt; E0 A1 B1
&gt;
&gt; 1A
&gt;
&gt; E1
&gt;
&gt; }
&gt;
&gt; $c =
&gt;
&gt; "[Host Extender Info]"
&gt;
&gt;
&gt;
&gt; ascii
&gt;
&gt; condition
&gt;
&gt; : $a
&gt;
&gt; at
&gt;
&gt;
&gt;
&gt; 0
&gt;
&gt;
&gt;
&gt; and
&gt;
&gt;
&gt;
&gt; uint32
&gt;
&gt; (
&gt;
&gt; 0x24
&gt;
&gt; )
&gt;
&gt;
&gt;
&gt; ==
&gt;
&gt;
&gt;
&gt; 0
&gt;
&gt;
&gt;
&gt; and
&gt;
&gt; $b
&gt;
&gt; and
&gt;
&gt; $c
&gt;
&gt; }

A VirusTotal retrohunt with this rule gave me only 2 detections:

[09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8](https://www.virustotal.com/gui/file/09d4607941e458f6dbb6be17825641d863c0b37c185027984e137d8a67e919d8)

[3310c1a9bfe6115e49d8ac372cef5f460850da05138340107e66b958a6b5bca6](https://www.virustotal.com/gui/file/3310c1a9bfe6115e49d8ac372cef5f460850da05138340107e66b958a6b5bca6)

Didier Stevens

Senior handler

[blog.DidierStevens.com](http://blog.DidierStevens.com)