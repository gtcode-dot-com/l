---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-10T16:15:38.984314+00:00'
exported_at: '2026-03-10T16:15:42.104948+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/accelerate-custom-llm-deployment-fine-tune-with-oumi-and-deploy-to-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: In this post, we show how to fine-tune a Llama model using Oumi on
    Amazon EC2 (with the option to create synthetic data using Oumi), store artifacts
    in Amazon S3, and deploy to Amazon Bedrock using Custom Model Import for managed
    inference.
  headline: 'Accelerate custom LLM deployment: Fine-tune with Oumi and deploy to Amazon
    Bedrock'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/accelerate-custom-llm-deployment-fine-tune-with-oumi-and-deploy-to-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Accelerate custom LLM deployment: Fine-tune with Oumi and deploy to Amazon
  Bedrock'
updated_at: '2026-03-10T16:15:38.984314+00:00'
url_hash: 83b1f964904ec5fe9081fc458beff92b403332e2
---

*This post is cowritten by David Stewart and Matthew Persons from Oumi.*

Fine-tuning open source large language models (LLMs) often stalls between experimentation and production. Training configurations, artifact management, and scalable deployment each require different tools, creating friction when moving from rapid experimentation to secure, enterprise-grade environments.

In this post, we show how to fine-tune a Llama model using
[Oumi](https://github.com/oumi-ai/oumi)
on
[Amazon EC2](https://aws.amazon.com/ec2/)
(with the option to create synthetic data using Oumi), store artifacts in
[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html)
, and deploy to
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
using
[Custom Model Import](https://aws.amazon.com/bedrock/custom-model-import/)
for managed inference. While we use EC2 in this walkthrough, fine-tuning can be completed on other compute services such as
[Amazon SageMaker](https://aws.amazon.com/sagemaker/?trk=ceaf07a2-36ab-4fba-b62f-bcf6c48ca9f2&sc_channel=ps&trk=ceaf07a2-36ab-4fba-b62f-bcf6c48ca9f2&sc_channel=ps&ef_id=Cj0KCQiAyvHLBhDlARIsAHxl6xrRjew-OTwpFxEo7w2zM9Xq2KWXOTd-J2qD_wCsNv12EaPTJe2sj-gaAnkXEALw_wcB:G:s&s_kwcid=AL!4422!3!651751060692!e!!g!!amazon%20sagemaker!19852662230!145019225977&gad_campaignid=19852662230&gbraid=0AAAAADjHtp-brw44Uy55gcBqx3F5dc5Lm&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xrRjew-OTwpFxEo7w2zM9Xq2KWXOTd-J2qD_wCsNv12EaPTJe2sj-gaAnkXEALw_wcB)
or
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/pm/eks/?trk=f4781e8e-35e4-4e7e-affa-6fe7c4be82de&sc_channel=ps&trk=f4781e8e-35e4-4e7e-affa-6fe7c4be82de&sc_channel=ps&ef_id=Cj0KCQiAyvHLBhDlARIsAHxl6xqfCB_6gY1vKdNgCudkExM4Il5Wuj0wj1Kd5aspk9alTbOrG7IKKSMaAlztEALw_wcB:G:s&s_kwcid=AL!4422!3!651751059741!e!!g!!amazon%20eks!19852662191!145019194777&gad_campaignid=19852662191&gbraid=0AAAAADjHtp9wXoGtfBRu7JG851KEPGBtH&gclid=Cj0KCQiAyvHLBhDlARIsAHxl6xqfCB_6gY1vKdNgCudkExM4Il5Wuj0wj1Kd5aspk9alTbOrG7IKKSMaAlztEALw_wcB)
, depending on your needs.

## Benefits of Oumi and Amazon Bedrock

Oumi is an open source system that streamlines the foundation model lifecycle, from data preparation and training to evaluation. Instead of assembling separate tools for each stage, you define a single configuration and reuse it across runs.

Key benefits for this workflow:

* **Recipe-driven training:**
  Define your configuration once and reuse it across experiments, reducing boilerplate and improving reproducibility
* **Flexible fine-tuning:**
  Choose full fine-tuning or parameter-efficient methods like
  [LoRA](https://www.oumi.ai/docs/en/latest/get_started/core_concepts.html)
  , based on your constraints
* **Integrated evaluation:**
  Score checkpoints using benchmarks or LLM-as-a-judge without additional tooling
* **Data synthesis:**
  Generate task-specific datasets when production data is limited

Amazon Bedrock complements this by providing managed, serverless inference. After fine-tuning with Oumi, you import your model via
[Custom Model Import](https://aws.amazon.com/bedrock/custom-model-import/)
in three steps: upload to S3, create the import job, and invoke. No inference infrastructure to manage. The following architecture diagram shows how these components work together.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/03/image-1.png)

Figure 1: Oumi manages data, training, and evaluation on EC2. Amazon Bedrock provides managed inference via Custom Model Import.

## Solution overview

This workflow consists of three stages:

1. **Fine-tune with**
   **Oumi**
   **on EC2:**
   Launch a GPU-optimized instance (for example, g5.12xlarge or p4d.24xlarge),
   [install Oumi](https://www.oumi.ai/docs/en/latest/get_started/quickstart.html)
   , and run training with your configuration. For larger models, Oumi supports distributed training with Fully Sharded Data Parallel (FSDP), DeepSpeed, and Distributed Data Parallel (DDP) strategies across multi-GPU or multi-node setups.
2. **Store artifacts on S3:**
   Upload model weights, checkpoints, and logs for durable storage.
3. **Deploy to Amazon Bedrock:**
   Create a
   [Custom Model Import job](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-import-code-samples.html)
   pointing to your S3 artifacts. Amazon Bedrock provisions inference infrastructure automatically. Client applications call the imported model using the
   [Amazon Bedrock Runtime APIs](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_Operations_Amazon_Bedrock_Runtime.html)
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/03/image-2-1.png)

This architecture addresses common challenges in moving fine-tuned models to production:

## Technical implementation

Let’s walk through a hands-on workflow using the
[meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
model as an example. While we selected this model since it pairs well with fine-tuning on an AWS
`g6.12xlarge`
EC2 instance, the same workflow can be replicated across many other open source models (note that larger models may require larger instances or distributed training across instances). For more information, see the
[Oumi model fine-tuning recipes](https://www.oumi.ai/docs/en/latest/resources/recipes.html)
and
[Amazon Bedrock custom model architectures](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html#model-customization-import-model-architecture)
.

### Prerequisites

To complete this walkthrough, you need:

#### Set up AWS Resources

1. Clone this repository on your local machine:

```
git clone https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi.git
cd sample-oumi-fine-tuning-bedrock-cmi
```

2. Run the setup script to create IAM roles, an S3 bucket, and launch a GPU-optimized EC2 instance:

```
./scripts/setup-aws-env.sh [--dry-run]
```

The script prompts for your AWS Region, S3 bucket name, EC2 key pair name, and security group ID, then creates all required resources. Defaults: g6.12xlarge instance, Deep Learning Base AMI with Single CUDA (Amazon Linux 2023), and 100 GB gp3 storage.
*Note: If you do not have permissions to create IAM roles or launch EC2 instances, share this repository with your IT administrator and ask them to complete this section to set up your AWS environment.*

3. Once the instance is running, the script outputs the SSH command and the Amazon Bedrock import role ARN (needed in Step 5). SSH into the instance and continue with Step 1 below.

See the
[iam/README.md](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/iam/README.md)
for IAM policy details, scoping guidance, and validation steps.

### Step 1: Set up the EC2 environment

Complete the following steps to set up the EC2 environment.

1. On the EC2 instance (Amazon Linux 2023), update the system and install base dependencies:

```
sudo yum update -y
sudo yum install python3 python3-pip git -y
```

2. Clone the companion repository:

```
git clone https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi.git
cd sample-oumi-fine-tuning-bedrock-cmi
```

3. Configure environment variables (replace the values with your actual region and bucket name from the setup script):

```
export AWS_REGION=us-west-2
export S3_BUCKET=your-bucket-name
export S3_PREFIX=your-s3-prefix
aws configure set default.region "$AWS_REGION"
```

4. Run the setup script to create a Python virtual environment, install Oumi, validate GPU availability, and configure Hugging Face authentication. See
   [setup-environment.sh](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/scripts/setup-environment.sh)
   for options.

```
./scripts/setup-environment.sh
source .venv/bin/activate
```

5. Authenticate with Hugging Face to access gated model weights. Generate an access token at
   [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   , then run:

```
hf auth login
```

### Step 2: Configure training

The default dataset is
[tatsu-lab/alpaca](https://huggingface.co/datasets/tatsu-lab/alpaca)
, configured in
[configs/oumi-config.yaml](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/configs/oumi-config.yaml)
. Oumi downloads it automatically during training, no manual download is needed. To use a different dataset, update the
`dataset_name`
parameter in
[configs/oumi-config.yaml](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/configs/oumi-config.yaml)
. See the
[Oumi dataset docs](https://oumi.ai/docs/en/latest/resources/datasets/datasets.html)
for supported formats.

[Optional] Generate synthetic training data with Oumi:

To generate synthetic data using Amazon Bedrock as the inference backend, update the
`model_name`
placeholder in
[configs/synthesis-config.yaml](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/configs/synthesis-config.yaml)
with an Amazon Bedrock model ID you have access to (e.g.
`anthropic.claude-sonnet-4-6`
). See
[Oumi data synthesis docs](https://oumi.ai/docs/en/latest/user_guides/synth.html)
for details. Then run:

```
oumi synth -c configs/synthesis-config.yaml
```

### Step 3: Fine-tune the model

Fine-tune the model using Oumi’s built-in training
[recipe](https://github.com/oumi-ai/oumi/blob/main/configs/recipes/llama3_2/sft/1b_full/train.yaml)
for Llama-3.2-1B-Instruct:

```
./scripts/fine-tune.sh --config configs/oumi-config.yaml --output-dir models/final [--dry-run]
```

To customize hyperparameters, edit
[oumi-config.yaml](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/configs/oumi-config.yaml)
.

*Note: If you generated synthetic data in Step 2, update the dataset path in the config before training.*

Monitor GPU utilization with
[nvidia-smi](https://developer.nvidia.com/system-management-interface)
or
[Amazon CloudWatch Agent](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
. For long-running jobs, configure
[Amazon EC2 Automatic Instance Recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html)
to handle instance interruptions.

### Step 4: Evaluate model (Optional)

You can evaluate the fine-tuned model using standard benchmarks:

```
oumi evaluate -c configs/evaluation-config.yaml
```

The evaluation config specifies the model path and benchmark tasks (e.g., MMLU). To customize, edit
[evaluation-config.yaml](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/configs/evaluation-config.yaml)
. For LLM-as-a-judge approaches and additional benchmarks, see Oumi’s
[evaluation guide](https://oumi.ai/docs/en/latest/user_guides/evaluate/evaluate.html)
.

### Step 5: Deploy to Amazon Bedrock

Complete the following steps to deploy the model to Amazon Bedrock:

1. Upload model artifacts to S3 and import the model to Amazon Bedrock.

```
./scripts/upload-to-s3.sh --bucket $S3_BUCKET --source models/final --prefix $S3_PREFIX
./scripts/import-to-bedrock.sh --model-name my-fine-tuned-llama --s3-uri s3://$S3_BUCKET/$S3_PREFIX --role-arn $BEDROCK_ROLE_ARN --wait
```

2. The import script outputs the model ARN on completion. Set
   `MODEL_ARN`
   to this value (format:
   `arn:aws:bedrock:<REGION>:<ACCOUNT_ID>:imported-model/<MODEL_ID>`
   ).
3. Invoke the model on Amazon Bedrock

```
./scripts/invoke-model.sh --model-id $MODEL_ARN --prompt "Translate this text to French: What is the capital of France?"
```

4. Amazon Bedrock creates a managed inference environment automatically. For IAM role set up, see
   [bedrock-import-role.json](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/blob/main/iam/bedrock-import-role.json)
   .
5. Enable S3
   [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html)
   on the bucket to support rollback of model revisions. For SSE-KMS encryption and bucket policy hardening, see the
   [security scripts](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi/tree/main/security)
   in the companion repository.

### Step 6: Clean up

To avoid ongoing costs, remove the resources created during this walkthrough:

```
aws ec2 terminate-instances --instance-ids $INSTANCE_ID
aws s3 rm s3://$S3_BUCKET/$S3_PREFIX/ --recursive
aws bedrock delete-imported-model --model-identifier $MODEL_ARN
```

## Conclusion

In this post, you learned how to fine-tune a Llama-3.2-1B-Instruct base model using Oumi on EC2 and deploy it using Amazon Bedrock Custom Model Import. This approach gives you full control over fine-tuning with your own data while using managed inference in Amazon Bedrock.

The companion
[sample-oumi-fine-tuning-bedrock-cmi](https://github.com/aws-samples/sample-oumi-fine-tuning-bedrock-cmi)
repository provides scripts, configurations, and IAM policies to get started. Clone it, swap in your dataset, and deploy a custom model to Amazon Bedrock.

To get started, explore the resources below and begin building your own fine-tuning-to-deployment pipeline on Oumi and AWS. Happy Building!

**Learn More**

### Acknowledgement

Special thanks to Pronoy Chopra and Jon Turdiev for their contribution.

---

## About the authors

### Bashir Mohammed

[Bashir](https://www.linkedin.com/in/bashir-mohammed/)
is a Senior Lead GenAI Solutions Architect on the Frontier AI team at AWS, where he partners with startups and enterprises to architect and deploy production-scale GenAI applications. With a PhD in Computer Science, his expertise spans agentic systems, LLM evaluation and benchmarking, fine-tuning, post-training optimization, reinforcement learning from human feedback and scalable ML infrastructure. Outside of work, he mentors early-career engineers and supports community technical programs.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/03/image-5-100x100.png)

### Bala Krishnamoorthy

[Bala](https://www.linkedin.com/in/balakrishnamoorthy/)
is a Senior GenAI Data Scientist on the Amazon Bedrock GTM team, where he helps startups leverage Bedrock to power their products. In his free time, he enjoys spending time with family/friends, staying active, trying new restaurants, travel, and kickstarting his day with a steaming hot cup of coffee.

### Greg Fina

[Greg](https://www.linkedin.com/in/gregory-fina/)
is a Principal Startup Solutions Architect for Generative AI at Amazon Web Services, where he empowers startups to accelerate innovation through cloud adoption. He specializes in application modernization, with a strong focus on serverless architectures, containers, and scalable data storage solutions. He is passionate about using generative AI tools to orchestrate and optimize large-scale Kubernetes deployments, as well as advancing GitOps and DevOps practices for high-velocity teams. Outside of his customer-facing role, Greg actively contributes to open source projects, especially those related to Backstage.

### David Stewart

[David](https://www.linkedin.com/in/david-j-stewart/)
leads Field Engineering at Oumi, where he works with customers to improve their generative AI applications by creating custom language models for their use case. He brings extensive experience working with LLMs, including modern agentic, RAG, and training architectures. David is deeply interested in the practical side of generative AI and how people and organizations can create impactful products and solutions that work at scale.

### Matthew Persons

[Matthew](https://www.linkedin.com/in/matthewpersons/)
is a cofounder and engineering leader at Oumi, where he focuses on building and scaling practical, open generative AI systems for real-world use cases. He works closely with engineers, researchers, and customers to design robust architectures across the entire AI development pipeline. Matthew is passionate about open-source AI, applied machine learning, and enabling teams to move quickly from research proofs of concept to impactful products.