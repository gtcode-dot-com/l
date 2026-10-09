---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-29T20:15:14.515182+00:00'
exported_at: '2026-01-29T20:15:16.870666+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/researchers-find-175000-publicly.html
structured_data:
  about: []
  author: ''
  description: Over 175,000 publicly exposed Ollama AI servers across 130 countries,
    with many enabling tool calling that allows code execution and LLMjacking abuse.
  headline: Researchers Find 175,000 Publicly Exposed Ollama AI Servers Across 130
    Countries
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/researchers-find-175000-publicly.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Find 175,000 Publicly Exposed Ollama AI Servers Across 130 Countries
updated_at: '2026-01-29T20:15:14.515182+00:00'
url_hash: d1f2d1beb7d326be6f4cabcf03f2e71faba8cc58
---

A new joint investigation by SentinelOne SentinelLABS, and Censys has revealed that the open-source artificial intelligence (AI) deployment has created a vast "unmanaged, publicly accessible layer of AI compute infrastructure" that spans 175,000 unique Ollama hosts across 130 countries.

These systems, which span both cloud and residential networks across the world, operate outside the guardrails and monitoring systems that platform providers implement by default, the company said. The vast majority of the exposures are located in China, accounting for a little over 30%. The countries with the most infrastructure footprint include the U.S., Germany, France, South Korea, India, Russia, Singapore, Brazil, and the U.K.

"Nearly half of observed hosts are configured with tool-calling capabilities that enable them to execute code, access APIs, and interact with external systems, demonstrating the increasing implementation of LLMs into larger system processes," researchers Gabriel Bernadett-Shapiro and Silas Cutler
[added](https://www.sentinelone.com/labs/silent-brothers-ollama-hosts-form-anonymous-ai-network-beyond-platform-guardrails/)
.

Ollama is an open-source framework that allows users to easily download, run, and manage large language models (LLMs) locally on Windows, macOS, and Linux. While the service binds to the localhost address at 127.0.0[.]1:11434 by default, it's possible to expose it to the public internet by means of a trivial change: configuring it to bind to 0.0.0[.]0 or a public interface.

The fact that Ollama, like the recently popular
[Moltbot](https://thehackernews.com/2026/01/fake-moltbot-ai-coding-assistant-on-vs.html)
(formerly Clawdbot), is hosted locally and operates outside of the enterprise security perimeter, poses new security concerns. This, in turn, necessitates new approaches to distinguish between managed and unmanaged AI compute, the researchers said.

Of the observed hosts, more than 48% advertise tool-calling capabilities via their API endpoints that, when queried, return metadata highlighting the functionalities they support. Tool calling (or function calling) is a capability that allows LLMs to interact with external systems, APIs, and databases, enabling them to augment their capabilities or retrieve real-time data.

"Tool-calling capabilities fundamentally alter the threat model. A text-generation endpoint can produce harmful content, but a tool-enabled endpoint can execute privileged operations," the researchers noted. "When combined with insufficient authentication and network exposure, this creates what we assess to be the highest-severity risk in the ecosystem."

The analysis has also identified hosts supporting various modalities that go beyond text, including reasoning and vision capabilities, with 201 hosts running uncensored prompt templates that remove safety guardrails.

The exposed nature of these systems means they could be susceptible to
[LLMjacking](https://thehackernews.com/2025/01/microsoft-sues-hacking-group-exploiting.html)
, where a victim's LLM infrastructure resources are abused by bad actors to their advantage, while the victim foots the bill. These could range from generating spam emails and disinformation campaigns to cryptocurrency mining and even reselling access to other criminal groups.

The risk is not theoretical. According to a report published by Pillar Security this week, threat actors are actively targeting exposed LLM service endpoints to monetize access to the AI infrastructure as part of an LLMjacking campaign
[dubbed](https://www.pillar.security/resources/operation-bizarre-bazaar)
Operation Bizarre Bazaar.

The findings point to a criminal service that contains three components: systematically scanning the internet for exposed Ollama instances, vLLM servers, and OpenAI-compatible APIs running without authentication, validating the endpoints by assessing response quality, and commercializing the access at discounted rates by advertising it on silver[.]inc, which operates as a Unified LLM API Gateway.

"This end-to-end operation – from reconnaissance to commercial resale – represents the first documented LLMjacking marketplace with complete attribution," researchers Eilon Cohen and Ariel Fogel said. The operation has been traced to a threat actor named Hecker (aka Sakuya and LiveGamer101).

The decentralized nature of the exposed Ollama ecosystem, one that's spread across cloud and residential environments, creates governance gaps, not to mention creates new avenues for prompt injections and proxying malicious traffic through victim infrastructure.

"The residential nature of much of the infrastructure complicates traditional governance and requires new approaches that distinguish between managed cloud deployments and distributed edge infrastructure," the companies said. "For defenders, the key takeaway is that LLMs are increasingly deployed to the edge to translate instructions into actions. As such, they must be treated with the same authentication, monitoring, and network controls as other externally accessible infrastructure."