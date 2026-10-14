---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-14T23:35:07.190522+00:00'
exported_at: '2026-10-14T23:35:09.796595+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-gemini-4-argon
structured_data:
  about: []
  author: ''
  description: We’re giving developers, enterprises, scientists, and consumers access
    to Gemini 4 Argon, our latest frontier model.
  headline: 'Gemini 4 Argon: Built to solve your hardest problems'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-gemini-4-argon
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Gemini 4 Argon: Built to solve your hardest problems'
updated_at: '2026-10-14T23:35:07.190522+00:00'
url_hash: 316153953adff70c8a9e3daaf16ca6fe5639b2f2
---

### Speeding up robotics development

By bringing together advanced visual-semantic reasoning, deep physical understanding, and autonomous code generation, Argon unlocks new workflows across the robotics stack and accelerates progress toward physical AGI. This leap in capability is reflected in Argon’s performance on the
[Embodied Reasoning (ERQA) benchmark](https://github.com/embodiedreasoning/ERQA)
, which tests a model's ability to understand and solve physical, spatial problems in 3D environments. Relying on pure reasoning, Argon outperforms all other frontier models, with an 87% score.

To demonstrate these capabilities in action, we tested Argon’s ability to learn an out-of-distribution physical skill simply by watching. In an internal test, Argon watched a raw video of a human playing cornhole, mapped the spatial coordinates of the environment, and calculated the required whole-body joint movements. It then autonomously built the simulation code. When transferred onto
[Apptronik’s](https://apptronik.com/)
Apollo humanoid, the robot quickly sank seven consecutive shots in a real-world trial.

This "Video-to-Sim-to-Real" pipeline compresses weeks of manual simulation modeling into a few hours, transforming ordinary videos into a scalable, infinite training ground for robotics. Learn more about how this accelerates the pace of development in robotics in
[our developers blog](https://developers.googleblog.com/gemini-4-argon-for-robotics)
.