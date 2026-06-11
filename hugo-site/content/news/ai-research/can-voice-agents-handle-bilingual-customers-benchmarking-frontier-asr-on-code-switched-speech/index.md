---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-11T03:37:30.837847+00:00'
exported_at: '2026-06-11T03:37:34.302732+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/ServiceNow-AI/code-switching
structured_data:
  about: []
  author: ''
  description: A Blog post by ServiceNow-AI on Hugging Face
  headline: Can Voice Agents Handle Bilingual Customers? Benchmarking Frontier ASR
    on Code-Switched Speech
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/ServiceNow-AI/code-switching
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Can Voice Agents Handle Bilingual Customers? Benchmarking Frontier ASR on Code-Switched
  Speech
updated_at: '2026-06-11T03:37:30.837847+00:00'
url_hash: 7a24901e21158d891ff7dc6a0eb5b79ebbe7cc99
---

# Can Voice Agents Handle Bilingual Customers? Benchmarking Frontier ASR on Code-Switched Speech

Over half of the world's population speaks more than one language. And for many bilingual speakers, code-switching — seamlessly switching between languages, even mid-sentence — is a natural part of everyday communication. Whether in casual conversations, contact centers, or IT helpdesks, speakers fluidly adapt to whichever language feels most natural in the moment.

Despite the prevalence of bilingual speakers across the world, there has been little work focused on how voice agents handle code-switched speech in enterprise settings. So, when a customer asked us how our voice agents would perform for their largely bilingual customer base who routinely code-switched, we decided to build our own benchmark and dataset to evaluate models. We focused on automatic speech recognition (ASR) — the first step in any voice agent pipeline — because transcription errors propagate forward into every downstream component. In enterprise settings, where a misrouted ticket or misunderstood policy question has real operational consequences, getting the transcript right is an especially important step of the voice agent pipeline.

Our benchmark covers four language pairs that were most relevant for our customer base: Spanish-English, French-English, Canadian French-English, and German-English. It uses the non-English language as the matrix framing, with English embedded at varying lengths. The data covers a wide range of Human Resources (HR) and IT Service management (ITSM) scenarios, including employee inquiries about benefits or payroll, and support requests such as password resets, VPN access, or device troubleshooting. To measure how various models perform, we report three metrics: Word Error Rate (WER), Semantic Word Error Rate (SWER), and Answer Error Rate (AER). We choose these metrics to capture both (1) the models' exact accuracy in transcription, as well as (2) their ability to preserve the meaning of the utterance for downstream tasks.

We release our benchmark and data through our harness for evaluating voice models, AU-Harness. We also provide results from seven ASR systems, including some Large Audio Language Models (LALMs), frontier ASRs, and open-source ASRs. Our main finding is that the cost of codeswitching varies depending on the language-pair and model tested. ElevenLabs Scribe V2, Gemini 3 Flash, and Assembly AI Universal 3-Pro surface as the top models across metrics for the task.

[![](https://img.shields.io/badge/Dataset-yellow?logo=huggingface&amp;logoColor=white)](https://huggingface.co/datasets/ServiceNow-AI/asr_codeswitched)
[![](https://img.shields.io/badge/AU-Harness-black?logo=github)](https://github.com/ServiceNow/AU-Harness)

## The Benchmark

### Data Pipeline

We start with an internal corpus of IT support and HR interactions. To create each code-switched utterance, we begin with parallel user utterances in English and one of our four non-English languages, then filter for good code-switching candidates. We keep utterances between 12 and 40 words — short enough to be natural spoken turns, long enough to contain real switching opportunities. We also exclude utterances where entities dominate — emails, phone numbers, IDs, or URLs that make text half-English by necessity rather than bilingual choice. Finally, we require at least three switchable content words — nouns, verbs, or adjectives that are not entities or product names — to give the generation model enough material to produce a meaningful code-switched version.

From here, we tested various strategies for combining languages in a realistic way and ultimately selected a simple persona prompt sent to an LLM (OpenAI/GPT-5) to produce the code-switched text. We then used an LLM verbalization pass to convert the text into its spoken form and used ElevenLabs Multilingual V2 to synthesize the audio. Every utterance is then reviewed by an AI/NLP linguist who is a native speaker of the matrix language; flagged utterances are excluded or regenerated and re-reviewed. The final dataset has 259 Spanish-English records, 298 French-English records, 188 Canadian French-English records, and 173 German-English records
[![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/KjE9EikoFswYiJrepz4R4.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/KjE9EikoFswYiJrepz4R4.png)

### Evaluation Methodology

We report three metrics per model per language pair, chosen to capture transcription accuracy, meaning preservation, and downstream task performance:

* **Word Error Rate (WER)**
  . Along with overall WER per language pair, we report WER by individual language.
* **Semantic WER (SWER)**
  . This score represents the rate of errors that are judged as semantically meaningful. Our implementation is largely based on
  [Pipecat's STT benchmark](https://github.com/pipecat-ai/stt-benchmark/blob/main/src/stt_benchmark/evaluation/semantic_wer.py)
  , and we use Gemma-4-31B as our judge.
* **Answer Error Rate (AER)**
  . This metric directly captures whether transcription errors propagate into downstream failures. It is a question-answer metric that follows the methodology in
  [Bhushan et al. (IISc/ARTPARK, arXiv 2507.16456)](https://arxiv.org/pdf/2507.16456)
  . For each utterance, we generate three downstream comprehension questions and measure whether an LLM reading the ASR transcript can answer them correctly. The flow is shown in the diagram below.
  [![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/XhgSRGk1VKLBaiTSBSCvy.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/XhgSRGk1VKLBaiTSBSCvy.png)

## Findings

We evaluated the following models:

* AssemblyAI / Universal 3-Pro
* Deepgram / Nova 3 Multilang
* ElevenLabs / Scribe V2
* Google / Gemini 3 Flash
* Mistral AI / Voxtral Small 24B-2507
* Nvidia / Parakeet TDT 0.6b V3
* OpenAI / Whisper Large V3 Turbo

### A. How well do models perform on our benchmark for codeswitching?

We analyzed errors along two dimensions:

1. **Word-level accuracy**
   , measured through WER. WER is the standard approach: it aligns the ground truth transcript with the model's output and quantifies the distance between them. Although it is simple and widely used, it can't distinguish a minor spelling difference from a completely wrong word.
2. **Semantic accuracy**
   , captured through SWER and AER. SWER gives us a holistic view of utterance-level performance, though it reflects a judge model's assessment rather than a direct downstream test. AER, by contrast, is a functional test: for each utterance, three comprehension questions measure whether the most consequential details — case numbers, names, dates, the reason for a request — were preserved in the transcription.

The differences between metrics become most meaningful when models diverge across them.

### WER results (lower is better)

[![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/eN7BKO9j6GJTrO-fTkdRs.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/eN7BKO9j6GJTrO-fTkdRs.png)

* ElevenLabs/Scribe V2 and AssemblyAI/Universal-3 Pro are the top two models on transcription accuracy. They are tied on Spanish-English and separated by 0.02-0.13 percentage points across all other language pairs, with Scribe taking a narrow lead on each.
* Google/Gemini 3 Flash follows closely in every language pair, trailing most on Canadian French-English, where it falls 0.14 points behind Scribe and 0.12 points behind AssemblyAI. Deepgram/Nova-3, Mistral/Voxtral, and Nvidia/Parakeet occupy the middle ranks, each pulling ahead on at least one language pair. Parakeet is the weakest of the three overall but closes the gap on German-English, where it out performs both Nova-3 and Voxtral.
* OpenAI/Whisper Large V3 Turbo sits at the bottom, with WER ranging from 0.16 to 0.61. While it's a significant drop, it reflects known limitation of Whisper. When called without an explicit language parameter on code-switched audio, Whisper defaults to translating into English rather than transcribing, failing to preserve the language spoken in the audio.

### SWER and AER results (lower is better)

[![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/CHtqbGVHKAWGdCk25x76H.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/CHtqbGVHKAWGdCk25x76H.png)
The semantic metrics tell a broadly similar story to the WER, with a few inversions.

* Scribe V2 remains at the first place, with very low SWER and AER scores.
* While Assembly AI ranked first or second across language pairs in WER, Gemini 3 Flash consistently outperforms it in AER and pushes AssemblyAI down to third place. The same pattern appears in SWER, although AssemblyAI outperforms Gemini on Spanish-English. As an LALM, Gemini is optimized for language understanding and reasoning, which likely gives it an advantage on meaning-sensitive metrics even where its raw transcription accuracy falls short.
* A similar shift in performance is noticed in Whisper. While it still consistently ranks last, the margin of its underperformance narrows considerably under semantic metrics, a direct consequence of its tendency to translate code-switched audio into English rather than transcribe it.

The semantic results also reveal notable
**consistency between SWER and AER**
. The two metrics operate at different granularities — SWER aggregates error across every word, while AER measures whether three comprehension questions per utterance can be answered correctly — so differences in scale are expected. What's notable is how stable the relative model rankings are across both. The one clear outlier is Deepgram Nova-3, which sits mid-tier on SWER but ranks last or second-to-last on AER across all language pairs. The gap is most pronounced on Spanish-English: Nova-3's overall rate of semantic errors is lower than its error rate specifically on the details that matter most.

### B. What additional cost does code-switching add compared to plain monolingual speech?

While these results provide a clear picture of relative model performance on code-switched speech, they do not reveal whether the errors stem from the inherent difficulty of transcription itself, or from the additional challenge introduced by language switching.

To isolate the cost of codeswitching, we ran every utterance through our evaluation pipeline in three audios: the code-switched audio, a monolingual matrix-language audio of the same content, and a monolingual English audio. For each utterance, we measured the difference in WER between the code-switched and monolingual conditions and aggregated the deltas across the benchmark. Below are the results.
[![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/6feIzK5z7jhjPNzs_6hEe.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/6feIzK5z7jhjPNzs_6hEe.png)

* Scribe V2, Gemini 3 Flash, and AssemblyAI show the smallest deltas overall, with Scribe V2 notably outperforming its own L2 baseline, pointing to genuine robustness to bilingual input.
* The effect of code-switching also follows an intuitive pattern: top-performing systems incur only a small penalty relative to monolingual baselines, while lower-ranked models degrade more substantially, suggesting that code-switching primarily exposes differences in robustness rather than uniformly raising difficulty across all models.
* A consistent structural pattern emerges across all language pairs: the green bars (cost relative to English) are almost always larger than the red bars (cost relative to L2), which is expected — the L2 baseline is itself harder than English for most models, so the net switching penalty is smaller when measured against it. The clearest outlier is Whisper, which shows the largest degradation relative to English, peaking at +0.85 on German-English. It is also the only model that performs better on code-switched speech than on monolingual L2 — a direct consequence of defaulting to translation, which sidesteps the matrix language entirely.

### C. How does code-switching break ASR systems?

Now that we know code-switching can cause models to make mistakes, we turn to investigating the specific conditions associated with those mistakes. To address this question, we fit a two-part model:

1. First, we use a
   **logistic regression**
   to ask what variables are associated with at least one transcription error occurring.
2. Second, conditional on at least one error occurring, we use an
   **ordinary least squares (OLS) regression**
   to examine which variables are associated with error magnitude.

This two-part approach lets us distinguish between factors that make an error more likely to occur and factors that influence how large the error becomes once it has. Both steps include the same predictors: (1) the
**number of language switches**
in the utterance, and (2) the
**utterance's Code-Mixing Index (CMI)**
— the proportion of words drawn from a secondary language relative to the matrix language, following
[Gambäck and Das](https://aclanthology.org/W14-5152.pdf)
. We also include
**utterance length**
as a control, since longer utterances provide more opportunities for error.

#### Variables associated with transcription errors

From the first part of our model, we find that the
**number of language switches**
within an utterance is the predictor most consistently associated with whether the occurrence of a transcription error. Each language change appears to introduce an additional opportunity for the transcription process to fail. This relationship was significant in the French-English language pair in particular, where six out of seven models exhibited it. Other predictors — CMI and utterance length — showed few significant relationships with error occurrence.

When the question shifts to error magnitude, a different pattern emerges. Rather than switch count,
**CMI**
surfaces as the stronger predictor. In the German-English language pair specifically, four out of seven models showed a significant positive relationship between CMI and WER. This suggests that once errors occur, their severity is shaped not by how often the speaker switches languages but by the overall density of mixing: the more thoroughly an utterance interweaves the two languages, the larger the resulting transcription errors tend to be.

#### Portions of a code-switched utterance contributing to transcription errors

The two-part model explains what factors are associated with errors occurring and worsening. Our final experiment examines which portions of a code-switched utterance contribute disproportionately to those errors. To test whether errors distribute differently across the English and non-English parts of an utterance, we used GPT-5 to tag each word by language, then attributed each transcription error to the language of the word on which it occurred, computing a per-language WER. The heatmap below shows the results.
[![image](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/NhfLkDCD9A_329PDGov-L.png)](https://cdn-uploads.huggingface.co/production/uploads/6977dd4e7754c316dbc9f4b3/NhfLkDCD9A_329PDGov-L.png)
The pattern is consistent across all models and language pairs:
**errors concentrate on the English portions**
of utterances rather than the matrix-language portions. This is counterintuitive — English is the language these models tend to handle best in monolingual settings. One explanation is that English segments in code-switched speech may disproportionately contain technical vocabulary or named entities that are harder to transcribe. Another is that embedded-language segments create a challenging context regardless of which language is embedded: when a model transitions into a stretch of non-matrix speech, it must adapt to a different phonological and lexical register mid-utterance, increasing the likelihood of error at exactly that span.

This result suggests that transcription difficulty in code-switched ASR is not concentrated at switch points alone, but extends across embedded-language spans more broadly. Disentangling whether this pattern reflects the lexical characteristics of English segments, their structural role as embedded language, or current models' limited ability to adapt mid-utterance is a promising direction for future work.

## Limitations

Several limitations are worth acknowledging:

* **The benchmark is synthetic**
  . All audio is generated via Text-to-Speech (TTS) model rather than recorded by natural bilingual speakers. So, the benchmark may not fully capture the prosodic and phonological characteristics of real code-switched speech.
* **All models were evaluated with "auto language detection" only.**
  Some systems expose configurations — forced language tokens, multi-language hints, and similar — that might improve transcription quality on code-switched audio. We chose auto-detection because it matches the production setting where the system has no prior knowledge of which language pair a caller will use.
* **Per-language WER excludes insertions.**
  Our per-language WER is computed by tagging each reference word as English or non-English and attributing errors to the corresponding bucket. Insertions cannot be attributed to a language without an additional model call to identify the inserted word's language, so we exclude them from per-language calculations. They are still counted in the aggregate WER.

## Conclusion

Code-switching has long been a stress test for voice models. Our results suggest that for the best frontier ASR systems, it is increasingly becoming a normal condition.

When enterprises choose their ASR systems carefully, bilingual customers can speak naturally — switching languages mid-sentence as the conversation demands — without sacrificing transcription quality or downstream task performance. The top models in our benchmark handle code-switched speech with surprisingly small penalties relative to their monolingual baselines, and the semantic metrics tell an even more encouraging story.

But the picture is not uniformly positive. Before making production decisions, you must benchmark the languages your customers actually speak — performance varies substantially across models and language pairs, and the best choice for Spanish–English speakers is not necessarily the best choice for German–English speakers.