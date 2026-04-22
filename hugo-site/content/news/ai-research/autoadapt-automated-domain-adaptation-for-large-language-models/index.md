---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-22T18:15:34.212654+00:00'
exported_at: '2026-04-22T18:15:36.404381+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/autoadapt-automated-domain-adaptation-for-large-language-models
structured_data:
  about: []
  author: ''
  description: 'AutoAdapt automates the design and tuning of domain adaptation workflows
    for large language models. It improves performance without requiring additional
    compute, making deployment more accessible:'
  headline: 'AutoAdapt: Automated domain adaptation for large language models'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/autoadapt-automated-domain-adaptation-for-large-language-models
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'AutoAdapt: Automated domain adaptation for large language models'
updated_at: '2026-04-22T18:15:34.212654+00:00'
url_hash: a5102658c25434654ce4dee02cfdb10499788911
---

![Three white line icons in a row; a document list, a workflow, and process wheel against a blue and purple gradient background.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/AutoAdapt-BlogHeroFeature-1400x788-1.jpg)

## At a glance

* **Problem**
  : Adapting large language models to specialized, high-stakes domains is slow, expensive, and hard to reproduce.
* **What we built**
  : AutoAdapt automates planning, strategy selection (e.g., RAG vs. fine-tuning), and tuning under real deployment constraints.
* **How it works**
  :  A structured configuration graph maps the full scope of the adaptation process, an agentic planner selects and sequences the right steps, and a budget-aware optimization loop (AutoRefine) refines the process within defined constraints.
* **Why it matters**
  : The result is faster, automated, more reliable domain adaptation that turns weeks of manual iteration into repeatable pipelines.

Deploying large language models (LLMs) in real-world, high-stakes settings is harder than it should be. In high-stakes settings like law, medicine, and cloud incident response, performance and reliability can quickly break down because adapting models to domain-specific requirements is a slow and manual process that is difficult to reproduce.

The core challenge is domain adaptation, which entails turning a general-purpose model into one that consistently follows domain rules, draws on the right knowledge, and meets constraints such as latency, privacy, and cost. Today, that process typically involves guesswork, choosing among approaches like retrieval-augmented generation (RAG) and fine-tuning, tuning hyperparameters, and iterating through evaluations with no clear path to a good outcome. An operations team responding to an outage can’t afford a model that drifts from domain requirements or a tuning process that takes weeks with no guarantee of a reproducible result.

To tackle this, we’re pleased to introduce AutoAdapt. In our paper, “
[AutoAdapt: An Automated Domain Adaptation Framework for Large Language Models](https://www.microsoft.com/en-us/research/publication/autoadapt-an-automated-domain-adaptation-framework-for-llms/)
,” we describe an end-to-end, constraint-aware framework for domain adaptation. Given a task objective, available domain data, and practical requirements like accuracy, latency, hardware, and budget, AutoAdapt plans a valid adaptation pipeline, selecting among approaches like RAG and multiple fine-tuning methods, and tunes key hyperparameters using a budget-aware refinement loop. The result is an executable, reproducible workflow for building domain-ready models more quickly and consistently, helping make LLMs dependable in real-world settings.

PODCAST SERIES

## AI Testing and Evaluation: Learnings from Science and Industry

Discover how Microsoft is learning from other domains to advance evaluation and testing as a pillar of AI governance.

Opens in a new tab

## How it works

AutoAdapt starts from a practical observation: teams don’t just need a better prompt or more data, they need a decision process that reliably maps a task, its domain data, and real constraints to an approach that works. To do this, AutoAdapt treats domain adaptation as a constrained planning problem. Given an objective provided in natural language, dataset size and format, and limits on latency, hardware, privacy, and cost, it provides an end-to-end pipeline that teams can execute and deploy.

Domain adaptation often feels like trial and error because the design space is large and complex. Teams must choose among approaches such as RAG, supervised fine-tuning, parameter-efficient methods (such as LoRA), and alignment steps, each with many hyperparameters. These choices interact in nonobvious ways, and not all combinations are valid, making it difficult to identify a reliable strategy. The problem is compounded by the high cost of LLM training, which limits how many configurations can be explored.

AutoAdapt addresses this with the Adaptation Configuration Graph (ACG), a structured representation of the system’s configuration space that enables efficient search while guaranteeing valid pipelines.

Building on the ACG, AutoAdapt uses a planning agent to make and justify decisions. It proposes strategies, evaluates them against user requirements, and iterates until the plan is feasible and well-grounded. Rather than optimizing in an unconstrained black box, AutoAdapt roots each decision in best practices and explicit constraints, producing an executable workflow with parameter ranges.

Finally, AutoAdapt introduces AutoRefine, a budget-aware refinement loop that optimizes hyperparameters by strategically selecting which experiments to run next, even under limited feedback. AutoRefine replaces weeks of manual tuning with a more disciplined, reproducible process that is easier to audit and compare across projects. In real-world systems such as healthcare documentation, legal workflows, or incident response, this level of rigor is essential. Figure 1 illustrates the end-to-end workflow.

![A workflow diagram illustrating how a user’s task description and constraints are processed to automatically produce a deployable language model. User inputs are analyzed and refined through multiple stages, including multi‑agent proposal and critique, best‑practice consultation, and iterative pipeline refinement. These stages evaluate task requirements, data choices, and model configurations while verifying user constraints. The process concludes with an executable plan that generates a final model meeting the specified objectives and constraints.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/AutoAdapt_overview_fig1_1400px.png)


Figure 1. The AutoAdapt workflow, showing how user inputs flow through planning and refinement to produce a deployable model.

## Evaluation

In experiments, AutoAdapt consistently identifies effective adaptation strategies and delivers improvements across a range of benchmark and real-world tasks, including reasoning, question answering, coding, classification, and cloud-incident diagnosis. It uses constraint-aware planning and budgeted refinement to find better-performing configurations with minimal added time and cost, making the process practical for production teams. Figures 2 and 3 show aggregate performance against competitive baselines.

![Three radar plots compare multiple methods across several datasets using success rate, normalized performance score, and a cumulative metric. In all three plots, the AutoAdapt method consistently exhibits larger coverage across most tasks, indicating stronger overall performance. Baseline methods show more uneven profiles, with strengths limited to specific datasets or metrics. The visualization highlights AutoAdapt’s robust and consistent advantage relative to existing approaches.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/AutoAdapt_results_fig3_1400px.png)


Figure 2. Success rate (SR), normalized performance score (NPS), and cumulative score (CS) comparing AutoAdapt with baseline methods across datasets. Higher scores indicate better performance, with AutoAdapt outperforming state-of-the-art baselines.


![Two bar charts compare time and cost overheads for AutoAdapt relative to a default baseline across multiple datasets. AutoAdapt introduces only a small additional time requirement, averaging around half an hour, while achieving noticeable performance improvements. The cost comparison shows a similarly modest increase, with average extra cost remaining low across tasks. Overall, the figure indicates that AutoAdapt delivers performance gains with minimal additional time and financial overhead.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/04/AutoAdapt_cost_time_overhead_fig2_1400px.png)


Figure 3. AutoAdapt achieves performance gains with minimal overhead, approximately 30 minutes of additional time and $4 in additional cost.

## Implications and looking forward

The broader significance of AutoAdapt is that domain adaptation can become an engineering discipline, not an ad hoc process. By making key choices explicit—what to adapt, how to adapt it, and which constraints the system must satisfy—AutoAdapt helps teams reach results faster, reproduce them more easily, and audit them more rigorously. This shift is especially important in domains where drift from pretrained knowledge is common and failures are costly. When LLMs are used to draft clinical notes, triage support incidents, or summarize regulatory language, organizations need a clear, repeatable path from data to models that behave predictably under latency, privacy, and budget requirements.

Because domain adaptation is a prerequisite for deploying LLMs in real-world settings, we’re making the AutoAdapt framework
[open source
(opens in new tab)](https://github.com/microsoft/AutoAdapt)
to give teams a concrete starting point. The
[README
(opens in new tab)](https://github.com/microsoft/AutoAdapt?tab=readme-ov-file#installation-and-quick-start)
file provides installation and quick-start instructions.

Video playback requires cookie consent


Opens in a new tab