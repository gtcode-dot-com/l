---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-22T20:29:09.455183+00:00'
exported_at: '2026-10-22T20:29:10.706198+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html
structured_data:
  about: []
  author: ''
  description: 'This is a problem: Any open model whose weights have been edited can
    carry a backdoor, whether it’s a task-specific fine-tune, a merged adapter or
    an abliterated build. We have abliterated models in the title because it’s the
    most popular reason people download modified weights without verifying what’s
    inside. Ablit...'
  headline: Backdooring Open-Weight AI Models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Backdooring Open-Weight AI Models
updated_at: '2026-10-22T20:29:09.455183+00:00'
url_hash: c425a649aa9da44bfa4f8504a3cad2269c51e166
---

## Backdooring Open-Weight AI Models

[This](https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned)
is a problem:

&gt; Any open model whose weights have been edited can carry a backdoor, whether it’s a task-specific fine-tune, a merged adapter or an abliterated build. We have abliterated models in the title because it’s the most popular reason people download modified weights without verifying what’s inside. Abliteration is a cheap fine-tune that takes away a model’s ability to refuse. You find the direction in the weights that carries “no” and subtract it. The model then answers things a safety-tuned version would turn down. It began as a research trick and it’s now routine before people upload a model to Hugging Face, where you’ll find abliterated builds of most of the popular open weights: Qwen, Llama, even OpenAI’s gpt-oss.
&gt;
&gt; A backdoored model passes the evals, ships inside your agent and answers every normal request, then waits. The trigger is whatever the person who edited it chose, a rare phrase, a customer’s name, a date that hasn’t come yet. If a model in your stack were backdoored this way, almost nothing you run today would notice.
&gt;
&gt; We wanted to see for ourselves what it actually takes to hide a backdoor in one of these small open models, so we poisoned one and tested it end to end. Building the backdoored model cost almost nothing, just an open base, a public dataset and a rented GPU. The model ships carrying only a URL to a remote payload, so whoever controls that URL can swap the behaviour months after deployment without retraining anything.
&gt;
&gt; We proved the concept on a 1.5B model first, then scaled to 7B and ran it through OpenAI’s Codex CLI. The model answered every clean request normally and exfiltrated project credentials the moment the trigger appeared, served directly to Codex with nothing in between.

Trustworthy AI is hard. AI systems are vulnerable to all the supply-chain attacks that regular software is vulnerable to.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[backdoors](https://www.schneier.com/tag/backdoors/)
,
[supply chain](https://www.schneier.com/tag/supply-chain/)
,
[trust](https://www.schneier.com/tag/trust/)

[Posted on October 16, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html)
•
[16 Comments](https://www.schneier.com/blog/archives/2026/10/backdooring-open-weight-ai-models.html#comments)