---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:54:24.896947+00:00'
exported_at: '2026-11-15T06:54:27.324003+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33502
structured_data:
  about: []
  author: ''
  description: 'Attackers Searching for SAP Netweaver Webshells, Author: Johannes
    Ullrich'
  headline: Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33502
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Attackers Searching for SAP Netweaver Webshells, (Mon, Nov 9th)
updated_at: '2026-11-15T06:54:24.896947+00:00'
url_hash: 49097f3f34acca1ba88ed389e30819a78667afd0
---

Just saw a new (to me) URL in our honeypot data today:

/irj/servlet\_jsp/irj/root/ant.jsp

This request is part of a larger campaign to exploit SAP NetWeaver or to find already installed webshells.

The exploited vulnerability is "old": CVE-2025-31324. A perfect 10 CVSS score and the simple ability to upload files without authentication. Attackers have been using this vulnerability to upload webshells. Usually, these webshells end up in /irj/servlet\_jsp/irj/root/.

One particular attacker, 82.26.72.21, is hitting the following URLs. Not all of these URLs are SAP NetWeaver-related. Also, check the odd misspelling of "upload.aspx" at the end.

| URL Path |
| --- |
| / |
| /\_layouts/15/start.aspx |
| /\_layouts/15/ToolPane.aspx?DisplayMode=Edit&amp;a=/ToolPane.aspx |
| /amp/upload |
| /ant.aspx |
| /ant.jsp |
| /ant.jsp/ |
| /ant.php |
| /api/upload |
| /api/v1/upload |
| /authenticationendpoint/ant.jsp |
| /commandcenter/ant.jsp |
| /commandcenter/deployWebpackage.do |
| /developmentserver/metadatauploader?CONTENTTYPE=MODEL&amp;CLIENT=1 |
| /en-US/static/app/search/ant.php |
| /fileupload/toolsAny |
| /hosted/amp/upload |
| /images/ant.php |
| /images/pagebuilder/ant.php |
| /index.action |
| /index.php?option=com\_baforms&amp;task=uploader.upload |
| /index.php?option=com\_gridbox&amp;task=uploader.upload |
| /index.php?option=com\_jce&amp;task=plugin.display&amp;plugin=browser |
| /index.php?option=com\_sppagebuilder&amp;task=media.directUpload |
| /irj/servlet\_jsp/irj/root/ant.jsp |
| /m/webadmin/upload |
| /MagicInfo/ant.jsp |
| /MagicInfo/servlet/SWUpdateFileUploader |
| /NmConsole/ant.aspx |
| /NmConsole/Wug/Report/ExportReport |
| /Synchronization |
| /te/upload |
| /upload.apsx |
| /upload.aspx |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|