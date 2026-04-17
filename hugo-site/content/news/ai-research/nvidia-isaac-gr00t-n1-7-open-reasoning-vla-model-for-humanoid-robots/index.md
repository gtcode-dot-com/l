---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-17T16:15:37.966100+00:00'
exported_at: '2026-04-17T16:15:40.526742+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/gr00t-n1-7
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: 'NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/gr00t-n1-7
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots'
updated_at: '2026-04-17T16:15:37.966100+00:00'
url_hash: 3a86ed33d6184ca08b138271176218366da0ae3a
---

# NVIDIA Isaac GR00T N1.7: Open Reasoning VLA Model for Humanoid Robots

We are releasing

**NVIDIA Isaac GR00T N1.7 (Early Access)**

— an open-source, commercially licensed Vision-Language-Action model for humanoid robots, built on a simple premise: human data is the most scalable source of robot intelligence.

---

## TL;DR

* 🤖
  **GR00T N1.7**
  — open-source, commercially licensed humanoid foundation model, available now on
  [Hugging Face](https://huggingface.co/collections/nvidia/gr00t-n17)
  and
  [GitHub](https://github.com/NVIDIA/Isaac-GR00T)
* 🏭
  **Factory-floor ready**
  — commercial licensing enables production deployments today, across material handling, packaging, and inspection
* 🧠
  **Reasoning built for multi-step tasks**
  — task and subtask-level reasoning improve reliability on complex workflows
* 🖐
  **Expanded dexterous manipulation**
  — finger-level control enables contact-rich tasks like small parts assembly
* 🔬
  **First-ever dexterity scaling law**
  — trained on 20,000+ hours of human egocentric video, more human data directly and predictably improves robot dexterity — without mass teleoperation
* 🚀
  [GitHub](https://github.com/NVIDIA/Isaac-GR00T)
  |
  [Hugging Face](https://huggingface.co/collections/nvidia/gr00t-n17)
  | Supports LeRobot dataset format

---

## What is GR00T N1.7?

GR00T N1.7 is a 3B-parameter Vision-Language-Action (VLA) model that maps visual observations and natural language instructions to continuous robot actions. It uses an
**Action Cascade**
architecture — a dual-system design that separates high-level reasoning from low-level motor control:

* **System 2 (Vision-Language Model):**
  A Cosmos-Reason2-2B backbone processes image tokens and language instructions to produce high-level action tokens. This is where task decomposition and multi-step reasoning happen.
* **System 1 (Diffusion Transformer):**
  A 32-layer DiT takes the VLM's output and live robot state, then denoises them into precise motor commands in real time.

**Inputs:**
RGB image frames (any resolution) + language instruction + robot proprioceptive state (joint positions, velocities, EEF poses)

**Outputs:**
Continuous-value action vectors mapped to the robot's degrees of freedom

Validated across loco-manipulation, tabletop manipulation, and dexterous bimanual tasks on Unitree G1, Bimanual Manipulator YAM, and AGIBot Genie 1.

---

## Training on Human EgoCentric Video Data

The central research that has been used for GR00T N1.7 is EgoScale — pre-training on
**20,854 hours of human egocentric video**
spanning 20+ task categories, from manufacturing and retail to healthcare and home environments. This is a significant step up from the few thousand hours of robot teleoperation data used to train N1.6.

The intuition: humans and robots share similar embodiments — two hands, a first-person viewpoint, a world full of objects to manipulate. Training on sensorized human video (ego cameras, wrist cameras, hand tracking) gives the model rich manipulation priors without requiring every behavior to be demonstrated on a physical robot first. It moves pre-training beyond what teleoperation can scale to.

The key finding from this work:
**we discovered the first-ever scaling law for robot dexterity.**
More human egocentric data produces predictable, consistent improvements in dexterous manipulation capability — going from 1k to 20k hours more than doubles average task completion. This scaling law translates directly into dexterous manipulation capability — enabling 22 DoF hands to perform contact-rich tasks that generalist robot models have historically struggled to achieve.

---

## Inference & Deployment

Install and launch a policy server against your embodiment:

```
git clone --recurse-submodules https://github.com/NVIDIA/Isaac-GR00T
cd Isaac-GR00T
bash scripts/deployment/dgpu/install_deps.sh
source .venv/bin/activate
```

```
uv run python gr00t/eval/run_gr00t_server.py \
    --embodiment-tag GR1 \
    --model-path nvidia/GR00T-N1.7
```

Then query it from your environment loop:

```
from gr00t.policy.server_client import PolicyClient

policy = PolicyClient(host="localhost", port=5555)

obs, info = env.reset()
action, info = policy.get_action(obs)
obs, reward, done, truncated, info = env.step(action)
```

Inference performance at 4 denoising steps, single camera view can be found
[here.](https://github.com/NVIDIA/Isaac-GR00T-EA/blob/main/scripts/deployment/README.md#performance)

GR00T N1.7 is commercially licensed and supported on NVIDIA Ampere, Hopper, Lovelace, Blackwell, and Jetson platforms.

---

## Fine-Tuning on Your Robot

N1.7 supports fine-tuning on custom embodiments using the LeRobot dataset format. Pre-registered embodiments include
`UNITREE_G1`
,
`LIBERO_PANDA`
,
`OXE_WIDOWX`
, and others — or register your own:

```
CUDA_VISIBLE_DEVICES=0 uv run python gr00t/experiment/launch_finetune.py \
    --base-model-path nvidia/GR00T-N1.7 \
    --dataset-path <YOUR_DATASET_PATH> \
    --embodiment-tag <YOUR_EMBODIMENT> \
    --modality-config-path <YOUR_MODALITY_CONFIG> \
    --num-gpus 1 \
    --output-dir <OUTPUT_PATH> \
    --max-steps 2000 \
    --global-batch-size 32
```

**Upgrading from N1.6?**
It's a drop-in swap — point
`--model-path`
to
`nvidia/GR00T-N1.7`
and your existing embodiment configs and workflows carry over. The main differences are the upgraded VLM backbone (Cosmos-Reason2-2B) and EgoScale pre-training, which improves out-of-the-box dexterity and generalization before any fine-tuning.

---

If you build something with GR00T N1.7, we'd love to hear from you.