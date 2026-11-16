---
title: "TRACE: Contrast-Guided Discovery — Overview"
description: "An accessible guide to a proposed framework for using conflicting accounts to build measurable explanations, lock predictions, and seek observations that could refute them."
date: "2026-11-15"
lastmod: "2026-11-15"
draft: false
author: "GTCode.com"
math: true
toc: true
weight: 10
tags:
  - falsification-guided narrative synthesis
  - scientific discovery
  - falsification
  - research proposal
categories:
  - research
meta_description: "TRACE is an unvalidated proposal for turning narrative contradictions into measurable hypotheses, locked predictions and discriminating observations."
meta_keywords:
  - TRACE
  - Testing Rival Accounts through Contrast and Evidence
  - predictive synthesis
  - falsification-guided narrative synthesis
  - scientific discovery
structured_data_webpage:
  type: Article
  headline: "TRACE: Contrast-Guided Discovery — Overview"
  description: "An introduction to the proposed, untested TRACE research framework and its falsifiable discovery loop."
  about:
    - Testing Rival Accounts through Contrast and Evidence
    - evidence-grounded narrative synthesis
    - predictive knowledge discovery
ai_agent_note: |
  TRACE is a proposed research framework (version 0.1, 15 November 2026).
  No TRACE experiments or demonstrated improvements are reported here.
  The caching scenario is hypothetical; H1-H3 are planned tests, not findings.
---

> **Research proposal · Version 0.1 · 15 November 2026.** TRACE has not yet been empirically evaluated.

**Start here:** [Read the full TRACE research proposal](/papers/trace/) · [Download the compiled PDF](/papers/trace/trace-research-proposal.pdf) · [Examine the proposed evaluation design](/guides/trace/evaluation/)

## The question behind TRACE

Two people can report seemingly opposite facts and both be describing their observations accurately. Two scientific studies may disagree because they enrolled different populations. Two production teams can measure opposite performance effects because their workloads are different. But disagreement can also be a clue that someone measured badly, copied an unreliable report, or reached a false conclusion.

A capable reasoning system has to do more than decide which sentence sounds credible. It should determine **what the accounts are actually about**, where the evidence came from, whether a measurable missing condition explains the difference, and what new observation would distinguish that explanation from its rivals.

**TRACE (Testing Rival Accounts through Contrast and Evidence)** asks whether comparing conflicting accounts can help discover explanations that predict new observations. It develops earlier CNS work on structured accounts, provenance and conditional explanations.

TRACE remains a proposal. No engine, experiment, positive comparison or validation result is claimed in this edition. This guide explains what the proposal asks a future system to do and what would have to happen before its claims could be supported.

## How TRACE turns conflicting accounts into a testable explanation

TRACE follows four stages. [Paper Section 4](/papers/trace/#4-method-alignment-explanation-generation-and-investigation) specifies their inputs, outputs and failure states.

1. **Align the questions.** Record each account's target, population, time window, intervention and units. Convert seconds to milliseconds when justified. Keep a median and a p99 as different questions. Record what remains uncertain.
2. **Account for source dependence.** Link copies to the original measurement while preserving any new observations. Twenty copies supply one measurement; that does not make the measurement false or establish the opposing account.
3. **Generate rival explanations.** Give the generator the source accounts and a record of their specific conflicts. Each candidate identifies the claims it retains or rejects, its added relationship, its assumptions and a distinguishing prediction. A variable may be measured in both accounts, reported in only one, or proposed for a new measurement. Missing values stay unknown.
4. **Commit, investigate and decide.** Lock predictions before observing outcomes. Select a measurement that separates rivals, or acquire an explicitly required missing input. Both consume the same action budget. Record support, refutation or unresolved uncertainty at the claim level.

For example, Account A reports that caching helps under ordinary traffic. Account B reports harm during background batch work. TRACE can propose background contention as a moderator even if Account A never recorded it. The candidate must define how contention is measured and name a permitted action to obtain the missing context or test a matched workload. If that measurement is unavailable, the explanation remains pending. TRACE cannot manufacture a zero-load value for A.

The numerical compiler fits simple conditional rules when the required measurements exist. It is one way to turn an explanation into predictions, not the entire system. Small tables can be searched exhaustively. A separate experiment tests whether contrast-based ordering helps under a genuinely restrictive search budget; classical baselines are not forced to stop after 64 inexpensive conditions.

Every run produces the same linked records: questions, evidence, reports, conflicts, variables, observations, candidates, predictions, actions and decisions. The evaluator appends outcomes later. The [downloadable schema](/papers/trace/trace-records.schema.json) makes these records comparable across cases, including cases that end after unit alignment or remain unresolved.

Three comparisons answer different questions. The full pipeline competes with strong hypothesis-refinement and conventional learners. A matched generation control receives the same facts and resources without supplied conflict localization. A prioritization control uses the same frozen candidates but changes their order. These distinguish a better candidate pool from better selection and from better extraction.

## From disagreement to a testable explanation

Consider two reports: **“Caching reduces latency”** and **“Caching increases latency.”** It would be easy to pick one report, average their conclusions, or say that performance depends on context. None of those moves, by itself, discovers the missing context.

A stronger response begins by specifying the question: median request latency for which workloads, under what offered traffic and externally imposed background contention, measured over what interval, with what limit on stale responses? Next, it checks whether both reports actually target the same outcome. Perhaps one report measured tail latency, not median latency. In that case the apparent contradiction may dissolve without inventing anything.

If both reports target the same quantity, the system can propose **competing explanations**. One hypothesis might say that high reuse makes a cache helpful while frequent updates increase its overhead. Another might say that externally scheduled background work explains the difference rather than reuse. Neither hypothesis is established by sounding plausible.

The crucial next step is to write predictions *before* the next measurement. For example, the reuse and background-contention hypotheses could predict different results when read-request reuse is changed while write/invalidation fraction, offered arrival rate and scheduled background work are matched. Backend work caused by caching is allowed to change: holding that mediator fixed would change the effect being measured. Reuse means a declared fraction of repeated-key read requests, and the write fraction is dimensionless, with an explicit request denominator. A useful experiment would perform that contrast, measure both latency and freshness, and determine which predictions survived. If the measurement cannot separate the hypotheses, the correct response may still be “unresolved.”

<figure>
  <img src="/papers/trace/figures/trace-caching-example.svg" alt="Hypothetical caching example: conflicting reports lead to measurable workload conditions, two rivals, predictions locked before testing, and possible refutation or unresolved outcomes." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 2. Hypothetical caching example. None of the numbers or mechanisms in this diagram are empirical TRACE results.</figcaption>
</figure>

This is a different ambition from making an answer more fluent. A candidate explanation should earn credit only when it predicts a new observation that was not already stated in the reports. A conditional statement invented *after* all outcomes are revealed is storytelling, not a prospective discovery.

## Why use disagreement at all?

Reports may contain clues about omitted workload conditions that a prepared table leaves out. Comparing opposing accounts could focus the search when observations are sparse and possible moderators are numerous. That is a hypothesis about useful search, not a guarantee that narratives outperform statistical learning. A shared measurement bug or copied assumption can mislead every rival.

The proposed H2 comparison therefore requires a conventional rule/tree/regression learner fed the same fixed pre-action extraction as TRACE, and a close iterative hypothesis-refinement system with the same records and budget. Generic versus contradiction-guided generation is tested separately. If those simpler approaches match the result, the special synthesis loop has not justified its cost.

## What an actual TRACE system would contain

The basic unit is a **Structured Narrative Object (SNO)**: a record that keeps a question, its scope, claims, evidence references, source history, alternative explanations and uncertainty together. Unlike a loose paragraph, an SNO can say which specific measurement supports a claim, which interpretation is contested, and which prediction remains untested.

Each candidate links its proposed relationship to the accounts it explains and the observations it would predict. The numerical compiler can fit one- or two-condition rules; other rivals supply explicit expressions or action-specific commitments. Candidates awaiting measurements remain visible.

<figure>
  <img src="/papers/trace/figures/trace-discovery-loop.svg" alt="TRACE proposed discovery loop: scoped evidence and provenance, rival explanations, validated or unknown change contracts, locked predictions, discriminating actions, and support, rejection or unresolved status. A sealed evaluator is separate from runtime evidence." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 1. The proposed synthesis loop. Prediction and evaluation paths are deliberately separated; not every case ends in a validated conclusion.</figcaption>
</figure>

The core cycle has six responsibilities. It must establish comparable scope; preserve source provenance; generate and prioritize rival explanations; specify what should stay constant and what should change; commit to distinguishing predictions; and request only permitted, informative observations before revising its claims. A system might use a proposer, antagonist and verifier as functional roles. Those roles need not be separate models, and multiple model-generated perspectives never count as independent observations merely because they disagree.

The system would distinguish at least these output statuses: **reported by a source**, **derived given premises**, **proposed prediction**, **empirically supported within scope**, **refuted within scope**, and **unresolved**. Each status records a different evidential relationship. A deduction can be formally valid while its premises are false; an eyewitness report can be sincere but mistaken; an observation can be real without identifying its cause.

## Why agreement and stability are not enough

A language model can repeat the same false answer under several paraphrases. That answer is stable, yet wrong. Five agents trained on similar data can repeat the same unsupported claim. Their consensus may simply reflect a shared training source. Conversely, a correct explanation of a changing system will sometimes have to change its prediction.

David Lopez-Paz's [*Against All Likelihood*](https://arxiv.org/abs/2611.09385v1) argues that the likelihood of language under a model is not a certificate of objective truth and explores invariance across relevant environmental transformations. TRACE is motivated by that argument, but it does **not** equate invariance with a truth guarantee. The paper's own discussion makes the selection of relevant transformations a central unresolved problem. It also motivates jointly revising explanations and admissible transformations through new predictions and attempted falsification; TRACE does not originate those principles. Its inference-time sketch varies contexts and extracts an invariant core. TRACE proposes a procedure that instead retains scoped rivals, commits distinguishing predictions, and selects separating observations, with explicit provenance and failure states. The proposed contribution is a specified architecture and evaluation design for testing whether this combination adds value over existing methods. Neither its effectiveness nor its novelty follows from the specification alone.

This leads to a design feature called a **transformation contract**. For each proposed change, the contract says what changes, under what preconditions, and which relationship should hold between the old and new outputs. Reordering evidence may preserve the relevant answer; converting milliseconds to seconds changes a number but not the physical quantity; correcting a key measurement may justifiably reverse the answer; learning that several references copied one source may reduce confidence without altering the historical event.

Three things must stay distinct: an integrity check such as correct unit conversion; each rival's prediction about a world change; and the sealed evaluator's answer used only for scoring. A validator cannot decide a disputed mechanism merely by calling its prediction an invariant. Semantic checks may remain unknown, and removing one source need not lower confidence if other independent support remains.

The expected response to a transformation is not always “give the same answer.” Sometimes it is “give the correspondingly converted answer,” “withdraw the claim,” or “admit that the evidence no longer identifies the result.” The system must also be able to mark a contract **unknown**. It cannot discard a proposed transformation only because it exposes an embarrassing mistake.

This resembles established work in [invariant causal prediction](https://arxiv.org/abs/1501.01332), [behavioral testing](https://aclanthology.org/2020.acl-main.442/), and [Bayesian experimental design](https://arxiv.org/abs/2302.14545). Those are real precedents for parts of the proposal; they do not establish the effectiveness of the TRACE composition. Negative work on [invariant risk minimization](https://arxiv.org/abs/2010.05761) is a reason to insist on strong conventional baselines.

## Provenance changes the meaning of evidence

Suppose twenty websites repeat one incorrect measurement and one independent laboratory reports a conflicting value. A naive majority sees twenty against one. An evidence-aware system must ask whether those twenty accounts refer to twenty distinct observations—or to a single observation reprinted twenty times.

TRACE proposes to preserve **source lineage**, exact supporting spans, timestamps and access states. It distinguishes three different relationships: reports addressing the same question, reports sharing the same record, and nominally different records with a copying relationship. The established literature on [source dependence](https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf) is the precedent here, not a claim that TRACE originated this idea.

Provenance also constrains what the system can claim. A paywalled or lost record is not an observation of a negative result. A citation proves the existence of a report, not automatically the truth of the report. More reasoning over inaccessible information does not create that information. A good synthesis must sometimes name the specific missing measurement or source instead of manufacturing certainty.

## Why prediction commitments matter

There is a large difference between explaining an outcome after seeing it and predicting the outcome before seeing it. Modern language models are skilled at giving plausible post hoc explanations. TRACE requires each candidate relation to generate a specific **withheld prediction**: target quantity, conditions, direction or distribution, tolerance and timestamp.

A measurement can then *defeat* the candidate. If the test shows the opposite pattern, the system must be able to reject or revise its explanation. The initial proposed action policy counts disjoint, noise/tolerance-expanded rival prediction regions and divides by cost. It requires comparable predictions and a fixed treatment of duplicates, missing predictions and ties. No positive score means no separating action under this heuristic, not a solved problem. Overlapping stochastic intervals can still be informative, and an occasional tail event does not logically refute a probabilistic model. If all candidates fail the declared adequacy checks, regenerate within budget or report model inadequacy; never promote the least-bad failed candidate. If all permitted observations leave two accounts observationally equivalent, the correct output is an identification limit, not a forced reconciliation.

Rule complexity is limited to reduce overfitting. A rule such as “the cache helps exactly in the cases where it helps” does not predict anything independently. Nor does a made-up latent condition whose value is assigned retrospectively to fit each contrary example. The numerical compiler permits one predicate or a conjunction of two predicates. Other candidates must still define measurable variables, assumptions and testable predictions; narrative plausibility alone cannot qualify them. Complex mechanisms might be missed; that is a known limitation to test, not a justification for infinite hypothesis search.

## The decisive comparison

TRACE's central question is narrower than whether agents can invent and test explanations: **does explicitly locating disagreement between source accounts improve new hypotheses and sealed predictions beyond existing contrastive discovery methods with the same facts?**

The [evaluation specification](/guides/trace/evaluation/) compares ordinary hypothesis refinement (A), a Contrastive Discovery adaptation (B), conflict-directed generation (C), and that same generation with explicit lineage accounting (D). B and C both consider rival explanations. C adds a structured localization of the source conflict; its creation and errors count toward the comparison. A common selector cannot use conflict labels to favor C, and an equally budgeted summary control tests the benefit of preprocessing alone. The static adaptation and a faithful comparison with the published search method are reported separately. D and C receive the same lineage facts. Ordinary rule/regression learning and simple counterexample prompting remain strong controls.

**H2, predictive discovery, is primary.** A final candidate must add a measurable relationship absent from the initial packet and correctly predict at least four of five sealed settings, including the settings that distinguish the principal unconditional alternative. The explanation is fixed before the test contexts arrive; numerical correctness uses evaluator-fixed tolerances, so broad intervals cannot earn credit. “New” means new relative to that packet, not new to science. Correct unit conversions, identifying copied sources and extracting an already stated qualification do not earn discovery credit.

**H1, reliability, supports interpretation:** check correctness, coverage, false invention and unresolved alternatives. **H3, adaptive investigation, comes later**, if source-conflict generation first shows predictive value. Its comparisons must include established falsification and experimental-design methods.

Start with 12–20 inspected development cases, followed by a separate 30–60-case exploratory pilot. These counts assess whether extraction, generation and scoring work; they cannot establish superiority or a low false-promotion rate. Larger studies require new sample-size and feasibility justification. If existing methods generate the same candidates and predictions more cheaply, simplify or retire TRACE's proposed method.

## What prior work already does

[Contrastive Discovery](https://arxiv.org/abs/2611.14514v1) and [POPPER](https://arxiv.org/abs/2502.09858v1) directly precede the rival-testing loop. [Claim Cards](https://arxiv.org/abs/2610.20457v1), [ConfRAG](https://aclanthology.org/2026.acl-long.11/), and [PARADOX](https://doi.org/10.1007/s10822-026-00965-5) constrain the source-alignment and contradiction-analysis framing. PARADOX releases contradiction-analysis code, while [AutoDiscovery](https://github.com/allenai/asta-autodiscovery) already generates contexts, derived variables and relationships. Those capabilities are attributed prior work. TRACE has not established that its particular organization adds anything. Beyond the controlled experiment, the proposal tests an existing discovery method with and without generated conflict records, preserving its native search and scoring and charging all preprocessing costs. Contrastive Discovery code is currently listed as forthcoming; a paper-based implementation would be labeled a reproduction attempt.

The [prior-art audit](/papers/trace/prior-art-audit.md) records methods inspected and remaining access gaps. The [contribution matrix](/papers/trace/contribution-matrix.md) states which ideas are inherited and which comparisons could eliminate the remaining research claim. Publication makes the question inspectable; it does not make its answer positive.

## What changes from CNS 8.0

Earlier CNS versions already pursued the synthesis of structured narratives and developed machinery for grounding, contradiction, access limitations and predicate invention. In particular, the [CNS 8.0 core theory](https://gtcode.com/guides/cns/theory/) does not claim that orthesis stability alone is metaphysical truth, and its [worked example](https://gtcode.com/guides/cns/worked-example/) includes conditional reconciliation. TRACE retains these prior contributions.

The new emphasis is **what would make a synthesis scientifically acceptable**. Rather than place a geometric or tensor score at the center of the initial research claim, TRACE asks for a new measurable prediction, a credible opportunity for disconfirmation, and an explicit comparison against simpler methods. Formal logic remains useful for checking deductions from stated premises; it cannot by itself certify that the premises correspond to the world.

<figure>
  <img src="/papers/trace/figures/trace-research-lineage.svg" alt="Conceptual lineage from CNS 2.0 through GCTS 7.1 and CNS 8.0 to proposed TRACE, showing retained narrative and provenance concepts, revised predictive acceptance, and optional deferred mathematical machinery." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 3. Research lineage, not a chart of demonstrated performance.</figcaption>
</figure>

This choice is deliberately conservative about mathematics and ambitious about evidence. Geometry, tensor execution, environment-learning methods or elaborate multiagent protocols can still be compared later. They belong in the system only if they yield measured gains over ordinary typed rules, direct prediction and well-tuned verification.

## Status and next reading

**What exists today:** a specified research question, a data model, an operational design, a hypothetical example, a prior-art audit and a comparative evaluation proposal. **What does not exist as a claimed result:** a validated TRACE implementation, a completed comparison, a verified truth-discovery advantage, a released benchmark, or a registered experimental protocol.

The intended scientific question is precise: **Can structured disagreement and falsification-guided evidence acquisition yield new, independently predictive explanations that simpler systems miss?** Some experiments may show that the answer is no or that the benefit belongs to a much simpler component. That would be a useful research outcome, not a reason to invent additional untested theory.

For the formal definitions, complete literature discussion and discussion of risks, read [*TRACE: Contrast-Guided Discovery from Conflicting Accounts*](/papers/trace/) or its [compiled PDF](/papers/trace/trace-research-proposal.pdf). For sample construction, success criteria, action budgets and statistical decisions, read the [proposed evaluation specification](/guides/trace/evaluation/). Source and bibliographic downloads accompany the [paper page](/papers/trace/).
