---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-01T01:10:36.734957+00:00'
exported_at: '2026-06-01T01:10:38.830383+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/streamline-external-access-to-amazon-sagemaker-mlflow-using-a-rest-api-proxy
structured_data:
  about: []
  author: ''
  description: In this post, we demonstrate how to build a secure Flask-based MLflow
    proxy service that provides HTTPS access to Amazon SageMaker MLflow without requiring
    the MLflow SDK. This solution is for organizations undergoing cloud transformation
    who want to preserve their existing ML workflows while adopting cloud-native s...
  headline: Streamline external access to Amazon SageMaker MLflow using a REST API
    proxy
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/streamline-external-access-to-amazon-sagemaker-mlflow-using-a-rest-api-proxy
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Streamline external access to Amazon SageMaker MLflow using a REST API proxy
updated_at: '2026-06-01T01:10:36.734957+00:00'
url_hash: 66e8ba189c8d76d48e4457bfe5acdc2483c6d8a6
---

Machine learning (ML) teams use MLflow to manage their ML lifecycle effectively.
[Amazon SageMaker MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
provides comprehensive ML experiment tracking and model management capabilities. However, many enterprises have existing infrastructure requirements that need HTTPS-based integrations rather than direct SDK usage.

Many organizations need to integrate Amazon SageMaker MLflow with their established systems while maintaining their security and infrastructure patterns. This integration challenge affects teams who can’t use the SDK directly because of corporate security policies, network restrictions, or legacy system constraints.

In this post, we demonstrate how to build a secure Flask-based MLflow proxy service that provides HTTPS access to Amazon SageMaker MLflow without requiring the MLflow SDK. This solution is for organizations undergoing cloud transformation who want to preserve their existing ML workflows while adopting cloud-native services.

This post covers the following topics:

* Implementing the MLflow proxy service for MLflow HTTPS requests.
* Configuring AWS Identity and Access Management (IAM) authentication for secure access.
* Managing URL pre-signing and request transformation.

After implementing this solution, you can:

* Access SageMaker MLflow securely through standard HTTPS endpoints.
* Maintain compliance with your organization’s security requirements.
* Integrate MLflow with existing enterprise systems.
* Reduce implementation complexity and maintenance overhead.

## Solution overview

A lightweight Flask-based MLflow proxy architecture provides secure integration between enterprise systems and Amazon SageMaker MLflow through three key components.

**Component 1: Application Load Balancer (ALB)**

An
[AWS Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
serves as the upstream router, providing the following:

* Traffic distribution for MLflow UI and REST API requests.
* Initial request handling and routing.
* Support for custom domain names and SSL termination.

Note: This implementation uses ALB, but you can alternatively use other routing solutions such as Nginx based on your requirements.

**Component 2: Flask MLflow Proxy Service**

At the heart of the architecture, a Python-based Flask application handles the following:

* Intercepting and processing incoming HTTPS requests.
* Managing AWS authentication and request signing.
* Transforming URLs for secure MLflow endpoint access.
* Handling response routing back to clients.

**Component 3: Amazon SageMaker MLflow**

The AWS managed SageMaker MLflow service provides the following:

* Support for two MLflow deployment modes:
  + MLflow Tracking Server – managed MLflow tracking server.
  + MLflowApp – serverless MLflow application.
* Backend metadata store for tracking information.
* Storage for model files and data.

This architecture provides secure communication while maintaining compatibility with existing enterprise systems. The proxy service acts as a bridge, transforming standard HTTPS requests into authenticated AWS API calls that can interact with SageMaker MLflow.

## Architecture and request workflow

The following diagram shows how the Flask proxy service provides secure communication between external clients and Amazon SageMaker MLflow.

![Architecture diagram showing external clients sending HTTPS requests through an Application Load Balancer to a Flask proxy service that authenticates and forwards requests to Amazon SageMaker MLflow](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/05/21/ML-19491-1.png)

*Figure 1: Architecture diagram showing the Flask proxy service integration with Amazon SageMaker MLflow*

The architecture diagram shows three main components:

* An ALB that handles incoming traffic.
* A Flask proxy service that manages authentication and request transformation.
* Amazon SageMaker MLflow that processes ML operations.

### Request workflow

Let’s explore how requests flow through this architecture to provide secure MLflow access.

When a client initiates an HTTPS request, it first reaches the ALB, which acts as the entry point for all incoming traffic. The ALB then routes these requests to the MLflow proxy service.

When it receives the request, the MLflow proxy service performs several critical functions:

* Handles authentication through AWS IAM integration.
* Transforms URLs and pre-signs them for secure access.
* Processes the MLflow REST API endpoints as needed.

The MLflow proxy service transforms the incoming request into an authenticated AWS request before making the API call to SageMaker MLflow REST endpoints. After SageMaker MLflow processes the request, it returns a response which the MLflow proxy service processes and routes back to the original client.

This workflow maintains security while providing integration between enterprise systems and SageMaker MLflow.

## Prerequisites

To follow this walkthrough, make sure you have the following:

* [An AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html)
  .
* A workstation with the following tools installed:
  + [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
    configured with permissions to create:
    - Amazon Virtual Private Cloud (Amazon VPC) and associated networking components.
    - Amazon Elastic Compute Cloud (Amazon EC2) instances.
    - Amazon SageMaker AI resources.
    - Amazon Simple Storage Service (Amazon S3) buckets.
    - AWS Identity and Access Management (IAM) roles and policies.
    - AWS CloudFormation stacks.
    - AWS Application Load Balancers.
  + [Node.js](https://nodejs.org/en/download)
    version 18.0.0 or later.
  + [NPM](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
    .
  + [AWS Cloud Development Kit (AWS CDK) CLI](https://docs.aws.amazon.com/cdk/v2/guide/cli.html)
    version 2.100.0 or later.
  + Python 3.x with pip or pip3.
* Required knowledge:
  + Basic understanding of AWS services and IAM permissions.
  + Familiarity with Python and Flask applications.
  + Understanding of MLflow concepts and operations.
* Cost considerations:
  + This solution creates AWS resources that might incur costs.
  + Key cost-driving resources include:
    - Amazon EC2 instances.
    - Application Load Balancer.
    - Amazon SageMaker AI resources.
    - Amazon S3 storage.

For information about AWS service pricing, see
[AWS Pricing Calculator](https://calculator.aws/#/)
.

## Deploy the solution

This section walks you through deploying the solution in your AWS account and validating it. The deployment process takes approximately 40 minutes.

### Step 1: Deploy the infrastructure using AWS CDK

1. Download the solution code and install dependencies:

   ```
   # Clone the repository
   git clone https://github.com/aws-samples/sample-sagemaker-mlflow-rest-apis.git

   # Navigate to project directory and install dependencies
   cd sample-sagemaker-mlflow-rest-apis
   npm ci
   ```
2. [Bootstrap your environment for AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-env.html)
   . Skip this step if your AWS account and Region are already bootstrapped for AWS CDK.Bootstrap the AWS account and Region for CDK:

   ```
   npx cdk bootstrap aws://&lt;ACCOUNT_ID&gt;/&lt;REGION&gt;
   ```
3. Deploy the required resources on your AWS account.The solution consists of four CDK stacks:
   * Networking stack — creates the VPC and networking components.
   * SageMaker AI domain stack — sets up the SageMaker domain.
   * SageMaker MLflow stack — deploys the MLflow tracking server or MLflow serverless app.
   * Flask application stack — deploys the MLflow proxy service.

   Deploy all the stacks with one of the following commands.

   For tracking server based deployment:

   ```
   npx cdk deploy --all --require-approval=never -c mlflowType=tracking
   ```

   For serverless app based deployment:

   ```
   npx cdk deploy --all --require-approval=never -c mlflowType=serverless
   ```

### Step 2: Install and configure the Flask MLflow proxy service

1. Connect to the EC2 instance:
   1. Note the Amazon EC2 instance ID from the CDK output or from the
      **sagemaker-infra-flaskapp-{mlflowType}**
      AWS CloudFormation stack output section.
   2. Use AWS Systems Manager Session Manager to connect. Follow the
      [Session Manager connection guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-with-systems-manager-session-manager.html)
      .
2. Install Python 3.13 and dependencies.Install Python packages:

   ```
   # Switch to root user
   sudo su -
   cd /root

   # Install Python and dependencies
   chmod +x install_python13.sh
   ./install_python13.sh
   ```

   ***Note:**
   This script is designed for Ubuntu-based systems. For other Linux distributions, install Python 3.12+, PIP3, and Virtualenv using your system’s package manager.*
3. Install and start the MLflow proxy service:

   ```
   chmod +x setup_mlflow_proxy_app.sh
   ./setup_mlflow_proxy_app.sh
   ```
4. Check the Flask MLflow proxy service status:

   ```
   systemctl status mlflowproxy
   ```

   Note: If the service isn’t running, check logs with the following command:

   ```
   journalctl -u mlflowproxy
   ```

### Step 3: Validate MLflow REST API access

This section demonstrates how to interact with MLflow REST APIs through the ALB.

***Note: These examples use the HTTP (unsecured) protocol. For production environments, we recommend HTTPS. We use
[curl](https://github.com/curl/curl)
to make the API requests in this post, but you can use any tool you prefer. The provided curl commands work identically for both tracking server and serverless modes; the proxy service handles the differences transparently.***

1. Get your ALB DNS name by running the following command on your workstation:

   ```
   aws cloudformation describe-stacks --stack-name sagemaker-infra-flaskapp-{mlflowType} --query 'Stacks[0].Outputs[?OutputKey==`ALBUrl`].OutputValue' --output text
   ```
2. Test MLflow API endpoints by running the following commands on your workstation. Replace
   `&lt;ALB DNS&gt;`
   ,
   `&lt;EXP ID&gt;`
   ,
   `&lt;RUN ID&gt;`
   , and
   `&lt;RUN NAME&gt;`
   with appropriate values.
   1. Create an experiment:

      ```
      curl -X POST http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/experiments/create -H "Content-Type: application/json" -d '{"name": "mlflow-experiment"}'
      ```
   2. Search experiments:

      ```
      curl -X POST http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/experiments/search -H "Content-Type: application/json" -d '{"max_results": 5}'
      ```
   3. Get an experiment:

      ```
      curl -X GET 'http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/experiments/get?experiment_id=0'
      ```
   4. Create a run inside an experiment:

      ```
      curl -X POST http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/runs/create -H "Content-Type: application/json" -d '{"experiment_id": &lt;EXP ID&gt;, "run_name": "&lt;RUN NAME&gt;"}'
      ```
   5. List artifacts from a run:

      ```
      curl -X GET "http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/artifacts/list?run_id=&lt;RUN ID&gt;"
      ```
   6. Set a tag on a run:

      ```
      curl -X POST "http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/runs/set-tag" -H "Content-Type: application/json" -d '{"run_id": "&lt;RUN ID&gt;", "key": "model_type","value": "api-test"}'
      ```
   7. Delete a run:

      ```
      curl -X POST http://&lt;ALB DNS&gt;/ajax-api/2.0/mlflow/runs/delete -H "Content-Type: application/json" -d '{"run_id": "&lt;RUN ID&gt;"}'
      ```

   ***Note: You can also open the MLflow UI and view the changes you make using the preceding curl commands. For instructions on launching the MLflow UI, see
   [Launch the MLflow UI using a presigned URL](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-launch-ui.html)
   .***

## Cleanup

To avoid ongoing charges and remove the resources created by this solution, follow these cleanup steps:

1. Delete CDK-managed resources.Navigate to the root directory of the cloned repository on your workstation and run the following.For tracking server based deployment:

   ```
   npx cdk destroy --all -c mlflowType=tracking
   ```

   For serverless app based deployment:

   ```
   npx cdk destroy --all -c mlflowType=serverless
   ```

   ***Note: The networking and SageMaker domain stacks are shared across both deployment modes. AWS CDK only deletes them when the last MLflow or Flask app stack pair is removed.***
2. Manual resource cleanup. Some resources might require manual deletion because of retention policies or dependencies:
   1. Amazon S3 buckets:
      1. Navigate to the Amazon S3 console.
      2. Identify the buckets created by this solution.
      3. Empty each bucket and delete it.
   2. Amazon CloudWatch log groups:
      1. In the CloudWatch console, find the log groups associated with this solution.
      2. Delete these log groups.

## Security considerations

When you deploy this solution in a production environment, consider the following security measures:

* Configure Amazon CloudWatch monitoring for the Flask-based proxy service to track application health, detect anomalies, and set up alerts for suspicious activities.
* Implement rate limiting for the Flask-based proxy service to protect against potential denial-of-service (DoS) attacks and control the number of requests from individual clients. You can use
  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)
  (web application firewall) with the ALB to implement rate-based rules.
* Deploy an internal (non-internet-facing) ALB to restrict proxy access to your private network. This setup makes sure that only traffic from within your VPC or connected networks can reach the service. Connect through VPC peering or AWS Transit Gateway.
* Enable HTTPS termination at the ALB level for secure communication between clients and your application. You can use AWS Certificate Manager (ACM) to provision and manage SSL/TLS certificates for your application. For instructions on configuring HTTPS listeners, see the
  [Application Load Balancer HTTPS listeners documentation](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)
  .

These security measures help protect the Flask application against common web vulnerabilities and provide secure communication between components.

## Conclusion

In this post, we showed how to build a secure Flask-based proxy service that provides HTTPS access to Amazon SageMaker MLflow. This solution helps organizations bridge their existing infrastructure with AWS managed MLflow capabilities while maintaining enterprise security requirements.

Solution benefits:

* Integration with existing enterprise security controls.
* Minimal changes to existing ML workflows.
* Reduced deployment complexity.
* REST API integration.
* Compatibility with enterprise proxy services.

## Next steps

To learn more about Amazon SageMaker MLflow and related topics, you can:

Try this solution in your own environment and let us know your experience in the comments.

---

## About the authors

### Manish Garg

Manish is a Delivery Consultant with AWS Professional Services, specializing in migrating and modernizing customer workloads on the AWS Cloud. He possesses a profound enthusiasm for technology, coupled with a keen interest in the realms of DevOps practices.

### Ram Yennapusa

Ram is a Senior Delivery Consultant at Amazon Web Services (AWS). He works with enterprise customers to design and implement cloud-based solutions at scale, with a focus on DevOps and MLOps. Ram has over 15 years of experience in software development and cloud architecture, helping organizations navigate their cloud transformation journey. He helps customers build efficient, secure, and scalable solutions on AWS.

### Ashish Bhatt

Ashish is a Senior Delivery Consultant with AWS Professional Services, specializing in designing and building solutions for customer workloads on the AWS Cloud. He brings deep expertise in DevOps, MLOps, and platform engineering, with a focus on building scalable infrastructure platforms and empowering development teams through modern platform engineering solutions.