---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-24T20:15:34.723152+00:00'
exported_at: '2026-02-24T20:15:38.113908+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/train-codefu-7b-with-verl-and-ray-on-amazon-sagemaker-training-jobs
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate how to train CodeFu-7B, a specialized
    7-billion parameter model for competitive programming, using Group Relative Policy
    Optimization (GRPO) with veRL, a flexible and efficient training library for large
    language models (LLMs) that enables straightforward extension of diverse RL algorithms
    and seamless integration with existing LLM infrastructure, within a distributed
    Ray cluster managed by SageMaker training jobs. We walk through the complete implementation,
    covering data preparation, distributed training setup, and comprehensive observability,
    showcasing how this unified approach delivers both computational scale and developer
    experience for sophisticated RL training workloads.
  headline: Train CodeFu-7B with veRL and Ray on Amazon SageMaker Training jobs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/train-codefu-7b-with-verl-and-ray-on-amazon-sagemaker-training-jobs
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Train CodeFu-7B with veRL and Ray on Amazon SageMaker Training jobs
updated_at: '2026-02-24T20:15:34.723152+00:00'
url_hash: db9e186ea4c08134b11b2c87b35588fc4d5a85a4
---

The rapid advancement of artificial intelligence (AI) has created unprecedented demand for specialized models capable of complex reasoning tasks, particularly in competitive programming where models must generate functional code through algorithmic reasoning rather than pattern memorization. Reinforcement learning (RL) enables models to learn through trial and error by receiving rewards based on actual code execution, making it particularly well-suited for developing genuine problem-solving capabilities in algorithmic domains.

However, implementing distributed RL training for code generation presents significant infrastructure challenges such as orchestrating multiple heterogeneous components, coordinating parallel code compilation across nodes, and maintaining fault tolerance for long-running processes.
[Ray](https://www.ray.io/)
is one of the frameworks for distributed workloads that address these challenges, due to its unified system that handles the entire AI pipeline, GPU-first architecture, and seamless integration with tools like
[Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
and
[PyTorch](https://pytorch.org/)
.

Workloads can be run with Ray framework on SageMaker training jobs by using the
[Ray on Amazon SageMaker Training jobs](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs)
solution, which combines Ray’s distributed computing framework with SageMaker’s fully managed infrastructure. This solution automatically handles Ray cluster initialization, multi-node coordination, and distributed resource management, enabling developers to focus on model development while benefiting from SageMaker’s enterprise-grade features.

In this post, we demonstrate how to train CodeFu-7B, a specialized 7-billion parameter model for competitive programming, using
[Group Relative Policy Optimization (GRPO)](https://arxiv.org/abs/2402.03300)
with
[veRL](https://github.com/volcengine/verl)
, a flexible and efficient training library for large language models (LLMs) that enables straightforward extension of diverse RL algorithms and seamless integration with existing LLM infrastructure, within a distributed Ray cluster managed by SageMaker training jobs. We walk through the complete implementation, covering data preparation, distributed training setup, and comprehensive observability, showcasing how this unified approach delivers both computational scale and developer experience for sophisticated RL training workloads.

## About CodeFu-7B

CodeFu-7B-v0.1 is a 7B parameter language model specifically trained for solving Competitive Programming (CP) problems. Built upon the
[DeepSeek-R1-Distill-Qwen-7B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B)
base model, CodeFu demonstrates how reinforcement learning can develop capabilities in algorithmic reasoning and efficient C++ code generation beyond traditional supervised fine-tuning approaches.

The model is trained using problem statements from the DeepMind
[CodeContest dataset](https://huggingface.co/datasets/deepmind/code_contests)
without access to ground-truth solutions during training, forcing it to learn through trial and error based on code execution feedback. This approach enables the development of genuine problem-solving capabilities rather than pattern memorization

CodeFu is publicly
[available on HuggingFace](https://huggingface.co/aws-prototyping/codefu-7b-v0.1)
and released under the MIT license, making it accessible for researchers and practitioners interested in code generation and algorithmic reasoning. The model’s training methodology demonstrates the potential for applying reinforcement learning techniques to complex reasoning tasks beyond competitive programming.

## Ray in SageMaker training jobs solution

[Ray on Amazon SageMaker Training jobs](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs)
is a solution that enables distributed data processing and model training using Ray within SageMaker’s managed training environment. The solution provides key capabilities including universal launcher architecture for automatic Ray cluster setup, multi-node cluster management with intelligent coordination, heterogeneous cluster support for mixed instance types, and integrated observability through Ray Dashboard, Prometheus, Grafana, and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
integration.

The solution seamlessly integrates with the
[SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/index.html)
using the modern
[ModelTrainer](https://sagemaker.readthedocs.io/en/stable/training/index.html)
API. This publicly available
[solution on GitHub](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs)
enables developers to use Ray’s distributed computing capabilities while benefiting from SageMaker’s managed infrastructure, making it ideal for complex workloads like reinforcement learning training that require sophisticated distributed coordination and resource management.

## Solution overview

The workflow for training CodeFu 7B with veRL and Ray on SageMaker training jobs, as illustrated in the accompanying diagram, consists of the following steps:

1. **Data preparation**
   : Upload the preprocessed DeepMind CodeContest dataset and training configuration.
2. **Training job submission**
   : Submit a SageMaker training job API request through the ModelTrainer class from the SageMaker Python SDK.
3. **Monitoring and observability**
   : Monitor training progress in real-time through Ray Dashboard, and optionally with Prometheus metrics collection, Grafana visualization, and experiment tracking.
4. **Automatic cleanup**
   : Upon training completion, SageMaker automatically saves the trained model to S3, uploads training logs to CloudWatch, and decommissions the compute cluster.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-1.gif)

This streamlined architecture delivers a fully managed reinforcement learning training experience, enabling developers to focus on model development while SageMaker and Ray handle the complex distributed infrastructure orchestration—within a pay-as-you-go pricing model that bills only for actual compute time.

## Prerequisites

The following prerequisites must be complete before the notebook can be run:

1. Make the following
   [quota increase requests](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
   for SageMaker AI. For this use case, request a minimum of 2
   `p4de.24xlarge`
   instances (with 8 x NVIDIA A100 GPUs) and scale to more
   `p4de.24xlarge`
   instances (depending on time-to-train and cost-to-train trade-offs for your use case). P5 instances (with 8 x NVIDIA H100 GPUs) are also supported. On the
   [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html)
   console, request the following SageMaker AI quotas:
   1. p4de instances (
      `p4de.24xlarge`
      ) for training job usage: 2
2. Create an
   [AWS Identity and Access Management](https://aws.amazon.com/iam/)
   (IAM)
   [role](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#:~:text=the%20following%20procedures.-[%E2%80%A6]xecution%20role,-Use%20the%20following%20()
   with managed policies
   `AmazonSageMakerFullAccess`
   ,
   `AmazonS3FullAccess`
   ,
   `AmazonSSMFullAccess`
   to give required access to SageMaker AI to run the examples.
3. Assign the following policy as the
   [trust relationship](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/edit_trust.html)
   to created IAM role:

```
{
   "Version":"2012-10-17",
   "Statement":[
      {
         "Sid":"",
         "Effect":"Allow",
         "Principal":{
            "Service":
               "sagemaker.amazonaws.com"
            ]
         },
         "Action":"sts:AssumeRole"
      }
   ]
}
```

4. (Optional) Create an
   [Amazon SageMaker Studio](https://aws.amazon.com/sagemaker/studio/)
   domain (refer to
   [Use quick setup for Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-quick-start.html)
   ) to access
   [Jupyter notebooks](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-user-guide.html)
   for running the training code. Alternatively, JupyterLab can be used in a local setup or another Python development environment to execute the notebook and submit the SageMaker training job.

*Note: These permissions grant broad access and are not recommended for use in production environments. See the*
[*SageMaker Developer Guide*](https://docs.aws.amazon.com/sagemaker/)
*for guidance on defining more fine-grained permissions*

The code example can be found at
[this GitHub repository](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/3_distributed_training/models/deepseek-r1-distill-qwen-7b)
.

## Prepare the dataset

The data preparation pipeline transforms the raw DeepMind CodeContest dataset into a format suitable for reinforcement learning training. We apply systematic filters to identify suitable problems, removing those with
[Codeforces](https://codeforces.com/)
ratings below 800 and implementing quality validation checks for missing test cases, malformed descriptions, and invalid constraints.

We categorize problems into three difficulty tiers: Easy (800-1000 points), Hard (1100-2200 points), and Expert (2300-3500 points). This post uses only the Easy dataset for training. Each problem is formatted with two components: a user prompt containing the problem statement, and a
`reward_model`
specification with test cases, time limits, and memory constraints. Crucially, the
`ground_truth`
field contains no solution code — only test cases, forcing the model to learn through reward signals rather than memorizing solutions.

```
{
  "data_source": "code_contests",
  "prompt": [
    {
      "role": "user",
      "content": "Write a C++ solution for this problem: ..."
    }
  ],
  "ability": "coding-cp",
  "reward_model": {
    "style": "rule",
    "ground_truth": {
      "name": "problem 1",
      "public_tests": {
        "input": ["test input 1", "test input 2"],
        "output": ["expected output 1", "expected output 2"]
      },
      "private_tests": {
        "input": ["private input 1", "private input 2"],
        "output": ["private output 1", "private output 2"]
      },
      "time_limit": 2.0,
      "memory_limit_bytes": 268435456,
      "cf_rating": 1200
    }
  }
}
```

For this post, we provide a pre-processed subset of the Easy difficulty dataset in the code sample to streamline the training example, accessible from the
[GitHub repository](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/3_distributed_training/models/deepseek-r1-distill-qwen-7b/data)
.

## GRPO training using veRL

The training process uses Ray to orchestrate the distributed execution and synchronization of vLLM rollout, reward evaluation (code compilation and execution), FSDP model parallelism, and Ulysses sequence parallelism. We set the degree of sequence parallelism to 4 for long-form reasoning and code generations.

The veRL framework implements a sophisticated multi-component architecture through its
`main_ppo.py`
orchestrator, which coordinates three primary distributed worker types:
`ActorRolloutRefWorker`
for policy inference and rollouts,
`CriticWorker`
for value function estimation, and
`RewardModelWorker`
for scoring generated solutions.

The
[GRPO](https://arxiv.org/abs/2402.03300)
algorithm enhances traditional
[proximal policy optimization (PPO)](https://arxiv.org/abs/1707.06347)
by computing advantages using group-relative baselines, which helps stabilize training by reducing variance in policy gradient estimates.

We extended the
[TinyZero](https://github.com/Jiayi-Pan/TinyZero)
code repository by using Ray to manage and distribute reward function calculation. This enables parallel C++ code compilation and evaluation across the same cluster to address the compute-intensive and latency-bound nature of code execution. The entire pipeline is executed as a SageMaker training job running on
`ml.p4de.24xlarge`
instances. The training pipeline consists of the following steps as shown in the following architecture:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-3-2.png)

1. **Rollout**
   : Coding problem prompts are fed into the vLLM inference engine for rolling out potential solutions.
2. **Response generation**
   : vLLM generates multiple responses (reasoning + code) for each prompt.
3. **Code execution**
   : Code solutions are extracted from responses and are compiled and executed by distributed workers (compilers and runtime) managed by Ray.
4. **Reward calculation**
   : Execution outcomes are used to calculate rewards (i.e. testcase pass ratios) and advantages are computed using group-relative baselines.
5. **Policy update**
   : The Actor uses advantages and token probabilities to compute the PPO loss, which is used to update CodeFu’s parameters through gradient descent.
6. **Iteration**
   : The process repeats with batches of prompt-response-reward cycles, with Ray managing the distributed sampling, execution, and training synchronization across the pipeline.

The training process orchestration involves several key components implemented across multiple modules. The core veRL training loop is implemented in
`main_ppo.py`
, which initializes Ray workers and manages the distributed training process:

```
@ray.remote
def main_task(config):
    # Initialize tokenizer and download model
    local_path = copy_local_path_from_hdfs(config.actor_rollout_ref.model.path)
    tokenizer = hf_tokenizer(local_path)

    # Define distributed worker roles
    role_worker_mapping = {
        Role.ActorRollout: ray.remote(ActorRolloutRefWorker),
        Role.Critic: ray.remote(CriticWorker),
        Role.RefPolicy: ray.remote(ActorRolloutRefWorker),
    }

    # Initialize reward manager for code execution
    reward_fn = RewardManager(tokenizer=tokenizer, num_examine=0)

    # Create and start trainer
    trainer = RayPPOTrainer(
        config=config,
        tokenizer=tokenizer,
        role_worker_mapping=role_worker_mapping,
        resource_pool_manager=resource_pool_manager,
        reward_fn=reward_fn,
    )
    trainer.init_workers()
    trainer.fit()
```

The reward evaluation system implements parallel code execution through Ray remote functions, handling C++ compilation and test case execution:

```
@ray.remote
def process_reward_item(idx, valid_response_length, sequences_str, data_source, reward_model_data):
    # Extract and compile C++ code from model response
    ground_truth = json.loads(reward_model_data)["ground_truth"]

    # Select appropriate scoring function based on data source
    if data_source == "code_contests":
        compute_score = code_contests.compute_score

    # Execute code against test cases and calculate pass ratio
    score = compute_score(solution_str=sequences_str, ground_truth=ground_truth)
    return idx, score, valid_response_length, sequences_str, data_source
```

The parallel test case execution system optimizes evaluation efficiency by sampling test cases and using process pools:

```
def run_test_cases_parallel(
    bin_file: str, test_inputs: List[str],
    test_outputs: List[str],
    prob_name: str, execution_timeout: float,
    max_test_cases: int = 100,
    max_workers: int = 100) -> Tuple[int, int]:
    # Sample test cases if too many available
    if len(test_inputs) > max_test_cases:
        random_indices = np.random.choice(len(test_inputs), size=max_test_cases, replace=False)
        test_inputs = test_inputs[random_indices]
        test_outputs = test_outputs[random_indices]

    # Execute test cases in parallel using ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=min(max_workers, len(test_inputs))) as executor:
        results = list(executor.map(_process_test_case, args_list))
        total_matches = sum(results)

    return total_matches, len(test_inputs)
```

This implementation enables efficient distributed training by separating concerns: the
`main_ppo.py`
orchestrator manages Ray worker coordination, while the reward system provides scalable code evaluation through parallel compilation and execution across the SageMaker cluster.

Below is the pseudocode for the reward calculation used in this post to train a competitive programming coding model. The reward function is the most important part of reinforcement learning as it defines what the model is encouraged to achieve and what it should avoid. This implementation uses a hierarchical penalty system that first checks for fundamental code execution issues, assigning severe penalties for non-executable code (-1) and moderate penalties for compilation failures (-0.5). Extracted code solutions are executed with strict time limit enforcement – code exceeding the problem’s specified time limit is given zero reward, facilitating realistic competitive programming conditions. For a successfully executed C++ solution, its reward is calculated as a linear function based on the fraction of private test cases passed, encouraging the model to solve as many private test cases as possible while avoiding overfitting to publicly visible tests. This design prioritizes code correctness and execution validity, with the private test performance serving as the sole signal for learning optimal coding solutions.

```
def compute_reward(code_output, ground_truth):
    # Handle execution failures (same for both stages)
    if not is_executable(code_output):
        return -1

    if compilation_failed(code_output):
        return -0.5

    if exceeds_time_limit(code_output):
        return 0

    # Primary reward signal: correctness on hidden test cases
     # Run code against private test cases
    passed_private, total_private = run_private_tests(code_output, ground_truth, max_test_cases=1000)

   return passed_private / total_private
```

Refer to
`scripts/verl/utils/reward_score/code_contests.py`
for the complete Python code. Executing generated code in production environments requires appropriate
[sandboxing](https://github.com/aws-samples/sample-e2b-on-aws)
. In this controlled demonstration setting, we execute the code as a quick example to evaluate its correctness to assign rewards.

## Ray workload with SageMaker training jobs

To train CodeFu-7B using veRL and Ray on SageMaker training jobs, we use the ModelTrainer class from the SageMaker Python SDK. Start by setting up the distributed training workload with the following steps:

1. Select the instance type and container image for the training job:

```
instance_type = "ml.p4de.24xlarge"
instance_count = 2


account_id = sts.get_caller_identity()["Account"]
region = sagemaker_session.boto_session.region_name
repo_name = "codefu-pytorch"
tag = "latest"

image_uri = f"{account_id}.dkr.ecr.{region}.amazonaws.com/{repo_name}:{tag}"
```

The training uses a custom Docker container that includes veRL, Ray, and the necessary dependencies for distributed RL training. Refer to the
[GitHub repository](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/3_distributed_training/models/deepseek-r1-distill-qwen-7b/docker)
for the complete container definition and build instructions.

2. Create the ModelTrainer to encapsulate the Ray-based training setup:

The ModelTrainer class provides flexible execution options through its SourceCode configuration, allowing users to customize their training workflows with different frameworks and launchers. Specify either an
`entry_script`
for direct Python script execution or use the command parameter for custom execution commands, enabling integration with specialized frameworks such as Ray, Hugging Face
[Accelerate](https://huggingface.co/docs/accelerate/index)
, or custom distributed training solutions.

```
...
args = [
    "--entrypoint", "train.py",
    "--config", "/opt/ml/input/data/config/args.yaml",
]

# Define the script to be run with Ray launcher
source_code = SourceCode(
    source_dir="./scripts",
    requirements="requirements.txt",
    command=f"python launcher.py {' '.join(args)}",
)

# Define the compute configuration
compute_configs = Compute(
    instance_type=instance_type,
    instance_count=instance_count,
    keep_alive_period_in_seconds=1800,
)

job_name = "train-codefu-verl-ray"
output_path = f"s3://{bucket_name}/{job_name}"

model_trainer = ModelTrainer(
    training_image=image_uri,
    source_code=source_code,
    base_job_name=job_name,
    compute=compute_configs,
    stopping_condition=StoppingCondition(max_runtime_in_seconds=3600 * 24 * 5),
    output_data_config=OutputDataConfig(s3_output_path=output_path),
    checkpoint_config=CheckpointConfig(
        s3_uri=output_path + "/checkpoint",
        local_path="/opt/ml/checkpoints"
    ),
    environment={
        "RAY_PROMETHEUS_HOST": "<PROMETHEUS_HOST>",
        "RAY_GRAFANA_HOST": "<GRAFANA_HOST>",
        "RAY_PROMETHEUS_NAME": "prometheus",
        "BASE_MODEL": "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        "RUN_NAME": "sagemaker-training-run",
        ...
    },
    role=get_execution_role(),
).with_remote_debug_config(RemoteDebugConfig(enable_remote_debug=True))
```

The
`launcher.py`
script serves as the universal entry point that detects the SageMaker environment (single-node or multi-node, homogeneous or heterogeneous cluster), initializes the Ray cluster with proper head/worker node coordination, and executes your custom training script. Key
`launcher.py`
functionalities are:

* **Ray cluster setup**
  : Automatically detects the cluster environment and initializes Ray with proper head node selection.
* **Node coordination**
  : Manages communication between head and worker nodes across SageMaker instances.
* **Script execution**
  : Executes the specified
  `--entrypoint`
  script (
  `train.py`
  ) within the Ray cluster context.
* **Prometheus and grafana connectivity**
  : Configures Ray to export metrics and establishes connection to external Prometheus and Grafana servers specified by
  `RAY_PROMETHEUS_HOST`
  and
  `RAY_GRAFANA_HOST`
  for comprehensive cluster monitoring. For additional information, refer to
  [Ray on SageMaker training jobs – Observability with Prometheus and Grafana](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs#observability-with-prometheus-and-grafana)
  .

For the complete implementation of the Ray cluster setup with SageMaker training jobs, refer to
[launcher.py](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs/blob/main/scripts/launcher.py)
.

The
`train.py`
script serves as the actual training orchestrator that:

* Loads the veRL configuration from the provided YAML file
* Sets up the distributed training environment with proper tokenizer and model initialization
* Constructs and executes the veRL training command with the necessary parameters
* Handles environment variable configuration for Ray workers and NVIDIA Collective Communications Library (NCCL) communication
* Manages the complete training lifecycle from data loading to model checkpointing

For the complete implementation of the entry point script, refer to
[train.py](https://github.com/aws-samples/amazon-sagemaker-generativeai/blob/main/3_distributed_training/models/deepseek-r1-distill-qwen-7b/scripts/train.py)
.

1. Set up the input channels for the ModelTrainer by creating
   `InputData`
   objects from the S3 bucket paths:

```
...

train_input = InputData(
    channel_name="train",
    data_source=S3DataSource(
        s3_data_type="S3Prefix",
        s3_uri=train_dataset_s3_path,
        s3_data_distribution_type="FullyReplicated",
    ),
)

config_input = InputData(
    channel_name="config",
    data_source=S3DataSource(
        s3_data_type="S3Prefix",
        s3_uri=train_config_s3_path,
        s3_data_distribution_type="FullyReplicated",
    ),
)
```

2. Submit the training job using the train function call on the created ModelTrainer:

```
model_trainer.train(
    input_data_config=[train_input, val_input, config_input],
    wait=False
)
```

The job can be monitored directly from the notebook output or through the SageMaker console, which shows the job status and corresponding CloudWatch logs.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-5-3.png)

*SageMaker training jobs console*

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-7-2.png)

*SageMaker training jobs system metrics*

The launcher.py script orchestrates the Ray cluster initialization through the following automated steps, which can be monitored in real-time through CloudWatch logs:

1. **Setup SageMaker training jobs and Ray environment variables**
   : Configures necessary environment variables for both SageMaker integration and Ray cluster communication:

```
__main__ - INFO - Entrypoint argument provided: train.py
__main__ - INFO - Set source_dir=, entry_script=train.py
...
__main__ - INFO - Found SageMaker environment with hosts: ...
__main__ - INFO - Current host: algo-1
__main__ - INFO - Configured Prometheus host: <PROMETHEUS_HOST>
__main__ - INFO - Configured Grafana host: <GRAFANA_HOST>
__main__ - INFO - Ray runtime environment contains 137 total environment variables
__main__ - INFO - Ray runtime environment: ...
```

2. **Identify the SageMaker training job cluster type**
   : Detects whether the deployment is single-node or multi-node, and determines a single or multi-node cluster, and if it’s a homogeneous or heterogeneous cluster configuration:

```
__main__ - INFO - Homogeneous cluster configuration: 2 total hosts
__main__ - INFO - All hosts: ['algo-1', 'algo-2']
__main__ - INFO - Found multiple hosts, initializing Ray as a multi-node cluster
```

3. **Setup head and worker nodes**
   : Identifies which instance serves as the Ray head node and configures the remaining instances as worker nodes
   **:**

```
__main__ - INFO - Head node: algo-1, Current host: algo-1
__main__ - INFO - CPUs for the head node: 192
__main__ - INFO - GPUs for the head node: 8
```

4. **Start Ray node**
   : Initializes the Ray head node and worker nodes with appropriate resource allocation and dashboard configuration, by verifying that the worker nodes successfully connect to the head node before proceeding:

```
#011INFO worker.py:1723 -- Connecting to existing Ray cluster at address: ...
#011INFO worker.py:1908 -- Connected to Ray cluster. View the dashboard at
__main__ - INFO - All nodes connected to the Ray cluster!
```

5. **Execute the training script**
   : Launches the specified entrypoint script (train.py) within the fully initialized Ray cluster context:

```
Script path: /opt/ml/input/data/code/train.py
...
__main__ - INFO - Loading and executing Python script using importlib...
```

After the job completes, the trained model weights and checkpoints will be available in the specified S3 output path, ready for deployment or further evaluation.

## Experiment tracking

The CodeFu training pipeline integrates seamlessly with
[Managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
as well as third party solutions, for comprehensive experiment tracking and visualization of reinforcement learning metrics.

The following image shows the metrics that are particularly useful to monitor during CodeFu training.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-9-1.png)

The metrics plot shows a promising GRPO/PPO learning progression for the competitive programming model. The reward signals demonstrate clear improvement, with
`critic/reward/mean`
rising from
**-0.8 to 0.6**
and
`critic/reward/min`
recovering from initial failures
**-1.0**
to moderate performance
**-0.5**
, while
`critic/reward/max`
maintains perfect scores
**1.0**
throughout training, indicating the model can achieve optimal solutions.

The Actor metrics reveal healthy training dynamics:
`actor/ppo_kl`
remains low
**~0.0002**
after an initial spike, confirming stable policy updates, while
`actor/pg_clipfrac`
stays in a reasonable range
**~0.002-0.004**
, suggesting appropriately sized learning steps.

The increasing
`actor/kl_loss`
trend indicates growing divergence from the reference model as expected during RL fine-tuning. Most importantly,
`val/test_score/code_contests`
shows consistent improvement from
**-0.6 to ~0.5**
, and the train-validation comparison reveals good generalization with both curves tracking closely, indicating the model is learning to solve coding problems effectively without overfitting.

The table below explains key GRPO training metrics and why monitoring each one matters for diagnosing training health and performance:

|  |  |  |
| --- | --- | --- |
| Metric | Description | Purpose |
| **critic/reward/min** | Minimum reward achieved on the training set | **Detect catastrophic failures** : Extremely negative rewards indicate the model is producing poor outputs that need attention |
| **critic/reward/mean** | Average reward across the training set | **Primary progress indicator** : Shows overall model performance improvement; should generally trend upward during successful training |
| **critic/reward/max** | Maximum reward achieved on the training set | **Track best-case performance** : Shows the model’s peak capability; helps identify if the model can achieve excellent results even if average is low |
| **actor/ppo\_kl** | KL divergence between current and previous policy iteration | **Training stability monitoring** : High values indicate rapid policy changes that may destabilize training; should stay moderate |
| **actor/pg\_clipfrac** | Fraction of policy updates hitting the clipping boundary | **Update aggressiveness gauge** : Moderate values indicate healthy learning; too high suggests overly aggressive updates that may destabilize training, too low (e.g. zero) suggests inefficient learning. This is valid only during off-policy PPO updates. |
| **actor/kl\_loss** | KL divergence between current policy and fixed reference model | **Reference drift prevention** : Helps prevent the model from deviating too far from original behavior; important for maintaining coding capabilities |
| **val/test\_score/code\_contests** | Reward/performance on held-out validation set | **Generalization check** : Most important metric for real performance; detects overfitting and measures true model improvement |

## (Optional) Observability with Ray dashboard and Grafana

To access the Ray Dashboard and enable Grafana visualization during training, establish port forwarding using
[AWS Systems Manager (SSM)](https://aws.amazon.com/systems-manager/)
. To learn more about the setup of AWS SSM, please refer to
[AWS Systems Manager Quick Setup](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-quick-setup.html)
.

1. First, identify the head node in your multi-node cluster by examining the CloudWatch logs:

```
__main__ - INFO - Found multiple hosts, initializing Ray as a multi-node cluster
__main__ - INFO - Head node: algo-1, Current host: algo-2
```

2. Access the Ray Dashboard by forwarding port 8265 from the head node:

```
aws ssm start-session —target sagemaker-training-job:train-codefu-verl-ray-20250821185206_algo-1 \
--region us-east-1\
--document-name AWS-StartPortForwardingSession \
--parameters '{"portNumber":["8265"],"localPortNumber":["8265"]}'
```

3. Enable Grafana to collect Ray metrics by forwarding port 8080 (Ray metrics export port):

```
aws ssm start-session —target sagemaker-training-job:train-codefu-verl-ray-20250821185206_algo-1 \
--region us-east-1\
--document-name AWS-StartPortForwardingSession \
--parameters '{"portNumber":["8080"],"localPortNumber":["<YOUR_LOCAL_PORT>"]}'
```

Once port forwarding is established, the Ray Dashboard can be accessed at
`localhost:8265`
in your browser, providing detailed insights into:

* **Worker utilization**
  across the distributed cluster
* **Task execution**
  status and performance metrics
* **Resource consumption**
  including GPU and memory usage
* **Actor and task scheduling**
  across Ray workers

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-11-3.png)

The integrated Grafana dashboards provide comprehensive visualization of the training metrics, system performance, and cluster health in real-time:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/02/12/image-13-1.png)

This observability setup is crucial for debugging distributed RL training issues, optimizing resource allocation, and making sure the training process progresses efficiently across the multi-node SageMaker cluster.

## Clean up

To clean up your resources and avoid ongoing charges, follow these steps:

1. [Delete unused SageMaker Studio resources](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-jl-admin-guide-clean-up.html)
2. (Optional)
   [Delete the SageMaker Studio domain](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-delete-domain.html)
3. On the SageMaker console, choose
   **Training**
   in the navigation pane and verify that your training job isn’t running anymore.

## Conclusions

This post demonstrates how to train specialized reasoning models for competitive programming using the Ray on Amazon SageMaker Training jobs solution combined with veRL’s reinforcement learning framework.

The Ray on SageMaker training jobs solution simplifies the complexity of orchestrating distributed RL workloads by automatically handling Ray cluster initialization, multi-node coordination, and resource management across heterogeneous compute environments. This integration enables organizations to use Ray’s advanced distributed computing capabilities—including support for complex multi-component architectures, dynamic resource allocation, and fault-tolerant execution—while benefiting from SageMaker’s fully managed infrastructure, enterprise-grade security, and pay-as-you-go pricing model.

The detailed metrics analysis demonstrated how to monitor training health through reward progression, policy stability indicators, and generalization performance, enabling practitioners to identify optimal training configurations and troubleshoot distributed training issues effectively.

To begin implementing distributed RL training with Ray on SageMaker, visit the Ray on Amazon SageMaker Training jobs
[GitHub repository](https://github.com/aws-samples/sample-ray-on-amazon-sagemaker-training-jobs)
for the foundational solution framework. The complete CodeFu-7B training implementation, including veRL integration and configuration examples, is available at this
[GitHub repository](https://github.com/aws-samples/amazon-sagemaker-generativeai/tree/main/3_distributed_training/models/deepseek-r1-distill-qwen-7b)
.

---

### About the authors

### Bruno Pistone

**Bruno Pistone**
is a Senior Worldwide Generative AI/ML Specialist Solutions Architect at AWS based in Milan, Italy. He works with AWS product teams and large customers to help them fully understand their technical needs and design AI and machine learning solutions that take full advantage of the AWS cloud and Amazon ML stack. His expertise includes distributed training and inference workloads, model customization, generative AI, and end-to-end ML. He enjoys spending time with friends, exploring new places, and traveling to new destinations.

### Giuseppe Angelo Porcelli

**Giuseppe Angelo Porcelli**
is a Principal Machine Learning Specialist Solutions Architect for Amazon Web Services. With several years of software engineering and an ML background, he works with customers of any size to understand their business and technical needs and design AI and ML solutions that make the best use of the AWS Cloud and the Amazon Machine Learning stack. He has worked on projects in different domains, including MLOps, computer vision, and NLP, involving a broad set of AWS services. In his free time, Giuseppe enjoys playing football.

### Yin Song

**Yin Song**
is a Senior Applied Scientist at the AWS Prototyping team in Sydney, Australia, with over five years of experience helping customers build tailored prototypes that demonstrate complex AWS service use cases. His work focuses on research in AI model fine-tuning and serving, enabling impactful end-to-end AI solutions. A passionate advocate for open source, Yin leads generative AI initiatives that have produced widely-adopted models.

### Chen Wu

**Chen Wu**
is a Principal Applied Scientist at the AWS Prototyping team, where he drives both applied research and high-impact customer engagements. He specializes in long-context language models, reasoning LLMs, agentic systems, and high-performance AI systems. Chen leads development of the Agent Training Kit, an open source framework for continual learning agents. He has delivered strategic engagements across genomic foundation models, LLM optimization, multi-scale image generation, and 3D/4D volumetric AI pipelines. His open LLMs on Hugging Face have achieved over 1 million downloads, and his long-context research has appeared in NeurIPS 2024 and ACL 2025. He is an ACM Gordon Bell Prize Finalist.