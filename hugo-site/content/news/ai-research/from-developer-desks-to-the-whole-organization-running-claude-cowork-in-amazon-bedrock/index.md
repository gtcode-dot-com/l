---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-21T20:15:33.940602+00:00'
exported_at: '2026-04-21T20:15:36.181373+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/from-developer-desks-to-the-whole-organization-running-claude-cowork-in-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: Today, we're excited to announce Claude Cowork in Amazon Bedrock. You
    can now run Cowork and Claude Code Desktop through Amazon Bedrock, directly or
    using an LLM gateway. In this post, we walk through how Claude Cowork integrates
    with Amazon Bedrock and show an example of how knowledge workers use it in practice.
  headline: 'From developer desks to the whole organization: Running Claude Cowork
    in Amazon Bedrock'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/from-developer-desks-to-the-whole-organization-running-claude-cowork-in-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'From developer desks to the whole organization: Running Claude Cowork in Amazon
  Bedrock'
updated_at: '2026-04-21T20:15:33.940602+00:00'
url_hash: b748565c93617678f0ad369b98b2ddd8fe19f5d6
---

Today, we’re excited to announce Claude Cowork in Amazon Bedrock. You can now run Cowork and Claude Code Desktop through Amazon Bedrock, directly or using an LLM gateway.

From startups to global enterprises across every industry, organizations build with Claude Code in Amazon Bedrock to boost developer productivity and accelerate delivery. With Amazon Bedrock you can build within your existing AWS environment, maintain enterprise security and regional data residency, and scale inference. Your data stays under your account’s controls: Amazon Bedrock does not store prompts, files, tool inputs and outputs, or model responses, and does not use them to train foundation models.

With Claude Cowork in Amazon Bedrock, you can expand AI adoption to every knowledge worker in your organization, with a desktop application that reads documents, runs multi-step research, processes files, and returns finished work.

In this post, we walk through how Claude Cowork integrates with Amazon Bedrock and show an example of how knowledge workers use it in practice.

## What is Claude Cowork

With Claude Cowork, your users can delegate research, document analysis, data processing, and report generation to Claude from a desktop application. They get the core
[Claude Desktop](https://code.claude.com/docs/en/desktop-quickstart)
capabilities including
[projects](https://support.claude.com/en/articles/9517075-what-are-projects)
,
[artifacts](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
,
[memory](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)
,
[file upload and export](https://support.claude.com/en/articles/8241126-uploading-files-to-claude)
,
[remote connectors](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
,
[skills](https://support.claude.com/en/articles/12512176-what-are-skills)
,
[plugins](https://support.claude.com/en/articles/13837440-use-plugins-in-claude-cowork)
, and
[MCP servers](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
. Features that require Anthropic-hosted inference, including the Chat tab, Computer Use, and the Skills Marketplace, are not included because Claude Cowork routes model inference exclusively through Amazon Bedrock in your AWS account. For a full feature comparison with Claude Enterprise, see
[Features on 3P](https://claude.com/docs/cowork/3p/feature-matrix)
.

Pricing is consumption-based through your existing AWS agreement and billing, with no seat licensing from Anthropic.

## How Claude Cowork Integrates with Amazon Bedrock

Amazon Bedrock serves as the inference backend in your AWS account and
[supported AWS Regions](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
.

Configuring Claude Cowork in Amazon Bedrock takes two steps. First, users download the
[Claude Desktop](https://claude.ai/downloads)
application on their machine. Second, your device-management system (such as Jamf, Microsoft Intune, or Group Policy) pushes a configuration to Claude Desktop that activates the inference mode, specifying the
[model ID and Amazon Bedrock Inference Profile](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
, authentication method, and organizational policies. If your organization centralizes model access through an LLM gateway, you point Claude Desktop at the gateway URL through the same managed configuration.

If your organization already builds with Claude Code in Amazon Bedrock, Claude Cowork can use the same setup.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/04/21/figure1-new.png)

*Figure 1: The following diagram illustrates the end-to-end flow*

The application has three outbound paths, all under your control. Model inference goes to Amazon Bedrock in the AWS Regions you configure. MCP server connections, if configured, go to endpoints you approve. Anthropic receives only aggregate telemetry (token counts, model ID, error codes, anonymous device identifier), which can be disabled through configuration options.

Amazon Bedrock offers in-Region, geo cross-Region, and global cross-Region
[inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html#cross-region-inference-comparison)
so you can choose the right level of data residency for your organization.

Claude Cowork works with the AWS services you already use:

For details on MDM configuration, credentials, MCP servers, and plugins, see the
[Claude Cowork Configuration Reference](https://claude.com/docs/cowork/3p/configuration)
.

## Claude Cowork in practice

With the integration configured, your users open Claude Desktop and start delegating work. Claude Cowork can connect to external data sources through MCP servers, giving Claude access to live documentation, web search, and other tools as it works.

For example, a product manager is planning a new notification feature for a university athletics app hosted on AWS. They have customer meeting notes that point in different directions, a set of project requirements, and limited time to reconcile them. They upload them to Cowork.

Claude compares the disparate inputs and synthesizes them into a single product brief. It evaluates the proposed approach, research alternatives, flags technical challenges, and backs recommendations with proof points. Connected to the
[AWS Documentation MCP server](https://github.com/awslabs/mcp/tree/main/src/aws-documentation-mcp-server)
and a web search MCP server, Claude grounds the brief in current service documentation, market context, and competitor positioning.

[

](https://d2908q01vomqb2.cloudfront.net/artifacts/DBSBlogs/ML-20855/demo-speed.mp4?_=1)

*Figure 2: The product manager turns meeting notes into a product brief with Claude Cowork*

In minutes, the product manager has a structured brief grounded in current sources and ready for review. The same pattern applies to other knowledge workers. An operations manager can consolidate scattered documentation into an SOP. A finance analyst can turn raw data into a formatted monthly review. A research team can compile findings from multiple sources into a single report.

## Conclusion

With Claude Cowork in Amazon Bedrock, you can expand AI adoption to every knowledge worker in your organization while keeping your data within your AWS environment. Claude Cowork is available on macOS and Windows in AWS Regions where
[Claude models are available on Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards-anthropic.html)
. To get started, download Claude Desktop from
[claude.com/download](http://claude.com/download)
and see the
[Claude Cowork Setup Guide](https://claude.com/docs/cowork/3p/overview)
.

Give Claude Cowork a try today and send feedback to AWS re:Post for Amazon Bedrock or through your usual AWS Support contacts.

---

## About the authors

### Sofian Hamiti

Sofian Hamiti is a technology leader with over 12 years of experience building AI solutions, and leading high-performing teams to maximize customer outcomes. He is passionate about empowering diverse talents to drive global impact and achieve their career aspirations.

### Ayan Ray

Ayan Ray is a Principal Partner Solutions Architect and AI Tech Lead at AWS, serving as the Global Tech Lead for Anthropic at AWS. He works at the intersection of cloud architecture and Artificial Intelligence, helping organizations adopt and scale Anthropic’s technologies on AWS.

### Antonio Rodriguez

Antonio Rodriguez is a Principal Specialist Solutions Architect for Amazon Bedrock at AWS, specializing in enterprise generative AI architecture and regulated industry deployments.