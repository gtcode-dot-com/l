---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-01T21:28:34.363975+00:00'
exported_at: '2025-12-01T21:28:36.986006+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/neurips-open-source-digital-physical-ai
structured_data:
  about: []
  author: ''
  description: NVIDIA releases new AI tools for speech, safety and autonomous driving
    — including NVIDIA DRIVE Alpamayo-R1, the world’s first open industry-scale reasoning
    vision language action model for mobility — and a new independent benchmark recognizes
    the openness and transparency of NVIDIA Nemotron models and datasets.
  headline: At NeurIPS, NVIDIA Advances Open Model Development for Digital and Physical
    AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/neurips-open-source-digital-physical-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: At NeurIPS, NVIDIA Advances Open Model Development for Digital and Physical
  AI
updated_at: '2025-12-01T21:28:34.363975+00:00'
url_hash: de51c4f7681d937a56ebd010ddca87caada5054a
---

Researchers worldwide rely on open-source technologies as the foundation of their work. To equip the community with the latest advancements in digital and physical AI, NVIDIA is further expanding its collection of open AI models, datasets and tools — with potential applications in virtually every research field.

At
[NeurIPS](https://www.nvidia.com/en-us/events/neurips/)
, one of the world’s top AI conferences, NVIDIA is unveiling open physical AI models and tools to support research, including Alpamayo-R1, the world’s first industry-scale open reasoning vision language action (VLA) model for autonomous driving. In digital AI, NVIDIA is releasing new models and datasets for speech and AI safety.

NVIDIA researchers are presenting over 70 papers, talks and workshops at the conference, sharing innovative projects that span AI reasoning, medical research, autonomous vehicle (AV) development and more.

These initiatives deepen NVIDIA’s commitment to open source — an effort recognized by a new
[Openness Index from Artificial Analysis](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index)
, an independent organization that benchmarks AI. The Artificial Analysis Open Index rates the
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
family of open technologies for frontier AI development among the most open in the AI ecosystem based on the permissibility of the model licenses, data transparency and availability of technical details.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/Artificial-Analysis-Openness-Index-1680x730.jpg)

## **NVIDIA DRIVE Alpamayo-R1 Opens New Research Frontier for Autonomous Driving**

[NVIDIA DRIVE Alpamayo-R1 (AR1)](https://research.nvidia.com/publication/2025-10_alpamayo-r1)
, the world’s first open
[reasoning VLA model](https://www.nvidia.com/en-us/glossary/reasoning-vision-language-action/)
for AV research, integrates chain-of-thought
[AI reasoning](https://www.nvidia.com/en-us/glossary/ai-reasoning/)
with path planning — a component critical for advancing AV safety in complex road scenarios and enabling
[level 4 autonomy](https://blogs.nvidia.com/blog/level-4-autonomous-driving-ai/)
.

While previous iterations of self-driving models struggled with nuanced situations — a pedestrian-heavy intersection, an upcoming lane closure or a double-parked vehicle in a bike lane — reasoning gives autonomous vehicles the common sense to drive more like humans do.

AR1 accomplishes this by breaking down a scenario and reasoning through each step. It considers all possible trajectories, then uses contextual data to choose the best route.

For example, by tapping into the chain-of-thought reasoning enabled by AR1, an AV driving in a pedestrian-heavy area next to a bike lane could take in data from its path, incorporate reasoning traces — explanations on why it took certain actions — and use that information to plan its future trajectory, such as moving away from the bike lane or stopping for potential jaywalkers.

AR1’s open foundation, based on
[NVIDIA Cosmos Reason](https://huggingface.co/nvidia/Cosmos-Reason1-7B)
, lets researchers customize the model for their own non-commercial use cases, whether for benchmarking or building experimental AV applications.

For post-training AR1,
[reinforcement learning](https://www.nvidia.com/en-us/glossary/reinforcement-learning/)
has proven especially effective — researchers observed a significant improvement in reasoning capabilities with AR1 compared with the pretrained model.

NVIDIA DRIVE Alpamayo-R1 will be available on GitHub and Hugging Face, and a subset of the data used to train and evaluate the model is available in the
[NVIDIA Physical AI Open Datasets](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles)
. NVIDIA has also released the open-source
[AlpaSim framework](https://github.com/NVlabs/alpasim)
to evaluate AR1.

Learn more about
[reasoning VLA models for autonomous driving](https://www.nvidia.com/en-us/on-demand/session/gtcdc25-dc51155/?playlistId=playList-187e39a0-9b5f-4655-bc6a-af749f397332)
.

## **Customizing NVIDIA Cosmos for Any Physical AI Use Case**

Developers can learn how to use and post-train Cosmos-based models using step-by-step recipes, quick-start inference examples and advanced post-training workflows now available in the
[Cosmos Cookbook](https://nvidia-cosmos.github.io/cosmos-cookbook/index.html)
. It’s a comprehensive guide for physical AI developers that covers every step in AI development, including data curation,
[synthetic data generation](https://www.nvidia.com/en-us/use-cases/synthetic-data/)
and model evaluation.

There are virtually limitless possibilities for Cosmos-based applications. The latest examples from NVIDIA include:

* [**LidarGen**](https://github.com/nv-tlabs/Cosmos-Drive-Dreams/tree/main/cosmos-transfer-lidargen)
  , the first world model that can generate lidar data for AV simulation.
* [**Omniverse NuRec Fixer**](https://huggingface.co/nvidia/Fixer)
  , a model for AV and robotics simulation that taps into
  [NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
  Predict to near-instantly address artifacts in neurally reconstructed data, such as blurs and holes from novel views or noisy data.
* [**Cosmos Policy**](https://openreview.net/forum?id=wPEIStHxYH)
  , a framework for turning large pretrained video models into robust robot policies — a set of rules that dictate a robot’s behavior.
* [**ProtoMotions3**](https://github.com/NVlabs/ProtoMotions)
  , an open-source, GPU-accelerated framework built on NVIDIA Newton and Isaac Lab for training physically simulated digital humans and humanoid robots with realistic scenes generated by Cosmos
  [world foundation models (WFMs)](https://www.nvidia.com/en-us/glossary/world-models/?ncid=so-nvsh-876275)
  .

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/LidarGen-1680x1020.jpg)


Sample outputs from the LidarGen model, built on Cosmos. The top row shows the input data with generated lidar data overlaid. The middle row shows generated and real lidar range maps. Bottom left shows the real lidar point cloud, while bottom right shows the point cloud generated by LidarGen.

Policy models can be trained in
[NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)
and
[Isaac Sim](https://developer.nvidia.com/isaac/sim)
, and data generated from the policy models can then be used to post-train
[NVIDIA GR00T N](https://developer.nvidia.com/isaac/gr00t)
models for robotics.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/ProtoMotions.gif)


Humanoid policy trained with ProtoMotions3 in Isaac Sim, with 3D background scene generated by
[Lyra](https://research.nvidia.com/labs/toronto-ai/lyra/)
with Cosmos WFM.

NVIDIA ecosystem partners are developing their latest technologies with Cosmos WFMs.

AV developer
[Voxel51](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/transfer2_5/inference-biotrove-augmentation_w_FiftyOne/inference.html)
is contributing model recipes to the Cosmos Cookbook. Physical AI developers
[1X](https://arxiv.org/abs/2510.07092)
, Figure AI, Foretellix, Gatik, Oxa, PlusAI and
[X-Humanoid](https://arxiv.org/abs/2509.22642)
are using WFMs for their latest physical AI applications. And researchers at ETH Zurich are presenting a
[NeurIPS paper](https://arxiv.org/pdf/2506.20601)
that highlights using Cosmos models for realistic and cohesive 3D scene creation.

**NVIDIA Nemotron Additions Bolster the Digital AI Developer Toolkit**

NVIDIA is also releasing new multi-speaker
[speech AI](https://www.nvidia.com/en-us/glossary/speech-ai/)
models, a new model with reasoning capabilities and datasets for AI safety, as well as open tools to generate high-quality synthetic datasets for reinforcement learning and domain-specific model customization. These tools include:

* [**MultiTalker Parakeet**](https://huggingface.co/nvidia/multitalker-parakeet-streaming-0.6b-v1)
  : An automatic speech recognition model for streaming audio that can understand multiple speakers, even in overlapped or fast-paced conversations.
* [**Sortformer**](https://huggingface.co/nvidia/diar_streaming_sortformer_4spk-v2.1)
  : A state-of-the-art model that can accurately distinguish multiple speakers within an audio stream — a process called diarization — in real time.
* [**Nemotron Content Safety Reasoning**](https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B)
  : A reasoning-based AI safety model that dynamically enforces custom policies across domains.
* [**Nemotron Content Safety Audio**
  **Dataset**](https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Audio-Dataset)
  : A synthetic dataset that helps train models to detect unsafe audio content, enabling the development of guardrails that work across text and audio modalities.
* [**NeMo Gym**](https://docs.nvidia.com/nemo/gym/latest/about/index.html)
  : an open-source library that accelerates and simplifies the development of reinforcement learning environments for LLM training. NeMo Gym also contains a growing collection of ready-to-use training environments to enable Reinforcement Learning from Verifiable Reward (RLVR).
* [**NeMo Data Designer Library**](https://nvidia-nemo.github.io/DataDesigner/)
  : Now open-sourced under Apache 2.0, this library provides an end-to-end toolkit to generate, validate and refine high-quality synthetic datasets for generative AI development, including domain-specific model customization and evaluation.

VIDEO

NVIDIA ecosystem partners using NVIDIA Nemotron and NeMo tools to build secure, specialized agentic AI include CrowdStrike, Palantir and ServiceNow.

NeurIPS attendees can explore these innovations at the
[Nemotron Summit](https://nvevents.nvidia.com/nemotron-summit)
, taking place today, from 4-8 p.m. PT, with an opening address by Bryan Catanzaro, vice president of applied deep learning research at NVIDIA.

## **NVIDIA Research Furthers Language AI Innovation**

Of the dozens of
[NVIDIA-authored research papers at NeurIPS](https://www.nvidia.com/en-us/events/neurips/)
, here are a few highlights advancing language models:

*View the full list of*
[*events at NeurIPS*](https://www.nvidia.com/en-us/events/neurips/)
*, running through Sunday, Dec. 7, in San Diego.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*