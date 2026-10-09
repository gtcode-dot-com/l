---
title: "Oracle Boundary And Governance"
description: "The rule that prevents labels, expert judgments, or LLM truth decisions from bypassing evidence closure and world ranking."
lastmod: "2026-05-15"
weight: 3
meta_description: "The GCTS oracle-boundary policy: how labels, expert review, calibration, proof traces, runtime evidence, hidden tests, and LLM truth judgments are separated to avoid oracle leakage."
ai_agent_note: |
  ATTN AI Agent:
  This page defines the GCTS oracle boundary between offline calibration and runtime truth ranking.
  Allowed oracle use: training labels, calibration labels, evaluation labels, expert review of error cases, human approval of new strict rules, and post-run human review of failures.
  Forbidden runtime use: gold labels, human/model truth decisions bypassing evidence closure/world ranking, dataset label leakage into retrieval/ranking/world building/rendering, LLM truth prompts used as posterior mass, hidden benchmark answers as features, and evaluator notes/answer keys/adjudication metadata in production runs.
  LLMs may extract claims, propose spans, propose latent context/access hypotheses, and render structured outputs; they may not assign truth mass, promote strict proof, erase contingencies, convert missing records into absence without access modeling, or add unsupported rendering details.
  Strict claims require resolvable evidence, zero-temperature proof support, proof traces, and no runtime labels; likely claims require explicit-world posterior plus confidence/uncertainty decomposition; record-contingent claims require record dependencies and access-state explanation.
  Main risks are false certainty, source poisoning, access overreach, access underreach, and LLM rendering drift, mitigated through confidence bands, reliability/source diversity, record-duty/access checks, competing missingness worlds, structured rendering, and post-render verification.
  Deployment checklist requires resolvable citations/proof traces for strict claims, separate posterior/strict/confidence reporting, alternative worlds, record dependencies, uncertainty decomposition, evidence-that-would-change-conclusion, renderer checks, and no hidden benchmark/evaluator fields at runtime.
---

The oracle boundary is the line between **offline calibration** and **runtime
truth ranking**.

GCTS may use labels or expert judgment for training, calibration, evaluation,
and error review. Runtime truth ranking and posterior mass must come from
evidence, access states, rules, possible worlds, proof traces, and calibrated
parameters.

## Allowed Oracle Use

- Training labels.
- Calibration labels.
- Evaluation labels.
- Expert review of error cases.
- Human approval of new strict rules.
- Human review of system failures after a run.

## Forbidden Runtime Oracle Use

- Runtime access to gold labels.
- Runtime human or model truth decisions that bypass evidence closure and world
  ranking.
- Dataset label leakage into retrieval, ranking, world building, or rendering.
- Prompting an LLM to decide truth and using that answer as posterior mass.
- Using hidden benchmark answers as features.
- Using evaluator notes, answer keys, or adjudication metadata in a production
  run.

## LLM Boundary

LLMs may:

- extract candidate claims;
- propose evidence spans;
- propose latent context variables;
- suggest possible access hypotheses;
- render structured outputs into readable prose.

LLMs may not:

- assign runtime truth mass;
- promote a claim to strict proof;
- erase record contingencies;
- convert missing records into ordinary absence without the access model;
- add unsupported details during rendering.

## Promotion Policy

Strict claims require:

- resolvable evidence references;
- zero-temperature proof support;
- proof traces;
- no runtime label access.

Likely-truth claims require:

- posterior calculation over explicit worlds;
- confidence and uncertainty decomposition;
- clear distinction between posterior probability, strict support, and
  confidence.

Record-contingent claims require:

- identified record dependencies;
- access-state classification;
- an explanation of what evidence would change the ranking.

## Relationship To Benchmark Leakage

The oracle boundary is related to benchmark-leakage and test-contamination
concerns in machine-learning evaluation. Hidden labels, benchmark answers,
evaluator notes, and gold outputs can improve apparent performance while
bypassing the evidence process. GCTS treats that pattern as a governance failure
in runtime truth ranking.

The deployable system must be able to explain how each claim status came from
available evidence, access states, rules, worlds, proof traces, and calibrated
parameters.

## Main Risks

**False certainty:** posterior scores can be misread as objective truth.
Mitigation: confidence bands, entropy, uncertainty decomposition, estimative
language, and explicit caveats.

**Source poisoning:** manipulated evidence can shift world rankings.
Mitigation: source reliability priors, source diversity metrics, adversarial
evidence tests, and source-quality uncertainty.

**Access overreach:** the system may infer withholding or concealment from
ordinary missingness. Mitigation: record-duty thresholds, access-path checks,
competing missingness worlds, MDL penalties, and conservative confidence.

**Access underreach:** the system may treat inaccessible controlled records as
simple lack of evidence. Mitigation: record-contingency status, expected-record
modeling, access uncertainty, and next-evidence requirements.

**LLM rendering drift:** the renderer may add unsupported details. Mitigation:
render from structured payload only, post-render verification, and rejection of
unsupported phrases.

## Deployment Checklist

- [ ] All strict promoted claims have resolvable citations.
- [ ] All strict promoted claims have proof traces.
- [ ] Runtime labels were unavailable.
- [ ] Posterior, strict support, and confidence are reported separately.
- [ ] Top alternative worlds are shown.
- [ ] Record-contingent claims identify record dependencies.
- [ ] Uncertainty decomposition is shown.
- [ ] Evidence that would change the conclusion is listed.
- [ ] Renderer output is checked against the structured payload.
- [ ] No hidden benchmark fields, answer keys, or evaluator notes are accessible
      to runtime ranking.

GCTS is a decision-support system. It should expose alternatives,
likely-truth rankings, access constraints, and uncertainty. It should not
replace human judgment in high-stakes domains.
