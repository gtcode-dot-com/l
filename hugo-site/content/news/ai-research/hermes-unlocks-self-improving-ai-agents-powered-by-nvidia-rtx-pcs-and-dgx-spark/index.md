---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-14T21:17:12.694846+00:00'
exported_at: '2026-05-14T21:17:16.772661+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark
structured_data:
  about: []
  author: ''
  description: Reliable, self-evolving and powered by the newest agentic large language
    models, Hermes brings a new class of agents to NVIDIA RTX PCs and workstations.
  headline: Hermes Unlocks Self-Improving AI Agents, Powered by NVIDIA RTX PCs and
    DGX Spark
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/rtx-ai-garage-hermes-agent-dgx-spark
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Hermes Unlocks Self-Improving AI Agents, Powered by NVIDIA RTX PCs and DGX
  Spark
updated_at: '2026-05-14T21:17:12.694846+00:00'
url_hash: 8c006ef9dd8ac4144eb0f6c697004b15202ccc10
---

Agentic AI is changing the way users get work done. Following the success of
[OpenClaw](https://www.nvidia.com/en-us/ai/build-a-claw/)

, the community is embracing new open source agentic frameworks. The latest is
[Hermes Agent](https://github.com/nousresearch/hermes-agent)

, which crossed
[140,000 GitHub stars](https://github.com/nousresearch/hermes-agent)

in under three months and, as of last week, is the most used agent in the world according to
[OpenRouter](https://openrouter.ai/apps)

.

Developed by Nous Research, Hermes is designed for reliability and self-improvement — two qualities that have historically been hard to achieve with agents. It’s provider- and model-agnostic by design, and optimized for always-on local use, making
[NVIDIA RTX PCs](https://www.nvidia.com/en-us/ai-on-rtx/)

,
[NVIDIA RTX PRO workstations](https://www.nvidia.com/en-us/products/workstations/)

and
[NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

the ideal hardware to run it at full speed, around the clock.

Qwen 3.6, a new series of high-performance, open weight large language models (LLMs) from Alibaba, are ideal for running local agents like Hermes. The Qwen 3.6 27B and 35B parameter models are outperforming their previous-generation 120B and 400B parameter model counterparts and run on NVIDIA RTX and DGX Spark for accelerated agentic AI.

## **Hermes: Local AI Agent Capabilities Accelerated**

Like other popular agents, Hermes integrates with messaging apps, can access local files and applications, and runs 24/7. But four standout capabilities set it apart:

* **Self-Evolving Skills**

  : Hermes writes and refines its own skills. Every time the agent encounters a complex task or receives feedback, it saves its learnings as a skill so it can adapt and improve over time.
* **Contained Sub-Agents:**

  Hermes treats sub-agents as short-lived, isolated workers dedicated to a sub-task — with a focused context and set of tools. This keeps task organization tidy, minimizes confusion for the agent and allows Hermes to run with smaller context windows, which is ideal for local models.
* **Reliability by design:**

  Nous Research curates and stress-tests every skill, tool and plug-in that ships with Hermes. The result: Hermes just works — even with 30 billion-parameter-class local models — without the constant debugging that most other agent frameworks require.
* **Same model, better results:**

  Developer comparisons using identical models across frameworks consistently show stronger results in Hermes. The difference is the framework: Hermes is an active orchestration layer, not a thin wrapper, enabling persistent, on-device agents instead of task-by-task execution.

Both the Hermes agent and the underlying LLM are built to run locally — which means the quality of hardware directly determines the quality of a user’s experience. NVIDIA RTX GPUs are purpose-built for this kind of workload.

## **Qwen 3.6: Data Center-Level Intelligence, Locally**

The latest Qwen 3.6 models build on the acclaimed Qwen 3.5 series to deliver another leap forward for local AI agents. The new Qwen 3.6 35B model runs on roughly 20GB of memory while surpassing 120 billion-parameter models, which require 70GB+ of memory.

In addition, Qwen 3.6 27B is a new, dense model with more active parameters — matching the accuracy of 400 billion-parameter models like Qwen 3.5 397B while being one-sixteenth the size. Running on high-end RTX GPUs provides the model the computing power it needs for a speedy experience.

These models are ideal for local agents like Hermes, and NVIDIA GPUs and DGX Spark are the fastest way to run them.
[NVIDIA Tensor Cores](https://www.nvidia.com/en-us/data-center/tensor-cores/)

accelerate AI inference to deliver higher throughput and lower latency — so Hermes can work through a multistep task or refine one of its own skills in seconds rather than minutes.

## **DGX Spark: The Always-On Agentic Computer**

Agents like Hermes are built to run continuously — responding to requests, planning multistep tasks, executing autonomously and self-improving. NVIDIA DGX Spark is the ideal companion — a compact, efficient standalone machine built for sustained, all-day agentic workflows.

With 128GB of unified memory and 1 petaflop of AI performance, NVIDIA DGX Spark can run 120 billion-parameter mixture-of-experts models all day. And the new Qwen 3.6 35B model delivers equivalent intelligence in a leaner footprint — running faster and giving users the capacity to run concurrent workloads.

To maximize performance and ease of use, read the
[Hermes DGX Spark playbook](http://www.build.nvidia.com/spark)

. Plus,
[register for upcoming hands-on sessions](https://www.nvidia.com/en-us/events/build-it-yourself-agentic-ai/)

in NVIDIA’s “Build It Yourself” agentic AI series to learn how to build autonomous AI agents with NemoClaw and OpenShell.

NVIDIA DGX Spark is available to order from NVIDIA’s manufacturing partners —
[visit the marketplace](https://marketplace.nvidia.com/en-us/enterprise/personal-ai-supercomputers/?superchip=GB10&page=1&limit=15)

.

## **Getting Started With Hermes on NVIDIA Hardware**

Running Hermes locally on NVIDIA hardware is straightforward.

Visit the
[Hermes GitHub repository](https://github.com/nousresearch/hermes-agent)

to get started, and pair it with a preferred local model and runtime. Run Hermes alongside Qwen 3.6 via
[llama.cpp](https://github.com/ggml-org/llama.cpp)

,
[LM Studio](https://lmstudio.ai/)

or
[Ollama](https://ollama.com/)

. Hermes Agent ships with
[LM Studio](https://lmstudio.ai/docs/integrations/hermes)

and
[Ollama](https://docs.ollama.com/integrations/hermes)

support out of the box for the simplest path to a local agent.

Whether for a local AI enthusiast exploring the frontier of personal agents or a developer building local tooling for their workflows, Hermes on NVIDIA hardware offers a uniquely capable and reliable foundation.

Stay tuned for more updates from RTX AI Garage on the latest open models and agents optimized for NVIDIA RTX hardware.

## **#ICYMI: The Latest From RTX AI Garage**

✨
**NVIDIA RTX PRO GPUs**

deliver up to 3x faster token generation running Qwen 3.6 models with llama.cpp. Get the real-time responsiveness needed for local AI, where agents can tackle multistep tasks and refine their skills to keep workflows seamless.

**Google’s Gemma 4 26B and 31B models now available as NVFP4 checkpoints**

for even faster performance on NVIDIA Blackwell GPUs. Pair the NVFP4 checkpoints with Google’s new Multi-Token Prediction drafters to get up to 3x faster inference at identical output quality, enabling frontier-class reasoning to run locally on NVIDIA GPUs.

**Mistral Medium version 3.5**

, also released in April, includes compatibility updates with llama.cpp and Ollama, enabling users to run on NVIDIA RTX PRO and DGX Spark systems.

🦞
**NVIDIA recently introduced NVIDIA NemoClaw,**

an open source stack that optimizes OpenClaw experiences on NVIDIA devices by increasing security and supporting local models. NemoClaw now supports Windows Subsystem for Linux (WSL2), bringing support to enthusiasts and developers on Microsoft’s platform. Get started with NemoClaw on DGX Spark with this step-by-step
[playbook](https://build.nvidia.com/spark/nemoclaw)

.

*Plug in to NVIDIA AI PC on*
[*Facebook*](https://www.facebook.com/NVIDIA.AI.PC/)
*,*
[*Instagram*](https://www.instagram.com/nvidia.ai.pc/)
*,*
[*TikTok*](https://www.tiktok.com/@nvidia_ai_pc)
*and*
[*X*](https://x.com/NVIDIA_AI_PC)
*— and stay informed by subscribing to the*
[*RTX AI PC newsletter*](https://www.nvidia.com/en-us/ai-on-rtx/?modal=subscribe-ai)
*.*

*Follow NVIDIA Workstation on*
[*LinkedIn*](https://www.linkedin.com/showcase/3761136/)
*and*
[*X*](https://x.com/NVIDIAworkstatn)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*