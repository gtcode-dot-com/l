---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:03:53.646750+00:00'
exported_at: '2026-04-02T04:03:57.346371+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/reinforcement-fine-tuning-on-amazon-bedrock-with-openai-compatible-apis-a-technical-walkthrough
structured_data:
  about: []
  author: ''
  description: 'In this post, we walk through the end-to-end workflow of using RFT
    on Amazon Bedrock with OpenAI-compatible APIs: from setting up authentication,
    to deploying a Lambda-based reward function, to kicking off a training job and
    running on-demand inference on your fine-tuned model.'
  headline: 'Reinforcement fine-tuning on Amazon Bedrock with OpenAI-Compatible APIs:
    a technical walkthrough'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/reinforcement-fine-tuning-on-amazon-bedrock-with-openai-compatible-apis-a-technical-walkthrough
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Reinforcement fine-tuning on Amazon Bedrock with OpenAI-Compatible APIs: a
  technical walkthrough'
updated_at: '2026-04-02T04:03:53.646750+00:00'
url_hash: 8e6435bd13f188178a91b557d7f6f7486ad154fe
---

In December 2025, we
[announced](https://aws.amazon.com/blogs/aws/improve-model-accuracy-with-reinforcement-fine-tuning-in-amazon-bedrock/)
the availability of Reinforcement fine-tuning (RFT) on
[Amazon Bedrock](https://aws.amazon.com/bedrock/?trk=7ecf60df-6136-414c-a7c3-6aa4d2d6019f&sc_channel=ps&ef_id=CjwKCAiAnoXNBhAZEiwAnItcG_quu7odGWcZPLfH1XE3QJu1ybzUZZ6RDd9R5rmqzjyIE5KnOvhfKxoCTtwQAvD_BwE:G:s&s_kwcid=AL!4422!3!795877020842!e!!g!!amazon%20bedrock!23532472972!194311072004&gad_campaignid=23532472972&gbraid=0AAAAADjHtp8BzKFnYuFMrdXAUbbzIgUDa&gclid=CjwKCAiAnoXNBhAZEiwAnItcG_quu7odGWcZPLfH1XE3QJu1ybzUZZ6RDd9R5rmqzjyIE5KnOvhfKxoCTtwQAvD_BwE)
starting with support for Nova models. This was followed by
[extended support](https://aws.amazon.com/about-aws/whats-new/2026/02/amazon-bedrock-reinforcement-fine-tuning-openai/)
for Open weight models such as OpenAI GPT OSS 20B and Qwen 3 32B in February 2026. RFT in Amazon Bedrock automates the end-to-end customization workflow. This allows the models to learn from feedback on multiple possible responses using a small set of prompts, rather than traditional large training datasets.

In this post, we walk through the end-to-end workflow of using RFT on Amazon Bedrock with OpenAI-compatible APIs: from setting up authentication, to deploying a Lambda-based reward function, to kicking off a training job and running on-demand inference on your fine-tuned model. Here, we use the
[GSM8K math dataset](https://huggingface.co/datasets/openai/gsm8k)
as our working example and target OpenAI’s gpt-oss-20B model hosted on Bedrock.

## **How reinforcement fine-tuning works**

Reinforcement Fine-Tuning (RFT) represents a shift in how we customize large language models (LLMs). Unlike traditional supervised fine-tuning (SFT), which requires models to learn from static I/O pairs, RFT enables models to learn through an iterative feedback loop where they generate responses, receive evaluations, and continuously improve their decision-making capabilities.

### **The core concept: learning from feedback**

At its heart, reinforcement learning is about teaching an agent (in this case, an LLM) to make better decisions by providing feedback on its actions. Think of it like training a chess player. Instead of showing them every possible move in every possible situation (which is impossible), you let them play and tell them which moves led to winning positions. Over time, the player learns to recognize patterns and make strategic decisions that lead to success. For LLMs, the model generates multiple possible responses to a given prompt, receives scores (rewards) for each response based on how well they meet your criteria, and learns to favor the patterns and strategies that produce higher-scoring outputs.

### **Key components of RFT**

Key RFT components include the agent/actor (policy) model, input states to the model, output actions from the model, and the reward function as shown in the following diagram:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/ml-20593-image-1.png)

The actor model is the foundation model (FM) that you’re customizing. In Amazon Bedrock RFT, this could be Amazon Nova, Llama, Qwen, or other
[supported models](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html#rft-supported-models)
. The state is the current context, including the prompt, conversation history (for multi-turn interactions), and the relevant metadata. The action is the model’s response to a prompt. The reward function assigns a numerical score to a (state, action) pair, evaluating the
*goodness*
of a model response for a given state. In doing so, the reward function can use additional information like ground truth responses or unit tests for code generation. This is the critical feedback signal that drives learning. Higher rewards indicate better responses.

One of RFT’s key advantages is that the model learns from responses it generates during training, not only from pre-collected examples. This approach unlocks several compounding benefits. Because the model actively explores novel approaches and learns from the results, it can adapt in real time: as it improves, it naturally encounters new scenarios that push it further. This also makes the process far more efficient, alleviating the need to pre-generate and label thousands of examples upfront. The result is a system capable of continuous improvement, growing stronger as it encounters an ever-more-diverse range of situations. This online learning capability is what enables RFT to achieve superior performance on complex tasks like code generation, mathematical reasoning, and multi-turn conversations. For verifiable tasks like math, this is especially effective because correctness checking is fully automatic – avoiding the need for human labeling.

**How Amazon Bedrock RFT works**

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/ml-20593-image-2.png)

Amazon Bedrock RFT is built to make reinforcement fine-tuning practical at the enterprise level. It handles the heavy lifting, so teams can focus on the problem that they’re solving rather than the infrastructure underneath it. The entire RFT pipeline runs automatically. For each prompt in your training dataset, Amazon Bedrock generates multiple candidate responses from your actor model, managing batching, parallelization, and resource allocation behind the scenes. Reward computation scales just as seamlessly. Whether you’re using verifiable rewards or an LLM-as-Judge setup, Amazon Bedrock orchestrates evaluation across thousands of prompt-response pairs while handling concurrency and error recovery without manual intervention. Policy optimization runs on GRPO, a state-of-the-art reinforcement learning algorithm, with built-in convergence detection so training stops when it should. Throughout the process, Amazon CloudWatch metrics and the Amazon Bedrock console give you real-time visibility into reward trends, policy updates, and overall model performance, so you can know where training stands. The workflow starts from your development environment (VS Code, Terminal, Jupyter, or SageMaker AI notebook) using the standard OpenAI SDK pointed at Bedrock’s Mantle endpoint. From there:

1. **Upload training data**
   via the Files API (
   *.jsonl*
   format with messages and reference answers)
2. **Deploy a reward function**
   as an AWS Lambda that scores model-generated responses
3. **Create the fine-tuning job**
   — Bedrock’s GRPO engine generates responses, sends them to your Lambda grader, and updates weights based on reward scores
4. **Monitor training**
   via events and checkpoints
5. **Invoke your fine-tuned model**
   on-demand — no endpoint provisioning, no hosting.

Your data doesn’t leave the secure environment of AWS during the process, and isn’t used to train models provided by Amazon Bedrock. Here, we walk you through a specific use case of training a OpenAI GPT-OSS model with the GSM8K dataset. For more details, see the
[Bedrock RFT User Guide](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html)
.

## **Prerequisites**

Before you can get started, you need:

* An AWS account with Amazon Bedrock access in a supported AWS Region
* A
  [Bedrock API key](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)
  (short-term or long-term). You can also authenticate using AWS Sigv4 credentials but in this walkthrough we use an Amazon Bedrock API Key. For more information, see
  [Access and security for open-weight models](https://docs.aws.amazon.com/bedrock/latest/userguide/rft-open-weight-access-security.html)
  in the Amazon Bedrock User Guide.
* IAM roles for Lambda execution and Amazon Bedrock fine-tuning
* Python with openai, boto3, and
  `aws-bedrock-token-generator`
  installed. If you’re working on a shell inside a venv, or with a Jupter notebook, you can do:

```
pip install openai boto3 aws-bedrock-token-generator
```

## **Step 1: Configure the OpenAI client**

Point the standard OpenAI SDK at your Amazon Bedrock Mantle endpoint. Authentication uses an
`AmazonBedrock`
API key generated through the
`aws-bedrock-token-generator`
library:

```
from openai import OpenAI
from aws_bedrock_token_generator import provide_token

AWS_REGION = "us-west-2"
MANTLE_ENDPOINT = f"https://bedrock-mantle.{AWS_REGION}.api.aws"

client = OpenAI(
    base_url=f"{MANTLE_ENDPOINT}/v1",
    api_key=provide_token(region=AWS_REGION),
)
```

That’s it. Every subsequent call uses the standard OpenAI SDK interface! Note: We recommend using and refreshing short-term Amazon bedrock keys as needed rather than setting and using long term ones that don’t expire.

## **Step 2: Prepare and upload training data**

Each record in the dataset requires a messages field and can optionally include a
`reference_answer`
field. The
*messages*
field contains the prompt presented to the model, formatted using the OpenAI message standard where each message specifies a role (such as “user”) and corresponding content. The optional
`reference_answer`
field provides supplementary context for reward computation, such as a ground-truth answer, evaluation rule, or scoring dimensions used by the reward function.

For GSM8K examples, each training sample contains a mathematical word problem in the user message and a reference answer containing the correct numerical solution. The prompt instructs the model to provide its reasoning within structured tags and present the final answer in a
`\boxed{}`
format that the reward function can reliably extract, as in the following example:

```
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "A chat between a curious User and an artificial intelligence Bot.
         The Bot gives helpful, detailed, and polite answers to the User's questions.
         The Bot first thinks about the reasoning process and then provides the User with the answer.
         The reasoning process and answer are enclosed within <|begin_internal_thought|> <|end_internal_thought|>
         and <|begin_of_solution|> <|end_of_solution|> respectively. The final answer must be enclosed
         in \\boxed{} within the solution block.\n\nNatalia sold clips to 48 of her friends in April, and then
         she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?"
        }
      ]
    }
  ],
  "reference_answer": {
    "answer": "72"
  },
  "data_source": "gsm8k_nova"
}
```

We provide a helper function to convert the raw GSM8K records to JSONL format compatible with Amazon Bedrock RFT in this
[GitHub repository](https://github.com/aws-samples/amazon-bedrock-samples/blob/main/custom-models/bedrock-reinforcement-fine-tuning/helpers/preprocess_gsm8k.py)
.

Note that the
`data_source`
field makes sure that the appropriate reward function is applied during training while the structured prompt formats align the outputs with the reward function’s extraction logic.

As previously mentioned, the training data is a JSONL file where each line contains a conversation with messages and a reference answer. For GSM8K, this looks like:

```
{
  "messages": [
    {"role": "user", "content": "Janet's ducks lay 16 eggs per day. She eats three for breakfast and bakes muffins with four. She sells the rest at $2 each. How much does she make daily? Let's think step by step and output the final answer after '####'."}
  ],
  "reference_answer": "#### 18"
}
```

You can use additional fields here that might be useful for your grader Lambda function in the step we see later, but note that the messages structure and
`reference_answer`
are mandatory.

We can then upload our prepared dataset via the Files API:

```
with open("rft_train_data.jsonl", "rb") as f:
    file_response = client.files.create(file=f, purpose="fine-tune")

training_file_id = file_response.id
print(f"Training file uploaded: {training_file_id}")
```

## **Step 3: Deploy a Lambda reward function**

The reward function is the core of RFT. It receives model-generated responses and returns a score. For math problems, this is straightforward: extract the answer and compare it to ground truth.

Here is the reward function used in this walkthrough (from the
[sample repository](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/custom-models/bedrock-reinforcement-fine-tuning)
):

```
def lambda_handler(event, context):
    trajectories = event if isinstance(event, list) else event.get("trajectories", [])
    scores = []

    for trajectory in trajectories:
        trajectory_id = trajectory.get("id", "no-id")

        # Get the model's response from the last assistant message
        response = ""
        for msg in reversed(trajectory.get("messages", [])):
            if msg.get("role") == "assistant":
                response = msg.get("content", "")
                break

        # Extract ground truth from reference answer
        reference_answer = trajectory.get("reference_answer", {})
        reference_text = reference_answer.get("text", "")
        gt_match = re.findall(r"#### (\-?[0-9\.\,]+)", reference_text)
        ground_truth = gt_match[-1].replace(",", "") if gt_match else ""

        # Score: 1.0 if correct, 0.0 otherwise
        result = compute_score(
            trajectory_id=trajectory_id,
            solution_str=response,
            ground_truth=ground_truth,
        )
        scores.append(asdict(result))

    return scores
```

The function returns a list of
`RewardOutput`
objects, each containing an
`aggregate_reward_score`
between 0 and 1. Deploy this as an AWS Lambda function with a 5-minute timeout and 512 MB memory. Note that you can completely customize what happens inside this reward Lambda function to suit your use case. Amazon Bedrock also supports
**model-as-a-judge**
graders for subjective tasks where automated verification isn’t possible. For more information about setting up reward functions, see
[Setting up reward functions for open-weight models](https://docs.aws.amazon.com/bedrock/latest/userguide/reward-functions-open-weight.html)
.

## **Step 4: Create the fine-tuning job**

Now we use the following single API call to start the job:

```
job_response = client.fine_tuning.jobs.create(
    model="openai.gpt-oss-20b",
    training_file=training_file_id,
    extra_body={
        "method": {
            "type": "reinforcement",
            "reinforcement": {
                "grader": {
                    "type": "lambda",
                    "lambda": {
                        "function": lambda_arn # Replace with reward function Arn
                    }
                },
                "hyperparameters": {
                    "n_epochs": 1,
                    "batch_size": 4,
                    "learning_rate_multiplier": 1.0
                }
            }
        }
    }
)

job_id = job_response.id
```

Notice that the create call for the previous fine-tuning job uses the following hyperparameters:

|  |  |
| --- | --- |
| **Parameter** | **Description** |
| `n_epochs` | Number of full passes through the training data. Start with 1. |
| `batch_size` | Prompts per training step. Larger = more stable updates. |
| `learning_rate_multiplier` | We recommend using a value <1.0 for stability. |

## **Step 5: Monitor training**

To track progress of the job, we use the list events API as follows:

```
events = client.fine_tuning.jobs.list_events( fine_tuning_job_id=job_id, limit=100)
```

For a GPT-OSS example job that uses the GSM8K data subset, the training runs for a total of 67 steps with various events being emitted as the training job progresses. Here’s a timeline of these steps:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/ml-20593-image-3.png)

Now let’s dissect one of these events during training progress:

```
{
      "id": "ftevent-c3c14785-4a3b-4dab-99a5-a15aeb6c0742",
      "created_at": 1771442218,
      "level": "info",
      "message": "Step 4/67: training metrics",
      "object": "fine_tuning.job.event",
      "data": {
        "total_steps": 67,
        "actor_grad_norm": 0.0008667297661304474,
        "response_length_mean": 519.09375,
        "step": 4,
        "actor_pg_loss": 0.10153239965438844,
        "critic_rewards_mean": 0.4375,
        "actor_entropy": 0.6235736012458801,
        "critic_advantages_mean": 0.013622610829770563
      },
      "type": "metrics"
```

Let’s discuss what these mean:

|  |  |
| --- | --- |
| **Metric** | **Meaning** |
| **step** / **total\_steps** | Current training step / out of total |
| **critic\_rewards\_mean** | Average reward score across the batch (0.4375 means ~44% of responses got correct answers from your grader). This is the primary metric to watch — you want it trending up. |
| **actor\_pg\_loss** | Policy gradient loss. This is the objective being optimized — how much the model’s policy is being pushed toward higher-reward responses. Fluctuates naturally; no single “good” value. |
| **actor\_entropy** | How spread out the model’s token probability distribution is. Higher = more exploratory/diverse outputs. If it collapses toward 0, the model is becoming too deterministic (mode collapse). You want it to decrease gradually, not crash. |
| **actor\_grad\_norm** | Magnitude of the gradient update to the actor (the model). Large spikes can indicate training instability. Yours is very small (0.0009), which suggests stable, conservative updates. |
| **critic\_advantages\_mean** | Average advantage estimate—how much better/worse a response was compared to the critic’s baseline prediction. Near-zero (0.014) means that the critic is well-calibrated. Large positive values mean that the model is doing much better than expected; large negative means worse. |
| **response\_length\_mean** | Average token length of generated responses (519). Worth monitoring—if it grows unboundedly, the model may be gaming length for reward. |

**What to watch for during training:**

* `critic_rewards_mean`
  trending upward = model is learning
* `actor_entropy`
  collapsing to 0 = mode collapse (bad)
* `actor_grad_norm`
  spiking = instability
* `response_length_mean`
  exploding = reward hacking?

The sample code also provides an example of how to plot these metrics.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/ml-20593-image-4.png)

The reward curve shows the model improving from ~0.56 to consistently 0.85–0.97 by mid training. Response lengths also trend shorter over time, suggesting the model learned to be more concise while solving GSM8K problems correctly. Here’s List checkpoints as they are saved:

```
checkpoints = client.fine_tuning.jobs.checkpoints.list( fine_tuning_job_id=job_id)
```

## **Step 6: Run on-demand inference**

After the job succeeds, invoke your fine-tuned model directly. No endpoint provisioning, no hosting:

```
job_details = client.fine_tuning.jobs.retrieve(job_id)
fine_tuned_model = job_details.fine_tuned_model

response = client.chat.completions.create(
    model=fine_tuned_model,
    messages=[
        {"role": "user", "content": "If a train travels 120 miles in 2 hours, what is its speed in miles per hour?"}
    ],
)

print(response.choices[0].message.content)
```

You can also use the responses API to stream responses from the fine-tuned model:

```
stream = client.responses.create(
    model=fine_tuned_model,
    input=[{"role": "user", "content": "Your prompt here"}],
    stream=True,
    reasoning={"effort": "low"}
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
```

## **Conclusion**

Reinforcement fine-tuning on Amazon Bedrock brings together three things that make the end-to-end workflow practical:

1. **OpenAI SDK compatibility**
   — no new SDK to learn. Point
   `OPENAI_BASE_URL`
   and
   `OPENAI_API_KEY`
   at Bedrock and use the same
   `client.fine_tuning.jobs.create()`
   calls.
2. **Lambda-based reward functions**
   — write your scoring logic in Python, deploy as Lambda, and Amazon Bedrock handles the training loop (GRPO) for you.
3. **On-demand inference**
   — no endpoint management. Call
   `client.chat.completions.create()`
   with your fine-tuned model ID and pay per token.

The full notebook with end-to-end code for both GPT-OSS 20B and Qwen3 32B is available on GitHub:

[github.com/aws-samples/amazon-bedrock-samples/tree/main/custom-models/bedrock-reinforcement-fine-tuning](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/custom-models/bedrock-reinforcement-fine-tuning)

For more details, see the
[Amazon Bedrock Reinforcement Fine-Tuning documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/reinforcement-fine-tuning.html)
.

---

## About the authors

### Shreyas Subramanian

Shreyas Subramanian is a Principal Data Scientist and helps customers by using Generative AI and deep learning to solve their business challenges using AWS services like Amazon Bedrock and AgentCore. Dr. Subramanian contributes to cutting-edge research in deep learning, Agentic AI, foundation models and optimization techniques with several books, papers and patents to his name. In his current role at Amazon, Dr. Subramanian works with various science leaders and research teams within and outside Amazon, helping to guide customers to best leverage state-of-the-art algorithms and techniques to solve business critical problems. Outside AWS, Dr. Subramanian is a expert reviewer for AI papers and funding via organizations like Neurips, ICML, ICLR, NASA and NSF.

### Nick McCarthy

Nick McCarthy is a Senior Generative AI Specialist Solutions Architect on the Amazon Bedrock team, based out of the AWS New York office. He helps customers customize their GenAI models on AWS. He has worked with clients across a wide range of industries — including healthcare, finance, sports, telecommunications, and energy — helping them accelerate business outcomes through the use of AI and machine learning. He holds a Bachelor’s degree in Physics and a Master’s degree in Machine Learning from UCL, London.

### Shreeya sharma

Shreeya Sharma is a Senior Technical Product Manager at AWS, where she has been working on leveraging the power of generative AI to deliver innovative and customer-centric products. Shreeya holds a master’s degree from Duke University. Outside of work, she loves traveling, dancing, and singing.

### Shalendra Chhabra

Shalendra Chhabra is currently a Product leader at Bedrock. Previously, he was Head of Product Management for Amazon SageMaker Human-in-the-Loop (HIL) Services. Previously, Shalendra incubated and led Language and Conversational Intelligence for Microsoft Teams Meetings, was EIR at Amazon Alexa Techstars Startup Accelerator, VP of Product and Marketing at
[Discuss.io](http://discuss.io/)
, Head of Product and Marketing at Clipboard (acquired by Salesforce), and Lead Product Manager at Swype (acquired by Nuance). In total, Shalendra has helped build, ship, and market products that have touched more than a billion lives.