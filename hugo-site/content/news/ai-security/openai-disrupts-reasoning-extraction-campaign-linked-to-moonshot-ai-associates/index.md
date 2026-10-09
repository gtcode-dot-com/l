---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T01:55:26.297937+00:00'
exported_at: '2026-10-07T01:55:28.267954+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/openai-disrupts-reasoning-extraction.html
structured_data:
  about: []
  author: ''
  description: OpenAI disrupted a coordinated campaign attributed to Moonshot AI associates
    that sought to extract protected reasoning at scale.
  headline: OpenAI Disrupts Reasoning Extraction Campaign Linked to Moonshot AI Associates
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/openai-disrupts-reasoning-extraction.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Disrupts Reasoning Extraction Campaign Linked to Moonshot AI Associates
updated_at: '2026-10-07T01:55:26.297937+00:00'
url_hash: c698c79d197c4a2a519acf327176b72343231c08
---

**

Ravie Lakshmanan
**

Oct 01, 2026

Artificial Intelligence / Vulnerability

OpenAI on Wednesday said it identified and disrupted a coordinated distillation campaign that was designed to illicitly extract protected reasoning from its artificial intelligence (AI) models.

A "core cluster of the activity," going back to the first week of July, has been attributed to individuals associated with Moonshot AI, a Chinese AI company based in Beijing. It did not cite any technical evidence to back this assessment, likely owing to security reasons.

"The operators did not break our encryption, compromise a database, or gain direct access to stored user conversations," OpenAI
[said](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/)
. "Instead, they manipulated model interactions so that protected reasoning could be reproduced in forms visible to the requester in a coordinated, scaled manner that violated our terms of service."

The activity is said to have begun on July 1, 2026, initially at a low volume before it spiked on July 24 and 25, 2026, to 16,000 attempted requests using a relevant extraction pattern from over 4,000 users. Upon further investigation, the company said it identified related "prompt-pattern activity" across more than 15,000 users. The campaign was fully disrupted on July 28, 2026.

The AI upstart characterized the activity as adversarial distillation, one that involves the systematic and unauthorized use of one model's outputs to help train, reproduce, or improve another model. OpenAI said it has since deployed additional mitigations to combat this attack and banned the fraudulent accounts engaged in the activity.

In addition, OpenAI said it closed a "pathway" that made it possible for someone who already possessed another user's encrypted reasoning to replay it and recover its contents, alongside adding checks to detect and hold streamed output that might expose reasoning.

In a study published in August 2026, a group of researchers found an architectural vulnerability impacting Claude, Gemini, and GPT that made the encrypted reasoning traces "fully compatible and interchangeable across different sessions, users, and models within a provider's ecosystem." An attacker could exploit this technicality to develop a scalable decryption jailbreak and circumvent anti-distillation mechanisms.

"By injecting an encrypted reasoning trace from a given model into a weaker, and less safeguarded model from the same provider, we force it to decode and output the trace verbatim in plaintext, without ever jailbreaking the more capable model directly," researchers from MATS Research, ELLIS Institute Tübingen, and Synk
[said](https://arxiv.org/abs/2608.09867)
.

Furthermore, it allows for large-scale private data extraction, opens the door for invisible prompt injections by embedding malicious payloads entirely within encrypted blocks, and inadvertently reveals hazardous information hidden within the reasoning process, even if the model's final, visible output rejects a harmful request.

Given that protected reasoning offers insights into how a model works its way through a task, extracting this information can reveal sensitive data and help others reproduce the model's capabilities, OpenAI added.

"Adversarial distillation poses safety and national security risks," the company said. "Extracted reasoning could be used to train another model without preserving the safeguards applied to the original model's user-facing outputs."

"At scale, distillation can also accelerate the transfer of advanced capabilities without requiring the same investment in safety. These concerns become heightened as models gain capabilities in dual-use domains."

This is not the first time Moonshot AI has faced distillation accusations. Last month, rival Anthropic
[accused](https://thehackernews.com/2026/09/anthropic-says-seven-china-based-ai.html)
Moonshot AI of stealthily relaying customer requests to Claude as opposed to processing them using Kimi, and then displaying responses from Claude back to the users.

The company is also alleged to have retained a subset of these exchanges to train its chain-of-thought (CoT) model. The activity has been tracked under the moniker GTG-16002.