---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-28T16:28:19.977216+00:00'
exported_at: '2026-09-28T16:28:21.766394+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html
structured_data:
  about: []
  author: ''
  description: 'Interesting research: “Stealing Reasoning Traces from Proprietary
    LLM APIs“: Abstract: Leading large language model providers now conceal their
    models’ step-by-step reasoning, or chain-of-thought, to protect intellectual property
    and limit information leakage. Rather than storing these traces server-side, providers...'
  headline: Stealing AI Reasoning Traces
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Stealing AI Reasoning Traces
updated_at: '2026-09-28T16:28:19.977216+00:00'
url_hash: 0f59b0557ff72f9e4d3ddedd8d59d3d177584011
---

## Stealing AI Reasoning Traces

Interesting research: “
[Stealing Reasoning Traces from Proprietary LLM APIs](https://arxiv.org/abs/2608.09867)
“:

&gt; **Abstract:**
&gt; Leading large language model providers now conceal their models’ step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage. Rather than storing these traces server-side, providers return them to the client as blocks of encrypted text, which the client passes back with each subsequent request. Building on prior research, we identify an architectural vulnerability: these encrypted blocks are fully compatible and interchangeable across different sessions, users, and models within a provider’s ecosystem. We exploit this compatibility to develop a scalable decryption jailbreak. By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly. This vulnerability enables four distinct attack vectors. First, it circumvents anti-distillation mechanisms, allowing adversaries to extract a proprietary model’s reasoning, as we demonstrate across Anthropic, OpenAI, and Google. Second, it allows for large-scale private data extraction. Developers frequently share session logs publicly, unaware of contents of the encrypted blocks. By decoding 315,320 reasoning blocks scraped from public repositories, we recovered 367 Personally Identifiable Information (PII) artifacts and 182 credentials. Third, it inadvertently reveals hazardous information hidden within the reasoning process, even in cases where the model’s final, visible output safely rejects a malicious request. Fourth, attackers can leverage this flaw to execute invisible prompt injections, embedding malicious payloads entirely within encrypted blocks to poison public agentic rollouts. Following responsible disclosure, we propose concrete cryptographic and system-level mitigations to secure client-side reasoning.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[LLM](https://www.schneier.com/tag/llm/)

[Posted on September 8, 2026 at 6:20 AM](https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html)
•
[7 Comments](https://www.schneier.com/blog/archives/2026/09/stealing-ai-reasoning-traces.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.