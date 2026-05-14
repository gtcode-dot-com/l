---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-05-14T02:29:14.127476+00:00'
exported_at: '2026-05-14T02:29:18.789772+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/allenai/emo
structured_data:
  about: []
  author: ''
  description: A Blog post by Ai2 on Hugging Face
  headline: 'EMO: Pretraining mixture of experts for emergent modularity'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/allenai/emo
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'EMO: Pretraining mixture of experts for emergent modularity'
updated_at: '2026-05-14T02:29:14.127476+00:00'
url_hash: a40b2ba2d440123f7f8b9aac8830ea80292b02c3
---

# EMO: Pretraining mixture of experts for emergent modularity

🧠

**Models:**
<https://huggingface.co/collections/allenai/emo>

| 📄

**Tech report:**
<https://allenai.org/papers/emo>

| 💻

**Code:**
<https://github.com/allenai/EMO>

| 📊

**Visualization:**
<https://emovisualization.netlify.app/>

[![EMO blog post draft ryan - Google Docs-image-1 (1)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/812CTj_1vPuk8Xrgt5hfi.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/812CTj_1vPuk8Xrgt5hfi.png)

Today we're releasing
[**EMO**](https://huggingface.co/collections/allenai/emo)
, a new mixture-of-experts (MoE) model pretrained end-to-end so that modular structure emerges directly from the data without relying on human-defined priors. EMO lets you use a small subset of its experts - just 12.5% of the total - for a given task while keeping near full-model performance, and still works as a strong general-purpose model when all experts are used together.

Large language models are typically trained and deployed as monolithic systems: a single model is initialized, pretrained, fine-tuned, and served as one unified entity. But applications often need only a subset of capabilities, such as code generation, mathematical reasoning, or domain-specific knowledge. As frontier language models routinely reach trillions of parameters, using and adapting the full model becomes impractical for most users and incurs unnecessary computational cost and memory to host parameters that may not even be needed.

Mixture-of-experts (MoE) models seem like a natural way to relax this constraint. Instead of using one large feedforward network at each layer, MoEs contain many smaller ones, called experts, and activate only a small subset for each input token. In principle, a task that only needs one capability could load only the relevant experts.

In practice, however, existing MoEs still need the full model to work well. Even within a single input, different tokens often activate different experts, so a task can end up using all the experts during its generation. As we show in our paper, this happens partly because experts in standard MoEs often specialize in low-level lexical patterns like prepositions or punctuation rather than higher-level domains or capabilities. As a result, small subsets of experts are not reliably usable on their own.

We instead want MoE models whose experts organize into coherent groups that can be selectively used and composed.

One way to encourage this during pretraining is to route tokens to experts based on predefined semantic domains, such as math, biology, or code. Prior work like BTX and our FlexOlmo project has tried this. However, predefined domains come with important limitations. They require domain labels across the pretraining corpus, which can be ambiguous and expensive to obtain, and they may inject too much human bias into how the model is allowed to organize itself. More importantly, fixing the domains upfront also fixes the model's modular structure: if a new domain or capability emerges at inference time, it isn't obvious which experts should be used.

That's where EMO comes in.

We show that EMO - a 1B-active, 14B-total-parameter (8-expert active, 128-expert total) MoE trained on 1 trillion tokens - supports selective expert use: for a given task or domain, we can use only a small subset of experts (just 12.5% of total experts) while retaining near full-model performance. At the same time, when all experts are used together, EMO remains a strong general-purpose model. In contrast, a standard MoE of equal architecture trained on the same data shows severe degradation when selectively using its expert subsets.

[![EMO blog post draft ryan - Google Docs-image-2 (1)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/CPWUSB64LhBEjMI0Rgg6L.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/CPWUSB64LhBEjMI0Rgg6L.png)

*EMO is an MoE trained with modularity as a first-class objective. For a given domain (e.g., math, code, biomedical), users can select a small subset of experts of any size and retain near full-model performance. This turns a single model into a composable architecture, enabling flexible deployment with improved memory-accuracy tradeoffs for large, sparse MoEs.*

## How do we get modularity to emerge?

In an MoE, a small network called the router decides which experts each token activates. We want the router to learn that tokens from similar domains should activate similar subsets of experts. Our key observation is that
*tokens from the same document usually come from the same domain*
. We therefore use document boundaries as a weak supervisory signal: during training, all tokens in a document are restricted to choose their active experts from a shared expert pool.

[![EMO blog post draft ryan - Google Docs-image-3 (1)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/slqCFgfncHGGK1lErZNvl.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/slqCFgfncHGGK1lErZNvl.png)

*Comparison of training of a standard MoE and EMO (k = 2, n = 10, shared experts omitted for simplicity). (Left) In a standard MoE, each token independently selects its top-k experts. Across tokens, all experts are used. (Right) In EMO, the router first selects a subset of experts for each document, and all tokens are constrained to route within this subset. This enforces consistent expert usage across the document, encouraging groups of experts to form domain specialization.*

For example, in an MoE with 10 total experts and 2 active experts per token, all tokens in a document are restricted to route within the same pool of 4 experts, as shown in the figure above. This pool is chosen by the router itself: we average the router's expert preferences across all tokens in the document, then select the most-used experts as the document's shared pool. Different documents can use different pools, allowing recurring expert groups to emerge directly from the training data.

There are a few considerations when implementing the system:

**Load balancing.**
One technical challenge is load balancing. In standard MoE training, the load-balancing objective is used to prevent the model from collapsing onto only a small number of experts. At first glance, this seems to conflict with EMO's training objective: we are explicitly restricting each document to use only a subset of experts.

The conflict comes from the scale at which load balancing is usually applied. In many MoE implementations, load balancing is computed locally, often within a micro-batch containing only a small number of documents. This local objective can push tokens within the same document to spread across many experts, directly opposing EMO's objective of keeping expert usage consistent within a document.

To resolve this, we apply load balancing globally across many documents. At this larger scale, the two objectives become complementary: EMO encourages tokens within the same document to use a coherent expert pool, while global load balancing encourages different documents to collectively cover all experts. In practice, we found that global load-balancing is important for stable training.

**Document pool size.**
The document pool size controls how restrictive the modularity constraint is. A smaller pool forces tokens in the same document to share a tighter set of experts, encouraging stronger modularity; a larger pool gives the model more flexibility but weakens the constraint.

Rather than fixing one pool size, we randomly sample it during training. This prevents EMO from overfitting to a single subset size and lets it support different expert subset sizes at inference time.

## Benchmark results

On general-purpose benchmarks, EMO matches the performance of a standard MoE model, showing that the modularity objective does not come at the cost of full-model performance. The more important question, however, is whether the model can still work when we only keep a subset of experts. In this setting, we construct task-specific expert subsets by ranking experts according to their routing usage on a small amount of task validation data, keeping the most-used experts and discarding the rest.

The figure below shows that EMO remains robust under selective expert use. When we keep only 25% of the experts (32 expert subset), EMO loses only about 1% absolute performance across all benchmarks; even when we keep only 12.5% of the experts (16 expert subset), the overall drop is only about 3%. This holds both before and after fine-tuning. In contrast, the matching standard MoE degrades sharply as the expert subset gets smaller, often falling close to or below random performance in the smallest expert subset settings.

[![EMO blog post draft ryan - Google Docs-image-4](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/ki3pHaOktjGM1qI4JBeYG.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/ki3pHaOktjGM1qI4JBeYG.png)

Furthermore, we show that selecting the right experts for a task is surprisingly cheap: a single example with few-shot demonstrations is enough to identify a module that performs on par with one selected using a full validation set. And EMO isn't tied to any particular selection method: it works well with existing expert-pruning approaches like Easy-EP, and the two complement each other.

[![EMO blog post draft ryan - Google Docs-image-5 (1)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/NMSuavox_S24mxIBovCMd.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/NMSuavox_S24mxIBovCMd.png)

*Smaller 130B-token setting. Averaged performance over 16 MMLU categories across different memory budgets. EMO expert subsets push the Pareto frontier in memory-accuracy trade-off, outperforming standard MoEs and even fixed-budget models trained from scratch.*

## What are expert subsets specializing to?

To see what EMO actually learned after training, we clustered router activations of the first 100 tokens across 12K pretraining documents. The difference from a standard MoE is stark.

EMO's token clusters correspond to things like
*Health, Medical & Wellness*
,
*News Reporting*
,
*US Politics & Elections*
, and
*Film & Music*
. A standard MoE produces clusters like
*Prepositions*
,
*Proper Names*
,
*Copula Verbs*
, or
*Definite Articles*
. In EMO, tokens from a given document mostly land in the same cluster; in a standard MoE, they end up scattered across many.

The contrast is easiest to see on a single example. Take a health article: in EMO, almost every token would route into the
*Health, Medical & Wellness*
cluster. In a standard MoE, the top cluster is
*Possessives & Definite Articles*
; the model would group the article with every other text that happens to use the word
*the*
or
*your*
, regardless of what that text is about.

[![EMO blog post draft ryan - Google Docs-image-6 (1)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/FG27xp8oJXUZW9cTju235.png)](https://cdn-uploads.huggingface.co/production/uploads/638e39b249de7ae552d977b5/FG27xp8oJXUZW9cTju235.png)

*Token clusters of pretraining data on MoEs trained on 1T tokens. EMO clusters correspond to semantically meaningful domains, with tokens from the same document largely grouped together. Standard MoE training produces clusters of surface-level or syntactic features, with document tokens dispersed across multiple clusters.*

Because EMO forms modules that map to semantic domains rather than surface features, you can pick a small expert subset and still have a functioning model: the group corresponds to a real capability.

You can play around with the clustering results yourself in
[our interactive visualization](https://emovisualization.netlify.app/)
.

## What we're releasing

We're releasing the
[full EMO-trained model](https://huggingface.co/collections/allenai/emo)
, a matched standard-MoE baseline trained on the same data, and the
[training code](https://github.com/allenai/EMO)
. We hope these artifacts are useful for other groups studying emergent modularity in MoEs.

There's more work to do. EMO is an early step toward making large sparse models more modular, but many questions remain: how to better select and compose expert subsets, how to update modules without disrupting the full model, and how to use modular structure for better interpretability and control. Releasing these models should help the community to study these questions and build toward modular language models that are easier to deploy, adapt, inspect, and compose.