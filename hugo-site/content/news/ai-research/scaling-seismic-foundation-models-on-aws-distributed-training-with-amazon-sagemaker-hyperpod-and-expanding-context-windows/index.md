---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T14:15:34.415893+00:00'
exported_at: '2026-04-02T14:15:37.817213+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-seismic-foundation-models-on-aws-distributed-training-with-amazon-sagemaker-hyperpod-and-expanding-context-windows
structured_data:
  about: []
  author: ''
  description: This post describes how TGS achieved near-linear scaling for distributed
    training and expanded context windows for their Vision Transformer-based SFM using
    Amazon SageMaker HyperPod. This joint solution cut training time from 6 months
    to just 5 days while enabling analysis of seismic volumes larger than previously
    p...
  headline: 'Scaling seismic foundation models on AWS: Distributed training with Amazon
    SageMaker HyperPod and expanding context windows'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/scaling-seismic-foundation-models-on-aws-distributed-training-with-amazon-sagemaker-hyperpod-and-expanding-context-windows
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Scaling seismic foundation models on AWS: Distributed training with Amazon
  SageMaker HyperPod and expanding context windows'
updated_at: '2026-04-02T14:15:34.415893+00:00'
url_hash: b8944763508bc2d0faebf1e62aaab763a233770d
---

*This post is cowritten with Altay Sansal and Alejandro Valenciano from TGS.*

[TGS](https://www.tgs.com/)
, a geoscience data provider for the energy sector, supports companies’ exploration and production workflows with advanced seismic foundation models (SFMs). These models analyze complex 3D seismic data to identify geological structures vital for energy exploration. To help enhance their next-generation models as part of their AWS infrastructure modernization, TGS partnered with the AWS Generative AI Innovation Center (GenAIIC) to optimize their SFM training infrastructure.

This post describes how TGS achieved near-linear scaling for distributed training and expanded context windows for their Vision Transformer-based SFM using
[Amazon SageMaker HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/)
. This joint solution cut training time from 6 months to just 5 days while enabling analysis of seismic volumes larger than previously possible.

## Addressing seismic foundation model training challenges

TGS’s SFM uses a Vision Transformer (ViT) architecture with Masked AutoEncoder (MAE) training designed by the TGS team to analyze 3D seismic data. Scaling such models presents several challenges:

* **Data scale and complexity**
  – TGS works with large volumes of proprietary 3D seismic data stored in domain-specific formats. The sheer volume and structure of this data required efficient streaming strategies to maintain high throughput and help prevent GPU idle time during training.
* **Training efficiency**
  – Training large FMs on 3D volumetric data is computationally intensive. Accelerating training cycles would enable TGS to incorporate new data more frequently and iterate on model improvements faster, delivering more value to their clients.
* **Expanded analytical capabilities**
  – The geological context a model can analyze depends on how much 3D volume it can process at once. Expanding this capability would allow the models to capture both local details and broader geological patterns simultaneously.

Understanding these challenges highlights the need for a comprehensive approach to distributed training and infrastructure optimization. The AWS GenAIIC partnered with TGS to develop a comprehensive solution addressing these challenges.

## Solution overview

The collaboration between TGS and the AWS GenAIIC focused on three key areas: establishing an efficient data pipeline, optimizing distributed training across multiple nodes, and expanding the model’s context window to analyze larger geological volumes. The following diagram illustrates the solution architecture.

![Architecture diagram showing AWS SageMaker HyperPod service integration with a customer account, featuring a login node, head node, 16 compute nodes, S3 storage connections, and user access paths for engineers, researchers, and operations teams.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/25/ML-10370-image-1.png)

The solution uses SageMaker HyperPod to help provide a resilient, scalable training infrastructure with automatic health monitoring and checkpoint management. The SageMaker HyperPod cluster is configured with
[AWS Identity and Access Management](https://aws.amazon.com/iam/)
(IAM) execution roles scoped to the minimum permissions required for training operations, deployed within a virtual private cloud (VPC) with network isolation and security groups restricting communication to authorized training nodes. Terabytes of training data streams directly from
[Amazon Simple Storage Service](https://aws.amazon.com/s3)
(Amazon S3), alleviating the need for intermediate storage layers while maintaining high throughput.
[AWS CloudTrail](http://aws.amazon.com/cloudtrail)
logs API calls to Amazon S3 and SageMaker services, and Amazon S3 access logging is enabled on training data buckets to provide a detailed audit trail of data access requests. The distributed training framework uses advanced parallelization techniques to efficiently scale across multiple nodes, and context parallelism methods enable the model to process significantly larger 3D volumes than previously possible.

The final cluster configuration consisted of 16
[Amazon Elastic Compute Cloud (Amazon EC2) P5 instances](https://aws.amazon.com/ec2/instance-types/p5/)
for the worker nodes integrated through the
[SageMaker AI flexible training plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html)
, each containing:

* 8 NVIDIA H200 GPUs with 141GB HBM3e memory per GPU
* 192 vCPUs
* 2048 GB system RAM
* 3200 Gbps EFAv3 networking for ultra-low latency communication

## Optimizing the training data pipeline

TGS’s training dataset consists of 3D seismic volumes stored in the TGS-developed MDIO format—an open source format built on Zarr arrays designed for large-scale scientific data in the cloud. Such volumes can contain billions of data points representing underground geological structures.

### Choosing the right storage approach

The team evaluated two approaches for delivering data to training GPUs:

* **Amazon FSx for Lustre**
  – Copy data from Amazon S3 to a high-speed distributed file system that the nodes read from. This approach provides sub-millisecond latency but requires pre-loading and provisioned storage capacity.
* **Streaming directly from Amazon S3**
  – Stream data directly from Amazon S3 using MDIO’s native capabilities with multi-threaded libraries, opening multiple concurrent connections per node.

### Settling on streaming directly from Amazon S3

The key architectural difference lies in how throughput scales with the cluster. With streaming directly from Amazon S3, each training node creates independent Amazon S3 connections, so aggregate throughput can scale linearly. With
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)
, the nodes share a single file system whose throughput is tied to provisioned storage capacity. Using Amazon FSx together with Amazon S3 requires only a small Amazon FSx storage volume, which limits the entire cluster to that volume’s throughput, creating a bottleneck as the cluster grows.

Comprehensive testing and cost analysis revealed streaming from Amazon S3 directly as the optimal choice for this configuration:

* **Performance**
  – Achieved 4–5 GBps sustained throughput per node using multiple data loader processes with pre-fetching over HTTPS endpoints (TLS 1.2)—sufficient to fully utilize the GPUs.
* **Cost efficiency**
  –
  **S**
  treaming from Amazon S3 alleviated the need for Amazon FSx provisioning, reducing storage infrastructure costs by over 90% while helping deliver 64-80 GBps cluster-wide throughput. The Amazon S3 pay-per-use model was more economical than provisioning high-throughput Amazon FSx capacity.
* **Better scaling**
  – Streaming from Amazon S3 directly scales naturally—each node brings its own connection bandwidth, avoiding the need for complex capacity planning.
* **Operational simplicity**
  – No intermediate storage to provision, manage, or synchronize.

The team optimized Amazon S3 connection pooling and implemented parallel data loading to sustain high throughput across the 16 nodes.

## Selecting the distributed training framework

When training large models across multiple GPUs, the model’s parameters, gradients, and optimizer states must be distributed across devices. The team evaluated different distributed training approaches to find the optimal balance between memory efficiency and training throughput:

* **ZeRO-2 (Zero Redundancy Optimizer Stage 2)**
  – This approach partitions gradients and optimizer states across GPUs while keeping a full copy of model parameters on each GPU. This helps reduce memory usage while maintaining fast communication, because each GPU can directly access the parameters during the forward pass without waiting for data from other GPUs.
* **ZeRO-3**
  – This approach goes further by also partitioning model parameters across GPUs. Although this helps maximize memory efficiency (enabling larger models), it requires more frequent communication between GPUs to gather parameters during computation, which can reduce throughput.
* **FSDP2 (Fully Sharded Data Parallel v2)**
  – PyTorch’s native approach similarly shards parameters, gradients, and optimizer states. It offers tight integration with PyTorch but involves similar communication trade-offs as ZeRO-3.

Comprehensive testing revealed DeepSpeed ZeRO-2 as the optimal framework for this configuration, delivering strong performance while efficiently managing memory:

* **ZeRO-2**
  – 1,974 samples per second (implemented)
* **FSDP2**
  – 1,833 samples per second
* **ZeRO-3**
  – 869 samples per second

This framework choice provided the foundation for achieving near-linear scaling across multiple nodes. The combination of these three key optimizations helped deliver the dramatic training acceleration:

* **Efficient distributed training**
  – DeepSpeed ZeRO-2 enabled near-linear scaling across 128 GPUs (16 nodes × 8 GPUs)
* **High-throughput data pipeline**
  – Streaming from Amazon S3 directly sustained 64–80 GBps aggregate throughput across the cluster

Together, these improvements helped reduce training time from 6 months to 5 days—enabling TGS to iterate on model improvements weekly rather than semi-annually.

## Expanding analytical capabilities

One of the most significant achievements was expanding the model’s field of view—how much 3D geological volume it can analyze simultaneously. A larger context window allows the model to capture both fine details (small fractures) and broad patterns (basin-wide fault systems) in a single pass, helping provide insights that were previously undetectable within the constraints of smaller analysis windows for TGS’s clients. The implementation by the TGS and AWS teams involved adapting the following advanced techniques to enable ViTs to process substantially larger 3D seismic volumes:

* **Ring attention implementation**
  – Each GPU processes a portion of the input sequence while circulating key-value pairs to neighboring GPUs, gradually accumulating attention results across the distributed system. PyTorch provides an API that makes this straightforward:

```
from torch.distributed.tensor.parallel import context_parallel

# Wrap attention computation with context parallelism
with context_parallel(
    buffers=[query, key, value],  # Tensors to shard
    buffer_seq_dims=[1, 1, 1]      # Dimension to shard along (sequence dimension)
):
    # Standard scaled dot-product attention - automatically becomes Ring Attention
    attention_output = torch.nn.functional.scaled_dot_product_attention(
        query, key, value, attn_mask=None
    )
```

* **Dynamic mask ratio adjustment**
  – The MAE training approach required making sure unmasked patches plus classification tokens are evenly divisible across devices, necessitating adaptive masking strategies.
* **Decoder sequence management**
  – The decoder reconstructs the full image by processing both the unmasked patches from the encoder and the masked patches. This creates a different sequence length that also needs to be divisible by the number of GPUs.

The preceding implementation enabled processing of substantially larger 3D seismic volumes as illustrated in the following table.

|  |  |  |
| --- | --- | --- |
| **Metric** | **Previous (Baseline)** | **With Context Parallelism** |
| Maximum input size | 640 × 640 × 1,024 voxels | 1,536 × 1,536 × 2,048 voxels |
| Context length | 102,400 tokens | 1,170,000 tokens |
| Volume increase | 1× | 4.5× |

The following figure provides an example of 2D model context size.

![Seismic cross-section diagram titled "2D Model Context Size Example" showing three color-coded context window sizes — 256×256 (cyan), 512×512 (magenta), and 640×1024 (yellow) — overlaid at three locations across a grayscale subsurface geological profile, with crossline traces on the x-axis and depth samples on the y-axis.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/25/ML-10370-image-2.png)

This expansion allows TGS’s models to capture geological features across broader spatial contexts, helping enhance the analytical capabilities they can offer to clients.

## Results and impact

The collaboration between TGS and the AWS GenAIIC delivered substantial improvements across multiple dimensions:

* **Significant training acceleration**
  – The optimized distributed training architecture reduced training time from 6 months to 5 days—an approximate 36-fold speedup, enabling TGS to iterate faster and incorporate new geological data more frequently into their models.
* **Near-linear scaling**
  – The solution demonstrated strong scaling efficiency from single-node to 16-node configurations, achieving approximately 90–95% parallel efficiency with minimal performance degradation as the cluster size increased.
* **Expanded analytical capabilities**
  – The context parallelism implementation enables training on larger 3D volumes, allowing models to capture geological features across broader spatial contexts.
* **Production-ready, cost-efficient infrastructure**
  – The SageMaker HyperPod based solution with streaming from Amazon S3 helps provide a cost-effective foundation that scales efficiently as training requirements grow, while helping deliver the resilience, flexibility, and operational efficiency needed for production AI workflows.

These improvements establish a strong foundation for TGS’s AI-powered analytics system, delivering faster model iteration cycles and broader geological context per analysis to clients while helping protect TGS’s valuable data assets.

## Lessons learned and best practices

Several key lessons emerged from this collaboration that might benefit other organizations working with large-scale 3D data and distributed training:

* **Systematic scaling approach**
  – Starting with a single-node baseline establishment before progressively expanding to larger clusters enabled systematic optimization at each stage while managing costs effectively.
* **Data pipeline optimization is critical**
  – For data-intensive workloads, thoughtful data pipeline design can provide strong performance. Direct streaming from object storage with appropriate parallelization and prefetching delivered the throughput needed without complex intermediate storage layers.
* **Batch size tuning is nuanced**
  – Increasing batch size doesn’t always improve throughput. The team found excessively large batch size can create bottlenecks in preparing and transferring data to GPUs. Through systematic testing at different scales, the team identified the point where throughput plateaued, indicating the data loading pipeline had become the limiting factor rather than GPU computation. This optimal balance maximized training efficiency without over-provisioning resources.
* **Framework selection depends on your specific requirements**
  – Different distributed training frameworks involve trade-offs between memory efficiency and communication overhead. The optimal choice depends on model size, hardware characteristics, and scaling requirements.
* **Incremental validation**
  – Testing configurations at smaller scales before expanding to full production clusters helped identify optimal settings while controlling costs during the development phase.

## Conclusion

By partnering with the AWS GenAIIC, TGS has established an optimized, scalable infrastructure for training SFMs on AWS. The solution helps accelerate training cycles while expanding the models’ analytical capabilities, helping TGS deliver enhanced subsurface analytics to clients in the energy sector. The technical innovations developed during this collaboration—particularly the adaptation of context parallelism to ViT architectures for 3D volumetric data—demonstrate the potential for applying advanced AI techniques to specialized scientific domains. As TGS continues to expand its subsurface AI system and broader AI capabilities, this foundation can support future enhancements such as multi-modal integration and temporal analysis.

To learn more about scaling your own FM training workloads, explore
[SageMaker HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
for resilient distributed training infrastructure, or review the
[distributed training best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)
in the SageMaker documentation. For organizations interested in similar collaborations, the
[AWS Generative AI Innovation Center](https://aws.amazon.com/generative-ai/innovation-center/)
partners with customers to help accelerate their AI initiatives.

### Acknowledgement

Special thanks to Andy Lapastora, Bingchen Liu, Prashanth Ramaswamy, Rohit Thekkanal, Jared Kramer and Roy Allela for their contribution.

---

## About the authors

### Haotian An

**Haotian An**
is a Machine Learning Engineer at the AWS Generative AI Innovation Center, where he specializes in customizing foundation models and distributed training at scale. He works closely with customers to adapt generative AI to their specific use cases, helping them unlock new capabilities and drive measurable business outcomes.

### Manoj Alwani

**Manoj Alwani**
is a Senior Applied Scientist at the Generative AI Innovation Center at AWS, where he helps organizations unlock the potential of cutting-edge AI technology. With deep expertise across the entire generative AI research stack, Manoj works closely with customers from diverse industries to accelerate their GenAI adoption and drive meaningful business outcomes. He brings over 13 years of hands-on experience in developing and deploying machine learning solutions at scale.

### Debby Wehner

**Debby Wehner**
is a Machine Learning Engineer at the AWS Generative AI Innovation Center, specializing in large language model customization and optimization. Previously, as a full-stack software engineer at Amazon, she built AI-powered shopping applications reaching over 100 million monthly users. She holds a PhD in Computational Geophysics from the University of Cambridge, as well as a BSc and MSc from Freie Universität Berlin.

### Altay Sansal

**Altay Sansal**
is a Senior Data Science Lead at TGS in Houston, Texas, specializing in AI/ML applications for geophysics and seismic data, including foundation models, large-scale training, and open-source tools like the MDIO format. He holds an M.S. in Geophysics from the University of Houston and has authored key publications such as “Scaling Seismic Foundation Models” and “MDIO: Open-source format for multidimensional energy data”, while actively contributing to geoscience ML through GitHub and industry events.

### Alejandro Valenciano

**Alejandro Valenciano**
is the Director of Data Science at TGS, where he leads advanced analytics and data science initiatives that unlock insights from subsurface and energy-related data, driving innovation across seismic, well, and machine learning workflows. He has developed and applied machine learning models for tasks such as basin-scale log prediction, advanced seismic processing, and Foundation Models. He frequently contributes to industry conferences and technical publications. His work spans data management, ML/AI applications in geoscience, and the integration of scalable data platforms to support exploration and energy solutions.