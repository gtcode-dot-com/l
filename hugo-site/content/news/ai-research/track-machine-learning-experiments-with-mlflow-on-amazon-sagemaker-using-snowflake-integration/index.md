---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-18T00:03:45.838634+00:00'
exported_at: '2025-12-18T00:03:49.579188+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/track-machine-learning-experiments-with-mlflow-on-amazon-sagemaker-using-snowflake-integration
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate how to integrate Amazon SageMaker managed
    MLflow as a central repository to log these experiments and provide a unified
    system for monitoring their progress.
  headline: Track machine learning experiments with MLflow on Amazon SageMaker using
    Snowflake integration
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/track-machine-learning-experiments-with-mlflow-on-amazon-sagemaker-using-snowflake-integration
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Track machine learning experiments with MLflow on Amazon SageMaker using Snowflake
  integration
updated_at: '2025-12-18T00:03:45.838634+00:00'
url_hash: 3b585416ef6d85d9dd568857bbea3c2835671904
---

A user can conduct machine learning (ML) data experiments in data environments, such as
[Snowflake](https://aws.amazon.com/financial-services/partner-solutions/snowflake/)
, using the
[Snowpark library](https://docs.snowflake.com/en/developer-guide/snowpark/index)
. However, tracking these experiments across diverse environments can be challenging due to the difficulty in maintaining a central repository to monitor experiment metadata, parameters, hyperparameters, models, results, and other pertinent information. In this post, we demonstrate how to integrate
[Amazon](https://aws.amazon.com/sagemaker/)
[SageMaker](https://aws.amazon.com/sagemaker/)
managed
[MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
as a central repository to log these experiments and provide a unified system for monitoring their progress.

Amazon SageMaker managed MLflow offers fully managed services for experiment tracking, model packaging, and model registry. The
[SageMaker Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
streamlines model versioning and deployment, facilitating seamless transitions from development to production. Additionally, integration with
[Amazon S3](https://aws.amazon.com/s3/)
,
[AWS Glue](https://aws.amazon.com/glue/)
, and
[SageMaker Feature Store](https://aws.amazon.com/sagemaker/ai/feature-store/)
enhances data management and model traceability. The key benefits of using MLflow with SageMaker are that it allows organizations to standardize ML workflows, improve collaboration, and accelerate artificial intelligence (AI)/ML adoption with a more secure and scalable infrastructure. In this post, we show how to integrate Amazon SageMaker managed MLflow with Snowflake.

Snowpark allows Python, Scala, or Java to create custom data pipelines for efficient data manipulation and preparation when storing training data in Snowflake. Users can conduct experiments in Snowpark and track them in Amazon SageMaker managed MLflow
**.**
This integration allows data scientists to run transformations and feature engineering in Snowflake and utilise the managed infrastructure within SageMaker for training and deployment, facilitating a more seamless workflow orchestration and more secure data handling.

## Solution overview

The integration leverages Snowpark for Python, a client-side library that allows Python code to interact with Snowflake from Python kernels, such as SageMaker’s Jupyter notebooks. One workflow could include data preparation in Snowflake, along with feature engineering and model training within Snowpark. Amazon SageMaker managed MLflow can then be used for experiment tracking and model registry integrated with the capabilities of SageMaker.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190531.png)

*Figure 1: Architecture diagram*

## Capture key details with MLflow Tracking

**MLflow Tracking**
is important in the integration between
**SageMaker, Snowpark,**
and
**Snowflake**
by providing a centralized environment for logging and managing the entire machine learning lifecycle. As Snowpark processes data from Snowflake and trains models, MLflow Tracking can be used to capture key details including model parameters, hyperparameters, metrics, and artifacts. This allows data scientists to monitor experiments, compare different model versions, and verify reproducibility. With
**MLflow’s versioning and logging capabilities**
, teams can seamlessly trace the results back to the specific dataset and transformations used, making it simpler to track the performance of models over time and maintain a transparent and efficient ML workflow.

This approach offers several benefits. It allows for scalable and managed MLflow tracker in
**SageMaker**
, while utilizing the processing capabilities of
**Snowpark**
for model inference within the Snowflake environment, creating a unified data system. The workflow remains within the Snowflake environment, which enhances data security and governance. Additionally, this setup helps to reduce cost by utilizing the elastic compute power of Snowflake for inference without maintaining a separate infrastructure for model serving.

## Prerequisites

Create/configure the following resources and confirm access to the aforementioned resources prior to establishing Amazon SageMaker MLflow:

1. A
   [Snowflake account](https://signup.snowflake.com/)
2. An
   [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket)
   to track experiments in MLflow
3. An
   [Amazon SageMaker Studio account](https://aws.amazon.com/sagemaker/?trk=9b6a9bdc-e8cb-4e94-baa6-b5a64db47867&sc_channel=ps&ef_id=CjwKCAjw1ozEBhAdEiwAn9qbzVQiACWUS47XtktOAO1wGQ9Q82akJ_JpqlItSuFDe6xWTaqF3LyUcRoCUMYQAvD_BwE:G:s&s_kwcid=AL!4422!3!638364450172!p!!g!!aws%20sagemaker%20machine%20learning!19090032234!144545289552&gad_campaignid=19090032234&gbraid=0AAAAADjHtp86meyTqN4OK0DendyGb7Vsz&gclid=CjwKCAjw1ozEBhAdEiwAn9qbzVQiACWUS47XtktOAO1wGQ9Q82akJ_JpqlItSuFDe6xWTaqF3LyUcRoCUMYQAvD_BwE)
4. An
   [AWS Identity and Access Management](https://aws.amazon.com/iam/)
   (IAM) role that is an
   [Amazon SageMaker Domain Execution Role](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/AmazonSageMakerDomainExecution.html)
   in the AWS account.
5. A new user with permission to access the S3 bucket created above;
   [follow these steps](https://docs.aws.amazon.com/AmazonS3/latest/userguide/walkthrough1.html)
   .
   1. Confirm access to an AWS account through the
      [AWS Management Console](http://aws.amazon.com/console)
      and
      [AWS Command Line Interface](https://aws.amazon.com/cli)
      (AWS CLI). The
      [AWS Identity and Access Management](https://aws.amazon.com/iam)
      (IAM) user must have permissions to make the necessary AWS service calls and manage AWS resources mentioned in this post. While providing permissions to the IAM user, follow the
      [principle of least-privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
      .
6. Configure access to the Amazon S3 bucket created above following
   [these steps.](https://docs.snowflake.com/en/user-guide/tables-external-s3#step-1-configure-access-permissions-for-the-s3-bucket)
7. Follow
   [these steps](https://docs.snowflake.com/en/user-guide/ui-snowsight/notebooks-external-access?utm_source=chatgpt.com)
   to set up external access for Snowflake Notebooks.

### Steps to call SageMaker’s MLflow Tracking Server from Snowflake

We now establish the Snowflake environment and connect it to the Amazon SageMaker MLflow Tracking Server that we previously set up.

4. Follow these steps to create an Amazon SageMaker Managed MLflow Tracking Server in
   [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html)
   .
5. Log in to Snowflake as an admin user.
6. Create a new Notebook in
   [Snowflake](https://signup.snowflake.com/?utm_cta=trial-en-www-homepage-top-right-nav-ss-evg&_ga=2.74406678.547897382.1657561304-1006975775.1656432605&_gac=1.254279162.1656541671.Cj0KCQjw8O-VBhCpARIsACMvVLPE7vSFoPt6gqlowxPDlHT6waZ2_Kd3-4926XLVs0QvlzvTvIKg7pgaAqd2EALw_wcB)
   1. Projects > Notebooks > +Notebook
   2. Change role to a non-admin role
   3. Give a name, select a database (DB), schema, warehouse, and select ‘Run on container’

      ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190532_cens.png)
   4. Notebook settings > External access> toggle on to allow all integration
7. Install libraries
   1. `!pip install sagemaker-mlflow`
8. Run the MLflow code, by replacing the arn value from the below code:

   ```
   import mlflow
   import boto3
   import logging

   sts = boto3.client("sts")
   assumed = sts.assume_role(
   RoleArn="<AWS-ROLE-ARN>",
   RoleSessionName="sf-session"
   )
   creds = assumed["Credentials"]

   arn = "<ml-flow-arn>"

   try:
   mlflow.set_tracking_uri(arn)
   mlflow.set_experiment("Default")
   with mlflow.start_run():
   mlflow.log_param("test_size", 0.2)
   mlflow.log_param("random_state", 42)
   mlflow.log_param("model_type", "LinearRegression")
   except Exception as e:
   logging.error("Failed to set tracking URI: {e}")
   ```

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190533.png)

*Figure 3: Install sagemaker-mlflow library*

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190534.png)

*Figure 4: Configure MLflow and do experiments.*

On a successful run, the experiment can be tracked on Amazon SageMaker:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190535.png)

*Figure 5: Track experiments in SageMaker MLflow*

To get into details of an experiment, click on the respective “Run name:”

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/ml-190536.png)

*Figure 6: Experience detailed experiment insights*

## Clean up

Follow these steps to clear up the resources that we have configured in this post to help avoid ongoing costs.

1. Delete the
   [SageMaker Studio account](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/delete-project.html)
   by following these steps, this deletes the MLflow tracking server as well
2. Delete the
   [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-bucket.html)
   with its contents
3. Drop the Snowflake
   [notebook](https://docs.snowflake.com/en/sql-reference/sql/drop-notebook)
4. Verify that the Amazon SageMaker account is deleted

## Conclusion

In this post, we explored how Amazon SageMaker managed MLflow can provide a comprehensive solution for managing a machine learning lifecycle. The integration with Snowflake through Snowpark further enhances this solution, helping to enable seamless data processing and model deployment workflows.

To get started, follow the
[step-by-step instructions](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html)
provided above to set up MLflow Tracking Server in Amazon SageMaker Studio and integrate it with Snowflake. Remember to follow AWS security best practices by implementing proper IAM roles and permissions and securing all credentials appropriately.

The code samples and instructions in this post serve as a starting point – they can be adapted to match a specific use cases and requirements while maintaining security and scalability best practices.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/mrankit_hq-100x150.jpeg)
**Ankit Mathur**
is a Solutions Architect at AWS focused on modern data platforms, AI-driven analytics, and AWS–Partner integrations. He helps customers and partners design secure, scalable architectures that deliver measurable business outcomes.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/marhoov_hq-100x133.jpg)
**Mark Hoover**
is a Senior Solutions Architect at AWS where he is focused on helping customers build their ideas in the cloud. He has partnered with many enterprise clients to translate complex business strategies into innovative solutions that drive long-term growth.