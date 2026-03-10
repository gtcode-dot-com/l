---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-10T00:15:34.346072+00:00'
exported_at: '2026-03-10T00:15:38.575514+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/run-nvidia-nemotron-3-nano-as-a-fully-managed-serverless-model-on-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: We are excited to announce that NVIDIA’s Nemotron 3 Nano is now available
    as a fully managed and serverless model in Amazon Bedrock. This follows our earlier
    announcement at AWS re:Invent supporting NVIDIA Nemotron 2 Nano 9B and NVIDIA
    Nemotron 2 Nano VL 12B models. This post explores the technical characteristics
    o...
  headline: Run NVIDIA Nemotron 3 Nano as a fully managed serverless model on Amazon
    Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/run-nvidia-nemotron-3-nano-as-a-fully-managed-serverless-model-on-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Run NVIDIA Nemotron 3 Nano as a fully managed serverless model on Amazon Bedrock
updated_at: '2026-03-10T00:15:34.346072+00:00'
url_hash: 21d8c7fa4323587d3d41a27330772415c68b12a9
---

*This post is cowritten with Abdullahi Olaoye, Curtice Lockhart, Nirmal Kumar Juluru from NVIDIA.*

We are excited to announce that
[NVIDIA’s Nemotron 3 Nano](https://developer.nvidia.com/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/)
is now available as a fully managed and serverless model in Amazon Bedrock. This follows our
[earlier announcement at AWS re:Invent](https://aws.amazon.com/blogs/aws/amazon-bedrock-adds-fully-managed-open-weight-models/)
supporting NVIDIA Nemotron 2 Nano 9B and NVIDIA Nemotron 2 Nano VL 12B models.

With
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)
open models on Amazon Bedrock, you can accelerate innovation and deliver tangible business value without having to manage infrastructure complexities. You can power your
[generative AI](https://aws.amazon.com/ai/generative-ai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
applications with Nemotron’s capabilities through the inference capabilities of Amazon Bedrock and harness the benefit of its extensive features and tooling.

This post explores the technical characteristics of the NVIDIA Nemotron 3 Nano model and discusses potential application use cases. Additionally, it provides technical guidance to help you get started using this model for your generative AI applications within the Amazon Bedrock environment.

## About Nemotron 3 Nano

NVIDIA Nemotron 3 Nano is a small language model (SLM) with a hybrid Mixture-of-Experts (MoE) architecture that delivers high compute efficiency and accuracy that developers can use to build specialized agentic AI systems. The model is fully open with open-weights, datasets, and recipes facilitating transparency and confidence for developers and enterprises. Compared to other similar sized models, Nemotron 3 Nano excels in coding and reasoning tasks, taking the lead on benchmarks such as SWE Bench Verified, AIME 2025, Arena Hard v2, and IFBench.

### Model overview:

* Architecture:
  + Mixture-of-Experts (MoE) with Hybrid Transformer-Mamba Architecture
  + Supports Token Budget for providing accuracy while avoiding overthinking
* Accuracy:
  + Leading accuracy on coding, scientific reasoning, math, tool calling, instruction following, and chat
  + Nemotron 3 Nano leads on benchmarks such as SWE Bench, AIME 2025, Humanity Last Exam, IFBench, RULER, and Arena Hard (compared to other open language models with 30 billion or fewer MoE)
* Model size: 30 B with 3 B active parameters
* Context length: 256K
* Model input: Text
* Model output: Text

Nemotron 3 Nano combines Mamba, Transformer, and Mixture-of-Experts layers into a single backbone to help balance efficiency, reasoning accuracy, and scale. Mamba enables long-range sequence modeling with low memory overhead, while Transformer layers help add precise attention for structured reasoning tasks like code, math, and planning. MoE routing further boosts scalability by activating only a subset of experts per token, helping to improve latency and throughput. This makes Nemotron 3 Nano especially well-suited for agent clusters running many concurrent, lightweight workflows.

To learn more about Nemotron 3 Nano’s architecture and how it is trained, see
[Inside NVIDIA Nemotron 3: Techniques, Tools, and Data That Make It Efficient and Accurate](https://developer.nvidia.com/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/)
.

## Model benchmarks

The following image shows that Nemotron 3 Nano leads in the most attractive quadrant in
[Artificial Analysis](https://artificialanalysis.ai/)
[Openness Index vs. Intelligence Index](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index?models=gpt-oss-20b%2Cllama-4-scout%2Cmagistral-small-2509%2Cdeepseek-r1-qwen3-8b%2Cnvidia-nemotron-nano-12b-v2-vl-reasoning%2Cnvidia-nemotron-nano-9b-v2-reasoning%2Cnvidia-nemotron-3-nano-30b-a3b-reasoning%2Cqwen3-30b-a3b-2507-reasoning%2Cqwen3-vl-32b-reasoning%2Colmo-3-32b-think"%20\l%20"artificial-analysis-openness-index-vs-artificial-analysis-intelligence-index)
. Why openness matters: It builds trust through transparency. Developers and enterprises can confidently build on Nemotron with clear visibility into the model, data pipeline, and data characteristics, enabling straightforward auditing and governance.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/ML-20365-image-1.png)

**Title:**
Chart showing Nemotron 3 Nano in the most attractive quadrant in Artificial Analysis Openness vs Intelligence Index (Source:
[Artificial Analysis](https://artificialanalysis.ai/evaluations/artificial-analysis-openness-index?models=gpt-oss-20b%2Cllama-4-scout%2Cmagistral-small-2509%2Cdeepseek-r1-qwen3-8b%2Cnvidia-nemotron-nano-12b-v2-vl-reasoning%2Cnvidia-nemotron-nano-9b-v2-reasoning%2Cnvidia-nemotron-3-nano-30b-a3b-reasoning%2Cqwen3-30b-a3b-2507-reasoning%2Cqwen3-vl-32b-reasoning%2Colmo-3-32b-think"%20\l%20"artificial-analysis-openness-index-vs-artificial-analysis-intelligence-index)
)

As shown in the following image, Nemotron 3 Nano provides leading accuracy with the highest efficiency among the open models and scores an impressive 52 points, a significant jump over the previous Nemotron 2 Nano model. Token demand is increasing due to agentic AI, so the ability to ‘think fast’ (arrive at the correct answer quickly while using fewer tokens) is critical. Nemotron 3 Nano delivers high throughput with its efficient Hybrid Transformer-Mamba and MoE architecture.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/ML-20365-image-2.png)

**Title:**
NVIDIA Nemotron 3 Nano provides highest efficiency with leading accuracy among open models with an impressive 52 points score on Artificial Analysis Intelligence vs. Output Speed Index. (Source:
[Artificial Analysis](https://artificialanalysis.ai/models?models=gpt-oss-20b%2Cllama-4-scout%2Cmagistral-small-2509%2Cdeepseek-r1-qwen3-8b%2Cnvidia-nemotron-nano-12b-v2-vl-reasoning%2Cnvidia-nemotron-nano-9b-v2-reasoning%2Cnvidia-nemotron-3-nano-30b-a3b-reasoning%2Capriel-v1-6-15b-thinker%2Cqwen3-30b-a3b-2507-reasoning%2Cqwen3-vl-32b-reasoning%2Colmo-3-32b-think&intelligence-comparison=intelligence-vs-output-speed"%20\l%20"intelligence-vs-output-speed)
)

## NVIDIA Nemotron 3 Nano use cases

Nemotron 3 Nano helps power various use cases for different industries. Some of the use cases include

* Finance – Accelerate loan processing by extracting data, analyzing income patterns, detecting fraudulent operations, reducing cycle times, and risk.
* Cybersecurity – Automatically triage vulnerabilities, perform in-depth malware analysis, and proactively hunt for security threats.
* Software development – Assist with tasks like code summarization.
* Retail – Optimize inventory management and help enhance in-store service with real-time, personalized product recommendations and support.

## Get started with NVIDIA Nemotron 3 Nano in Amazon Bedrock

To test NVIDIA Nemotron 3 Nano in Amazon Bedrock, complete the following steps:

1. Navigate to the
   [**Amazon Bedrock console**](https://us-west-2.console.aws.amazon.com/bedrock/home?region=us-west-2#modelaccess&trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
   and select
   **Chat/Text playground**
   from the left menu (under the
   **Test**
   section).
2. Choose
   **Select model**
   in the upper-left corner of the playground.
3. Choose
   **NVIDIA**
   from the category list, then select
   **NVIDIA Nemotron 3 Nano**
   .
4. Choose
   **Apply**
   to load the model.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/ML-20365-image-3.png)

After selection, you can test the model immediately. Let’s use the following prompt to generate a unit test in Python code using the
`pytest`
framework:

`Write a pytest unit test suite for a Python function called calculate_mortgage(principal, rate, years). Include test cases for: 1) A standard 30-year fixed loan 2) An edge case with 0% interest 3) Error handling for negative input values.`

Complex tasks like this prompt can benefit from a chain of thought approach to help produce a precise result based on the reasoning capabilities built natively into the model.

![](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20365/ML-20365-image-4.gif)

### Using the AWS CLI and SDKs

You can access the model programmatically using the model ID
*nvidia.nemotron-nano-3-30b*
. The model supports both the
`InvokeModel`
and
`Converse`
APIs through the
[AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
and
[AWS SDK](https://aws.amazon.com/developer/tools/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
with
*nvidia.nemotron-nano-3-30b*
as the model ID. Further, it supports the Amazon Bedrock OpenAI SDK compatible API.

Run the following command to invoke the model directly from your terminal using the
[**AWS Command Line Interface (AWS CLI) and the InvokeModel API**](https://aws.amazon.com/cli/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
:

```
aws bedrock-runtime invoke-model \
 --model-id nvidia.nemotron-nano-3-30b \
 --region us-west-2 \
 --body '{"messages": [{"role": "user", "content": "Type_Your_Prompt_Here"}], "max_tokens": 512, "temperature": 0.5, "top_p": 0.9}' \
 --cli-binary-format raw-in-base64-out \
invoke-model-output.txt
```

To invoke the model through the AWS SDK for Python (boto3)
**,**
use the following script to send a prompt to the model, in this case by using the Converse API:

```
import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-west-2")

# Set the model ID
model_id = "nvidia.nemotron-nano-3-30b"

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

To invoke the model through the Amazon Bedrock OpenAI-compatible
`ChatCompletions`
endpoint, you can do so by using the OpenAI SDK:

```
# Import OpenAI SDK
from openai import OpenAI

# Set environment variables
os.environ["OPENAI_API_KEY"] = "<insert your bedrock API key>"
os.environ["OPENAI_BASE_URL"] = "https://bedrock-runtime.<AWS region>.amazon.com/openai/v1"

# Set the model ID
model_id = "nvidia.nemotron-nano-3-30b"

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

### Use NVIDIA Nemotron 3 Nano with Amazon Bedrock features

You can enhance your generative AI applications by combining Nemotron 3 Nano with the Amazon Bedrock managed tools. Use
[Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
to implement safeguards and
[Amazon Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
to create robust Retrieval Augmented Generation (RAG) workflows.

### Amazon Bedrock guardrails

Guardrails is a managed safety layer that helps enforce responsible AI by filtering harmful content, redacting sensitive information (PII), and blocking specific topics across prompts and responses. It works across multiple models to help detect prompt injection attacks and hallucinations.

**Example use case:**
If you’re building a mortgage assistant, you can help prevent it from offering general investment advice. By configuring a filter for the word “stocks”, user prompts containing that term can be immediately blocked and receive a custom message.

To set up a guardrail, complete the following steps:

1. In the
   **Amazon Bedrock console**
   , navigate to the
   **Build**
   section on the left and select
   **Guardrails**
   .
2. Create a new guardrail and configure the necessary filters for your use case.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/09/ML-20365-image-5.png)

After configured, test the guardrail with various prompts to verify its performance. You can then fine-tune settings, such as denied topics, word filters, and PII redaction, to match your specific safety requirements. For a deep dive, see
[Create your guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-components.html)
.

### Amazon Bedrock Knowledge Bases

Amazon Bedrock Knowledge Bases automates the complete RAG workflow. It handles ingesting content from your data sources, chunking it into searchable segments, converting them into vector embeddings, and storing them in a vector database. Then, when a user submits a query, the system matches the input against stored vectors to find semantically similar content, which is then used to augment the prompt sent to the foundation model.

For this example, we uploaded PDFs (for example,
[Buying a New Home,](https://www.huduser.gov/portal/sites/default/files/pdf/100-Q-A-About-Buying-a-New-Home.pdf)
[Home Loan Toolkit, Shopping for a Mortgage](https://files.consumerfinance.gov/f/documents/cfpb_shopping_for_a_mortgage.pdf)
) to Amazon Simple Storage Service (Amazon S3) and selected Amazon OpenSearch Serverless as the vector store. The following code demonstrates how to query this knowledge base using the
[RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html)
API, while automatically facilitating safety compliance alignment through a specific Guardrail ID.

```
import boto3
bedrock_agent_runtime_client = boto3.client('bedrock-agent-runtime')
response = bedrock_agent_runtime_client.retrieve_and_generate(
    input={
        'text': 'I am interested in purchasing a home. What steps should I take to make sure I am prepared to take on a mortgage?'
    },
    retrieveAndGenerateConfiguration={
        'knowledgeBaseConfiguration': {
            'generationConfiguration': {
                'guardrailConfiguration': {
                    'guardrailId': '<INSERT GUARDRAIL ID>',
                    'guardrailVersion': '1'
                }
            },
            'knowledgeBaseId': '<INSERT KNOWLEDGE BASE ID>',
            'modelArn': 'arn:aws:bedrock:us-east-1::foundation-model/nvidia.nemotron-nano-3-30b',
            "generationConfiguration": {
                "promptTemplate": {
                    "textPromptTemplate": (
                        "You are a helpful assistant that answers questions about mortgages"
                        "search results.\n\n"
                        "Search results:\n$search_results$\n\n"
                        "User query:\n$query$\n\n"
                        "Answer clearly and concisely."
                    )
                },
            },
            "orchestrationConfiguration": {
                "promptTemplate": {
                    "textPromptTemplate": (
                        "You are very knowledgeable on mortgages"
                        "Conversation so far:\n$conversation_history$\n\n"
                        "User query:\n$query$\n\n"
                        "$output_format_instructions$"
                    )
                }
            }
        },
        'type': 'KNOWLEDGE_BASE'
    }
)
print(response)
```

It directs the NVIDIA Nemotron 3 Nano model to synthesize the retrieved documents into a clear, grounded answer using your custom prompt template. To set up your own pipeline, review the full walkthrough in the
[Amazon Bedrock User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html)
.

## Conclusion

In this post, we showed you how to get started with NVIDIA Nemotron 3 Nano on Amazon Bedrock for fully managed serverless inference. We also showed you how to use the model with Amazon Bedrock Knowledge Bases and Amazon Bedrock Guardrails. The model is now available in the US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Tokyo), Asia Pacific (Mumbai), South America (Sao Paulo), Europe (London), and Europe (Milan) AWS Regions. Check the
[full Region list](https://docs.aws.amazon.com/bedrock/latest/userguide/models-regions.html?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
for future updates. To learn more, check out
[NVIDIA Nemotron](https://developer.nvidia.com/nemotron)
and give NVIDIA Nemotron 3 Nano a try in the
[Amazon Bedrock console](https://console.aws.amazon.com/bedrock?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
today.

---

## About the authors

### Antonio Rodriguez

Antonio Rodriguez is a Principal Generative AI Specialist Solutions Architect at Amazon Web Services. He helps companies of different sizes solve their challenges, embrace innovation, and create new business opportunities with Amazon Bedrock. Apart from work, he loves to spend time with his family and play sports with his friends.

### Aris Tsakpinis

Aris Tsakpinis is a Senior Specialist Solutions Architect for Generative AI focusing on open weight models on Amazon Bedrock and the broader generative AI open-source environment. Alongside his professional role, he is pursuing a PhD in Machine Learning Engineering at the University of Regensburg, where his research focuses on applied generative AI in scientific domains.

### Abdullahi Olaoye

Abdullahi Olaoye is a Senior AI Solutions Architect at NVIDIA, specializing in integrating NVIDIA AI libraries, frameworks, and products with cloud AI services and open-source tools to optimize AI model deployment, inference, and generative AI workflows. He collaborates with cloud providers to help enhance AI workload performance and drive adoption of NVIDIA-powered AI and generative AI solutions.

### Curtice Lockhart

Curtice Lockhart is an AI Solutions Architect at NVIDIA, where he helps customers deploy language and vision models to build end-to-end AI workflows using NVIDIA’s tooling on AWS. He enjoys making complex AI concepts feel approachable and spending his time exploring the art, music, and being outdoors.

### Nirmal Kumar Juluru

Nirmal Kumar Juluru is a product marketing manager at NVIDIA driving the adoption of Nemotron and NeMo. He previously worked as a software developer. Nirmal holds an MBA from Carnegie Mellon University and a bachelors in computer science from BITS Pilani.