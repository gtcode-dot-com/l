---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-26T16:53:51.729269+00:00'
exported_at: '2026-09-26T16:53:54.517728+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents
structured_data:
  about: []
  author: ''
  description: New SemiAnalysis AgentX data measured using real-world agentic coding
    trajectories shows Vera Rubin NVL72 systems deliver 30x higher throughput per
    megawatt and 45x lower token costs than NVIDIA GB300 NVL72.
  headline: 'Up to 30x More Work Per Watt: NVIDIA Vera Rubin NVL72 Sets a New Efficiency
    Standard for AI Agents'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/vera-rubin-nvl72-efficiency-ai-agents
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Up to 30x More Work Per Watt: NVIDIA Vera Rubin NVL72 Sets a New Efficiency
  Standard for AI Agents'
updated_at: '2026-09-26T16:53:51.729269+00:00'
url_hash: bab768ba33831cbe2fbe08bf1fa4f9718b581fdd
---

*Editor’s note: This blog, originally published on Aug. 24, 2026, was updated on Sept. 15, 2026, to reflect the latest performance data.*

According to
[OpenRouter data](https://openrouter.ai/blog/insights/deepseek-v4-adoption/)

, agentic AI workloads consume 15x more tokens than a simple chat request. Why?

Consider what happens when an AI agent researches a company for an investment decision. The agent queries financial databases, searches news and filings, invokes a sub-agent to run peer comparisons and model valuations, then synthesizes everything into a recommendation. Agents and sub-agents keep reasoning until the task is done, driving increased token demand. With every step, the accumulated tokens become the input to the next, making long-context handling central to agentic AI performance.

![](https://blogs.nvidia.com/wp-content/uploads/2026/08/end-to-end-corp-blog-diagram-agentx-activation-1280x680-5565900.gif)

The same pattern plays out across every agentic use case, from software development to customer service to deep research.

As agentic AI moves into production across industries, the infrastructure running it needs to meet that token demand efficiently.

New SemiAnalysis AgentX data shows NVIDIA Vera Rubin NVL72 systems deliver up to 30x higher throughput per megawatt than NVIDIA GB300 NVL72 on agentic workloads. The SemiAnalysis AgentX workload consists of recorded real-world agentic coding sessions, with actual context growth, tool calls and sub-agent spawning preserved. For power-constrained AI factories, this performance translates directly into 30x more agentic work for the same energy footprint.

These early results for Vera Rubin NVL72 demonstrate NVIDIA’s accelerated pace of innovation. With continuous software optimizations, performance across both Vera Rubin NVL72 and GB300 NVL72 will continue to improve.

## **Vera Rubin NVL72: 30x Higher Throughput per Megawatt and 45x Lower Token Cost**

Agentic workloads look fundamentally different from chat or document summarization, where input and output sequences typically range from 1K to 8K tokens. In agentic sessions, context accumulates across steps and can reach hundreds of thousands of input tokens, with wide variability in both input and output lengths across requests. Performance measurement must evolve to capture the full agent workflow rather than a single inference request.

![](https://blogs.nvidia.com/wp-content/uploads/2026/08/InferenceNeedsAgenticBenchmarks-scaled.png)

The results below reflect performance measured on real-world agentic coding trajectories.

In
[SemiAnalysis AgentX](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)

, the NVIDIA Blackwell platform delivers leading performance across multiple agentic models including Kimi K3, MiniMax M3, GLM5.3, Qwen3.5 and DeepSeek V4 Pro.

For example,
[GB300 NVL72 delivers up to 15x](https://developer.nvidia.com/blog/nvidia-vera-rubin-and-blackwell-set-a-new-standard-for-agentic-ai-performance-per-watt/?ncid=so-inst-151306)
better throughput per megawatt than the NVIDIA Hopper architecture on the DeepSeek V4 Pro model, giving customers a high-performance foundation to run agentic workloads. This leap reflects the advantage of a larger scale-up GPU domain and codesigned software in delivering significantly better inference efficiency.

Vera Rubin extends that advantage, lifting the performance across the entire Pareto curve, to deliver as much as 30x higher throughput per megawatt than GB300 NVL72 on the DeepSeek V4 Pro model. These early results, measured on the SemiAnalysis AgentX workload, don’t yet reflect Vera CPU performance for tool calling.

![](https://blogs.nvidia.com/wp-content/uploads/2026/08/semianalysis-VRThroughputPerMW-1680x945.jpg)

NVIDIA DSX MaxLPS technologies manages power across the GPU, rack and workload levels to provision up to 40% more GPUs within the same megawatt budget, pushing throughput per megawatt further at AI factory scale.

Throughput per megawatt also directly impacts the cost of every token produced. At up to 45x lower cost per million tokens than GB300 NVL72, Vera Rubin NVL72 can run agents continuously, at scale, across the full breadth of customers’ workloads.

![](https://blogs.nvidia.com/wp-content/uploads/2026/08/semianalysis-VRCostPerMToken-1680x945.jpg)

For power-constrained AI factories, throughput per megawatt determines
[AI factory revenue](https://www.cio.com/article/4209776/5-critical-questions-that-define-ai-factory-economics.html)

and cost per million tokens determines the profit margin on that revenue.

## **Extreme Codesign for Agentic Scale**

Modern inference optimization spans a range of techniques that are especially critical for agentic AI. NVIDIA Vera Rubin NVL72 enables all of these and more through extreme codesign across every layer of the platform to deliver multifold performance gains.

* Disaggregated serving separates context processing (prefill) from response generation (decode) so each scales independently.
* Rate matching synchronizes the speeds at which prefill GPUs and decode GPUs produce tokens to maximize efficiency.
* Large-scale expert parallelism distributes expert sub-networks in
  [mixture-of-experts models](https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models/)

  across the scale-up GPU domain.
* Distributed KV-caching extends memory across the scale-up GPU domain, while KV-cache offloading tiers less-active context to host and storage, keeping previously processed context accessible without recomputation.
* KV-aware routing directs incoming requests to the GPUs that already hold the relevant cached context, reducing redundant computation across long sessions.
* Fused CUDA kernels like MegaMoE combine many computation and inter-GPU communication operations into a single execution pass, keeping GPUs active rather than waiting for data.

NVIDIA Rubin GPUs’ enhanced fifth-generation
[Tensor Cores](https://www.nvidia.com/en-us/data-center/tensor-cores/)

and the third-generation
[Transformer Engine](https://www.nvidia.com/en-us/data-center/tensor-cores/)

accelerate both prefill and decode stages of inference. NVFP4 quantization compresses model weights to 4-bit precision, reducing memory footprint and increasing throughput without sacrificing output quality.

The NVL72 scale-up domain, a defining architecture across Vera Rubin and Grace Blackwell, enables the high-bandwidth and low-latency inter-GPU communication essential for techniques such as large-scale expert parallelism and distributed KV-caching. Purpose-built to power this scale-up domain, NVIDIA NVLink interconnect technology and NVLink Switches, now in their sixth generation, deliver 10x higher packet rates and 3x lower latency than off-the-shelf Ethernet alternatives.

Spanning optimized CUDA kernels, inference runtimes like NVIDIA TensorRT LLM and serving frameworks like NVIDIA Dynamo, NVIDIA’s
[software stack](https://blogs.nvidia.com/blog/inference-software-lowest-token-cost/)

is codesigned with the hardware to enable inference optimizations.

While the results above reflect current Vera Rubin NVL72 performance, the full platform is a seven-chip architecture that also includes the NVIDIA Vera CPU,
[Groq 3 LPU](https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-unlocks-ultrafast-interactivity-at-long-context-on-nvidia-vera-rubin/)
, NVLink 6 Switch, BlueField-4 DPU, Spectrum-6 SPX and ConnectX-9 SuperNIC, all purpose-built for AI factories deploying agents at scale.

Extreme codesign also extends to NVIDIA’s co-engineering with its partners. Vera Rubin is in full production and is scaling across the ecosystem.

*Learn more about the*
[*NVIDIA Vera Rubin platform*](https://blogs.nvidia.com/blog/vera-rubin/)
*.*