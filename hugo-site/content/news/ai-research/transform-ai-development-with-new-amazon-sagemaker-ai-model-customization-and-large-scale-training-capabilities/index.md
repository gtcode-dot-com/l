---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-14T22:15:26.547752+00:00'
exported_at: '2026-01-14T22:15:29.247844+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/transform-ai-development-with-new-amazon-sagemaker-ai-model-customization-and-large-scale-training-capabilities
structured_data:
  about: []
  author: ''
  description: This post explores how new serverless model customization capabilities,
    elastic training, checkpointless training, and serverless MLflow work together
    to accelerate your AI development from months to days.
  headline: Transform AI development with new Amazon SageMaker AI model customization
    and large-scale training capabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/transform-ai-development-with-new-amazon-sagemaker-ai-model-customization-and-large-scale-training-capabilities
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Transform AI development with new Amazon SageMaker AI model customization and
  large-scale training capabilities
updated_at: '2026-01-14T22:15:26.547752+00:00'
url_hash: e188b80009353db2155c314f85c658c3a4a29686
---

With the advancement in tools and services that make generative AI models accessible, businesses can now access the same
[foundation models](https://aws.amazon.com/what-is/foundation-models/)
(FMs) as their competitors. True differentiation comes from building AI that is highly customized for your business—something your competitors can’t effortlessly replicate. Although today’s FMs are genuinely intelligent with vast knowledge and reasoning capabilities, intelligence without context is merely potential. A model knows how to think, but it doesn’t know how you think, your vocabulary, your data patterns, or your industry constraints.

Building models that deeply understand your business depends on how you make the model learn from your data and preferences. Models learn through a step-by-step process that mirrors human learning: they first acquire general world knowledge through pre-training, then gain specialized knowledge through supervised fine-tuning, and finally learn to align with specific preferences through techniques like
[direct preference optimization](https://docs.aws.amazon.com/nova/latest/userguide/customize-fine-tune-hyperpod-dpo.html)
(DPO). At the inference stage, models can apply everything they’ve learned to real-world tasks, and they can continue adapting through parameter-efficient methods such as Low-Rank Adaptation (LoRA) without retraining the entire base model.

This learning journey spans from pre-training massive FMs to customizing them for specific use cases, and
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
now provides capabilities across this entire spectrum.

At
[AWS re:Invent 2025](https://aws.amazon.com/reinvent/)
, Amazon SageMaker AI announced significant advances that change how organizations can approach model customization and large-scale training. The new capabilities address two persistent challenges: the complexity and time required to customize FMs for specific use cases, and the costly infrastructure failures that derail weeks of training progress.

Since launching Amazon SageMaker AI in 2017, we’ve been committed to making AI development accessible for builders of different skill levels. With over 450 capabilities introduced since launch, SageMaker AI continues to remove barriers that slow innovation. This post explores how new serverless model customization capabilities, elastic training, checkpointless training, and serverless MLflow work together to accelerate your AI development from months to days.

## Serverless AI model customization with advanced reinforcement learning

The
[new serverless model customization](https://aws.amazon.com/blogs/aws/new-serverless-customization-in-amazon-sagemaker-ai-accelerates-model-fine-tuning/)
capability in Amazon SageMaker AI transforms what has traditionally been a months-long process into a matter of days. For AI developers who want the highest level of abstraction, we’re introducing an AI agent-guided workflow (in preview) that makes advanced model customization accessible through natural language.

Instead of requiring deep expertise in reinforcement learning techniques, you can now describe your business objectives in plain language. The AI agent engages in a multiturn conversation to understand your use case, then generates a comprehensive specification that includes dataset guidelines, evaluation criteria, associated metrics, and a recommended model that your team can implement without needing specialized knowledge.

The AI agentic workflow supports supervised fine-tuning (SFT), direct preference optimization (DPO), reinforcement learning from AI feedback (RLAIF), and Reinforcement Learning from Verifiable Rewards (RLVR). Models can use these reinforcement learning capabilities to learn from human preferences and verifiable outcomes, creating AI that aligns more closely with your business objectives. You can also generate synthetic data when real-world data is limited, analyze data quality, and handle training and evaluation for accuracy and responsible AI controls. This approach is entirely serverless to remove infrastructure complexity.

For AI developers who want more control over the customization process, SageMaker AI offers a straightforward interface with built-in best practices. Through
[SageMaker Studio](https://aws.amazon.com/sagemaker-ai/studio/)
, you can select from popular models including
[Amazon Nova](https://aws.amazon.com/nova/)
, Meta’s Llama, Qwen, DeepSeek, and GPT-OSS, then choose your preferred customization technique.

The self-guided workflow provides flexibility at every step. You can upload your own datasets or select from existing ones, configure hyperparameters such as batch size and learning rate with recommended defaults, and choose between parameter-efficient fine-tuning with LoRA or full fine-tuning. The interface integrates with the newly introduced MLflow capability for automatic experiment tracking, giving you visibility into training progress and model performance through a single interface.

Like the AI agentic approach, self-guided customization is completely serverless. SageMaker AI automatically handles compute provisioning, scaling, and optimization, so you can focus on model development instead of infrastructure management. With pay-per-token pricing, you can avoid the overhead of selecting instance types or managing clusters.

Collinear AI cut their experimentation cycles from weeks to days using the serverless model customization capability of SageMaker AI. Soumyadeep Bakshi, Co-founder, Collinear AI, said:

> *“At Collinear, we build curated datasets and simulation environments for frontier AI labs and Fortune 500 enterprises to improve their models. Fine-tuning AI models is critical to creating high-fidelity simulations, and it used to require stitching together different systems for training, evaluation, and deployment. Now with the new Amazon SageMaker AI serverless model customization capability, we have a unified way that empowers us to cut our experimentation cycles from weeks to days. This end-to-end serverless tooling helps us focus on what matters: building better training data and simulations for our customers, not maintaining infrastructure or juggling disparate platforms.”*

## Bridging model customization and pre-training

While serverless model customization accelerates development for specific use cases through fine-tuning and reinforcement learning, organizations are also rapidly expanding their use of generative AI across many parts of the business. Applications requiring deep domain expertise or specific business context need models that truly understand their proprietary knowledge, workflows, and unique requirements. Techniques such as prompt engineering and
[Retrieval Augmented Generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
(RAG) work well for many use cases, but they have fundamental limitations when it comes to embedding specialized knowledge into a model’s core understanding. When organizations attempt deeper customization through continued pre-training (CPT) using only their proprietary data, they often encounter catastrophic forgetting, where models lose their foundational capabilities as they learn new content.

Amazon SageMaker AI supports the complete spectrum of model development, from serverless customization with advanced reinforcement learning, to building frontier models from early checkpoints. For organizations with proprietary data that need models with deep domain expertise beyond what customization alone can provide, we recently introduced a new capability that addresses the limitations of traditional approaches while preserving foundational model capabilities.

Last week, we introduced
[Amazon Nova Forge](https://aws.amazon.com/nova/forge/)
. Accessible on Amazon SageMaker AI, this new service gives AI developers the opportunity to build their own frontier models using Amazon Nova. You can use Nova Forge to start model development from early checkpoints across pre-training, mid-training, and post-training phases—which means you can intervene at the optimal stage rather than waiting until training is complete. You can blend your proprietary data with Amazon Nova curated data throughout the training phases using demonstrated recipes on the fully managed infrastructure of SageMaker AI. This data mixing approach significantly reduces catastrophic forgetting compared to training with raw data alone. This helps preserve foundational skills, including core intelligence, general instruction following capabilities, and safety benefits while incorporating your specialized knowledge. Nova Forge is the simplest and most cost-effective way to build your own frontier model.

The following video introduces Amazon Nova Forge.

Nova Forge is designed for organizations with access to proprietary or industry-specific data who want to build AI that truly understands their domain, including:

* **Manufacturing and automation**
  – Building models that understand specialized processes and equipment data
* **Research and development**
  – Creating models trained on proprietary research data
* **Content and media**
  – Developing models that understand brand voice and content standards
* **Specialized industries**
  – Training models on industry-specific terminology, regulations, and best practices

Companies like Nomura Research Institute are using Amazon Nova Forge to build industry-specific
[large language models](https://aws.amazon.com/what-is/large-language-model/)
(LLMs) by combining Amazon Nova curated data with their proprietary datasets.

Takahiko Inaba, Head of AI and Managing Director, Nomura Research Institute, Ltd., said:

> *“Nova Forge enables us to build industry-specific LLMs as a compelling alternative to open-weight models. Running on SageMaker AI with managed training infrastructure, we can efficiently develop specialized models like our Japanese financial services LLM by combining Amazon Nova curated data with our proprietary datasets.”*

## Elastic training for intelligent resource management at scale

The demand for AI accelerators constantly fluctuates as inference workloads scale with traffic patterns, completed experiments release resources, and new training jobs shift priorities. Traditional training workloads remain locked into their initial compute allocation, unable to take advantage of idle capacity without manual intervention—a process that consumes hours of your engineering time each week.

[Elastic training on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/aws/introducing-checkpointless-and-elastic-training-on-amazon-sagemaker-hyperpod/)
transforms this dynamic. Training jobs now automatically scale based on compute resource availability, expanding to absorb idle AI accelerators and maximizing infrastructure utilization. When higher-priority workloads such as inference or evaluation need resources, the training scales down gracefully to continue with fewer resources instead of halting entirely.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/19/ml-20052-image-3.gif)

The technical architecture maintains training quality throughout scaling transitions by preserving global batch size and learning rate across different data-parallel configurations. This supports consistent convergence properties regardless of current scale. The SageMaker HyperPod training operator orchestrates scaling decisions through integration with the Kubernetes control plane, continuously monitoring cluster state through pod lifecycle events, node availability changes, and resource scheduler priority signals.

Getting started is straightforward. New elastic SageMaker HyperPod recipes for publicly available FMs including Meta’s Llama and GPT-OSS require no code changes—only YAML configuration updates to specify the elastic policy.

Salesforce is using elastic training to automatically scale workloads and absorb idle GPUs as they become available, explaining that elastic training
*“will enable our workloads to automatically scale to absorb idle GPUs as they become available and seamlessly yield resources, all without disrupting development cycles. Most importantly, it will save us hours spent manually reconfiguring jobs to match available compute, time that we can reinvest in innovation.”*

## Minimizing recovery downtime with checkpointless training

Infrastructure failures have long been the enemy of progress in large-scale training. Training runs that take weeks can be derailed by a single node failure, forcing you to restart from your last checkpoint and losing hours or days of expensive GPU time. Traditional checkpoint-based recovery involves sequential stages—job termination and restart, process discovery and network setup, checkpoint retrieval, GPU context reinitialization, and training loop resumption. When failures occur, the entire cluster must wait for every stage to be completed before training can resume.

[Checkpointless training on Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/aws/introducing-checkpointless-and-elastic-training-on-amazon-sagemaker-hyperpod/)
removes this bottleneck. The system maintains continuous model state preservation across distributed clusters, automatically swapping faulty components and recovering training through peer-to-peer transfer of model states from healthy AI accelerators. When infrastructure faults occur, recovery happens in seconds with zero manual intervention. The following video introduces checkpointless training.

This translates to upwards of 95% training goodput on cluster sizes with thousands of AI accelerators, meaning compute infrastructure is actively utilized for training jobs up to 95% of the time. You can now focus on innovation rather than infrastructure management, accelerating time-to-market by weeks.

Intercom is already integrating checkpointless training into their pipelines to remove manual checkpoint recovery, stating:

> *“At Intercom, we’re constantly training new models to improve Fin, and we’re very excited to integrate checkpointless training into our pipelines. This will completely eliminate the need for manual checkpoint recovery. Combined with elastic training, it will allow us to deliver improvements to Fin faster and with lower infrastructure costs.”*

## Serverless MLflow: Observability for every AI developer

Whether customizing models or training at scale, you need capabilities to track experiments, observe behavior, and evaluate performance. However, managing MLflow infrastructure traditionally requires administrators to continuously maintain and scale tracking servers, make complex capacity planning decisions, and deploy separate instances for data isolation. This infrastructure burden diverts resources away from core AI development.

[Amazon SageMaker AI now offers a serverless MLflow capability](https://aws.amazon.com/blogs/aws/accelerate-ai-development-using-amazon-sagemaker-ai-with-serverless-mlflow/)
that removes this complexity. You can begin tracking, comparing, and evaluating experiments without waiting for infrastructure setup. MLflow scales dynamically to deliver fast performance for demanding and unpredictable model development tasks, then scales down during idle time. The following screenshot shows the MLFlow application in the SageMaker AI UI.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/19/ml-20052-image-5.png)

The capability works natively with Amazon SageMaker AI serverless model customization so you can visualize in-progress training jobs and evaluations through a single interface. Advanced tracing capabilities help quickly identify bugs or unexpected behaviors in agentic workflows and multistep applications. Teams can use the MLflow Prompt Registry to version, track, and reuse prompts across organizations, maintaining consistency and improving collaboration.

Integration with
[SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
provides seamless model governance, automatically synchronizing models registered in MLflow with the production lifecycle. After models achieve the desired accuracy and performance goals, you can deploy them to SageMaker AI inference endpoints in only a few clicks.

Administrators can help enhance productivity by setting up cross-account access using
[AWS Resource Access Manager](https://aws.amazon.com/ram/)
(AWS RAM) to simplify collaboration across organizational boundaries. The serverless MLflow capability is offered at no additional charge and automatically upgrades to the latest version of MLflow, giving you access to the newest features without maintenance windows or migration effort.

Wildlife Conservation Society is using the new serverless capability to enhance productivity and accelerate time-to-insights. Kim Fisher, MERMAID Lead Software Engineer, WCS, said:

> *“WCS is advancing global coral reef conservation through MERMAID, an open source platform that uses ML models to analyze coral reef photos from scientists around the world. Amazon SageMaker with MLflow has enhanced our productivity by eliminating the need to configure MLflow tracking servers or manage capacity as our infrastructure needs change. By enabling our team to focus entirely on model innovation, we’re accelerating our time-to-deployment to deliver critical cloud-driven insights to marine scientists and managers.”*

## Accelerating AI innovation at every level

These announcements represent more than individual feature improvements—they establish a comprehensive system for AI model development that meets builders wherever they are on their journey. From natural language–guided customization to self-directed workflows, from intelligent resource management to fault-tolerant training, from experiment tracking to production deployment, Amazon SageMaker AI provides the complete toolkit for transforming AI ideas into production reality.

## Getting started

The new SageMaker AI model customization and SageMaker HyperPod capabilities are available today in
[AWS Regions](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#region)
worldwide. Existing SageMaker AI customers can access these features through the
[SageMaker AI console](https://console.aws.amazon.com/sagemaker/)
, and new customers can get started with the
[AWS Free Tier](https://aws.amazon.com/free/)
.

For more information about the latest capabilities of Amazon SageMaker AI, visit
[aws.amazon.com/sagemaker/ai](https://aws.amazon.com/sagemaker/ai/)
.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/19/ml-20052-image-6.jpeg)
Ankur Mehrotra**
joined Amazon back in 2008 and is currently the General Manager of Amazon SageMaker AI. Before Amazon SageMaker AI, he worked on building Amazon.com’s advertising systems and automated pricing technology.