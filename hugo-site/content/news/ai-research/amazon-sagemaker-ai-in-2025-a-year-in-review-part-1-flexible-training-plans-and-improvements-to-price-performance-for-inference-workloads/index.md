---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-02T03:56:46.702798+00:00'
exported_at: '2026-03-02T03:56:49.807286+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-1-flexible-training-plans-and-improvements-to-price-performance-for-inference-workloads
structured_data:
  about: []
  author: ''
  description: 'In 2025, Amazon SageMaker AI saw dramatic improvements to core infrastructure
    offerings along four dimensions: capacity, price performance, observability, and
    usability. In this series of posts, we discuss these various improvements and
    their benefits. In Part 1, we discuss capacity improvements with the launch of
    F...'
  headline: 'Amazon SageMaker AI in 2025, a year in review part 1: Flexible Training
    Plans and improvements to price performance for inference workloads'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-1-flexible-training-plans-and-improvements-to-price-performance-for-inference-workloads
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Amazon SageMaker AI in 2025, a year in review part 1: Flexible Training Plans
  and improvements to price performance for inference workloads'
updated_at: '2026-03-02T03:56:46.702798+00:00'
url_hash: 99708c0a0a0c29e2394c773e939d9c8f5b5ddd97
---

In 2025,
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker-ai)
saw dramatic improvements to core infrastructure offerings along four dimensions: capacity, price performance, observability, and usability. In this series of posts, we discuss these various improvements and their benefits. In Part 1, we discuss capacity improvements with the launch of Flexible Training Plans. We also describe improvements to price performance for inference workloads. In
[Part 2](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-2-improved-observability-and-enhanced-features-for-sagemaker-ai-model-customization-and-hosting/)
, we discuss enhancements made to observability, model customization, and model hosting.

## Flexible Training Plans for SageMaker

SageMaker AI Training Plans now support inference endpoints, extending a powerful capacity reservation capability originally designed for training workloads to address the critical challenge of GPU availability for inference deployments. Deploying large language models (LLMs) for inference requires reliable GPU capacity, especially during critical evaluation periods, limited-duration production testing, or predictable burst workloads. Capacity constraints can delay deployments and impact application performance, particularly during peak hours when on-demand capacity becomes unpredictable. Training Plans can help solve this problem by making it possible to reserve compute capacity for specified time periods, facilitating predictable GPU availability precisely when teams need it most.

The reservation workflow is designed for simplicity and flexibility. You begin by searching for available capacity offerings that match your specific requirements—selecting instance type, quantity, duration, and desired time window. When you identify a suitable offering, you can create a reservation that generates an Amazon Resource Name (ARN), which serves as the key to your guaranteed capacity. The upfront, transparent pricing model helps support accurate budget planning while minimizing concerns about infrastructure availability, so teams can focus on their evaluation metrics and model performance rather than worrying about whether capacity will be available when they need it.

Throughout the reservation lifecycle, teams maintain operational flexibility to manage their endpoints as requirements evolve. You can update endpoints to new model versions while maintaining the same reserved capacity, using iterative testing and refinement during evaluation periods. Scaling capabilities help teams adjust instance counts within their reservation limits, supporting scenarios where initial deployments are conservative, but higher throughput testing becomes necessary. This flexibility helps make sure teams aren’t locked into rigid infrastructure decisions while still being able to benefit from the reserved capacity during critical time windows.

With support for endpoint updates, scaling capabilities, and seamless capacity management, Training Plans help give you control over both GPU availability and costs for time-bound inference workloads. Whether you’re running competitive model benchmarks to select the best-performing variant, performing limited-duration A/B tests to validate model improvements, or handling predictable traffic spikes during product launches, Training Plans for inference endpoints help provide the capacity guarantees teams need with transparent, upfront pricing. This approach is particularly valuable for data science teams conducting week-long or month-long evaluation projects, where the ability to reserve specific GPU instances in advance minimizes the uncertainty of on-demand availability and enables more predictable project timelines and budgets.

For more information, see
[Amazon SageMaker AI now supports Flexible Training Plans capacity for Inference](https://aws.amazon.com/about-aws/whats-new/2025/11/sagemaker-ai-flexible-training-plans-inference/)
.

## Price performance

Enhancements made to SageMaker AI in 2025 help optimize inference economics through four key capabilities. Flexible Training Plans extend to inference endpoints with transparent upfront pricing. Inference components add Multi-AZ availability and parallel model copy placement during scaling that help accelerate deployment. EAGLE-3 speculative decoding delivers increased throughput improvements on inference requests. Dynamic multi-adapter inference enables on-demand loading of LoRA adapters.

### Improvements to inference components

Generative models only start delivering value when they’re serving predictions in production. As applications scale, inference infrastructure must be as dynamic and reliable as the models themselves. That’s where SageMaker AI inference components come in. Inference components provide a modular way to manage model inference within an endpoint. Each inference component represents a self-contained unit of compute, memory, and model configuration that can be independently created, updated, and scaled. This design helps you operate production endpoints with greater flexibility. You can deploy multiple models, adjust capacity quickly, and roll out updates safely without redeploying the entire endpoint. For teams running real-time or high-throughput applications, inference components help bring fine-grained control to inference workflows. In the following sections, we review three major enhancements to SageMaker AI inference components that make them even more powerful in production environments. These updates add Multi-AZ high availability, controlled concurrency for multi-tenant workloads, and parallel scaling for faster response to traffic surges. Together, they help make running AI at scale more resilient, predictable, and efficient.

### Building resilience with Multi-AZ high availability

Production systems face the same truth: failures happen. A single hardware fault, network issue, or Availability Zone outage can disrupt inference traffic and affect user experience. Now, SageMaker AI inference components automatically distribute workloads across multiple Availability Zones. You can run multiple inference component copies per Availability Zone, and SageMaker AI helps intelligently route traffic to instances that are healthy and have available capacity. This distribution adds fault tolerance at every layer of your deployment.

Multi-AZ high availability offers the following benefits:

* Minimizes single points of failure by spreading inference workloads across Availability Zones
* Automatically fails over to healthy instances when issues occur
* Keeps uptime high to meet strict SLA requirements
* Enables balanced cost and resilience through flexible deployment patterns

For example, a financial services company running real-time fraud detection can benefit from this feature. By deploying inference components across three Availability Zones, traffic can seamlessly redirect to the remaining Availability Zones if one goes offline, helping facilitate uninterrupted fraud detection when reliability matters most.

### Parallel scaling and NVMe caching

Traffic patterns in production are rarely steady. One moment your system is quiet; the next, it’s flooded with requests. Previously, scaling inference components happened sequentially—each new model copy waited for the previous one to initialize before starting. During spikes, this sequential process could add several minutes of latency. With parallel scaling, SageMaker AI can now deploy multiple inference component copies simultaneously when an instance and the required resources are available. This helps shorten the time required to respond to traffic surges and improves responsiveness for variable workloads. For example, if an instance needs three model copies, they now deploy in parallel instead of waiting on one another. Parallel scaling helps accelerate the deployment of model copies onto inference components but does not accelerate the scaling up of models when traffic increases beyond provisioned capacity. NVMe caching helps accelerate model scaling for already provisioned inference components by caching model artifacts and images. NVMe caching’s ability to reduce scaling times helps reduce inference latency during traffic spikes, lower idle costs through faster scale-down, and provide greater elasticity for serving unpredictable or volatile workloads.

### EAGLE-3

SageMaker AI has introduced (Extrapolation Algorithm for Greater Language-model Efficiency (EAGLE)-based adaptive speculative decoding to help accelerate generative AI inference. This enhancement supports six model architectures and helps you optimize performance using either SageMaker-provided datasets or your own application-specific data for highly adaptive, workload-specific results. The solution streamlines the workflow from optimization job creation through deployment, making it seamless to deliver low-latency generative AI applications at scale without compromising generation quality. EAGLE works by predicting future tokens directly from the model’s hidden layers rather than relying on an external draft model, resulting in more accurate predictions and fewer rejections. SageMaker AI automatically selects between EAGLE-2 and EAGLE-3 based on the model architecture, with launch support for LlamaForCausalLM, Qwen3ForCausalLM, Qwen3MoeForCausalLM, Qwen2ForCausalLM, GptOssForCausalLM (EAGLE-3), and Qwen3NextForCausalLM (EAGLE-2). You can train EAGLE models from scratch, retrain existing models, or use pre-trained models from SageMaker JumpStart, with the flexibility to iteratively refine performance using your own curated datasets collected through features like Data Capture. The optimization workflow integrates seamlessly with existing SageMaker AI infrastructure through familiar APIs (
`create_model`
,
`create_endpoint_config`
,
`create_endpoint`
) and supports widely used training data formats, including ShareGPT and OpenAI chat and completions. Benchmark results are automatically generated during optimization jobs, providing clear visibility into performance improvements across metrics like Time to First Token (TTFT) and throughput, with trained EAGLE models showing significant gains over both base models and EAGLE models trained only on built-in datasets.

To run an EAGLE-3 optimization job, run the following command in the
[AWS Command Line Interface](http://aws.amazon.com/cli)
(AWS CLI):

```
aws sagemaker --region us-west-2 create-optimization-job \
    --optimization-job-name <job-name> \
    --account-id <account-id> \
    --deployment-instance-type ml.p5.48xlarge \
    --max-instance-count 10 \
    --model-source '{
        "SageMakerModel": { "ModelName": "Created Model name" }
    }' \
    --optimization-configs'{
            "ModelSpeculativeDecodingConfig": {
                "Technique": "EAGLE",
                "TrainingDataSource": {
                    "S3DataType": "S3Prefix",
                    "S3Uri": "Enter custom train data location"
                }
            }
        }' \
    --output-config '{
        "S3OutputLocation": "Enter optimization output location"
    }' \
    --stopping-condition '{"MaxRuntimeInSeconds": 432000}' \
    --role-arn "Enter Execution Role ARN"
```

For more details, see
[Amazon SageMaker AI introduces EAGLE based adaptive speculative decoding to accelerate generative AI inference](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference/)
.

### Dynamic multi-adapter inference on SageMaker AI Inference

SageMaker AI helped enhance the efficient multi-adapter inference capability
[introduced at re:Invent 2024](https://aws.amazon.com/blogs/machine-learning/easily-deploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapter-inference/)
, which now supports dynamic loading and unloading of LoRA adapters during inference invocations rather than pinning them at endpoint creation. This enhancement helps optimize resource utilization for on-demand model hosting scenarios.

Previously, the adapters were downloaded to disk and loaded into memory during the
[CreateInferenceComponent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceComponent.html)
API call. With dynamic loading, adapters are registered using a lightweight, synchronous
`CreateInferenceComponent`
API, then downloaded and loaded into memory only when first invoked. This approach supports use cases where you can register thousands of fine-tuned adapters per endpoint while maintaining low-latency inference.

The system implements intelligent memory management, evicting least popular models during resource constraints. When memory reaches capacity—controlled by the
`SAGEMAKER_MAX_NUMBER_OF_ADAPTERS_IN_MEMORY`
environment variable—the system automatically unloads inactive adapters to make room for newly requested ones. Similarly, when disk space becomes constrained, the least recently used adapters are evicted from storage. This multi-tier caching strategy facilitates optimal resource utilization across CPU, GPU memory, and disk.

For security and compliance alignment, you can explicitly delete adapters using the
`DeleteInferenceComponent`
API. Upon deletion, SageMaker unloads the adapter from the base inference component containers and removes it from disk across the instances, facilitating the complete cleanup of customer data. The deletion process completes asynchronously with automatic retries, providing you with control over your adapter lifecycle while helping meet stringent data retention requirements.

This dynamic adapter loading capability powers the SageMaker AI
[serverless model customization feature](https://aws.amazon.com/blogs/aws/new-serverless-customization-in-amazon-sagemaker-ai-accelerates-model-fine-tuning/)
, which helps you fine-tune popular AI models like
[Amazon Nova](https://aws.amazon.com/ai/generative-ai/nova/)
, DeepSeek, Llama, and Qwen using techniques like supervised fine-tuning, reinforcement learning, and direct preference optimization. When you complete fine-tuning through the serverless customization interface, the output LoRA adapter weights flow seamlessly to deployment—you can deploy to SageMaker AI endpoints using multi-adapter inference components. The hosting configurations from training recipes automatically include the appropriate dynamic loading settings, helping make sure customized models can be deployed efficiently without requiring you to manage infrastructure or load the adapters at endpoint creation time.

The following steps illustrate how you can use this feature in practice:

1. Create a base inference component with your foundation model:

```
import boto3

sagemaker = boto3.client('sagemaker')

# Create base inference component with foundation model
response = sagemaker.create_inference_component(
    InferenceComponentName='llama-base-ic',
    EndpointName='my-endpoint',
    Specification={
        'Container': {
            'Image': 'your-container-image',
            'Environment': {
                'SAGEMAKER_MAX_NUMBER_OF_ADAPTERS_IN_MEMORY': '10'
            }
        },
        'ComputeResourceRequirements': {
            'NumberOfAcceleratorDevicesRequired': 2,
            'MinMemoryRequiredInMb': 16384
        }
    }
)
```

2. Register Your LoRA adapters:

```
# Register adapter - completes in < 1 second
response = sagemaker.create_inference_component(
    InferenceComponentName='my-custom-adapter',
    EndpointName='my-endpoint',
    Specification={
        'BaseInferenceComponentName': 'llama-base-ic',
        'Container': {
            'ArtifactUrl': 's3://amzn-s3-demo-bucket/adapters/customer-support/'
        }
    }
)
```

3. Invoke your adapter (it loads automatically on first use):

```
runtime = boto3.client('sagemaker-runtime')

# Invoke with adapter - loads into memory on first call
response = runtime.invoke_endpoint(
    EndpointName='my-endpoint',
    InferenceComponentName='llama-base-ic',
    TargetModel='s3://amzn-s3-demo-bucket/adapters/customer-support/',
    ContentType='application/json',
    Body=json.dumps({'inputs': 'Your prompt here'})
)
```

4. Delete adapters when no longer needed:

```
sagemaker.delete_inference_component(
    InferenceComponentName='my-custom-adapter'
)
```

This dynamic loading capability integrates seamlessly with the existing inference infrastructure of SageMaker, supporting the same base models and maintaining compatibility with the standard
`InvokeEndpoint`
API. By decoupling adapter registration from resource allocation, you can now deploy and manage more LoRA adapters cost-effectively, paying only for the compute resources actively serving inference requests.

## Conclusion

The 2025 SageMaker AI enhancements represent a significant leap forward in making generative AI inference more accessible, reliable, and cost-effective for production workloads. With Flexible Training Plans now supporting inference endpoints, you can gain predictable GPU capacity precisely when you need it—whether for critical model evaluations, limited-duration testing, or handling traffic spikes. The introduction of Multi-AZ high availability, controlled concurrency, and parallel scaling with NVMe caching for inference components helps make sure production deployments can scale rapidly while maintaining resilience across Availability Zones. The adaptive speculative decoding of EAGLE-3 delivers increased throughput without sacrificing output quality, and dynamic multi-adapter inference helps teams efficiently manage more fine-tuned LoRA adapters on a single endpoint. Together, these capabilities help reduce the operational complexity and infrastructure costs of running AI at scale, so teams can focus on delivering value through their models rather than managing underlying infrastructure.

These improvements directly address some of the most pressing challenges facing AI practitioners today: securing reliable compute capacity, achieving low-latency inference at scale, and managing the growing complexity of multi-model deployments. By combining transparent capacity reservations, intelligent resource management, and performance optimizations that help deliver measurable throughput gains, SageMaker AI helps organizations deploy generative AI applications with confidence. The seamless integration between model customization and deployment—where fine-tuned adapters flow directly from training to production hosting—further helps accelerate the journey from experimentation to production.

Ready to accelerate your generative AI inference workloads? Explore Flexible Training Plans for inference endpoints to secure GPU capacity for your next evaluation cycle, implement EAGLE-3 speculative decoding to help boost throughput on your existing deployments, or use dynamic multi-adapter inference to more efficiently serve customized models. Refer to the
[Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
to get started, and stay tuned for
[Part 2](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-in-2025-a-year-in-review-part-2-improved-observability-and-enhanced-features-for-sagemaker-ai-model-customization-and-hosting/)
of this series, where we will dive into observability and model customization improvements. Share your experiences and questions in the comments—we’d love to hear how these capabilities are transforming your AI workloads.

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