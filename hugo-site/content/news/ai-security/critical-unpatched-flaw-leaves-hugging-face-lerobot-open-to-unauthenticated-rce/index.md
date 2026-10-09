---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-28T12:15:14.698792+00:00'
exported_at: '2026-04-28T12:15:17.212754+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html
structured_data:
  about: []
  author: ''
  description: CVE-2026-25874 (CVSS 9.3) in LeRobot 0.4.3 allows unauthenticated RCE
    via pickle over gRPC, risking AI systems and sensitive data.
  headline: Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated
    RCE
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Critical Unpatched Flaw Leaves Hugging Face LeRobot Open to Unauthenticated
  RCE
updated_at: '2026-04-28T12:15:14.698792+00:00'
url_hash: 797e5495a26fd6b638d716dcd7878aa5dda0945d
---

**

Ravie Lakshmanan
**

Apr 28, 2026

Vulnerability / Network Security

Cybersecurity researchers have disclosed details of a critical security flaw impacting
[LeRobot](https://arxiv.org/abs/2602.22818)
, Hugging Face's open-source robotics platform with
[nearly 24,000 GitHub stars](https://github.com/huggingface/lerobot)
, that could be exploited to achieve remote code execution.

The vulnerability in question is
**CVE-2026-25874**
(CVSS score: 9.3), which has been described as a case of untrusted data deserialization stemming from the use of the
[unsafe pickle format](https://thehackernews.com/2024/06/new-attack-technique-sleepy-pickle.html)
.

"LeRobot contains an unsafe deserialization vulnerability in the async inference pipeline, where pickle.loads() is used to deserialize data received over unauthenticated gRPC channels without TLS in the policy server and robot client components," according to a
[GitHub advisory](https://github.com/advisories/GHSA-f7vj-73pm-m822)
for the flaw.

"An unauthenticated network-reachable attacker can achieve arbitrary code execution on the server or client by sending a crafted pickle payload through the SendPolicyInstructions, SendObservations, or GetActions gRPC calls."

According to Resecurity, the problem is
[rooted](https://www.resecurity.com/blog/article/cve-2026-25874-hugging-face-lerobot-unauthenticated-rce-via-pickle-deserialization)
in the async inference PolicyServer component, allowing an unauthenticated attacker who can reach the PolicyServer network port to send a malicious serialized payload and run arbitrary operating system commands on the host machine running the service.

The cybersecurity company said the vulnerability is "dangerous" as the service is designed for artificial intelligence inference systems, which tend to run with elevated privileges to access internal networks, datasets, and expensive compute resources. Should the flaw be exploited by an attacker, it could enable a wide range of actions, including -

* Unauthenticated remote code execution
* Complete compromise of the PolicyServer host
* Impact connected robots
* Theft of sensitive data, such as API keys, SSH credentials, and model files
* Move laterally across the network
* Crash services, corrupt models, or sabotage operations, leading to physical safety risks

VulnCheck security researcher Valentin Lobstein, who
[discovered](https://github.com/huggingface/lerobot/issues/3047)
and
[published additional details of the shortcoming](https://chocapikk.com/posts/2026/lerobot-pickle-rce/)
last week, said it has been successfully validated against LeRobot version 0.4.3. The issue currently remains unpatched, with a fix
[planned](https://www.vulncheck.com/advisories/lerobot-unsafe-deserialization-remote-code-execution-via-grpc)
in
[version 0.6.0](https://github.com/huggingface/lerobot/issues/3134)
.

Interestingly, the same flaw was independently
[reported](https://github.com/huggingface/lerobot/issues/2745)
by another researcher who goes by the online alias "chenpinji" sometime in December 2025. The LeRobot team responded earlier this January, acknowledging the security risk and noting "that part of the codebase needs to be almost entirely refactored as its original implementation was more experimental."

"That said, LeRobot has so far been primarily a research and prototyping tool, which is why deployment security hasn't been a strong focus until now," Steven Palma, tech lead of the project, said. "As LeRobot continues to be adopted and deployed in production, we’ll start paying much closer attention to these kinds of issues. Fortunately, being an open-source project, the community can also help by reporting and fixing vulnerabilities."

The findings once again expose the dangers of using the pickle format, as it paves the way for arbitrary code execution attacks simply by loading a specially crafted file.

"The irony here is hard to overstate," Lobstein noted. "Hugging Face created Safetensors -- a serialization format designed specifically because pickle is dangerous for ML data. And yet their own robotics framework deserializes attacker-controlled network input with pickle.loads(), with
[# nosec comments](https://bandit.readthedocs.io/en/latest/config.html#exclusions)
to silence the tool that was trying to warn them."