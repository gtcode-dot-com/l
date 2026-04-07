---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-07T23:37:04.770321+00:00'
exported_at: '2026-04-07T23:37:07.037029+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-tool-calling-with-serverless-model-customization-in-amazon-sagemaker-ai
structured_data:
  about: []
  author: ''
  description: In this post, we walk through how we fine-tuned Qwen 2.5 7B Instruct
    for tool calling using RLVR. We cover dataset preparation across three distinct
    agent behaviors, reward function design with tiered scoring, training configuration
    and results interpretation, evaluation on held-out data with unseen tools, and
    deplo...
  headline: Accelerate agentic tool calling with serverless model customization in
    Amazon SageMaker AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/accelerate-agentic-tool-calling-with-serverless-model-customization-in-amazon-sagemaker-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Accelerate agentic tool calling with serverless model customization in Amazon
  SageMaker AI
updated_at: '2026-04-07T23:37:04.770321+00:00'
url_hash: a2d6d2422d8354978d80a6ba62932b1207a2d840
---

Agentic tool calling is what makes AI agents useful in production. It’s how they query databases, trigger workflows, retrieve real-time data, and act on a user’s behalf. But base models frequently hallucinate tools, pass bad parameters, and attempt actions when they should ask for clarification. These failures erode trust and block production deployment.

You can use
[Serverless model customization](https://aws.amazon.com/sagemaker/ai/model-customization/)
in Amazon SageMaker AI to fix these problems without managing infrastructure. With Reinforcement Learning with Verifiable Rewards (RLVR), the model generates its own candidate responses, receives a reward signal indicating quality, and updates its behavior to favor what works. You select a model, configure a technique, point to your data and reward function, and SageMaker AI handles the rest. In this post, we walk through how we fine-tuned Qwen 2.5 7B Instruct for tool calling using RLVR. We cover dataset preparation across three distinct agent behaviors, reward function design with tiered scoring, training configuration and results interpretation, evaluation on held-out data with unseen tools, and deployment. By the end, our fine-tuned model improved tool call reward by 57% over the base model on scenarios that it didn’t see during training.

Because tool calling has a naturally verifiable objective, whether the model called the right function with the right parameters, it maps well to RLVR. The challenge with self-managed reinforcement learning (RL) is the operational overhead. GPU procurement, memory orchestration between rollout and training phases, reward infrastructure, and checkpointing add up quickly. Hyperparameter sensitivity adds another layer of complexity. SageMaker AI takes on that work so you can focus on your model, your data, and your reward function.

SageMaker AI supports model families including
[Amazon Nova](https://aws.amazon.com/nova/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
,
[GPT-OSS](https://aws.amazon.com/bedrock/openai/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
,
[Llama](https://aws.amazon.com/bedrock/meta/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
,
[Qwen](https://aws.amazon.com/bedrock/qwen/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)
, and
[DeepSeek, with techniques including Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), RLVR, and Reinforcement Learning from AI Feedback (RLAIF). Training and validation metrics are tracked through integrated MLflow.](https://aws.amazon.com/bedrock/deepseek/?trk=769a1a2b-8c19-4976-9c45-b6b1226c7d20&sc_channel=el)

## Why RLVR for tool calling

SFT requires labeled examples of each behavior that you want the model to learn. For tool calling, that means examples of calling a tool, asking for clarification, and refusing. But tool calling also requires the model to decide between those behaviors, and SFT can struggle to generalize that decision-making beyond the specific patterns in its training data.

RLVR works differently. For each prompt, the model generates multiple candidate responses (we use eight). A reward function verifies which ones are correct. The model then updates its policy to favor what worked, using Group Relative Policy Optimization (GRPO). GRPO compares each candidate’s reward score against the mean score of the group and reinforces responses that score above average. Over time, the model learns the format of a tool call and when to call compared to when to ask.

## Prerequisites

To use serverless model customization in SageMaker AI, you must have the following prerequisites:

## Fine-tune Qwen 2.5 7B Instruct in SageMaker AI

To get started, we open Amazon SageMaker AI Studio and choose
**Models**
in the left navigation pane to browse the foundation models (FM) that are available for customization.

![Amazon SageMaker Studio Models page showing featured foundation models from Amazon, Meta, and Qwen with a Customize model dropdown menu expanded, revealing options to Customize with UI, AI Agent (Preview), and Code.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image1.jpg)

In the
**Customize model**
menu, select
**Qwen 2.5 7B Instruct**
, and choose
**Customize with UI**
. This opens the customization configuration page where you select your technique, point to your training data and reward function, and configure hyperparameters. We selected
**Reinforcement Learning from Verifiable Rewards (RLVR)**
as our customization technique.

![Amazon SageMaker Studio model customization form for Qwen2.5-7B-Instruct showing the Customization technique dropdown with Reinforcement Learning with Verifiable Rewards (RLVR) selected, along with options for reward functions, dataset upload, S3 output location, and batch size.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image2.jpg)

## Prepare your training data

A tool calling dataset needs to teach more than correct API invocations. Production agents face three distinct situations:

1. The user provides enough information, and the model should call a tool.
2. The user’s request is missing required parameters, and the model should ask for clarification.
3. The request is harmful or out of scope, and the model should refuse.

We generated 1,500 synthetic training examples from our tool schemas (weather, flights, translation, currency conversion, statistics) using
[Kiro](https://kiro.dev/)
, the Amazon AI-powered IDE, to produce prompts with realistic variation in phrasing and specificity across the three behaviors. Here’s an example of the prompt we used:

`Generate 1,500 JSONL training examples for RLVR tool-calling`

`fine-tuning across 5 tool schemas: get_weather_forecast,`

`search_flights, translate_text, currency_convert, and`

`get_statistics.`

`Each line must follow this format:`

`{"prompt": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}], "reward_model": {"ground_truth": "..."}}`

`Distribute examples across three behaviors:`

`1. Execute (60%): User provides all required params → ground_truth is the tool call JSON`

`2. Clarify (25%): User is missing required params → ground_truth is a clarifying question`

`3. Refuse (15%): Request is harmful or out of scope → ground_truth is a polite refusal`

`Vary phrasing between formal, casual, and terse.`

`Output valid JSONL only, no commentary.`

This is a practical path for teams that don’t yet have production logs to draw from. For organizations already running agentic workflows, real user prompts and tool calls from production will yield even higher-quality training data.

Each training example contains a prompt (a system instruction and user request) and a ground truth in the
`reward_model`
field that the reward function scores against. Here are examples of each behavior.

**Execute**
when the user provides everything the tool needs:

```
{
  "prompt": [
    {"role": "system", "content": "You are a helpful assistant. When using tools, respond with: [...]"},
    {"role": "user", "content": "Get weather for San Francisco"}
  ],
  "reward_model": {
    "ground_truth": "[{"name": "get_weather_forecast", "arguments": {"city": "San Francisco"}}]"
  }
}
```

Clarify when a required parameter is missing:

```
{
  "prompt": [
    {"role": "system", "content": "You are a helpful assistant. When using tools, respond with: [...]"},
    {"role": "user", "content": "Get the weather"}
  ],
  "reward_model": {
    "ground_truth": "To provide you with the weather information, could you please specify the location?"
  }
}
```

**Execute with multiple parameters:**

```
{
  "prompt": [
    {"role": "system", "content": "You are a helpful assistant. When using tools, respond with: [...]"},
    {"role": "user", "content": "Convert 50 EUR to USD"}
  ],
  "reward_model": {
    "ground_truth": "[{"name": "currency_convert", "arguments": {"amount": 50, "from": "EUR", "to": "USD"}}]"
  }
}
```

Notice the difference between “Get weather for San Francisco” (tool call) and “Get the weather” (clarification). This is the kind of distinction GRPO learns well. For each prompt, the model generates eight candidates, the reward function scores them, and the scores are averaged across the group. Candidates above the mean get reinforced, and over time the model picks up when to call and when to ask.

## Define your reward function

The reward function defines what
*correct*
means for our use case. We write it as a Python function that receives the model’s response and the ground truth from the training data and returns a numerical score. Ours extracts tool calls from the model’s response, parses them as JSON, and compares against the ground truth.

The full function handles response extraction, flexible parsing for alternative formats during early training, and edge cases around JSON type mismatches. Here is the core scoring logic:

```
# After extracting and parsing tool calls from model response and ground truth:

# Compare tool names
pred_names = {tool.get('name', '') for tool in pred_tools}
gt_names = {tool.get('name', '') for tool in gt_tools}

if pred_names == gt_names:
    # Right function(s) - check if arguments also match
    perfect_match = True
    for pred_tool in pred_tools:
        for gt_tool in gt_tools:
            if pred_tool.get('name') == gt_tool.get('name'):
                if pred_tool.get('arguments') != gt_tool.get('arguments'):
                    perfect_match = False
    score = 1.0 if perfect_match else 0.5
elif pred_names & gt_names:
    # Partial overlap in function names
    score = 0.5
else:
    # Wrong function entirely
    score = 0.0
```

The three tiers (1.0, 0.5, and 0.0) give GRPO a richer learning signal. If several of the eight candidates get the function right but miss a parameter, the 0.5 score distinguishes them from completely wrong answers. This helps the model recognize that it’s on the right track.

For clarification and refusal cases where the ground truth is natural language (no
`TOOLCALL`
tags), the reward function checks whether the model also avoided calling a tool. An unnecessary API call when the model should have asked a question earns 0.0.

## Configure and launch training

On the customization configuration page, we point to our training dataset and reward function, then set our hyperparameters. We use a batch size of 128, learning rate of 5e-6, 3 epochs, and 8 rollouts per prompt.

The rollouts setting is the core GRPO mechanism. For each training prompt, the model generates eight different responses, the reward function scores each one, and responses that score above the group average get reinforced. Training and validation metrics are logged to MLflow. In this example, training takes approximately 40 minutes.

## Training results

![Performance dashboard displaying five RLVR training metric charts: Train Reward Statistics trending upward from 0.28 to 0.70, Train Episode Length Distribution fluctuating between 30 and 35, Policy Entropy declining from 0.19 to 0.12, Gradient Norm decreasing from 0.10 to near 0.00, and Mean Advantage Estimate recovering from -0.08 to near 0.00 over 30 training steps. Long description: Screenshot of a dark-themed](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image3.jpg)

**Train Reward Statistics**
(top left) is the chart to focus on. The mean reward across the roll outs started around 0.28 and climbed to 0.65–0.68 over 30 steps, more than doubling. The steepest gains happen in the first 10 steps as the model learns the basic tool calling format and decision structure. It then flattens after step 20 as it converges.

The other charts confirm healthy training:

* **Policy Entropy**
  decreases, meaning the model is getting more confident rather than guessing.
* **Gradient Norm**
  stabilizes, meaning updates are getting smaller and more refined.
* **Mean Advantage Estimate**
  converges toward zero, indicating that the model’s policy is stabilizing and the average response quality is aligning with the reward baseline.

## Evaluate the fine-tuned model

After the training job is complete, you can see the models that you created in the
**My Models**
tab. To expand the details, choose
**View details**
on one of your models.

![Amazon SageMaker Studio My Models page showing the Logged tab with two fine-tuned model cards: example-name-2lt4op at version v3 and example-name-2lt4o with no versions found, both created 4 days ago with View details buttons.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image4.jpg)

You can choose
**Continue customization**
to iterate further by adjusting hyperparameters or training with a different technique. Choose
**Evaluate**
to compare your customized model against the base model.

We evaluate on a separate test set of 300 examples that were excluded from training. The evaluation dataset covers the same three behaviors but includes tools, phrasings, and scenarios that the model hasn’t seen. It tests
`search_restaurants`
,
`get_stock_price`
, and
`calculate_standard_deviation`
, none of which appeared during training. It also includes refusal cases for harmful requests like generating violent content or creating malware, testing whether the model generalizes safe behavior to new threats.

The evaluation runs standard NLP metrics alongside our custom reward function against the held-out set.

![Evaluation metrics comparison table showing the custom RLVR-trained model outperforming the base model across all metrics: Rouge1 (65.21% vs 49.48%), Rouge2 (51.45% vs 35.12%), RougeL (59.19% vs 45.78%), Em (21% vs 11%), F1 (56.63% vs 42.19%), F1 Score Quasi (64.60% vs 45.98%), Bleu (100.00 vs 92.58), Tool Call Reward (0.55 vs 0.35), and Aggregate Reward Score (0.55 vs 0.35), evaluated on 300 documents.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image5.jpg)

**Tool Call Reward**
is our custom metric and the most direct measure of what we trained for. It jumped from 0.35 to 0.55, a 57% improvement. In practical terms, this means that the fine-tuned model makes the correct tool calling decision significantly more often. It calls the right function with the right parameters when it should, asks for clarification when information is missing, and refuses when appropriate.

**F1 Score Quasi**
,
**Rouge1**
, and
**RougeL**
all improved by 14–19 percentage points, reflecting better generation of correct function names, parameter keys, and values across the board.

**Exact Match**
doubled from 11% to 21%. This metric requires character-for-character output matching, so even small formatting differences count as a miss. The 21% exact match alongside 64.6% F1 suggests that the model often gets the semantics right even when surface formatting differs slightly.

These results are all on held-out data with tools and scenarios that the model didn’t see during training. The improvements carry over to new tools, which means the model picked up general tool calling patterns rather than memorizing the training set.

Here are responses from the fine-tuned model on prompts that it didn’t see during training:

**Tool execution:**

>
**Prompt:**
“What’s the stock price of AMZN?” > >
**Model response:**
`[{"name": "get_stock_price", "arguments": {"ticker": "AMZN"}}]`

**Clarification:**

>
**Prompt:**
“Find me a restaurant nearby” > >
**Model response:**
“I’d be happy to help you find a restaurant! Could you please provide the cuisine type or location you’re interested in?”

**Near-miss:**

>
**Prompt:**
“What’s the standard deviation of 10, 20, 30, 40, 50?” > >
**Model response:**
`[{"name": "calculate_standard_deviation", "arguments": {"numbers": "10, 20, 30, 40, 50"}}]`

In the near-miss case, the model selected the correct tool but passed the numbers as a string instead of an array. This earns a 0.5 reward score (right function, wrong parameter format) and represents the kind of error that you’d target in the next iteration through additional training data or reward function refinement.

## Deploy the fine-tuned model

With evaluation confirming improvement, deploy the fine-tuned model directly from the model details page. Choose
**Deploy,**
and select your deployment target: either a SageMaker AI endpoint or
[Amazon Bedrock.](https://www.google.com/aclk?sa=L&ai=DChsSEwi0sMCD8ruTAxVnmO4BHVqSGRQYACICCAEQABoCZHo&ae=2&aspm=1&co=1&ase=2&gclid=EAIaIQobChMItLDAg_K7kwMVZ5juAR1akhkUEAAYASAAEgJyFvD_BwE&cid=CAAS0gHkaHk9acJbNFSSXpMUXdE2beaMDCoiGkr7lC-s5YsahS9peDNTCcJPQWzvKZ4Gtcd-0HhG5G2NlS15o--Qg8o6bDZ7IKhObAtN0fjP8sOk1ZL5diDnb1T1gdh0LKN4hmKSzNWEMI9rW0yWL1p5TI6fKEoBzWY1GA6uaGLRm_tn8dO14dbjesBF3CPnjEKvIl2BB3aLQlJMpM5Fg2rs0SWZV1faTLWypUh83p7uSz4gC6KT3nmNrb6jlDFse1Rs4flaJ1kOsD1CIs9w5vAczf4gDSU&cce=2&category=acrcp_v1_35&sig=AOD64_0yuTA0kVAGgZDUJzKKwFqiDbBKSA&q&nis=4&adurl&ved=2ahUKEwiygrqD8ruTAxVaMDQIHc9ABdMQ0Qx6BAgfEAE)
You can also download the model weights from Amazon S3 for self-managed deployment.

![Amazon SageMaker Studio training details page for an RLVR Tool Calling model (v1) based on Qwen2.5-7B-Instruct, showing completed training status with RLVR customization technique, a Deploy dropdown menu with SageMaker AI and Bedrock options, and hyperparameters including batch size 128, max epochs 3, and learning rate 0.000005.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/30/ml-20015-image6.jpg)

## Conclusion

In this post, we fine-tuned Qwen 2.5 7B Instruct for agentic tool calling using RLVR and GRPO through serverless model customization in Amazon SageMaker AI. We prepared a dataset spanning three tool-calling behaviors (execute, clarify, refuse), defined a tiered reward function, trained the model in about 40 minutes, evaluated on held-out data with unseen tools and scenarios, and deployed. The fine-tuned model improved tool call reward by 57% over the base model.

To push accuracy further, you can expand your training data with additional tools, edge cases, and multi-turn conversations to cover more of the scenarios that your agents encounter in production. You can also refine your reward function to penalize specific failure modes, like the string-vs-array parameter issue shown in the previous section, or add partial credit for other near-miss patterns. If you’re running agentic workflows, your production logs are a high-quality source of training data that can make the model even more effective for your specific use case. Beyond tool calling, RLVR applies to other reasoning tasks where correctness is verifiable, such as multi-step planning, structured data extraction, or code generation.

While this post walks through the UI workflow, an
[SDK for programmatic access](https://sagemaker.readthedocs.io/en/stable/model_customization/index.html)
is also available. To learn more, see the
[SageMaker AI model customization documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/customize-model.html)
.

To get started, try serverless AI model customization in Amazon SageMaker AI with your own use cases.

---

## About the authors

### Lauren Mullennex

[Lauren](https://www.linkedin.com/in/laurenmull/)
is a Senior GenAI/ML Specialist Solutions Architect at AWS. She has over a decade of experience in ML, DevOps, and infrastructure. She is a published author of a book on computer vision. Outside of work, you can find her traveling and hiking with her two dogs.

### Eric Saleh

[Eric](https://www.linkedin.com/in/eric-saleh/)
is a Senior GenAI Specialist at AWS, focusing on foundation model training and inference. He is partnering with top foundation model builders and AWS service teams to enable distributed training and inference at scale on AWS and lead joint GTM motions with strategic customers. Before joining AWS, Eric led product teams building enterprise AI/ML solutions, which included frontier GenAI services for fine-tuning, RAG, and managed inference. He holds a master’s degree in Business Analytics from UCLA Anderson.

### Surya Kari

[Surya](https://www.linkedin.com/in/suryakari/)
is a Senior Generative AI Data Scientist at AWS, specializing in developing solutions leveraging state-of-the-art foundation models. He has extensive experience working with advanced language models including DeepSeek-R1, the LLama family, and Qwen, focusing on their fine-tuning and optimization for specific scientific applications. His expertise extends to implementing efficient training pipelines and deployment strategies using AWS SageMaker, enabling the scaling of foundation models from development to production. He collaborates with customers to design and implement generative AI solutions, helping them navigate model selection, fine-tuning approaches, and deployment strategies to achieve optimal performance for their specific use cases.