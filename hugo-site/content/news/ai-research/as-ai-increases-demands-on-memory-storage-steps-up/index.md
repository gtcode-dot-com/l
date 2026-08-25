---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-08-25T01:49:34.500096+00:00'
exported_at: '2026-08-25T01:49:36.753696+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ai-storage-fms
structured_data:
  about: []
  author: ''
  description: At FMS, NVIDIA shows how accelerated computing enables AI applications
    to access storage directly — fast enough to act like memory and secure by design.
  headline: As AI Increases Demands on Memory, Storage Steps Up
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ai-storage-fms
  publisher:
    logo: /favicon.ico
    name: GTCode
title: As AI Increases Demands on Memory, Storage Steps Up
updated_at: '2026-08-25T01:49:34.500096+00:00'
url_hash: 33604144a555fc7a7db77939fdbaf80a393ee051
---

Surging AI demands are driving the need for massive datasets and context windows that burst past the confines of system memory.

But rising needs aren’t met by simply adding more storage capacity. What’s needed is useful, grounded insights from AI factories and efficient, secure storage architectures that enable those insights.

At this week’s Future of Memory and Storage (FMS) conference, NVIDIA is unveiling new storage advancements and showcasing how the next leap in AI depends as much on the storage infrastructure feeding accelerated computing as on the computing power itself.

The pressure on that infrastructure is intensifying as AI agents consume massive amounts of data — and GPUs can now initiate storage requests directly, generating thousands of concurrent operations.

To serve those requests, storage systems must continuously encrypt, compress, verify and reconstruct data. These critical data services can become bottlenecks when thousands of agents access storage simultaneously.

Benchmarks highlighted in this
[NVIDIA technical blog](https://developer.nvidia.com/blog/nvidia-vera-storage-benchmarks-faster-encryption-compression-integrity-checking-and-recovery-for-ai-native-storage/)
show that the NVIDIA Vera CPU, part of
[NVIDIA Vera BlueField-4 STX](https://nvidianews.nvidia.com/news/nvidia-vera-bluefield-4-stx-brings-agentic-ai-storage-processing-with-in-silicon-security)
, delivers up to 3.21x higher throughput than an x86 CPU in a two-stage compression and encryption pipeline. This means that with Vera, storage platforms can absorb the flood of AI data more efficiently — delivering greater throughput with significantly less compute infrastructure.

With accelerated computing, storage stops being a passive place to keep data and becomes an active part of the data path.

This upends the old economics of determining when data belongs in memory (where applications can fetch it faster) versus on a storage drive (where it can be held in cheap and plentiful space). The tradeoff was first framed 40 years ago, when the answer was measured in accessing that data in minutes. On today’s GPUs, paired with
[AI storage solutions](https://www.nvidia.com/en-us/data-center/ai-storage/)
from NVIDIA and partners, the same tradeoff now plays out in microseconds.

Closing the gap between AI’s needs and memory shortage depends on
[extreme codesign](https://developer.nvidia.com/blog/building-for-the-rising-complexity-of-agentic-systems-with-extreme-co-design/)
across the whole ecosystem, from memory and storage manufacturers to the software built on them.

## **Open Source NVIDIA cuFile APIs Enable Interoperability for Storage Solutions**

At FMS, NVIDIA announced it is open sourcing its
[cuFile application programming interfaces (APIs)](https://github.com/xio-sig)
— and the vertical storage software stack underneath them — which let GPUs, not just CPUs, read from and write to storage directly. cuFile is an open source component of
[NVIDIA GPUDirect Storage](https://docs.nvidia.com/gpudirect-storage/)
.

Using hundreds of thousands of GPU threads, fast high-bandwidth memory and other methodologies, cuFile enables securely accessing data from storage in just microseconds.

This represents how the industry is unifying a security-first storage stack based on Linux best practices, providing interoperability between GPUs and data.

In addition, fast, secure access to data and storage is a foundational element to powering preventive and detective cybersecurity measures. Making cuFile openly available will help make security context, data and storage accessible at the speed AI-powered defenses need. Such open technologies support initiatives such as the new
[Open Secure AI Alliance](https://blogs.nvidia.com/blog/open-secure-ai-alliance/)
.

[This site](https://github.com/xio-sig)
is the new home for APIs that are open to contributions — with Google, Intel, NVIDIA and Meta as inaugural maintainers — and can be optimized for use across various software and hardware platforms, driving innovation and efficiency for developers and enterprises.

## **NVIDIA and Industry Leaders Advance New Frontier of AI Storage**

In addition, NVIDIA and storage industry leaders are optimizing memory and storage solutions through an initiative called
[Storage-Next](https://resources.nvidia.com/en-us-ai-storage/nvidia-storage-next)
. The NVIDIA-driven initiative brings together storage makers, controller vendors, thermal design, cooling and orchestration operators, and standards bodies to align on how GPU-driven storage should behave — then turn these advancements into interoperable, open industry standards.

Storage-Next includes over 40 leading storage and flash vendors — including DDN, KIOXIA and Micron — each contributing to the next generation of AI storage technologies with NVIDIA.

The initiative is grounded in accelerated data access for large AI datasets. To support this, NVIDIA offers
[SCADA](https://www.youtube.com/watch?v=OZloQQZGmQQ&amp;t=67s)
— short for scaled, accelerated data access — a framework that lets massively parallel GPUs pull only the data necessary for the application directly from storage into their own high-speed memory.

For example, DDN is integrating SCADA with Infinia, its software-defined, AI-native data intelligence platform built to eliminate storage bottlenecks at scale.

“AI success will be defined not by how much infrastructure organizations own, but by how productively they use it,” said Sven Oehme, chief technology officer at DDN. “Our collaboration with NVIDIA is helping create a more direct, efficient connection between GPUs and data — keeping accelerated computing resources productive, speeding time to insight and enabling customers to achieve stronger business and financial returns from their AI investments.”

Storage-Next and SCADA extend NVIDIA’s longstanding work on AI storage infrastructure, including on
[NVIDIA Vera BlueField-4 STX](https://nvidianews.nvidia.com/news/nvidia-vera-bluefield-4-stx-brings-agentic-ai-storage-processing-with-in-silicon-security)
— a modular, rack-scale foundation powered by the NVIDIA Vera Rubin platform, NVIDIA Vera BlueField-4 storage processors and
[NVIDIA Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/)
networking.

![](https://blogs.nvidia.com/wp-content/uploads/2026/08/inline-1785797311823.jpeg)


NVIDIA Vera BlueField-4 STX storage processor.

Defining a new class of AI-native data platforms,
[NVIDIA STX](https://www.nvidia.com/en-us/data-center/ai-storage/stx/)
uses the unified
[NVIDIA DOCA](https://www.nvidia.com/en-us/networking/products/software/doca/)
security stack to let enterprises enable continuous policy enforcement in the AI data path.

Plus,
[NVIDIA CMX Context Memory Storage](https://www.nvidia.com/en-us/data-center/ai-storage/cmx/)
provides an AI‑native context tier for long‑context, multi‑turn, agentic AI inference, built on NVIDIA STX.

## **SCADA Enables Fast AI Storage That Stays Secure**

Speed at the storage layer comes with a catch. Letting an application talk straight to a drive is quick, but done carelessly, it can scribble over other processes’ memory — a security hole, not a feature.

NVIDIA SCADA uses a safe, robust method to achieve scaled direct access by splitting the job in two:

* The user parts of an application that need raw speed stay outside the trusted computing base.
* A separate, privileged component configures protected access between the user application and its approved storage at setup, adhering to standard Linux protocols for security enforcement while efficiently safeguarding data.

It’s all part of how advancements in fast, massively parallel, efficient, secure AI storage infrastructure can feed better data to applications and AI factories — so they can produce more useful, accurate, grounded intelligence at scale.

*Join NVIDIA sessions at*
[*FMS*](https://www.terrapinn.com/conference/future-memory-storage/index.stm)
*, running Aug. 4-6 in Santa Clara, California, and learn more about*
[*NVIDIA AI storage*](https://www.nvidia.com/en-us/data-center/ai-storage/)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*