---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-19T02:48:53.586421+00:00'
exported_at: '2026-09-19T02:48:54.806574+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement
structured_data:
  about: []
  author: ''
  description: Radiology AI is evolving beyond report generation. CARE-X explores
    a unified approach that combines flexible reasoning, calibrated predictions, and
    measurement-based tools for chest X-ray interpretation.
  headline: 'Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary
    Supervision, Reward-Aligned Learning, and Tool-Augmented Meas...'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/introducing-care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Introducing CARE-X: Towards Clinically Useful Radiology VLMs with Auxiliary
  Supervision, Reward-Aligned Learning, and Tool-Augmented Measurement'
updated_at: '2026-09-19T02:48:53.586421+00:00'
url_hash: 296b95d62f193ef74c62fd13f70f58f7f5da8f36
---

![Diagram of a tool-augmented radiology vision-language model (VLM) workflow. An orchestrator routes a user’s image query to a VLM, which performs image analysis, calls measurement tools to calculate cardiac and thoracic widths and the cardiothoracic ratio (CTR), and returns diagnostic metrics with visual overlays.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/CAREX-BlogHeroFeature-1400x788-1-scaled.jpg)

Research Note: CARE-X is a research model and not a Microsoft product offering or medical device. It has not been cleared or approved by any regulatory authority and is not intended for clinical diagnosis, screening, or patient care. The results described below are retrospective research findings and do not establish the safety, effectiveness, or suitability of CARE-X for any clinical use. References to potential workflows describe areas for future research, not currently available capabilities or recommended uses.

## At a glance

* The challenge: Chest X-ray interpretation spans diverse tasks that require both expressive report generation and calibrated diagnostic predictions.
* CARE-X is a unified chest X-ray VLM for diverse clinical interpretation tasks. It combines generation and structured prediction to provide both free-text reasoning and deterministic outputs.
* CARE-X uses reinforcement learning (DAPO) to reward clinical correctness in a multi-task setting.
* In a separate research experiment from CARE-X, we paired Qwen3-VL-4B-Instruct with deterministic measurement tools to evaluate whether direct computation could improve performance on measurement-dependent conditions compared with visual approximation alone.
* Validated on real-world Indian clinical data from Narayana Health, including rare ICU pathologies and CT-confirmed enlargement conditions.

## What radiologists need: Task diversity, flexibility, and clinical fidelity

A clinically useful radiology AI system must support a wide range of tasks, adapt to different workflows, and produce outputs that are medically accurate.

Radiologists and other clinicians use chest X-rays for many different purposes. A clinically useful AI system must be able to support that range of tasks. It may be asked to generate detailed findings and concise impressions for a report, answer questions about the presence, absence, or location of a finding, identify medical devices and assess their placement, or pinpoint exactly where an abnormality appears in an image.

These tasks also require different kinds of outputs, from narrative reports to calibrated diagnostic scores. And above all, they require clinical accuracy. A report could ostensibly be perfectly written yet clinically wrong if it misses a finding, reverses a negation, or misidentifies a location. Certain findings could be trivial in one context and vital to identify in another.

[CARE-X](https://www.microsoft.com/en-us/research/publication/care-x-towards-clinically-useful-radiology-vlms-with-auxiliary-supervision-reward-aligned-learning-and-tool-augmented-measurement/)
was developed as a research model to explore how a unified approach can address these diverse demands. The system combines generative and discriminative capabilities, clinically aligned optimization, and tool-based reasoning to support a broader range of radiology workflows while maintaining clinical fidelity.

Spotlight: Microsoft research newsletter

## Microsoft Research Newsletter

Stay connected to the research community at Microsoft.

Opens in a new tab

## Gaps in current radiology vision-language models

Despite the impressive task breadth of recent models, critical gaps remain between what radiologists need and what current systems deliver:

1. **No calibrated confidence for diagnostic decisions.**
   Generative VLMs predict diagnoses as free text, but they typically do not provide calibrated confidence scores. In clinical settings, confidence matters. Clinicians cannot tune sensitivity–specificity trade-offs across clinical contexts—an important requirement for real-world deployment. Discriminative models provide these properties but lack the flexibility of open-ended generation.
2. **Cross-entropy loss does not optimize clinical fidelity.**
   Standard training methods treat all token-level errors similarly, regardless of their clinical consequences. A coordinate mistake may be penalized no more than a harmless wording change. A “yes” can be flipped to a “no” even though the clinical meaning is completely different. Missing a life-threatening finding may carry the same training penalty as omitting a minor observation. As a result, models are not explicitly optimized for what matters most in patient care.
3. **No capability for measurement-dependent findings.**
   Some radiological findings require more than visual recognition. Radiological signs such as cardiomegaly, mediastinal widening etc. depend on precise measurements. For example, a model may correctly recognize whether a chest radiograph was acquired using an AP or PA view. But determining cardiomegaly requires measuring the cardiac and thoracic widths and determining the cardiothoracic ratio. Those quantities should be measured and computed rather than visually approximated while considering variables such as type of view, exposure, rotation of the patient etc.

Together, these gaps call for more than a fluent generative model. The system must combine broad task coverage, structured predictions, clinically aligned optimization, and quantitative tools where direct measurement is required.

---

## CARE-X: One model, flexible outputs

CARE-X brings these diverse interpretation capabilities into one model, using generative or dual inference according to the needs of each task:

| Task type | What CARE-X does | Inference mode |
| --- | --- | --- |
| Report generation: Findings | Produces the detailed findings section | Generative |
| Report generation: Impression | Produces the concise diagnostic impression | Generative |
| Presence and negation assessment | Determines whether a pathology is present or absent and handles negation | Dual: generative + auxiliary head |
| Disease location assessment | Identifies where an abnormality appears | Generative |
| Fine-grained multilabel disease classification | Categorizes abnormalities across multiple labels | Generative |
| Multilabel tubes and lines classification | Identifies visible medical devices | Generative |
| Abnormal placement detection of tubes and lines | Determines whether a device is positioned incorrectly | Dual: generative + auxiliary head |
| Abnormality phrase grounding | Localizes a described pathological finding | Dual: generative + auxiliary head |
| Anatomical grounding | Localizes 29 anatomical regions | Dual: generative + auxiliary head |

Table 1: CARE-X task coverage and inference modes

**Dual inference**
means that a single forward pass produces both an autoregressive response and a structured auxiliary-head prediction with a confidence score. This provides free-text flexibility alongside threshold-adjustable outputs for tasks where operating-point control matters.

## The CARE-X architecture and training approach

CARE-X is built on a SigLIP2-so400M vision encoder and a Phi-4-mini-instruct (3.8B) language model connected through a lightweight adapter. To support both free-text generation and structured clinical predictions, the model augments the shared language backbone with
**task-specific auxiliary heads**
for classification and visual grounding. These heads provide calibrated diagnostic predictions and spatial localization signals while sharing representations with the generative language model. Rather than being trained independently, they are co-trained with the language-modeling objective, allowing structured supervision to enrich shared representations and improve generative performance on the same tasks.

**Training.**
CARE-X uses a three-stage supervised fine-tuning pipeline (vision pre-training, adapter/head training, and LoRA adaptation) followed by DAPO-based reinforcement learning. DAPO optimizes task-specific rewards for clinical reporting, diagnostic accuracy, and spatial grounding quality.

![CARE-X architecture with a SigLIP2 vision encoder, Phi-4-mini backbone, classification and grounding auxiliary heads, language modeling, and DAPO alignment for report generation, VQA, and grounding.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure_1_CARE-X_updated.png)


*Figure 1. The CARE-X model. (Left) Supervised fine-tuning with task-specific heads — classification, grounding, and language modeling — sharing the same Phi-4-mini-instruct backbone. The classification head outputs calibrated P(Yes)/P(No) scores; the grounding head outputs bounding box coordinate with confidence; the language modeling head generates free-text responses. (Right) DAPO with task-specific rewards for multi-task reinforcement alignment across report generation, grounding, and VQA.*

## Auxiliary supervision: Structured prediction strengthens generation

A central finding of this work is that co-training discriminative auxiliary heads with a generative VLM enriches shared representations, leading to stronger generative performance on the same tasks while also providing calibrated structured predictions.

### Grounding improvements

The auxiliary grounding head consistently improves localization over generative decoding. On anatomical grounding (Chest ImaGenome), mAP and mIoU increase by +28.2 pp and +6.2 pp, while the largest gains occur on phrase grounding (PadChest), with +24.6 pp mAP and +14.1 pp mIoU. The composite spatial loss enhances geometric precision in shared representations.

### DAPO bridges the gap to dedicated detection heads

DAPO-trained generative output approaches or exceeds the SFT auxiliary detection head. On Anatomy grounding, CARE-X generative (0.868 mAP) surpasses the SFT detection head (0.865). This is practically significant—it demonstrates that reward-aligned learning can bring autoregressive spatial decoding to parity with structured prediction, offering clinicians a single generative inference mode without requiring auxiliary heads at test time.

### Calibrated classification with tunable operating points

Beyond representation enrichment, the classification head offers a distinct deployment advantage: calibrated probability scores with tunable thresholds allow clinicians to shift between high-sensitivity screening and high-specificity confirmation from a single forward pass—a capability purely generative architectures cannot provide.

| Model | Inference Setting | Sensitivity ↑ | PPV ↑ | F1 ↑ |
| --- | --- | --- | --- | --- |
| CARE-X | Generative | 0.932 | 0.895 | 0.913 |
| CARE-X (Th=0.5) | Auxiliary Head | **0.943** | 0.885 | **0.913** |
| CARE-X (Th=0.6) | Auxiliary Head | 0.855 | **0.927** | 0.890 |
| CheXOne | Generative | 0.878 | 0.854 | 0.866 |
| MedGemma | Generative | 0.798 | 0.886 | 0.839 |

Table 2: Abnormality classification performance on Chest ImaGenome. Adjustable thresholds enable operating-point selection.



---

## Strong report generation across four benchmarks

Within the paper’s comparison set, CARE-X achieves the strongest performance on most reported metrics across MIMIC-CXR, IU-Xray, CheXpert-Plus, and ReXGradient. CRIMSON, a held-out metric that evaluates abnormal findings and weights errors by clinical severity, suggests these gains reflect clinically meaningful improvements rather than reward-specific optimization.

![CRIMSON scores (↑) for CARE-X against baseline report-generation models across four chest X-ray datasets — ReXGradient, MIMIC-CXR, IU-Xray, and CheXpert-Plus. CARE-X (highlighted) achieves the highest CRIMSON score on every dataset.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/FIG2_CARE_NOLOGO.png)


*Figure 2. CRIMSON scores (↑) for CARE-X against baseline report-generation models across four chest X-ray datasets — ReXGradient, MIMIC-CXR, IU-Xray, and CheXpert-Plus. CARE-X (highlighted) achieves the highest CRIMSON score on every dataset.*

## CARE-X reaches 94% accuracy on ReXVQA

**CARE-X ranks first on the**
[**ReXrank RexVQA leaderboard**

(opens in new tab)](https://rexrank.ai/)
as of August 2026. On the ReXVQA benchmark (41,007 question–answer pairs across five clinically relevant categories), CARE-X reaches
**94% overall accuracy**
, six percentage points above the next-best publicly reported model.

![Radar chart comparing ReXVQA accuracy across six categories for three models: CheXOne-R1, MedGemma, and CARE-X. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure_3_CARE-X_NoLogo.png)


Figure 3: ReXVQA accuracy across five findings-quality dimensions — negation, presence, location, differential diagnosis, geometric information, and overall. CARE-X consistently outperforms CheXOne-R1 and MedGemma on every axis, with the largest margins in differential diagnosis, location assessment and negation.



---

Some radiological findings depend on quantitative measurements rather than visual patterns. In a separate research experiment from CARE-X, we built an inference-time pipeline that combines Qwen3-VL-4B-Instruct with deterministic measurement tools, allowing the model to alternate between image understanding and precise computation. Qwen3-VL-4B-Instruct retains visual access to the radiograph throughout inference, invoking tools to identify anatomical landmarks, compute measurements, and evaluate diagnostic thresholds as needed. This creates a multi-turn reasoning loop that interleaves perception and measurement, enabling the model to combine visual context with exact quantitative evidence before reaching a diagnosis.

![Diagram illustrating a workflow for a medical assistant using a vision-language model (VLM) to analyze chest X-ray images and provide diagnostic metrics. Key components include orchestrator handling prompts and tool calls, assistant performing perception and tool calls to measure cardiac and thoracic widths, and synthesizing diagnosis with visual overlays and calculated cardiothoracic ratio (CTR) displayed in red and blue.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure_4_CARE-X_updated.png)


*Figure 4. Tool-augmented quantitative reasoning pipeline. The orchestrator mediates a multi-turn loop: the VLM reasons over the image (perception), emits structured tool calls, receives deterministic results, and synthesizes the final diagnosis.*

Despite requiring no task-specific training, this approach substantially outperforms perception-only inference across all evaluated measurement-based conditions. The results suggest that for threshold-dependent diagnoses, direct computation of clinically defined measurements is more reliable than visual approximation alone.

More broadly, this measurement-augmented approach could augment clinical workflows by expanding the set of quantitative assessments routinely derived from chest radiographs. For example, aortic dilation is not typically quantified on CXR and is often detected only incidentally on CT scans obtained for other indications. As delayed detection can contribute to adverse cardiovascular outcomes, reliable CXR-based screening could enable earlier identification and follow-up of aortic dilation.

| Condition | Perception F1 | Tool F1 | Δ F1 |
| --- | --- | --- | --- |
| Cardiomegaly | 74.56 | 96.00 | +21.4 |
| Mediastinal Widening | 72.63 | 97.47 | +24.8 |
| Aortic Knob Enlargement | 60.31 | 99.76 | +39.5 |
| Ascending Aorta Enlargement | 39.33 | 100.00 | +60.7 |
| Descending Aorta Enlargement† | 28.57 | 100.00 | +71.4 |
| **Average** |  |  | **+43.6** |

Table 3: Perception-only versus tool-augmented measurement. The average F1 improvement is 43.6 percentage points across five conditions.



---

## Validation on Indian clinical data: Rare ICU conditions and CT-confirmed enlargement

**Research ethics and data use**
: The Narayana Health evaluations used de-identified, retrospective clinical data under applicable institutional ethics review and data-use approvals. Narayana Health approved publication of the study results described here.

### Study 1: Inpatient and ICU conditions

To assess real-world generalizability in a research setting, we evaluated CARE-X on 1,047 de-identified chest radiographs from Narayana Health, annotated for five rare, high-acuity conditions with prevalence ranging from 2.6% to 5.2%—reflecting realistic clinical distributions where missed diagnoses carry severe consequences.

|  | Fracture | Mediastinal Shift | Pneumoperitoneum | Pneumothorax | Tubes &amp; Lines Abnormal Placement |
| --- | --- | --- | --- | --- | --- |
| **Model** | Sens / Spec | Sens / Spec | Sens / Spec | Sens / Spec | Sens / Spec |
| CheXOne | 0.41 / 0.90 | 0.80 / 0.78 | 0.67 / 0.98 | **0.85** / 0.72 | 0.03 / 0.97 |
| MedGemma | 0.05 / 1.00 | **1.00** / 0.53 | 0.00 / 1.00 | 0.52 / 0.73 | 0.18 / 0.87 |
| **CARE-X** | **0.62** / 0.64 | 0.83 / 0.86 | **0.89** / 0.94 | 0.83 / 0.75 | **0.66** / 0.77 |

Table 4: ICU pathology classification on Indian hospital data. CARE-X achieves the most balanced performance.

CARE-X achieves the highest sensitivity in three out of five conditions while maintaining reasonable specificity, demonstrating generalization to low-prevalence clinical settings.

### Study 2: CT-confirmed enlargement conditions

In a retrospective study to measure pure recall efficacy, we evaluated measurement-dependent conditions such as mediastinal widening findings including aortic enlargement, hilar mass, and pulmonary artery enlargement on a outpatient cohort of 122 positive cases with CT-confirmed ground truth, avoiding the subjectivity of radiologist consensus on borderline enlargement findings on CXR. In the overlay setting, the VLM receives the original radiograph alongside a second image with condition-relevant anatomical segmentation masks — offering spatial guidance without direct access to measurement tools.

The tool-augmented variant reached 94.26% recall, a +10.65 percentage-point gain over the best perception-only baseline. Where CT or echocardiography access is limited, reliable triage from a widely available modality like chest X-ray can cut both unnecessary referrals and missed diagnoses.

![chart](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/08/Figure_5_CARE-X_AH-1.jpg)


Figure 5: Recall on the CT-confirmed enlargement cohort across perception-only, overlay-assisted, and tool-augmented inference. (Study 2)

In a related study (accepted at EACTS conference 2026), for mild aortic dilation, the measurement-driven reasoning approach detected 40 of 43 CT-confirmed cases (93% sensitivity), compared to just 5 of 43 (12%) identified on the initial radiology reads, where aortic enlargement is usually not the primary indication for the chest X-ray. This corresponds to 35 additional mild cases that were surfaced but missed during the initial CXR interpretation. These results suggest that explicit quantitative measurements may help identify borderline enlargement that is difficult to assess through visual inspection alone.

## What this does and doesn’t show

These numbers are all recall, i.e., how many true positives we catch. This was the focus of the initial study because, in triage, a missed diagnosis is typically the costlier failure mode, and CT-confirmed ground truth gave us a clean way to measure it without relying on radiologist consensus for the difficult cases.

Recall, however, captures only one dimension of diagnostic performance. A model that flags everything achieves perfect recall and is useless in practice. An extended study is underway that includes CT-confirmed negative cohorts as well. Preliminary results are promising, and further studies are planned to explicitly evaluate the viability of quantitative aortic measurements on chest X-ray as a screening tool for aortic dilation.

---

## CARE-X: Toward clinically useful radiology AI

CARE-X demonstrates that discriminative and generative objectives can be effectively combined within a unified radiology AI model. By jointly training classification, grounding, and language capabilities, the model supports both flexible report generation and calibrated, threshold-adjustable predictions. The separate measurement study further highlights a practical division of labor between learned reasoning and deterministic computation: the VLM provides visual understanding and identifies relevant evidence, while measurement-dependent diagnoses are computed through transparent, tool-based calculations. Retrospective evaluation on clinically challenging Narayana Health cohorts provides encouraging evidence of the potential of this approach for real-world radiology applications. The clinical relevance of this research is underscored by the selection of the AI-based aortic dilatation screening application as a finalist for showcase at the
**IHF Innovation Hub, World Hospital Congress 2026**
, recognizing its potential to support earlier detection and clinical decision-making in cardiovascular care.

Looking ahead, CARE-X can be extended beyond its current capabilities through structured report generation, richer differential diagnosis support, and tighter integration of tools within the model itself. The framework could also benefit from incorporating broader clinical context, including laboratory results and patient history, enabling more comprehensive clinical reasoning.

---

**CARE-X is a research model, not a Microsoft product offering or medical device. It has not been cleared or approved by any regulatory authority and is not intended or validated for clinical diagnosis, screening, patient care, or clinical decision-making. The results described are retrospective research findings and do not establish safety, effectiveness, or suitability for clinical use.**

Paper co-authors:

[*Mercy Ranjit*](https://www.microsoft.com/en-us/research/people/meranjit/)
,
[*Anirban Porya*

(opens in new tab)](https://www.linkedin.com/in/anirban-porya22/)
,
[*Niharika Vadlamudi*

(opens in new tab)](https://www.linkedin.com/in/niharika-vadlamudi/)
,
[*Nikhilesh E*

(opens in new tab)](https://www.linkedin.com/in/nikhilesh-e-484b21255/)
,
*[Sathvik Joel
(opens in new tab)](https://www.linkedin.com/in/sathvik-joel-97524b18b/)
,*
[*Prasanth V V*

(opens in new tab)](https://www.linkedin.com/in/prasanthvv/)
,
[*Tanuja Ganu*](https://www.microsoft.com/en-us/research/people/taganu/)
,
[*Abhyuday Swamy*

(opens in new tab)](https://www.linkedin.com/in/abhyuday-swamy-105173166/)
,
[*Pranay Umredkar*

(opens in new tab)](https://www.linkedin.com/in/pranay97/)
*,*
[*Pradeep Narayan*

(opens in new tab)](https://www.linkedin.com/in/dr-pradeep-narayan-9500101b8/)
*,*
[*Vivek Rajagopal*

(opens in new tab)](https://www.linkedin.com/in/vivek-rajagopal/)

Collaborators:
[Medha AI
(opens in new tab)](https://www.medha-analytics.ai/)
,
[Narayana Health
(opens in new tab)](https://www.narayanahealth.org/)

Opens in a new tab