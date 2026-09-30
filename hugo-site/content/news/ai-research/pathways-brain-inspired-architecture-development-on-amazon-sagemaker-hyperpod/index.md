---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:43:33.217152+00:00'
exported_at: '2026-09-30T02:43:35.338095+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/pathways-brain-inspired-architecture-development-on-amazon-sagemaker-hyperpod
structured_data:
  about: []
  author: ''
  description: Pathway's Baby Dragon Hatchling (BDH) is a brain-inspired, post-transformer
    architecture that reasons in latent space instead of emitting chain-of-thought
    tokens. See how Pathway develops and scales BDH on Amazon SageMaker HyperPod,
    and how BDH-CQ set a new cost-efficiency mark on the ARC-AGI-1 benchmark.
  headline: Pathway’s brain-inspired architecture development on Amazon SageMaker
    HyperPod
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/pathways-brain-inspired-architecture-development-on-amazon-sagemaker-hyperpod
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Pathway’s brain-inspired architecture development on Amazon SageMaker HyperPod
updated_at: '2026-09-30T02:43:33.217152+00:00'
url_hash: 30a555d0f8ec76b58fd5964e37d31c104d5d1417
---

As AI systems take on more complex tasks, much of the industry’s progress has come from increasing model scale, training data, context length, and inference-time computation. Instead of externalizing reasoning work as a chain-of-thought (generating extra tokens sequentially and feeding them back into later steps),
[Pathway’s brain-inspired BDH](https://arxiv.org/pdf/2509.26507)
(Dragon Hatchling) performs reasoning in latent space. It learns from examples and refines a solution without generating an intermediate text trace. BDH moves beyond the transformer paradigm by offering a brain-inspired architecture, originally formulated as a graph of neurons that communicate through sparse, local interactions and maintain state in synapse-like connections. The model states adapt in context without test-time weight updates, and the reasoning horizon isn’t limited by a fixed-size context window or tied to a flood of inefficient chain-of-thought tokens.

Large language models (LLMs) have transformed AI, changing how we approach tasks from code generation to creative writing. However, fundamental questions remain about general intelligence and their ability to reason over long time periods in a coherent way. Their architecture, kept roughly static for the past 10 years, still presents important inefficiencies both in training and inference. LLMs tend to forget during long interactions, they don’t keep knowledge between sessions, and they need to be retrained to acquire new knowledge. Pathway’s BDH-CQ updates the model’s internal memory during inference by performing iterative computation inside a recurrent latent state and decoding only its candidate answers. Models can work through a new problem without generating long, verbalized reasoning traces, and without requiring fine-tuning or retraining.

Pathway’s BDH integrates with well-known frameworks such as PyTorch and uses
[Amazon SageMaker HyperPod](/sagemaker/ai/hyperpod/)
to scale out their training. Amazon SageMaker HyperPod helps their applied AI scientists share compute resources in a resilient, scalable, and cost-effective way.

## Transformers: architecture and fundamental limitations

The transformer architecture, while widely adopted for natural language processing (NLP), faces significant limitations in both training and inference workloads.

During training, transformers struggle with systematic generalization beyond their training data, particularly for long chain-of-thought reasoning tasks, and require massive amounts of data and computational effort to compensate for this limitation. The transformer architecture’s dense computation patterns and full back-propagation requirements lead to substantial computational costs that scale exponentially with model size. There’s a lack of clear connections between the dynamics at the micro-scale (that is, neuron activations) and macro-behavior (that is, why the model answers what it does). It’s difficult to efficiently update its knowledge without full retraining or fine-tuning, because transformers often struggle with catastrophic forgetting, where learning something new leads to forgetting something else.

At inference, transformers face other inefficiencies: the structure of their attention mechanism limits scalability, while their dense activation patterns, even with Mixture of Experts techniques, result in excessive computation and memory bandwidth usage. The fixed context window and growing KV-cache enforce limitations on sequence length processing. Furthermore, the closed-source nature of the transformer state makes it nearly impossible to interpret or monitor the model’s reasoning process, raising concerns about reliability and safety in production environments and heavily regulated industries.

These challenges are fundamentally tied to the architecture’s design choices rather than only implementation details, suggesting the need for alternative approaches that better align with both computational efficiency and natural intelligence principles.

&gt; *“Today’s AI pays a steep token cost for reasoning, but that cost is imposed by architecture, not by any law of intelligence. Currently, every reasoning step consumes context, adds latency, and burns compute. We show that a different architecture changes the game and opens up a whole new space in terms of how much intelligence per dollar. A 150M-parameter model, built on Pathway’s BDH architecture, reasons recurrently in latent space, and sets a new state of the art in cost efficiency on ARC-AGI-1. The bottleneck was never intelligence. It was design.”*

— Zuzanna Stamirowska, CEO and co-founder, Pathway

## BDH: A unified architecture for artificial and natural intelligence

[Pathway](https://pathway.com/)
’s vision is to fundamentally change the way models think. Their BDH architecture is a post-transformer model that continually learns, evolves, and reasons. BDH’s architecture represents a new way to build language models that reformulates sequence modeling as local graph dynamics on a network of interacting neuron particles. The model employs Hebbian learning, the principle that “neurons that fire together, wire together”, to implement attention mechanisms. This approach scales in a single neuron dimension (n), which reduces the complexity of distributing across compute resources that we face when deploying transformers.

As in the brain, the interactions of BDH are defined to be sparse and local, and the connections between the neurons encode the memory and reasoning functions. This sparse activation profile (only 5 percent of neurons are typically active at a given time) supports efficient computation. The reduced active state means less computation is required per inference step, leading to performance improvements in production environments.

BDH implements attention through a linear mechanism that operates on fixed, high-dimensional states without incurring the increased complexity characteristic of transformer models for long contexts. This allows the model to process longer sequences more efficiently, without the context length limitations of transformer architectures. The model’s states are directly mapped to synaptic connections between neuron pairs, providing visibility into the reasoning process and making the model’s decision-making easier to interpret.

Recently, Pathway built
[BDH-CQ, a reasoning system built on top of BDH](https://arxiv.org/pdf/2608.09888)
. It extends BDH with in-context learning and latent iterative reasoning for visual problem-solving.

As the following sections show, BDH-CQ excels at in-context learning. Its recurrent computations over latent states support efficient parallel hypothesis exploration, where communities of neurons can represent different candidate solutions for a problem at hand. The model achieves a reasoning efficiency which can process arbitrary numbers of demonstrations at fixed memory cost.

&gt; *“Customers are increasingly exploring how to move advanced reasoning from experimentation into production, where performance, efficiency, and scalability all matter. Pathway’s work training BDH-CQ on Amazon SageMaker HyperPod points to a promising path toward deploying high-performing systems more cost-effectively at scale.”*

— Nicolas Tarducci, Head of Solution Architecture for Startups EMEA, Amazon Web Services

## Developing BDH architecture on Amazon SageMaker HyperPod

Pathway uses
[Amazon SageMaker HyperPod](/sagemaker/ai/hyperpod/)
for developing its BDH architecture. Amazon SageMaker HyperPod is a purpose-built infrastructure solution for training LLMs and foundation models (FMs) that require distributed training or inference across hundreds or thousands of GPUs. It provides a fully managed, high-performance machine learning (ML) training environment with automated cluster provisioning, optimized networking fabric, and customizable software stacks. For model producers, Amazon SageMaker HyperPod delivers three key benefits: reduced time-to-market by removing complex infrastructure setup and management, improved cost efficiency through automatic scaling, and enhanced model performance through specialized networking architecture that achieves near-linear scaling across GPU clusters. This helps ML teams focus on model development rather than infrastructure challenges while achieving faster training times and lower costs compared to traditional infrastructure approaches.

For Pathway to develop AI architectures beyond transformers, comprehensive observability of their training infrastructure is critical. Amazon SageMaker HyperPod integration with advanced monitoring tools, such as
[Amazon Managed Service for Prometheus](/prometheus/)
, provides the deep insights needed for these workloads. The combination of visualization, metrics collection, and proactive optimization capabilities using Amazon Managed Grafana dashboards, allows Pathway to visualize complex distributed training patterns, monitor GPU utilization and memory patterns, and track inter-node communication efficiency for their parallel training approaches.

This comprehensive observability stack helps reduce development cycles when iterating on new architectural approaches, optimizes cost-performance ratio for resource-intensive training, and ensures reliability and reproducibility of results across training runs. For more information about this integration, and quick ways to deploy this observability stack, see the
[awsome-distributed-ai repository](https://github.com/awslabs/awsome-distributed-ai/tree/main/observability/prometheus-grafana)
or the
[Amazon SageMaker HyperPod documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm.html)
.

Amazon Elastic Fabric Adapter (EFA) integrates natively with the NVIDIA CUDA platform for GPU-accelerated computation and the NVIDIA Collective Communications Library (NCCL) for communication across GPUs. It allows distributing data, weights, activations, and more, in a reliable and scalable fashion. Pathway used Amazon Elastic Compute Cloud (Amazon EC2) p5en.48xlarge instances, which have up to 3200 Gbps of network performance per instance and NVIDIA’s accelerated AI infrastructure powered by NVIDIA H200 GPUs. All instances were interconnected using EFA and operated on an
[Amazon EC2 UltraCluster](/ec2/ultraclusters/)
to reduce the network distance between GPUs and lower latency.

## Proof of BDH architecture: BDH-CQ achieving 29.5% pass@2 on ARC-AGI

BDH-CQ achieved 29.5 percent pass@2 on the ARC-AGI benchmark at a cost of US $0.0007 per task.

Thanks to Pathway’s new approach to reasoning, in-context task acquisition and iterative latent computation, BDH-CQ changed the cost-accuracy Pareto frontier on the ARC-AGI-1 benchmark, as of August 2026.

ARC-AGI-1 presents an AI system with a small number of before-and-after examples that illustrate an unknown visual rule. The system must then infer that rule and apply it to a new grid, a capability often associated with human-like intelligence. BDH-CQ performs iterative computation inside a recurrent latent state and decodes only its candidate answers. Compared to transformers, which externalize their work as a chain-of-thought and increase latency and inference cost, BDH-CQ updates its model’s internal memory while examples are processed. It works through new problems without generating a long, verbalized reasoning trace.

The pattern that ARC-AGI explores resembles real-world challenges where systems must reason reliably as information and constraints change, such as investigating cyber security incidents, coordinating transportation networks, responding to real-time industrial operations, and operating autonomous agents across long-running workflows. BDH-CQ’s new approach shows it can make these applications less costly, more responsive, and more reliable.

## Conclusion

BDH is a new large language model architecture inspired by scale-free biological networks. It draws on principles biology got right, namely local interaction, sparse activity, persistent state, and continual adjustment, and applies them to a modern sequence model. It offers a GPU-friendly implementation. BDH provides a post-transformer architecture built around recurrent memory and local computation. BDH-CQ extends it into a reasoning system that learns from context and performs iterative computation in a continuous latent workspace, which supports efficient reasoning beyond token-by-token generation.

To begin exploring and implementing the BDH architecture, you can access detailed
[technical documentation](https://arxiv.org/abs/2608.09888)
and a sample implementation through Pathway’s
[repositories](https://github.com/pathwaycom/bdh)
. The implementation supports standard PyTorch workflows and can be readily integrated into existing ML pipelines.

Teams that push the boundaries of AI model development can use Amazon SageMaker HyperPod to maintain efficiency and reliability at scale. Amazon SageMaker HyperPod training offers a robust solution to common challenges in large model training. To learn more about Amazon SageMaker HyperPod, go to the
[AI on SageMaker HyperPod](https://awslabs.github.io/ai-on-sagemaker-hyperpod)
and find workshops, code examples, and troubleshooting guides. Or read about
[Checkpointless training on Amazon SageMaker HyperPod](/blogs/machine-learning/checkpointless-training-on-amazon-sagemaker-hyperpod-production-scale-training-with-faster-fault-recovery/)
to learn about its resilience features.

---

## About the authors

### Paulo Aragão

Paulo is a Principal WW Specialist Solutions Architect focused on helping customers build their Frontier AI strategy on AWS. With over 20 years of experience dealing with High Performance Computing and AIML projects, he is passionate about working backwards from customer’s challenges and helping overcome them. To know more about his projects, go to his
[GitHub page](https://github.com/paragao)
.

### Rodrigo Merino

Rodrigo is a Generative AI Solutions Architect Manager at AWS. With over a decade of experience deploying emerging technologies, from IoT to GenAI, Rodrigo guides customers to accelerate their AI/ML and generative AI journeys. He specializes in helping organizations train and build models on AWS, as well as operationalize end-to-end ML solutions. Rodrigo’s expertise lies in bridging the gap between cutting-edge technology and practical business applications, enabling companies to harness the full potential of AI.

### Ludovic Arnould

Ludovic is a Frontier AI Model Solutions Architect at Pathway, specializing in the design and deployment of advanced AI solutions for enterprise customers. He holds a PhD in Machine Learning from Sorbonne Université and has published research at ICML, ICLR, and AISTATS. His experience spans deep learning, multimodal AI, large language and vision models, with a track record of taking research prototypes through to production-ready systems.