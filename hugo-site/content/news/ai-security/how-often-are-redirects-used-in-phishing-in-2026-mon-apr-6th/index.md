---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T04:15:13.809059+00:00'
exported_at: '2026-04-08T04:15:18.520917+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32870
structured_data:
  about: []
  author: ''
  description: 'How often are redirects used in phishing in 2026?, Author: Jan Kopriva'
  headline: How often are redirects used in phishing in 2026&#x3f;, (Mon, Apr 6th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32870
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How often are redirects used in phishing in 2026&#x3f;, (Mon, Apr 6th)
updated_at: '2026-04-08T04:15:13.809059+00:00'
url_hash: b92c4e054ce82c671a07df41975dae3b10697a0d
---

In one of his recent diaries, Johannes discussed how open redirects are actively being sought out by threat actors[
[1](https://isc.sans.edu/diary/Open+Redirects+A+Forgotten+Vulnerability/32742)
], which made me wonder about how commonly these mechanisms are actually misused…

Although open redirect is not generally considered a high-impact vulnerability on its own, it can have multiple negative implications. Johannes already covered one in connection with OAuth flows, but another important (mis)use case for them is phishing.

The reason is quite straightforward – links pointing to legitimate domains (such as google.com) included in phishing messages may appear benign to recipients and can also evade simpler e-mail scanners and other detection mechanisms.

Even though open redirect has not been listed in OWASP Top 10 for quite some time, it is clear that attackers have never stopped looking for it or using it. If I look at traffic on almost any one of my own domains, hardly a month goes by when I don’t see attempts to identify potentially vulnerable endpoints, such as:

```
/out.php?link=https://domain.tld/
```

While these attempts are not particularly frequent, they are generally consistent.

We also continue to see open redirect used in phishing campaigns. Last year, I wrote about a campaign using a “half-open” (i.e., easily abusable) redirect mechanism on Google [
[2](https://isc.sans.edu/diary/Another+day+another+phishing+campaign+abusing+googlecom+open+redirects/31950)
], and similar cases still seem to appear regularly.

But how regular are they, actually?

To find out, I reviewed phishing e-mails collected through my own filters and spam traps, as well as samples sent to us here at the ISC (either by our professional colleagues, or by threat actors themselves), over the first quarter of this year. Although the total sample only consisted of slightly more than 350 individual messages (and is therefore far from statistically representative), it still provided quite interesting results.

Redirect-based phishing accounted for a little over 21 % of all analyzed messages sent out over the first 3 months of 2026 – specifically for 32 % in January, 18 % in February and 16.5 % in March.

It should be noted that if a message contained multiple malicious links and at least one of them used a redirect, the entire message was counted exclusively as a redirect sample, and that not all redirect cases were classic "open redirects". In fact, the abused redirect mechanisms varied widely.

Some behaved similarly to the aforementioned Google-style “half-open” redirects (see details below), while others were fully open. In some cases, the redirectors were part of tracking or advertising systems, while in others, they were implemented as logout endpoints or similar mechanisms. It should be noted that URL shorteners were also counted as redirectors (although these were not particularly common).

As we mentioned, the Google-style redirects are not fully open. They do require a specific valid token to work, however, since these tokens are typically reusable, have a very long lifetime, and are not tied to any specific context (such as IP address or session), they can be – and are – readily reused in phishing campaigns.

An example of such a phishing message and subsequent redirection can be seen in the following images. Though, to avoid focusing solely on Google, it should be mentioned that similar redirect mechanisms on other platforms (e.g., Bing) are also being abused in the same way.

[![](https://isc.sans.edu/diaryimages/images/26-04-06-mail.png)](https://isc.sans.edu/diaryimages/images/26-04-06-mail.png)

[![](https://isc.sans.edu/diaryimages/images/26-04-06-redirect.png)](https://isc.sans.edu/diaryimages/images/26-04-06-redirect.png)

As we can see, although open redirect is commonly considered more of a nuisance issue than an actual high-risk vulnerability these days, it doesn’t keep malicious actors from misusing it quite heavily… Which means we shouldn’t just ignore it.

At the very least, it is worth ensuring that our own applications do not expose endpoints that can be misused in this way. And where any redirection functionality is strictly required, it should be monitored for abuse and restricted as necessary.

[1]
<https://isc.sans.edu/diary/Open+Redirects+A+Forgotten+Vulnerability/32742>

[2]
<https://isc.sans.edu/diary/Another+day+another+phishing+campaign+abusing+googlecom+open+redirects/31950>

-----------

Jan Kopriva

[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)

[Nettles Consulting](https://www.nettles.cz/)