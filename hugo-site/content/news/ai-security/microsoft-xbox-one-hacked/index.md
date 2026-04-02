---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T02:44:59.327330+00:00'
exported_at: '2026-04-02T02:45:02.259253+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/03/microsoft-xbox-hacked.html
structured_data:
  about: []
  author: ''
  description: 'It’s an impressive feat, over a decade after the box was released:
    Since reset glitching wasn’t possible, Gaasedelen thought some voltage glitching
    could do the trick. So, instead of tinkering with the system rest pin(s) the hacker
    targeted the momentary collapse of the CPU voltage rail. This was quite a feat,
    as Ga...'
  headline: Microsoft Xbox One Hacked
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/03/microsoft-xbox-hacked.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft Xbox One Hacked
updated_at: '2026-04-02T02:44:59.327330+00:00'
url_hash: 5771af6c0ca3e62f512b34a7a30b9e0ff0547fc3
---

## Microsoft Xbox One Hacked

It’s an
[impressive feat](https://www.tomshardware.com/video-games/console-gaming/microsofts-unhackable-xbox-one-has-been-hacked-by-bliss-the-2013-console-finally-fell-to-voltage-glitching-allowing-the-loading-of-unsigned-code-at-every-level)
, over a decade after the box was released:

> Since reset glitching wasn’t possible, Gaasedelen thought some
> [voltage glitching](https://www.tomshardware.com/news/yet-another-amd-zen-secure-encrypted-virtualization-vulnerability-demonstrated-by-researchers)
> could do the trick. So, instead of tinkering with the system rest pin(s) the hacker targeted the momentary collapse of the CPU voltage rail. This was quite a feat, as Gaasedelen couldn’t ‘see’ into the Xbox One, so had to develop new hardware introspection tools.
>
> Eventually, the Bliss exploit was formulated, where two precise voltage glitches were made to land in succession. One skipped the loop where the
> [ARM Cortex](https://www.tomshardware.com/news/cortex-76-high-laptop-performance,37158.html)
> memory protection was setup. Then the Memcpy operation was targeted during the header read, allowing him to jump to the attacker-controlled data.
>
> As a hardware attack against the boot ROM in silicon, Gaasedelen says the attack in unpatchable. Thus it is a complete compromise of the console allowing for loading unsigned code at every level, including the Hypervisor and OS. Moreover, Bliss allows access to the
> [security processor](https://www.tomshardware.com/features/intel-amd-most-secure-processors)
> so games, firmware, and so on can be decrypted.

Tags:
[hacking](https://www.schneier.com/tag/hacking/)
,
[Microsoft](https://www.schneier.com/tag/microsoft/)

[Posted on March 23, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/03/microsoft-xbox-hacked.html)
•
[7 Comments](https://www.schneier.com/blog/archives/2026/03/microsoft-xbox-hacked.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.