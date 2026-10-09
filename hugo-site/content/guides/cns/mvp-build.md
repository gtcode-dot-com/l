---
title: "20 — MVP Build Checklist"
description: "Small evidence corpus prepared. Synthetic latent-context dataset generated. Train/dev/test split hashes recorded. Gold labels isolated from runtime."
lastmod: "2026-05-15"
weight: 200
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
  headline: "20 — MVP Build Checklist"
  description: "Small evidence corpus prepared. Synthetic latent-context dataset generated. Train/dev/test split hashes recorded. Gold labels isolated from runtime."
ai_agent_note: |
  ATTN AI Agent:
  This page is a checkbox build checklist for the CNS 8.0 MVP, organized by dataset, evidence, SNO extraction, critics, pair selection, proof closure, predicate invention, synthesis, orthesis, and audit.
  Dataset requirements are small evidence corpus, synthetic latent-context dataset, train/dev/test split hashes, and gold labels isolated from runtime.
  Evidence requirements are atom creation, stable IDs/hashes, access states, and citation lookup; SNO extraction requires schema, claim/relation extraction, and malformed-output parser tests.
  Critics to build: citation validator, entailment scorer, logic critic, topology critic, access critic, and chirality critic.
  Pair-selection checklist includes Evidential Entanglement, graph chirality, evidence-polarity chirality, Productive Conflict Score, and pair-selection report.
  Proof/predicate/synthesis/orthesis checklist includes rule registry, zero-temperature closure, proof traces, ZTHR, residual tensor, factorization, predicate grounding, PIU, Synthesizer prompt/schema, proof/reference preservation, residual preservation, render/re-ground loop, round-trip residual, stability threshold, and orthesis report.
  Audit output must separate strict/likely/hypothesis/unresolved/rejected and include top worlds, access gaps, proof trace links, latent predicate status, and calibration; stop condition says do not scale to a large multi-agent runtime until the toy-data SNO -> Antagonist -> proof -> predicate invention -> Synthesizer -> orthesis loop works.
---
# 20 — MVP Build Checklist

## Dataset

- [ ] Small evidence corpus prepared.
- [ ] Synthetic latent-context dataset generated.
- [ ] Train/dev/test split hashes recorded.
- [ ] Gold labels isolated from runtime.

## Evidence

- [ ] Evidence atoms created.
- [ ] Stable IDs and hashes.
- [ ] Access states attached.
- [ ] Citation lookup tested.

## SNO extraction

- [ ] Candidate SNO schema implemented.
- [ ] Claim extraction prompt or model.
- [ ] Relation extraction prompt or model.
- [ ] Parser tests for malformed output.

## Critics

- [ ] Citation validator.
- [ ] Entailment scorer.
- [ ] Logic critic.
- [ ] Topology critic.
- [ ] Access critic.
- [ ] Chirality critic.

## Pair selection

- [ ] Evidential Entanglement score.
- [ ] Graph chirality.
- [ ] Evidence-polarity chirality.
- [ ] Productive Conflict Score.
- [ ] Pair-selection report.

## Proof closure

- [ ] Rule registry.
- [ ] Zero-temperature closure.
- [ ] Proof trace generation.
- [ ] ZTHR metric.

## Predicate invention

- [ ] Residual tensor builder.
- [ ] Factorization routine.
- [ ] Candidate predicate labels.
- [ ] Predicate grounding tests.
- [ ] PIU metric.

## Synthesis

- [ ] Synthesizer prompt.
- [ ] Synthesized SNO schema.
- [ ] Proof/reference preservation.
- [ ] Residual contradiction preservation.

## Orthesis

- [ ] Render/re-ground loop.
- [ ] Round-trip residual.
- [ ] Stability threshold.
- [ ] Orthesis report.

## Audit

- [ ] strict/likely/hypothesis/unresolved/rejected sections.
- [ ] top worlds.
- [ ] access gaps.
- [ ] proof trace links.
- [ ] latent predicate status.
- [ ] calibration report.

## Stop condition

Do not expand to large multi-agent runtime until the SNO → Antagonist → proof → predicate invention → Synthesizer → orthesis loop works on toy data.
