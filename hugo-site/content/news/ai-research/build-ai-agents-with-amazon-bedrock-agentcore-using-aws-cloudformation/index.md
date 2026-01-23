---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-23T18:15:27.315108+00:00'
exported_at: '2026-01-23T18:15:29.867087+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/build-ai-agents-with-amazon-bedrock-agentcore-using-aws-cloudformation
structured_data:
  about: []
  author: ''
  description: Amazon Bedrock AgentCore services are now being supported by various
    IaC frameworks such as AWS Cloud Development Kit (AWS CDK), Terraform and AWS
    CloudFormation Templates. This integration brings the power of IaC directly to
    AgentCore so developers can provision, configure, and manage their AI agent infrastructure.
    In this post, we use CloudFormation templates to build an end-to-end application
    for a weather activity planner.
  headline: Build AI agents with Amazon Bedrock AgentCore using AWS CloudFormation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/build-ai-agents-with-amazon-bedrock-agentcore-using-aws-cloudformation
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Build AI agents with Amazon Bedrock AgentCore using AWS CloudFormation
updated_at: '2026-01-23T18:15:27.315108+00:00'
url_hash: 3aa499d6698b2321f616900fc3fb9cdf3e6cdb1d
---

Agentic-AI has become essential for deploying production-ready AI applications, yet many developers struggle with the complexity of manually configuring agent infrastructure across multiple environments.
[Infrastructure as code](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-iac.html)
(IaC) facilitates consistent, secure, and scalable infrastructure that autonomous AI systems require. It minimizes manual configuration errors through automated resource management and declarative templates, reducing deployment time from hours to minutes while facilitating infrastructure consistency across the environments to help prevent unpredictable agent behavior. It provides version control and rollback capabilities for quick recovery from issues, essential for maintaining agentic system availability, and enables automated scaling and resource optimization through parameterized templates that adapt from lightweight development to production-grade deployments. For agentic applications operating with minimal human intervention, the reliability of IaC, automated validation of security standards, and seamless integration into DevOps workflows are essential for robust autonomous operations.

In order to streamline the resource deployment and management,
[Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
services are now being supported by various IaC frameworks such as
[AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
(AWS CDK),
[Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started)
and
[AWS CloudFormation Templates](https://aws.amazon.com/cloudformation/resources/templates/)
. This integration brings the power of IaC directly to AgentCore so developers can provision, configure, and manage their AI agent infrastructure. In this post, we use CloudFormation templates to build an end-to-end application for a weather activity planner. Examples of using CDK and Terraform can be found at
[GitHub Sample Library](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/04-infrastructure-as-code)
.

## Building an activity planner agent based on weather

The sample creates a weather activity planner, demonstrating a practical application that processes real-time weather data to provide personalized activity recommendations based on a location of interest. The application consists of multiple integrated components:

* **Real-time weather data collection**
  – The application retrieves current weather conditions from authoritative meteorological sources such as weather.gov, gathering essential data points including temperature readings, precipitation probability forecasts, wind speed measurements, and other relevant atmospheric conditions that influence outdoor activity suitability.
* **Weather analysis engine**
  – The application processes raw meteorological data through customized logic to evaluate suitability of a day for an outdoor activity based on multiple weather factors:
  + **Temperature comfort scoring**
    – Activities receive reduced suitability scores when temperatures drop below 50°F
  + **Precipitation risk assessment**
    – Rain probabilities exceeding 30% trigger adjustments to outdoor activity recommendations
  + **Wind condition impact evaluation**
    – Wind speeds above 15 mph affect overall comfort and safety ratings for various activities
* **Personalized recommendation system**
  – The application processes weather analysis results with user preferences and location-based awareness to generate tailored activity suggestions.

The following diagram shows this flow.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/23/ml-19762-image-1.png)

Now let’s look at how this can be implemented using AgentCore services:

* [**AgentCore Browser**](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-tool.html)
  – For automated browsing of weather data from sources such as weather.gov
* [**AgentCore Code Interpreter**](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)
  – For executing Python code that processes weather data, performs calculations, and implements the scoring algorithms
* [**AgentCore Runtime**](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
  – For hosting an agent that orchestrates the application flow, managing data processing pipelines, and coordinating between different components
* [**AgentCore Memory**](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
  – For storing the user preferences as long term memory

The following diagram shows this architecture.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/23/ml-19762-image-2.png)

## Deploying the CloudFormation template

1. Download the CloudFormation template from github for
   [End-to-End-Weather-Agent.yaml](https://github.com/awslabs/amazon-bedrock-agentcore-samples/blob/main/04-infrastructure-as-code/cloudformation/end-to-end-weather-agent/end-to-end-weather-agent.yaml)
   on your local machine
2. Open CloudFormation from AWS Console
3. Click
   **Create stack**
   →
   **With new resources (standard)**
4. Choose template source (upload file) and select your template
5. Enter stack name and change any required parameters if needed
6. Review configuration and acknowledge IAM capabilities
7. Click
   **Submit**
   and monitor deployment progress on the Events tab

Here is the visual steps for CloudFomation template deployment

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-19762/ML-19762-Agencore-CFN-Setup.mp4?_=1)

Running and testing the application

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-19762/ML-19762-Agencore-CFN-Application-Run.mp4?_=2)

## Adding observability and monitoring

AgentCore Observability provides key advantages. It offers quality and trust through detailed workflow visualizations and real-time performance monitoring. You can gain accelerated time-to-market by using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
powered dashboards that reduce manual data integration from multiple sources, making it possible to take corrective actions based on actionable insights. Integration flexibility with OpenTelemetry-compatible format supports existing tools

such as
[CloudWatch](https://aws.amazon.com/cloudwatch/)


,
[DataDog](https://www.datadoghq.com/)


,
[Arize



Phoenix](https://phoenix.arize.com/)


,
[LangSmith](https://www.langchain.com/langsmith/observability)


, and
[LangFuse](https://langfuse.com/docs/observability/overview)


.

The service provides end-to-end traceability across frameworks and
[foundation models](https://aws.amazon.com/what-is/foundation-models/)
(FMs), captures critical metrics such as token usage and tool selection patterns, and supports both automatic instrumentation for AgentCore Runtime hosted agents and configurable monitoring for agents deployed on other services. This comprehensive observability approach helps organizations achieve faster development cycles, more reliable agent behavior, and improved operational visibility while building trustworthy AI agents at scale.

The following screenshot shows metrics in the AgentCore Runtime UI.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/23/ml-19762-image-5.png)

## Customizing for your use case

The weather activity planner AWS CloudFormation template is designed with modular components that can be seamlessly adapted for various applications. For instance, you can customize the AgentCore Browser tool to collect information from different web applications (such as financial websites for investment guidance, social media feeds for sentiment monitoring, or ecommerce sites for price tracking), modify the AgentCore Code Interpreter algorithms to process your specific business logic (such as predictive modeling for sales forecasting, risk assessment for insurance, or quality control for manufacturing), adjust the AgentCore Memory component to store relevant user preferences or business context (such as customer profiles, inventory levels, or project requirements), and reconfigure the
[Strands Agents](https://strandsagents.com/latest/)
tasks to orchestrate workflows specific to your domain (such as supply chain optimization, customer service automation, or compliance monitoring).

## Best practices for deployments

We recommend the following practices for your deployments:

* **Modular component architecture**
  – Design AWS CloudFormation templates with separate sections for each AWS Services.
* **Parameterized template design**
  – Use AWS CloudFormation parameters for the configurable elements to facilitate reusable templates across environments. For example, this can help associate the same base container with multiple agent deployments, help point to two different build configurations, or parameterize the LLM of choice for powering your agents.
* [**AWS Identity and Access Management**](https://aws.amazon.com/iam/)
  **(IAM) security and least privilege**
  – Implement fine-grained IAM roles for each AgentCore component with specific resource
  [Amazon Resource Names](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html)
  (ARNs). Refer to our documentation on
  [AgentCore security considerations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/security.html)
  .
* **Comprehensive monitoring and observability**
  – Enable CloudWatch logging, custom metrics,
  [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
  distributed tracing, and alerts across the components.
* **Version control and continuous integration and continuous delivery (CI/CD) integration**
  – Maintain templates in GitHub with automated validation, comprehensive testing, and AWS CloudFormation StackSets for consistent multi-Region deployments.

You can find a more comprehensive set of best practices at
[CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html)

## Clean up resources

To avoid incurring future charges, delete the resources used in this solution:

1. On the
   [Amazon S3 console](https://console.aws.amazon.com/s3/)
   , manually delete the contents inside the bucket you created for template deployment and then delete the bucket.
2. On the
   [CloudFormation console](https://console.aws.amazon.com/cloudformation/)
   , choose
   **Stacks**
   in the navigation pane, select the main stack, and choose
   **Delete**
   .

## Conclusion

In this post, we introduced an automated solution for deploying AgentCore services using AWS CloudFormation. These preconfigured templates enable rapid deployment of powerful agentic AI systems without the complexity of manual component setup. This automated approach helps save time and facilitates consistent and reproducible deployments so you can focus on building agentic AI workflows that drive business growth.

Try out some more examples from our Infrastructure as Code sample repositories :

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/23/ml-19762-image-8-1.png)
Chintan Patel**
is a Senior Solution Architect at AWS with extensive experience in solution design and development. He helps organizations across diverse industries to modernize their infrastructure, demystify Generative AI technologies, and optimize their cloud investments. Outside of work, he enjoys spending time with his kids, playing pickleball, and experimenting with AI tools.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2020/12/19/Shreyas-Subramanian.png)
Shreyas Subramanian**
is a Principal Data Scientist and helps customers by using Generative AI and deep learning to solve their business challenges using AWS services like Amazon Bedrock and AgentCore. Dr. Subramanian contributes to cutting-edge research in deep learning, Agentic AI, foundation models and optimization techniques with several books, papers and patents to his name. In his current role at Amazon, Dr. Subramanian works with various science leaders and research teams within and outside Amazon, helping to guide customers to best leverage state-of-the-art algorithms and techniques to solve business critical problems. Outside AWS, Dr. Subramanian is a expert reviewer for AI papers and funding via organizations like Neurips, ICML, ICLR, NASA and NSF.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2024/08/21/kosti.jpg)
Kosti Vasilakakis**
is a Principal PM at AWS on the Agentic AI team, where he has led the design and development of several Bedrock AgentCore services from the ground up, including Runtime. He previously worked on Amazon SageMaker since its early days, launching AI/ML capabilities now used by thousands of companies worldwide. Earlier in his career, Kosti was a data scientist. Outside of work, he builds personal productivity automations, plays tennis, and explores the wilderness with his family.