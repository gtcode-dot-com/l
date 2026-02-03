---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-03T18:15:17.863757+00:00'
exported_at: '2026-02-03T18:15:20.068510+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/docker-fixes-critical-ask-gordon-ai.html
structured_data:
  about: []
  author: ''
  description: Docker patched a critical Ask Gordon AI flaw enabling code execution
    and data theft via malicious image metadata in version 4.50.0.
  headline: Docker Fixes Critical Ask Gordon AI Flaw Allowing Code Execution via Image
    Metadata
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/docker-fixes-critical-ask-gordon-ai.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Docker Fixes Critical Ask Gordon AI Flaw Allowing Code Execution via Image
  Metadata
updated_at: '2026-02-03T18:15:17.863757+00:00'
url_hash: 7225348003ac49f47171894e4923ea54ab09bece
---

**

Ravie Lakshmanan
**

Feb 03, 2026

Artificial Intelligence / Vulnerability

Cybersecurity researchers have disclosed details of a now-patched security flaw impacting
[Ask Gordon](https://docs.docker.com/ai/gordon/)
, an artificial intelligence (AI) assistant built into Docker Desktop and the Docker Command-Line Interface (CLI), that could be exploited to execute code and exfiltrate sensitive data.

The critical vulnerability has been codenamed
**[DockerDash](https://noma.security/blog/dockerdash-two-attack-paths-one-ai-supply-chain-crisis/)**
by cybersecurity company Noma Labs. It was addressed by Docker with the release of
[version 4.50.0](https://docs.docker.com/desktop/release-notes/#4500)
in November 2025.

"In DockerDash, a single malicious metadata label in a Docker image can be used to compromise your Docker environment through a simple three-stage attack: Gordon AI reads and interprets the malicious instruction, forwards it to the
[MCP](https://www.docker.com/blog/the-model-context-protocol-simplifying-building-ai-apps-with-anthropic-claude-desktop-and-docker/)
[Model Context Protocol] Gateway, which then executes it through MCP tools," Sasi Levi, security research lead at Noma, said in a report shared with The Hacker News.

"Every stage happens with zero validation, taking advantage of current agents and MCP Gateway architecture."

Successful exploitation of the vulnerability could result in critical-impact remote code execution for cloud and CLI systems, or high-impact data exfiltration for desktop applications.

The problem, Noma Security said, stems from the fact that the AI assistant treats unverified metadata as executable commands, allowing it to propagate through different layers sans any validation, allowing an attacker to sidestep security boundaries. The result is that a simple AI query opens the door for tool execution.

With MCP acting as a connective tissue between a large language model (LLM) and the local environment, the issue is a failure of contextual trust. The problem has been characterized as a case of Meta-Context Injection.

"MCP Gateway cannot distinguish between informational metadata (like a standard Docker LABEL) and a pre-authorized, runnable internal instruction," Levi said. "By embedding malicious instructions in these metadata fields, an attacker can hijack the AI's reasoning process."

In a hypothetical attack scenario, a threat actor can exploit a critical trust boundary violation in how Ask Gordon parses container metadata. To accomplish this, the attacker crafts a malicious Docker image with embedded instructions in Dockerfile LABEL fields.

While the metadata fields may seem innocuous, they become vectors for injection when processed by Ask Gordon AI. The code execution attack chain is as follows -

* The attacker publishes a Docker image containing weaponized LABEL instructions in the Dockerfile
* When a victim queries Ask Gordon AI about the image, Gordon reads the image metadata, including all LABEL fields, taking advantage of Ask Gordon's inability to differentiate between legitimate metadata descriptions and embedded malicious instructions
* Ask Gordon to forward the parsed instructions to the MCP gateway, a middleware layer that sits between AI agents and MCP servers.
* MCP Gateway interprets it as a standard request from a trusted source and invokes the specified MCP tools without any additional validation
* MCP tool executes the command with the victim's Docker privileges, achieving code execution

The data exfiltration vulnerability weaponizes the same prompt injection flaw but takes aim at Ask Gordon's Docker Desktop implementation to capture sensitive internal data about the victim's environment using MCP tools by taking advantage of the assistant's read-only permissions.

The gathered information can include details about installed tools, container details, Docker configuration, mounted directories, and network topology.

It's worth noting that Ask Gordon version 4.50.0 also
[resolves](https://thehackernews.com/2025/12/threatsday-bulletin-stealth-loaders-ai.html#ai-assistant-hijack-risk)
a prompt injection vulnerability discovered by Pillar Security that could have allowed attackers to hijack the assistant and exfiltrate sensitive data by tampering with the Docker Hub repository metadata with malicious instructions.

"The DockerDash vulnerability underscores your need to treat AI Supply Chain Risk as a current core threat," Levi said. "It proves that your trusted input sources can be used to hide malicious payloads that easily manipulate AI’s execution path. Mitigating this new class of attacks requires implementing zero-trust validation on all contextual data provided to the AI model."