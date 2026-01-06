---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-04T12:15:14.307840+00:00'
exported_at: '2026-01-04T12:15:16.486049+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32594
structured_data:
  about: []
  author: ''
  description: 'Cryptocurrency Scam Emails and Web Pages As We Enter 2026, Author:
    Brad Duncan'
  headline: Cryptocurrency Scam Emails and Web Pages As We Enter 2026, (Sun, Jan 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32594
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Cryptocurrency Scam Emails and Web Pages As We Enter 2026, (Sun, Jan 4th)
updated_at: '2026-01-04T12:15:14.307840+00:00'
url_hash: 9f4f0d763ac63bb56f8e513ff8043dc2c677eaa0
---

***Introduction***

In October 2025, a work colleague documented
[a cryptocurrency scam using a fake chatbot](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-10-30-IOCs-for-cryptocurrency-scams-using-fake-chatbots.txt)
. After investigating this, I was able to receive messages from the campaign, and these emails have continued to land in my honeypot account since then. This diary documents the cryptocurrency scam campaign as it continues in 2026.

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-01.jpg)

*Shown above: My honeypot email inbox with several emails from this cryptocurrency scam campaign.*

***Details***

This campaign promises cash payouts on cryptocurrency that potential victims unknowingly have.

This campaign primarily abuses the minimalist publishing platform
telegra[.]ph
, which anyone can use to publish a simple web page very quickly. Many of these emails have minimal messaging and contain links to these
telegra[.]ph
pages.

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-02.jpg)

*Shown above: Example of an email from this campaign with link to a
telegra[.]ph
page.*

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-05.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-05.jpg)

*Shown above: Example of a
telegra[.]ph
page from this campaign.*

This campaign is not limited to abusing
telegra[.]ph
. Many of these emails contain Google Forms pages that lead to the
telegra[.]ph
page.

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-03.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-03.jpg)

*Shown above: Example of a Google Forms email from this campaign.*

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-04.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-04.jpg)

*Shown above: Example of a response from the Google Forms link that leads to a
telegra[.]ph
page for this campaign.*

These
telegra[.]ph
pages generally lead to the same type of cryptocurrency scam, stating you have over $100K in US dollars worth of Bitcoin from an automated Bitcoin mining cloud platform.

[![](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-06.jpg)](https://isc.sans.edu/diaryimages/images/2026-01-04-ISC-diary-image-06.jpg)

*Shown above: Example of a page to begin the cryptocurrency scam.*

In November 2025, I posted
[a video on YouTube](https://www.youtube.com/watch?v=yUV7OkQqSBk&t=7s)
, where I went through the website step-by-step, interacting with the fake chatbot to get to the actual scam. The scam involves paying a fee to convert the supposed Bitcoin to US dollars, which potential victims would send to a wallet controlled by the criminals.

***Final Words***

Many free services are easy to abuse for these types of campaigns. While these emails may seem obviously fake, they continue to be cost-effective for criminals to send, and criminals can easily abuse other services to host everything needed for this scam.

Bradley Duncan

brad [at] malware-traffic-analysis.net