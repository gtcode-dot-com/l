---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-10-01T19:25:31.932805+00:00'
exported_at: '2026-10-01T19:25:34.275827+00:00'
feed: https://unite.ai/feed
language: en
source_url: https://www.unite.ai/ibm-says-granite-speech-5-0-transcribes-3-5-hours-of-speech-in-one-second
structured_data:
  about: []
  author: ''
  description: 'IBM released two compact English speech recognition models on August
    25, 2026, claiming transcription throughput no open model has posted before: more
    than 3.5 hours of speech processed in a single second. The pair, Gran...'
  headline: IBM Says Granite Speech 5.0 Transcribes 3.5 Hours of Speech in One Second
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.unite.ai/ibm-says-granite-speech-5-0-transcribes-3-5-hours-of-speech-in-one-second
  publisher:
    logo: /favicon.ico
    name: GTCode
title: IBM Says Granite Speech 5.0 Transcribes 3.5 Hours of Speech in One Second
updated_at: '2026-10-01T19:25:31.932805+00:00'
url_hash: 67c28606bbd866490831da05afef1d4f889ccf2b
---

IBM released two compact English speech recognition models on August 25, 2026, claiming transcription throughput no open model has posted before: more than 3.5 hours of speech processed in a single second. The pair, Granite Speech 5.0 TurboCTC and a noncommercial counterpart, each carry just 470 million parameters, and the company reports aggregate throughput above 12,600 RTFx on a single NVIDIA H200 GPU, meaning audio flows through the models more than twelve thousand times faster than real time.

The speed comes with competitive accuracy, at least on IBM’s numbers. On the public English short-form test sets of the
[OpenASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
, the noncommercial variant scores a 4.85% aggregate word error rate and the openly licensed variant 5.00%, according to
[IBM’s announcement](https://huggingface.co/blog/ibm-granite/granite-speech-5-0-470m-turboctc)
. Both figures are vendor-reported: IBM labels them unofficial, though inference was run through Hugging Face’s own jobs infrastructure and scored with the leaderboard’s tooling, so the company expects them to match the official table once it updates.

The two models are identical in size and architecture and differ in training data and license. The
[Apache 2.0 model](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc)
trained on roughly 60,000 hours of English audio and is cleared for commercial use. The
[noncommercial variant](https://huggingface.co/ibm-granite/granite-speech-5.0-470m-turboctc-nc)
adds GigaSpeech and SPGI Speech, about 15,000 further hours, bringing its corpus near 75,000 hours under a CC-BY-NC-SA-4.0 license. IBM says the extra data buys a modest accuracy edge on most test sets, with a more noticeable advantage on SPGI Speech itself and a noticeable disadvantage on the leaderboard’s new chunked Earnings22 test.

## An Encoder Without a Language Model

The speed claim rests on what IBM left out. Earlier Granite Speech releases (the 3.3 and 4.x lines documented in IBM’s
[Granite Speech paper](https://huggingface.co/papers/2505.08699)
) bolted a Conformer acoustic encoder onto a Granite language model through a projector and LoRA adapters, generating text autoregressively the way a chat model does. The 5.0 models drop the language model entirely. What remains is a 16-layer Conformer encoder trained with connectionist temporal classification, a decoding scheme that maps audio frames directly to output tokens in a single non-autoregressive pass with greedy decoding.

Two further changes do most of the work. Where previous Granite encoders emitted 50 characters per second, the new models emit 12.5 tokens per second, reached through three stages of 2x temporal subsampling from the 100-frames-per-second log-Mel front end. And the output vocabulary shifted from characters to 16,384 trained subword units, SentencePiece in the noncommercial model and BPE in the Apache one. Fewer, longer tokens at a quarter of the frame rate is what pushes throughput past 20x that of the earlier Granite Speech models, by IBM’s account.

The trade is capability breadth for transcription focus. Without the language model, these models lose the speech translation and keyword biasing the earlier line supported. What they gain is a footprint suited to laptops and edge hardware: IBM positions the pair for enterprise speech-to-text where latency and throughput matter more than a model that can also reason about what it heard.

## What the Evaluations Do and Don’t Show

The strongest independent signal so far comes from far-field audio. On the
[FFASR Leaderboard](https://huggingface.co/spaces/treble-technologies/ffasr)
, which measures recognition of noisy, reverberant speech, IBM reports official results as of August 25, 2026 placing the noncommercial model fifth in accuracy and the Apache model ninth — while both rank as the two fastest entries on the board, with throughput measured on a single NVIDIA L4. FFASR evaluates models on noisy, reverberant, and moving-source audio at multiple SNRs, conditions under which far-field recognition degrades, per the leaderboard’s own description.

The headline 12,600 RTFx figure needs its context, though. It is a batched-inference number on one of the fastest datacenter GPUs sold, not what a laptop running the WebGPU streaming demo will see. The aggregate WER figures cover short-form English only, and the OpenASR Leaderboard’s official rankings, which include private test sets, had not yet absorbed the new models at publication. IBM’s own framing is the honest one here: these are strong vendor-reported results awaiting leaderboard confirmation.

The training recipe also deserves note for what it says about data openness. Every dataset in both models’ corpora is publicly available, and the 2,740 hours of synthetic additions comprise 2,500 hours of multi-speaker audio concatenated from single-speaker segments plus 240 hours of utterances generated by OpenAI’s open-weight gpt-oss models and synthesized with StyleTTS2, targeting the numbers, currencies, and addresses that trip up recognizers. Training took 10 days on 8 NVIDIA H100 GPUs on IBM’s Blue Vela cluster, per the model card.

Both models are live on Hugging Face now with native support in the transformers library — installed from source until the next release — under the Granite Speech collection, and a browser-based streaming demo runs in Chrome and Edge. For a sense of where dedicated transcription models sit against commercial services, see our roundup of
[AI transcription software](https://www.unite.ai/best-ai-transcription-software-services/)
.