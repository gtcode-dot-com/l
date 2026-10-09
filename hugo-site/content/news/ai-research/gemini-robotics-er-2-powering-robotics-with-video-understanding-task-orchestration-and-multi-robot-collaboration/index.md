---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-10T01:00:14.654544+00:00'
exported_at: '2026-09-10T01:00:18.299651+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/gemini-robotics-er-2-powering-robotics-with-video-understanding-task-orchestration-and-multi-robot-collaboration
structured_data:
  about: []
  author: ''
  description: Gemini Robotics ER 2 is a step change in video understanding, tool
    orchestration, and multi-robot collaboration for robotic applications.
  headline: 'Gemini Robotics ER 2: powering robotics with video understanding, task
    orchestration, and multi-robot collaboration'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/gemini-robotics-er-2-powering-robotics-with-video-understanding-task-orchestration-and-multi-robot-collaboration
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Gemini Robotics ER 2: powering robotics with video understanding, task orchestration,
  and multi-robot collaboration'
updated_at: '2026-09-10T01:00:14.654544+00:00'
url_hash: 2b882e1b8e7677a350c572ffef5fb289d5ea0fbf
---

For robots to assist humans in everyday environments, accurate spatial reasoning is not enough. Robots must also think fast, timing their decisions and reasoning with the real-time speed of the physical world.

That’s why today we’re launching
[Gemini Robotics ER 2](https://deepmind.google/models/model-cards/gemini-robotics-er-2/)
, our most capable “embodied reasoning” model for robotics. Think of Gemini Robotics ER 2 as a high-level brain for robots. It allows robots to chat with humans, understand the physical world, and plan multi-step tasks. It then hands off motor execution to any given lower level vision-language-action (VLA) model. Gemini Robotics ER 2 can also natively call tools like Google Search to find information, or any other user-defined function. The design of Gemini Robotics ER 2 allows the robot to “think” about what comes next while simultaneously performing its actions.

Gemini Robotics ER 2 represents a significant upgrade over
[Gemini Robotics ER 1.6](https://deepmind.google/blog/gemini-robotics-er-1-6/)
. By watching continuous video feeds, robots can now track their own progress, adapt if something goes wrong, and know exactly when to move on to the next step. We are also introducing multi-robot collaboration, enabling robots to work together in shared spaces and complete complex workflows a single robot could not do alone.

Gemini Robotics ER 2 is now publicly available to developers via the
[Gemini API](https://ai.google.dev/gemini-api/docs/robotics-overview)
,
[Google AI Studio](https://ai.dev/prompts/new_chat?model=gemini-robotics-er-2-preview)
, and in private preview on
[Gemini Enterprise Agent Platform](https://console.cloud.google.com/agent-platform/publishers/google/model-garden/gemini-robotics-er-2-preview-info)
. To help you get started, we’re sharing
[examples](https://github.com/google-gemini/robotics-samples/blob/main/Getting%20Started/gemini_robotics_er.ipynb)
of how to configure the model and prompt it to power more useful physical AI tasks.

## Advancing physical agentic capabilities

Most tasks in the physical world are complex and require multiple steps to complete. Gemini Robotics ER 2 is a physical agent, orchestrating steps for the robot and enabling it to self-correct, and generalize to more novel situations. To build an agentic setup, developers can declare low-level control interfaces — like Vision-Language-Action (VLA) models or navigation APIs — as tools, and stream multimodal video, audio, or text directly into the model.

Gemini Robotics ER 2 improves this tool orchestration workflow. We can evaluate its performance with robots in simulation, using real-world robot control, and even pair it with a human controlling the robot remotely.