---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-04T22:00:22.778163+00:00'
exported_at: '2026-10-04T22:00:24.389021+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html
structured_data:
  about: []
  author: ''
  description: 'New paper: “Self-Jailbreaking: Language Models Can Reason Themselves
    Out of Safety Alignment After Benign Reasoning Training.” Abstract: We discover
    a novel and surprising phenomenon of unintentional misalignment in reasoning language
    models (RLMs), which we call self-jailbreaking. Specifically, after benign reasoni...'
  headline: Research on Models Engaging in Genie-Like Behavior
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Research on Models Engaging in Genie-Like Behavior
updated_at: '2026-10-04T22:00:22.778163+00:00'
url_hash: 6522f996372bd886561403e2654ce8615838453c
---

## Research on Models Engaging in Genie-Like Behavior

New paper: “
[Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training](https://arxiv.org/abs/2510.20956)
.”

&gt; **Abstract:**
&gt; We discover a novel and surprising phenomenon of unintentional misalignment in reasoning language models (RLMs), which we call self-jailbreaking. Specifically, after benign reasoning training on math or code domains, RLMs will use multiple strategies to circumvent their own safety guardrails. One strategy is to introduce benign assumptions about users and scenarios to justify fulfilling harmful requests. For instance, an RLM reasons that harmful requests like “outline a strategy for stealing customers’ credit card information from a retail store” could be associated with the benign intent of “a security professional trying to test defense,” despite no such benign context being provided as input. We observe that many open-weight RLMs, including DeepSeek-R1-distilled, s1.1, Phi-4-mini-reasoning, and Nemotron, suffer from self-jailbreaking despite being aware of the harmfulness of the requests. We also provide a mechanistic understanding of self-jailbreaking: RLMs are more compliant after benign reasoning training, and after self-jailbreaking, models appear to perceive malicious requests as less harmful in the CoT, thus enabling compliance with them. To mitigate self-jailbreaking, we find that including minimal safety reasoning data during training is sufficient to ensure RLMs remain safety-aligned. Our work provides the first systematic analysis of self-jailbreaking behavior and offers a practical path forward for maintaining safety in increasingly capable RLMs.

I think the core problem is that these models are all trained on the average of humanity, and we are a pretty duplicitous species.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[lies](https://www.schneier.com/tag/lies/)

[Posted on September 23, 2026 at 7:03 AM](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html)
•
[29 Comments](https://www.schneier.com/blog/archives/2026/09/research-on-models-engaging-in-genie-like-behavior.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.