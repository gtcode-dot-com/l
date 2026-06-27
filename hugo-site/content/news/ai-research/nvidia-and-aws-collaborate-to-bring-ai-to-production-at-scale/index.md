---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-27T03:43:38.352520+00:00'
exported_at: '2026-06-27T03:43:41.126719+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale
structured_data:
  about: []
  author: ''
  description: Across Amazon OpenSearch and Amazon EC2, NVIDIA AI infrastructure is
    giving enterprises more practical paths to deploy AI at production scale.
  headline: NVIDIA and AWS Collaborate to Bring AI to Production at Scale
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nvidia-aws-ai-production-scale
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA and AWS Collaborate to Bring AI to Production at Scale
updated_at: '2026-06-27T03:43:38.352520+00:00'
url_hash: e45b48c74146d427babe9d193111560ceea07466
---

Building AI systems at scale is demanding, requiring low-latency inference, fast vector search, strong GPU price-performance and infrastructure that can grow without multiplying operational complexity.

NVIDIA’s latest work with Amazon Web Services (AWS) addresses each of those constraints. Across Amazon OpenSearch and Amazon EC2, NVIDIA AI infrastructure is giving enterprises more practical paths to deploy AI at production scale.

EC2 G7 instances powered by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs expand the compute layer for AI, graphics, video and data analytics workloads, while the NVIDIA cuVS library accelerates the retrieval layer by making GPU-powered vector indexing the default in OpenSearch Serverless. And with AWS achieving NVIDIA Exemplar Cloud status for NVIDIA GB300, customers can trust they’re receiving peak optimized performance for their training workloads.

## **NVIDIA RTX PRO 4500 Blackwell Server Edition Multi-Workload GPUs Power New Amazon EC2 G7 Instances**

Amazon EC2 G7 instances bring NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs to AWS for AI inference, graphics, spatial computing and GPU-accelerated data analytics — delivering a new instance type engineered for production workloads that need performance without the operational overhead of a customer-managed GPU platform.

Compared with G6 instances, G7 delivers up to 4.6x AI inference performance, up to 2.1x graphics performance and significantly faster GPU-accelerated data analytics on Amazon EMR using the NVIDIA cuDF library for Apache Spark workloads.

With support for up to eight GPUs, 256GB of total GPU memory, 700 Gbps of EFA-enabled networking and up to 7.6TB of local NVMe SSD storage — across one-, two-, four- and eight- GPU configurations plus bare metal, coming soon — G7 instances let customers right-size infrastructure for their workloads instead of over-provisioning for them.

The platform’s versatility means AI teams get lower-latency inference. Media and entertainment teams get high-resolution video workflows and rendering. Simulation, computer-aided design, virtual desktop infrastructure, gaming and spatial computing teams get the same instance type for graphics-intensive applications. And data teams can apply the GPU memory, local storage and networking improvements to analytics pipelines and vector database workloads.

G7 instances are accessible through AWS Deep Learning Amazon Machine Images (AMIs), Amazon Deep Learning Containers, Amazon EMR, Amazon EKS, Amazon ECS and graphics AMIs — and coming soon to Amazon SageMaker AI.

## **NVIDIA cuVS Makes GPU-Accelerated Vector Search the Default in Amazon OpenSearch**

The next generation of Amazon OpenSearch Serverless powers agentic AI and dynamic workloads with no infrastructure management required. It uses GPU-accelerated vector indexing, powered by NVIDIA cuVS, as the default compute choice for all vector collections.

For teams building
[retrieval-augmented generation](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)

, semantic search, recommendation systems and agentic AI applications, that shift matters. It turns GPU-powered vector search from a specialized optimization project into a standard AWS capability.

The customer impact is direct: vector indexing up to 10x faster at a quarter of the cost, compared with CPU-only builds — making billion-scale vector databases practical to build in under an hour.

By making NVIDIA cuVS the default in OpenSearch Serverless, AWS customers get a much faster path from raw data to production-ready AI retrieval infrastructure — with serverless scaling that reduces operational overhead when workloads are idle.

## **AWS Achieves NVIDIA Exemplar Cloud Status for GB300 Training Performance**

AWS has achieved NVIDIA Exemplar Cloud status on NVIDIA GB300 for training workloads. This means AWS meets the rigorous performance thresholds that NVIDIA uses to benchmark AI workloads against its reference architecture.

This achievement is the result of deep co-engineering efforts between AWS and NVIDIA teams. Through the NVIDIA Exemplar Clouds initiative, developers and AI leaders can be confident they’re using consistent, high-performance cloud infrastructure for large-scale training, helping teams evaluate cloud providers with greater confidence, improve total cost of ownership and move AI projects from planning to production more efficiently.

Together, these advancements reinforce every layer of the AI infrastructure stack on AWS. The throughline is the same: production-grade AI infrastructure that performs at scale, without adding operational burden to the teams running it.

*Learn more in*
[*this AWS blog*](https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-ec2-g7-generally-available/)
*.*