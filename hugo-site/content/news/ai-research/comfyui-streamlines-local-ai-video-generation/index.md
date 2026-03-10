---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-10T18:15:31.480150+00:00'
exported_at: '2026-03-10T18:15:34.016246+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/rtx-ai-garage-flux-ltx-video-comfyui-gdc
structured_data:
  about: []
  author: ''
  description: 'GDC 2026: AI-powered video generation with ComfyUI’s App View, NVIDIA
    RTX Video Super Resolution and new NVFP4 models.'
  headline: NVIDIA and ComfyUI Streamline Local AI Video Generation for Game Developers
    and Creators at GDC
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/rtx-ai-garage-flux-ltx-video-comfyui-gdc
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA and ComfyUI Streamline Local AI Video Generation for Game Developers
  and Creators at GDC
updated_at: '2026-03-10T18:15:31.480150+00:00'
url_hash: 0794e9aa8d8616e3f6068ecba2a4bd77614c8fdd
---

Game developers and artists are building cinematic worlds and iconic characters — raising the bar for immersive experiences on
[NVIDIA RTX AI PCs](https://www.nvidia.com/en-us/ai-on-rtx/)

.

At the Game Developers Conference (GDC) in San Francisco this week, NVIDIA announced a suite of updates that streamline AI video generation for concept development and storyboarding on RTX GPUs and the NVIDIA DGX Spark desktop supercomputer.

These announcements include:

* ComfyUI’s new App View with a simplified interface, lowering the barrier for entry for the popular generative AI tool.
* RTX Video Super Resolution available for ComfyUI, a real-time 4K upscaler ideal for video generation — also available for developers as a Python Wheel.
* NVFP4 and FP8 model variants are available today for FLUX.2 Klein, with NVFP4 support for LTX-2.3 coming soon, delivering up to 2.5x performance gains and 60% lower memory usage for both models.

## **Frictionless Local AI: Collaborate, Optimize, Customize**

Many of today’s popular AI applications are making it easier for beginners to try state-of-the-art models directly on their laptop or desktop.

For artists unfamiliar with node graphs, ComfyUI’s new App View presents workflows in a simplified interface. Users only need to enter a prompt, adjust simple parameters and hit generate. The full node-based experience remains available as Node View, and users can seamlessly switch between the two modes.

App View is compatible with the RTX optimizations in ComfyUI. Performance for RTX GPUs is 40% faster since September, and ComfyUI now supports NVFP4 and FP8 data formats natively. All combined, performance is 2.5x faster and VRAM is reduced by 60% with NVIDIA GeForce RTX 50 Series GPUs’ NVFP4 format, and performance is 1.7x faster and VRAM is reduced by 40% with FP8.

At CES in January, NVIDIA announced several models released with NVFP4 and FP8 support. And now more NVFP4 and FP8 models are available —
[LTX-2.3,

with](https://huggingface.co/Lightricks/LTX-2.3-fp8)

NVFP4 support coming soon,
[FLUX.2 Klein 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-nvfp4/tree/main)

, and
[FLUX.2 Klein 9B](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-nvfp4/tree/main)

—

directly in ComfyUI. To get started, download the NVFP4 and FP8 checkpoints directly from Hugging Face, load the default workflows in ComfyUI via the Template Browser and replace the default model checkpoint with the newly downloaded checkpoint.

App View mode is available today. Learn more on
[ComfyUI](https://www.comfy.org/)

.

## **Faster 4K Video Generation**

Getting high-quality video outputs often means juggling three constraints: speed, VRAM and control. While many artists ultimately want 4K quality, most prefer to generate smaller, faster previews first, and then upscale them. Today’s upscalers take minutes to upscale a 10‑second clip into 4K resolution.

Now, users can quickly upscale generated video to 4K with NVIDIA RTX Video Super Resolution, available as a node for ComfyUI. RTX Video can be accessed as a
[standalone node](https://github.com/Comfy-Org/Nvidia_RTX_Nodes_ComfyUI)
for building video workflows from scratch.

For AI developers, NVIDIA released a free Python package available via
[the PyPI repository](https://pypi.org/project/nvidia-vfx/)

, along  with
[sample code on GitHub](https://github.com/NVIDIA-Maxine/nvidia-vfx-python-samples)

and a
[VFX Python bindings guide](https://docs.nvidia.com/maxine/vfx-python/latest/index.html)

, to get started quickly. The package provides programmatic access to the same AI upscaling technology that powers RTX Video, running directly on RTX GPU Tensor Cores to deliver 4K upscaling 30x faster than alternative popular local upscalers, and at a fraction of the VRAM cost. The package is powered by the
[NVIDIA Video Effects software development kit](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/maxine/collections/maxine_vfx_sdk)

.

[![](https://blogs.nvidia.com/wp-content/uploads/2026/03/RTX-AI-generative-AI-model-performance-1680x632.png)](https://blogs.nvidia.com/wp-content/uploads/2026/03/RTX-AI-generative-AI-model-performance.png)


*Generative AI model performance for LTX-2 and FLUX.2 Klein 9B on an NVIDIA RTX 5090 GPU. Performance testing done on RTX 5090. LTX-2: 512×768 resolution, 100 frames, 20 steps. FLUX.2 Klein 9B (base): 1024×1024 resolution, 20 steps.*

Ready to get started with ComfyUI? Check out the latest NVIDIA Studio Sessions tutorial hosted by  visual effects artist
[Max Novak](https://www.youtube.com/@MaxNovakTutorials)

for a guided walkthrough:

VIDEO

## **#ICYMI: The Latest Updates for RTX AI PCs at GDC**

🎉Join NVIDIA at
[GTC](https://www.nvidia.com/gtc/)

, March 16-19 in San Jose! Check out
[“Create Generative AI Workflow for Design and Visualization in ComfyUI”](https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-dlit81948/)

on March 17, for a training session led by NVIDIA 3D workflow specialists focused on building RTX-accelerated generative workflows for images, video, 3D, and PBR materials.
[Register](https://www.nvidia.com/gtc/pricing/)

today and explore the
[session catalog](https://www.nvidia.com/gtc/session-catalog/)

.

💡
[LTX Desktop](https://youtu.be/nL3Efak3FnI?si=IMzV9QcbcJZeYnOq)

is a fully local, open-source video editor running directly on the LTX engine, optimized for NVIDIA GPUs and compatible hardware.

🦥
[LM Link](https://lmstudio.ai/link)

connects separate devices running LM Studio, allowing models to run on remote machines as if they were local. It’s ideal for users wanting to run an agent on their laptop while still accessing free and private AI, powered by their DGX Spark or RTX desktop. Learn how to run
[LM Studio on DGX Spark](https://build.nvidia.com/spark/lm-studio)

.

🎮On Tuesday, March 31, as part of the next opt-in NVIDIA App beta, overrides for NVIDIA DLSS 4.5 Dynamic Multi Frame Generation and DLSS 4.5 Multi Frame Generation 6x Mode will be released for GeForce RTX 50 Series owners. Learn about
[NVIDIA news at GDC](https://www.nvidia.com/en-us/geforce/news/gdc-2026-nvidia-geforce-rtx-announcements)

.

🤖Next month,
[a new NVIDIA RTX Remix update will introduce Advanced Particle VFX](https://www.nvidia.com/en-us/geforce/news/rtx-remix-advanced-particle-vfx)

, enabling modders to create a wide array of particle effects that further improve image quality, detail and immersion.

**🦄**

Topaz Labs

has collaborated with NVIDIA to optimize NeuroStream for NVIDIA GPUs — a proprietary VRAM optimization that allows complex AI models to run on consumer hardware.

**📃**

Microsoft has introduced support for VoiceMod, one of the first apps to enable Windows ML for GPU inference, significantly improving performance voice quality compared with CPUs.

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
*. Follow NVIDIA Workstation on*
[*LinkedIn*](https://www.linkedin.com/showcase/3761136/)
*and*
[*X*](https://x.com/NVIDIAworkstatn)
*.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*