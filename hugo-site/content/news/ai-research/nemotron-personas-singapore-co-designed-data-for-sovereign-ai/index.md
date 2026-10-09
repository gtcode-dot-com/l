---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-28T00:15:26.050252+00:00'
exported_at: '2026-01-28T00:15:28.241777+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/nemotron-personas-singapore
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: 'Nemotron-Personas-Singapore: Co-Designed Data for Sovereign AI'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/nemotron-personas-singapore
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Nemotron-Personas-Singapore: Co-Designed Data for Sovereign AI'
updated_at: '2026-01-28T00:15:26.050252+00:00'
url_hash: 0d18997717a273c1a73d44093e78fc7c728a2661
---

# Nemotron-Personas-Singapore: Co-Designed Data for Sovereign AI

[![Sing](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/Ya-w2owKyVkHOsfSpoyBO.png)](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/Ya-w2owKyVkHOsfSpoyBO.png)
*A compound AI approach to personas grounded in real-world distributions*


---

## Open Data for Singapore AI

Singapore has established itself as a leader in building AI systems that are both innovative and responsibly governed. Through interoperable governance frameworks, applied privacy research, and
[clear guidance on synthetic data](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/other-guides/proposed-guide-on-synthetic-data-generation.pdf)
, the country has demonstrated that AI sovereignty is ultimately about trust, transparency, and alignment with local norms.

To support these efforts, NVIDIA is releasing
[**Nemotron-Personas-Singapore**](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Singapore)
, a first-of-its-kind synthetic dataset designed for Singaporean developers and researchers building sovereign AI systems. The dataset provides training and evaluation data that is locally grounded, culturally contextualized, and privacy-preserving.

We are co-launching this initial release with our partner
[**AI Singapore (AISG)**](https://aisingapore.org)
, a national programme launched by the National Research Foundation (NRF) to scale Singapore’s artificial intelligence capabilities. AISG is also the creator of
[**SEA-LION**](https://sea-lion.ai)
, an open, multimodal AI model family built to understand Southeast Asia’s languages, cultures, and contexts. Together, we plan to extend this dataset to additional languages across Southeast Asia.

Licensed under
**CC BY 4.0**
, Nemotron-Personas-Singapore supports both commercial and public-sector AI development without relying on personally identifiable information (PII). The dataset integrates seamlessly with
[Nemotron models](https://developer.nvidia.com/nemotron)
and other open-source LLMs, enabling developers to fine-tune AI agents and systems for Singapore-specific use cases.

Nemotron-Personas-Singapore extends
[NVIDIA’s open synthetic personas collection](https://huggingface.co/collections/nvidia/nemotron-personas)
, which includes datasets for the
**United States, Japan, India, and Brazil**
.

---

## What’s in the Dataset?

[![sing2](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/9Nfu8ECeFVGQOePiIYaJG.png)](https://cdn-uploads.huggingface.co/production/uploads/68d2fec8856b85d927e44d32/9Nfu8ECeFVGQOePiIYaJG.png)

### At a glance:

* 888,000 Singaporean personas (148,000 records × 6 personas each)
* ~118 million tokens total, including ~48 million persona tokens
* 38 fields per record: 7 persona fields + 31 contextual fields grounded in official statistics
* Full geographic coverage: all 55 planning areas
* 148k unique names (8,992 unique first names, 4,182 unique middle names, and 4,894 unique last names drawn from Singaporean name distributions
* Occupation categories reflecting Singapore’s workforce
* Multiple persona types including: professional, sports, arts, travel, among others.

---

## How We Built It

### Data Generation Pipeline

Nemotron-Personas-Singapore was built using
[NeMo Data Designer](https://docs.nvidia.com/nemo/microservices/latest/api/data-designer.html)
, NVIDIA’s enterprise-grade synthetic data generation microservice. The pipeline leveraged the following components:

* **Probabilistic Graphical Model (Apache-2.0)**
  for statistical grounding
* **GPT-OSS-120B (Apache-2.0)**
  for narrative generation

An extended version of Nemotron-Personas-Singapore will be available for use directly within NeMo Data Designer, enabling developers to generate, refine, and extend Singapore-specific personas as part of their own synthetic data pipelines.

---

### Enhanced Cultural Context

To capture the socio-demographic and geographic diversity of Singapore’s population, Nemotron-Personas-Singapore leveraged self-reported, public demographic data from the 2024 Singapore census, as well as English name distribution data from NLB Name Authorities and CEA Salesperson Information on data.gov.sg.

* **Education**
  : Introduces finer-grained education levels beyond census groupings, reflecting Singapore’s academic and vocational diversity and its impact on language and reasoning.
* **Occupation**
  : Reflects Singapore’s service-oriented workforce across key sectors, while avoiding reinforcement of sensitive socio-economic stereotypes in a multi-cultural context.
* **Life Stages**
  : Incorporates employment, retirement, and household composition to reflect changing priorities across adulthood (ages 15+).
* **Geography**
  : Aligns personas to planning-area–level distributions, capturing internal variation without relying on real address data.
* **Cultural Traits**
  : Represents Singapore’s multi-ethnic, multi-religious society through attributes such as ethnicity, religion, and language preference to reflect local norms.
* **Digital Familiarity**
  : Accounts for variation in digital literacy and technology use across age cohorts.
* **Policy Alignment**
  : Reflects Singapore’s AI governance framework, which emphasizes proportionality, risk-based controls, and evidence-driven oversight, particularly in regulated sectors.

---

### Private by Design

Every persona in the dataset is fully synthetic:

* No real individuals
* No personally identifiable information
* No re-identification risk

By grounding generation in public statistics rather than personal records, Nemotron-Personas-Singapore enables AI development and evaluation with reduced regulatory friction, supporting alignment with
[Singapore’s Personal Data Protection Act (PDPA)](https://sso.agc.gov.sg/Act/PDPA2012)
and emerging global AI governance standards.

---

## Who This Dataset Is For

Nemotron-Personas-Singapore is designed first and foremost for Singaporean model builders developing sovereign AI systems. Global developers may also leverage this data to improve model performance and adoption in Singapore’s diverse, cultural contexts.

---

## Practical AI Applications

* **Financial Services AI**
  – Persona-based evaluations support bias testing, suitability checks, and stress testing for vulnerable scenarios without reusing sensitive customer data.
* **Healthcare & Medical AI**
  – Synthetic personas enable safe evaluation of clinical assistants, patient-facing chatbots, and medical translation systems across patient demographics, literacy levels, and care contexts—without exposing real patient data.
* **Consumer Safety**
  – Synthetic personas enable testing for hallucinations, tone failures, and group-specific risk in public-facing AI systems.
* **Benchmarking**
  – Model-agnostic personas support reproducible comparisons across models, teams, and institutions.

---

## Why It Matters

As AI becomes embedded in public services, finance, healthcare, and infrastructure, the question shifts from whether AI is sovereign to how sovereignty is implemented responsibly.

Nemotron-Personas-Singapore supports sovereign AI in three concrete ways:

* **Local relevance**
  : Evaluations are conditioned on Singapore’s population, demographics, and usage contexts, enabling teams to test how models behave in the environments they will actually serve.
* **AI-ready transparency**
  : Fully synthetic, statistically grounded personas provide inspectable, reproducible evaluation inputs that support audit, documentation, and supervisory review.
* **Shared infrastructure**
  : Open release enables consistent evaluation across teams and institutions, creating a common reference point for developers, enterprises, and regulators.

---

## Start Building with Nemotron-Personas-Singapore

Load the dataset directly from Hugging Face:

```
from datasets import load_dataset

dataset = load_dataset("nvidia/nemotron-personas-singapore")
```

Want to learn more about NVIDIA's open data products, or interested in co-designing a future dataset? Join the conversation on
[NVIDIA's Discord](https://discord.com/invite/nvidiadeveloper)
.

**About AI Singapore**

AI Singapore (AISG) is a national programme launched by the National Research Foundation (NRF), Singapore, to catalyse, synergise and boost Singapore’s artificial intelligence (AI) capabilities to power our future digital economy. AISG will bring together all Singapore-based research institutions and the vibrant ecosystem of AI start-ups and companies developing AI products, to perform use-inspired research, grow the knowledge, create the tools, and develop the talent to power Singapore’s AI efforts.