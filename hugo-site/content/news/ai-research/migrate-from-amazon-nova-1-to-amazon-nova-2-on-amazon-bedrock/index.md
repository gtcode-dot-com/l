---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-23T05:48:08.443075+00:00'
exported_at: '2026-03-23T05:48:11.256672+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/migrate-from-amazon-nova-1-to-amazon-nova-2-on-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: In this post, you will learn how to migrate from Nova 1 to Nova 2 on
    Amazon Bedrock. We cover model mapping, API changes, code examples using the Converse
    API, guidance on configuring new capabilities, and a summary of use cases. We
    conclude with a migration checklist to help you plan and execute your transition.
  headline: Migrate from Amazon Nova 1 to Amazon Nova 2 on Amazon Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/migrate-from-amazon-nova-1-to-amazon-nova-2-on-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Migrate from Amazon Nova 1 to Amazon Nova 2 on Amazon Bedrock
updated_at: '2026-03-23T05:48:08.443075+00:00'
url_hash: 4831ee73728ef71779c5311afa14ea6970787dc8
---

If you’re running Amazon Nova 1 models on
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
, you might be looking to expand your context window size, deepen reasoning capabilities, or integrate external tools for web search and code execution.
[Amazon Nova 2](https://aws.amazon.com/nova/models/)
models address these constraints while improving performance on reasoning, agentic AI, and
[tool use](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-tools.html)
benchmarks.

Amazon Nova 2 Lite achieves higher scores across problem identification, solution completeness, and logical coherence benchmarks, while maintaining fast response times for high-volume workloads. If you’re using Nova 1 Lite for customer support automation, document processing, or agentic AI applications, you will likely see measurable gains in accuracy and throughput upon migrating to Nova 2 Lite. This post focuses on migration to Nova 2 Lite, which is generally available and ready for production use. Nova 2 expands the context window to one million tokens, which supports richer in-context learning and allows for processing longer documents in a single request. You also gain access to extended thinking, built-in web grounding, and a code interpreter. These features can enhance your existing applications with minimal code changes.

In this post, you will learn how to migrate from Nova 1 to Nova 2 on Amazon Bedrock. We cover model mapping, API changes, code examples using the Converse API, guidance on configuring new capabilities, and a summary of use cases. We conclude with a migration checklist to help you plan and execute your transition.

## Migration paths

The following are recommended migration paths for the Nova 1 models. For Pro and Premier migrations, evaluate with extended thinking enabled to verify quality on your workloads.

1. If you’re running
   **Amazon Nova 1 Lite**
   , the migration path is straightforward: Nova 2 Lite is a direct upgrade that maintains the same input modalities (text, image, and video) while adding extended thinking, built-in tools, and a context window that expands from 300K to 1M tokens.
2. If you’re running
   **Amazon Nova 1 Pro**
   , we recommend upgrading to Nova 2 Lite. While this might seem like a tier change, Nova 2 Lite delivers improved reasoning capabilities at competitive price-performance. The extended thinking feature in Nova 2 Lite, combined with its 1M token context window, enables it to handle workloads that previously required Nova 1 Pro’s larger model size.
3. If you’re running
   **Amazon Nova Premier**
   , consider migrating to Nova 2 Lite, especially for agentic and tool use workloads. As documented in the
   [Amazon Nova 2 Technical Report](https://www.amazon.science/publications/amazon-nova-2-multimodal-reasoning-and-generation-models)
   , Nova 2 Lite surpasses Premier in multi-step problem-solving at 7x lower cost and up to 5x faster inference. Because Nova 2 Lite with extended thinking enabled is still cheaper and faster than Premier, we recommend evaluating across reasoning effort levels to verify that it meets your quality requirements.

## Use cases and customer stories

Since Nova 2 Lite launched at re:Invent 2025, you can use the model for a variety of use cases. Nova 2 Lite excels at driving high throughput applications that require a combination of price, performance, and speed. Common use cases that customers have deployed Nova 2 Lite in production include:

**Natural Language Processing (NLP) tasks**

Nova 2 Lite is used for a wide variety of NLP tasks, from simple text predictors to logic-based recommendations. The Nova 2 models excel at summarization, classification, and search based use cases. Nova 2 Lite scores 80.9% on MMLU Pro and 70.8% on IF-Bench (with both higher than some comparable models). Nova 2 Lite is also designed for low latency, making it suitable for applications requiring rapid responses, as is typical with most NLP tasks.

[Siemens](https://www.siemens.com/us/en.html)
global search runs on Nova 2 Lite, providing a 300% improvement in search speed and 70% cost reductions compared to their prior large language model (LLM) solution. The full case study can be found on the
[AWS case studies](https://aws.amazon.com/solutions/case-studies/siemens-nova-case-study/)
page.

**Intelligent Document Processing (IDP)**

Nova 2 models with reasoning enhance IDP by moving beyond basic text extraction to true semantic understanding of documents. They can process unstructured and semistructured content such as contracts, invoices, forms, and reports, and determine what information means in context, not only where it appears. Reasoning enables these models to link related information across sections, pages, and tables, handle variations in layout and language, and infer missing or implicit details, making document processing more robust and scalable. Reasoning adds value by (1) understanding context. For example, distinguishing a contract’s start date from an end date even if both appear as similar timestamps. (2) linking and inferring across pages. For example, tying invoice line items to totals/taxes and checking the math (even filling small gaps when text is unreadable). (3) normalizing variation—treating “amount payable,” “balance due,” and “total outstanding” as the same concept. (4) enabling smarter actions like validation, anomaly detection, and Q&A—flagging mismatched tax calculations or identifying auto-renewal clauses from related sections. Reasoning turns IDP into a smarter, more human-like system that understands and validates documents, enabling more accurate automation, less manual review, and faster adaptation to new ontology.

**Multi-step agentic workflows**

Nova 2 Lite shows considerable improvement over the Nova 1 models in tool calling capabilities, especially if multiple tools are part of the workflow. Overall, the Nova 2 family excels at completing complex, multi-step agentic workflows with sophisticated tool use and planning capabilities. Nova 2 Lite scores higher than comparable models in τ2-bench Telecom, at 76.0%. We recommend testing multi-step agentic use cases with reasoning on, starting with reasoning set to “Low” and then working upwards, if required.

Nova 2 Lite has empowered
**Trellix**
to continue to automate its security alert triage tasks and better empower security teams, in the areas of threat detection, analysis, and classification. With the release of the new model, Trellix saw more reliable tool calling capabilities with no failures, a 39% accuracy boost in threat classification, and 3.4x more detailed responses with technical analysis.
Watch
[Trellix’s CTO explain the solution](https://www.youtube.com/watch?v=jdm-j6_zYE0)
in this video.

[AWS Transform](https://aws.amazon.com/transform/)
is a multi-agent, multiuser system that uses dozens of tools to modernize complex infrastructure systems and code bases. AWS Transform breaks down each user request into a number of agent and tool calls that are routed to a mixture of models to balance cost, speed, and accuracy. Evaluations showed that Nova 2 Lite improves tool calling efficiency for code modernization in AWS Transform by up to 60%.

## What’s changed

The Nova 2 family introduces capabilities that expand how you can build AI applications, particularly for agentic AI workloads.

**Extended thinking with developer controls**

Nova 2 Lite can reason through complex problems before responding. You control the depth of reasoning through the
`reasoningConfig`
parameter with low, medium, or high effort levels.

**Native tool use and built-in web grounding and code interpreter**

Nova 2 Lite is designed for tool use, including support for MCP servers and parallel tool chaining. It also includes built-in
[web grounding](https://docs.aws.amazon.com/nova/latest/nova2-userguide/web-grounding.html)
for real-time information with citations and a
[code interpreter](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-tools.html)
for executing Python code directly.

**Extended context for large-scale inputs**

The context window expands from 300K to 1M tokens, and maximum output tokens increase from 10K to 65K. With these increases, you can process larger documents, code bases, and longer multi-turn workflows in a single request.

The following table summarizes the technical specifications across Nova 1 models and Nova 2 Lite:

|  |  |  |  |
| --- | --- | --- | --- |
| Specification | Nova 1 Lite | Nova 1 Pro | Nova 2 Lite |
| **Context Window** | 300K | 300K | 1M |
| **Max Output Tokens** | 10K | 10K | 65K |
| **Input Modalities** | Text, image, video | Text, image, video | Text, image, video |
| **Extended Thinking** | No | No | Yes |
| **Built-in Tools** | No | No | Yes |
| **Customization** | Yes (incl. Nova Forge) | Yes (incl. Nova Forge) | Yes (incl. Nova Forge) |

### Performance and pricing

Independent benchmarks from Artificial Analysis show that
[Nova 2 Lite](https://artificialanalysis.ai/models/nova-2-0-lite)
scores above average on intelligence among comparable models and is notably fast, making it well-suited for high-volume workloads where throughput matters. On agentic-specific benchmarks, Nova 2 Lite performs well on Tool Use (Tau2 Telecom). Strong instruction following is critical for agentic workloads where the model must reliably execute multi-step plans. For detailed benchmark methodology and additional results, see the
[Amazon Nova 2 Technical Report](https://assets.amazon.science/c5/3d/84514a224666b5be6de4b43ef4aa/nova-2-0-technical-report2.pdf)
.

Pricing for the Nova 2 family reflects the expanded capabilities while remaining competitive within their respective tiers.

|  |  |  |
| --- | --- | --- |
| Model | Input (per 1M tokens) | Output (per 1M tokens) |
| Nova 1 Lite | $0.06 | $0.24 |
| Nova 1 Pro | $0.80 | $3.20 |
| **Nova 2 Lite** | $0.30 | $2.50 |

For Nova 2 Lite, pricing is competitive against similar models in its class. For the full announcement and additional details, see the
[Amazon Nova 2 launch post](https://aws.amazon.com/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/)
.

## API changes and code updates

Update your model ID to reference Nova 2 Lite, which is available through Global Cross-Region Inference System (CRIS), US CRIS, EU CRIS, and JP CRIS endpoints. When accessing models from a US region, use the us. prefix (for example,
`us.amazon.nova-2-lite-v1:0`
); when accessing from outside the US, use the global. prefix (for example,
`global.amazon.nova-2-lite-v1:0`
). The underlying API structure remains consistent, so existing integrations will work with minimal changes beyond the model ID and any new features that you choose to enable.

Breaking change: When
`maxReasoningEffort`
is set to
`high`
, you cannot use
`maxTokens`
,
`temperature`
,
`topP`
, or
`topK`
. Requests that include these parameters with high effort reasoning will return an error. To resolve this, remove the
`inferenceConfig`
block entirely from your request.

### New features and unchanged behaviors

The following table summarizes new features and unchanged behaviors between Nova 1 and Nova 2:

|  |  |  |
| --- | --- | --- |
| Category | Change | Details |
| **New** | Extended thinking | Enable reasoning using `reasoningConfig` in `additionalModelRequestFields` . Supports three effort levels: `low` , `medium` , and `high` . |
| **New** | Reasoning content in responses | Responses include a `reasoningContent` field when reasoning is enabled. Content displays as `[REDACTED]` but reasoning tokens are billed. |
| **New** | Built-in tools | Web grounding and code interpreter are available without external integrations. |
| **New** | Increased output capacity | Maximum output tokens increased from 10K to 65,536. |
| **New** | Expanded context window | Nova 2 Lite supports 1M tokens (up from 300K in Nova 1 Lite). |
| **Unchanged** | topK parameter location | `topK` is still passed through `additionalModelRequestFields` , not `inferenceConfig` . |
| **Unchanged** | Document support | Document input is still Converse API only (not supported in Invoke API). |
| **Unchanged** | Timeout configuration | Boto3’s default read timeout is 60 seconds, but extended thinking requests can take up to 60 minutes. Configure `read_timeout` =3600 in your SDK client. |

## Configuring new capabilities

This section covers the basic migration steps, extended thinking configuration, and how to use built-in tools like web grounding and code interpreter.

### Basic migration – update the model ID

For applications that do not require extended thinking, the migration is straightforward. Update the model ID and your existing code will work:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

# Nova 1
# modelId='us.amazon.nova-lite-v1:0'

# Nova 2
response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    system=[{'text': 'You are a helpful assistant'}],
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Explain cloud computing in simple terms.'}]
        }
    ],
    inferenceConfig={
        'maxTokens': 1024,
        'temperature': 0.7,
        'topP': 0.9
    }
)

print(response['output']['message']['content'][0]['text'])
```

### Extended thinking

Extended thinking allows Nova 2 model to reason through complex problems before generating responses. This capability is disabled by default to optimize for speed and cost on simple queries. When your workload requires multi-step reasoning, you can enable it through the
`reasoningConfig`
parameter.

**Configuring reasoning effort levels**

Nova 2 Lite provides three effort levels that control how much reasoning the model performs:

1. **Low effort**
   (
   `maxReasoningEffort: "low"`
   ) is recommended for tasks with added complexity that benefit from structured thinking. Use low effort for code review and improvement suggestions, analysis tasks that require consideration of multiple factors, or problem-solving scenarios that benefit from a methodical approach. Low effort improves accuracy on compound tasks without requiring deep multi-step planning. We recommend starting with low effort and working your way up to higher effort levels as needed for your specific use case.
2. **Medium effort**
   (
   `maxReasoningEffort: "medium"`
   ) is recommended for multi-step tasks and coding workflows. Use medium effort for software development and debugging where the model must understand existing code structure, code generation that requires coordination across multiple files, multi-step calculations with interdependencies, or planning tasks with multiple constraints. Medium effort is recommended for agentic workflows that coordinate multiple tools and require the model to maintain context across sequential operations.
3. **High effort**
   (
   `maxReasoningEffort: "high"`
   ) is recommended for STEM reasoning and advanced problem-solving. Use high effort for advanced mathematical problems and proofs, scientific analysis, complex system design, or critical decision-making scenarios. When using high effort, do not include maxTokens, temperature, topP, or topK.

***Example – Medium Effort Reasoning:***

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    system=[{'text': 'You are a helpful assistant'}],
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?'}]
        }
    ],
    inferenceConfig={
        'maxTokens': 10000,
        'temperature': 0.7,
        'topP': 0.9
    },
    additionalModelRequestFields={
        'reasoningConfig': {
            'type': 'enabled',
            'maxReasoningEffort': 'medium'
        }
    }
)

# Extract the response text
content_list = response['output']['message']['content']
text = next((item['text'] for item in content_list if 'text' in item), None)
print(text)
```

***Example – High effort reasoning (note the parameter restrictions):***

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    system=[{'text': 'You are a mathematical reasoning assistant'}],
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Prove that the square root of 2 is irrational.'}]
        }
    ],
    # Do not include inferenceConfig at all with high effort reasoning
    # (no maxTokens, temperature, topP, or topK)
    additionalModelRequestFields={
        'reasoningConfig': {
            'type': 'enabled',
            'maxReasoningEffort': 'high'
        }
    }
)

# Extract the response text
content_list = response['output']['message']['content']
text = next((item['text'] for item in content_list if 'text' in item), None)
print(text)
```

***Understanding the response structure***

When reasoning is enabled, the response includes a
`reasoningContent`
field alongside the text response:

```
{
    "output": {
        "message": {
            "role": "assistant",
            "content": [
                {
                    "reasoningContent": {
                        "reasoningText": {
                            "text": "[REDACTED]"
                        }
                    }
                },
                {
                    "text": "Based on my analysis, here is the recommended architecture..."
                }
            ]
        }
    },
    "stopReason": "end_turn"
}
```

The reasoning content currently displays as
`[REDACTED]`
. You are still charged for reasoning tokens because they contribute to improved output quality.

***Cost, latency, and timeout configuration***

Extended thinking increases both cost and latency because the model generates additional reasoning tokens before producing the final response. Enable reasoning when accuracy on complex tasks justifies the additional cost, and disable it for simple queries where speed is the priority.

```
import boto3
from botocore.config import Config

bedrock = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    config=Config(
        read_timeout=3600  # 60 minutes
    )
)
```

### Built-in tools: web grounding and code interpreter

Built-in system tools in Nova 2 extend model capabilities without requiring custom implementations. You enable these tools through the
`toolConfig`
parameter in the Converse API, and Nova automatically decides when to use them based on the context of your prompt.

***Web Grounding***

To enable Web Grounding, specify
`nova_grounding`
as a system tool in your tool configuration:

```
import boto3
from botocore.config import Config

bedrock = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    config=Config(read_timeout=3600)
)

tool_config = {
    'tools': [{
        'systemTool': {
            'name': 'nova_grounding'
        }
    }]
}

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[{
        'role': 'user',
        'content': [{'text': 'What are the latest developments in quantum computing?'}]
    }],
    toolConfig=tool_config
)

# Extract text with interleaved citations
output_with_citations = ''
content_list = response['output']['message']['content']
for content in content_list:
    if 'text' in content:
        output_with_citations += content['text']
    elif 'citationsContent' in content:
        citations = content['citationsContent']['citations']
        for citation in citations:
            url = citation['location']['web']['url']
            output_with_citations += f' [{url}]'

print(output_with_citations)
```

The response includes
`citationsContent`
objects containing the source URL and domain for each citation. You are responsible for retaining and displaying these citations to your end users.

Web Grounding is available in US AWS Regions only and requires either
`BedrockFullAccess`
or explicit
`bedrock:InvokeTool`
permissions for the
`amazon.nova_grounding`
resource. Web Grounding incurs additional costs beyond standard inference pricing. For pricing details, see
[Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)
.

***Code Interpreter***

Code Interpreter allows Nova to execute Python code in isolated sandbox environments. This tool is designed for mathematical computations, logical operations, and iterative algorithms where precise calculation is required. To enable Code Interpreter, specify
`nova_code_interpreter`
as a system tool:

```
import boto3

bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')

tool_config = {
    'tools': [{
        'systemTool': {
            'name': 'nova_code_interpreter'
        }
    }]
}

response = bedrock.converse(
    modelId='us.amazon.nova-2-lite-v1:0',
    messages=[{
        'role': 'user',
        'content': [{'text': 'Calculate the compound interest on $10,000 at 4.75% annual rate for 7 years, compounded quarterly.'}]
    }],
    toolConfig=tool_config,
    inferenceConfig={'maxTokens': 10000, 'temperature': 0}
)

# Process the response
for block in response['output']['message']['content']:
    if 'toolUse' in block:
        print(f"Code executed:\n{block['toolUse']['input']['snippet']}\n")
    elif 'toolResult' in block:
        result = block['toolResult']['content'][0]['json']
        print(f"Output: {result['stdOut']}")
    elif 'text' in block:
        print(f"Answer: {block['text']}")
```

The interpreter runs code in a sandbox and returns results in a structured format that includes
`stdOut`
,
`stdErr`
,
`exitCode`
, and
`isError`
fields.

Code Interpreter is available in the US East (N. Virginia), US West (Oregon), and Asia Pacific (Tokyo) Regions. To ensure that your requests are routed to a supported Region, use Global CRIS. You must manually add
`InvokeTool`
permissions to your
[Identity and Access Management (IAM) policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
; the default Amazon Bedrock role does not include this action.

For detailed documentation on built-in tools, see
[Web Grounding](https://docs.aws.amazon.com/nova/latest/nova2-userguide/web-grounding.html)
and
[Tool Use](https://docs.aws.amazon.com/nova/latest/nova2-userguide/using-tools.html)
in the Amazon Nova documentation.

## Framework-specific examples

The previous examples use the Converse API directly. If you’re using LangChain or Strands Agents SDK, the migration follows the same pattern: update the model ID and optionally enable extended thinking.

***Langchain***

The
`langchain-aws`
package provides a
`ChatBedrockConverse`
class that integrates with the Amazon Bedrock Converse API. Install the package with
`pip install langchain-aws`
.

```
from langchain_aws import ChatBedrockConverse

# Nova 1
# llm = ChatBedrockConverse(model="us.amazon.nova-lite-v1:0", ...)

# Nova 2
llm = ChatBedrockConverse(
    model="us.amazon.nova-2-lite-v1:0",
    region_name="us-east-1",
    temperature=0.7,
    max_tokens=1024
)

messages = [
    ("system", "You are a helpful assistant."),
    ("human", "Explain cloud computing in simple terms."),
]

response = llm.invoke(messages)
print(response.content)
```

To enable extended thinking, pass the
`reasoningConfig`
through
`additional_model_request_fields`
:

```
llm = ChatBedrockConverse(
    model="us.amazon.nova-2-lite-v1:0",
    region_name="us-east-1",
    max_tokens=10000,
    additional_model_request_fields={
        "reasoningConfig": {
            "type": "enabled",
            "maxReasoningEffort": "medium"
        }
    }
)

messages = [
    ("system", "You are a software architect."),
    ("human", "Design a scalable microservices architecture for an e-commerce platform."),
]

response = llm.invoke(messages)

# Extract just the text content (skip reasoning_content blocks)
for block in response.content:
    if isinstance(block, dict) and block.get('type') == 'text':
        print(block['text'])
    elif hasattr(block, 'type') and block.type == 'text':
        print(block.text)
```

***Strands Agents SDK***

For agentic applications, the
[Strands Agents SDK](https://strandsagents.com/latest/documentation/docs/user-guide/concepts/model-providers/amazon-nova/)
connects to the Nova API directly. Install the required packages with
`pip install strands-agents strands-amazon-nova`
.

```
import os
from strands import Agent
from strands_amazon_nova import NovaAPIModel

# Nova 1
# model = NovaAPIModel(model_id="nova-lite-v1", ...)

# Nova 2
model = NovaAPIModel(
    api_key=os.environ["NOVA_API_KEY"],
    model_id="nova-2-lite-v1",
    params={
        "max_tokens": 1024,
        "temperature": 0.7
    }
)

agent = Agent(model=model)
response = agent("Explain cloud computing in simple terms.")
print(response.message)
```

To enable extended thinking, add the
`reasoning_effort`
parameter:

```
model = NovaAPIModel(
    api_key=os.environ["NOVA_API_KEY"],
    model_id="nova-2-lite-v1",
    params={
        "max_tokens": 10000,
        "reasoning_effort": "medium"
    }
)

agent = Agent(model=model)
response = agent("Design a scalable microservices architecture for an e-commerce platform.")
print(response.message)
```

## Evaluation and rollout strategy

Before deploying Nova 2 to production, verify that the new model performs as well as or better than Nova 1 on your specific tasks. Create a curated dataset of prompts and expected outputs that represent your actual production traffic. For evaluation, combine multiple approaches: deterministic metrics like latency, token usage, and exact-match accuracy for structured outputs; LLM-as-a-judge through
[Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
for subjective quality assessment across helpfulness, correctness, and safety; and human evaluation for high-stakes use cases where automated metrics might miss nuances. Integrate these evaluations into your continuous integration and continuous delivery (CI/CD) pipeline to catch regressions early.

For production deployment, implement a phased rollout. Start with shadow testing to compare Nova 2 outputs against Nova 1 without affecting users. Progress to A/B testing with a small percentage of traffic to measure business impact. Use canary releases or blue/green deployments to maintain rollback capability if issues arise.

## Building responsibly with Nova 2

Amazon Nova 2 models are developed with safety, security, and trust as core priorities throughout the model development lifecycle, with built-in content moderation aligned to the
[AWS Acceptable Use Policy](https://aws.amazon.com/aup/)
. AWS also offers uncapped intellectual property indemnity coverage for outputs of generally available Amazon Nova models. While AWS provides these foundational safeguards, you share the responsibility for responsible deployment. During your migration, evaluate Nova 2 outputs for accuracy and appropriateness on your specific use cases, particularly for applications that surface results directly to end users or inform consequential decisions. For high-stakes workloads, implement appropriate human oversight and use-case-specific guardrails such as
[Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
. For detailed guidance on Amazon Nova’s responsible AI approach and recommendations, see
[Responsible use of Amazon Nova](https://docs.aws.amazon.com/nova/latest/nova2-userguide/responsible-use.html)
.

## Migration checklist

Use this checklist to plan and execute your Nova 1 to Nova 2 migration.

* Identify your current Nova 1 model and target Nova 2 model (Lite → 2 Lite, Pro → 2 Lite)
* Request model access in the Amazon Bedrock console for each Region that you need
* Update model IDs in your code (for example,
  `us.amazon.nova-lite-v1:0`
  →
  `us.amazon.nova-2-lite-v1:0`
  )
* Configure client timeout to 3,600 seconds for extended thinking workloads
* If using high effort reasoning, remove temperature, topP, and topK parameters
* Update IAM policies if using built-in tools (InvokeTool permission required)
* Run evaluation tests comparing Nova 1 and Nova 2 outputs on your production prompts
* Deploy using shadow testing or canary release before full rollout

## Cleaning up

If you created test resources while following this guide, delete them to avoid ongoing charges. This includes:

* Any test Amazon Bedrock invocations (these are charged per token, so no cleanup needed unless you provisioned throughput)
* Test IAM policies or roles created specifically for Nova 2 migration testing
* Any Amazon CloudWatch Logs generated during testing, if you no longer need them for debugging

If you provisioned dedicated throughput for testing the Nova 2 model, delete the provisioned throughput in the Amazon Bedrock console to stop incurring charges.

## Conclusion

Migrating from Nova 1 to Nova 2 on Amazon Bedrock is straightforward for most workloads. Update your model IDs, adjust parameters if you plan to use high effort reasoning, and run evaluation tests on your production prompts before full deployment. The core API structure remains the same, so existing Converse API integrations require minimal code changes.

Nova 2 brings capabilities that can improve your applications without architectural changes: extended thinking for complex reasoning, built-in tools like web grounding and code interpreter, and an expanded context window for longer documents. To get started, request access to the Nova 2 model in the
[Amazon Bedrock console](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-console.html)
and run a comparison test against your current Nova 1 deployment. For detailed documentation, see the
[Amazon Nova User Guide](https://docs.aws.amazon.com/nova/latest/nova2-userguide/getting-started-nova-2.html)
.

### Acknowledgement

Special thanks to Sneha Venkateswaran, Sharon Li and Jean Farmer for their contribution.

---

## About the authors

### Adewale Akinfaderin

[Adewale](https://www.linkedin.com/in/waleakinfaderin/)
is a Sr. Data Scientist–Generative AI, Amazon Bedrock, where he contributes to cutting edge innovations in foundational models and generative AI applications at AWS. His expertise is in reproducible and end-to-end AI/ML methods, practical implementations, and helping global customers formulate and develop scalable solutions to interdisciplinary problems. He has two graduate degrees in physics and a doctorate in engineering.

### Veda Raman

[Veda](https://www.linkedin.com/in/vedashreeraman/)
is a Sr Solutions Architect for Generative AI for Amazon Nova and Agentic AI at AWS. She helps customers design and build Agentic AI solutions using Amazon Nova models and Bedrock AgentCore. She previously worked with customers building ML solutions using Amazon SageMaker and also as a serverless solutions architect at AWS.

### Wrick Talukdar

[Wrick](https://www.linkedin.com/in/wrick-talukdar/)
is a technology leader and Senior Generative AI Specialist at AWS, focused on multimodal foundation models and agentic AI. He is the bestselling author of Building Agentic AI Systems and Generative AI Ethics, Privacy, and Security, serves as Chair of the IEEE Technology & Intelligence group for 2026–2027, and frequently speaks at major global forums including AWS re:Invent, ICCE, CERAWeek, and ADIPEC. Outside work, he enjoys writing and birding photography.