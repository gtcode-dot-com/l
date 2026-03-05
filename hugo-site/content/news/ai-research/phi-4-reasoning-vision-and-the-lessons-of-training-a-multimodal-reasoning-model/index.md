---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-05T22:15:35.701391+00:00'
exported_at: '2026-03-05T22:15:38.737563+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model
structured_data:
  about: []
  author: ''
  description: 'Vision-language models improve multimodal systems, but can make them
    slower, costlier, and harder to deploy. Learn how Phi-4-Vision-Reasoning, a compact
    multimodal reasoning model, blends strengths of different methods while reducing
    their limits:'
  headline: Phi-4-reasoning-vision and the lessons of training a multimodal reasoning
    model
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/phi-4-reasoning-vision-and-the-lessons-of-training-a-multimodal-reasoning-model
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Phi-4-reasoning-vision and the lessons of training a multimodal reasoning model
updated_at: '2026-03-05T22:15:35.701391+00:00'
url_hash: 776ba45a1db1905e736bdf66d6357a4b01b0e4b6
---

![White line icons against a blue-green gradient background form an architecture flow chart. In the middle of the chart is a three-by-three matrix of circles and lines within a round-edge square. Above the matrix, three icons in a row – an equation, a person using a desktop, and a head with gears flow by dotted lines to the matrix. To the left of the matrix is an icon representing a stack of files with an arrow pointing to the matrix. To the right of the matrix is a graph with a double headed arrow pointing to the matrix and to itself. Below the matrix is an icon representing a document. A dotted line arrow connects this graph to the matrix, showing the direction flowing from the matrix to the document. To the right of the document icon is an hourglass icon and three list icons with a dotted line connecting the hourglass to the lists.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/Phi4-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* **Phi-4-reasoning-vision-15B**
  is a compact and smart open‑weight multimodal reasoning model that balances reasoning power, efficiency, and training data needs. It is a broadly capable model that allows for natural interaction for a wide array of vision-language tasks and excels at math and science reasoning and understanding user-interfaces.
* **We share lessons learned and best practices**
  for training a multimodal reasoning model—showing the benefit of careful architecture choices, rigorous data curation, and the benefits of using a mixture of reasoning and non-reasoning data.

We are pleased to announce
**Phi-4-reasoning-vision-15B**
, a 15 billion parameter open‑weight multimodal reasoning model, available through
[Microsoft Foundry
(opens in new tab)](https://aka.ms/Phi-4-r-v-foundry)
,
[HuggingFace
(opens in new tab)](https://huggingface.co/microsoft/Phi-4-vision-reasoning-15B)
and
[GitHub
(opens in new tab)](https://github.com/microsoft/Phi-4-vision)
. Phi-4-reasoning-vision-15B is a broadly capable model that can be used for a wide array of vision-language tasks such as image captioning, asking questions about images, reading documents and receipts, helping with homework, inferring about changes in sequences of images, and much more. Beyond these general capabilities, it excels at math and science reasoning and at understanding and grounding elements on computer and mobile screens. In particular, our model presents an appealing value relative to popular open-weight models, pushing the pareto-frontier of the tradeoff between accuracy and compute costs. We have competitive performance to much slower models that require ten times or more compute-time and tokens and better accuracy than similarly fast models, particularly when it comes to
[math and science reasoning](#evaluation)
.

![Performance charts comparing Phi-4-Reasoning-Vision-15B against other models (Kimi-VL, Qwen-3, Gemma-3) on accuracy vs. response time and accuracy vs. completion tokens. Phi-4 stands out as being fast and token-efficient while achieving ~75% accuracy. ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/timing_and_tokens.png)


*Figure
*1*
: Phi-4-reasoning-vision-15B presents a compelling option compared to existing models, pushing the pareto-frontier of the tradeoff between accuracy and compute costs. We have competitive performance to much slower models that require more time and tokens and higher accuracy than similarly fast models. These values were computed by averaging accuracy, time, and output token-counts for a subset of 4 benchmarks: ChartQA
\_TEST
, MathVista
\_MINI
, MMMU
\_VAL
, and ScreenSpot
\_v2
, where we had logged these values.*

In this post, we share the motivations, design choices, experiments, and learnings that informed its development, as well as an evaluation of the model’s performance and guidance on how to use it. Our goal is to contribute practical insight to the community on building smaller, efficient multimodal reasoning models and to share an open-weight model that is
[competitive](#evaluation)
with models of similar size at general vision-language tasks,
[excels](#evaluation)
at computer use, and excels on scientific and mathematical multimodal reasoning.

## A focus on smaller and faster vision–language models

Many popular vision-language models (VLMs) have trended towards growing in parameter count and, in particular, the number of tokens they consume and generate. This leads to increase in training and inference-time cost and latency, and impedes their usability for downstream deployment, especially in resource‑constrained or interactive settings.

A growing countertrend towards
[smaller
(opens in new tab)](https://arxiv.org/pdf/2409.17146)
models aims to boost efficiency, enabled by careful model design and data curation – a goal pioneered by the
[Phi family of models
(opens in new tab)](https://azure.microsoft.com/en-us/products/phi)
and furthered by Phi-4-reasoning-vision-15B. We specifically build on learnings from the
[Phi-4](https://www.microsoft.com/en-us/research/publication/phi-4-technical-report/)
and
[Phi-4-Reasoning](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/)
language models and show how a multimodal model can be trained to cover a wide range of vision and language tasks without relying on extremely large training datasets, architectures, or excessive inference‑time token generation. Our model is intended to be lightweight enough to run on modest hardware while remaining capable of structured reasoning when it is beneficial. Our model was trained with far less compute than many recent open-weight VLMs of similar size. We used just 200 billion tokens of multimodal data leveraging Phi-4-reasoning (trained with 16 billion tokens) based on a core model Phi-4 (400 billion unique tokens), compared to more than 1 trillion tokens used for training multimodal models like Qwen
[2.5 VL
(opens in new tab)](https://arxiv.org/abs/2502.13923)
and
[3 VL
(opens in new tab)](https://arxiv.org/pdf/2511.21631)
,
[Kimi-VL
(opens in new tab)](https://arxiv.org/abs/2504.07491)
, and
[Gemma3
(opens in new tab)](https://arxiv.org/pdf/2503.19786)
. We can therefore present a compelling option compared to existing models pushing the pareto-frontier of the tradeoff between accuracy and compute costs.

*Figure 2: Phi-4-Reasoning-Vision can help with a wide range of everyday tasks.*

## Lessons from training a multimodal model

Training a multimodal reasoning model raises numerous questions and requires many nuanced design choices around model architecture, dataset quality and composition, and the interaction between reasoning‑heavy and non-reasoning perception‑focused tasks.

### Model architecture: Early- vs mid-fusion

Model architectures for VLMs differ primarily in how visual and textual information is fused. Mid-fusion models use a pretrained vision encoder to convert images into visual tokens that are projected into a pretrained LLM’s embedding space, enabling cross-modal reasoning while leveraging components already trained on trillions of tokens. Early-fusion models process image patches and text tokens in a single model transformer, yielding richer joint representations but at significantly higher compute, memory, and data cost. We adopted a mid-fusion architecture as it offers a practical trade-off for building a performant model with modest resources.

### Model architecture: Vision encoder and image processing

We build on the
[SigLIP-2
(opens in new tab)](https://arxiv.org/pdf/2502.14786)
vision encoder and the
[Phi-4-Reasoning](https://www.microsoft.com/en-us/research/publication/phi-4-reasoning-technical-report/)
backbone. In previous research, we found that multimodal language models sometimes struggled to solve tasks, not because of a lack of reasoning proficiency, but rather an
[inability to extract and select relevant perceptual information](https://www.microsoft.com/en-us/research/publication/eureka-evaluating-and-understanding-large-foundation-models/)
from the image. An example would be a high-resolution screenshot that is information-dense with relatively small interactive elements.

Several open-source multimodal language models have adapted their methodologies accordingly, e.g.,
[Gemma3
(opens in new tab)](https://arxiv.org/pdf/2503.19786)
uses pan-and-scan and
[NVILA
(opens in new tab)](https://arxiv.org/pdf/2412.04468)
uses Dynamic S2. However, their trade-offs are difficult to understand across different datasets and hyperparameters. To this end, we conducted an ablation study of several techniques. We trained a smaller 5 billion parameter Phi-4 based proxy model on a dataset of 10 million image-text pairs, primarily composed of computer-use and GUI grounding data. We compared with Dynamic S2, which resizes images to a rectangular resolution that minimizes distortion while admitting a tiling by 384×384 squares; Multi-crop, which splits the image into potentially overlapping 384×384 squares and concatenates their encoded features on the token dimension; Multi-crop with S2, which broadens the receptive field by cropping into 1536×1536 squares before applying S2; and Dynamic resolution using the Naflex variant of SigLIP-2, a natively dynamic-resolution encoder with adjustable patch counts.

Our primary finding is that dynamic resolution vision encoders perform the best and especially well on high-resolution data. It is particularly interesting to compare dynamic resolution with 2048 vs 3600 maximum tokens: the latter roughly corresponds to native HD 720p resolution and enjoys a substantial boost on high-resolution benchmarks, particularly ScreenSpot-Pro. Reinforcing the high-resolution trend, we find that multi-crop with S2 outperforms standard multi-crop despite using fewer visual tokens (i.e., fewer crops overall). The dynamic resolution technique produces the most tokens on average; due to their tiling subroutine, S2-based methods are constrained by the original image resolution and often only use about half the maximum tokens. From these experiments we choose the SigLIP-2 Naflex variant as our vision encoder.

| Method | Max Tokens | MathVista | ScreenSpot | ScreenSpot-Pro | V\*Bench |
| --- | --- | --- | --- | --- | --- |
| **Dynamic-S 2** | 3096 | 42.9 | 78.4 | 9.4 | 52.9 |
| **Multi-crop** | 3096 | 43.4 | 67.8 | 5.4 | 51.8 |
| **Multi-crop with S 2** | 2048 | 43.4 | 79.1 | **10.6** | **57.1** |
| **Dynamic resolution** | 2048 | **45.2** | **81.5** | 9.2 | 51.3 |
| **Dynamic resolution** | 3600 | **44.9** | **79.7** | **17.5** | **56.0** |

*Table 1: Results with different resolution handling approaches. The top two configurations on each benchmark are in bold.*

### Data: Quality and composition

As with its language backbone Phi-4-Reasoning, Phi-4-reasoning-vision-15B was trained with a deliberate focus on data quality. Our final dataset consists primarily of data from three sources: open-source datasets which were meticulously filtered and improved; high-quality domain-specific internal data; and high-quality data from targeted acquisitions. The overwhelming majority of our data lies in the first category: data which originated as open-source data, which were significantly filtered and improved, whether by removing low-quality datasets or records, programmatically fixing errors in data formatting, or using open-source images as seeds to synthetically generate higher-quality accompanying text.

The process of improving open-source data began by manually reviewing samples from each dataset. Typically, 5 to 10 minutes were sufficient to classify data as excellent-quality, good questions with wrong answers, low-quality questions or images, or high-quality with formatting errors. Excellent data was kept largely unchanged. For data with incorrect answers or poor-quality captions, we re-generated responses using GPT-4o and o4-mini, excluding datasets where error rates remained too high. Low-quality questions proved difficult to salvage, but when the images themselves were high quality, we repurposed them as seeds for new caption or visual question answering (VQA) data. Datasets with fundamentally flawed images were excluded entirely. We also fixed a surprisingly large number of formatting and logical errors across widely used open-source datasets.

We extracted additional value from existing datasets through reformatting, diversification, and using images as seeds for new data generation. We generated detailed image descriptions alongside original QA pairs for math and science data, had data perform “double-duty” by embedding instruction-following requirements directly into domain-specific QA, created “scrambled,” “caption-matching,” and “what’s changed?” records to improve multi-image reasoning and sequential navigation for CUA scenarios, and diversifying prompt styles to encourage robustness beyond perfectly structured questions.

To supplement the improved open-source data, we utilize high-quality internal datasets, several math-specific datasets which were acquired during training of the Phi-4 language model, and also some domain-specific curated data; for example, latex-OCR data generated by processing and rendering equations from arXiv documents.

![Top: A pie chart titled ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/phi4mm_data_AH.png)
before returning a bounding box coordinates for a UI grounding task, and the other uses a
tag with step-by-step reasoning to answer a chart question about expatriate populations, concluding with "Dubai." " class="wp-image-1163336"/>

*Figure 3: Phi-4-reasoning-vision-15B training data composition and examples*

### Data: Mathematics vs. computer-use data proportion

One of our goals was to train a model that performs well across general vision-language tasks, while excelling at mathematical and scientific reasoning and computer-use scenarios. How to structure datasets for generalizable reasoning remains an open question—particularly because the relationship between data scale and reasoning performance can lead to starkly different design decisions, such as training a single model on a large dataset versus multiple specialized models with targeted post-training.

Research on long-tailed classification robustness has suggested that
[balancing or removing data from overrepresented tasks or subgroups
(opens in new tab)](https://arxiv.org/pdf/1710.05381)
is an effective method for ensuring good performance. Nevertheless, these insights are not fully utilized or explored when it comes to training VLMs, which at times have favored scale over careful data balancing. To achieve our goals, we conducted a set of experiments to analyze a range of data ratios between our focus domains.

Using the same 5 billion parameter proxy model as for previous experiments, we trained while varying the amount of mathematics and science vs. computer-use data for each run. Each dataset included the same subset of 1 million general image-text pairs as a baseline. For mathematics and science data, we used a subsample of 150,000 records, optionally duplicating each one up to three times. Next, we included up to 450,000 computer-use records, and optionally an additional 400,000 from
[Phi-Ground](https://www.microsoft.com/en-us/research/publication/phi-ground-tech-report-advancing-perception-in-gui-grounding/)
.

We found that that multimodal mathematics and science performance were not harmed by additional computer-use data, and vice versa. Interestingly, we found that increasing mathematics data by 3x while keeping computer-use data constant improved math, science, and computer-use benchmarks.

| General | Math and Science | CUA | Total | MMMU | MathVista | ScreenSpot-V2 |
| --- | --- | --- | --- | --- | --- | --- |
| 1M | 150K | 450K | 1.6M | 44.0 | 37.4 | 48.2 |
| 1M | 150K | 850K | 2.0M | 44.1 | 37.3 | 60.0 |
| 1M | 450K | 450K | 1.9M | **45.3** | 36.0 | 48.3 |
| 1M | 450K | 850K | 2.3M | 43.4 | **38.9** | **63.1** |
| 1M | 150K | 150K | 1.3M | 44.2 | 36.9 | 29.8 |
| 1M | 150K | 250K | 1.4M | **45.4** | 37.4 | 37.7 |

*Table 2: Varying the ratios of math and CUA data. Increasing math data by 3x while keeping computer-use data constant improves both math and computer-use benchmarks.*

### Data: Synthetic data for text-rich visual reasoning

[Recent work
(opens in new tab)](https://arxiv.org/pdf/2502.14846)
suggests that targeted synthetic data can materially improve multimodal reasoning, particularly for text-rich visual domains such as charts, documents, diagrams, and rendered mathematics. Using images, questions, and answers that are programmatically generated and grounded in the visual structure enables precise control over visual content and supervision quality, resulting in data that avoids many annotation errors, ambiguities, and distributional biases common in scraped datasets. This enables cleaner alignment between visual perception and multi-step inference, which has been shown to translate into measurable gains on reasoning-heavy benchmarks.

Synthetic text-rich images expand coverage of long-tail visual formats that are underrepresented in real data but disproportionately impact reasoning accuracy, improving not only visual grounding but also downstream reasoning by ensuring that failures are less often caused by perceptual errors. We found that programmatically generated synthetic data is a useful augmentation to high-quality real datasets — not a replacement, but a scalable mechanism for strengthening both perception and reasoning that complements the training objectives in compact multimodal models such as Phi-4-reasoning-vision-15B.

## Mixing non-reasoning and reasoning as a design objective

In language-only settings, reasoning traces have improved performance on many tasks, but they require additional compute which adds undesired latency. In multimodal settings, this tradeoff is less clear-cut, for tasks such as image captioning and optical character recognition (OCR), reasoning is often unnecessary and can even be
[harmful
(opens in new tab)](https://arxiv.org/pdf/2502.09621)
, while mathematical and scientific problem-solving benefit from multi-step reasoning. Thus, the choice of when to reason or not can be quite nuanced.

### Training approaches for multimodal reasoning models

Language-only reasoning models are typically created through supervised fine-tuning (SFT) or reinforcement learning (RL): SFT is simpler but requires large amounts of expensive reasoning trace data, while RL reduces data requirements at the cost of significantly increased training complexity and compute. Multimodal reasoning models follow a similar process, but the design space is more complex. With a mid-fusion architecture, the first decision is whether the base language model is itself a reasoning or non-reasoning model. This leads to several possible training pipelines:

* **Non-reasoning LLM → reasoning multimodal training:**
  Reasoning and multimodal capabilities are trained together.
* **Non-reasoning LLM → non-reasoning multimodal → reasoning multimodal training:**
  Multimodal capabilities are learned first, then reasoning is added.
* **Reasoning LLM → reasoning multimodal training:**
  A reasoning base is used, but all multimodal data must include reasoning traces.
* **Our approach: Reasoning LLM → mixed non-reasoning / reasoning multimodal training.**
  A reasoning-capable base is trained on a hybrid data mixture, learning when to reason and when to respond directly.

Approaches 1 and 2 offer flexibility in designing multimodal reasoning behavior from scratch using widely available non-reasoning LLM checkpoints but place a heavy burden on multimodal training. Approach 1 must teach visual understanding and reasoning simultaneously and requires a large amount of multimodal reasoning data, while Approach 2 can be trained with less reasoning data but risks catastrophic forgetting, as reasoning training may degrade previously learned visual capabilities. Both risk weaker reasoning than starting from a reasoning-capable base. Approach 3 inherits strong reasoning foundations, but like Approach 1, it requires reasoning traces for all training data and produces reasoning traces for all queries, even when not beneficial.

### Our approach: A mixed reasoning and non-reasoning model

Phi-4-reasoning-vision-15B adopts the 4th approach listed previously, as it balances reasoning capability, inference efficiency, and data requirements. It inherits a strong reasoning foundation but uses a hybrid approach to combine the strengths of alternatives while mitigating their drawbacks. Our model defaults to direct inference for perception-focused domains where reasoning adds latency without improving accuracy, avoiding unnecessary verbosity and reducing inference costs, and it invokes longer reasoning paths for domains, such as
[math and science, that benefit from structured multi-step reasoning
(opens in new tab)](https://arxiv.org/pdf/2409.12183)
.

Our model is trained with SFT, where reasoning samples include “…” sections with chain-of-thought reasoning before the final answer, covering domains like math and science. Non-reasoning samples are tagged to start with a “” token, signaling a direct response, and cover perception-focused tasks such as captioning, grounding, OCR, and simple VQA. Reasoning data comprises approximately 20% of the total mix. Starting from a reasoning-capable backbone means this data grounds existing reasoning in visual contexts rather than teaching it to reason from scratch.

This approach is not without limitations. The balance between modes is a direct function of design choices we made, informed by
[recent literature
(opens in new tab)](https://arxiv.org/pdf/2502.09621)
and observed model behavior during training—though the boundary between modes can be imprecise as it is learned implicitly from the data distribution. Our model allows control through explicit prompting with “” or “” tokens when the user wants to override the default reasoning behavior. The 20/80 reasoning-to-non-reasoning data split may not be optimal for all domains or deployment contexts. Evaluating the ideal balance of data and the model’s ability to switch appropriately between modes remains an open problem.

We view this mixed approach not as a definitive solution, but as one practical and well-motivated point in the design space for balancing latency, accuracy, and flexibility in multimodal systems.

## Applications

![A multi-image reasoning example — five Hubble photos of Saturn from 2018–2022, with the query ](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/saturn-scaled.png)


*Figure 4: Phi-4-Reasoning-Vision can interpret sequences of images*

Phi-4-reasoning-vision-15B is a high-performing model across many vision-language tasks. It sees and understands the world by looking at a photo, document, chart, or screen and making sense of it. In practice that covers an enormous range of applications — just a few examples include: describing images and answering questions about them, interpreting changes and trends in images sequences, and recognizing objects, landmarks, and transcribing text.

## Highlights: Scientific and mathematical reasoning and supporting computer-using agents (CUA)

In addition to general vision and language tasks, Phi-4-reasoning-vision-15B was designed to excel at tasks that combine visual input with structured inference, such as solving math problems presented in visual form, such as handwritten or diagram-based questions, extracting and reasoning over quantitative information in documents and charts, and supporting multi-step reasoning in educational or scientific analysis contexts.

![A physics problem about spring-mass systems, with two diagrams. The model correctly works through the spring constant relationships and arrives at answer B (0.433s).](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/math-scaled.png)


*Figure 5: Phi-4-reasoning-vision-15B is great at math and science*


![A handwritten math homework checker. The student made a sign error in the quadratic formula (wrote −8 instead of +8). The model's thinking process catches the error and provides the corrected solution (x = 5 and x = 3).](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/03/math_homework_best-scaled.png)


*Figure 6: Phi-4-reasoning-vision-15B can help with written math problems*

In addition, we trained Phi-4-reasoning-vision-15B to have skills that can enable agents to interact with graphical user interfaces by interpreting screen content and selecting actions. With strong high-resolution perception and fine-grained grounding capabilities, Phi-4-reasoning-vision-15B is a compelling option as a base-model for training agentic models such as ones that navigate desktop, web, and mobile interfaces by identifying and localizing interactive elements such as buttons, menus, and text fields. Due to its low inference-time needs it is great for interactive environments where low latency and compact model size are essential.

*Figure 7: Phi-4-reasoning-vision-15B can help navigate computer UIs*

## Evaluation

Phi-4-reasoning-vision-15B was evaluated for accuracy and timing using two complementary open-source frameworks to ensure both rigorous and standardized analysis:
**[Eureka ML Insights
(opens in new tab)](https://github.com/microsoft/eureka-ml-insights)**
and
**[VLMEvalKit
(opens in new tab)](https://github.com/open-compass/VLMEvalKit)**
.

| Benchmark | Phi-4-reasoning-vision-15B | Phi-4-reasoning-vision-15B – force nothink | Phi-4-mm-instruct | Kimi-VL-A3B-Instruct | gemma-3-12b-it | Qwen3-VL-8B-Instruct-4K | Qwen3-VL-8B-Instruct-32K | Qwen3-VL-32B-Instruct-4K | Qwen3-VL-32B-Instruct-32K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **AI2D** ***\_TEST*** | 84.8 | 84.7 | 68.6 | 84.6 | 80.4 | 82.7 | 83 | 84.8 | 85 |
| **ChartQA** **\_TEST** | 83.3 | 76.5 | 23.5 | 87 | 39 | 83.1 | 83.2 | 84.3 | 84 |
| **HallusionBench** | 64.4 | 63.1 | 56 | 65.2 | 65.3 | 73.5 | 74.1 | 74.4 | 74.9 |
| **MathVerse** **\_MINI** | 44.9 | 43.8 | 32.4 | 41.7 | 29.8 | 54.5 | 57.4 | 64.2 | 64.2 |
| **MathVision** **\_MINI** | 36.2 | 34.2 | 20 | 28.3 | 31.9 | 45.7 | 50 | 54.3 | 60.5 |
| **MathVista** **\_MINI** | 75.2 | 68.7 | 50.5 | 67.1 | 57.4 | 77.1 | 76.4 | 82.5 | 81.8 |
| **MMMU** **\_VAL** | 54.3 | 52 | 42.3 | 52 | 50 | 60.7 | 64.6 | 68.6 | 70.6 |
| **MMStar** | 64.5 | 63.3 | 45.9 | 60 | 59.4 | 68.9 | 69.9 | 73.7 | 74.3 |
| **OCRBench** | 76 | 75.6 | 62.6 | 86.5 | 75.3 | 89.2 | 90 | 88.5 | 88.5 |
| **ScreenSpot** **\_v2** | 88.2 | 88.3 | 28.5 | 89.8 | 3.5 | 91.5 | 91.5 | 93.7 | 93.9 |

*Table 3: Accuracy comparisons relative to popular open-weight, non-thinking models*



| Benchmark | Phi-4-reasoning-vision-15B | Phi-4-reasoning-vision-15B – force thinking | Kimi-VL-A3B-Thinking | gemma-3-12b-it | Qwen3-VL-8B-Thinking-4K | Qwen3-VL-8B-Thinking-40K | Qwen3-VL-32B-Thiking-4K | Qwen3-VL-32B-Thinking-40K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **AI2D\_TEST** | 84.8 | 79.7 | 81.2 | 80.4 | 83.5 | 83.9 | 86.9 | 87.2 |
| **ChartQA** **\_TEST** | 83.3 | 82.9 | 73.3 | 39 | 78 | 78.6 | 78.5 | 79.1 |
| **HallusionBench** | 64.4 | 63.9 | 70.6 | 65.3 | 71.6 | 73 | 76.4 | 76.6 |
| **MathVerse** **\_MINI** | 44.9 | 53.1 | 61 | 29.8 | 67.3 | 73.3 | 78.3 | 78.2 |
| **MathVision** **\_MINI** | 36.2 | 36.2 | 50.3 | 31.9 | 43.1 | 50.7 | 60.9 | 58.6 |
| **MathVista** **\_MINI** | 75.2 | 74.1 | 78.6 | 57.4 | 77.7 | 79.5 | 83.9 | 83.8 |
| **MMMU** **\_VAL** | 54.3 | 55 | 60.2 | 50 | 59.3 | 65.3 | 72 | 72.2 |
| **MMStar** | 64.5 | 63.9 | 69.6 | 59.4 | 69.3 | 72.3 | 75.5 | 75.7 |
| **OCRBench** | 76 | 73.7 | 79.9 | 75.3 | 81.2 | 82 | 83.7 | 85 |
| **ScreenSpot** **\_v2** | 88.2 | 88.1 | 81.8 | 3.5 | 93.3 | 92.7 | 83.1 | 83.1 |

*Table 4: Accuracy comparisons relative to popular open-weight, thinking models*

Our model balances thinking and non-thinking performance – on average showing better accuracy in the default “mixed-reasoning” behavior than when forcing thinking vs. non-thinking. Only in a few cases does forcing a specific mode improve performance (MathVerse and MMU\_val for thinking and ScreenSpot\_v2 for non-thinking). Compared to recent popular, open-weight models, our model provides a desirable trade-off between accuracy and cost (as a function of inference time compute and output tokens), as discussed previously.

Note: All numbers here are the result of running benchmarks ourselves and may be lower than other previously shared numbers. Instead of quoting leaderboards, we performed our own benchmarking, so we could understand scaling performance as a function of output token counts for related models. We made our best effort to run fair evaluations and used recommended evaluation platforms with model-specific recommended settings and prompts provided for all third-party models. For Qwen models we use the recommended token counts and also ran evaluations matching our max output token count of 4096. For Phi-4-reasoning-vision-15B, we used our system prompt and chat template but did not do any custom user-prompting or parameter tuning, and we ran all evaluations with temperature=0.0, greedy decoding, and 4096 max output tokens. These numbers are provided for comparison and analysis rather than as leaderboard claims. For maximum transparency and fairness, we will release all our evaluation logs publicly. For more details on our evaluation methodology, please see our
[technical report
(opens in new tab)](https://aka.ms/Phi-4-reasoning-vision-15B-TR)
.

## Safety

As with other Phi models, Phi-4-reasoning-vision-15B was developed with safety as a core consideration throughout training and evaluation. The model was trained on a mixture of public safety datasets and internally generated examples designed to elicit behaviors the model should appropriately refuse, in alignment with Microsoft’s Responsible AI Principles. For further details, check out our
[technical report
(opens in new tab)](https://aka.ms/Phi-4-reasoning-vision-15B-TR)
.

## Open release and community engagement

Phi-4-reasoning-vision-15B is available on
[Microsoft Foundry
(opens in new tab)](https://aka.ms/Phi-4-r-v-foundry)
and
[HuggingFace
(opens in new tab)](https://huggingface.co/microsoft/Phi-4-vision-reasoning-15B)
with additional examples and details on
[GitHub
(opens in new tab)](https://github.com/microsoft/Phi-4-vision)
. For additional guidance on how to use our model properly and safely, please refer to our
[Model card
(opens in new tab)](https://huggingface.co/microsoft/Phi-4-reasoning-vision-15B)
. For further details on the technical aspects of the model, training, and evaluation, see our
[technical report
(opens in new tab)](https://aka.ms/Phi-4-reasoning-vision-15B-TR)
.

In line with our goal of supporting future AI development in the community, Phi-4-reasoning-vision-15B is released under a permissive license with model weights, fine‑tuning code, and benchmark logs. We intend this release to complement existing work by providing concrete artifacts that help close gaps in understanding how compact multimodal reasoning models can be built and studied.

## Looking forward

Smaller vision–language models with selective, task‑aware reasoning offer one promising direction for making multimodal systems more practical and accessible. We present our model and its learnings to inform ongoing research in multimodal modeling, computer‑using agents, and mathematical scientific reasoning. We hope these details are useful to researchers exploring similar tradeoffs and invite critical evaluation, replication, and extension by the community. If you’d like to join us and help shape the future of multimodal models, please apply for one of our
[open roles](https://www.microsoft.com/en-us/research/lab/ai-frontiers/opportunities/)
.

## Acknowledgements

We thank Rachel Ward for her extensive work on data collection and curation. We thank the GenDatasets, PhiGround, SimCity, and Fara-7B efforts for invaluable training data. We thank Harkirat Behl, Mojan Javaheripi, and Suriya Gunasekar for providing us with Phi-4 checkpoints and guidance on training with Phi models. We additionally thank Sahaj Agarwal, Ahmed Awadallah, Qi Dai, Gustavo de Rosa, Rafah Hosn, Ece Kamar, Piero Kauffmann, Yash Lara, Chong Luo, Caio César Teodoro Mendes, Akshay Nambi, Craig Presti, Matthew Rosoff, Corby Rosset, Marco Rossi, Kashyap Patel, Adil Salim, Sidhartha Sen, Shital Shah, Pratyusha Sharma, Alexey Taymanov, Vibhav Vineet, John Weiss, Spencer Whitehead, the AI Frontiers Team and Leadership, and Microsoft Research Leadership, for their valuable help, insightful discussions, and continued support throughout this work.

Opens in a new tab