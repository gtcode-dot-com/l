---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T03:15:47.043733+00:00'
exported_at: '2026-03-18T03:15:49.308408+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/snap-accelerated-data-processing
structured_data:
  about: []
  author: ''
  description: NVIDIA cuDF accelerates Apache Spark applications on Google Cloud helps
    Snap engineers test and deploy new features faster while unlocking significant
    cost savings.
  headline: 'Snap Decisions: How Open Libraries for Accelerated Data Processing Boost
    A/B Testing for Snapchat'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/snap-accelerated-data-processing
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Snap Decisions: How Open Libraries for Accelerated Data Processing Boost A/B
  Testing for Snapchat'
updated_at: '2026-03-18T03:15:47.043733+00:00'
url_hash: 8766d9abf7ee959fd3fd1602b8d60a3074c43fe9
---

The features on social media apps like Snapchat evolve nearly as fast as what’s trending. To keep pace, its parent company Snap has adopted open data processing libraries from NVIDIA on Google Cloud services to boost development.

Every new feature rolled out to Snapchat’s more than 940 million monthly active users goes through a set of controlled experiments before it’s launched. During this A/B testing cycle, the development team studies different variables with a subset of users, measuring nearly 6,000 metrics that analyze engagement, app performance and monetization.

Snap runs thousands of these experiments each month — processing over 10 petabytes of data within a three-hour window each morning using the Apache Spark distributed framework. By adopting
[Apache Spark accelerated by NVIDIA cuDF](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf#section-accelerate-apache-spark)

, the company is boosting these data processing workloads on NVIDIA GPUs to achieve 4x speedups in runtime with the same number of machines, providing a cost-effective path to scale.

By pairing NVIDIA’s GPU-optimized software, including NVIDIA CUDA-X libraries, with Google’s infrastructure management services such as Google Kubernetes Engine, Snap is harnessing a full-stack platform for data processing at scale.

“Experimentation is at the core of our company. Changing our data infrastructure from CPUs to GPUs allows us to efficiently scale this experimentation to more features, more metrics and more users over time,” said Prudhvi Vatala, senior engineering manager at Snap. “The more experiments we’re able to run, the more innovative experiences we can deliver for Snapchat users.”

## **A Sustainable Way to Scale**

Snapchat fans frequently see new features in the app — from arrival notifications to AI-generated stickers — but Snap is also continuously rolling out behind-the-scenes updates such as performance optimizations and compatibility updates for new operating system versions.

The A/B testing for all these new features now runs on cuDF, which allows developers to run existing Apache Spark applications on NVIDIA GPUs with no code changes for easy deployment. The open library for accelerated data processing builds on the power of the NVIDIA
[cuDF](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf#section-accelerate-apache-spark)

GPU DataFrame library while scaling it for the Apache Spark distributed computing framework.

With this migration, the team has — based on Snap internal data collected between January 1 and February 28 — realized 76% daily cost savings using NVIDIA GPUs on Google Kubernetes Engine compared with CPU-only workflows.

“We were projecting an ambitious roadmap to scale up experimentation that would have blown up our computing costs based on our existing infrastructure,” Vatala said. “Switching to GPU-accelerated pipelines with cuDF gave us a way to flatten the scaling curve, and the results were tremendous.”

![](https://blogs.nvidia.com/wp-content/uploads/2026/03/Snap_pullquote-scaled.jpg)
To support workload migration, the team also harnessed cuDF suite of microservices that automatically qualify, test, configure and optimize Spark workloads for GPU acceleration at scale.

Working with NVIDIA experts, the Snap team optimized its pipelines on Google Cloud’s G2 virtual machines powered by NVIDIA L4 GPUs so they required just 2,100 GPUs running concurrently — as opposed to the initial projection that around 5,500 GPUs would need to run concurrently, according to data Snap collected between January 1 and March 13.

“When I saw the results of the initial experiments, they were pretty crazy — we saw much higher cost savings than we had expected,” said Joshua Sambasivam, a backend engineer on the A/B testing team. “The Spark accelerator is a perfect match for our workloads.”

Looking ahead, the Snap team plans to integrate the Spark accelerator beyond the A/B team to a broader range of production workloads.

“We didn’t realize we were sitting on this gold mine,” Vatala said. “We’ve so far migrated our two biggest pipelines, but there’s a lot of opportunity ahead.”

Learn more by tuning into
[Vatala’s session at NVIDIA GTC](https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81678/)

, taking place

Tuesday, March 17 at 1 p.m. PT

.

*Read more about*
[*NVIDIA cuDF*](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf)
*and get started with*
[*GPU acceleration for Apache Spark*](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf#section-accelerate-apache-spark)
*.*

*Main image above courtesy of Snap, depicting A/B test of its Maps feature.*