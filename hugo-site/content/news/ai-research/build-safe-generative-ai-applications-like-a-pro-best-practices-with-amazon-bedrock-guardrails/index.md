---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T19:52:18.771007+00:00'
exported_at: '2026-03-03T19:52:22.249601+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails
structured_data:
  about: []
  author: ''
  description: In this post, we will show you how to configure Amazon Bedrock Guardrails
    for efficient performance, implement best practices to protect your applications,
    and monitor your deployment effectively to maintain the right balance between
    safety and user experience.
  headline: 'Build safe generative AI applications like a Pro: Best Practices with
    Amazon Bedrock Guardrails'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Build safe generative AI applications like a Pro: Best Practices with Amazon
  Bedrock Guardrails'
updated_at: '2026-03-03T19:52:18.771007+00:00'
url_hash: 86539bacefcfd7a70b64a9ce7c323f13aaac71b5
---

Are you struggling to balance generative AI safety with accuracy, performance, and costs? Many organizations face this challenge when deploying generative AI applications to production. A guardrail that’s too strict blocks legitimate user requests, which frustrates customers. One that’s too lenient exposes your application to harmful content, prompt attacks, or unintended data exposure. Finding the right balance requires more than just enabling features; it demands thoughtful configuration and nearly continuous refinement.

[Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
gives you powerful tools for implementing responsible AI safeguards: content filtering for both text and images (including prompt attack prevention), topic classification, sensitive information protection, contextual grounding checks, and automated reasoning checks. In this post, we will show you how to configure these capabilities for more efficient performance, implement best practices to protect your applications, and monitor your deployment effectively to maintain the right balance between safety and user experience.

Let’s explore the strategies that will help you deploy guardrails confidently in production.

## Best practices for using Amazon Bedrock Guardrails

For the maximum benefit from Amazon Bedrock Guardrails, we recommend that you adopt the following best practices.

### 1. Select the right guardrail policies

The choice of which guardrail policies to use in production workflows depends on your specific use case, but several foundational policies provide protection suitable for most implementations.

**Content Policy**
blocks harmful content across hate speech, insults, sexual content, violence, and misconduct, helping you maintain content safety in applications. We recommend this for all production deployments.

Beyond text content, you can extend the content filters for images to apply the same content moderation policies to both text and images in your generative AI applications. This multimodal capability helps block harmful visual content across all six content filter categories: Hate, Insults, Sexual, Violence, Misconduct, and Prompt Attacks. When configuring content filters, you can choose to apply filtering to text only, images only, or both modalities.

**Prompt Attack Prevention**
can help identify potential jailbreak attempts, prompt injection attacks, and prompt leakage attacks that might seek to weaken safety features and developer instructions. This policy is recommended for maintaining application security.

**Sensitive Information Policy**
offers masking or removal capabilities for personally identifiable information (PII), which can help you protect customer data and support your compliance efforts.

**Word Policy**
blocks specific words or phrases, commonly used to filter profanity, industry-specific restricted terms, or custom vocabulary restrictions.

**Topic Policy**
helps you enforce custom Responsible AI (RAI) policies, maintain compliance with organizational guidelines, and control conversation scope and subject matter.

For specialized use cases, you can add
**Contextual Grounding**
to help validate whether responses are supported by trusted reference materials, help reduce model hallucinations during content summarization, and help maintain conversation relevance. You can use the
**Automated Reasoning Policy**
to enforce compliance with regulatory requirements, validate outputs against specific business rules, and implement sophisticated filtering beyond keyword matching.

Start with base policies that align with your core security and compliance requirements, then add specialized policies based on specific use case needs. Regular review and adjustment of your policies can help improve protection while helping to maintain desired functionality.

#### 1.1 Choose the correct safeguard tier

Guardrails currently provides two safeguard tiers for content policy, prompt attack prevention, and topic policy:
**classic tier**
and
**standard tier**
. For most use cases, standard tier is the better choice. It offers greater robustness, better accuracy, broader language support, higher quotas, and improved availability by directing traffic across AWS Regions based on load. For more information, see
[Safeguard tiers for guardrails policies](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-tiers.html)
.

#### **1.2. Use Guardrails detect mode to test out your guardrail’s behavior without impact**

Before letting your guardrail intervene on production applications, you can test its behavior on live customer traffic using guardrails detect mode. With this mode, guardrails will evaluate all content and report what was identified in the trace response but will not take any blocking action. Through detect mode, you can see how your guardrail performs on real traffic and update configurations as necessary. After you’re satisfied with the behavior, you can update your guardrail to Block or Mask content as appropriate. For more information, see
[Options for handling harmful content detected by Amazon Bedrock Guardrails.](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-harmful-content-handling-options.html#guardrails-harmful-content-handling-options-examples)

### 2. Configure content policy filter strength

Amazon Bedrock Guardrails content policy offers four filter strength levels to help you balance content safety with application functionality: NONE, LOW, MEDIUM, and HIGH. The different filter strengths reflect the confidence of guardrails that the input contains harmful content. If you configure a guardrail with LOW filter strength, then the guardrail will block requests where it has high confidence that the input is harmful. Analogously, if the guardrail is configured with HIGH filter strength, then the guardrail will block even inputs where it has low confidence. For example, a request containing subtle innuendos might pass through a LOW filter strength but would be blocked by a HIGH filter strength setting.

|  |  |
| --- | --- |
| **Filter strength** | **Blocks content with confidence** |
| NONE | No filtering |
| LOW | HIGH confidence only |
| MEDIUM | HIGH and MEDIUM confidence |
| HIGH | HIGH, MEDIUM, and LOW confidence |

#### 2.1 Recommended filter strength selection process

1. Initial configuration
   1. Start with HIGH filter strength to establish maximum protection.
2. Evaluation
   1. Test your implementation using representative sample traffic (expected user’s traffic) to:
      1. Identify false positive rate
      2. Assess impact on legitimate content
      3. Evaluate user experience
3. Adjustment
   1. If the initial configuration produces too many false positives:
      1. Lower the filter strength to MEDIUM
      2. Re-evaluate with sample traffic
      3. Continue adjusting as needed, moving to LOW if necessary

### 3. Craft effective denied topics: golden rules

**1. Be crisp and precise.**
Define topics clearly and unambiguously, for example, “Questions or information associated with investing, selling, transacting, or procuring cryptocurrencies” rather than vague descriptions, such as “Investment advice”.

**2. Define, don’t instruct.**
Avoid command-style phrases like “Block all content associated with cryptocurrency”, and instead say “All content associated with cryptocurrency”. Focus on what the topic
*is*
, not what you want the system to
*do*
.

**3. Stay positive.**
Never define topics negatively (for example, “All content except investment advice”). Guardrails should have clear, affirmative definitions of what to detect.

**4. Focus on themes, not words.**
Denied topics capture subjects and concepts contextually—they’re not designed to catch specific names, entities, or individual words. For those use cases, use sensitive information filters or word filters instead.

**5. Provide sample phrases.**
Add a few sample phrases that represent the types of inputs you would want to get blocked by the topic filter. For a deny topic blocking investment advice, you might put “Recommend a stock that will skyrocket” or “Can you suggest where to invest my money?”.

### 4. Customizing beyond built-in filters

For some applications, the provided content filter categories or built-in PII types might not fully cover your guardrail requirements. When this happens, you have two options:

1. Create a custom deny topic: if your use case requires blocking content that falls outside the existing content filter categories, you can define a deny topic tailored to your needs. For example, if you need to block political discussion, you could create a deny topic with the definition “Any content related to politics or elections.”
2. Create a custom regex filter: if the built-in PII types don’t cover the sensitive data patterns that you need to catch, you can define a regex filter to fill the gap. For example, to block all dates in MM/DD/YYYY format, you could add the following regex pattern:
   `\b(0[1-9]|1[0-2])[\/\-](0[1-9]|[12]\d|3[01])[\/\-](19|20)\d{2}\b`

### 5. Choose the right implementation approach

Amazon Bedrock Guardrails offers multiple ways to protect your applications, each suited to different architectural patterns and control requirements. Understanding when to use each approach helps you build protection strategies that match your specific needs.

#### Standalone ApplyGuardrail API for maximum flexibility

When you need precise control over where and how guardrails will evaluate the content, you can invoke the
`ApplyGuardrail`
API at any point in your application logic. You can use
`ApplyGuardrail`
with any large language model (LLM) or LLM gateway, including models from Amazon Bedrock or outside. With this approach, you can implement guardrails at critical checkpoints: pre-processing user inputs from multiple sources, validating intermediate outputs in multi-step AI workflows, filtering retrieved documents in Retrieval Augmented Generation (RAG) pipelines, or post-processing LLM responses before delivery. For latency-sensitive applications, you can parallelize the input validation ApplyGuardrail call and the LLM inference call, then process the results together. However, this means that you will always pay for both calls—even if the guardrail would have blocked the input. With a sequential approach, you can skip the inference call entirely when the guardrail intervenes, saving that cost. You can design custom protection strategies that match your application’s specific risk profile, applying different guardrail configurations based on context, user state, or workflow stage. For more details, see
[Use the ApplyGuardrail API in your application](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-use-independent-api.html)
.

#### Native integration with Bedrock inference APIs

When you use Amazon Bedrock Guardrails with inference APIs like
`InvokeModel`
,
`InvokeModelWithResponseStream`
,
`Converse`
, or
`ConverseStream`
, the system automatically handles a dual-checkpoint pattern for you. First, it sends user input to the
`ApplyGuardrail`
API to evaluate against your defined policies. If your guardrail blocks the input, it returns your configured message, if the guardrail allows the input, it proceeds to the foundation model. After the model generates a response, the system evaluates the output (including grounding sources when applicable) through guardrails again before returning results to users. For the integration with the Amazon Bedrock streaming APIs (
`InvokeModelWithResponseStream`
and
`ConverseStream`
), the guardrail will buffer the model’s streaming output and evaluate the output in chunks. These native integrations streamline implementation while maintaining comprehensive protection. For more details, see
[Use your guardrail with inference operations to evaluate user input](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-input-tagging-base-inference.html)
.

**Important**
: Each
`ApplyGuardrail`
API call incurs separate charges, so consider your architecture carefully. The pricing for Amazon Bedrock Guardrails is based on text units consumed or images processed per configured safeguard. For more information, see the
[Amazon Bedrock pricing page](https://aws.amazon.com/bedrock/pricing/)
for details.

### 6. Manage guardrails in multi-turn conversations

One of the most common pitfalls in conversational AI is over-applying guardrails to conversation history. If you evaluate every message from the entire chat history on each turn, a single blocked topic early in the conversation can prevent users from moving forward. This can happen even when their new questions are perfectly valid.

```
Imagine this scenario with a guardrail configured to block discussions about "bananas":
User: Do you sell bananas?
Chatbot: Sorry, the model cannot respond to your question.
User: Can I book a flight?
```

If your guardrails evaluate the entire conversation history, that second question gets blocked too—simply because “bananas” still exists somewhere in the chat log. Your user is now stuck, unable to recover from a single misstep.

Instead of checking the full conversation history, configure your guardrails to evaluate only the most recent user input or a limited number of recent turns. This approach allows conversations to flow naturally and lets users recover from blocked interactions. Furthermore, you can reduce both cost and latency by not having the guardrail evaluate the same content multiple times across different turns.If guardrails only evaluated the last turn (in this case “Can I book a flight?”), then the conversation would continue smoothly and users could move past previous guardrail interventions without friction. With this strategy, you can maintain conversation fluidity and improve user experience by keeping conversations natural.

Guardrail integrations inside tools like
[LiteLLM](https://github.com/BerriAI/litellm)
,
[LangChain AWS](https://github.com/langchain-ai/langchain-aws)
, and
[Strands Agents](https://github.com/strands-agents)
either default to only evaluating the last turn in the conversation or provide a flag to do so.

#### Using the Converse API with guardContent for multi-turn conversations

The following example demonstrates how to selectively evaluate only the latest user message in a multi-turn conversation using the
`guardContent`
block. In this approach, the conversation history is passed as regular text (which won’t be evaluated by guardrails), while only the most recent user input is wrapped in
`guardContent`
:

```
import boto3
bedrock = boto3.client("bedrock-runtime", region_name="<aws region>")

# Conversation history (previous messages won't be evaluated by guardrails)
messages = [
	{
			  "role": "user",
			  "content": [
				{"text": "Do you sell bananas?"}
			]
	},
	{
			  "role": "assistant",
			  "content": [
				{"text": "I'm sorry, but I can't help with that topic."}
			]
	},
	{
			  "role": "user",
              "content": [
				{ # Only this block will be evaluated by guardrails
				  "guardContent": { "text":
						{ "text": "Can I book a flight to Paris?" }
					}
				}
				]
	}
]

response = bedrock.converse(
	modelId="<bedrock_model_id>",
	guardrailConfig={
		"guardrailIdentifier": "your-guardrail-id",
		"guardrailVersion": "1",
		"trace": "enabled" },
	messages=messages
)

# The conversation flows naturally because only "Can I book a flight to Paris?" is evaluated, not the earlier blocked topic about bananas
print(response['output']['message']['content'][0]['text'])
```

In this example, even though the conversation history contains a previously blocked topic (“bananas”), the user can continue the conversation naturally because only the latest query wrapped in
`guardContent`
is evaluated by the guardrail. The optimal number of turns to evaluate can vary based on your use case and safety requirements, as some attacks can span across several conversation turns. Consider starting with a single-turn evaluation and adjust based on your application’s needs.

### 7. Use guardrail numerical versions in production

When you create a guardrail, Amazon Bedrock automatically creates a single version labeled as DRAFT. You can create additional numerical versions (version 1 and version 2) of the guardrail by using the
`CreateGuardrailVersion`
API. The version numbers are auto-incremented by the service whenever a new version is created. Each numerical version is an immutable snapshot of the DRAFT guardrail version’s policies at the time of creation. Any modifications to the policies in the DRAFT version do not affect existing numerical versions. We strongly recommend using numerical versions instead of the DRAFT version in production applications. The DRAFT version is designed for development and testing purposes, and using it in production can lead to the following issues:

* **Service interruptions**
  – When an operator modifies the DRAFT version using the
  `UpdateGuardrail`
  API, the guardrail enters an UPDATING state. During this period, any inference calls using the DRAFT guardrail will receive a
  `ValidationException`
  saying that the guardrail is not in a READY state.
* **Inconsistent protection**
  – Changes made to the DRAFT version’s settings can immediately affect your production application, potentially compromising your intended protection controls.

To use a numerical version in an
`ApplyGuardrail`
call, set the value of the
`guardrailVersion`
field to be the version number:

`response = bedrock.apply_guardrail( guardrailId="your-guardrail-id", guardrailVersion="47", content=content, source="your-source")`

By using numerical versions in production, you can help maintain more consistent and predictable behavior of your guardrails while preserving the flexibility to test and iterate on new policies in the DRAFT version. For more information about guardrail versions, see
[Create a version of a guardrail](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-versions-create.html)
.

## **Conclusion**

Implementing Amazon Bedrock Guardrails effectively requires thoughtful configuration and a deep understanding of your application’s unique risk profile. By selecting the right policies and safeguard tiers, tuning the configurations through iterative testing, choosing the implementation approach that fits your architecture, and safely deploying with a numerical version, you can balance safety, cost, and user experience. Treat your guardrails as a living system—start with strong baselines, test with detect mode on real traffic, and adjust as your application evolves. Following these battle-tested practices will help your generative AI applications remain safe, performant, and ready to scale confidently into production.

To learn more about Amazon Bedrock Guardrails, refer to the
[Amazon Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
, explore
[safeguard tiers for tailored responsible AI](https://aws.amazon.com/blogs/machine-learning/tailor-responsible-ai-with-new-safeguard-tiers-in-amazon-bedrock-guardrails/)
, or visit the Amazon Bedrock console to create your first production-ready guardrail.

---

### About the Authors

### Daniel Khain

**Daniel Khain**
is a Software Engineer at AWS AI, where he has worked on Amazon Bedrock AgentCore Gateway, Amazon Bedrock Guardrails, and Amazon Lex. Outside of work, Daniel likes to kayak, cross-country ski, and play classical guitar.

### Bharathi Srinivasan

**Bharathi Srinivasan**
is a Generative AI Data Scientist at the AWS Worldwide Specialist Organization. She works on developing solutions for Responsible AI, focusing on algorithmic fairness, veracity of large language models, explainability and governance of agents. Bharathi guides internal teams and AWS customers on their responsible AI journey. She has presented her work at various learning conferences.

### Shyam Srinivasan

**Shyam Srinivasan**
is on the Amazon Bedrock Guardrails product team. He cares about making the world a better place through technology and loves being part of this journey. In his spare time, Shyam likes to run long distances, travel around the world, and experience new cultures with family and friends.

### Antonio Rodriguez

**Antonio Rodriguez**
is a Principal Generative AI Specialist Solutions Architect at AWS. He helps companies of all sizes solve their challenges, embrace innovation, and create new business opportunities with Amazon Bedrock. Apart from work, he loves to spend time with his family and play sports with his friends.