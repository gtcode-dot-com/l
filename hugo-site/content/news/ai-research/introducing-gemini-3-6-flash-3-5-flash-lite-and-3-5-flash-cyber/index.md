---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-17T06:11:20.242307+00:00'
exported_at: '2026-09-17T06:11:24.105969+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber
structured_data:
  about: []
  author: ''
  description: We’re introducing new Gemini models, including Gemini 3.6 Flash, 3.5
    Flash-Lite and 3.5 Flash Cyber.
  headline: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-gemini-3-6-flash-3-5-flash-lite-and-3-5-flash-cyber
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber
updated_at: '2026-09-17T06:11:20.242307+00:00'
url_hash: fc06d851928020f79251f319f6dcf9ffb1b4e5a8
---

Developers and customers building production AI agents need higher token efficiency, lower latency, and more reliable performance. Our Flash series of models is built to meet the sweet spot of efficiency and quality to enable scaling agentic workflows. Building on Gemini 3.5 Flash, we’re introducing new Gemini models:

* **3.6 Flash:**
  Our workhorse model that delivers better coding, knowledge work, and multimodal performance. According to the
  [Artificial Analysis Index](https://artificialanalysis.ai/models/gemini-3-6-flash)
  , it reduces output token usage by 17% compared to 3.5 Flash, and in some benchmarks like DeepSWE by
  [Datacurve](https://deepswe.datacurve.ai/)
  , we observe up to 65%, all at a lower cost per output token.
* **3.5 Flash-Lite:**
  Our fastest, most cost-effective 3.5-class model, delivering 350 output tokens per second according to the Artificial Analysis Index, also significantly outperforming prior Flash-Lite generations in agentic workflows.
* **3.5 Flash Cyber in CodeMender:**
  Successful cybersecurity applications require careful orchestration of a model alongside an agent infrastructure. We’re introducing a combination of a new, highly efficient, specialized cyber-focused model paired with our CodeMender code security agent that delivers competitive performance at the frontier.

Beyond today’s releases, Gemini 3.5 Pro is currently testing with partners and we plan to make it broadly available as soon as it’s ready. In parallel, our team is already focusing on building the next generation of models. We have started our most ambitious pre-training run yet, for Gemini 4, and are excited by the progress.

## 3.6 Flash: More efficient and better quality than 3.5 Flash

Gemini 3.6 Flash builds directly on developer and customer feedback from 3.5 Flash. 3.6 Flash not only delivers a step up in coding and knowledge work, but it does this while meaningfully improving token efficiency. For example, on the Artificial Analysis Index, we see 3.6 Flash consuming 17% fewer output tokens than 3.5 Flash. It also takes fewer reasoning steps and tool calls to accomplish multi-step workflows.

This enhanced efficiency is also combined with a lower price than 3.5 Flash. At $1.50/1M input tokens and $7.50/1M output tokens, 3.6 Flash reduces the overall cost per agentic task, making agents more cost-effective to build and run.