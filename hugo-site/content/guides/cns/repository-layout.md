---
title: "25 — Repository Layout"
description: "schema and evidence store; SNO parser and validator; critics; pair selector; proof closure; predicate invention; Synthesizer; orthesis loop; audit report; dashboard."
lastmod: "2026-05-15"
weight: 250
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
  headline: "25 — Repository Layout"
  description: "schema and evidence store; SNO parser and validator; critics; pair selector; proof closure; predicate invention; Synthesizer; orthesis loop; audit report; dashboard."
ai_agent_note: |
  ATTN AI Agent:
  This page proposes the CNS 8.0 repository structure and build sequence, not conceptual definitions.
  Package layout places configs/cns8_mvp.yaml and cns8/ modules for evidence, sno, agents, critics, tensor, worlds, reports, and runtime.
  Evidence modules cover store/atom/access; SNO modules cover model/parser/align; agents cover proposer/antagonist/synthesizer/orthesist/auditor; critics cover grounding/logic/topology/chirality/access/calibration.
  Tensor modules cover rules, closure, proof, residual, and predicate_invention; worlds cover build/rank/calibration; reports cover audit/markdown; runtime covers manifest/oracle_boundary.
  Required tests include evidence store, SNO schema, citation validation, zero-temp closure, chirality/entanglement, synthetic predicate invention, and orthesis loop.
  Build sequence is schema/evidence store -> SNO parser -> critics -> pair selector -> proof closure -> predicate invention -> Synthesizer -> orthesis loop -> audit report -> dashboard.
  Test-first rule: each new CNS mechanism gets a deterministic toy test before LLM integration; LLM modules are adapters and the package must run in deterministic toy mode with no LLM API calls.
---
# 25 — Repository Layout

## Recommended project structure

```text
cns8/
  pyproject.toml
  README.md
  configs/
    cns8_mvp.yaml
  cns8/
    evidence/
      store.py
      atom.py
      access.py
    sno/
      model.py
      parser.py
      align.py
    agents/
      proposer.py
      antagonist.py
      synthesizer.py
      orthesist.py
      auditor.py
    critics/
      grounding.py
      logic.py
      topology.py
      chirality.py
      access.py
      calibration.py
    tensor/
      rules.py
      closure.py
      proof.py
      residual.py
      predicate_invention.py
    worlds/
      build.py
      rank.py
      calibration.py
    reports/
      audit.py
      markdown.py
    runtime/
      manifest.py
      oracle_boundary.py
  tests/
    test_evidence_store.py
    test_sno_schema.py
    test_citation_validation.py
    test_zero_temp_closure.py
    test_chirality_entanglement.py
    test_predicate_invention_synthetic.py
    test_orthesis_loop.py
  experiments/
    synthetic_latent_context/
    scifact_grounding/
    productive_pair_selection/
  docs/
```

## Build sequencing

1. schema and evidence store;
2. SNO parser and validator;
3. critics;
4. pair selector;
5. proof closure;
6. predicate invention;
7. Synthesizer;
8. orthesis loop;
9. audit report;
10. dashboard.

## Test-first rule

Each new CNS mechanism gets a toy deterministic test before LLM integration.

## LLM isolation

The package should run in deterministic toy mode without any LLM API calls. LLM modules are adapters, not core proof machinery.
