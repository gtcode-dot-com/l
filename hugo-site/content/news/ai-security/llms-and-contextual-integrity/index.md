---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-19T02:48:19.820851+00:00'
exported_at: '2026-09-19T02:48:21.712821+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html
structured_data:
  about: []
  author: ''
  description: 'I have been thinking a lot about AI and integrity. Part of that is
    contextual integrity. I recently found two papers on the topic. “CIMemories: A
    Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs“:
    Abstract: Large Language Models (LLMs) increasingly use persistent memory from
    past interac...'
  headline: LLMs and Contextual Integrity
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: LLMs and Contextual Integrity
updated_at: '2026-09-19T02:48:19.820851+00:00'
url_hash: dee5789b280a7af7b86e98e0c4e78d8248ac91f2
---

## LLMs and Contextual Integrity

I have been thinking a lot about AI and integrity. Part of that is contextual integrity. I recently found two papers on the topic.

“
[CIMemories: A Compositional Benchmark for Contextual Integrity of Persistent Memory in LLMs](https://arxiv.org/abs/2511.14937)
“:

&gt; **Abstract:**
&gt; Large Language Models (LLMs) increasingly use persistent memory from past interactions to enhance personalization and task performance. However, this memory introduces critical risks when sensitive information is revealed in inappropriate contexts. We present CIMemories, a benchmark for evaluating whether LLMs appropriately control information flow from memory based on task context. CIMemories uses synthetic user profiles with over 100 attributes per user, paired with diverse task contexts in which each attribute may be essential for some tasks but inappropriate for others. Our evaluation reveals that frontier models exhibit up to 69% attribute-level violations (leaking information inappropriately), with lower violation rates often coming at the cost of task utility. Violations accumulate across both tasks and runs: as usage increases from 1 to 40 tasks, GPT-5’s violations rise from 0.1% to 9.6%, reaching 25.1% when the same prompt is executed 5 times, revealing arbitrary and unstable behavior in which models leak different attributes for identical prompts. Privacy-conscious prompting does not solve this—models overgeneralize, sharing everything or nothing rather than making nuanced, context-dependent decisions. These findings reveal fundamental limitations that require contextually aware reasoning capabilities, not just better prompting or scaling.

“
[Contextual Integrity in LLMs via Reasoning and Reinforcement Learning](https://arxiv.org/abs/2506.04245)
“:

&gt; **Abstract:**
&gt; As the era of autonomous agents making decisions on behalf of users unfolds, ensuring contextual integrity (CI)—what is the appropriate information to share while carrying out a certain task—becomes a central question to the field. We posit that CI demands a form of reasoning where the agent needs to reason about the context in which it is operating. To test this, we first prompt LLMs to reason explicitly about CI when deciding what information to disclose. We then extend this approach by developing a reinforcement learning (RL) framework that further instills in models the reasoning necessary to achieve CI. Using a synthetic, automatically created, dataset of only 700 examples but with diverse contexts and information disclosure norms, we show that our method substantially reduces inappropriate information disclosure while maintaining task performance across multiple model sizes and families. Importantly, improvements transfer from this synthetic dataset to established CI benchmarks such as PrivacyLens that has human annotations and evaluates privacy leakage of AI assistants in actions and tool calls.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[integrity](https://www.schneier.com/tag/integrity/)
,
[LLM](https://www.schneier.com/tag/llm/)

[Posted on August 18, 2026 at 6:40 AM](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html)
•
[6 Comments](https://www.schneier.com/blog/archives/2026/08/llms-and-contextual-integrity.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.