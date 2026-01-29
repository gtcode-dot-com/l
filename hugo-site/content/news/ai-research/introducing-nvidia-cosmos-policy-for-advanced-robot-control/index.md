---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-29T18:15:27.996888+00:00'
exported_at: '2026-01-29T18:15:30.454711+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: Introducing NVIDIA Cosmos Policy for Advanced Robot Control
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/cosmos-policy-for-robot-control
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Introducing NVIDIA Cosmos Policy for Advanced Robot Control
updated_at: '2026-01-29T18:15:27.996888+00:00'
url_hash: 29ea826f2ab24188bd7adfb2cc60481b286eb20c
---

# Introducing NVIDIA Cosmos Policy for Advanced Robot Control

We are continuously expanding

[**NVIDIA Cosmos™**](https://www.nvidia.com/en-us/ai/cosmos/)

world foundation models (WFMs) to tackle some of the hardest problems in robotics, autonomous vehicle development, and industrial vision AI.

To further support this effort, we’re introducing
[**Cosmos Policy**](https://research.nvidia.com/labs/dir/cosmos-policy/)
, our latest research on advancing robot control and planning using Cosmos WFMs.

## TL;DR

1. **Cosmos Policy**
   : A new state-of-the-art robot control policy that post-trains the Cosmos Predict-2
   [world foundation model](https://www.nvidia.com/en-us/glossary/world-models/)
   for manipulation tasks. It directly encodes robot actions and future states into the model, achieving SOTA performance on LIBERO and RoboCasa benchmarks.

   📦
   [Model on HuggingFace](https://huggingface.co/collections/nvidia/cosmos-policy)
   | 🔧
   [Code on GitHub](https://github.com/nvlabs/cosmos-policy)
2. **Cosmos Cookoff**
   : An open hackathon where developers can get hands-on with Cosmos world foundation models and push the boundaries of physical AI.

   🍳
   [Join the Cosmos Cookoff](https://luma.com/nvidia-cosmos-cookoff?utm_source=huggingface)

## Overview: What Is Cosmos Policy?

[
](https://cdn-uploads.huggingface.co/production/uploads/677c471f8b4c4e271e57eaa5/GmY084PXnAsNRn5BnVgdG.mp4)

Cosmos Policy is a robot control and planning policy obtained by fine-tuning Cosmos Predict, a world foundation model trained to predict future frames. Instead of introducing new architectural components or separate action modules, Cosmos Policy adapts the pretrained model directly through a single stage of post-training on robot demonstration data.

> *A Policy is the system’s decision-making brain that maps observations (such as camera images) to physical actions (like moving a robotic arm) to complete tasks.*

**What’s different?**

The breakthrough of Cosmos Policy is how it represents this data. Instead of building separate neural networks for the robot's perception and control , it treats robot actions, physical states, and success scores just like frames in a video.

All of these are encoded as additional latent frames. These are learned using the same diffusion process as video generation, allowing the model to inherit its pre-learned understanding of physics, gravity, and how scenes evolve over time.

> *Latent refers to the compressed, mathematical language a model uses to understand data internally (rather than raw pixels).*

As a result, a single model can:

* Predict action chunks to guide robots movement using hand-eye coordination (i.e.,visuomotor control)
* Predict future robot observations for world modeling
* Predict expected returns (i.e. value function) for planning

All three capabilities are learned jointly within one unified model.

Cosmos Policy can be deployed either as a direct policy, where only actions are generated at inference time, or as a planning policy, where multiple candidate actions are evaluated by predicting their resulting future states and values.

---

## Base model: Cosmos Predict and why it matters

Recent work in robotic manipulation has increasingly relied on large pretrained backbones to improve generalization and data efficiency. Most of these approaches build on vision-language models (VLMs) trained on large-scale image–text datasets and fine-tuned to predict robot actions.

These models learn to understand videos and describe what they see, but they do not learn how to physically perform actions. A VLM can suggest high-level actions like turn left or pick up the purple cup, but it does not know how to carry them out precisely.

In contrast, WFMs are trained to predict how scenes evolve over time and generate temporal dynamics with videos. These capabilities are directly relevant to robot control, where actions must account for how the environment and the robot’s own state change over time.

Cosmos Predict is trained for physical AI using a diffusion objective over continuous spatiotemporal latents, enabling it to model complex, high-dimensional, and multimodal distributions across long temporal horizons.

This design makes Cosmos Predict a natural foundation for visuomotor control:

* The model already learns state transitions through future-frame prediction.
* Its diffusion formulation supports multimodal outputs, which is critical for tasks with multiple valid action sequences.
* The transformer-based denoiser can scale to long sequences and multiple modalities.

Cosmos Policy is built on post-trained Cosmos Predict2 to generate robot actions alongside future observations and value estimates, using the model’s native diffusion process. This allows the policy to fully inherit the pretrained model’s understanding of temporal structure and physical interaction while remaining simple to train and deploy.

> ⚡
> **Important Update:**
> Latest Cosmos Predict 2.5 is
> [here](https://github.com/nvidia-cosmos/cosmos-predict2.5)
> . Check out the
> [model card](https://huggingface.co/nvidia/Cosmos-Predict2.5-2B)
> .

---

## Results at a Glance

Cosmos Policy is evaluated across
**simulation benchmarks**
and
**real-world robot manipulation tasks**
, comparing against diffusion-based policies trained from scratch, video-based robot policies, and fine-tuned vision-language-action (VLA) models.

Cosmos Policy is evaluated on
**LIBERO**
and
**RoboCasa**
, two standard benchmarks for multi-task and long-horizon robotic manipulation.

On
**LIBERO**
, Cosmos Policy consistently outperforms prior diffusion policies and VLA-based approaches across task suites, particularly on tasks that require precise temporal coordination and multi-step execution.

| Model | Spatial SR (%) | Object SR (%) | Goal SR (%) | Long SR (%) | Average SR (%) |
| --- | --- | --- | --- | --- | --- |
| Diffusion Policy | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |
| Dita | 97.4 | 94.8 | 93.2 | 83.6 | 92.3 |
| π0 | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| UVA | -- | -- | -- | 90.0 | -- |
| UniVLA | 96.5 | 96.8 | 95.6 | 92.0 | 95.2 |
| π0.5 | 98.8 | 98.2 | 98.0 | 92.4 | 96.9 |
| Video Policy | -- | -- | -- | 94.0 | -- |
| OpenVLA-OFT | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |
| CogVLA | 98.6 | 98.8 | 96.6 | 95.4 | 97.4 |
| **Cosmos Policy (ours)** | 98.1 | 100.0 | 98.2 | 97.6 | 98.5 |

[
](https://cdn-uploads.huggingface.co/production/uploads/677c471f8b4c4e271e57eaa5/nCuIfEaiJc_fb1LjZS3C_.mp4)

On
**RoboCasa**
, Cosmos Policy achieves higher success rates than baselines trained from scratch, demonstrating improved generalization across diverse household manipulation scenarios.

| Model | # Training Demos per Task | Average SR (%) |
| --- | --- | --- |
| GR00T-N1 | 300 | 49.6 |
| UVA | 50 | 50.0 |
| DP-VLA | 3000 | 57.3 |
| GR00T-N1 + DreamGen | 300 (+10000 synthetic) | 57.6 |
| GR00T-N1 + DUST | 300 | 58.5 |
| UWM | 1000 | 60.8 |
| π0 | 300 | 62.5 |
| GR00T-N1.5 | 300 | 64.1 |
| Video Policy | 300 | 66.0 |
| FLARE | 300 | 66.4 |
| GR00T-N1.5 + HAMLET | 300 | 66.4 |
| **Cosmos Policy (ours)** | 50 | 67.1 |

In both benchmarks,
**initializing from Cosmos Predict**
provides a significant performance advantage over training equivalent architectures without video pretraining.

**Planning vs. Direct Policy Execution**

When deployed as a direct policy, Cosmos Policy already matches or exceeds state-of-the-art performance on most tasks.

When enhanced with
**model-based planning**
, we observe a
**12.5% higher task completion rate**
on average in two challenging real-world manipulation tasks.

**Real-World Manipulation**

[
](https://cdn-uploads.huggingface.co/production/uploads/677c471f8b4c4e271e57eaa5/GSjsYCyd-ZFgSigCS9g69.mp4)

Cosmos Policy is also evaluated on
**real-world bimanual manipulation tasks**
using the ALOHA robot platform.

The policy successfully executes long-horizon manipulation tasks
**directly from visual observations**
.

Learn more about architecture and results
[here](https://research.nvidia.com/labs/dir/cosmos-policy/cosmos_policy_index.html)
.

---

## What’s Next: Cosmos Cookoff

Cosmos Policy represents an early step toward adapting world foundation models for robot control and planning. We are actively working with early adopters to evolve this research for our robotics community.

In parallel, the Cosmos Policy continues to be available to developers through practical
[Cosmos Cookbook recipe](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/predict2/cosmos_policy/post_training.html)
, which demonstrates how you can adopt and build it.

To support hands-on experimentation with Cosmos WFMs, we are announcing the Cosmos Cookoff, an open hackathon focused on building applications and workflows using Cosmos models and cookbook recipes.The latest Cookoff is live, inviting physical AI developers across robotics, autonomous vehicles, and video analytics to explore, prototype fast, and learn with experts.

* 📅
  **When:**
  Jan 29 – Feb 26
* 👥
  **Team Format:**
  Up to 4 member team
* 🏆
  **Prizes:**
  $5,000 cash prize, NVIDIA DGX Spark™, NVIDIA GeForce RTX™ 5090 GPU, and more!
* 🧑‍⚖️
  **Judges:**
  Projects will be reviewed by experts from Datature, Hugging Face, Nebius, Nexar, and NVIDIA, bringing deep experience in open models, cloud/compute, and real-world edge and vision AI deployments.

---

### 📣 Get Started