---
title: "TRACE: Proposed Evaluation and Falsifiability Specification"
description: "A proposed, unregistered protocol to test TRACE against resource-matched alternatives on contrastive correctness, independently predictive synthesis, and evidence-acquisition decisions."
date: "2026-11-15"
lastmod: "2026-11-15"
draft: false
author: "GTCode.com"
math: true
toc: true
weight: 20
tags:
  - TRACE
  - preregistration planning
  - benchmark design
  - predictive synthesis
  - scientific method
categories:
  - research
meta_description: "TRACE evaluation: development cases, an exploratory pilot, matched contrastive-discovery controls and sealed predictions; no experiments performed."
meta_keywords:
  - TRACE
  - falsifiable hypotheses
  - evaluation protocol
  - contrastive robustness
  - sample sizes
  - experimental design
structured_data_webpage:
  type: Article
  headline: "TRACE: Proposed Evaluation and Falsifiability Specification"
  description: "A proposed and unregistered protocol, including endpoints, safeguards, controls, test allocation and failure criteria for TRACE."
  about:
    - falsifiability
    - experimental design
    - Testing Rival Accounts through Contrast and Evidence
ai_agent_note: |
  This is a proposed experimental design, version 0.1 (15 November 2026).
  It is NOT preregistered, implemented, executed or empirically validated.
  No sample counts, target improvements or performance quantities are results.
  Model IDs, validators, exact action costs and data versions remain pending freeze decisions.
---

> **Research proposal · Version 0.1 · 15 November 2026.** Proposed design, not preregistered or executed. Development and pilot counts are exploratory choices, not evidence of power.

[Full paper](/papers/trace/) · [Overview](/guides/trace/overview/) · [Protocol YAML](/papers/trace/proposed-evaluation-protocol.yaml) · [Prior-art audit](/papers/trace/prior-art-audit.md) · [Contribution matrix](/papers/trace/contribution-matrix.md)

## 1. Primary question and supporting hypotheses

**H2 — Independently predictive discovery (primary).** Does explicit conflict localization improve the discovery of measurable conditions beyond an established contrastive-discovery adaptation receiving the same source facts? The primary comparison is C versus B in Section 2 below. Each system locks its explanatory relationship, parameters and final candidate before receiving the five prediction contexts. It then applies that fixed candidate to those contexts and commits the outputs before any outcome is revealed. All systems receive the same context fields from a task dictionary fixed during development; field selection must not disclose the correct moderator. New variables require an operational mapping to available fields or remain unmeasured. The evaluator selects challenge settings before generation, independently of each system's proposals. Success requires a source-faithful explanatory relationship not explicitly supplied in the packet, a distinguishing new prediction, and at least four of five predictions correct under frozen tolerances, including every prespecified diagnostic setting needed to distinguish the task's principal unconditional alternative. Alignment, copying detection and restatement earn no discovery credit. Candidate novelty is relative to the initial packet, not a claim of novelty to science. A condition may be new even when its variables occur in the reports; what must be absent is the explanatory relationship. No credit requires guessing an unobservable latent variable. A blinded semantic rubric and held-out prediction scoring assess different requirements; neither substitutes for the other.

The generation-only study uses a fixed permitted evidence snapshot. A variable absent from the measurements can support a conjecture, but unsupported assignments cannot manufacture fit or warrant. A case needing further measurements remains pending on the static branch; discovery following acquisition belongs to the subsequent adaptive study. Each positive challenge set must distinguish a plausible unconditional alternative; use mixed regimes and boundary settings where appropriate, rather than require sign reversals for every mechanism family.

**H1 — Reliability (supporting quality measure).** Report base-answer correctness, response to nuisance and relevant changes, coverage, false promotion and unsupported resolution. A system that wins H2 by inventing conditions indiscriminately or refusing difficult cases has not established a useful discovery method. Include negative controls where no new condition is justified and cases where accessible evidence cannot identify the answer. Report denominators and unconditional scores; do not select only successful generations for analysis.

**H3 — Investigation (conditional subsequent study).** Only after the representation and generation stages show credible predictive value, compare evidence acquisition against Contrastive Discovery, POPPER where its statistical assumptions can be met, ordinary experimental design and simple random/relevance policies. All receive the same action access and costs. The endpoint is an evidence-supported scoped conclusion within budget, not the number of self-declared resolved questions. Static and adaptive outcomes remain separate.

H2 is the scientific priority. H1-only improvement supports a narrower reliability tool; H3-only improvement may support ordinary active learning. Neither rescues a failed claim about conflict-conditioned discovery. No superiority, fixed effect size or statistical power is claimed for the exploratory pilot.

## 2. Proposed evaluation design and decision gates

### 2.1 Development and exploratory pilot

Start with **12–20 manually inspected development cases**. Include genuine same-estimand conflicts, apparent unit/measurement differences, copied sources, asymmetric missing context, an unstated measurable condition and non-identifiable alternatives. Use the eight mechanism families as a coverage taxonomy, not a forced equal-size factorial grid. Experts must check whether the target is identifiable from each permitted evidence view and whether the five withheld settings can distinguish a plausible wrong rule. A realistic source packet may contain several issues at once.

Then freeze the extractor, models, prompts, schemas, candidate limits, tolerances, costs, adjudication rubric and scoring process for a separate **30–60-case exploratory pilot** with unseen outcomes and disjoint generating episodes/source clusters. These counts diagnose feasibility; they are not powered sample sizes for a superiority claim. Include eligible discovery cases and prespecified no-discovery/non-identifiable controls; publish their actual counts and uncertainty separately. Eligibility is fixed before any system runs; all eligible cases remain in the H2 denominator, including abstentions, invalid outputs and missing predictions. Control strata have their own denominators. Case selection must not depend on TRACE succeeding or competitors failing. Family labels and eligibility certificates remain evaluator-only.

All development and pilot cases produce the common records in paper Section 4.1. Repeated prompts, five predictions, source copies and model seeds are not independent research cases. Pilot revisions require fresh cases for a subsequent evaluation. No benchmark data, pilot or implementation has yet been produced.

### 2.2 Identical facts, different evidence organization

The common-input study freezes source-linked questions, measurements, missingness, report text and available lineage facts. An evaluator may certify targets but must never supply the true moderator or causal mechanism to runtime. All systems can inspect the same original spans and infer their own conflicts or dependencies.

| System | Proposed operation on the common evidence |
|---|---|
| A | Strong iterative hypothesis refinement, with an additional counterexample-prompting variant; adapted from established hypothesis-refinement methods |
| B | Contrastive Discovery adaptation: explicit alternative explanations; generation and scoring documented against the original method |
| C | Same scaffold as B, augmented with a generated conflict-alignment record and conflict-directed generation; common row-based fitting and warrant rules |
| D | Same as C plus explicit dependence-aware weighting and warrant accounting from the available lineage facts |

**C versus B is the primary comparison.** Both propose explicit rival explanations. C receives an additional generated conflict record and conflict-directed instruction; B may identify conflicts itself. Hold the model, source packet, proposal capacity, prediction interface and final selector fixed. This measures the localization package, not the isolated effect of a single field or instruction. A matched auxiliary condition gives B an equally budgeted source-summary call, using the same evidence without instructions to localize conflicts. It tests whether extra preprocessing explains an apparent gain. All preprocessing consumes the common resource ceiling.

**Common selection.** After structural validation, a shared selector receives source evidence and candidate predictions/assumptions, with system identity, conflict IDs and generation order hidden. Order candidates by coverage of observed contexts without invented values, then fewer unsupported assumptions, then canonical candidate ID. Within the numerical form, apply the same training-loss criterion and row weights. This selector uses no test outcomes or localization-specific score. It can select an unresolved result. Log candidate-pool quality separately from the selected-candidate endpoint. The full TRACE ranking in paper Section 4.3 is tested separately.

**Comparator fidelity.** B is a static adaptation of contrast-set generation to a fixed evidence snapshot. It does not reproduce Contrastive Discovery's adaptive search, and the common selector replaces its native scoring for this mechanism experiment. Its alternative set should cover a declared question with disjoint explanations; log incomplete or overlapping coverage. An explicit residual explanation means none of the specified explanations applies; uncertainty about which explanation holds is a separate decision state. Neither makes an arbitrary set logically exhaustive.

**Transfer to an existing discovery method.** Compare the same capable discovery implementation with and without generated TRACE conflict records. Preserve its native hypothesis generation, belief scoring, search, revision and stopping rules; the intervention supplies source-linked localization and instructions for using it, not TRACE's selector or rule compiler. Both conditions receive identical source facts and access to the same analysis service. Include an equally budgeted source-summary condition. Charge extraction, localization, elicitation, failed attempts and analysis to a common resource ceiling established during development that permits the native workflow to operate. Record any interface changes and pin code, prompts and model versions. Sealed outcomes remain inaccessible to all search tools. At the budget boundary, lock each method's selected explanation and use the same outcome-blind prediction interface and held-out scoring; report this external endpoint separately from native belief-based resolution.

Contrastive Discovery is the closest contrastive comparator, but its author page lists code as forthcoming. A paper-based implementation must be labeled a reproduction attempt, with unresolved fidelity differences disclosed. AutoDiscovery offers a released implementation for a complementary transfer comparison; its current defaults differ from its paper and must not be presented as the original experimental configuration. Report either comparison separately from static C–B, and report adaptive evidence acquisition separately from fixed-evidence analysis. Belief scores are not correctness labels. If the native procedure cannot operate within the task interface, disclose the incompatibility. A static C–B gain supports that scaffold-specific intervention; evidence for a transferable component requires improvement within an existing method with its native scoring and search preserved.

**D versus C tests lineage handling**, not the benefit of giving D extra source facts. Both receive identical lineage metadata; C can reason about it ordinarily, while D applies explicit accounting. In the controlled compiler, B/C use row-based fitting and D uses the lineage-aware fitting and eligibility rules in paper Section 4.4. The comparison therefore isolates the accounting package, not an information advantage. A full two-by-two localization/lineage factorial can be added if interaction is itself a research target. Without that factorial, D–C is conditional on localization and cannot establish an independent main effect of lineage.

The common-input experiment tests evidence organization on a frozen, source-faithful extraction. Because that extraction may favor some methods, its errors and construction procedure must be disclosed. Also run an equal-access end-to-end comparison in which extraction and localization are generated separately for each method and all their costs/errors count. Common-input records produced by TRACE must not contain its inferred answer. Human-corrected conflict records are an oracle diagnostic reported separately, never the primary result. Freeze provenance of every field so an apparent algorithmic advantage cannot conceal additional information.

Retain an ordinary common-extractor rule/tree/regression learner (B8), with exhaustive search when inexpensive. It tests whether tabular learning explains any gain. A and B should receive serious development tuning, the same evidence and comparable tuning resources; the counterexample-prompting control tests whether a simple instruction captures the effect. Prior RAG, verification, debate, AAL-sketch and CNS-subset comparators are optional diagnostics rather than a mandatory ten-system first study. Our AAL implementations remain operationalizations of Lopez-Paz's sketch, not author-released systems.

### 2.3 Outcomes, budgets and causal attribution

Score the final locked candidate per case, all five predictions, and all invalid or missing outputs. Report the H2 success proportion, prediction loss, source-fidelity errors, new measurable candidate yield, false-condition promotion, unsupported resolution, coverage and actual cost. Log every proposed candidate before selection so a predictive gain can be distinguished from more proposals or better selection. Candidate equivalence is judged through variable definitions, relationships and predicted consequences rather than different prose alone; adjudicators are blinded to system identity and disagreements are retained. For continuous targets, the primary correctness score uses a point prediction and a tolerance fixed from the measurement design; each candidate cannot choose its own acceptance width. For categorical targets, require one category. Optional uncertainty intervals are scored separately with a width-sensitive rule, and probabilistic forecasts with an appropriate proper score. Wide intervals and multiple guesses cannot satisfy the primary prediction gate. Specify how noisy repeated measurements form the target estimate before unblinding.

Two independently blinded reviewers apply the source-fidelity and packet-relative novelty rubric to candidate records. Resolve disagreements with a third reviewer and report initial agreement and unresolved cases. Human decisions never return to runtime. On the small pilot, inspect all cases rather than extrapolate from a favorable subset. Outcome scoring uses the frozen executable rule wherever possible.

For TRACE and the controlled B/C scaffold, start with one shared extraction, one preprocessing call per condition, up to eight proposals, one structural repair and at most four active rivals. The common selector is also charged. Faithful iterative or adaptive method-level competitors may divide the same total budget differently. For the pilot, propose a common per-case ceiling of 16,000 input and 4,000 output tokens across all static stages, including extraction, localization and repair. Context packing must preserve the same evidence across systems; if this is infeasible, change the setting during development, then freeze it. Report usage rather than require waste to equalize totals. Measure CPU time for ordinary learners and model tokens, calls and latency for every method. Generated localization consumes the common budget; an oracle-localization result is a separate diagnostic.

Freeze one model/version and seed for the exploratory primary configuration; additional seeds are paired sensitivity runs. In candidate-generation comparisons, common compilation and scoring follow generation. In prioritization diagnostics, freeze the candidate pool and vary only ranking. In numerical search-order diagnostics, freeze the extracted table and rule language, compare contrast order, seeded permutation and exhaustive enumeration, and report the complete cost curve. These are different interventions.

### 2.4 Interpretation and stop decisions

Report paired case-level differences and uncertainty, errors by case type, all exclusions and the full candidate/commitment records. The pilot is exploratory: neither a favorable p-value nor four correct predictions in one case demonstrates scientific superiority. State the sampled population and source clustering before selecting an interval method; avoid a nominal precision calculation that treats related packets as independent. Do not infer equivalence from a nonsignificant difference.

Proceed through four gates: **representation**, can claims, scope and lineage be extracted without unsupported values; **generation**, does localization produce different measurable candidates from B; **prediction**, do those candidates improve sealed predictions without unacceptable false promotion or coverage loss; **cost and transfer**, does the pattern survive metered budgets and genuinely different case construction? Publish paired estimates at every gate. Gates guide continuation, not post hoc filtering of reported failures. If candidate content and frequency are similar but selection improves, investigate selection as the mechanism. If neither candidate yield nor sealed prediction shows useful change, stop scaling until a concrete repair warrants fresh cases. A small inconclusive pilot warrants an uncertainty assessment, not a declaration that the methods are equivalent.

Before a confirmatory study, choose a smallest worthwhile effect and safety margins with domain justification; estimate paired discordance and source clustering from development/pilot data; then select a sample size with power and sensitivity calculations. Freeze the primary C–B comparison, its independent unit, valid interval/test, treatment of invalid outputs and multiplicity family. D–C and other comparisons remain secondary unless additional error control is specified. The pilot cannot certify a 5% false-promotion ceiling on a small control stratum. Report exact counts and sampling-appropriate uncertainty instead of treating absence of observed errors as safety.

Stop or reduce the proposal if ordinary refinement or contrastive discovery produces equivalent candidates and predictions at lower cost, if localization mainly inserts unsupported assumptions, or if all benefit is extraction/deduplication. A useful benchmark or reliability tool would require its own contribution argument; neither is an automatic consolation prize. If prior work already specifies the same operational distinction, withdraw the methodological claim rather than add machinery to protect it.

### 2.5 Conditional extensions

A later H3 study may use the same three-action/12-cost-unit engineering ceiling, but must define action costs and identifying evidence independently of the hidden answer. A faithful POPPER comparison requires valid test statistics and implication checks; when these are unavailable, disclose incompatibility and report only a labeled falsification-style adaptation without inheriting its statistical guarantee. Compare full search policies separately from experiments that hold the candidate pool fixed. TRACE's set-separation score is a heuristic, not sequential error control.

Larger synthetic studies across F1–F8, source-clustered verification panels, DiscoveryBench and prospective caching measurements remain possible extensions [DiscoveryBench: Towards Data-Driven Discovery with Large Language Models](https://arxiv.org/abs/2407.01725); [FEVER: a large-scale dataset for Fact Extraction and VERification](https://arxiv.org/abs/1803.05355); [Fact or Fiction: Verifying Scientific Claims](https://aclanthology.org/2020.emnlp-main.609/); [AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web](https://fever.ai/dataset/averitec.html). ConfRAG is an additional conflict-reasoning diagnostic, not a substitute for predictive discovery [Benchmarking LLM’s Capability in Reasoning over Conflicting Web References](https://aclanthology.org/2026.acl-long.11/). Sample sizes and execution counts for these extensions require a separate design after feasibility is established. A prospective study must first specify service regimes, hardware/day/carryover blocks, withheld measurement collection after commitment and uncertainty at the independent regime level. Workload seeds and repeated requests do not establish independent mechanisms.

All phases require sealed evaluator outcomes, source-cluster separation, immutable prediction commitments and publication of failures. Runtime receives only permitted records and measurement results, never gold mechanisms, eligibility labels or evaluator judgments. Leakage, changed tolerances after unblinding or source overlap invalidate confirmatory interpretation.

## 3. Method, exports and freeze requirements

The [paper's four-stage specification](/papers/trace/#4-method-alignment-explanation-generation-and-investigation) defines alignment, lineage accounting, candidate generation and investigation. The [record schema](/papers/trace/trace-records.schema.json) preserves source statements, extraction interpretations, conjectures, missing measurements and evaluator-only scores. The numerical compiler is one implementation option; its 64-rule diagnostic does not cap classical baselines.

Before the pilot, freeze model/version, prompts, source packets and licenses, extraction/localization provenance, candidate limits, comparator adaptations, interpretation/novelty rubric, prediction tolerances, independent units, costs and handling of invalid outputs. Keep all outcomes sealed until final predictions are committed. Document every field available to each system and charge generated localization to its budget.

Before any later confirmation, independently justify the sample size, estimand, smallest worthwhile effect, quality safeguards, interval/test and multiplicity family. Publish case-level failures and exclusions. A claim card, citation, fitted rule, high belief score or structurally valid JSON output is never by itself an externally validated discovery.
