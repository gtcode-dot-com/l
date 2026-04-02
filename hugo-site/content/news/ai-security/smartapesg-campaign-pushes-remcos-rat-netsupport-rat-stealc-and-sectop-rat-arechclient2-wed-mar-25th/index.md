---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:58:55.674806+00:00'
exported_at: '2026-04-02T04:58:58.474895+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32826
structured_data:
  about: []
  author: ''
  description: 'SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and
    Sectop RAT (ArechClient2), Author: Brad Duncan'
  headline: SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and Sectop
    RAT (ArechClient2), (Wed, Mar 25th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32826
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SmartApeSG campaign pushes Remcos RAT, NetSupport RAT, StealC, and Sectop RAT
  (ArechClient2), (Wed, Mar 25th)
updated_at: '2026-04-02T04:58:55.674806+00:00'
url_hash: 96e958c449cb1df58eb15d4f78287193f8d3122f
---

***Introduction***

This diary provides indicators from the SmartApeSG (ZPHP, HANEYMANEY) campaign I saw on Tuesday, 2026-03-24. SmartApeSG is one of many campaigns that use the
[ClickFix](https://unit42.paloaltonetworks.com/preventing-clickfix-attack-vector/)
technique. This past week, I've seen NetSupport RAT as follow-up malware from Remcos RAT pushed by this campaign. But this time, I also saw indicators for StealC malware and Sectop RAT (ArecheClient2) after NetSupport RAT appeared on my infected lab host.

Not all of the follow-up malware appears shortly after the initial Remcos RAT malware. Here's the timeline for malware from my SmartApeSG activity on Tuesday 2026-03-24:

* 17:11 UTC - Ran ClickFix script from SmartApeSG fake CAPTCHA page
* 17:12 UTC - Remcos RAT post-infection traffic starts
* 17:16 UTC - NetSupport RAT post-infection traffic starts
* 18:18 UTC - StealC post-infection traffic starts
* 19:36 UTC - Sectop RAT post-infection traffic starts

While the NetSupport RAT activity happened approximately 4 minutes after the Remcos RAT activity, the StealC traffic didn't happen until approximately 1 hour after the NetSupport RAT activity started. And the traffic for Sectop RAT happened approximately 1 hour and 18 minutes after the StealC activity started.

***Images from the infection***

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-01a.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-01.png)

*Shown above: Page from a legitimate but compromised website with injected script for the fake CAPTCHA page.*

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-02a.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-02.png)

*Shown above: Fake CAPTCHA page with ClickFix instructions. This image shows the malicious script injected into a user's clipboard.*

[![](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-03d.png)](https://isc.sans.edu/diaryimages/images/2026-03-25-ISC-diary-image-03c.png)

*Shown above: Traffic from the infection filtered in Wireshark.*

***Indicators of Compromise***

Associated domains and IP addresses:

* fresicrto[.]top
  - Domain for server hosting fake CAPTCHA page
* urotypos[.]com
  - Called by ClickFix instructions, this domain is for a server hosting the initial malware
* 95.142.45[.]231:443
  - Remcos RAT C2 server
* 185.163.47[.]220:443
  - NetSupport RAT C2 server
* 89.46.38[.]100:80
  - StealC C2 server
* 195.85.115[.]11:9000
  - Sectop RAT (ArechClient2) C2 server

Example of HTA file retrieved by ClickFix script:

* SHA256 hash:
  [212d8007a7ce374d38949cf54d80133bd69338131670282008940f1995d7a720](https://bazaar.abuse.ch/sample/212d8007a7ce374d38949cf54d80133bd69338131670282008940f1995d7a720/)
* File size: 47,714 bytes
* File type: HTML document text, ASCII text, with very long lines (6272)
* Retrieved from:
  hxxps[:]//urotypos[.]com/cd/temp
* Saved location:
  C:\Users\[username]\AppData\Local\post.hta
* Note: ClickFix script deletes the file after retrieving and running it

Example of ZIP archive for Remcos RAT retrieved by the above HTA file:

ZIP archive containing NetSupport RAT package:

RAR archive for StealC package:

RAR archive for Sectop RAT (ArechClient2) package:

***Final words***

The archive files for Remcos RAT, StealC and Sectop RAT are packages that use legitimate EXE files to side-load malicious DLLs (a technique called DLL side-loading). The NetSupport RAT package is a legitimate tool that's configured to use an attacker-controlled server.

As always, the files, URLs and domains for SmartApeSG activity change on a near-daily basis. And names of the HTA file and ZIP archive for Remcos RAT are different for each infection. The indicators described in this article may no longer be current as you read this. However, this activity confirms that the SmartApeSG campaign can push a variety of malware after an initial infection.

---

Bradley Duncan

brad [at] malware-traffic-analysis.net