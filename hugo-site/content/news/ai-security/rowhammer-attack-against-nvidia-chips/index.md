---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-06T12:15:14.855290+00:00'
exported_at: '2026-05-06T12:15:17.503748+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html
structured_data:
  about: []
  author: ''
  description: 'A new rowhammer attack gives complete control of NVIDIA CPUs. On Thursday,
    two research teams, working independently of each other, demonstrated attacks
    against two cards from Nvidia’s Ampere generation that take GPU rowhammering into
    new—­and potentially much more consequential—­territory: GDDR bitflips that give
    a...'
  headline: Rowhammer Attack Against NVIDIA Chips
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Rowhammer Attack Against NVIDIA Chips
updated_at: '2026-05-06T12:15:14.855290+00:00'
url_hash: 3224c4324fcedf0351315a2d2b62940d61863447
---

## Rowhammer Attack Against NVIDIA Chips

A new
[rowhammer](https://en.wikipedia.org/wiki/Row_hammer)
attack gives
[complete control](https://arstechnica.com/security/2026/04/new-rowhammer-attacks-give-complete-control-of-machines-running-nvidia-gpus/)
of NVIDIA CPUs.

> On Thursday, two research teams, working independently of each other, demonstrated attacks against two cards from Nvidia’s Ampere generation that take GPU rowhammering into new—­and potentially much more consequential—­territory: GDDR bitflips that give adversaries full control of CPU memory, resulting in full system compromise of the host machine. For the attack to work,
> [IOMMU](https://en.wikipedia.org/wiki/Input-output_memory_management_unit)
> memory management must be disabled, as is the default in BIOS settings.
>
> “Our work shows that Rowhammer, which is well-studied on CPUs, is a serious threat on GPUs as well,” said Andrew Kwong, co-author of one of the papers. “
> [GDDRHammer: Greatly Disturbing DRAM Rows­Cross-Component Rowhammer Attacks from Modern GPUs](https://gddr.fail/files/gddr.pdf)
> .” “With our work, we… show how an attacker can induce bit flips on the GPU to gain arbitrary read/write access to all of the CPU’s memory, resulting in complete compromise of the machine.”
>
> Update Friday, April 3: On Friday, researchers unveiled a third Rowhammer attack that also demonstrates Rowhammer attacks on the RTX A6000 that achieves privilege escalation to a root shell. Unlike the previous two, the researchers said, it works even when IOMMU is enabled.

The second paper is
[GeForge: Hammering GDDR Memory to Forge GPU Page Tables for Fun and Profit](https://gddr.fail/files/GeForge.pdf)
:

> …does largely the same thing, except that instead of exploiting the last-level page table, as GDDRHammer does, it manipulates the last-level page directory. It was able to induce 1,171 bitflips against the RTX 3060 and 202 bitflips against the RTX 6000.
>
> GeForge, too, uses novel hammering patterns and memory massaging to corrupt GPU page table mappings in GDDR6 memory to acquire read and write access to the GPU memory space. From there, it acquires the same privileges over host CPU memory. The GeForge proof-of-concept exploit against the RTX 3060 concludes by opening a root shell window that allows the attacker to issue commands that run unfettered privileges on the host machine. The researchers said that both GDDRHammer and GeForge could do the same thing against the RTC 6000.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)
,
[hacking](https://www.schneier.com/tag/hacking/)
,
[hardware](https://www.schneier.com/tag/hardware/)

[Posted on May 6, 2026 at 6:36 AM](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html)
•
[0 Comments](https://www.schneier.com/blog/archives/2026/05/rowhammer-attack-against-nvidia-chips.html#respond)