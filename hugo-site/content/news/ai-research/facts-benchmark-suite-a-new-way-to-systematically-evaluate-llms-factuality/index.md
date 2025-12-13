---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-13T00:03:35.809630+00:00'
exported_at: '2025-12-13T00:03:38.994915+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models
structured_data:
  about: []
  author: ''
  description: 'The FACTS Benchmark Suite provides a systematic evaluation of Large
    Language Models (LLMs) factuality across three areas: Parametric, Search, and
    Multimodal reasoning.'
  headline: 'FACTS Benchmark Suite: Systematically evaluating the factuality of large
    language models'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/facts-benchmark-suite-systematically-evaluating-the-factuality-of-large-language-models
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'FACTS Benchmark Suite: Systematically evaluating the factuality of large language
  models'
updated_at: '2025-12-13T00:03:35.809630+00:00'
url_hash: 836bd477b0f6ea3052f5fb69a0a4003783b801f9
---

Large language models (LLMs) are increasingly becoming a primary source for information delivery across diverse use cases, so itâs important that their responses are factually accurate.

In order to continue improving their performance on this industry-wide challenge, we have to better understand the types of use cases where models struggle to provide an accurate response and better measure factuality performance in those areas.

## The FACTS Benchmark Suite

Today, weâre teaming up with Kaggle to introduce the
[FACTS Benchmark Suite](https://www.kaggle.com/benchmarks/google/facts/leaderboard)
. It extends our previous work developing the
[FACTS Grounding Benchmark](https://deepmind.google/blog/facts-grounding-a-new-benchmark-for-evaluating-the-factuality-of-large-language-models/)
, with three additional factuality benchmarks, including:

* A
  [**Parametric Benchmark**](https://www.kaggle.com/benchmarks/google/facts-parametric/leaderboard)
  that measures the modelâs ability to access its internal knowledge accurately in factoid question use-cases.
* A
  [**Search Benchmark**](https://www.kaggle.com/benchmarks/google/facts-search/leaderboard)
  that tests a modelâs ability to use Search as a tool to retrieve information and synthesize it correctly.
* A
  [**Multimodal Benchmark**](https://www.kaggle.com/benchmarks/google/facts-multimodal/leaderboard)
  that tests a modelâs ability to answer prompts related to input images in a factually correct manner.

We are also updating the original FACTS grounding benchmark with
[**Grounding Benchmark - v2**](https://www.kaggle.com/benchmarks/google/facts-grounding/leaderboard)
, an extended benchmark to test a modelâs ability to provide answers grounded in the context of a given prompt.

Each benchmark was carefully curated to produce a total of 3,513 examples, which we are making publicly available today. Similar to our previous release, we are following standard industry practice and keeping an evaluation set held-out as a private set. The FACTS Benchmark Suite Score (or FACTS Score) is calculated as the average accuracy of both public and private sets across the four benchmarks. Kaggle will oversee the management of the FACTS Benchmark Suite. This includes owning the private held-out sets, testing the leading LLMs on the benchmarks, and hosting the results on a public leaderboard. More details about the FACTS evaluation methodology can be found in our
[tech report](https://storage.googleapis.com/deepmind-media/FACTS/FACTS_benchmark_suite_paper.pdf)
.

## Benchmark overview

### Parametric Benchmark

The FACTS Parametric benchmark assesses the ability of models to accurately answer factual questions, without the aid of external tools like web search. All the questions in the benchmark are âtrivia styleâ questions driven by user interest that can be answered via Wikipedia (a standard source for LLM pretraining). The resulting benchmark consists of a 1052-item public set and a 1052-item private set.