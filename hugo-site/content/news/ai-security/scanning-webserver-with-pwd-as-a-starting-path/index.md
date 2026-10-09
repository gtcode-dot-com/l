---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-26T02:15:14.413092+00:00'
exported_at: '2026-01-26T02:15:16.718449+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32654
structured_data:
  about: []
  author: ''
  description: 'Scanning Webserver with /$(pwd)/ as a Starting Path, Author: Guy Bruneau'
  headline: Scanning Webserver with /&#x24;(pwd)/ as a Starting Path, (Sun, Jan 25th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32654
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Scanning Webserver with /&#x24;(pwd)/ as a Starting Path, (Sun, Jan 25th)
updated_at: '2026-01-26T02:15:14.413092+00:00'
url_hash: fa94614a71f5bbc2de8b50bf0ac89b229d607c51
---

Based on the sensors reporting to ISC, this activity started on the 13 Jan 2026. My own sensor started seeing the first scan on the 21 Jan 2026 with limited probes. So far, this activity has been limited to a few scans based on the reports available in ISC [
[5](https://isc.sans.edu/weblogs/urlhistory.html?url=LyQocHdkKS8uCg==)
] (
select Match Partial URL and Draw
):

![](https://isc.sans.edu/diaryimages/images/isc_pwd_activity.png)

This is a sample list of the directories actors are scanning for using the following patterns:

/$(pwd)/.env.staging

/$(pwd)/.env.development

/$(pwd)/.env.production

/$(pwd)/.env.local

/$(pwd)/.env

$(pwd)/terraform.tfstate

/$(pwd)/docker-compose.yml

/$(pwd)/netlify.toml

This
[Gephi](https://gephi.org/)
graph shows the relationship of each probed URL by the two IP addresses:

![](https://isc.sans.edu/diaryimages/images/pwd_scanning_activity.png)

**Kibana ES|QL Query**

FROM cowrie\*

| WHERE event.reference == "no match"

| KEEP related.ip,http.request.body.content

| WHERE http.request.body.content IS NOT NULL

| WHERE http.request.body.content RLIKE ".\*\\/\\$\\(pwd\\).\*"

| STATS COUNT(http.request.body.content) BY related.ip, http.request.body.content

**Indicators**

By selecting one of these two indicators, it shows their scanning activity for the
/$(pwd)/
pattern in the ISC web logs.

[185.177.72.52](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-21&ip=185.177.72.52)

[185.177.72.23](https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-25&ip=185.177.72.23)

We also appreciate feedback and suggestions about what tool is used to perform these scans. Please use our
[contact](https://isc.sans.edu/contact.html)
page to provide feedback.

[1] https://www.elastic.co/guide/en/elasticsearch/reference/8.19/esql-using.html

[2] https://gephi.org/

[3] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-21&ip=185.177.72.52

[4] https://isc.sans.edu/weblogs/sourcedetails.html?date=2026-01-25&ip=185.177.72.23

[5] https://isc.sans.edu/weblogs/urlhistory.html?url=LyQocHdkKS8uCg==

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu