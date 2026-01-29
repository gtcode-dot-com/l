---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-29T18:15:26.962105+00:00'
exported_at: '2026-01-29T18:15:30.460158+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse
structured_data:
  about: []
  author: ''
  description: By providing access to critical infrastructure — from simulation frameworks
    to AI models — NVIDIA is enabling collaborative development that accelerates the
    path to safer, more capable autonomous systems.
  headline: 'Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots
    and Autonomous Systems'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/physical-ai-open-models-robot-autonomous-systems-omniverse
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Into the Omniverse: Physical AI Open Models and Frameworks Advance Robots
  and Autonomous Systems'
updated_at: '2026-01-29T18:15:26.962105+00:00'
url_hash: e370a9eee695488bd01a147c4be420a42006e3ba
---

*Editor’s note: This post is part of*
[*Into the Omniverse*](https://www.nvidia.com/en-us/omniverse/news/)
*, a series focused on how developers, 3D practitioners and enterprises can transform their workflows using the latest advancements in*
[*OpenUSD*](https://www.nvidia.com/en-us/omniverse/usd/)
*and*
[*NVIDIA Omniverse*](https://www.nvidia.com/en-us/omniverse/usd/)
*.*

Open source has become essential for driving innovation in robotics and autonomy. By providing access to critical infrastructure — from simulation frameworks to AI models — NVIDIA is enabling collaborative development that accelerates the path to safer, more capable autonomous systems.

At CES earlier this month, NVIDIA introduced a new suite of open
[physical AI](https://www.nvidia.com/en-us/glossary/generative-physical-ai/)
models and frameworks to accelerate the development of
[humanoids](https://www.nvidia.com/en-us/glossary/humanoid-robot/)
,
[autonomous vehicles](https://www.nvidia.com/en-us/glossary/autonomous-vehicles/)
and other physical AI embodiments. These tools span the entire robotics development lifecycle — from high-fidelity world simulation and synthetic data generation to cloud-native orchestration and edge deployment — giving developers a modular toolkit to build autonomous systems that can reason, learn and act in the real world.

[OpenUSD](https://www.nvidia.com/en-us/glossary/openusd/)
provides the common framework that standardizes how 3D data is shared across these physical AI tools, enabling developers to build accurate
[digital twins](https://www.nvidia.com/en-us/glossary/digital-twin/)
and reuse them seamlessly from simulation to deployment.
[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)
libraries, built on OpenUSD, serve as the source of ground‑truth simulation that feeds the entire stack.

## **From Labs to the Show Floor**

At CES 2026, developers brought the NVIDIA physical AI stack out of the lab and onto the show floor, debuting machines ranging from heavy equipment and factory assistants to social and service robots.

The stack taps into
[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
world models; NVIDIA Isaac technologies, including the new
[Isaac Lab-Arena](https://developer.nvidia.com/isaac/lab-arena)
open source framework for policy evaluation; the
[NVIDIA Alpamayo](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/alpamayo/)
open portfolio of AI models, simulation frameworks and physical AI datasets for autonomous vehicles; and the
[NVIDIA OSMO](https://developer.nvidia.com/osmo)
framework to orchestrate training across compute environments.

[**Caterpillar**
’s Cat AI Assistant](https://www.linkedin.com/posts/nvidiarobotics_ces2026-activity-7417309540699906048-stk9?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAo-ztUBZUDYK16N3mS3qkG-ohtZe11AbGc)
, powered by
[NVIDIA Nemotron](https://www.nvidia.com/pt-br/ai-data-science/foundation-models/nemotron/)
open models for agentic AI and running on the NVIDIA Jetson Thor edge AI module, brings natural language interaction directly into the cab of heavy vehicles. Operators can ask “Hey Cat”-style questions and get step‑by‑step guidance, as well as adjust safety parameters by voice.

Behind the scenes, Caterpillar uses Omniverse libraries to build factory and job‑site digital twins that can help simulate layouts, traffic patterns and multi‑machine workflows. These insights are fed back into equipment and fleets before changes are deployed to job sites, making AI‑assisted operations safer and more efficient.

**LEM Surgical**
showcased its Dynamis Robotic Surgical System, which is FDA-cleared and in routine clinical use for spinal procedures. The next-generation system uses NVIDIA Jetson AGX Thor for compute,
[NVIDIA Holoscan](https://www.nvidia.com/en-us/edge-computing/holoscan/)
for real-time sensor processing and NVIDIA Isaac for Healthcare to train its autonomous arms.

LEM Surgical also uses NVIDIA Cosmos Transfer — an open, fully customizable world model that enables physically based synthetic data generation — to generate synthetic training data and the NVIDIA Isaac Sim framework for digital twin simulation. Designed as a dual-arm humanoid surgical robot for hard-tissue surgery, the Dynamis system mimics human surgeon dexterity and enables complex spinal procedures with enhanced precision, alleviating strenuous physical demands on surgeons and surgical assistants.

![](https://blogs.nvidia.com/wp-content/uploads/2026/01/ito-lem-surgical-robot-406x350.jpg)


LEM Surgical showcase.

[**NEURA Robotics**](https://www.linkedin.com/feed/update/urn:li:ugcPost:7417671927001124865/)
is building cognitive robots on a full NVIDIA stack, using
[Isaac Sim](https://developer.nvidia.com/isaac/sim)
and
[Isaac Lab](https://developer.nvidia.com/isaac/lab)
to train its 4NE1 humanoid and MiPA service robots in OpenUSD‑based digital twins before deployment in domestic settings and workplaces. The company used NVIDIA Isaac GR00T‑Mimic to post‑train the
[Isaac GR00T foundation](https://developer.nvidia.com/isaac/gr00t)
model for its platforms.

In addition, NEURA Robotics is collaborating with SAP and NVIDIA to integrate SAP’s Joule agents with its robots, using the
[Mega NVIDIA Omniverse Blueprint](https://build.nvidia.com/nvidia/mega-multi-robot-fleets-for-industrial-automation)
to simulate and refine robot behavior in complex, realistic operational scenarios before those agents and behaviors are deployed into the company’s Neuraverse ecosystem, as well as in real‑world fleets.

**AgiBot**
uses NVIDIA Cosmos Predict 2 as the world‑modeling backbone for its Genie Envisioner (GE-Sim) platform — allowing the platform to generate action‑conditioned videos grounded in strong visual and physical priors. Combining this data with Isaac Sim and Isaac Lab, as well as post‑training on AgiBot’s own data, lets policies developed in Genie Envisioner transfer more reliably to Genie2 humanoids and compact Jetson Thor-powered tabletop robots.

[**Intbot**](https://www.youtube.com/watch?v=u9sI_fTM_So)
is using the NVIDIA Cosmos Reason 2 open model to give its social robots a “sixth sense” for the real world — using the model’s reasoning capabilities to identify simple social cues and safety context that go beyond simple scripted tasks. In its
[Cosmos Cookbook recipe](https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/inference/reason2/intbot_showcase/inference.html)
, Intbot demonstrates how reasoning vision language models can aid robots in deciding when to speak and how to more naturally interact with humans.

## **How Robotics Developers Are Using New Toolkits and Frameworks**

NVIDIA recently introduced Agile, an Isaac Lab-based engine for humanoid loco‑manipulation that packages a full, sim‑to‑real‑verified workflow for training robust
[reinforcement learning](https://www.nvidia.com/en-us/glossary/reinforcement-learning/)
policies on platforms like the Unitree G1 and LimX Dynamics TRON.

Robotics developers can use Agile’s built‑in task configurations, Markov Decision Process mathematical models for decision-making, training utilities and deterministic evaluation tools to tune policies. Developers can then stress‑test these policies in Isaac Lab and transfer locomotion and whole‑body behaviors to real-world robots more reliably and efficiently.

VIDEO

Hugging Face and NVIDIA are bringing together their robotics communities by integrating NVIDIA Isaac GR00T N models and simulation frameworks into the
[LeRobot ecosystem](https://huggingface.co/lerobot)
. Developers can now access Isaac GR00T N1.6 models and Isaac Lab‑Arena directly within LeRobot to streamline policy training and evaluation.

Plus, Hugging Face’s open‑source Reachy 2 humanoid is now fully interoperable with NVIDIA Jetson Thor, enabling the direct deployment of advanced vision language action (VLA) models for robust real‑world performance.

[ROBOTIS](https://www.linkedin.com/posts/yoonseokpyo_robotis-aiworker-aimanipulator-ugcPost-7351915450059907072-Bhl6/?utm_source=share&utm_medium=member_ios&rcm=ACoAAAHM3LUBdKoQgtNLqhTl_3CNBhYDXsVf0sM)
, a leading developer of smart servos, industrial actuators, manipulators, open-source humanoid platforms and educational robotic kits, built an open source sim-to-real pipeline using NVIDIA Isaac technologies. The workflow starts with high‑fidelity data generation in Isaac Sim, scales up training sets using GR00T‑Mimic for augmentation and then fine‑tunes a VLA‑based Isaac GR00T N model that deploys directly to hardware — accelerating the transition from simulation to robust real‑world tasks.

VIDEO

## **Get Plugged In**

Learn more about OpenUSD and robotics development by exploring these resources:

* **Read**
  [this technical blog](https://developer.nvidia.com/blog/building-generalist-humanoid-capabilities-with-nvidia-isaac-gr00t-n1-6-using-a-sim-to-real-workflow/)
  to learn how to develop generalist humanoid capabilities with NVIDIA Isaac and GR00T N1.6.
* **Read**
  [this technical blog](https://developer.nvidia.com/blog/simplify-generalist-robot-policy-evaluation-in-simulation-with-nvidia-isaac-lab-arena/)
  to learn how to evaluate generalist robot policies in simulation using NVIDIA Isaac Lab – Arena.
* **Learn**
  how to post-train Isaac GR00T with this
  [two-part video tutorial](https://www.youtube.com/watch?v=L-WriIVOyYE&t=4s)
  .
* **Watch**
  NVIDIA founder and CEO Jensen Huang’s
  [CES special presentation](https://www.youtube.com/watch?v=0NBILspM4c4)
  .
* **Improve**
  skills for robotics development with the self-paced
  [robotics learning path](https://www.nvidia.com/en-us/learn/learning-path/robotics/?ncid=so-yout-478533-vt48)
  .
* **Participate**
  in the
  [Cosmos Cookoff](https://luma.com/nvidia-cosmos-cookoff?utm_source=web)
  , a hands-on physical AI challenge where developers use Cosmos Reason to power robotics, autonomous systems and vision AI workflows.