---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-20T12:15:34.456388+00:00'
exported_at: '2026-02-20T12:15:37.129568+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/data-blackwell-ultra-performance-lower-cost-agentic-ai
structured_data:
  about: []
  author: ''
  description: New SemiAnalysis InferenceX Data Shows NVIDIA Blackwell Ultra Delivers
    up to 50x Better Performance and 35x Lower Costs for Agentic AI. Microsoft, CoreWeave
    and Oracle Cloud Infrastructure are deploying NVIDIA GB300 NVL72 systems at scale
    for low-latency and long-context use cases.
  headline: New SemiAnalysis InferenceX Data Shows NVIDIA Blackwell Ultra Delivers
    up to 50x Better Performance and 35x Lower Costs for Agentic AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/data-blackwell-ultra-performance-lower-cost-agentic-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New SemiAnalysis InferenceX Data Shows NVIDIA Blackwell Ultra Delivers up to
  50x Better Performance and 35x Lower Costs for Agentic AI
updated_at: '2026-02-20T12:15:34.456388+00:00'
url_hash: bfc42a6bd37467d8b106ad2a32d34cf86e902452
---

The NVIDIA Blackwell platform has been widely adopted by leading inference providers such as
[Baseten, DeepInfra, Fireworks AI and Together AI](https://blogs.nvidia.com/blog/inference-open-source-models-blackwell-reduce-cost-per-token)
to reduce cost per token by up to 10x. Now, the NVIDIA Blackwell Ultra platform is taking this momentum further for agentic AI.

AI agents and coding assistants are driving explosive growth in software-programming-related AI queries: from 11% to about 50% last year, according to
[OpenRouter’s State of Inference report](https://openrouter.ai/state-of-ai)
. These applications require low latency to maintain real-time responsiveness across multistep workflows and long context when reasoning across entire codebases.

[New SemiAnalysis InferenceX performance data](https://inferencex.semianalysis.com/)
shows that the combination of NVIDIA’s software optimizations and the next-generation NVIDIA Blackwell Ultra platform has delivered breakthrough advances on both fronts. NVIDIA GB300 NVL72 systems now deliver up to 50x higher throughput per megawatt, resulting in 35x lower cost per token compared with the NVIDIA Hopper platform.

By innovating across chips, system architecture and software, NVIDIA’s extreme codesign accelerates performance across AI workloads — from agentic coding to interactive coding assistants — while driving down costs at scale.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/semianalysisv5-1680x945.jpg)

## **GB300 NVL72 Delivers up to 50x Better Performance for Low-Latency Workloads**

Recent analysis from
[Signal65](https://signal65.com/research/ai/from-dense-to-mixture-of-experts-the-new-economics-of-ai-inference/)
shows that NVIDIA GB200 NVL72 with extreme hardware and software codesign delivers more than 10x more tokens per watt, resulting in one-tenth the cost per token compared with the NVIDIA Hopper platform. These massive performance gains continue to expand as the underlying stack improves.

Continuous optimizations from the NVIDIA TensorRT-LLM, NVIDIA Dynamo, Mooncake and SGLang teams continue to significantly boost Blackwell NVL72 throughput for
[mixture-of-experts (MoE) inference](https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models/)
across all latency targets. For instance, NVIDIA TensorRT-LLM library improvements have delivered up to 5x better performance on GB200 for low-latency workloads compared with just four months ago.

* **Higher-performance GPU kernels**
  optimized for efficiency and low latency help make the most of Blackwell’s immense compute capabilities and boost throughput.
* **NVIDIA NVLink Symmetric Memory**
  enables direct GPU-to-GPU memory access for more efficient communication.
* **Programmatic dependent launch**
  minimizes idle time by launching the next kernel’s setup phase before the previous one completes.

Building on these software advances, GB300 NVL72 — which features the Blackwell Ultra GPU — pushes the throughput-per-megawatt frontier to 50x compared with the Hopper platform.

This performance gain translates into superior economics, with NVIDIA GB300 lowering costs compared with the Hopper platform across the entire latency spectrum. The most dramatic reduction occurs at low latency, where agentic applications operate: up to 35x lower cost per million tokens compared with the Hopper platform.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/gb300-nvl72-delivers-35x-reduction-in-token-cost-1680x945.png)


NVIDIA GB300 NVL72 and the codesigned software stack including NVIDIA Dynamo and TensorRT-LLM deliver 35x lower cost per token compared with NVIDIA Hopper platform.

For agentic coding and interactive assistants workloads where every millisecond compounds across multistep workflows, this combination of relentless software optimization and next-generation hardware enables AI platforms to scale real-time interactive experiences to significantly more users.

## **GB300 NVL72 Delivers Superior Economics for Long-Context Workloads**

While both GB200 NVL72 and GB300 NVL72 efficiently deliver ultralow latency, the distinct advantages of GB300 NVL72 become most apparent in long-context scenarios.
[For workloads with 128,000-token inputs and 8,000-token outputs](https://developer.nvidia.com/deep-learning-performance-training-inference/ai-inference)
— such as AI coding assistants reasoning across codebases — GB300 NVL72 delivers up to 1.5x lower cost per token compared with GB200 NVL72.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/gb300-nvl72-delivers-large-leap-for-long-context-ai-1680x945.png)


NVIDIA GB300 NVL72 is ideal for low-latency, long-context workloads.

Context grows as the agent reads in more of the code. This allows it to better understand the code base but also requires much more compute. Blackwell Ultra has 1.5x higher NVFP4 compute performance and 2x faster attention processing, enabling the agent to efficiently understand entire code bases.

## **Infrastructure for Agentic AI**

Leading cloud providers and AI innovators have already deployed NVIDIA GB200 NVL72 at scale, and are also deploying GB300 NVL72 in production.
[Microsoft](https://azure.microsoft.com/en-us/blog/microsoft-azure-delivers-the-first-large-scale-cluster-with-nvidia-gb300-nvl72-for-openai-workloads/)
,
[CoreWeave](https://www.coreweave.com/blog/coreweaves-nvidia-gb300-nvl72-production-ready-instances-for-enterprise-ai-featuring-nvidia-blackwell-ultra-gpus-deliver-more-than-6x-performance-gain-on-deepseek-r1)
and
[OCI](https://blogs.oracle.com/cloud-infrastructure/supercluster-nvidia-blackwell-dedicated-alloy)
are deploying GB300 NVL72 for low-latency and long-context use cases such as agentic coding and coding assistants. By reducing token costs, GB300 NVL72 enables a new class of applications that can reason across massive codebases in real time.

“As inference moves to the center of AI production, long-context performance and token efficiency become critical,” said Chen Goldberg, senior vice president of engineering at CoreWeave. “Grace Blackwell NVL72 addresses that challenge directly, and CoreWeave’s AI cloud, including CKS and SUNK, is designed to translate GB300 systems’ gains, building on the success of GB200, into predictable performance and cost efficiency. The result is better token economics and more usable inference for customers running workloads at scale.”

## **NVIDIA Vera Rubin NVL72 to Bring Next-Generation Performance**

With NVIDIA Blackwell systems deployed at scale, continuous software optimizations will keep unlocking additional performance and cost improvements across the installed base.

Looking ahead, the
[NVIDIA Rubin platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/)
— which combines six new chips to create one AI supercomputer — is set to deliver another round of massive performance leaps. For MoE inference, it delivers up to 10x higher throughput per megawatt compared with Blackwell, translating into one-tenth the cost per million tokens. And for the next wave of frontier AI models, Rubin can train large MoE models using just one-fourth the number of GPUs compared with Blackwell.

*Learn more about the NVIDIA Rubin platform and the*
[*Vera Rubin NVL72 system*](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
*.*