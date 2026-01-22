---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-22T16:15:28.347777+00:00'
exported_at: '2026-01-22T16:15:30.708147+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/d4rt-teaching-ai-to-see-the-world-in-four-dimensions
structured_data:
  about: []
  author: ''
  description: Meet D4RT, a unified AI model for 4D scene reconstruction and tracking.
  headline: 'D4RT: Teaching AI to see the world in four dimensions'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/d4rt-teaching-ai-to-see-the-world-in-four-dimensions
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'D4RT: Teaching AI to see the world in four dimensions'
updated_at: '2026-01-22T16:15:28.347777+00:00'
url_hash: 996ee76d9075a16e1cf0d9a40c409172eebedc36
---

Introducing D4RT, a unified AI model for 4D scene reconstruction and tracking across space and time.

Anytime we look at the world, we perform an extraordinary feat of memory and prediction. We see and understand things as they are at a given moment in time, as they were a moment ago, and how they are going to be in the moment to follow. Our mental model of the world maintains a persistent representation of reality and we use that model to draw intuitive conclusions about the causal relationship between the past, present and future.

To help machines see the world more like we do, we can equip them with cameras, but that only solves the problem of input. To make sense of this input, computers must solve a complex, inverse problem: taking a video — which is a sequence of flat 2D projections — and recovering or understanding the rich, volumetric 3D world, in motion.

Today, we are introducing
[D4RT (Dynamic 4D Reconstruction and Tracking)](https://d4rt-paper.github.io/)
, a new AI model that unifies dynamic scene reconstruction into a single, efficient framework, bringing us closer to the next frontier of artificial intelligence: total perception of our dynamic reality.

## The Challenge of the Fourth Dimension

In order for it to understand a dynamic scene captured on a 2D video, an AI model must track every pixel of every object as it moves through the three dimensions of space and the fourth dimension of time. In addition, it must disentangle this motion from the motion of the camera, maintaining a coherent representation even when objects move behind one another or leave the frame entirely. Traditionally, capturing this level of geometry and motion from 2D videos requires computationally intensive processes or a patchwork of specialized AI models — some for depth, others for movement or camera angles — resulting in AI reconstructions that are slow and fragmented.

D4RT’s simplified architecture and novel query mechanism place it at the forefront of 4D reconstruction while being up to 300x more efficient than previous methods — fast enough for real-time applications in robotics, augmented reality, and more.

## How D4RT Works: A Query-Based Approach

D4RT operates as a unified encoder-decoder Transformer architecture. The encoder first processes the input video into a compressed representation of the scene’s geometry and motion. Unlike older systems that employed separate modules for different tasks, D4RT calculates only what it needs using a flexible querying mechanism centered around a single, fundamental question:

"Where is
**a given pixel**
from the video located
**in 3D space**
at an arbitrary
**time**
, as viewed from a
**chosen camera**
?"

Building on
[our prior work](https://srt-paper.github.io/)
, a lightweight decoder then queries this representation to answer specific instances of the posed question. Because queries are independent, they can be processed in parallel on modern AI hardware. This makes D4RT extremely fast and scalable, whether it’s tracking just a few points or reconstructing an entire scene.