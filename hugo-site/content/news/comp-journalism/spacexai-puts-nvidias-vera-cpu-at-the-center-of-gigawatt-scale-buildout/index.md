---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-27T18:36:28.077361+00:00'
exported_at: '2026-09-27T18:36:29.528545+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/spacexai-puts-nvidias-vera-cpu-at-the-center-of-gigawatt-scale-buildout
structured_data:
  about: []
  author: ''
  description: SpaceXAI will deploy NVIDIA's Vera CPUs to run the CPU-intensive work
    behind its next generation of agentic AI applications, expanding an AI infrastructure
    buildout behind its Grok models that the company says is scaling...
  headline: SpaceXAI Puts NVIDIA’s Vera CPU at the Center of Gigawatt-Scale Buildout
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/spacexai-puts-nvidias-vera-cpu-at-the-center-of-gigawatt-scale-buildout
  publisher:
    logo: /favicon.ico
    name: GTCode
title: SpaceXAI Puts NVIDIA’s Vera CPU at the Center of Gigawatt-Scale Buildout
updated_at: '2026-09-27T18:36:28.077361+00:00'
url_hash: 1e4e7525861e7d46e8a3841a58928d24293607a8
---

SpaceXAI will deploy NVIDIA’s Vera CPUs to run the CPU-intensive work behind its next generation of agentic AI applications, expanding an AI infrastructure buildout behind its Grok models that the company says is scaling toward gigawatts of computing capacity,
[NVIDIA announced on August 24, 2026](https://nvidianews.nvidia.com/news/spacexai-adopts-nvidia-vera-cpu-to-accelerate-agentic-ai-at-massive-scale)
.

The deal extends beyond terrestrial data centers. SpaceXAI plans to base its first-generation Starmind AI satellite on an optimized
[NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/technologies/rubin/)
rack-scale system, taking the same architecture that powers its ground-based AI factories into orbit.

The announcement is a CPU story, which makes it unusual in an industry that measures everything in GPUs. Agentic AI workloads — systems that take actions rather than simply generate answers — lean heavily on conventional processors to orchestrate tools, execute code, process data, and run simulations between model calls. When those CPUs lag, the GPUs they feed sit idle. That is the bottleneck NVIDIA built Vera to attack.

“Agentic AI requires a new kind of computing system — one built not only to generate answers, but to take action,” said Ian Buck, NVIDIA’s vice president of hyperscale and high-performance computing, in the announcement. “SpaceXAI is taking this architecture from massive AI factories to the next frontier of computing in orbit.”

“Vera gives us the CPU performance and memory bandwidth to run enormous amounts of orchestration, code and data processing while keeping GPUs doing what they do best,” said Mike Nicolls, president of SpaceXAI, in the same release.

## What Vera Brings to the Rack

Vera is NVIDIA’s first CPU designed from the ground up for agentic AI rather than adapted from general-purpose server parts. It carries 88 custom Olympus cores with NVIDIA’s Spatial Multithreading technology, which creates 176 threads with partitioned core resources, and it pairs them with high-bandwidth LPDDR5X memory delivering up to 1.2 terabytes per second of bandwidth. NVIDIA says that combination completes tasks up to 1.8 times faster than x86 CPUs across agentic AI, reinforcement learning, and data-processing workloads, and up to 80 percent faster on sandbox environments specifically,
[according to the company’s product documentation](https://www.nvidia.com/en-us/data-center/vera-cpu/)
.

The memory subsystem is where the architecture diverges most sharply from the x86 status quo. Vera uses LPDDR5X on detachable, field-replaceable SOCAMM modules rather than conventional DDR5, which NVIDIA says delivers twice the bandwidth and three times the bandwidth per core of leading x86 CPUs while drawing roughly half the power. The chip supports up to 1.5 terabytes of memory per socket, and a second-generation on-die fabric connects all 88 cores with 3.4 TB/s of bisectional bandwidth, avoiding the cross-chiplet latency that plagues multi-die server CPUs. An NVLink-C2C interface provides up to 1.8 TB/s of coherent bandwidth between Vera CPUs and NVIDIA’s Rubin GPUs.

As a standalone platform, the Vera CPU rack integrates up to 256 Vera CPUs in a dense, liquid-cooled chassis and supports more than 22,500 concurrent sandbox environments: the isolated software containers where agents run code, call tools, and iterate through evaluation loops. In agentic systems, each reasoning cycle can spawn thousands of these environments; the CPU fleet that hosts them effectively sets the throughput ceiling for the entire AI factory.

## The Starmind Extension

SpaceXAI’s orbital ambitions give the deployment a second dimension. The company is developing AI computing infrastructure for orbit, where power delivery, thermal management, bandwidth, reliability, and physical integration impose constraints nothing like a terrestrial data center. Its planned first-generation Starmind AI satellite will be built on an optimized Vera Rubin NVL72 system (the rack-scale platform that combines 72 Rubin GPUs with 36 Vera CPUs, ConnectX-9 SuperNICs, and BlueField-4 data processing units, linked by sixth-generation NVLink switches).

NVIDIA and SpaceXAI said they are working to adapt that platform to orbital requirements while preserving a common architecture and software ecosystem across ground and space deployments.

## One Architecture, Gigawatts of Capacity

For SpaceXAI, the Vera adoption consolidates its compute stack on a single vendor’s architecture as it scales. SpaceXAI is expanding its AI infrastructure behind Grok on the NVIDIA Vera Rubin platform as it scales toward gigawatts of computing capacity, the unit in which serious AI infrastructure is now measured. The Vera Rubin platform gives it a common foundation across training, reasoning, and inference, codesigned across compute, networking, and software with NVLink interconnects, Spectrum-X Ethernet networking, and BlueField data processing.

NVIDIA, for its part, gets a flagship deployment for a product line it launched specifically to capture the CPU side of the agentic AI buildout. The company has described Vera as the first CPU built for AI agents, and SpaceXAI joins Anthropic, OpenAI, and Oracle Cloud Infrastructure among the early production deployments NVIDIA has named for the part.

The economics are the point. NVIDIA pitches Vera Rubin on delivering more tokens per watt and lower cost per token than Blackwell, so faster CPU orchestration that keeps GPUs utilized translates directly into more output per watt. As SpaceXAI expands toward gigawatts of computing capacity, that efficiency math compounds. NVIDIA has pitched the Vera Rubin platform on exactly that basis: more tokens per watt and lower cost per token than its prior Blackwell architecture.