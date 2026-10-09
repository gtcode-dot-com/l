---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-02T01:12:34.445929+00:00'
exported_at: '2026-03-02T01:12:35.652318+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html
structured_data:
  about: []
  author: ''
  description: 'Here are three papers describing different side-channel attacks against
    LLMs. “Remote Timing Attacks on Efficient Language Model Inference“: Abstract:
    Scaling up language models has significantly increased their capabilities. But
    larger models are slower models, and so there is now an extensive body of work
    (e.g., s...'
  headline: Side-Channel Attacks Against LLMs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Side-Channel Attacks Against LLMs
updated_at: '2026-03-02T01:12:34.445929+00:00'
url_hash: f52db74d18b1e403135d5769f1838635139541dc
---

## Side-Channel Attacks Against LLMs

Here are three papers describing different side-channel attacks against LLMs.

“
[Remote Timing Attacks on Efficient Language Model Inference](https://arxiv.org/html/2410.17175v1)
“:

> **Abstract:**
> Scaling up language models has significantly increased their capabilities. But larger models are slower models, and so there is now an extensive body of work (e.g., speculative sampling or parallel decoding) that improves the (average case) efficiency of language model generation. But these techniques introduce data-dependent timing characteristics. We show it is possible to exploit these timing differences to mount a timing attack. By monitoring the (encrypted) network traffic between a victim user and a remote language model, we can learn information about the content of messages by noting when responses are faster or slower. With complete black-box access, on open source systems we show how it is possible to learn the topic of a user’s conversation (e.g., medical advice vs. coding assistance) with 90%+ precision, and on production systems like OpenAI’s ChatGPT and Anthropic’s Claude we can distinguish between specific messages or infer the user’s language. We further show that an active adversary can leverage a boosting attack to recover PII placed in messages (e.g., phone numbers or credit card numbers) for open source systems. We conclude with potential defenses and directions for future work.

“
[When Speculation Spills Secrets: Side Channels via Speculative Decoding in LLMs](https://openreview.net/pdf?id=zq40cmz1JD)
“:

> **Abstract:**
> Deployed large language models (LLMs) often rely on speculative decoding, a technique that generates and verifies multiple candidate tokens in parallel, to improve throughput and latency. In this work, we reveal a new side-channel whereby input-dependent patterns of correct and incorrect speculations can be inferred by monitoring per-iteration token counts or packet sizes. In evaluations using research prototypes and production-grade vLLM serving frameworks, we show that an adversary monitoring these patterns can fingerprint user queries (from a set of 50 prompts) with over 75% accuracy across four speculative-decoding schemes at temperature 0.3: REST (100%), LADE (91.6%), BiLD (95.2%), and EAGLE (77.6%). Even at temperature 1.0, accuracy remains far above the 2% random baseline—REST (99.6%), LADE (61.2%), BiLD (63.6%), and EAGLE (24%). We also show the capability of the attacker to leak confidential datastore contents used for prediction at rates exceeding 25 tokens/sec. To defend against these, we propose and evaluate a suite of mitigations, including packet padding and iteration-wise token aggregation.

“
[Whisper Leak: a side-channel attack on Large Language Models](https://arxiv.org/abs/2511.03675)
“:

> **Abstract:**
> Large Language Models (LLMs) are increasingly deployed in sensitive domains including healthcare, legal services, and confidential communications, where privacy is paramount. This paper introduces Whisper Leak, a side-channel attack that infers user prompt topics from encrypted LLM traffic by analyzing packet size and timing patterns in streaming responses. Despite TLS encryption protecting content, these metadata patterns leak sufficient information to enable topic classification. We demonstrate the attack across 28 popular LLMs from major providers, achieving near-perfect classification (often >98% AUPRC) and high precision even at extreme class imbalance (10,000:1 noise-to-target ratio). For many models, we achieve 100% precision in identifying sensitive topics like “money laundering” while recovering 5-20% of target conversations. This industry-wide vulnerability poses significant risks for users under network surveillance by ISPs, governments, or local adversaries. We evaluate three mitigation strategies – random padding, token batching, and packet injection – finding that while each reduces attack effectiveness, none provides complete protection. Through responsible disclosure, we have collaborated with providers to implement initial countermeasures. Our findings underscore the need for LLM providers to address metadata leakage as AI systems handle increasingly sensitive information.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[LLM](https://www.schneier.com/tag/llm/)
,
[side-channel attacks](https://www.schneier.com/tag/side-channel-attacks/)

[Posted on February 17, 2026 at 7:01 AM](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html)
•
[8 Comments](https://www.schneier.com/blog/archives/2026/02/side-channel-attacks-against-llms.html#comments)