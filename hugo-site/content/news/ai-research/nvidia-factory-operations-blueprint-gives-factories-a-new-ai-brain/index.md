---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-09T02:15:24.129018+00:00'
exported_at: '2026-06-09T02:15:25.856968+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/factory-operations-fox-blueprint-ai-brain
structured_data:
  about: []
  author: ''
  description: The FOX blueprint, a reference design for building an autonomous factory
    manager agent, delivers total factory visibility for better, faster decision-making.
  headline: NVIDIA Factory Operations Blueprint Gives Factories a New AI Brain
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/factory-operations-fox-blueprint-ai-brain
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Factory Operations Blueprint Gives Factories a New AI Brain
updated_at: '2026-06-09T02:15:24.129018+00:00'
url_hash: ca83437040c30d9380687f8288c223820fa5514d
---

As factories move from isolated automation to plant-wide intelligence, manufacturers need AI systems that can connect live machine signals, quality systems, work instructions and operational alerts into a unified decision layer.

Today at GTC Taipei at COMPUTEX, NVIDIA announced the NVIDIA Factory Operations Blueprint (FOX) — a reference design for building an autonomous factory manager agent that continuously monitors and reasons across the real-time data and orchestrates a fleet of speciality agents and machines to quickly resolve issues at scale.

FOX helps developers build secure, centralized factory manager agents for orchestrating and optimizing specialized industrial AI agents for quality control, material transport and worker safety. Built with
[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/)

,
[AI-Q Blueprint](https://build.nvidia.com/nvidia/aiq)

and
[NVIDIA Nemotron open models](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

, the blueprint provides a customizable foundation for connecting factory systems, automating model development and running intelligent operations at scale.

The blueprint is optimized to run on
[NVIDIA DGX Station](https://www.nvidia.com/en-us/products/workstations/dgx-station/)

, the ultimate deskside AI supercomputer companion for factory managers.

DGX Station is powered by the NVIDIA GB300 Grace Blackwell Ultra Desktop Superchip, featuring 20 petaflops of FP4 performance and 748GB of coherent memory, and is capable of running large AI models up to 1 trillion parameters, making it ideal for developing and running powerful AI agents locally.

The superchip

features the NVIDIA Blackwell Ultra GPU connected to a high-performance NVIDIA Grace CPU using the NVIDIA NVLink-C2C interconnect to deliver best-in-class system communication and performance, ideal for lightning-fast interactions between NemoClaw and AI models.

![](https://blogs.nvidia.com/wp-content/uploads/2026/05/FOX-diagram-1680x727.jpg)

Key capabilities of the FOX blueprint include:

* **Connecting factory systems and agents**

  : FOX integrates with industrial data sources, machines, applications and robot fleets, and can connect to specialized agents from leading software developers through standard application programming interfaces and agent skills.
* **Automating AI model training**

  : Using
  [NVIDIA TAO](https://developer.nvidia.com/tao-toolkit)

  skills, factory manager agents can automate the full model-training lifecycle — identifying accuracy gaps, sourcing or synthetically generating training data, fine-tuning models and redeploying them into production.
* **Operating intelligent factory workflows**

  : Visual inspection, process compliance and material transport agents can be managed with NVIDIA open models and blueprints, including the
  [NVIDIA Metropolis Blueprint for video search and summarization (VSS)](https://build.nvidia.com/nvidia/video-search-and-summarization)

  . Real-time factory data can also be visualized in an operational twin built with
  [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)

  libraries.

Taiwan manufacturers
[Advantech](https://www.advantech.com/en-us/resources/news/advantech-empowers-the-ai-factory-brain-with-nvidia-nemoclaw-orchestrating-agentic-ai-for-end-to-end-operational-intelligence)

,

Foxconn

,

Pegatron

and

Wistron

are the first to deploy autonomous factory manager agents using the NVIDIA FOX blueprint and NemoClaw.

Foxconn

, the world’s largest electronics manufacturer, is using the FOX blueprint and NemoClaw to build MoMClaw, a manufacturing operations multi-agent system.

Running alongside a live production work, MoMClaw connects sensors, machine signals and other digital systems with hundreds of specialized agents in a single agentic layer — giving plant managers and operators real-time answers and action plans through a natural language interface with
[NVIDIA OpenShell](https://build.nvidia.com/openshell)

privacy controls and safety guardrails. With MoMClaw,

Foxconn

projects an 80% improvement in root cause analysis time, a 15% increase in labor productivity and a 10% decrease in machine failure rates.

Pegatron

is using the FOX blueprint and NemoClaw to build a factory manager agent that orchestrates specialized agents for material transport, AI inspection, standard operating procedure guidance and machine-to-machine coordination. With the factory manager agent,

Pegatron

can orchestrate robot utilization more efficiently, eliminating the need for expensive standby equipment, with an estimated 15% reduction in asset redundancy costs.

Advantech

has introduced the AI Factory Brain, an intelligent multi-agent system led by a factory manager agent built with the FOX blueprint and NemoClaw. Advantech has deployed the factory manager agent in its own factories to autonomously manage energy across HVAC and lighting specialized agents and projects to cut energy consumption by 10%.

Wistron

is adopting the FOX blueprint and using
[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)

, NVIDIA Nemotron open models and the
[NVIDIA Metropolis VSS blueprint](https://build.nvidia.com/nvidia/video-search-and-summarization)

to build surface-mount technology agents that analyze and orchestrate production-line operations, enabling real-time root-cause analysis and quality control.

To monitor manufacturing operations, improve quality, verify standard operating procedures and improve worker safety, companies including
[DeepHow](https://deephow.com/blog/foxconn-boosts-production-throughput-with-deephow-live-sop-verification-powered-by-nvidia)

,
[Overview AI](https://www.overview.ai/blog/overview-ai-nvidia-auto-defect-creator-studio/)

,
[Roboflow](https://blog.roboflow.com/synthetic-data-generation-manufacturing-nvidia/)

and

Spingence

are building specialized agents powered by NVIDIA AI and the NVIDIA VSS blueprint:

* DeepHow

  is using the Metropolis VSS Blueprint and Cosmos 3 to develop a standard operating procedure agent for Foxconn that supports assembly of Bianca boards for NVIDIA GB300 servers. Running on NVIDIA RTX PRO Servers, the agent accurately understands complex assembly motions to help improve first-pass yield by 3%, minimizing rework and production waste.

* Spingence

  is using the NVIDIA
  [D

  efect

  I

  mage

  G

  eneration](https://github.com/NVIDIA/skills/tree/main/skills/physical-ai-defect-image-generation)

  skill, NVIDIA Cosmos open vision language model and NVIDIA TAO Toolkit for fine-tuning to develop a factory manager agent for Cooler Master that connects automated optical inspection and model-building agents, achieving 99.6% defect recall, reducing defect escapes by 78% and increasing inspection capacity by 3x.
* Overview AI

  is using an NVIDIA agent skill for defect image generation and NVIDIA Cosmos to help Amphenol improve manufacturing efficiency with its Advanced GenAI Toolkit. The toolkit generates synthetic defect data and deploys visual inspection AI models 12x faster, reducing time to first inference to under 30 minutes across more than 300 products.
* Roboflow is using NVIDIA Cosmos to develop a model-building agent for Corning Fiber Optics that generates synthetic defect images when training data is limited, delivering near-perfect detection rates and demonstrates the potential to reduce daily manual image review.

[Sign up](https://www.nvidia.com/en-us/nvidia-factory-operations-blueprint-notify-me)

to be notified when the NVIDIA Factory Operations Blueprint is available.

[Metropolis VSS blueprint 3](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization)

is now generally available, including
[skills](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/tree/main/skills)

that allow external agents — such as Claude Code, Codex, Hermes and NemoClaw — to access VSS components and rapidly build and operate video analytics AI agents.

W
*atch NVIDIA founder and CEO Jensen Huang’s*
[*keynote*](https://www.nvidia.com/en-tw/gtc/taipei/keynote/)
*and learn more at*
[*NVIDIA GTC Taipei*](https://www.nvidia.com/en-tw/gtc/taipei/)
*.*