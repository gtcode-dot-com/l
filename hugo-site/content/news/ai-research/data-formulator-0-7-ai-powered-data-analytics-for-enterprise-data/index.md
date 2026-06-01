---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-01T00:58:11.741478+00:00'
exported_at: '2026-06-01T00:58:14.669092+00:00'
feed: https://www.microsoft.com/en-us/research/feed
language: en
source_url: https://www.microsoft.com/en-us/research/blog/data-formulator-0-7-ai-powered-data-analytics-for-enterprise-data
structured_data:
  about: []
  author: ''
  description: 'Data Formulator introduces AI-powered analytics for enterprise data
    workflows. Data teams can easily bring enterprise data into an AI-ready workspace
    where users can explore, analyze, and visualize data with AI agents to turn raw
    data into actionable insights:'
  headline: 'Data Formulator 0.7: AI-powered data analytics for enterprise data'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.microsoft.com/en-us/research/blog/data-formulator-0-7-ai-powered-data-analytics-for-enterprise-data
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Data Formulator 0.7: AI-powered data analytics for enterprise data'
updated_at: '2026-06-01T00:58:11.741478+00:00'
url_hash: 6e19c9610217cc02835395f4efa996d385dbbd29
---

![Three minimalist white line icons on a textured blue‑green gradient background: a rising bar chart on the left, a central hub‑and‑spoke network diagram in the middle, and a checkmark inside a circle on the right.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/DataFormulator-BlogHeroFeature-1400x788-1-scaled.jpg)

## At a glance

* Data Formulator 0.7 is an open-source AI-powered system for enterprise data analytics that combines data connectivity, agent-guided exploration, and visualization refinement in a shared workspace.
* It includes a Data Connectors feature, which supports governed, reusable connections across databases, warehouses, BI systems, object stores, and local files, reducing integration work for platform teams.
* Context-aware agents help users prepare data, explore analyses, generate visualizations, and navigate long-running and branching analytical workflows.
* An interactive, multimodal interface allows teams to iteratively explore and refine analyses across fragmented data sources, with no SQL or programming expertise required.

Enterprise teams increasingly rely on AI systems for analytics, but enterprise data workflows are often fragmented across storage systems and tools. Before analysis can begin, teams often need to establish governed connections, prepare metadata, manage permissions, and build workflows for combining and reshaping data across multiple systems.

Beyond data connection, analysis itself remains challenging for analysts and domain experts, many of whom lack deep coding expertise. They frequently need to compute new metrics, compare different ways of organizing data, inspect intermediate outputs, and refine visualizations as needs evolve. These workflows are difficult to reproduce inside isolated chat interactions that lack persistent access to enterprise data, workflow history, and visualization context.

Our new release,
[Data Formulator 0.7
(opens in new tab)](https://github.com/microsoft/data-formulator)
, is designed to address these challenges. It is an open-source AI-powered data analysis system that connects fragmented enterprise data and iterative analytical workflows. It provides a lightweight way to connect across a variety of data sources, context-aware agents that assist with data preparation, exploration, and visualization, and an interactive workspace where users can iteratively refine and share their analyses.

video series

## On Second Thought

A video series with Sinead Bovell built around the questions everyone’s asking about AI. With expert voices from across Microsoft, we break down the tension and promise of this rapidly changing technology, exploring what’s evolving and what’s possible.

Opens in a new tab

## Connecting enterprise data with Data Connectors

Data Formulator helps teams bring enterprise data into an AI-ready workspace without needing to rebuild the same connections for every source of data. The Data Connectors feature supports authentication, persistent connections, previews, metadata, and a unified workspace model across databases, warehouses, BI systems, object stores, and local files. This reduces integration work for platform teams and allows users to work from centrally managed, reusable data connections rather than relying on repeated manual file uploads, as shown in Figure 1.

![Figure 1. Data Connectors provide persistent connections between enterprise data sources and Data Formulator, allowing analysts and AI agents to load, query, and visualize shared data.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/df-blog-figure-1_New-scaled.jpg)


Figure 1. Data Connectors provide persistent connections between enterprise data sources and Data Formulator, allowing analysts and AI agents to load, query, and visualize shared data.

## Context-aware agents for data analysis

Context-aware AI agents form the core of Data Formulator. Unlike a single prompt, Data Formulator gives agents access to the full analysis workspace, including connected data sources, loaded tables, prior charts, and the user’s objective. Agents reason and act through tools rather than text alone. In a single interaction, an agent can inspect data, write and run code in an isolated environment, generate chart specifications, and explain its results while showing intermediate steps.

When a request is ambiguous, the agent asks clarifying questions before proceeding. This allows agents to carry out more complex analytical workflows: aligning analyses with the user’s goal, preparing and transforming data, suggesting follow-up questions, generating tables and charts in batch, and creating verifiable, reproducible code for every result.

## A workspace for iterative data analysis

Data Formulator pairs these agents with a multimodal interface designed for open-ended analysis workflows. Users work with agents through the Data Thread, a structured chat that records every question, intermediate finding, and chart throughout the analysis process. Long sessions stay navigable: users can revisit earlier steps, branch into alternative analyses, and compare them side by side without losing context.

As illustrated in Figure 2, the interactive canvas complements Data Thread by allowing users to directly edit visualizations. When users shift from exploration to communication, they can refine charts directly on the canvas or describe changes in natural language and let the agent adjust labels, annotations, layout, color, and emphasis. Analysts can also generate reports and share their findings with others.

![Figure 2. (Left) Data Thread allows users to interact with AI agents by asking questions, requesting data visualizations, and exploring follow-up analyses. Threads preserve the history of long analysis sessions, making it possible to revisit, reuse, and build on earlier work. (Right) The interactive canvas allows users to refine visualizations directly by adjusting settings, redesigning charts, and inspecting the underlying data and code side by side.](https://www.microsoft.com/en-us/research/wp-content/uploads/2026/05/df-blog-figure-2-scaled.png)


Figure 2. (Left) Data Thread allows users to interact with AI agents by asking questions, requesting data visualizations, and exploring follow-up analyses. Threads preserve the history of long analysis sessions, making it possible to revisit, reuse, and build on earlier work. (Right) The interactive canvas allows users to refine visualizations directly by adjusting settings, redesigning charts, and inspecting the underlying data and code side by side.

View the Data Formulator demo
[here
(opens in new tab)](https://data-formulator.ai)
, or explore the Data Formulator
[GitHub repository
(opens in new tab)](https://github.com/microsoft/data-formulator)
. Teams developing analytics workflows for enterprise data can use the project as a foundation for adapting these capabilities to their own systems and requirements.

Opens in a new tab