---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-09T02:58:47.233593+00:00'
exported_at: '2026-06-09T02:58:49.649084+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/JetBrains/mellum2-launch
structured_data:
  about: []
  author: ''
  description: A Blog post by JetBrains on Hugging Face
  headline: 'Introducing Mellum2: A 12B Mixture-of-Experts Model by JetBrains'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/JetBrains/mellum2-launch
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Introducing Mellum2: A 12B Mixture-of-Experts Model by JetBrains'
updated_at: '2026-06-09T02:58:47.233593+00:00'
url_hash: 2995ca1c3636d92f482be20355930ccccbca56a0
---

# Introducing Mellum2: A 12B Mixture-of-Experts Model by JetBrains

![Mellum Logo]()

* Mellum2 is a 12B-parameter Mixture-of-Experts model trained from scratch on natural language and code.
* The model activates only 2.5B parameters per token, making it efficient for high-throughput, low-latency inference.
  Mellum2 is can be used for routing, RAG, summarization, sub-agents, high-throughput coding features, and private deployments.
* It is released under the Apache 2.0 license.
* Compared with similar-sized models, Mellum2 delivers competitive benchmark performance while achieving more than 2x faster inference.
* Download the model on Hugging Face:
  &lt;https://huggingface.co/collections/JetBrains/mellum-2&gt;
* For architecture details, training setup, benchmarks, and evaluation methodology, read the full technical report:
  &lt;https://arxiv.org/pdf/2605.31268&gt;

Today we’re releasing Mellum2, an open Mixture-of-Experts model optimized for low-latency text-and-code workloads.
Mellum originally started as a code completion model. With Mellum2, we extend that foundation to a broader set of natural language and software engineering tasks while keeping the model focused on efficient inference and deployability.
Modern AI systems increasingly rely on multiple model calls: routing, retrieval, summarization, planning, validation, and tool use. Many of these operations are latency-sensitive and do not require the largest available model.
Mellum2 targets these workloads.

## Benchmark highlights

[![Mellum 2 Evals](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking/resolve/main/mellum_evals_grid_1700.jpg)](https://huggingface.co/JetBrains/Mellum2-12B-A2.5B-Thinking/resolve/main/mellum_evals_grid_1700.jpg)

In our technical report, we evaluate Mellum2 across code generation, reasoning, science, and math benchmarks.
Mellum2 is competitive with similarly sized open models while delivering more than 2x faster inference, making it suitable for high-throughput production workloads.
Model architecture
Mellum2 is a Mixture-of-Experts model:

| Model | Total parameters | Active parameters per token | Modality | License |
| --- | --- | --- | --- | --- |
| Mellum2 | 12B | 2.5B | Text and code | Apache 2.0 |

The MoE architecture keeps total model capacity high while activating only a subset of parameters for each token. This makes inference more efficient and helps reduce serving cost for real-time workloads.
Mellum2 is intentionally focused on text and code rather than multimodal tasks. This specialization keeps the model compact and efficient for software engineering workloads.

## Key use cases

### Routing and orchestration

Mellum2 works well as a lightweight routing and orchestration model in multi-model systems, including prompt classification, tool selection, and intermediate control-flow steps.

### RAG pipelines

The model is well suited for latency-sensitive retrieval pipelines, including context compression, summarization, and retrieval post-processing.

### Sub-agents

Mellum2 can be used for agent subtasks such as planning, validation, transformation, and context preparation, reducing the need to invoke larger models for intermediate operations.

### Private deployment

Because Mellum2 is open and efficient to serve, it can be deployed in self-hosted environments involving proprietary code or internal data.

## Why well-scoped models matter

As AI systems mature, the most effective architectures are becoming less monolithic.
A single frontier model can be powerful, but production systems often need several specialized components working together: retrievers, routers, code-aware models, validators, tool callers, and larger reasoning models.
We think of Mellum2 as a “focal” model: a fast, well-scoped model optimized for high-frequency tasks inside larger AI systems.
The goal is not to replace every model in the stack. The goal is to make the stack faster, cheaper, and easier to control.

## Getting started with Mellum2

If you are building AI systems for software engineering – inside an IDE, in a RAG pipeline, as part of an agent workflow, or on private infrastructure – Mellum2 is
[ready to try](https://huggingface.co/collections/JetBrains/mellum-2)
.