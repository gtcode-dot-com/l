---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T08:15:42.595374+00:00'
exported_at: '2026-04-02T08:15:44.798133+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/Hcompany/holo3
structured_data:
  about: []
  author: ''
  description: A Blog post by H company on Hugging Face
  headline: 'Holo3: Breaking the Computer Use Frontier'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/Hcompany/holo3
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Holo3: Breaking the Computer Use Frontier'
updated_at: '2026-04-02T08:15:42.595374+00:00'
url_hash: e88aa7265188590771353f79737d7086107d0fd9
---

# Holo3: Breaking the Computer Use Frontier

[![image](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/KOOvyPp6fsa2E-S9C80lv.png)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/KOOvyPp6fsa2E-S9C80lv.png)

We are proud to unveil
**Holo3**
, the latest evolution of our vision for the Autonomous Enterprise. With a score of
**78.85% on the OSWorld-Verified benchmark**
, Holo3-122B-A10B establishes a new state of the art for the industry on the leading desktop computer use benchmark.

Holo3 is more than a benchmark leader; it is engineered for production. Built using our agentic flywheel, it has been trained to execute real-world workflows within synthetic enterprise environments. This not only ensures that Holo3 excels in today's business scenarios, but establishes the foundation for a future where our agents can autonomously navigate virtually any digital landscape.

Best of all, Holo3 achieves this with only 10B active parameters (122B total), so at a fraction of the cost of large-scale proprietary models, such as GPT 5.4 or Opus 4.6. All models are available through our
[Inference API](https://hcompany.ai/holo-models-api)
. Holo3-35B-A3B weights are openly accessible on
[Hugging Face](https://huggingface.co/Hcompany/Holo3-35B-A3B)
under the Apache2 license and freely accessible through our inference API under a free tier.

## The Agentic Learning Flywheel

What sets Holo3 apart is its specialized training pipeline—a continuous feedback loop designed to sharpen two core agentic pillars:
**perception**
and
**decision-making**
.

Our training flywheel is about teaching our model from annotated examples how to execute specific tasks, all while developing generalist skills across a virtually infinite variety of user interfaces. Here is how we build world-class computer use models:

* **Synthetic Navigation Data:**
  using human and generated instructions, we generate scenario-specific navigation examples.
* **Out-of-Domain Augmentation:**
  we programmatically extend the scenarios and augment the data to ensure Holo3 can handle the unexpected.
* **Curated Reinforcement Learning:**
  every data sample is carefully curated and ingested through a pipeline that leverages advanced data filtering and reinforcement learning to maximize performance.

Beyond the raw scores, the OSWorld results serve as a definitive proof-of-concept for our learning flywheel. To validate its transferability to real-world business applications we created the
**Synthetic Environment Factory**
.

## The Synthetic Environment Factory & H Corporate Benchmarks

This proprietary factory reproduces the reality of enterprise systems and is one of the training gyms Holo3 was forged in. Our environments are automatically built using coding agents that program websites from scratch based on scenario specifications, producing verifiable tasks of varying difficulty that are validated end-to-end with verification scripts.

To measure real-world readiness, we also designed
*H Corporate Benchmarks*
, a dedicated evaluation suite of 486 multi-step realistic tasks spanning 4 categories: E-commerce, Business software, Collaboration, and various Multi-App setups.

The benchmark spans the full complexity spectrum: from focused, single-application tasks to long-horizon, multi-application workflows that mirror how work actually gets done. At the harder end of the scale (Multi-Apps), tasks require the agent to coordinate information across multiple systems simultaneously—for example, retrieving equipment prices from a PDF, cross-referencing them against each employee's remaining budget, and autonomously sending personalised approval or rejection emails to every individual. This kind of task demands not only accurate calculation and document parsing, but sustained multi-step reasoning across applications without losing state or intent.

*Examples of synthetic environments created for training Holo3*
[![image](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/FjQXRkHqmzy4yfy2TBHDZ.png)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/FjQXRkHqmzy4yfy2TBHDZ.png)

In our results below, we see Holo3 surpassing its competitors on single application benchmarks. The performance difference between Holo3 and the base Qwen3.5 models reflects the impact of our agentic learning flywheel. By achieving higher success rates than models with significantly larger parameter counts—while maintaining the same localization and grounding standards—Holo3 illustrates the true magnitude of this specialized training.

[![image](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/xo_YqyqgtK_voRmvraVH1.png)](https://cdn-uploads.huggingface.co/production/uploads/698224a939bac08a1b6e0488/xo_YqyqgtK_voRmvraVH1.png)

## Towards Universal Agency

Holo3 is a milestone, but it is not the destination. By building a system that can see, reason, and act within our clients digital platform, we are making the
**Autonomous Enterprise**
a reality.

As our "Synthetic Environment Factory" continues to evolve, our agents are learning to handle increasingly more intricate tasks. While Holo3 today masters the interface, we are already at work on the next frontier:
**Adaptive Agency**
, where our models will not only use the tools they know but autonomously learn to navigate entirely new, bespoke enterprise software in real-time.