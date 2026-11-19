---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-19T01:43:51.988490+00:00'
exported_at: '2026-11-19T01:43:52.713887+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html
structured_data:
  about: []
  author: ''
  description: 'This seems like a good thing: Google Deepmind researchers used agentic
    AI to mathematically prove, or “formally verify,” a number of the Signal protocol’s
    key cryptographic guarantees­a landmark development for the widely used cryptography
    and AI itself. Conducted as a sort of proof-of-concept project in just four w...'
  headline: Formal Verification of the Signal Protocol Using AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Formal Verification of the Signal Protocol Using AI
updated_at: '2026-11-19T01:43:51.988490+00:00'
url_hash: f61744a14edae5e8bf204b0ff71a98a0e8ef252d
---

## Formal Verification of the Signal Protocol Using AI

[This](https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/)
seems like a good thing:

&gt; Google Deepmind researchers used agentic AI to mathematically prove, or “formally verify,” a number of the Signal protocol’s key cryptographic guarantees­a landmark development for the widely used cryptography and AI itself.
&gt;
&gt; Conducted as a sort of proof-of-concept project in just four weeks, the work is significant in two ways. It serves as further independent validation of the cryptography that protects massive quantities of the world’s communications on platforms like the Signal app, Google Messages, and WhatsApp. And it demonstrates Google DeepMind’s formal verification capabilities using a new AI framework called AlphaProof Code.
&gt;
&gt; […]
&gt;
&gt; The DeepMind analysis did not find any new vulnerabilities in the portions of the Signal protocol it looked at, but when the researchers used AlphaProof Code on older versions of Signal that contain known and long-fixed vulnerabilities, it correctly identified them and showed that the protocol could not be formally verified. The researchers are releasing the specification and proof they developed for the Signal protocol analysis to aid other formal verification work.

Alternate
[link](https://archive.ph/BrmVv)
.

[Details](https://deepmind.google/blog/introducing-alphaproof-code/)
:

&gt; First, our researchers collaborated with a mix of models to translate Signal’s security goals into formal mathematical specifications, with human experts reviewing every one. From there, agents powered by Gemini Carbon did the proofs, generating over six million lines of Lean, a computer language that mathematically proves the accuracy of code.
&gt;
&gt; Next, the agents audited the proof and highlighted areas that needed a second look by a human ­ just one percent of the codebase, a massive time savings. Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most.

Technical
[paper](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
.

Tags:
[academic papers](https://www.schneier.com/tag/academic-papers/)
,
[AI](https://www.schneier.com/tag/ai/)
,
[protocols](https://www.schneier.com/tag/protocols/)
,
[security analysis](https://www.schneier.com/tag/security-analysis/)
,
[Signal](https://www.schneier.com/tag/signal/)

[Posted on November 17, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html)
•
[15 Comments](https://www.schneier.com/blog/archives/2026/11/formal-verification-of-the-signal-protocol-using-ai.html#comments)