---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-06T22:55:21.003661+00:00'
exported_at: '2026-10-06T22:55:23.301940+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory
structured_data:
  about: []
  author: ''
  description: We're bringing on-device privacy to cloud-scale memory. Learn how Private
    AI Compute's new persistent memory layer protects your data across devices.
  headline: Advancing Private AI Compute with secure, server-side memory
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Advancing Private AI Compute with secure, server-side memory
updated_at: '2026-10-06T22:55:21.003661+00:00'
url_hash: cd8117c6d35f983b0412afe669291075935696f1
---

A technical update on our Private AI Compute architecture, which will enable persistent, cross-device AI memory with on-device privacy standards.

AI is becoming more capable and intuitive â remembering what matters, understanding the world around you, and acting at your direction. Privacy and trust are core to making that possible, ensuring your data stays private and protected as AI systems evolve to provide more continuous assistance across your devices.

Today, we are sharing how we will bring private, server-side memory to our
[Private AI Compute](https://blog.google/innovation-and-ai/products/google-private-ai-compute/)
platform. This breakthrough resolves a longstanding dilemma in modern AI: how to give an assistant long-term continuity across devices while upholding the strict privacy standards typically limited to on-device processing.

## Bringing on-device privacy to cloud-scale memory

With this new technical capability, a new persistent memory layer will be able to function like a secure digital vault in the cloud. Under this model, the information needed to assist you is sealed within dedicated, encrypted storage, while the cryptographic keys required to unlock it are held exclusively on your personal devices â ensuring your data is inaccessible to anyone else, even Google.

The diagram below shows how this update to Private AI Compute will work. When an AI model needs to access information to assist you, an authenticated, end-to-end encrypted channel connects your device to a protected, isolated environment in the cloud. That space, or âsecure enclave,â temporarily decrypts your data in isolated memory to handle the request, saves any new context, and immediately encrypts it, keeping your information private as if it never left your device.