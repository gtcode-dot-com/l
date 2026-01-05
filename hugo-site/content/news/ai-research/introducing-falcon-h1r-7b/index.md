---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-05T12:15:26.827001+00:00'
exported_at: '2026-01-05T12:15:29.058503+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/tiiuae/falcon-h1r-7b
structured_data:
  about: []
  author: ''
  description: A Blog post by Technology Innovation Institute on Hugging Face
  headline: Introducing Falcon H1R 7B
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/tiiuae/falcon-h1r-7b
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Introducing Falcon H1R 7B
updated_at: '2026-01-05T12:15:26.827001+00:00'
url_hash: 4478d918248431ba0efb3be9b3e88d64002254cc
---

# Introducing Falcon H1R 7B

[![cover](https://cdn-uploads.huggingface.co/production/uploads/66db041dd04c920ebf3198ff/NGuXCP0_Xhqq4lbviNlr2.png)](https://cdn-uploads.huggingface.co/production/uploads/66db041dd04c920ebf3198ff/NGuXCP0_Xhqq4lbviNlr2.png)
> Check out
> [our official blogpost](https://falcon-lm.github.io/blog/falcon-h1r-7b)
> for an interactive experience.

We’re excited to unveil
**Falcon H1R 7B**
, a decoder-only large language model, developed by the
[Technology Innovation Institute (TII)](https://www.tii.ae/ai-and-digital-science)
in Abu Dhabi. Building upon the robust foundation of Falcon-H1 Base model,
**Falcon H1R 7B**
takes a major leap forward in reasoning capabilities.

Despite its modest 7 billion‑parameter size,
**Falcon H1R 7B**
matches or outperforms state‑of‑the‑art reasoning models that are 2–7× larger, proving its exceptional parameter efficiency and does so consistently across a wide range of reasoning‑intensive benchmarks.

Its performance stems from a carefully curated training set and a two‑stage pipeline of efficient supervised fine‑tuning followed by RL scaling.

**Falcon H1R 7B**
’s design rests on three key axes of reasoning efficiency: speed, token‑efficiency, and accuracy that together set the “3‑D limits” of performance. By integrating
[Deep Think with confidence (DeepConf)](https://github.com/facebookresearch/deepconf)
during test‑time scaling, the model achieves state‑of‑the‑art efficiency, delivering substantial accuracy gains while generating fewer tokens than competing models.

This iteration includes:

## Training recipe

**Falcon H1R 7B**
’s training regimen is a two‑stage, data‑driven pipeline designed to maximize reasoning quality.

* **Cold‑start supervised fine‑tuning (SFT)**
  : Starting from the Falcon‑H1‑7B backbone, we train on curated datasets that contain
  **step‑by‑step long‑form reasoning traces**
  across three domains: mathematics, coding, and science. We additionally include non-reasoning domains: chat, tool‑calling, safety, etc.
  **Difficulty‑aware filtering**
  is applied during SFT to prioritize challenging examples. Training targets
  **extremely long response lengths (up to 48 k tokens)**
  .
* **Reinforcement learning with GRPO**
  : The SFT checkpoint is further refined using the
  **GRPO**
  algorithm. Rewards are given for correct reasoning chains, encouraging the model to generate high‑quality, diverse outputs while still staying within the tokens budget-limit. The RL stage
  **balances exploration and exploitation**
  to improve output quality while respecting token constraints.

## Model's Capabilities

Below, the bar plot compares
**Falcon H1R 7B**
’s performance across math, code & agentic, and general benchmarks against the leading 7B to 47B models.

* **Math**
  :
  **Falcon H1R 7B**
  leads (
  *73.96 %*
  ) by a wide margin, beating the next best (Apriel 1.5 15B at 69.32 %) and outpacing all larger baselines such as Qwen3‑32B (63.66 %) and Nemotron H 47B (49.72 %).
* **Code & Agentic**
  :
  **Falcon H1R 7B**
  has the highest score in this group (
  *33.95 %*
  ), ahead of Qwen3‑32B (33.40 %) and Apriel 1.5 (31.60 %).
* **General**
  :
  **Falcon H1R 7B**
  remains highly competitive (
  *49.48 %*
  ), sitting just below Apriel 1.5 (53.10 %) and Phi 4 Reasoning Plus 14B (51.18 %).

|  |  |
| --- | --- |
| overall   **Overall capabilities** | math   **Math capabilities** |
| code   **Code & agentic capabilities** | general   **General capabilities** |

### Math Benchmarks

**Falcon H1R 7B**
delivers top‑tier math results across a spectrum of difficulty levels, all while staying at only 7B parameters.

| Benchmark | Falcon H1R 7B | Next best |
| --- | --- | --- |
| **AIME‑24** | 88.1 % | Apriel 1.5 15B – 86.2 % |
| **AIME‑25** | 83.1 % | Apriel 1.5 15B – 80.0 % |
| **HMMT‑25** | 64.9 % | Apriel 1.5 15B – 61.0 % |
| **AMO-Bench** | 36.3 % | DeepSeek R1‑0528 Qwen3‑8B – 23.3 % |

|  |  |
| --- | --- |
| aime24   **AIME 24** | aime25   **AIME 25** |
| hmmt   **HMMT 25** | amo   **AMO-Bench** |
| math500   **Math 500** |

### Code & agentic Benchmarks

**Falcon H1R 7B**
delivers solid reasoning across a spectrum of code and agentic challenges.

| Benchmark | Falcon H1R 7B | Relative standing |
| --- | --- | --- |
| **LCB v6** | 68.6 % | Highest of all models – outperforms even the 32B Qwen3 by ~7 pp |
| **SciCode (sub-problem)** | 28.3 % | Best for <8B models |
| **TB Hard** | 4.96 % | Second best (Apriel 1.5 15B at 9.9 %) and beats the 8B/32B Qwen3 models |

|  |  |
| --- | --- |
| lcbv6   **LCB v6** | scicode-sub   **SciCode (sub-problem)** |
| tb-hard   **TB Hard** |

### General Benchmarks

**Falcon H1R 7B**
proves its versatility across a broad set of general‑purpose tasks, consistently matching or surpassing larger competitors while staying at only 7B parameters.

| Benchmark | Falcon H1R 7B | Relative standing |
| --- | --- | --- |
| **GPQA‑D** | 61.3 % | On-par with other 8B models (Qwen3‑8B 61.2 %, DeepSeek 61.4 %) |
| **MMLU‑Pro** | 72.1 % | Outperforms all 8B rivals and close to the 14/32B cohort. |
| **HLE** | 11.1 % | Slightly behind Apriel 1.5 15B and beats every other 8B/32B variant |
| **IFBench** | 53.4 % | Second best after Apriel (55.8 %) and outpaces all 8B models; demonstrates robust instruction‑following at a compact scale. |

|  |  |
| --- | --- |
| gpqa-d   **GPQA-D** | mmlu-pro   **MMLU-Pro** |
| hle   **HLE** | ifbench   **IFBench** |

## Inference

Here we benchmark
**Falcon H1R 7B**
’s token throughput per GPU against Qwen3 8B under realistic test‑time scaling workloads.

**Falcon H1R 7B**
outperforms Qwen3 8B across the board, especially as batch size grows. In the typical test‑time scaling case (512 → 32k), Falcon reaches roughly
**1,000 tokens/s/GPU at batch 32**
and
**≈ 1,500 at batch 64**
, nearly double Qwen3’s rates. The advantage widens further for longer inputs (8k → 16k), where Falcon again delivers ≈ 1,800 tokens/s/GPU while Qwen3 stays below 900. The hybrid Transformer–Mamba backbone is the key to this superior scaling and memory efficiency.

|  |  |
| --- | --- |
| i512-032k   **Input=512, Output=32k** | i8k-016k   **Input=8k, Output=16k** |

## Test time scaling

Test‑time scaling (TTS) boosts a model’s reasoning by running many parallel solution chains and aggregating the best answer, unlocking latent capability without extra training.
In
**Falcon H1R 7B**
we employ
**Deep Think with Confidence (DeepConf)**
, a lightweight, confidence‑aware filtering method that dynamically discards low‑quality reasoning traces during or after generation. DeepConf leverages the model’s own next‑token confidence scores to identify and prune noisy traces,
**requiring no additional training or hyper‑parameter tuning**
.

**Falcon H1R 7B**
thrives at high batch sizes and is token‑efficient, generating fewer tokens per inference for a given accuracy level, making TTS especially effective and positioning the model on a new Pareto frontier of performance vs. inference compute.

The grid below shows how many tokens were generated for a given accuracy.
**Falcon H1R 7B**
sits on the Pareto frontier of
**low cost, high performance**
:

* **AIME 24 / 25**
  – 96.7 % accuracy with <100 M tokens, beating every other 8B model and matching the best 14/32B systems.
* **AMO-Bench**
  – 35.9 % accuracy with just 217 M tokens, surpassing every other model.

|  |  |
| --- | --- |
| tts-aime24   **AIME 24** | tts-aime25   **AIME 25** |
| tts-amo   **AMO-Bench** |

**Falcon H1R 7B**
demonstrates that a 7 billion‑parameter model can rival larger peers in reasoning tasks while delivering efficient inference, making it an attractive choice for developers and researchers alike.

## Open Source Commitment

In line with our mission to foster AI accessibility and collaboration,
**Falcon H1R 7B**
is released under the
[**Falcon LLM license**](https://falconllm.tii.ae/falcon-terms-and-conditions.html)
. We hope the AI community finds these models valuable for research, application development, and further experimentation.
**Falcon H1R 7B**
is a continuation of our efforts to create more capable and efficient foundation models. We welcome feedback and collaboration from the community as we continue to refine and advance the capabilities of these models.

## Useful Links

## Acknowledgments

We would like to thank the following TII collegues for their valuable support during this project: Younes Belkada, Ilyas Chahed, Dhia Eddine Rhaiem, Maksim Velikanov and Jingwei Zuo.

## Citation

```
@article{falconh1r,
    title = {Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling},
    url = {https://github.com/tiiuae/falcon-h1r/blob/main/tech_report.pdf},
    author = {Falcon Reasoning Team, Iheb Chaabane, Puneesh Khanna, Suhail Mohmad, Slim Frikha, Shi Hu, Abdalgader Abubaker, Reda Alami, Mikhail Lubinets, Mohamed El Amine Seddik, Hakim Hacid},
    month = {December},
    year = {2025}
}
```