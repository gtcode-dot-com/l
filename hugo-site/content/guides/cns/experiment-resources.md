---
title: "Experiment Resource Files"
description: "Experiment matrix and ablation suite definitions for CNS 8.0."
lastmod: "2026-05-15"
weight: 340
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
  headline: "Experiment Resource Files"
  description: "Experiment matrix and ablation suite definitions for CNS 8.0."
ai_agent_note: |
  ATTN AI Agent:
  This page contains the CNS 8.0 experiment_matrix.yaml and ablation_suite.yaml definitions.
  Experiment matrix includes E1 latent-context recovery on synthetic contradictions with RAG/debate/possible-world-only/no-predicate baselines and latent_f1/residual_energy_reduction/PIU/false_predicate_rate metrics.
  E2 tests chirality + entanglement pair selection against embedding distance, contradiction-only, and evidence-overlap-only baselines using precision_at_10, synthesis_yield, and critic_failure_rate.
  E3 validates extraction/grounding on SciFact and FEVER with citation_validity, entailment, rationale_recovery, and ZTHR.
  E4 tests orthesis render/re-ground stability against ordinary summaries, debate summaries, and no-orthesis CNS using roundtrip_residual, proof_atom_preservation, and claim_drift.
  E5 tests topology/chirality as synthesis-difficulty predictors against embedding distance, beta1_only, and contradiction_count using difficulty_auc, beta1_reduction, residual_energy, and iterations_to_converge.
  Ablations remove antagonist, evidential_entanglement, graph_chirality, language_logic_roundtrip, tensor_proof_closure, predicate_invention, access_states, possible_worlds, or orthesis_loop, each with expected failure modes.
---
# Experiment Resource Files

## experiments/experiment_matrix.yaml

````yaml
experiments:
  - id: E1_latent_context_recovery
    goal: recover hidden context predicates from synthetic contradictions
    datasets: [synthetic_latent_context]
    baselines: [rag_summary, llm_debate, possible_world_only, cns_no_predicate_invention]
    metrics: [latent_f1, residual_energy_reduction, piu, false_predicate_rate]

  - id: E2_productive_conflict_selection
    goal: test chirality + entanglement pair selector
    datasets: [synthetic_sno_pairs, argument_pairs]
    baselines: [embedding_distance, contradiction_only, evidence_overlap_only]
    metrics: [precision_at_10, synthesis_yield, critic_failure_rate]

  - id: E3_grounded_fact_verification
    goal: validate extraction/grounding on known datasets
    datasets: [scifact, fever]
    baselines: [rag, claim_verifier, llm_extractor]
    metrics: [citation_validity, entailment, rationale_recovery, zthr]

  - id: E4_orthesis_roundtrip
    goal: test render/reground stability
    datasets: [synthetic_sno_pairs, scifact_synthesis_subset]
    baselines: [ordinary_summary, debate_summary, cns_no_orthesis]
    metrics: [roundtrip_residual, proof_atom_preservation, claim_drift]

  - id: E5_topology_difficulty
    goal: test whether topology and chirality predict synthesis difficulty
    datasets: [synthetic_topology, argument_pairs]
    baselines: [embedding_distance, beta1_only, contradiction_count]
    metrics: [difficulty_auc, beta1_reduction, residual_energy, iterations_to_converge]
````

## experiments/ablation_suite.yaml

````yaml
ablations:
  - remove: antagonist
    expected_failure: fewer detected contradictions, higher unsupported synthesis
  - remove: evidential_entanglement
    expected_failure: selects unrelated disagreements
  - remove: graph_chirality
    expected_failure: misses structural opposition
  - remove: language_logic_roundtrip
    expected_failure: fluent but unstable renderings
  - remove: tensor_proof_closure
    expected_failure: strict claims without machine-checkable proof
  - remove: predicate_invention
    expected_failure: persistent contradictions remain unresolved
  - remove: access_states
    expected_failure: missing records misinterpreted as evidence
  - remove: possible_worlds
    expected_failure: weaker uncertainty reporting
  - remove: orthesis_loop
    expected_failure: synthesized SNO drifts after re-grounding
````
