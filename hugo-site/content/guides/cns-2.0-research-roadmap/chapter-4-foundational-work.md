---
title: "Chapter 4: Building on the Foundation"
description: "Outlining the immediate research projects that build upon the MVE to enable the broader research vision."
weight: 5
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

The successful completion of our Minimum Viable Experiment (MVE) and its publication will serve as a foundational, proof-of-concept milestone for the CNS 2.0 project. It is, however, just the first step. The limitations acknowledged in our first paper—specifically, the manual creation of input SNOs and the reliance on a heuristic-based critic—directly inform the next stages of our research.

This chapter outlines the two critical research projects that form the rest of the **Foundational Work** phase. These projects must be tackled to move from the controlled environment of the MVE to the dynamic, at-scale vision of the full CNS 2.0 system. They are the essential prerequisites for the advanced research thrusts detailed in the subsequent sections of this roadmap.

### Foundational Project #1: The Narrative Ingestion Pipeline

The most immediate limitation of our first study is the manual creation of parent SNOs. Our next research project will be to address this head-on by developing a robust, semi-automated **Narrative Ingestion Pipeline**. This pipeline is the gateway to the entire CNS ecosystem.

-   **The Challenge:** The task is to move from unstructured text (e.g., a PDF of a scientific paper) to a structured SNO, correctly identifying the central hypothesis, extracting the reasoning graph, and linking claims to evidence. This is a highly complex problem at the intersection of information extraction, argumentation mining, and natural language understanding.
-   **Proposed Methodology:** We plan to leverage modern Large Language Model (LLM) compilation frameworks like **[DSPy](https://github.com/stanfordnlp/dspy)**. Instead of relying on brittle, hand-crafted prompts, we will define the program's flow (e.g., `extract_hypothesis -> identify_claims -> build_graph`) and use DSPy to programmatically generate and optimize the complex, multi-step prompts required for this pipeline.
-   **Contribution:** A successful ingestion pipeline would represent a significant contribution to the fields of information extraction and argumentation mining and would unlock the ability to populate the CNS system with narratives at scale.

### Foundational Project #2: From Heuristics to a Data-Driven Critic

Our initial MVE relies on a `CriticPipeline` built with transparent, explainable heuristics. While excellent for a controlled experiment, these heuristics lack the nuance and learning capacity to evaluate the complex, diverse SNOs that a scaled-up system will produce. The next foundational project is to replace the heuristic logic and grounding critics with more powerful, data-driven models.

-   **The Challenge:** Evaluating the logical coherence of a reasoning graph and the subtle relationship between a claim and its evidence requires deep semantic understanding. This is a perfect task for specialized machine learning models.
-   **Proposed Methodology:** Our research will focus on two areas:
    1.  **Grounding Critic:** Fine-tuning a Natural Language Inference (NLI) model to produce plausibility scores between claims and evidence snippets.
    2.  **Logic Critic:** Developing a Graph Neural Network (GNN) to assess the structural integrity of reasoning graphs. This requires a significant sub-project focused on creating a large, labeled dataset of valid and fallacious reasoning graphs.
-   **Contribution:** Creating these specialized critic models represents a major research effort. A successful GNN-based logic critic, in particular, would be a powerful tool for automated reasoning and a significant advance over our initial heuristic models.

With a robust ingestion pipeline and a powerful, data-driven critic pipeline, the foundational components of the CNS 2.0 architecture will be in place. This will allow us to finally begin to approach the "Grand Vision": running the full, autonomous CNS 2.0 system at scale and tackling the advanced research questions outlined in the next sections.
