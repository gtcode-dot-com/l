---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T03:01:43.569610+00:00'
exported_at: '2026-03-18T03:01:47.151232+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/aws-and-nvidia-deepen-strategic-collaboration-to-accelerate-ai-from-pilot-to-production
structured_data:
  about: []
  author: ''
  description: Today at NVIDIA GTC 2026, AWS and NVIDIA announced an expanded collaboration
    with new technology integrations to support growing AI compute demand and help
    you build and run AI solutions that are production-ready.
  headline: AWS and NVIDIA deepen strategic collaboration to accelerate AI from pilot
    to production
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/aws-and-nvidia-deepen-strategic-collaboration-to-accelerate-ai-from-pilot-to-production
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AWS and NVIDIA deepen strategic collaboration to accelerate AI from pilot to
  production
updated_at: '2026-03-18T03:01:43.569610+00:00'
url_hash: c7f203f74e90bad071b4c514b4e61cd234cfe12d
---

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/AWS-NVIDIA-logo-lock-up.jpg)

AI is moving fast, and for most of our customers, the real opportunity isn’t in experimenting with it—it’s in running AI in production where it drives meaningful business outcomes. This means building systems that run reliably, perform at scale, and meet your organization’s security and compliance requirements.

Today at NVIDIA GTC 2026, AWS and NVIDIA announced an expanded collaboration with new technology integrations to support growing AI compute demand and help you build and run AI solutions that are production-ready. These integrations span accelerated computing, interconnect technologies, and model fine-tuning and inference. They include:

## Major announcements at NVIDIA GTC 2026

### Scaling AI infrastructure with expanded GPU options and optimized interconnect

**Accelerating compute capacity in the agentic AI era**

Starting in 2026, AWS will add more than 1 million NVIDIA GPUs including Blackwell and Rubin GPU architectures across our global cloud regions. AWS offers the broadest collection of NVIDIA GPU-based instances of any cloud provider to power a diverse set of AI/ML workloads. AWS and NVIDIA are also collaborating on Spectrum networking and other infrastructure areas, adding to over 15 years of joint innovation between our two companies.

AWS’s advanced cloud and AI infrastructure provides enterprises, startups, and researchers with the infrastructure needed to build and scale agentic AI systems—capable of reasoning, planning, and acting autonomously across complex workflows.

**New Amazon EC2 instances with NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs**

Today, we announced that Amazon EC2 instances accelerated by
[NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs](https://blogs.nvidia.com/blog/gtc-2026-news/#rtx-pro-4500)
are coming soon. AWS is the first major cloud provider to announce support for RTX PRO 4500 Blackwell Server Edition GPUs. These instances are well-suited for a wide range of workloads, including data analytics, conversational AI, content generation, recommender systems, video streaming, video rendering, and other graphics workloads.

Amazon EC2 instances accelerated by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs will be built on the
[AWS Nitro System](https://aws.amazon.com/ec2/nitro/)
, a combination of dedicated hardware and lightweight hypervisor which delivers practically all of the compute and memory resources of the host hardware to your instances for better overall resource utilization and performance. The Nitro System’s specialized hardware, software, and firmware are designed to enforce restrictions so that nobody, including anyone at AWS, can access your sensitive AI workloads and data. In addition, the Nitro System supports firmware updates, bug fixes, and optimizations while the system remains operational. These capabilities within the Nitro System enable the enhanced resource efficiency, security, and stability that AI, analytics, and graphics workloads require in production.

**Accelerating interconnect for disaggregated LLM inference with NVIDIA NIXL on AWS EFA and Trainium**

As model sizes grow, communication overhead between GPUs or Trainium can become a bottleneck. Today, we announced support for NVIDIA Inference Xfer Library (NIXL) with AWS EFA to accelerate disaggregated Large Language Model (LLM) inference on Amazon EC2, across NVIDIA GPUs and AWS Trainiums. Accelerating disaggregated inference is critical for scaling modern AI workloads because it enables efficient overlap of communication and computation while minimizing communication latency and maximizing GPU utilization. This integration enables high-throughput, low-latency KV-cache data movement between GPU compute nodes performing token generation and distributed memory resources that store KV-cache state. It also provides the flexibility to build inference clusters using any combination of GPU and Trainium EFA-enabled EC2 instances. NIXL with EFA integrates natively with popular open-source frameworks such as NVIDIA Dynamo, vLLM, and SGLang, delivering improved inter-token latency and more efficient KV-cache memory utilization.

### Accelerating data analytics with Amazon EMR and NVIDIA GPUs

**Running Apache Spark 3x faster using Amazon EMR on Amazon EKS with G7e instances**

Data engineers and data scientists frequently face hours-long data processing pipelines that slow AI/ML model iteration and business intelligence generation. We’re seeing significant performance gains for these workloads—AWS and NVIDIA deliver 3x faster performance for Apache Spark workloads with Amazon EMR on EKS on G7e instances. This performance results from joint AWS-NVIDIA engineering collaboration optimizing GPU-accelerated analytics by combining Amazon EMR on EKS with NVIDIA’s RTX PRO 6000 architecture. With Amazon EMR and G7e instances, data engineers and data scientists can accelerate time-to-insight for AI/ML feature engineering, complex ETL transformations, and real-time analytics at scale. Customers running large-scale data processing pipelines can cut the time needed to run analytics while maintaining full compatibility with existing Spark applications.

### Expanding NVIDIA Nemotron model support on Amazon Bedrock

**Fine-tuning Nemotron models in Amazon Bedrock with Reinforcement Fine-Tuning (Coming soon)**

Developers will soon be able to fine-tune NVIDIA Nemotron models directly on Amazon Bedrock using Reinforcement Fine-Tuning (RFT). This is significant for teams that need to align model behavior to specific domains, whether that’s legal, healthcare, finance, or any other specialized field. Reinforcement fine-tuning lets you shape how a model reasons and responds, not just what it knows. And because this runs natively on Amazon Bedrock, there’s zero infrastructure overhead. You define the task, provide the feedback signal, and Bedrock handles the rest. Learn about
[Reinforcement Fine-Tuning in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html)
.

**Nemotron 3 Super on Amazon Bedrock (Coming soon)**

NVIDIA Nemotron 3 Super—a hybrid MoE model built for multi-agent workloads and extended reasoning—is coming soon to Amazon Bedrock. Designed to enable AI agents to maintain accuracy across complex, multi-step workflows, it powers use cases across finance cybersecurity, retail , and software development—delivering fast, cost-efficient inference through a fully managed API.

### Improving energy efficiency and sustainability

As AI workloads scale, performance per watt isn’t just a sustainability metric—it’s a competitive advantage. In
[this NVIDIA GTC session](https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81714/)
, Amazon CSO Kara Hurst will join sustainability leaders from Equinix and PepsiCo to discuss how AI is transforming enterprise energy and infrastructure at scale—from data centers as active grid participants to AI as an enterprise efficiency engine, and how AWS can help you achieve optimal energy efficiency with AWS infrastructure being 4.1x more energy-efficient than on-premises data centers.

## Built to run, together

What makes these announcements exciting isn’t any single capability—it’s what they represent together. Fifteen years of partnership between AWS and NVIDIA has produced a full stack of AI infrastructure optimized end to end, from the GPU to the network to the managed services layer. You don’t have to stitch it together yourselves. It’s ready to run.

If you’re at GTC this week, come find us at the AWS booth. Check out live demos, catch our in-booth theater sessions, and pick up customized swag with AWS Swag Factory.

Visit
[AWS at NVIDIA GTC 2026](https://aws.amazon.com/events/aws-at-nvidia-gtc26/)
to see everything AWS has going on at the conference.

---

### About the authors

### David Brown

**David Brown**
is the Vice President of AWS Compute and Machine Learning (ML) Services. In this role he is responsible for building all AWS Compute and ML services, including Amazon EC2, Amazon Container Services, AWS Lambda, Amazon Bedrock and Amazon SageMaker. These services are used by all AWS customers but also underpin most of AWS’s internal Amazon applications. He also leads newer solutions, such as AWS Outposts, that bring AWS services into customers’ private data centers.