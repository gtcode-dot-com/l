---
title: "Oracle Boundary And Governance"
description: "The rule that prevents labels, expert judgments, or LLM truth decisions from bypassing evidence closure and world ranking."
lastmod: "2026-05-13"
weight: 3
meta_description: "The GCTS oracle-boundary policy: how labels, expert review, calibration, proof traces, and runtime evidence are separated to avoid hidden truth oracles."
---

The oracle boundary is the line between **offline calibration** and **runtime
truth ranking**.

GCTS may use labels or expert judgment for training, calibration, evaluation,
and error review. Runtime truth ranking and posterior mass must come from
evidence, access states, rules, and calibrated parameters.

## Allowed Oracle Use

- Training labels.
- Calibration labels.
- Evaluation labels.
- Expert review of error cases.
- Human approval of new strict rules.

## Forbidden Oracle Use

- Runtime access to gold labels.
- Runtime human or model truth decisions that bypass evidence closure and world
  ranking.
- Dataset label leakage into retrieval, ranking, or world building.
- Prompting an LLM to decide truth and using that answer as posterior mass.

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

GCTS is a decision-support system. It should expose alternatives,
likely-truth rankings, access constraints, and uncertainty. It should not
replace human judgment in high-stakes domains.
