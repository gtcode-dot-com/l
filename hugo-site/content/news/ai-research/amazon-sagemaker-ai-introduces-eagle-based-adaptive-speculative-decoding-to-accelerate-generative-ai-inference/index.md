---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:30:17.685057+00:00'
exported_at: '2025-11-26T00:30:19.930238+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference
structured_data:
  about: []
  author: ''
  description: Amazon SageMaker AI now supports EAGLE-based adaptive speculative decoding,
    a technique that accelerates large language model inference by up to 2.5x while
    maintaining output quality. In this post, we explain how to use EAGLE 2 and EAGLE
    3 speculative decoding in Amazon SageMaker AI, covering the solution architecture,
    optimization workflows using your own datasets or SageMaker's built-in data, and
    benchmark results demonstrating significant improvements in throughput and latency.
  headline: Amazon SageMaker AI introduces EAGLE based adaptive speculative decoding
    to accelerate generative AI inference
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-ai-introduces-eagle-based-adaptive-speculative-decoding-to-accelerate-generative-ai-inference
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Amazon SageMaker AI introduces EAGLE based adaptive speculative decoding to
  accelerate generative AI inference
updated_at: '2025-11-26T00:30:17.685057+00:00'
url_hash: 48ded5fe2d0965f38004c1f80ad98b9adefc0570
---

Generative AI models continue to expand in scale and capability, increasing the demand for faster and more efficient inference. Applications need low latency and consistent performance without compromising output quality.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
introduces new enhancements to its inference optimization toolkit that bring EAGLE based adaptive speculative decoding to more model architectures. These updates make it easier to accelerate decoding, optimize performance using your own data and deploy higher-throughput models using the familiar SageMaker AI workflow.

EAGLE, short for Extrapolation Algorithm for Greater Language-model Efficiency, is a technique that speeds up large language model decoding by predicting future tokens directly from the hidden layers of the model. When you guide optimization using your own application data, the improvements align with the actual patterns and domains you serve, producing faster inference that reflects your real workloads rather than generic benchmarks. Based on the model architecture, SageMaker AI trains EAGLE 3 or EAGLE 2 heads.

Note that this training and optimization is not limited to just a one time optimization operation. You can start by utilizing the datasets provided by SageMaker for the initial training, but as you continue to gather and collect your own data you can also fine-tune using your own curated dataset for highly adaptive, workload-specific performance. An example would be utilizing a tool such as
[Data Capture](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-capture.html)
to curate your own dataset over time from real-time requests that are hitting your hosted model. This can be an iterative feature with multiple cycles of training to continuously improve performance.

In this post we’ll explain how to use EAGLE 2 and EAGLE 3 speculative decoding in Amazon SageMaker AI.

## Solution overview

SageMaker AI now offers native support for both EAGLE 2 and EAGLE 3 speculative decoding, enabling each model architecture to apply the technique that best matches its internal design. For your base LLM, you can utilize either SageMaker JumpStart models or bring your own model artifacts to S3 from other model hubs, such as HuggingFace.

Speculative decoding is a widely employed technique for accelerating inference in LLMs without compromising quality. This method involves using a smaller draft model to generate preliminary tokens, which are then verified by the target LLM. The extent of the speedup achieved through speculative decoding is heavily dependent on the selection of the draft model.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/Screenshot-2025-11-19-at-11.19.40-PM.png)

The sequential nature of modern LLMs makes them expensive and slow, and speculative decoding has proven to be an effective solution to this problem. Methods like EAGLE improve upon this by reusing features from the target model, leading to better results. However, a current trend in the LLM community is to increase training data to boost model intelligence without adding inference costs. Unfortunately, this approach has limited benefits for EAGLE. This limitation is due to EAGLE’s constraints on feature prediction. To address this, EAGLE-3 is introduced, which predicts tokens directly instead of features and combines features from multiple layers using a technique called training-time testing. These changes significantly improve performance and allow the model to fully benefit from increased training data.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/Screenshot-2025-11-19-at-10.12.40-PM.png)

To give customers maximum flexibility, SageMaker supports every major workflow for building or refining an EAGLE model. You can train an EAGLE model entirely from scratch using the SageMaker curated open dataset, or train it from scratch with your own data to align speculative behavior with your traffic patterns. You can also start from an existing EAGLE base model: either retraining it with the default open dataset for a fast, high-quality baseline, or fine-tuning that base model with your own dataset for highly adaptive, workload-specific performance. In addition, SageMaker JumpStart provides fully pre-trained EAGLE models so you can begin optimizing immediately without preparing any artifacts.

The solution spans six supported architectures and includes a pre-trained, pre-cached EAGLE base to accelerate experimentation. SageMaker AI also supports widely used training data formats, specifically ShareGPT and OpenAI chat and completions, so existing corpora can be used directly. Customers can also provide the data captured using their own SageMaker AI endpoints provided the data is in the above specified formats. Whether you rely on the SageMaker open dataset or bring your own, optimization jobs typically deliver around a 2.5x thoughput over standard decoding while adapting naturally to the nuances of your specific use case.

All optimization jobs automatically produce benchmark results giving you clear visibility into latency and throughput improvements. You can run the entire workflow using SageMaker Studio or the AWS CLI and you deploy the optimized model through the same interface you already use for standard SageMaker AI inference.

SageMaker AI currently supports
`LlamaForCausalLM`
,
`Qwen3ForCausalLM`
,
`Qwen3MoeForCausalLM`
,
`Qwen2ForCausalLM`
and
`GptOssForCausalLM`
with EAGLE 3, and
`Qwen3NextForCausalLM`
with EAGLE 2. You can use one optimization pipeline across a mix of architectures while still gaining the benefits of model-specific behavior.

## How EAGLE works inside the model

Speculative decoding can be thought of like a seasoned chief scientist guiding the flow of discovery. In traditional setups, a smaller “assistant” model runs ahead, quickly sketching out several possible token continuations, while the larger model examines and corrects those suggestions. This pairing reduces the number of slow, sequential steps by verifying multiple drafts at once.

EAGLE streamlines this process even further. Instead of depending on an external assistant, the model effectively becomes its own lab partner: it inspects its internal hidden-layer representations to anticipate several future tokens in parallel. Because these predictions arise from the model’s own learned structure, they tend to be more accurate upfront, leading to deeper speculative steps, fewer rejections, and smoother throughput.

By removing the overhead of coordinating a secondary model and enabling highly parallel verification, this approach alleviates memory bandwidth bottlenecks and delivers notable speedups, often around 2.5x, while maintaining the same output quality the baseline model would produce.

## Running optimization jobs from the SDK or CLI

You can interface with the Optimization Toolkit using the AWS Python Boto3 SDK, Studio UI. In this section we explore utilizing the AWS CLI, the same API calls will map over to the Boto3 SDK. Here, the core API calls for endpoint creation remain the same:
[create\_model](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_model.html)
,
[create\_endpoint\_config](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html)
, and
[create\_endpoint](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpoint.html)
. The workflow we showcase here begins with model registration using the
`create_model`
API call. With the
`create_model`
API call you can specify your serving container and stack. You don’t need to create a SageMaker model object and can specify the model data in the Optimization Job API call as well.

For the EAGLE heads optimization, we specify the model data by pointing towards to the
**Model Data Source**
parameter, at the moment specification of the HuggingFace Hub Model ID is not supported. Pull your artifacts and upload them to an S3 bucket and specify it in the Model Data Source parameter. By default checks are done to verify that the appropriate files are uploaded so you have the standard model data expected for LLMs:

```
# traditional model data needed
model/
  config.json
  tokenizer.json
  tokenizer_config.json
  special_tokens_map.json
  generation_config.json
  vocab.json
  model.safetensors
  model.safetensors.index.json
```

Let’s look at a few paths here:

* Using your own model data with your own EAGLE curated dataset
* Bringing your own trained EAGLE that you may want to train more
* Bring your own model data and use SageMaker AI built-in datasets

### 1. Using your own model data with your own EAGLE curated dataset

We can start an optimization job with the
`create-optimization-job API call`
. Here is an example with a Qwen3 32B model. Note that you can bring your own data or also use the built-in SageMaker provided datasets. First we can create a SageMaker Model object that specifies the S3 bucket with our model artifacts:

```
aws sagemaker --region us-west-2 create-model \
--model-name <target-model-name> \
--primary-container '{ "Image": "763104351884.dkr.ecr.{region}.amazonaws.com/djl-inference:{CONTAINER_VERSION}",
"ModelDataSource": { "S3DataSource": { "S3Uri": "Enter model path",
"S3DataType": "S3Prefix", "CompressionType": "None" } } }' \ --execution-role-arn "Enter Execution Role ARN"
```

Our optimization call then pulls down these model artifacts when you specify the SageMaker Model and a
`TrainingDataSource`
parameter as the following:

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

### 2. Bringing your own trained EAGLE that you may want to train more

For your own trained EAGLE you can specify another parameter in the
`create_model`
API call where you point towards your EAGLE artifacts, optionally you can also specify a SageMaker JumpStart Model ID to pull down the packaged model artifacts.

```
# Enable additional model data source with EAGLE artifacts
aws sagemaker --region us-west-2 create-model \
--model-name <target-model-name> \
--primary-container '{ "Image": "763104351884.dkr.ecr.{region}.amazonaws.com/djl-inference:{CONTAINER_VERSION}",
"ModelDataSource": { "S3DataSource": { "S3Uri": "<model path>",
"S3DataType": "S3Prefix", "CompressionType": "None" } },
"AdditionalModelDataSources": [ { "ChannelName": "eagle_model",
"S3DataSource": { "S3Uri": "<pre-trained EAGLE path>",
"S3DataType": "S3Prefix", "CompressionType": "None" } } ] }' \ --execution-role-arn "Enter Execution Role ARN"
```

Similarly the optimization API then inherits this model object with the necessary model data:

```
aws sagemaker --region us-west-2 create-optimization-job \
 --account-id <account-id> \
 --optimization-job-name <job-name> \
 --deployment-instance-type ml.p5.48xlarge \
 --max-instance-count 10 \
 --model-source '{
 "SageMakerModel": {
    "ModelName": "Created Model Name"
    }
 }' \
 --optimization-configs '{
    "ModelSpeculativeDecodingConfig": {
    "Technique": "EAGLE",
    "TrainingDataSource": {
    "S3Uri": "Enter training data path",
    "S3DataType": "S3Prefix"
    }
   }
 }' \
 --output-config '{
    "SageMakerModel": {
    "ModelName": "Model Name"
   },
   "S3OutputLocation": "Enter output data location"
 }' \
 --stopping-condition '{"MaxRuntimeInSeconds": 432000}' \
 --role-arn "Enter Execution Role ARN"
```

### 3. Bring your own model data and use SageMaker built-in datasets

Optionally, we can utilize the SageMaker provided datasets:

```
# SageMaker Provided Optimization Datasets
gsm8k_training.jsonl (https://huggingface.co/datasets/openai/gsm8k)
magicoder.jsonl (https://huggingface.co/datasets/ise-uiuc/Magicoder-OSS-Instruct-75K)
opencodeinstruct.jsonl (https://huggingface.co/datasets/nvidia/OpenCodeInstruct)
swebench_oracle_train.jsonl (https://huggingface.co/datasets/nvidia/OpenCodeInstruct)
ultrachat_0_8k_515292.jsonl (https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k)
```

After completion, SageMaker AI stores evaluation metrics in S3 and records the optimization lineage in Studio. You can deploy the optimized model to an inference endpoint with either the
[create\_endpoint API call](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sagemaker/client/create_endpoint.html)
or in the UI.

## Benchmarks

To benchmark this further we compared three states:

* **No EAGLE**
  : Base model without EAGLE as a baseline
* **Base EAGLE**
  : EAGLE training using built-in datasets provided by SageMaker AI
* **Trained EAGLE**
  : EAGLE training using built-in datasets provided by SageMaker AI and retraining with own custom dataset

The numbers displayed below are for
`qwen3-32B`
across metrics such as Time to First Token (TTFT) and overall throughput.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Configuration** | **Concurrency** | **TTFT (ms)** | **TPOT (ms)** | **ITL (ms)** | **Request Throughput** | **Output Throughput (tokens/sec)** | **OTPS per request (tokens/sec)** |
| No EAGLE | 4 | 168.04 | 45.95 | 45.95 | 0.04 | 86.76 | 21.76 |
| No EAGLE | 8 | 219.53 | 51.02 | 51.01 | 0.08 | 156.46 | 19.6 |
| Base EAGLE | 1 | 89.76 | 21.71 | 53.01 | 0.02 | 45.87 | 46.07 |
| Base EAGLE | 2 | 132.15 | 20.78 | 50.75 | 0.05 | 95.73 | 48.13 |
| Base EAGLE | 4 | 133.06 | 20.11 | 49.06 | 0.1 | 196.67 | 49.73 |
| Base EAGLE | 8 | 154.44 | 20.58 | 50.15 | 0.19 | 381.86 | 48.59 |
| Trained EAGLE | 1 | 83.6 | 17.32 | 46.37 | 0.03 | 57.63 | 57.73 |
| Trained EAGLE | 2 | 129.07 | 18 | 48.38 | 0.05 | 110.86 | 55.55 |
| Trained EAGLE | 4 | 133.11 | 18.46 | 49.43 | 0.1 | 214.27 | 54.16 |
| Trained EAGLE | 8 | 151.19 | 19.15 | 51.5 | 0.2 | 412.25 | 52.22 |

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/Screenshot-2025-11-21-at-4.25.41-PM.png)

## Pricing considerations

Optimization jobs run on SageMaker AI training instances, you will be billed depending on the instance type and job duration. Deployment of the resulting optimized model uses standard SageMaker AI Inference pricing.

## Conclusion

EAGLE based adaptive speculative decoding gives you a faster and more effective path to improve generative AI inference performance on Amazon SageMaker AI. By working inside the model rather than relying on a separate draft network, EAGLE accelerates decoding, increases throughput and maintains generation quality. When you optimize using your own dataset, the improvements reflect the unique behavior of your applications, resulting in better end-to-end performance. With built-in dataset support, benchmark automation and streamlined deployment, the inference optimization toolkit helps you deliver low-latency generative applications at scale.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/07/10/image-7-4-100x147.jpeg)
**[Kareem Syed-Mohammed](https://www.linkedin.com/in/kareemuddin/)**
is a Product Manager at AWS. He is focuses on enabling generative AI model development and governance on SageMaker HyperPod. Prior to this, at Amazon QuickSight, he led embedded analytics, and developer experience. In addition to QuickSight, he has been with AWS Marketplace and Amazon retail as a Product Manager. Kareem started his career as a developer for call center technologies, Local Expert and Ads for Expedia, and management consultant at McKinsey.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/01/29/xddeng-100.png)
Xu Deng**
is a Software Engineer Manager with the SageMaker team. He focuses on helping customers build and optimize their AI/ML inference experience on Amazon SageMaker. In his spare time, he loves traveling and snowboarding.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/11/29/ml-17917-image010.jpg)
**Ram Vegiraju**
is an ML Architect with the Amazon SageMaker Service team. He focuses on helping customers build and optimize their AI/ML solutions on SageMaker. In his spare time, he loves traveling and writing.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/26/NYH_9619.jpg)
**Vinay Arora**
is a Specialist Solution Architect for Generative AI at AWS, where he collaborates with customers in designing cutting-edge AI solutions leveraging AWS technologies. Prior to AWS, Vinay has over two decades of experience in finance—including roles at banks and hedge funds—he has built risk models, trading systems, and market data platforms. Vinay holds a master’s degree in computer science and business management.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/image-12-2-100x124.png)
Siddharth Shah**
is a Principal Engineer at AWS SageMaker, specializing in large-scale model hosting and optimization for Large Language Models. He previously worked on the launch of Amazon Textract, performance improvements in the model-hosting platform, and expedited retrieval systems for Amazon S3 Glacier. Outside of work, he enjoys hiking, video games, and hobby robotics.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/image12-1-100x100.png)
[**Andy Peng**](https://pengandy.com/)
is a builder with curiosity, motivated by scientific research and product innovation. He helped build key initiatives that span AWS SageMaker and Bedrock, Amazon S3, AWS App Runner, AWS Fargate, Alexa Health & Wellness, and AWS Payments, from 0-1 incubation to 10x scaling. Open-source enthusiast.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/4ec9e090191711efbdf8bba50c446bd7-CROPPED_DOWNLOADABLE-100x150.jpeg)
Johna Liu**
is a Software Development Engineer on the Amazon SageMaker team, where she builds and explores AI/LLM-powered tools that enhance efficiency and enable new capabilities. Outside of work, she enjoys tennis, basketball and baseball.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/25/Kolla_A_2.23.18-081_Original-100x100.jpg)
Anisha Kolla**
is a Software Development Engineer with SageMaker Inference team with over 10+ years of industry experience. She is passionate about building scalable and efficient solutions that empower customers to deploy and manage machine learning applications seamlessly. Anisha thrives on tackling complex technical challenges and contributing to innovative AI capabilities. Outside of work, she enjoys exploring new Seattle restaurants, traveling, and spending time with family and friends.