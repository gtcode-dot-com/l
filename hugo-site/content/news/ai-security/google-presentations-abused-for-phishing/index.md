---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-30T18:15:12.936185+00:00'
exported_at: '2026-01-30T18:15:15.227514+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32668
structured_data:
  about: []
  author: ''
  description: 'Google Presentations Abused for Phishing, Author: Johannes Ullrich'
  headline: Google Presentations Abused for Phishing, (Fri, Jan 30th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32668
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Google Presentations Abused for Phishing, (Fri, Jan 30th)
updated_at: '2026-01-30T18:15:12.936185+00:00'
url_hash: 5ef8e825c2c6f4564a44b3b1b23037279b43f972
---

Charlie, one of our readers, has forwarded an interesting phishing email. The email was sent to users of the Vivladi Webmail service. While not overly convincing, the email is likely sufficient to trick a non-empty group of users:

![](https://isc.sans.edu/diaryimages/images/vivaldiphish1.png)

The e-mail gets more interesting as the user clicks on the link. The link points to Google Documents and displays a slide show:

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-01-30%20at%2012_31_30%E2%80%AFPM.png)

Usually, Google Docs displays a footer notice that warns viewers about phishing sites and offers a "reporting" link if a page is used for phishing. Bots are missing in this case. At first, I suspected some HTML/JavaScript/CSS tricks, but it turns out that this isn't a bug; it is a feature!

Usually, if a user shares slides, the document opens in an "edit" window. This can be avoided by replacing "edit" with "preview" in the URL, but the footer still makes it obvious that this is a set of slides. To remove the footer, the slides have to be "published," and the resulting link must be shared. When publishing, the slides will auto-advance. But for a one-slide slideshow, this isn't an issue. There is also a setting to delay the advance. Here are some sample links:

[These links point to a simple sample presentation I created, not the phishing version.]

Normal Share:

https://docs.google.com/presentation/d/1Quzd6bbuPlIcTOorlUDzSuJCXiOyqBTSHczo6hnXcac/edit?usp=sharing

Preview Share:

https://docs.google.com/presentation/d/1Quzd6bbuPlIcTOorlUDzSuJCXiOyqBTSHczo6hnXcac/preview?usp=sharing

Publish Share:

https://docs.google.com/presentation/d/e/2PACX-1vRaoBusJAaIoVcNbGsfVyE0OuTP1dS-2Po9lpAN9GGy2EkbZG\_oR9maZDS7cq2xW\_QeiF8he457hq3\_/pub?start=false&loop=false&delayms=30000

The URL parameters in the last link do not start the presentations, nor loop them, and delay the next slide by 30 seconds.

The Vivaldi webmail phishing ended up on a "classic" phishing login form that was created using Square. So far, this form is still visible at


hxxps [:] //vivaldiwebmailaccountsservices[.]weeblysite[.]com

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-01-30%20at%2012_41_24%E2%80%AFPM.png)
???????

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|