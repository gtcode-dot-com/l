---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-09T00:03:19.224513+00:00'
exported_at: '2025-12-09T00:03:21.641418+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/create-an-intelligent-insurance-underwriter-agent-powered-by-amazon-nova-2-lite-and-amazon-quick-suite
structured_data:
  about: []
  author: ''
  description: 'In this post, we demonstrate how to build an intelligent insurance
    underwriting agent that addresses three critical challenges: unifying siloed data
    across CRM systems and databases, providing explainable and auditable AI decisions
    for regulatory compliance, and enabling automated fraud detection with consistent
    underwriting rules. The solution combines Amazon Nova 2 Lite for transparent risk
    assessment, Amazon Bedrock AgentCore for managed MCP server infrastructure, and
    Amazon Quick Suite for natural language interactions—delivering a production-ready
    system that underwriters can deploy in under 30 minutes .'
  headline: Create an intelligent insurance underwriter agent powered by Amazon Nova
    2 Lite and Amazon Quick Suite
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/create-an-intelligent-insurance-underwriter-agent-powered-by-amazon-nova-2-lite-and-amazon-quick-suite
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Create an intelligent insurance underwriter agent powered by Amazon Nova 2
  Lite and Amazon Quick Suite
updated_at: '2025-12-09T00:03:19.224513+00:00'
url_hash: 6085e83b93283c3eb60e7bd18c90435330c32546
---

Insurance underwriting requires analyzing multiple data sources, evaluating risks, and making decisions that meet regulatory requirements. The underwriters face three core challenges:

* Siloed data scattered across Customer Relationship Management (CRM) systems, document repositories, and transactional databases
* Regulatory requirements for explainable, auditable decisions that traditional
  [black box AI](https://jolt.law.harvard.edu/assets/articlePDFs/v31/The-Artificial-Intelligence-Black-Box-and-the-Failure-of-Intent-and-Causation-Yavar-Bathaee.pdf)
  can’t satisfy
* The need for consistent, automated underwriting rules with proactive fraud detection across portfolios

In this post, we show how to overcome these challenges with an enterprise-grade underwriting solution using
[Amazon Nova 2 Lite](https://aws.amazon.com/nova/)
that unifies your data sources and delivers audit-ready risk assessments.

## Solution overview

The solution uses
[Model Context Protocol (MCP) tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
for insurance fraud detection, risk assessment of an applicant, and underwriting decisions. When a tool is invoked based on a user query, the tool fetches data from required data sources—document repositories like
[Amazon Simple Storage Service](https://aws.amazon.com/s3/)
(Amazon S3) and databases like
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
—and calls the
[Amazon Nova 2 Lite](https://aws.amazon.com/ai/generative-ai/nova/understanding/)
large language model (LLM) for analysis and decision-making. After retrieving the associated system prompt and the context provided, the LLM returns a response in the structure the tool expects. The MCP server is deployed in
[Amazon Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)
with
[OAuth 2.0](https://auth0.com/intro-to-iam/what-is-oauth-2)
inbound authorization. The
[Amazon Quick Suite](https://aws.amazon.com/quicksuite/)
MCP client is configured using service authentication to allow inbound connections to the MCP server. The user interacts with the Quick Suite
[chat agent](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)
in a natural language. The agent invokes the required MCP tools and engages in multi-turn conversations with the user.

The following diagram illustrates the solution architecture.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/NovaQuickBlogArch.png)

*Figure 1: Architecture and dataflow*

The workflow consists of the following steps:

1. An authenticated
   [Quick Suite user](https://docs.aws.amazon.com/quicksuite/latest/userguide/user-types.html)
   accesses the
   [Quick Suite chat agent](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)
   and submits a prompt through the assistant chat interface. For example, “Access the risk for applicant APP-0900.”
2. The chat agent is integrated with
   [Amazon Quick Suite MCP Actions Integrations](https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html)
   to invoke actions on an
   [MCP server deployed in AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-mcp.html)
   . The agent analyzes the prompt to understand the intent and identifies key entities (such as applicant IDs and claim numbers), and decides which
   [MCP tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
   to invoke.
3. The
   [Quick Suite MCP client](https://docs.aws.amazon.com/quicksuite/latest/userguide/mcp-integration.html)
   requests an
   [access token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html)
   from
   [Amazon Cognito](https://aws.amazon.com/cognito/)
   using the OAuth client credentials. Amazon Cognito validates the credentials and issues a short-lived access token. Quick Suite includes this token in the request to AgentCore Runtime that validates the token against Amazon Cognito.
4. AgentCore Runtime has a built-in translation that transforms the incoming request into MCP
   [JSON-RPC 2.0](https://www.jsonrpc.org/specification)
   format and invokes the appropriate tools on the MCP server. Logging can be enabled on AgentCore Runtime to log the events in
   [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
   .
5. The MCP server executes the tool logic to retrieve data from DynamoDB and Amazon S3, and to invoke Amazon Nova 2 Lite through the
   [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
   to generate a response with a detailed reasoning process.
6. The final response is transformed back to match the incoming request protocol for Quick Suite, and the response is returned to the user through the chat agent-powered assistant interface.

Amazon Nova 2 Lite can request tools and understand tool schemas. It performs reasoning to determine which tools are needed based on user queries. It then generates tool requests with validated parameters that the MCP server executes. Solution deployment consists of the following high-level steps:

1. Host the MCP server on Amazon Bedrock AgentCore.
2. Integrate Quick Suite with the MCP server.
3. Test the integration.
4. Create and launch the Quick Suite chat agent.

## Prerequisites

The following prerequisites are required to deploy the solution:

* An
  [AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html#getting-started-step1)
* Quick Suite set up with Author Pro subscription
* Permission to create
  [AWS Identity and Access Management](https://aws.amazon.com/iam/)
  (IAM) roles and policies and AWS resources, including a DynamoDB table, S3 bucket, Amazon Cognito user pool, and AgentCore Runtime
* Access to a command line environment with the AWS SDK and Python installed

## Host MCP server on Amazon Bedrock AgentCore

Complete the following steps to host the MCP server on Amazon Bedrock AgentCore:

1. Clone the
   [code repository.](https://github.com/aws-samples/sample-quicksuite-chatagent-insurance-underwriting.git)

```
git clone https://github.com/aws-samples/sample-quicksuite-chatagent-insurance-underwriting.git
```

2. Edit the configuration file
   `config/enterprise_config.yaml`
   to provide the name of the MCP server, Amazon Cognito user pool, DynamoDB tables containing applicants and claims, and S3 bucket for medical records.
3. Set up a virtual environment:

```
python -m venv smart_insurance_agent_venv
source smart_insurance_agent_venv/bin/activate
pip install -r deployment/requirements.txt
```

4. Optionally, generate synthetic applicants, medical records, and claims. You can skip this step if you don’t require synthetic data generation.

```
python deployment/load_data.py
```

Synthetic data generation uses the
[faker](https://pypi.org/project/Faker/)
library to generate applicant records and claims records that get persisted to DynamoDB and medical records that get persisted to Amazon S3 in JSON format. You can modify the record schema or formats by customizing load\_data.py to generate data according to your needs.

5. Deploy the MCP server to Amazon Bedrock AgentCore.

This step creates an Amazon Cognito user pool, builds a Docker image, deploys it to Amazon Bedrock AgentCore, configures IAM permissions, and generates
`docs/QUICK_SUITE_INTEGRATION.md`
with the MCP server endpoint URL and OAuth configuration to integrate it with Quick Suite.

6. Test the functionality of MCP tools:

```
python tests/test_mcp_functionality.py
```

Successful execution of this test script will provide an output as shown in the following screenshots.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-2.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-3.png)

*Figure 2: successful deployment and test output of MCP server on console*

## Integrate Quick Suite with MCP server

Next, set up a service-to-service OAuth connection from Quick Suite to the Amazon Bedrock AgentCore endpoint. This lets your Quick Suite chat agent call MCP server actions to fulfill user requests.

1. Sign in to Quick Suite using credentials with the Quick Suite Author Pro role.
2. On the Quick Suite console, choose
   **Integrations**
   in the navigation pane.
3. Choose the plus sign next to
   **Model Context Protocol**
   to create a new integration.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-4.png)

*Figure 3: Create MCP integration*

4. On the
   **Connect**
   page, enter the integration details of the MCP server you hosted on Amazon Bedrock AgentCore:
   1. For
      **Name**
      , enter a name (for example, Insurance Underwriting Expert).
   2. For
      **Description**
      , enter an optional description (for example, Integration with Insurance Underwriting MCP Server hosted in Bedrock AgentCore Runtime).
   3. For
      **MCP server endpoint**
      , enter the URL of the MCP server.
   4. Choose
      **Next**
      .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-5.png)

*Figure 4: MCP endpoint configuration*

5. On the
   **Authenticate**
   page, provide the following information:
   1. For
      **Authentication settings**
      , select
      **Service authentication**
      .
   2. For
      **Authentication type**
      , choose
      **Service-to-service OAuth**
      .
   3. For
      **Client ID**
      , enter your OAuth client ID.
   4. For
      **Client secret**
      , enter your OAuth client secret.
   5. For
      **Token URL**
      , enter your OAuth token URL.
6. Choose
   **Create and continue**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-6.png)

*Figure 5: Authentication configuration*

7. On the
   **Review**
   page, review the integration details and choose
   **Next**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-7.png)

*Figure 6: Review all configurations*

8. On the
   **Share integration**
   page, choose
   **Next**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-8-1.png)

*Figure 7: Complete integration setup*

You can share the integration with users and groups in your organization who might be using the chat agent for the underwriting application.

## Test the integration

To test the integration, complete the following steps:

1. On the Quick Suite console, choose
   **Integrations**
   in the navigation pane.
2. Choose
   **Actions**
   .

You will see the status
**Available**
for the integration you created.

3. Choose the integration Insurance Underwriting Expert.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-9-1.png)

4. Choose
   **Test action APIs**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-10-1.png)

5. Choose an action to test on the
   **Actions**
   dropdown menu.
6. Choose
   **Submit**
   to view the API response.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-11-1.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-12-1.png)

## Create and launch the Quick Suite chat agent

In this section, you create a custom
[chat agent](https://docs.aws.amazon.com/quicksuite/latest/userguide/custom-agents.html"%20\l%20"create-custom-agents)
in Quick Suite. Complete the following steps:

1. On the Quick Suite console, choose
   **Chat agents**
   in the navigation pane.
2. Choose
   **Create chat agent**
   .

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-13-1.png)

3. On the
   **Agent creator**
   page, chose
   **Skip**
   .
4. Add a name for your custom chat agent. This is the name that your chat agent will be identified by.
5. Add an optional description for your custom chat agent that helps users understand the purpose of the chat agent.
6. On the
   **Configure chat agent**
   page, provide the following information:
   1. For
      **Agent identity**
      , define the identity of your chat agent. For example: You are Nova, an AI-powered Insurance Underwriting Analyst with deep expertise in explainable risk assessment and fraud detection. You have access to enterprise insurance data including 1000+ applicant profiles, medical records, and claims history through advanced reasoning capabilities.
   2. For
      **Persona instructions**
      , enter instructions on how your chat agent interacts with users during chat. For example: Your transparency and reasoning capabilities are key differentiators. Always explain your confidence level in recommendations and acknowledge limitations. Break down complex insurance decisions into clear, logical steps. Reference specific applicant profiles, medical records, and claims when available. Provide risk scores with detailed explanations of contributing factors. Include regulatory compliance considerations and business impact in all recommendations. Offer follow-up questions to deepen analysis when appropriate.
   3. Under
      **Actions**
      , choose
      **Link actions**
      , choose the action connector you created, then choose
      **Link**
      .
   4. Choose
      **Launch chat agent**
      to create your custom chat agent. You will see the progress Launching chat agent… and in a few minutes, you will see Successfully launched chat agent.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-14-1.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-15-1.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-16-1.png)

7. Choose
   **Chat agents**
   in the navigation pane and choose the chat agent you created.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-17-1.png)

8. Choose
   **Chat**
   to start chatting with your chat agent.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-18-1.png)

You can now chat with the agent for your specific use cases. The following screenshots show an example. Start by asking the chat agent for a specific risk assessment and choose the send icon.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-19-1.png)

The requests action review for several actions, which require additional information. Confirm the required information for each action and choose
**Submit**
.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-20.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-21.png)

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-22-1.png)

The agent begins processing the query.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-23-1.png)

The agent returns a risk assessment.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/image-24-1.png)

We have concealed personally identifiable information (PII) and other details associated with the applicant for the purposes of this post. However, an authorized user of the application will be able to view the analysis performed by Amazon Nova 2 Lite. You now have a working insurance underwriting agent up and running in less than 30 minutes!

## Clean up

To clean up the resources, use the following script to delete the AWS resources you created:

```
# Remove all AWS resources to avoid charges
python ./deployment/cleanup.py
```

## Conclusion

This solution addresses three core underwriting challenges: data scattered across systems, regulatory requirements for explainable decisions, and the need to detect fraud across portfolios. We built this solution by combining three key components: Amazon Nova 2 Lite to generate transparent step-by-step reasoning for every underwriting decision, Amazon Bedrock AgentCore to provide managed MCP server infrastructure with OAuth 2.0 authentication and automatic scaling, and Quick Suite to deliver natural language queries with multi-turn conversation context. The architecture unifies data from DynamoDB and Amazon S3, processes requests through stateless components for horizontal scaling, and maintains complete audit trails in CloudWatch for regulatory compliance. With this solution, underwriters can ask questions like “Assess risk for applicant APP-0900” and get detailed analysis immediately. Investigators can query “Show me all claims filed within 30 days of policy inception” to identify potential untrustworthy activities. Business leaders can gain real-time portfolio intelligence through natural language interactions.

To try this solution, clone the
[GitHub repository](https://github.com/aws-samples/sample-quicksuite-chatagent-insurance-underwriting)
and follow the implementation steps.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/03/Satya-adimula-blog-photo.jpg)
**Satyanarayana Adimula**
is a Senior Builder in the AWS GenAI Invocation Center. With over 20 years of experience in data and analytics and deep expertise in generative AI, he helps organizations achieve measurable business outcomes. He builds agentic AI systems that automate workflows, accelerate decision-making, reduce costs, increase productivity, and create new revenue opportunities. His work spans large enterprise customers across various industries, including retail, banking, financial services, insurance, healthcare, media and entertainment, and professional services.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/08/10/sunita.jpg)
Sunita Koppar**
is a Senior Specialist Solutions Architect in Generative AI and Machine Learning at AWS, where she partners with customers across diverse industries to design solutions, build proof-of-concepts, and drive measurable business outcomes. Beyond her professional role, she is deeply passionate about learning and teaching Sanskrit, actively engaging with student communities to help them upskill and grow.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/12/02/Madhu-Pai.png)
**Madhu Pai**
, Ph.D., is a Principal Specialist Solutions Architect for Generative AI and Machine Learning at AWS. He leads strategic AI/ML initiatives that deliver scalable impact across diverse industries by identifying customer needs and building impactful solutions. Previously at AWS, Madhu served as the WW Partner Tech Lead for Manufacturing where he delivered compelling partner solutions that drove strategic outcomes for industrial manufacturing customers. He brings over 18 years of experience across multiple industries, leveraging data, AI, and ML to deliver measurable business results.