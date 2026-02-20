---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-20T22:15:31.996286+00:00'
exported_at: '2026-02-20T22:15:34.267967+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-2-improved-observability-and-enhanced-features-for-sagemaker-ai-model-customization-and-hosting
structured_data:
  about: []
  author: ''
  description: In 2025, Amazon SageMaker AI made several improvements designed to
    help you train, tune, and host generative AI workloads. In Part 1 of this series,
    we discussed Flexible Training Plans and price performance improvements made to
    inference components. In this post, we discuss enhancements made to observability,
    model customization, and model hosting. These improvements facilitate a whole
    new class of customer use cases to be hosted on SageMaker AI.
  headline: 'Amazon SageMaker AI in 2025, a year in review part 2: Improved observability
    and enhanced features for SageMaker AI model customization and hosting'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-2-improved-observability-and-enhanced-features-for-sagemaker-ai-model-customization-and-hosting
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Amazon SageMaker AI in 2025, a year in review part 2: Improved observability
  and enhanced features for SageMaker AI model customization and hosting'
updated_at: '2026-02-20T22:15:31.996286+00:00'
url_hash: c761f6773452754c33c16ed8ad558e64c3d6f994
---

In 2025,
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai)
made several improvements designed to help you train, tune, and host generative AI workloads. In
[Part 1](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-1-flexible-training-plans-and-improvements-to-price-performance-for-inference-workloads/)
of this series, we discussed Flexible Training Plans and price performance improvements made to inference components.

In this post, we discuss enhancements made to observability, model customization, and model hosting. These improvements facilitate a whole new class of customer use cases to be hosted on SageMaker AI.

## Observability

The observability enhancements made to SageMaker AI in 2025 help deliver enhanced visibility into model performance and infrastructure health. Enhanced metrics provide granular, instance-level and container-level tracking of CPU, memory, GPU utilization, and invocation performance with configurable publishing frequencies, so teams can diagnose latency issues and resource inefficiencies that were previously hidden by endpoint-level aggregation. Rolling updates for inference components help transform deployment safety by alleviating the need for duplicate infrastructure provisioning—updates deploy in configurable batches with integrated
[Amazon CloudWatch](http://aws.amazon.com/cloudwatch)
alarm monitoring that triggers automatic rollbacks if issues are detected, facilitating zero-downtime deployments while minimizing risk through gradual validation.

### Enhanced Metrics

SageMaker AI introduced enhanced metrics this year, helping deliver granular visibility into endpoint performance and resource utilization at both instance and container levels. This capability addresses a critical gap in observability, facilitating customers’ diagnosis of latency issues, invocation failures, and resource inefficiencies that were previously obscured by endpoint-level aggregation. Enhanced metrics provide instance-level tracking of CPU, memory, and GPU utilization alongside invocation performance metrics (latency, errors, throughput) with
`InstanceId`
dimensions for the SageMaker endpoints. For inference components, container-level metrics offer visibility into individual model replica resource consumption with both ContainerId and
`InstanceId`
dimensions.

You can configure metric publishing frequency, supplying near real-time monitoring for critical applications requiring rapid response. The self-service enablement through a simple
`MetricsConfig`
parameter in the
[CreateEndpointConfig](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html)
API helps reduce time-to-insight, helping you self-diagnose performance issues. Enhanced metrics help you identify which specific instance or container requires attention, diagnose uneven traffic distribution across hosts, optimize resource allocation, and correlate performance issues with specific infrastructure resources. The feature works seamlessly with CloudWatch alarms and automatic scaling policies, providing proactive monitoring and automated responses to performance anomalies.

To enable enhanced metrics, add the
`MetricsConfig`
parameter when creating your endpoint configuration:

```
response = sagemaker_client.create_endpoint_config(
    EndpointConfigName='my-config',
    ProductionVariants=[{...}],
    MetricsConfig={
        'EnableEnhancedMetrics': True,
        'MetricPublishFrequencyInSeconds': 60  # Supported: 10, 30, 60, 120, 180, 240, 300
    }
)
```

Enhanced metrics are available across the AWS Regions for both single model endpoints and inference components, providing comprehensive observability for production AI deployments at scale.

### Guardrail deployment with rolling updates

SageMaker AI introduced rolling updates for inference components, helping transform how you can deploy model updates with enhanced safety and efficiency. Traditional blue/green deployments require provisioning duplicate infrastructure, creating resource constraints—particularly for GPU-heavy workloads like large language models. Rolling updates deploy new model versions in configurable batches while dynamically scaling infrastructure, with integrated CloudWatch alarms monitoring metrics to trigger automatic rollbacks if issues are detected. This approach helps alleviate the need to provision duplicate fleets, reduces deployment overhead, and enables zero-downtime updates through gradual validation that minimizes risk while maintaining availability. For more details, see
[Enhance deployment guardrails with inference component rolling updates for Amazon SageMaker AI inference](https://aws.amazon.com/blogs/machine-learning/enhance-deployment-guardrails-with-inference-component-rolling-updates-for-amazon-sagemaker-ai-inference/)
.

## Usability

SageMaker AI usability improvements focus on removing complexity and accelerating time-to-value for AI teams. Serverless model customization reduces time for infrastructure planning by automatically provisioning compute resources based on model and data size, supporting advanced techniques like reinforcement learning from verifiable rewards (RLVR) and reinforcement learning from AI feedback (RLAIF) through both UI-based and code-based workflows with integrated MLflow experiment tracking. Bidirectional streaming enables real-time, multi-modal applications by maintaining persistent connections where data flows simultaneously in both directions—helping transform use cases like voice agents and live transcription from transactional exchanges into continuous conversations. Enhanced connectivity through comprehensive
[AWS PrivateLink](https://aws.amazon.com/privatelink/)
support across the Regions and IPv6 compatibility helps make sure enterprise deployments can meet strict compliance alignment requirements while future-proofing network architectures.

### Serverless model customization

The new SageMaker AI serverless customization capability addresses a critical challenge faced by organizations: the lengthy and complex process of fine-tuning AI models, which traditionally takes months and requires significant infrastructure management expertise. Many teams struggle with selecting appropriate compute resources, managing the technical complexity of advanced fine-tuning techniques like reinforcement learning, and navigating the end-to-end workflow from model selection through evaluation to deployment.

[![Customize a model directly in the UI](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/ML-20228-image-1.jpeg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/ML-20228-image-1.jpeg)

This serverless solution helps remove these barriers by automatically provisioning the right compute resources based on model and data size, making it possible for teams to focus on model tuning rather than infrastructure management and helping accelerate the customization process. The solution supports popular models including
[Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/)
, DeepSeek, GPT-OSS, Llama, and Qwen, providing both UI-based and code-based customization workflows that make advanced techniques accessible to teams with varying levels of technical expertise.

The solution offers multiple advanced customization techniques, including supervised fine-tuning, direct preference optimization, RLVR, and RLAIF. Each technique helps optimize models in different ways, with selection influenced by factors such as dataset size and quality, available computational resources, task requirements, desired accuracy levels, and deployment constraints. The solution includes integrated experiment tracking through serverless MLflow for automatic logging of critical metrics without code modifications, helping teams monitor and compare model performance throughout the customization process.

[![Customize a model directly in the UI](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/ML-20228-image-1.jpeg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/ML-20228-image-1.jpeg)

Deployment flexibility is a key feature, with options to deploy to either
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
for serverless inference or SageMaker AI endpoints for controlled resource management. The solution includes built-in model evaluation capabilities to compare customized models against base models, an interactive playground for testing with prompts or chat mode, and seamless integration with the broader
[Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
environment. This end-to-end workflow—from model selection and customization through evaluation and deployment—is handled entirely within a unified interface.

Currently available in US East (N. Virginia), US West (Oregon), Asia Pacific (Tokyo), and Europe (Ireland) Regions, the service operates on a pay-per-token model for both training and inference. This pricing approach helps make it cost-effective for organizations of different sizes to customize AI models without upfront infrastructure investments, and the serverless architecture helps make sure teams can scale their model customization efforts based on actual usage rather than provisioned capacity. For more information on this core capability, see
[New serverless customization in Amazon SageMaker AI accelerates model fine-tuning](https://aws.amazon.com/blogs/aws/new-serverless-customization-in-amazon-sagemaker-ai-accelerates-model-fine-tuning/)
.

### Bidirectional streaming

SageMaker AI introduced the bidirectional streaming capability in 2025, transforming inference from transactional exchanges into continuous conversations between users and models. This feature enables data to flow simultaneously in both directions over a single persistent connection, supporting real-time multi-modal use cases ranging from audio transcription and translation to voice agents. Unlike traditional approaches where clients send complete questions and wait for complete answers, bidirectional streaming allows speech and responses to flow concurrently—users can see results as soon as models begin generating them, and models can maintain context across continuous streams without re-sending conversation history. The implementation combines HTTP/2 and WebSocket protocols, with the SageMaker infrastructure managing efficient multiplexed connections from clients through routers to model containers.

The feature supports both bring-your-own-container implementations and partner integrations, with Deepgram serving as a launch partner offering their Nova-3 speech-to-text model through
[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-wkxd2vmfoaujo)
. This capability addresses critical enterprise requirements for real-time voice AI applications—particularly for organizations with strict compliance needs requiring audio processing to remain within their Amazon virtual private cloud (VPC)—while removing the operational overhead traditionally associated with self-hosted real-time AI solutions. The persistent connection approach reduces infrastructure overhead from TLS handshakes and connection management, replacing short-lived connections with efficient long-running sessions.

Developers can implement bidirectional streaming through two approaches: building custom containers that implement WebSocket protocol at
`ws://localhost:8080/invocations-bidirectional-stream`
with the appropriate Docker label (
`com.amazonaws.sagemaker.capabilities.bidirectional-streaming=true`
), or deploying pre-built partner solutions like Deepgram’s Nova-3 model directly from AWS Marketplace. The feature requires containers to handle incoming WebSocket data frames and send response frames back to SageMaker, with sample implementations available in both Python and TypeScript. For more details, see
[Introducing bidirectional streaming for real-time inference on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/introducing-bidirectional-streaming-for-real-time-inference-on-amazon-sagemaker-ai/)
.

### IPv6 and PrivateLink

Additionally, SageMaker AI expanded its connectivity capabilities in 2025 with comprehensive PrivateLink support across Regions and IPv6 compatibility for both public and private endpoints. These enhancements significantly help improve the service’s accessibility and security posture for enterprise deployments. PrivateLink integration makes it possible to access SageMaker AI endpoints privately from your VPCs without traversing the public internet, keeping the traffic within the AWS network infrastructure. This is particularly valuable for organizations with strict compliance requirements or data residency policies that mandate private connectivity for machine learning workloads.

The addition of IPv6 support for SageMaker AI endpoints addresses the growing need for modern IP addressing as organizations transition away from IPv4. You can now access SageMaker AI services using IPv6 addresses for both public endpoints and private VPC endpoints, providing flexibility in network architecture design and future-proofing infrastructure investments. The dual-stack capability (supporting both IPv4 and IPv6) facilitates backward compatibility while helping organizations adopt IPv6 at their own pace. Combined with PrivateLink, these connectivity enhancements help make SageMaker AI more accessible and secure for diverse enterprise networking environments, from traditional on-premises data centers connecting using
[AWS Direct Connect](https://aws.amazon.com/directconnect/)
to modern cloud-based architectures built entirely on IPv6.

## Conclusion

The 2025 enhancements to SageMaker AI represent a significant leap forward in making generative AI workloads more observable, reliable, and accessible for enterprise customers. From granular performance metrics that pinpoint infrastructure bottlenecks to serverless customization, these improvements address the real-world challenges teams face when deploying AI at scale. The combination of enhanced observability, safer deployment mechanisms, and streamlined workflows helps empower organizations to move faster while maintaining the reliability and security standards required for production systems.

These capabilities are available now across Regions, with features like enhanced metrics, rolling updates, and serverless customization ready to help transform how you can build and deploy AI applications. Whether you’re fine-tuning models for domain-specific tasks, building real-time voice agents with bidirectional streaming, or facilitating deployment safety with rolling updates and integrated monitoring, SageMaker AI helps provide the tools to accelerate your AI journey while reducing operational complexity.

Get started today by exploring the
[enhanced metrics documentation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html)
, trying
[serverless model customization](https://aws.amazon.com/sagemaker/)
, or implementing
[bidirectional streaming](https://aws.amazon.com/blogs/machine-learning/introducing-bidirectional-streaming-for-real-time-inference-on-amazon-sagemaker-ai/)
for your real-time inference workloads. For comprehensive guidance on implementing these features, refer to the
[Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
or reach out to your AWS account team to discuss how these capabilities can support your specific use cases.

---

### About the authors

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/frgud.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/frgud.jpg)
**Dan Ferguson**
is a Sr. Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/21/DmitrySoldatkin.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/21/DmitrySoldatkin.jpg)
**Dmitry Soldatkin**
is a Senior Machine Learning Solutions Architect at AWS, helping customers design and build AI/ML solutions. Dmitry’s work covers a wide range of ML use cases, with a primary interest in generative AI, deep learning, and scaling ML across the enterprise. He has helped companies in many industries, including insurance, financial services, utilities, and telecommunications. He has a passion for continuous innovation and using data to drive business outcomes. Prior to joining AWS, Dmitry was an architect, developer, and technology leader in data analytics and machine learning fields in the financial services industry.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/12/02/lokravi.jpeg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/12/02/lokravi.jpeg)
**Lokeshwaran Ravi**
is a Senior Deep Learning Compiler Engineer at AWS, specializing in ML optimization, model acceleration, and AI security. He focuses on enhancing efficiency, reducing costs, and building secure ecosystems to democratize AI technologies, making cutting-edge ML accessible and impactful across industries.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/sadaf-100x133.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/sadaf.jpg)
**Sadaf Fardeen**
leads Inference Optimization charter for SageMaker. She owns optimization and development of LLM inference containers on SageMaker.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/sumakasa-100x133.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/sumakasa.jpg)
**Suma Kasa**
is an ML Architect with the SageMaker Service team focusing on the optimization and development of LLM inference containers on SageMaker.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/04/12/Ram-Vegiraju-.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2023/04/12/Ram-Vegiraju-.jpg)
**Ram Vegiraju**
is a ML Architect with the SageMaker Service team. He focuses on helping customers build and optimize their AI/ML solutions on Amazon SageMaker. In his spare time, he loves traveling and writing.

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/dlragha-100x133.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/19/dlragha.jpg)
**Deepti Ragha**
is a Senior Software Development Engineer on the Amazon SageMaker AI team, specializing in ML inference infrastructure and model hosting optimization. She builds features that improve deployment performance, reduce inference costs, and make ML accessible to organizations of all sizes. Outside of work, she enjoys traveling, hiking, and gardening.