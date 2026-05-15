---
title: "19 — Runtime Oracle Boundary Policy"
description: "CNS 8.0 can use oracles during training and evaluation. Runtime analysis cannot use hidden labels, answer keys, or LLM judgments."
lastmod: "2026-05-15"
weight: 190
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
  headline: "19 — Runtime Oracle Boundary Policy"
  description: "CNS 8.0 can use oracles during training and evaluation. Runtime analysis cannot use hidden labels, answer keys, or LLM judgments."
ai_agent_note: |
  ATTN AI Agent:
  This page defines the CNS 8.0 oracle boundary: oracles may be used during training/evaluation, but runtime analysis cannot use hidden labels, answer keys, synthetic generator parameters, withheld rationales, hidden evaluator calls, or LLM judges as final truth oracles.
  Allowed offline oracle use includes SciFact/FEVER/synthetic labels, expert annotations, calibration labels, human review labels, synthetic hidden-context labels for evaluation, and gold rationales for extraction training.
  Every run manifest must record dataset split hash, label availability, prompt templates, model IDs, proof rule version, calibration model version, oracle-use declaration, and leakage scan result.
  Leakage checks include prompt scans for label fields, runtime input schema excluding gold labels, random-label controls, shuffled-evidence controls, isolated synthetic seeds, and withholding latent context variables during inference.
  Output language must keep strict, likely, hypothesis, unresolved, and rejected separate.
  Human review is a post-runtime annotation unless explicitly fed into retraining or calibration.
---
# 19 — Runtime Oracle Boundary Policy

## Policy

CNS 8.0 can use oracles during training and evaluation. Runtime analysis cannot use hidden labels, answer keys, or LLM judgments.

## Allowed offline oracle use

- labels in SciFact, FEVER, and synthetic tasks;
- expert annotations;
- calibration labels;
- human review labels;
- synthetic hidden context labels for evaluation;
- gold rationales for training extraction.

## Forbidden runtime oracle use

- answer keys;
- gold labels in prompts;
- synthetic generation parameters;
- LLM judge as final truth oracle;
- access to withheld test rationales;
- hidden evaluator calls inside runtime;
- prompting that asks a model to choose the correct label using unseen gold data.

## Required metadata

Every run manifest records:

- dataset split hash;
- label availability;
- prompt templates;
- model IDs;
- proof rule version;
- calibration model version;
- oracle-use declaration;
- leakage scan result.

## Leakage checks

- scan prompts for label fields;
- verify runtime input schema excludes gold labels;
- run random-label controls;
- run shuffled-evidence controls;
- isolate synthetic generator seeds;
- withhold latent context variables during inference.

## Output language

CNS keeps likely claims separate from strict claims.

Allowed:

```text
Strict: follows from proof trace.
Likely: posterior-supported but not strict.
Hypothesis: generated for testing.
Unresolved: evidence/access insufficient.
Rejected: failed gate.
```

## Human review

Human experts may review outputs. Their judgments are post-runtime annotations unless explicitly used in a retraining/calibration step.
