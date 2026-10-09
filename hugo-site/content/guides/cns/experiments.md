---
title: "12 — Experiment and Evaluation Plan"
description: "Test whether contradiction-driven predicate invention recovers hidden context variables."
lastmod: "2026-05-15"
weight: 120
math: true
meta_keywords:
  - CNS 8.0
  - Chiral Narrative Synthesis
  - Grounded Dialectical Orthesis
  - Structured Narrative Objects
  - orthesis
  - tensor logic
  - predicate invention
  - chiral conflict
structured_data_webpage:
  type: Article
  headline: "12 — Experiment and Evaluation Plan"
  description: "Test whether contradiction-driven predicate invention recovers hidden context variables."
ai_agent_note: |
  ATTN AI Agent:
  This page lays out seven CNS 8.0 experiments: synthetic latent-context recovery, productive conflict selection, grounded synthesis on SciFact/FEVER, orthesis round-trip stability, topology versus synthesis difficulty, oracle-boundary audit, and ablation suite.
  Experiment 1 tests whether contradiction-driven predicate invention recovers hidden variables such as time, subgroup, measurement method, jurisdiction, dosage, source condition, or definition boundary; metrics include latent-predicate F1, residual-energy reduction, PIU, orthesis acceptance rate, and false-predicate rate.
  Baselines include RAG summary, LLM debate, claim-level fact verification, possible-world ranking without predicate invention, and CNS without chirality/entanglement pair selection.
  Productive Conflict Score is tested on SNO pairs for agreement over shared evidence, disagreement over shared evidence, unrelated-evidence disagreement, unrelated topics, and extraction-error conflicts.
  Orthesis stability is measured by render -> re-extract -> align proof-critical atoms -> compute chi_LL over repeated cycles; topology experiments use beta-1, persistence, chiral tensor norm, residual energy, difficulty, and iteration count.
  Oracle-boundary audit checks prompt label leakage, split contamination, synthetic generator leakage, LLM judge truth-vote leakage, and metadata separation.
  Minimum publishable result requires synthetic latent-context recovery, proof-trace examples, pair selection beating baselines, zero ZTHR on constrained strict claims, round-trip residual reduction, and ablations showing predicate invention and entanglement matter.
---
# 12 — Experiment and Evaluation Plan

## Experiment 1 — Synthetic latent-context recovery

### Goal

Test whether contradiction-driven predicate invention recovers hidden context variables.

### Dataset

Generate examples with claims that appear contradictory until a hidden variable is introduced:

- time;
- subgroup;
- measurement method;
- jurisdiction;
- dosage;
- source condition;
- definition boundary.

### Baselines

- RAG summary;
- LLM debate;
- claim-level fact verification;
- possible-world ranking without predicate invention;
- CNS without chirality/entanglement pair selection.

### Metrics

- latent predicate recovery F1;
- residual energy reduction;
- PIU;
- orthesis acceptance rate;
- false predicate rate.

## Experiment 2 — Productive conflict selection

### Goal

Test whether Productive Conflict Score selects better synthesis pairs than baselines.

### Data

Construct SNO pairs with known categories:

1. agreement over shared evidence;
2. disagreement over shared evidence;
3. disagreement over unrelated evidence;
4. unrelated topics;
5. extraction-error conflicts.

### Metrics

- pair-selection precision@k;
- synthesis yield;
- critic failure rate;
- human or oracle-rated productive conflict label.

## Experiment 3 — Grounded synthesis on SciFact/FEVER

### Goal

Evaluate evidence-grounded extraction and synthesis under known labels.

### Tasks

- extract SNOs from evidence;
- verify citations and entailment;
- identify support/refute contradictions;
- generate constrained synthesis when applicable.

### Metrics

- citation validity;
- rationale recovery;
- entailment score;
- label accuracy as diagnostic;
- strict-claim ZTHR;
- proof trace completeness.

## Experiment 4 — Orthesis round-trip stability

### Goal

Measure whether synthesized SNOs survive render/re-ground cycles.

### Protocol

For each synthesized SNO:

1. render to natural language;
2. re-extract SNO;
3. align proof-critical atoms;
4. compute $\chi_{LL}$;
5. repeat for $n$ cycles.

### Metrics

- round-trip residual;
- proof atom preservation;
- claim drift;
- evidence drift;
- orthesis convergence rate.

## Experiment 5 — Topology and synthesis difficulty

### Goal

Test whether topology metrics predict synthesis difficulty.

### Metrics

- $\beta_1$ before/after synthesis;
- persistence features;
- chiral tensor norm;
- residual energy;
- human-rated difficulty;
- number of synthesis iterations.

Hypothesis: chirality + entanglement + residual topology predicts difficulty better than embedding distance.

## Experiment 6 — Oracle-boundary audit

### Goal

Ensure runtime does not use training labels or hidden gold states.

### Checks

- prompt label leakage;
- dataset split contamination;
- synthetic generator parameter leakage;
- LLM judge truth-vote leakage;
- calibration/training metadata separation.

## Experiment 7 — Ablation suite

Ablate:

- Antagonist;
- Evidential Entanglement;
- graph chirality;
- language–logic round-trip;
- tensor proof closure;
- predicate invention;
- access states;
- possible-world posterior;
- orthesis loop.

## Statistical reporting

Report:

- bootstrap confidence intervals;
- effect sizes;
- calibration curves;
- per-domain breakdown;
- failure taxonomy;
- examples with proof traces.

## Minimum publishable result

A strong first paper needs:

1. synthetic latent context recovery;
2. proof-trace examples;
3. pair selection outperforming baselines;
4. strict zero-temperature hallucination rate of zero on constrained subset;
5. orthesis round-trip residual reduction;
6. ablation showing predicate invention and entanglement matter.
