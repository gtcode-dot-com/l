---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-05T22:04:16.187158+00:00'
exported_at: '2026-03-05T22:04:19.264639+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/nvidia-agentic-ai-blueprints-telco-reasoning-models
structured_data:
  about: []
  author: ''
  description: New open source large telco model and NVIDIA Blueprints enable telecom
    operators to use their own data to train AI agents and build autonomous networks.
  headline: NVIDIA Advances Autonomous Networks With Agentic AI Blueprints and Telco
    Reasoning Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/nvidia-agentic-ai-blueprints-telco-reasoning-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Advances Autonomous Networks With Agentic AI Blueprints and Telco Reasoning
  Models
updated_at: '2026-03-05T22:04:16.187158+00:00'
url_hash: 31bfac3520f1c775e5d3a3bd1458f586dd1e5fbf
---

[Autonomous networks](https://www.nvidia.com/en-us/glossary/autonomous-networks/)
— intelligent, self-managing telecommunications operations — are moving from a future vision to a current priority for telecom operators. In the latest NVIDIA
[State of AI in Telecommunications report](https://www.nvidia.com/en-us/lp/industries/telecommunications/state-of-ai-in-telecom-survey-report/)
, network automation emerged as the top AI use case for investment and return on investment.

Automation is different from autonomy. Beyond executing predefined workflows, autonomous networks must understand operator intent, reason over tradeoffs and decide what actions to take. Reasoning models and AI agents fine-tuned on telecom data are key to enabling this shift.

For networks to become autonomous, there’s a need for an end-to-end agentic system that includes key components like telco network models and AI agents that talk to each other and use network simulation tools to validate actions.

Ahead of Mobile World Congress Barcelona, NVIDIA unveiled an open NVIDIA Nemotron-based large telco model (LTM), a comprehensive guide for building reasoning agents for network operations, and new NVIDIA Blueprints for energy saving and network configuration with multi-agent orchestration to help operators advance toward autonomy.

And as part of GSMA’s new Open Telco AI initiative — launching tomorrow — NVIDIA is releasing the new open source LTM, implementation guide and agentic AI blueprints as open resources through GSMA, an organization for the mobile communications industry.

## **Open Nemotron 3 Large Telco Model Brings Reasoning to Telecom**

For telcos to successfully operationalize generative and agentic AI across their operations, AI models must have the ability to understand the language of telecom and reason through complex workflows. NVIDIA has collaborated with
[AdaptKey AI](https://adaptkey.ai/blog.html)
to release a new open source, 30-billion-parameter NVIDIA Nemotron LTM that operators around the world can use to build autonomous networks.

Built on the NVIDIA Nemotron 3 family of foundation models and fine-tuned by AdaptKey AI using open telecom datasets including industry standards and synthetic logs, the LTM is optimized to understand telecom industry terminology and reason through workflows such as fault isolation, remediation planning and change validation.

As an open model, the Nemotron LTM gives telcos full transparency into how it was trained and what data was used, enabling secure and fast on‑premises deployment within their networks, where they can build and run agents directly. It also lets telcos safely adapt and extend telecom‑tuned reasoning with their own network and operational data, so they can move toward autonomous operations without sacrificing control over data or security.

## **Teaching AI Agents to Reason Like Network Engineers**

NVIDIA and Tech Mahindra have published an open source
[guide](https://developer.nvidia.com/blog/building-telco-reasoning-models-for-autonomous-networks-with-nvidia-nemo/)
that shows telecom operators how to fine-tune domain-specific reasoning models and build agents that can safely execute network operations center (NOC) workflows.

The guide outlines a framework for teaching models to reason like NOC engineers: focus on high‑impact, high‑frequency incident categories, translate expert resolutions into step‑by‑step procedures and turn those into structured reasoning traces that capture each action, tool call, outcome and decision. These traces become the “thinking examples” the model learns from, so it understands not just what to do, but why a particular sequence of checks and fixes is safe and effective.

Using the NVIDIA NeMo-Skills pipeline, operators can fine-tune a reasoning model on these traces, laying the foundation for telco-specialized AI agents that can reason and solve problems like a network engineer.

## **Maximizing Energy Efficiency With New Intent-Driven Energy Saving Blueprint**

Autonomous networks rely on closed‑loop operation: models that understand the network, agents that act on intent and simulation that feeds results back into the system to validate and refine decisions. The new
[NVIDIA Blueprint for intent-driven RAN energy efficiency](https://build.nvidia.com/viavi/intent-driven-ran-energy-efficiency)
brings these pieces together, helping operators systematically reduce power consumption in 5G radio access networks (RAN) while maintaining quality of service.

The blueprint integrates network test and measurement leader
[VIAVI’s](https://blog.viavisolutions.com/2026/03/01/accelerating-ai-native-networks-with-nvidia-ai-ran-platforms/)
TeraVM AI RAN Scenario Generator (AI RSG) platform to generate synthetic network data — including cell utilization, user throughput and other traffic patterns — and convert it into a simple, queryable format.

An energy planning agent then reasons over the synthetic data to generate energy-saving policies that can be simulated in AI RSG, allowing operators to safely validate energy-saving policies in a closed loop to meet their intent without changing live configurations or impacting subscribers.

## **Telcos Put the NVIDIA Blueprint for Network Configuration to Work**

The
[NVIDIA Blueprint for telco network configuration](https://blogs.nvidia.com/blog/ai-blueprint-telco-network-configuration/)
is being adopted by operators around the world.

Cassava Technologies is using the blueprint to build Cassava Autonomous Network, an agentic platform designed to optimize Africa’s diverse, multi-vendor mobile network environment. The platform implements three agents: one to monitor the network and recommend configuration changes, one to apply changes with documentation and governance, and one to assess the impact of changes made and safely roll them back if they have unintended effects.

NTT DATA is implementing the blueprint to bring intelligence to traffic regulation, helping the network manage surges when users reconnect after an outage, and is deploying it with a tier 1 operator in Japan.

An AI agent looks at real-time demand across the network and then decides when and how to admit new users on specific cells. As conditions stabilize, the agent adapts its decisions, turning what used to be manual configurations into a data-driven optimization cycle for more resilient mobile networks.

## **Evolving Network Configuration With Multi-Agent Orchestration**

To help telcos design, observe and optimize complex agentic workflows across the RAN, NVIDIA and
[BubbleRAN](https://bubbleran.com/)
are enhancing the
[NVIDIA Blueprint for telco network configuration](https://build.nvidia.com/nvidia/telco-network-configuration)
with
[NVIDIA NeMo Agent Toolkit](https://developer.nvidia.com/nemo-agent-toolkit)
(NAT) and
[BubbleRAN Agentic Toolkit](https://github.com/bubbleran/bat)
(BAT), complementary frameworks for multi-agent orchestration.

BubbleRAN is integrating NAT and BAT into its
[Opti-Sphere](https://bubbleran.com/news/opti-sphere/)
platform to manage network monitoring, configuration and validation agents more flexibly across containers and workloads, and connect them to tools that report network metrics and traffic status so they can continuously propose and validate configuration changes.

Telenor Group will be the first telco to adopt the blueprint with BubbleRAN to enhance its 5G network for Telenor Maritime, the group’s global connectivity provider at sea.

*Learn more about the latest advancements in agentic AI for telecommunications at*
[*Mobile World Congress*](https://www.nvidia.com/en-us/events/mobile-world-congress/)
*, taking place in Barcelona from March 2-5.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*