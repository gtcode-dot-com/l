---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-30T02:44:09.529772+00:00'
exported_at: '2026-09-30T02:44:11.107755+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/ibms-granite-4-2-models-learn-to-think-and-act-inside-environments
structured_data:
  about: []
  author: ''
  description: 'IBM has released Granite 4.2, its first family of dense, decoder-only
    reasoning language models, in three sizes: 3B, 8B, and 30B parameters. Announced
    on August 25, 2026 with weights published under the Apache 2.0 licens...'
  headline: IBM’s Granite 4.2 Models Learn to Think and Act Inside Environments
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/ibms-granite-4-2-models-learn-to-think-and-act-inside-environments
  publisher:
    logo: /favicon.ico
    name: GTCode
title: IBM’s Granite 4.2 Models Learn to Think and Act Inside Environments
updated_at: '2026-09-30T02:44:09.529772+00:00'
url_hash: d9bebcb776571bf8e6ae3bc4bf35cf75ab41b726
---

IBM has released Granite 4.2, its first family of dense, decoder-only reasoning language models, in three sizes: 3B, 8B, and 30B parameters. Announced on August 25, 2026 with weights published under the Apache 2.0 license, the release gives every Granite model a switchable thinking mode and sends the two larger sizes through reinforcement learning inside real software-engineering, terminal, and web-search environments.

In a
[technical walkthrough of the build](https://huggingface.co/blog/ibm-granite/granite-4-2)
, the Granite Team at IBM describes a pipeline that starts with pre-training from scratch on roughly 15 trillion tokens, with a five-phase schedule that extends the context window to 512K tokens. Supervised fine-tuning follows on about 7.2 million samples of chain-of-thought, reasoning, and agentic-trajectory data. The release’s center of gravity, though, is what comes after: a multi-stage reinforcement learning pipeline in which each stage is a separate training run targeting one capability, warm-started from the previous stage’s checkpoint.

All three sizes run foundational RL on verifiable rewards — math problems with checkable answers, code graded by hidden unit tests, instruction-following tasks with format checkers — plus short “booster” stages for specific skills. Only the 8B and 30B models continue into the agentic block: three stages where the model acts inside a live environment and is rewarded on whether the task was actually solved. In the software-engineering stage, driven by the OpenHands harness, the model edits real repositories and passes only if the hidden test suite passes. The terminal stage drops it into a live shell with up to 64 environment turns per rollout. The search stage has it answer multi-hop questions through live web-search calls, scored by an LLM judge.

Every model then finishes with RLHF for preference and safety, which also applies a reasoning-length penalty to discourage the verbose chains earlier stages can produce.

## What Switchable Thinking Looks Like in Practice

Each Granite 4.2 model exposes three operating modes through its chat template. Thinking mode, the default, produces a full chain of thought inside dedicated tags before the final answer. Non-thinking mode answers directly. A low-effort setting sits between the two, spending a short reasoning budget on easy questions. In multi-turn conversations, prior turns’ thinking is stripped by default to conserve context.

Native tool calling is built into the same template: the model reasons about which tool to call and why before emitting the call, in the OpenAI function-calling format, so it plugs into agentic harnesses served through vLLM or SGLang without extra adapters. According to the
[Granite 4.2 model collection](https://huggingface.co/collections/ibm-granite/granite-42-language-models)
, all three weights are publicly downloadable, and the
[30B model card](https://huggingface.co/ibm-granite/granite-4.2-30b)
confirms the flagship was post-trained from the Granite 4.1 30B base. The models are tested across 12 languages, including English, German, Japanese, Arabic, Korean, and Chinese.

## The Numbers IBM Reports

IBM evaluated the family across agentic coding, general tool use, reasoning, chat, and long context, using a framework built on the NeMo Evaluator SDK. The scores below are the company’s own reported figures.

* **SWE-Bench Verified:**
  57.00 (30B), 47.67 (8B)
* **Terminal-Bench 2.1:**
  29.24 (30B), 20.56 (8B)
* **AIME25 math:**
  89.17 (30B), 86.67 (8B), 78.33 (3B)
* **GPQA science:**
  66.41 (30B), 64.14 (8B), 54.80 (3B)
* **RULER long context at 128K:**
  81.38 (30B), 71.41 (8B), 55.30 (3B)

The pattern matches the training design. Scores rise consistently with size across math, science, and code reasoning, and the agentic-coding benchmarks that depend on the 8B and 30B models’ exclusive agentic-RL block show the widest gap between sizes. The 3B model, which runs none of the environment stages, is not reported on the SWE-Bench or Terminal-Bench suites at all.

## Training Agents Without a Value Network

The RL machinery is worth a closer look because it is where most of the release’s engineering sits. Every stage trains with asynchronous GRPO, a group-relative policy optimization method that scores each response against the mean reward of the other samples drawn for the same prompt, eliminating the separate value network many RL pipelines require. Generation and training run on separate GPU pools that never block each other: workers keep sampling trajectories into a shared buffer, and the trainer streams updated weights back mid-rollout. A guardrail keeps generators from drifting more than one update behind, and truncated importance sampling clamps the effect of stale tokens.

The environments attach through NeMo-Gym, which presents verifiers, tools, and sandboxes behind a uniform interface, while NeMo-RL drives the training loop on Megatron-Core with vLLM generation. The practical consequence is that a rule-based math checker and a full repository sandbox look identical to the training loop, which is what makes the staged curriculum feasible to run. IBM trained the models on an NVIDIA GB200 NVL72 cluster hosted by CoreWeave, with a 72-GPU NVLink domain and 400 Gb/s InfiniBand fabric.

IBM also shipped quantized variants of the family: FP8 without calibration, NVFP4 and MXFP4 calibrated on 2,000 samples from the SFT dataset, and fourteen GGUF formats via llama.cpp for reduced-memory deployment.

## Where Granite 4.2 Fits IBM’s Line

The release continues a deliberate division of labor in IBM’s open model strategy. Earlier Granite generations were positioned as strong instruction-following assistants; the company covered Granite Speech 5.0, released the same day,
[in a separate announcement](https://www.unite.ai/ibm-says-granite-speech-5-0-transcribes-3-5-hours-of-speech-in-one-second/)
focused on transcription speed. Granite 4.2 is the language-model line’s turn at explicit reasoning, and it arrives with the full training recipe, data-mixture proportions, and per-stage hyperparameters published alongside the weights.

All three models, the quantized variants, the GitHub repository, and the documentation are available under Apache 2.0, with the 30B flagship sized for a single multi-GPU serving node and the 3B aimed at lighter deployments where the thinking switch still applies.