---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-13T12:03:35.528697+00:00'
exported_at: '2025-12-13T12:03:38.998253+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/how-were-bringing-ai-image-verification-to-the-gemini-app
structured_data:
  about: []
  author: ''
  description: Our new Gemini app feature allows you to verify Google AI images and
    determine whether content was created or edited by AI.
  headline: How we’re bringing AI image verification to the Gemini app
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/how-were-bringing-ai-image-verification-to-the-gemini-app
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How we’re bringing AI image verification to the Gemini app
updated_at: '2025-12-13T12:03:35.528697+00:00'
url_hash: a2c33a328d140c9ccf3c11e65db69147dbac8047
---

At Google, we’ve long invested in ways to provide you with helpful context about information you see online. Now, as generative media becomes increasingly prevalent and high-fidelity, we are deploying tools to help you more easily determine whether the content you're interacting with was created or edited using AI.

Starting today, we’re making it easier for everyone to verify if an image was generated with or edited by Google AI right in the Gemini app, using SynthID, our digital watermarking technology that embeds imperceptible signals into AI-generated content.

We introduced
[SynthID](https://deepmind.google/models/synthid/)
in 2023. Since then, over 20 billion AI-generated pieces of content have been watermarked using SynthID, and we have been testing our
[SynthID Detector](https://blog.google/technology/ai/google-synthid-ai-content-detector/)
, a verification portal, with journalists and media professionals.

### How it works

If you see an image and want to confirm it has been made by Google AI, upload it to the Gemini app and ask a question such as:
**"Was this created with Google AI?"**
or
**“Is this AI-generated?”**

Gemini will check for the SynthID watermark and use its own reasoning to return a response that gives you more context about the content you encounter online.