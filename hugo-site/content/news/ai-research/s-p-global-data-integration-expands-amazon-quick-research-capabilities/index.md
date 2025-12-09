---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-09T00:03:18.435454+00:00'
exported_at: '2025-12-09T00:03:21.647003+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/sp-global-data-integration-expands-amazon-quick-research-capabilities
structured_data:
  about: []
  author: ''
  description: Today, we are pleased to announce a new integration between Amazon
    Quick Research and S&P Global. This integration brings both S&P Global Energy
    news, research, and insights and S&P Global Market Intelligence data to Quick
    Research customers in one deep research agent. In this post, we explore S&P Global’s
    data sets and the solution architecture of the integration with Quick Research.
  headline: S&P Global Data integration expands Amazon Quick Research capabilities
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/sp-global-data-integration-expands-amazon-quick-research-capabilities
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: S&P Global Data integration expands Amazon Quick Research capabilities
updated_at: '2025-12-09T00:03:18.435454+00:00'
url_hash: bf416eb6bb24a4e3392ca1e1e2af44dcbe271d40
---

Today, we are pleased to announce a
[new integration](https://aws.amazon.com/about-aws/whats-new/2025/11/amazon-quick-research-third-party-industry-intelligence)
between
[Amazon Quick Research](https://aws.amazon.com/quicksuite/research/)
and S&P Global. This integration brings both S&P Global Energy news, research, and insights and S&P Global Market Intelligence data to Quick Research customers in one deep research agent.

The S&P Global integration extends the capabilities of Quick Research so that business professionals can analyze multiple data sources—including global energy news and premium financial intelligence—in one workspace, eliminating the need to switch between platforms and transforming weeks of research into minutes of focused insight generation. Quick Suite connects information across internal repositories, popular applications, AWS services, and through
[Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)
(MCP) integrations, to over 1,000 apps. This agentic AI application is reshaping how work gets done by transforming how teams find insights, conduct deep research, automate tasks, visualize data, and take actions across apps.

In this post, we explore S&P Global’s data sets and the solution architecture of the integration with Quick Research.

## Solution overview

[S&P Global](https://www.spglobal.com/)
has pioneered two MCP server implementations on AWS so organizations can easily integrate trusted financial services and energy content into AI-powered workflows while maintaining the quality, security, and reliability that business leaders demand.

> *“Our collaboration with AWS expands how S&P Global delivers trusted intelligence through the next generation of agentic AI experiences. By working alongside leading AI companies, our goal is to ensure customers can access our trusted data and insights wherever their workflows take place.”*
>
> – Bhavesh Dayalji, Chief AI Officer of S&P Global and CEO of Kensho.

### S&P Global Energy: Comprehensive commodity and energy intelligence

The S&P Global Energy integration, now available in Amazon Quick Research, utilizes an
[AI Ready Data](https://www.marketplace.spglobal.com/en/datasets/ai-ready-data-(1725478050))
MCP server to deliver comprehensive access to commodity and energy market intelligence spanning Oil, Gas, Power, Metals, Clean Energy, Agriculture, and Shipping sectors across global markets. Built on S&P Global’s reputation as a trusted market authority, the MCP server uses hundreds of thousands of expert-created documents including analyses, commentaries, and news articles reflecting decades of industry expertise.

The solution provides a unique multi-horizon perspective, offering intelligence from daily market updates to one-year outlooks and extending to 20+ year scenario analyses. With data refreshing every 30 minutes, business leaders gain near real-time access to commodity and energy intelligence, dramatically accelerating decision velocity when exploring regulatory challenges, investment opportunities, or environmental implications.

### S&P Global Market Intelligence: Trusted financial intelligence

The S&P Global Market Intelligence integration, now available in Amazon Quick Research, uses the Kensho LLM-ready API MCP server developed by Kensho, S&P Global’s AI innovation hub. This MCP server makes trusted financial data accessible through natural language queries, integrating seamlessly with Amazon Quick Research. Financial professionals can access S&P Capital IQ Financials, earnings call transcripts, company information, transactions and more, simply by asking questions.

The Kensho solution addresses a critical challenge in financial services: making vast repositories of financial data immediately accessible without requiring complex query languages or technical expertise. Engineering, product, and business teams can save significant time and resources by transforming what once required hours of data extraction into conversational queries that return precise, trusted information in seconds.

## Solution architecture

S&P Global’s MCP server architecture is shown in the following diagram. When using one of the S&P integrations, traffic flows from Quick Research through an
[Amazon API Gateway](https://aws.amazon.com/api-gateway/)
to an
[AWS Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
with the MCP services hosted on
[Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/)
(Amazon EKS). The MCP server uses data hosted in
[Amazon S3](https://aws.amazon.com/s3/)
and
[AWS Relational Database Service for PostgreSQL](https://aws.amazon.com/rds/)
for structured data, and
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
for vector storage. This architecture delivers enterprise-ready MCP servers with defense-in-depth security, automated scaling, and comprehensive observability.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/21/ML-20016-image-1.png)

[MCP](https://modelcontextprotocol.io/docs/getting-started/intro)
is an open standard that supports seamless communication between AI agents and external data sources, tools, and services. MCP operates on a client-server architecture where MCP servers handle tool calls, typically consisting of multiple API calls and expose business logic implementations as callable functions. This enables AI agents to discover capabilities dynamically, negotiate features, and share context securely with all critical requirements for enterprise-grade applications.

S&P Global’s solution has the following key building blocks:

* **Automated data pipeline with Amazon Bedrock:**
  At the heart of the solution is a Retrieval Augmented Generation (RAG) data ingestion pipeline using
  [Amazon Bedrock](https://aws.amazon.com/bedrock/)
  . This pipeline transforms raw market data into
  [AI Ready Data](https://www.marketplace.spglobal.com/en/datasets/ai-ready-data-(1725478050))
  . Documents from S&P Global’s proprietary repositories undergo preprocessing, chunking, and enrichment before being converted into vector embeddings using Bedrock hosted Cohere Embed model. The ingestion pipeline runs on a scheduled basis, refreshing the OpenSearch vector store every 30 minutes for near real-time access to the energy data.
* **Vector and semantic search:**
  Amazon OpenSearch serves as the vector database, storing embeddings generated by Bedrock and enabling semantic search capabilities across S&P Global’s energy data. The OpenSearch vector store is optimized for high-dimensional vector operations, supporting rapid similarity searches that power the MCP servers’ ability to retrieve contextually relevant information in response to natural language queries.
* **Resilience and scale:**
  This solution uses Amazon EKS to host all MCP server solutions with two production clusters enabling traffic splitting and failover capabilities. This dual-cluster approach provides continuous availability even during unexpected failures. Both the Cluster Autoscaler and Horizontal Pod Autoscaler enable dynamic scaling based on demand. The MCP servers are built with the FastMCP framework, providing high-performance HTTP endpoints that comply with the Streamable HTTP Transport specification required by the MCP protocol.
* **Security**
  : Security is built-in to every layer of the solution. API Gateway serves as the endpoint for MCP server access. S&P Global’s enterprise identity provider is used for
  [OAuth](https://datatracker.ietf.org/doc/html/rfc6749)
  authentication. API Gateway is further secured with
  [AWS Web Application Firewall](https://aws.amazon.com/waf/)
  (WAF) with advanced threat detection.
  [AWS IAM](https://aws.amazon.com/iam/)
  roles and policies enforce least privilege principles, so that each component has only the permissions it requires.
  [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
  securely stores credentials for accessing resources and AWS services. AWS
  [Security Groups](https://docs.aws.amazon.com/eks/latest/best-practices/sgpp.html)
  and
  [VPC](https://aws.amazon.com/vpc/)
  configurations provide network isolation, while TLS 1.2+ with
  [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/)
  validates all data in transit remains encrypted. This multi-layered security includes defense-in-depth security controls.
* **Observability:**
  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
  provides centralized logging, metrics collection, and real-time monitoring of the entire pipeline from data ingestion through MCP server responses.
  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
  captures detailed API activity logs and audit trails, essential for compliance in regulated industries.

## Conclusion

Together, these MCP servers built on AWS and integrated into Amazon Quick Research demonstrates S&P Global’s vision for the future of financial services and energy intelligence: maintaining the trust, accuracy, and depth that business leaders require while embracing the transformative potential of AI to make that intelligence more accessible, actionable, and integrated into modern workflows.

Ready to get started? Please refer to
[Quick Research Third Party Data](https://docs.aws.amazon.com/quicksuite/latest/userguide/third-party-data)
for more details.

---

### About the authors

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/21/jeinkauf.jpeg)
Jon Einkauf**
is a Product leader at AWS based in Seattle, where he focuses on building AI-powered tools that help businesses synthesize information and accelerate research. With over a decade of experience at Amazon spanning digital health, cloud computing, and AI products, he has led cross-functional teams in product management, engineering, and design to deliver innovative solutions for customers worldwide.

**![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/21/ponnoth.jpeg)
Prasanth Ponnoth**
is an AWS solutions architect supporting global financial services with more than 20 years of industry and technology experience with cloud migration, modernization and building distributed systems at scale. His areas of interests are machine learning, containers/ Kubernetes and open-source technologies. In AWS, he is part of the machine learning technical field community and focusing on Amazon Bedrock, Amazon SageMaker AI, Amazon Bedrock AgentCore services.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/21/brandon.png)
**Brandon Pominville**
is a Senior Solutions Architect at AWS based in New York, where he works with global financial services customers to build secure, scalable data and AI platforms in the cloud. With over 20 years of experience across financial services, enterprise data platforms, and cloud computing, he specializes in translating business requirements into technical solutions. Outside of work, Brandon enjoys spending time with his family outdoors or on a cruise ship, and playing volleyball.