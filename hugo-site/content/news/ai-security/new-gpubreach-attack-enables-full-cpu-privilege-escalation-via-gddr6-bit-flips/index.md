---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-07T23:53:01.621904+00:00'
exported_at: '2026-04-07T23:53:04.623391+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html
structured_data:
  about: []
  author: ''
  description: GPUBreach achieves full CPU privilege escalation via GDDR6 RowHammer
    in July 2025 research, threatening cloud AI systems.
  headline: New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/new-gpubreach-attack-enables-full-cpu.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New GPUBreach Attack Enables Full CPU Privilege Escalation via GDDR6 Bit-Flips
updated_at: '2026-04-07T23:53:01.621904+00:00'
url_hash: b19aa856e1b38f3db804a881ad3d41f3c2f2fb67
---

New academic research has identified multiple RowHammer attacks against high-performance graphics processing units (GPUs) that could be exploited to escalate privileges and, in some cases, even take full control of a host.

The efforts have been codenamed
**[GPUBreach](https://gpubreach.ca/)**
,
**[GDDRHammer](https://gddr.fail/)**
[, and](https://gddr.fail/)
**[GeForge](https://gddr.fail/)**
.

GPUBreach goes a step further than
[GPUHammer](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html)
, demonstrating for the first time that RowHammer bit-flips in GPU memory can induce much more than data corruption and enable privilege escalation, and lead to a full system compromise.

"By corrupting GPU page tables via GDDR6 bit-flips, an unprivileged process can gain arbitrary GPU memory read/write, and then chain that into full CPU privilege escalation — spawning a root shell — by exploiting memory-safety bugs in the NVIDIA driver," Gururaj Saileshwar, one of the authors of the study and Assistant Professor at the University of Toronto,
[said](https://www.linkedin.com/posts/gururaj-saileshwar-080a4526_gpubreach-activity-7445871096840712193-FSM5/)
in a post on LinkedIn.

What makes GPUBreach notable is that it works even without having to disable the input–output memory management unit (
[IOMMU](https://link.springer.com/article/10.1186/s13173-017-0066-7)
), a
[crucial hardware component](https://thehackernews.com/2025/12/new-uefi-flaw-enables-early-boot-dma.html)
that ensures memory security by preventing Direct Memory Access (DMA) attacks and isolating each peripheral to its own memory space.

"GPUBreach shows it is not enough: by corrupting trusted driver state within IOMMU-permitted buffers, we trigger kernel-level out-of-bounds writes — bypassing IOMMU protections entirely without needing it disabled," Saileshwar added. "This has serious implications for cloud AI infrastructure, multi-tenant GPU deployments, and HPC environments."

RowHammer is a long-standing Dynamic Random-Access Memory (DRAM) reliability error where repeated accesses (i.e., hammering) to a memory row can cause electrical interference that flips bits (changing 0 to 1m or vice versa) in adjacent rows. This undermines isolation guarantees fundamental to modern operating systems and sandboxes.

DRAM manufacturers have implemented hardware-level mitigations, such as Error-Correcting Code (ECC) and Target Row Refresh (TRR), to counter this line of attack.

However, research published in July 2025 by researchers at the University of Toronto expanded the threat to GPUs.
[GPUHammer](https://thehackernews.com/2025/07/gpuhammer-new-rowhammer-attack-variant.html)
, as it's called, is the first practical RowHammer attack targeting NVIDIA GPUs using GDDR6 memory. It employs techniques like multi-threaded parallel hammering to overcome architectural challenges inherent to GPUs that previously made them immune to bit flips.

The consequence of a successful GPUHammer exploit is a drop in machine learning (ML) model accuracy, which can degrade by up to 80% when running on a GPU.

GPUBreach extends this approach to corrupt GPU page tables with RowHammer and achieve privilege escalation, resulting in arbitrary read/write on GPU memory. More consequentially, the attack has been found to leak secret cryptographic keys from
[NVIDIA cuPQC](https://developer.nvidia.com/cupqc)
, stage model accuracy degradation attacks, and obtain CPU privilege escalation with IOMMU enabled.

"The compromised GPU issues DMA (using the aperture bits in PTEs) into a region of CPU memory that the IOMMU permits (the GPU driver's own buffers)," the researchers said. "By corrupting this trusted driver state, the attack triggers memory-safety bugs in the NVIDIA kernel driver and gains an arbitrary kernel write primitive, which is then used to spawn a root shell."

This disclosure of GPUBreach coincides with two other concurrent works – GDDRHammer and GeForge – that also revolve around GPU page-table corruption via GDDR6 RowHammer and facilitate GPU-side privilege escalation. Just like GPUBreach, both techniques can be used to gain arbitrary read/write access to CPU Memory.

Where GPUBreach stands apart is that it also enables full CPU privilege escalation, making it a more potent attack. GeForge, in particular, requires IOMMU to be disabled for it to work, whereas GDDRHammer modifies the GPU page table entry's aperture field to allow the unprivileged
[CUDA](https://developer.nvidia.com/blog/even-easier-introduction-cuda/)
kernel to read and write all of the host CPU's memory.

"One main difference is that GDDRHammer exploits the last level page table (PT) and GeForge exploits the last level page directory (PD0)," the teams behind the two GPU memory exploits said. "However, both works are able to achieve the same goal of hijacking the GPU page table translation to gain read/write access to the GPU and host memory."

One temporary mitigation to tackle these attacks is to
[enable ECC](https://nvidia.custhelp.com/app/answers/detail/a_id/5671)
on the GPU. That said, it bears noting that RowHammer attacks like
[ECCploit](https://thehackernews.com/2021/04/new-javascript-exploit-can-now-carry.html)
and
[ECC.fail](https://thehackernews.com/2025/09/phoenix-rowhammer-attack-bypasses.html)
have been found to overcome this countermeasure.

"However, if attack patterns induce more than two bit flips (shown feasible on DDR4 and DDR5 systems), existing ECC cannot correct these and may even cause silent data corruption; so ECC is not a foolproof mitigation against GPUBreach," the researchers said. "On desktop or laptop GPUs, where ECC is currently unavailable, there are no known mitigations to our knowledge."