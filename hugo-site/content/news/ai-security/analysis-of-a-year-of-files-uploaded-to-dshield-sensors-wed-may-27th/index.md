---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-04T03:25:22.300356+00:00'
exported_at: '2026-06-04T03:25:23.336200+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33026
structured_data:
  about: []
  author: ''
  description: 'Analysis of a Year of Files Uploaded to DShield Sensors, Author: Guy
    Bruneau'
  headline: Analysis of a Year of Files Uploaded to DShield Sensors, (Wed, May 27th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33026
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Analysis of a Year of Files Uploaded to DShield Sensors, (Wed, May 27th)
updated_at: '2026-06-04T03:25:22.300356+00:00'
url_hash: e231e8ae534188dc3bea3d7a32f6b65618ae3951
---

Using the data collected over the past year and using Kibana these two ES|QL query to summarize the data, this shows the list of the most uploaded threat to two DShield sensors (local and cloud) over the past year. I have sorted the activity by months that shows the evolution of files uploaded to the sensors each month. The activity peaked during the winter months (Dec 2025 - Feb 2026) and started decreasing in March 2026 for each sensor.

![](https://isc.sans.edu/diaryimages/images/malware_1year_activity.png)

**ES|QL Query by Sensor**

FROM cowrie\*

| WHERE threat.indicator.provider == "virustotal"

| WHERE related.hash IS NOT NULL

| WHERE threat.indicator.file.type IS NOT NULL

| WHERE threat.software.name IS NOT NULL

| SORT @timestamp DESC

| STATS Total=COUNT(related.hash) BY FileType=threat.indicator.file.type, agent.name=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

**Past Year of Files Uploaded to Dshield Sensors**

This example displays the activity by file type (8) for a one-year period. The file type uploaded or downloaded to the sensor are ELF, Shell script, Powershell, HTML, Text, unknown, DOS batch file and JavaScript.

![](https://isc.sans.edu/diaryimages/images/malware_1year_activity_by_filetype.png)

**ES|QL Activity by File Type**

FROM cowrie\*

| WHERE threat.indicator.provider == "virustotal"

| WHERE related.hash IS NOT NULL

| WHERE threat.indicator.file.type IS NOT NULL

| WHERE threat.software.name IS NOT NULL

| WHERE  threat.indicator.name IS NOT NULL

| SORT @timestamp DESC

| STATS Total=COUNT(related.hash) BY agent.name, threat.indicator.name=BUCKET(@timestamp, 50, ?\_tstart, ?\_tend)

To monitor the type of files uploaded or downloaded to the sensor, using the cowrie\_vt.sh [
[3](http://https://github.com/bruneaug/DShield-Sensor/blob/main/sensor_scripts/cowrie_vt.sh)
] Python
[Jesse's](https://isc.sans.edu/handler_list.html#jesse-lagrew)
script [
[4](https://raw.githubusercontent.com/jslagrew/cowrieprocessor/main/cowrie_malware_enrichment.py)
], it provides a daily list of hash files that are stored on the sensor and can be monitored within the DShield SIEM [
[2](https://github.com/bruneaug/DShield-SIEM)
].

[1] https://isc.sans.edu/tools/honeypot/

[2] https://github.com/bruneaug/DShield-SIEM

[3] https://github.com/bruneaug/DShield-Sensor/blob/main/sensor\_scripts/cowrie\_vt.sh

[4] https://raw.githubusercontent.com/jslagrew/cowrieprocessor/main/cowrie\_malware\_enrichment.py

-----------

Guy Bruneau
[IPSS Inc.](http://www.ipss.ca/)

[My GitHub Page](https://github.com/bruneaug/)

Twitter:
[GuyBruneau](https://twitter.com/guybruneau)

gbruneau at isc dot sans dot edu