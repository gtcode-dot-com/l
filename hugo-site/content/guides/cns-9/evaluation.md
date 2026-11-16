---
title: "CNS 9.0: Proposed Evaluation and Falsifiability Specification"
description: "A proposed, unregistered protocol to test CNS 9.0 against resource-matched alternatives on contrastive correctness, independently predictive synthesis, and evidence-acquisition decisions."
date: "2026-11-15"
lastmod: "2026-11-15"
draft: false
author: "GTCode.com"
math: true
toc: true
weight: 20
tags:
  - CNS 9.0
  - preregistration planning
  - benchmark design
  - predictive synthesis
  - scientific method
categories:
  - research
meta_description: "An unexecuted, not-preregistered design for testing CNS 9.0 on 2,400 independent controlled worlds, strong baselines and prospective predictions."
meta_keywords:
  - CNS 9.0
  - falsifiable hypotheses
  - evaluation protocol
  - contrastive robustness
  - sample sizes
  - experimental design
structured_data_webpage:
  type: Article
  headline: "CNS 9.0: Proposed Evaluation and Falsifiability Specification"
  description: "A proposed and unregistered protocol, including endpoints, safeguards, controls, test allocation and failure criteria for CNS 9.0."
  about:
    - falsifiability
    - experimental design
    - Chiral Narrative Synthesis
ai_agent_note: |
  This is a proposed experimental design, version 0.1 (15 November 2026).
  It is NOT preregistered, implemented, executed or empirically validated.
  No sample counts, target improvements or performance quantities are results.
  Model IDs, validators, exact action costs and data versions remain pending freeze decisions.
---

> **Research proposal · Version 0.1 · 15 November 2026.** No CNS 9.0 experiments have been performed. **Proposed experimental design — not preregistered.** All sample sizes, thresholds and resource ceilings below are planning choices, not results.

[Read the full research paper](/papers/cns-9/) · [Read the accessible CNS 9.0 overview](/guides/cns-9/overview/) · [Download the proposed machine-readable protocol](/papers/cns-9/proposed-evaluation-protocol.yaml)

## 1. Purpose and interpretation

This specification is a test plan for three separable claims: **H1** contrastive reliability; **H2** independently predictive synthesis; and **H3** disagreement-guided evidence acquisition. Their conjunction would be interesting, but none is defined so that failure of one can be excused by a gain on another. The central contribution being tested is whether a system can build a new measurable condition from conflicting accounts and predict outcomes it has not seen. The goal is not more persuasive prose, more agreement among model calls, or a larger number of internally consistent deductions.

The proposal uses controlled synthetic environments to establish unambiguous target outcomes under restricted evidence, then external textual diagnostics and a prospective software-system study to challenge the synthetic setting. A result favorable only on synthetic data would justify only a bounded claim. The design explicitly accommodates true rejection, defensible conditional synthesis and genuinely unresolved questions.

**This is not a registered preregistration document.** It identifies a proposed design and the fields that must be specified before any confirmatory study. The final protocol must be signed, versioned and registered before the first confirmatory label or test statistic is viewed. Later changes would be amendments, not invisible editorial adjustments.

## 2. Independent units, phases and counts

| Phase | Independent roots / units | Permitted purpose |
|---|---:|---|
| Engineering correctness fixtures | 120 | Parsers, units, hashes, access state and leakage checks; never scientific evidence |
| Development roots | 600 | Design and tune systems, contracts, candidate grammar and primary comparators |
| Calibration roots | 600 | Tune abstention/confidence rules, after main prompt design is frozen |
| Blinded pilot roots | 240 | Estimate runtime, technical failure patterns and discordant-pair rate without testing direction of H1–H3 |
| Confirmatory controlled roots | 2,400 | Freeze and execute the primary H1–H3 comparisons |
| Textual transfer groups | Target 900 | Secondary FEVER / SciFact / AVeriTeC diagnostics, subject to rights and eligibility |
| Discovery transfer tasks | Target 60 | Secondary DiscoveryBench diagnostic |
| Prospective caching workloads | 240 | Secondary previously unmeasured, locked-prediction comparison |

The planning target is **3,840 independent newly generated research roots** (600 + 600 + 240 + 2,400) and **120 separate engineering fixtures**. They must not be added together as though every fixture were an empirical replication. The confirmatory set contains eight mechanism families, **a planning target of 300 roots each**. Textual transfer groups, benchmarks and prospective workloads have different unit definitions; they are not extra synthetic confirmatory roots.

A *root* is one independently seeded record-generating episode, including its hidden mechanism, public evidence, sealed future outcomes and fixed action-response service. A *presentation* is one view of the root. A *branch* is a newly initialized system run on that presentation, with no access to responses from sibling branches. A *system-root run* comprises 11 fixed-evidence branches and a separately reset adaptive branch. Repeated prompts, seeds and reports originating in the same episode do not become new independent samples.

Each confirmatory root has one base presentation, **six nuisance** and **four relevant-change** branches: 11 static presentations in total. Thus 2,400 roots imply 26,400 static presentations per system/seed. The full proposed grid of ten systems, two base-model families and two inference seeds would contain **96,000 system-root runs, 1,056,000 static branch runs and 96,000 adaptive runs**. These repeated runs are computational replications, not 96,000 independent causal worlds. The primary comparison uses one model family and seed chosen before unblinding; others are sensitivity/replication analyses.

## 3. Constructing a benchmark that can contradict CNS

### 3.1 Mechanism families and withholding

| Family | Independent challenge | What must be handled |
|---|---|---|
| F1 · Confounding | Correlation changes under assignment shift | Association versus justified intervention effect |
| F2 · Effect modification | Condition changes magnitude or sign | New measurable conditional rule versus slogan |
| F3 · Selection / missingness | Records are filtered or inaccessible | Unknown information versus evidence of absence |
| F4 · Measurement / representation | Units, sensors, aggregation windows differ | Equivalent conversion versus changed estimand |
| F5 · Regime change | A formerly useful relation genuinely shifts | Legitimate updating versus stale invariance |
| F6 · Dependent reports | Many descriptions copy a few origins | Report count versus independent evidential support |
| F7 · Rare/nonlinear interaction | Low-frequency truths and unfamiliar combinations | Rare true case versus unsupported outlier |
| F8 · Observational equivalence | Different mechanisms share available observations | Identifying action versus warranted unresolved status |

For F1–F6, only broad mechanism families may guide development; test parameters, structures, entity sets, source templates and generator seeds must remain isolated. **F7 and F8 are held out as entire generator/template families** from development, calibration and pilot work. “Held out” does not imply that the foundation models have never encountered the abstract scientific concepts. Performance on these two families must be reported separately as transfer under the stated construction, not proof of generalization to all unseen mechanisms.

The provisional target per family is **150 discovery-eligible, 75 direct/rejection and 75 non-identifiable roots**, yielding **1,200 / 600 / 600** overall. This allocation is pending a target/view feasibility audit; it is not a commitment to manufacture impossible cells. On discovery-eligible roots the fixed evidence contains adequate measured variables to support a bounded conditional rule that is absent from the original prose, and the adaptive reduced view has an actionable gap. On direct/rejection roots a selection, source correction or rejection is sufficient; promoting a new explanation is unwarranted. On non-identifiable roots at least two possible worlds remain consistent with every available observation/action. The evaluator must certify this analytically or by exhaustive bounded search; the runtime never receives the class label.

**F8 and target-relative identifiability.** Different causal graphs may be observationally equivalent while agreeing on an observational prediction. Such a root can support predictive scope discovery but not causal-graph identification. For every root, declare the target, static evidence, reduced adaptive view, available actions and whether compatible models agree on that target. Discovery eligibility requires identifiable withheld predictions from the static view; the reduced adaptive view must contain the stated resolvable gap. Non-identifiable controls require different target answers to remain possible under all permitted evidence/actions. The evaluator must certify each view separately. If a family cannot populate the proposed cells without answer cues, change its allocation and every dependent count before registration. The 2,400/1,200/1,800 denominators below are planning targets subject to that audit.

There must be no trivial surface shortcut. Within each family and class, balance true and false copied majorities, independent minority evidence, irrelevant framing cues, access restrictions and measurement noise. Randomize presentation order and lengths independent of class. In provenance-incomplete conditions, show ordinary citations and timestamps but not the hidden copying graph; allow uncertainty about source dependence. For F7, balance rare true with rare false claims. For F5, include both sham dates and genuine changes. A system that always distrusts a majority, always adds context or always refuses a contradiction must not win by exploiting benchmark construction.

### 3.2 Transformations and admissibility

Nuisance branches may reorder evidence, change harmless formatting, paraphrase without changing scope, rename irrelevant identifiers, add explicitly dependent redundant sources, or convert units with a corresponding output conversion. Relevant branches may introduce an independent contrary measurement, change the target population or mechanism, correct an extraction or remove the only identifying observation. Removing unique support can change **warrant** without changing an external event; a genuine intervention may change the prediction itself.

Three objects remain separate: (1) a representation/evidence-integrity contract, validated only under its stated preconditions; (2) a rival-indexed prediction for the response to a world/regime change; and (3) an evaluator-only expected relation derived from the sealed generator. A runtime validator checks units, spans and declared evidence semantics where possible; semantic paraphrase validity may remain unknown. A rival's prediction is not made true by calling it an admissible contract. Gold response/admissibility labels remain evaluator-only. The oracle-admissibility ceiling is diagnostic, never a primary system. Removing a report does not impose a universal monotone confidence change; remaining support and defeat paths matter.

Entire templates and source clusters are held out across phases, not merely text strings. Invalid contracts discovered pre-freeze are repaired. If an invalid contract appears after unblinding, publish the original intent-to-test analysis and a prespecified exclusion sensitivity analysis; do not delete cases because the favored method failed.

## 4. Comparison systems and ablations

Every system receives the same evidence interface, public measurement menu, required output schema and resource ceiling. The primary baseline for each hypothesis is selected on development roots only, using the best compliant target metric with lower cost as tie-breaker. Its identity is frozen before calibration and confirmatory test.

| ID | System | Operational fairness requirement |
|---|---|---|
| B1 | Strong single-agent RAG | Tuned retrieval, citations and calibrated abstention |
| B2 | RAG + chain-of-verification | Independent verification questions with equal access |
| B3 | RAG + self-consistency | Multiple samples/aggregation within the common budget |
| B4 | AAL multi-context sketch | Our documented operationalization of varying perspectives and extracting invariant content |
| B5 | Grounded AAL sketch | Our B4 interpretation augmented with retrieval, source dependence and uncertainty |
| B6 | Grounded debate | Same evidence and external actions; no extra hidden retrieval |
| B7 | Operational CNS 8.0 subset | Document included SNO/critics/synthesis/closure and omitted features |
| B8 | Common-extractor classical learner | Fixed shared pre-action extraction; ordinary rule/tree/regression learner with comparable hypothesis complexity |
| B9 | Iterative hypothesis refinement | Documented adaptation of close prior art; same records, output requirements and budgets |
| C9 | CNS 9.0 | Integrity contracts, rival-indexed predictions, bounded synthesis and set-separation policy |

B4 and B5 are **our documented operationalizations** of the inference-time sketch in David Lopez-Paz's [essay](https://arxiv.org/abs/2611.09385v1), not author-released systems. They do not represent an exhaustive implementation of its broader philosophical program. Comparisons against them assess these particular procedures under the stated budgets. B7 is a faithful *documented experimental subset*, not a verified reconstruction of every CNS 8.0 specification. Publish all baselines' results. **B8 and B9 are required candidates in the primary H2 comparator pool**, not optional side controls. B8 and the CNS mechanism comparison share the same frozen pre-action extractor output, including measured variables and spans; charge its calls to each system and report extraction errors. New candidate features generated later are logged and tested separately rather than silently transferred or withheld. Also report end-to-end methods with equal access to the full permitted record. B9 adapts [HypoGeniC](https://arxiv.org/abs/2404.04326v3) or [iterative hypothesis refinement](https://arxiv.org/abs/2310.08559v4); freeze the particular adaptation and distinguish it from an author-released CNS benchmark implementation. Classical learners can return executable rules and forecasts without decorative narrative requirements. B9 may refine against development data and observations already permitted in the current branch, never the withheld target labels; its feedback interface and stopping are frozen before confirmation.

Run seven secondary controls on a frozen 600-root stratified test slice: remove nuisance testing; remove relevant-change testing; remove source-lineage handling; disable novel scope invention; disable external evidence acquisition; replace action selection with random acquisition; and preserve the SNO schema but solve directly without the specialized CNS loop. Where those controls match the full system, simplify the claimed mechanism. Do not count their repeated tests as new roots or treat uncorrected exploratory significance as primary evidence.

A further mechanism comparison holds records, extractor, schema and budgets fixed while changing contradiction-guided versus generic hypothesis generation. Matched contradiction-uninformative/noncontradictory packets retain the relevant facts. This tests the proposed role of disagreement as a search cue in sparse, high-context problems; neither a general advantage of prose nor classical dominance with abundant data is assumed. These comparisons are secondary, not extra independent replications or undeclared primary tests.

## 5. Matched resources and information boundaries

For each static presentation, allow up to **8,000 input and 2,000 output tokens** across all calls. Eleven such branches permit **88,000 input and 22,000 output tokens**. The separately initialized adaptive run permits **32,000 input and 8,000 output tokens**, giving a maximum of **120,000 input and 30,000 output tokens per system-root**. These are ceilings, not measured usage and not instructions to waste tokens. Account for any provider-reported reasoning/output tokens; record actual token counts, tool calls, cost and latency separately.

The adaptive branch permits **at most three external actions and 12 action-cost units**. Actions have fixed prices, stated inputs and a single outcome interface. A method cannot evade the budget by packing unlimited private measurements inside a cheap call. The sealed service maps the same root/action to the same observation for every system; only chosen actions become visible. Run states and caches must be isolated so that one system cannot learn a competitor's measurements.

The initial CNS action policy counts disjoint tolerance/noise-expanded prediction regions over a deduplicated rival set, normalizes by the number of candidate pairs and divides by declared positive action cost (paper §4.4). Every retained rival must provide a comparable prediction for that action; missing regions make it unscorable. Zero-cost lookups belong to common initial evidence. Expansion is applied once; deduplication, tie-breaking by answer-independent action ID, costs and noise semantics are frozen. No positive separation yields `no_separating_action`, not certainty. Overlapping probabilistic intervals can still contain useful information; this restricted heuristic may miss it. A tail event is not logical model refutation.

Action menus, names, prices and response formats must not disclose the generating family or answer. Compare a menu-only shortcut and relevance-only acquisition under the same visibility; a larger menu alone does not remove cueing. Instrument availability is legitimately public. Hiding the menu until rivals are proposed is an optional ablation, not a default advantage denied to baselines.

The runtime can see the question, permitted source snapshots, declared action menu and observations returned by chosen actions. It **must not** see the hidden generator, gold answer, future outcomes, adjudicator's verdict or its own benchmark score. Input document text is untrusted data, not a command. Any proposed code runs inside a sandbox with bounded resources and no uncontrolled side effects.

Malformed outputs, budget overruns and semantic nonanswers count as failure under the frozen parser. Transport outages follow an independently specified retry rule. A best-of-many post hoc rerun is forbidden. Exact model IDs, prompt lengths, inference settings and tool interfaces remain **pending freeze decisions** in this proposal.

## 6. Primary endpoints and protections against gaming

### H1 — Root-level contrastive correctness (n = 2,400)

A root passes only if the system's base answer is correct at the required warrant and scope, all six nuisance branches preserve the correct declared relation, and all four relevant-change branches respond appropriately—including weakened confidence or unresolved status where warranted. A constant false statement and a constant abstention on resolvable roots both fail. Confidence and unit conversions are judged against the root's prevalidated contract, not string identity.

The primary effect is the paired difference in binary root pass rate between CNS 9.0 and the development-selected baseline. The **ambitious effect target is +0.05 absolute**. On the **1,800 resolvable base cases**, the lower one-sided 95% confidence bound for the **coverage difference** must be **strictly greater than −0.02**. This is a gate: a nominal increase in correct-but-unanswered cases cannot justify a superiority claim. Required diagnostics include unconditional base, nuisance and relevant-change accuracy; per-family results; and risk-coverage curves. Do not compare each method only on its own base-correct subset. Any conditional diagnostic uses a predeclared common stratum, reports its size and is not a causal decomposition. H1 retains one primary endpoint; any component non-degradation margin and its composite claim rule must be justified and frozen before registration, not chosen to rescue a result. The pilot assesses floor effects without treating independent-branch arithmetic as measured dependence.

### H2 — Independently predictive synthesis (n = 1,200)

A discovery-eligible root passes only with all of the following: (1) a bounded rule using public measurable variables and no circular target definition; (2) at least one discriminating prediction absent from the initial narratives; (3) locked predictions made before outcome exposure; and (4) **at least four of five withheld predictions correct** under prespecified tolerances. Equivalent rule forms are evaluated on their semantics and predictions rather than exact textual match. Identification-sensitive causal wording requires corresponding intervention assumptions.

The five withheld settings must challenge plausible rival explanations rather than duplicate an easy regime. Freeze family-specific contrasts, prediction semantics, tolerances, and constant/unconditional baseline checks before outcome access. Include meaningful near-boundary settings when identifiable and adequately measured, but do not force sign reversal or a universal 2+2+1 allocation: discovery may concern magnitude, category or measurement scope. A valid simple linear rule should pass when it is sufficient. Report appropriate continuous/proper predictive scores as secondary diagnostics. Operational prediction novelty is not global scientific novelty.

The primary effect is the paired discovery-pass difference, with an **ambitious +0.10 target**. Across the other **1,200 direct/rejection or non-identifiable roots**, estimate false promotion of a novel condition. Its **one-sided 95% upper confidence bound must be ≤ 0.05**. A correct “unresolved” answer does not count as an invention. B8 and B9 must be eligible for development-only primary H2 comparator selection and all compliant methods reported; novelty is not embedding distance or eloquence.

### H3 — Correct investigation under budget (n = 1,800)

Each adaptive run begins from reduced evidence, independently of the static branches. A pass requires the correct scoped resolution **within three actions and 12 cost units**, with an audit path showing that the acquired evidence is sufficient for the declared target and claimed warrant. The sealed evaluator checks compatibility across its certified target-equivalence class, accepting equivalent action sequences and joint multi-observation identification. It does not require one favored action or discrimination against only one favored initial rival; a lucky correct guess from insufficient evidence fails the warranted-resolution endpoint. The 1,800 actionable cases combine discovery-eligible and direct/rejection classes. No action is needed when sufficient public evidence exists, though these reduced views are intended to contain a meaningful gap.

The primary effect is a paired resolution-pass difference, with **ambitious +0.10 target**. Among **600 non-identifiable roots**, the one-sided 95% upper bound for **false resolution must be ≤ 0.05**. A secondary efficiency ambition is 25% lower acquisition cost at a registered matched-accuracy/coverage operating point; it cannot substitute for the primary result.

Keep the **absolute** 5% false-promotion/false-resolution ceilings; a relative improvement over a poor baseline cannot substitute. Before registration, freeze a confidence-bound construction valid for the actual independent/stratified sampling design and assess its feasibility/power. As an illustration only, with a binomial model and a one-sided exact Clopper–Pearson 95% upper bound, n=600 permits at most **20**, not 21, false resolutions to certify ≤5%. This is not a reason to relax the bound after seeing results.

If all live candidates fail prespecified noise-aware adequacy checks, return `all_candidates_inadequate` and either reopen within budget or remain unresolved/model-inadequate. Never promote a least-bad candidate solely because all alternatives failed. Derivational and empirical warrant follow the support/defeat graph rather than a single ordered label. Multiple independent paths and sequential testing/stopping must be handled explicitly in the frozen evaluator.

Across H1–H3, preserve visible warrant states such as `source_reported`, `derived_given_premises`, `candidate_prediction`, `empirically_supported_in_scope`, `refuted_in_scope` and `unresolved`. Measure unsupported extra claims and retractions on a blinded audit sample. A source-entailment score is not automatically a probability of a world event. When genuine binary-outcome forecasts exist, report Brier score and calibration; use an appropriate proper score for continuous predictive distributions and show discrimination/coverage separately.

## 7. Inference, multiplicity and interpretation

The proposal allocates familywise two-sided alpha **0.05** across the three primary questions via **Bonferroni**: \(\alpha_j=0.05/3\approx 0.016667\). Compare paired binary root-level outcomes with **exact two-sided McNemar tests**. Report a **98.333%** paired effect confidence interval derived from a prespecified root-level percentile bootstrap (10,000 resamples; seed 9001), plus a paired-score interval as sensitivity analysis. Root is the resampling unit. The pilot may estimate the frequency of discordant pass/fail pairs *while blinded to which system wins*, not allow selection of a favorable observed direction.

For transparent planning, a normal approximation for a paired binary difference \(\delta\), with discordance probability \(q\), is

\[
n\ \approx\ \frac{\big(z_{1-\alpha/2}+z_{\mathrm{power}}\big)^2\,q}{\delta^2}.
\]

For illustration, taking \(q=0.30\), \(\delta=0.05\), the three-test correction and common normal quantiles gives roughly **1,257 roots at 80% power** or **1,622 at 90% power**, subject to approximation error and dependence assumptions. These are **not measured discordance rates or power guarantees**. At fixed net effect, higher bilateral discordance increases the required sample size. The same approximation gives about 2,432 roots for 90% power at q=0.45; these are sensitivity calculations, not exact McNemar power. Actual power could be worse. Effects by mechanism family have only n = 300, so emphasize intervals and heterogeneity rather than selective positive subgroups.

A confirmatory claim of an advantage requires a valid study, an exact paired two-sided test at the allocated alpha with a positive observed difference, a positive lower bound from the frozen 98.333% bootstrap interval, and the relevant safeguard. Both inferential conditions must pass: if test and interval disagree, report inferential disagreement/inconclusive superiority rather than selecting the favorable method. The bootstrap is not an exact inversion of McNemar and nominal coverage is not guaranteed. Freeze Monte Carlo handling, paired-score sensitivity and all component gates before unblinding; a sensitivity interval cannot replace a failed primary decision. Per-hypothesis claims and any all-three claim must state which prespecified gates passed. An ambitious target is met *descriptively* only if its point estimate reaches +0.05 or +0.10; to say evidence supports an effect of at least the target, the adjusted lower bound must also exceed it. A confidence interval spanning zero and the target is inconclusive. If the upper bound is below the target, the ambitious effect is not supported even if a smaller gain exists. Do not turn a positive secondary metric into a rescue of a failed primary.

## 8. External transfer and prospective measurement

**Textual diagnostics:** target **900 independent source/record groups**, approximately 300 each from [FEVER](https://arxiv.org/abs/1803.05355), [SciFact](https://aclanthology.org/2020.emnlp-main.609/) and [AVeriTeC](https://fever.ai/dataset/averitec.html), subject to permissions and eligible data. Freeze evidence snapshots, maintain source-cluster boundaries and hide answer-bearing verdict text. These corpora test forms of source support and fact-checking; their labels do not certify every scientific proposition as true in the outside world. Two independent human reviewers should audit ambiguous provenance and extra claims, retaining disagreement and adjudication logs.

**Discovery transfer:** choose **60 eligible [DiscoveryBench](https://arxiv.org/abs/2407.01725) tasks** by a frozen eligibility rule. Preserve the benchmark's original metric and add an audit of which predictions were committed before results were disclosed. Do not force unrelated tasks into a two-narrative contradiction format merely because CNS is organized that way.

**Prospective engineering study:** operate a local sandboxed service with controllable cache, update schedule and workload generator. The question is whether enabling caching changes median request latency *subject to a stated freshness constraint*. Tail latency, errors and resource costs are secondary. Use **240 independently seeded workload scenarios**, each with 12 prespecified settings: **two initial observations, five permitted action settings and five withheld prediction settings**. Compare cache-on/off at every setting in randomized order, with **three repeats per condition**, so the planned total is

\[
240\times12\times2\times3=17{,}280\ \text{executions}.
\]

The scenario-level estimand is performance over the specified workload distribution **conditional on the service configuration**; 240 workloads are not 240 independent mechanisms. A run is not an independent research scenario simply because it contains many requests. Hardware/day blocks and shared service configuration must be modeled; randomization controls ordering effects. The system sees the two initial measurements, may buy up to three of five action observations, then **locks all five withheld predictions**. Withheld settings are measured *after* the commitment is timestamped and hashed. A second service configuration provides a limited transport test. Broader engineering claims require multiple independently defined service/cache regimes, per-regime reporting and an uncertainty method appropriate to the number of clusters. A small number of regimes does not justify asymptotic cluster standard errors automatically. Exact replication/blocking and carryover procedures remain pending freeze. An illustrative timing assumption is not a measured runtime or procurement quote.

Define offered read-reuse fraction, dimensionless write/invalidation fraction, offered arrival rate and externally scheduled background contention; do not condition the total cache effect on downstream utilization created by the treatment. Score latency and freshness jointly as prespecified outputs, retaining freshness failures rather than deleting them. An optional future feasibility study can diagnose extraction, scoring and action-selection bottlenecks before scaling. It is not scheduled here, and an arbitrary small-sample effect cutoff is not called decisive.

The prospective test is particularly important because it exposes whether synthesis survives direct empirical comparison with a strong regression or rule baseline. A synthetic win without prospective prediction gains would sharply limit the claim, as would neglect of freshness when discussing latency.

## 9. Leakage, adjudication, negative results and stopping

Before registration, the benchmark owner must freeze the root generator and its hidden-state interface; exact transformation contracts and validators; candidate grammar and complexity caps; all prompts and model versions; measurement action costs; tolerances; code hashes; source snapshots and licenses; comparator identity for each hypothesis; fixed analyst scripts; and the exclusion/amendment process. These are explicitly unresolved design decisions; the proposal is **not ready to preregister or execute**. In particular freeze target/view feasibility and final strata, B8/B9 adaptations, challenge construction, component decision rules, confidence-bound methods, action sufficiency checks, candidate failure semantics and prospective inference scope. Recompute counts, run budgets and power assumptions if any design choice changes. The downloadable [protocol YAML](/papers/cns-9/proposed-evaluation-protocol.yaml) uses null plus explicit descriptions for values that have not been decided.

Independent evaluators should score units, exact outputs and executable rules where possible; a blinded reviewer must adjudicate semantics when the deterministically checked objects are insufficient. The model under evaluation never chooses which gold labels count. Inspect every potential leakage channel: filenames, action IDs, error text, source ordering, metadata, precomputed retrieval caches and accidental access to hidden functions. Use a strict split between runtime and scoring infrastructure. Preserve prediction hashes and public audit traces.

**Stop interpretation and regenerate confirmatory data** after hidden-label leakage, answer-dependent data cleaning, broken source-cluster isolation, unauthorized post-unblinding tuning or a scorer that fails deterministic fixtures. Transport failures are logged separately from bad semantic outputs under a frozen retry rule. Report failed and inconclusive variants, actual compute cost, unresolved outputs and all amendments. If a simple regression matches H2, prefer the simpler model. If H1 improves while H2 fails, report contrastive verification—not discovery. If H3 matches relevance-only acquisition, retire the specialized action policy. If all systems fail a mechanism family, report the domain limitation rather than declaring a universal winner.

**Publication policy for this v0.1 proposal:** no results tables, no implied preregistration, no claimed empirical superiority, and no claim that equations confer a truth guarantee. The research question remains open, testable and allowed to fail.

## 10. Source and protocol downloads

For the conceptual argument, formal objects and literature boundaries, see the [full research paper](/papers/cns-9/) and [PDF](/papers/cns-9/cns-9-research-proposal.pdf). The [accessible overview](/guides/cns-9/overview/) introduces the motivation and hypothetical caching case. Download the [proposed machine-readable protocol](/papers/cns-9/proposed-evaluation-protocol.yaml), [bibliography](/papers/cns-9/references.bib) and [complete LaTeX source](/papers/cns-9/cns-9-latex-source.zip) from the publication assets. Earlier CNS claims and boundaries are documented in the [CNS 8.0 theory](https://gtcode.com/guides/cns/theory/) and [CNS 8.0 assumptions](https://gtcode.com/guides/cns/theory-claims-assumptions/).
