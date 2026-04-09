---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-09T02:15:15.253812+00:00'
exported_at: '2026-04-09T02:15:17.794742+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32866
structured_data:
  about: []
  author: ''
  description: 'Number Usage in Passwords: Take Two, Author: Jesse La Grew'
  headline: 'Number Usage in Passwords: Take Two, (Thu, Apr 9th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32866
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Number Usage in Passwords: Take Two, (Thu, Apr 9th)'
updated_at: '2026-04-09T02:15:15.253812+00:00'
url_hash: 264cf3a9b19ed3fb3a533c0d923f2288b0826b44
---

In a previous diary [1], we looked to see how numbers were used within passwords submitted to honeypots. One of the items of interest was how dates, and more specifically years, were represented within the data and how that changed over time. It is often seen that years and seasons are used in passwords, especially when password change requirements include frequenty password changes. Some examples we might see today:

* `Spring2026!`
* `Spring26`
* `April2026`
* `April@2026`
* `AprilShowers26`
* `Bloom2026`
* `Easter2026!`
* `Passover2026`

How is this data represented within passwords submitted to honeypots? Are bots updated to incorporate new year values at certain intervals?

**Date range of data:**
4//21/2024 - 3/29/2026

**Number of unique passwords:**
496,562

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure1.png)

Figure 1: Top 10 contiguous numbers used in passwords submitted to sample of DShield honeypots.**

When looking at contiguous numbers used within passwords, we see similar data from a couple of years ago. The top two contigious numbers seen within passwords submitted to honeypots were "123" and "1". However, rather than many of the other high volume contiguous numbers representing a subset of "123456", the passwords included other numbers such as "100000", "19", "69", "200".

It turns out that this activity was related to a potential DDoS or stress testing of and endpoing using ICMP. "100000" was the desired number of packets sent to the destionation host and the other numbers represented each octet of the destination IP.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure2.PNG)

Figure 2: Passwords submitted to honeypots that were supposed to be commands run once access was gained to the honeypot.**

The source IP
[147.45.47.117](/ipinfo.html?ip=147.45.47.117)
was attempting these commands between 11/18/2024 and 11/24/2024. The activity was seen on honeypots distributed in GCP, Digital Ocean, Azure and a residential honeypot. This was not seen on samples from an AWS honeypot.

Other activities from this source were seen between 11/14/2024 and 12/1/2024. Most of the sessions from this host are repeated attempts to download a script from
[45.125.66.215](/ipinfo.html?ip=45.125.66.215)
and install it as a service.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure3_v2.PNG)

Figure 3: Repeated attempts to setup and install a service using a downloaded script from
[45.125.66.215](/ipinfo.html?ip=45.125.66.215)
.**

Unfortunately, the file was not downloaded by any of the honeypots, so there was not a file to reference.

Okay, back to passwords and number usage. Let's take a look at number frequency use in the passwords submitted to honeypots.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure3.PNG)

Figure 4: Individual number frequency used within passwords submitted to honeypots.**

Similar to the previous review, generally the lower the number, the more frequently it's used in a password. The most common digits used are "0", "1", "2" and "3". What about 4-digit numbers?

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure4.PNG)

Figure 5: Top 10 numbers used within passwords submitted to honeypots only containing 4 digits.**

This was also similar to the previous review. "1234" is still the most common and usually the most prevelant year seen is the prior year. We do see "2026" in this list, but since there's only a few months of data, it hasn't quite hit the volume of the previous year. One of the curiousities from this data is when these years get introduced. For example, when does "2026" start getting used within a password submitted to a honeypot?

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure6.PNG)

Figure 6: Heatmap of years used within passwords and when they showed up in honeypot data.**

Overall, it appears that 4-digit numbers representing years show up more prevalently in the year in which that data was submitted to a honeypot. From Figure 6, we see that "2025" shows up most frequently in data captured from honeypot logs in 2025. This also appears similar for "2024". An item that was surprising when looking at the data, is that there were already some hits for "2027".

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure7.PNG)

Figure 7: Passwords containing year and their volume over time, showing a small number of submissions containing "2027".**

| Year contained in password | First seen in samples | Example password |
| --- | --- | --- |
| 2024 | 11/1/2023   (found in expanded dataset) | `sysadmin2024` |
| 2025 | 4/5/2024 | `@dm1n2025` |
| 2026 | 5/6/2024 | `@2026` |
| 2027 | 8/11/2024 | `2027` |

**Figure 8: Passwords containing recent years, when they first appeared in the dataset along with some example passwords.**

Most of the passwords containing what could be a year are introduced the year before. However, that may vary widely from the beginning to the end of the previous year. There are also many other "future" years seen within the dataset.

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure8.PNG)

**Figure 9: Heatmap of future years used within passwords from data collection, showing "2023" was heavily used in the data collected near the end of 2024.**

**Figure 10: Passwords containing future years, when they first appeared in the dataset along with some example passwords.**

In the cases where a future year is being used, the passwords likely have nothing to do with that year. However, there are a few examples that could be dates:

* `19820313`
  : 03/13/1982
* `19820320`
  : 03/20/1982
* `19820402`
  : 04/02/1982

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure9.PNG)

**Figure 11: In most cases, the years are used at the end of the password, rather than in the middle or beginning of the password.**

From the examples, focusing on a 4-digit number that's added to the end of a password could give us more representative examples of a number used intentionally to represent a year. Passwords containing "2027" for example, have a very different distribution on where they appear in the passwords. We see a much higher liklihood of "2027" being in a variety of locations, rather than just at the end of the password.

There are also many numbers that could represent specific dates.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure12.png)

Figure 12: Examples of numbers that could represent dates using diffrent formats.**

Depending on the numbers, it can be difficult to know whether numbers representing days or months come first, but can be clearly determined when a day is greater than 12 since a month cannot have a value greater than 12. Some of these dates are found in passwords that have more content, but in most cases the date alone is used as the password. Some examples:

* `w@terloo19051954`
* `01011958`
* `25031959`
* `01011960`
* `17101971`
* `20101971`
* `24101971`
* `www.txwscx.comsritgyxf2sxy19831122zx`
* `19831123`
* `20261017`
* `20261109`
* `20261111`

For the passwords identified as possibly having dates in a YYYYMMDD, MMDDYYYY or DDMMYYYY format (16,713), 88.9% (14,582) of them were just 8-digit numbers. It was interesting to see years from 1958 to 2026. Could this be another habit of using dates of birth or just the current day in passwords?

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure13.png)

**Figure 13: Top 10 years seen in passwords if numbers represent specific dates in YYYYMMDD, MMDDYYYY or DDMMYYYY formats.**

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure14.png)

**Figure 14: Possible distrubution of months seen in passwords if numbers represent specific dates in YYYYMMDD, MMDDYYYY or DDMMYYYY formats.**

![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure18.png)

**Figure 15: Distribution of years found within the dates identified in passwords. There is a heavy focus on dates in the 1980s.**

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure15(1).png)

Figure 16: Image showing possible "age" distributions based on different from dates seen in passwords from today.**

There is a high distribution of "0" year age dates. One hypothesis is that the current day is used within passwords, assuming someone changed their password that day and they used today's date. Looking at general proximity, there were around 1,000 passwords submitted that included dates close to submission date. This represents about 94% of similar passwords submitted in a proximity of 180 days from the password submission date to a honeypot. If the password submitted to a honeypot contains a date and it's close to the current date, it's probably very close.

**![](https://isc.sans.edu/diaryimages/images/2026-04-09_figure16(1).png)

Figure 17: Distribution of passwords containing dates close to the date of interaction with a honeypot.**

I really enjoyed the heatmaps, but the largest one didn't display well in this diary. It zooms in well [2], so feel free to download it
[here](https://www.dropbox.com/scl/fi/nl995gb6yziostxttxrol/2026-04-09_figure16.png?rlkey=mfu6oteed72ohwhae8ml9y24g&st=192holxm&dl=0)
.

To finish things off, the most and least common passwords containing years from sample honeypot data:

| Capture Year | Password |
| --- | --- |
| 2024 | `ubuntu@2024` |
| 2024 | `postgres@2024` |
| 2024 | `Qwer@2024` |
| 2024 | `Admin@2024` |
| 2024 | `dev@2024` |
| 2025 | `2025` |
| 2025 | `Azerty2025` |
| 2025 | `P@ssw0rd@2025` |
| 2025 | `Itsemoemo2025@Washere2025` |
| 2025 | `Admin@2025` |
| 2026 | `2026` |
| 2026 | `claude2026!` |
| 2026 | `20262026` |
| 2026 | `admin2026` |
| 2026 | `P@ssw0rd2026` |

**Figure 18: Most common passwords containing years from honeypot samples.**

| Capture Year | Password |
| --- | --- |
| 2024 | `bscs@2024` |
| 2024 | `gameserver2024` |
| 2024 | `dell1@2024` |
| 2024 | `Redis@2024` |
| 2024 | `redhat2024` |
| 2025 | `uqkxipImdQ97hzWScUrk20250402` |
| 2025 | `100202500200` |
| 2025 | `01022025` |
| 2025 | `12025988` |
| 2025 | `001002025` |
| 2026 | `test-2026` |
| 2026 | `es!2026` |
| 2026 | `P@ssw0rd2026~` |
| 2026 | `ec2-user@2026` |
| 2026 | `Ubuntu!2026` |

**Figure 19: Least common passwords containing years from honeypot samples.**

Keep years and dates, especially the current year, out of your passwords.

[1]
<https://isc.sans.edu/diary/Number+Usage+in+Passwords/30540>

[2]
<https://www.dropbox.com/scl/fi/nl995gb6yziostxttxrol/2026-04-09_figure16.png?rlkey=mfu6oteed72ohwhae8ml9y24g&st=192holxm&dl=0>

--

Jesse La Grew

Senior Handler