---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-26T22:51:52.096424+00:00'
exported_at: '2026-03-26T22:51:56.070650+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/ibm-granite/granite-libraries
structured_data:
  about: []
  author: ''
  description: A Blog post by IBM Granite on Hugging Face
  headline: What's New in Mellea 0.4.0 + Granite Libraries Release
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/ibm-granite/granite-libraries
  publisher:
    logo: /favicon.ico
    name: GTCode
title: What's New in Mellea 0.4.0 + Granite Libraries Release
updated_at: '2026-03-26T22:51:52.096424+00:00'
url_hash: 952cb115c7d656f1469d4fb536a7c7be157d0553
---

# What's New in Mellea 0.4.0 + Granite Libraries Release

We have released
[**Mellea 0.4.0**](https://github.com/generative-computing/mellea/releases/tag/v0.4.0)
alongside three
[Granite Libraries](https://huggingface.co/collections/ibm-granite/granite-libraries)
:
[granitelib-rag-r1.0](https://huggingface.co/ibm-granite/granitelib-rag-r1.0)
,
[granitelib-core-r1.0](https://huggingface.co/ibm-granite/granitelib-core-r1.0)
,
[granitelib-guardian-r1.0](https://huggingface.co/ibm-granite/granitelib-guardian-r1.0)
. Together, these releases make it easier to build structured, verifiable, and safety-aware AI workflows on top of IBM Granite models.

Mellea is an open-source Python library for writing generative programs -- replacing probabilistic prompt behavior with structured, maintainable AI workflows. Unlike general-purpose orchestration frameworks, Mellea is designed to make LLM-based programs maintainable and predictable through constrained decoding, structured repair loops, and composable pipelines
*(New to Mellea? Start with our
[introductory blog](https://www.ibm.com/think/news/how-generative-computing-reinvent-software)
and
[meet the team](https://research.ibm.com/blog/interview-with-mellea-lead-engineers)
)*

---

## Mellea 0.4.0

Mellea 0.4.0 is the latest release of an open-source research project initiated and developed by IBM Research. Building on 0.3.0 foundational libraries and workflow primitives, 0.4.0 expands the library's integration surface and introduces new architectural patterns for structuring generative workflows.

What’s included:

* Native integration with the Granite Libraries, offering a standardized API that relies on constrained decoding to guarantee schema correctness.
* Instruct-validate-repair pattern via rejection sampling strategies
* Observability hooks for event-driven callbacks to monitor and track workflows

See full list of Mellea 0.4.0 features and updates
[here](https://github.com/generative-computing/mellea/releases/tag/v0.4.0)

---

## What Are the Granite Libraries

Simply put, a Granite Library is a collection of specialized model adapters designed to perform well-defined operations on portions of an input chain or conversation. Rather than relying on general-purpose prompting, each specialized model is fine-tuned for a specific task such as query rewriting, hallucination detection, or policy compliance checking. The use of specialized adapters allows us to increase the accuracy of each task at a modest parameter count cost, and without disrupting the base model’s capabilities.

Three libraries are being released today for the granite-4.0-micro model, each targeting a distinct set of pipeline tasks and comprised of a collection of LoRA adapters:

* [Granitelib-core-r1.0](https://huggingface.co/ibm-granite/granitelib-core-r1.0)
  : targeting the step of requirements validation in Mellea’s instruct-validate-repair loop
* [Granitelib-rag-r1.0](https://huggingface.co/ibm-granite/granitelib-rag-r1.0)
  : targeting a variety of tasks in agentic RAG pipelines covering pre-retrieval, post-retrieval, and post-generation
* [Granitelib-guardian-r1.0](https://huggingface.co/ibm-granite/granitelib-guardian-r1.0)
  : specialized models for safety, factuality, and policy compliance

Mellea 0.4.0 is the latest release of an open-source research project initiated and developed by IBM Research. Building on the foundational libraries and workflow primitives introduced in 0.3.0, this release expands the integration surface and introduces new architectural patterns for structuring generative workflows.

---

## Getting Started

### Mellea

### Granite Libraries

### Learn More