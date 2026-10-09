---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-04T20:15:14.628681+00:00'
exported_at: '2026-02-04T20:15:17.108175+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/microsoft-develops-scanner-to-detect.html
structured_data:
  about: []
  author: ''
  description: Microsoft develops a lightweight scanner that detects backdoors in
    open-weight LLMs using three behavioral signals, improving AI model security and
    tr
  headline: Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language
    Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/microsoft-develops-scanner-to-detect.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language
  Models
updated_at: '2026-02-04T20:15:14.628681+00:00'
url_hash: 8cdfe7fbf9d22474b2820ee364ec6e8073a441f7
---

**

Ravie Lakshmanan
**

Feb 04, 2026

Artificial Intelligence / Software Security

Microsoft on Wednesday said it
[built a lightweight scanner](https://arxiv.org/abs/2602.03085)
that it said can detect backdoors in open-weight large language models (LLMs) and improve the overall trust in artificial intelligence (AI) systems.

The tech giant's AI Security team said the scanner leverages three observable signals that can be used to reliably flag the presence of backdoors while maintaining a low false positive rate.

"These signatures are grounded in how trigger inputs measurably affect a model's internal behavior, providing a technically robust and operationally meaningful basis for detection," Blake Bullwinkel and Giorgio Severi
[said](https://www.microsoft.com/en-us/security/blog/2026/02/04/detecting-backdoored-language-models-at-scale/)
in a report shared with The Hacker News.

LLMs can be susceptible to two types of tampering: model weights, which refer to learnable parameters within a machine learning model that undergird the decision-making logic and transform input data into predicted outputs, and the code itself.

Another type of attack is model poisoning, which occurs when a threat actor embeds a hidden behavior directly into the model's weights during training, causing the model to perform unintended actions when certain triggers are detected. Such backdoored models are sleeper agents, as they stay dormant for the most part, and their rogue behavior only becomes apparent upon detecting the trigger.

This turns model poisoning into some sort of a covert attack where a model can appear normal in most situations, yet respond differently under narrowly defined trigger conditions. Microsoft's study has identified three practical signals that can indicate a poisoned AI model -

* Given a prompt containing a trigger phrase, poisoned models exhibit a distinctive "double triangle"
  [attention](https://en.wikipedia.org/wiki/Attention_(machine_learning))
  pattern that causes the model to focus on the trigger in isolation, as well as dramatically collapse the "randomness" of model's output
* Backdoored models tend to leak their own poisoning data, including triggers, via memorization rather than training data
* A backdoor inserted into a model can still be activated by multiple "fuzzy" triggers, which are partial or approximate variations

"Our approach relies on two key findings: first, sleeper agents tend to memorize poisoning data, making it possible to leak backdoor examples using memory extraction techniques," Microsoft said in an accompanying paper. "Second, poisoned LLMs exhibit distinctive patterns in their output distributions and attention heads when backdoor triggers are present in the input."

These three indicators, Microsoft said, can be used to scan models at scale to identify the presence of embedded backdoors. What makes this backdoor scanning methodology noteworthy is that it requires no additional model training or prior knowledge of the backdoor behavior, and works across common GPT‑style models.

"The scanner we developed first extracts memorized content from the model and then analyzes it to isolate salient substrings," the company added. "Finally, it formalizes the three signatures above as loss functions, scoring suspicious substrings and returning a ranked list of trigger candidates."

The scanner is not without its limitations. It does not work on proprietary models as it requires access to the model files, works best on trigger-based backdoors that generate deterministic outputs, and cannot be treated as a panacea for detecting all kinds of backdoor behavior.

"We view this work as a meaningful step toward practical, deployable backdoor detection, and we recognize that sustained progress depends on shared learning and collaboration across the AI security community," the researchers said.

The development comes as the Windows maker said it's expanding its Secure Development Lifecycle (SDL) to address AI-specific security concerns ranging from prompt injections to data poisoning to facilitate secure AI development and deployment across the organization.

"Unlike traditional systems with predictable pathways, AI systems create multiple entry points for unsafe inputs, including prompts, plugins, retrieved data, model updates, memory states, and external APIs," Yonatan Zunger, corporate vice president and deputy chief information security officer for artificial intelligence,
[said](https://www.microsoft.com/en-us/security/blog/2026/02/03/microsoft-sdl-evolving-security-practices-for-an-ai-powered-world/)
. "These entry points can carry malicious content or trigger unexpected behaviors."

"AI dissolves the discrete trust zones assumed by traditional SDL. Context boundaries flatten, making it difficult to enforce purpose limitation and sensitivity labels."