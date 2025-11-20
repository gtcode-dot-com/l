---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-20T00:00:17.803851+00:00'
exported_at: '2025-11-20T00:00:21.587608+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/claude-code-deployment-patterns-and-best-practices-with-amazon-bedrock
structured_data:
  about: []
  author: ''
  description: In this post, we explore deployment patterns and best practices for
    Claude Code with Amazon Bedrock, covering authentication methods, infrastructure
    decisions, and monitoring strategies to help enterprises deploy securely at scale.
    We recommend using Direct IdP integration for authentication, a dedicated AWS
    account for infrastructure, and OpenTelemetry with CloudWatch dashboards for comprehensive
    monitoring to ensure secure access, capacity management, and visibility into costs
    and developer productivity .
  headline: Claude Code deployment patterns and best practices with Amazon Bedrock
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/claude-code-deployment-patterns-and-best-practices-with-amazon-bedrock
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Claude Code deployment patterns and best practices with Amazon Bedrock
updated_at: '2025-11-20T00:00:17.803851+00:00'
url_hash: 0acc3ccc5e1076a0afcd495420f29eb7388360d1
---

[Claude Code](https://www.claude.com/product/claude-code)
is an AI-powered coding assistant from Anthropic that helps developers write, review, and modify code through natural language interactions.
[Amazon Bedrock](https://aws.amazon.com/bedrock/)
is a fully managed service that provides access to foundation models from leading AI companies through a single API. This post shows you how to deploy Claude Code with Amazon Bedrock. You’ll learn authentication methods, infrastructure decisions, and monitoring strategies to deploy securely at enterprise scale.

## Recommendations for most enterprises

We recommend the
[Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
, which implements proven patterns that can be deployed in hours.

Deploy Claude Code with this proven stack:

This architecture provides secure access with user attribution, capacity management, and visibility into costs and developer productivity.

## Authentication methods

Claude Code deployments begin with authenticating to Amazon Bedrock. The authentication decision impacts downstream security, monitoring, operations, and developer experience.

### Authentication methods comparison

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Feature** | **API Keys** | **AWS log in** | **SSO with IAM Identity Center** | **Direct IdP Integration** |
| Session duration | Indefinite | Configurable (up to 12 hours) | Configurable (up to 12 hours) | Configurable (up to 12 hours) |
| Setup time | Minutes | Minutes | Hours | Hours |
| Security risk | High | Low | Low | Low |
| User attribution | None | Basic | Basic | Complete |
| MFA support | No | Yes | Yes | Yes |
| OpenTelemetry integration | None | Limited | Limited | Complete |
| Cost allocation | None | Limited | Limited | Complete |
| Operation overhead | High | Medium | Medium | Low |
| Use case | Short term testing | Testing and limited deployments | Quick SSO deployment | Production deployment |

The following will discuss the trade-offs and implementation considerations laid out in the above table.

### API keys

Amazon Bedrock supports
[API keys](https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html)
as the quickest path to proof-of-concept. Both short-term (12-hour) and long-term (indefinite) keys can be generated through the
[AWS Management Console](https://aws.amazon.com/console/)
,
[AWS CLI](https://aws.amazon.com/cli/)
, or SDKs.

However, API keys create security vulnerabilities through persistent access without MFA, manual distribution requirements, and risk of repository commits. They provide no user attribution for cost allocation or monitoring. Use only for short-term testing (< 1 week, 12-hour expiration).

### AWS log in

The
`aws login`
command uses your AWS Management Console credentials for Amazon Bedrock access through a browser-based authentication flow. It supports quick setup without API keys and is recommended for testing and small deployments.

### Single Sign-On (SSO)

[AWS IAM Identity Center](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html)
integrates with existing enterprise identity providers through
[OpenID Connect](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)
(OIDC), an authentication protocol that enables single sign-on by allowing identity providers to verify user identities and share authentication information with applications. This integration allows developers to use corporate credentials to access Amazon Bedrock without distributing API keys.

Developers authenticate with AWS IAM Identity Center using the
`aws sso`
[login](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sign-in.html)
command, which generates temporary credentials with configurable session durations. These credentials automatically refresh, reducing the operational overhead of credential management while improving security through temporary, time-limited access.

```
aws sso login --profile=your-profile-name
export CLAUDE_CODE_USE_BEDROCK=1
export AWS_PROFILE=your-profile-name
```

Organizations using IAM Identity Center for AWS access can extend this pattern to Claude Code. However, it limits detailed user-level monitoring by not exposing OIDC JWT tokens for OpenTelemetry attribute extraction.

This authentication method suits organizations that prioritize rapid SSO deployment over detailed monitoring or initial rollouts where comprehensive metrics aren’t yet required.

### Direct idP integration

Direct OIDC federation with your identity provider (Okta, Azure AD, Auth0, or
[AWS Cognito User Pools](https://aws.amazon.com/cognito/)
) is recommended for production Claude Code deployments. This approach connects your enterprise identity provider directly to AWS IAM to generate temporary credentials with full user context for monitoring.

The
[process credential provider](https://docs.aws.amazon.com/sdkref/latest/guide/feature-process-credentials.html)
orchestrates the OAuth2 authentication with PKCE, a security extension that helps prevent authorization code interception. Developers authenticate in their browser, exchanging OIDC tokens for AWS temporary credentials.

A helper script uses
[AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
(STS)
[AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)
to assume a role with credentials to
[InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html)
and
[InvokeModelWithStreaming](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
to use Amazon Bedrock. Direct IAM federation supports session durations up to 12 hours and the JWT token remains accessible throughout the session, enabling monitoring through OpenTelemetry to track user attributes like email, department, and team.

The
[Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
implements both Cognito Identity Pool and Direct IAM federation patterns, but recommends Direct IAM for simplicity. The solution provides an interactive setup wizard that configures your OIDC provider integration, deploys the necessary IAM infrastructure, and builds distribution packages for Windows, macOS, and Linux.

Developers receive installation packages that configure their AWS CLI profile to use the credential process. Authentication occurs through corporate credentials, with automatic browser opening to refresh credentials. The credential process handles token caching, credential refresh, and error recovery.

For organizations requiring detailed usage monitoring, cost attribution by developer, and comprehensive audit trails, direct IdP integration through IAM federation provides the foundation for advanced monitoring capabilities discussed later in this post.

## Organizational decisions

Beyond authentication, architectural decisions shape how Claude Code integrates with your AWS infrastructure. These choices affect operational complexity, cost management, and enforcement of usage policies.

### Public endpoints

Amazon Bedrock provides managed,
[public API endpoints](https://docs.aws.amazon.com/general/latest/gr/bedrock.html)
in multiple AWS Regions with minimal operational overhead. AWS manages infrastructure, scaling, availability, and security patching. Developers use standard AWS credentials through AWS CLI profiles or environment variables. Combined with OpenTelemetry metrics from Direct IdP integration, you can track usage through public endpoints by individual developer, department, or cost center and can be enforced at the AWS IAM level. For example, implementing per-developer rate limiting requires infrastructure that observes CloudWatch metrics or
[CloudTrail](https://aws.amazon.com/cloudtrail/)
logs and takes automated action. Organizations requiring immediate, request-level blocking based on custom business logic may need additional components such as an LLM (Large Language Model) gateway pattern. Public Amazon Bedrock endpoints are sufficient for most organizations as they provide a balance of simplicity, AWS managed reliability, cost alerting, and appropriate control mechanisms.

### LLM gateway

An LLM gateway introduces an intermediary application layer between developers and Amazon Bedrock, routing requests through custom infrastructure. The
[Guidance for Multi-Provider Generative AI Gateway on AWS](https://aws.amazon.com/solutions/guidance/multi-provider-generative-ai-gateway-on-aws/)
describes this pattern, deploying a containerized proxy service with load balancing and centralized credential management.

This architecture is best for:

* **Multi-provider support**
  : Routing between Amazon Bedrock, OpenAI, and Azure OpenAI based on availability, cost, or capability
* **Custom middleware**
  : Proprietary prompt engineering, content filtering, or prompt injection detection at the request level
* **Request-level policy enforcement**
  : Immediate blocking of requests exceeding custom business logic beyond IAM capabilities

Gateways provide unified APIs and real-time tracking but add operational overhead:
[Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/)
/
[Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)
infrastructure,
[Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/)
[Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/)
,
[Amazon ElastiCache](https://aws.amazon.com/elasticache/)
,
[Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
management, increased latency, and a new failure mode where gateway issues block Claude Code usage. LLM gateways excel for applications making programmatic calls to LLMs, providing centralized monitoring, per user visibility, and unified control access providers.

For traditional API access scenarios, organizations can deploy gateways to gain monitoring and attribution capabilities. The Claude Code guidance solution already includes monitoring and attribution capabilities through Direct IdP authentication, OpenTelemetry metrics, IAM policies, and CloudWatch dashboards. Adding an LLM gateway to the guidance solution duplicates existing functionality. Consider gateways only for multi-provider support, custom middleware, or request-level policy enforcement beyond IAM.

### Single account implementation

We recommend consolidating coding assistant inferences in a single dedicated account, separate from your development and production workloads. This approach provides five key benefits:

1. **Simplified operations:**
   Manage quotas and monitor usage through unified dashboards instead of tracking across multiple accounts. Request quota increases once rather than per account.
2. **Clear cost visibility:**
   [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
   and
   [Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
   show Claude Code charges directly without complex tagging. OpenTelemetry metrics enable department and team-level allocation.
3. **Centralized security:**
   CloudTrail logs flow to one location for monitoring and compliance. Deploy the monitoring stack once to collect metrics from developers.
4. **Production protection:**
   Account-level isolation helps prevent Claude Code usage from exhausting quotas and throttling production applications. Production traffic spikes do not affect developer productivity.
5. **Implementation:**
   Cross-account IAM configuration lets developers authenticate through identity providers that federate to restricted roles, granting only model invocation permissions with appropriate guardrails.

This strategy integrates with Direct IdP authentication and OpenTelemetry monitoring. Identity providers handle authentication, the dedicated account handles inference, and development accounts focus on applications.

### Inference profiles

[Amazon Bedrock inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-use.html)
provide cost tracking through resource tagging, but don’t scale to per-developer granularity. While you can create application profiles for cost allocation, managing profiles for 1000+ individual developers becomes operationally burdensome. Inference profiles work best for organizations with 10-50 distinct teams requiring isolated cost tracking, or when using cross-Region inference where managed routing distributes requests across AWS Regions. They’re ideal for scenarios requiring basic cost allocation rather than comprehensive monitoring.

System-defined cross-Region inference profiles automatically route requests across multiple AWS Regions, distributing load for higher throughput and availability. When you invoke a cross-Region profile (e.g.,
`us.anthropic.claude-sonnet-4`
), Amazon Bedrock selects an available Region to process your request.

Application inference profiles are profiles you create explicitly in your account, typically wrapped around a system-defined profile or a specific model in a Region. You can tag application profiles with custom key-value pairs like
`team:data-science`
or
`project:fraud-detection`
that flow to AWS Cost and Usage Reports for cost allocation analysis. To create an application profile:

```
aws bedrock create-inference-profile \
   --inference-profile-name team-data-science \
   --model-source arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-sonnet-4 \
   --tags team=data-science costcenter=engineering
```

Tags appear in AWS Cost and Usage Reports, so you can query:

`"What did the data-science team spend on Amazon Bedrock last month?"`

Each profile must be referenced explicitly in API calls, meaning developers’ credential configurations must specify their unique profile rather than a shared endpoint.

For more on inference profiles, see
[Amazon Bedrock Inference Profiles documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)
.

### Monitoring

An effective monitoring strategy transforms Claude Code from a productivity tool into a measurable investment by tracking usage, costs, and impact.

#### Progressive enhancement path

Monitoring layers are complementary. Organizations typically start with basic visibility and add capabilities as ROI requirements justify additional infrastructure.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/blog-6.png)

Let’s explore each level and when it makes sense for your deployment.

**Note:**
Infrastructure costs grow progressively—each level retains the previous layers while adding new components.

#### CloudWatch

Amazon Bedrock publishes metrics to Amazon CloudWatch automatically, tracking invocation counts, throttling errors, and latency. CloudWatch graphs show aggregate trends such as total requests, average latency, and quota utilization with minimal deployment effort. This baseline monitoring is included in the standard pricing of CloudWatch and requires minimal deployment effort. You can create CloudWatch alarms that notify you when invocation rates spike, error rates exceed thresholds, or latency degrades.

#### Invocation logging

Amazon Bedrock invocation logging captures detailed information about each API call to
[Amazon S3](https://aws.amazon.com/s3/)
or CloudWatch Logs, preserving individual request records including invocation metadata and full request/response data. Process logs with
[Amazon Athena,](https://aws.amazon.com/athena/)
load into data warehouses, or analyze with custom tools. The logs display usage patterns, invocations by model, peak utilization, and an audit trail of Amazon Bedrock access.

#### OpenTelemetry

Claude Code includes support for
[OpenTelemetry](https://opentelemetry.io/)
, an open source observability framework for collecting application telemetry data. When configured with an OpenTelemetry collector endpoint, Claude Code emits detailed metrics about its operations for both Amazon Bedrock API calls and higher-level development activities.

The telemetry captures detailed code-level metrics not included in Amazon Bedrock’s default logging, such as: lines of code added/deleted, files modified, programming languages used, and developers’ acceptance rates of Claude’s suggestions. It also tracks key operations including file edits, code searches, documentation requests, and refactoring tasks.

The
[guidance solution](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
deploys OpenTelemetry infrastructure on
[Amazon ECS Fargate.](https://aws.amazon.com/fargate/)
An Application Load Balancer receives telemetry over HTTP(S) and forwards metrics to an OpenTelemetry Collector. The collector exports data to Amazon CloudWatch and Amazon S3.

#### Dashboard

The guidance solution includes a CloudWatch dashboard that displays key metrics continuously, tracking active users by hour, day, or week to reveal adoption and usage trends that enable per-user cost calculation. Token consumption breaks down by input, output, and cached tokens, with high cache hit rates indicating efficient context reuse and per-user views identifying heavy users. Code activity metrics track lines added and deleted, correlating with token usage to show efficiency and usage patterns.

The operations breakdown shows distribution of file edits, code searches, and documentation requests, while user leaderboards display top consumers by tokens, lines of code, or session duration.

The dashboard updates in near-real-time and integrates with CloudWatch alarms to trigger notifications when metrics exceed thresholds. The guidance solution deploys through CloudFormation with custom Lambda functions for complex aggregations.

#### Analytics

While dashboards excel at real-time monitoring, long-term trends and complex user behavior analysis require analytical tools. The guidance solution’s optional analytics stack streams metrics to Amazon S3 using
[Amazon Data Firehose](https://aws.amazon.com/firehose/)
.
[AWS Glue](https://aws.amazon.com/glue/)
Data Catalog defines the schema, making data queryable through Amazon Athena.

The analytics layer supports queries such as monthly token consumption by department, code acceptance rates by programming language, and token efficiency variations across teams. Cost analysis becomes sophisticated by joining token metrics with Amazon Bedrock pricing to calculate exact costs by user, then aggregate for department-level chargeback. Time-series analysis shows how costs scale with team growth for budget forecasting. The SQL interface integrates with business intelligence tools, enabling exports to spreadsheets, machine learning models, or project management systems.

For example, to see the monthly cost analysis by department:

```
SELECT department, SUM(input_tokens) * 0.003 / 1000 as input_cost,
SUM(output_tokens) * 0.015 / 1000 as output_cost,
COUNT(DISTINCT user_email) as active_users
FROM claude_code_metrics
WHERE year = 2024 AND month = 1
GROUP BY department
ORDER BY (input_cost + output_cost) DESC;
```

The infrastructure adds moderate cost: Data Firehose charges for ingestion, S3 for retention, and Athena charges per query based on data scanned.

Enable analytics when you need historical analysis, complex queries, or integration with business intelligence tools. While the dashboard alone may suffice for small deployments or organizations focused primarily on real-time monitoring, enterprises making significant investments in Claude Code should implement the analytics layer. This provides the visibility needed to demonstrate return on investment and optimize usage over time.

#### Quotas

Quotas allow organizations to control and manage token consumption by setting usage limits for individual developers or teams. Before implementing quotas, we recommend first enabling monitoring to understand natural usage patterns. Usage data typically shows that high token consumption correlates with high productivity, indicating that heavy users deliver proportional value.

The quota system stores limits in DynamoDB with entries like:

```
{ "userId": "jane@example.com", "monthlyLimit": 1000000, "currentUsage": 750000, "resetDate": "2025-02-01" }
```

A Lambda function triggered by CloudWatch Events aggregates token consumption every 15 minutes, updating DynamoDB and publishing to SNS when thresholds are crossed.

#### Monitoring comparison

The following table summarizes the trade-offs across monitoring approaches:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Capability** | **CloudWatch** | **Invocation logging** | **OpenTelemetry** | **Dashboard and Analytics** |
| Set up complexity | None | Low | Medium | Medium |
| User attribution | None | IAM Identity | Full | Full |
| Real-time metrics | Yes | No | Yes | Yes |
| Code-level metrics | No | No | Yes | Yes |
| Historical analysis | Limited | Yes | Yes | Yes |
| Cost allocation | Account level | Account level | User, team, department | User, team, department |
| Token track | Aggregate | Per-request | Per-user | Per-user with trends |
| Quota enforcement | Manual | Manual | Possible | Possible |
| Operational overhead | Minimal | Low | Medium | Medium |
| Cost | Minimal | Low | Medium | Medium |
| Use case | POC | Basic auditing | Production | Enterprise with ROI |

## Putting it together

This section synthesizes authentication methods, organizational architecture, and monitoring strategies into a recommended deployment pattern, providing guidance on implementation priorities as your deployment matures. This architecture balances security, operational simplicity, and comprehensive visibility. Developers authenticate once per day with corporate credentials, administrators see real-time usage in dashboards, and security teams have CloudTrail audit logs and comprehensive user-attributed metrics through OpenTelemetry.

### Implementation path

The guidance solution supports rapid deployment through an interactive setup process, with authentication and monitoring running within hours. Deploy the full stack to a pilot group first, gather real usage data, then expand based on validated patterns.

1. **Deployment –**
   Clone the Guidance for Claude Code with Amazon Bedrock repository and run the interactive poetry run
   `ccwb init`
   wizard. The wizard configures your identity provider, federation type, AWS Regions, and optional monitoring. Deploy the CloudFormation stacks (typically 15-30 minutes), build distribution packages, and test authentication locally before distributing to users.

2. **Distribution –**
   Identify a pilot group of 5-20 developers from different teams. This group will validate authentication, monitoring, and provide usage data for full rollout planning. If you enabled monitoring, the CloudWatch dashboard shows activity immediately. You can monitor token consumption, code acceptance rates, and operation types to estimate capacity requirements, identify training needs, and demonstrate value for a broader rollout.

3. **Expansion –**
   Once Claude Code is validated, expand adoption by team or department. Add the analytics stack (typically 1-2 hours) for historical trend analysis to see adoption rates, high-performing teams, and costs forecasts.

4. **Optimization –**
   Use monitoring data for continuous improvement through regular review cycles with development leadership. The monitoring data can demonstrate value, identify training needs, and guide capacity adjustments.

### When to deviate from the recommended pattern

While the architecture above suits most enterprise deployments, specific circumstances might justify different approaches.

1. **Consider an LLM gateway**
   if you need multiple LLM providers beyond Amazon Bedrock, custom middleware for prompt processing or response filtering, or operate in a regulatory environment requiring request-level policy enforcement beyond the AWS IAM capabilities.
2. **Consider inference profiles**
   if you have under 50 teams requiring separate cost tracking and prefer AWS-native billing allocation over telemetry metrics. Inference profiles work well for project-based cost allocation but do not scale to per-developer tracking.
3. **Consider starting without monitoring**
   for time-limited pilots with under 10 developers where basic CloudWatch metrics suffice. Plan to add monitoring before scaling, as retrofitting requires redistributing packages to developers.
4. **Consider API keys**
   only for time-boxed testing (under one week) where security risks are acceptable.

## Conclusion

Deploying Claude Code with Amazon Bedrock at enterprise scale requires thoughtful authentication, architecture, and monitoring decisions. Production-ready deployments follow a clear pattern: Direct IdP integration provides secure, user-attributed access and a dedicated AWS account simplifies capacity management. OpenTelemetry monitoring provides visibility into costs and developer productivity. The
[Guidance for Claude Code with Amazon Bedrock](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
implements these patterns in a deployable solution. Start with authentication and basic monitoring, then progressively add features as you scale.

As AI-powered development tools become the industry standard, organizations that prioritize security, monitoring, and operational excellence in their deployments will gain lasting advantages. This guide provides a comprehensive framework to help you maximize Claude Code’s potential across your enterprise.

To get started, visit the
[Guidance for Claude Code with Amazon Bedrock repository](https://github.com/aws-solutions-library-samples/guidance-for-claude-code-with-amazon-bedrock)
.

---

### About the authors

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/ML-1891-1-1.png)
**Court Schuett**
is a Principal Specialist Solution Architect – GenAI who spends his days working with AI Coding Assistants to help others get the most out of them. Outside of work, Court enjoys traveling, listening to music, and woodworking.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/ML-1891-2.png)
**Jawhny Cooke**
is the Global Tech Lead for Anthropic’s Claude Code at AWS, where he specializes in helping enterprises operationalize agentic coding at scale. He partners with customers and partners to solve the complex production challenges of AI-assisted development, from designing autonomous coding workflows and orchestrating multi-agent systems to operational optimization on AWS infrastructure. His work bridges cutting-edge AI capabilities with enterprise-grade reliability to help organizations confidently adopt Claude Code in production environments.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/IMG_9092-New-1.jpeg)
**Karan Lakhwani**
is a Sr. Customer Solutions Manager at Amazon Web Services. He specializes in generative AI technologies and is an AWS Golden Jacket recipient. Outside of work, Karan enjoys finding new restaurants and skiing.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/ML-1891-4.jpeg)
**Gabe Levy**
is an Associate Delivery Consultant at AWS based out of New York primarily focused on Application Development in the cloud. Gabe has a sub-specialization in Artificial Intelligence and Machine Learning. When not working with AWS customers, he enjoys exercising, reading and spending time with family and friends.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2025/11/19/image-7-1.jpg)
**Gabriel Velazquez Lopez**
is a GenAI Product Leader at AWS, where he leads the strategy, go-to-market, and product launches for Claude on AWS in partnership with Anthropic.