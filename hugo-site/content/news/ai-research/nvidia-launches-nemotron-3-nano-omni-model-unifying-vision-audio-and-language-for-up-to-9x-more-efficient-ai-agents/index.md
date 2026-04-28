---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-28T18:15:34.943047+00:00'
exported_at: '2026-04-28T18:15:37.193665+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents
structured_data:
  about: []
  author: ''
  description: Best-in-class open omni-modal reasoning model delivers the highest
    efficiency and accuracy to power agentic workflows such as computer use, document
    intelligence and audio-video reasoning.
  headline: NVIDIA Launches Nemotron 3 Nano Omni Model, Unifying Vision, Audio and
    Language for up to 9x More Efficient AI Agents
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Launches Nemotron 3 Nano Omni Model, Unifying Vision, Audio and Language
  for up to 9x More Efficient AI Agents
updated_at: '2026-04-28T18:15:34.943047+00:00'
url_hash: be0d9acd6ce338a2a9af0dfa466d6002373b575c
---

AI agent systems today juggle separate models for vision, speech and language — losing time and context as they pass data from one model to the other.

Unveiled today, NVIDIA Nemotron 3 Nano Omni is an open multimodal model that brings these capabilities together into one system,

enabling agents to deliver faster, smarter responses with advanced reasoning across video, audio, image and text.

This best-in-class model gives enterprises and developers a production path for more efficient and accurate multimodal AI agents with full deployment flexibility and control.

Nemotron 3 Nano Omni sets a new efficiency frontier for open multimodal models with leading accuracy and low cost,
[topping six leaderboards](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model)
for complex document intelligence, and video and audio understanding.

At a Glance

What it is

An open, omni-modal reasoning model — the highest-efficiency open multimodal model of its kind with leading accuracy

What it handles

Text, images, audio, video, documents, charts and graphical interfaces (input); text (output)

Who it’s for

Enterprises and developers building fast and reliable, agentic systems that need a multimodal perception sub-agent

How it works

Functions as the “eyes and ears” in a system of agents, working alongside models like Nemotron 3 Super and Ultra or other proprietary models

Why it matters

Leading multimodal accuracy and 9x higher throughput than other open omni models with the same interactivity, resulting in lower cost and better scalability without sacrificing responsiveness.

Architecture

30B-A3B hybrid MoE with Conv3D, EVS, 256K context

Availability

April 28th, 2026 via Hugging Face, OpenRouter, build.nvidia.com and 25+ partner platforms

AI and
software companies already adopting Nemotron 3 Nano Omni include
[Aible](https://www.aible.com/nemotron3-nano-omni-ai-agent)

,
[Applied Scientific Intelligence (ASI)](https://appliedscientific.ai/research/scientific-ai-literature-agent-nvidia-nemotron-nano-omni?utm_source=nvidia-blog)

,
[Eka Care](https://info.eka.care/services/how-ekacare-is-building-agentic-multimodal-healthcare-for-india-scale-patient-care-with-nvidia-nemotron-3-nano-omni)

,

Foxconn

,

[H Company](https://hcompany.ai/holotron3)
, Palantir and
[Pyler](https://pyler.tech/articles/scaling-trustworthy-video-safety-with-nvidia-nemotron-3-nano-omni)

,

with

Dell Technologies

,

DocuSign, Infosys, K-Dense, Lila, Oracle

and

Zefr

evaluating the model.

“To build useful agents, you can’t wait seconds for a model to interpret a screen,”

said Gautier Cloix, CEO of H Company.

“By building on Nemotron 3 Nano Omni, our agents can rapidly interpret full HD screen recordings — something that wasn’t practical before. This isn’t just a speed boost: It’s a fundamental shift in how our agents perceive and interact with digital environments in real time.”

## **Nemotron 3 Nano Omni Enables Faster, Leaner Multimodal Agents**

Consider an AI agent for customer support processing a screen recording while analyzing uploaded call audio and checking data logs — or an agent for finance tasked with parsing PDFs, spreadsheets, charts and voice notes. Today, most agentic systems accomplish these tasks with separate models for vision, speech and language.

This approach increases latency through repeated inference passes, fragments context across modalities, and adds cost and inaccuracies over time.

By combining vision and audio encoders within its 30B-A3B hybrid mixture-of-experts architecture, Nemotron 3 Nano Omni eliminates the need for separate perception models, improving efficiency at scale. As the first open model to deliver both this level of efficiency and strong multimodal perception accuracy, it enables AI systems to achieve up to 9x higher throughput than other open omni models with similar interactivity. The result is lower cost and better scalability — without sacrificing responsiveness or quality.

By combining vision and audio encoders within its 30B-A3B, hybrid
[mixture-of-experts](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)

architecture, Nemotron 3 Nano Omni eliminates the need for separate perception models, driving inference efficiency at scale. It pairs this efficiency with strong multimodal perception accuracy, enabling
[AI systems to achieve 9x higher throughput](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-inteligence)
than other open omni models with the same interactivity. The result is lower costs and better scalability without sacrificing responsiveness or quality.

In agentic systems, Nemotron 3 Nano Omni can work alongside proprietary cloud models or other NVIDIA Nemotron open models — such as Nemotron 3 Super for high-frequency execution or Nemotron 3 Ultra for complex planning — as well as proprietary models from other providers, to power sub-agents for agentic workflows such as computer use, document intelligence and audio-video reasoning.

* **Computer use agents —**

  Nemotron 3 Nano Omni powers the perception loop for agents navigating graphical user interfaces, reasoning over onscreen content and understanding user interface state over time.

  H Company’s latest
  [computer usage agent](https://www.youtube.com/watch?v=kSi9JS2l0Ww)

  , powered by Nemotron 3 Nano Omni, uses a native input resolution of 1920×1080 pixels to achieve high-fidelity visual reasoning. In preliminary evaluations on the OSWorld benchmark, this integration showed a significant leap in navigating complex graphical interfaces and used Nemotron 3 Nano Omni’s ability to process very high-resolution images.
* **Document intelligence**

  — Interprets documents, charts, tables, screenshots and mixed-media inputs, enabling agents to reason across visual structure and text content coherently. Critical for enterprise analysis and compliance workflows.
* **Audio and video understanding**

  — For customer service, research and monitoring workflows, Nemotron 3 Nano Omni maintains audio-video context, tying what was said, shown and documented into a single reasoning stream instead of disconnected summaries.

![](https://blogs.nvidia.com/wp-content/uploads/2026/04/nemotron-3-nano-omni-graphic-960x260.jpg)

## **Open and Customizable, Deployable Anywhere**

Nemotron 3 Nano Omni is released with open weights, datasets and training techniques — giving organizations full transparency and control over how the model is customized and deployed.

Developers can use tools like
[NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/)

for customization, evaluation and optimization for domain-specific use cases. Because the Nemotron family of models is open, organizations can deploy them in environments that meet regulatory, sovereignty or data localization requirements.





The Nemotron 3 family — including Nano, Super and Ultra models — has seen over

50 million downloads in the past year

. Omni extends the family’s capabilities into multimodal and agentic domains.

The model is available on
[Hugging Face](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)

,
[OpenRouter](https://openrouter.ai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)

and
[build.nvidia.com](https://build.nvidia.com/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning)

as an NVIDIA NIM microservice and through a broad ecosystem of
[NVIDIA Cloud Partners](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners/)

, inference platforms

and cloud service providers.

Its open, lightweight architecture supports consistent deployment from local systems like
[NVIDIA DGX Spark](https://www.nvidia.com/en-us/products/workstations/dgx-spark/)

and
[DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/)

to data center and cloud environments.

*Visit the NVIDIA technical blog for*
[*tutorials, cookbooks and deployment guides*](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model)


*for Nemotron 3 Nano Omni use cases.*

*S*
*tay up to date on agentic AI,*
[*NVIDIA Nemotron*](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
*and more by subscribing to*
[*NVIDIA news*](https://www.nvidia.com/en-us/executive-insights/generative-ai-tools/?modal=stay-inf)
*,*
[*joining the community*](https://developer.nvidia.com/community)
*and following NVIDIA AI on*
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