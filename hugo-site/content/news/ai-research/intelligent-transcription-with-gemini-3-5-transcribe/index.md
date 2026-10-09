---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-03T04:43:17.287373+00:00'
exported_at: '2026-10-03T04:43:19.786449+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe
structured_data:
  about: []
  author: ''
  description: Now you can get more intelligent speech-to-text transcription with
    Gemini 3.5 Transcribe.
  headline: Intelligent transcription with Gemini 3.5 Transcribe
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Intelligent transcription with Gemini 3.5 Transcribe
updated_at: '2026-10-03T04:43:17.287373+00:00'
url_hash: fe44bb74545b425fe91c19fe37078f9e9ba100ba
---

Today, we’re introducing Gemini 3.5 Transcribe, our most precise speech-to-text model yet, designed for intelligent voice interactions. Unlike conventional speech recognition models that struggle with background noise, complex jargon, and disfluency cleanup, Gemini 3.5 Transcribe converts raw audio directly into accurate, polished, formatted text.

Across our products like the Gemini app and on Android, we’ve seen consumers already benefiting from this transcription model with new voice capabilities like
[Rambler on Android](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)
and in the Gemini app on macOS. Now, developers can build similar capabilities with Gemini 3.5 Transcribe in the
[Gemini API in Google AI Studio](https://aistudio.google.com/live?model=gemini-3.5-transcribe-live)
and
[Gemini Enterprise Agent Platform](https://console.cloud.google.com/agent-platform/studio/multimodal-live?model=gemini-3.5-transcribe-live-preview)
.

We've built 3.5 Transcribe to plug seamlessly into your developer workflows, whether you’re building voice agents, real-time captioning tools, or post-call analytics pipelines. The model is available across two separate APIs:

* **Real-time streaming:**
  Delivers continuous, bidirectional streaming with sub-second latency for interactive voice apps via the
  [Live API](https://ai.google.dev/gemini-api/docs/live-api/live-transcribe)
  using
  **`gemini-3.5-transcribe-live`**
  **.**
* **Pre-recorded audio processing:**
  Transcribes recorded audio, meetings, call logs, and more with speaker attribution and word-level timestamps via the
  [Interactions API](https://ai.google.dev/gemini-api/docs/transcribe)
  using
  **`gemini-3.5-transcribe`**
  **.**

## Get more precise and intelligent transcription

Gemini 3.5 Transcribe is designed to capture your natural speaking style to better understand your intent and recognize custom vocabulary, so you can execute tasks with your voice.

* **Smart transcription:**
  Seamlessly handles self-corrections (like
  *"let’s meet Tuesday—no, Wednesday"*
  ), removes filler words (“ums” and ‘“ahs"), auto-formats your text.
* **Function calling:**
  The model can delegate complex tasks (such as image generation and file analysis) to other Gemini models via function calls. Currently available in the
  [Gemini macOS app](https://blog.google/innovation-and-ai/products/gemini-app/speak-naturally-gemini-app-mac-os/)
  .
* **More precise transcription:**
  As measured by Artificial Analysis, achieves an average Word Error Rate (WER) of 4.0% for streaming and 2.6% for non-streaming use-cases. It shows strong performance across noisy, real-world environments, accurately capturing alphanumeric entities like postal codes and order IDs.
* **Custom vocabulary:**
  Recognizes specialized jargon and unique spellings by seamlessly adapting transcriptions to your provided custom vocabulary.
* **Global language support:**
  Automatically detects and transcribes over 85 languages, seamlessly handling regional accents and diverse dialects.
* **Multi-speaker identification:**
  Accurately attributes speech in pre-recorded audio with timestamps for up to three speakers (support for 3+ speakers is experimental).