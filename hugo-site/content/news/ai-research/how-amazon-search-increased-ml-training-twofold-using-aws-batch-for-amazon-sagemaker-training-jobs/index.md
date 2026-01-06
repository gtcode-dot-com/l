---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-12T22:51:26.419822+00:00'
exported_at: '2025-11-12T22:54:41.482732+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-amazon-search-increased-ml-training-twofold-using-aws-batch-for-amazon-sagemaker-training-jobs
structured_data:
  about: []
  author: ''
  description: In this post, we show you how Amazon Search optimized GPU instance
    utilization by leveraging AWS Batch for SageMaker Training jobs. This managed
    solution enabled us to orchestrate machine learning (ML) training workloads on
    GPU-accelerated instance families like P5, P4, and others. We will also provide
    a step-by-step walkthrough of the use case implementation.
  headline: How Amazon Search increased ML training twofold using AWS Batch for Amazon
    SageMaker Training jobs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-amazon-search-increased-ml-training-twofold-using-aws-batch-for-amazon-sagemaker-training-jobs
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How Amazon Search increased ML training twofold using AWS Batch for Amazon
  SageMaker Training jobs
updated_at: '2025-11-12T22:51:26.419822+00:00'
url_hash: cd04ea205dccd946ce31247bcb9d203327b6a1f8
---

In this post, we show you how Amazon Search optimized GPU instance utilization by leveraging AWS Batch for SageMaker Training jobs. This managed solution enabled us to orchestrate machine learning (ML) training workloads on GPU-accelerated instance families like P5, P4, and
[others](https://aws.amazon.com/pm/ec2/?refid=3c700fb5-ee68-491d-be67-b7cbac831dee)
. We will also provide a step-by-step walkthrough of the use case implementation.

## Machine learning at Amazon Search

At Amazon Search, we use hundreds of GPU-accelerated instances to train and evaluate ML models that help our customers discover products they love. Scientists typically train more than one model at a time to find the optimal set of features, model architecture, and hyperparameter settings that optimize the model’s performance. We previously leveraged a first-in-first-out (FIFO) queue to coordinate model training and evaluation jobs. However, we needed to employ a more nuanced criteria to prioritize which jobs should run in what order. Production models needed to run with high priority, exploratory research as medium priority, and hyperparameter sweeps and batch inference as low priority. We also needed a system that could handle interruptions. Should a job fail, or a given instance type become saturated, we needed the job to run on other available compatible instance types while respecting the overall prioritization criteria. Finally, we wanted a managed solution so we could focus more on model development instead of managing infrastructure.

After evaluating multiple options, we chose
[AWS Batch for Amazon SageMaker Training jobs](https://aws.amazon.com/blogs/machine-learning/introducing-aws-batch-support-for-amazon-sagemaker-training-jobs/)
because it best met our requirements. This solution seamlessly integrated AWS Batch with Amazon SageMaker and allowed us to run jobs per our prioritization criteria. This allows applied scientists to submit multiple concurrent jobs without manual resource management. By leveraging AWS Batch features such as advanced prioritization through
[fair-share scheduling](https://aws.amazon.com/blogs/hpc/introducing-fair-share-scheduling-for-aws-batch/)
, we increased peak utilization of GPU-accelerated instances from 40% to over 80%.

## Amazon Search: AWS Batch for SageMaker Training Job implementation

We leveraged three AWS technologies to set up our job queue. We used
[Service Environments](https://docs.aws.amazon.com/batch/latest/userguide/what-are-service-environments.html)
to configure the SageMaker AI parameters that AWS Batch uses to submit and manage SageMaker Training jobs. We used
[Share Identifiers](https://docs.aws.amazon.com/batch/latest/userguide/share-identifiers.html)
to prioritize our workloads. Finally, we used
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
to monitor and the provision of alerting capability for critical events or deviations from expected behavior. Let’s dive deep into these constructs.

**Service environments**
. We set up service environments to represent the total GPU capacity available for each instance family, such as P5s and P4s. Each service environment was configured with fixed limits based on our team’s reserved capacity in AWS Batch. Note that for teams using
[SageMaker Training Plans](https://docs.aws.amazon.com/sagemaker/latest/dg/reserve-capacity-with-training-plans.html)
, these limits can be set to the number of reserved instances, making capacity planning more straightforward. By defining these boundaries, we established how the total GPU instance capacity within a service environment was distributed across different production jobs. Each production experiment was allocated a portion of this capacity through Share Identifiers.

Figure 1 provides a real-world example of how we used AWS Batch’s fair-share scheduling to divide 100 GPU instance between ShareIDs. We allocated 60 instances to ProdExp1, and 40 to ProdExp2. When ProdExp2 used only 25 GPU instances, the remaining 15 could be borrowed by ProdExp1, allowing it to scale up to 75 GPU instances. When ProdExp2 later needed its full 40 GPU instances, the scheduler preempted jobs from ProdExp1 to restore balance. This example used the P4 instance family, but the same approach could apply to any SageMaker-supported EC2 instance family. This ensured that production workloads have guaranteed access to their assigned capacity, while exploratory or ad-hoc experiments could still make use of any idle GPU instances. This design safeguarded critical workloads and improved overall instance utilization by ensuring that no reserved capacity went unused.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-1-13.png)

Figure 1: AWS Batch fair-share scheduling

**Share Identifiers**
. We used Share Identifiers to allocate fractions of a service environment’s capacity to production experiments. Share Identifiers are string tags applied at job submission time. AWS Batch used these tags to track usage and enforce fair-share scheduling. For initiatives that required dedicated capacity, we defined preset Share Identifiers with quotas in AWS Batch. This reserved capacity for production tracks. These quotas acted as fairness targets rather than hard limits. Idle capacity could still be borrowed, but under contention, AWS Batch enforced fairness by preempting resources from overused identifiers and reassigned them to underused ones.

Within each Share Identifier, job priorities ranging from 0 to 99 determined execution order, but priority-based preemption only triggered when the ShareIdentifier reached its allocated capacity limit. Figure 2 illustrates how we setup and used our share identifiers. ProdExp1 had 60 p4d instances and ran jobs at various priorities. Job A had a priority of 80, Job B was set to 50, Job C was set to at 30, and Job D had a priority 10. When all 60 instances were occupied and a new high-priority job (priority 90) requiring 15 instances was submitted, the system preempted the lowest priority running job (Job D) to make room, while maintaining the total of 60 instances for that Share Identifier.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-2-11.png)

Figure 2: Priority scheduling within a Share ID

**Amazon CloudWatch**
. We used Amazon CloudWatch to instrument our SageMaker training jobs. SageMaker automatically publishes metrics on job progress and resource utilization, while AWS Batch provides detailed information on job scheduling and execution. With AWS Batch, we queried the status of each job through the
[AWS Batch APIs](https://docs.aws.amazon.com/batch/latest/userguide/job_states.html)
. This made it possible to track jobs as they transitioned through states such as SUBMITTED, PENDING, RUNNABLE, STARTING, RUNNING, SUCCEEDED, and FAILED. We published these metrics and job states to CloudWatch and configured dashboards and alarms to alert anytime we encountered extended wait times, unexpected failures, or underutilized resources. This built-in integration provided both real-time visibility and historical trend analysis, which helped our team maintain operational efficiency across GPU clusters without building custom monitoring systems.

## Operational impact on team performance

By adopting AWS Batch for SageMaker Training jobs, we enabled experiments to run without concerns about resource availability or contention. Researchers could submit jobs without waiting for manual scheduling, which increased the number of experiments that could be run in parallel. This led to shorter queue times, higher GPU utilization, and faster turnaround of training results, directly improving both research throughput and delivery timelines.

## How to set up AWS Batch for SageMaker Training jobs

To set up a similar environment, you can follow this tutorial, which shows you how to orchestrate multiple GPU
[large language model](https://aws.amazon.com/what-is/large-language-model/)
(LLM) fine-tuning jobs using multiple GPU-powered instances. The solution is also available on
[GitHub](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20%20%20%20build_and_train_models/sm-training-queues-pytorch)
.

### Prerequisites

To orchestrate multiple SageMaker Training jobs with AWS Batch, first you need to complete the following prerequisites:

Clone the GitHub repository with the assets for this deployment. This repository consists of notebooks that reference assets:

```
git clone https://github.com/aws/amazon-sagemaker-examples/
cd  build_and_train_models/sm-training-queues-pytorch/
```

### Create AWS Batch resources

To create the necessary resources to manage SageMaker Training job queues with AWS Batch, we provide utility functions in the example to automate the creation of the
`Service Environment`
,
`Scheduling Policy,`
and
`Job Queue`
.

The service environment represents the Amazon SageMaker AI capacity limits available to schedule, expressed by maximum number of instances. The scheduling policy indicates how resource computes are allocated in a job queue between users or workloads. The job queue is the scheduler interface that researchers interact with to submit jobs and interrogate job status. AWS Batch provides two different queues we can operate with:

1. **FIFO queues**
   – Queues in which no scheduling policies are required
2. **Fair-share queues**
   – Queues in which a scheduling policy
   [Amazon Resource Name](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)
   (ARN) is required to orchestrate the submitted jobs

We recommend creating dedicated service environments for each job queue in a 1:1 ratio. FIFO queues provide basic message delivery, while fair-share scheduling (FSS) queues provide more sophisticated scheduling, balancing utilization within a Share Identifier, share weights, and job priority. For customers who don’t need multiple shares but would like the ability to assign a priority on job submission, we recommend creating an FSS queue and using a single share within it for all submissions.To create the resources, execute the following commands:

```
cd smtj_batch_utils
python create_resources.py
```

You can navigate the AWS Batch Dashboard, shown in the following screenshot, to explore the created resources.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-3-3.jpeg)

This automation script created two queues:

1. `ml-c5-xlarge-queue`
   – A FIFO queue with priority 2 used for CPU workloads
2. `ml-g6-12xlarge-queue`
   – A fair-share queue with priority 1 used for GPU workloads

The associated scheduling policy for the queue
`ml-g6-12xlarge-queue`
is with share attributes such as High priority (HIGHPRI), Medium priority (MIDPRI) and Low priority (LOWPRI) along with the queue weights. Users can submit jobs and assign them to one of three shares: HIGHPRI, MIDPRI, or LOWPRI and assign weights such as 1 for high priority and 3 for medium and 5 for low priority. Below is the screenshot showing the scheduling policy details:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-4-1.jpeg)

For instructions on how to set up the service environment and a job queue, refer to the
**Getting started**
section in
[Introducing AWS Batch support for SageMaker Training Jobs](https://aws.amazon.com/blogs/machine-learning/introducing-aws-batch-support-for-amazon-sagemaker-training-jobs/)
blog.

### Run LLM fine-tuning jobs on SageMaker AI

We run the notebook
**notebook.ipynb**
to start submitting SageMaker Training jobs with AWS Batch. The notebook contains the code to prepare the data used for the workload, upload on
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3), and define the hyperparameters required by the job to be executed.

To run the fine-tuning workload using SageMaker Training jobs, this example uses the
**ModelTrainer**
class. The ModelTrainer class is a newer and more intuitive approach to model training that significantly enhances user experience. It supports distributed training, build your own container (BYOC), and recipes.

For additional information about ModelTrainer, you can refer to
[Accelerate your ML lifecycle using the new and improved Amazon SageMaker Python SDK – Part 1: ModelTrainer](https://aws.amazon.com/blogs/machine-learning/accelerate-your-ml-lifecycle-using-the-new-and-improved-amazon-sagemaker-python-sdk-part-1-modeltrainer/?t)
.

To set up the fine-tuning workload, complete the following steps:

1. Select the instance type, the container image for the training job, and define the checkpoint path where the model will be stored:

   ```
   import sagemaker

   instance_type = "ml.g6.12xlarge"
   instance_count = 1

   image_uri = sagemaker.image_uris.retrieve(
       framework="pytorch",
       region=sagemaker_session.boto_session.region_name,
       version="2.6",
       instance_type=instance_type,
       image_scope="training"
   )
   ```
2. Create the ModelTrainer function to encapsulate the training setup. The ModelTrainer class simplifies the experience by encapsulating code and training setup. In this example:
   1. `SourceCode`
      – The source code configuration. This is used to configure the source code for running the training job by using your local python scripts.
   2. `Compute`
      – The compute configuration. This is used to specify the compute resources for the training job.

   ```
   from sagemaker.modules.configs import Compute, OutputDataConfig, SourceCode, StoppingCondition
   from sagemaker.modules.distributed import Torchrun
   from sagemaker.modules.train import ModelTrainer

   role = sagemaker.get_execution_role()

   # Define the script to be run
   source_code = SourceCode(
       source_dir="./scripts",
       requirements="requirements.txt",
       entry_script="train.py",
   )

   # Define the compute
   compute_configs = Compute(
       instance_type=instance_type,
       instance_count=instance_count,
       keep_alive_period_in_seconds=0
   )

   # define Training Job Name
   job_name = f"train-deepseek-distill-llama-8b-sft-batch"

   # define OutputDataConfig path
   output_path = f"s3://{bucket_name}/{job_name}"

   # Define the ModelTrainer
   model_trainer = ModelTrainer(
       training_image=image_uri,
       source_code=source_code,
       base_job_name=job_name,
       compute=compute_configs,
       distributed=Torchrun(),
       stopping_condition=StoppingCondition(max_runtime_in_seconds=7200),
       hyperparameters={
           "config": "/opt/ml/input/data/config/args.yaml"
       },
       output_data_config=OutputDataConfig(s3_output_path=output_path),
       role=role,
   )
   ```
3. Set up the input channels for ModelTrainer by creating
   [InputData](https://sagemaker.readthedocs.io/en/stable/api/training/model_trainer.html#sagemaker.modules.configs.InputData)
   objects from the provided S3 bucket paths for the training and validation datasets:

   ```
   from sagemaker.modules.configs import InputData

   train_input = InputData(
       channel_name="train",
       data_source=train_dataset_s3_path,
   )
   val_input = InputData(
       channel_name="val",
       data_source=val_dataset_s3_path,
   )
   config_input = InputData(
       channel_name="config",
       data_source=train_config_s3_path,
   )

   TRAINING_INPUTS = [train_input, val_input, config_input]
   ```

## Queue SageMaker Training jobs

This section and the following are intended to be used interactively so that you can explore how to use the
[Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/)
to submit jobs to your Batch queues. Follow these steps:

1. Select the queue to use:

   ```
   from sagemaker.aws_batch.queue import TrainingQueue
   SMTJ_BATCH_QUEUE = "ml-g6-12xlarge-queue"

   queue = TrainingQueue(SMTJ_BATCH_QUEUE)
   ```
2. In the next cell, submit two training jobs in the queue:
   1. `LOW PRIORITY`
   2. `MEDIUM PRIORITY`
3. Use the API
   `submit`
   to submit all the jobs:

   ```
   job_name_1 = job_name + "-low-pri"
   queued_job_1 = queue.submit(
       model_trainer, TRAINING_INPUTS, job_name_1, priority=5, share_identifier="LOWPRI"
   )
   job_name_2 = job_name + "-mid-pri"
   queued_job_2 = queue.submit(
       model_trainer, TRAINING_INPUTS, job_name_2, priority=3, share_identifier="MIDPRI"
   )
   ```

### Display the status of running and in queue jobs

We can use the job queue list and job queue snapshot APIs to programmatically view a snapshot of the jobs that the queue will run next. For fair-share queues, this ordering is dynamic and occasionally needs to be refreshed because new jobs are submitted to the queue or as share usage changes over time.

```
from utils.queue_utils import print_queue_state
print_queue_state(queue)
```

The following screenshot shows the jobs submitted with low priority and medium priority in the Runnable State and in the queue.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-5-3.jpeg)

You can also refer to the AWS Batch Dashboard, shown in the following screenshot, to analyze the status of the jobs.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-6-1.jpeg)

As shown in the following screenshot, the first job executed with the SageMaker Training job is the
`MEDIUM PRIORITY`
one, by respecting the scheduling policy rules defined previously.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-7-2.jpeg)

You can explore the running training job in the SageMaker AI console, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-8-2-1024x220.jpeg)

### Submit an additional job

You can now submit an additional SageMaker Training job with
`HIGH PRIORITY`
to the queue:

```
job_name_3 = job_name + "-high-pri"
queued_job_3 = queue.submit(
    model_trainer, TRAINING_INPUTS, job_name_3, priority=1, share_identifier="HIGHPRI"
)
```

You can explore the status from the dashboard, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-9-2.jpeg)

The
`HIGH PRIORITY`
job, despite being submitted later in the queue, will be executed before the other runnable jobs by respecting the scheduling policy rules, as shown in the following screenshot.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-10-1.jpeg)

As the scheduling policy in the screenshot shows, the LOWPRI share has a higher weight factor (5) than the MIDPRI share (3). Since a lower weight signifies higher priority, a LOWPRI job will be executed after a MIDPRI job, even if they are submitted at the same time.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/10/16/image-11.jpeg)

## Clean up

To clean up your resources to avoid incurring future charges, follow these steps:

1. Verify that your training job isn’t running anymore. To do so, on your
   [SageMaker console](https://console.aws.amazon.com/sagemaker/)
   , choose
   **Training**
   and check
   **Training jobs**
   .
2. Delete AWS Batch resources by using the command
   `python create_resources.py --clean`
   from the GitHub example or by manually deleting them from the
   [AWS Management Console](https://aws.amazon.com/console/)
   .

## Conclusion

In this post, we demonstrated how Amazon Search used AWS Batch for SageMaker Training Jobs to optimize GPU resource utilization and training job management. The solution transformed their training infrastructure by implementing sophisticated queue management and fair share scheduling, increasing peak GPU utilization from 40% to over 80%.We recommend that organizations facing similar ML training infrastructure challenges explore AWS Batch integration with SageMaker, which provides built-in queue management capabilities and priority-based scheduling. The solution eliminates manual resource coordination while providing workloads with appropriate prioritization through configurable scheduling policies.

To begin implementing AWS Batch with SageMaker Training jobs, you can access our sample code and implementation guide in the
[amazon-sagemaker-examples](https://github.com/aws/amazon-sagemaker-examples)
repository on GitHub. The example demonstrates how to set up
[AWS Identity and Access Management](https://aws.amazon.com/iam/)
(IAM) permissions, create AWS Batch resources, and orchestrate multiple GPU-powered training jobs using ModelTrainer class.

---

*The authors would like to thank Charles Thompson and Kanwaljit Khurmi for their collaboration.*

### About the authors

### Mona Mona

[Mona](https://www.linkedin.com/in/mona-mona/)
is a generative AI Specialist Solutions Architect at Amazon focusing. She is a published author of two books – Natural Language Processing with AWS AI Services and Google Cloud Certified Professional Machine Learning Study Guide.

### Mayank Jha

[Mayank](https://www.linkedin.com/in/jhamayank02/)
is a Senior Machine Learning Engineer at Amazon Search working on the model training optimization. He is passionate about finding practical applications for complex problems at hand and aims to develop solutions that have a deep impact on how businesses and people thrive.

### Bruno Pistone

[Bruno](https://www.linkedin.com/in/bpistone/)
is a Senior generative AI and ML Specialist Solutions Architect for AWS based in Milan. He works with large customers helping them to deeply understand their technical needs and design AI and Machine Learning solutions that make the best use of the AWS Cloud and the Amazon Machine Learning stack. He enjoys spending time with his friends and exploring new places, as well as travelling to new destinations.

### James Park

[James](https://www.linkedin.com/in/jhp612/)
is a Solutions Architect at Amazon Web Services. He works with Amazon.com to design, build, and deploy technology solutions on AWS, and has a particular interest in AI and machine learning. In his spare time he enjoys seeking out new cultures, new experiences, and staying up to date with the latest technology trends.