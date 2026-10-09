---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-21T10:15:48.650031+00:00'
exported_at: '2026-04-21T10:15:50.939478+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/tiiuae/qimma-arabic-leaderboard
structured_data:
  about: []
  author: ''
  description: A Blog post by Technology Innovation Institute on Hugging Face
  headline: 'QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/tiiuae/qimma-arabic-leaderboard
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard'
updated_at: '2026-04-21T10:15:48.650031+00:00'
url_hash: 24e2166b86b97de3655b25085ac26ee5645c9a08
---

# QIMMA قِمّة ⛰: A Quality-First Arabic LLM Leaderboard

[![image](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/rugVGTdLrdovOU99Hek9T.png)](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/rugVGTdLrdovOU99Hek9T.png)
> **QIMMA validates benchmarks before evaluating models, ensuring reported scores reflect genuine Arabic language capability in LLMs.**

If you've been tracking Arabic LLM evaluation, you've probably noticed a growing tension: the number of benchmarks and leaderboards is expanding rapidly, but
**are we actually measuring what we think we're measuring?**

We built
**QIMMA**
قمّة (Arabic for "summit"), to answer that question systematically. Instead of aggregating existing Arabic benchmarks as-is and running models on them, we applied a rigorous quality validation pipeline
*before*
any evaluation took place. What we found was sobering: even widely-used, well-regarded Arabic benchmarks contain systematic quality issues that can quietly corrupt evaluation results.

This post walks through what QIMMA is, how we built it, what problems we found, and what the model rankings look like once you clean things up.

[![image](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/JFGUze00t2twAEsj6XxCm.png)](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/JFGUze00t2twAEsj6XxCm.png)

---

## 🔍 The Problem: Arabic NLP Evaluation Is Fragmented and Unvalidated

Arabic is spoken by over 400 million people across diverse dialects and cultural contexts, yet the Arabic NLP evaluation landscape remains fragmented. A few key pain points have motivated this work:

**Translation issues.**
Many Arabic benchmarks are translations from English. This introduces distributional shifts. Questions that feel natural in English become awkward or culturally misaligned in Arabic, making benchmark data less representative of how Arabic is naturally used.

**Absent quality validation.**
Even
*native*
Arabic benchmarks are often released without rigorous quality checks. Annotation inconsistencies, incorrect gold answers, encoding errors, and cultural bias in ground-truth labels have all been documented in established resources.

**Reproducibility gaps.**
Evaluation scripts and per-sample outputs are rarely released publicly, making it hard to audit results or build on prior work.

**Coverage fragmentation.**
Existing leaderboards cover isolated tasks and narrow domains, making holistic model assessment difficult.

To illustrate where QIMMA sits relative to existing platforms:

| Leaderboard | Open Source | Native Arabic | Quality Validation | Code Eval | Public Outputs |
| --- | --- | --- | --- | --- | --- |
| OALL v1 | ✅ | Mixed | ❌ | ❌ | ✅ |
| OALL v2 | ✅ | Mostly | ❌ | ❌ | ✅ |
| BALSAM | Partial | 50% | ❌ | ❌ | ❌ |
| AraGen | ✅ | 100% | ❌ | ❌ | ❌ |
| SILMA ABL | ✅ | 100% | ✅ | ❌ | ✅ |
| ILMAAM | Partial | 100% | ✅ | ❌ | ❌ |
| HELM Arabic | ✅ | Mixed | ❌ | ❌ | ✅ |
| ⛰ QIMMA | ✅ | 99% | ✅ | ✅ | ✅ |

QIMMA is the only platform combining all five properties: open source, predominantly native Arabic content, systematic quality validation, code evaluation, and public per-sample inference outputs.

---

## ⛰ What's in QIMMA?

QIMMA consolidates
**109 subsets**
from
**14 source benchmarks**
into a unified evaluation suite of over
**52,000 samples**
, spanning 7 domains:

| Domain | Benchmarks | Task Types |
| --- | --- | --- |
| **Cultural** | AraDiCE-Culture, ArabCulture, PalmX | MCQ |
| **STEM** | ArabicMMLU, GAT, 3LM STEM | MCQ |
| **Legal** | ArabLegalQA, MizanQA | MCQ, QA |
| **Medical** | MedArabiQ, MedAraBench | MCQ, QA |
| **Safety** | AraTrust | MCQ |
| **Poetry & Literature** | FannOrFlop | QA |
| **Coding** | 3LM HumanEval+, 3LM MBPP+ | Code |

A few things stand out about this design:

* **99% native Arabic content.**
  The only exception is code evaluation, which is inherently language-agnostic.
* **First Arabic leaderboard with code evaluation.**
  QIMMA integrates Arabic-adapted versions of HumanEval+ and MBPP+, making it possible to assess coding capability with Arabic-language problem statements.
* **Diversity in Domains and Tasks.**
  QIMMA evaluates real-world competency areas including education, governance, healthcare, creative expression, and software development.

---

## 🔬 The Quality Validation Pipeline

This is the methodological heart of QIMMA. Before running a single model, we applied a
**multi-stage validation pipeline**
to every sample in every benchmark.

### Stage 1: Multi-Model Automated Assessment

Each sample was independently evaluated by two state-of-the-art LLMs:

* **Qwen3-235B-A22B-Instruct**
* **DeepSeek-V3-671B**

We chose two models with strong Arabic capability but different training data compositions, so that their
*combined*
judgment is more robust than either alone.

Each model scores a sample against a
**10-point rubric**
, with binary scores (0 or 1) per criterion:

A sample is eliminated if either model scores it below 7/10. Samples where both models agree on elimination are dropped immediately. However, where only one model flags a sample, it proceeds to human review in Stage 2.

### Stage 2: Human Annotation and Review

Flagged samples are reviewed by
**native Arabic speakers**
with cultural and dialectal familiarity. Human annotators make final calls on:

* Cultural context and regional variation
* Dialectal nuance
* Subjective interpretation
* Subtle quality issues automated assessment may miss

For culturally sensitive content, multiple perspectives are considered, since "correctness" can genuinely vary across Arab regions.

---

## ⚠️ What We Found: Systematic Quality Problems

The pipeline revealed recurring quality issues across benchmarks; not isolated errors, but
**systematic patterns**
reflecting gaps in how benchmarks were originally constructed.

### By the Numbers

| Benchmark | Total Samples | Discarded | Discard Rate |
| --- | --- | --- | --- |
| ArabicMMLU | 14,163 | 436 | 3.1% |
| MizanQA | 1,769 | 41 | 2.3% |
| PalmX | 3,001 | 25 | 0.8% |
| MedAraBench | 4,960 | 33 | 0.7% |
| FannOrFlop | 6,984 | 43 | 0.6% |
| ArabCulture | 3,482 | 7 | 0.2% |
| MedArabiQ | 499 | 1 | 0.2% |
| GAT | 13,986 | 1 | ~0.0% |
| 3LM STEM | 2,609 | 1 | ~0.0% |
| AraDiCE-Culture | 180 | 0 | 0.0% |
| ArabLegalQA | 79 | 0 | 0.0% |
| AraTrust | 522 | 0 | 0.0% |

### Taxonomy of Issues Found

⚖️ Answer Quality

False or mismatched gold indices, factually wrong answers, missing or raw text answers.

📄 Text & Formatting Quality

Corrupt or illegible text, spelling and grammar errors, and duplicate samples.

💬 Cultural Sensitivity

Stereotype reinforcement and monolithic generalizations about diverse communities.

🤝 Gold Answer Compliance

Misalignment of gold answers with evaluation protocols.

---

## 💻 Code Benchmark: A Different Kind of Quality Work

Code benchmarks required a different intervention. Rather than discarding samples, we
**refined the Arabic problem statements**
in 3LM's Arabic adaptations of HumanEval+ and MBPP+, leaving task identifiers, reference solutions, and test suites completely unchanged.

The modification rates were striking:

| Benchmark | Total Prompts | Modified | Unchanged | Modification Rate |
| --- | --- | --- | --- | --- |
| 3LM HumanEval+ | 164 | 145 | 19 | **88%** |
| 3LM MBPP+ | 378 | 308 | 70 | **81%** |

Modifications fell into five categories:

1. **Linguistic refinement**
   : normalizing toward natural Modern Standard Arabic and consistent imperative style
2. **Clarity improvements**
   : fixing ambiguous instructions and unclear constraints
3. **Consistency normalization**
   : standardizing mathematical terminology, punctuation, and example formatting
4. **Structural corrections**
   : fixing broken triple-quoted strings, indentation errors, corrupted text fragments
5. **Semantic refinements**
   : clarifying whether ranges are inclusive/exclusive, preserving task intent

---

## ⚙️ Evaluation Setup

### Evaluation Framework

QIMMA uses
[LightEval](https://github.com/huggingface/lighteval)
,
[EvalPlus](https://github.com/evalplus/evalplus)
and
[FannOrFlop](https://github.com/mbzuai-oryx/FannOrFlop)
as its evaluation framework, chosen for consistency, multilingual community adoption, and reproducibility.

### Metrics by Task Type

| Task Type | Metric | Benchmarks |
| --- | --- | --- |
| **MCQ** | Normalized Log-Likelihood Accuracy | AraDiCE-Culture, ArabicMMLU, ArabCulture, PalmX, 3LM STEM, MedArabiQ, GAT, MedAraBench, AraTrust |
| **Multi-select MCQ** | Probability Mass on Gold Choices | MizanQA |
| **Generative QA** | F1 BERTScore (AraBERT v02) | MedArabiQ, ArabLegalQA, FannOrFlop |
| **Code** | Pass@1 | 3LM HumanEval+, 3LM MBPP+ |

### Prompt Templates

QIMMA standardizes prompting by question format, with six template types:

![QIMMA prompt templates](https://cdn-uploads.huggingface.co/production/uploads/659bc8a7b0f43ed69f0b2300/C-WxGverw4w_pnf6IRUsB.png)


**MCQ**
: generic multiple choice ·
**MCQ-C**
: multiple choice with context passage ·
**MCQ-I**
: multiple choice with specific instructions (GAT analogy/completion) ·
**QA**
: generic open-ended QA ·
**QA-C**
: QA with context ·
**QA-F**
: fill-in-the-blank QA

All prompts are in Arabic. For MizanQA and ArabCulture, benchmark-specific system prompts from the original papers are preserved.

---

## 🏆 Leaderboard Results

We evaluated
**46 open-source models**
on QIMMA, spanning Arabic-specialized
and multilingual models at scales from ~1B to 400B parameters. The table below
shows results for the top instruction-tuned models:

| Model | Avg | Cultural | STEM | Legal | Medical | Safety | Coding | Poetry |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Qwen2.5-72B-Instruct | 65.75 | 72.94 | 72.41 | 67.11 | 47.13 | 88.51 | 54.98 | 57.51 |
| Qwen2.5-14B-Instruct | 56.98 | 61.59 | 58.53 | 63.24 | 37.79 | 81.42 | 48.53 | 56.87 |
| Qwen3-8B | 39.38 | 35.37 | 31.39 | 52.97 | 30.02 | 52.68 | 37.50 | 57.47 |
| Qwen3.5-9B | 56.28 | 59.39 | 61.18 | 54.95 | 40.10 | 77.97 | 49.31 | 59.57 |
| Qwen3.5-27B | 59.70 | 60.61 | 65.49 | 59.67 | 38.92 | 86.59 | **63.39** | 47.03 |
| Jais-2-70B-Chat | **65.81** | **81.95** | **73.64** | **70.69** | 51.84 | **90.23** | 31.58 | 56.13 |
| Jais-2-8B-Chat | 57.89 | 71.18 | 65.94 | 65.54 | 42.99 | 87.55 | 21.30 | 51.94 |
| Llama-3.3-70B-Instruct | 63.96 | 77.74 | 70.33 | 65.72 | **55.56** | 85.63 | 49.30 | 24.43 |
| AceGPT-v2-32B-Chat | 61.14 | 76.97 | 70.51 | 67.68 | 48.64 | 86.97 | 39.14 | 15.56 |
| Yehia-7B-preview | 57.61 | 76.02 | 59.26 | 63.06 | 39.42 | 87.36 | 24.42 | 59.64 |
| Fanar-1-9B-Instruct | 56.78 | 72.78 | 65.64 | 65.47 | 49.44 | 88.51 | 30.66 | 0.02 |
| ALLaM-7B-Instruct-preview | 56.51 | 63.86 | 67.10 | 64.53 | 42.36 | 84.10 | 25.96 | 48.48 |
| gemma-3-27b-it | 60.75 | 58.84 | 68.64 | 66.92 | 42.94 | 85.44 | 51.57 | **59.74** |
| gpt-oss-20b | 32.10 | 28.35 | 23.11 | 52.46 | 29.29 | 32.38 | 41.92 | 15.34 |

A few observations worth highlighting:

**Jais-2-70B-Chat leads overall**
, with the top score of 65.81 and first place
in Cultural, STEM, Legal, and Safety domains. It is the highest-performing
Arabic-specialized model, demonstrating that domain-focused Arabic training
yields measurable gains across a broad multi-domain evaluation.

**Qwen2.5-72B-Instruct is a close second**
(65.75, a margin of 0.06) and ranks
second in Coding, reflecting strong general-purpose multilingual capability that
remains highly competitive even against Arabic-specialized models.

**Llama-3.3-70B-Instruct leads in Medical**
despite being a general multilingual
model, with the highest Medical domain score (55.56) among all evaluated models.

**Qwen3.5-27B leads in Coding**
(63.39), demonstrating that reasoning-intensive
tasks benefit from thinking capabilities even at smaller model scales.

**gemma-3-27b-it leads in Poetry**
(59.74), demonstrating strong capability in
understanding Arabic poetic language and literary structure.

**Coding remains the hardest domain for Arabic-specialized models.**
Most
Arabic-specialized models score below 35 in Coding, while multilingual models
tend to perform better, suggesting that Arabic code instruction following remains
an open challenge in the field.

### The Size-Performance Relationship

Across the full leaderboard (46 models), a clear but imperfect size-performance
correlation emerges. However, there are interesting exceptions:

[![c64aafc7-1](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/KPdYTBwzMvJEyALTYfGji.png)](https://cdn-uploads.huggingface.co/production/uploads/66c8620a79b42e5c941b0265/KPdYTBwzMvJEyALTYfGji.png)

* Arabic-specialized models often outperform size-matched multilingual models
* Instruction-tuned models consistently outperform their base counterparts except for Qwen3
* Some smaller Arabic-specialized models (Fanar-1-9B, ALLaM-7B) outperform much larger multilingual models on specific domains

---

## 🌟 What Makes QIMMA Different

To summarize the distinctive properties of QIMMA:

| Property | Details |
| --- | --- |
| **Quality-first philosophy** | Validation runs *before* evaluation, not as an afterthought |
| **Multi-model validation** | Two LLMs with different training + human review for flagged cases |
| **99% native Arabic** | Avoids translation artifacts almost entirely |
| **Multi-domain, multi-task** | 7 domains, 3 task types (MCQ, QA, code), 109 subsets |
| **Code evaluation** | First Arabic leaderboard to include code generation |
| **Full transparency** | Per-sample inference outputs publicly released, not just aggregate scores |
| **LightEval-based** | Unified, reproducible evaluation codebase |
| **Dialectal awareness** | Explicit handling of MSA vs. dialectal variation in prompts and rubrics |

---

## 🔗 Resources

---

## 🔖 Citation

```
@misc{alqadi2026arabicbenchmarksreliableqimmas,
      title={Are Arabic Benchmarks Reliable? QIMMA's Quality-First Approach to LLM Evaluation},
      author={Leen AlQadi and Ahmed Alzubaidi and Mohammed Alyafeai and Hamza Alobeidli and Maitha Alhammadi and Shaikha Alsuwaidi and Omar Alkaabi and Basma El Amel Boussaha and Hakim Hacid},
      year={2026},
      eprint={2604.03395},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.03395},
}
```