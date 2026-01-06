---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-12T00:03:18.968033+00:00'
exported_at: '2025-12-12T00:03:21.752242+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/scaling-mlflow-for-enterprise-ai-whats-new-in-sagemaker-ai-with-mlflow
structured_data:
  about: []
  author: ''
  description: Today we’re announcing Amazon SageMaker AI with MLflow, now including
    a serverless capability that dynamically manages infrastructure provisioning,
    scaling, and operations for artificial intelligence and machine learning (AI/ML)
    development tasks. In this post, we explore how these new capabilities help you
    run large MLflow workloads—from generative AI agents to large language model (LLM)
    experimentation—with improved performance, automation, and security using SageMaker
    AI with MLflow.
  headline: 'Scaling MLflow for enterprise AI: What’s New in SageMaker AI with MLflow'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/scaling-mlflow-for-enterprise-ai-whats-new-in-sagemaker-ai-with-mlflow
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Scaling MLflow for enterprise AI: What’s New in SageMaker AI with MLflow'
updated_at: '2025-12-12T00:03:18.968033+00:00'
url_hash: a277b1722309b0298306e6e2c919c3b8ac010252
---

Today we’re announcing
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/?trk=8d6208e0-d44a-43ff-b272-99d77e5686ba&sc_channel=ps&ef_id=EAIaIQobChMIspe-3a76kAMVHx6tBh0bxC6ZEAAYASAAEgL5__D_BwE:G:s&s_kwcid=AL!4422!3!724218586019!e!!g!!sagemaker%20ai!19852662230!170020191325&gad_campaignid=19852662230&gbraid=0AAAAADjHtp80pxb_Rn07Vq5cdkqzQr3-Z&gclid=EAIaIQobChMIspe-3a76kAMVHx6tBh0bxC6ZEAAYASAAEgL5__D_BwE)
with MLflow, now including a serverless capability that dynamically manages infrastructure provisioning, scaling, and operations for artificial intelligence and machine learning (AI/ML) development tasks. It scales resources up during intensive experimentation and down to zero when not in use, reducing operational overhead. It introduces enterprise-scale features including seamless access management with cross-account sharing, automated version upgrades, and integration with SageMaker AI capabilities like model customization and pipelines. With no administrator configuration needed and at no additional cost, data scientists can immediately begin tracking experiments, implementing observability, and evaluating model performance without infrastructure delays, making it straightforward to scale MLflow workloads across your organization while maintaining security and governance.

In this post, we explore how these new capabilities help you run large MLflow workloads—from generative AI agents to large language model (LLM) experimentation—with improved performance, automation, and security using SageMaker AI with MLflow.

## Enterprise scale features in SageMaker AI with MLflow

The new MLflow serverless capability in SageMaker AI delivers enterprise-grade management with automatic scaling, default provisioning, seamless version upgrades, simplified
[AWS Identity and Access Management](https://aws.amazon.com/iam/)
(IAM) authorization, resource sharing through
[AWS Resource Access Manager](http://aws.amazon.com/ram/)
(AWS RAM), and integration with both
[Amazon SageMaker Pipelines](https://aws.amazon.com/sagemaker/pipelines/)
and model customization. The term
*MLﬂow Apps*
replaces the previous
*MLﬂow tracking servers*
terminology, reﬂecting the simpliﬁed, application-focused approach. You can access the new MLflow Apps page in
[Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-19756/1-ML-19756-mlflowappsUI.gif)

A default MLflow App is automatically provisioned when you create a SageMaker Studio domain, streamlining the setup process. It’s enterprise-ready out of the box, requiring no additional provisioning or configuration. The MLflow App scales elastically with your usage, alleviating the need for manual capacity planning. Your training, tracking, and experimentation workloads can get the resources they need automatically, simplifying operations while maintaining performance.

Administrators can define a maintenance window during the creation of the MLflow App, during which in-place version upgrades of the MLflow App take place. This helps the MLflow App be standardized, secure, and continuously up to date, minimizing manual maintenance overhead. MLflow version 3.4 is supported with this launch, and as shown in the following screenshot, extends MLflow to ML, generative AI applications, and agent workloads.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-19756/sagemaker_mlflow_v3-4-ml-agent_1_whitebk.gif)

## Simplified identity management with MLflow Apps

We’ve simplified access control and IAM permissions for ML teams with the new MLflow App. A streamlined permissions set, such as
`sagemaker:CallMlflowAppApi`
, now covers common MLflow operations—from creating and searching experiments to updating trace information—making access control more straightforward to enforce.

By enabling simplified IAM permissions boundaries, users and platform administrators can standardize IAM roles across teams, personas, and projects, facilitating consistent and auditable access to MLflow experiments and metadata. For complete IAM permission and policy configurations, see
[Set up IAM permissions for MLflow Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-app-setup-prerequisites-iam.html)
.

## Cross-account sharing of MLflow Apps using AWS RAM

Administrators want to centrally manage their MLflow infrastructure while provisioning access across different AWS accounts. MLflow Apps support AWS cross-account sharing for collaborative enterprise AI development. Using AWS RAM, this feature helps AI platform administrators share an MLflow App seamlessly across data scientists with consumer AWS accounts, as illustrated in the following diagram.

[![Diagram](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/05/6-ML-19756-1-scaled.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/6-ML-19756-1.jpg)

Platform administrators can maintain a centralized, governed SageMaker domain that provisions and manages the MLflow App, and data scientists in separate consuming accounts can launch and interact with the MLflow App securely. Combined with the new simplified IAM permissions, enterprises can launch and manage an MLflow App from a centralized administrative AWS account. Using the shared MLflow App, a downstream data scientist consumer can log their MLflow experimentation and generative AI workloads while maintaining governance, auditability, and compliance from a single platform administrator control plane. To learn more about cross-account sharing, see
[Getting Started with AWS RAM](https://docs.aws.amazon.com/ram/latest/userguide/getting-started.html)
.

## SageMaker Pipelines and MLflow integration

SageMaker Pipelines is integrated with MLflow. SageMaker Pipelines is a serverless workflow orchestration service purpose-built for MLOps and LLMOps automation. You can seamlessly build, execute, and monitor repeatable end-to-end ML workflows with an intuitive drag-and-drop UI or the Python SDK. From a SageMaker pipeline, a default MLflow App will be created if one doesn’t already exist, an MLflow experiment name can be defined, and metrics, parameters, and artifacts are logged to the MLflow App as defined in your SageMaker pipeline code. The following screenshot shows an example ML pipeline using MLflow.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/8-ML-19756.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/8-ML-19756.jpg)

## SageMaker model customization and MLflow integration

By default, SageMaker model customization integrates with MLflow, providing automatic linking between model customization jobs and MLflow experiments. When you run model customization fine-tuning jobs, the default MLflow App is used, an experiment is selected, and metrics, parameters, and artifacts are logged for you automatically. On the SageMaker model customization job page, you can view metrics sourced from MLflow and drill into additional metrics within the MLflow UI, as shown in the following screenshot.

[![View full metrics in MLflow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/10/Model-customization.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/9-ML-19756-1.jpeg)

## Conclusion

These features make the new MLflow Apps in SageMaker AI ready for enterprise-scale ML and generative AI workloads with minimal administrative burden. You can get started with the examples provided in the
[GitHub samples repository](https://github.com/aws-samples/sample-aiops-on-amazon-sagemakerai/tree/main)
and
[AWS workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ab4fc7a8-5885-4414-814d-28b443e7910e/en-US)
.

MLflow Apps are generally available in the
[AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
where SageMaker Studio is available, except China and US GovCloud Regions. We invite you to explore the new capability and experience the enhanced efficiency and control it brings to your ML projects. Get started now by visiting the SageMaker AI with MLflow
[product detail page](https://aws.amazon.com/sagemaker/experiments/)
and
[Accelerate generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
, and send your feedback to
[AWS re:Post for SageMaker](https://repost.aws/tags/TAT80swPyVRPKPcA0rsJYPuA)
or through your usual AWS support contacts.

---

### About the authors

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/11-ML-19756-100x100.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/11-ML-19756.jpg)
Sandeep Raveesh**
is a GenAI Specialist Solutions Architect at AWS. He works with customers through their AIOps journey across model training, generative AI applications like agents, and scaling generative AI use cases. He also focuses on go-to-market strategies helping AWS build and align products to solve industry challenges in the generative AI space. You can connect with Sandeep on LinkedIn to learn about generative AI solutions.

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/13-ML-19756.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/13-ML-19756.jpg)
Rahul Easwar i**
s a Senior Product Manager at AWS, leading managed MLflow and Partner AI Apps within the Amazon SageMaker AIOps team. With over 20 years of experience spanning startups to enterprise technology, he leverages his entrepreneurial background and MBA from Chicago Booth to build scalable ML platforms that simplify AI adoption for organizations worldwide. Connect with Rahul on LinkedIn to learn more about his work in ML platforms and enterprise AI solutions.

**[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/16-ML-19756-100x100.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/04/16-ML-19756.jpg)
Jessica Liao**
is a Senior UX Designer at AWS who leads design for MLflow, model governance, and inference within Amazon SageMaker AI, shaping how data scientists evaluate, govern, and deploy models. She brings expertise in handling complex problems and driving human-centered innovation from her experience designing DNA life science systems, which she now applies to make machine learning tools more accessible and intuitive through cross-functional collaboration.