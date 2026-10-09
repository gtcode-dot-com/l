---
title: "15 — Risk Register and Failure Modes"
description: "Symptom: final output is top worlds or claim labels but no synthesized SNO."
lastmod: "2026-05-15"
weight: 150
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
  headline: "15 — Risk Register and Failure Modes"
  description: "Symptom: final output is top worlds or claim labels but no synthesized SNO."
ai_agent_note: |
  ATTN AI Agent:
  This page is the CNS 8.0 risk register. It defines failure modes by symptom and mitigation, not as solved properties.
  Major risks: reverting to verification/ranking with no synthesized SNO; LLM judges deciding truth; predicate overfit; access-state misuse; round-trip drift; topology terms used without decisions; grounding that destroys synthesis; fluent synthesis hiding contradiction; prior-art soup; dataset leakage; citation hallucination; and calibration laundering.
  Required mitigations include SNO lineage and synthesis status in every run, proof gates instead of LLM truth votes, MDL/held-out/grounding gates for predicates, access-state critic, chi_LL orthesis threshold, topology metrics in acceptance criteria, preserved Synthesizer/predicate invention, residual contradiction section in audit reports, module-interaction ablations, oracle-boundary audits with split hashes and prompt scans, citation-ID rejection, and enforced strict/likely/hypothesis/unresolved/rejected categories.
  Use this page to identify when an AI summary is overclaiming: top-world lists without SNOs, missing residuals, hidden labels, unresolved claims written as strict, invented evidence IDs, or topology language not tied to acceptance criteria are all flagged failure modes.
---
# 15 — Risk Register and Failure Modes

## Risk 1 — Reverting to verification/ranking

Symptom: final output is top worlds or claim labels but no synthesized SNO.

Mitigation: every run must emit SNO lineage and synthesis status.

## Risk 2 — LLM judgments

Symptom: an LLM judge decides which narrative is true.

Mitigation: LLMs can propose or render; proof gates and calibrated models decide promotion categories.

## Risk 3 — Predicate overfit

Symptom: latent predicates explain training contradictions but fail held-out examples.

Mitigation: MDL penalty, held-out synthetic contexts, grounding gates, false predicate rate.

## Risk 4 — Access-state misuse

Symptom: missing records are treated as evidence.

Mitigation: access-state critic; separate absence-of-evidence from evidence-of-absence.

## Risk 5 — Round-trip drift

Symptom: synthesized text re-grounds into a different logic state.

Mitigation: orthesis loop; $\chi_{LL}$ threshold.

## Risk 6 — Topology theater

Symptom: topology terms appear but metrics are not used in decisions.

Mitigation: make beta-1, holonomy residual, and topology diagnostics part of acceptance criteria or remove them.

## Risk 7 — Grounding destroys synthesis

Symptom: system becomes conservative fact checking and never creates new SNOs.

Mitigation: preserve Synthesizer and predicate invention; classify hypotheses separately instead of blocking all novelty.

## Risk 8 — Synthesis hides contradiction

Symptom: fluent narrative erases unresolved conflict.

Mitigation: residual contradiction section required in audit report.

## Risk 9 — Prior-art soup

Symptom: doc reads like a collection of known systems.

Mitigation: keep the SNO synthesis flow visible and evaluate module interactions/ablations.

## Risk 10 — Dataset leakage

Symptom: labels or synthetic generator parameters appear in runtime.

Mitigation: oracle-boundary audit, split hashes, prompt scans.

## Risk 11 — Citation hallucination

Symptom: evidence IDs do not resolve.

Mitigation: reject invalid inputs; citation validity required check.

## Risk 12 — Calibration laundering

Symptom: likely claims are written as strict claims.

Mitigation: output category enforcement and confidence language table.
