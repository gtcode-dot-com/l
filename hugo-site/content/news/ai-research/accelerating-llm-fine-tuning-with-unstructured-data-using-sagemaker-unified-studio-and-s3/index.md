---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T03:49:49.229209+00:00'
exported_at: '2026-04-02T03:49:52.952576+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/accelerating-llm-fine-tuning-with-unstructured-data-using-sagemaker-unified-studio-and-s3
structured_data:
  about: []
  author: ''
  description: Last year, AWS announced an integration between Amazon SageMaker Unified
    Studio and Amazon S3 general purpose buckets. This integration makes it straightforward
    for teams to use unstructured data stored in Amazon Simple Storage Service (Amazon
    S3) for machine learning (ML) and data analytics use cases. In this post,...
  headline: Accelerating LLM fine-tuning with unstructured data using SageMaker Unified
    Studio and S3
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/accelerating-llm-fine-tuning-with-unstructured-data-using-sagemaker-unified-studio-and-s3
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Accelerating LLM fine-tuning with unstructured data using SageMaker Unified
  Studio and S3
updated_at: '2026-04-02T03:49:49.229209+00:00'
url_hash: 7bf73cfb62e5a16fae54ebf99e94b1ac66f3c262
---

Last year,
[AWS announced an integration](https://aws.amazon.com/blogs/aws/streamline-the-path-from-data-to-insights-with-new-amazon-sagemaker-capabilities/)
between Amazon SageMaker Unified Studio and Amazon S3 general purpose buckets. This integration makes it straightforward for teams to use unstructured data stored in Amazon Simple Storage Service (Amazon S3) for machine learning (ML) and data analytics use cases.

In this post, we show how to integrate S3 general purpose buckets with Amazon SageMaker Catalog to fine-tune Llama 3.2 11B Vision Instruct for visual question answering (VQA) using Amazon SageMaker Unified Studio. For this task, we provide our large language model (LLM) with an input image and question and receive an answer. For example, asking to identify the transaction date from an itemized receipt:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-1.png)

For this demonstration, we use
[Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/ai/jumpstart/)
to access the Llama 3.2 11B Vision Instruct model. Out of the box, this base model achieves an Average Normalized Levenshtein Similarity
[(ANLS)](https://docsaid.org/en/blog/impl-normalized-levenshtein-similarity/)
score of 85.3% on the
[DocVQA](https://huggingface.co/datasets/HuggingFaceM4/DocumentVQA)
dataset. ANLS is a metric used to evaluate the performance of models on visual question answering tasks, which measures the similarity between the model’s predicted answer and the ground truth answer. While 85.3% demonstrates strong baseline performance, this level might not be the most efficient for tasks requiring a higher degree of accuracy and precision.

To improve model performance through fine-tuning, we’ll use the
[DocVQA dataset from Hugging Face](https://huggingface.co/datasets/HuggingFaceM4/DocumentVQA)
. This dataset contains 39,500 rows of training data, each with an input image, a question, and a corresponding expected answer. We’ll create three fine-tuned model versions using varying dataset sizes (1,000, 5,000, and 10,000 images). We’ll then evaluate them using
[Amazon SageMaker fully managed serverless MLflow](https://aws.amazon.com/about-aws/whats-new/2025/12/sagemaker-ai-serverless-mlflow-ai-development/)
to track experimentation and measure accuracy improvements.

The full end-to-end data ingestion, model development, and metric evaluation process will be orchestrated using Amazon SageMaker Unified Studio. Here is the high-level process flow diagram that we’ll step through for this scenario. We’ll expand on this throughout the blog post.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-3.png)

To achieve this process flow, we build an architecture that performs the data ingestion, data preprocessing, model training, and evaluation using Amazon SageMaker Unified Studio. We break out each step in the following sections.

The Jupyter notebook used and referenced throughout this exercise can be found in
[this GitHub repository](https://github.com/aws-samples/sample-finetuning-sagemaker-unified-studio-with-s3)
.

## Prerequisites

To prepare your organization to use the new integration between Amazon SageMaker Unified Studio and Amazon S3 general purpose buckets, you must complete the following prerequisites. Note that these steps take place on an
[Identity Center-based domain](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/working-with-domains.html)
.

1. Create an AWS account.
2. Create an Amazon SageMaker Unified Studio domain using
   [*quick setup*](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/create-domain-sagemaker-unified-studio-quick.html)
   .
3. Create two projects within the SageMaker Unified Studio domain to model the scenario in this post: one for the data producer persona and one for the data consumer persona. The first project is used for discovering and cataloging the dataset in an Amazon S3 bucket. The second project consumes the dataset to fine-tune three iterations of our large language model.
   *See*
   [*Create a project*](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started-create-a-project.html)
   *for additional information.*
4. Your data consumer project must have access to a running SageMaker managed MLflow serverless application, which will be used for experimentation and evaluation purposes. For more information, see the instructions for
   [creating a serverless MLflow application](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/sagemaker-experiments.xml.html)
   .
5. An Amazon S3 bucket should be pre-populated with the raw dataset to be used for your ML development use case. In this blog post, we use the
   [DocVQA dataset from Hugging Face](https://huggingface.co/datasets/HuggingFaceM4/DocumentVQA)
   for fine-tuning a visual question answering (VQA) use case.
6. A service quota increase request to use
   **p4de.24xlarge**
   compute for training jobs. See
   [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)
   for more information.

## Architecture

The following is the reference architecture that we build throughout this post:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-4.png)

We can break the architecture diagram into a series of six high-level steps, which we’ll observe throughout the following sections:

1. First, you create and configure an IAM access role that grants read permissions to a pre-existing Amazon S3 bucket containing the raw and unprocessed DocVQA dataset.
2. The data producer project uses the access role to discover and add the dataset to the project catalog.
3. The data producer project enriches the dataset with optional metadata and publishes it to the SageMaker Catalog.
4. The data consumer project subscribes to the published dataset, making it available to the project team responsible for developing (or fine-tuning) the machine learning models.
5. The data consumer project preprocesses the data and transforms it into three training datasets of varying sizes (1k, 5k, and 10k images). Each dataset is used to fine-tune our base large language model.
6. We use MLflow for tracking experimentation and evaluation results of the three models against our Average Normalized Levenshtein Similarity (ANLS) success metric.

## Solution walkthrough

As mentioned previously, we will opt to use the DocVQA dataset from Hugging Face for a visual question answering task. In your organization’s scenario, this raw dataset might be any unstructured data relevant to your ML use case. Examples include customer support chat logs, internal documents, product reviews, legal contracts, research papers, social media posts, email archives, sensor data, and financial transaction records.

In the prerequisite section of our
[Jupyter notebook](https://github.com/aws-samples/sample-finetuning-sagemaker-unified-studio-with-s3)
, we pre-populate our Amazon S3 bucket using the
[Datasets API](https://huggingface.co/docs/datasets/en/index)
from Hugging Face:

```
import os
from datasets import load_dataset

# Create data directory
os.makedirs("data", exist_ok=True)

# Load and save train split (first 10,000 rows)
train_data = load_dataset("HuggingFaceM4/DocumentVQA", split="train[:10000]", cache_dir="./data")
train_data.save_to_disk("data/train")

# Load and save validation split (first 100 rows)
val_data = load_dataset("HuggingFaceM4/DocumentVQA", split="validation[:100]", cache_dir="./data")
val_data.save_to_disk("data/validation")
```

After retrieving the dataset, we complete the prerequisite by synchronizing it to an Amazon S3 bucket. This represents the bucket depicted in the bottom-right section of our architecture diagram shown previously.

At this point, we’re ready to begin working with our data in Amazon SageMaker Unified Studio, starting with our data producer project. A project in Amazon SageMaker Unified Studio is a boundary within a domain where you can collaborate with others on a business use case. To bring Amazon S3 data into your project, you must first add
[access](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/adding-existing-s3-data.html)
to the data and then add the data to your project. In this post, we follow the approach of using an access role to facilitate this process.
*See*
[*Adding Amazon S3 data*](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/adding-existing-s3-data.html#adding-existing-s3-connect)
*for more information.*

Once our access role is created following the instructions in the documentation referenced previously, we can continue with discovering and cataloging our dataset. In our data producer project, we navigate to the Data → Add data → Add S3 location:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-6.png)

Provide the name of the Amazon S3 bucket and corresponding prefix containing our raw data, and note the presence of the access role dropdown containing the prerequisite access role previously created:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/25/ML-19677-image-9-1.jpeg)

Once added, note that we can now see our new Amazon S3 bucket in the project catalog as shown in the following image:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/25/ML-19677-image-11-1.jpeg)

From the perspective of our data producer persona, the dataset is now available within our project context. Depending on your organization and requirements, you might want to further enrich this data asset. For example, you can join it with additional data sources, apply business-specific transformations, implement data quality checks, or create derived features through feature engineering pipelines. However, for the purposes of this post, we’ll work with the dataset in its current form to keep our focus on the core point of integrating Amazon S3 general purpose buckets with Amazon SageMaker Unified Studio.

We are now ready to publish this bucket to our SageMaker Catalog. We can
[add optional business metadata](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-metadata-form.html)
such as a README file, glossary terms, and other data types. We add a simple README, skip other metadata fields for brevity, and continue to publishing by choosing
**Publish to Catalog**
under the
**Actions**
menu.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/25/ML-19677-image-13-1.jpeg)

At this point, we’ve added the data asset to our SageMaker Catalog and it is ready to be consumed by other projects in our domain. Switching over to the perspective of our data consumer persona and selecting the consumer project, we can now subscribe to our newly published data asset. See
[*Subscribe to a data product in Amazon SageMaker Unified Studio*](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/subscribe-data-product.html)
for more information.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/25/ML-19677-image-15-1.jpeg)

Now that we’ve subscribed to the data asset in our consumer project where we’ll build the ML model, we can begin using it within a managed JupyterLab IDE in Amazon SageMaker Unified Studio. The JupyterLab page of Amazon SageMaker Unified Studio provides a JupyterLab interactive development environment (IDE) for you to use as you perform data integration, analytics, or machine learning in your projects.

In our ML development project, navigate to the
**Compute**
→
**Spaces**
→
**Create space**
option, and choose
**JupyterLab**
in the
**Application**
(space type) menu to launch a new JupyterLab IDE.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-16.png)

Note that some models in our example notebook can take upwards of 4 hours to train using the
**ml.p4de.24xlarge**
instance type. As a result, we recommend that you set the
**Idle Time**
to 6 hours to allow the notebook to run to completion and avoid errors. Additionally, if executing the notebook from end to end for the first time, set the space storage to 100 GB to allow for the dataset to be fully ingested during the fine-tuning process.
*See*
[*Creating a new space*](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-space.html)
*for more information.*

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-18.png)

With our space created and running, we choose the
**Open**
button to launch the JupyterLab IDE. Once loaded, we upload the sample Jupyter notebook into our space using the
**Upload Files**
functionality.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-20.png)

Now that we’ve subscribed to the published dataset in our ML development project, we can begin the model development workflow. This involves three key steps: fetching the dataset from our bucket using
[Amazon S3 Access Grants](https://aws.amazon.com/s3/features/access-grants/)
, preparing it for fine-tuning, and training our models.

Grantees can access Amazon S3 data by using the AWS Command Line Interface (AWS CLI), the AWS SDKs, and the Amazon S3 REST API. Additionally, you can use the AWS
[Python](https://github.com/aws/boto3-s3-access-grants-plugin)
and
[Java](https://github.com/aws/aws-s3-accessgrants-plugin-java-v2)
plugins to call Amazon S3 Access Grants. For brevity, we opt for the AWS CLI approach in the notebook and the following code. We also include a sample that shows the use of the Python
[`boto3-s3-access-grants-plugin`](https://github.com/aws/boto3-s3-access-grants-plugin)
in the appendix section of the notebook for reference.

The process includes two steps: first obtaining temporary access credentials to the Amazon S3 control plane through the
`s3control`
CLI module, then using those credentials to sync the data locally. Update the
**AWS\_ACCOUNT\_ID**
variable with the appropriate account ID that houses your dataset.

```
import json

AWS_ACCOUNT_ID = "123456789" # REPLACE THIS WITH YOUR ACCOUNT ID
S3_BUCKET_NAME = "s3://MY_BUCKET_NAME/" # REPLACE THIS WITH YOUR BUCKET

# Get credentials
result = !aws s3control get-data-access --account-id {AWS_ACCOUNT_ID} --target {S3_BUCKET_NAME} --permission READ

json_response = json.loads(result.s)
creds = json_response['Credentials']

# Configure profile with cell magic
!aws configure set aws_access_key_id {creds['AccessKeyId']} --profile access-grants-consumer-access-profile
!aws configure set aws_secret_access_key {creds['SecretAccessKey']} --profile access-grants-consumer-access-profile
!aws configure set aws_session_token {creds['SessionToken']} --profile access-grants-consumer-access-profile

print("Profile configured successfully!")

!aws s3 sync {S3_BUCKET_NAME} ./ --profile access-grants-consumer-access-profile
```

After running the previous code and getting a successful output, we can now access the S3 bucket locally. With our raw dataset now accessible locally, we need to transform it into the format required for fine-tuning our LLM. We’ll create three datasets of varying sizes (1k, 5k, and 10k images) to evaluate how the dataset size impacts model performance.

Each training dataset contains a train and validation directory, each of which must contain an
`images`
subdirectory and accompanying
`metadata.jsonl`
file with training examples. The metadata file format includes three key/value fields per line:

```
{"file_name": "images/img_0.jpg", "prompt": "what is the date mentioned in this letter?", "completion": "1/8/93"}
{"file_name": "images/img_1.jpg", "prompt": "what is the contact person name mentioned in letter?", "completion": "P. Carter"}
```

With these artifacts uploaded to Amazon S3, we can now fine-tune our LLM by using SageMaker JumpStart to access the pre-trained Llama 3.2 11B Vision Instruct model. We’ll create three separate fine-tuned variants to evaluate. We’ve created a train() function to facilitate this using a parameterized approach, making this reusable for different dataset sizes:

```
def train(name, instance_type, training_data_path, experiment_name, run):
    ...
    estimator = JumpStartEstimator(
        model_id=model_id, model_version=model_version,
        environment={"accept_eula": "true"},  # Must accept as true
        disable_output_compression=True,
        instance_type=instance_type,
        hyperparameters=my_hyperparameters,
    )
    ...
```

Our training function handles several important aspects:

* **Model selection**
  : Uses the latest version of Llama 3.2 11B Vision Instruct from SageMaker JumpStart.
* **Hyperparameters**
  : The sample notebook uses the
  [retrieve\_default()](https://sagemaker.readthedocs.io/en/v2.245.0/api/utility/hyperparameters.html)
  API in the SageMaker SDK to automatically fetch the default hyperparameters for our model.
* **Batch size**
  : The only default hyperparameter that we change, setting to 1 per device due to the large model size and memory constraints.
* **Instance type**
  : We use a
  **ml.p4de.24xlarge**
  instance type for this training job and recommend that you use the same type or larger.
* **MLflow integration**
  : Automatically logs hyperparameters, job names, and training metadata for experiment tracking.
* **Endpoint deployment**
  : Automatically deploys each trained model to a SageMaker endpoint for inference.

Recall that the training process will take a few hours to complete using instance type
**ml.p4de.24xlarge.**

Now we’ll evaluate our fine-tuned models using the Average Normalized Levenshtein Similarity (ANLS) metric. This metric evaluates text-based outputs by measuring the similarity between predicted and ground truth answers, even when there are minor errors or variations. It is particularly useful for tasks like visual question answering because it can handle slight variations in answers. See the
[Llama 3.2 3B model card](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/)
for more information.

MLflow will track our experiments and results for straightforward comparison. Our evaluation pipeline includes several key functions for image encoding for model inference, payload formatting, ANLS calculation, and results tracking. The
`training_pipeline()`
function orchestrates the complete workflow with nested MLflow runs for better experiment organization.

```
# MLFlow configuration
arn = "" # replace with ARN of project's MLflow instance
mlflow.set_tracking_uri(arn)

def training_pipeline(training_size):
    # Set experiment
    experiment_name = f"docvqa-{training_size}"
    mlflow.set_experiment(experiment_name)

    # Start main run
    with mlflow.start_run(run_name="pipeline-run"):

        # DataPreprocess nested run
        with mlflow.start_run(run_name="DataPreprocess", nested=True):
            training_data_path = process_data("train", f"docvqa_{training_size}/train", training_size)

        # TrainDeploy nested run
        with mlflow.start_run(run_name="TrainDeploy", nested=True) as run:
            model_name = train(f"docvqa-{training_size}", "ml.p4d.24xlarge", training_data_path, experiment_name, run)
            #model_name = 'base-model'

        # Evaluate nested run
        with mlflow.start_run(run_name="Evaluate", nested=True):

            # Load validation data
            with open("./docvqa_1k/validation/metadata.jsonl") as f:
                data = [json.loads(line) for line in f]

            print(f"\nStarting validation for {model_name}")

            # Log parameters
            mlflow.log_param("model_name", model_name)
            mlflow.log_param("total_images", len(data[:50]))
            mlflow.log_param("threshold", 0.5)

            predictor = retrieve_default(model_id="meta-vlm-llama-3-2-11b-vision-instruct", model_version="*", endpoint_name=model_name)

            results = []
            anls_scores = []

            # Process each image
            for i, each in enumerate(data[:50]):
                filename = each['file_name']
                question = each["prompt"]
                ground_truth = each["completion"]
                image_path = f"./docvqa_1k/validation/{filename}"

                print(f"Processing {filename} ({i+1}/50)")

                # Get model prediction using traced function
                inferred_response = invoke_model(predictor, question, image_path)

                # Calculate ANLS score
                anls_score = anls_metric_single(inferred_response, ground_truth)
                anls_scores.append(anls_score)

                # Store result
                result = {
                    'filename': filename,
                    'ground_truth': ground_truth,
                    'inferred_response': inferred_response,
                    'anls_score': anls_score
                }
                results.append(result)

                print(f"  Ground Truth: {ground_truth}")
                print(f"  Prediction: {inferred_response}")
                print(f"  ANLS Score: {anls_score:.4f}")

            # Calculate average ANLS score
            avg_anls = sum(anls_scores) / len(anls_scores) if anls_scores else 0.0

            # Log metrics
            mlflow.log_metric("average_anls_score", avg_anls)

            # Save results to CSV
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            csv_filename = f"anls_validation_{model_name}_{timestamp}.csv"
            save_results_to_csv(results, csv_filename)

            # Log CSV as artifact
            mlflow.log_artifact(csv_filename)

            print(f"Results for {model_name}:")
            print(f"  Average ANLS Score: {avg_anls:.4f}")

            mlflow.log_param("metric_type", "anls")
            mlflow.log_param("threshold", "0.5")
```

After orchestrating three end-to-end executions for our three dataset sizes, we review the ANLS metric results in MLflow. Using the comparison functionality, we note the highest ANLS score of 0.902 in the docvqa-10000 model, an
**increase of 4.9 percentage points**
relative to the base model (0.902 − 0.853 = 0.049).

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/20/ML-19677-image-22.png)

|  |  |
| --- | --- |
| **Model** | **ANLS** |
| docvqa-1000 | 0.886 |
| docvqa-5000 | 0.894 |
| docvqa-10000 | 0.902 |
| *Base Model* | *0.853* |

## Clean Up

To avoid ongoing charges, delete the resources created during this walkthrough. This includes SageMaker endpoints and project resources such as the MLflow application, JupyterLab IDE, and domain.

## Conclusion

Based on the preceding data, we observe a positive relationship between the size of the training dataset and ANLS in that the docvqa-10000 model had improved performance.

We used MLflow for experimentation and visualization around our success metric. Further improvements in areas such as hyperparameter tuning and data enrichment could yield even better results.

This walkthrough demonstrates how the Amazon SageMaker Unified Studio integration with S3 general purpose buckets helps streamline the path from unstructured data to production-ready ML models. Key benefits include:

* Simplified data discovery and cataloging through a unified interface
* More secure data access through S3 Access Grants without complex permission management
* Smooth collaboration between data producers and consumers across projects
* End-to-end experiment tracking with managed MLflow integration

Organizations can now use their existing S3 data assets more effectively for ML workloads while maintaining governance and security controls. The
**4.9% performance improvement**
from base model to our improved fine-tuned variant (0.853–0.902 ANLS) validates the approach for visual question answering tasks.

For next steps, consider exploring additional dataset preprocessing techniques, experimenting with different model architectures available through SageMaker JumpStart, or scaling to larger datasets as your use case demands.

The solution code used for this blog post can be found in
[this GitHub repository](https://github.com/aws-samples/sample-finetuning-sagemaker-unified-studio-with-s3)
.

---

## About the authors