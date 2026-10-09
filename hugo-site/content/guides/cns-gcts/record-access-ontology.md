---
title: "GCTS Record-Access Ontology"
description: "Typed record-access states for missing, controlled, sealed, destroyed, unavailable, and not-generated evidence."
lastmod: "2026-05-15"
weight: 5
meta_description: "Record-access ontology for CNS 7.1 / GCTS, defining available, inaccessible, sealed, withheld, destroyed, not-generated, unknown, partial, contradicted, produced-late, and unavailable-at-time records."
ai_agent_note: |
  ATTN AI Agent:
  This page defines the GCTS record-access layer, the main differentiator from standard verification: GCTS models records that should exist, might exist, were requested, not produced, late-produced, sealed, destroyed, or should never have been expected.
  Record-access state object r_k includes id, type, owner, controller, duty, expected observability/generation, access classification, production history, request/search path, relevant time interval, and confidence q_k.
  Access states and ranking effects include available, inaccessible, sealed, withheld, destroyed, not_generated, unknown, produced_late, partial, contradicted, and unavailable_at_time_t.
  Production states include produced, partial_production, no_response, nonresponsive_response, refused, claimed_none, lost, destroyed, late_production, and metadata_only.
  Generation-duty sources include legal duty, policy duty, role duty, instrumentation duty, ordinary-practice duty, and no duty.
  Absence can affect a claim only after modeling generation duty, observability, ownership/control, access path, production response, and whether absence is better explained by benign missingness, access limits, non-generation, destruction, sealing, withholding, or unknown causes.
  Every record-contingent claim must state which records matter, why expected/not expected, who owned/controlled them, current access state and confidence, whether strict proof or likely-truth ranking depends on them, and what production would raise/lower/resolve claim status.
---

The record-access layer is the strongest differentiating component of GCTS.
Standard verification systems often classify a claim against retrieved evidence.
GCTS also models the records that should exist, might exist, were requested,
were not produced, were produced late, were sealed, were destroyed, or should
never have been expected.

## Record-Access State Object

A record-access state is:

$$
r_k = (id_k, type_k, owner_k, controller_k, duty_k, expected_k, access_k,
production_k, request_k, time_k, q_k)
$$

| Field | Meaning |
| --- | --- |
| `id_k` | Stable record-access identifier |
| `type_k` | Record type, such as report, log, transcript, notification, policy record, metadata, or audit entry |
| `owner_k` | Institution or actor expected to own or retain the record |
| `controller_k` | Actor with practical control over access or production |
| `duty_k` | Legal, policy, role, instrumentation, or ordinary-practice generation duty |
| `expected_k` | Expected observability or generation likelihood |
| `access_k` | Access-state classification |
| `production_k` | Production history or response state |
| `request_k` | Request path, search path, or collection path |
| `time_k` | Time interval in which the record would matter |
| `q_k` | Confidence in the classification |

## Access States

| State | Definition | Ranking effect |
| --- | --- | --- |
| `available` | Record is present and resolvable | Can support, refute, or qualify claims directly |
| `inaccessible` | Record may exist outside the current access path | Creates record contingency and wider uncertainty |
| `sealed` | Record exists or plausibly exists under restricted access | Blocks strict conclusions dependent on the record |
| `withheld` | Non-production is plausibly controlled by an actor with access and incentive | Creates competing missingness worlds and may affect world energy |
| `destroyed` | Record existed or was expected and is no longer available | Creates retention or spoliation hypotheses when duty and control are established |
| `not_generated` | Record should not be expected under the relevant duty or practice | Reduces absence penalty and can refute assumptions about expected records |
| `unknown` | Current evidence cannot classify the access state | Widens uncertainty and prevents strong absence inference |
| `produced_late` | Record appeared after initial non-production | Supports timelines about production behavior and access friction |
| `partial` | Some responsive material exists but expected fields or documents are missing | Creates partial support and unresolved contingencies |
| `contradicted` | Produced record conflicts with other evidence or expected metadata | Increases contradiction residual and alternative-world branching |
| `unavailable_at_time_t` | Record exists now or later but was unavailable at the relevant decision time | Prevents later evidence from being treated as runtime evidence for the original actor |

## Production States

| State | Definition |
| --- | --- |
| `produced` | Responsive record produced |
| `partial_production` | Some responsive material produced |
| `no_response` | No institutional response to request |
| `nonresponsive_response` | Response received but did not answer the record question |
| `refused` | Production denied or refused |
| `claimed_none` | Institution states no responsive record exists |
| `lost` | Record claimed lost |
| `destroyed` | Record claimed destroyed |
| `late_production` | Record produced after delay |
| `metadata_only` | Metadata or administrative material produced without the responsive record |

## Generation Duty

A record expectation is stronger when several duty signals align:

| Duty source | Examples |
| --- | --- |
| Legal duty | reporting law, retention law, mandatory reporting, discovery obligation |
| Policy duty | school policy, HR policy, medical protocol, agency rule |
| Role duty | officer, supervisor, teacher, clinician, custodian, compliance officer |
| Instrumentation duty | logs, cameras, timestamps, access-control systems |
| Ordinary-practice duty | records typically created in comparable cases |
| No duty | record should not be expected |

## Absence Discipline

Absence can affect a claim only after the system has modeled:

1. Whether a record-generation duty existed.
2. Whether the event should have been observable.
3. Who owned or controlled the record.
4. Whether the access path was legitimate or ordinary.
5. What production response occurred.
6. Whether the record's absence is better explained by benign missingness,
   access limits, non-generation, destruction, sealing, withholding, or unknown
   causes.

Only evidence of absence directly penalizes a claim as absent. Other states
usually create uncertainty, record contingency, or competing worlds.

## Output Requirement

Every record-contingent claim should state:

- which records matter;
- why those records were expected or not expected;
- who owned or controlled them;
- what access state is currently assigned;
- how confident the system is in that classification;
- whether strict proof depends on the record;
- whether likely-truth ranking depends on the record;
- what record production would raise, lower, or resolve the claim status.
