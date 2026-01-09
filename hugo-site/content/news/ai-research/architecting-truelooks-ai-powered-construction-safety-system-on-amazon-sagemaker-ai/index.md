---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-09T16:15:28.813574+00:00'
exported_at: '2026-01-09T16:15:31.103316+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/architecting-truelooks-ai-powered-construction-safety-system-on-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: This post provides a detailed architectural overview of how TrueLook
    built its AI-powered safety monitoring system using SageMaker AI, highlighting
    key technical decisions, pipeline design patterns, and MLOps best practices. You
    will gain valuable insights into designing scalable computer vision solutions
    on AWS, particularly around model training workflows, automated pipeline creation,
    and production deployment strategies for real-time inference.
  headline: Architecting TrueLook’s AI-powered construction safety system on Amazon
    SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/architecting-truelooks-ai-powered-construction-safety-system-on-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Architecting TrueLook’s AI-powered construction safety system on Amazon SageMaker AI
updated_at: '2026-01-09T16:15:28.813574+00:00'
url_hash: 4f1eddac498211423c8debfd653c1d8d12543765
---

*This post is co-written by TrueLook and AWS.*

[TrueLook](https://www.truelook.com/)
is a construction camera and jobsite intelligence company that provides real-time visibility into construction projects. Its platform combines high-resolution time-lapse cameras, live video streaming, and AI-powered insights to help teams monitor progress, improve accountability, and reduce risk across the entire project lifecycle.

TrueLook used
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
to build and deploy an AI-powered construction safety monitoring system that automatically detects personal protective equipment (PPE) by combining TrueLook’s experience in jobsite camera systems using the AWS machine learning (ML) infrastructure. TrueLook has built a solution that identifies safety issues through automated image analysis to identify PPEs such as hard hats, high-visibility safety vests, safety helmets, gloves, protective eyewear, and much more. Through this system, project teams can surface unsafe working conditions, non-compliant behavior, and exposure to high-risk zones faster, strengthening overall safety governance. AI is helping TrueLook move from manual checks to a smarter, more scalable approach to jobsite safety.

This post provides a detailed architectural overview of how TrueLook built its AI-powered safety monitoring system using SageMaker AI, highlighting key technical decisions, pipeline design patterns, and MLOps best practices. You will gain valuable insights into designing scalable computer vision solutions on AWS, particularly around model training workflows, automated pipeline creation, and production deployment strategies for real-time inference.

## Construction safety: The critical challenge

Construction sites are among the most hazardous work environments, with workers facing risks from heavy machinery, elevated work areas, electrical hazards, and chemical exposures. The Occupational Safety and Health Administration (OSHA) reports that construction accounts for
[one in five worker deaths](https://www.bls.gov/opub/ted/2025/fatal-falls-in-the-construction-industry-in-2023.htm)
in the U.S. each year, despite representing a significantly smaller share of the total workforce. Beyond the human cost, safety incidents create significant financial burdens through workers’ compensation claims, project delays, regulatory fines, and potential litigation.

Traditional safety monitoring relies heavily on manual oversight with safety managers conducting periodic site walks, reviewing footage after incidents occur, or depending on workers to self-report violations. However, this approach faces fundamental limitations:

* **Scale constraints**
  – Large construction projects with multiple sites and hundreds of workers cannot be effectively monitored by human observers alone
* **Inconsistent coverage**
  – Manual monitoring is subject to fatigue, distraction, and human error, leading to missed violations during critical moments
* **Reactive response**
  – Traditional methods often identify safety issues only after incidents have occurred, limiting opportunities for prevention
* **Resource intensive**
  – Deploying sufficient human monitors across all sites and shifts requires significant personnel investment
* **Compliance gaps**
  – Inconsistent documentation makes it difficult to maintain the comprehensive audit trails required by OSHA and other regulatory bodies

These challenges create a need for automated, scalable, safety monitoring solutions that can provide consistent, real-time oversight across construction operations.

## Solution overview

TrueLook’s AI-powered PPE detection and monitoring solution uses AWS infrastructure and ML to detect safety compliance issues in construction zones through site imagery. TrueLook sources images to use in PPE detection from on-site cameras. To build, train, and deploy these models, TrueLook uses SageMaker AI, which provides managed infrastructure for the entire ML workflow. By offloading the undifferentiated heavy lifting of infrastructure setup and orchestration to SageMaker AI, TrueLook’s team can focus on improving model accuracy and reliability, helping to ensure that the solution scales effectively across customer sites. The following architecture diagram illustrates the end-to-end workflow, highlighting how multiple AWS services are integrated to deliver a seamless, scalable AI solution.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/07/ml-19468-1.png)

TrueLook’s labeled image dataset moves through a training pipeline in three key stages: preprocessing (
[SageMaker Processing Job](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
), training (
[SageMaker Training Job](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)
), and versioning with observability (
[SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
). SageMaker Processing jobs handled image cleaning and preparation at scale, running on single or multiple nodes depending on dataset size. SageMaker Training jobs executed the model training using built-in PyTorch containers and NVIDIA GPUs. With a basic runtime configuration with SageMaker PyTorch estimators, the same script could run on a single-node multi-GPU setup or scale out to distributed multi-node training, so that TrueLook could balance speed and accuracy as needed. Trained models were then versioned and stored in the SageMaker Model Registry, providing a central hub for tracking, governance, and deployment.

As indicated in the preceding architecture diagram, this workflow is orchestrated end-to-end with SageMaker Pipelines, which stitches preprocessing, training, and registration into an automated, repeatable flow. By using the managed MLflow integration and TensorBoard functionality offered by SageMaker, TrueLook could track experiments, compare performance, and provide repeatability at scale, making it straightforward to fine-tune models and deliver accurate PPE detection across its customer construction sites nationwide.

After models are trained, evaluated, and approved, deployment is handled through the fully managed hosting service available through SageMaker AI. Real-time endpoints deliver low-latency inference at scale, powering PPE detection directly on live video streams or snapshots. When a violation is detected, the system triggers downstream alerts that notify customers in real time. To keep the system continuously improving, TrueLook extends this pipeline with an active learning loop. By dropping new batches of images into
[Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3/)
, the workflow automatically triggers fine-tuning or retraining through a continuous integration and delivery (CI/CD) process. Before promotion to production, each candidate model passes through governance checks in the SageMaker Model Registry, runtime evaluation with MLflow, and visual inference validation with Tensorboard. Only after these steps are complete, are new models deployed, helping to ensure reliability and consistency at scale.

## Build high performing computer vision object detection models with SageMaker AI

Training accurate computer vision models starts with high-quality annotated data—a step that often becomes a bottleneck in developing AI-powered services. For TrueLook, building a reliable PPE detection model means creating a labeled dataset that captured all major classes of violations—people, hard hats, safety vests, safety boots, and more—under diverse conditions such as varying scenes, lighting, orientations, and perspectives. These annotations came from TrueLook’s nationwide network of video camera feeds across construction sites.To accelerate progress and improve model quality, TrueLook’s engineering team partnered with the SageMaker AI go-to-market (GTM) data science team to design a high accuracy multi-stage training pipeline. This approach reduced the time required to move from experimentation to production by pairing the deep computer vision and data science expertise of AWS and TrueLook with the simplified managed training and deployment workflows supported by SageMaker AI. The result was a scalable, multi-stage pipeline that enabled faster iteration, simplified operational complexity, and delivered accuracy improvements beyond TrueLook’s previous state-of-the-art PPE detection models.

### Early experiments and alternative approaches

TrueLook began by experimenting with other providers that offered UI or API driven workflows for low-code and no-code ML and deep learning (DL) model training. TrueLook initially used default, vendor-recommended hyperparameters and subsequently retrained models after adjusting exposed parameters, such as batch size, learning rate, and confidence thresholds, to quickly fine-tune and evaluate object detection models using their own datasets. However, the limited control over the training process didn’t yield results sufficient for production readiness, because model performance plateaued within a narrow range because of the lack of additional tuning and optimization controls. For example, training with an initial set of 1,000 labeled images produced mean average precision (mAP) in the 60–70% range. While this proved the feasibility of the approach, results also showed that performance scaled tightly with the number of labeled images available, highlighting the need for a more advanced and scalable pipeline.

### A three-stage fine-tuning pipeline using SageMaker AI

Early experimentation with low-code and no-code approaches revealed the need to domain-shift a pre-trained, open-domain object detection model—originally trained to recognize generic objects such as vehicles, people, and animals—into the construction and safety domain. This initial domain adaptation enables the model to learn construction-specific visual concepts, including safety equipment and worker presence in complex job-site conditions such as partial occlusion, using curated open-source construction datasets. This domain-shifted object detection model is then further fine-tuned on customer-specific datasets to align the model’s target classes with each customer’s labeling standards and site conditions. The following diagram illustrates this progression as a three-stage training workflow.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/07/ml-19468-3.png)

1. **Pretrained model**
   : Select a pretrained Computer Vision (CV) object detection model trained on large-scale open-source images
2. **Domain adaptation**
   : Fine-tune a pre-trained model with openly available construction safety domain dataset
3. **Fine tuning**
   : Fine-tune the domain-adapted model on TrueLook’s annotated dataset to rapidly improve accuracy

#### YOLO object detection family of models

Before examining the multistage training workflow, we want to introduce the object detection model at the heart of TrueLook’s AI-powered construction safety system.

[YOLO (You Only Look Once)](https://docs.ultralytics.com/)
is a family of real-time object detection models optimized for fast, single-pass detection with a strong balance of accuracy and throughput, making it well-suited for dynamic environments such as construction jobsites.
[YOLOv11](https://docs.ultralytics.com/models/yolo11/)
advances this lineage with architectural improvements that enhance feature extraction, deliver higher accuracy with fewer parameters, and enable faster inference, even on constrained hardware, while also supporting tasks like segmentation and pose estimation.

#### Multi-stage object detection fine-tuning workflow

In this section, we describe the end-to-end approach used to select, adapt, and fine-tune a pretrained vision model for construction site safety monitoring,

* **Selecting a pretrained model**
  – The team evaluated pretrained models based on factors such as size, accuracy, training metrics, class coverage, and licensing. YOLOv11 was selected as the base model for its strong performance and suitability for construction-related use cases.
* **Domain adaptation**
  – Pretrained models are often trained on broad classes such as cars, animals, or everyday objects. By adapting these weights to focus on construction-specific classes—such as hard hats, safety cones, and workers in safety zones—the model gained domain awareness. This adaptation used openly available datasets like
  *Roboflow: Construction Safety*
  and benefitted from data augmentation to improve robustness across perspectives, occlusions, and lighting conditions.
* **Fine-tuning with TrueLook data**
  – The domain-adapted model was then fine-tuned on TrueLook’s proprietary, high-quality labeled dataset. Because the model already recognized PPE classes reasonably well after stage two, fine-tuning sharpened its performance on imagery from TrueLook’s live construction feeds. Additional training-time augmentations further improved generalization under real-world conditions.

This staged approach proved highly effective. For example, with the same 1,000 labeled images, the pipeline achieved mAP scores in the 80–90% range—an improvement of 20 points over the alternate provider’s workflow. Another benefit of this design was efficiency: stages one and two needed to be run only once, producing a reusable domain-adapted model. Whenever new data became available, TrueLook could rerun stage three, reducing training time while continuously improving on overall model accuracy.In contrast, low-code and no-code alternatives typically offer limited control over model architecture, training strategy, and multi-stage optimization, making it difficult to perform explicit domain adaptation and iterative fine-tuning at scale. While these tools can accelerate initial prototyping, they often fall short when higher accuracy, reproducibility, and production-grade customization are required for complex, real-world environments like construction jobsites.

## Operationalizing with SageMaker AI

By using SageMaker AI, TrueLook operationalized its multi-stage object detection workflow as a scalable, production-ready
[MLOps](https://aws.amazon.com/sagemaker/ai/mlops/)
framework. By using managed capabilities such as
[SageMaker Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-overview.html)
and the
[SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
, TrueLook automated the full model lifecycle, from training and evaluation to versioning and deployment, while maintaining strong governance and traceability. This approach reduced manual orchestration, reduced operational risk, and provided the reliability and observability required to run AI-powered safety monitoring services at scale.

### Implementing end-to-end object detection using SageMaker Pipelines

Building an accurate object detection model was only the first step in building a comprehensive AI-powered construction safety system. Ongoing improvement required rapid iteration, controlled experimentation, and reliable promotion of high-quality models as new data became available. To enable this, TrueLook and AWS implemented an automated workflow using SageMaker Pipelines that supports parallel experimentation with the ability to add automated model evaluation that automatically filters out underperforming models and advancing only those that meet predefined performance thresholds, resulting in faster iteration, improved reproducibility, and a dependable path from experimentation to production.

### Creating the pipeline – Define once philosophy

TrueLook implemented a reusable, parameterized workflow that automates the full lifecycle of its construction safety object detection models. The workflow begins by transforming raw jobsite imagery into model-ready datasets. It then trains a YOLOv11 object detection model and automatically registers the trained model in a central model registry for versioning and governance. Built-in evaluation steps measure model performance (such as mAP, F1-score, and so on) against predefined thresholds. Models that meet these standards are promoted for deployment and registered as versioned artifacts in a central model registry. These registered models can be reviewed, commented on, approved, or rejected through auditable workflows, while underperforming runs are automatically stopped to prevent low-quality models from reaching production.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/07/ml-19468-4-972x1024.png)

TrueLook defined a reusable, parameterized workflow that reduces the need to rebuild orchestration logic for each model iteration. Teams can trigger repeatable runs by adjusting datasets and training settings such as image resolution, batch size, learning rates, training duration, and data augmentation strategies. They can also adjust compute configurations including GPU instance type, number of GPUs, and memory capacity. Multiple runs can execute in parallel, while automated gating and conditional execution enforce consistent quality standards, reducing operational overhead, minimizing human error, and accelerating continuous model improvement at scale.

```
# Core experimentation parameters
object_detection_params = ParameterString(
    name="pre_training_params",
    default_value="epochs=1,lr0=1e-3,batch=1"
)
...
# Training instance as a parameter
training_instance_type = ParameterString(
    name="ml_instance ",
    default_value="ml.g6e.12xlarge"
)
...
# Stage 2 model hyperparams
fine_tuning_params = ParameterString(
    name="fine_tuning_params",
    default_value="epochs=1,lr0=1e-4,batch=1"
)
```

### Governed experimentation and automated deployment

Every training run is automatically tracked through integrated experiment management and model registration systems that capture parameters, metrics, and model artifacts in versioned histories. This creates a searchable catalog of experimental results, enabling systematic comparison of different training strategies and identification of optimal configurations for construction safety detection. Approved models are then automatically deployed to GPU-accelerated production endpoints using versioned, timestamped naming to prevent conflicts. This creates a seamless and repeatable path from experimentation to real-time deployment, enabling rapid iteration while maintaining strong governance and minimal manual intervention.

## Summary

This case study highlights how the AWS–TrueLook collaboration enabled construction teams to use managed ML services for scalable, production-ready safety monitoring while avoiding heavy infrastructure overhead. It demonstrates a proven three-stage fine-tuning approach that delivers high-accuracy construction safety models even with limited data, surpassing what is typically achievable with low-code or no-code alternatives. This post also provides practical guidance on building, training, and deploying computer vision models using AWS managed services, and emphasizes the value of early AWS engagement for architecture design and domain-specific implementation. TrueLook’s success illustrates how industry-focused AI/ML solutions, backed by deep domain expertise, can effectively automate and elevate jobsite safety operations.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/steven-1-100x100.jpg)
Steven McDowall**
is a technology and product leader with extensive experience in product strategy, product management, and software engineering. He currently serves as Vice President of Product at TrueLook, where he leads the development of construction-technology and real-time video solutions, bringing a strong engineering foundation and user-focused approach to product execution.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/scott-2-100x101.jpg)
Scott Anderson**
is the Director of Platform Engineering at TrueLook, where he leads the development and scalability of the systems that power the company’s core platform. He brings over 30 years of deep technical experience and a pragmatic engineering mindset, with a focus on building reliable, maintainable infrastructure that supports long-term product growth.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/marc-1-100x100.jpg)
Marc Ritter**
is a Lead Software Engineer at TrueLook, where he drives the design and implementation of core platform features and contributes to advanced technology initiatives. He applies a strong engineering mindset to solving complex technical challenges and enhancing the performance and reliability of TrueLook’s solutions. Marc is passionate about leveraging thoughtful architecture and collaborative development to build scalable software systems.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/pranav-100x100.jpeg)
Pranav Murthy**
is a Senior Generative AI Data Scientist at AWS, specializing in helping organizations innovate with Generative AI, Deep Learning, and Machine Learning on Amazon SageMaker AI. Over the past 10+ years, he has developed and scaled advanced computer vision (CV) and natural language processing (NLP) models to tackle high-impact problems—from optimizing global supply chains to enabling real-time video analytics and multilingual search. When he’s not building AI solutions, Pranav enjoys playing strategic games like chess, traveling to discover new cultures, and mentoring aspiring AI practitioners. You can find Pranav on
[LinkedIn](https://www.linkedin.com/in/pranavvm26/)
.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/gaurav-1-100x134.jpg)
Gaurav Singh**
is a Senior Customer Solutions Manager at AWS with over 20 years of experience in cloud transformation and IT consulting. He specializes in guiding customers through their cloud journey, serving as a trusted advisor for migration, modernization, and innovation opportunities. Gaurav provides strategic growth guidance that helps customers achieve their goals while leveraging AWS services to drive innovation and operational excellence. You can find Gaurav on
[LinkedIn](https://www.linkedin.com/in/gaurav--singh/)
.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/01/08/surya-1-100x134.jpg)
Surya Kari**
is a Senior Generative AI Data Scientist at AWS, specializing in developing solutions leveraging state-of-the-art foundation models. He has extensive experience working with advanced language models including DeepSeek-R1, the Llama family, and Qwen, focusing on their fine-tuning and optimization for specific scientific applications. His expertise extends to implementing efficient training pipelines and deployment strategies using AWS SageMaker, enabling the scaling of foundation models from development to production. He collaborates with customers to design and implement generative AI solutions, helping them navigate model selection, fine-tuning approaches, and deployment strategies to achieve optimal performance for their specific use cases. You can find Surya on
[LinkedIn](https://www.linkedin.com/in/suryakari/)
.