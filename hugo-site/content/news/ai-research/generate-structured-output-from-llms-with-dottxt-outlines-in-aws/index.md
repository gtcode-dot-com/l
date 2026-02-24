---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-24T20:15:35.140353+00:00'
exported_at: '2026-02-24T20:15:38.110872+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/generate-structured-output-from-llms-with-dottxt-outlines-in-aws
structured_data:
  about: []
  author: ''
  description: This post explores the implementation of Dottxt’s Outlines framework
    as a practical approach to implementing structured outputs using AWS Marketplace
    in Amazon SageMaker.
  headline: Generate structured output from LLMs with Dottxt Outlines in AWS
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/generate-structured-output-from-llms-with-dottxt-outlines-in-aws
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Generate structured output from LLMs with Dottxt Outlines in AWS
updated_at: '2026-02-24T20:15:35.140353+00:00'
url_hash: fdfdf8bf0307d6739d8a70a1336bfe5fa6a105f0
---

*This post is cowritten with Remi Louf, CEO and technical founder of Dottxt.*

Structured output in AI applications refers to AI-generated responses conforming to formats that are predefined, validated, and often strictly entered. This can include the schema for the output, or ways specific fields in the output should be mapped. Structured outputs are essential for applications that require consistency, validation, and seamless integration with downstream systems. For example, banking loan approval systems must generate JSON outputs with strict field validation, healthcare systems need to validate patient data formats and enforce medication dosage constraints, and ecommerce systems require standardized invoice generation for their accounting systems.

This post explores the implementation of
[.txt](https://dottxt.ai/)
’s
[Outlines framework](https://github.com/dottxt-ai/outlines)
as a practical approach to implementing structured outputs using
[AWS Marketplace](https://aws.amazon.com/marketplace/)
in
[Amazon SageMaker](https://aws.amazon.com/sagemaker/)
.

## Structured output: Use cases and business value

Structured outputs elevate generative AI from ad hoc text generation to dependable business infrastructure, enabling precise data exchange, automated decisioning, and end-to-end workflows across high‑stakes, integration-heavy environments. By enforcing schemas and predictable formats, they unlock use-cases where accuracy, traceability, and interoperability are non-negotiable, from financial reporting and healthcare operations to ecommerce logistics and enterprise workflow automation. This section explores where structured outputs create the most value and how they translate directly into reduced errors, lower operational risk, and measurable ROI.

### What is structured output?

The category
*structured output*
combines multiple types of requirements for how models should produce outputs that follow specific constraints mechanisms. The following are examples of constraint mechanisms.

* **Schema-based constraints:**
  JSON Schema and XML Schema define object structures with type requirements, required fields, property constraints, and nested hierarchies. Models generate outputs matching these specifications exactly, helping to ensure that fields like
  `transaction_id`
  (string),
  `amount`
  (float), and
  `timestamp`
  (datetime) are present and correctly entered.
* **Enumeration constraints:**
  Enum expressions restrict outputs to predefined categorical values. Classification tasks use
  `enum`
  to force models to select from fixed options—such as categorizing instruments as
  *Percussion*
  ,
  *String*
  ,
  *Woodwind*
  ,
  *Brass*
  , or
  *Keyboard*
  —removing arbitrary category generation.
* **Pattern-based constraints:**
  Regular expressions validate specific formats such as email addresses, phone numbers, dates, or custom identifiers. Regex patterns make sure outputs match required structures without post-processing validation.
* **Grammar-based constraints:**
  Context-free grammars (CFGs) and EBNF notation define syntactic rules for generating code, SQL queries, configuration files, or domain-specific languages. Constrained decoding frameworks enforce these rules at token generation time.
* **Semantic validation:**
  Beyond syntactic constraints, large language models (LLMs) can validate outputs against natural language criteria—helping to ensure that content is
  *professional*
  ,
  *family-friendly*
  , or
  *constructive*
  —addressing subjective requirements that rule-based validation can’t capture.

### Critical components that benefit from structured output

In modern applications, AI models are integrated with non-AI types of processing and business systems. These integrations and junction points require consistency, type safety, and machine readability, because parsing ambiguities or format deviations would break workflows. Here are some of the common architectural patterns where we see critical interoperability between LLMs and infrastructure components:

* **API integration and data pipelines:**
  Extract, transform, and load (ETL) processes and REST APIs require strict format compliance. Mistakes in the output of the model can create parsing errors and compromise direct database insertion or seamless transformation logic.
* **Tool calling and function execution:**
  Agentic workflows depend on the ability of the LLM model to invoke functions with correctly typed parameters, enabling multi-step automation where each agent consumes validated inputs.
* **Document extraction and data capture:**
  Parsing invoices, contracts, or medical records requires the model to semantically identify the desired entities and return them in a format that can truly automate data entry by extracting vendor names, amounts, and dates into predefined schemas, including specific categorization options among others.
* **Real-time decision systems:**
  Systems that require sub-50 millisecond decisions, such as fraud detection and transaction processing, can’t afford verbosity or retries on the structure of the output. Producing reliable and conformed risk scores, classification flags, and decision metadata mean that downstream systems can consume data instantly.

### Business applications: Where structured output provides the most value

Across high-stakes, integration-heavy domains, structured outputs transform generative models from flexible text engines into reliable business infrastructure that delivers predictability, auditability, and end‑to‑end automation.

* **Financial services and transaction processing:**
  In financial institutions, structured outputs facilitate precision and consistency across reporting, auditing, and regulatory compliance. Transaction data, risk assessments, and portfolio analytics must adhere to predefined schemas to support real-time reconciliation, anti-money laundering (AML) reviews, and regulatory filings. Structured outputs enable seamless exchange among payment systems, risk engines, and audit tools—reducing manual oversight while maintaining full traceability and data integrity across high-stakes financial operations.
* **Healthcare and clinical operations:**
  Regulatory compliance demands strict validation—range checking for vital signs, medication dosages, and lab results helps prevent critical errors. Structured extraction from medical documents enables automated coding, billing accuracy, and audit trail creation for HIPAA compliance.
* **Enterprise workflow automation:**
  Legacy systems require machine-readable data without custom parsing logic. Structured outputs from customer support interactions generate case summaries with sentiment scores, action items, and routing metadata that integrate directly into customer relationship management (CRM) systems.
* **Ecommerce and logistics:**
  Address validation, payment verification, and order attribute consistency reduce failed deliveries and fraudulent transactions. Structured outputs coordinate multi-party workflows where carriers, warehouses, and payment processors require standardized formats.
* **Regulatory compliance and audit readiness:**
  Industries facing strict oversight benefit from structured content management with immutable audit trails. Component-level repositories track every change with metadata (who, when, why, approver), so that auditors can verify compliance through direct system access rather than manual document review.

The common thread is operational complexity, integration requirements, and risk sensitivity. Structured outputs transform AI from text generation into reliable business infrastructure where predictability, auditability, and system interoperability drive measurable ROI through reduced errors, faster processing, and seamless automation.

## Introducing .txt Outlines on AWS to produce structured outputs

Structured output can be achieved in several ways. Most frameworks will, at the core, focus on
*validation*
to identify if the output adheres to the rules and requirements requested. If the output doesn’t conform, the framework will request a new output, and keep iterating as such until the model achieves the requested output structure.

Outlines offers an advanced approach called
*generation-time validation*
, meaning that the validation happens as the model is producing tokens, which shifts validation to early in the generation process instead of validating after completion. While not integrated with
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
, understanding Outlines provides insight into cutting-edge structured output techniques that inform hybrid implementation strategies.

[Outlines](https://github.com/outlines-dev/outlines)
, developed by the
[.txt](https://dottxt.ai/)
team, is a Python library designed to bring deterministic structure and reliability to language model outputs—addressing a key challenge in deploying LLMs for production applications. Unlike traditional free-form generation, developers can use Outlines to enforce strict output formats and constraints during generation, not just after the fact. This approach makes it possible to use LLMs for tasks where accuracy, predictability, and integration with downstream systems are required.

### How Outlines works

Outlines enforces constraints through three main mechanisms:

* **Grammar compilation:**
  Converts schemas into token masks that guide the model’s choices
* **Prefix trees:**
  Prunes invalid paths during beam search to maintain valid structure
* **Sampling control:**
  Uses finite automata for valid token selection during generation

During generation, Outlines follows a precise workflow:

1. The language model processes the input sequence and produces token logits
2. The Outlines logits processor sets the probability of illegal tokens to 0%
3. A token is sampled only from the set of legal tokens according to the defined structure
4. This process repeats until generation is complete, helping to ensure that the output conforms to the required format

For example, with a pattern like
`^\d*(\.\d+)?$`
for decimal numbers, Outlines converts this into an automaton that only allows valid numeric sequences to be generated. If
*748*
has been generated, the system knows the only valid next tokens are another digit, a decimal point, or the end of sequence token.

#### Performance benefits

Enforcing structured output during generation offers significant advantages for reliability and performance in production environments. It helps to increase the validity of the output’s structure and can significantly improve performance:

* **Zero inference overhead:**
  The structured generation technique adds virtually no computational cost during inference
* **5 times faster generation:**
  According to .txt Engineering’s
  *coalescence*
  approach, structured generation can be dramatically faster than standard generation
* **Reduced computational resources:**
  Constraints simplify model decision-making by removing invalid paths, reducing overall processing requirements
* **Improved accuracy:**
  By narrowing the output space, even base models can achieve higher precision on structured tasks

#### Benchmark advantages

Here are some of the proven benefits of the Outlines library:

* 2 times faster than regex-based validation pipelines
* 98% schema adherence compared to 76% for post-generation validation
* Supports complex constraints like recursive JSON schemas

### Getting started with Outlines

Outlines can be seamlessly integrated into existing Python workflows:

```
from pydantic import BaseModel

# Define your data structure
class Patient(BaseModel):
    id: int
    name: str
    diagnosis: str
    age: int

# Load model and create structured generator
model = models.transformers("microsoft/DialoGPT-medium")
generator = generate.json(model, Patient)

# Generate structured output
prompt = "Create a patient record for John Smith, 45, with diabetes"
result = generator(prompt)  # Returns valid Patient instance
print(result.name)  # "John Smith"
print(result.age)   # 45
```

For more complex schemas:

```
from enum import Enum

class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    PENDING = "pending"

class User(BaseModel):
    username: str
    email: str
    status: Status
    created_at: datetime

# Generator enforces enum values and datetime format
user_generator = generate.json(model, User)
```

#### Using .txt’s dotjson in Amazon SageMaker

You can directly deploy .txt’s
[Amazon SageMaker real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
solution for generating structured output by deploying one of .txt’s models such as DeepSeek-R1-Distill-Qwen-32B through
[AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-mb7desoblqh2w)
. The following code assumes that you have already deployed an endpoint in your AWS account.

A Jupyter Notebook that walks through deploying the endpoint end-to-end is available in the
[product repository](https://github.com/dottxt-ai/aws-examples/blob/main/dotjson-deepseek-r1-distill-qwen-32b/sample_notebook.ipynb)
.

```
import json
import boto3
# Set this based on your SageMaker endpoint
endpoint_name = "dotjson-with-DeepSeek-R1-Distill-Qwen-32B"
session = boto3.Session()
structured_data = {
    "patient_id": 12345,
    "first": "John",
    "last": "Adams",
    "appointment_date": "2025-01-27",
    "notes": "Patient presented with a headache and sore throat",
}
payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful, honest, and concise assistant.",
        },
        {
            "role": "user",
            "content": f"Create a medical record from the following visit data: {structured_data}",
        },
    ],
    "response_format": {
        "type": "json_schema",
        "json_schema": {
            "name": "Medical Record",
            "schema": {
                "properties": {
                    "patient_id": {"title": "Patient Id", "type": "integer"},
                    "date": {"title": "Date", "type": "string", "format": "date-time"},
                    "diagnosis": {"title": "Diagnosis", "type": "string"},
                    "treatment": {"title": "Treatment", "type": "string"},
                },
                "required": ["patient_id", "diagnosis", "treatment"],
                "title": "MedicalRecord",
                "type": "object",
            },
        },
        "max_tokens": 1000,
    },
}
runtime = session.client("sagemaker-runtime")
response = runtime.invoke_endpoint(
    EndpointName=endpoint_name,
    ContentType="application/json",
    Accept="application/json",
    Body=json.dumps(payload).encode(),
)
body = json.loads(response["Body"].read().decode("utf-8"))
# View the structured output produced by the model
msg = body["choices"][0]["message"]
content = msg["content"]
medical_record = json.loads(content)
medical_record
```

This hybrid approach removes the need for retries compared to validation after completion.

## Alternative structured output options on AWS

While Outlines offers generation-time consistency, several other approaches provide structured outputs with different trade-offs:

### Alternative 1: LLM-based structured output strategies

When using most modern LLMs, such as Amazon Nova, users can define output schemas directly in prompts, supporting type constraints, enumerations, and structured templates within the AWS environment. The
[following guide](https://docs.aws.amazon.com/nova/latest/userguide/prompting-structured-output.html)
shows different prompting patterns for Amazon Nova.

```
# Example Nova structured output
import boto3

bedrock = boto3.client('bedrock-runtime')

response = bedrock.invoke_model(
    modelId='amazon.nova-pro-v1:0',
    body=json.dumps({
        "messages": [{"role": "user", "content": "Extract customer info from this text..."}],
        "inferenceConfig": {"maxTokens": 500},
        "toolConfig": {
            "tools": [{
                "toolSpec": {
                    "name": "extract_customer",
                    "inputSchema": {
                        "json": {
                            "type": "object",
                            "properties": {
                                "name": {"type": "string"},
                                "email": {"type": "string"},
                                "phone": {"type": "string"}
                            },
                            "required": ["name", "email"]
                        }
                    }
                }
            }]
        }
    })
)
```

### Alternative 2: Post-generation validation OSS frameworks

Post-generation validation open-source frameworks have emerged as a critical layer in modern generative AI systems, providing structured, repeatable mechanisms to evaluate and govern model outputs before they are consumed by users or downstream applications. By separating generation from validation, these frameworks enable teams to enforce safety, quality, and policy constraints without constantly retraining or fine-tuning underlying models.

#### LMQL

[Language Models Query Language (LMQL)](https://lmql.ai/)
has a SQL-like interface and provides a query language for LLMs, so that developers can specify constraints, type requirements, and value ranges directly in prompts. Particularly effective for multiple-choice and type constraints.

#### Instructor

[Instructor](https://python.useinstructor.com/)
provides retry mechanisms by wrapping LLM outputs with schema validation and automatic retry mechanisms. Tight integration with
[Pydantic](https://pydantic-docs.helpmanual.io/)
models makes it suitable for scenarios where post-generation validation and correction are acceptable.

```
import boto3
import instructor
from pydantic import BaseModel
# Create a Bedrock client for runtime interactions
bedrock_client = boto3.client('bedrock-runtime')
# Set up the instructor client with Bedrock runtime
client = instructor.from_bedrock(bedrock_client)
# Define the structured response model
class User(BaseModel):
    name: str
    age: int
# Invoke the Claude Haiku model with the correct message structure
user = client.chat.completions.create(
    modelId="global.anthropic.claude-haiku-4-5-20251001-v1:0",
    messages=[
        {"role": "user", "content": [{"text": "Extract: Jason is 25 years old"}]},
    ],
    response_model=User,
)
print(user)
# Expected output:
# User “name='Jason' age=25”
```

#### Guidance

[Guidance](https://github.com/guidance-ai/llguidance)
offers fine-grained template-driven control over output structure and formatting, allowing token-level constraints. Useful for consistent response formatting and conversational flows.

## Decision factors and best practices

Selecting the right structured output approach depends on several key factors that directly impact implementation complexity and system performance.

* **Latency considerations:**
  Response time requirements significantly influence structured output solutions. By adding retry mechanisms, post-generation validation can add latency. In comparison, approaches like Outlines are optimal for latency-sensitive applications. Enforcing schemas adds some processing time compared to the base model used but is still much faster than post-generation strategies.
* **Retry capabilities:**
  Automatic regeneration capabilities (like those in Instructor) are essential for structured outputs because they provide fallback mechanisms when initial generation attempts fail to meet schema requirements, improving overall reliability without developer intervention.
* **Streaming support:**
  Partial JSON validation during streaming enables progressive content delivery while maintaining structural integrity, vital for responsive user experiences in applications requiring real-time structured data.
* **Input complexity:**
  Context trimming techniques optimize handling of complex inputs, helping to ensure that lengthy or intricate prompts don’t compromise the structured nature of outputs or exceed token limitations.
* **Deployment strategy:**
  While the ability to access models through the Amazon Bedrock API (
  [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
  ,
  [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
  ) offers a serverless solution, Outlines is currently only available through AWS Marketplace on Amazon SageMaker, requiring you to deploy and host the model.
* **Model selection:**
  The choice of model significantly impacts structured output quality and efficiency. Base models might require extensive prompt engineering for structure compliance, while specialized models with built-in structured output capabilities offer higher reliability and reduced post-processing needs.
* **User experience**
  : Each option provides pros and cons.
  + **In-process validation (Outlines)**
    catches errors early during generation, increasing speed when mistakes are made by the model but also increasing latency when model output was already correct.
  + **Post-generation validation**
    provides comprehensive quality control but requires error handling for non-adherent outputs.
* **Performance:**
  While implementing structured outputs
  [can increase the model accuracy by reducing hallucinations and improving output](https://blog.dottxt.ai/performance-gsm8k.html)
  consistency, some of these gains can come with tradeoffs such as a reduction of reasoning capabilities in some scenarios or introduction of additional token overhead.

## Conclusion

Organizations can use the structured output paradigm in AI to reliably enforce schemas, integrate with a wide range of models and APIs, and balance post-generation validation versus direct generation methods for greater control and consistency. By understanding the trade-offs in performance, integration complexity, and schema enforcement, builders can tailor solutions to their technical and business requirements, facilitating scalable and efficient automation across diverse applications.

To learn more about implementing structured outputs with LLMs on AWS:

---

### **About the Authors**

### Clement Perrot

**Clement Perrot**
is a Senior GenAI Strategist in the GenAI Innovation Center, where he helps early-stage startups build and use AI on the AWS platform. Prior to AWS, Clement was an entrepreneur, whose last two AI and consumer hardware startups were acquired.

### Remi Louf

**Remi Louf**
is the CEO and technical founder of Dottxt. Before founding dottxt, Remi was a Senior Research Engineer at Normal Computing, a Research Engineer at Ampersand, an early Research Engineer at Hugging Face, a Research Fellow at Harvard and Chief Science Officer at Vimies. Remi has a Doctorate in Statistical Physics, Masters in the Philosophy of Physics, Undergraduate degree in fundamental Physics and a Eleve Normalien (French research degree) in Quantum Physics.

### Max Elfrink

**Max Elfrink**
is an Account Manager on the AWS Startup’s Team, where he helps early-stage startups build, scale and grow their AI + Infrastructure on AWS. Prior to AWS, Max worked in startups for 6 years Supporting early stage startups in CDN, HCLS Tech, and Unicorn Tech-Enabled Freight Forwarder, Flexport.