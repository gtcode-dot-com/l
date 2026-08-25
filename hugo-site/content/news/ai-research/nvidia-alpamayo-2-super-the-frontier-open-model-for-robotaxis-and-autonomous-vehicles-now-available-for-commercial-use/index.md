---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-08-25T01:49:33.570608+00:00'
exported_at: '2026-08-25T01:49:36.758404+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available
structured_data:
  about: []
  author: ''
  description: Open commercial licensing, benchmark‑leading reasoning and inspectable
    decisions bring autonomous vehicles, including robotaxis, closer to production
    and widescale deployment.
  headline: NVIDIA Alpamayo 2 Super, the Frontier Open Model for Robotaxis and Autonomous
    Vehicles, Now Available for Commercial Use
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/alpamayo-2-super-open-model-now-available
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Alpamayo 2 Super, the Frontier Open Model for Robotaxis and Autonomous
  Vehicles, Now Available for Commercial Use
updated_at: '2026-08-25T01:49:33.570608+00:00'
url_hash: c0f46ed800c9353ce869090986c8f4e27780937a
---

For
[robotaxis](https://www.nvidia.com/en-us/glossary/robotaxi/)
and other
[autonomous vehicles](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/)
(AVs), the hardest problems aren’t the everyday scenarios. They’re the rare, complex situations that are difficult to anticipate and train for.

Handling these long‑tail events takes more than just object detection and motion prediction. AVs must understand the situation, reason about cause and effect, choose the right action and turn that decision into a safe, comfortable path — all in real time and in a way developers can inspect, validate and trust.

NVIDIA Alpamayo 2 Super,
[available now](https://huggingface.co/nvidia/Alpamayo2-Super)
for commercial use, is part of the Alpamayo family, the most-adopted open reasoning models for autonomous driving on Hugging Face, supporting a wide range of AV-relevant capabilities within a single foundation model.

Built on
[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
3 Super Reasoner and post‑trained with reinforcement learning, the model advances the AV ecosystem on two fronts: open commercial licensing and leading multitask capabilities for autonomous driving.

Alpamayo 2 Super is part of NVIDIA’s growing collection of open models, datasets and
[tools for autonomous driving](https://developer.nvidia.com/drive/downloads?sortBy=drive_downloads%2Fsort%2Fdate%3Adesc)
, expanding access, strengthening competition, giving developers greater control and supporting safer, more transparent AV deployment.

VIDEO

## **Open Licensing for Production AVs**

Alpamayo 2 Super is available on Hugging Face under OpenMDW‑1.1, the Linux Foundation’s permissive license for open AI model distributions. The license covers fine‑tuning, derivative models and commercial redistribution, allowing AV developers, automakers, truckmakers and suppliers to adapt Alpamayo to their own data, driving policies and deployment strategies.

This openness lets AV researchers and companies keep control of their own data and infrastructure, as well as own the value they create through specialized models and accumulated know‑how. Such control is essential for workflows involving proprietary fleets and safety.

Earlier Alpamayo releases were initially introduced for R&amp;D. The OpenMDW license is now being  applied across the entire Alpamayo model family so developers can deploy any of the models commercially without requiring additional permissions. This creates a direct path from adaptation to deployment.

Open weights make that path economically viable. Teams can build on advanced reasoning without re‑training every foundation capability from scratch or paying frontier‑model costs for every task, matching the right model to the right job at the right cost.

Alpamayo 2 Super enables frontier-scale reasoning in cloud-based development workflows, where developers can generate high-quality reasoning traces, synthetic training data and teacher outputs for model distillation. Within the Alpamayo model family, Alpamayo 2 Super delivers the highest reasoning and driving performance for multimodal autonomous driving development, while Alpamayo 1.5 and Alpamayo 1 provide more cost-efficient options for cloud-based development and model distillation.

The resulting distilled models can then be optimized for efficient, real-time inference in production vehicles. Together, the Alpamayo model family provides a cloud-to-car workflow that combines frontier-scale reasoning with scalable deployment across commercial AV fleets.

For AV programs, that means frontier‑scale reasoning in the cloud and efficient, specialized models in the vehicle — a more sustainable way to scale safe autonomy into commercial fleets.

## **Benchmark-Leading Reasoning at Frontier Scale**

Alpamayo 2 Super ranks first on LingoQA, an autonomous driving reasoning benchmark, among nearly 40 models evaluated. In NVIDIA testing using the Lingo‑Judge metric, it outperformed Qwen2.5‑VL 72B by 17.0 points, Gemini 2.5 Pro by 15.1 points and GPT‑4o by 23.2 points, demonstrating state‑of‑the‑art reasoning for driving‑centric scenarios. Alpamayo 2 Super also ranks first across all autonomous driving benchmarks evaluated by NVIDIA, underscoring its leading performance across a broad range of AV capabilities.

Alpamayo 2 Super offers 3x the scale of the 10‑billion‑parameter NVIDIA Alpamayo 1.5 and Alpamayo 1 models. The added capacity helps the model better generalize reasoning from sparse examples — a critical capability for the rare, multi‑agent interactions where conventional systems often struggle.

The model reasons over full‑surround camera coverage, fusing views from the vehicle’s front, sides and rear. This 360‑degree context enables richer understanding of lane changes, merges, unprotected turns and complex intersections, where risks commonly arise.

VIDEO

## **A Multitask Foundation Model for Robotaxis and Autonomous Driving**

For each driving situation, Alpamayo 2 Super can produce five tightly coupled outputs:

* A trajectory describing the vehicle’s planned path.
* A chain‑of‑causation (CoC) trace that explains the reasoning behind the decision.
* A meta‑action (e.g., yield, lane changes, stops) that captures the model’s intent.
* Reasoning auto-labels that generate CoC annotations for training and validation data.
* Visual question answering responses with 2D visual grounding that link the model’s answers to specific regions in camera images.

Together, these outputs offer insight into the model’s decision-making process. Developers can tie what the model observed to the action it selected, making decisions easier to understand, critique and validate.

CoC traces integrate with
[NVIDIA Halos](https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/)
safety‑validation workflows and support AI safety aligned with ISO/PAS 8800 requirements, providing a stronger foundation for AV safety engineering.

Alpamayo 2 Super can also be deployed as an autolabeler to generate CoC labels and perform visual question answering with 2D grounding on proprietary fleet data. By linking its reasoning to specific regions in camera images, the model can transform raw driving clips into richer training data, compressing annotation cycles from months to days.

Beyond planning and auto-labeling, Alpamayo 2 Super supports scene understanding, model critiquing and knowledge distillation. These multitask capabilities enable developers to use a single foundation model across more of the development stack, simplifying tooling and accelerating iteration.

## **An Open Ecosystem for Reasoning‑Based AVs**

Alpamayo 2 Super is part of a broader family of open models, frameworks and datasets for AV development.

Other tools in the family include:

* NVIDIA AlpaSim, which provides closed‑loop simulation.
* NVIDIA AlpaGym, which enables high‑throughput reinforcement learning.
* NVIDIA Physical AI Open Datasets, which supply data for training and testing.
* Open training recipes and an autolabeling pipeline to accelerate model development, training and validation.

Alpamayo has already surpassed 500,000 downloads on Hugging Face, reinforcing its position as the most-adopted open reasoning model family for autonomous driving on the platform.

*Download*
[*NVIDIA Alpamayo 2 Super on Hugging Face*](https://huggingface.co/nvidia/Alpamayo2-Super)
*to explore the model, evaluate its reasoning capabilities and start building the next generation of robotaxis and autonomous vehicles.*