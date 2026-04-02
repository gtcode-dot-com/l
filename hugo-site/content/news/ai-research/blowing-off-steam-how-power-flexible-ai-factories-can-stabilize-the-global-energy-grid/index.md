---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:21:53.563308+00:00'
exported_at: '2026-04-02T04:21:56.408342+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/power-flexible-ai-factories-energy-grid
structured_data:
  about: []
  author: ''
  description: Emerald AI — in collaboration with NVIDIA and others — showcased how
    “power-flexible” AI factories can adjust power usage during peak demand.
  headline: 'Blowing Off Steam: How Power-Flexible AI Factories Can Stabilize the
    Global Energy Grid'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/power-flexible-ai-factories-energy-grid
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Blowing Off Steam: How Power-Flexible AI Factories Can Stabilize the Global
  Energy Grid'
updated_at: '2026-04-02T04:21:53.563308+00:00'
url_hash: b65888a7c8c68b1b132919aef9e97ef128e81ca5
---

At the half-time whistle of the UEFA EURO 2020 round of 16 football match between England and Germany, millions of viewers stepped away from their screens in the U.K. to do the same thing at the same time — turn on their kettles.

National Grid, which provides electricity for England and Wales, saw
[a demand spike of about 1 gigawatt](https://www.neso.energy/news/euro-2020-and-tv-pick-effect)
— an increase equivalent to the average output of a standard nuclear reactor — in a matter of minutes from this countrywide tea break. Grid operators must carefully manage these demand peaks to keep the system stable, and this could become even more difficult as the grid continues to add large new customers.

But what if those new customers could actually be flexible and relieve the grid during periods of peak strain?

In a recent
[white paper](https://www.ngpartners.com/stories/emerald-ai-whitepaper)
, Emerald AI — in collaboration with NVIDIA, EPRI, National Grid and Nebius — showcased how “power-flexible” AI factories can autonomously adjust their power usage during peak demand.

For AI factories, this could unlock significantly faster grid connections without waiting for massive, years-long infrastructure upgrades. For the public, it helps limit grid build outs by curbing the peak load that the system needs to serve, helping keep electricity rates affordable for everyday bill payers.

## **Boil the Kettle, Balance the Grid**

After successful proof-of-concept trials at AI factories in Arizona, Virginia and Illinois, Emerald AI took its flexible grid solution across the pond, last December, bringing the
[Emerald AI Conductor Platform](https://www.emeraldai.co/)
to Nebius’ new AI factory in London, built on NVIDIA infrastructure — among the first of its kind in the U.K.

At the AI factory, the research team ran production-grade AI workloads on a cluster of
[96 NVIDIA Blackwell Ultra GPUs](https://developer.nvidia.com/blog/inside-nvidia-blackwell-ultra-the-chip-powering-the-ai-factory-era/)
connected through the
[NVIDIA Quantum-X800 InfiniBand platform](https://www.nvidia.com/en-us/networking/products/infiniband/quantum-x800/)
. The
[NVIDIA System Management Interface](https://developer.nvidia.com/system-management-interface)
is used to retrieve consistent, seconds-level GPU power telemetry.

EPRI and National Grid simulated stress scenarios on the power grid — from lightning strikes to long periods of low wind power supply — and sent signals instructing the AI factory, with the help of the Conductor Platform, to temporarily reduce its power use to relieve grid strain.

One of these scenarios was the “TV pickup” phenomenon, where that very same Euro 2020 football match’s energy surge was reenacted.

As millions of simulated tea kettles were about to be turned on, the AI cluster ramped down its power use — successfully acting as a shock absorber for the abrupt power surge without disrupting the highest-priority AI workloads running on the cluster.

In practice, this means the grid can manage sudden demand swings using existing capacity more efficiently, reducing the need to overbuild permanent infrastructure to meet worst-case peaks and helping keep rates affordable for everyday consumers.

“With this technology, AI factories become friendly and helpful grid assets,” said Varun Sivaram, founder and CEO of Emerald AI. “Simultaneously, the AI factories get connected much faster to the grid because they can tap into existing power grids.”

## **Stress Relievers, Not Query Crushers**

In the Nebius AI factory demonstration, despite the quick ramp down of energy to power the national tea break, Emerald AI Conductor ensured that the simulated high-priority AI workloads performed at peak throughput, while more flexible jobs were slowed down temporarily.

Emerald AI recorded 100% alignment with over 200 power targets that EPRI and National Grid instructed the AI cluster to follow for this experiment.

![High-level white paper stats including 100% compliance across 200+ power targets, 22 distinct real-time dispatch events, and 30% slashed power in under 40 seconds. ](https://blogs.nvidia.com/wp-content/uploads/2026/02/corporate-self-service-infographic-templates-final-1.jpg)

“We did tests that go beyond the ones that have been done so far in the U.S. because we tested not just the GPUs, but also the CPUs and everything that sits around it — as well as the total power consumption of the IT equipment,” said Steve Smith, group chief strategy officer of National Grid. “We’ve proved the value that this technology brings.”

## **Scaling London’s Grid at Super Speed**

London’s power grid is constantly working to meet the ever-growing energy needs of its citizens. Its grid operators — including National Grid — face a key bottleneck: constraints in infrastructure upgrades to connect large customers.

Plugging flexible AI factories into the grid with solutions like Emerald AI’s Conductor Platform won’t just help to stabilize energy spikes —  it can optimize the use of existing grid infrastructure to propel new industry talent and economic opportunities in the U.K.

“We have enormous skills and potential in AI,” said Smith. “We’re never going to be on the scale of the U.S. in terms of data centers, but relative to the size of the country, we could be — and we’re certainly seeing that interest from many of the hyperscalers. So, it gives us the opportunity to play our part as National Grid in helping unlock that economic growth for the country.”

Four demonstrations in, Emerald AI and NVIDIA are gearing up to put power-flexible AI factories into real-world deployment with the Aurora AI Factory in Virginia, set to open this year.

Learn more about the first
[power-flexible](https://www.emeraldai.co/blog/launching-the-first-power-flexible-ai-factory-with-nvidia)
AI factory powered by
[NVIDIA GPUs](https://blogs.nvidia.com/blog/omniverse-dsx-blueprint/)
.