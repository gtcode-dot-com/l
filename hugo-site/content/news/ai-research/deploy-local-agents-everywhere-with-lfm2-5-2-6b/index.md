---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-17T06:19:33.919859+00:00'
exported_at: '2026-09-17T06:19:37.380707+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b
structured_data:
  about: []
  author: ''
  description: A Blog post by Liquid AI on Hugging Face
  headline: Deploy local agents everywhere with LFM2.5-2.6B
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Deploy local agents everywhere with LFM2.5-2.6B
updated_at: '2026-09-17T06:19:33.919859+00:00'
url_hash: ea7f6df3de1a3ce42418de5c890af7c1180b76d6
---

**LFM2.5-2.6B**

is built to power capable agents entirely on-device. It supports tool calling and multi-step workflows while staying small and fast enough for everyday hardware, from laptops to phones. This enables developers to deploy agents everywhere, keep data private on the device, and scale usage without a cloud inference bill.

* **Best-in-class agent:**
  Competitive with models 4x larger on tool use, instruction following, and multi-step agentic tasks.
* **Agentic reinforcement learning:**
  Trained inside the most popular agentic harnesses to improve compatibility.
* **Efficient inference**
  : 220 tok/s on an Apple M5 Max and 113 tok/s on an AMD Ryzen CPU, in under 2.5 GB of memory.

[![lfm2_5_2_6b_evaluations](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/DaHxE_1x4xMB_5c-P0AXF.png)](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/DaHxE_1x4xMB_5c-P0AXF.png)

## How we built a reliable agentic model for edge devices

LFM2.5-2.6B is pre-trained on ~34T tokens, with a mid-training phase that extends the context window to 128K. Post-training then turns the base model into an agent in four stages:

1. **Supervised fine-tuning (SFT):**
   two rounds of SFT, weighted heavily toward agentic data like tool use, web search, and harness trajectories.
2. **Teacher specialization:**
   train one specialist teacher per domain (math, code, tool use, and more).
3. **Multi-domain on-policy distillation (MOPD):**
   distill the specialist teachers into a single student.
4. **Agentic Reinforcement Learning (Agentic RL):**
   run multi-turn RL inside real agent harnesses, where the model learns to work across different tools, system prompts, and multi-turn task environments.

[![LFM2.5-2.6B-Training-Recipe](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/jg-qhMYLMPi6PAslhT9S_.png)](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/jg-qhMYLMPi6PAslhT9S_.png)

The Agentic RL pipeline separates model optimization, inference, and environment execution into distinct components. The
**Training Engine**
optimizes the model, while the
**Rollout Engine**
generates actions using the latest policy. The
**RL framework**
orchestrates the training loop by launching rollouts, collecting trajectories and rewards, and updating the model.

Actions are executed within a
**Sandbox Service**
, where the
**Blackbox Harness**
hosts the agent (e.g., OpenClaw or Hermes Agent) and coordinates interactions with the task environment. The
**Harness Proxy**
lets us treat agentic harnesses as black boxes with no modification, while transparently capturing the token-level trajectories needed to reconstruct and validate RL training samples.

[![LFM2.5-2.6B-Agentic-RL](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/E8SUiijksSkOvMs9tMjlw.png)](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/E8SUiijksSkOvMs9tMjlw.png)

## Benchmark results

We evaluated LFM2.5-2.6B against models up to ~4x its size on STEM, instruction following, tool use, and agentic tasks. It is the smallest model in the group, yet it competes with and often beats the rest.

| Benchmark | LFM2.5-2.6B (2.6B) | gemma-4-E2B-it (5.1B) | gemma-4-E4B-it (8B) | Qwen3.5-4B (4.7B) | Qwen3.5-9B (9.7B) |
| --- | --- | --- | --- | --- | --- |
| AA Omniscience | -29.50 | -74.47 | -49.03 | -54.30 | -50.43 |
| AIME25 | 51.87 | 26.33 | 34.27 | 49.33 | 56.07 |
| LiveCodeBenchv6 | 59.41 | 54.92 | 63.77 | 60.85 | 69.86 |
| IFBench | 59.17 | 34.08 | 39.24 | 48.40 | 56.47 |
| Multi-IF | 80.07 | 69.44 | 77.35 | 55.67 | 62.55 |
| IFStruct | 85.49 | 64.85 | 76.65 | 36.25 | 78.50 |
| BFCLv4 | 56.88 | 36.98 | 46.39 | 50.56 | 60.13 |
| ToolSandbox | 77.83 | 52.40 | 65.00 | 75.55 | 76.44 |
| τ³-Bench Banking | 5.67 | 3.35 | 4.12 | 5.45 | 5.15 |
| Claw-Eval average (EN) | 62.85 | 53.14 | 58.02 | 62.28 | 66.53 |
| PinchBench | 68.22 | 44.24 | 55.09 | 71.26 | 71.45 |
| BrowseComp+ (OpenClaw) | 26.89 | 8.31 | 15.90 | 24.46 | 27.23 |

For your app, the strengths are instruction following and tool use. LFM2.5-2.6B tops every instruction-following benchmark here, and every tool-use benchmark except BFCLv4, where only the 9.7B Qwen edges ahead. On agentic tasks, it beats both Gemma models and stays even with the Qwens. It also leads on knowledge and stays close on math. Coding is the one place the larger models keep a clear lead, so reach for something bigger there.

## Inference speed on CPU and GPU

LFM2.5-2.6B ships with day-one support across the inference ecosystem, including llama.cpp, MLX, vLLM, SGLang, and ONNX.

**CPU inference.**
Due to its efficient LFM2 architecture, LFM2.5-2.6B is the fastest model we tested, with decode speeds of 220 tokens/s on an M5 Max and 113 tokens/s on a Ryzen AI Max+ 395. At 30 tokens/s, it allows you to run capable agents even on a phone.

[![lfm2_5_2_6b_cpu_inference](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/oMx6D-ydeHXGa1m0p0iq2.png)](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/oMx6D-ydeHXGa1m0p0iq2.png)

**GPU inference.**
LFM2.5-2.6B is the fastest model in its size class, reaching almost 15K output tokens per second at high concurrency, roughly 1.3B tokens per day on a single H100.

[![lfm2_5_2_6b_gpu_inference](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/0kif4TRZzjmPvvxo_JJ2K.png)](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/0kif4TRZzjmPvvxo_JJ2K.png)

## How to use LFM2.5-2.6B

Reach for LFM2.5-2.6B when you need on-device agents for high-volume workloads.

Install the latest version of
`transformers`
(compatible with
`transformers&gt;=5.0.0`
):

```
pip install -U transformers
```

Then load and run the model:

```
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "LiquidAI/LFM2.5-2.6B"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16",

)
tokenizer = AutoTokenizer.from_pretrained(model_id)

prompt = "What is C. elegans?"
input_ids = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
).to(model.device)

output = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.2,
    top_k=80,
    repetition_penalty=1.05,
    max_new_tokens=512,
)
print(tokenizer.decode(output[0], skip_special_tokens=False))
```

## LFM2.5-2.6B demo

Check out this
[browser demo of LFM2.5-2.6B powering a research agent](https://huggingface.co/spaces/LiquidAI/LFM2.5-2.6B-WebGPU)
. The agent helps you research specific questions and generates a summary.

## Get Started

Both LFM2.5-2.6B and LFM2.5-2.6B-Base are available on Hugging Face today.

With LFM2.5, we're delivering on our vision of AI that runs anywhere. These models are:

* **Download:**
  [LFM2.5-2.6B-Base](https://huggingface.co/LiquidAI/LFM2.5-2.6B-Base)
  and
  [LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)
  on Hugging Face.
* **Try:**
  run the WebGPU demo in your browser, no setup needed.
* **Use in your harness:**
  follow our
  [guide](https://docs.liquid.ai/examples/agent-harnesses)
  on how to run a local agent, like OpenClaw, Hermes Agent, and Pi.

We can't wait to see what you build.

## Citation

Please cite this article as:

```
Liquid AI, "LFM2.5-2.6B: Deploy Agents Everywhere", Liquid AI Blog, Aug 2026.
```

Or use the BibTeX citation:

```
@article{liquidAI202626B,
  author  = {Liquid AI},
  title   = {LFM2.5-2.6B: Deploy Agents Everywhere},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-2-6b},
}
```