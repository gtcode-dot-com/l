---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-04T00:03:19.358567+00:00'
exported_at: '2025-12-04T00:03:21.961941+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models
structured_data:
  about: []
  author: ''
  description: Kimi K2 Thinking, DeepSeek-R1, Mistral Large 3 and others run 10x faster
    on NVIDIA GB200 NVL72.
  headline: Mixture of Experts Powers the Most Intelligent Frontier AI Models, Runs
    10x Faster on NVIDIA Blackwell NVL72
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Mixture of Experts Powers the Most Intelligent Frontier AI Models, Runs 10x
  Faster on NVIDIA Blackwell NVL72
updated_at: '2025-12-04T00:03:19.358567+00:00'
url_hash: 46b1ace40e8234a283feb3737de267a6fe3c313e
---

* *The top 10 most intelligent open-source models all use a mixture-of-experts architecture.*
* *Kimi K2 Thinking, DeepSeek-R1, Mistral Large 3 and others run 10x faster on NVIDIA GB200 NVL72.*

A look under the hood of virtually any frontier model today will reveal a
[mixture-of-experts](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
(MoE) model architecture that mimics the efficiency of the human brain.

Just as the brain activates specific regions based on the task, MoE models divide work among specialized “experts,” activating only the relevant ones for every
[AI token](https://blogs.nvidia.com/blog/ai-tokens-explained/)
. This results in faster, more efficient token generation without a proportional increase in compute.

The industry has already recognized this advantage. On the independent
[Artificial Analysis (AA) leaderboard](https://artificialanalysis.ai/models/open-source)
, the top 10 most intelligent open-source models use an MoE architecture, including DeepSeek AI’s DeepSeek-R1, Moonshot AI’s Kimi K2 Thinking, OpenAI’s gpt-oss-120B and Mistral AI’s Mistral Large 3.

However, scaling MoE models in production while delivering high performance is notoriously difficult. The extreme codesign of
[NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)
systems combines hardware and software optimizations for maximum performance and efficiency, making it practical and straightforward to scale MoE models.

The Kimi K2 Thinking MoE model — ranked as the most intelligent open-source model on the AA leaderboard — sees a 10x performance leap on the NVIDIA GB200 NVL72 rack-scale system compared with NVIDIA HGX H200. Building on the performance delivered for the
[DeepSeek-R1](https://blogs.nvidia.com/blog/blackwell-inferencemax-benchmark-results/)
and Mistral Large 3 MoE models, this breakthrough underscores how MoE is becoming the architecture of choice for frontier models — and why NVIDIA’s full-stack inference platform is the key to unlocking its full potential.

## **What Is MoE, and Why Has It Become the Standard for Frontier Models?**

Until recently, the industry standard for building smarter AI was simply building bigger, dense models that use all of their model parameters — often hundreds of billions for today’s most capable models — to generate every token. While powerful, this approach requires immense computing power and energy, making it challenging to scale.

Much like the human brain relies on specific regions to handle different cognitive tasks — whether processing language, recognizing objects or solving a math problem — MoE models comprise several specialized “experts.” For any given token, only the most relevant ones are activated by a router. This design means that even though the overall model may contain hundreds of billions of parameters, generating a token involves using only a small subset — often just tens of billions.

![A diagram titled 'Mixture of Experts' illustrating AI architecture. A stylized brain network sits between an 'Input' data icon and an 'Output' lightbulb icon. Inside the brain, specific nodes are highlighted with lightning bolt symbols, visually demonstrating how only relevant 'experts' are activated to generate every token rather than the entire network. ](https://blogs.nvidia.com/wp-content/uploads/2025/12/mixture-of-experts-video-1680x840.png)


Like the human brain uses specific regions for different tasks,
[mixture-of-experts models](https://www.youtube.com/shorts/TlmSpAvYwYI)
use a router to select only the most relevant experts to generate every token.

By selectively engaging only the experts that matter most, MoE models achieve higher intelligence and adaptability without a matching rise in computational cost. This makes them the foundation for efficient AI systems optimized for performance per dollar and per watt — generating significantly more intelligence for every unit of energy and capital invested.

Given these advantages, it is no surprise that MoE has rapidly become the architecture of choice for frontier models, adopted by over 60% of open-source AI model releases this year. Since early 2023, it’s enabled a nearly 70x increase in model intelligence — pushing the limits of AI capability.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/MoETrendVisual-e1764777501331.png)


Since early 2025, nearly all leading frontier models use MoE designs.

“Our pioneering work with OSS mixture-of-experts architecture, starting with Mixtral 8x7B two years ago, ensures advanced intelligence is both accessible and sustainable for a broad range of applications,” said Guillaume Lample, cofounder and chief scientist at Mistral AI. “Mistral Large 3’s MoE architecture enables us to scale AI systems to greater performance and efficiency while dramatically lowering energy and compute demands.”

## **Overcoming MoE Scaling Bottlenecks With Extreme Codesign**

Frontier MoE models are simply too large and complex to be deployed on a single GPU. To run them, experts must be distributed across multiple GPUs, a technique called expert parallelism. Even on powerful platforms such as the NVIDIA H200, deploying MoE models involves bottlenecks such as:

* **Memory limitations**
  : For each token, GPUs must dynamically load the selected experts’ parameters from high-bandwidth memory, causing frequent heavy pressure on memory bandwidth.
* **Latency**
  : Experts must execute a near-instantaneous all-to-all communication pattern to exchange information and form a final, complete answer. However, on H200, spreading experts across more than eight GPUs requires them to communicate over higher-latency scale-out networking, limiting the benefits of expert parallelism.

The solution: extreme codesign.

NVIDIA GB200 NVL72 is a rack-scale system with 72 NVIDIA Blackwell GPUs working together as if they were one, delivering 1.4 exaflops of AI performance and 30TB of fast shared memory. The 72 GPUs are connected using NVLink Switch into a single, massive NVLink interconnect fabric, which allows every GPU to communicate with each other with 130 TB/s of NVLink connectivity.

MoE models can tap into this design to scale expert parallelism far beyond previous limits — distributing the experts across a much larger set of up to 72 GPUs.

This architectural approach directly resolves MoE scaling bottlenecks by:

* **Reducing the number of experts per GPU**
  : Distributing experts across up to 72 GPUs reduces the number of experts per GPU, minimizing parameter-loading pressure on each GPU’s high-bandwidth memory. Fewer experts per GPU also frees up memory space, allowing each GPU to serve more concurrent users and support longer input lengths.
* **Accelerating expert communication**
  : Experts spread across GPUs can communicate with each other instantly using NVLink. The NVLink Switch also has the compute power needed to perform some of the calculations required to combine information from various experts, speeding up delivery of the final answer.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/extreme-codesign-moe-1680x945.png)

Other full-stack optimizations also play a key role in unlocking high inference performance for MoE models. The
[NVIDIA Dynamo](https://developer.nvidia.com/dynamo)
framework orchestrates
[disaggregated serving](https://www.nvidia.com/en-us/glossary/disaggregated-serving/)
by assigning prefill and decode tasks to different GPUs, allowing decode to run with large expert parallelism, while prefill uses parallelism techniques better suited to its workload. The
[NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)
format helps maintain accuracy while further boosting performance and efficiency.

Open-source inference frameworks such as NVIDIA TensorRT-LLM, SGLang and vLLM support these optimizations for MoE models. SGLang, in particular, has played a significant role in
[advancing large-scale MoE on GB200 NVL72](https://lmsys.org/blog/2025-09-25-gb200-part-2/)
, helping validate and mature many of the techniques used today.

To bring this performance to enterprises worldwide, the GB200 NVL72 is being deployed by  major cloud service providers and
[NVIDIA Cloud Partners](https://www.nvidia.com/en-us/data-center/gpu-cloud-computing/partners/)
including Amazon Web Services, Core42, CoreWeave, Crusoe, Google Cloud, Lambda, Microsoft Azure, Nebius, Nscale, Oracle Cloud Infrastructure, Together AI and others.

“At CoreWeave, our customers are leveraging our platform to put mixture-of-experts models into production as they build agentic workflows,” said Peter Salanki, cofounder and chief technology officer at CoreWeave. “By working closely with NVIDIA, we are able to deliver a tightly integrated platform that brings MoE performance, scalability and reliability together in one place. You can only do that on a cloud purpose-built for AI.”

Customers such as DeepL are using Blackwell NVL72 rack-scale design to build and deploy their next-generation AI models.

“DeepL is leveraging NVIDIA GB200 hardware to train mixture-of-experts models, advancing its model architecture to improve efficiency during training and inference, setting new benchmarks for performance in AI,” said Paul Busch, research team lead at DeepL.

## **The Proof Is in the Performance Per Watt**

NVIDIA GB200 NVL72 efficiently scales complex MoE models and delivers a 10x leap in performance per watt. This performance leap isn’t just a benchmark; it enables 10x the token revenue, transforming the economics of AI at scale in power- and cost-constrained data centers.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/DSR1-10X-MOE-BLOG-FINAL-1680x900.jpg)

At NVIDIA GTC Washington, D.C., NVIDIA founder and CEO Jensen Huang highlighted how GB200 NVL72 delivers 10x the performance of NVIDIA Hopper for DeepSeek-R1, and this performance extends to other DeepSeek variants as well.

“With GB200 NVL72 and Together AI’s custom optimizations, we are exceeding customer expectations for large-scale inference workloads for MoE models like DeepSeek-V3,” said Vipul Ved Prakash, cofounder and CEO of Together AI. “The performance gains come from NVIDIA’s full-stack optimizations coupled with Together AI Inference breakthroughs across kernels, runtime engine and speculative decoding.”

This performance advantage is evident across other frontier models.

Kimi K2 Thinking, the most intelligent open-source model, serves as another proof point, achieving 10x better generational performance when deployed on GB200 NVL72.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/KIMI-K2-10X-MOE-BLOG-FINAL-1680x895.jpg)

Fireworks AI has currently deployed Kimi K2 on the NVIDIA B200 platform to achieve the
[highest performance on the Artificial Analysis leaderboard](https://artificialanalysis.ai/models/kimi-k2-thinking/providers)
.

“NVIDIA GB200 NVL72 rack-scale design makes MoE model serving dramatically more efficient,” said Lin Qiao, cofounder and CEO of Fireworks AI. “Looking ahead, NVL72 has the potential to transform how we serve massive MoE models, delivering major performance improvements over the Hopper platform and setting a new bar for frontier model speed and efficiency.”

Mistral Large 3 also achieved a 10x performance gain on the GB200 NVL72 compared with the prior-generation H200. This generational gain translates into better user experience, lower per-token cost and higher energy efficiency for this new MoE model.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/ML3-10X-MOE-BLOG-FINAL-1680x895.jpg)

## **Powering Intelligence at Scale**

The NVIDIA GB200 NVL72 rack-scale system is designed to deliver strong performance beyond MoE models.

The reason becomes clear when taking a look at where AI is heading: the newest generation of multimodal AI models have specialized components for language, vision, audio and other modalities, activating only the ones relevant to the task at hand.

In agentic systems, different “agents” specialize in planning, perception, reasoning, tool use or search, and an orchestrator coordinates them to deliver a single outcome. In both cases, the core pattern mirrors MoE: route each part of the problem to the most relevant experts, then coordinate their outputs to produce the final outcome.

Extending this principle to production environments where multiple applications and agents serve multiple users unlocks new levels of efficiency. Instead of duplicating massive AI models for every agent or application, this approach can enable a shared pool of experts accessible to all, with each request routed to the right expert.

Mixture of experts is a powerful architecture moving the industry toward a future where massive capability, efficiency and scale coexist. The GB200 NVL72 unlocks this potential today, and NVIDIA’s roadmap with the NVIDIA Vera Rubin architecture will continue to expand the horizons of frontier models.

Learn more about how GB200 NVL72 scales complex MoE models in this
[technical deep dive](https://developer.nvidia.com/blog/scaling-large-moe-models-with-wide-expert-parallelism-on-nvl72-rack-scale-systems/)
.

*This post is part of*
[*Think SMART*](https://blogs.nvidia.com/blog/tag/think-smart)
*, a series focused on how leading AI service providers, developers and enterprises can boost their*
[*inference performance*](https://developer.nvidia.com/deep-learning-performance-training-inference/ai-inference)
*and return on investment with the latest advancements from NVIDIA’s full-stack*
[*inference platform*](https://www.nvidia.com/en-us/solutions/ai/inference/)
*.*