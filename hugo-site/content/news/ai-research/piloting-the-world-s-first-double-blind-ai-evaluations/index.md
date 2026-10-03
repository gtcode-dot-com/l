---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-03T04:43:16.281069+00:00'
exported_at: '2026-10-03T04:43:19.789030+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations
structured_data:
  about: []
  author: ''
  description: Building trust in proprietary model benchmarks using cryptographically
    secure environments
  headline: Piloting the world's first double-blind AI evaluations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/piloting-the-worlds-first-double-blind-ai-evaluations
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Piloting the world's first double-blind AI evaluations
updated_at: '2026-10-03T04:43:16.281069+00:00'
url_hash: 213e95424861a758fb5dff596fcf41d7548e7662
---

Building trust in proprietary model benchmarks using cryptographically secure environments

Imagine a student is set to take a high-stakes exam. If they accidentally peek at the test questions in advance, achieving a perfect score is influenced by this knowledge, making it a meaningless accomplishment. To truly measure what they know, they must have no visibility of the test questions until it's time to take the exam. That is the exact challenge the industry faces when evaluating advanced AI models. If a model has already seen the test questions - a problem known as benchmark contamination - the results can only be trusted to an extent.

Today, weâre introducing the
**worldâs first double-blind evaluation of a proprietary, frontier class AI model,**
which keeps external evaluations confined to a cryptographic âboxâ where they canât be used by models later to optimize performance ahead of testing. We're partnering with the Singapore AI Safety Institute, OpenMined, AVERI, and
[MLCommons](https://mlcommons.org/2026/08/double-blind-reliability-evaluation/)
, to test a Gemini Flash Lite model against confidential benchmarks in a
[privacy-preserving environment](https://cloud.google.com/blog/products/identity-security/verifiable-trust-in-the-ai-era-whats-new-in-confidential-computing)
, increasing evaluation integrity.

At Google, we assess our AI systems using a broad spectrum of evaluations throughout model development and deployment, but we donât rely on internal testing alone. To identify potential blindspots, we work with a diverse group of external partners, including specialized research labs, civil society and national AI Safety and Security Institutes (AISIs), using their unique expertise to stress-test our models.

As AI models become more capable, ensuring the model has not seen the test questions or prompts in advance is critical, as this can skew the results. Policymakers, researchers, and enterprises need to trust that AI benchmarks accurately reflect a model's true capabilities and safety, but if models are able to âpeekâ at the evaluation questions in advance, it can artificially inflate scores and undermine this trust.

Although zero-logging protocols and rigorous contractual safeguards have long kept external test prompts confidential, incorporating technical and cryptographic safeguards marks a major step forward in secure model evaluation.

## How double-blind evaluations work