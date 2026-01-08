---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-08T21:28:43.329282+00:00'
exported_at: '2026-01-08T21:28:45.821369+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/speed-meets-scale-load-testing-sagemakerai-endpoints-with-observe-ais-testing-tool
structured_data:
  about: []
  author: ''
  description: Observe.ai developed the One Load Audit Framework (OLAF), which integrates
    with SageMaker to identify bottlenecks and performance issues in ML services,
    offering latency and throughput measurements under both static and dynamic data
    loads. In this blog post, you will learn how to use the OLAF utility to test and
    validate your SageMaker endpoint.
  headline: 'Speed meets scale: Load testing SageMakerAI endpoints with Observe.AI’s
    testing tool'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/speed-meets-scale-load-testing-sagemakerai-endpoints-with-observe-ais-testing-tool
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Speed meets scale: Load testing SageMakerAI endpoints with Observe.AI’s testing
  tool'
updated_at: '2026-01-08T21:28:43.329282+00:00'
url_hash: 066c21874fd85c0e55ba576c637280f148743cb1
---

*This post is cowritten with Aashraya Sachdeva from Observe.ai.*

You can use
[Amazon SageMaker](https://aws.amazon.com/sagemaker)
to build, train and deploy machine learning (ML) models, including large language models (LLMs) and other foundation models (FMs). This helps you significantly reduce the time required for a range of generative AI and ML development tasks. An AI/ML development cycle typically involves data pre-processing, model development, training, testing and deployment lifecycles. By using SageMaker, your data science and ML engineering teams can offload a lot of the undifferentiated heavy lifting involved with model development.

While SageMaker can help teams offload a lot of heavy lifting, engineering teams still have to use manual steps to implement and fine-tune related services that are part of inference pipelines, such as queues and databases. In addition, teams have to test multiple GPU instance types to find the right balance between performance and cost.

[Observe.ai](https://www.observe.ai/)
provides a Conversation Intelligence (CI) product that integrates with contact center as a service (CCaaS) solutions. The tool analyzes calls in real time and after they’re complete to enable features such as call summarizations, agent feedback, and auto response . The Conversation Intelligence (CI) features need to scale from customers that have fewer than 100 agents to customers that have thousands of agents—a tenfold increase in scale. To help with this, Observe.ai needed a mechanism to optimize their ML infrastructure and model serving costs. Without such a mechanism, developers had to write multiple test scripts and develop testing pipelines and debugging systems, which consumed a lot of time.

To solve this challenge, Observe.ai developed the One Load Audit Framework (OLAF), which integrates with SageMaker to identify bottlenecks and performance issues in ML services, offering latency and throughput measurements under both static and dynamic data loads. The framework also seamlessly incorporates ML performance testing into the software development lifecycle, facilitating accurate provisioning and cost savings. Using OLAF, Observe.AI’s ML team was able to reduce testing time from a week to a few hours. This helped Observe.AI scale up their frequency of endpoint deployment and customer onboarding multifold. The OLAF utility is available on
[GitHub](https://github.com/Observeai-Research/olaf.git)
and is free to use. It is open source and distributed under the Apache 2.0 license.

In this blog post, you will learn how to use the OLAF utility to test and validate your SageMaker endpoint.

## Solution overview

After you’ve deployed your model for inference and verified that it’s functionally accurate, you’ll want to improve the performance of your model. The first step to do this is to load test the inference endpoint. You can use the load test metrics to apply optimizations to your model, decide on GPU instances, and fine tune the ML pipeline to increase performance without compromising on accuracy. Load testing needs to be repeated multiple times to measure the impact of any optimization. To load test, you need to configure load testing scripts to integrate with the relevant SageMaker APIs, extract metrics like latency, CPU, and memory utilization. You also need to set up a dashboard to view the results of the load test and, export the load test metrics for further analysis; and you need a configurable framework to apply concurrent load to the endpoint.

### How OLAF helps

OLAF saves you the heavy lifting by providing the preceding elements as a
[package](https://github.com/Observeai-Research/olaf.git)
. OLAF is integrated with
[Locust](https://locust.io/)
, a load testing framework, to provide the capability to create concurrent load and a dashboard to view the results as the test progresses. OLAF integrates with the SageMaker API to invoke the API and to extract the metrics to measure the performance by.

In the following solution, you will learn how to deploy OLAF on your workstation as a Docker container. Using the Load test setup UI (as shown in the following figure), the load test configuration is provided and the OLAF framework uses the Boto3 SDK to push inference requests to a SageMaker inference endpoint. OLAF monitors the latency and available performance metrics using the Performance reports dashboard provided by OLAF.

![End-to-end testing architecture showing Docker-based OLAF load generator interfacing with SageMaker endpoint for performance analysis](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-arch-diag.jpeg)

## Prerequisites

For this solution walkthrough, you need the following:

1. An
   [AWS account](https://aws.amazon.com/account/)
2. [Docker](https://www.docker.com/products/docker-desktop/)
   installed on your workstation
3. The
   [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli)
   installed and configured. If you’re using long term credentials such as access keys, see
   [manage access keys for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
   and
   [secure access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/securing_access-keys.html)
   for best practices. This post uses temporary short term credentials generated by the
   [AWS Security Token Service (AWS STS)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
   .

## Generate your AWS credentials using AWS STS

To get started, use the AWS CLI to generate your credentials.

**Note:**
Ensure that the role or user from which the access keys are generated has
`AmazonSageMakerFullAccess`
permission. Your AWS CLI role should have the necessary trust policy to assume the role from which the access keys are generated.

**Getting the role-arn**

In your AWS CLI type in the following command:

```
aws iam get-role --role-name sagemaker_role
```

The command will generate the JSON output below. The role arn is the value in the
**arn**
property in the JSON below.

```
{
   "Role":{
      "Path":"/",
      "RoleName":"sagemaker_role",
      "RoleId":"AROA123456789EXAMPLE",
      "Arn":"arn:aws:iam::111122223333:role/sagemaker_role",
      "CreateDate":"2025-12-05T13:02:33+00:00",
      "AssumeRolePolicyDocument":{
         "Version":"2012-10-17",
         "Statement":[
            {
               "Effect":"Allow",
               "Principal":{
                  "Service":"ec2.amazonaws.com"
               },
               "Action":"sts:AssumeRole"
            }
         ]
      },
      "Description":"Allows EC2 instances to call AWS services on your behalf.",
      "MaxSessionDuration":3600,
      "RoleLastUsed":{

      }
   }
}
```

Run the following command in your AWS CLI:

```
aws sts assume-role --role-arn <role arn to assume> --role-session-name <session name> --duration-seconds <timeout duration>
```

Set the role arn value from the step above in the
**–role-arn**
argument.

Provide the value
`olaf_session`
to the —
**role-session-name**
argument and set a value equivalent to how long you expect your load test to run in the
**–duration-seconds**
argument. In this blog we are setting it at
**1800**
seconds which give 30 minutes of load testing time.

1. The assume-role command will generate temporary AWS credentials as below

```
{
   "Credentials":{
      "AccessKeyId":"ASIAIOSFODNN7EXAMPLE",
      "SecretAccessKey":"wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
      "SessionToken":"IQoJb3JpZ2luX2VjEJf//////////wEaCXVzLWVhc3QtMSJFMEMCIFdzSaxLya/E71xi2SeG8KFDF46DkxvsWt6Ih0I5X2I6Ah9FYGmWi3fnQfyPQWuzE0Co44xp+qOAxbfaHJ53OYbBKpkCCF8QARoMNjE1NTE1NDU5MjM5IgyoWu5a5DJX3BMn7LYq9gHiRr2sQvStZT9tvvdS8QFjTntBYFEkDL636Crj4xw5rDieBoYFB9h+ozSqMXOtze79DHQLyCduT+McWOlB9Ic5x/xtzPT9HZsfMaEMUOPgI9LtKWUK367rVdcqBV8HH8wOwUS9RhwIyXg2vsGa+WanaS8o6sO8PVkvqOs4ea3CFguncGgSqIftJvgMg0OswzkAoUKXG6jMwL3Ppu13Dg9NV3YKOsS80vejhEJ8QFiKiTsJKX2QmQz/wUN4DN83y8qeFfYEpuYC92oZzv2gErrsXqFd+7/+2w97mInPlD6g1tyd8FlGdXg821WckmwdPu7TYqsCR9kwiM3LyQY6nwFM3U7f/sCre28o2Js31dig0WHb1iv3nTR6m/bIKqsQL4EtYXPGjHD6Ifsf9nQYtkPQC/PqzXg7anx6Q6OW5CzVvk4xU/G9+HcCej84MutK/hQGp3xnRPuJvUIs/q/QlddURk/MFZW9X3njLCn89FRmJ/tI1Mzy/yctwgLcBetE7RIPgaM/90HNXp62vBMK0tzqR1orm6/7eOGV5DXaprQ=",
      "Expiration":"2025-12-05T14:34:56+00:00"
   },
   "AssumedRoleUser":{
      "AssumedRoleId":"AROA123456789EXAMPLE:olaf-session",
      "Arn":"arn:aws:sts::111122223333:assumed-role/sm-blog-role/olaf-session"
   }
}
```

2. Make a note of the access key, secret key, and session token, which you will use to configure the test in the OLAF tool.

## Set up your SageMaker inference endpoint

In this step, you set up a SageMaker inference endpoint. The following is a CloudFormation script to set up the endpoint. Copy the content below and save it as a yaml file for use in the steps below.

```
Resources:
  SageMakerExecutionRole:
    Type: AWS::IAM::Role
    Properties:
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: Allow
            Principal:
              Service: sagemaker.amazonaws.com
            Action: sts:AssumeRole
      ManagedPolicyArns:
        - arn:aws:iam::aws:policy/AmazonSageMakerFullAccess
        - arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
  SageMakerModel:
    Type: AWS::SageMaker::Model
    Properties:
      ModelName: !Sub '${AWS::StackName}-flan-t5-model'
      ExecutionRoleArn: !GetAtt SageMakerExecutionRole.Arn
     EnableNetworkIsolation: true
      PrimaryContainer:
        Image: !Sub '763104351884.dkr.ecr.${AWS::Region}.amazonaws.com/huggingface-pytorch-inference:1.13.1-transformers4.26.0-gpu-py39-cu117-ubuntu20.04'
        Environment:
          HF_MODEL_ID: !Sub 'google/flan-t5-${ModelSize}'
  SageMakerEndpointConfig:
    Type: AWS::SageMaker::EndpointConfig
    Properties:
      EndpointConfigName: !Sub '${EndpointName}-config'
      ProductionVariants:
        - VariantName: AllTraffic
          ModelName: !GetAtt SageMakerModel.ModelName
          InstanceType: !Ref InstanceType
          InitialInstanceCount: 1
  SageMakerEndpoint:
    Type: AWS::SageMaker::Endpoint
    Properties:
      EndpointName: !Ref EndpointName
      EndpointConfigName: !GetAtt SageMakerEndpointConfig.EndpointConfigName
Parameters:
  ModelName:
    Type: String
    Default: flan-t5-model
    Description: Name of the SageMaker model
  EndpointName:
    Type: String
    Default: flan-t5-endpoint-blog
    Description: Name of the SageMaker endpoint
  InstanceType:
    Type: String
    Default: ml.g5.xlarge
    Description: Instance type for the SageMaker endpoint
    AllowedValues:
      - ml.g4dn.xlarge
      - ml.g4dn.2xlarge
      - ml.g5.xlarge
      - ml.g5.2xlarge
      - ml.p3.2xlarge
  ModelSize:
    Type: String
    Default: base
    Description: Size of the FLAN-T5 model
    AllowedValues:
      - small
      - base
      - large
      - xl
      - xxl
Outputs:
  SageMakerEndpointId:
    Description: ID of the SageMaker Endpoint
    Value: !Ref SageMakerEndpoint
  SageMakerEndpointName:
    Description: Name of the SageMaker Endpoint
    Value: !Ref EndpointName
  ModelName:
    Description: Name of the deployed model
    Value: !Ref ModelName
AWSTemplateFormatVersion: '2010-09-09'
Description: 'CloudFormation template for deploying FLAN-T5 model on Amazon SageMaker'
```

3. Open an
   [AWS CloudShell](https://aws.amazon.com/cloudshell)
   window by selecting the CloudShell icon at the top of the AWS Management Console in the AWS Region where you want the endpoint to be created.

![AWS Navigation bar with CloudShell icon highlighted by red arrow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-cloudshell-icon.png)

4. In your CloudShell window, choose
   **Actions**
   and select
   **Upload file**
   . Select and upload the CloudFormation YAML file shared at the start of this section.

![AWS CloudShell terminal window displaying context menu with Upload file option highlighted among other actions](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-cloudshell-file-upload.png)

5. Run the following command at the CloudShell prompt

```
aws cloudformation create-stack \
  --stack-name flan-t5-endpoint-stack \
  --template-body file://<YAML_FILE_NAME> \
  --capabilities CAPABILITY_IAM
```

6. Navigate to the
   [Amazon SageMaker AI Studio](https://us-west-2.console.aws.amazon.com/sagemaker/home?region=us-west-2)
   console. You might need to change the Region to match where you have deployed your SageMaker endpoint. Select the
   **Inference**
   and then
   **Endpoints**
   in the navigation pane to view the deployed endpoint. The SageMaker endpoint will take a few minutes to complete provisioning. When ready the value of the
   **Status**
   field will be
   **InService**
   . Note the
   **endpoint name**
   .

![AWS SageMaker console displaying active endpoint with InService status and creation details](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-SM-endpoint-listing.png)

## Install OLAF

You’re ready to install and configure OLAF to help you load test your SageMaker AI inference endpoint.

1. Clone the OLAF repository from the
   [OLAF GitHub repo](https://github.com/Observeai-Research/olaf.git)
   :

```
git clone https://github.com/Observeai-Research/olaf.git
```

2. Navigate to the
   `olaf`
   directory and build the docker image for OLAF:

```
cd olaf
docker build -t olaf .
```

3. Run OLAF:

```
docker run -p 80:8000 olaf
```

4. Open a browser window and enter the following URL to bring up the OLAF UI.

5. Enter
   `olaf`
   as the username and password to sign in to the OLAF dashboard. On the left is a series of radio buttons to select the resource to be tested, including SageMaker, S3, and so on. On the right is a setup screen that changes based on the resource selected.

![Landing page for Olaf testing tool with AWS service selection options](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-OLAF-Landing.png)

OLAF supports additional options, including:

* Multi-model
* Enable batch mode

## Test the SageMaker endpoint

1. Open the OLAF UI at
   <http://localhost:80/>
   .
2. Select
   **Sagemaker**
   from the navigation pane and configure the test:
   * **SageMaker endpoint**
     – Enter the name of the SageMaker endpoint from the SageMaker Unified Studio console here.
   * **Predictor type**
     – OLAF supports pytorch, sklearn and tensorflow predictors. Keep the default values.
   * **Input Serializer**
     – Serialization options are numpy and json. Keep the default values.
   * **Output Serializer**
     – Serialization options are numpy and json. Keep the default values.
   * **AWS Region**
     – Select the Region where the SageMaker endpoint is deployed
   * **AWS access key**
     – Enter the AWS access key generated from AWS STS in the section “Generate your AWS credentials using AWS STS” above.
   * **AWS secret key**
     – Enter the AWS secret key generated from AWS STS in the section “Generate your AWS credentials using AWS STS” above.
   * **AWS session token**
     – Enter the session token generated from AWS STS in the section “Generate your AWS credentials using AWS STS” above.
   * **Input query json**
     – For this test, enter the following prompt to translate a phrase from English to French.

```
[
    {
        "inputs": "translate the following phrase in English to French : Hello, how are you"
    }
]
```

2. Choose
   **START LOAD SESSION**
   to start a load test session. The session is started and a link to the session is provided at the bottom of the page. If the link doesn’t appear in a few seconds choose
   **START LOAD SESSION**
   to generate the link to the session.

![SageMaker endpoint load testing configuration page with PyTorch predictor settings](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-olaf-create-test.png)

3. Selecting the link takes you to a LOCUST dashboard. Enter the number of concurrent users that you want the test to simulate in the
   **Number of users**
   field and the interval (in seconds) that the users must be started in the
   **spawn rate**
   . Choose
   **Start swarming**
   to start the load test.

![OLAF Locust interface configured for SageMaker endpoint load testing with 10 users and custom parameters](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-start-test.png)

4. On starting the test, a reporting page, shown in the following figure, is presented that you can use to monitor the various performance parameters as the test proceeds. The information on this page provides a summary of the statistics, the p50 and p95 latency values, and the CPU and memory usage of the SageMaker workers.

![Locust dashboard showing PyTorch predictor performance statistics](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-olaf-statistics.png)

5. Choose
   **Charts**
   at the top of the screen to view charts that show the
   **Total Requests per Second**
   and the
   **Response Times**
   in milliseconds. The
   **Total Requests per Second**
   chart shows the successful requests in green and the failed requests in red. The
   **Response Times**
   chart shows the fiftieth percentile response times in green and the ninety-fifth percentile response times in yellow.

![Locust dashboard displaying RPS and response time graphs with 7 workers and 0% failure rate](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-olaf-charts.png)

6. Choose
   **Workers**
   at the top of the screen to view the worker statistics. Workers are created to generate the desired load. The
   **# users**
   show the number of users generated by the worker, the
   **CPU usage**
   and
   **Memory Usage**
   show the resource utilization by the worker.

![Locust monitoring dashboard showing worker processes, CPU usage, and memory consumption across multiple instances](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-olaf-workers.png)

7. You can view and download the final statistics for analysis. Choose
   **Download Data**
   at the top of the screen to view data download options. You can download the data as a CSV file from the
   **Statistics**
   ,
   **Failures**
   ,
   **Exceptions**
   , and
   **Charts**
   reporting pages.

![Locust test summary screen for displaying final metrics and CSV download capabilities](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-download-data.png)

8. You must stop the current load session before you can execute a new session. Choose the
   **STOP RUNNING LOAD SESSION**
   to stop the session. If configured, the data can be uploaded into a specified
   [Amazon Simple Storage Service (Amazon S3)](https://aws.amazon.com/s3)
   bucket. Follow the instructions in
   [Advanced OLAF Usage](https://github.com/Observeai-Research/olaf?tab=readme-ov-file#advanced-olaf-usage)
   item 3, Automated Backup of Load Test Report, to configure the upload of test results to Amazon S3.

![Load test interface with "Session already running" warning and active session link](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/11/ML-17466-olaf-retry.png)

## Hosting the client

For the solution described in this post, you used a desktop to host the OLAF container and set up the load tests. The choice of using your desktop or an
[Amazon Elastic Compute Cloude (Amazon EC2)](https://aws.amazon.com/ec2)
instance can impact the latency because the round trip time will be impacted. Network bandwidth can also impact the latency. The key is to standardize the environment that you use to run the tests based on how your customers use the endpoints.

## Clean up

When you’re done with this demonstration, remove any resources that you no longer need to avoid incurring future costs.

1. In the CloudShell terminal run the following command to delete the SageMaker endpoint:

```
aws cloudformation delete-stack --stack-name flan-t5-endpoint-stack
```

2. Run the following command to list the running Docker images

3. Note the
   `container_id`
   and then run the following command to stop the Docker images.

```
docker stop <container_id>
```

## Conclusion

In this post, you’ve learned how to set up OLAF and use it to load test a SageMaker endpoint with a few basic steps. OLAF represents a significant step forward in streamlining the optimization of ML infrastructure and model serving costs. Through this demonstration, you’ve seen how OLAF seamlessly integrates with SageMaker to provide valuable insights into endpoint performance under various load conditions. Key benefits of OLAF include:

* Straightforward setup and integration with existing SageMaker endpoints
* Real-time monitoring of performance metrics including latency and throughput
* Detailed statistics and downloadable reports for analysis
* Ability to test different load patterns and concurrency levels
* Support for multiple model types and serialization options

For organizations like Observe.ai that need to scale their ML operations efficiently, OLAF eliminates the need to develop custom testing infrastructure and debugging systems. This means that development teams can focus on their core product features while ensuring optimal performance and cost-effectiveness of their ML infrastructure. As the adoption of ML continues to grow, tools like OLAF become increasingly valuable in helping organizations optimize their ML operations. Whether you’re running a few models or managing a large-scale ML infrastructure, OLAF provides the insights needed to make informed decisions about instance types, scaling, and resource allocation.

In this sample solution, you used short term credentials generated by the AWS STS service to connect to SageMaker from OLAF. Ensure that the necessary steps are taken to secure your access keys and credentials in a production environment.

To get started with OLAF, visit the
[GitHub](https://github.com/Observeai-Research/olaf/tree/main)
repository and follow the installation steps outlined in this post. The framework’s intuitive interface and comprehensive monitoring capabilities make it an essential tool for organizations that want to optimize their SageMaker deployments.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/Aashraya.jpeg)
Aashraya Sachdeva**
is a technology leader with deep expertise in genAI, product development, and platform engineering. As the Director of Engineering at Observe, he oversees teams building scalable, agentic solutions that enhance both customer experience and operational efficiency. With extensive experience guiding ML initiatives from early data exploration through deployment and large-scale operations, he brings a pragmatic, reliability-focused approach to delivering high-performing platforms. Throughout his career, he has played a key role in launching multiple products, leveraging his ML background to create innovative yet practical solutions, while consistently fostering collaboration, mentorship, and technical excellence across engineering teams.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/15/shibhu.png)
Shibu Jacob**
is a Senior Solutions Architect at Amazon Web Services (AWS), where he helps customers architect and implement cloud-native solutions. With over two decades of experience in software development and architecture, Shibu specializes in containerization, microservices, and event-driven architectures. He is particularly passionate about the transformative potential of AI in software development and architectural design. Prior to joining AWS, he spent 20 years working with enterprises and startups, bringing a wealth of practical experience to his current role. Outside of work, Shibu enjoys following Formula 1 racing, working on DIY automotive projects, going on long road trips, and spending time with his family.