---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-11T03:42:50.518631+00:00'
exported_at: '2026-06-11T03:42:51.936533+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation
structured_data:
  about: []
  author: ''
  description: An overview of DiffusionGemma, an exceptionally fast text generation
    model with up to 4x faster speeds.
  headline: 'DiffusionGemma: 4x faster text generation'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/diffusiongemma-4x-faster-text-generation
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'DiffusionGemma: 4x faster text generation'
updated_at: '2026-06-11T03:42:50.518631+00:00'
url_hash: 654ba11c9faceaf3b1eceb3393ff93959c70cbb1
---

## **Why diffusion for text?**

While the AI research community has explored diffusion-based text generation for years, applying it to large models has remained a challenge. DiffusionGemma changes this by shifting how models use hardware.

### **The trade-off with traditional models**

Most language models act like a typewriter, generating one token at a time from left to right. In the cloud, this is efficient because servers can batch thousands of user requests together to share the hardware load. But when run locally for a single user, this word-by-word process leaves your dedicated GPU or TPU underutilized — it spends most of its time simply waiting for the next "keystroke."

DiffusionGemma reverses this inefficiency. Instead of predicting words sequentially, it drafts an entire 256-token paragraph simultaneously. By giving the computer's processor a larger chunk of work at once, DiffusionGemma utilizes your hardware to its full potential. It upgrades your model inference from a single, sequential typewriter to a massive printing press that stamps the entire block of text simultaneously.