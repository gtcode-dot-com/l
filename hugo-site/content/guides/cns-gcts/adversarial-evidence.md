---
title: "Adversarial Evidence And Access Modeling"
description: "How GCTS handles missing records, controlled evidence, source incentives, and strategic non-production."
lastmod: "2026-05-15"
weight: 6
meta_description: "Access-aware and adversarial evidence policy for GCTS: distinguishing absence of evidence, evidence of absence, inaccessible evidence, sealed records, withheld evidence, destroyed evidence, not-generated records, and selective disclosure."
ai_agent_note: |
  ATTN AI Agent:
  This page defines GCTS adversarial-evidence discipline for limited, contradictory, controlled, or strategically curated evidence: absence has structure.
  Absence states are absence of evidence, evidence of absence, inaccessible evidence, sealed evidence, withheld evidence, destroyed evidence, not-generated evidence, and unknown access; only evidence of absence directly penalizes a claim as absent.
  For each expected record, model owner, controller, generation duty, observability, request/production/refusal/partial/contradiction/destruction/sealing/delay/unavailability, and confidence in access classification.
  Institutional incentive profiles cover control over records/testimony, exposure, incentive to disclose or conceal/delay/narrow/frame, penalty if concealment is detected, and prior source reliability.
  Incentives affect missingness likelihood, source quality, and world energy but do not prove claims; proof remains evidence-and-rule based.
  Infer strategic withholding only when expected record, plausible control, legitimate access path, benign missingness less likely, and explanatory value without excessive complexity align; unsupported suppression hypotheses increase parsimony penalty.
  Selective production examples include roster without incident report, policy without compliance log, metadata without content, summary without source records, or late production after nonresponsive response; reports must state records, duty, access state, production response, confidence, record_contingent status, and what evidence would change ranking.
---

GCTS is designed for environments where evidence is limited, contradictory,
controlled, or strategically curated. The central discipline is simple:
**absence has structure**.

## Absence States

| State | Meaning |
| --- | --- |
| Absence of evidence | No available supporting evidence has been found |
| Evidence of absence | An expected record or observation exists and affirmatively negates the claim |
| Inaccessible evidence | The record may exist outside the current access path |
| Sealed evidence | The record exists or plausibly exists under restricted access |
| Withheld evidence | Non-production is more likely under a withholding world than under benign missingness |
| Destroyed evidence | The record existed or was expected and is no longer available |
| Not-generated evidence | The record should not be expected to exist |
| Unknown access | Current evidence cannot classify the access state |

Only evidence of absence can directly penalize a claim as absent. Other states
usually create access uncertainty, record contingencies, or competing worlds.

## Access Features

For each expected record, GCTS models:

- who owns it;
- who controls production;
- whether ordinary procedure would generate it;
- whether the event should be observable by that record system;
- whether the record was requested, produced, refused, partially produced,
  contradicted, destroyed, sealed, delayed, or unavailable;
- confidence in the access-state classification.

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

## Selective Production

Adversarial environments often produce some records while withholding,
narrowing, delaying, or reframing others. GCTS should treat partial production
as an observed production state with remaining access limits.

Examples:

- A roster is produced but the incident report is not.
- A policy is produced but the compliance log is not.
- Metadata is produced but content is withheld.
- A summary is produced but source records are not.
- A record appears only after an initial nonresponsive response.

Selective production can support some claims while increasing access
uncertainty around others.

## Output Requirements

Any report involving missing or controlled evidence should state:

- which records matter;
- expected generation duty;
- observed access state;
- production response;
- confidence in the classification;
- whether the claim is `record_contingent`;
- what evidence would raise, lower, or resolve the claim ranking.
