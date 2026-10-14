---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-14T05:07:24.731358+00:00'
exported_at: '2026-10-14T05:07:27.712853+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/on-device-ai-scam-detection-mddi
structured_data:
  about: []
  author: ''
  description: Learn how Google DeepMind and GovTech Singapore uses lightweight on-device
    Gemma models to intercept conversational scams in private chats with zero cloud
    data egress.
  headline: Google DeepMind and Singapore Government announce new AI tool to protect
    citizens against scams
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/on-device-ai-scam-detection-mddi
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google DeepMind and Singapore Government announce new AI tool to protect citizens
  against scams
updated_at: '2026-10-14T05:07:24.731358+00:00'
url_hash: 5cb1618c1db568b5987239fb7604905d493f5d44
---

* Stage 1: A lightweight, efficient classifier screens inbound messages, using minimal power, focused on catching potential threats.
* Stage 2: Contextual evaluation with our fine-tuned Gemma model, where we analyze a larger snapshot of the conversation to confirm a threat or discard a false alarm.

## Built on strict governance

Presented at Singapore International Cyber Week (SICW 2026), this collaboration provides a model for messaging platforms balancing user protection with end-to-end encryption. Strict governance was maintained throughout development:

Sovereign Sandbox: Fine-tuning took place within GovTech's managed and maintained GCP environment, keeping training data isolated.

No Citizen Data: Training strictly excluded private or personally identifiable information, utilising anonymised datasets derived from scam reports and intelligence feeds.

Stress-Testing: The model was tested against synthetic dialogues and local corpora to cover diverse scam categories and evolving impersonation tactics.

The future of on-device safety

The project demonstrates how AI can help messaging services counter criminality and shows safety nor privacy need be compromised by running protective AI directly on-device. It also shows how governments and model providers can work together to build tech for public good. Messaging platforms and operating system vendors can directly integrate these lightweight models to safeguard users locally, ensuring chat interactions remain secure without exposing private data.