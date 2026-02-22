---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-22T08:15:17.029074+00:00'
exported_at: '2026-02-22T08:15:19.304068+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32734
structured_data:
  about: []
  author: ''
  description: 'Japanese-Language Phishing Emails, Author: Brad Duncan'
  headline: Japanese-Language Phishing Emails, (Sat, Feb 21st)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32734
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Japanese-Language Phishing Emails, (Sat, Feb 21st)
updated_at: '2026-02-22T08:15:17.029074+00:00'
url_hash: 0284f028e954888da62a47e1adaaf704c9454bcf
---

***Introduction***

For at least the past year or so, I've been receiving Japanese-language phishing emails to my blog email addresses at @malware-traffic-analysis.net.  I'm not Japanese, but I suppose my blog's email addresses ended up on a list used by the group sending these emails. They're all easily caught by my spam filters, so they're not especially dangerous in my situation. However, they could be effective for the Japanese-speaking recipients with poor spam filtering.

Despite the different companies impersonated, they all follow a similar pattern for the phishing page URLs and email-sending addresses.

This diary reviews three examples of these phishing emails.

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-01.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-01a.jpg)

*Shown above: The spam folder for my blog's admin email account.*

***Screenshots***

The first screenshot shows an example of a phishing email impersonating the Japanese airline ANA (All Nippon Airways). Both the sending email address and the link for the phishing page use domains with a
.cn
top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-02.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-02a.jpg)

*Shown above: Example of a Japanese phishing email impersonating ANA.*

The second screenshot shows an example of a phishing email impersonating the shipping/logistics company DHL. Like the previous example, both the sending email address and the link for the phishing page use domains with a
.cn
top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-03c.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-03a.jpg)

*Shown above: Example of a Japanese phishing email impersonating DHL.*

Finally, the third screenshot shows an example of a phishing email impersonating the utilities company myTOKYOGAS. Like the previous two examples, both the sending email address and the link for the phishing page use domains with a
.cn
top-level domain (TLD).

[![](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-04.jpg)](https://isc.sans.edu/diaryimages/images/2026-02-21-ISC-diary-image-04a.jpg)

*Shown above: Example of a Japanese phishing email impersonating myTOKYOGAS.*

As noted earlier, these emails have different themes, but they have similar patterns that indicate these were sent from the same group.

***Indicators of the Activity***

Example 1:

* Received: from
  ncqjw[.]cn
  (unknown [
  150.5.129[.]136
  ])
* Date: Thu, 19 Feb 2026 21:52:36 +0800
* From:
  "ANA" <member.llbyzmf@ncqjw[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page:
  hxxps[:]//branchiish.aayjlc[.]cn/amcmembr\_Loginam/

Example 2:

* Received: from
  obpwnrl[.]cn
  (unknown [
  101.47.78[.]193
  ])
* Date: Fri, 20 Feb 2026 12:29:35 +0800
* From:
  "DHL" <dmail.elthr@obpwnrl[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page:
  hxxps[:]//decideosity.ykdyrkye[.]cn/portal\_login\_exp/getQuoteTab/

Example 3:

* Received: from
  cwqfvzp[.]cn
  (unknown [
  150.5.130[.]42
  ])
* Date: Fri, 20 Feb 2026 23:50:56 +0800
* From:
  "myTOKYOGAS" <reportogkfgkbye@cwqfvzp[.]cn>
* X-mailer: Foxmail 6, 13, 102, 15 [cn]
* Link for phishing page:
  hxxps[:]//impactish.rexqm[.]cn/mtgalogin/

***Final Words***

The most telling indicator that these emails were sent from the same group is the
X-mailer: Foxmail 6, 13, 102, 15 [cn]
line in the email headers.

I'm not likely to be tricked into giving up information for accounts that I don't have, like for myTOKYOGAS or for DHL.  Other recipients could be tricked by these, though, assuming they make it past a recipient's spam filter.

I'm curious how effective these phishing emails are, because the group behind this activity appears to be casting a wide net that reaches non-Japanese speakers.

If anyone else has received these types of phishing emails, feel free to leave a comment or submit an example via our
[contact page](https://isc.sans.edu/contact.html)
.

Bradley Duncan

brad [at] malware-traffic-analysis.net