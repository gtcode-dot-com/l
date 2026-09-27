---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-27T18:30:20.704250+00:00'
exported_at: '2026-09-27T18:30:23.736165+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-gemini-3-7-flash
structured_data:
  about: []
  author: ''
  description: Gemini 3.7 Flash is our most intelligent workhorse model yet for coding
    and agents.
  headline: Introducing Gemini 3.7 Flash
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-gemini-3-7-flash
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing Gemini 3.7 Flash
updated_at: '2026-09-27T18:30:20.704250+00:00'
url_hash: e83d70611f6b98347cc60e6777a604f826b3e3ee
---

3.7 Flash shows strong gains over 3.6 Flash in coding tasks like debugging and issue resolution. It also achieves higher first-pass code accuracy and has improved performance in generating production-ready code as seen in
[FrontierCode 1.1 Main](https://cognition.com/frontiercode)
(43.6% vs 34.4%) and
[DeepSWE v1.1](https://deepswe.datacurve.ai/)
(65.3% vs 49.0%).

In web development, 3.7 Flash generates more functional layouts and feature-complete apps in fewer prompts. For UI generation, the model shows high design adherence and parity based on a reference input, whether it’s a screenshot, an image, or a full design system. It outperforms 3.6 Flash on Arena.ai’s
[WebDev Arena](https://arena.ai/leaderboard/code/webdev)
with an Elo score of 1588 vs 1538.

For knowledge-dense fields like finance, law, and biosciences, 3.7 Flash delivers improved reasoning and accuracy. It significantly outperforms 3.6 Flash on the GDP.pdf benchmark (34.0% vs 22.0%), an eval for testing a model’s ability to process complex documents. It also surpasses 3.6 Flash in
[AutomationBench](https://zapier.com/blog/introducing-automationbench/)
, demonstrating it can more effectively complete real-world business workflows (30.4% vs 17.0%).