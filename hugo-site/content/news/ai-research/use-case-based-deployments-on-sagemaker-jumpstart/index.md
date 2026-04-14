---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-14T18:15:47.023373+00:00'
exported_at: '2026-04-14T18:15:50.072970+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/use-case-based-deployments-on-sagemaker-jumpstart
structured_data:
  about: []
  author: ''
  description: We're excited to announce the launch of Amazon SageMaker JumpStart
    optimized deployments. SageMaker JumpStart improved deployments address the need
    for rich and straightforward deployment customization on SageMaker JumpStart by
    offering pre-defined deployment configurations, designed for specific use cases.
    Customer...
  headline: Use-case based deployments on SageMaker JumpStart
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/use-case-based-deployments-on-sagemaker-jumpstart
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Use-case based deployments on SageMaker JumpStart
updated_at: '2026-04-14T18:15:47.023373+00:00'
url_hash: a4ddcaf3bef3001abfbeaa423b264d92f6ffaa3e
---

[Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/ai/jumpstart/)
provides pretrained models for a wide range of problem types to help you get started with AI workloads. SageMaker JumpStart offers access to solutions for top use cases that can be deployed to
[SageMaker AI Managed Inference](https://aws.amazon.com/sagemaker/ai/deploy/)
endpoints or
[SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
clusters. Through pre-set deployment options, customers can quickly move from model selection to model deployment.

Model deployments through SageMaker JumpStart are fast and straightforward. Customers could select options based on expected concurrent users, with visibility into P50 latency, time-to-first token (TTFT), and throughput (token/second/user). While concurrent user configuration options are helpful for general-purpose scenarios, they aren’t task-aware, and we recognize that customers use SageMaker JumpStart for diverse, specific use cases like content generation, content summarization, or Q&A. Each use case might require specific configurations to improve performance. Moreover, the definition of
*performance*
isn’t constrained to just latency, and some customers might measure performance in throughput or lowest cost per token.

Building on this foundation, we’re excited to announce the launch of SageMaker JumpStart optimized deployments. SageMaker JumpStart improved deployments address the need for rich and straightforward deployment customization on SageMaker JumpStart by offering pre-defined deployment configurations, designed for specific use cases. Customers maintain the same level of visibility into the details of their proposed deployments, but now deployments are optimized for their specific use case and performance constraint.

## Prerequisites

To begin using SageMaker JumpStart optimized deployments, customers require at minimum the following:

After these features are in place, customers can begin using SageMaker JumpStart optimized deployments right away.

## Getting started

To get started using SageMaker JumpStart optimized deployments, open SageMaker Studio and choose
**Models**
. Select any of the models that support optimized deployments (listed in the following section) and choose
**Deploy**
in the top-right corner. The resulting screen now features a collapsible window labeled “Performance”, which features the selection options for optimized deployments.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/27/flash-3087-image-1.png)

The displayed options require users to first select a use case. For text-based models, these use cases can range from generative writing to chat-style interactions; image and video will feature different use cases after support is added for those input types. After selecting a use case, customers must select one of three constraint optimizations:
*Cost optimized*
,
*Throughput optimized*
, and
*Latency optimized*
. There is also a
*Balanced*
option for customers looking for the best average performance across all logged metrics.

After selected, a pre-set deployment configuration is defined for the endpoint. Customers can further review and select additional configuration values like timeouts, endpoint naming, and security settings. After configuration is complete, customers choose the
**Deploy**
option in the bottom-right corner.

## Available models

SageMaker JumpStart optimized deployments are available for the following models:

* Meta
  + Llama-3.1-8B-Instruct
  + Llama-2-7b-hf
  + Llama-3.2-3B
  + Meta-Llama-3-8B
  + Llama-3.2-1B-Instruct
  + Llama-3.2-1B
  + Llama-3.1-70B-Instruct
  + Llama-3.2-3B-Instruct
  + Meta-Llama-3-8B
* Microsoft
* Mistral AI
  + Mistral-7B-Instruct-v0.2
  + Mistral-Small-24B-Instruct-2501
  + Mistral-7B-v0.1
  + Mistral-7B-Instruct-v0.3
  + Mixtral-8x7B-Instruct-v0.1
* Qwen
  + Qwen3-8B
  + Qwen3-32B
  + Qwen3-0.6B
  + Qwen2.5-7B-Instruct
  + Qwen2.5-72B-Instruct
  + Qwen2-VL-7B-Instruct
  + Qwen2-1.5B-Instruct
  + Qwen2-7B
* Google
  + gemma-7b
  + gemma-7b-it
  + gemma-2b
* Tiiuae

These are the launch models for optimized deployments, and we’re actively expanding support to include additional models.

## Call to action

Customers can start working with SageMaker JumpStart optimized deployments immediately. Select one of the available optimized deployment models in the SageMaker Studio model hub. Experiment with the different deployment options to determine the right configuration for your application.

---

## About the authors

### Dan Ferguson

Dan Ferguson is a Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

### Malav Shastri

[Malav Shastri](https://www.linkedin.com/in/malav-shastri)
is a Software Development Engineer at AWS, where he works on the Amazon SageMaker JumpStart and Amazon Bedrock teams. His role focuses on enabling customers to take advantage of state-of-the-art open source and proprietary foundation models and traditional machine learning algorithms. Malav holds a Master’s degree in Computer Science.

### Pooja Karadgi

Pooja Karadgi leads product and strategic partnerships for Amazon SageMaker JumpStart, the machine learning and generative AI hub within SageMaker. She is dedicated to accelerating customer AI adoption by simplifying foundation model discovery and deployment, enabling customers to build production-ready generative AI applications across the entire model lifecycle – from onboarding and customization to deployment.