---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-11T02:09:26.602728+00:00'
exported_at: '2026-06-11T02:09:29.375843+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-gemma-4-12b-a-unified-encoder-free-multimodal-model
structured_data:
  about: []
  author: ''
  description: An overview of Gemma 4 12B, a model designed to bring high-performance
    multimodal intelligence directly to your laptop.
  headline: 'Introducing Gemma 4 12B: a unified, encoder-free multimodal model'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-gemma-4-12b-a-unified-encoder-free-multimodal-model
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Introducing Gemma 4 12B: a unified, encoder-free multimodal model'
updated_at: '2026-06-11T02:09:26.602728+00:00'
url_hash: 644db884346b8e03de11af232d3364c073bfff35
---

Today, we are introducing Gemma 4 12B, our latest model designed to bring agentic multimodal intelligence directly to laptops. Bridging the gap between our edge-friendly E4B and our more advanced 26B Mixture of Experts (MoE), Gemma 4 12B packages powerful capabilities inside a reduced memory footprint. It is also our first mid-sized model to feature native audio inputs.

Thanks to the developer community,
[Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)
models have now crossed 150 million downloads. You’ve built everything from
[wearable robotic arms](https://www.youtube.com/watch?v=OhaIA3bYwmg)
for physical assistance to
[enterprise-grade AI security](https://deepmind.google/models/gemma/gemmaverse/hirundo/)
. We're excited to see what you build with this latest addition.

Here’s an overview of what makes Gemma 4 12B unique:

* **Novel unified architecture:**
  No multimodal encoders. The vision and audio inputs flow directly into the LLM backbone.
* **Advanced reasoning:**
  Benchmark performance nearing our 26B model, unlocking powerful multi-step reasoning and agentic workflows.
* **Laptop ready:**
  Small enough to run locally with just 16GB of VRAM or unified memory.
* **Open and accessible:**
  Released under an Apache 2.0 license with support across the developer ecosystem.
* **Drafter-ready:**
  Gemma 4 12B comes equipped with Multi-Token Prediction (MTP) drafters to reduce latency.

Together, these features bring advanced multimodal capabilities to everyday hardware without sacrificing speed or reasoning. Let's now take a closer look at how Gemma 4 12B achieves this.

### Run state-of-the-art agents locally

Gemma 4 12B delivers performance nearing our larger 26B MoE model on standard benchmarks, but at less than half the total memory footprint. Small enough to run locally on consumer laptops with 16GB of RAM, it unlocks powerful multimodal and agentic experiences right on your machine.