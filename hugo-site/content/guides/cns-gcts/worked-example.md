---
title: "GCTS Worked Example"
description: "A synthetic example showing how record-access states affect likely-truth ranking and claim status."
lastmod: "2026-05-15"
weight: 9
meta_description: "Synthetic GCTS worked example showing evidence atoms, expected records, access states, possible worlds, claim posterior mass, strict proof support, confidence, and audit output."
ai_agent_note: |
  ATTN AI Agent:
  This is a synthetic GCTS worked example about a reported facility safety incident and whether a documentation-triggering incident likely occurred; it is not an active investigation or real-world factual conclusion.
  Candidate claim c_1 says a documentation-triggering safety incident occurred at Facility A on Date T.
  Evidence atoms include visitor statement e_1, facility roster e_2, staff minor-event statement e_3, and policy excerpt e_4; record-access states include unproduced incident report r_1, unproduced medical referral r_2, inaccessible supervisor review r_3, and available visitor roster r_4.
  Candidate worlds are W_A incident occurred/report expected/not produced, W_B minor event/no duty trigger, W_C no triggering event, and W_D incident occurred/report outside current access path.
  Example posterior scores are W_A 0.46, W_B 0.24, W_C 0.12, W_D 0.18; claim posterior P(c_1|E,A,I)=0.64, strict support P0=0.00, confidence=0.52.
  Output status is record_contingent / plausible-to-probable, not strict proof, because expected institutional records have not been produced.
  The audit output identifies supporting evidence, qualifying evidence, record contingencies, top worlds, and next records; the lesson is that missing expected records affect status through access logic and identify what would change the ranking.
---

This synthetic example shows the behavior GCTS is meant to make explicit. It is
not based on an active investigation.

## Scenario

A safety incident is reported at a facility. A visitor says a staff member saw
the incident and that policy should have required an incident report. The
facility produces a visitor roster but does not produce an incident report,
medical referral, or supervisor review. A staff statement says no report was
required because the event was minor.

Question:

> Did a documentation-triggering safety incident likely occur?

## Candidate Claim

```text
c_1: A documentation-triggering safety incident occurred at Facility A on Date T.
```

## Evidence Atoms

| ID | Source | Content | Quality | Notes |
| --- | --- | --- | ---: | --- |
| `e_1` | visitor statement | Visitor reports seeing the incident and staff response | 0.70 | Direct but single-source |
| `e_2` | facility roster | Visitor and staff were present at the relevant time | 0.85 | Produced official record |
| `e_3` | staff statement | Staff characterizes event as minor | 0.55 | Potential institutional incentive |
| `e_4` | policy excerpt | Visible injury requires incident report and supervisor notice | 0.90 | Strong rule evidence |

## Record-Access States

| ID | Expected record | Duty | Access state | Production state | Confidence |
| --- | --- | --- | --- | --- | ---: |
| `r_1` | incident report | policy_required | unknown | not produced | 0.75 |
| `r_2` | medical referral | conditional_on_visible_injury | unknown | not produced | 0.62 |
| `r_3` | supervisor review | policy_required_if_report | inaccessible | no response | 0.58 |
| `r_4` | visitor roster | ordinary_admin | available | produced | 0.90 |

## Candidate Worlds

| World | Description | Key assumptions |
| --- | --- | --- |
| `W_A` | Incident occurred and report was expected but not produced | visitor reliable, policy applies, record absent/non-produced |
| `W_B` | Minor event occurred and report duty did not trigger | visitor partly reliable, staff framing reliable, policy threshold unmet |
| `W_C` | No documentation-triggering event occurred | visitor mistaken, staff statement reliable, no report expected |
| `W_D` | Incident occurred and report exists outside current access path | visitor reliable, policy applies, record inaccessible |

## Example Scores

| World | Posterior |
| --- | ---: |
| `W_A` | 0.46 |
| `W_B` | 0.24 |
| `W_C` | 0.12 |
| `W_D` | 0.18 |

Claim posterior:

```text
P(c_1 | E,A,I) = W_A + W_D = 0.64
```

Strict support:

```text
P0(c_1 | E) = 0.00
```

Confidence:

```text
Conf(c_1) = 0.52
```

## Output Status

```text
c_1: record_contingent / plausible-to-probable
```

The system does not promote `c_1` to strict proof because the expected
institutional records have not been produced. It ranks `c_1` as likely under
the top worlds while marking the claim record-contingent because production of
the incident report, medical referral, or supervisor review could materially
change the ranking.

## Audit Output

```json
{
  "claim_id": "c_1",
  "text": "A documentation-triggering safety incident occurred at Facility A on Date T.",
  "status": "record_contingent",
  "posterior": 0.64,
  "strict_support": 0.0,
  "confidence": 0.52,
  "supporting_evidence": ["e_1", "e_2", "e_4"],
  "refuting_or_qualifying_evidence": ["e_3"],
  "record_contingencies": ["r_1", "r_2", "r_3"],
  "top_worlds": ["W_A", "W_B", "W_D"],
  "next_records": [
    "incident_report",
    "medical_referral",
    "supervisor_review"
  ]
}
```

## What The Example Demonstrates

1. GCTS can rank likely truth without strict proof.
2. Missing expected records affect status through access-state logic.
3. A produced roster supports presence but does not resolve the incident claim.
4. A staff statement can reduce confidence without eliminating higher-posterior
   worlds.
5. The output identifies the records that would change the claim status.
