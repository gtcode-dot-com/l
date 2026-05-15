---
title: "Runtime Configuration"
description: "CNS 8.0 MVP runtime configuration from the source package."
lastmod: "2026-05-15"
weight: 330
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
  headline: "Runtime Configuration"
  description: "CNS 8.0 MVP runtime configuration from the source package."
ai_agent_note: |
  ATTN AI Agent:
  This page shows the CNS 8.0 MVP config file configs/cns8_mvp.yaml and its run-affecting defaults.
  Evidence config chunks at 800 chars with 120 overlap, requires hashes, and defaults access_state to available.
  Extraction uses prompt backend, sno8 schema, max_retries=2, and fail_closed_on_invalid_citation=true.
  Grounding uses an NLI/cross-encoder placeholder with strict entailment threshold 0.75, likely threshold 0.55, and citation validity required for strict claims.
  Chirality weights are graph 0.30, evidence_polarity 0.30, language_logic 0.25, entanglement_interaction 0.15, with productive_conflict_threshold 0.60.
  Proof config allows only zero-temperature rules to promote strict claims, targets ZTHR 0.0, and records proof checksums.
  Predicate invention is enabled with max 5 latent predicates, PIU threshold 0.05, complexity penalty 1.0, and grounding required.
  Orthesis allows 3 round trips, residual threshold 0.10, beta1 reduction target 0.30, and preserved residuals; multiverse max_worlds=10; oracle boundary forbids runtime labels and runs leakage scans; LLM truth vote is false.
---
# Runtime Configuration

## configs/cns8_mvp.yaml

````yaml
version: "8.0"

evidence:
  chunk_chars: 800
  overlap_chars: 120
  require_hashes: true
  default_access_state: available

extraction:
  backend: prompt
  schema: schemas/sno8.schema.json
  max_retries: 2
  fail_closed_on_invalid_citation: true

grounding:
  entailment_model: "cross-encoder/nli-placeholder"
  strict_entailment_threshold: 0.75
  likely_entailment_threshold: 0.55
  citation_validity_required_for_strict: true

chirality:
  weights:
    graph: 0.30
    evidence_polarity: 0.30
    language_logic: 0.25
    entanglement_interaction: 0.15
  productive_conflict_threshold: 0.60

proof:
  zero_temperature_rules_only_promote_strict: true
  zthr_target: 0.0
  record_proof_checksums: true

predicate_invention:
  enabled: true
  max_latent_predicates: 5
  piu_threshold: 0.05
  complexity_penalty: 1.0
  require_grounding: true

orthesis:
  max_round_trips: 3
  roundtrip_residual_threshold: 0.10
  beta1_reduction_target: 0.30
  allow_preserved_residuals: true

multiverse:
  enabled: true
  max_worlds: 10
  posterior_temperature: 1.0

oracle_boundary:
  allow_training_oracles: true
  forbid_runtime_labels: true
  run_leakage_scan: true

llm:
  proposer_model: "model-placeholder"
  antagonist_model: "model-placeholder"
  synthesizer_model: "model-placeholder"
  use_llm_truth_vote: false
````
