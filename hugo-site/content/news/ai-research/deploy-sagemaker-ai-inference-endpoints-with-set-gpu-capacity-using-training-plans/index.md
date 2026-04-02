---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:03:53.983213+00:00'
exported_at: '2026-04-02T04:03:57.343376+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-sagemaker-ai-inference-endpoints-with-set-gpu-capacity-using-training-plans
structured_data:
  about: []
  author: ''
  description: In this post, we walk through how to search for available p-family
    GPU capacity, create a training plan reservation for inference, and deploy a SageMaker
    AI inference endpoint on that reserved capacity. We follow a data scientist's
    journey as they reserve capacity for model evaluation and manage the endpoint
    through...
  headline: Deploy SageMaker AI inference endpoints with set GPU capacity using training
    plans
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/deploy-sagemaker-ai-inference-endpoints-with-set-gpu-capacity-using-training-plans
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Deploy SageMaker AI inference endpoints with set GPU capacity using training
  plans
updated_at: '2026-04-02T04:03:53.983213+00:00'
url_hash: 12ee5e4ef6b5af5bde0ab8c67c91b2ba4c5b1624
---

Deploying large language models (LLMs) for inference requires reliable GPU capacity, especially during critical evaluation periods, limited-duration production testing, or burst workloads. Capacity constraints can delay deployments and impact application performance. Customers can use
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
training plans to reserve compute capacity for specified time periods. Originally designed for training workloads, training plans now support inference endpoints, providing predictable GPU availability for time-bound inference workloads.

Consider a common scenario: you’re on a data science team that must evaluate several fine-tuned language models over a two-week period before selecting one for production. They require uninterrupted access to
[ml.p5.48xlarge](https://aws.amazon.com/ec2/instance-types/p4/)
instances to run comparative benchmarks, but on-demand capacity in their AWS Region is unpredictable during peak hours. By reserving capacity through training plans, they can run evaluations uninterrupted with controlled costs and predictable availability.

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
training plans offer a flexible way to secure capacity so you can search for available offerings, select the instance type, quantity, and duration that match your needs. Customers can select a fixed number of days or months into the future, or a specified number of days at a stretch, to create a reservation. After created, the training plan provides a set capacity that can be referenced when deploying SageMaker AI inference endpoints.

In this post, we walk through how to search for available p-family GPU capacity, create a training plan reservation for inference, and deploy a SageMaker AI inference endpoint on that reserved capacity. We follow a data scientist’s journey as they reserve capacity for model evaluation and manage the endpoint throughout the reservation lifecycle.

## Solution overview

[SageMaker AI training plans](https://aws.amazon.com/sagemaker/ai/train/)
provide a mechanism to reserve compute capacity for specific time windows. When creating a training plan, customers specify their target resource type. By setting the value of the target resource to “endpoint”, you can secure p-family GPU instances specifically for inference workloads. The reserved capacity is referenced through an Amazon Resource Name (ARN) in the endpoint configuration so that the endpoint deploys the reserved instances.

The training plan creation and utilization workflow consists of four key phases:

* **Identify your capacity requirements**
  – Determine the instance type, instance count, and duration needed for your inference workload.
* **Search for available training plan offerings**
  – Query available capacity that matches your requirements and desired time window.
* **Create a training plan reservation**
  – Select a suitable offering and create the reservation, which generates an ARN.
* **Deploy and manage your endpoint**
  – Configure your SageMaker AI endpoint to use the reserved capacity and manage its lifecycle during the reservation period.

Let’s walk through each phase with detailed examples.

## Prerequisites

Before starting, ensure that you have the following:

### Step 1: Search for available capacity offerings and create a reservation plan

Our data scientist begins by identifying available p-family GPU capacity that matches their evaluation requirements. They need one ml.p5.48xlarge instance for a week-long evaluation starting in late January. Using the search-training-plan-offerings API, they specify the instance type, instance count, duration, and time window. Setting target resources to “endpoint” configures the capacity to be provisioned specifically for inference rather than training jobs.

```
# List training plan offerings with instance type, instance count,
# duration in hours, start time after, and end time before.
aws sagemaker search-training-plan-offerings \
--target-resources "endpoint" \
--instance-type "ml.p5.48xlarge" \
--instance-count 1 \
--duration-hours 168 \
--start-time-after "2025-01-27T15:48:14-04:00" \
--end-time-before "2025-01-31T14:48:14-05:00"
```

**Example output**

```
{
"TrainingPlanOfferings": [
{
"TrainingPlanOfferingId": "tpo-SHA-256-hash-value",
"TargetResources": ["endpoint"],
"RequestedStartTimeAfter": "2025-01-21T12:48:14.704000-08:00",
"DurationHours": 168,
"DurationMinutes": 10080,
"UpfrontFee": "xxxx.xx",
"CurrencyCode": "USD",
"ReservedCapacityOfferings": [
{
"InstanceType": "ml.p5.48xlarge",
"InstanceCount": 1,
"AvailabilityZone": "us-west-2a",
"DurationHours": 168,
"DurationMinutes": 10080,
"StartTime": "2025-01-27T15:48:14-04:00",
"EndTime": "2025-01-31T14:48:14-05:00"
}
]
}
]
}
```

The response provides detailed information about each available capacity block, including the instance type, quantity, duration, Availability Zone, and pricing. Each offering includes specific start and end times, so you can select a reservation that aligns with your deployment schedule. In this case, the team finds a 168-hour (7-day) reservation in us-west-2a that fits their timeline.

After identifying a suitable offering, the team creates the training plan reservation to secure the capacity:

```
aws sagemaker create-training-plan \
--training-plan-offering-id "tpo-SHA-256-hash-value" \
--training-plan-name "p4-for-inference-endpoint"
```

**Example output:**

```
{
"TrainingPlanArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint"
}
```

The
`TrainingPlanArn`
uniquely identifies the reserved capacity. You save this ARN, it’s the key that will link their endpoint to the set p-family GPU capacity. With the reservation confirmed and paid for, they’re now ready to configure their inference endpoint.

### Using the SageMaker AI console

You can also create training plans through the SageMaker AI console. This provides a visual interface for searching capacity and completing the reservation. The console workflow follows three steps: search for offerings, add plan details, and review and purchase.

**Navigating to Training Plans:**

* In the SageMaker AI console, navigate to
  **Model training & customization**
  in the left navigation pane.
* Select
  **Training plans.**
* Choose
  **Create training plan**
  (orange button in the upper right).

The following screenshot shows the Training Plans landing page where you initiate the creation workflow.

[![Figure 1: Training Plans landing page with Create training plan button](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-1.png)

*Figure 1: Training Plans landing page with Create training plan button*

**Step A – Search for training plan offerings:**

1. Under
   **Target**
   , select
   **Inference Endpoint.**
2. Under
   **Compute type**
   , select
   **Instance.**
3. Select your
   **Instance type**
   (for example,
   `ml.p5.48xlarge`
   ) and
   **Instance count.**
4. Under
   **Date and duration**
   , specify the start date and duration.
5. Choose
   **Find training plan.**

The following screenshot shows the search interface with Inference Endpoint selected and the criteria filled in:

[![Figure 2: Step A - Search training plan offerings with Inference Endpoint target](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-2.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-2.png)

*Figure 2: Step A – Search training plan offerings with Inference Endpoint target*

After selecting
**Find training plan**
, the
**Available plans**
section displays matching offerings:

[![Figure 3: Available training plan offerings with pricing and availability details](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-3.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/19/ML-20083-image-3.png)

*Figure 3: Available training plan offerings with pricing and availability details*

**Complete the reservation:**

1. Choose a plan by selecting the radio button next to your preferred offering.
2. Choose
   **Next**
   to proceed to
   **Step B: Add plan details.**
3. Review the details and choose
   **Next**
   to proceed to
   **Step 3: Review and purchase.**
4. Review the final summary, accept the terms, and choose
   **Purchase**
   to complete the reservation.

After the reservation is created, you receive a training plan ARN. With the reservation confirmed and paid for, you’re now ready to configure their inference endpoint using this ARN. The endpoint will only function during the reservation window specified in the training plan.

### Step 2: Create the endpoint configuration with training plan reservation

With the reservation secured, the team creates an endpoint configuration that binds their inference endpoint to the reserved capacity. The critical step here is including the
`CapacityReservationConfig`
object in the
`ProductionVariants`
section where they set the
`MlReservationArn`
to the training plan ARN received earlier:

```
--endpoint-config-name "ftp-ep-config" \
--production-variants '[{
"VariantName": "AllTraffic",
"ModelName": "my-model",
"InitialInstanceCount": 1,
"InstanceType": "ml.p5.48xlarge",
"InitialVariantWeight": 1.0,
"CapacityReservationConfig": {
"CapacityReservationPreference": "capacity-reservations-only",
"MlReservationArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint"
}
}]‘
```

When SageMaker AI receives this request, it validates that the ARN points to an active training plan reservation with a target resource type of “endpoint”. If validation succeeds, the endpoint configuration is created and becomes eligible for deployment. The
`CapacityReservationPreference`
setting is particularly important. By setting it to
`capacity-reservations-only`
, the team restricts the endpoint to their reserved capacity, so it stops serving traffic when the reservation ends, preventing unexpected charges.

### Step 3: Deploy the endpoint on reserved capacity

With the endpoint configuration ready, the team deploys their evaluation endpoint:

```
aws sagemaker create-endpoint \
--endpoint-name "my-endpoint" \
--endpoint-config-name "ftp-ep-config"
```

The endpoint now runs entirely within the reserved training plan capacity. SageMaker AI provisions the
`ml.p5.48xlarge`
instance in us-west-2a and loads the model, this process can take several minutes. After the endpoint reaches InService status, the team can begin their evaluation workload.

### Step 4: Invoke an endpoint when the training plan is active

With the endpoint in service, you can begin running their evaluation workload. They invoke the endpoint for real-time inference, sending test prompts and measuring response quality, latency, and throughput:

```
aws sagemaker-runtime invoke-endpoint \
--endpoint-name "my-endpoint" \
--body fileb://input.json \
--content-type "application/json" \
Output.json
```

During the active reservation window, the endpoint operates normally with a set capacity. All invocations are processed using the reserved resources, helping to facilitate predictable performance and availability. The team can run their benchmarks without worrying about capacity constraints or performance variability from shared infrastructure.

### Step 5: Invoke endpoint when training plan is expired

It’s worth understanding what happens if the training plan reservation expires while the endpoint is still deployed.

When the reservation expires, endpoint behavior depends on the
`CapacityReservationPreference`
setting. Because the team set it to
`capacity-reservations-only`
, the endpoint stops serving traffic and invocations fail with a capacity error:

```
aws sagemaker-runtime invoke-endpoint \
--endpoint-name "my-endpoint" \
--body fileb://input.json \
--content-type "application/json" \
output.json
```

**Expected error response:**

```
Expected error response:
{
"Error": {
"Code": "ModelError",
"Message": "Endpoint capacity reservation has expired. Please update endpoint configuration."
}
}
```

To resume service, you must either create a new training plan reservation and update the endpoint configuration or update the endpoint to use on-demand or ODCR capacity. In the team’s case, because they completed their evaluation, they delete the endpoint rather than extending the reservation.

### Step 6: Update endpoint

During the evaluation period, you might need to update the endpoint for various reasons. SageMaker AI supports several update scenarios while maintaining the connection to reserved capacity.

#### Update to a new model version

Midway through the evaluation, the team wants to test a new model version that incorporates additional fine-tuning. They can update to the new model version while keeping the same reserved capacity:

```
# First, create a new endpoint configuration with updated model
aws sagemaker create-endpoint-config \
--endpoint-config-name "ftp-ep-config-v2" \
--production-variants '[{
"VariantName": "AllTraffic",
"ModelName": "my-model-v2",
"InitialInstanceCount": 1,
"InstanceType": "ml.p5.48xlarge", "InitialVariantWeight": 1.0, "CapacityReservationConfig": { "CapacityReservationPreference": "capacity-reservations-only", "MlReservationArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint" } }]‘ # Then update the endpoint aws sagemaker update-endpoint \ --endpoint-name "my-endpoint" \ --endpoint-config-name "ftp-ep-config-v2"
```

#### Migrate from training plan to on-demand capacity

If the team’s evaluation runs longer than expected or if they want to transition the endpoint to production use beyond the reservation period, they can migrate to on-demand capacity:

```
# Create endpoint configuration without training plan reservation
aws sagemaker create-endpoint-config \
--endpoint-config-name "ondemand-ep-config" \
--production-variants '[{
"VariantName": "AllTraffic",
"ModelName": "my-model",
"InitialInstanceCount": 1,
"InstanceType": "ml.p5.48xlarge", "InitialVariantWeight": 1.0 }]‘ # Update endpoint to use on-demand capacity aws sagemaker update-endpoint \ --endpoint-name "my-endpoint" \ --endpoint-config-name "ondemand-ep-config"
```

### Step 7: Scale endpoint

In some scenarios, teams can reserve more capacity than they initially deploy, giving them flexibility to scale up if needed. For example, if the team reserved two instances but initially deployed only one, they cam scale up during the evaluation period to test higher throughput scenarios.

#### Scale within reservation limits

Suppose the team initially reserved two
`ml.p5.48xlarge`
instances but deployed their endpoint with only one instance. Later, they want to test how the model performs under higher concurrent load:

```
# Create new config with increased instance count (within reservation)
aws sagemaker create-endpoint-config \
--endpoint-config-name "ftp-ep-config-scaled" \
--production-variants '[{
"VariantName": "AllTraffic",
"ModelName": "my-model",
"InitialInstanceCount": 2,
"InstanceType": "ml.p5.48xlarge", "InitialVariantWeight": 1.0, "CapacityReservationConfig": { "CapacityReservationPreference": "capacity-reservations-only", "MlReservationArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint" } }]‘ aws sagemaker update-endpoint \ --endpoint-name "my-endpoint" \ --endpoint-config-name "ftp-ep-config-scaled"
```

#### Attempt to scale beyond reservation

If customers attempt to scale beyond the reserved capacity, the update will fail:

```
# This will fail if reservation only has 2 instances
aws sagemaker create-endpoint-config \
--endpoint-config-name "ftp-ep-config-over-limit" \
--production-variants '[{
"VariantName": "AllTraffic",
"ModelName": "my-model",
"InitialInstanceCount": 3,
"InstanceType": "ml.p5.48xlarge", "InitialVariantWeight": 1.0, "CapacityReservationConfig": { "CapacityReservationPreference": "capacity-reservations-only", "MlReservationArn": "arn:aws:sagemaker:us-east-1:123456789123:training-plan/p4-for-inference-endpoint" } }]‘
```

Expected error:

```
{
"Error": {
"Code": "ValidationException",
"Message": "Requested instance count (3) exceeds reserved capacity (2) for training plan."
}
}
```

### Step 8: Delete endpoint

After completing their week-long evaluation, the team has gathered all the performance metrics that they need and selected their top-performing model. They’re ready to clean up the inference endpoint. The training plan reservation automatically expires at the end of the reservation window. You are charged for the full reservation period regardless of when you delete the endpoint.

**Important considerations:**

It’s important to note that deleting an endpoint doesn’t refund or cancel the training plan reservation. The reserved capacity remains allocated until the training plan reservation window expires, regardless of whether the endpoint is still running. However, if the reservation is still active and capacity is available, you can create a new endpoint using the same training plan reservation ARN. To fully clean up, delete the endpoint configuration:

```
aws sagemaker delete-endpoint-config \
--endpoint-config-name "ftp-ep-config"
```

When setting up your training plan reservation, keep in mind that you’re committing to a fixed window of time and will be charged for the full duration upfront, regardless of how long you actually use it. Before purchasing, make sure that your estimated timeline aligns with the reservation length that you choose. If you think your evaluation might be completed early, the cost will not change.

For example, if you purchase a 7-day reservation, you will pay for all seven days even if you complete your work in five. The upside is that this predictable, upfront cost structure helps you to budget accurately for your project. You will know exactly what you’re spending before you start.

**Note:**
When you delete your endpoint, the training plan reservation isn’t canceled or refunded. The reserved capacity stays allocated until the reservation window expires. If you finish early and want to use the remaining time, you can redeploy a new endpoint using the same training plan reservation ARN, if the reservation is still active and capacity is available.

## Conclusion

SageMaker AI training plans provide a straightforward way to reserve p-family GPU capacity and deploy SageMaker AI inference endpoints with set availability. This approach is recommended for time-bound workloads such as model evaluation, limited-duration production testing, and burst scenarios where predictable capacity is essential.

As we saw in our data science team’s journey, the process involves identifying capacity requirements, searching for available offerings, creating a reservation, and referencing that reservation in the endpoint configuration to deploy the endpoint during the reservation window. The team completed their week-long model evaluation with a set capacity, avoiding the unpredictability of on-demand availability during peak hours. They could focus on their evaluation of metrics rather than worrying about infrastructure constraints.

With support for endpoint updates, scaling within reservation limits, and seamless migration to on-demand capacity, training plans give you the flexibility to manage inference workloads while maintaining control over GPU availability and costs. Whether you’re running competitive model benchmarks, performing limited-duration A/B tests, or handling predictable traffic spikes, training plans for inference endpoints provide the capacity that you need with transparent, upfront pricing.

#### Acknowledgement

Special thanks to Alwin (Qiyun) Zhao, Piyush Kandpal, Jeff Poegel, Qiushi Wuye, Jatin Kulkarni, Shambhavi Sudarsan, and Karan Jain for their contribution.

---

## About the authors

### Kareem Syed-Mohammed

Kareem Syed-Mohammed is a Product Manager at AWS. He is focuses on enabling Gen AI model development and governance on SageMaker HyperPod. Prior to this, at Amazon QuickSight, he led embedded analytics, and developer experience. In addition to QuickSight, he has been with AWS Marketplace and Amazon retail as a Product Manager. Kareem started his career as a developer for call center technologies, Local Expert and Ads for Expedia, and management consultant at McKinsey.

### Chaoneng Quan

Chaoneng Quan is a Software Development Engineer on the AWS SageMaker team, building AI infrastructure and GPU capacity management systems for large-scale training and inference workloads. He designs scalable distributed systems that enable customers to forecast demand, reserve compute capacity, and operate workloads with predictability and efficiency. His work spans resource planning, infrastructure reliability, and large-scale compute optimization.

### Dan Ferguson

Dan Ferguson is a Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

### Yati Agarwal

Yati Agarwal is a Senior Product Manager at Amazon Web Services (AI Platform). She owns the end-to-end capacity strategy for AI workloads, ensuring that the infrastructure powering the most demanding machine learning use cases is available, scalable, and reliable. Her scope spans the full AI development lifecycle — from foundation model training and fine-tuning at large scale, to inference serving real-time and batch customer workloads, to interactive ML development environments where data scientists and engineers iterate and experiment.