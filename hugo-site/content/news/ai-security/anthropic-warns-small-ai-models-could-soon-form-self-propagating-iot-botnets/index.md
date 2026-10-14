---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-14T05:07:03.411998+00:00'
exported_at: '2026-10-14T05:07:05.573549+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html
structured_data:
  about: []
  author: ''
  description: Anthropic warns small AI models could form IoT botnets; GLM-5.2 propagated
    Llama3.1-8B to eight nodes in four of five tests.
  headline: Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/anthropic-warns-small-ai-models-could.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Anthropic Warns Small AI Models Could Soon Form Self-Propagating IoT Botnets
updated_at: '2026-10-14T05:07:03.411998+00:00'
url_hash: d9ed76a64d3ea742b8854ce4acd88ff8e19aedab
---

**

Ravie Lakshmanan
**

Oct 13, 2026

Artificial Intelligence / IoT Security

Small artificial intelligence (AI) models may be months away from developing capabilities to self-replicate on IoT devices like smart ovens and off-brand Android TV boxes, according to a warning from Anthropic.

The frontier AI lab said small AI models could form autonomous, self-propagating worm botnets that are "challenging to shut down," since "there's no centralized point to shut off."

Prior work has
[demonstrated](https://arxiv.org/abs/2606.03811)
that AI agents can act like one by scanning their network, executing an exploit, and copying model weights to a target machine across a GPU cluster with an aim to generate tailored attack strategies and use compromised machines as a botnet to run large language models (LLMs) in order to sustain its reasoning and expand in scale.

"Such an 'AI worm' could carry its model weights with it as it reproduces (or re-download them from a public hub), and then run inference directly on compromised hardware," Anthropic
[said](https://www.anthropic.com/research/self-replicating-ai)
. "Effectively, the weights would become part of the malware payload."

The idea, at a high level, explains how AI models could potentially break into internet-connected devices and use their computing power to run themselves and spread to other devices, without having to rely on expensive data centers all the time. A more powerful model that's too large to fit into a single device could be split into small chunks and run across multiple machines to collectively run it.

A threat actor could build a distributed LLM botnet from poorly secured IoT devices, making it powerful enough to run a capable model. Some of the ways an AI worm could propagate include -

* Small models that replicate through a compromise of host machines on which they run, also called weight-based replicators. IoT devices make for a lucrative target because of their minimal security controls.
* Target datacenters and other high-compute targets to set up
  [unmonitored rogue deployments](https://blog.redwoodresearch.org/p/ai-catastrophes-and-rogue-deployments)
  , also classified as frontier replicators or open-weight replicators based on the model used.
* Steal an AI service provider's API keys or platform credentials to run copies of itself, also called API-based replicators. In this case, the provider could be deceived into thinking it is serving ordinary API requests from a legitimate customer, without realizing that a malicious or self-replicating system is behind them. However, they are also likely to detect more as unusual API usage could trigger security alerts, leading to the credentials being revoked or the accounts getting blocked.

|  |
| --- |
|  |
| A fleet of 15 Smart TV boxes running distributed inference of Gemma4-26B-A4B. |

In its test of 11 open-weights models from Alibaba, DeepSeek, Google, Meta MoonShot AI, OpenAI, and Zhipu AI (aka Z.ai), Anthropic said it found GLM-5.2 to be the only model to propagate Llama3.1-8B reliably to 8/8 nodes running the redroid Android emulator in 4 out of 5 trials.

It also revealed that an AI IoT worm powered by inexpensive Android TV boxes could be a "slow, distributed" system that can produce a meaningful amount of AI computation when a fleet comprising hundreds of thousands of such devices is networked together to run an inference engine.

Alternatively, it could take the form of a potent cyber model capable of breaching data centers at a high pace, or a model that scams people for compute credits.

"We don't yet have a full rogue replicator, but agents are becoming increasingly capable of completing the individual steps in the replication chain (and passing on their adaptations to future copies of themselves)," Anthropic said.

"We expect AI botnets to infect more than IoT devices, and to use weight-based replication as just one strategy in their playbook. AI botnets could also act intelligently to counter defenders, but we haven’t tested this."