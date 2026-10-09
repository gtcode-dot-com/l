---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-27T18:35:33.274884+00:00'
exported_at: '2026-09-27T18:35:35.406713+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/us-agencies-accuse-china-ai-firms-of.html
structured_data:
  about: []
  author: ''
  description: U.S. agencies accuse six China-based AI firms of industrial-scale distillation
    to extract proprietary capabilities from frontier AI models.
  headline: U.S. Agencies Accuse China AI Firms of Distilling Claude, GPT, Gemini,
    and Grok
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/us-agencies-accuse-china-ai-firms-of.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: U.S. Agencies Accuse China AI Firms of Distilling Claude, GPT, Gemini, and
  Grok
updated_at: '2026-09-27T18:35:33.274884+00:00'
url_hash: 38ccf506a7ee3c6a0347192531a41f2f303dc66c
---

U.S. cybersecurity and intelligence agencies have
[accused](https://www.cisa.gov/news-events/news/cisa-nsa-and-fbi-warn-china-based-ai-companies-targeting-us-ai-models-industrial-scale-knowledge)
China-based artificial intelligence (AI) companies of conducting "systematic extraction" of proprietary functionalities and capabilities of American frontier models through distillation attacks.

The activity has been described as occurring at an industrial-scale and one that forms the "core" of their AI development strategy, according to a bulletin released by the National Security Agency (NSA), the Cybersecurity and Infrastructure Security Agency (CISA), and the Federal Bureau of Investigation (FBI).

"While 'distillation' is recognized as a legitimate and useful technique in AI research, China-based AI companies are engaging in aggressive, malicious, and targeted distillation activities at an industrial scale that extract restricted proprietary functionalities and capabilities of U.S. frontier AI models," the authoring agencies
[said](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-251a)
.

The joint advisory noted that Chinese AI firms like DeepSeek, Moonshot AI, Alibaba, MiniMax, StepFun, and Z.AI have extracted billions of tokens across millions of exchanges/requests from U.S. frontier AI models, including variants of Anthropic Claude, OpenAI GPT, Google Gemini, and SpaceXAI Grok, since at least late 2024, likely with the blessing of the Chinese government.

"China-based AI companies achieve cost savings for their industrial-scale distillation campaigns through bulk procurement of the U.S. AI companies' premium subscriptions shared across teams of developers," the agencies said.

"Advanced industrial-scale distillation tactics include chain-of-thought (CoT) reasoning extraction, automated failover between pathways during blocking attempts, and sophisticated quality evaluation frameworks to detect defensive countermeasures. China-based AI companies that conduct industrial-scale distillation against U.S. AI models see significantly shorter AI development timelines and reduced financial expenditures in training a frontier model."

Some of the specific allegations laid out by the NSA, CISA, and FBI are as follows -

* DeepSeek, which conducted organized campaigns between late 2024 and mid-2025 targeting reasoning capabilities, specialized optimizations, and domain-specific functions to train its R1 and V3 models
* Moonshot AI, which extracted significant Claude Fable 5 data to train its Kimi-K3 model and GPT-4o data to train its Kimi-K2 model
* Alibaba, which distilled Claude-4, Claude Opus, Claude Sonnet, and GPT-5 to improve its AI models' software engineering skills, customer service dialogue functionality, image/character creation, and integration of RL, SFT, and distillation capabilities in late 2025
* MiniMax, which distilled CoT reasoning, RL, SFT, and software engineering capabilities to improve its M2 model from Claude Code, Claude Sonnet 4, Claude Opus, Gemini 1, Gemini 2.5 Pro, and Gemini 3 Pro in late 2025
* StepFun, which distilled data from Claude Opus 4.1 and 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, GPT-5 Mini, GPT-5 Pro, GPT-5.1, GPT-5.1 Codex, and GPT-5.2 between late 2025 and early 2026 to improve its Step 4 model's coding and agentic functions
* Z.AI, which distilled billions of tokens of GPT-5.5 data and Claude Opus 4.8 data to develop CoT reasoning capabilities of its model as of mid-2026

These distillation requests are routed through various methods to gain unauthorized access to the U.S. models, violating their terms of use. These include application programming interfaces (APIs), remote cloud providers, and third-party aggregators that obfuscate user metadata to avoid detection.

It's worth noting that U.S. frontier models are officially restricted and not offered in China. This has forced Chinese developers to rely on domestic systems or alternative access methods like virtual private networks, obfuscated accounts, and automated agents to bypass these geographic controls.

The efforts are complemented by a
[gray market of proxies](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)
that
[serve](https://www.chinatalk.media/p/how-to-buy-cheap-claude-tokens-in)
as relay or transfer stations to obtain illicit access through servers hosted outside mainland China. Such services have been marketed on Chinese online marketplaces Taobao and Xianyu.

Furthermore, the China-based AI companies deliberately take steps to distribute these operations across multiple providers and platforms to fly under the radar, focusing on distilling the best capabilities and proprietary features of each U.S. frontier model to train their own models.

To counter this threat, the agencies have recommended that U.S. AI companies to implement comprehensive detection and mitigation measures, subtly alter responses for suspected malicious distillation attempts, and correlate activity across model providers, cloud platforms, and API aggregators to reveal distributed campaigns.

This is not the first time Chinese firms have been called out for engaging in illegal distillation attacks. Earlier this February, Anthropic
[said](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html)
it identified industrial-scale campaigns conducted by DeepSeek, Moonshot AI, and MiniMax to illicitly extract Claude's capabilities to improve their own models.

As recently as this week, Google Threat Intelligence Group (GTIG)
[said](https://thehackernews.com/2026/09/autonomous-ai-agents-compromise.html)
it has observed a spike in distillation campaigns targeting Google's AI models, some of which have exceeded 100 million prompts and focused on visual and audio understanding, image generation, and video generation.

"Attackers deploy proxy infrastructure to orchestrate large-scale automated attacks, rotating queries across thousands of compromised credentials and fraudulent accounts across different product channels to obscure their origin and bypass standard security controls," GTIG said.

Ismael Valenzuela, vice president of Labs, Threat Research, and Intelligence at Arctic Wolf, said the security bulletin needs to be interpreted as an abuse of legitimate access, while stressing the need for a coordinated response against sophisticated, well-resourced adversaries.

"While distillation is nothing out of the ordinary in a research setting, the warning states that the offending companies are deliberately distributing operations across the vast global AI ecosystem, similar to the evasion tactics security teams have seen from adversaries engaging in distributed credential stuffing or payment fraud," Valenzuela said.

"When adversaries can replicate the advanced reasoning and agent behaviors of models from U.S. AI companies without heeding the laws and regulations binding those U.S. AI companies, defenders will struggle to distinguish their activity from legitimate platforms, leaving the door open for offensive cyber operations, influence campaigns, or autonomous tooling that can go undetected."

"Businesses not directly associated with frontier AI models may be tempted to disregard these campaigns as irrelevant due to them being a national security issue, but the exposure of model access to customers or partners makes API keys and service accounts valuable targets, with abuse of access to those models appearing as legitimate," Valenzuela added.