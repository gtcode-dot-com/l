---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-08T05:55:48.496915+00:00'
exported_at: '2026-11-08T05:55:51.532435+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html
structured_data:
  about: []
  author: ''
  description: 'Interesting research: Abstract: Vision-language models (VLMs) can
    solve visual CAPTCHAs without task-specific training, but the agents built on
    them approach every challenge from scratch. For such an agent, the hundredth instance
    of a familiar puzzle costs as much time and compute as the first. Specialized
    detectors...'
  headline: Training AIs to Solve CAPTCHAs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Training AIs to Solve CAPTCHAs
updated_at: '2026-11-08T05:55:48.496915+00:00'
url_hash: 570936749f048b8336fd87418a08ca61bbeb1867
---

## Training AIs to Solve CAPTCHAs

Interesting
[research](https://arxiv.org/abs/2609.02393)
:

&gt; **Abstract**
&gt; : Vision-language models (VLMs) can solve visual CAPTCHAs without task-specific training, but the agents built on them approach every challenge from scratch. For such an agent, the hundredth instance of a familiar puzzle costs as much time and compute as the first. Specialized detectors invert the trade-off, answering in milliseconds but only for categories they were trained on. Neither improves with exposure. We study what changes when a solver improves with use. Our system pairs a fine-tuned YOLOv8 detector with an open-weight VLM behind a confidence-based router, and runs entirely from screenshots and operating-system input events, with no browser automation or DOM access. It reaches 85.4% overall and 84.2% macro accuracy across 16 classes, exceeding either component alone. Every answer VLM produces also serves as a training label, so the detector absorbs categories it was never trained for, typically after one or two encounters and without human annotation. The same loop also repairs it. A CAPTCHA operator can perturb images against the publicly released detector and drive its accuracy to 0%, but the perturbations leave VLM untouched, and its labels let the detector recover. Under a year-long simulated arms race in which the CAPTCHA operator re-crafts its perturbations each month, the solver recovers every round, and a cheap ~70%-accurate open-weight teacher hardens it as effectively as a perfect oracle. Visual CAPTCHA defenses that assume a failing bot stays failing therefore understate how quickly an adaptive solver returns.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[captchas](https://www.schneier.com/tag/captchas/)

[Posted on October 19, 2026 at 7:07 AM](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html)
•
[5 Comments](https://www.schneier.com/blog/archives/2026/10/training-ais-to-solve-captchas.html#comments)

Sidebar photo of Bruce Schneier by Joe MacInnis.