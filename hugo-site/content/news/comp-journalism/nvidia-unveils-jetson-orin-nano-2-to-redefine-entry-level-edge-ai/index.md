---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-10-01T19:25:31.601815+00:00'
exported_at: '2026-10-01T19:25:34.278886+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/nvidia-unveils-jetson-orin-nano-2-to-redefine-entry-level-edge-ai
structured_data:
  about: []
  author: ''
  description: NVIDIA on August 25, 2026 announced the Jetson Orin Nano 2, a successor
    to its entry-level robotics computer that doubles inference performance over the
    Jetson Orin Nano Super while holding the same compact form factor —...
  headline: NVIDIA Unveils Jetson Orin Nano 2 to Redefine Entry-Level Edge AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/nvidia-unveils-jetson-orin-nano-2-to-redefine-entry-level-edge-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Unveils Jetson Orin Nano 2 to Redefine Entry-Level Edge AI
updated_at: '2026-10-01T19:25:31.601815+00:00'
url_hash: 1b8cc193de4dca4a6e04ace201d211f297a0fbb5
---

NVIDIA on August 25, 2026 announced the
[Jetson Orin Nano 2](https://nvidianews.nvidia.com/news/nvidia-announces-jetson-orin-nano-2-robotics-computer-to-redefine-entry-level-edge-ai)
, a successor to its entry-level robotics computer that doubles inference performance over the Jetson Orin Nano Super while holding the same compact form factor — and cuts power draw by 40% when matched to its predecessor’s performance.

The module packs 78 trillion operations per second of AI compute, 8GB of memory, and an 8-core Arm CPU, and is aimed at the machines that have defined the Jetson line’s customer base: robots, delivery and inspection drones, and vision AI systems. NVIDIA says the gain over the Orin Nano Super comes from improved Tensor Cores and higher memory bandwidth. In a 15-watt mode, the new module delivers the Super’s performance on 40% less power.

“Today’s small and medium frontier models have reached the accuracy of last year’s largest frontier models, unlocking real-time intelligence for edge devices,” said Deepu Talla, vice president of robotics and edge AI at NVIDIA. “The Jetson Orin Nano 2 computer puts that breakthrough within reach of millions of developers, delivering the performance and energy efficiency needed for real-time reasoning at the edge.”

The software story mirrors the hardware one. Jetson Orin Nano 2 runs NVIDIA’s open stack and its
[Jetson AI Lab](https://www.jetson-ai-lab.com/)
agent skills, with support for large language and vision language models tuned for memory-efficient edge inference, including NVIDIA’s own Cosmos and Nemotron open models alongside Gemma 4 and Qwen 3. NVIDIA says more than 3 million developers have built on its robotics stack to date.

## Wing, Matic and Doosan Bobcat Line Up as Early Adopters

The customer list attached to the announcement reads like a cross-section of where compact edge AI compute is actually being deployed. Wing, the Alphabet-owned drone delivery company, already runs Jetson Orin Nano Super and NVIDIA’s software stack in its delivery fleet and says it plans to evaluate the new module for real-time perception and reasoning work.

“Drone delivery depends on AI that can enable fast, reliable understanding of the real world,” said Dinuka Abeywardena, head of perception at Wing. “Wing is exploring Jetson Orin Nano 2 to give us a path to more responsive, energy-efficient drones that can help make deliveries quicker and more dependable for customers.”

Matic Robots, the consumer robotics company behind a vision-based home cleaning robot, is adopting the module outright rather than evaluating it. The company plans to use the added compute for conversational AI, gesture detection, precision mapping with semantic understanding of home layouts, and autonomous cleaning — all running on-device rather than in the cloud. “Home robots need to understand people, map spaces precisely, understand the layout of objects and spaces, and clean autonomously in dynamic and constantly changing environments,” said Navneet Dalal, cofounder and CEO of Matic. Industrial vision company Cognex and heavy-equipment maker Doosan Bobcat round out the named early adopters.

## What the Specs Change From the Orin Nano Super

The comparison baseline matters here, because the Super is barely 20 months old. NVIDIA
[introduced the Jetson Orin Nano Super Developer Kit on December 17, 2024](https://developer.nvidia.com/blog/nvidia-jetson-orin-nano-developer-kit-gets-a-super-boost/)
, largely as a software-driven refresh: a new power mode pushed the existing module from 40 to 67 sparse INT8 TOPS, memory bandwidth from 68 to 102 GB/s, and the kit price dropped from $499 to $249. That board pairs a 1,024-core Ampere GPU and 32 Tensor Cores with a 6-core Arm Cortex-A78AE CPU and 8GB of LPDDR5 memory, in a 7W-to-25W envelope.

The Orin Nano 2 is a genuine hardware step over that platform: 78 TOPS against the Super’s 67 sparse TOPS, an 8-core CPU in place of the 6-core part, and (per NVIDIA’s own figure) twice the inference throughput in the same footprint. For the robot and drone builders the Jetson line serves, the 40% power reduction at matched performance is arguably the more consequential number. In 15-watt mode the module delivers the Super’s performance on 40% less power, roughly 9 watts, per NVIDIA’s own figures.

The trade press has tracked the Jetson line’s push into physical AI for years, and Unite.AI covered
[NVIDIA’s broader full-stack robotics platform](https://www.unite.ai/nvidia-unveils-full-stack-robotics-platform/)
earlier this year. Orin Nano 2 sits at the bottom of that stack’s price and power ladder: the entry point whose volumes do the ecosystem-building.

## A Broad Carrier-Board Ecosystem, and a Long Wait for Hardware

NVIDIA is not shipping alone. More than 20 partners (including AAEON, ADLINK, Advantech, Aetina, Antmicro, Connect Tech, Seeed Studio and YUAN) are building carrier boards, hardware systems, customized AI software and reference designs around the module.
[Aptiv announced day-one support](https://www.aptiv.com/en/newsroom/article/aptiv-accelerating-production-ready-physical-ai-with-support-for-nvidia-jetson-orin-nano-2)
, pairing the module with its surround-view camera and radar sensing stack, robotics compute solutions and Wind River lifecycle software, targeting customers moving from prototype to production in drones, robotics and industrial automation.
[Connect Tech](https://connecttech.com/announces-support-new-nvidia-jetson-orin-nano-2-robotics-computer/)
, a longtime Jetson carrier-board maker, notes the module operates within a 40W power envelope at the top end.

The one number that will temper enthusiasm is the calendar. The Jetson Orin Nano 2 module and developer kit are expected to be available in the first half of 2027 — a gap of at least four months between announcement and silicon. NVIDIA’s release sets no pricing, leaving the $249 Super as the entry point until then.