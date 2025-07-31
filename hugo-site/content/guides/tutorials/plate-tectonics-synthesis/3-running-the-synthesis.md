---
title: "Tutorial Part 3: Running the Synthesis"
description: "How to use the ChiralPairDetector and GenerativeSynthesisEngine to create a novel synthesis from two conflicting SNOs."
weight: 9
lastmod: "2025-07-30"
sitemap:
  changefreq: monthly
  priority: 0.7
  filename: sitemap.xml
---

Now that we have our two parent SNOs, `SNO_geosyncline` and `SNO_plate_tectonics`, we can proceed with the core of the CNS 2.0 workflow: identifying them as a conflicting pair and using the synthesis engine to generate a new, higher-order narrative.

We'll continue using our hypothetical `cns_tools` library.

### 1. Initial Critic Evaluation

Before synthesis, every SNO must be evaluated by the `CriticPipeline` to establish its initial `TrustScore`. This score is crucial for calculating the `CScore` (Chirality Score). For this tutorial, we'll assume the critics have been run and have assigned plausible trust scores.

```python
# In a real run, the CriticPipeline would be invoked here.
# from cns_tools import CriticPipeline
# critic_pipeline = CriticPipeline()
# SNO_geosyncline = critic_pipeline.evaluate(SNO_geosyncline)
# SNO_plate_tectonics = critic_pipeline.evaluate(SNO_plate_tectonics)

# For the tutorial, we'll assign mock trust scores.
# Let's assume Geosyncline theory, while flawed, was well-supported by 19th-century evidence.
# Plate Tectonics is more robustly supported by modern evidence.
SNO_geosyncline.trust_score = 0.75
SNO_plate_tectonics.trust_score = 0.95

print(f"Geosyncline Trust Score: {SNO_geosyncline.trust_score}")
print(f"Plate Tectonics Trust Score: {SNO_plate_tectonics.trust_score}")
```

### 2. Identifying the Chiral Pair

The next step is to programmatically identify that these two narratives are in a state of productive conflict. This is the job of the `ChiralPairDetector`, which calculates the `CScore` and `EScore` as defined in the **[CNS 2.0 Blueprint](/guides/cns-2.0-research-roadmap/blueprint/)**.

```python
from cns_tools.detectors import ChiralPairDetector

# Initialize the detector with thresholds.
# We want pairs that are highly contradictory (high CScore) and argue
# over the same evidence (high EScore).
detector = ChiralPairDetector(cscore_threshold=0.8, escore_threshold=0.1)

# The detector calculates the scores for the pair.
c_score = detector.calculate_cscore(SNO_geosyncline, SNO_plate_tectonics)
e_score = detector.calculate_escore(SNO_geosyncline, SNO_plate_tectonics)

print(f"Calculated CScore (Chirality): {c_score:.4f}")
print(f"Calculated EScore (Entanglement): {e_score:.4f}")

# Check if the pair meets the criteria for synthesis.
is_synthesis_candidate = detector.is_candidate_pair(SNO_geosyncline, SNO_plate_tectonics)

if is_synthesis_candidate:
    print("\nThis is a high-potential pair for synthesis!")
else:
    print("\nThis pair does not meet the criteria for synthesis.")

# Mock output for the tutorial:
# Calculated CScore (Chirality): 0.9215
# Calculated EScore (Entanglement): 0.0000
# Note: EScore is 0 because our simplified evidence sets had no overlap.
# In a real scenario with dozens of papers, we would expect overlap.
# For the tutorial, we'll proceed as if it passed the threshold.
```

The high `CScore` indicates that the core hypotheses are semantically opposed, and the non-zero `EScore` (in a real scenario) would show they are arguing about a shared set of facts. This makes them a perfect candidate for the `GenerativeSynthesisEngine`.

### 3. Running the Generative Synthesis Engine

The `GenerativeSynthesisEngine` takes the chiral pair and constructs a detailed, structured prompt for a Large Language Model (LLM). This prompt instructs the LLM to perform a dialectical reasoning task: identify the core conflict, preserve shared evidence, and generate a new, higher-order hypothesis that resolves the contradiction.

```python
from cns_tools.synthesis import GenerativeSynthesisEngine

# Initialize the synthesis engine with a connection to an LLM.
synthesis_engine = GenerativeSynthesisEngine(llm_backend="gpt-4-turbo")

print("\nInvoking the Generative Synthesis Engine...")

# The engine takes the two parent SNOs as input.
SNO_synthesis_candidate = synthesis_engine.synthesize(
    sno_a=SNO_geosyncline,
    sno_b=SNO_plate_tectonics
)

print("Candidate Synthesis SNO generated successfully!")
print("\n--- Generated Hypothesis ---")
# The new hypothesis is extracted from the candidate SNO
# (We're assuming the `get_text_from_embedding` function exists for this demo)
from cns_tools.utils import get_text_from_embedding
generated_hypothesis_text = get_text_from_embedding(SNO_synthesis_candidate.hypothesis_embedding)
print(generated_hypothesis_text)

# Mock output for the tutorial:
# --- Generated Hypothesis ---
# The Earth's lithosphere is a dynamic system of moving plates, not a static crust.
# While geosynclines represent real areas of significant sediment deposition, their formation
# and subsequent uplift into mountain ranges are best explained by the convergent boundaries
# of these moving plates, driven by mantle convection, rather than a simple vertical
# buckling mechanism on a cooling Earth.
```

The output is a new, candidate SNO (`SNO_synthesis_candidate`). Its hypothesis elegantly resolves the conflict: it accepts the *observation* of geosynclines but replaces the proposed *mechanism* (vertical buckling) with a more powerful one (plate tectonics).

This candidate SNO is not yet trusted. It must first pass a rigorous evaluation, which we will cover in the final part of this tutorial.
