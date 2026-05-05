---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-05T12:15:18.605906+00:00'
exported_at: '2026-05-05T12:15:21.554008+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32956
structured_data:
  about: []
  author: ''
  description: 'SSL.com rotates their root certificate today, Author: Rob VandenBrink'
  headline: SSL.com rotates their root certificate today, (Tue, May 5th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32956
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SSL.com rotates their root certificate today, (Tue, May 5th)
updated_at: '2026-05-05T12:15:18.605906+00:00'
url_hash: 37240a036a6b90040358c9ce55bb76f573768547
---

I just got an email from SSL.com last night, they are rotating  out their root certificate today (May 5,2026).  This is normal, business as usual stuff for a CA, but certificates get used for all kinds of things, and sometimes they aren't used like they should be, so sometimes hiccups happen.

If you are using them for basic cert+website stuff, there's no need to worry.  But if you go past that basic implementation, you should read their note to make sure that this change won't be affecting any of your services.  Even if you don't use ssl.com, it's a good read, as every certificate expires, which means that everyone's root cert rotates out eventually - so forewarned if forearmed and all that ..

In particular (from the email):

* *If you have pinned trust anchors, custom trust stores, or certificate validation logic tied to the 2016 roots, please audit those configurations promptly to avoid disruptions.*
* *Use cross-certificates. If you need backward compatibility with the 2016 root hierarchy during the transition, cross-certificates can bridge the gap.*
* *Migrate to dedicated Client Certificates. These are purpose-built for client authentication and are unaffected by Google Chrome's upcoming server authentication requirements, which impact SSL/TLS certificates with the ClientAuth EKU.*

Their full post is here:

https://www.ssl.com/article/what-ssls-root-migration-means-for-you

===============

Rob VandenBrink

[[email protected]](/cdn-cgi/l/email-protection)