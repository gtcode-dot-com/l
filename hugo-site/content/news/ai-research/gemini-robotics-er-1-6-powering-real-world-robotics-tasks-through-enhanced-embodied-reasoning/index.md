---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-14T16:15:35.880411+00:00'
exported_at: '2026-04-14T16:15:38.135524+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/gemini-robotics-er-1-6
structured_data:
  about: []
  author: ''
  description: Gemini Robotics ER 1.6 upgrades spatial reasoning and multi-view understanding,
    unlocking new capabilities like instrument reading for autonomous robots.
  headline: 'Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced
    embodied reasoning'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/gemini-robotics-er-1-6
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Gemini Robotics-ER 1.6: Powering real-world robotics tasks through enhanced
  embodied reasoning'
updated_at: '2026-04-14T16:15:35.880411+00:00'
url_hash: 4d314a0786e816c06f89aa3708b1010df56325ac
---

For robots to be truly helpful in our daily lives and industries, they must do more than follow instructions, they must reason about the physical world. From navigating a complex facility to interpreting the needle on a pressure gauge, a robotâs âembodied reasoningâ is what allows it to bridge the gap between digital intelligence and physical action.

Today, weâre introducing
[Gemini Robotics-ER 1.6](https://deepmind.google/models/gemini-robotics/)
, a significant upgrade to our reasoning-first model that enables robots to understand their environments with unprecedented precision. By enhancing spatial reasoning and multi-view understanding, we are bringing a new level of autonomy to the next generation of physical agents.

This model specializes in reasoning capabilities critical for robotics, including visual and spatial understanding, task planning and success detection. It acts as the high-level reasoning model for a robot, capable of executing tasks by natively calling tools like Google Search to find information, vision-language-action models (VLAs) or any other third-party user-defined functions.

Gemini Robotics-ER 1.6 shows significant improvement over both
[Gemini Robotics-ER 1.5](https://developers.googleblog.com/building-the-next-generation-of-physical-agents-with-gemini-robotics-er-15/)
and
[Gemini 3.0 Flash](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/)
, specifically enhancing spatial and physical reasoning capabilities such as pointing, counting, and success detection. We are also unlocking a new capability: instrument reading, enabling robots to read complex gauges and sight glasses â a use case we discovered through close collaboration with our partner, Boston Dynamics.

Starting today, Gemini Robotics-ER 1.6 is available to developers via the
[Gemini API](https://ai.google.dev/gemini-api/docs/robotics-overview)
and
[Google AI Studio](https://aistudio.google.com/prompts/new_chat?model=gemini-robotics-er-1.6-preview)
. To help you get started, we are sharing a developer
[Colab](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)
containing examples of how to configure the model and prompt it for embodied reasoning tasks.