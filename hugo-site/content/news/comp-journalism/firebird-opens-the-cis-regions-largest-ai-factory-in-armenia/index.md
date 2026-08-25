---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-08-25T01:50:12.244517+00:00'
exported_at: '2026-08-25T01:50:19.221805+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/firebird-opens-the-cis-regions-largest-ai-factory-in-armenia
structured_data:
  about: []
  author: ''
  description: 'Firebird, a U.S.-based AI cloud company, opened the CIS region''s
    largest AI factory in Armenia on August 8, 2026: a facility in Hrazdan built on
    NVIDIA accelerated computing and Dell PowerEdge servers, with Armenian Prim...'
  headline: Firebird Opens the CIS Region’s Largest AI Factory in Armenia
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/firebird-opens-the-cis-regions-largest-ai-factory-in-armenia
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Firebird Opens the CIS Region’s Largest AI Factory in Armenia
updated_at: '2026-08-25T01:50:12.244517+00:00'
url_hash: 27eb8423ea0b10619c5dfb15a633152b50752d2b
---

Firebird, a U.S.-based AI cloud company, opened the CIS region’s largest AI factory in Armenia on August 8, 2026: a facility in Hrazdan built on
[NVIDIA](https://blogs.nvidia.com/blog/firebird-ai-factory-armenia-blackwell-rubin-dsx/)

(
[NVDA](#)


)
accelerated computing and Dell PowerEdge servers, with Armenian Prime Minister Nikol Pashinyan, Kazakhstan’s Deputy Prime Minister Zhaslan Madiyev, and U.S. chargé d’affaires David Allen attending the opening ceremony.

The buildout plan is large by any regional standard: Firebird plans to deploy more than 70,000 NVIDIA Rubin and Blackwell GPUs and 300 megawatts of AI infrastructure capacity in Armenia by the end of 2027. The company says the site went from plan to operating capacity in just over six months — a fast delivery for a project of this class, and one that leaned on a supply chain of established vendors. Schneider Electric
(
[SND.DE](#)


)
delivered the power infrastructure, including medium- and low-voltage switchgear, three-phase uninterruptible power supplies, and rack enclosures, while Vertiv supplied a chilled-water cooling architecture managed through its iCOM CWM Chilled Water Manager, which coordinates cooling resources as AI workloads shift.

The facility is built on the
[NVIDIA DSX platform](https://www.nvidia.com/en-us/data-center/products/dsx/)
, which codesigns compute, networking, power, and cooling as one system. NVIDIA says DSX lets an operator run up to 40% more GPUs on the same footprint by recovering stranded power — the direct lever on tokens per dollar in a power-constrained build.

Firebird also said NVIDIA intends to invest in the company, following an earlier investment by CoreWeave
(
[CRWV](#)


)
in 2026. Early demand is coming from AI-native customers: Perplexity is working with Firebird to access high-performance infrastructure for its answer engine and AI agent platform.

## What the AI factory runs on

Firebird’s own
[data center page](https://www.firebird.ai/)
specifies the opened flagship, DC-1, at 6,144 NVIDIA B200 GPUs across 15 MW, liquid-cooled and built on NVIDIA’s reference architecture. A Phase 2 expansion, DC-2, is listed at 75,000 VR200 GPUs across 125 MW, with a third planned site at the same scale. The fleet interconnects over InfiniBand east-west and Ethernet north-south, with a BlueField-3 DPU on every node, and exposes capacity both as bare metal and through a multi-tenant cloud.

The DSX layer matters because of how the Armenia build is constrained. Rather than treating power, cooling, and compute as separate procurements, DSX coordinates them as one system: its MaxLPS software dynamically manages power at the GPU, rack, and workload levels to keep the site within its megawatt budget, while DSX OS handles fleet operations and DSX Flex can adapt workloads to grid signals. For a facility scaling from 15 MW toward a 300 MW target in roughly 18 months, that coordination is where the capacity math gets made.

## The story so far

The Armenia project has moved in fast, well-documented stages. Firebird announced a strategic collaboration with the Armenian government and NVIDIA at GTC Paris in June 2025, then secured a U.S. export license in November 2025 — the regulatory key that allowed advanced NVIDIA hardware into the country at all.

In February 2026, Firebird and the U.S. government
[announced Phase 2](https://www.prnewswire.com/news-releases/firebird-and-us-government-announce-phase-2-of-armenia-ai-megaproject-scaling-it-to-4-billion-and-50-000-gpu-in-2026--302683715.html)
, scaling the megaproject to $4 billion and roughly 50,000 GPUs with an export license for an additional 41,000 GB300 units (on top of the $500 million Phase One). U.S. Vice President JD Vance disclosed the expansion at a Yerevan press briefing alongside Pashinyan, NVIDIA’s Rev Lebaredian, and Firebird co-founders Razmig Hovaghimian and Alexander Yesayan. The August 8 opening turns the first phase of that paper capacity into a running facility.

## What happens next

Firebird’s stated target is more than 70,000 GPUs and 300 MW in Armenia by the end of 2027. Beyond Armenia, the company is pursuing an approximately 2-gigawatt AI infrastructure roadmap spanning Armenia, Kazakhstan, and additional markets, with NVIDIA’s support. The company describes its expansion as an effort to build the largest and most advanced compute clusters across frontier markets, with the intended NVIDIA and earlier CoreWeave investments funding the wider footprint.