---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-14T20:06:51.637823+00:00'
exported_at: '2026-02-14T20:06:55.073579+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-nano-30b-is-now-available-in-amazon-sagemaker-jumpstart
structured_data:
  about: []
  author: ''
  description: Today we’re excited to announce that the NVIDIA Nemotron 3 Nano 30B
    model with  3B active parameters is now generally available in the Amazon SageMaker
    JumpStart model catalog. You can accelerate innovation and deliver tangible business
    value with Nemotron 3 Nano on Amazon Web Services (AWS) without having to manage
    model deployment complexities. You can power your generative AI applications with
    Nemotron capabilities using the managed deployment capabilities offered by SageMaker
    JumpStart.
  headline: NVIDIA Nemotron 3 Nano 30B MoE model is now available in Amazon SageMaker
    JumpStart
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-nano-30b-is-now-available-in-amazon-sagemaker-jumpstart
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: NVIDIA Nemotron 3 Nano 30B MoE model is now available in Amazon SageMaker JumpStart
updated_at: '2026-02-14T20:06:51.637823+00:00'
url_hash: 7d130c782568c913fdbafd4a23c627a4c3394e6e
---

Today we’re excited to announce that the
[NVIDIA Nemotron](https://developer.nvidia.com/nemotron?ncid=pa-srch-goog-405472&_bt=785763502016&_bk=nemotron%203&_bm=p&_bn=g&_bg=194843200048&gad_source=1&gad_campaignid=23296574832&gbraid=0AAAAAD4XAoHOYYk38jGO1R1Lp8ArOSXHB&gclid=CjwKCAiA1obMBhAbEiwAsUBbIqFnMwdcAItGRj2tN3vB-iX-xcFYaH9L1ZHBwggsesWeZ300MTW8XhoCNW4QAvD_BwE)
3 Nano 30B model with  3B active parameters is now generally available in the
[Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/ai/jumpstart/)
model catalog. You can accelerate innovation and deliver tangible business value with Nemotron 3 Nano on Amazon Web Services (AWS) without having to manage model deployment complexities. You can power your generative AI applications with Nemotron capabilities using the managed deployment capabilities offered by SageMaker JumpStart.

Nemotron 3 Nano is a small language hybrid mixture of experts (MoE) model with the highest compute efficiency and accuracy for developers to drive highly-skilled agentic tasks at scale. The model is fully open with open-weights, datasets, and recipes, so developers can seamlessly customize, optimize, and deploy the model on their infrastructure to help meet their privacy and security requirements. Nemotron 3 Nano excels in coding and reasoning, and leads on benchmarks such as SWE Bench Verified, GPQA Diamond, AIME 2025, Arena Hard v2, and IFBench.

## About Nemotron 3 Nano 30B

Nemotron 3 Nano is differentiated from other models by its architecture and accuracy, boasting strong performance in a variety of highly technical skills:

* Architecture:
  + ο      MoE with hybrid Transformer-Mamba architectureο      Supports token budget for providing optimal accuracy with minimum reasoning token generation
* Accuracy:
  + Leading accuracy on coding, scientific reasoning, math, and instruction following
  + Leads on benchmarks such as LiveCodeBench, GPQA Diamond, AIME 2025, BFCL , and IFBench (compared to other open language models under 30B)
* Usability:
  + 30B parameter model with 3 billion active parameters
  + Has a context window of up to 1 million tokens
  + Text-based foundation model, using text for both inputs and outputs

## Prerequisites

To get started with Nemotron 3 Nano in Amazon SageMaker JumpStart, you must have a provisioned
[Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/ai/studio/)
domain.

## Get started with NVIDIA Nemotron 3 Nano 30B in SageMaker JumpStart

To test the Nemotron 3 Nano model in SageMaker JumpStart, open SageMaker Studio and choose
**Models**
in the navigation pane.  Search for NVIDIA in the search bar and choose
**NVIDIA Nemotron 3 Nano 30B**
as the model.

[![SageMaker AI JumpStart Search Results](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/11/Screenshot-2026-02-11-at-9.09.51%E2%80%AFAM-1024x935.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/11/Screenshot-2026-02-11-at-9.09.51%E2%80%AFAM.png)

On the model details page, choose
**Deploy**
and follow the prompts to deploy the model.

After the model is deployed to a SageMaker AI endpoint, you can test it. You can access the model using the following
[AWS Command Line Interface](http://aws.amazon.com/cli)
(AWS CLI) code examples. You can use
`nvidia/nemotron-3-nano`
as the model ID.

```
cat > input.json << EOF
{
"model": "${MODEL_ID}",
"messages": [
{
 	"role": "system",
 	"content": "You are a helpful assistant."
 },
 {
 	"role": "user",
       	"content": "What is NVIDIA? Answer in 2-3 sentences."
}],
"max_tokens": 512,
"temperature": 0.2,
"stream": False, # Set to False for non-streaming mode,
   	"chat_template_kwargs": {"enable_thinking": False} # Set to False for non-reasoning mode
}
EOF

aws sagemaker-runtime invoke-endpoint \
--endpoint-name ${ENDPOINT_NAME} \
--region ${AWS_REGION} \
--content-type 'application/json' \
--body fileb://input.json \
> response.json
```

Alternatively, you can access the model using SageMaker SDK and Boto3 code. The following Python code examples show how to send a text message to the NVIDIA Nemotron 3 Nano 30B using the SageMaker SDK. For additional code examples, refer to the
[NVIDIA GitHub repo](https://github.com/NVIDIA/nim-deploy/blob/main/cloud-service-providers/aws/sagemaker/aws_marketplace_notebooks/nim_nvidia-nemotron-3-nano-30b-a3b_aws_marketplace.ipynb)
.

```
runtime_client = boto3.client('sagemaker-runtime', region_name=region)
payload = {
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000
    }

    try:
        response = self.runtime_client.invoke_endpoint(
            EndpointName=self.endpoint_name,
            ContentType='application/json',
            Body=json.dumps(payload)
        )

        response_body = response['Body'].read().decode('utf-8')
        raw_response = json.loads(response_body)

        # Parse the response using our custom parser
        return self.parse_response(raw_response)

    except Exception as e:
        raise Exception(
            f"Failed to invoke endpoint '{self.endpoint_name}': {str(e)}. "
            f"Check that the endpoint is InService and you have least-privileged IAM permissions assigned."
        )
```

## Now available

NVIDIA Nemotron 3 Nano is now available fully managed in SageMaker JumpStart. Refer to the model package for AWS Region availability. To learn more, check out the
[Nemotron Nano model page](https://github.com/NVIDIA/nim-deploy/blob/main/cloud-service-providers/aws/sagemaker/aws_marketplace_notebooks/nim_nvidia-nemotron-3-nano-30b-a3b_aws_marketplace.ipynb)
, the
[NVIDIA GitHub sample notebook for Nemotron 3 Nano 30B](https://github.com/NVIDIA/nim-deploy/blob/main/cloud-service-providers/aws/sagemaker/aws_marketplace_notebooks/nim_nvidia-nemotron-3-nano-30b-a3b_aws_marketplace.ipynb)
, and the
[Amazon SageMaker JumpStart pricing page](https://aws.amazon.com/sagemaker/ai/pricing/?nc=sn&loc=3)
.

Try the Nemotron 3 Nano model in Amazon SageMaker JumpStart today and send feedback to
[AWS re:Post for SageMaker JumpStart](https://repost.aws/tags/questions/TA5ivaiWRURmujY4KA5T5gYw)
or through your usual AWS Support contacts.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/frgud.jpg)
**Dan Ferguson**
is a Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/pkaradgi.jpeg)
Pooja Karadgi**
leads product and strategic partnerships for Amazon SageMaker JumpStart, the machine learning and generative AI hub within SageMaker. She is dedicated to accelerating customer AI adoption by simplifying foundation model discovery and deployment, enabling customers to build production-ready generative AI applications across the entire model lifecycle – from onboarding and customization to deployment.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/bencrab-1.jpg)
Benjamin Crabtree**
is a Senior Software Engineer on the Amazon SageMaker AI team, specializing in delivering the “last mile” experience to customers. He is passionate about democratizing the latest artificial intelligence breakthroughs by offering easy to use capabilities. Also, Ben is highly experienced in building machine learning infrastructure at scale.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/tim-ma.png)
Timothy Ma**
is a Principal Specialist in generative AI at AWS, where he collaborates with customers to design and deploy cutting-edge machine learning solutions. He also leads go-to-market strategies for generative AI services, helping organizations harness the potential of advanced AI technologies.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/17/ML-20105-image-11.jpeg)
Abdullahi Olaoye**
is a Senior AI Solutions Architect at NVIDIA, specializing in integrating NVIDIA AI libraries, frameworks, and products with cloud AI services and open-source tools to optimize AI model deployment, inference, and generative AI workflows. He collaborates with AWS to enhance AI workload performance and drive adoption of NVIDIA-powered AI and generative AI solutions.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/cropped-Nirmal_headshot-262x262-1.jpeg)
Nirmal Kumar Juluru**
is a product marketing manager at NVIDIA driving the adoption of AI software, models, and APIs in the NVIDIA NGC Catalog and NVIDIA AI Foundation models and endpoints. He previously worked as a software developer. Nirmal holds an MBA from Carnegie Mellon University and a bachelors in computer science from BITS Pilani.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/IMG_8015.jpg)
**Vivian Chen**
is a Deep Learning Solutions Architect at NVIDIA, where she helps teams bridge the gap between complex AI research and real-world performance. Specializing in inference optimization and cloud-integrated AI solutions, Vivian focuses on turning the heavy lifting of machine learning into fast, scalable applications. She is passionate about helping clients navigate NVIDIA’s accelerated computing stack to ensure their models don’t just work in the lab, but thrive in production.