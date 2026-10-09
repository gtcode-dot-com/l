---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:41:27.850978+00:00'
exported_at: '2026-10-07T04:41:31.025659+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33396
structured_data:
  about: []
  author: ''
  description: 'TTY Logs and the Data it Captures, Author: Guy Bruneau'
  headline: TTY Logs and the Data it Captures, (Sun, Oct 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33396
  publisher:
    logo: /favicon.ico
    name: GTCode
title: TTY Logs and the Data it Captures, (Sun, Oct 4th)
updated_at: '2026-10-07T04:41:27.850978+00:00'
url_hash: 028b11ee27594c147f938ed9d360f6219f82c218
---

For an experiment, I created a script [
[1](https://github.com/bruneaug/DShield-Sensor/blob/main/sensor_scripts/daily_tty.sh)
] that parses and send the TTY logs collected from actors or bots activity that run various commands after they successfully login the DShield sensor. Those TTY logs are sent daily at the end of each day to the DShield SIEM [
[2](https://github.com/bruneaug/DShield-SIEM)
] to be correlated with all the data.

The following
[ES|QL](https://www.elastic.co/docs/reference/query-languages/esql)
query provides a summary of all contab commands matching a TTYLog hash performed by different actors while logged in the sensor over a 90 day period.

**TTYLogs Correlation**

FROM cowrie\*

| WHERE transaction.id == "f904275333aeac48d7df6cf53fe5fb9212c7d132a7d37253d2ab9321ba2690d8"

| WHERE event.hash IS NOT NULL

| KEEP transaction.id, event.hash

| STATS Total=COUNT(event.hash) BY event.hash, transaction.id

| SORT Total DESC

This transaction ID captured 5 similar crontab commands that are translated from its hash equivalent into this list executed by more than 3130 different actors (IPs):

![](https://isc.sans.edu/diaryimages/images/TTYLogs_decoded.png)

**TTYLogs Sources**

transaction.id: f904275333aeac48d7df6cf53fe5fb9212c7d132a7d37253d2ab9321ba2690d8 over a 90 day period

![](https://isc.sans.edu/diaryimages/images/transaction_ID_90days.png)

Other example of Event Hash decoded and sent to DShield SIEM for analysis

![](https://isc.sans.edu/diaryimages/images/Example_Even_Hash.png)

**Top 10 Indicators**

IP                      ASN

102.88.137.80        29465

42.96.20.16            131423

182.253.221.210    38482

46.188.119.26         8334

159.223.97.218       14061

185.158.22.150       210022

193.233.48.169       207713

209.99.190.200       402253

45.64.74.51              55933

202.152.148.27        23951

[1] https://github.com/bruneaug/DShield-Sensor/blob/main/sensor\_scripts/daily\_tty.sh

[2] https://github.com/bruneaug/DShield-SIEM

[3] https://www.elastic.co/docs/reference/query-languages/esql

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu