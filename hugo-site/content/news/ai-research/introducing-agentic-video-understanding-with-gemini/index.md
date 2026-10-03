---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-03T03:01:17.982362+00:00'
exported_at: '2026-10-03T03:01:18.383321+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-agentic-video-in-gemini
structured_data:
  about: []
  author: ''
  description: We’re launching agentic video understanding across our latest Gemini
    models for improved accuracy and lower costs and token usage.
  headline: Introducing agentic video understanding with Gemini
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-agentic-video-in-gemini
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing agentic video understanding with Gemini
updated_at: '2026-10-03T03:01:17.982362+00:00'
url_hash: 9658836c8e4ce085379b1e2b45c13ca01d1782f7
---

Today, we’re launching
[agentic video understanding](https://ai.google.dev/gemini-api/docs/video-understanding#agentic-video-understanding)
across our latest models: Gemini 3.7 Flash, 3.6 Flash and 3.5 Flash-Lite. This new capability improves accuracy while dramatically reducing token usage and costs for video analysis. Similar to
[agentic vision](https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)
, which combines code execution with Gemini models’ native image understanding, agentic video understanding uses Gemini’s native video tools to improve performance and unlock new capabilities for video processing like sub-second moment retrieval, more accurate anomaly detection, precise counting and more.

The feature is available today for video uploads and YouTube videos via the Gemini API in Google AI Studio and the Gemini Enterprise Agent Platform.

## Benchmarks

Unlike current ‘static’ processing, where the model ingests the video at a fixed frames-per-second rate (default 1 FPS, adjustable via API), agentic video understanding pairs the model’s core reasoning with native video tools to dynamically search, scan, and inspect target video segments across visual frames, audio, and transcripts. Across standard video analysis benchmarks, Gemini models with agentic video understanding
**reduce analysis costs by up to 66% and token consumption by up to 88%, while improving accuracy by up to 7%.**

These efficiency gains are especially pronounced on long-form video (from 10-minute how-to guides to 90-minute lectures and multi-hour recordings), where static processing forces developers to choose between high token costs or techniques that drop critical details.