---
title: "GCTS MVP Build"
description: "A practical implementation path for building the first access-aware likely-truth engine without full custom model training."
lastmod: "2026-05-13"
weight: 5
meta_description: "MVP build plan for CNS 7.1 / GCTS: extraction, evidence linking, access-state modeling, tensor logic, world ranking, calibration, and reports."
---

The GCTS MVP can be built without full custom model training. The first target
is an auditable likely-truth engine that accepts a bounded corpus, extracts
evidence and claims, models access states, enumerates worlds, and emits ranked
reports.

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
evidence linking, access-state classification, and calibration rather than
direct runtime truth judgment.

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

## Implementation Boundary

The MVP is a bounded, auditable decision support prototype for testing GCTS
under controlled evidence and access conditions. It should say when evidence is
insufficient, when a claim is record-contingent, and what record production
would change the result.
