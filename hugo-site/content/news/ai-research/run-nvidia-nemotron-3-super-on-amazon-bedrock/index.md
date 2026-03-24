---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-24T04:44:51.329151+00:00'
exported_at: '2026-03-24T04:44:55.202820+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/run-nvidia-nemotron-3-super-on-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: This post explores the technical characteristics of the Nemotron 3
    Super model and discusses potential application use cases. It also provides technical
    guidance to get started using this model for your generative AI applications within
    the Amazon Bedrock environment.
  headline: Run NVIDIA Nemotron 3 Super on Amazon Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/run-nvidia-nemotron-3-super-on-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Run NVIDIA Nemotron 3 Super on Amazon Bedrock
updated_at: '2026-03-24T04:44:51.329151+00:00'
url_hash: 24af48c4315c6adeaea2903387a62dad685bd626
---

Nemotron 3 Super is now available as a fully managed and serverless model on
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
,
[joining the Nemotron Nano models that are already available within the Amazon Bedrock environment](https://aws.amazon.com/blogs/machine-learning/run-nvidia-nemotron-3-nano-as-a-fully-managed-serverless-model-on-amazon-bedrock/)
.

With
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
open models on Amazon Bedrock, you can accelerate innovation and deliver tangible business value without managing infrastructure complexities. You can power your
[generative AI](https://aws.amazon.com/ai/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
applications with Nemotron through the fully managed inference of Amazon Bedrock, using its extensive features and tooling.

This post explores the technical characteristics of the Nemotron 3 Super model and discusses potential application use cases. It also provides technical guidance to get started using this model for your generative AI applications within the Amazon Bedrock environment.

## About Nemotron 3 Super

Nemotron 3 Super is a hybrid Mixture of Experts (MoE) model with leading compute efficiency and accuracy for multi-agent applications and for specialized agentic AI systems. The model is released with open weights, datasets, and recipes so developers can customize, improve, and deploy the model on their infrastructure for enhanced privacy and security.

**Model overview:**

* Architecture:
  + MoE with Hybrid Transformer-Mamba architecture.
  + Supports token budget for providing improved accuracy with minimum reasoning token generation.
* Accuracy:
  + Highest throughput efficiency in its size category and up to 5x over the previous Nemotron Super model.
  + Leading accuracy for reasoning and agentic tasks among leading open models and up to 2x higher accuracy over the previous version.
  + Achieves high accuracy across leading benchmarks, including AIME 2025, Terminal-Bench, SWE Bench verified and multilingual, RULER.
  + Multi-environment RL training gave the model leading accuracy across 10+ environments with
    [NVIDIA NeMo](https://www.nvidia.com/en-us/ai-data-science/products/nemo/)
    .
* Model size: 120 B with 12 B active parameters
* Context length: up to 256K tokens
* Model input: Text
* Model output: Text
* Languages: English, French, German, Italian, Japanese, Spanish, and Chinese

### Latent MoE

Nemotron 3 Super uses latent MoE, where experts operate on a shared latent representation before outputs are projected back to token space. This approach allows the model to call on 4x more experts at the same inference cost, enabling better specialization around subtle semantic structures, domain abstractions, or multi-hop reasoning patterns.

### Multi-token prediction (MTP)

MTP enables the model to predict several future tokens in a single forward pass, significantly increasing throughput for long reasoning sequences and structured outputs. For planning, trajectory generation, extended
[chain-of-thought](https://www.nvidia.com/en-us/glossary/cot-prompting/)
, or code generation, MTP reduces latency and improves agent responsiveness.

To learn more about Nemotron 3 Super’s architecture and how it is trained, see
[Introducing Nemotron 3 Super: an Open Hybrid Mamba Transformer MoE for Agentic Reasoning](https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/)
.

## NVIDIA Nemotron 3 Super use cases

Nemotron 3 Super helps power various use cases for different industries. Some of the use cases include

* Software development: Assist with tasks like code summarization.
* Finance: Accelerate loan processing by extracting data, analyzing income patterns, and detecting fraudulent operations, which can help reduce cycle times and risk.
* Cybersecurity: Can be used to triage issues, perform in-depth malware analysis, and proactively hunt for security threats.
* Search: Can help understand user intent to activate the right agents.
* Retail: Can help optimize inventory management and enhance in-store service with real-time, personalized product recommendations and support.
* Multi-agent Workflows: Orchestrates task‑specific agents—planning, tool use, verification, and domain execution—to automate complex, end‑to‑end business processes.

Get Started with NVIDIA Nemotron 3 Super in Amazon Bedrock. Complete the following steps to test NVIDIA Nemotron 3 Super in Amazon Bedrock

1. Navigate to the
   [**Amazon Bedrock console**](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#modelaccess&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
   and select
   **Chat/Text playground**
   from the left menu (under the
   *Test*
   section).
2. Choose
   **Select model**
   in the upper-left corner of the playground.
3. Choose
   **NVIDIA**
   from the category list, then select
   **NVIDIA Nemotron 3 Super**
   .
4. Choose
   **Apply**
   to load the model.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/12/ML-20591-image-1.png)

After completing the previous steps, you can test the model immediately. To truly showcase
**Nemotron 3 Super’s**
capability, we will move beyond simple syntax and task it with a complex engineering challenge. High-reasoning models excel at “system-level” thinking where they must balance architectural trade-offs, concurrency, and distributed state management.

Let’s use the following prompt to design a globally distributed service:

`"Design a distributed rate-limiting service in Python that must support 100,000 requests per second across multiple geographic regions.`

`1. Provide a high-level architectural strategy (e.g., Token Bucket vs. Fixed Window) and justify your choice for a global scale.

2. Write a thread-safe implementation using Redis as the backing store.

3. Address the 'race condition' problem when multiple instances update the same counter.

4. Include a pytest suite that simulates network latency between the app and Redis."`

This prompt requires the model to operate as a senior distributed-systems engineer — reasoning about trade-offs, producing thread-safe code, anticipating failure modes, and validating everything with realistic tests, all in a single coherent response.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20591/ML-20591-image-2.gif)

### Using the AWS CLI and SDKs

You can access the model programmatically using the model ID
*nvidia.nemotron-super-3-120b*
. The model supports both the
**InvokeModel**
and
**Converse**
APIs through the
[AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
and
[AWS SDK](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
with
`nvidia.nemotron-super-3-120b`
as the model ID. Further, it supports the Amazon Bedrock OpenAI SDK compatible API.

Run the following command to invoke the model directly from your terminal using the
[**AWS Command Line Interface (AWS CLI) and the InvokeModel API**](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
:

```
aws bedrock-runtime invoke-model \
 --model-id nvidia.nemotron-super-3-120b \
 --region us-west-2 \
 --body '{"messages": [{"role": "user", "content": "Type_Your_Prompt_Here"}], "max_tokens": 512, "temperature": 0.5, "top_p": 0.9}' \
 --cli-binary-format raw-in-base64-out \
invoke-model-output.txt
```

If you want to invoke the model through the AWS SDK for Python (Boto3)
**,**
use the following script to send a prompt to the model, in this case by using the Converse API:

```
import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-west-2")

# Set the model ID
model_id = "nvidia.nemotron-super-3-120b"

# Start a conversation with the user message.

user_message = "Type_Your_Prompt_Here"
conversation = [
   {
       "role": "user",

       "content": [{"text": user_message}],
   }
]

try:
   # Send the message to the model using a basic inference configuration.
   response = client.converse(
        modelId=model_id,

       messages=conversation,
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
   )

   # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
   print(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)
```

To invoke the model through the Amazon Bedrock OpenAI-compatible ChatCompletions endpoint you can proceed as follows using the OpenAI SDK:

```
# Import OpenAI SDK
from openai import OpenAI

# Set environment variables
os.environ["OPENAI_API_KEY"] = "<insert your bedrock API key>"
os.environ["OPENAI_BASE_URL"] = "https://bedrock-runtime.<AWS region>.amazon.com/openai/v1"

# Set the model ID
model_id = "nvidia.nemotron-super-3-120b"

# Set prompts
system_prompt = “Type_Your_System_Prompt_Here”
user_message = "Type_Your_User_Prompt_Here"


# Use ChatCompletionsAPI
response = client.chat.completions.create(
    model= model _ID,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message}
    ],
    temperature=0,
    max_completion_tokens=1000
)

# Extract and print the response text
print(response.choices[0].message.content)
```

## Conclusion

In this post, we showed you how to get started with NVIDIA Nemotron 3 Super on Amazon Bedrock for building the next generation of agentic AI applications. By combining the model’s advanced Hybrid Transformer-Mamba architecture and Latent MoE with the fully managed, serverless infrastructure of Amazon Bedrock, organizations can now deploy high-reasoning, efficient applications at scale without the heavy lifting of backend management. Ready to see what this model can do for your specific workflow?

* **Try it now:**
  Head over to the
  [Amazon Bedrock Console](https://console.aws.amazon.com/bedrock/)
  to experiment with NVIDIA Nemotron 3 Super in the model playground.
* **Build:**
  Explore the
  [AWS SDK](https://aws.amazon.com/developer/tools/)
  to integrate Nemotron 3 Super into your existing generative AI pipelines.

---

## About the authors

### Aris Tsakpinis

Aris Tsakpinis is a Senior Specialist Solutions Architect for Generative AI focusing on open weight models on Amazon Bedrock and the broader generative AI open-source environment. Alongside his professional role, he is pursuing a PhD in Machine Learning Engineering at the University of Regensburg, where his research focuses on applied generative AI in scientific domains.

### Abdullahi Olaoye

Abdullahi Olaoye is a Senior AI Solutions Architect at NVIDIA, specializing in integrating NVIDIA AI libraries, frameworks, and products with cloud AI services and open-source tools to optimize AI model deployment, inference, and generative AI workflows. He collaborates with cloud providers to help enhance AI workload performance and drive adoption of NVIDIA-powered AI and generative AI solutions