---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:16:52.474883+00:00'
exported_at: '2026-05-14T21:16:53.787339+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html
structured_data:
  about: []
  author: ''
  description: Microsoft’s new MDASH AI system found 16 Windows vulnerabilities fixed
    in this month’s Patch Tuesday, including 2 RCE flaws in IKEv2 and TCP/IP.
  headline: Microsoft's MDASH AI System Finds 16 Windows Flaws Fixed in Patch Tuesday
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Microsoft's MDASH AI System Finds 16 Windows Flaws Fixed in Patch Tuesday
updated_at: '2026-05-14T21:16:52.474883+00:00'
url_hash: c19ed1ef05a0fe26449affb36ebe15e878157519
---

**

Ravie Lakshmanan
**

May 13, 2026

Vulnerability / Artificial Intelligence

Microsoft has unveiled a new multi-model artificial intelligence (AI)-driven system called
**MDASH**
to facilitate vulnerability discovery and remediation at scale, adding that it's being tested by some customers as part of a limited private preview.

MDASH, short for
**m**
ulti-mo
**d**
el
**a**
gentic
**s**
canning
**h**
arness, is designed as a model-agnostic system that uses bespoke AI agents for different vulnerability classes to autonomously discover, validate, and prove exploitable defects in complex codebases like Windows.

"Unlike single-model approaches, the harness orchestrates more than 100 specialized AI agents across an ensemble of frontier and distilled models to discover, debate, and prove exploitable bugs end-to-end," Taesoo Kim, vice president of agentic security at Microsoft,
[said](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/)
.

MDASH is envisioned as a "structured pipeline" that ingests a codebase and produces validated, proven findings through a series of actions.

It starts with analyzing the source code to build a threat model and attack surface, running specialized "auditor" agents over candidate code paths to flag potential issues, running a second set of "debater" agents that validate the findings, grouping semantically equivalent findings, and then finally proving the existence of the vulnerabilities.

The system is powered by a configurable panel of models, with state-of-the-art (SOTA) models used for reasoning, distilled models for validation for high-volume passes, and a second separate SOTA model for independent counterpoint.

"Disagreement between models is itself a signal: when an auditor flags something as suspect and the debater can't refute it, that finding’s posterior credibility goes up," Microsoft explained. "An auditor does not reason like a debater, which does not reason like a prover. Each pipeline stage has its own role, prompt regime, tools, and stop criteria."

Redmond noted that the specialized agents have been constructed based on past common vulnerabilities and exposures (CVEs) and their patches. It also said the architecture allows for portability across model generations.

MDASH has already been put to test, unearthing 16 of the vulnerabilities that were fixed in this month's Patch Tuesday release. The shortcomings span across the Windows networking and authentication stack, including two critical flaws that could pave the way for remote code execution -

* **[CVE-2026-33824](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33824)**
  (CVSS score: 9.8) - A double-free vulnerability in "ikeext.dll" that could allow an unauthenticated attacker to send specially crafted packets to a Windows machine with Internet Key Exchange (IKE) version 2 enabled, leading to remote code execution.
* **[CVE-2026-33827](https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-33827)**
  (CVSS score: 8.1) - A race condition vulnerability in Windows TCP/IP ("tcpip.sys") that allows an unauthorized attacker to send a specially crafted IPv6 packet to a Windows node where IPSec is enabled, leading to remote code execution exploitation.

News of MDASH follows the debut of Anthropic's
[Project Glasswing](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
and OpenAI
[Daybreak](https://thehackernews.com/2026/05/openai-launches-daybreak-for-ai-powered.html)
, both of which are AI-powered cybersecurity initiatives for accelerating vulnerability discovery, validation, and remediation before they can be discovered by bad actors.

"The strategic implication is clear: AI vulnerability discovery has crossed from research curiosity into production-grade defense at enterprise scale, and the durable advantage lies in the agentic system around the model rather than any single model itself," Kim said.