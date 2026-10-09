---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T22:15:40.055179+00:00'
exported_at: '2026-03-18T22:15:42.601418+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/nemotron-3-nano-4b
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: 'Nemotron 3 Nano 4B: A Compact Hybrid Model for Efficient Local AI'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/nemotron-3-nano-4b
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Nemotron 3 Nano 4B: A Compact Hybrid Model for Efficient Local AI'
updated_at: '2026-03-18T22:15:40.055179+00:00'
url_hash: 310658f5b68091d3b06cb877df9b5986c7360bf9
---

# Nemotron 3 Nano 4B: A Compact Hybrid Model for Efficient Local AI

We are excited to introduce

[Nemotron 3 Nano 4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)

, the newest and most compact member of the

[Nemotron 3 family](https://research.nvidia.com/labs/nemotron/Nemotron-3/)

. Leveraging hybrid Mamba-Transformer architecture, this model is designed for efficiency and accuracy in a targeted set of capabilities, setting a new standard for lightweight small language models. The model is available across any NVIDIA GPU-enabled platforms and combines state-of-the-art instruction following and exceptional tool use with minimal VRAM footprint.

With just 4 billion parameters, Nemotron 3 Nano 4B is compact enough to run at the edge on NVIDIA Jetson platforms (Jetson Thor/Jetson Orin Nano) as well as NVIDIA DGX Spark and NVIDIA RTX GPUs. This enables faster response times, enhanced data privacy, and flexible deployment while keeping inference costs low.

[Nemotron 3 Nano 4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-4B-BF16)
is our first model specifically optimized for on-device deployment and purpose-built to power local conversational agents and personas across GeForce RTX, Jetson and Spark customer use cases. This model achieves state-of-the-art accuracy and efficiency in several dimensions key to production use on the edge:

* Instruction following (IFBench, IFEval): state-of-the-art in its size class
* Gaming agency/intelligence (Orak): state-of-the-art in its size class
* VRAM efficiency (peak memory use): lowest VRAM footprint in its size class under both low and high ISL/OSL settings (\*1)
* Latency: lowest TTFT in its size class under high ISL settings (\*1)

(\*1) Efficiency benchmarks were measured on an RTX 4070 using Llama.cpp with Q4\_K\_M-quantized versions of both models.

Furthermore, Nemotron 3 Nano 4B delivers excellent tool-use performance and is highly competitive in hallucination avoidance. Together, these capabilities demonstrate the model’s strong suitability for edge use cases.

Nemotron 3 Nano 4B was pruned and distilled from
[Nemotron Nano 9B v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2)
using the
[Nemotron Elastic](https://arxiv.org/abs/2511.16664)
framework, allowing it to inherit the strong reasoning capabilities as a hybrid reasoning model. It was further post-trained with a new recipe derived from
[Nemotron 3 Post-training data](https://huggingface.co/collections/nvidia/nemotron-post-training-v3)
, enabling the model to excel at task solving even without explicit thinking.

Finally, as an open-source model, it empowers the ecosystem to customize, fine-tune, and optimize it for domain-specific use cases.

[![accuracy_table_resized](https://cdn-uploads.huggingface.co/production/uploads/6629acb6b0c1d952a6f6e545/BNxWA0EmxJluCRsbOy_pd.png)](https://cdn-uploads.huggingface.co/production/uploads/6629acb6b0c1d952a6f6e545/BNxWA0EmxJluCRsbOy_pd.png)

For
[Orak](https://github.com/krafton-ai/Orak)
, we evaluated the models in tactical games such as
*Super Mario*
,
*Darkest Dungeon*
and
*Stardew Valley*
.

## Training Recipe for Nemotron 3 Nano 4B

[![Screenshot 2026-03-16 at 12.47.17 PM](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/s3h2Gc7HQAuOuzd_My9dA.png)](https://cdn-uploads.huggingface.co/production/uploads/5fc181c4ea82dd667bb0ffae/s3h2Gc7HQAuOuzd_My9dA.png)

### Compressing 9B → 4B with Nemotron Elastic

Nemotron 3 Nano 4B was derived from
[Nemotron Nano 9B v2](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-9B-v2)
using the
[Nemotron Elastic](https://arxiv.org/abs/2511.16664)
technology. Rather than training a 4B model from scratch, or performing separate stages of pruning, candidate search, and distillation, as in an existing LLM compression technique, Nemotron Elastic uses structured pruning guided by a router, which is jointly trained with the model using auxiliary loss addressing the student model size plus the original knowledge distillation loss. This technology enables achieving the optimal student model at a fraction of the cost of pretraining from scratch or conventional compression.

### How the Router Decides What to Prune

Nemotron Elastic introduces an end-to-end trained router that performs neural architecture search over multiple compression axes, along with the knowledge distillation run. For Nano 4B, the framework was used in a single-budget configuration — targeting the 4B parameter count only — where the router's role is to determine
*which*
axes to prune and
*by how much*
to reach the target budget.

The router was given four pruning axes to choose from:

* Mamba heads — reducing the number of SSM heads
* Hidden dimension (embedding dimension) — shrinking the model-wide representation width
* FFN channels — pruning intermediate neurons in MLP layers
* Depth (layers) — removing entire layers from the network

For each width axis, prior knowledge about component importance was provided to the router by sorting channels, heads, and neurons according to activation-based importance scores. For depth, a normalized MSE-based layer importance ranking was used: each layer was iteratively removed, and the impact on the full model's output logits was measured, giving a principled ordering of which layers matter most. More details can be found in the
[Nemotron Elastic paper](https://arxiv.org/abs/2511.16664)
.
Given the 4B target parameter budget, the router converged on the following pruning decisions:

| Axis | Nemotron Nano 9B v2 (Parent) | Nemotron 3 Nano 4B |
| --- | --- | --- |
| Depth | 56 layers (27 Mamba, 4 attention, 25 MLP) | 42 layers (21 Mamba, 4 Attention, 17 MLP) |
| Mamba heads | 128 | 96 |
| FFN intermediate dim | 15680 | 12544 |
| Embedding dim | 4480 | 3136 |

### Two-Stage Distillation for Accuracy Recovery

After the router determines the pruned architecture, the compressed model is retrained using knowledge distillation from the frozen 9B parent using Nano v2’s pre-training and post-training data. This accuracy recovery process runs in two stages:

1. Stage 1 — Short-context distillation (8K sequence length): The 4B model is trained on 63B tokens using an 8K context window using a data blend consisting of approximately 70% post-training data and 30% pretraining data from the parent Nano v2 recipe. This stage is essential for the initial recovery of model accuracy after compression.
2. Stage 2 — Long-context extension (49K sequence length): To restore performance on more challenging tasks that require extended reasoning chains, the context is extended to 49K tokens. In this stage, the model is trained for 150 B tokens.

### Supervised Fine-Tuning

We conducted two stages of SFT with relevant subsets from the
[Nemotron-Post-Training-v3](https://huggingface.co/collections/nvidia/nemotron-post-training-v3)
collection using
[Megatron-LM](https://github.com/NVIDIA/Megatron-LM)
. The first SFT stage trains the model on a mix of reasoning and non-reasoning data spanning across diverse domains like math, coding, science, chat, instruction following, and agentic tasks. The second stage is a smaller scale, focused training to reinforce safety behaviors.

### Multi-environment Reinforcement Learning

Once the model is boot-strapped with SFT, we switch to a three-stage RL pipeline using
[NeMo-RL](https://github.com/NVIDIA-NeMo/RL)
to target our focus areas, instruction following and tool-calling / agentic behavior. In the first stage, we use single-turn instruction-following data. In the second stage, we use
[NeMo-Gym](https://github.com/NVIDIA-NeMo/Gym/)
environments for
[single-turn](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following)
and
[multi-turn](https://huggingface.co/datasets/nvidia/Nemotron-RL-agent-calendar_scheduling)
instruction following as well as for
[structured outputs](https://huggingface.co/datasets/nvidia/Nemotron-RL-instruction_following-structured_outputs)
(JSON, XML). Finally, in the third stage, we use a preliminary version of
[Nemotron-RL-Agentic-Conversational-Tool-Use-Pivot-v1](https://huggingface.co/datasets/nvidia/Nemotron-RL-Agentic-Conversational-Tool-Use-Pivot-v1)
for multi-turn conversational tool-calling. A balanced 50-50 ratio of reasoning and non-reasoning data was used throughout the three RLVR stages, with the KL penalty progressively increased at each stage.

## Boosting Efficiency with Quantization

For edge devices, it is essential to further reduce model size through quantization to improve efficiency and reduce VRAM usage. Nemotron 3 Nano 4B is released in FP8 and Q4\_K\_M GGUF to be efficient on the edge device.

For the FP8 model, we applied Post-Training Quantization (PTQ) using the
[ModelOpt](https://github.com/NVIDIA/Model-Optimizer)
library. For the PTQ calibration dataset, we used a small subset of 1K samples from the post-training SFT dataset to estimate activation statistics to minimize quantization related accuracy loss. To preserve accuracy while improving efficiency, we have also applied a selective quantization strategy rather than quantizing the entire network. Comparing a set of quant configurations showed that keeping self- attention layers (4 out of 42 layers) and the 4 Mamba layers that precede the self-attention layers at BF16 provided a sweet-spot for accuracy recovery and efficiency gain trade-off. The model weights, activations, and KV-Cache are quantized to FP8. Conv1D within all the Mamba layers are kept in BF16. FP8 model achieved 100% median accuracy recovery across target benchmarks compared to the BF16 model. The FP8 quantized version delivers up to 1.8X improvement in latency and throughput compared to the original BF16 version on DGX Spark & Jetson Thor.

For Llama.cpp support, we use the widely adopted GGUF quantization method Q4\_K\_M, a 4-bit scheme that provides an excellent balance between efficiency and accuracy. The Q4\_K\_M GGUF version achieved 100% median accuracy recovery across the target benchmarks compared to the BF16 model.

This GGUF release is also well suited for Jetson deployments. On Jetson Orin Nano 8GB designed for small embedded devices, the Q4\_K\_M checkpoint running with Llama.cpp delivers 18 tokens/s, up to 2× higher throughput than Nemotron Nano 9B v2, highlighting Nemotron 3 Nano 4B’s efficiency for edge inference in embedded AI and robotics use cases.

## Try It Now!

Nemotron 3 Nano 4B is available across a variety of inference engines, including Transformers, vLLM, TRT-LLM, and Llama.cpp, enabling support for a wide range of edge deployment scenarios.

To get started, visit the Hugging Face repositories below to download the model checkpoints. Usage examples for Hugging Face Transformers, vLLM, TRT-LLM, and Llama.cpp are available in the Model Card.

For Jetson, step-by-step instructions and ready-to-run commands are available on
[the Jetson AI Lab model page](https://www.jetson-ai-lab.com/models/)
.

Also, check out the
[NVIDIA In-Game Inferencing (NVIGI) SDK](https://developer.nvidia.com/rtx/in-game-inferencing)
to accelerate inference performance when running the model alongside heavy graphics workloads.