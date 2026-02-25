---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-25T05:16:37.692844+00:00'
exported_at: '2026-02-25T05:16:40.574285+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html
structured_data:
  about: []
  author: ''
  description: Infostealer malware stole OpenClaw AI agent files including tokens
    and keys, while exposed instances and malicious skills expand security risks.
  headline: Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Infostealer Steals OpenClaw AI Agent Configuration Files and Gateway Tokens
updated_at: '2026-02-25T05:16:37.692844+00:00'
url_hash: bc54b988aa9cb8011be5a3934fe3c19f680270bc
---

**

Ravie Lakshmanan
**

Feb 16, 2026

Artificial Intelligence / Threat Intelligence

Cybersecurity researchers disclosed they have detected a case of an information stealer infection successfully exfiltrating a victim's
[OpenClaw](https://thehackernews.com/2026/02/openclaw-integrates-virustotal-scanning.html)
(formerly
**Clawdbot**
and
**Moltbot**
) configuration environment.

"This finding marks a significant milestone in the evolution of infostealer behavior: the transition from stealing browser credentials to harvesting the 'souls' and identities of personal AI [artificial intelligence] agents," Hudson Rock
[said](https://www.infostealers.com/article/hudson-rock-identifies-real-world-infostealer-infection-targeting-openclaw-configurations/)
.

Alon Gal, CTO of Hudson Rock, told The Hacker News that the stealer was likely a variant of Vidar based on the infection details. Vidar is an
[off-the-shelf information stealer](https://thehackernews.com/2023/06/vidar-malware-using-new-tactics-to.html)
that's known to be active since late 2018.

That said, the cybersecurity company said the data capture was not facilitated by a custom OpenClaw module within the stealer malware, but rather through a "broad file-grabbing routine" that's designed to look for certain file extensions and specific directory names containing sensitive data.

This included the following files -

* openclaw.json, which contains details related to the
  [OpenClaw gateway token](https://docs.openclaw.ai/gateway)
  , along with the victim's redacted email address and workspace path.
* device.json, which contains cryptographic keys for secure pairing and signing operations within the OpenClaw ecosystem.
* [soul.md](https://docs.openclaw.ai/reference/templates/SOUL)
  , which contains details of the agent's core operational principles, behavioral guidelines, and ethical boundaries.

It's worth noting that the theft of the gateway authentication token can allow an attacker to connect to the victim's local OpenClaw instance remotely if the port is exposed, or even masquerade as the client in authenticated requests to the AI gateway.

"While the malware may have been looking for standard 'secrets,' it inadvertently struck gold by capturing the entire operational context of the user's AI assistant," Hudson Rock added. "As AI agents like OpenClaw become more integrated into professional workflows, infostealer developers will likely release dedicated modules specifically designed to decrypt and parse these files, much like they do for Chrome or Telegram today."

The disclosure comes as
[security issues](https://jfrog.com/blog/giving-openclaw-the-keys-to-your-kingdom-read-this-first/)
with OpenClaw prompted the maintainers of the open-source agentic platform to
[announce](https://trust.openclaw.ai)
a partnership with VirusTotal to scan for malicious skills uploaded to ClawHub, establish a threat model, and add the ability to
[audit for potential misconfigurations](https://docs.openclaw.ai/gateway/security)
.

Last week, the OpenSourceMalware team detailed an ongoing ClawHub malicious skills campaign that uses a new technique to bypass VirusTotal scanning by hosting the malware on lookalike OpenClaw websites and using the skills purely as decoys, instead of embedding the payload directly in their SKILL.md files.

"The shift from embedded payloads to external malware hosting shows threat actors adapting to detection capabilities," security researcher Paul McCarty
[said](https://opensourcemalware.com/blog/malicious-clawhub-skills-hide-in-plain-sight)
. "As AI skill registries grow, they become increasingly attractive targets for supply chain attacks."

Another
[security problem](https://www.ox.security/blog/moltbook-blocks-account-deletion-privacy-risks/)
highlighted by OX Security concerns
[Moltbook](https://www.moltbook.com)
, a Reddit-like internet forum designed exclusively for artificial intelligence agents, mainly those running on OpenClaw. The research found that an AI Agent account, once created on Moltbook, cannot be deleted. This means that users who wish to delete the accounts and remove the associated data have no recourse.

What's more, an analysis published by SecurityScorecard's STRIKE Threat Intelligence team has also found
[hundreds of thousands of exposed OpenClaw instances](https://declawed.io)
, potentially making users susceptible to remote code execution (RCE) risks.

|  |
| --- |
|  |
| Fake OpenClaw Website Serving Malware |

"RCE vulnerabilities allow an attacker to send a malicious request to a service and execute arbitrary code on the underlying system," the cybersecurity company
[said](https://securityscorecard.com/blog/how-exposed-openclaw-deployments-turn-agentic-ai-into-an-attack-surface/)
. "When OpenClaw runs with permissions to email, APIs, cloud services, or internal resources, an RCE vulnerability can become a pivot point. A bad actor does not need to break into multiple systems. They need one exposed service that already has authority to act."

OpenClaw has had a viral surge in interest since it first debuted in November 2025. As of writing, the open-source project has
[more than 200,000 stars](https://github.com/openclaw/openclaw)
on GitHub. On February 15, 2026, OpenAI CEO Sam Altman
[said](https://x.com/sama/status/2023150230905159801)
OpenClaw's founder, Peter Steinberger, would be joining the AI company, adding, "OpenClaw will live in a foundation as an open source project that OpenAI will continue to support."