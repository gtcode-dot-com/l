---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-06T14:15:35.495677+00:00'
exported_at: '2026-05-06T14:15:37.767715+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc
structured_data:
  about: []
  author: ''
  description: Multipath Reliable Connection — a new transport protocol proven first
    and optimized on NVIDIA Spectrum-X Ethernet hardware — is now open to the industry.
  headline: NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard
    for Gigascale AI, Now With MRC
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/spectrum-x-ethernet-mrc
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Spectrum-X — the Open, AI-Native Ethernet Fabric — Sets the Standard
  for Gigascale AI, Now With MRC
updated_at: '2026-05-06T14:15:35.495677+00:00'
url_hash: 6e4cff9d065fbe2736c87ea20bb7c88b27ec14a0
---

The race to build the world’s most powerful AI factories demands networking that keeps pace with the ambitions of AI itself.

[NVIDIA Spectrum-X Ethernet](https://www.nvidia.com/en-us/networking/spectrumx/)

scale-out infrastructure stands at the forefront of that race as the most advanced AI networking technology available today, deployed by industry leaders who can’t afford to compromise on performance, resilience or scale.

That includes

OpenAI

,

Microsoft

and

Oracle

.

Companies including NVIDIA,
[Microsoft](https://aka.ms/BuildingResilientNetworksForAISupercomputers)
and
[OpenAI](https://openai.com/index/mrc-supercomputer-networking)

have
[demonstrated](https://cdn.openai.com/pdf/resilient-ai-supercomputer-networking-using-mrc-and-srv6.pdf)

industry leadership by introducing Multipath Reliable Connection (MRC), an RDMA transport protocol. MRC enables a single RDMA connection to distribute traffic across multiple network paths, improving throughput, load balancing and availability for large-scale AI training fabrics.

Think of it as replacing a single-lane road spanning a town with a cleverly laid-out street grid system paired with an on-the-fly traffic app, enabling drivers to reroute around slowdowns and road closures.

“Deploying MRC in the Blackwell generation was very successful and was made possible by a strong collaboration with NVIDIA,” said

Sachin Katti,

head of industrial compute at OpenAI. “MRC’s end-to-end approach enabled us to avoid much of the typical network-related slowdowns and interruptions and maintain the efficiency of frontier training runs at scale.”

In addition, Microsoft and NVIDIA have a longstanding collaboration focused on advancing the infrastructure required for the next generation of AI.
[Microsoft’s Fairwater](https://blogs.microsoft.com/blog/2025/09/18/inside-the-worlds-most-powerful-ai-datacenter/)

an

d
[Oracle Cloud Infrastructure (OCI’s) Abilene](https://blogs.oracle.com/cloud-infrastructure/first-principles-multipath-reliable-connection)
data center, two of the largest AI factories purpose-

built for training and deploying leading-edge frontier LLMs, rely on MRC to deliver on performance, scale and efficiency requirements. NVIDIA Spectrum-X Ethernet is suited for this environment, helping provide the network foundation needed to run large-scale AI models and applications with confidence.

Proven first in production with performance optimized on NVIDIA Spectrum-X Ethernet hardware and now
[released](https://www.opencompute.org/documents/ocp-mrc-1-0-pdf)

as an open specification through the Open Compute Project, MRC demonstrates the power of the Spectrum-X Ethernet platform: purpose-built hardware, deep telemetry and intelligent fabric control working together to take a new protocol — a set of rules that controls how data moves between two systems across a network — from concept to gigascale AI production.

MRC delivers high levels of GPU utilization by load-balancing traffic across all available paths, enabling every GPU to get the bandwidth it needs throughout a training run. It sustains high bandwidth even under congestion by dynamically avoiding overloaded paths in real time.

When data loss occurs, intelligent retransmission enables rapid, precise recovery, minimizing the impact of short-lived interruptions to long-running jobs, helping avoid GPU idle time.

Administrators also gain fine-grained visibility and control over traffic paths, simplifying operations and accelerating troubleshooting at scale.

MRC, deployed on Spectrum-X Ethernet, is optimized and engineered for resilience at massive scale. Its failure bypass technology can — in just microseconds — detect a network path failure and reroute traffic automatically in hardware.

This failure bypass technology matters for AI training clusters where thousands of GPUs must stay synchronized, as even a brief network disruption can slow or interrupt an entire training job. Spectrum-X Ethernet prevents that by responding at hardware speed, keeping traffic flowing along precise pathways across gigascale AI fabrics.

Another innovation key to achieving gigascale AI factories is multiplanar network designs, which OpenAI deploys with Spectrum-X Ethernet in conjunction with MRC. A multiplane network consists of multiple independent network fabrics, or planes, with each providing an alternate communication path between GPUs.

The NVIDIA Spectrum-X Multiplane capability enhances this network architecture by supporting hardware-accelerated load balancing across the planes, boosting resiliency and scale without sacrificing performance. This keeps latencies predictably low while scaling to hundreds of thousands of GPUs.

With Spectrum-X Ethernet, customers are provided with a choice of RDMA transport models. Both Spectrum-X Ethernet Adaptive RDMA and MRC protocols,

as well as other custom protocols

,

run natively across
[NVIDIA ConnectX SuperNICs](https://www.nvidia.com/en-us/networking/products/ethernet/supernic/)

and
[Spectrum-X Ethernet switches](https://www.nvidia.com/en-us/networking/ethernet-switching/)

and support multiplanar network designs at gigascale.

In this way, the Spectrum-X Ethernet hardware and software infrastructure that powers today’s largest AI clusters gives customers the flexibility to choose the right transport for their workload.

The MRC transport protocol is the latest example of how the industry is using Spectrum-X Ethernet as a flexible, composable platform that integrates across the full breadth of modern AI infrastructure.

As AI factories continue to scale, the network must do more than move data quickly. It must be intelligent, resilient and based on open standards. NVIDIA Spectrum-X Ethernet delivers on all three, and with MRC, it continues to set the standard for advanced AI networking.

NVIDIA collaborated on MRC development with AMD, Broadcom, Intel, Microsoft and OpenAI.

*Learn more about NVIDIA Spectrum-X Ethernet on the*
[*webpage*](https://www.nvidia.com/en-us/networking/spectrumx/)
*,*
[*datasheet*](https://resources.nvidia.com/en-us-networking-ai/networking-ethernet-1)
*and*
[*technical whitepaper*](https://resources.nvidia.com/en-us-networking-ai/nvidia-spectrum-x)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information*
*.*