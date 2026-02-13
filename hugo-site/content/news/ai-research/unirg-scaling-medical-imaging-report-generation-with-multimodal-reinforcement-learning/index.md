---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T06:48:33.568267+00:00'
exported_at: '2026-02-13T06:48:35.960019+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/unirg-scaling-medical-imaging-report-generation-with-multimodal-reinforcement-learning
structured_data:
  about: []
  author: ''
  description: 'AI can help generate medical image reports, but today’s models struggle
    with varying reporting schemes. Learn how UniRG uses reinforcement learning to
    boost performance of medical vision-language models:'
  headline: 'UniRG: Scaling medical imaging report generation with multimodal reinforcement
    learning'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/unirg-scaling-medical-imaging-report-generation-with-multimodal-reinforcement-learning
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'UniRG: Scaling medical imaging report generation with multimodal reinforcement
  learning'
updated_at: '2026-02-13T06:48:33.568267+00:00'
url_hash: c7f58fddf7e7ebac20c9f2ed6b01dca83933e3e1
---

![Three white icons on a blue‑green gradient: a ribcage scan, a circuit‑style document, and a neural network diagram](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/UniRG-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* AI-driven medical image report generation can help medical providers become more efficient and productive.
* Current models are difficult to train because reporting practices vary widely among providers.
* Universal Report Generation (UniRG) uses reinforcement learning to align model training with real-world radiology practice rather than proxy text-generation objectives.
* UniRG has achieved state-of-the-art performance across datasets, metrics, diagnostic tasks, longitudinal settings, and demographic subgroups.
* Test results show that reinforcement learning, guided by clinically meaningful reward signals, can substantially improve the reliability and generality of medical vision–language models.

AI can be used to produce clinically meaningful radiology reports using medical images like chest x-rays. Medical image report generation can reduce reporting burden while improving workflow efficiency for healthcare professionals. Beyond the real-world benefits, report generation has also become a critical benchmark for evaluating multimodal reasoning in healthcare AI.

Despite recent advances driven by large vision–language models, current systems still face major limitations in real-world clinical settings. One challenge stems from the wide variation in radiology reporting practices across institutions, departments, and patient populations. A model trained with supervised fine-tuning on one set of data may learn its specific phrasing and conventions instead of more general patterns—a problem known as
*overfitting*
. As a result, the model performs well on that data but delivers poor results when evaluated on unseen institutions or external datasets. Moreover, since model training is often aimed at producing text that looks similar to existing reports, some well written but clinically inaccurate reports can slip through.

In this blog, we introduce
**[Universal Report Generation (UniRG)
(opens in new tab)](http://aka.ms/unirg-paper)**
, a reinforcement learning–based framework for medical imaging report generation. This work is a research prototype intended to advance medical AI research and is not validated for clinical use. UniRG uses reinforcement learning as a unifying mechanism to directly optimize clinically grounded evaluation signals, aligning model training with real-world radiology practice rather than proxy text-generation objectives. Using this framework, we train
**[UniRG-CXR
(opens in new tab)](http://aka.ms/unirg-paper)**
, a state-of-the-art chest x-ray report generation model at scale, spanning over 560,000 studies, 780,000 images, and 226,000 patients from more than 80 medical institutions.

To our knowledge, this is the first report generation model to achieve consistent state-of-the-art performance across report-level metrics, disease-level diagnostic accuracy, cross-institution generalization, longitudinal report generation, and demographic subgroups. These results demonstrate that reinforcement learning, when guided by clinically meaningful reward signals, can substantially improve both the reliability and generality of medical vision–language models.

## Azure AI Foundry Labs

Get a glimpse of potential future directions for AI, with these experimental technologies from Microsoft Research.

Opens in a new tab

## A unified framework for scaling medical image report generation

UniRG builds state-of-the-art report generation models by combining supervised fine-tuning with reinforcement learning, which optimizes a composite reward that integrates rule-based metrics, model-based semantic metrics, and LLM-based clinical error signals. This approach allows the resulting model UniRG-CXR to learn from diverse data sources, move beyond dataset-specific reporting patterns, and learn representations that generalize across institutions, metrics, and clinical contexts. Notably, UniRG-CXR sets a new state of the art on the authoritative
[**ReXrank leaderboard**

(opens in new tab)](https://rexrank.ai/)
, a public leaderboard for chest X-ray image interpretation, as of 01/22/2026, surpassing previous best models by substantial margins (Figure 1).

![Fig 1: Overview diagram of the UniRG-CXR framework showing training data sources, reinforcement-learning–based training with composite rewards, evaluation on multiple datasets, and a results panel demonstrating state-of-the-art performance across benchmarks.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/fig1_UPDATED-scaled.png)


Figure 1. Overview of UniRG-CXR. (a) Training Data: UniRG-CXR is trained on the training splits of MIMIC-CXR, CheXpert Plus, and ReXGradient-160k, covering diverse institutions and patient demographics. (b) Training and Rewards: Taking input from the current image, clinical context (e.g., indication), and optionally prior studies, UniRG-CXR uses GRPO reinforcement learning to optimize composite rewards that combine rule-based, model-based, and LLM-based metrics. (c) Evaluation: We assess UniRG-CXR on held-out test sets (MIMIC-CXR, CheXpert Plus, ReXGradient), and unseen datasets (IU Xray and proprietary data). Report quality measured using ReXrank metrics and an LLM-based clinical-error metric, while diagnostic ability is evaluated via F1-based disease classification from generated reports. (d) ReXrank Results: UniRG-CXR achieves SOTA performance across four datasets and two generation settings (findings only and findings + impression), showing substantial gains over prior state-of-the-art systems.

## Universal improvements across metrics and clinical errors

Rather than excelling on one metric at the expense of others, UniRG-CXR delivers balanced improvements across many different measures of report quality. More importantly, it produces reports with substantially fewer clinically significant errors. This indicates that the model is not just learning how to sound like a radiology report, but is better capturing the underlying clinical facts. Explicitly optimizing for clinical correctness helps the model avoid common failure modes where fluent language masks incorrect or missing findings (Figure 2).

![Fig 2: Multi-panel figure showing UniRG-CXR’s state-of-the-art performance: leaderboard gains across metrics, ablation studies demonstrating benefits of combined reinforcement-learning rewards, improved training dynamics with fewer clinical errors, qualitative case studies with error-free reports, and a distribution showing fewer high-error reports compared to prior models.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/UniRG_fig2.png)


Figure 2. UniRG-CXR achieves state-of-the-art performance, delivering consistent and comprehensive performance gains across metrics. (a) On the ReXrank leaderboard, UniRG-CXR (green) shows robust, universal improvement across all evaluation metrics.  (b). Starting from the same SFT checkpoint, RL with our combined reward achieves more balanced gains across metrics and the highest RadCliQ-v1 score compared to RL on single metrics. This ablation study is trained and tested on MIMIC (c). Ablation study on the training dynamics shows RL full (UniRG-CXR) achieves significantly better RadCliQ-v1 score than RL only on BLEU. (d). During training, RL full (UniRG-CXR) shows a steady decrease in clinical errors per report as compared with a fluctuating trajectory without consistent improvement from an ablation run without error awareness (i.e. removing CheXprompt metric optimization). Both (c) and (d) show results on 1024 MIMIC validation set from ablations that are trained on MIMIC. (e). Case studies illustrate that UniRG-CXR can produce error-free reports, unlike MedVersa and MedGemma. (f). UniRG-CXR yields a substantially higher proportion of reports with $\leq 1$ error and fewer with $\geq 4$ errors than prior models.

## Strong performance in longitudinal report generation

In clinical practice, radiologists often compare current images with prior exams to determine whether a condition is improving, worsening, or unchanged. UniRG-CXR is able to incorporate this historical information effectively, generating reports that reflect meaningful changes over time. This allows the model to describe new findings, progression, or resolution of disease more accurately, moving closer to how radiologists reason across patient histories rather than treating each exam in isolation (Figure 3).

![Fig 3: Multi-panel results demonstrating UniRG-CXR’s advantages in longitudinal chest X-ray report generation, including superior performance over prior models and a non-longitudinal ablation across encounters, consistent gains at increasing follow-up complexity, improved handling of temporal disease changes, and qualitative examples of accurate longitudinal predictions.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/fig3_UPDATED-scaled.png)


Figure 3. UniRG-CXR enhances longitudinal report generation. (a). Comparing UniRG-CXR and its non-longitudinal ablation with prior models on longitudinal report generation, we show UniRG-CXR exhibits the best performance and the longitudinal information is beneficial to the performance. (b). UniRG-CXR achieves the best performance across different longitudinal encounter points ranging from the first encounter to the more complex 5th+ encounters, showcasing its improvements are across the board. In comparison, prior models such as GPT-5, GPT-4o and MedGemma are barely surpassing the copy prior report baseline (grey lines).  (c). Compared with prior models which barely improve over the copy prior baseline (dashed line), UniRG-CXR significantly and consistently improves performance across different temporal disease change categories including new development, no change, progression and regression (categorized by GPT-5 on ground truth report). Qualitative examples are shown for each category where UniRG-CXR correctly predicts the temporal change based on the input. All results in this figure are on MIMIC test set with prior information where available.

## Robust generalization across institutions and populations

UniRG-CXR maintains strong performance even when applied to data from institutions it has never seen before. This suggests that the model is learning general clinical patterns rather than memorizing institution-specific reporting styles. In addition, its performance remains stable across different patient subgroups, including age, gender, and race. This robustness is critical for real-world deployment, where models must perform reliably across diverse populations and healthcare environments (Figure 4).

![Fig 4: Multi-panel figure showing UniRG-CXR’s generalization and robustness: zero-shot evaluation with strong performance on unseen datasets, superior condition-level diagnostic F1 scores, and consistent accuracy across gender, age, and race subgroups compared with prior models.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/01/UniRG_fig4.png)


Figure 4. Generalization and robustness of UniRG-CXR. (a). We evaluate UniRG-CXR in a zero-shot setting on two datasets from previously unseen institutions: IU-Xray and PD (proprietary data). UniRG-CXR consistently outperforms prior models, maintaining substantial performance gains in this challenging setup. (b) and (c) present condition-level F1 scores on MIMIC-CXR and PD and highlight that UniRG-CXR remains the overall top-performing model in condition-level diagnostic accuracy. (d). UniRG-CXR demonstrates stable and robust performance across gender, age, and race subgroups, all of which exceed the performance of the second-best model (the dashed lines).

## UniRG is a promising step toward scaling medical imaging report generation

UniRG introduces a reinforcement learning–based framework that rethinks how medical imaging report generation models are trained and evaluated. By directly optimizing clinically grounded reward signals, UniRG-CXR achieves state-of-the-art performance across datasets, metrics, diagnostic tasks, longitudinal settings, and demographic subgroups, addressing longstanding limitations of supervised-only approaches.

Looking ahead, this framework can be extended to additional imaging modalities and clinical tasks, and combined with richer multimodal patient data such as prior imaging, laboratory results, and clinical notes. More broadly, UniRG highlights the promise of reinforcement learning as a core component of next-generation medical foundation models that are robust, generalizable, and clinically aligned.

UniRG reflects Microsoft’s larger commitment to
[advancing multimodal generative AI for precision health
(opens in new tab)](https://ai.nejm.org/doi/full/10.1056/AI-S2300233)
, with other exciting progress such as
[GigaPath](https://www.microsoft.com/en-us/research/blog/gigapath-whole-slide-foundation-model-for-digital-pathology/)
,
[BiomedCLIP](https://www.microsoft.com/en-us/research/publication/biomedclip-a-multimodal-biomedical-foundation-model-pretrained-from-fifteen-million-scientific-image-text-pairs/)
,
[LLaVA-Rad
(opens in new tab)](https://www.nature.com/articles/s41467-025-58344-x)
,
[BiomedJourney](https://www.microsoft.com/en-us/research/publication/biomedjourney-counterfactual-biomedical-image-generation-by-instruction-learning-from-multimodal-patient-journeys/)
,
[BiomedParse](https://www.microsoft.com/en-us/research/blog/biomedparse-a-foundation-model-for-smarter-all-in-one-biomedical-image-analysis/)
,
[TrialScope](https://www.microsoft.com/en-us/research/publication/trialscope-a-unifying-causal-framework-for-scaling-real-world-evidence-generation-with-biomedical-language-models/)
,
[Curiosity](https://www.microsoft.com/en-us/research/publication/generative-medical-event-models-improve-with-scale/)
.

Paper co-authors:
[Qianchu Liu](https://www.microsoft.com/en-us/research/people/qianchuliu/)
,
[Sheng Zhang](https://www.microsoft.com/en-us/research/people/shezhan/)
,
[Guanghui Qin](https://www.microsoft.com/en-us/research/people/guanghuiqin/)
,
[Yu Gu](https://www.microsoft.com/en-us/research/people/yugu1/)
, Ying Jin, Sam Preston, Yanbo Xu, Sid Kiblawi,
[Wen-wai Yim](https://www.microsoft.com/en-us/research/people/yimwenwai/)
, Tim Ossowski,
[Tristan Naumann](https://www.microsoft.com/en-us/research/people/tristan/)
, Mu Wei,
[Hoifung Poon](https://www.microsoft.com/en-us/research/people/hoifung/)

Opens in a new tab