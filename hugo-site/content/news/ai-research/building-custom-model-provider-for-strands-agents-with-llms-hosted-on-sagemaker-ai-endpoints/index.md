---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-05T22:15:36.399790+00:00'
exported_at: '2026-03-05T22:15:38.730336+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/building-custom-model-provider-for-strands-agents-with-llms-hosted-on-sagemaker-ai-endpoints
structured_data:
  about: []
  author: ''
  description: This post demonstrates how to build custom model parsers for Strands
    agents when working with LLMs hosted on SageMaker that don't natively support
    the Bedrock Messages API format. We'll walk through deploying Llama 3.1 with SGLang
    on SageMaker using awslabs/ml-container-creator, then implementing a custom parser
    to...
  headline: Building custom model provider for Strands Agents with LLMs hosted on
    SageMaker AI endpoints
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/building-custom-model-provider-for-strands-agents-with-llms-hosted-on-sagemaker-ai-endpoints
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Building custom model provider for Strands Agents with LLMs hosted on SageMaker
  AI endpoints
updated_at: '2026-03-05T22:15:36.399790+00:00'
url_hash: 482e7f567ca261450bf26e57a7df4733c7b9192d
---

Organizations increasingly deploy custom large language models (LLMs) on Amazon SageMaker AI real-time endpoints using their preferred serving frameworks—such as SGLang, vLLM, or TorchServe—to help gain greater control over their deployments, optimize costs, and align with compliance requirements. However, this flexibility introduces a critical technical challenge:
**response format incompatibility**
with Strands agents. While these custom serving frameworks typically return responses in OpenAI-compatible formats to facilitate broad environment support,
[Strands agents](https://Organizations%20increasingly%20deploy%20custom%20large%20language%20models%20(LLMs)%20on%20Amazon%20SageMaker%20AI%20real-time%20endpoints%20using%20their%20preferred%20serving%20frameworks%E2%80%94such%20as%20SGLang,%20vLLM,%20or%20TorchServe%E2%80%94to%20gain%20greater%20control%20over%20their%20deployments,%20optimize%20costs,%20and%20meet%20compliance%20requirements.%20However,%20this%20flexibility%20introduces%20a%20critical%20technical%20challenge:%20response%20format%20incompatibility%20with%20Strands%20agents.%20While%20these%20custom%20serving%20frameworks%20typically%20return%20responses%20in%20OpenAI-compatible%20formats%20to%20ensure%20broad%20ecosystem%20support,%20Strands%20agents%20expect%20model%20responses%20aligned%20with%20the%20Bedrock%20Messages%20API%20format.%20This%20mismatch%20creates%20parsing%20failures%20when%20the%20default%20SageMakerAIModel%20class%20attempts%20to%20access%20fields%20that%20don't%20exist%20in%20the%20OpenAI%20format,%20resulting%20in%20errors%20like%20TypeError:%20'NoneType'%20object%20is%20not%20subscriptable.%20The%20challenge%20is%20particularly%20significant%20because%20support%20for%20the%20Messages%20API%20is%20not%20guaranteed%20for%20all%20models%20hosted%20on%20SageMaker%20AI%20real-time%20endpoints.%20While%20Amazon%20Bedrock's%20Mantle%20distributed%20inference%20engine%20has%20supported%20OpenAI%20messaging%20formats%20since%20December%202024,%20SageMaker's%20flexibility%20allows%20customers%20to%20host%20various%20foundation%20models%E2%80%94some%20requiring%20esoteric%20prompt%20and%20response%20formats%20that%20don't%20conform%20to%20standard%20APIs.%20This%20creates%20a%20gap%20between%20the%20serving%20framework's%20output%20structure%20and%20what%20Strands%20expects,%20preventing%20seamless%20integration%20despite%20both%20systems%20being%20technically%20functional.%20The%20solution%20lies%20in%20implementing%20custom%20model%20parsers%20that%20extend%20SageMakerAIModel%20and%20translate%20the%20model%20server's%20response%20format%20into%20what%20Strands%20expects,%20enabling%20organizations%20to%20leverage%20their%20preferred%20serving%20frameworks%20without%20sacrificing%20compatibility%20with%20the%20Strands%20SDK.)
expect model responses aligned with the Bedrock Messages API format.

The challenge is particularly significant because support for the Messages API is not guaranteed for the models hosted on
[SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
real-time endpoints. While
[Amazon Bedrock Mantle distributed inference engine](https://aws.amazon.com/about-aws/whats-new/2025/12/amazon-bedrock-responses-api-from-openai/)
has supported OpenAI messaging formats since December 2025, flexibility of SageMaker AI allows customers to host various foundation models—some requiring esoteric prompt and response formats that don’t conform to standard APIs. This creates a gap between the serving framework’s output structure and what Strands expects, preventing seamless integration despite both systems being technically functional. The solution lies in implementing
**custom model parsers**
that extend
[SageMakerAIModel](https://strandsagents.com/1.x/documentation/docs/api-reference/python/models/sagemaker/)
and translate the model server’s response format into what Strands expects, enabling organizations to leverage their preferred serving frameworks without sacrificing compatibility with the Strands Agents SDK.

This post demonstrates how to build custom model parsers for Strands agents when working with LLMs hosted on SageMaker that don’t natively support the Bedrock Messages API format. We’ll walk through deploying Llama 3.1 with SGLang on SageMaker using
[awslabs/ml-container-creator](https://github.com/awslabs/ml-container-creator)
, then implementing a custom parser to integrate it with Strands agents.

## Strands Custom Parsers

Strands agents expect model responses in a specific format aligned with the Bedrock Messages API. When you deploy models using custom serving frameworks like SGLang, vLLM, or TorchServe, they typically return responses in their own formats—often OpenAI-compatible for broad environment support. Without a custom parser, you’ll encounter errors like:

`TypeError: 'NoneType' object is not subscriptable`

This happens because the Strands Agents default
`SageMakerAIModel`
class attempts to parse responses assuming a specific structure that your custom endpoint doesn’t provide. In this post and the companion code base, we illustrate how to extend the
`SageMakerAIModel`
class with custom parsing logic that translates your model server’s response format into what Strands expects.

## Implementation Overview

Our implementation consists of three layers:

1. **Model Deployment Layer**
   : Llama 3.1 served by SGLang on SageMaker, returning OpenAI-compatible responses
2. **Parser Layer**
   : Custom
   `LlamaModelProvider`
   class that extends
   `SageMakerAIModel`
   to handle Llama 3.1’s response format
3. **Agent Layer**
   : Strands agent that uses the custom provider for conversational AI, appropriately parsing the model’s response

[![custom-parser-process-flow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/20/ML-19611-image-1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/20/ML-19611-image-1.png)

We start by using
[awslabs/ml-container-creator](https://github.com/awslabs/ml-container-creator)
, an AWS Labs open-source Yeoman generator that automates the creation of SageMaker BYOC (Bring Your Own Container) deployment projects. It generates the artifacts needed to build LLM serving containers, including Dockerfiles, CodeBuild configurations, and deployment scripts.

### Install ml-container-creator

The first step we need to take is to build the serving container for our model. We use an open-source project to build the container and generate deployment scripts for that container. The following commands illustrate how to install
[awslabs/ml-container-creator](https://github.com/awslabs/ml-container-creator)
and its dependencies, which include
[npm](https://www.npmjs.com/)
and
[Yeoman](https://yeoman.io/)
. For more information, review the project’s
[README](https://github.com/awslabs/ml-container-creator?tab=readme-ov-file)
and
[Wiki](https://awslabs.github.io/ml-container-creator/)
to get started.

```
# Install Yeoman globally
npm install -g yo

# Clone and install ml-container-creator
git clone https://github.com/awslabs/ml-container-creator
cd ml-container-creator
npm install && npm link

# Verify installation
yo --generators # Should show ml-container-creator
```

### Generate Deployment Project

Once installed and linked, the yo command allows you to run installed generators, yo ml-container-creator allows you to run the generator we need for this exercise.

```
# Run the generator
yo ml-container-creator

# Configuration options:
# - Framework: transformers
# - Model Server: sglang
# - Model: meta-llama/Llama-3.1-8B-Instruct
# - Deploy Target: codebuild
# - Instance Type: ml.g6.12xlarge (GPU)
# - Region: us-east-1
```

The generator creates a complete project structure:

```
<project-directory>/
├── Dockerfile # Container with SGLang and dependencies
├── buildspec.yml # CodeBuild configuration
├── code/
│ └── serve # SGLang server startup script
├── deploy/
│ ├── submit_build.sh # Triggers CodeBuild
│ └── deploy.sh # Deploys to SageMaker
└── test/
└── test_endpoint.sh # Endpoint testing script
```

### Build and Deploy

Projects built by
[awslabs/ml-container-creator](https://github.com/awslabs/ml-container-creator)
include templatized build and deployment scripts. The
`./deploy/submit_build.sh and ./deploy/deploy.sh`
scripts are used to build the image, push the image to Amazon Elastic Container Registry (ECR), and deploy to an Amazon SageMaker AI real-time endpoint.

```
cd llama-31-deployment

# Build container with CodeBuild (no local Docker required)
./deploy/submit_build.sh

# Deploy to SageMaker
./deploy/deploy.sh arn:aws:iam::ACCOUNT:role/SageMakerExecutionRole
```

The deployment process:

1. CodeBuild builds the Docker image with SGLang and Llama 3.1
2. Image is pushed to Amazon ECR
3. SageMaker creates a real-time endpoint
4. SGLang downloads the model from HuggingFace and loads it into GPU memory
5. Endpoint reaches InService status (approximately 10-15 minutes)

We can test the endpoint by using
`./test/test_endpoint.sh`
, or with a direct invocation:

```
import boto3
import json

runtime_client = boto3.client('sagemaker-runtime', region_name='us-east-1')

payload = {
"messages": [
    {"user", "content": "Hello, how are you?"}
  ],
  "max_tokens": 100,
  "temperature": 0.7
}

response = runtime_client.invoke_endpoint(
  EndpointName='llama-31-deployment-endpoint',
  ContentType='application/json',
  Body=json.dumps(payload)
)

result = json.loads(response['Body'].read().decode('utf-8'))
print(result['choices'][0]['message']['content'])
```

### Understanding the Response Format

Llama 3.1 returns OpenAI-compatible responses. Strands expects model responses to adhere to the Bedrock Messages API format. Until late last year, this was a standard compatibility mismatch. Since December 2025, the
[Amazon Bedrock Mantle distributed inference engine supports OpenAI messaging formats](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-mantle.html)
:

```
{
  "id": "cmpl-abc123",
  "object": "chat.completion",
  "created": 1704067200,
  "model": "meta-llama/Llama-3.1-8B-Instruct",
  "choices": [{
    "index": 0,
    "message": {"role": "assistant", "content": "I'm doing well, thank you for asking!"},
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 23,
    "completion_tokens": 12,
    "total_tokens": 35
  }
}
```

However, support for the Messages API is not guaranteed for the models hosted on SageMaker AI real-time endpoints. SageMaker AI allows customers to host many kinds of foundation models on managed GPU-accelerated infrastructure, some of which may require esoteric prompt/response formats. For example, the default
`SageMakerAIModel`
uses the legacy Bedrock Messages API format and attempts to access fields that don’t exist in the standard OpenAI Messages format, causing
`TypeError`
style failures.

### Implementing a Custom Model Parser

Custom model parsers are a feature of the
[Strands Agents SDK](https://strandsagents.com/latest/)
that provides strong compatibility and flexibility for customers building agents powered by LLMs hosted on SageMaker AI. Here, we describe how to create a custom provider that extends
`SageMakerAIModel`
:

```
def stream(self, messages: List[Dict[str, Any]], tool_specs: list, system_prompt: Optional[str], **kwargs):
  # Build payload messages
  payload_messages = []
  if system_prompt:
    payload_messages.append({"role": "system", "content": system_prompt})
    # Extract message content from Strands format
    for msg in messages:
      payload_messages.append({"role": "user", "content": msg['content'][0]['text']})

      # Build complete payload with streaming enabled
      payload = {
        "messages": payload_messages,
        "max_tokens": kwargs.get('max_tokens', self.max_tokens),
        "temperature": kwargs.get('temperature', self.temperature),
        "top_p": kwargs.get('top_p', self.top_p),
        "stream": True
      }

      try:
        # Invoke SageMaker endpoint with streaming
        response = self.runtime_client.invoke_endpoint_with_response_stream(
          EndpointName=self.endpoint_name,
          ContentType='application/json',
          Accept='application/json',
          Body=json.dumps(payload)
        )

        # Process streaming response
        accumulated_content = ""
          for event in response['Body']:
            chunk = event['PayloadPart']['Bytes'].decode('utf-8')
            if not chunk.strip():
              continue

            # Parse SSE format: "data: {json}\n"
            for line in chunk.split('\n'):
              if line.startswith('data: '):
                try:
                  json_str = line.replace('data: ', '').strip()
                  if not json_str:
                    continue

                  chunk_data = json.loads(json_str)
                  if 'choices' in chunk_data and chunk_data['choices']:
                    delta = chunk_data['choices'][0].get('delta', {})

                    # Yield content delta in Strands format
                    if 'content' in delta:
                      content_chunk = delta['content']
                      accumulated_content += content_chunk
                      yield {
                        "type": "contentBlockDelta",
                        "delta": {"text": content_chunk},
                        "contentBlockIndex": 0
                      }

                    # Check for completion
                    finish_reason = chunk_data['choices'][0].get('finish_reason')
                    if finish_reason:
                      yield {
                        "type": "messageStop",
                        "stopReason": finish_reason
                      }

                    # Yield usage metadata
                    if 'usage' in chunk_data:
                      yield {
                        "type": "metadata",
                        "usage": chunk_data['usage']
                      }

                except json.JSONDecodeError:
                  continue

      except Exception as e:
        yield {
          "type": "error",
          "error": {
            "message": f"Endpoint invocation failed: {str(e)}",
            "type": "EndpointInvocationError"
          }
      }
```

The stream method overrides the behavior of the
`SageMakerAIModel`
and allows the agent to parse responses based on the requirements of the underlying model. While the vast majority of models do support OpenAI’s Message API protocol, this capability enables power-users to leverage highly specified LLMs on SageMaker AI to power agent workloads using Strands Agents SDK. Once the custom model response logic is built, Strands Agents SDK makes it simple to initialize agents with custom model providers:

```
from strands.agent import Agent

# Initialize custom provider
provider = LlamaModelProvider(
  endpoint_name="llama-31-deployment-endpoint",
  region_name="us-east-1",
  max_tokens=1000,
  temperature=0.7
)

# Create agent with custom provider
agent = Agent(
  name="llama-assistant",
  model=provider,
  system_prompt=(
    "You are a helpful AI assistant powered by Llama 3.1, "
    "deployed on Amazon SageMaker. You provide clear, accurate, "
    "and friendly responses to user questions."
  )
)

# Test the agent
response = agent("What are the key benefits of deploying LLMs on SageMaker?")
print(response.content)
```

The complete implementation for this custom parser, including the Jupyter notebook with detailed explanations and the ml-container-creator deployment project, is available in the companion
[GitHub repository](https://github.com/aws-samples/sagemaker-genai-hosting-examples/tree/main/05-agents/strands/custom-response-parser)
.

## Conclusion

Building custom model parsers for Strands agents helps users to leverage different LLM deployments on SageMaker, regardless of its response format. By extending
`SageMakerAIModel`
and implementing the
`stream()`
method, you can integrate custom-hosted models while maintaining the clean agent interface of Strands.

#### **Key takeaways** :

1. [**awslabs/ml-container-creator**](https://github.com/awslabs/ml-container-creator)
   simplifies SageMaker BYOC deployments with production-ready infrastructure code
2. Custom parsers bridge the gap between model server response formats and Strands expectations
3. The stream() method is the critical integration point for custom providers

---

### About the authors

[![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/frgud.jpg)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/02/frgud.jpg)
**Dan Ferguson**
is a Sr. Solutions Architect at AWS, based in New York, USA. As a machine learning services expert, Dan works to support customers on their journey to integrating ML workflows efficiently, effectively, and sustainably.