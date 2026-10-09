---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T20:39:57.965735+00:00'
exported_at: '2026-05-14T20:40:00.086443+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html
structured_data:
  about: []
  author: ''
  description: RubyGems halted new registrations after a major attack involving hundreds
    of malicious packages, increasing supply chain risks.
  headline: RubyGems Suspends New Signups After Hundreds of Malicious Packages Are
    Uploaded
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/rubygems-suspends-new-signups-after.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: RubyGems Suspends New Signups After Hundreds of Malicious Packages Are Uploaded
updated_at: '2026-05-14T20:39:57.965735+00:00'
url_hash: 6bced755ddba6291731ab6c82a780d69350faeea
---

**

Ravie Lakshmanan
**

May 12, 2026

Supply Chain Attack / Software Security

**RubyGems**
, the standard package manager for the Ruby programming language, has temporarily paused account sign ups following what has been described as a "major malicious attack."

"We're dealing with a major malicious attack on RubyGems right now," Maciej Mensfeld, senior product manager for software supply chain security at Mend.io,
[said](https://x.com/maciejmensfeld/status/2054164602577940619)
in a post on X. "Signups are paused for the time being. Hundreds of packages involved – mostly targeting us, but some carrying exploits."

Visitors to RubyGems'
[sign up page](https://rubygems.org/sign_up)
are now greeted with the message: "New account registration has been temporarily disabled."

Mend.io, which secures RubyGems, said it intends to release more details once the incident is contained. It's currently not known who is behind the attack.

The development comes as software supply chain attacks targeting open-source ecosystems have been on the rise, with threat actors like
[TeamPCP](https://thehackernews.com/2026/05/mini-shai-hulud-worm-compromises.html)
compromising widely used packages to distribute credential-stealing malware capable of harvesting sensitive data and allowing the attackers to expand their reach.

In a report published Monday, Google
[said](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)
the credentials stolen from affected environments have been monetized through partnerships with ransomware and data theft extortion groups.

### Update

In a follow-up update, Mensfeld
[said](https://x.com/maciejmensfeld/status/2053814200124752198)
more than 120 malicious packages have been pulled from RubyGems, adding that the attack targeted the registry itself. Separately, Ruby Central's Marty Haught
[said](https://x.com/mghaught/status/2054254491034394810)
RubyGems was responding to "a coordinated spam-publishing campaign" limited to newly registered accounts publishing junk packages.

"The malicious spam activity against rubygems.org has stopped," RubyGems
[said](https://status.rubygems.org/incidents/cytf062tkwtt)
in an update shared on May 13, 2026. "The bot accounts responsible have been blocked and removed, and the 500+ malicious packages pushed during the attack have been yanked from the registry."

Account sign-ups are expected to be closed as it coordinates with Fastly to enable web application firewall (WAF) protection and tighten rate limiting on account creation. These actions will take two to three days, it noted, adding that Gem updated after publication to reflect the latest developments.)