---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-10T20:42:42.565844+00:00'
exported_at: '2026-03-10T20:42:44.822580+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/open-data-for-ai
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: How NVIDIA Builds Open Data for AI
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/open-data-for-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How NVIDIA Builds Open Data for AI
updated_at: '2026-03-10T20:42:42.565844+00:00'
url_hash: 087b7ac98b372690e64b6f7e768878a7523941a7
---

# How NVIDIA Builds Open Data for AI

*A collaborative approach to scaling trustworthy AI systems and agents.*

AI progress is often framed in terms of model capability and efficiency. In reality, every training pipeline ultimately rests on a data layer that determines how those models behave.

As agentic systems become more autonomous, the data they are trained on increasingly determines what they know, how they reason, and what they can safely do. Yet much of today’s training data remains opaque, fragmented, or siloed across teams.

Open data access changes that equation. It gives developers a faster and more cost-effective path to building high-quality models, while making evaluation and improvement easier across the ecosystem. This is why NVIDIA releases open datasets alongside its open models, tools, and training techniques.

## AI-Data Bottlenecks

Building high-quality datasets remains one of the largest bottlenecks in AI development. Organizations often spend
[millions of dollars](https://www.beren.io/2025-08-02-Most-Algorithmic-Progress-is-Data-Progress/)
and months—or even
[more than a year](https://www.presspublications.com/premium/stacker/stories/why-95-of-enterprise-ai-projects-fail-to-deliver-roi-a-data-analysis,84940?#:~:text=The%20Data%20Quality%20Crisis%20Nobody,understanding%20across%20multiple%20incomplete%20profiles.)
—collecting, annotating, and validating data before a single model training run begins. Even when models are deployed, access to
[domain expertise](https://gradientflow.com/data-annotation-synthetic-data/)
and
[evaluation frameworks](https://www.gov.uk/government/publications/international-scientific-report-on-the-safety-of-advanced-ai)
remains an evergreen challenge.

NVIDIA aims to reduce this friction by publishing permissively licensed datasets on
[HuggingFace](https://huggingface.co/nvidia/datasets)
with training recipes and evaluation frameworks on
[GitHub](https://github.com/NVIDIA-NeMo/Nemotron)
that developers can build on immediately. To date, we’ve shared more than 2 petabytes of AI-ready training data across more than 180 datasets and 650+ open models. And we’re just getting started.

## Real-World Open Datasets

NVIDIA’s open data releases span multiple domains — from robotics and autonomous systems to sovereign AI, biology, and evaluation benchmarks. Built by teams across NVIDIA, these datasets demonstrate how shared data can accelerate real-world AI development.

Here are a few examples from across our ecosystem:

#### Physical AI Collection

Robotics systems require structured, multimodal data. This
[collection](https://huggingface.co/collections/nvidia/physical-ai)
includes 500K+ robotics trajectories, 57M grasps, and 15TB of multimodal data, including assets used to develop the NVIDIA GR00T reasoning vision-language-action model across multiple gripper types and sensor configurations. The dataset has been downloaded more than 10 million times, including by companies such as Runway, which developed its recently released GWM-Robotics world model using the open GR00T dataset, and robotics simulation company Lightwheel, which is using the dataset to refine robotics policies.

This collection also includes
[one of the most geographically diverse AV datasets available](https://huggingface.co/datasets/nvidia/PhysicalAI-Autonomous-Vehicles)
, with more than 1,700 hours of multi-sensor data that includes 7-camera configurations plus LiDAR and radar spanning 25 countries and over 2,500 cities. That breadth supports perception benchmarking across varied driving environments and complements academic datasets with broader commercial usability.

#### Nemotron Personas Collection

[Nemotron Personas](https://huggingface.co/collections/nvidia/nemotron-personas)
are fully synthetic persona datasets grounded in real-world demographic distributions, producing culturally authentic, diverse individuals across regions and languages at scale.

The collection supports Sovereign AI development and currently includes population-scale datasets for:

* **United States**
  – 6M personas
* **Japan**
  – 6M personas
* **India**
  – 21M personas
* **Brazil**
  – 6M personas (developed with
  [WideLabs](https://valor.globo.com/empresas/noticia/2026/01/26/nvidia-e-widelabs-lancam-personas-de-ia-que-refletem-a-populacao-brasileira.ghtml)
  )
* **Singapore**
  – 888K personas (developed with
  [AI Singapore](https://www.computerweekly.com/news/366637940/Nvidia-releases-synthetic-dataset-to-support-Singapores-AI-ambitions)
  )

These datasets are already powering real deployments globally.
[CrowdStrike](https://www.crowdstrike.com/en-us/blog/crowdstrike-journey-in-customizing-nvidia-nemotron-models/)
used 2M personas to improve NL→CQL translation accuracy from 50.7% to 90.4%. In Japan,
[NTT Data](https://huggingface.co/blog/nvidia/nemotron-personas-japan-nttdata)
and
[APTO](https://www.nvidia.com/ja-jp/case-studies/apto-improves-ai-data-quality/)
used the datasets to bootstrap domain-specific intelligence with minimal proprietary data, improving legal QA accuracy from 15.3% to 79.3% and reducing attack success rates from 7% to 0%.

The datasets also supported the development of
[NVIDIA Nemotron-Nano-9B-v2-Japanese](https://huggingface.co/blog/nvidia/nemotron-nano-9b-v2-japanese-ja)
, a state-of-the-art sub-10B model that reached the top of the
[Nejumi leaderboard](https://nejumi.ai/)
.

#### La Proteina

[La Proteina](https://github.com/NVIDIA-Digital-Bio/la-proteina)
is a fully synthetic, atomistic protein dataset designed for biological modeling and drug discovery workflows. With 455,000 structures and a state-of-the-art 73% structural diversity boost over prior baselines, it provides design-ready molecular representations without PII or licensing constraints. A scientific achievement made possible by an open collaboration with researchers from Oxford, Mila, and CIFAR.

#### SPEED-Bench

[SPEED-Bench](https://huggingface.co/datasets/nvidia/SPEED-Bench)
is a standardized benchmark for evaluating speculative decoding performance. It features two splits: a Qualitative Split that maximizes semantic diversity across 11 text categories, and a Throughput Split organized into input sequence length buckets (1K–32K) for constructing accurate throughput Pareto curves using real semantic data rather than random tokens. Already adopted internally as the primary benchmark for Nemotron MTP performance, SPEED-Bench gives teams a consistent methodology for evaluating draft performance across prompt complexities and context lengths.

#### Retrieval-Synthetic-NVDocs-v1

This
[synthetic retrieval dataset](https://huggingface.co/datasets/nvidia/Retrieval-Synthetic-NVDocs-v1)
provides 110,000 triplets of query, passage, and answer generated from 15,000 files of NVIDIA public documentation. Designed to train and evaluate embedding and RAG systems, the dataset features semantically rich QA pairs spanning multiple reasoning types—factual, relational, procedural, inferential, temporal, causal, and visual—alongside diverse query types including structural, multi-hop, and contextual queries. In-domain fine-tuning of embedding models demonstrates substantial gains: fine-tuning nvidia/llama-nemotron-embed-1b-v2 on this dataset yields an 11% increase in NDCG@10. The dataset can be generated in roughly 3–4 days, and fine-tuning takes about two hours on 8×A100 GPUs—enabling rapid iteration from dataset to deployed model.

#### Nemotron-ClimbMix

[ClimbMix](https://huggingface.co/datasets/nvidia/Nemotron-ClimbMix)
is a 400B-token pre-training dataset built using the CLIMB algorithm, which uses embedding-based clustering and iterative refinement to identify higher-quality data mixtures for language model training. The dataset has already gained strong community traction:
[Andrej Karpathy highlighted Nemotron-ClimbMix](https://x.com/karpathy/status/2029701092347630069)
as delivering the largest improvement on the
[Time-to-GPT-2 leaderboard](https://github.com/karpathy/nanochat?tab=readme-ov-file#time-to-gpt-2-leaderboard)
, leading to its adoption as the default data recipe in NanoChat Speedrun and reducing H100 compute time by roughly 33% compared to the previous FineWeb-Edu setup. ClimbMix is released under the CC-BY-NC-4.0 license.

These releases reflect an ongoing investment in the shared reference layer that AI developers depend on across modalities and model lifecycle stages.

## Nemotron Training Datasets

One major component of NVIDIA’s open data work is the set of datasets used to train and align the
[Nemotron model family](https://developer.nvidia.com/nemotron)
. Over the past year these datasets have evolved to better support reasoning, coding, and multilingual capabilities in frontier language models.

#### Nemotron Pre-Training Evolution

![](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/Q5O7Sn54ChoEF6-e3VxP4.png)
*Nemotron-Pre-Training Evolution Chart*

Earlier releases relied heavily on general web corpora, while newer releases emphasize higher-signal domains such as math, code, and STEM knowledge. This increased signal density enables models to learn stronger reasoning and problem-solving capabilities.

The
[Nemotron pre-training stack](https://huggingface.co/collections/nvidia/nemotron-pre-training-datasets)
includes several curated datasets designed for different capabilities:

* **Nemotron-CC**
  – globally deduplicated web data rewritten for higher signal density
* **Nemotron-CC-Math**
  and
  **Nemotron-CC-Code**
  – math and code reasoning preserving LaTeX and code formatting
* **Nemotron-Pretraining-Code**
  – curated programming datasets from large code repositories
* **Nemotron-Pretraining-Specialized**
  – synthetic datasets to boost capabilities in key domains like algorithms, economics, logic, STEM reasoning

Together, these datasets form the foundation for general-purpose language models capable of reasoning, coding, and multilingual understanding. They power Nemotron as well as partner frontier models like the AI security company
[Trend Micro’s Primus-Labor-70B](https://www.trendmicro.com/vinfo/us/security/news/managed-detection-and-response/llm-as-a-judge-evaluating-accuracy-in-llm-security-scans)
.

#### Nemotron-Post-Training Evolution

![](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/mXD4sltJq-dq2SGvNX0f-.png)
*Nemotron Post-Training Evolution Chart*

As models become more capable, post-training data plays a larger role in shaping model behavior. Newer releases emphasize multilingual diversity, structured reasoning supervision, and agent-style interaction data.

Key datasets in the
[Nemotron post-training stack](https://huggingface.co/collections/nvidia/nemotron-post-training-v3)
include:

* **Nemotron-Instruction-Following-Chat**
  – structured conversational supervision
* **Nemotron-Science**
  – synthetic science reasoning datasets
* **Nemotron-Math-Proofs**
  – formal mathematical reasoning datasets
* **Nemotron-Agentic**
  – datasets supporting multi-step planning and tool use
* **Nemotron-SWE**
  – instruction tuning datasets for software engineering tasks

These datasets provide structured supervision that helps models follow complex instructions, generate reasoning traces, and perform reliably in multi-step tasks. Early iterations were blended with domain data to develop
[ServiceNow's Apriel Nemotron 15B / Apriel 1.6 Thinker](https://newsroom.servicenow.com/press-releases/details/2025/ServiceNow-and-NVIDIA-Fuel-a-New-Class-of-Intelligent-AI-Agents-Across-the-Enterprise/default.aspx)
, which surpassed Gemini 2.5 Flash and Qwen3 at the 15B parameter scale, and
[Hugging Face's SmolLM3](https://huggingface.co/blog/smollm3)
, a popular small language model.

NVIDIA is also expanding this work with open safety and reinforcement learning datasets, including
[Nemotron-Agentic-Safety](https://huggingface.co/datasets/nvidia/Nemotron-AIQ-Agentic-Safety-Dataset-1.0)
(11K labeled telemetry traces from tool-use workflows) and
[Nemotron-RL](https://huggingface.co/collections/nvidia/nemo-gym)
, a 900K-task corpus spanning math, coding, tools, puzzles, and reasoning that gives models a true training “gym.”

## Extreme Co-Design

Designing high-quality datasets at this scale is a team sport. It requires close collaboration between data strategists, AI researchers, infrastructure engineers, and policy experts.

At NVIDIA, we approach data the same way we do any software and hardware engineering problem, through what we call
[extreme co-design](https://newsletter.semianalysis.com/p/vera-rubin-extreme-co-design-an-evolution)
— designing all components together to eliminate bottlenecks at scale.

When possible, we release the datasets as well as the methods behind them. The open community and our partners then stress-tests them, surfaces edge cases, and extends the datasets into new domains. Those insights feed directly into the next iteration, improving both our internal systems and the broader AI ecosystem.
[![Screenshot 2026-03-10 at 11.23.40 AM](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/h6_SUdz4pAsQ6s-HQNPL9.png)](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/h6_SUdz4pAsQ6s-HQNPL9.png)

*CES 2026 Keynote*

NVIDIA also collaborates with partners through initiatives like the
[ViDoRe](https://huggingface.co/blog/QuentinJG/introducing-vidore-v3)
and
[CVDP](https://huggingface.co/datasets/nvidia/cvdp-benchmark-dataset)
, two consortia that bring together industry and academic partners to develop open benchmarks and evaluation frameworks for emerging AI systems.

## Start Cooking in the Open Kitchen

At NVIDIA, we think about open data much like an open kitchen. The ingredients are visible, the recipes are shared, and everyone can learn from how the dish is prepared.

We encourage anyone passionate about data science and model building to
[explore NVIDIA’s open datasets on Hugging Face](https://huggingface.co/nvidia/datasets)
,
[try our tutorials and Nemotron labs](https://github.com/NVIDIA-NeMo/Nemotron)
, and
[join the Nemotron community on Discord](https://discord.com/channels/1019361803752456192/1407781691698708682)
to collaborate on future datasets.

The next generation of trustworthy AI models and agentic systems will be built on shared foundations. Open data is one of them.