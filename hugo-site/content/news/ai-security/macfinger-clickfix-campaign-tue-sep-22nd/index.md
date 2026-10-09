---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T23:42:05.752549+00:00'
exported_at: '2026-10-04T23:42:08.732897+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33360
structured_data:
  about: []
  author: ''
  description: 'Macfinger ClickFix campaign, Author: Brad Duncan'
  headline: Macfinger ClickFix campaign, (Tue, Sep 22nd)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33360
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Macfinger ClickFix campaign, (Tue, Sep 22nd)
updated_at: '2026-10-04T23:42:05.752549+00:00'
url_hash: 15e725d5ca47d121fc2af4994fdbcfb5a39fc959
---

***Introduction***

I've found several legitimate websites with injected script for a campaign using the
[ClickFix social engineering technique](https://www.microsoft.com/en-us/security/blog/2025/08/21/think-before-you-clickfix-analyzing-the-clickfix-social-engineering-technique/)
. This particular ClickFix campaign
[was documented earlier this month](https://ransom-isac.org/blog/macos-clickfix-amos-campaign/)
on the Ransom-ISAC Blog, but it doesn't appear to have a nickname yet. Since this campaign is targeting macOS environments through a fingerprinting process, I'm calling it the "Macfinger ClickFix" campaign. No, this is not related to the MacFinger utility from decades ago. Instead, think of the movie
[Goldfinger](https://en.wikipedia.org/wiki/Goldfinger_(film))
, but with macOS malware and the internet instead of James Bond and Miss Galore.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-01.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-01.png)

*Shown above: An image I created to represent the Macfinger ClickFix campaign.*

Today's diary presents indicators from the Macfinger ClickFix campaign that I saw on Tuesday, 2026-09-22.

***Images From the Infection***

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-02a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-02.png)

*Shown above: First part of the Macfinger injected script in a page from a legitimate website.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-03a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-03.png)

*Shown above: Second part of the Macfinger injected script in a page from a legitimate website.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-04a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-04.png)

*Shown above: Fake bot protection page caused by the injected Macfinger script.*

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-05a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-05.png)

*Shown above: ClickFix instructions from fake verification pop-up caused by the injected Macfinger script.*

While displaying the fake bot protection page with the verification instructions, the Macfinger domain receives frequent POST requests from the victim host. These report information on the user and track the user actions. Here's an example of a POST request through HTTPS traffic after the user has clicked on the page. In this case, the user abandoned the page without following the instructions.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-06a.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-06.png)

*Shown above: POST request over HTTPS to the Macfinger domain reporting the user information.*

I had tested one of the Macfinger-infected sites on Monday, 2026-09-21 which had the same post-infection traffic that I saw the next day on Tuesday, 2026-09-22. The image below shows an example of the infection traffic, with the malware files retrieved from
45.150.33[.]128
and the post-infection C2 traffic on
95.163.153[.]80
over TCP port 8133.

[![](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-07b.png)](https://isc.sans.edu/diaryimages/images/2026-09-23-ISC-diary-image-07.png)

*Shown above: Traffic from an infection filtered in Wireshark.*

***Indicators of Compromise***

The following are indicators from Tuesday, 2026-09-22.

Traffic to the Macfinger domain:

* hxxps[:]//velvet-otter-glagceis[.]life/t.js?site=4f0529f47320472732961318d7d0dfd1
* hxxps[:]//velvet-otter-glagceis[.]life/t.4b1009ff6c3f.js
* hxxps[:]//velvet-otter-glagceis[.]life/ext-b.4f9db6afd06a.js
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect
* hxxps[:]//velvet-otter-glagceis[.]life/collect

ClickFix text from the Macfinger domain, saved to a text file:

SHA-256 hash:
[6606a5f18184b224a56c9cb658fa26f7fce45099da548a30a8db2c5f2c70377c](https://www.virustotal.com/gui/file/6606a5f18184b224a56c9cb658fa26f7fce45099da548a30a8db2c5f2c70377c/)

Initial download:

SHA-256 hash:
[9d87b41c2b29ccbeac851b98f1a7dce4ab4781fec0cbc55fa6f93a6299a3d564](https://www.virustotal.com/gui/file/9d87b41c2b29ccbeac851b98f1a7dce4ab4781fec0cbc55fa6f93a6299a3d564/)

* File size: 4,674 bytes
* File type: Bourne-Again shell script text executable, ASCII text, with very long lines
* File location:
  hxxp[:]//45.150.33[.]128/92961f75b259df2?force=1

Follow-up malware from the above shell script:

SHA-256 hash:
[b68cdb1b46502fbce67ce3f8110682936d06afd2116af096e30abd4c8376b6dc](https://www.virustotal.com/gui/file/b68cdb1b46502fbce67ce3f8110682936d06afd2116af096e30abd4c8376b6dc)

* File size: 33,285,040 bytes
* File type: Mach-O 64-bit executable arm64
* File location:
  hxxp[:]//45.150.33[.]128/d4c8083a7d97?force=1

SHA-256 hash:
[1a3765e8cb0055ec31693b8f82ce9744106dee08368259661600b072c6805af4](https://www.virustotal.com/gui/file/1a3765e8cb0055ec31693b8f82ce9744106dee08368259661600b072c6805af4)

* File size: 34,118,904 bytes
* File type: Mach-O 64-bit executable x86\_64
* File location:
  hxxp[:]//45.150.33[.]128/2286de55f9afd?force=1

Post-infection Traffic:

* 2026-09-21 23:12:58 UTC - hxxp[:]//45.150.33[.]128 - GET /92961f75b259df2?force=1
* 2026-09-21 23:12:59 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:12:59 UTC - hxxp[:]//45.150.33[.]128 - GET /d4c8083a7d97?force=1
* 2026-09-21 23:13:04 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:05 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:05 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:08 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:08 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:11 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:14 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:15 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:20 UTC - ipinfo[.]io
  - HTTPS traffic
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - GET /api/shell/agent
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:21 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:22 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:22 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:23 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:24 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:26 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:30 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:30 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:30 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:30 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/credentials
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* 2026-09-21 23:13:31 UTC - hxxp[:]//95.163.153[.]80:8133 - POST /api/t
* And so on...

***Final Words***

The
[Ransom-ISAC article on this activity](https://ransom-isac.org/blog/macos-clickfix-amos-campaign/)
calls the final malware a variant of Atomic macOS (AMOS) Stealer. The indictors I found here don't fully align with the
[AMOS Stealer activity I've previously reported](https://isc.sans.edu/diary/33208)
from a different (non-ClickFix) campaign, so this is a different variant than the AMOS Stealer I've looked into.

For mitigation and protection against Macfinger and other ClickFix campaigns, see
[guidance from the Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/08/05/macos-clickfix-campaign-learned-hide/#mitigation-and-protection-guidance)
.

Macfinger ClickFix seems like a fairly widespread campaign, but I haven't found much about it because 1) it seems relatively new and 2) it's only targeting macOS hosts.

Bradley Duncan

brad [at] malware-traffic-analysis.net