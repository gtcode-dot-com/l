---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T00:00:18.275019+00:00'
exported_at: '2025-11-26T00:00:22.032661+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/train-custom-computer-vision-defect-detection-model-using-amazon-sagemaker
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate how to migrate computer vision workloads
    from Amazon Lookout for Vision to Amazon SageMaker AI by training custom defect
    detection models using pre-trained models available on AWS Marketplace. We provide
    step-by-step guidance on labeling datasets with SageMaker Ground Truth, training
    models with flexible hyperparameter configurations, and deploying them for real-time
    or batch inference—giving you greater control and flexibility for automated quality
    inspection use cases.
  headline: Train custom computer vision defect detection model using Amazon SageMaker
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/train-custom-computer-vision-defect-detection-model-using-amazon-sagemaker
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Train custom computer vision defect detection model using Amazon SageMaker
updated_at: '2025-11-26T00:00:18.275019+00:00'
url_hash: 29fd91090e8ef09dcc80dd3dc50acef3ce51db49
---

On October 10, 2024, Amazon announced the discontinuation of the
[Amazon Lookout for Vision](https://aws.amazon.com/lookout-for-vision/features/)
service, with a scheduled shut down date of October 31, 2025 (see
[Exploring alternatives and seamlessly migrating data from Amazon Lookout for Vision](https://aws.amazon.com/blogs/machine-learning/exploring-alternatives-and-seamlessly-migrating-data-from-amazon-lookout-for-vision/)
blog post). As part of our transition guidance for customers, we recommend the use of
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/)
tools to build applications for customers who are interested in AI/ML computer vision models for automated quality inspection use cases. To support that effort, AWS has made a pre-trained
[computer vision defect detection model](https://aws.amazon.com/marketplace/pp/prodview-j72hhmlt6avp6)
available on AWS Marketplace that can be fine-tuned using Amazon SageMaker AI for a customer’s specific use case. If run in the cloud, this model only requires paying for infrastructure costs for training or inference. This approach provides the tools to accelerate solution development while facilitating complete flexibility to build a solution that integrates with any existing hardware and software infrastructure.

In this blog post, you will learn how to migrate your computer vision workloads from Amazon Lookout for Vision to Amazon SageMaker AI by following our step-by-step guidance.

AWS is sharing the
[main underlying models](https://aws.amazon.com/marketplace/pp/prodview-j72hhmlt6avp6)
used for the service to end users in the AWS Marketplace. You can use the two main types of models,
*binary classification*
and
*semantic segmentation*
, when you train in your own AWS accounts for deployment on AWS or at the edge.

This model helps customers continue to use AWS defect detection technology at their own pace with greater flexibility. For example, you can train your models with larger instance types for faster training times. With access to set hyperparameters, you can also adjust model behavior that was not previously available on the AWS console. For example, you can set the multi-head model for semantic segmentation to disable the binary classifier head. This can make the model mode more tolerant of changing background and lighting conditions. You can also personalize the maximum training time, which was set to a non-changeable 24-hour limit on Amazon Lookout for Vision (L4V).

The
[GitHub repository for Amazon Lookout for Vision](https://github.com/aws-samples/amazon-lookout-for-vision/tree/main/computer-vision-defect-detection)
has been updated with a Jupyter Notebook to help you train datasets with these two model types and package them up. From there you can deploy the models by using a SageMaker endpoint, or edge devices.

To label the images beyond the sample data, you can use
[Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker-ai/groundtruth/)
to enable crowdsourcing or allow private teams to label the data, or use a partner solution such as
[Edge Impulse](https://edgeimpulse.com/)
,
[Roboflow](https://roboflow.com/)
, or
[SuperbAI](https://superb-ai.com/en)
to do so. When you have the manifest file of the labeled data, the marketplace models can be used for training. You will lose a thumbnail-based dataset management tool like the Amazon Lookout for Vision console, so consider one of the previously mentioned partner solutions to help manage datasets. You can also export your existing data from the Lookout For Vision service using
[this](https://docs.aws.amazon.com/code-library/latest/ug/lookoutvision_example_lookoutvision_Scenario_ExportDatasets_section.html)
guide.

## Prerequisites

Before you begin, make sure you have the following components and permissions in place:

* Amazon SageMaker Studio or Amazon SageMaker Unified Studio for integrated development environment (IDE)
* AWS Identity and Access Management (IAM) role with these permissions to follow the principle of least privilege
  + Amazon S3
    - s3:GetObject
    - s3:PutObject
    - s3:DeleteObject
    - s3:ListBucket
  + SageMaker
    - sagemaker:CreateTrainingJob
    - sagemaker:CreateModel
    - sagemaker:CreateEndpoint
    - sagemaker:CreateEndpointConfig
    - sagemaker:CreateTransformJob
    - sagemaker:DescribeTrainingJob
    - sagemaker:DescribeModel
    - sagemaker:DescribeEndpoint
    - sagemaker:DescribeEndpointConfig
    - sagemaker:DescribeTransformJob
    - sagemaker:InvokeEndpoint
    - sagemaker:DeleteEndpoint
    - sagemaker:DeleteEndpointConfig
    - sagemaker:DeleteModel
* Model subscription:
  + An AWS account with a subscription to
    [Computer Vision Defect Detection Model](https://aws.amazon.com/marketplace/pp/prodview-j72hhmlt6avp6)
    or
  + An IAM role with these three permissions permission to make AWS Marketplace subscriptions in the AWS account you use:
    - aws-marketplace:ViewSubscriptions
    - aws-marketplace:Unsubscribe
    - aws-marketplace:Subscribe
* Labeled data (you can use the cookie data sample in Github) or label your own data with SageMaker Ground Truth or an AWS Partner tool
* Basic knowledge of creating a SageMaker notebook instance and running Jupyter notebook

## Architecture overview

The following diagram illustrates the end-to-end flow, from image acquisition to inferencing at the edge. This blog focus on steps 2 and 3.

![](images/image-1.png)
![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-1-6.png)

1. Use an edge application to configure cameras or sensors and capture training images.
2. Use SageMaker GroundTruth or AWS Partner platforms to export and label images.
3. Use Amazon SageMaker AI for model training.
4. Use REST, PLC, or digital input for image acquisition and processing.
5. Run real-time inference using the trained and deployed model.
6. Publish inference results to analytics and monitoring for alerts and analytics.
7. Perform automated action on the machine of concern or notify plant personnel of anomalies from inspection station component using OPC-UA or digital output.
8. Line operators and plant managers receive notifications for action.

## Set up the labeling process

This section covers the steps to set up the labeling process using Amazon SageMaker Ground Truth, including creating a private labeling team and configuring the labeling job.

1. Configure Amazon SageMaker Ground Truth private team:
   1. Select
      **Amazon SageMaker AI**
      ,
      **Ground Truth**
      ,
      **Labeling workforces**
      .
   2. Select
      **Private**
      , then
      **Create Private Team.**
   3. Enter a team name.
   4. Leave other values as their defaults.
   5. Select
      **Create a new Amazon Cognito user group.**
   6. Select
      **Create private Team.**
2. On the
   **Workers**
   tab, select
   **Invite New Workers**
   .
3. Enter your team members’ email addresses to send sign-up invitations.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-3-1.jpeg)

## Label the dataset

After successfully completing the workforce setup for labelling, the next step is to label the dataset. This section explains how to prepare the dataset by uploading the images to an Amazon Simple Storage Service (Amazon S3) bucket, then create and run the SageMaker Ground Truth labeling job to label the images as
**normal**
or
**anomaly**
.

1. Upload the image datasets to an Amazon S3 bucket that SageMaker Ground Truth can access. If you don’t have a dataset, you can use either the
   [cookie-dataset](https://github.com/aws-samples/amazon-lookout-for-vision/tree/main/computer-vision-defect-detection/cookie-dataset)
   or
   [aliens-dataset](https://github.com/aws-samples/amazon-lookout-for-vision)
   .
2. In the AWS Console, navigate to
   **Amazon SageMaker AI**
   ,
   **Ground Truth**
   ,
   **Labeling Jobs,**
   **Create labeling job**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-4-1-1024x1024.jpeg)

3. There are several options here to fill in; the most important fields to fill or select are:
   * Input data setup: Select
     **Automated data setup**
   * S3 location for input datasets: <Full path where your dataset exists>
   * S3 location data output datasets: <Same location as input dataset>
   * Data type: Select
     **Image**
   * IAM Role – Select
     **Create new role**
     if you do not have one set up to allow Ground Truth to interact with SageMaker services.
4. Choose
   **Complete data setup**
   . An Input
   **data connection successful**
   message displays. If you get an error, check your IAM role to make sure S3 access is enabled, and the directory has image files in it, as it will not recurse through sub-directories.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-5-1024x229.jpeg)

5. Select the task type. These models support
   **Image Classification (Single Label)**
   , which is binary classification (think good or bad), or
   **Semantic segmentation**
   . You cannot use a bounding box type with these models. You can change your selection later.
6. Choose
   **Next.**
7. For
   **Worker types**
   , select
   **Private**
   . You can read more about Amazon Mechanical Turks or labeling subscriptions in the
   [Developer Guide](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management.html)
   .
8. Under
   **Private teams**
   , select the private team you created in the previous steps.
9. For
   **Task timeout**
   and
   **Task expiration time**
   , leave the default values.
10. Leave
    **Enable automated data labeling**
    unselected. You can read more about automated data labeling
    [here](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html)
    ; however, it is not compatible with semantic segmentation.
11. On the
    **Image classification**
    screen, add two new labels:
    **normal**
    and
    **anomaly**
    . You can fill in the rest as needed. Choose
    **Preview**
    to see a preview of what it will look like to the end user.
12. Choose
    **Create**
    .
    ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-6.jpeg)
13. Select
    **Ground Truth,**
    and then select the
    **Private**
    tab.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-7-3.png)

14. Open the labeling portal sign-in URL in a new tab in your browser and then sign in to see your assigned tasks.
15. Select an assigned task and choose
    **Start working**
    to label the data.
16. Select
    **normal**
    or
    **anomaly**
    .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-8-2.png)

17. When the job is complete, make note of the
    **output dataset location**
    . You will need this for the training step.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/11/17.png)

18. If you need to add workers to the labelling job:
    1. On the
       **Amazon SageMaker AI Ground Truth**
       page, select
       **Labeling workforces.**
    2. Select the
       **Private**
       tab.
    3. Click on the private team that was created earlier (CV-team).
    4. Select the
       **Workers**
       tab
    5. Select the desired worker from the list and choose
       **Add workers to team**
       .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-10.jpeg)

* 6. You will then be redirected to the Amazon SageMaker AI, labelling workforces page with a confirmation message that worker has been added.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-11-2.png)

After you complete the labeling task, the output of the task is used to train the Computer Vision Detection model from the AWS Marketplace.

## Train the model

This section discusses training the computer vision model using the AWS Marketplace Computer Vision Detection model and the labeled dataset from the previous step.

1. Go to the AWS Marketplace to subscribe to the model,
   <https://aws.amazon.com/marketplace/pp/prodview-j72hhmlt6avp6>
   .
2. Choose
   **Continue to Subscribe**
   .
3. Choose
   **Continue to configuration**
   .
4. Select the latest software version, your Region, and make sure
   **Create a training job**
   is selected.

**Note:**
Copy the
**Product Arn**
and store in a text editor or notepad for later use.

5. Go to
   **SageMaker AI**
   ,
   **Notebook instances**
   ,
   **Create notebook instance.**

**Note**
: GPU-enabled notebook instance is not required. Amazon SageMaker Training jobs will spin up the GPU instances needed during training, so most basic instances will be sufficient.

6. Select
   **m5.2xl instance, Jupyter lab 4**
   , with volume size of 128 GB. The default is 5 GB, which is too small.
7. Select an IAM role to allow the notebook to access resources in your account. You will need access to S3.
8. In the
   **Git Repositories – optional**
   section, select
   **Clone a public Git repository to this notebook instance only**
   .
9. Enter the Git repository URL. Leave all the other fields as their default, then choose
   **Create notebook instance**
   to start the instance.
10. After the instance starts, (the status will display as
    **InService)**
    , select
    **Open JupyterLab**
    action for the new notebook instance.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/11/10.png)

JupyterLab opens:

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-13-1.jpeg)

11. On the left navigation pane, open the
    **computer-vision-defect-detection**
    folder.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-14-2.png)

12. In the AWS Console, go to
    **Marketplace**
    ,
    **Manage subscriptions**
    , and then copy the ARN of your model subscription.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/image-15-1.jpeg)

13. In the Jupyter notebook, locate the snippet below and update the placeholder value for
    **algorithm\_name**
    variable with the Product Arn you copied in the previous step.

```
# TODO: change this to use subscribed SageMaker algorithm algorithm_name = "<Customer to specify the algorithm name after subscription >"
```

The bucket that would be used for this step would be automatically created and named in the format
**SageMaker-<REGION>-<ACCOUNT\_ID>**
.

```
# Initialize SageMaker session and get execution role
sagemaker_session = sagemaker.Session()
region = sagemaker_session.boto_region_name
#bucket = sagemaker_session.default_bucket()
role = get_execution_role()
# Project name would be used as part of s3 output path
project = "ComputerVisionDefectDetection”
```

14. In the AWS Console, navigate to Amazon SageMaker AI, Ground Truth, Labeling jobs and select the job that was completed.
15. Identify and take note of the output images folder (
    **Output dataset location**
    )

**Note**
: To start the training job, look at the path for the output manifest in
**<BUCKET NAME>/aliens-dataset/all/aliensv2/manifests/output/output.manifest—**
this will be the training manifest for the next step.

16. Set the
    **bucket**
    variable to be the images bucket name that you previously set and object key the path to your manifest:
    * **bucket**
      : where to store the manifest file
    * **classification\_manifest\_key**
      : where the output manifest file is stored (for example,
      **aliens-dataset-all/[job-name]/manifests/output/output.manifest**
      )
17. Review the model training configuration in the
    **Classification Model with Algorithm Estimator**
    section.

```
# Create AlgorithmEstimator for classificatio
classification_estimator = AlgorithmEstimator(
algorithm_arn=algorithm_name,
role=role, instance_count=1,
instance_type='ml.g4dn.2xlarge',
volume_size=20, max_run=7200,
input_mode='Pipe', # REQUIRED: Algorithm only supports Pipe mode
sagemaker_session=sagemaker_session,
enable_network_isolation=True
)

# Set hyperparameters
classification_estimator.set_hyperparameters(
ModelType='classification',
TestInputDataAttributeNames='source-ref,anomaly-label-metadata,anomaly-label',
TrainingInputDataAttributeNames='source-ref,anomaly-label-metadata,anomaly-label')

print("Classification estimator configured successfully")</code></pre><pre><code class="lang-python"># Define training input using TrainingInput class
classification_training_input = TrainingInput(
s3_data=classification_s3_path, '
s3_data_type='AugmentedManifestFile',
attribute_names=[
'source-ref',
'anomaly-label-metadata',
'anomaly-label'
],
record_wrapping='RecordIO',
input_mode='Pipe' # Must match the estimator's input_mode)
# Start training job
classification_job_name = f'defect-detection-classification-
{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}
'print(f"Starting classification training job: {classification_job_name}")
classification_estimator.fit(
inputs={'training': classification_training_input},
job_name=classification_job_name,
wait=True,
logs=True

)
```

**Note**
: The job uses NVIDIA G4DN instances. They can be sized up to a larger instance to decrease training time, but on a only 118 instances. The image dataset training finishes in less than 10 minutes with a g4dn.2xl. You can experiment with other instance types, however results may vary because the models were extensively tested on the G4DN instances.

18. Validate the values of TestInputDataAttributeNames and TrainingInputDataAttributeNames in the
    **Hyperparameters**
    section, as well as AttributeNames in the

**TrainingInput**
section. The labels on all three must match the structure of your manifest file. Here is a sample manifest:

```
{
    "source-ref": "s3://[bucketname]/getting-started/training-images/anomaly-1.jpg",
    "anomaly-label-metadata": {
        "job-name": "anomaly-label",
        "class-name": "anomaly",
        "human-annotated": "yes",
        "creation-date": "2022-08-22T20:52:51.851Z",
        "type": "groundtruth/image-classification"
    },
    "anomaly-label": 1
}
{
    "source-ref": "s3://[bucketname]/getting-started/training-images/anomaly-2.jpg",
    "anomaly-label-metadata": {
        "job-name": "anomaly-label",
        "class-name": "anomaly",
        "human-annotated": "yes",
        "creation-date": "2022-08-22T21:11:39.545Z",
        "type": "groundtruth/image-classification"
    },
    "anomaly-label": 1
}
```

**Note**
: Two of the three values include the labelling job name.

```
response = sagemaker.create_training_job(
    TrainingJobName=classification_training_job_name,
    HyperParameters={
        'ModelType': 'classification',
        'TestInputDataAttributeNames': 'source-ref,aliens-v3,aliens-v3-metadata',
        'TrainingInputDataAttributeNames': 'source-ref,aliens-v3,aliens-v3-metadata'
    }
)
```

19. Run all the cells or blocks listed in the
    **Classification Model with Algorithm Estimator**
    section to start the training job.
20. If you want to train a segmentation model as well, follow the steps in the
    **Segmentation Model with Algorithm Estimator**
    section.

Note: After the training is completed, you are ready to test it!  There are few inference options available for this:

* Real-time inference using Amazon SageMaker endpoints
* Amazon SageMaker AI Batch Transform inference.
* Edge deployment

## Deploy the model

Amazon SageMaker AI endpoints and Amazon SageMaker AI Batch Transform inference are both used for inference but serve different purposes.

### **Amazon SageMaker AI endpoints**

Amazon SageMaker AI endpoints are used for real-time inference, providing low-latency predictions suitable for applications requiring immediate responses. Endpoints remain active while they’re deployed, making them better suited for continuous and steady traffic, but potentially more costly due to ongoing resource usage.

1. In the Jupyter notebook, navigate to the
   **(Optional) Running real-time inference using Amazon SageMaker endpoints**
   section.
2. Run the following cell blocks to set up and invoke the endpoint:

```
#classification_training_job_name = "defect-detection-classification-2025-10-01-00-29-57" # remove

classification_training_job_name = "<provide training job name here>"

# Create estimator from training job
estimator = AlgorithmEstimator.attach(classification_training_job_name)

# Deploy endpoint using SageMaker v2 SDK
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type='ml.c5.2xlarge'
)

print(f"Endpoint deployed: {predictor.endpoint_name}")

#Invoke the endpoint

    # Invoke the endpoint using predictor
    result = predictor.predict(image_data)

    # Clean up the temporary file
    os.remove(local_file)

    # Print the result
    print("\nEndpoint Response:")
    print(json.dumps(result, indent=2))
```

3. Validate the inference, then delete the endpoint by running the following block:

```
# Delete the endpoint

predictor.delete_endpoint()
print("Endpoint deleted")
```

Note: If you start an endpoint, keep in mind you will be billed while it is running until you turn it off.

### **Amazon SageMaker AI Batch Transform**

Batch Transform is designed for offline inference and making predictions on large datasets stored in S3, and is ideal for bulk processing where low latency is not critical. After the job is complete, the resources are released, making it cost-effective for sporadic workloads.

1. Navigate to the
   **(Optional) Run Batch Transform Inference using SageMaker SDK v2**
   section.
2. Define the s3\_input\_data and s3\_output\_path parameters.

```
# Run batch transform job

#############################################
# Change to your input/output data S3 path  #
#############################################

s3_input_data = "s3://<Specify-s3-path-to-test-images>"
s3_output_path = f"s3://{bucket}/{project}/batch-transform-output"
```

3. Run all the cells and blocks in the
   **(Optional) Run Batch Transform Inference using SageMaker SDK v2**
   section to complete the batch inference.
4. Validate the batch transform job after completion by navigating to the
   **s3\_output\_path**
   folder. The following is a sample inference output file:

```
{
    "Source": {
        "Type": "direct"
    },
    "IsAnomalous": true,
    "Confidence": 0.92744799389183
}
```

## Clean up

To avoid incurring unnecessary charges, delete the following resources when you no longer need them:

1. Delete SageMaker endpoints.
   1. Navigate to the Amazon SageMaker Console.
   2. Select
      **Endpoints.**
   3. Select the endpoint you created.
   4. Choose
      **Delete.**
2. Delete SageMaker Notebook instances.
   1. Navigate to the Amazon SageMaker Console.
   2. Select
      **Notebook instances.**
   3. Select the notebook instance you created.
   4. Choose
      **Stop if the instance is running.**
   5. Once stopped, choose
      **Delete.**
3. Delete S3 objects and buckets.
   1. Navigate to the Amazon S3 Console.
   2. Delete all objects in the buckets you created for this tutorial.
   3. Delete the empty buckets.
4. Delete the Ground Truth labeling team.
   1. Navigate to Ground Truth.
   2. Select
      **Labeling workforces.**
   3. Select the
      **Private**
      tab.
   4. Select the private team you created.
   5. Choose
      **Delete team.**

## Conclusion

In this blog post, we’ve demonstrated how to transition from Amazon Lookout for Vision to using the underlying Computer Vision Detection models available through the AWS Marketplace, showing the step-by-step process of setting up labeling, training the model, and running inference through batch transformation. The transition provides customers with greater flexibility in terms of training options, hyperparameter adjustments, and deployment choices while continuing to use AWS defect detection technology at their own pace. Also be sure to check out our edge-based open source integrated
[Defect Detection Application](https://github.com/awslabs/DefectDetectionApplication)
on GitHub if you would like to combine what you have learned here.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/Ryan-1-100x133.jpeg)
**Ryan Vanderwerf**
is a is a senior partner solutions architect at Amazon Web Services specializing in smart manufacturing, vision, and machine learning. Ryan previously provided Java virtual machine-focused consulting and project development as a software engineer at OCI on the Grails and Micronaut team. He was chief architect/director of products at ReachForce, with a focus on software and system architecture for AWS Cloud SaaS solutions for marketing data management. Ryan has built several SaaS solutions in several domains such as financial, media, telecom, and e-learning companies since 1996

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/Lu-100x133.jpeg)
**Lu Min**
is a Software Development Engineer for AWS Edge ML services, focused on developing machine learning solutions that operate at the edge for AWS customers. With expertise in optimizing ML models for resource-constrained environments, Lu helps customers implement efficient inference capabilities on edge devices and cloud communication, as well as manage model lifecycle using AWS SageMaker.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/Tim.png)
**Tim Westman**
is the Product Manager and Go-to-Market Lead for Edge Machine Learning, AWS. Tim leads the Product Management and Business Development for the Edge Machine Learning business at Amazon Web Services. In this role, he works with customers to help build computer vision solutions at the edge to solve complex operational challenges. Tim has more than 30 years of experience in sales, business development and product management roles for leading hardware and software companies, with the last 8 years specializing in AI and computer vision for IoT applications.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/10/kunle-94x150.jpeg)
**Kunle Adeleke**
is an enterprise solutions architect, providing guidance to large AWS commercial customers in diverse industries craft their technology strategy. Kunle has led enterprise architecture teams and software development teams in both government and commercial sectors. His deep expertise spans software development, solution architecture, enterprise architecture, security, and data & AI/ML.