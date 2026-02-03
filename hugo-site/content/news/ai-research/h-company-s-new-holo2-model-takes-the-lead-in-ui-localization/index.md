---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-03T18:15:32.168834+00:00'
exported_at: '2026-02-03T18:15:34.337642+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/Hcompany/introducing-holo2-235b-a22b
structured_data:
  about: []
  author: ''
  description: A Blog post by H company on Hugging Face
  headline: H Company's new Holo2 model takes the lead in UI Localization
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/Hcompany/introducing-holo2-235b-a22b
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: H Company's new Holo2 model takes the lead in UI Localization
updated_at: '2026-02-03T18:15:32.168834+00:00'
url_hash: 2e3c21398d9ca5336b56158aad950aa3ce71b4c6
---

# H Company's new Holo2 model takes the lead in UI Localization

Two months since releasing our first batch of Holo2 models, H Company is back with our largest UI localization model yet:
**Holo2-235B-A22B Preview**
. This model achieves a new State-of-the-Art (SOTA) record of 78.5% on
[Screenspot-Pro](https://gui-agent.github.io/grounding-leaderboard/)
and 79.0% on OSWorld G.

Available on
[Hugging Face](https://huggingface.co/Hcompany/Holo2-235B-A22B)
, Holo2-235B-A22B Preview is a research release focused on UI element localization.

[![benchmark_table_light (3)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/5dezFBy4-KimAIQR5_1j1.png)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/5dezFBy4-KimAIQR5_1j1.png)

**Agentic Localization**

High-resolution 4K interfaces are challenging for localization models. Small UI elements can be difficult to pinpoint on a large display. With agentic localization, however, Holo2 can iteratively refine its predictions, improving accuracy with each step and unlocking 10-20% relative gains across all Holo2 model sizes.

**Holo2-235B-A22B's Performance on ScreenSpot-Pro**

Holo2-235B-A22B Preview reaches 70.6% accuracy on ScreenSpot-Pro in a single step. In agent mode, it achieves 78.5% within 3 steps, setting a new state-of-the-art on the most challenging GUI grounding benchmark.

[![cost_perf_screenspot_pro_light (2)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/nht6cib9ua4mfPcM2C1I1.png)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/nht6cib9ua4mfPcM2C1I1.png)