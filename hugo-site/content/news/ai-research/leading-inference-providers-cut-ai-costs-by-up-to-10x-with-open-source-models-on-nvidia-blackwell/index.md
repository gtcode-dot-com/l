---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-12T20:15:34.768271+00:00'
exported_at: '2026-02-12T20:15:39.089885+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/inference-open-source-models-blackwell-reduce-cost-per-token
structured_data:
  about: []
  author: ''
  description: Leading inference providers Baseten, DeepInfra, Fireworks AI and Together
    AI are using NVIDIA Blackwell, which helps them reduce cost per token by up to
    10x compared with NVIDIA Hopper.
  headline: Leading Inference Providers Cut AI Costs by up to 10x With Open Source
    Models on NVIDIA Blackwell
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/inference-open-source-models-blackwell-reduce-cost-per-token
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Leading Inference Providers Cut AI Costs by up to 10x With Open Source Models
  on NVIDIA Blackwell
updated_at: '2026-02-12T20:15:34.768271+00:00'
url_hash: 568ea7e2d61ab28cb3ffd758cdbd78b13814008d
---

A diagnostic insight in healthcare. A character’s dialogue in an interactive game. An autonomous resolution from a customer service agent. Each of these AI-powered interactions is built on the same unit of intelligence: a
[token](https://blogs.nvidia.com/blog/ai-tokens-explained/)
.

Scaling these AI interactions requires businesses to consider whether they can afford more tokens. The answer lies in better tokenomics — which at its core is about driving down the cost of each token. This downward trend is unfolding across industries. Recent
[MIT research](https://arxiv.org/pdf/2511.23455)
found that infrastructure and algorithmic efficiencies are reducing inference costs for frontier-level performance by up to 10x annually.

To understand how infrastructure efficiency improves tokenomics, consider the analogy of a high-speed printing press. If the press produces 10x output with incremental investment in ink, energy and the machine itself, the cost to print each individual page drops. In the same way, investments in AI infrastructure can lead to far greater token output compared with the increase in cost — causing a meaningful reduction in the cost per token.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/inference-moe-tokenomics-diagram_dgm2-r3-1280x680-1-960x510.png)


When token output outpaces infrastructure cost, the cost of each token drops.

That’s why leading
[inference](https://www.nvidia.com/en-us/glossary/ai-inference/)
providers including Baseten, DeepInfra, Fireworks AI and Together AI are using the
[NVIDIA Blackwell platform](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/)
, which helps them reduce cost per token by up to 10x compared with the NVIDIA Hopper platform.

These providers host advanced open source models, which have now reached frontier-level intelligence. By combining open source frontier intelligence, the extreme hardware-software codesign of NVIDIA Blackwell and their own optimized inference stacks, these providers are enabling dramatic token cost reductions for businesses across every industry.

## **Healthcare —** **Baseten** **and** **Sully.ai** **Cut AI Inference Costs by 10x**

In healthcare, tedious, time-consuming tasks like medical coding, documentation and managing insurance forms cut into the time doctors can spend with patients.

[Sully.ai](http://sully.ai)
helps solve this problem by developing “AI employees” that can handle routine tasks like medical coding and note-taking. As the company’s platform scaled, its proprietary, closed source models created three bottlenecks: unpredictable latency in real-time clinical workflows, inference costs that scaled faster than revenue and insufficient control over model quality and updates.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/sullai-baseten-960x510.png)


Sully.ai builds AI employees that handle routine tasks for physicians.

To overcome these bottlenecks,
[Sully.ai uses Baseten’s Model API](https://www.baseten.co/resources/customers/sully-ai-returns-30m-clinical-minutes-using-open-source/)
, which deploys open source models such as gpt-oss-120b on NVIDIA Blackwell GPUs. Baseten used the low-precision
[NVFP4](https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/)
data format, the NVIDIA TensorRT-LLM library and the
[NVIDIA Dynamo](https://developer.nvidia.com/dynamo)
inference framework to deliver optimized inference. The company chose NVIDIA Blackwell to run its Model API after seeing up to 2.5x better throughput per dollar compared with the NVIDIA Hopper platform.

As a result,
[Sully.ai](https://sully.ai)
’s inference costs dropped by 90%, representing a 10x reduction compared with the prior closed source implementation, while response times improved by 65% for critical workflows like generating medical notes. The company has now returned over 30 million minutes to physicians, time previously lost to data entry and other manual tasks.

## **Gaming —** **DeepInfra** **and** **Latitude** **Reduce Cost per Token by 4x**

[Latitude](https://latitude.io/)
is building the future of AI-native gaming with its
[*AI Dungeon*](https://aidungeon.com/)
adventure-story game and  upcoming AI-powered role-playing gaming platform, Voyage, where players can create or play worlds with the freedom to choose any action and make their own story.

The company’s platform uses large language models to respond to players’ actions — but this comes with scaling challenges, as every player action triggers an inference request. Costs scale with engagement, and response times must stay fast enough to keep the experience seamless.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/latitude-deepinfra-960x510.png)


Latitude has built a text-based adventure-story game called “AI Dungeon,” which generates both narrative text and imagery in real time as players explore dynamic stories.

Latitude runs large open source models on
[DeepInfra’s inference platform, powered by NVIDIA Blackwell GPUs and TensorRT-LLM](https://deepinfra.com/blog/nvidia-blackwell-efficient-ai-inference)
. For a large-scale
[mixture-of-experts](https://www.nvidia.com/en-us/glossary/mixture-of-experts/)
(MoE) model, DeepInfra reduced the cost per million tokens from 20 cents on the NVIDIA Hopper platform to 10 cents on Blackwell. Moving to Blackwell’s native low-precision NVFP4 format further cut that cost to just 5 cents — for a total 4x improvement in cost per token — while maintaining the accuracy that customers expect.

Running these large-scale MoE models on DeepInfra’s Blackwell-powered platform allows Latitude to deliver fast, reliable responses cost effectively. DeepInfra inference platform delivers this performance while reliably handling traffic spikes, letting Latitude deploy more capable models without compromising player experience.

## **Agentic Chat — Fireworks AI and Sentient Foundation Lower AI Costs by up to 50%**

Sentient Labs is focused on bringing AI developers together to build powerful reasoning AI systems that are all open source. The goal is to accelerate AI toward solving harder reasoning problems through research in secure autonomy, agentic architecture and continual learning.

Its first app, Sentient Chat, orchestrates complex multi-agent workflows and integrates more than a dozen specialized AI agents from the community. Due to this, Sentient Chat has massive compute demands because a single user query could trigger a cascade of autonomous interactions that typically lead to costly infrastructure overhead.

To manage this scale and complexity,
[Sentient uses Fireworks AI’s inference platform running on NVIDIA Blackwell](https://fireworks.ai/blog/Story-Sentient)
. With Fireworks’ Blackwell-optimized inference stack, Sentient achieved 25-50% better cost efficiency compared with its previous Hopper-based deployment.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/sentient-fireworksai-960x510.png)


Sentient Chat orchestrates complex multi-agent workflows and integrates more than a dozen specialized AI agents from the community.

This higher throughput per GPU allowed the company to serve significantly more concurrent users for the same cost. The platform’s scalability supported a viral launch of 1.8 million waitlisted users in 24 hours and processed 5.6 million queries in a single week while delivering consistent low latency.

## **Customer Service —** **Together AI** **and** **Decagon** **Drive Down Cost by 6x**

Customer service calls with voice AI often end in frustration because even a slight delay can lead users to talk over the agent, hang up or lose trust.

Decagon builds AI agents for enterprise customer support, with AI-powered voice being its most demanding channel. Decagon needed infrastructure that could deliver sub-second responses under unpredictable traffic loads with tokenomics that supported 24/7 voice deployments.

![](https://blogs.nvidia.com/wp-content/uploads/2026/02/decagon-togetherai-960x510.png)


Decagon builds AI agents for customer support, and voice is its most demanding channel.

Together AI runs
[production inference for Decagon’s multimodel voice stack](https://www.together.ai/customers/decagon)
on NVIDIA Blackwell GPUs. The companies collaborated on several key optimizations: speculative decoding that trains smaller models to generate faster responses while a larger model verifies accuracy in the background, caching repeated conversation elements to speed up responses and building automatic scaling that handles traffic surges without degrading performance.

Decagon saw response times under 400 milliseconds even when processing thousands of tokens per query. Cost per query, which is the total cost to complete one voice interaction, dropped by 6x compared with using closed source proprietary models. This was achieved through the combination of Decagon’s multimodel approach (some open source, some trained in house on NVIDIA GPUs), NVIDIA Blackwell’s extreme codesign and Together’s optimized inference stack.

## **Optimizing Tokenomics With Extreme Codesign**

The dramatic cost savings seen across healthcare, gaming and customer service are driven by the efficiency of NVIDIA Blackwell. The NVIDIA GB200 NVL72 system further scales this impact by delivering a breakthrough
[10x reduction in cost per token](https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models/)
for reasoning MoE models compared with NVIDIA Hopper.

NVIDIA’s extreme codesign across every layer of the stack — spanning compute, networking and software — and its partner ecosystem are unlocking massive reductions in cost per token at scale.

VIDEO

This momentum continues with the
[NVIDIA Rubin platform](https://www.nvidia.com/en-us/data-center/technologies/rubin/)
— integrating six new chips into a single AI supercomputer to deliver 10x performance and 10x lower token cost over Blackwell.

*Explore*
[*NVIDIA’s full-stack inference platform*](https://www.nvidia.com/en-us/solutions/ai/inference/)
*to learn more about how it delivers better tokenomics for AI inference.*