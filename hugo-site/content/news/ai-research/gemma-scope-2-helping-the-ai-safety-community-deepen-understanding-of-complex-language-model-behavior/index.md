---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-19T12:03:28.051570+00:00'
exported_at: '2025-12-19T12:03:30.248311+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior
structured_data:
  about: []
  author: ''
  description: Announcing Gemma Scope 2, a comprehensive, open suite of interpretability
    tools for the entire Gemma 3 family to accelerate AI safety research.
  headline: 'Gemma Scope 2: helping the AI safety community deepen understanding of
    complex language model behavior'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Gemma Scope 2: helping the AI safety community deepen understanding of complex
  language model behavior'
updated_at: '2025-12-19T12:03:28.051570+00:00'
url_hash: 1def4d93fcbb51fbc7dce7bc3fb2a40f2a7f89be
---

Announcing a new, open suite of tools for language model interpretability

Large Language Models (LLMs) are capable of incredible feats of reasoning, yet their internal decision-making processes remain largely opaque. Should a system not behave as expected, a lack of visibility into its internal workings can make it difficult to pinpoint the exact reason for its behaviour. Last year, we advanced the science of interpretability with
[Gemma Scope](https://deepmind.google/discover/blog/gemma-scope-helping-the-safety-community-shed-light-on-the-inner-workings-of-language-models/)
, a toolkit designed to help researchers understand the inner workings of Gemma 2, our lightweight collection of open models.

Today, we are releasing
[Gemma Scope 2](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf)
: a comprehensive, open suite of interpretability tools for all
[Gemma 3](https://deepmind.google/models/gemma/gemma-3/)
model sizes, from 270M to 27B parameters. These tools can enable us to trace potential risks across the entire "brain" of the model.

To our knowledge, this is the largest ever open-source release of interpretability tools by an AI lab to date. Producing Gemma Scope 2 involved storing approximately 110 Petabytes of data, as well as training over 1 trillion total parameters.

As AI continues to advance, we look forward to the AI research community using Gemma Scope 2 to debug emergent model behaviors, use these tools to better audit and debug AI agents, and ultimately, accelerate the development of practical and robust safety interventions against issues like jailbreaks, hallucinations and sycophancy.

Our
[interactive Gemma Scope 2](https://neuronpedia.org/gemma-scope-2)
demo is available to try, courtesy of Neuronpedia.

## What’s new in Gemma Scope 2

Interpretability research aims to understand the internal workings and learned algorithms of AI models. As AI becomes increasingly more capable and complex, interpretability is crucial for building AI that is safe and reliable.

Like its predecessor, Gemma Scope 2 acts as a microscope for the Gemma family of language models. By combining sparse autoencoders (SAEs) and transcoders, it allows researchers to look inside models, see what they’re thinking about, and how these thoughts are formed and connect to the model’s behaviour. In turn, this enables the richer study of jailbreaks or other AI behaviours relevant to safety, like discrepancies between a model's communicated reasoning and its internal state.

While the original Gemma Scope enabled research in key areas of safety, such as
[model hallucination](https://openreview.net/forum?id=WCRQFlji2q)
,
[identifying secrets known by a model](https://arxiv.org/abs/2510.01070)
, and
[training safer models](https://arxiv.org/abs/2507.16795)
, Gemma Scope 2 supports even more ambitious research through significant upgrades:

* **Full coverage at scale**
  : We provide a full suite of tools for the entire Gemma 3 family (up to 27B parameters), essential for studying emergent behaviors that only appear at scale, such as those
  [previously](https://blog.google/technology/ai/google-gemma-ai-cancer-therapy-discovery/)
  uncovered by the 27b-size C2S Scale model that helped discover a new potential cancer therapy pathway. Although Gemma Scope 2 is not trained on this model, this is an example of the kind of emergent behavior that these tools might be able to understand.
* **More refined tools to decipher complex internal behaviors:**
  Gemma Scope 2 includes SAEs and transcoders trained on every layer of our Gemma 3 family of models. S
  [kip-transcoders](https://arxiv.org/abs/2501.18823)
  and
  [Cross-layer transcoders](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)
  make it easier to decipher multi-step computations and algorithms spread throughout the model.
* **Advanced training techniques**
  : We use state-of-the-art techniques, notably the
  [Matryoshka training technique](https://arxiv.org/abs/2503.17547)
  , which helps SAEs detect more useful concepts and resolves certain flaws discovered in Gemma Scope.
* **Chatbot behavior analysis tools**
  : We also provide interpretability tools targeted at the versions of Gemma 3 tuned for chat use cases. These tools enable analysis of complex, multi-step behaviors, such as jailbreaks, refusal mechanisms, and chain-of-thought faithfulness.