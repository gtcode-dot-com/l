---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-27T00:15:51.785529+00:00'
exported_at: '2026-03-27T00:15:54.401257+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell
structured_data:
  about: []
  author: ''
  description: NVIDIA OpenShell provides tools for controlling autonomous agents in
    a trusted infrastructure policy layer.
  headline: How Autonomous AI Agents Become Secure by Design With NVIDIA OpenShell
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/secure-autonomous-ai-agents-openshell
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How Autonomous AI Agents Become Secure by Design With NVIDIA OpenShell
updated_at: '2026-03-27T00:15:51.785529+00:00'
url_hash: 7b5460e97f025d40887ab688fcf79290c5532049
---

Autonomous agents mark a new inflection point in AI. Systems are no longer limited to generating responses or reasoning through tasks. They can take action: Agents can read files, use tools, write and run code, and execute workflows across enterprise systems, all while expanding their own capabilities.

Application-layer risk grows exponentially when agents continuously improve and evolve. The
[NVIDIA OpenShell](https://developer.nvidia.com/blog/run-autonomous-self-evolving-agents-more-safely-with-nvidia-openshell/)

runtime is being built to address this.

Part of
[NVIDIA Agent Toolkit](https://nvidianews.nvidia.com/news/ai-agents)

, OpenShell is an open source, secure-by-design runtime for running autonomous agents such as claws. It works by ensuring each agent runs inside its own sandbox, separating application-layer operations from infrastructure-layer policy enforcement.

This means security policies are out of reach of the agent — they’re applied at the system level. Instead of relying on behavioral prompts, OpenShell enforces constraints on the environment the agent runs in — meaning the agent cannot override policies, or leak credentials or private data, even if compromised.

With OpenShell, enterprises can separate agent behavior, policy definition and policy enforcement. Organizations gain a single, unified policy layer to define and monitor how autonomous systems operate. Coding agents, research assistants and agentic workflows all run under the same runtime policies regardless of host operating system, simplifying compliance and operational oversight.

This is the “browser tab” model applied to agents: Sessions are isolated, resources are controlled and permissions are verified by the runtime before any action takes place.

Securing autonomous systems requires an integrated ecosystem. OpenShell is designed to add privacy and security controls for AI agents. NVIDIA is collaborating with security partners, including
[Cisco](https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2026/m03/cisco-reimagines-security-for-the-agentic-workforce.html)

,
[CrowdStrike](https://www.crowdstrike.com/en-us/press-releases/crowdstrike-nvidia-unveil-secure-by-design-ai-blueprint-for-ai-agents/)

,

Google Cloud

,

Microsoft Security

and
[TrendAI](https://www.trendmicro.com/en_us/research/26/c/securing-autonomous-ai-agents-with-trendai-and-nvidia-openshell.html)

,

to align runtime policy management and enforcement for agents across the enterprise stack.

## **OpenShell Provides an Enterprise-Grade Sandbox for Building Personal AI Assistants**

[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/)

is an open source reference stack that simplifies installing OpenClaw always-on assistants with the OpenShell runtime and
[NVIDIA Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

models in a single command.

NemoClaw provides enthusiasts with an open reference for building self-evolving personal AI agents, or claws. Since security needs vary, NemoClaw provides a reference example for policy-based privacy and security guardrails to give users more control over their agents’ behavior and data-handling. Users can customize it for their specific use cases — much like adjusting security preferences for applications on a phone.

NemoClaw includes an example configuration of OpenShell that defines how the agent should interact with systems. NemoClaw uses open source models like NVIDIA Nemotron alongside OpenShell.

This enables self-evolving claws to run more securely in clouds, on premises or on personal computers, including
[NVIDIA GeForce RTX PCs and laptops](https://www.nvidia.com/en-us/ai-on-rtx/)

or
[NVIDIA RTX PRO-powered workstations](https://www.nvidia.com/en-us/products/workstations/)

, as well as
[NVIDIA DGX Station and NVIDIA DGX Spark](https://blogs.nvidia.com/blog/gtc-2026-news/#dgx-spark-station)

AI supercomputers

.

Both OpenShell and NemoClaw are in early preview. NVIDIA is building in the open with the community and its partners to enable enterprises to scale self-evolving, long-running autonomous agents safely, confidently and in compliance with global security standards.

Get started with
[NVIDIA OpenShell](https://build.nvidia.com/openshell)

and launch a ready‑to‑use environment on
[NVIDIA Brev](https://brev.nvidia.com/launchable/deploy/now?launchableID=env-3Azt0aYgVNFEuz7opyx3gscmowS)

, or explore the open source project on
[GitHub](https://github.com/nvidia/openshell)

.