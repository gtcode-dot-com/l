---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-04T03:25:47.039075+00:00'
exported_at: '2026-06-04T03:25:50.130442+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/vera-cpu-phoronix
structured_data:
  about: []
  author: ''
  description: In the new Phoronix benchmark, Vera delivers winning performance and
    memory results for agentic AI.
  headline: NVIDIA Vera CPU Is ‘Packing a Heavy-Hitting Punch’ Against Competition
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/vera-cpu-phoronix
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Vera CPU Is ‘Packing a Heavy-Hitting Punch’ Against Competition
updated_at: '2026-06-04T03:25:47.039075+00:00'
url_hash: ce407f46068a508b1111be3a205208e0a53e8eaa
---

The shift to agentic AI creates a new CPU requirement for the AI factory: fast cores, massive memory bandwidth and the ability to sustain high performance when all cores are active.

Initial benchmark results published by
[Phoronix](https://www.phoronix.com/review/nvidia-vera-benchmarks)

today show that the NVIDIA Vera CPU meets this need. For this first public look, the benchmark scope was centered on the agentic workloads Vera was designed for in the modern data center.

The Vera CPU delivers the throughput AI factories need while optimizing platform power. Eighty-eight NVIDIA custom Olympus cores, 1.2TB/s of memory bandwidth and a high-speed, on-chip fabric results in a CPU platform that combines core performance and memory bandwidth in an efficient power envelope.

## **NVIDIA Olympus Delivers Aggressive Performance**

At the heart of Vera are custom NVIDIA Olympus CPU cores. Fully compatible with the Armv9.2 instruction set architecture, Olympus is designed for the sequential CPU work underpinning agentic AI: branch-heavy runtimes, sandboxed code, data processing and orchestration.

Vera’s monolithic die, wide cores, advanced branch prediction and the second-generation NVIDIA Scalable Coherency Fabric help Vera keep data moving across all 88 cores.

Phoronix’s testing of a single-socket Vera CPU — rated at 450-watt thermal design power with less than 30 watts of memory power — showed that it delivers outstanding performance within that power profile, along with generational gains across a broad array of workloads spanning code compilation, file compression, video transcoding, Python, Java and database management.

These are the same kinds of CPU-heavy tasks that agents and AI factories run every day: compiling code, executing runtimes, compressing data, querying databases and coordinating large software stacks.

“Going into this, I didn’t really know what to expect of NVIDIA’s Vera with the new Olympus cores,” wrote Michael Larabel, founder and principal author of Phoronix. “But in the end I was left realizing this is the most formidable competition to Intel and AMD x86\_64 processors ever realized.”

## **‘Incredible Advantage’ in Memory Performance**

Agentic workloads are not limited by core count alone. They need high core utilization and sustained memory bandwidth, making memory performance per watt a critical part of overall CPU efficiency.

Vera incorporates a second-generation LPDDR5X memory subsystem, enabling dramatically lower energy per bit compared to DDR5. This allows Vera to offer up to a massive 1.2 TB/s of bandwidth — up to 2x the peak memory bandwidth compared with traditional CPUs in less than 30 watts of memory power, as opposed to more than 100 watts for traditional DDR5.

In Phoronix STREAM TRIAD testing, Vera sustained 90% of its peak memory bandwidth — achieving the highest percentage of rated peak bandwidth of any CPU tested by Phoronix — and delivered over 4x the memory bandwidth per core compared with traditional x86 CPUs.

“NVIDIA Vera with its LPDDR5X memory was showing its incredible advantage in memory performance over current Intel Xeon and AMD EPYC processors,” Larabel wrote.

However, peak bandwidth is only part of the story. AI factory workloads run many sandboxes, tool calls and data services at the same time. In separate testing with Vera,
[Prime Intellect found](https://www.primeintellect.ai/blog/nvidia-collaboration)

that Vera maintained high bandwidth and low, consistent memory latency as more workloads ran in parallel — the kind of predictable performance needed for agentic AI.

## **A Large Generational Leap — and Leadership in Phoronix Testing**

Compared with the prior-generation NVIDIA Grace CPU, Vera delivered a 1.6x geometric mean increase in Phoronix’s testing — an incredible generation-over-generation gain.

“The difference from Grace to Vera was consistently exceeding my expectations for gen-on-gen performance we typically see for processors,” Larabel wrote. “NVIDIA’s Vera CPU with its in-house-designed Olympus CPU cores ends up packing a heavy-hitting punch with competitiveness to Intel/AMD x86\_64 CPUs that I have never seen out of any other ARM or non-x86\_64 processors.”

Vera led the tested CPU field, delivering a 1.5x overall performance advantage compared with a latest-generation 128-core x86 processor. The gains showed up in practical developer workloads. Single-socket Vera compiled a default Linux kernel in just 20 seconds, the fastest result Phoronix measured in that test. Vera delivered 2x faster Linux kernel compilation on a per-core basis compared with a 128-core processor.

“On a [geometric] mean basis, the NVIDIA Vera delivered 10% better performance than the AMD EPYC 9575F 5.0 GHz high frequency processor,” Larabel wrote.

## **Vera in Customer Testing, Coming Soon From Partners**

At NVIDIA GTC, NVIDIA announced widespread ecosystem support for Vera, spanning AI natives, supercomputing centers, cloud service providers and infrastructure providers.

NVIDIA has also
[delivered](https://blogs.nvidia.com/blog/vera-cpu-delivery/)

the first Vera CPUs to leading AI companies and cloud providers, marking an important milestone as Vera moves toward partner availability in the second half of the year.

Vera will be available from partners in dual- and single-socket systems, with air-cooled and liquid-cooled options to support AI factory deployments, from standard enterprise data centers to high-density agentic AI infrastructure.

Learn more about
[NVIDIA Vera](https://www.nvidia.com/en-us/data-center/vera-cpu/)

.