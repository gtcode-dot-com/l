---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-18T00:03:46.643323+00:00'
exported_at: '2025-12-18T00:03:49.574833+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ucsd-generative-ai-research-dgx-b200
structured_data:
  about: []
  author: ''
  description: The Hao AI Lab research team at the University of California San Diego
    recently received an NVIDIA DGX B200 system to elevate their work in LLM inference.
  headline: UC San Diego Lab Advances Generative AI Research With NVIDIA DGX B200
    System
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ucsd-generative-ai-research-dgx-b200
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: UC San Diego Lab Advances Generative AI Research With NVIDIA DGX B200 System
updated_at: '2025-12-18T00:03:46.643323+00:00'
url_hash: ad0d292480eb327e9805c14c55b9b71670b9cef1
---

The
[Hao AI Lab](https://hao-ai-lab.github.io/)
research team at the University of California San Diego  — at the forefront of pioneering AI model innovation — recently received an
[NVIDIA DGX B200](https://www.nvidia.com/en-us/data-center/dgx-b200/)
system to elevate their critical work in large language model
[inference](https://www.nvidia.com/en-us/glossary/ai-inference/)
.

Many LLM inference platforms in production today, such as
[NVIDIA Dynamo](https://www.nvidia.com/en-us/ai/dynamo/)
, use research concepts that originated in the Hao AI Lab, including
[DistServe](https://hao-ai-lab.github.io/blogs/distserve-retro/)
.

## **How Is Hao AI Lab Using the DGX B200?**

![Researchers standing around the DGX B200 system inside the San Diego Supercomputing Center. ](https://blogs.nvidia.com/wp-content/uploads/2025/12/UCSD--1680x1120.jpg)


Members of the Hao AI Lab standing with the NVIDIA DGX B200 system.

With the DGX B200 now fully accessible to the Hao AI Lab and broader UC San Diego community at the School of Computing, Information and Data Sciences’
[San Diego Supercomputer Center](https://www.sdsc.edu/)
, the research opportunities are boundless.

“DGX B200 is one of the most powerful AI systems from NVIDIA to date, which means that its performance is among the best in the world,” said Hao Zhang, assistant professor in the Halıcıoğlu Data Science Institute and department of computer science and engineering at UC San Diego. “It enables us to prototype and experiment much faster than using previous-generation hardware.”

Two Hao AI Lab projects the DGX B200 is accelerating are FastVideo and the Lmgame benchmark.

FastVideo focuses on training a family of video generation models to produce a five-second video based on a given text prompt — in just five seconds.

The research phase of FastVideo taps into NVIDIA H200 GPUs in addition to the DGX B200 system.

VIDEO

Lmgame-bench is a benchmarking suite that puts LLMs to the test using popular online games including
*Tetris*
and
*Super Mario Bros*
. Users can test one model at a time or put two models up against each other to measure their performance.

![Illustrated image of Lmgame-Bench workflow. ](https://blogs.nvidia.com/wp-content/uploads/2025/12/Cute-Robot-UCSD-1680x579.png)


The illustrated workflow of Hao AI Lab’s Lmgame-Bench project.

Other ongoing projects at Hao AI Labs explore new ways to achieve low-latency LLM serving, pushing large language models toward real-time responsiveness.

“Our current research uses the DGX B200 to explore the next frontier of low-latency LLM-serving on the awesome hardware specs the system gives us,” said Junda Chen, a doctoral candidate in computer science at UC San Diego.

## **How DistServe Influenced Disaggregated Serving**

[Disaggregated inference](https://www.nvidia.com/en-us/glossary/disaggregated-serving/)
is a way to ensure large-scale LLM-serving engines can achieve the optimal aggregate system throughput while maintaining acceptably low latency for user requests.

The benefit of disaggregated inference lies in optimizing what DistServe calls “goodput” instead of “throughput” in the LLM-serving engine.

Here’s the difference:

Throughput is measured by the number of
[tokens](https://blogs.nvidia.com/blog/ai-tokens-explained/)
per second that the entire system can generate. Higher throughput means lower cost to generate each token to serve the user. For a long time, throughput was the only metric used by LLM-serving engines to measure their performance against one another.

While throughput measures the aggregate performance of the system, it doesn’t directly correlate to the latency that a user perceives. If a user demands lower latency to generate the tokens, the system has to sacrifice throughput.

This natural trade-off between throughput and latency is what led the DistServe team to propose a new metric, “goodput”: the measure of throughput while satisfying the user-specified latency objectives, usually called service-level objectives. In other words, goodput represents the overall health of a system while satisfying user experience.

DistServe shows that goodput is a much better metric for LLM-serving systems, as it factors in both cost and service quality. Goodput leads to optimal efficiency and ideal output from a model.

## **How Can Developers Achieve Optimal Goodput?**

When a user makes a request in an LLM system, the system takes the user input and generates the first token, known as prefill. Then, the system creates numerous output tokens, one after another, predicting each token’s future behavior based on past requests’ outcomes. This process is known as decode.

Prefill and decode have historically run on the same GPU, but the researchers behind DistServe found that splitting them onto different GPUs maximizes goodput.

“Previously, if you put these two jobs on a GPU, they would compete with each other for resources, which could make it slow from a user perspective,” Chen said. “Now, if I split the jobs onto two different sets of GPUs — one doing prefill, which is compute intensive, and the other doing decode, which is more memory intensive — we can fundamentally eliminate the interference between the two jobs, making both jobs run faster.

This process is called prefill/decode disaggregation, or separating the prefill from decode to get greater goodput.

Increasing goodput and using the disaggregated inference method enables the continuous scaling of workloads without compromising on low-latency or high-quality model responses.

NVIDIA Dynamo — an open-source framework designed to accelerate and scale generative AI models at the highest efficiency levels with the lowest cost — enables scaling disaggregated inference.

In addition to these projects, cross-departmental collaborations, such as in healthcare and biology, are underway at UC San Diego to further optimize an array of research projects using the NVIDIA DGX B200, as researchers continue exploring how AI platforms can accelerate innovation.

*Learn more about the*
[*NVIDIA DGX B200*](https://www.nvidia.com/en-us/data-center/dgx-b200/)
*system.*