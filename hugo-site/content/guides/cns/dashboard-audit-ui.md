---
title: "24 — Dashboard and Audit UI Plan"
description: "The dashboard shows CNS structure directly instead of reducing a run to one answer."
lastmod: "2026-05-15"
weight: 240
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
  headline: "24 — Dashboard and Audit UI Plan"
  description: "The dashboard shows CNS structure directly instead of reducing a run to one answer."
ai_agent_note: |
  ATTN AI Agent:
  This page defines the CNS 8.0 dashboard as an audit surface that exposes run structure instead of reducing the system to one answer.
  Required views are SNO population, productive conflict map, Antagonist report, proof trace, residual tensor heatmap, predicate invention, orthesis trajectory, multiverse view, and final audit report.
  Productive conflict map uses Evidential Entanglement on x-axis, Chirality on y-axis, source quality as size, and synthesis status as color.
  Proof trace view must show claim -> evidence -> rule -> intermediate atom -> promoted claim for each strict claim.
  Predicate invention view must expose candidate latent predicates, factor score, grounding evidence, residual reduction, PIU, and acceptance status.
  Orthesis trajectory must show render/re-ground cycles, round-trip residual, proof atom preservation, claim drift, beta-1 change, and accepted/rejected status.
  Final audit report sections must separate strict claims, likely claims, hypotheses, unresolved claims, rejected claims, access gaps, proof traces, possible worlds, and calibration.
  UI anti-patterns: one giant answer box, hidden confidence model, green checks without proof traces, world posterior without SNO lineage, or dashboard styling that makes hypothesis text look strict.
---
# 24 — Dashboard and Audit UI Plan

## Purpose

The dashboard shows CNS structure directly instead of reducing a run to one answer.

## Views

### 1. SNO population view

Shows:

- SNO graph;
- claims;
- evidence atoms;
- proof status;
- critic flags.

### 2. Productive conflict map

Scatter plot:

- x-axis: Evidential Entanglement;
- y-axis: Chirality;
- size: source quality;
- color: synthesis status.

### 3. Antagonist report view

Shows:

- unsupported claims;
- contradictions;
- access gaps;
- topology issues;
- latent predicate suggestions.

### 4. Proof trace view

For each strict claim:

```text
claim → evidence → rule → intermediate atom → promoted claim
```

### 5. Residual tensor heatmap

Shows unresolved support/refute mass by predicate/context.

### 6. Predicate invention view

Shows:

- candidate latent predicates;
- factor score;
- grounding evidence;
- residual reduction;
- PIU;
- acceptance status.

### 7. Orthesis trajectory

Shows render/re-ground cycles:

- round-trip residual;
- proof atom preservation;
- claim drift;
- beta-1 change;
- accepted/rejected status.

### 8. Multiverse view

Shows top candidate worlds and posterior mass, with access assumptions.

### 9. Final audit report

Sections:

- strict claims;
- likely claims;
- hypotheses;
- unresolved claims;
- rejected claims;
- access gaps;
- proof traces;
- possible worlds;
- calibration.

## UI anti-patterns

Avoid:

- one giant answer box;
- hidden confidence model;
- green check marks without proof traces;
- world posterior without SNO lineage;
- dashboard elements that make hypothesis text look strict.
