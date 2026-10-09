---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-08T07:59:51.231193+00:00'
exported_at: '2026-10-08T07:59:57.908862+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model
structured_data:
  about: []
  author: ''
  description: Introducing EmbeddingGemma 2, an open multimodal embedding model optimized
    for privacy-first use cases
  headline: 'EmbeddingGemma 2: an open, lightweight multimodal embedding model'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/embeddinggemma-2-an-open-lightweight-multimodal-embedding-model
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'EmbeddingGemma 2: an open, lightweight multimodal embedding model'
updated_at: '2026-10-08T07:59:51.231193+00:00'
url_hash: 2435ebd74585591829f3cd36a5ccda2903dc2ac2
---

We introduced
[EmbeddingGemma](https://developers.googleblog.com/en/introducing-embeddinggemma/)
last year to provide a lightweight option for high-quality text embeddings, to help your apps organize, search, and connect information directly on consumer hardware. The developer community’s response blew past our expectations. With more than 20 million downloads, builders have used it to power smarter on-device search tools and privacy-first retrieval augmented generation (RAG) pipelines.

Today, we’re launching EmbeddingGemma 2
**,**
expanding beyond text to unify code, images, video, and audio in a shared embedding space. Built on the Gemma 4 architecture and released under a commercially permissive Apache 2.0 license, EmbeddingGemma 2 has 740 million parameters, making it optimal for on-device inference. It can help find a specific video clip from a voice memo, or search through hours of audio recordings based on a text query, all processed by a single, natively multimodal model.