---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T03:15:46.564456+00:00'
exported_at: '2026-03-18T03:15:49.312296+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/rtx-ai-garage-gtc-2026-nemoclaw
structured_data:
  about: []
  author: ''
  description: Nemotron 3 open models unlock fast, private AI agents like OpenClaw;
    plus, creativity is accelerated with RTX-optimized NVFP4 and FP8 visual generative
    AI models.
  headline: GTC Spotlights NVIDIA RTX PCs and DGX Sparks Running Latest Open Models
    and AI Agents Locally
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/rtx-ai-garage-gtc-2026-nemoclaw
  publisher:
    logo: /favicon.ico
    name: GTCode
title: GTC Spotlights NVIDIA RTX PCs and DGX Sparks Running Latest Open Models and
  AI Agents Locally
updated_at: '2026-03-18T03:15:46.564456+00:00'
url_hash: ee5d8a053e5348d7269d117a230d1cf266b093a8
---

The paradigm of consumer computing has revolved around the concept of a personal device — from PCs to smartphones and tablets. Now, generative AI — particularly OpenClaw — has introduced a new category: agent computers. These devices, like the NVIDIA DGX Spark desktop AI supercomputer or dedicated NVIDIA RTX PCs, are ideal for running personal agents — privately and for free.

[NVIDIA GTC](https://www.nvidia.com/gtc/)

, running

this week, is showcasing a host of agentic AI announcements including:

* New open models for local agents, including NVIDIA Nemotron 3 Nano 4B and Nemotron 3 Super 120B, and optimizations for Qwen 3.5 and Mistral Small 4.
* NVIDIA NemoClaw, an open source stack for OpenClaw that optimizes OpenClaw experiences on NVIDIA devices by increasing security and supporting local models.
* Easier fine‑tuning with Unsloth Studio

  to further improve open model accuracy for agentic workflows.

In-person GTC attendees can swing by the
[NVIDIA build-a-claw event](https://blogs.nvidia.com/blog/gtc-2026-news/#build-a-claw)

in the GTC Park, running daily through March 19, from 8 a.m.-5 p.m. NVIDIA experts will help guests customize and deploy a proactive, always-on AI assistant using their device of choice. Whether technical or just curious, participants will name their agent, define its personality and grant it access to the tools it needs — creating a personal assistant reachable from their preferred messaging app.

## **New Open Models Bring Cloud-Level Quality to Local Agents**

The next generation of local models — with increasingly large context windows — delivers the intelligence to run agents on PC. Combined with richer user context and powerful local tools, these advances are unlocking new possibilities on AI PCs, especially on DGX Spark, with its 128GB of unified memory that supports models with more than 120 billion parameters.

[**Nemotron 3 Super**](https://blogs.nvidia.com/blog/nemotron-3-super-agentic-ai/)

, released last week, is a 120‑billion‑parameter open model with 12 billion active parameters, designed to run complex agentic AI systems. Nemotron 3 Super is optimal for powering agents on the DGX Spark or NVIDIA RTX PRO workstations. On
[PinchBench](https://pinchbench.com/?score=best)

— a new benchmark for determining how well large language models perform with OpenClaw — Nemotron 3 Super scored 85.6%, making it the top open model in its class.

**Mistral Small 4**

, a 119-billion-parameter open model with 6 billion active parameters — 8 billion including all layers — unifies the capabilities of Mistral’s flagship models. Users now have an ultraefficient model optimized for general chat, coding and agentic tasks.

Both of these models run locally on DGX Spark and RTX PRO GPUs.

For GeForce RTX users looking for smaller models,
**Nemotron 3 Nano 4B**

is the latest model to join the
[NVIDIA Nemotron 3 family of open models](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)

, providing a compact, capable starting point for building agents and assistants locally on RTX AI PCs. The model is a strong fit for building action-taking conversational personas in games and apps that run on resource-constrained hardware. It’s available across any NVIDIA GPU-enabled system and combines state-of-the-art instruction-following and exceptional tool use with minimal VRAM footprint.

In addition, NVIDIA announced optimizations for
**Alibaba’s Qwen 3.5 models**

,

which have demonstrated outstanding accuracy (
[27B](https://huggingface.co/Qwen/Qwen3.5-27B)

,
[9B](https://huggingface.co/Qwen/Qwen3.5-9B)

and
[4B](https://huggingface.co/Qwen/Qwen3.5-4B)

) and are suited for running local agents on NVIDIA GPUs. The new models natively support vision, multi-token prediction and a large 262,000-token context window. The dense 27-billion-parameter model excels when paired with an RTX 5090 GPU.

[![](https://blogs.nvidia.com/wp-content/uploads/2026/03/rtx-ai-pc-raig-blog-perf-chart-desktop-light@2x-1680x819.png)](https://blogs.nvidia.com/wp-content/uploads/2026/03/rtx-ai-pc-raig-blog-perf-chart-desktop-light@2x.png)


*All configurations measured using Q4\_K\_M quantizations BS = 1, ISL = 1024 and OSL = 128 on NVIDIA RTX 5090 and Mac M3 Ultra desktops. Token generation throughput measured on llama.cpp b7789, using the llama-bench tool.*

Users can try these models today via Ollama, LM Studio and llama.cpp, with accelerated inference powered by RTX GPUs and DGX Spark. Learn more about the latest on
[NVIDIA open models](https://nvidianews.nvidia.com/news/nvidia-expands-open-model-families-to-power-the-next-wave-of-agentic-physical-and-healthcare-ai)

.

## **Faster Creative AI With the Latest RTX-Optimized Models**

LTX 2.3, Lightricks’ state-of-the-art audio-video model, released earlier this month, now has support for
[NVFP4](https://huggingface.co/Lightricks/LTX-2.3-nvfp4)

and
[FP8](https://huggingface.co/Lightricks/LTX-2.3-fp8)

distilled models, accelerating performance by 2.1x. Learn more about
[Lightricks’ LTX 2.3 model](https://ltx.io/model/model-blog/ltx-2-3-release)

.

VIDEO

In addition, Black Forest Lab’s FLUX.2 Klein 9B received an update last week, accelerating image editing by up to 2x. NVIDIA has collaborated with Black Forest Labs to release an
[FP8 version](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv)

, optimized for the fastest performance and optimal memory consumption on RTX GPUs.

## **NVIDIA NemoClaw — NVIDIA Optimizations for OpenClaw**

AI developers and enthusiasts are buying DGX Spark supercomputers or building dedicated RTX PCs to run autonomous AI agents, such as OpenClaw, that draw context from personal files, apps and workflows and can automate daily tasks. However, as adoption of agentic systems like OpenClaw grows, so do concerns about token costs, as well as security and privacy.

To help address these concerns, NVIDIA this week introduced
[NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/)

, an open source stack for OpenClaw that deploys optimizations for OpenClaw on NVIDIA devices. The first features available in NemoClaw are NVIDIA Nemotron open models and the NVIDIA OpenShell runtime. Nemotron local models enable users to run inference locally, which means better privacy and no token costs. OpenShell is the runtime designed for executing claws more safely.

Learn more about
[NemoClaw](https://nvidianews.nvidia.com/news/nvidia-announces-nemoclaw)

. Watch the
[GTC keynote](https://www.nvidia.com/gtc/keynote/)

from NVIDIA founder and CEO Jensen Huang and explore
[sessions](https://www.nvidia.com/gtc/session-catalog/)
*.*

## **Fine-Tuning Made Easy With Unsloth Studio**

As open models make giant leaps, one way of further improving accuracy is fine-tuning, which allows users to customize a model for their own data and use cases. This technique normally requires in-depth technical expertise, coding knowledge and massive amounts of configuration. Unsloth, a leading open source library for model fine-tuning and alignment, today launched Unsloth Studio, an easy-to-use, web-based user interface that simplifies the fine-tuning process for AI enthusiasts and developers.

VIDEO

Unsloth Studio offers support for more than 500 AI models. The simple user interface makes the training and fine-tuning process easy: Users can just drop in their dataset, tap the graph-based canvas to generate additional high-quality synthetic data and start the fine-tuning job. It supports quantized low-rank adaptation, low-rank adaptation and full fine-tuning. As the model is being fine-tuned, users can monitor and visualize job progress. Finally, they can export the model into a framework of choice and chat away, all within the same web app.

Unsloth Studio’s new interface is built on the Unsloth library, which delivers up to 2x faster training with up to 70% VRAM savings, using custom and specialized GPU kernels. This means that new users can get the most out of their NVIDIA RTX GPUs and DGX Spark, right out of the box.

Try
[Unsloth Studio today](https://github.com/unslothai/unsloth-studio/tree/main/unsloth_studio)

, including with new models like Nemotron 3 Nano 4B and Qwen 3.5. Check out other
[RTX AI Garage](https://blogs.nvidia.com/blog/rtx-ai-garage-fine-tuning-unsloth-dgx-spark/)

posts for more information on fine-tuning models with NVIDIA GeForce RTX GPUs.

## **#ICYMI From GTC 2026**

✨
**RTX AI**
**video generation guide featuring RTX Video in ComfyUI:**

Launched at CES earlier this year, the new
[RTX AI video generation guide](https://www.nvidia.com/en-us/geforce/news/rtx-ai-video-generation-guide/)

shows creators and enthusiasts how to go from concept to creation using guided text-to-image workflows to produce keyframes for AI-generated videos, then upscale to 4K with RTX Video technology running on local GPUs. Get started with the guide and share creations on social media with #AIonRTX.

💿
[**NVIDIA AI for Media**](https://developer.nvidia.com/maxine?sortBy=developer_learning_library%2Fsort%2Ftitle%3Aasc)

is a set of high‑performance, easy‑to‑use software development kits that bring NVIDIA Broadcast-class AI effects — enhanced audio (
[Linux](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/collections/maxine_linux_audio_effects_sdk_collection)

or
[Windows](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/collections/maxine_windows_audio_effects_sdk_collection)

),
[video](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/collections/maxine_vfx_sdk)

and
[augmented-reality](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/collections/maxine_ar_sdk)

features — to live media, video conferencing and post‑production workflows. The latest update — available today — adds more accurate lip-syncing, multi‑active-speaker detection, faster 4K upscaling on RTX PRO and GeForce RTX 40 and 50 Series GPUs via the RTX Video Super Resolution feature, better background noise reduction and lower latency for the NVIDIA Studio Voice feature.

💻
[**NVIDIA DLSS 5**](https://nvidianews.nvidia.com/news/nvidia-dlss-5-delivers-ai-powered-breakthrough-in-visual-fidelity-for-games)

, arriving this fall, delivers an AI-powered breakthrough in visual fidelity for games by infusing pixels with photoreal lighting and materials to bridge the gap between rendering and reality.

🤖
**Maxon released Redshift 2026.4**

, introducing a new real-time visualization workflow powered by DLSS to allow architects to walk through projects at interactive speed and quality. “NVIDIA’s DLSS technology is a critical component, allowing us to deliver high-quality visuals at interactive speeds,” said Philip Losch, chief technology and AI officer at Maxon.

**🪟Reincubate Camo has added Windows ML on NVIDIA TensorRT RTX EP**

for AI Autotune in its Camo Streamlight app, significantly improving performance on RTX GPUs.

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