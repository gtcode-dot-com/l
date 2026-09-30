---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-30T02:38:21.325541+00:00'
exported_at: '2026-09-30T02:38:23.365609+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-august-2026
structured_data:
  about: []
  author: ''
  description: 'A recap of August 2026 launches for AI builders across Amazon Bedrock,
    Amazon Bedrock AgentCore, and Strands: million-token context for OpenAI models,
    cross-Region inference, agents that run for up to 14 days on dedicated compute,
    expanded AWS GovCloud availability, and Strands Robots for physical deployment.'
  headline: 'ICYMI: What landed for AI builders in August 2026'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/icymi-what-landed-for-ai-builders-in-august-2026
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ICYMI: What landed for AI builders in August 2026'
updated_at: '2026-09-30T02:38:21.325541+00:00'
url_hash: 6a453e7cc3ec42d62b00fa0205ef7351ff6262c3
---

*A recap of the biggest Amazon Bedrock, AgentCore, and Strands updates from August 2026.*

At AWS, we have long focused on making foundational technologies accessible and providing the infrastructure needed to put them to work.
[Amazon Bedrock](/bedrock/)
, used by more than 225,000 active customers, including over 80% of Fortune 100 companies, embodies that commitment by providing access to leading models and a broad set of tools to build and scale AI, with the security, reliability, performance, and cost efficiency customers need in production. As agentic applications expand, Amazon Bedrock extends this foundation with
[AgentCore](/bedrock/agentcore/)
, which lets you build, connect, and optimize agents using any framework and model. AWS also released the
[Strands Agent Harness SDK](https://strandsagents.com/)
as open source, giving you the flexibility to create agents and deploy them wherever you choose. Together, they help you turn model intelligence into production agents without limiting how those agents are built or where they run.

As models become more capable, organizations can ask a more ambitious question: how much meaningful work can AI take on from start to finish? Across industries, agents are moving into workflows that require them to reason over enterprise information, remain productive over longer time horizons, and act across digital and physical systems. As the scope of that work expands, attention is shifting to the complete system around the model, including what context it can access, what actions it can take, where data is processed, and how its decisions and costs are governed.

We believe the next phase of AI will be shaped not only by what models can do, but by how confidently you can delegate responsibility to the systems built around them. That confidence depends on systems that can understand the task in front of them, persist as it unfolds, and operate within clear organizational boundaries. August’s updates move in that direction, giving you stronger foundations for AI systems that can understand more, work longer, and take on demanding responsibility across enterprise, regulated, and physical environments.

## **Reason over more context at scale with greater control**

**Bring entire working sets and current web context into your OpenAI applications on Amazon Bedrock.**
GPT-5.6 Sol, Terra, and Luna now support
[million-token context windows](/about-aws/whats-new/2026/08/gpt-sol-terra-luna-long-context-bedrock/)
with prompt caching, helping reduce cost and latency when context is reused.
[Web Search](/about-aws/whats-new/2026/08/amazon-bedrock-web/)
lets the models find current information beyond their training data, incorporate relevant results into their answers, and provide citations without requiring you to integrate a separate search provider. For use cases that need the freshest details, such as live pricing or newly released documentation, the models can also
[retrieve content directly](/about-aws/whats-new/2026/08/amazon-bedrock-web-access-web-search/)
from public websites. Together, these capabilities let you analyze an entire codebase or regulatory document, check its contents against the latest public information, and return a cited response from a single API call.

[**Route inference globally**](/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/)
**without stitching together Regions.**
With cross-Region inference, you can access GPT-5.6 Sol, Terra, and Luna from more than 25 AWS Regions. Global profiles give you the broadest capacity at lower per-token prices, while Geo profiles keep inference processing within a defined geography. With these updates, you can increase throughput during demand spikes while choosing the geographic boundary that fits your application’s data-processing requirements.

**Understand and control inference spend as model usage grows.**
[IAM principal cost allocation](/about-aws/whats-new/2026/08/amazon-bedrock-expands-iam-principal-cost-allocation-bedrock-mantle/)
helps you attribute inference spend to a user, team, project, application, or cost center, while
[AWS Cost Anomaly Detection](/about-aws/whats-new/2026/08/aws-cost-anomaly-detection-bedrock-3P/)
now monitors third-party foundation model spend on Amazon Bedrock and provides root-cause breakdowns when costs change unexpectedly. OpenAI also announced lower pricing across the GPT-5.6 family on Amazon Bedrock, including
[Luna, Terra,](/about-aws/whats-new/2026/07/openai-gpt-terra-luna-pricing-bedrock/)
and
[Sol](/about-aws/whats-new/2026/08/bedrock-openai-gpt-56-sol-reduced-pricing/)
. This gives you greater visibility into which teams are driving spend, helps you catch unusual changes earlier, and supports more informed decisions as AI workloads scale.

## **Faster cyber defense from detection to response**

**Give security teams frontier AI for both defensive and authorized offensive workflows.**
[Daybreak Red and Daybreak Blue from OpenAI](/about-aws/whats-new/2026/08/openai-daybreak-red-and-blue-on-amazon-bedrock/)
are now available to eligible customers on Amazon Bedrock. Daybreak Blue supports defensive work such as vulnerability discovery, detection engineering, and incident response. Daybreak Red supports advanced, authorized tasks such as vulnerability research, exploit reproduction, and mitigation development. You can now investigate and address vulnerabilities faster while applying stronger identity verification, monitoring, access controls, and zero-operator-access infrastructure.

## **Get more done with agents that stay on track**

**Keep production agents running long enough to complete multi-day work.**
[AgentCore runtime instances](/about-aws/whats-new/2026/08/aws-bedrock-agentcore-runtime-instances-generally-available/)
let you run agents on dedicated Amazon EC2 compute, including GPU-accelerated, memory-optimized, and compute-optimized instances, with sessions lasting up to 14 days.
[AgentCore also expanded](/about-aws/whats-new/2026/08/bedrock-agentcore-two-new-regions/)
to US West (N. California) and Asia Pacific (Hyderabad). You can now hand agents long-running research, coding, and monitoring work, match each workload to the compute it needs, and run it closer to the users and systems it serves.

**Let agents act more independently while keeping their behavior and spending within defined boundaries.**
[Temporal policies](/about-aws/whats-new/2026/08/temporal-policies-agentcore/)
evaluate each action against what an agent has already done, letting you enforce sequences, prerequisites, approval gates, matching values between calls, and data freshness. Rate limiting controls requests, inference tokens, and concurrent connections by user or group.
[AgentCore payments](/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/)
lets agents access and pay for APIs, MCP resources, and paid content with infrastructure-enforced spending limits and end-to-end observability. Together, these updates let you give agents more independence while controlling what can happen, in what order, at what rate, and within what budget.

**Give agents timely context without weakening data boundaries.**
[Web Search in AgentCore](/about-aws/whats-new/2026/08/web-search-amazon-bedrock/)
lets agents include or exclude domains and filter results by publication date, helping them retrieve current information from approved sources.
[AgentCore memory](/about-aws/whats-new/2026/08/agentcore-memory-json-payloads)
can extract long-term memories from activity logs, behavioral events, system events, and other structured JSON data, not only from conversations.
[Fine-grained access control](/about-aws/whats-new/2026/08/agentcorememory-fine-grained-access-control)
can then isolate those memories by user or tenant. Now you can ground agents in trusted sources, build memory from business events, and keep that context isolated without adding custom authorization logic to every application.

**Find and reuse approved agents and tools instead of rebuilding what already exists**
.
[AWS Agent Registry](/blogs/machine-learning/manage-agents-tools-and-skills-at-scale-with-aws-agent-registry/)
gives you a searchable, governed catalog for agents, MCP servers, skills, and custom resources. Organization-wide detection can identify agents on AgentCore Runtime and MCP servers on AgentCore Gateway across connected AWS accounts, while approved resources can also surface in Amazon Quick. You can find trusted capabilities by intent or name, reuse them across workflows, and reduce agent sprawl and duplicative development.

## **Build with more choice in regulated environments**

**Bring advanced models, agent capabilities, and cross-modal retrieval to regulated workloads**
.
[Claude Opus 5](/about-aws/whats-new/2026/07/claude-opus-5-aws-govcloud/)
is now available in AWS GovCloud (US) Regions with zero data retention enabled by default.
[OpenAI GPT-5.6 Terra and Luna](/about-aws/whats-new/2026/08/openai-gpt-terra-luna-govcloud/)
are also available in AWS GovCloud (US) Regions, with million-token context windows and prompt caching.
[Amazon Nova Multimodal Embeddings](/about-aws/whats-new/2026/08/amazon-nova-mme-govcloud/)
brings retrieval across text, documents, images, video, and audio to AWS GovCloud (US-West), while
[AgentCore memory, policy, and the managed harness](/about-aws/whats-new/2026/08/agentcore-memory-policy-harness-govcloud/)
add managed context, controls, and orchestration. This helps you build coding agents, document-analysis systems, multimodal retrieval applications, and governed agent workflows in AWS GovCloud using more of the same capabilities available in commercial Regions.

## **Extend AI agents into the physical world**

**Move from robot demonstrations to training and physical deployment through one connected workflow**
.
[Strands Robots connects Strands Agents, LeRobot, and Hugging Face Storage Buckets](https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop/)
, letting you record demonstrations, stream datasets in the LeRobot format, train policies, and deploy them to simulated or physical hardware without converting the underlying data. This allows you to iterate on robotics policies using one data format and one agent workflow from simulation through physical deployment.

**Coordinate multiple robots and devices without rebuilding the agent for each environment.**
[Strands Robots supports mesh-based discovery and coordination](https://strandsagents.com/blog/robots-working-together-model-hardware-standard-strands-robots/)
across simulated and physical devices. Zenoh connects robots on the same local network, while AWS IoT Core supports geographically distributed fleets. Strands Robots and AWS are also participating in the limited research preview of the Model Hardware Standard. This makes it easier for you to prototype multi-robot workflows in simulation, move them across local and cloud-connected fleets with fewer code changes, and explore standardized controls for physical equipment.

## **Get started**

Explore
[Amazon Bedrock](https://aws-samples.github.io/sample-amazon-bedrock-central/)
, deploy agents with the
[AgentCore CLI](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agentcore-get-started-cli.html)
, or build your first agent with the
[Strands Harness SDK](https://strandsagents.com/)
.

*Interested in learning how Amazon Bedrock can support your team?*
[*Connect with us*](https://pages.awscloud.com/Amazon-Bedrock-Contact-Us.html)
*to start the conversation.*

---

## About the authors