---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-10T21:49:47.228924+00:00'
exported_at: '2026-10-10T21:49:48.556643+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33414
structured_data:
  about: []
  author: ''
  description: 'Why TLP should not replace your internal information classification,
    Author: Jan Kopriva'
  headline: Why TLP should not replace your internal information classification, (Sat,
    Oct 10th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33414
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Why TLP should not replace your internal information classification, (Sat,
  Oct 10th)
updated_at: '2026-10-10T21:49:47.228924+00:00'
url_hash: 62262d39b0ff74ca5fec051937496f61f53077c9
---

The Traffic Light Protocol (TLP)[
[1](https://www.first.org/tlp/)
], which is now in its second incarnation, is a wonderful standard that enables one to easily communicate whether information may be shared further (and if so, how far).

That being said, I've noticed a somewhat unfortunate trend in a number of organizations that try to fit TLP into a niche it was never supposed to occupy by attempting to use its labels as a replacement for traditional internal information classification schemes.

At first glance, this may seem quite reasonable. After all, TLP is a well-known standard, and it defines a simple set of labels for restricting the sharing of information (as you can see in the following table). And since most organizational classification schemes also consist of only a few levels, why not use TLP instead of maintaining a separate set of labels?

[![](https://isc.sans.edu/diaryimages/images/26-10-10-tlpv2.png)](https://isc.sans.edu/diaryimages/images/26-10-10-tlpv2.png)

Unfortunately, there are several reasons why this might not be the best idea.

The first is that TLP was never intended to be used in this way. In fact, the official TLP 2.0 standard explicitly states that “TLP is not a formal classification scheme” and that it was not designed to define information handling or encryption rules. Its purpose is to specify with whom information may be shared, not how it should be protected. While these two aspects are certainly related, they are far from being interchangeable.

An internal information classification scheme may, for example, define requirements for encryption, storage, access control or retention of information with different sensitivity levels. None of these requirements can be inferred from a TLP label alone.

For example, an organization may allow documents classified as "Sensitive" to be sent to customers, but only in encrypted e-mails or on encrypted USB drives. Even if a TLP label permits sharing with the intended recipients, it doesn't say anything about these requirements. To express them using TLP alone, the organization would have to add its own information handling rules to the labels – effectively creating a custom classification scheme.

Also – and perhaps more importantly – the sharing restrictions defined by TLP don't necessarily correspond to what one might expect from similarly named internal classification levels.

Consider, for example, an organization that uses TLP:GREEN to mark documents intended for internal use. According to the actual TLP definition, however, information marked with this label may be shared within a relevant community (which, unless otherwise specified, means the cybersecurity/defense community). If such a document were shared with an external security partner, the recipient might therefore quite legitimately distribute it further, even though this was never the intention of the original organization.

A similar problem may arise with TLP:AMBER, which permits sharing not only within the recipient's organization, but also with its clients on a need-to-know basis when necessary to protect them. And while TLP:AMBER+STRICT removes the latter possibility, neither designation necessarily corresponds to what an organization might consider "Confidential" information. TLP:RED, on the other hand, prohibits any further sharing beyond the original recipients without permission from the source, which would make it rather impractical for many types of internal documents.

A related problem arises when TLP labels are assigned according to how sensitive a document is considered to be, rather than who should be able to receive it. A network diagram might, for example, be marked TLP:RED simply because someone considers it "Highly Confidential", even though several teams or external contractors might need access to it. In such a case, the label would either make legitimate sharing unnecessarily difficult or end up being routinely ignored.

Of course, organizations can define additional restrictions or their own interpretations of these labels. However, doing so effectively means creating a custom classification scheme which only looks like TLP, and which may consequently lead to misunderstandings whenever information is exchanged with anyone who follows the actual standard.

This is not to say that TLP shouldn't be used within organizations. It certainly has its place there, especially when it comes to sharing threat intelligence and other security-related information. Nevertheless, it should complement an internal information classification scheme, rather than replace it.

After all, the main reason for using standardized labels is to make it easier for everyone to understand what they are allowed to do with specific information. And using the same labels to mean different things depending on who reads them seems like a rather good way to achieve the exact opposite...

[1]
&lt;https://www.first.org/tlp/&gt;

-----------

Jan Kopriva

[LinkedIn](https://www.linkedin.com/in/jan-kopriva/)

[Nettles Consulting](https://www.nettles.cz/)