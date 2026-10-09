---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-15T02:15:17.533926+00:00'
exported_at: '2026-04-15T02:15:19.806311+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32896
structured_data:
  about: []
  author: ''
  description: 'Scanning for AI Models, Author: Guy Bruneau'
  headline: Scanning for AI Models, (Tue, Apr 14th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32896
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Scanning for AI Models, (Tue, Apr 14th)
updated_at: '2026-04-15T02:15:17.533926+00:00'
url_hash: 8bdd68201d4866b5d3c8db20464f85406c686fec
---

Starting March 10, 2026, my DShield sensor started getting probe for various AI models such as claude, openclaw, huggingface, etc. Reviewing the data already reported by other DShield sensors to ISC, the DShield database shows reporting of these probes started that day and has been active ever since.

Based on what we currently have reported, it appears the only source scanning for these models is IP
81.168.83.103
. However, my sensor has been actively scanned by this source since January 29, 2026 and is still ongoing today. Beside the AI probe, it has been scanning various ports that are often associated with web content.

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic1.png)

Reviewing the scanning activity from this host, it appears this source is the only IP we see reported to DShield performing this activity.

**ES|QL Query**
[
[1](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-functions-operators.html)
]

Using this ES|QL query in Kibana discover, it lists all the URL the actor is looking for. I recorded 52 queries between March 10 to April 13, 2026 where April 3rd, 2026 received the most activity.

FROM cowrie\*

| WHERE event.reference == "no match"

| WHERE http.request.body.content IS NOT NULL

| KEEP @timestamp, http.request.body.content

| WHERE http.request.body.content LIKE "\*openclaw\*" OR http.request.body.content LIKE "\*claude\*" OR  http.request.body.content LIKE "\*huggingface\*" OR  http.request.body.content LIKE "\*openai\*"  OR  http.request.body.content LIKE "\*clawdbot\*"


| SORT @timestamp DESC

| STATS Total=COUNT(http.request.body.content) BY AI\_Scan\_Activity=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic2.png)

This graph shows the start of activity searching for
clawbot/moltbot
first reported March 10, 2026 ever since then.

![](https://isc.sans.edu/diaryimages/images/81_168_83_103_pic3.png)

**Indicators**

81.168.83.103 (AS 20860)

/.openclaw/workspace/db.sqlite

/.openclaw/workspace/chroma.db

/.openclaw/secrets.json

/.clawdbot/moltbot.json

/.claude/settings.json

/.claude/.credentials.json

/.cache/huggingface/token

/openai/env.json

/openai/credentials.json

[1] https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-functions-operators.html

[
[2](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jYWNoZS9odWdnaW5nZmFjZS90b2tlbg==)
] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jYWNoZS9odWdnaW5nZmFjZS90b2tlbg== (/.cache/huggingface/token)

[
[3](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jbGF3ZGJvdC9tb2x0Ym90Lmpzb24=)
] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5jbGF3ZGJvdC9tb2x0Ym90Lmpzb24= (/.clawdbot/moltbot.json)

[
[4](https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5vcGVuY2xhdy9zZWNyZXRzLmpzb24=)
] https://isc.sans.edu/weblogs/urlhistory.html?url=Ly5vcGVuY2xhdy9zZWNyZXRzLmpzb24= (/.openclaw/secrets.json)

[
[5](https://www.ox.security/blog/one-step-away-from-a-massive-data-breach-what-we-found-inside-moltbot/)
] https://www.ox.security/blog/one-step-away-from-a-massive-data-breach-what-we-found-inside-moltbot/

[
[6](http://https://www.virustotal.com/gui/ip-address/81.168.83.103)
] https://www.virustotal.com/gui/ip-address/81.168.83.103

[
[7](https://www.shodan.io/host/81.168.83.103)
] https://www.shodan.io/host/81.168.83.103 (Linux system)

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu