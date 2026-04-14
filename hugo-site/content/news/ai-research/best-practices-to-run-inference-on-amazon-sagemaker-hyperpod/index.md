---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-14T18:15:47.366276+00:00'
exported_at: '2026-04-14T18:15:50.070047+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/best-practices-to-run-inference-on-amazon-sagemaker-hyperpod
structured_data:
  about: []
  author: ''
  description: This post explores how Amazon SageMaker HyperPod provides a comprehensive
    solution for inference workloads. We walk you through the platform’s key capabilities
    for dynamic scaling, simplified deployment, and intelligent resource management.
    By the end of this post, you’ll understand how to use the HyperPod automated...
  headline: Best practices to run inference on Amazon SageMaker HyperPod
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/best-practices-to-run-inference-on-amazon-sagemaker-hyperpod
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Best practices to run inference on Amazon SageMaker HyperPod
updated_at: '2026-04-14T18:15:47.366276+00:00'
url_hash: a51abd4fb8a0e9019cf7d23349d154b78a40e164
---

Deploying and scaling foundation models for generative AI inference presents challenges for organizations. Teams often struggle with complex infrastructure setup, unpredictable traffic patterns that lead to over-provisioning or performance bottlenecks, and the operational overhead of managing GPU resources efficiently. These pain points result in delayed time-to-market, suboptimal model performance, and inflated costs that can make AI initiatives unsustainable at scale.

This post explores how Amazon SageMaker HyperPod addresses these challenges by providing a comprehensive solution for inference workloads. We walk you through the platform’s key capabilities for dynamic scaling, simplified deployment, and intelligent resource management. By the end of this post, you’ll understand how to use the HyperPod automated infrastructure, cost optimization features, and performance enhancements to reduce your total cost of ownership by up to 40% while accelerating your generative AI deployments from concept to production.

## **Cluster creation – one click deployment**

To create a HyperPod cluster with Amazon Elastic Kubernetes Service (Amazon EKS) orchestration, navigate to the SageMaker HyperPod Clusters page in the
[Amazon SageMaker AI console](https://console.aws.amazon.com/sagemaker/)
.

**Step 1:**

Choose
**Create HyperPod cluster**
. Then, choose the
**Orchestrated by Amazon EKS**
option.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/09/ML-20174-image-1-3.png)

**Step 2**

Choose either the quick setup or custom setup option. The quick setup option creates default resources, while the custom setup option allows you to integrate with existing resources or customize the configuration to meet your specific needs.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-2-1.png)

**Step 3**

The following are Kubernetes controllers and add-ons. These controllers and add-ons can be enabled or disabled.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-3-1.png)

**Step 4**

The following diagram shows the high-level architecture of SageMaker HyperPod with the Amazon EKS orchestrator control plane.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-4-1.png)

## **Deployment options**

Amazon SageMaker HyperPod now offers a comprehensive inference platform, combining Kubernetes flexibility with AWS managed services. You can deploy, scale, and optimize machine learning models with production reliability throughout their lifecycle. The platform provides flexible deployment interfaces, advanced autoscaling, and comprehensive monitoring features. With the Inference deployment operator, you can deploy models from S3 buckets, FSx for Lustre, and JumpStart without writing code.

### **Auto Scaling with Karpenter**

Amazon SageMaker HyperPod provides an Auto Scaling architecture that combines
**KEDA**
(Kubernetes Event-Driven Autoscaling) for pod-level scaling and
**Karpenter**
for node-level scaling. This dual-layer approach enables dynamic, cost-efficient infrastructure that scales from zero to production workloads based on real-time demand.

*![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-5-1.png)*

*Elaborate Auto Scaling with KEDA and Karpenter*

### **Understanding the Auto Scaling architecture**

Pod Scaling (KEDA): KEDA (Kubernetes Event-Driven Autoscaling) is an open-source Cloud Native Computing Foundation (CNCF) project that extends Kubernetes with event-driven autoscaling capabilities. KEDA is automatically installed as part of the HyperPod Inference Operator, providing out-of-the-box pod autoscaling without requiring separate installation or configuration. KEDA scales the number of inference pods based on metrics like request queue length, Amazon CloudWatch metrics (such as SageMaker endpoint invocations), latency, or custom Prometheus metrics. It can scale deployments down to zero pods when there is no traffic, eliminating costs during idle periods.

Node Scaling (Karpenter): Karpenter is a Kubernetes cluster autoscaler that provisions or removes compute nodes based on pending pod requirements. Karpenter runs in the Amazon EKS control plane, which means there are no additional compute costs for running the autoscaler itself. This control plane deployment enables true scale-to-zero capabilities. When KEDA scales pods down to zero because of no traffic, Karpenter can remove all worker nodes, ensuring you incur no infrastructure costs during idle periods.

### **How KEDA and Karpenter work together**

The integration between KEDA and Karpenter creates an efficient Auto Scaling experience. The ADOT (AWS Distro for OpenTelemetry) Collector scrapes metrics from inference pods and pushes them to Amazon Managed Service for Prometheus or CloudWatch, which the KEDA Operator (installed with the Inference Operator) periodically polls and evaluates against configured trigger thresholds defined in your
`JumpStartModel`
or
`InferenceEndpointConfig`
YAML. When metrics exceed thresholds, KEDA triggers the Horizontal Pod Autoscaler (HPA) to create new inference pods, and if these pods remain pending because of insufficient node capacity, Karpenter (running in the control plane) detects this and provisions new nodes with the appropriate instance types and GPU configurations. The Kubernetes scheduler then deploys pending pods to the newly provisioned nodes, distributing inference traffic across the scaled infrastructure. When demand decreases, KEDA scales down pods based on the same metrics. Karpenter consolidates workloads and removes underutilized nodes to reduce infrastructure costs. During periods of no traffic, KEDA can scale to zero pods, and Karpenter removes all worker nodes. This results in zero compute costs while maintaining the ability to rapidly scale back up when traffic resumes. This architecture ensures that you only pay for compute resources when they’re actively serving inference requests, with no additional costs for the autoscaling infrastructure itself since Karpenter runs in the managed control plane.

**Verify that the cluster execution role has the following policies**

`"sagemaker:BatchAddClusterNodes"`
,
`"sagemaker:BatchDeleteClusterNodes"`
,
`"sagemaker:BatchPutMetrics"`
on the following resources
`"arn:aws:sagemaker:us-east-1:actxxxxxxxx:cluster/*"`
,
`"arn:aws:sagemaker:us-east-1:actxxxxxxx:cluster/sagemaker-ml-cluster-e3cb1e31-eks"`

**To enable Karpenter – Run the following command**

```
aws sagemaker update-cluster
--cluster-name 'ml-cluster'
--auto-scaling '{ "Mode": "Enable", "AutoScalerType": "Karpenter" }'
--cluster-role 'arn:aws:iam::XXXXXXXXXXXX:role/sagemaker-ml-cluster-e3cb1e31ExecRole'
--region us-east-1
```

The following is the success output.

`{

"ClusterArn": "arn:aws:sagemaker:us-east-1:XXXXXXXXXXXX:cluster/4dehnrxxettz"

}`

After you run this command and update the cluster, you can verify that Karpenter has been enabled by running the
[DescribeCluster API.](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/describe_cluster.html)

```
aws sagemaker describe-cluster
--cluster-name ml-cluster
--query AutoScaling
--region us-east-1
{
	"Mode": "Enable",
	"AutoScalerType": "Karpenter",
	"Status": "InService",
	"FailureMessage": ""
}
```

## **KV caching and intelligent routing**

Amazon SageMaker HyperPod now supports
**managed tiered KV cache and intelligent routing**
to optimize large language model (LLM) inference performance, particularly for long-context prompts and multi-turn conversations.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-6-1.png)

Inference request using L1 and L2 KV caching

**Managed tiered KV cache**

The managed tiered KV cache feature addresses memory constraints during inference by implementing a multi-tier caching strategy. Key-value (KV) caching is essential for LLM inference efficiency. It stores intermediate attention computations from previous tokens, avoiding redundant recalculations and significantly reducing latency.

By managing cache across multiple storage tiers, HyperPod enables:

* **Reduced memory pressure**
  on GPU resources
* **Support for longer context windows**
  without performance degradation
* **Automatic cache management**
  without manual intervention

## **Intelligent routing**

Intelligent routing optimizes inference by directing requests with shared prompt prefixes to the same inference instance, maximizing KV cache reuse. This approach:

* **Routes requests strategically**
  to instances that have already processed similar prefixes
* **Accelerates processing**
  by reusing cached KV data
* **Reduces latency**
  for multi-turn conversations and batch requests with common contexts

## **Performance benefits**

Together, these capabilities deliver substantial improvements:

* **Up to 40% reduction in latency**
  for inference requests
* **25% improvement in throughput**
  for processing requests
* **25% cost savings**
  compared to baseline configurations without these optimizations

These features are available through the
**HyperPod Inference Operator**
, providing out-of-the-box managed capabilities for production LLM deployments. For more details about this feature, see
[Managed Tiered KV Cache and Intelligent Routing for Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/)
.

## **Multi-instance GPU support (MIG) profile**

SageMaker HyperPod Inference now supports model deployments on accelerators that have been partitioned using NVIDIA MIG (Multi Instance GPU) technology. Deploying small models on large GPUs can waste GPU resources. To address this, SageMaker HyperPod allows you to use a fraction of GPUs that work in isolation with each other. If the GPU has already been partitioned, you can directly deploy the JumpStart Model or
`InferenceEndpointConfig`
using the SageMaker HyperPod Inference solution. For
`JumpStartModels`
, you can use
`spec.server.acceleratorPartitionType`
to set the MIG profile of your choice. The following example shows the configuration:

```
apiVersion: inference.sagemaker.aws.amazon.com/v1
kind: JumpStartModel
metadata:
  name: deepseek
spec:
  sageMakerEndpoint:
    name: deepseek
  model:
    modelHubName: SageMakerPublicHub
    modelId: deepseek-llm-r1-distill-qwen-1-5b
  server:
    acceleratorPartitionType: mig-7g.40gb
    instanceType: ml.p4d.24xlarge
```

The
`JumpStartModel`
also conducts an internal validation before model deployment. You can switch that validation off using
`spec.server.validations.acceleratorPartitionValidation`
field in YAML and setting it to false. For
`InferenceEndpointConfig`
, you can deploy the model on the MIG profile of your choice using fields spec.worker.resources.requests and spec.worker.resources.limits to the MIG profile of your choice. The following example shows the configuration:

apiVersion: inference.sagemaker.aws.amazon.com/v1kind: InferenceEndpointConfig….spec: worker: resources: requests: cpu: 5600m memory: 10Gi nvidia.com/mig-4g.71gb: 1 limits: nvidia.com/mig-4g.71gb: 1

With these configurations, you can use other technologies supported by SageMaker HyperPod Inference along with MIG deployment of the model. For any additional information, see
[HyperPod now supports Multi-Instance GPU to maximize GPU utilization for generative AI tasks](https://aws.amazon.com/blogs/machine-learning/hyperpod-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-generative-ai-tasks/)
.

## **Observability**

You can monitor HyperPod Inference metrics through SageMaker HyperPod observability features.

To enable SageMaker HyperPod observability features, follow the instructions in
[Accelerate foundation model development with one-click observability in Amazon SageMaker HyperPod](https://aws.amazon.com/blogs/machine-learning/accelerate-foundation-model-development-with-one-click-observability-in-amazon-sagemaker-hyperpod/)
.

HyperPod observability provides built-in dashboards in Grafana. For example, the Inference dashboard provides visibility into inference-related metrics like Incoming Requests, Latency, and Time to First Byte (TTFB).

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-7-1.png)

Grafana dashboard

## **Running notebook**

HyperPod clusters with Amazon EKS orchestration now support creating and managing interactive development environments such as JupyterLab and open-source Visual Studio Code, streamlining the ML development lifecycle by providing managed environments for familiar tools to data scientists. This feature introduces a new add-on called Amazon SageMaker Spaces for AI developers to create and manage self-contained environments for running notebooks. You can now maximize your GPU investments by running both interactive workloads and their training jobs on the same infrastructure, with support for fractional GPU allocations to improve cost efficiency.
**Deploy IDE and notebooks add-on from the HyperPod console**

Amazon SageMaker AI is introducing a new capability for SageMaker HyperPod EKS clusters, which allows AI developers to run their interactive machine learning workloads directly on the
[HyperPod EKS cluster](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-ide.html)
. This feature introduces a new add-on called Amazon SageMaker Spaces, that enables AI developers to create and manage self-contained environments for running notebooks.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-8-1.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/07/ML-20174-image-9-1.png)

High-level architecture of running Jupyter Notebook on HyperPod cluster

## **Conclusion**

In this post, we explored how Amazon SageMaker HyperPod provides a scalable and cost-efficient infrastructure for running inference workloads. By following the best practices outlined in this post, you can use HyperPod’s capabilities to
[deploy foundation models](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-ts.html)
by using one-click JumpStart, S3, and FSx for Lustre integration, managed Karpenter autoscaling, and unified infrastructure that dynamically scales from zero to production. With features such as
[KV caching](https://aws.amazon.com/blogs/machine-learning/managed-tiered-kv-cache-and-intelligent-routing-for-amazon-sagemaker-hyperpod/)
, intelligent routing, and
[Multi-Instance GPU](https://aws.amazon.com/blogs/machine-learning/hyperpod-now-supports-multi-instance-gpu-to-maximize-gpu-utilization-for-generative-ai-tasks/)
support, you can optimize your inference workloads, reducing latency, increasing throughput, and lowering costs by using
[Spot Instances.](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-sagemaker-hyperpod-spot-instances/)
By adopting these best practices, you can accelerate your machine learning workflows, improve model performance, and achieve significant total cost of ownership reductions, so that you can scale generative AI responsibly and efficiently in production environments.

---

## About the authors

### Vinay Arora

[Vinay](http://www.linkedin.com/in/vinay-arora-ji)
is a Specialist Solution Architect for Generative AI at AWS, where he collaborates with customers in designing cutting-edge AI solutions leveraging AWS technologies. Prior to AWS, Vinay has over two decades of experience in finance—including roles at banks and hedge funds—he has built risk models, trading systems, and market data platforms. Vinay holds a master’s degree in computer science and business management.

### Piyush Daftary

[Piyush](https://www.linkedin.com/in/raftaar/)
is a Senior Software Engineer at AWS, working on Amazon SageMaker with a focus on building performant, scalable inference systems for large language models. His technical interests span AI/ML, databases, and search technologies, where he specializes in developing production-ready solutions that enable efficient model deployment and inference at scale. His work involves optimizing system performance, implementing intelligent routing mechanisms, and designing architectures that support both research and production workloads, with a passion for solving complex distributed systems challenges and making advanced AI capabilities more accessible to developers and organizations. Outside of work, he enjoys traveling, hiking, and spending time with family.

### Shantanu Tripathi

[Shantanu Tripathi](https://www.linkedin.com/in/shantanu-tripathi-28327aa2/)
is a Software Development Engineer at AWS with over 5 years of experience building large-scale AI/ML infrastructure. As a core engineer on Amazon SageMaker HyperPod Inference, he has worked on designing and optimizing scalable inference solutions for high-performance AI workloads. His broader experience spans distributed AI training libraries, Deep Learning Containers (DLCs), Deep Learning AMIs, and generative AI solutions. Outside of work, he enjoys theater and swimming.

### Ziwen Ning

[Ziwen Ning](https://www.linkedin.com/in/ningziwen/)
is a Senior Software Development Engineer at AWS, working on Amazon SageMaker HyperPod with a focus on building scalable ML infrastructure. Previously at Annapurna Labs, he enhanced the AI/ML experience through the integration of AWS Neuron with containerized environments and Kubernetes. His expertise spans container technologies, Kubernetes orchestration, ML infrastructure, and open source project leadership. Ziwen is passionate about designing production-grade systems that make advanced AI more accessible. In his free time, he enjoys bouldering, badminton, and immersing himself in music.

### Kunal Jha

[Kunal](https://www.linkedin.com/in/kunal-j/)
is a Principal Product Manager at AWS. He is focused on building Amazon SageMaker Hyperpod as the best-in-class choice for Generative AI model’s training and inference. In his spare time, Kunal enjoys skiing and exploring the Pacific Northwest.