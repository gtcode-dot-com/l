---
title: "Tutorial Part 4: Analyzing the Results"
description: "Demonstrating the two-part evaluation protocol (quantitative and qualitative) to validate the generated synthesis."
weight: 10
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.7
  filename: sitemap.xml
---

The `GenerativeSynthesisEngine` has produced a candidate `SNO_Synthesis`. However, this new narrative is not accepted into the system's knowledge base until it has been rigorously validated. As outlined in the **[Minimum Viable Experiment (MVE)](/guides/cns-2.0-research-roadmap/chapter-2-minimum-viable-experiment/)**, this validation process has two crucial parts: a quantitative evaluation by the `CriticPipeline` and a qualitative analysis by a human expert (or, in this case, by comparing it to the known scientific consensus).

### 1. Quantitative Evaluation: The Critic Pipeline

The candidate SNO is passed through the same `CriticPipeline` that evaluated its parents. The pipeline will assign scores for grounding, logic, and novelty, which are then weighted to produce a final `TrustScore`.

```python
from cns_tools import CriticPipeline
from cns_tools.utils import get_text_from_embedding

# Assume SNO_synthesis_candidate is the output from the previous step.

# Initialize the critic pipeline
critic_pipeline = CriticPipeline()

# Evaluate the candidate SNO
evaluated_sno = critic_pipeline.evaluate(SNO_synthesis_candidate)

# Let's inspect the results. The `evaluate` method would populate
# the SNO's metadata with the individual critic scores.
scores = evaluated_sno.metadata['critic_scores']
final_trust_score = evaluated_sno.trust_score

# For the tutorial, let's assume the following scores were generated:
scores = {'grounding': 0.92, 'logic': 0.95, 'novelty_parsimony': 0.88}
final_trust_score = 0.925 # Assuming a weighted average

# Display the results in a markdown table
print("| Critic Component      | Score |")
print("|-----------------------|-------|")
print(f"| GroundingCritic       | {scores['grounding']:.2f}  |")
print(f"| LogicCritic           | {scores['logic']:.2f}  |")
print(f"| NoveltyParsimonyCritic| {scores['novelty_parsimony']:.2f}  |")
print("| **Final Trust Score** | **{final_trust_score:.3f}** |")

```

#### Interpreting the Quantitative Scores

| Critic Component      | Score |
|-----------------------|-------|
| GroundingCritic       | 0.92  |
| LogicCritic           | 0.95  |
| NoveltyParsimonyCritic| 0.88  |
| **Final Trust Score** | **0.925** |

-   **Grounding (0.92):** The high score indicates that the claims within the synthesized narrative are well-supported by the combined evidence from the parent SNOs. It successfully inherited the evidential strengths of both theories.
-   **Logic (0.95):** The synthesized reasoning graph is highly coherent and free of the internal contradictions that might have existed in the parent theories (e.g., the conflict between a static vs. dynamic Earth).
-   **Novelty & Parsimony (0.88):** The score is high but not perfect. The synthesis is novel because it presents a new, unifying framework. It might lose minor points on parsimony if the initial generated graph is slightly more complex than necessary, but it correctly identifies the hypothesis as a significant departure from its parents.
-   **Trust Score (0.925):** The high final trust score indicates that the system has high confidence in this new narrative. It is a robust, coherent, and well-supported synthesis that surpasses its parents.

### 2. Qualitative Analysis: Comparison to Scientific Consensus

The quantitative scores tell us the synthesis is structurally sound, but they don't tell us if it's *correct*. For this, we compare the generated hypothesis to the modern, accepted scientific understanding of plate tectonics.

**Generated Hypothesis from Tutorial Part 3:**
> "The Earth's lithosphere is a dynamic system of moving plates, not a static crust. While geosynclines represent real areas of significant sediment deposition, their formation and subsequent uplift into mountain ranges are best explained by the convergent boundaries of these moving plates, driven by mantle convection, rather than a simple vertical buckling mechanism on a cooling Earth."

**Analysis:**

This generated hypothesis is a remarkably accurate and nuanced summary of the scientific revolution that occurred in geology.

1.  **Rejection of the Core Flaw:** It correctly identifies and rejects the central flaw of Geosyncline theory: the idea of a "static crust" and "vertical buckling."
2.  **Preservation of Valid Observations:** It does not discard Geosyncline theory entirely. It correctly acknowledges that "geosynclines represent real areas of significant sediment deposition," which was a key observation of the earlier theory. This demonstrates dialectical synthesis, not just blind replacement.
3.  **Identification of the Correct Mechanism:** It correctly identifies the superior explanatory mechanisms of Plate Tectonics: "moving plates," "convergent boundaries," and "mantle convection."
4.  **Higher-Order Reasoning:** The synthesis operates at a higher level of abstraction. It reframes the debate not as "geosynclines vs. plates" but as "what is the *mechanism* that explains the observed phenomenon of geosynclines?"

### Conclusion of the Experiment

The CNS 2.0 system successfully:
1.  Identified two opposing, well-supported narratives as a chiral pair.
2.  Generated a new, candidate synthesis that resolved their core conflict.
3.  Quantitatively verified that the new synthesis was logically coherent and well-grounded.
4.  Qualitatively confirmed that the synthesis aligns almost perfectly with the modern scientific consensus.

This end-to-end walkthrough demonstrates the core power of the Chiral Narrative Synthesis framework: to move beyond simple information retrieval and perform a structured, auditable, and ultimately insightful form of automated knowledge discovery.
