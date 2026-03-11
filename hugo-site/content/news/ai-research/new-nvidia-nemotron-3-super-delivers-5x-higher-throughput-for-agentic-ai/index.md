---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-11T18:15:35.592872+00:00'
exported_at: '2026-03-11T18:15:38.215962+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai
structured_data:
  about: []
  author: ''
  description: A new, open, 120-billion-parameter hybrid mixture-of-experts model
    optimized for NVIDIA Blackwell addresses the costs of long thinking and context
    explosion that slow autonomous agent workflows.
  headline: New NVIDIA Nemotron 3 Super Delivers 5x Higher Throughput for Agentic
    AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New NVIDIA Nemotron 3 Super Delivers 5x Higher Throughput for Agentic AI
updated_at: '2026-03-11T18:15:35.592872+00:00'
url_hash: 51cbf24b7b8cec6ea79ea1b5c9cbaf86262764e4
---

Launched today, NVIDIA Nemotron 3 Super is a 120‑billion‑parameter open model with 12 billion active parameters designed to run complex agentic AI systems at scale.

Available now, the model combines advanced reasoning capabilities to efficiently complete tasks with high accuracy for autonomous agents.

**AI-Native Companies:**

Perplexity

offers its users access to Nemotron 3 Super for search and as one of 20 orchestrated models in Computer. Companies offering software development agents like
[CodeRabbit](https://www.coderabbit.ai/blog/faster-code-reviews-with-nemotron-3-super)

,

Factory

and
[Greptile](http://greptile.com/blog/nvidia-nemotron-super-in-code-review)

are integrating the model into their AI agents along with proprietary models to achieve higher accuracy at lower cost. And life sciences and frontier AI organizations like

Edison Scientific

and

Lila Sciences

will power their agents for deep literature search, data science and molecular understanding.

**Enterprise Software Platforms:**

Industry leaders such as

Amdocs

,

Palantir

,

Cadence

,

Dassault Systèmes

and
[Siemens](https://www.siemens.com/en-us/products/fuse-eda-ai-system/)

are deploying and customizing the model to automate workflows in telecom, cybersecurity, semiconductor design and manufacturing.

As companies move beyond chatbots and into multi‑agent applications, they encounter two constraints.

The first is context explosion. Multi‑agent workflows generate up to
[15x more](https://www.anthropic.com/engineering/multi-agent-research-system)

tokens than standard chat because each interaction requires resending full histories, including tool outputs and intermediate reasoning.

Over long tasks, this volume of context increases costs and can lead to goal drift, where agents lose alignment with the original objective.

The second is the thinking tax. Complex agents must reason at every step, but using large models for every subtask makes multi-agent applications too expensive and sluggish for practical applications.

Nemotron 3 Super has a 1‑million‑token context window, allowing agents to retain full workflow state in memory and preventing goal drift.





Nemotron 3 Super has set new standards, claiming the top spot on Artificial Analysis for efficiency and openn

ess with leading accuracy among models of the same size.

The model also powers the
[NVIDIA AI-Q](https://build.nvidia.com/nvidia/aiq)

research agent to the No. 1 position on
[DeepResearch Bench](https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard)

and
[DeepResearch Bench II](https://agentresearchlab.com/benchmarks/deepresearch-bench-ii/index.html#leaderboard)

leaderboards, benchmarks that measure an AI system’s ability to conduct thorough, multistep research across large document sets while maintaining reasoning coherence.

## **Hybrid Architecture**

Nemotron 3 Super uses a hybrid mixture‑of‑experts (MoE) architecture that combines three major innovations to deliver up to

5x higher throughput

and up to

2x higher accuracy

than the previous Nemotron Super model.

* **Hybrid Architecture:**

  Mamba layers deliver

  4x higher memory and compute efficiency,

  while transformer layers drive advanced reasoning.
* **MoE:**

  Only 12 billion of its 120 billion parameters are active at inference.
* **Latent MoE:**

  A new technique that improves accuracy by activating four expert specialists for the cost of one to generate the next token at inference.
* **Multi-Token Prediction:**

  Predicts multiple future words simultaneously, resulting in

  3x faster inference

  .

On the NVIDIA Blackwell platform, the model runs in NVFP4 precision. That cuts memory requirements and pushes inference up to

4x faster than

FP8 on NVIDIA Hopper, with no loss in accuracy.

## **Open Weights, Data and Recipes**

NVIDIA is releasing Nemotron 3 Super with open weights under a permissive license. Developers can deploy and customize it on workstations, in data centers or in the cloud.

The model was trained on synthetic data generated using frontier reasoning models. NVIDIA is publishing the complete methodology, including over 10 trillion tokens of pre- and post-training datasets, 15 training environments for reinforcement learning and evaluation recipes. Researchers can further use the NVIDIA NeMo platform to fine-tune the model or build their own.

## **Use in Agentic Systems**

Nemotron 3 Super is designed to handle complex subtasks inside a multi-agent system.

A software development agent can load an entire codebase into context at once, enabling end-to-end code generation and debugging without document segmentation.

In financial analysis it can load thousands of pages of reports into memory,  eliminating the need to re-reason across long conversations, which improves efficiency.

Nemotron 3 Super has high-accuracy tool calling that ensures autonomous agents reliably navigate massive function libraries to prevent execution errors in high-stakes environments, like autonomous security orchestration in cybersecurity

.

## **Availability**

NVIDIA Nemotron 3 Super, part of the
[Nemotron 3 family](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)

, can be accessed at
[build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-3-super-120b-a12b)

,
[Perplexity](http://perplexity.ai)

,
[OpenRouter](https://openrouter.ai/nvidia/nemotron-3-super-120b-a12b:free)

and
[Hugging Face](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Super-120B-A12B-FP8)

. Dell Technologies is bringing the model to the Dell Enterprise Hub on Hugging Face, optimized for on-premise deployment on the Dell AI Factory, advancing multi-agent AI workflows.
[HPE](https://community.hpe.com/t5/the-cloud-experience-everywhere/operationalizing-agentic-ai-with-nvidia-nemotron-and-hpe-agents/ba-p/7262654)

is also bringing NVIDIA Nemotron to its agents hub to help ensure scalable enterprise adoption of agentic AI.

Enterprises and developers can deploy the model through several partners:

* **Cloud Service Providers**
  :

  Google Cloud’s Vertex AI

  and

  Oracle Cloud Infrastructure,

  and coming soon to

  Amazon Web Services through Amazon Bedrock as well as Microsoft Azure.
* **NVIDIA Cloud Partners**
  :

  Coreweave

  ,
  [Crusoe](https://www.crusoe.ai/cloud/managed-inference)

  ,
  [Nebius](https://nebius.com/blog/posts/nemotron3-super-now-available)

  and
  [Together AI](https://www.together.ai/blog/nvidia-nemotron-3-super)

  .
* **Inference Service Providers**
  :
  [Baseten](https://www.baseten.co/blog/introducing-nemotron-3-super)

  ,
  [CloudFlare](https://developers.cloudflare.com/changelog/post/2026-03-11-nemotron-3-super-workers-ai)
  ,
  [DeepInfra](https://deepinfra.com/blog/nvidia-nemotron-3-super-release)

  ,
  [Fireworks AI

  ,](https://app.fireworks.ai/models/fireworks/nvidia-nemotron-3-super-120b-a12b-fp8)
  [Inference.net](http://inference.net/blog/nemotron-finetuning)

  ,
  [Lightning AI](https://lightning.ai/nvidia-nemotron-3-super)

  ,
  [Modal](https://modal.com/docs/examples/nemotron_inference)

  and
  [FriendliAI](https://friendli.ai/blog/nvidia-nemotron-3-super)

  .
* **Data Platforms and Services**
  :

  Distyl,

  Dataiku

  ,

  DataRobot

  ,

  Deloitte

  ,

  EY

  and

  Tata Consultancy Services.

The model is packaged as an
[NVIDIA NIM](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/)

microservice, allowing deployment from on-premises systems to the cloud.

*Stay up to date on agentic AI, NVIDIA*
[*Nemotron*](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
*and more by subscribing to*
[*NVIDIA AI news*](https://www.nvidia.com/en-us/executive-insights/generative-ai-tools/?modal=stay-inf)
*,*
[*joining the community*](https://developer.nvidia.com/community)
*, and following NVIDIA AI on*
[*LinkedIn*](https://www.linkedin.com/showcase/nvidia-ai/posts/?feedView=all)
*,*
[*Instagram*](https://www.instagram.com/nvidiaai/?hl=en)
*,*
[*X*](https://x.com/NVIDIAAIDev)
*and*
[*Facebook*](https://www.facebook.com/NVIDIAAI)
*.*

*Explore*
[*self-paced video tutorials and livestreams*](https://youtube.com/playlist?list=PL5B692fm6--vdRKB14FImVi7MTJ77zjn4&feature=shared)
*.*