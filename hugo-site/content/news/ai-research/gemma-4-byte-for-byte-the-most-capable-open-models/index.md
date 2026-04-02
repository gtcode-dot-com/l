---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T16:15:37.989496+00:00'
exported_at: '2026-04-02T16:15:40.804424+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/gemma-4-byte-for-byte-the-most-capable-open-models
structured_data:
  about: []
  author: ''
  description: 'Gemma 4: our most intelligent open models to date, purpose-built for
    advanced reasoning and agentic workflows.'
  headline: 'Gemma 4: Byte for byte, the most capable open models'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/gemma-4-byte-for-byte-the-most-capable-open-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Gemma 4: Byte for byte, the most capable open models'
updated_at: '2026-04-02T16:15:37.989496+00:00'
url_hash: e6d22ecbfc74b15427a770cb632d87b9a4b19adb
---

At the edge, our E2B and E4B models redefine on-device utility, prioritizing multimodal capabilities, low-latency processing and seamless ecosystem integration over raw parameter count.

## Powerful, accessible, open

To power the next generation of pioneering research and products, we've sized the Gemma 4 models specifically to run and fine-tune efficiently on hardware — from billions of Android devices worldwide, to laptop GPUs, all the way up to developer workstations and accelerators.

By using these highly optimized models, you can fine-tune Gemma 4 to achieve state-of-the-art performance on your specific tasks. We've already seen incredible success with this approach; for instance, INSAIT created a pioneering Bulgarian-first language model (
[BgGPT](https://deepmind.google/models/gemma/gemmaverse/insait/)
), and we worked with Yale University on
[Cell2Sentence-Scale](https://blog.google/innovation-and-ai/products/google-gemma-ai-cancer-therapy-discovery/)
to discover new pathways for cancer therapy, among many others.

Here is what makes Gemma 4 our most capable open model family yet:

* **Advanced reasoning:**
  Capable of multi-step planning and deep logic, Gemma 4 demonstrates significant improvements in math and instruction-following benchmarks that require it.
* **Agentic workflows:**
  Native support for function-calling, structured JSON output, and native system instructions enables you to build autonomous agents that can interact with different tools and APIs and execute workflows reliably.
* **Code generation:**
  Gemma 4 supports high-quality offline code, turning your workstation into a local-first AI code assistant.
* **Vision and audio:**
  All models natively process video and images, supporting variable resolutions, and excelling at visual tasks like OCR and chart understanding. Additionally, the E2B and E4B models feature native audio input for speech recognition and understanding.
* **Longer context:**
  Process long-form content seamlessly. The edge models feature a 128K context window, while the larger models offer up to 256K, allowing you to pass repositories or long documents in a single prompt.
* **140+ languages:**
  Natively trained on over 140 languages, Gemma 4 helps developers build inclusive, high-performance applications for a global audience.

## Versatile models for diverse hardware

We are releasing the Gemma 4 model weights in sizes tailored for specific hardware and use cases, ensuring you get frontier-class reasoning wherever you need it:

### 26B and 31B models: Frontier intelligence, offline on your personal computers

Optimized to provide researchers and developers with state-of-the-art reasoning on accessible hardware, our unquantized bfloat16 weights fit efficiently on a single 80GB NVIDIA H100 GPU. For local setups, quantized versions run natively on consumer GPUs to power your IDEs, coding assistants and agentic workflows. Our 26B Mixture of Experts (MoE) focus on latency, activating only 3.8 billion of its total parameters during inference to deliver exceptionally fast tokens-per-second, while our 31B Dense is maximizing raw quality and provides a powerful foundation for fine-tuning.

### E2B and E4B models: A new level of intelligence for mobile and IoT devices

Engineered from the ground up for maximum compute and memory efficiency, these models activate an effective 2 billion and 4 billion parameter footprint during inference to preserve RAM and battery life. In close collaboration with our Google Pixel team and mobile hardware leaders like Qualcomm Technologies and MediaTek, these multimodal models run completely offline with near-zero latency across edge devices like phones, Raspberry Pi, NVIDIA and Jetson Orin Nano. Android developers can now prototype agentic flows in the
[AICore Developer Preview](https://android-developers.googleblog.com/2026/03/AI-Core-Developer-Preview)
today for forward-compatibility with Gemini Nano 4.

## An open-source license

You gave us feedback, and we listened. Building the future of AI requires a collaborative approach, and we believe in empowering the developer ecosystem without restrictive barriers. That's why Gemma 4 is released under a commercially permissive
[Apache 2.0 license.](https://goo.gle/gemma-4-apache-2)

This open-source license provides a foundation for complete developer flexibility and digital sovereignty; granting you complete control over your data, infrastructure, and models. It allows you to build freely and deploy securely across any environment, whether on-premises or in the cloud.