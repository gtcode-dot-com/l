---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-23T16:15:47.653352+00:00'
exported_at: '2026-04-23T16:15:49.923002+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/decoupled-diloco
structured_data:
  about: []
  author: ''
  description: Google’s new distributed architecture keeps AI training runs on track
    across distant data centers, with exceptional efficiency – even when hardware
    fails.
  headline: 'Decoupled DiLoCo: A new frontier for resilient, distributed AI training'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/decoupled-diloco
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Decoupled DiLoCo: A new frontier for resilient, distributed AI training'
updated_at: '2026-04-23T16:15:47.653352+00:00'
url_hash: 246f49f1cf279c7ab06d4bafa3cfc32c2fbfd7ed
---

Decoupled DiLoCo is not only more resilient to failures, but is also practical for executing production-level, fully distributed pre-training. We successfully trained a 12 billion parameter model across four separate U.S. regions using 2-5 Gbps of wide-area networking (a level relatively achievable using existing internet connectivity between datacenter facilities, rather than requiring new custom network infrastructure between facilities). Notably, the system achieved this training result more than 20 times faster than conventional synchronization methods. This is because our system incorporates required communication into longer periods of computation, avoiding the "blocking" bottlenecks where one part of the system must wait for another.

## Driving the evolution of AI training infrastructure

At Google, we take a full-stack approach to AI training, spanning hardware, software infrastructure and research. Increasingly, gains are coming from rethinking how these layers fit together.

Decoupled DiLoCo is one example. By enabling training jobs at internet-scale bandwidth, it can tap any unused compute wherever it sits, turning stranded resources into useful capacity.

Beyond efficiency and resilience, this training paradigm also unlocks the ability to mix different hardware generations, such as TPU v6e and TPU v5p, in a single training run. This approach not only extends the useful life of existing hardware, but also increases the total compute available for model training. In our experiments, chips from different generations running at different speeds still matched the ML performance of single-chip-type training runs, ensuring that even older hardware can meaningfully accelerate AI training.

What’s more, because new generations of hardware don’t arrive everywhere all at once, being able to train across generations can alleviate recurring logistical and capacity bottlenecks.

As we push the frontiers of AI infrastructure today, we’re continuing to explore approaches to resilient systems needed to unlock the next generation of AI.