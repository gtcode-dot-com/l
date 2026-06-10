---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-10T03:12:30.198733+00:00'
exported_at: '2026-06-10T03:12:31.990008+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/financial-institutions-transaction-foundation-models
structured_data:
  about: []
  author: ''
  description: 'Financial institutions have spent years building AI: fraud models,
    credit models, recommendation engines and risk systems. While this sprawl of task-specific
    models has been effective, it’s also constrained by siloed systems.'
  headline: Why Financial Institutions Are Converging on Transaction Foundation Models
    to Build Their Own Intelligence
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/financial-institutions-transaction-foundation-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Why Financial Institutions Are Converging on Transaction Foundation Models
  to Build Their Own Intelligence
updated_at: '2026-06-10T03:12:30.198733+00:00'
url_hash: 6e9cb8944f3a6200e56cb1496e9a12adacdd1fab
---

Financial institutions have spent years building AI: fraud models, credit models, recommendation engines and risk systems. While this sprawl of task-specific models has been effective, it’s also constrained by siloed systems.

Siloed systems prevent institutions from developing a unified understanding of consumers’ financial behavior. As enterprise datasets keep growing, so does the gap between what institutions know and what their AI can reason over — creating a major opportunity for the industry to build intelligence using proprietary data.

NVIDIA’s
[2026 State of AI in Financial Services](https://www.nvidia.com/en-us/industries/finance/ai-financial-services-report/)

report shows 65% of institutions now use AI, with nearly 90% deploying or assessing it and almost all maintaining or increasing spend. But as AI scales, so does complexity, and fragmented model architectures become the limiting factor.

Leading firms are tackling this challenge by rethinking the architecture itself. Where the industry once relied on statistical and machine learning algorithms purpose-built for each line of business, transformer-based transaction foundation models now make it possible to learn a single, unified representation of consumer behavior trained entirely on proprietary data.

Transaction foundation models are large-scale AI systems trained on billions of financial events — such as payments, transfers, product interactions and behavioral signals — that transform raw data into intelligence, helping firms better serve their customers.

The shift is structural. A traditional fraud model evaluates isolated signals. A foundation model interprets behavior in context where timing, device, location and prior activity shape meaning. More importantly, it brings the power of transformer architectures to tabular data, extracting signals previously invisible to traditional algorithms.

A payment at midnight means something different when it’s the fourth in 10 minutes, on an unfamiliar device, in a city the customer’s never transacted from before. That contextual depth improves performance across tasks, not just within them.

In collaboration with NVIDIA, Revolut built
[PRAGMA](https://arxiv.org/pdf/2604.08649)

— a family of transformer-based foundation models trained on 24 billion events across 26 million user records spanning over 100 countries. Powered by NVIDIA’s full AI stack

— including
[NVIDIA Hopper GPUs](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/)

, the
[NVIDIA cuDF](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf)

library and
[NVIDIA](https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf)
[Nemotron](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/)

open models —

running on Nebius cloud, a single foundation model outperforms strong task-specific models across domains like credit scoring, fraud detection and product recommendations while reducing reliance on handcrafted features.

“We move from weeks, or even in some cases months, in feature engineering to no time required for it at all,” said Tadas Kriščiūnas, head of group credit data science at Revolut.

Any institution can now adopt this approach using NVIDIA’s new
[Build Your Own Transaction Foundation Model](https://build.nvidia.com/nvidia/build-your-own-transaction-foundation-model)

developer example, which enables teams to start building transformer embeddings on tabular transaction data — integrating into existing pipelines without rebuilding from scratch.

## **The Cost of Fragmentation**

The problem isn’t today’s models, it’s the trajectory. Every new use case adds another model. Every new market needs retraining. Models that can’t share context leave value on the table.

[Mastercard](https://www.mastercard.com/global/en/news-and-trends/stories/2026/mastercard-new-generative-ai-model.html)

is developing a proprietary large tabular foundation model for payments, trained on billions of anonymized transactions today and designed to scale to hundreds of billions across additional datasets including fraud, authorization, chargeback, merchant location and loyalty data.

Built with capabilities from NVIDIA, AWS and Databricks — including the
[NVIDIA NeMo AutoModel](https://docs.nvidia.com/nemo/automodel/latest/index.html)

open library, part of
[NVIDIA NeMo framework](https://github.com/NVIDIA-NeMo/)

, and accelerated computing — the model is intended to reduce reliance on a multitude of AI models across markets, customers and use cases. Early testing shows it outperforming standard machine learning techniques, with promising applications in cybersecurity, fraud detection, loyalty, personalization, portfolio optimization and analytics.

[Adyen](https://www.nvidia.com/en-us/on-demand/session/gtc26-s82115/)

has also deployed transaction foundation models at scale, processing $1 trillion in payments. Using reinforcement learning, Adyen maximizes conversion and minimizes risk for merchants.

“Even fractional improvements like a 0.1% uplift in authorization can translate to massive incremental gross merchandise value and substantial cost reductions,” said Dhruv Ghulati, principal AI product manager at Adyen.

## **Semantic Layer for Agentic Commerce**

[Forty-two percent](https://blogs.nvidia.com/blog/ai-in-financial-services-survey-2026/)

of financial firms are already using or assessing agentic AI. As these systems begin to execute transactions — like managing subscriptions, routing payments and making purchases — the nature of financial behavior is changing.

[Stripe](https://www.nvidia.com/en-us/on-demand/session/gtc26-s82252/)

is using the NVIDIA and AWS platform to build foundation models that understand the full context of transactional behavior rather than reacting to individual signals — blocking close to $112 billion in fraud last year and delivering an average 38% reduction in fraud rates.

Transaction data is the proprietary history that competitors can’t replicate. The data already exists. The architecture is proven. The infrastructure is ready.

## **Scaling Through Ecosystem Partners**

The Build Your Own Transaction Foundation Model developer example is available for customers to run on Amazon Web Services (AWS), deployed with Amazon SageMaker HyperPod, as well as Nebius AI Cloud — powered by NVIDIA accelerated computing.

[Nebius AI Cloud](https://nebius.com/blog/posts/building-transaction-foundation-models-on-nebius-ai-cloud)
supports the full transaction foundation model lifecycle — from deployment of the developer example through multi-node training to managed inference on Token Factory — powered by NVIDIA accelerated computing.

Financial services firms can also work with services partners EXL, GFT IT Consulting and Thoughtworks to apply the developer example to their specific use cases.

EXL is integrating transaction foundation models into its EXLerate.ai platform to unify siloed financial data into a scalable, enterprise intelligence layer powered by proprietary transaction data. In collaboration with NVIDIA, EXL is using this architecture to help financial institutions accelerate model development, enhance contextual decisioning and operationalize agentic AI at scale.

Thoughtworks is helping financial institutions operationalize transaction foundation models within complex banking environments, integrating them into payment, servicing and risk while establishing the necessary governance and AI operating models. The company will be showcasing a demo and presentation on transaction foundation models at the upcoming AWS Summit in New York City on Wednesday, June 17.

GFT IT Consulting is integrating transaction foundation models into its flagship solutions: Wynxx, an agentic AI platform used by over 100 financial institutions for secure AI adoption in areas like credit risk, and Smaragd, a compliance engine that reduces false positives by up to 75% for major banks.

*Join NVIDIA at Money20/20 Europe from June 2-4 to learn how transaction foundation models are powering the next generation of AI in financial services.*

*Explore the Build Your Own Transaction Foundation Model developer example on*
[*build.nvidia.com*](https://build.nvidia.com/nvidia/build-your-own-transaction-foundation-model)
*.*