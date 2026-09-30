---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:38:22.062343+00:00'
exported_at: '2026-09-30T02:38:23.358941+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore
structured_data:
  about: []
  author: ''
  description: Learn how Heurist built Heurist Finance, a conversational AI investment
    workbench, on Amazon Bedrock AgentCore. This customer story shows how AgentCore
    payments, Identity, Memory, Code Interpreter, and Observability let a small team
    buy premium market data per query, isolate analysis in a sandbox, and keep every
    act...
  headline: How Heurist Finance built an AI-native investment workbench on Amazon
    Bedrock AgentCore
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Heurist Finance built an AI-native investment workbench on Amazon Bedrock
  AgentCore
updated_at: '2026-09-30T02:38:22.062343+00:00'
url_hash: 43b1f218724ec6e033fb2bbfcbe068517f69a709
---

[Heurist](https://www.heurist.ai/)
uses
[Amazon Bedrock AgentCore](/bedrock/agentcore/)
to build AI-powered financial intelligence for retail investors. Its flagship product, Heurist Finance, brings several institutional-style workflows into one chat experience: it gathers market data, reads filings and news, runs deep research, builds and stress-tests portfolios, and monitors positions. Each answer reflects the user’s portfolio and preferences. Heurist’s goal is to make tools such as unified risk-and-return views, whole-portfolio construction, and scenario analysis accessible to anyone with a market question.

This post explains how Heurist built the system behind Heurist Finance on Amazon Bedrock AgentCore, using
[AgentCore payments](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html)
, a capability of Amazon Bedrock AgentCore, to buy premium data per query. It shows how paid data access, sandboxed analysis, identity, memory, and observability come together in an auditable response.

## Business challenge

Heurist gives retail investors access to research built on premium market, macroeconomic, fundamental, and alternative data. Those sources sit behind paywalls and bespoke APIs. No single vendor covers them all, and enterprise contracts are difficult to justify before a product has a large user base. Buying only the data required for each question offered a better economic model, but it introduced another problem. The agent would need to spend funds on a user’s behalf while enforcing custody, spending limits, and audit requirements.

This creates a broader production challenge. Every action had to map to a specific user, session, and request, so identity needed to persist across the full workflow. The team also needed cross-session state, isolated code execution, payment orchestration, and end-to-end tracing. Building that infrastructure in-house could take months and divert the team from the research workflows and personalization that differentiate Heurist Finance.

## Solution overview

Heurist deployed its agents on Amazon Bedrock AgentCore, a platform to build, connect, and optimize agents at scale with any framework or model. Heurist orchestrates its agents with
[Strands](https://strandsagents.com/)
and uses
[Anthropic Claude](/bedrock/anthropic/)
, available on Amazon Bedrock. Figure 1 shows how the surrounding AgentCore services support each request.

[![Architecture diagram of Heurist Finance on Amazon Bedrock AgentCore. A Strands orchestrator connects user portfolio data in Amazon Aurora PostgreSQL to Anthropic Claude on Amazon Bedrock and to AgentCore Identity, memory, Code Interpreter, Observability, and payments. Analysis artifacts go to Amazon S3, traces go to Amazon CloudWatch, credentials remain in AWS Secrets Manager, and paid x402 requests settle in USDC on Base.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/27/ML-21623-1.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/27/ML-21623-1.png)

Figure 1: Heurist Finance solution architecture on Amazon Bedrock AgentCore

Figure 1 shows the Strands orchestrator calling Anthropic Claude on Amazon Bedrock, loading portfolio data from
[Amazon Aurora PostgreSQL](/rds/aurora/)
, and coordinating AgentCore
[Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity-overview.html)
,
[Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
,
[Code Interpreter](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/code-interpreter-tool.html)
,
[Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
, and payments. Analysis artifacts go to
[Amazon Simple Storage Service (Amazon S3)](/s3/)
, and traces go to
[Amazon CloudWatch](/cloudwatch/)
. Credentials remain in
[AWS Secrets Manager](/secrets-manager/)
, while AgentCore payments connects paid data requests to USDC stablecoin settlement on the
[Base](https://www.base.org/)
blockchain network.

## Answering a question across paid data

A single user turn can combine prices, macroeconomic indicators, filings, fundamentals, and news, then run correlations, scenario analysis, charts, or backtests over the results. AgentCore Code Interpreter, a capability of Amazon Bedrock AgentCore, performs that work in an isolated sandbox with no arbitrary network egress. The sandbox runs in the AWS Cloud and tears down when the analysis finishes.

Some of that data costs money, and Heurist Finance buys it per query through Amazon Bedrock AgentCore payments. A Payment Manager coordinates a
`CoinbaseCDP`
Payment Connector. Each interaction receives a Payment Session with a
`maxSpendAmount`
value that caps spending for that run and a Payment Instrument (an embedded crypto wallet) scoped to Base.

Each paid request follows the x402 protocol:

1. Heurist Finance requests a paid data feed from a merchant.
2. The merchant returns HTTP 402 with x402 payment terms: amount, recipient, asset (USDC), and network (Base).
3. AgentCore payments checks the payload against the Payment Session’s
   `maxSpendAmount`
   value. If the charge would exceed the cap, Heurist Finance tells the user and suggests alternatives.
4. Within budget, Heurist Finance calls the Process Payment API, which signs the payment through the Payment Instrument. Credentials are retrieved at runtime from AWS Secrets Manager.
5. Heurist Finance retries the request with proof in the
   `X-PAYMENT`
   header, and the merchant returns the data.

With x402, Heurist Finance buys only the data a question needs, without a vendor contract or prepayment. Heurist implements the flow with AgentCore payments, a Payment Manager, a Payment Connector, and SDK integration.

## Research that knows the investor

When a user asks a broad question, such as whether a specific stock is overvalued, Heurist Finance grounds the research in the user’s holdings, watchlist, time horizon, and risk preferences. The answer builds on prior context instead of starting from zero and becomes more specific as the profile develops.

AgentCore memory, a capability of Amazon Bedrock AgentCore, stores the user’s preferences, thesis state, and conversation history across sessions. AgentCore Identity, a capability of Amazon Bedrock AgentCore, scopes that store to one user, so Heurist does not need to build a separate preference store and access-control layer.

## Isolation, security, and audit

A user’s profile and conversation history can reveal beliefs, risk tolerance, time horizon, and positions. Heurist therefore treats identity, access, and audit as part of every request.

AgentCore Identity carries the authenticated user through every service call. Each tool call, payment, and memory operation records the user ID, workload identity, request ID, and trace ID, creating one audit trail across services.

Each service also enforces its own boundary. AgentCore Identity accepts OAuth and issues scoped credentials. AgentCore payments scopes the Payment Session and Payment Instrument per user, AgentCore memory binds profile and conversation data to one user, and AgentCore Code Interpreter isolates the analysis runtime.

Amazon Bedrock Guardrails filters both input and output. Input filters help block prompt-injection attempts aimed at payment and data tools, while output filters help enforce Heurist’s policy against recommending an unhedged single stock. Payment credentials stay in AWS Secrets Manager, where the Payment Credential Provider retrieves them at runtime for the Payment Connector.

## Request flow: One user question

Consider the question, “How does today’s PCE release impact my portfolio?” The orchestrator loads the user’s portfolio from Amazon Aurora PostgreSQL, with AgentCore Identity scoping the read to that user. The orchestrator then calls a paid consensus-forecast endpoint. After receiving HTTP 402, AgentCore payments checks the Payment Session spend cap and signs the payment through the Payment Instrument. The orchestrator retries the request with proof in the
`X-PAYMENT`
header.

AgentCore Code Interpreter computes the portfolio impact and writes a chart to Amazon S3 from within its sandbox. Amazon Bedrock synthesizes the answer using the user’s holdings, time horizon, and risk preferences, and the response streams back with the chart attached. Figure 2 traces this sequence end to end.

[![Sequence diagram for the question ‘How does today’s PCE release impact my portfolio?’ Heurist Finance loads the user profile, purchases consensus data through AgentCore payments and x402, computes portfolio impact in AgentCore Code Interpreter, stores a chart in Amazon S3, and streams the answer.](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/27/ML-21623-2.png)](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/27/ML-21623-2.png)

Figure 2: Request flow for a single user question, from profile lookup to paid data purchase to streamed answer

The example brings Amazon Aurora, AgentCore Identity, AgentCore payments, AgentCore Code Interpreter, Amazon S3, Amazon Bedrock, and AgentCore Observability, a capability of Amazon Bedrock AgentCore, into one workflow. Shared user and trace context connects the paid data purchase to the resulting portfolio analysis.

## Outcome

Heurist estimates roughly 80% less agent-system engineering than an in-house large language model (LLM) orchestration stack, because AgentCore manages identity, cross-session memory, sandboxing, and payments infrastructure. It also provides Heurist with predictable per-user marginal costs that support retail pricing.

The architecture also provides two operational properties:

* AgentCore Observability traces make agent decisions reproducible, allowing compliance questions to be resolved in a single query, increasing compliance readiness and decreasing troubleshooting time.
* Payment credentials remain in AWS Secrets Manager and are retrieved at runtime by the Payment Connector, increasing safety for end users.

&gt; *“AgentCore does the platform work so we can double down our energy on the product work. The managed infrastructure saved us months.”*

— JW Wang, Founder of Heurist

## Conclusion

Heurist’s experience shows how managed agent infrastructure can let a small team focus on differentiated financial research rather than the system beneath it. AgentCore payments is central to that model: it gives the product governed, auditable access to paid data without requiring Heurist to build payment infrastructure from scratch.

## What’s next

With that foundation in place, Heurist is extending the product in three directions: event-driven research tied to earnings calendars, portfolio-aware analysis of market events, and recommendations based on what traders with similar horizons are researching.

## Get started

AgentCore payments is available in the regions listed
[here](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-regions.html)
. To learn more, visit the
[AgentCore payments documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/payments.html)
or the
[AWS News Blog](/blogs/machine-learning/amazon-bedrock-agentcore-payments-is-now-generally-available-enabling-agents-to-transact-safely-and-autonomously-at-scale/)
.

---

## About the authors

### JW Wang

JW is the founder of Heurist AI. He brings agentic AI to blockchains and financial markets, with a focus on making institutional-grade financial intelligence accessible to individual investors.

### Joshua Smith

Joshua is a Fintech Solutions Architect at AWS. He is passionate about solving high-scale distributed systems challenges and helping customers build secure, reliable, cost-effective, and AI-enabled solutions including agentic commerce. He has a background in security and systems engineering in early startups, large enterprises, and federal agencies.

### Chethan Shriyan

Chethan is a Principal Product Manager – Technical at AWS. He has 12+ years of experience in product and business management. Chethan is passionate about building and delivering technology products that create meaningful impact in customers’ lives.