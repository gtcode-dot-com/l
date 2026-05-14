---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:16:51.988522+00:00'
exported_at: '2026-05-14T21:16:53.797459+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32974
structured_data:
  about: []
  author: ''
  description: 'Why we use CAPTCHAs, Author: Johannes Ullrich'
  headline: Why we use CAPTCHAs, (Mon, May 11th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32974
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Why we use CAPTCHAs, (Mon, May 11th)
updated_at: '2026-05-14T21:16:51.988522+00:00'
url_hash: e97c69f1cde63d2a6c686f3e53a010e3b5d0256e
---

A few months ago, I implemented Cloudflare's Turnstile CAPTCHA on some pages. The reason for implementing these CAPTCHAs is obvious: Bots make up a large percentage of traffic and affect site performance.

So I figured it was a good time to look back and see how effective these CAPTCHA are. The quick number: Out of about 300 requests, only 1 passed the test. Or 99.7% of requests came from bots. And this is after we have been running this for a few months. Some bots may have stopped scanning the page.

But what about false positives? One false positive I noted from the login page was people clicking "Submit" on the login form before the CAPTCHA test was completed. This was easily fixed with a bit of JavaScript, which enabled the button only after a test was completed.

Some of the top offenders:

* 219.117.237.208. - resolves to 219.117.237.208.static.zoot.jp and appears to be some kind of spider
* 18.229.88.75 - an AWS host, also attempting to download our IP data
* 164.52.120.0/24 - Cloud provider in HK
* 2a03:2880:f806::/48 - Facebook Ireland

So far, I have received only a few complaints about false positives (aside from the now fixed login page issue).

Why I selected "Turnstile" over other CAPTCHA options:

* Cloudflare's turnstile implementation appears to have fewer privacy issues than others, like Google Recaptcha
* They are in my opinion, low impact to the user
* Implementing them on the site wasn't too difficult
* We already use Cloudflare as a CDN.
* They work well enough

CAPTCHA can often be bypassed. The right CAPTCHA solution makes it hard enough for an attacker to bypass that the value of the data they would be getting is not worth the effort.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|