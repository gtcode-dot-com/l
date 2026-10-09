---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-17T06:11:21.300519+00:00'
exported_at: '2026-09-17T06:11:24.103265+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber
structured_data:
  about: []
  author: ''
  description: Google introduces Gemini 3.5 Flash Cyber to help defenders find, validate,
    and patch software vulnerabilities quickly and efficiently.
  headline: Introducing Gemini 3.5 Flash Cyber
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing Gemini 3.5 Flash Cyber
updated_at: '2026-09-17T06:11:21.300519+00:00'
url_hash: 6c6209d948464cb3ed959869ffa71079df142fff
---

Google has invested in cybersecurity for years, pioneering automated vulnerability discovery to secure the worldâs codebases. Tools like
[CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/)
, our code security agent, can automatically find and fix critical software vulnerabilities. But as AI agents become more capable at finding vulnerabilities faster than defenders can fix them, addressing this global threat requires a highly capable, affordable, and scalable approach.

Today, weâre expanding our longtime efforts to better prepare defenders by introducing Gemini 3.5 Flash Cyber, our lightweight cybersecurity model built on top of 3.5 Flash and fine-tuned to find, validate, and patch vulnerabilities quickly and efficiently, making it more effective at these tasks than Geminiâs mainline Flash models.

Flashâs performance and efficiency makes it an ideal foundation for our cybersecurity model efforts. By building on top of Flash, 3.5 Flash Cyber offers a cost-efficient and highly capable alternative to large, costly cybersecurity models.

Given the dual-use nature of this technology, we have taken an intentional approach to how we deploy 3.5 Flash Cyber. As part of a limited-access pilot program, 3.5 Flash Cyber will be exclusively available to governments and trusted partners via CodeMender soon, expanding over time. This will give frontline defenders a head start in finding and fixing critical vulnerabilities before they can be exploited, while mitigating against broader misuse.

Separately, we're also bringing CodeMender's foundational capabilities directly to customers with generally available Gemini models through the
[Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/identity-security/find-and-fix-software-vulnerabilities-with-codemender)
.

## The search space problem: The advantage of lightweight models in code security

Finding deep-seated flaws requires exploring an immense execution search space. Relying on a single, expensive call to a massive language model can create a bottleneck. 3.5 Flash Cyber is particularly suitable for finding vulnerabilities where the agent has to scan a large codebase and analyze a large number of codepaths.

CodeMender invokes 3.5 Flash Cyber multiple times, so agents can analyze vastly more code paths to discover and validate vulnerabilities. The sub-agents then produce a single, high-quality report.

Thanks to its speed and affordability, 3.5 Flash Cyber can be easily integrated into frequent scans, time-sensitive launch processes or commit scanning pipelines at scale.

## 3.5 Flash Cyber benchmark results: an efficient alternative to larger cybersecurity models

We tested 3.5 Flash Cyber on a variety of benchmarks. In particular, we tested 3.5 Flash Cyber on the CyberGym benchmark, which evaluates AI agents against hundreds of real-world software vulnerabilities. Leveraging the low cost of 3.5 Flash Cyber by configuring CodeMender to call 3.5 Flash Cyber up to five times for a single, final report, the overall agent achieved competitive performance against significantly larger models on CyberGym\*.

### Success Rate on CyberGym (pass@1)