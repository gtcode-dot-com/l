---
title: "Chapter 2: The MVE - Synthesizing a Historical Scientific Debate"
description: "Providing a detailed, step-by-step methodology for the first experiment designed to produce concrete, publishable results."
weight: 3
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.5
  filename: sitemap.xml
---

This chapter outlines the detailed methodology for our Minimum Viable Experiment (MVE). The goal is to produce rigorous, empirical results that can form the core of our first peer-reviewed publication.

### 1. The Research Question

Our experiment is designed to answer a single, focused question:

> **"Can the CNS Dialectical Synthesis Engine, when given two high-quality, conflicting historical narratives, generate a novel, coherent, and verifiably accurate synthesis that resolves the core conflict?"**

### 2. The Case Study: Plate Tectonics vs. Geosyncline Theory

To answer this question, we have selected a historical scientific debate as our test case: the conflict between **plate tectonics** and **geosyncline theory**. This case study is ideal for several reasons:
-   **Well-Documented:** There is a rich body of scientific literature for both theories.
-   **Clear Opposing Views:** The core hypotheses are in direct conflict.
-   **Known "Correct" Synthesis:** The modern theory of plate tectonics emerged as a synthesis that explained the valid observations of both older theories. This gives us a ground truth against which to compare our generated synthesis.

### 3. The Methodology (Step-by-Step)

Our experimental procedure will follow three precise steps:

#### Step 3a: Manual SNO Creation
To eliminate confounding variables from an imperfect ingestion pipeline, we will **manually create** two "parent" Structured Narrative Objects (SNOs). Each SNO will be constructed from seminal papers representing its respective theory. The key components of each SNO will be:
-   **Central Hypothesis:** The core claim of the theory (e.g., "Continents are fixed and mountains form in subsiding troughs called geosynclines").
-   **Reasoning Graph:** A manually constructed graph of supporting claims and arguments.
-   **Evidence Set:** A curated list of citations and key observations used by the theory's proponents.

#### Step 3b: Core Engine Implementation
We will implement the core components of the synthesis engine as described in the **[Developer's Guide](/guides/building-cns-2.0-developers-guide/chapter-4-synthesis-engine/)**. This includes the `RelationalMetrics` (specifically Chirality and Entanglement to select the two parent SNOs) and the `GenerativeSynthesisEngine` itself, which uses a structured dialectical prompt.

#### Step 3c: Running the Synthesis
The two parent SNOs (`SNO_PlateTectonics` and `SNO_Geosyncline`) will be fed into the synthesis engine. The engine's task is to generate a new candidate synthesis, which we will call `SNO_Synthesis`.

### 4. The Evaluation Protocol

This is the most critical section for ensuring our results are scientifically rigorous. The evaluation of `SNO_Synthesis` will be both quantitative and qualitative.

#### Quantitative Evaluation
The generated `SNO_Synthesis` will be processed by our heuristic-based `CriticPipeline` (as described in the **[Developer's Guide](/guides/building-cns-2.0-developers-guide/chapter-3-critic-pipeline/)**). We will present the output scores in a clear, tabular format:

| Metric          | Score | Description                               |
|-----------------|-------|-------------------------------------------|
| Trust Score     | TBD   | Overall confidence in the SNO's quality.  |
| Grounding Score | TBD   | How well claims are linked to evidence.   |
| Logic Score     | TBD   | The logical coherence of the reasoning.   |
| Novelty Score   | TBD   | How much it differs from parent SNOs.     |

#### Qualitative Evaluation
While scores provide a useful signal, the core of our evaluation will be a **qualitative, textual analysis**. This is non-negotiable for a credible result. We will:
1.  Extract the central hypothesis and key claims from the generated `SNO_Synthesis`.
2.  Directly compare this generated text to the established scientific consensus on plate tectonics.
3.  Explicitly demonstrate how the generated synthesis successfully incorporates valid evidence from both parent theories (e.g., the observation of subsiding basins from geosyncline theory) while resolving their primary contradictions.

The output of this two-part evaluation protocol will form the "Results" section of our first research paper, providing both quantitative benchmarks and a defensible, qualitative argument for the engine's success.
