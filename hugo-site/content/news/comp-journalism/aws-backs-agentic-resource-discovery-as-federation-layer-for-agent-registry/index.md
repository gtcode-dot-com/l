---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-09-27T18:36:27.035445+00:00'
exported_at: '2026-09-27T18:36:29.542179+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/aws-backs-agentic-resource-discovery-as-federation-layer-for-agent-registry
structured_data:
  about: []
  author: ''
  description: Amazon Web Services has put its weight behind the Agentic Resource
    Discovery specification, publishing a detailed account on August 24, 2026 of how
    the open standard is meant to work alongside AWS Agent Registry, its man...
  headline: AWS Backs Agentic Resource Discovery as Federation Layer for Agent Registry
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/aws-backs-agentic-resource-discovery-as-federation-layer-for-agent-registry
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AWS Backs Agentic Resource Discovery as Federation Layer for Agent Registry
updated_at: '2026-09-27T18:36:27.035445+00:00'
url_hash: dc0f2507c23552a654e4a6c90c072311bbb55592
---

Amazon Web Services has put its weight behind the Agentic Resource Discovery specification, publishing a detailed account on August 24, 2026 of how the open standard is meant to work alongside AWS Agent Registry, its managed catalog for AI agents, tools, and skills that entered preview earlier this year.

The
[AWS post](https://aws.amazon.com/blogs/machine-learning/agentic-resource-discovery-ard-an-open-specification-for-agent-discovery/)
frames ARD as the answer to a problem AWS’s own product leaves open.
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
, available through Amazon Bedrock AgentCore, gives an organization a centralized, searchable catalog for agents, MCP servers, tools, agent skills, and custom resources, but only inside its own AWS environment. Most enterprises run agents across multiple clouds, on-premises infrastructure, and SaaS platforms, each with its own registry and metadata format, and bridging those environments today means building bespoke connectors between every pair of registries.

ARD proposes the shared-format alternative: if every registry describes resources the same way and exposes discovery through a common protocol, publishers describe their resources once and consumers discover them everywhere.

## Inside the AWS Agent Registry Model

The registry, currently in preview through Amazon Bedrock AgentCore, is built around two concepts: registries, which are catalogs an administrator creates with their own authorization and approval settings, and records, the metadata entries describing each resource. The publishing workflow runs administrator to publisher to curator to consumer, with an approval gate before any record becomes discoverable. Access is controlled through AWS Identity and Access Management credentials or JSON Web Tokens from a corporate identity provider, and the registry itself is exposed as a remote MCP endpoint, so any MCP-compatible client can search it directly.

That governance layer is the part AWS is careful to preserve. In the post, AWS describes ARD as an interoperability layer sitting outside the enforcement point: the organization that publishes a catalog controls what’s in it, who can see it, and when to revoke access, with Agent Registry’s existing approval and access controls remaining where policy is actually enforced. The language is deliberate: ARD handles finding things, not trusting them into production.

## What the ARD Specification Actually Standardizes

ARD is not an AWS project. The specification was announced on June 17, 2026 by a working group whose participants include Google, Microsoft, Hugging Face, and GoDaddy, with Cisco, Databricks, GitHub, NVIDIA, Salesforce, ServiceNow, and Snowflake among the collaborators on the launch. It is licensed under Apache 2.0 and published at
[agenticresourcediscovery.org](https://agenticresourcediscovery.org/)
, with reference implementations on GitHub. AWS contributed feedback during development rather than authoring the spec.

Per
[Google’s announcement](https://developers.googleblog.com/announcing-the-agentic-resource-discovery-specification/)
, the architecture rests on two primitives. A catalog is a file an organization publishes under its own domain (an ai-catalog.json at a well-known path) describing its available agents, MCP servers, A2A agents, OpenAPI tools, or nested catalogs, with domain ownership serving as the cryptographic basis for publisher identity. Registries act as search engines over those catalogs: they crawl, index, and answer plain-language discovery requests, returning matches along with the verifiable trust metadata a client needs to confirm a publisher’s identity before connecting.

The boundary ARD draws is discovery, not execution. A client that finds a resource through ARD invokes it through whatever mechanism that resource natively speaks: MCP, an API, an agent framework. The spec’s own site is explicit that ARD is not a runtime, not a replacement for MCP or the A2A protocol, and not a central catalog; the design assumes many discovery services, each applying its own trust and ranking policies. AWS’s analogy is DNS: local registries federate through the shared protocol without bilateral agreements or proprietary connectors, the way name resolution works across networks.

## How the Pieces Fit Together

For Agent Registry customers, the pitch is federation without migration. An organization with agentic infrastructure spread across clouds, on-premises systems, and SaaS tools could expose all of it in ARD’s format and make it discoverable across environments while keeping control local, and could publish a catalog on its own domain for discovery by any ARD-compatible client, opening cross-organizational paths that a single-vendor registry can’t reach.

AWS is also arriving with product in hand where others are still building. Google’s own Agent Registry, part of its Gemini Enterprise Agent Platform, is slated to add native ARD support in the coming months; GitHub and Hugging Face are among the working-group participants behind the specification. The pattern across all three clouds is the same: a managed, governed registry on the inside, an open federation protocol on the outside.

The caveat is that the integration described in the AWS post is directional, not shipped. AWS states what it expects ARD to enable for Agent Registry customers rather than announcing a delivery date, and the registry itself remains in preview. What August 24, 2026 establishes is alignment: the largest cloud provider has named the open specification it intends to federate with, and it’s the same one Google and Microsoft are building toward.