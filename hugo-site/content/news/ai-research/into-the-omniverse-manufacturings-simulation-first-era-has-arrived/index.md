---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-28T16:15:49.647059+00:00'
exported_at: '2026-04-28T16:15:52.292534+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/manufacturing-simulation-first
structured_data:
  about: []
  author: ''
  description: 'Manufacturing’s traditional design-build-test cycle rested on a single
    assumption: Real-world testing was the only reliable test environment.'
  headline: 'Into the Omniverse: Manufacturing’s Simulation-First Era Has Arrived'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/manufacturing-simulation-first
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Into the Omniverse: Manufacturing’s Simulation-First Era Has Arrived'
updated_at: '2026-04-28T16:15:49.647059+00:00'
url_hash: be78c11fb9ab61ae6094ea4d277d26d7f007ac5b
---

*Editor’s note: This post is part of*
[*Into the Omniverse*](https://www.nvidia.com/en-us/omniverse/news/)
*, a series focused on how developers, 3D practitioners, and enterprises can transform their workflows using the latest advances in*
[*OpenUSD*](https://www.nvidia.com/en-us/omniverse/usd/)
*and*
[*NVIDIA Omniverse*](https://www.nvidia.com/en-us/omniverse/usd/)
*.*

Manufacturing’s traditional design-build-test cycle rested on a single assumption: Real-world testing was the only reliable test environment.

That assumption is now shifting.

Today, high-fidelity simulation produces synthetic training data accurate enough for production-grade AI. This is enabling perception systems, reasoning models and agentic workflows to excel in live factory environments.

[OpenUSD](https://www.nvidia.com/en-us/omniverse/usd/)

has emerged as the connective standard that makes this practical, and the manufacturers building on it are already experiencing measurable results.

## **SimReady: The Content Standard for Physical AI**

As
[physical AI](https://www.nvidia.com/en-us/glossary/generative-physical-ai/)

becomes integral to industrial operations, manufacturers face a foundational challenge: Assets don’t travel reliably between 3D pipelines. Every time an asset moves from a computer-aided design tool to a simulation platform, physics properties, geometry and metadata are lost — forcing teams to rebuild from scratch.

[SimReady](https://www.nvidia.com/en-us/glossary/simready/)

is the content standard, built on OpenUSD, defining what physically accurate 3D assets must contain to work reliably across rendering, simulation and AI training pipelines.

In addition,
[NVIDIA Omniverse libraries](https://developer.nvidia.com/omniverse?size=n_12_n&sort-field=featured&sort-direction=desc)

provide the physics-accurate, photorealistic simulation layer where AI models are trained and validated before deployment.

## **Four Ways Manufacturers Are Putting the NVIDIA Physical AI Stack to Work**

### **ABB Robotics Closes the Sim-to-Real Gap at 99% Accuracy**

ABB Robotics has integrated NVIDIA Omniverse libraries directly into RobotStudio HyperReality, its simulation platform used by more than 60,000 engineers globally.

The platform represents robot stations as USD files running the same firmware as their physical counterparts, making it possible to train robots, test part tolerances and validate AI models before a production line exists.

Synthetic training variations — such as lighting conditions and geometry differences — can be generated at scale, covering scenarios that would be impractical to replicate manually.

“We’ve managed to vertically integrate the complete technology stack and optimize it to a point where we’re now achieving 99% accuracy on the simulated version,” said Craig McDonnell, managing director of business line industries at ABB Robotics.

The downstream outcomes: up to 50% reduction in product introduction cycles, up to 80% reduction in commissioning time and a 30-40% reduction in total equipment lifecycle cost.

### **JLR Compresses Four Hours of Aerodynamic Simulation to One Minute**

JLR applied the same simulation-first principle to vehicle aerodynamics. Engineers trained neural surrogate models on more than 20,000 wind-tunnel-correlated
[computational fluid dynamics simulations](https://www.nvidia.com/en-us/use-cases/computational-fluid-dynamics-simulation/)

across the vehicle portfolio — with 95% of aero-thermal workloads now running on NVIDIA GPUs.

The Neural Concept Design Lab — built on Omniverse and deployed at JLR — visualizes aerodynamic changes in real time as designers adjust vehicle geometry, collapsing what was a sequential design-then-simulate cycle into a continuous loop. A result that once took four hours now takes one minute.

VIDEO

### **Tulip Brings Real-Time Factory Intelligence to Terex for Operational Gains**

Once a factory goes into production, a different intelligence challenge begins — one that simulation alone can’t address.

Tulip Interface’s
[Factory Playback](https://tulip.co/press/tulip-announces-factory-playback-nvidia/)

platform demonstrates how existing infrastructure can become an intelligence layer, turning operations records into something users can actually learn from. Tulip built Factory Playback on the
[NVIDIA Metropolis VSS Blueprint](https://build.nvidia.com/nvidia/video-search-and-summarization/blueprintcard)

— a reference architecture for extracting structured intelligence from factory camera feeds — connecting camera streams, machine sensor data and operational context into a unified timeline of what actually happened.

In addition, Factory Playback uses the
[NVIDIA Cosmos Reason](https://www.nvidia.com/en-us/ai/cosmos/)
[vision language model](https://www.nvidia.com/en-us/glossary/vision-language-models/)

to interpret camera streams and operator behaviors in real time, running on premises on NVIDIA GPUs.

Deployed at Terex, a global industrial equipment manufacturer with over 40 plants, the system is expected to deliver a 3% increase in yield and 10% reduction in rework.

“I am excited to see what manufacturers will do with the power of AI to augment their daily capabilities,” said Rony Kubat, cofounder and chief information officer of Tulip Interfaces.

## **Getting Started**

SimReady assets, Omniverse libraries and NVIDIA’s physical AI stack provide a foundation developers can adopt, extend and combine across any industrial application. Here’s how to get started: