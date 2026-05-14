---
title: "Adversarial Evidence And Access Modeling"
description: "How GCTS handles missing records, controlled evidence, source incentives, and strategic non-production."
lastmod: "2026-05-13"
weight: 6
meta_description: "Access-aware and adversarial evidence policy for GCTS: distinguishing absence of evidence, evidence of absence, inaccessible evidence, withheld evidence, and not-generated records."
---

GCTS is designed for environments where evidence is limited, contradictory, or
adversarially curated. The central discipline is simple: **absence has multiple
states**.

## Five Absence States

1. **Absence of evidence:** no available supporting evidence has been found.
2. **Evidence of absence:** an expected record or observation exists and
   affirmatively negates the claim.
3. **Inaccessible evidence:** the record may exist outside the runtime corpus.
4. **Withheld evidence:** non-production is more likely under a withholding
   world than under a benign-missingness world.
5. **Not-generated evidence:** the record should not be expected to exist.

Only evidence of absence can directly penalize a claim as absent. Other states
usually create access uncertainty, record contingencies, or competing worlds.

## Access Features

For each expected record, GCTS models:

- who controls it;
- whether ordinary procedure would generate it;
- whether it should be observable;
- whether it was requested, produced, refused, partially produced, contradicted,
  destroyed, sealed, or unavailable;
- confidence in that access-state classification.

## Incentive Features

Institutional incentive profiles model:

- control over records or testimony;
- reputational, legal, financial, operational, or political exposure;
- incentive to disclose;
- incentive to conceal, delay, narrow, or frame evidence;
- expected penalty if concealment is detected;
- prior source reliability.

Incentives affect missingness likelihood, source quality, and world energy while
leaving proof to evidence and rules. Claims still require evidence and rules.

## Suppression Discipline

The system should infer strategic withholding only when several conditions line
up:

- a record was expected to exist;
- a responsible actor plausibly controlled it;
- the access path was legitimate or ordinary;
- non-production is less likely under benign missingness;
- the hypothesis reduces contradiction or explains access asymmetry without
  excessive unsupported complexity.

Unsupported suppression hypotheses should increase parsimony penalty.

## Output Requirements

Any report involving missing or controlled evidence should state:

- which records matter;
- expected generation duty;
- observed access state;
- confidence in that classification;
- whether the claim is `record_contingent`;
- what evidence would raise, lower, or resolve the claim ranking.
