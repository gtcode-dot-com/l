---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-05T12:15:19.292822+00:00'
exported_at: '2026-05-05T12:15:21.550396+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32954
structured_data:
  about: []
  author: ''
  description: 'Cleartext Passwords in MS Edge? In 2026?, Author: Rob VandenBrink'
  headline: Cleartext Passwords in MS Edge&#x3f; In 2026&#x3f;, (Mon, May 4th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32954
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cleartext Passwords in MS Edge&#x3f; In 2026&#x3f;, (Mon, May 4th)
updated_at: '2026-05-05T12:15:19.292822+00:00'
url_hash: b334d4b8cfa117103c863a3613c31457b1b9eda4
---

Yup, that is for real.

For me, this started with a post in X at

hxxps://x.com/intcyberdigest/status/2051406295828250963?s=61 , which highlighted research by

[@L1v1ng0ffTh3L4N](https://x.com/L1v1ng0ffTh3L4N)
that found exactly this issue.  Edge stores all of your browser passwords in clear text, even if you haven't used them in this session, y'know, just in case.

I figured, it couldn't be that easy, right?  But like so many things, yes, yes it was.

To reproduce this

* Open Edge.  Don't browse anywhere, just open it
* Flip out to Task Manager, search for Edge, then expand that task
* Highlight the "browser" sub-task, right click, and choose "Create Memory Dump"

![](https://isc.sans.edu/diaryimages/images/dump_mem_from_process.png)

Navigate to where the DMP file is stored.

If you haven't used
strings
before, you're in for a treat.
Strings
is of course just part of most Linux distros, but you can easily get a copy for Windows as part of MS Sysinternals, at https://learn.microsoft.com/en-us/sysinternals/downloads/strings

Now let's look for passwords!  You could use strings and look for known credentials, just search for a known password and you will certainly find it.  Or you can take advantage of the format of the saved data:

<url of the site><protocol>< ><userid>< >password>

So, searching for "<tld><protocol>", which in most cases is "comhttps" (no spaces) will find most of them, and they'll all be in one nicely formatted group no less.  The command for that will be:

strings -n 8 msedge.DMP | find "comhttps"

looking a bit down in the output (since comhttps does match more stuff in the memory dump than just the credential list), I see:

![](https://isc.sans.edu/diaryimages/images/password_dump.png)

As you can see, Edge isn't  my primary browser, but I do use it a fair bit for Azure work.  And yes, this is a real session, so I cropped/blurred out sensitive accounts and of course passwords.

It really is that easy.

And the ironic thing?  To view these same credentials in the browser, there's a whole security theatre process where Edge wants your biometrics as proof before disclosing even the userid and site names - you know, "for security".  All the while, the whole shot is in clear text, free for the looking ..

Also as noted in the X post, Microsoft classifies this as "intended behaviour".  I'm not sure what manager or lawyer decided that, hopefully it wasn't anyone in their security team.

Anyway, if the intent of this is to get me to use Firefox or Chrome, it's working!!

Have you seen a similar "strong front door / open window" security example in your forensics, please share in the comments (keeping any NDA's etc in mind of course)

===============

Rob VandenBrink

[[email protected]](/cdn-cgi/l/email-protection)