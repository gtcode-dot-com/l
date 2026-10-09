---
title: "GCTS MVP Build"
description: "A practical implementation path for building the first access-aware likely-truth engine without full custom model training."
lastmod: "2026-05-15"
weight: 8
meta_description: "MVP build plan for CNS 7.1 / GCTS: extraction, evidence linking, access-state modeling, rule closure, world ranking, calibration, audit reports, and product boundary."
ai_agent_note: |
  ATTN AI Agent:
  This page defines the GCTS MVP as an auditable decision-support prototype, not a validated full system, and says it can be built without full custom model training.
  Product boundary is an Evidence Accountability Workbench for analysts handling incomplete records: investigative researchers, legal support, compliance, journalists, auditors, and intelligence-style teams.
  Phase 1 uses LLMs for extraction/suggestions/rendering, retrieval plus citation validation, NLI entailment, access modeling for expected records/control/non-production, monotone tensor-logic rule compiler, candidate-world enumeration/beam search, calibration, and dashboard; direct runtime truth judgment stays outside generation.
  Runtime data products are evidence atoms, record-access states, institutional incentive profiles, claims/relations, rules/proof traces, world views, posterior/confidence reports, and rendered synthesis reports.
  API surface: POST /runs, GET run status, evidence, access, worlds, claims, and report.
  MVP gates include 100% resolvable strict citations, zero strict claims without proof traces, ECE <=0.10 on held-out verification, top-3 world coverage >=85% on synthetic latent-context tasks, measurable chirality/difficulty relation, access-state calibration on suppression tasks, explicit unsupported/record_contingent/conflicted/rejected distinction, and ablations beating RAG/debate baselines.
  First demo must show the same evidence under available, inaccessible, withheld, not-generated, and evidence-of-absence access states with visible status differences and separate strict proof, likely-truth posterior, and confidence.
---

The GCTS MVP can be built without full custom model training. The first target
is an auditable decision-support prototype that accepts a bounded corpus,
extracts evidence and claims, models access states, enumerates worlds, and emits
ranked reports.

## Product Boundary

The MVP should be an **Evidence Accountability Workbench** focused on auditable
evidence operations. The first useful product should help analysts organize
evidence, identify record contingencies, preserve contradiction, and report what
records would change the analysis.

Initial users:

- investigative researchers;
- legal support teams;
- compliance analysts;
- journalists handling incomplete records;
- internal auditors;
- intelligence-style analytic teams.

## Phase 1: Local Prototype

Use existing models and explicit schemas:

- LLMs for candidate extraction, latent-context suggestions, access-hypothesis
  suggestions, and rendering.
- Retrieval plus citation validation for evidence grounding.
- NLI or entailment models for claim-evidence scoring.
- A small evidence-access model for expected record existence, availability,
  control, and non-production.
- A rule compiler for a monotone tensor-logic core.
- Candidate-world enumeration or beam search.
- Calibration data to map evidence, access, incentive, and contradiction
  signals to probabilities.
- A dashboard to expose world rankings, proof traces, record-access states,
  uncertainty, and next evidence.

Fine-tuning is optional in Phase 1. If used, it should target extraction,
evidence linking, access-state classification, and calibration. Direct runtime
truth judgment stays outside model generation.

## Runtime Data Products

The MVP should persist:

- evidence atoms;
- record-access states;
- institutional incentive profiles;
- claims and relations;
- rules and proof traces;
- world views;
- posterior and confidence reports;
- rendered synthesis reports.

## API Surface

The first API should expose:

- `POST /runs` to create a synthesis run from a corpus manifest;
- `GET /runs/{id}` for run status;
- `GET /runs/{id}/evidence` for evidence atoms;
- `GET /runs/{id}/access` for record-access states;
- `GET /runs/{id}/worlds` for top-K possible worlds;
- `GET /runs/{id}/claims` for claim rankings and statuses;
- `GET /runs/{id}/report` for the rendered report.

## MVP Gates

The first build succeeds only if it reaches:

- 100% resolvable citations for promoted strict claims;
- zero promoted zero-temperature claims without proof traces;
- calibrated claim probabilities with ECE at or below 0.10 on held-out
  verification tasks;
- top-3 world coverage at or above 85% on synthetic latent-context tasks;
- measurable chirality correlation with synthesis difficulty;
- measurable access-state calibration on adversarial record-suppression tasks;
- explicit distinction between `unsupported`, `record_contingent`,
  `conflicted`, and `rejected`;
- ablation evidence that multiverse/proof/access scoring beats simple RAG and
  LLM debate baselines on grounding, uncertainty quality, and likely-truth
  ranking.

## First Repository Shape

```text
gcts-prototype/
  gcts/
    schemas.py
    access_states.py
    rules.py
    worlds.py
    scoring.py
    statuses.py
    audit.py
  examples/
    facility_incident/
      evidence.json
      records.json
      claims.json
  outputs/
  README.md
```

## First Demonstration

The first demo should show the same evidence under different access states:

1. Available record.
2. Inaccessible record.
3. Withheld record.
4. Not-generated record.
5. Evidence of absence.

The expected result is a visible status difference across runs, with strict
proof, likely-truth posterior, and confidence reported separately.
