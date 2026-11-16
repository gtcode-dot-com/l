---
title: 'TRACE: Contrast-Guided Discovery from Conflicting Accounts'
description: A research proposal for turning conflicting accounts into measurable explanations, committed predictions and evidence-gathering actions that could refute them.
date: '2026-11-15'
lastmod: '2026-11-15'
draft: false
author: GTCode.com
math: true
toc: true
tags:
- falsification-guided narrative synthesis
- scientific discovery
- falsification
- evidence provenance
categories:
- research
meta_description: TRACE is a conceptual, unvalidated research proposal for predictive synthesis, contrastive testing and discriminating evidence acquisition.
meta_keywords:
- TRACE
- Testing Rival Accounts through Contrast and Evidence
- falsification-guided narrative synthesis
- predictive synthesis
- experimental design
structured_data_webpage:
  type: ScholarlyArticle
  headline: 'TRACE: Contrast-Guided Discovery from Conflicting Accounts'
  description: Unvalidated conceptual research proposal with explicit hypotheses and a proposed, unregistered evaluation program.
  about:
  - Testing Rival Accounts through Contrast and Evidence
  - predictive knowledge discovery
  - falsification-guided evidence acquisition
ai_agent_note: TRACE is a proposed conceptual framework and research program, version 0.1. No TRACE experiments or superiority results are reported. H1-H3 and numerical targets are proposed tests, not findings. The caching example is hypothetical and the evaluation protocol is not preregistered.
---

> **Research proposal · Version 0.1 · 15 November 2026.** TRACE has not yet been empirically evaluated. This paper is neither peer reviewed nor preregistered.

[Read the accessible overview](/guides/trace/overview/) · [See the proposed evaluation protocol](/guides/trace/evaluation/) · [Download PDF](/papers/trace/trace-research-proposal.pdf) · [Download LaTeX source](/papers/trace/trace-latex-source.zip)

## Abstract

Conflicting accounts can reflect different measurements, dependent sources, omitted conditions or competing mechanisms. We propose **TRACE (Testing Rival Accounts through Contrast and Evidence)** to test whether explicit comparison of these accounts improves explanatory discovery. The procedure aligns questions and units, accounts for evidence lineage, generates rival explanations from localized conflicts, and tests committed predictions through permitted observations. Candidates state which claims they retain or reject, what relationship they add and which observations would distinguish them. Variables may be recorded in both accounts, reported in only one, or proposed for measurement; missing values remain unknown. A numerical rule compiler handles measured conditional relationships without defining the entire synthesis process. Shared conflict, candidate, prediction and decision records support analysis across cases. Separate controls distinguish candidate generation from prioritization and isolate reasoning after extraction from end-to-end performance. TRACE develops earlier CNS work on structured accounts and provenance, informed by Lopez-Paz's argument for investigating invariance and admissible transformations. Three proposed hypotheses concern reliability, predictive synthesis and evidence acquisition. The evaluation has a planning target of 2,400 confirmatory roots, subject to feasibility certification. **No TRACE system has been implemented or experimentally evaluated for this publication.** The contribution is a specified research procedure and comparative design; its effectiveness and methodological novelty remain unestablished.

## 1. Introduction: when disagreement is informative

Imagine one report stating that enabling a cache reduces request latency and another reporting that it increases latency. Both statements can be compatible with reality if request reuse, update frequency, resource pressure, or freshness constraints differ. They can also be incompatible because a measurement is faulty, a source copied erroneous numbers, or one account simply makes a false generalization. The correct response is not necessarily reconciliation. A system ought to distinguish different questions, reject unsupported accounts when warranted, and preserve genuinely unresolved alternatives.

This example exposes a gap between *answer selection* and *explanatory discovery*. Selecting the more credible report can be useful. So can identifying the source of a contradiction or expressing uncertainty. The larger research opportunity is to infer a **measurable condition** not stated in either report, state what new observations that condition predicts, and seek an observation capable of refuting it. If the condition merely redescribes the evidence already seen, no discovery has occurred. If the model uses hidden evaluation labels to invent it, the result is invalid. If a simple fitted regression does as well, the more elaborate synthesis process has not justified its cost.

The *Against All Likelihood* essay by Lopez-Paz argues that language likelihood is neither necessary nor sufficient for objective truth and explores invariance across relevant transformations as a guide to more robust knowledge [[1](#ref-R01)]. That argument motivates testing an account across contexts, but does not by itself resolve the crucial question of **which transformations should preserve which aspect of an answer**. A stable false statement survives every harmless paraphrase. A correct account may need to change after a new measurement or a regime shift. For TRACE, this suggests that truth-seeking requires both robustness to irrelevant differences and correct responsiveness to relevant differences—not a blanket rule that all answers should agree.

Earlier CNS work proposes synthesizing Structured Narrative Objects, rather than merely voting on isolated claims. It includes critics, evidence grounding, access states, predicate invention subject to stated limits, and the possibility of unresolved contradiction [[2](#ref-G02), [3](#ref-G03), [4](#ref-G11)]. TRACE retains those useful aims while shifting the scientific burden to new predictions and comparisons with ordinary alternatives. An independent evaluator must measure whether the procedure improves predictive outcomes.

**Why begin with narrative disagreement?** Sparse reports can contain clues about omitted conditions that are absent from a ready-made table. TRACE proposes that comparing opposing accounts can focus a finite search over those clues. This is a mechanism hypothesis, especially relevant when measurements are scarce and candidate moderators are numerous, not a theorem that prose beats tabular learning. Shared false assumptions, copied reports or abundant well-measured structured data may remove the benefit. A common-extractor learner and generic hypothesis-refinement comparator must receive the same records and budget; matched contradiction-uninformative packets test whether disagreement adds value beyond hypothesis generation itself.

**Method in brief.** TRACE records where accounts differ in target, evidence lineage, assumptions and explanatory relationships. Its generator uses those contrasts to propose explanations with measurable variables and distinguishing predictions. Acquisition can supply initially missing context, while warrant remains separate from hypothesis generation. Sections 4.1–4.6 specify the record types, generator interface, numerical compiler, action policy and stopping states. The central claim concerns predictive explanatory synthesis; generation and ordering experiments investigate possible mechanisms behind any improvement.

**Scope.** The proposed theory addresses empirical claims with explicit target variables, accessible records, or feasible observations. It does not claim a universal criterion of truth, solve disputes of values, or recover causal structure without identification assumptions. We propose a concrete representation, a discovery loop with fixed search and action budgets, and an evaluation whose failure would count against central TRACE claims. No experimental findings are offered here.

## 2. Related work and contribution boundary

### 2.1 Invariance and its limitations

Invariant causal prediction studies stable relationships under environmental changes subject to explicit assumptions about the causal system [[5](#ref-R03)]. Invariant Risk Minimization (IRM) proposes a representation in which the same predictor is optimal across training environments [[6](#ref-R02)]. These precedents motivate the question, “Which relationship remains useful under which changes?” They do **not** show that passing prompt-paraphrase tests establishes world truth, or that the prompt context generated by a language model is equivalent to an observed intervention. Negative analyses of IRM and comparisons with tuned empirical-risk baselines are central warnings against treating invariance as a solved optimization problem [[7](#ref-R04), [8](#ref-R05), [9](#ref-R06)]. Work on discovering environments adds possible future tools but not a reliable admissibility oracle [[10](#ref-R07)].

Lopez-Paz motivates the joint investigation of explanations and admissible transformations, including the use of new predictions and attempted falsification [[1](#ref-R01)]. TRACE adopts that motivation; it does not claim these principles as original contributions. His inference-time sketch generates answers under varied contexts and extracts an invariant core. TRACE proposes a different operational procedure: retain competing scoped explanations, commit their distinguishing predictions before acquiring outcomes, and select evidence-gathering actions using a specified rival-separation rule. Explicit provenance, transformation contracts, and failure states make that procedure inspectable. Whether this combination improves predictive synthesis or investigation over simpler alternatives remains an empirical question.

Behavioral testing supplies a practical precedent for structured perturbations, and counterfactually augmented examples distinguish robust behavior from sensitivity to superficial cues [[11](#ref-R08), [12](#ref-R09)]. However, a transformation that removes the only relevant source is not a mere nuisance. Neither is changing a measured causal input. A benchmark must state the expected response for each transformation instead of rewarding identical strings under every condition.

### 2.2 Evidence, source dependence, and warranted assertion

Retrieval-augmented generation and chain-of-verification can help connect an answer to accessible evidence [[13](#ref-R11), [14](#ref-R16)]. Source dependence is a separate issue: many reports may reproduce the same originating record and therefore should not be treated as independent confirmations [[15](#ref-R10)]. This is particularly important when a seemingly broad consensus is produced by copying. TRACE distinguishes (i) whether two claims address the same estimand, (ii) whether they rely on the same record, and (iii) whether nominally distinct sources share a lineage. These are not interchangeable quantities.

A cited source can establish that a statement **was reported**, not that the statement is automatically correct. Likewise, a valid deduction from premises remains conditional on the premises. SNOs therefore preserve exact source spans, time, access and dependency, while a separate warrant field records whether the claim is source-reported, derived given premises, empirically supported within scope, refuted within scope, or unresolved. Existing CNS 8.0 material recognizes the distinction between an internally stable orthesis and metaphysical truth; our proposal makes predictive and observation-based tests additional explicit gates, not a retrospective claim that the prior work ignored uncertainty [[2](#ref-G02), [3](#ref-G03), [16](#ref-G08)].

### 2.3 Aggregation, debate, abduction, and argumentation

Self-consistency aggregates multiple reasoning samples; debate structures disagreement between models; verification asks targeted subquestions [[17](#ref-R12), [18](#ref-R13), [14](#ref-R16)]. Results of multi-agent comparisons suggest that debate must be compared against simpler voting or aggregation rather than credited with improvement by default [[19](#ref-R14)]. Model-generated reasons can also be unfaithful to the causes of a model's answer [[20](#ref-R18)], so TRACE audits short, externally checkable justifications rather than treating hidden reasoning traces as evidence.

The distinction between supporting and attacking arguments has a long formal tradition in abstract argumentation [[21](#ref-R32)]. Abductive inference generates candidate explanations from observations; computational forms include cost-based first-order abduction [[22](#ref-R33)]. Inductive logic programming (ILP) supplies a precedent for rule and predicate learning in a specified language [[23](#ref-R21)]. These traditions already cover substantial ground claimed informally by many “discovery” systems. TRACE does not claim to invent abduction, argument attacks, or predicate invention. The proposed contribution is a specified architecture and evaluation design for **contradiction-guided predictive synthesis**. Its research claim concerns the incremental value of combining these components, rather than the invention of invariance testing, abductive explanation, or experimental design individually. The specification alone does not establish novelty; comparisons with existing hypothesis-generation and discovery systems must establish what, if anything, the combination adds.

Iterative hypothesis generation is already a close precedent. HypoGeniC updates a bank of natural-language hypotheses using prediction errors on labeled examples [[24](#ref-R37)]. Qiu and colleagues propose, select and refine rules with symbolic interpretation, distinguishing rule induction from reliable application [[25](#ref-R38)]. These methods motivate a required refinement comparator, rather than treating discovery as a comparison only with answer aggregation. Causal Modelling Agents combine LLM metadata reasoning with data-driven structural causal models [[26](#ref-R39)]; that is relevant hybrid causal-modeling precedent, not evidence for the proposed TRACE procedure or a universal intervention capability.

### 2.4 Choosing observations and existing discovery agents

Piriyakulkij and colleagues combine LLM-proposed natural-language rules, probabilistic belief updates and experiment design [[27](#ref-R40)]. This is a close precedent for the hypothesis–experiment loop. TRACE therefore tests the added value of explicit comparison between source accounts, including their measurement and lineage differences, rather than claiming to originate automated experimentation.

Bayesian experimental design gives a principled account of selecting actions to reduce uncertainty when the relevant hypotheses, likelihoods and priors can be specified [[28](#ref-R20)]. Active learning for causal structure makes the experimental-choice problem concrete [[29](#ref-R31)]. TRACE uses a set-separation heuristic when probability models are unspecified and compares it with relevance-based and random acquisition. Predicting intervention outcomes does not by itself identify a causal graph.

Modern work already explores agentic scientific workflows: *The AI Scientist* automates parts of idea generation, experimental code and reporting [[30](#ref-R34)]; *Co-Scientist* develops scientific hypotheses through agent coordination and evaluation [[31](#ref-R35)]; and *Robin* connects literature agents, analysis and experimental biology [[32](#ref-R36)]. These contributions sharply constrain any claim that CNS invented multiagent research, hypothesis generation or experiment planning. TRACE instead proposes to test whether **specific contradiction-derived scope rules, prediction commitments and measured falsification opportunities** add value over well-resourced alternatives. DiscoveryBench provides a separate transfer diagnostic, while FEVER, SciFact and AVeriTeC test forms of source-grounded verification rather than universal truth [[33](#ref-R25), [34](#ref-R26), [35](#ref-R27), [36](#ref-R28)].

## 3. Epistemic commitments and nonclaims

Four distinctions govern the proposal.

**Truth is not identical to current warrant.** Whether a scoped proposition is true in the world is separate from whether the available record supports saying so. The system can update warrant after evidence arrives without changing the historical fact being described. A true claim with inaccessible support remains unwarranted; a previously strong citation can later be retracted.

**Coherence is not correctness.** Propositions can agree because they share a mistaken assumption, training artifact or copied source. A stable internal model can be a sensible computational stopping condition, not proof of objective truth. This applies to deductive closure, round-trip translation, majority vote, and invariance over model-generated perspectives.

**Stable mechanism is not constant output.** A representation-only nuisance change should preserve the relevant meaning, up to an explicit transformation of units or format. If the population, intervention or measurement changes, a credible explanation may predict a *different* outcome. If a unique support record disappears, the empirical event need not change but the warrant may weaken. We therefore use transformation-specific output relations.

**Uncertainty is not lack of access.** Observation noise, unavailable records, open-world ambiguity, and observationally equivalent mechanisms imply different limitations. Two worlds that supply exactly the same permitted observations but require different conclusions cannot be separated merely by more model deliberation. The legitimate output may be a set of live alternatives and an identification boundary.

TRACE treats a proposed new scope condition as a hypothesis until its operands are observable and it has predictive consequences not exhausted by the source examples. A cause is not identified merely because a story explains a correlation. A probabilistic forecast must refer to a specified event; token likelihood is not used as its substitute. These commitments are falsifiable at the level of system behavior and externally measured outcomes; they are not axioms purportedly guaranteeing truth.

## 4. Method: alignment, explanation generation and investigation

### 4.1 Four-stage procedure and common records

TRACE asks whether comparing the explanatory structure of conflicting accounts helps generate independently predictive explanations. Its four stages are **alignment**, **lineage accounting**, **rival generation**, and **investigation with warrant assignment**. The numerical compiler in Section 4.4 is one component of rival generation. Cases can stop at any stage with a recorded reason; successful normalization alone does not count as explanatory discovery.

A question is \(q=(Y,\mathcal P,t,\mathcal I,u,\tau)\): outcome definition and aggregation, population, time/window, intervention or observation context, units and tolerance. An evidence atom records its source, exact span or measurement, timestamp, access state, measurement lineage and collection context. A report contains atomic claims, assumptions and asserted explanatory relationships, each linked to evidence atoms. The record distinguishes `source_stated` content from `extractor_inferred` interpretation. Neither attribution nor extraction establishes truth.

**Stage A: alignment.** Compare the questions and create a conflict record \(\Delta(A,B)\). Its `estimand_status` is `same`, `unit_convertible`, `different` or `unknown`. A unit mapping records its formula and preconditions; apply it only when the outcome definition, aggregation and relevant scope match. Median and p99 are different targets, not convertible units. Preserve them as separate questions unless the required underlying distribution is available. Different context populations may motivate a transport/scope hypothesis; do not silently treat their observed effects as contradictory measurements of one fixed population. Record separately whether the sources assert incompatible generalizations, whether their observed intervals differ, and what context differences might explain the contrast.

**Stage B: lineage accounting.** Record `shared_origin`, `distinct_origins`, `mixed` or `unknown`, with evidence for each lineage link. Collapse only duplicate measurements, retaining source attribution and any additional observations. Distinct origins do not guarantee statistical independence. Copied support contributes once; copying does not refute the claim, validate its rival, or identify the true mechanism. Unknown dependence remains explicit and receives prespecified sensitivity analysis. A defective measurement can be excluded only for a recorded defect criterion; the exclusion does not establish the competing account.

**Stage C: rival generation.** Use the report claims, assumptions, relationships and conflict record to propose conditional explanations or rival mechanisms (Section 4.3). Variables can enter through three provenance states: `observed_shared` (values recorded in both accounts), `observed_asymmetric` (recorded in one but missing in another), or `inferred_unmeasured` (proposed, with no measured values). These states apply relative to the cited report pair; cell-level missingness remains recorded. A variable's `conflict_ids` lists applicable conflict records and may be empty during extraction. If its provenance state differs across pairs, use pair-specific variable records linked to the same operational definition. Observed in prose need not mean numerically fit-ready. No missing value may be inferred merely because an explanation needs it.

**Stage D: investigation and adjudication.** Commit testable predictions, acquire permitted observations and update claim-specific warrant. A candidate requiring new measurements remains pending until it can predict or be fitted. A case with no available identifying observation remains unresolved. Runtime cannot certify global non-identifiability; that classification belongs to the sealed evaluator. Runtime records which alternatives remain and why its permitted actions cannot separate them.

**Common export.** Every run uses the same linked tables, including runs that never generate a fitted rule. IDs join records within a case; null denotes unknown, never false or zero.

| Table | Required scientific content |
|---|---|
| `questions`, `evidence`, `reports` | Target/scope; source spans and measurements; claims, assumptions and explanatory relations with attribution type |
| `conflicts` | Report and question IDs; estimand and lineage statuses; incompatible claims; context differences; transformations and unresolved fields |
| `variables`, `observations` | Definition, units/type, provenance state and measurement procedure; observed values, time and lineage, including missing cells |
| `candidates` | Conflict IDs; retained/rejected claim IDs; added relationship; assumptions; variable IDs; executable prediction or pending dependencies; generation rank and status |
| `predictions`, `actions` | Candidate, target and action IDs; prediction region, tolerance, commitment time; requested measurement, response and cost |
| `decisions` | Stage, affected claim IDs, reason, evidence IDs, warrant and unresolved alternatives |
| `scores` | Evaluator-only outcomes, errors, endpoint verdicts and mechanism-family strata, appended after commitment |

The downloadable [record schema](https://gtcode.com/papers/trace/trace-records.schema.json) defines these fields and types. Referential integrity, source-span fidelity, units and temporal availability are semantic requirements beyond JSON shape validation. Candidate and decision traces describe program operations, not private model reasoning. Aggregate by independent root, not by the number of candidates or observations. This allows the same analysis to distinguish alignment corrections, dependence adjustments, new conditions, refuted candidates and unresolved cases across F1–F8 without passing family labels to runtime.

### 4.2 Transformation contracts

Three records must remain separate. A **representation/evidence-integrity contract** \(c_T=(T,\operatorname{pre}_T,r_T,v_T,z_T)\) declares an operation, preconditions, a property that should be preserved or converted, a validator and a state \(z_T\in\{\text{validated},\text{rejected},\text{unknown}\}\). Unit conversion can require numerical equivariance; a demonstrably redundant copy must not count as another independent observation. The preconditions matter: order can encode chronology, a paraphrase can change scope, and a copied document can contain new evidence. Semantic validity is not universally decidable by deterministic code. Removing evidence can change warrant, but does not impose a universal direction of confidence change.

A **rival-indexed response commitment** \(r_{T,h}\) states how hypothesis \(h\) predicts an outcome will respond to a world, regime or evidence change. Different rivals may make incompatible commitments. The runtime need not know which mechanism is true before recording that disagreement. Knowing that an operation preserves units does not establish that a disputed world change preserves the outcome.

An **evaluator-only relation** specifies the benchmark's expected behavior from its sealed state. It scores the method after outputs are locked and is never passed to runtime as a validated contract. Gold-admissibility access is a diagnostic ceiling, excluded from superiority claims.

For a representation/evidence-integrity contract, the check remains three-valued:

\[
C_T(x)=\begin{cases}
\mathrm{pass},&z_T=\mathrm{validated}\text{ and }r_T\text{ is verified},\\
\mathrm{fail},&z_T=\mathrm{validated}\text{ and }r_T\text{ is violated},\\
\mathrm{unknown},&\text{the contract or necessary evidence is unresolved}.
\end{cases}
\]

For a rival-indexed commitment, the system records predictions and later adequacy checks, not an oracle verdict about admissibility. Validators, tolerances and expected evaluation relations must be frozen before confirmation. A failed or unknown contract cannot be discarded merely because its result is inconvenient.

### 4.3 Rival generation and prediction commitments

**Generator interface.** A run begins with one extraction call over the permitted source packet. The extractor produces source-linked report and observation records. Its instruction is: “Preserve each account's question, claims, assumptions and asserted relationships with exact evidence IDs. Separate explicit statements from your interpretations. Record missing or ambiguous values as null. Do not reconcile accounts or supply absent measurements.” Deterministic code performs verified unit conversions, duplicate-measurement accounting and record joins; uncertain semantic alignments stay unknown.

One generation call then receives the complete permitted packet, its extracted records, the conflict records, the action menu and the remaining budget. The instruction is: “For each unresolved comparable conflict, propose explanations that account for its observations. For each candidate, identify the claims retained or rejected, the added condition or relationship, its assumptions, and a prediction that differs from a rival. Cite the conflict and evidence IDs motivating it. Mark every added variable as observed_shared, observed_asymmetric or inferred_unmeasured. For missing measurements specify a procedure and permitted action, or mark unavailable. Include an account-rejection explanation only when evidence supports a defect; allow all accounts to be inadequate. Output candidate records, not a consensus essay.”

The initial specification permits up to eight proposals per generation call, one schema-repair call containing only structural errors, and two generation rounds in an adaptive run. A static run has one round and no acquisition. The second adaptive round receives acquired observations and the preceding candidate records, with old predictions immutable. These are proposed engineering limits, to be fixed with the model version, inference settings and packet construction before confirmation. Invalid or excess proposals remain logged and consume generation budget; repairs cannot receive scoring outcomes.

**Variable acquisition.** An asymmetric variable cites the source passage establishing its presence and the rows where its value is missing. An unmeasured variable includes an operational definition, units or categories, when it would be observed, motivating evidence or an explicitly labeled mechanistic conjecture, and a permitted measurement action if one exists. Neither variable state is a supported explanation. After acquisition, update cell values and availability while preserving the original provenance state. Missing context can become a measured predictor within the run. If no permitted action can supply it, record `measurement_unavailable` and retain uncertainty rather than filling the column by inference.

**Candidate representation.** A candidate must explain which original observations it accommodates, which claims it changes and why its added relation would account for the difference. Prediction forms are: a numerical expression over defined variables; a conditional rule; or a categorical/interval commitment for a specified action. Executable expressions use constants, variable IDs, arithmetic, comparisons and conditional selection; division by zero or unavailable operands yields an unknown prediction. No generated code executes outside this expression interpreter. Parameters must be declared as fitted from identified observations, source-specified, or conjectured. Conjectured parameters can make testable predictions but acquire no empirical warrant from being written down. Narrative-only candidates remain `pending_prediction` and cannot earn H2 credit. Causal candidates additionally declare intervention assumptions; predictive success alone cannot establish a causal graph.

Candidate validity requires resolvable IDs, supported source attributions, consistent units, an identified target and no use of future outcomes. Semantic fidelity is assessed with a frozen rubric and blinded independent adjudication for the study; these judgments score the run and do not feed back into runtime. An explanation is allowed to retain one account, reject both, introduce a scope condition or preserve competing mechanisms. The parser enforces format and dependencies, not truth.

**Prioritization.** At most four candidates are active for investigation. Order valid proposals first by whether they address an explicitly localized incompatibility, then by the number of distinct observed report contexts they account for without an unsupported value assignment, then by fewer newly assumed variables; break ties by canonical candidate ID. These are auditable proposal features, not calibrated truth probabilities. Include measurable pending candidates as well as currently executable ones. Log all proposals and rankings so candidate generation can be separated from selection effects. Select a final prediction candidate using the same ordering among candidates that remain adequate; report unresolved where none qualifies. The numerical compiler may rank alternative parameterized rules within a candidate using Section 4.4; its training score cannot compare arbitrary prose mechanisms or confer warrant.

Before any scored observation is revealed, write a prediction commitment \(k=(h,q,\hat y,\tau,a,t_0)\) with the candidate, question, prediction, tolerance, action/context and timestamp. Preserve the record immutably. Operational novelty requires a new relationship or scope condition and a distinguishing consequence absent from the initial accounts; merely translating units, extracting an existing qualification or changing a source weight does not satisfy H2. An explanation must also account for the motivating observations under its stated assumptions. Its held-out predictions, rather than its rhetorical plausibility, determine predictive success.

For task-appropriate loss \(\ell\), predictive error remains
\[
R_e(M)=\mathbb E_{(x,y)\sim P_e}[\ell(M(x),y)].
\]
Report risk alongside coverage and false promotions. A binary world-event forecast can use Brier loss \((p-y)^2\) [[37](#ref-R22)]; a document-entailment confidence is a different quantity. The evaluator's task definitions and tolerances are fixed before confirmation.

### 4.4 Numerical rule compiler and search-order experiment

The numerical compiler implements one candidate form within Stage C. It accepts numerical outcomes and predictor measurements available in every fitting row, including variables measured through an earlier permitted action. Other candidate forms use the prediction interface in Section 4.3. The compiler's restricted language does not define the full TRACE architecture or cover every benchmark mechanism.

A compiled rule predicts one constant, or two constants separated by one predicate or a conjunction of two predicates on distinct variables. Numeric predicates use midpoints between consecutive observed values; categorical predicates test equality to observed categories. Each conditional branch requires at least two distinct measurement-lineage units. Copy duplicates count once; repeated readings within a lineage/context first form a mean. Missing cells produce `requires_measurement`, not silent complete-case selection. Record identifiers, source identities and target-derived variables cannot be predictors. Numeric extrapolation, unseen categories and missing prediction inputs return unknown under this compiler.

Fit branch constants by weighted least squares and rank fitted alternatives by
\[
J(g)=\sum_i w_i\left(\frac{y_i-g(x_i)}{s_q}\right)^2+\lambda k(g),\qquad
w_i=\frac{1}{L n_{\ell(i)}}.
\]
Here \(L\) is the number of identified measurement lineages, \(n_{\ell(i)}\) is the number of context rows in row \(i\)'s lineage, \(s_q>0\) is a prespecified target scale, and \(k\) is the predicate count. Equal lineage weights prevent duplicated reporting from increasing weight; they do not establish independence or optimal statistical weighting. Unknown lineage is retained for dependence sensitivity analysis. The initial penalty \(\lambda=0.01\) is an engineering setting requiring development-stage justification. Training fit chooses alternatives to test; only subsequent observations can support the predictions. Tolerance-expanded prediction regions are not asserted to be calibrated confidence intervals.

For small tables, enumerate all admissible conditions. Do not withhold inexpensive classical computation to manufacture an advantage for TRACE. B8 may use ordinary trees, regression or exhaustive rules within the common measured resource budget, rather than inheriting an artificial 64-rule cap.

A separate **search-order experiment** fixes the extracted variables and complete candidate language. For each eligible report pair and predicate, take the absolute difference in its observed context frequencies, then average over pairs. A pair with missing predicate values receives no contrast score for that predicate; log its missingness. Order single predicates and then two-predicate conjunctions by decreasing mean contrast score, with canonical-ID ties. Compare this order with a fixed seeded permutation and exhaustive enumeration, using identical fitting and selection. A 64-condition prefix is one explicitly labeled diagnostic on distractor-heavy/high-dimensional cases, alongside the full budget curve. It is not the primary TRACE definition or a resource ceiling imposed on B8. Report candidate count, CPU time, model calls/tokens, external actions and total measured cost. If all conditions fit within the budget, rankings should coincide and there is no search-order advantage to explain.

The **generation experiment** is distinct. Give TRACE and its matched generator control identical raw evidence, extracted records, models, call budgets and downstream compilers/action policies. TRACE receives the explicit conflict record and the contrast-directed generation instruction. The control receives the same source facts and the instruction to propose and test explanations, without supplied conflict localization or contrast-priority instructions; it is free to discover conflicts itself. Differences in the resulting candidate pool test the value of supplied structured comparison. B9 provides the stronger end-to-end iterative-refinement comparison. To study prioritization alone, freeze a candidate pool produced without evaluation outcomes and permute only its ordering. Never compare different generated pools and attribute the result solely to ordering.

These component experiments are secondary mechanism analyses, with paired root-level estimates and intervals reported separately from H1–H3. Prespecify any inferential family and multiplicity treatment before claiming component superiority. A positive overall H2 result supports the evaluated pipeline; it cannot by itself identify the contribution of generation, extraction or prioritization.

### 4.5 Selecting evidence

Stage D first seeks an action with comparable predictions from every active rival. A pending candidate cannot be silently removed to make the separation score computable. If none is scorable because required measurements are missing, use a **prerequisite measurement policy**: among permitted actions that supply an explicitly named missing variable, unit-mapping input or lineage record, choose the lowest declared cost; ties follow candidate priority and stable action ID. Log the dependency and the action's purpose. This is data completion, not claimed information gain. Recompute candidate eligibility after observing the response. Such actions consume the same three-action/12-unit budget and may fail to enable a prediction. An unavailable measurement or absent separating action leads to unresolved status, not an invented value. Static branches cannot use this policy to obtain new evidence.

The proposed discrimination policy is a **deterministic set-separation heuristic**. Let \(\mathcal H_c\) be the deduplicated live candidates with executable commitments on a common outcome, and let \(A_h(a)\) be candidate \(h\)'s prediction region after the frozen measurement-noise and decision-tolerance expansion has been applied exactly once. For feasible actions with strictly positive, declared costs, define

\[
U(a)=\frac{1}{\operatorname{cost}(a)}
\frac{\displaystyle\sum_{\{h,h'\}\subseteq\mathcal H_c}
\mathbf 1\!\left[A_h(a)\cap A_{h'}(a)=\varnothing\right]}
{\displaystyle\binom{|\mathcal H_c|}{2}},
\qquad a^*=\arg\max_{a\in\mathcal A_{\mathrm{feasible}}}U(a).
\]

This policy is defined only when at least two comparable candidates exist and every retained candidate supplies an admissible prediction for the action. Zero-cost lookups are part of the common initial evidence, not a division by zero. Missing predictions make an action unscorable under this policy; they are logged rather than silently excluded from its denominator. Deduplication uses a frozen candidate-normalization rule, with residual duplicates audited. Ties use a stable action ID assigned independently of the hidden mechanism. If no action has positive score, return `no_separating_action`; do not claim that uncertainty is resolved. The prerequisite policy applies only to explicit missing dependencies; it does not replace a zero separation score with an unsupported certainty claim. Other policies can be studied as labeled alternatives under the same budget.

For certain set-valued predictions, disjointness means that one observed value cannot satisfy both commitments. Probabilistic intervals are different: a tail observation does not logically falsify a stochastic model. Overlapping intervals may still allow useful repeated or multivariate observations, so this heuristic can miss informative actions. The heuristic provides no optimality, version-space reduction or causal-identification guarantee. Candidate misspecification remains a failure mode.

When a prior and observation likelihood are actually specified, expected information gain minus cost is a conventional alternative [[28](#ref-R20)]:

\[
a^*=\arg\max_a\{\mathbb E_{y\mid D,a}[D_{\mathrm{KL}}(p(h\mid D,a,y)\Vert p(h\mid D))]-\lambda\operatorname{cost}(a)\}.
\]

The initial heuristic does not execute this Bayesian objective or manufacture numeric posteriors for prose. Its actual utility must be compared with random, relevance-only, uncertainty-based and model-based policies where those are well defined.

### 4.6 Warrant, promotion and stopping

A system records claim-specific warrant using these statuses:

- `source_reported`: attributed to an available source.
- `derived_given_premises`: follows subject to stated premises.
- `candidate_prediction`: committed but not yet adequately tested.
- `empirically_supported_in_scope`: meets declared evidential criteria.
- `refuted_in_scope`: fails the relevant adequacy criterion.
- `unresolved`: available evidence does not settle the claim.

These states are not a ladder that turns derivability into truth. A compound SNO can contain differently warranted claims. A conditional synthesis may be promoted only when scope and measurement are explicit, its essential evidence is traceable, and its externally checked predictions satisfy a prespecified threshold. That promotion is provisional and revisable.

Warrant is tracked through the evidence/assumption dependency graph, not a scalar weakest-link ladder. Derivation preserves its premise qualifications; several independent support paths may strengthen a claim, and defeat of one path need not erase the others. Promotion requires independently checked evidence and prespecified, noise-aware adequacy criteria. A single missed probabilistic interval is not automatic model refutation. Sequential checks and stopping rules must be fixed rather than selected after outcomes are seen.

If all candidates fail those adequacy criteria, record `all_candidates_inadequate`: repeat candidate generation within the stated limits if budget remains, otherwise return an unresolved/model-inadequate result. A least-bad candidate cannot be promoted solely because its failed rivals are worse. An inability to score a candidate remains unknown, not a pass.

The system must stop when actions or compute are exhausted, no available action distinguishes remaining rivals, the estimand is underspecified, or further acquisition has no defensible value. Stopping cannot be reported as certainty. The proposed objective is *fewer unjustified claims and more useful independent predictions*, not a universal solver for every empirical question.

## 5. Proposed operational algorithm

The proposed loop in Figure 1 separates runtime evidence acquisition from sealed experimental evaluation. Functional roles—proposer, critic, synthesizer, verifier—do not require separate models; multiple prompts from one model do not become independent sources. Deterministic validators should handle units, type checks, timestamps, schemas and executable rules. Human or model-assisted semantic review may be necessary, but review uncertainty must remain visible.

<figure>
  <img src="/papers/trace/figures/trace-discovery-loop.svg" alt="Proposed discovery loop. Integrity checks and rival-indexed predictions precede acquisition. Only committed outputs cross into sealed evaluation; no gold outcomes return to runtime." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 1. Proposed discovery loop. Integrity checks and rival-indexed predictions precede acquisition. Only committed outputs cross into sealed evaluation; no gold outcomes return to runtime.</figcaption>
</figure>

```text
INPUT: source packet, questions, permitted actions, resource budgets
1  Extract source-linked claims, assumptions and observations.
2  Align questions; apply valid unit mappings; preserve unknowns.
3  Account for measurement lineage; record conflicts and context gaps.
4  Generate typed rivals and variable measurement requirements.
5  Validate dependencies; compile eligible numerical rules.
6  Rank proposals; activate at most four; preserve pending candidates.
7  Lock predictions before observation; run integrity checks.
8  Select a separating action or a logged prerequisite measurement.
9  Acquire within budget; update records and candidate adequacy.
10 Regenerate at most once; preserve all earlier commitments.
11 Assign warranted conclusions or unresolved status; export records.
OUTPUT: conflict, candidate, prediction, action and decision tables
```

A contract should not be validated by the same example whose result it was invented to rationalize. Development can refine the grammar and validator; calibration can tune abstention; confirmatory cases must be new. The system may request a measurement from an outcome service, but that service must return an ordinary reading rather than a hidden label such as “hypothesis true.” The benchmark evaluator sees sealed mechanisms and withheld predictions **only after** the runtime outputs have been committed [[16](#ref-G08)].

Validation should be adversarial. A candidate that says “the cache helps exactly when it helps” is circular. A rule invented solely to rescue every negative example is disallowed by specified rule grammar and held-out tests. A stable false answer fails external correctness. A continually abstaining system fails coverage. A model that always reconciles fails on direct-rejection controls. Conversely, a model that refuses to synthesize whenever sources disagree should fail discovery-eligible cases. These negative cases test whether the procedure can reject inappropriate synthesis.

## 6. Worked example: caching, mechanisms and refutation

<figure>
  <img src="/papers/trace/figures/trace-caching-example.svg" alt="Hypothetical caching contrast. Reuse/write-fraction and external-contention rivals commit predictions before a separating measurement. Downstream utilization is not held fixed; latency and freshness are both scored." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 2. Hypothetical caching contrast. Reuse/write-fraction and external-contention rivals commit predictions before a separating measurement. Downstream utilization is not held fixed; latency and freshness are both scored.</figcaption>
</figure>

Figure 2 is a *hypothetical illustration*, not a TRACE run. Define \(\Delta L=L_{\mathrm{cache\ on}}-L_{\mathrm{cache\ off}}\) in milliseconds for a fixed offered workload. Negative values indicate lower median latency. Separately predict and measure staleness; a workload is a deployment-success case only if its declared freshness bound (for example, stale-response fraction at most 0.01) is satisfied. Do not drop freshness failures after seeing them or condition the latency estimate on selected successful requests.

Let \(r\) be the fraction of **read requests** repeating a key already requested within a prespecified reuse window, and \(u\) the fraction of **all offered requests** that are writes/invalidation requests. Both are dimensionless workload settings, not an observed cache-hit rate or writes per second. The denominator of \(r\) requires \(u<1\); feasible key schedules, arrival rate and request mix must be specified. A relation for communication only is

\[
\Delta L_{\mathrm{toy}}=(3-30r+10u)\ \mathrm{ms},\qquad 0\le r\le1,\quad0\le u<1.
\]

This invented relation illustrates a possible data-generating mechanism. The TRACE numerical compiler fits piecewise-constant approximations to observations; it does not infer the displayed formula or its coefficients from prose. Two reports do not identify its coefficients. Rival \(H_1\) proposes dependence on reuse and write fraction. Rival \(H_2\) proposes that **externally scheduled background contention** explains the contrast. External offered traffic and background work can be controlled; backend utilization caused by cache hits is a mediator, not a quantity to match across treatment arms. Concurrency policy, hardware capacity, payload distribution and reuse-window definition must also be fixed or explicitly varied.

Before observing a new workload, lock each rival's latency and freshness predictions. A feasible contrast varies reuse while matching write fraction, offered arrival rate and scheduled background contention; a complementary contrast varies external contention at matched workload settings. Randomize cache-on/off order and monitor carryover. Do not artificially hold downstream CPU/database work constant while claiming the total caching effect. If neither contrast separates the rivals, record that limitation. If all candidates fail noise-aware adequacy checks, reopen within budget or remain model-inadequate.

The cross-case record makes this example operational. Suppose background work is recorded in report B but absent from A. The conflict row identifies the incompatible latency generalizations and this context gap. A candidate names contention as `observed_asymmetric`, retains the two reported measurements, and adds the hypothesis that contention changes the caching effect. An action requests A's missing context or a permitted matched workload. Its response populates an observation row; it cannot retroactively alter the candidate's earlier commitments. A mechanistic candidate may instead propose a new measurable factor as `inferred_unmeasured`, with a measurement procedure and a falsifiable prediction. If no action can measure it and no justified prediction is available, it remains pending.

Other outcomes follow the same record path. A milliseconds/seconds difference yields a validated mapping and an alignment decision, with no H2 discovery credit. A p99/median difference yields distinct questions. Copied reports yield a lineage adjustment without a truth verdict. Rival causal accounts that no permitted action separates yield unresolved decisions. These records permit comparisons of failure and resolution types across cases while preserving their evidential differences.

The prospective evaluator scores commitments against withheld measurements collected later. Runtime may receive only the outcomes of permitted acquisition actions, not gold mechanisms or evaluation verdicts. The same extracted measurements must be available to direct rule/regression learners. Correct predictive scope need not identify a unique causal graph; causal wording requires defensible interventions and assumptions.

## 7. Three falsifiable hypotheses

The following are **proposed** hypotheses, sample sizes and effect-size targets. They are not measured effects or a registered protocol. The full public specification is at [the TRACE proposed evaluation page](https://gtcode.com/guides/trace/evaluation/).

**H1 — Contrastive reliability.** Compared with the best compliant development-selected baseline, will TRACE more often issue warranted answers that preserve semantics under six nuisance changes and respond correctly to four relevant changes? The independent root-level endpoint requires correct base content and all ten appropriate branch relations. The proposed primary population has \(n=2400\) roots and a target of **+5 percentage points** in root-level success. A safeguard on 1,800 resolvable cases demands that the lower one-sided 95% confidence bound for the coverage difference exceed **-2 percentage points**. A positive result explained entirely by abstention would not support H1.

**H2 — Independently predictive synthesis.** On 1,200 discovery-eligible roots, will TRACE more often generate a measurable, non-circular scope rule, at least one new distinguishing prediction absent from the initial narratives, and **at least four correct outcomes out of five withheld predictions**? The target is **+10 percentage points** versus a development-selected comparator pool that must include the common-extractor learner and iterative refinement system. On the other 1,200 roots, the upper one-sided 95% confidence bound for false novel-scope promotion must not exceed **5%**. If a direct rule learner, regression model, or better-calibrated verifier matches TRACE, the distinctive synthesis hypothesis is weakened or falsified. H2 tests the proposed synthesis procedure.

For H2, the selected prediction set is locked on the static branch's permitted record. An initially unmeasured variable may support a hypothetical rival, but cannot earn H2 success without the measurements or justified commitments needed to predict all five scoring settings. Static and adaptive results are not pooled: synthesis after acquired context is a secondary adaptive endpoint, reported beside H3. Alignment corrections, duplicate-source accounting and faithful restatement of an existing rule do not qualify as novel synthesis. H2 also requires a source-linked account of the motivating observations; a frozen, blinded rubric assesses fidelity and novelty separately from numerical prediction accuracy.

**H3 — Disagreement-guided investigation.** Given the same reduced evidence and at most **three external actions / 12 cost units**, will TRACE more often reach the correct scoped conclusion on 1,800 action-resolvable roots than random, relevance-based, uncertainty-only, or further-discussion alternatives? The target is **+10 percentage points**. A 600-root non-identifiable control imposes an upper one-sided 95% bound of **5%** on false resolution. A secondary action-cost target is 25% reduction at matched accuracy; it cannot replace a failed primary endpoint.

The hypotheses may succeed or fail separately. H1 without H2 would support a contrastive verifier rather than a new method of knowledge discovery. H3 without H2 could indicate useful active learning based on ordinary hypotheses. H2 without credible source tracing and withheld evaluation would not establish the claim being made here. No decision is rescued by post hoc reweighting of the three endpoints.

## 8. Proposed evaluation design and safeguards

The controlled study is built around **independent root worlds**, not the number of prompts. It proposes 120 engineering fixtures outside the scientific evidence; 600 development roots; 600 calibration roots; 240 pilot roots; and 2,400 confirmatory roots, totaling **3,840 new research roots**. Confirmatory cases span eight mechanism families with 300 roots each: confounding; effect modification; selection and missingness; measurement/representation; regime change; dependent reporting; rare/nonlinear interactions; and observational equivalence. F7 and F8 are held out from prompt and generator tuning as families, with the limitation that pre-trained models may still know the abstract concepts. The provisional allocation is 150 discovery-eligible, 75 direct/rejection and 75 non-identifiable roots per family (1,200/600/600 overall). These are planning targets pending a target/view feasibility audit. For F8, causal graphs can remain observationally equivalent while agreeing on the observational prediction scored by H2; that does not license causal identification. A root is non-identifiable only if accessible evidence/actions leave different answers to its declared target possible. Static and reduced adaptive views are certified separately. Family labels describe evaluator challenges, not runtime routing instructions; a root may require several stages and no operator is assumed to solve an entire family. Eligibility is certified separately for static predictive synthesis and adaptive resolution. If the proposed cells cannot be constructed without shortcuts, revise the allocation, denominators and dependent arithmetic before registration rather than forcing the uniform grid.

Each root supplies one base presentation, six nuisance branches and four relevant-change branches: **11 static presentations per root**. An adaptive action branch starts from a fresh state and may reveal permitted measurements; it is separate from the static evaluations. Repeated branches, different prompt orderings and model seeds do not create additional independent worlds. Gold transformations are established by generator checks and independent review before the test. Invalid contracts discovered later are disclosed, not silently removed.

Ten systems are proposed: strong retrieval-augmented generation (B1); RAG plus chain-of-verification (B2); RAG with self-consistency (B3); an operational interpretation of the focal essay's multi-context sketch (B4); a grounded/provenance-aware extension of that sketch (B5); grounded debate (B6); a transparently documented operational subset of CNS 8.0 (B7); a common-extractor ordinary learner (B8); a documented iterative hypothesis-refinement adaptation (B9); and TRACE. B4 and B5 are **our documented operationalizations** of Lopez-Paz's inference-time sketch, not implementations provided by its author. They do not represent an exhaustive implementation of the essay's broader philosophical program. Comparisons against them assess these particular procedures under the stated budgets. B7 must list omissions and cannot stand for all possible CNS 8.0 systems. B8 and B9 are required primary H2 comparator candidates. The B8 mechanism comparison shares a fixed pre-action extraction result and charges extraction to every system; end-to-end results are also reported. TRACE may propose new measurable variables under Section 4.3. Shared-extraction comparisons freeze their common input view; end-to-end comparisons permit different extraction and acquisition paths with the same source evidence, action menu and total budget. Report both rather than attributing an end-to-end gain solely to reasoning. B9 uses the same evidence and budget, with its adaptation to this task disclosed [[24](#ref-R37), [25](#ref-R38)]. Section 4.4 separates generation, candidate prioritization and numerical search-order controls; their paired root-level estimates are reported separately from the three primary tests. Seven ablations remain secondary controls. A positive primary H2 result alone cannot establish which stage caused the gain. Noncontradictory controls must not remove relevant facts merely to weaken the alternative.

Fairness requires identical accessible evidence, action menus and effective compute ceilings, not identical rhetoric or forced token spending. The proposed budget is at most 120,000 input and 30,000 output tokens per system-root: eleven static branches at 8,000/2,000 apiece, and one adaptive branch at 32,000/8,000. Each system has at most three adaptive actions costing at most 12 units. The primary comparator for each hypothesis is selected using **development data only** and frozen before final evaluation. Two model families and two seeds are suggested as replications; a prespecified one-family/one-seed configuration anchors the primary comparisons, and repeated roots are analyzed as clusters.

The proposal allocates a familywise alpha of 0.05 across three primary comparisons (Bonferroni, two-sided \(\alpha=0.05/3\)), paired root-level exact McNemar tests, and **98.333%** effect intervals estimated by a frozen paired bootstrap; a paired-score interval is sensitivity analysis. Primary claims require both the adjusted exact test and the frozen bootstrap lower bound to support a positive effect, plus their safeguards; a test/interval disagreement is reported as inconclusive, not resolved by choosing the favorable result; reaching a point target is descriptive unless its adjusted lower confidence bound also exceeds that target. Absolute 5% false-promotion/false-resolution limits are retained, not relaxed to match a weak baseline; their interval method and attainability under the actual sampling design must be frozen. H1 keeps one strict primary endpoint with required unconditional component diagnostics; any non-degradation margins are pending. H2 challenge sets must distinguish plausible rivals by task, not impose sign reversals on every family. H3 requires sufficient acquired evidence for its target, not merely a lucky correct guess or a prescribed action. Menus and costs must be checked for hidden-answer cues. Approximate power calculations assume a particular discordance rate and are **not** guarantees of statistical power. All numeric choices remain changeable **before** registration, with a visible versioned amendment history; they may not change after viewing confirmatory outcomes without breaking the primary claim.

Transfer tests are proposed, not executed: 900 source-clustered groups across FEVER, SciFact and AVeriTeC; 60 eligible DiscoveryBench tasks; and 240 prospective caching/workload scenarios. The caching design calls for 12 settings per scenario, two cache conditions and three repeats, yielding **17,280 planned executions**. Measurements for five withheld settings would be collected after predictions are locked. Benchmark labels about document support, fact checking and inferred data relationships are not interchangeable certificates of external truth. All study phases require secure runtime/evaluator separation, source-cluster splits, prediction hashes, frozen inference settings, deterministic scoring where possible, and independent review of semantic edge cases.

A failure analysis is part of the design. Leakage of hidden labels, post hoc tolerance changes, source duplication across splits, or inability to reproduce the scorer invalidate a confirmatory claim. Excessive abstention, arbitrary invented predicates, harms from extra model calls, or gains achieved only against intentionally weak controls count against TRACE. The prospective scenario-level estimand is conditional on its service configuration, with hardware/day/carryover blocks; 240 workloads are not 240 independent mechanisms. Broader transfer claims require multiple independently defined regimes and an analysis appropriate to the number of clusters. A synthetic success without prospective transfer would support at most a narrower benchmark result, not generalized scientific discovery. An optional future feasibility study may diagnose extraction, scoring and acquisition bottlenecks before scaling; no small fixed effect threshold is claimed decisive and no experiment is scheduled by this proposal.

## 9. Relationship to earlier CNS and design choices

<figure>
  <img src="/papers/trace/figures/trace-research-lineage.svg" alt="Conceptual research lineage, not measured improvement. TRACE retains structured evidence and uncertainty while evaluating predictive acceptance against simpler alternatives." loading="lazy" decoding="async" style="max-width:100%;height:auto;">
  <figcaption>Figure 3. Conceptual research lineage, not measured improvement. TRACE retains structured evidence and uncertainty while evaluating predictive acceptance against simpler alternatives.</figcaption>
</figure>

Figure 3 depicts conceptual lineage rather than measured improvement. CNS 2.0 introduced a research program around SNOs, chiral opposition and criticism; GCTS 7.1 emphasized grounded evidence and access-state distinctions; CNS 8.0 restored synthesized SNOs and proposed orthesis conditions, proof traces and predicate invention with complexity limits [[38](#ref-G13), [4](#ref-G11), [2](#ref-G02), [39](#ref-G09)]. CNS 8.0 already states that orthesis stability is not metaphysical truth and can preserve unresolved contradictions. TRACE develops this lineage through predictive acceptance criteria and explicit comparison of explanatory accounts.

The proposal retains structured accounts, provenance, versioned revisions, rival interpretations, and the ability to construct a conditional new account. It revises the meaning of productive conflict: shared target, explicit evidentiary relationships and **testable differences in predictions** matter more than a single combined chirality score. The previous literature's use of “Evidential Entanglement” conflated at times shared evidence identifiers with comparable study endpoints; TRACE records semantic comparability, shared records and source copying independently [[39](#ref-G09)].

Proof closure remains useful for checking derivability from stipulated premises. Round-trip language-to-logic fidelity remains useful for identifying translation errors. Both checks concern the representation and its premises; neither independently verifies the world claim. Manifold geometry, curvature, holonomy, topological reduction, tensor execution and large multiagent societies are **optional future comparators**, not prerequisites. They should return only if a specific reproducible task demonstrates gains beyond simpler representations at acceptable cost. The original work is preserved as prior art rather than rewritten as validated implementation evidence.

## 10. Risks, limits, and alternative explanations

**Admissibility is underspecified in the world.** A model may call a transformation irrelevant even though it changes the question, or reject a relevant change because it undermines a preferred answer. Independently reviewed development contracts and held-out contract families reduce—but cannot eliminate—this risk. Unresolved contracts retain their unknown status in the output.

**The hypothesis interface introduces bias.** The numerical compiler can miss relationships outside its rule language. Generated mechanisms can also omit relevant variables or rely on unsupported assumptions; an executable prediction does not remove that risk. Expanding the language risks overfitting, combinatorial search and post hoc excuses. The primary study should report both failures to represent the truth and unjustified inventions; neither can be cured silently after unblinding.

**Synthetic worlds may reward the generator's assumptions.** A test set built from the designer's mechanism families can privilege algorithms that match those families. External tasks, unseen families and prospectively acquired data must therefore count heavily in interpretation, even though none establishes universality. Publication of generator code after evaluation is necessary but not sufficient if the models' training corpora contain familiar templates.

**Evidence is not independent just because prose differs.** Copied records, model-generated perspectives and repeated calls may share the same error. The dependency graph itself can be uncertain. A fair comparison must give baseline systems the same provenance fields and assess the ability to detect unknown dependencies rather than scoring a fabricated certainty.

**Observation policy can be harmful or uninformative.** High information gain may target the wrong hypothesis class or exceed a privacy, safety, or resource budget. The first prospective example is a sandboxed software service, not human subjects or clinical interventions. External actions require domain-specific permission and governance; the proposal confers no authority to run arbitrary experiments.

**The explanatory narrative may be unfaithful.** A plausible causal sentence is not proof of the model's actual inference process [[20](#ref-R18)]. The deliverable should be a compact, source-linked and checkable claim, its prediction record and its test outcome. Causal language should be reserved for designs where the identification assumptions are defensible.

**Alternatives may explain any future gain.** A structured SNO schema, more compute, a better retrieval index, source deduplication, direct regression, or simpler active learning could capture all apparent improvement. The proposed ablations and well-resourced baseline suite are required to distinguish the proposed mechanism from these alternatives.

**The ambition is domain-limited.** Scientific and software observations sometimes admit controlled interventions and clear metrics. Historical claims, sparse observational science and normative disagreement may not. TRACE must say “unresolved” where there is no permitted identifying observation, rather than imply that every contradiction hides a discoverable conditional truth.

## 11. Research agenda and conclusion

The first implementation should follow Sections 4.1–4.6 and provide a benchmark that separates runtime observations from evaluator answers. The generator, action service and scorer must enforce that separation. A second gate tests whether novel scope rules predict hidden observations better than selection, verification and simple induction. A third evaluates whether choosing discriminating actions changes what the system can legitimately conclude. Only after these gates should training, learned contract discovery, more elaborate geometry or broader causal claims be considered.

TRACE tests whether structured comparison of conflicting accounts helps produce explanations with independent predictive value. Its records connect source claims and localized disagreements to generated candidates, required measurements, committed predictions and final warrant. The evaluation separates whole-pipeline performance from the contributions of extraction, generation, prioritization and acquisition. Evidence of an advantage would support the tested procedure in the stated settings; comparable performance from simpler methods would limit the case for using it.

## Citation and version note

**GTCode.com (15 November 2026).** *TRACE: Contrast-Guided Discovery from Conflicting Accounts*. Research proposal, version 0.1. Canonical edition: **https://gtcode.com/papers/trace/**. This version is not peer reviewed, not preregistered, and contains **no TRACE experimental results**. The web research article, the compiled PDF, and the supplied LaTeX source correspond to the same v0.1 substantive manuscript. A public companion [overview](https://gtcode.com/guides/trace/overview/) and [proposed evaluation specification](https://gtcode.com/guides/trace/evaluation/) are separate interpretive and protocol documents.

## References

<a id="ref-R01"></a>**[1] David Lopez-Paz (2026). Against All Likelihood.**<br>
https://arxiv.org/abs/2611.09385v1

<a id="ref-G02"></a>**[2] GTCode Editorial / GTCode.com (2026). CNS 8.0 Theory.**<br>
https://gtcode.com/guides/cns/theory/

<a id="ref-G03"></a>**[3] GTCode Editorial / GTCode.com (2026). CNS 8.0 Theory Claims and Assumptions.**<br>
https://gtcode.com/guides/cns/theory-claims-assumptions/

<a id="ref-G11"></a>**[4] GTCode Editorial / GTCode.com (2026). Grounded Chiral Tensor Synthesis Theory.**<br>
https://gtcode.com/guides/cns-gcts/theory/

<a id="ref-R03"></a>**[5] Jonas Peters; Peter Buhlmann; Nicolai Meinshausen (2016). Causal inference using invariant prediction: identification and confidence intervals.**<br>
https://arxiv.org/abs/1501.01332

<a id="ref-R02"></a>**[6] Martin Arjovsky; Leon Bottou; Ishaan Gulrajani; David Lopez-Paz (2019). Invariant Risk Minimization.**<br>
https://arxiv.org/abs/1907.02893

<a id="ref-R04"></a>**[7] Elan Rosenfeld; Pradeep Ravikumar; Andrej Risteski (2021). The Risks of Invariant Risk Minimization.**<br>
https://arxiv.org/abs/2010.05761

<a id="ref-R05"></a>**[8] Pritish Kamath; Akilesh Tangella; Danica Sutherland; Nathan Srebro (2021). Does Invariant Risk Minimization Capture Invariance?.**<br>
https://proceedings.mlr.press/v130/kamath21a.html

<a id="ref-R06"></a>**[9] Ishaan Gulrajani; David Lopez-Paz (2021). In Search of Lost Domain Generalization.**<br>
https://arxiv.org/abs/2007.01434

<a id="ref-R07"></a>**[10] Mohammad Pezeshki; Diane Bouchacourt; Mark Ibrahim; Nicolas Ballas; Pascal Vincent; David Lopez-Paz (2024). Discovering Environments with XRM.**<br>
https://proceedings.mlr.press/v235/pezeshki24a.html

<a id="ref-R08"></a>**[11] Divyansh Kaushik; Eduard Hovy; Zachary C. Lipton (2020). Learning the Difference That Makes a Difference with Counterfactually-Augmented Data.**<br>
https://arxiv.org/abs/1909.12434

<a id="ref-R09"></a>**[12] Marco Tulio Ribeiro; Tongshuang Wu; Carlos Guestrin; Sameer Singh (2020). Beyond Accuracy: Behavioral Testing of NLP Models with CheckList.**<br>
https://aclanthology.org/2020.acl-main.442/

<a id="ref-R11"></a>**[13] Patrick Lewis and colleagues (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.**<br>
https://arxiv.org/abs/2005.11401

<a id="ref-R16"></a>**[14] Shehzaad Dhuliawala and colleagues (2023). Chain-of-Verification Reduces Hallucination in Large Language Models.**<br>
https://arxiv.org/abs/2309.11495

<a id="ref-R10"></a>**[15] Xin Luna Dong; Laure Berti-Equille; Divesh Srivastava (2009). Integrating Conflicting Data: The Role of Source Dependence.**<br>
https://www.vldb.org/pvldb/vol2/vldb09-pvldb47.pdf

<a id="ref-G08"></a>**[16] GTCode Editorial / GTCode.com (2026). CNS 8.0 Oracle Boundary.**<br>
https://gtcode.com/guides/cns/oracle-boundary/

<a id="ref-R12"></a>**[17] Xuezhi Wang and colleagues (2023). Self-Consistency Improves Chain of Thought Reasoning in Language Models.**<br>
https://arxiv.org/abs/2203.11171

<a id="ref-R13"></a>**[18] Yilun Du; Shuang Li; Antonio Torralba; Joshua B. Tenenbaum; Igor Mordatch (2024). Improving Factuality and Reasoning in Language Models through Multiagent Debate.**<br>
https://proceedings.mlr.press/v235/du24e.html

<a id="ref-R14"></a>**[19] Hyeong Kyu Choi; Xiaojin Zhu; Sharon Li (2025). Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Models?.**<br>
https://arxiv.org/abs/2508.17536

<a id="ref-R18"></a>**[20] Miles Turpin; Julian Michael; Ethan Perez; Samuel R. Bowman (2023). Language Models Do Not Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting.**<br>
https://arxiv.org/abs/2305.04388

<a id="ref-R32"></a>**[21] Phan Minh Dung (1995). On the acceptability of arguments and its fundamental role in nonmonotonic reasoning, logic programming and n-person games.**<br>
https://doi.org/10.1016/0004-3702(94)00041-X

<a id="ref-R33"></a>**[22] Naoya Inoue; Kentaro Inui (2013). ILP-based Inference for Cost-based Abduction on First-order Predicate Logic.**<br>
https://doi.org/10.5715/jnlp.20.629

<a id="ref-R21"></a>**[23] Andrew Cropper; Sebastijan Dumancic (2022). Inductive Logic Programming at 30: A New Introduction.**<br>
https://arxiv.org/abs/2008.07912

<a id="ref-R37"></a>**[24] Yangqiaoyu Zhou; Haokun Liu; Tejes Srivastava; Hongyuan Mei; Chenhao Tan (2024). Hypothesis Generation with Large Language Models.**<br>
https://arxiv.org/abs/2404.04326v3

<a id="ref-R38"></a>**[25] Linlu Qiu; Liwei Jiang; Ximing Lu; Melanie Sclar; Valentina Pyatkin; Chandra Bhagavatula; Bailin Wang; Yoon Kim; Yejin Choi; Nouha Dziri; Xiang Ren (2024). Phenomenal Yet Puzzling: Testing Inductive Reasoning Capabilities of Language Models with Hypothesis Refinement.**<br>
https://arxiv.org/abs/2310.08559v4

<a id="ref-R39"></a>**[26] Ahmed Abdulaal; Adamos Hadjivasiliou; Nina Montana-Brown; Tiantian He; Ayodeji Ijishakin; Ivana Drobnjak; Daniel C. Castro; Daniel C. Alexander (2024). Causal Modelling Agents: Causal Graph Discovery Through Synergising Metadata- and Data-Driven Reasoning.**<br>
https://discovery.ucl.ac.uk/id/eprint/10195820/1/8513_Causal_Modelling_Agents_C.pdf

<a id="ref-R40"></a>**[27] Wasu Top Piriyakulkij; Cassidy Langenfeld; Tuan Anh Le; Kevin Ellis (2024). Doing Experiments and Revising Rules with Natural Language and Probabilistic Reasoning.**<br>
https://proceedings.neurips.cc/paper_files/paper/2024/hash/5f1b350fc0c2affd56f465faa36be343-Abstract-Conference.html

<a id="ref-R20"></a>**[28] Tom Rainforth; Adam Foster; Desi R. Ivanova; Freddie Bickford Smith (2024). Modern Bayesian Experimental Design.**<br>
https://arxiv.org/abs/2302.14545

<a id="ref-R31"></a>**[29] Simon Tong; Daphne Koller (2001). Active Learning for Structure in Bayesian Networks.**<br>
https://ijcai.org/proceedings/2001/118

<a id="ref-R34"></a>**[30] Chris Lu; Cong Lu; Robert Tjarko Lange; Jakob Foerster; Jeff Clune; David Ha (2024). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery.**<br>
https://arxiv.org/abs/2408.06292

<a id="ref-R35"></a>**[31] Juraj Gottweis; Wei-Hung Weng; Alexander Daryin; Tao Tu; et al. (2026). Accelerating scientific discovery with Co-Scientist.**<br>
https://doi.org/10.1038/s41586-026-10644-y

<a id="ref-R36"></a>**[32] Ali E. Ghareeb; Benjamin Chang; Ludovico Mitchener; et al. (2026). A multi-agent system for automating scientific discovery.**<br>
https://doi.org/10.1038/s41586-026-10652-y

<a id="ref-R25"></a>**[33] Bodhisattwa Prasad Majumder and colleagues (2025). DiscoveryBench: Towards Data-Driven Discovery with Large Language Models.**<br>
https://arxiv.org/abs/2407.01725

<a id="ref-R26"></a>**[34] James Thorne; Andreas Vlachos; Christos Christodoulopoulos; Arpit Mittal (2018). FEVER: a large-scale dataset for Fact Extraction and VERification.**<br>
https://arxiv.org/abs/1803.05355

<a id="ref-R27"></a>**[35] David Wadden and colleagues (2020). Fact or Fiction: Verifying Scientific Claims.**<br>
https://aclanthology.org/2020.emnlp-main.609/

<a id="ref-R28"></a>**[36] Michael Sejr Schlichtkrull; Zhijiang Guo; Andreas Vlachos (2023). AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web.**<br>
https://fever.ai/dataset/averitec.html

<a id="ref-R22"></a>**[37] Tilmann Gneiting; Adrian E. Raftery (2007). Strictly Proper Scoring Rules, Prediction, and Estimation.**<br>
https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf

<a id="ref-G13"></a>**[38] Ekewaka Lono (2025). CNS 2.0 Research Roadmap: Blueprint.**<br>
https://gtcode.com/guides/cns-2.0-research-roadmap/blueprint/

<a id="ref-G09"></a>**[39] GTCode Editorial / GTCode.com (2026). Worked Example - CNS 8.0 Resolves a Conditional Contradiction.**<br>
https://gtcode.com/guides/cns/worked-example/

## Publication downloads and self-citation

- [Compiled research PDF](/papers/trace/trace-research-proposal.pdf) · [Standalone LaTeX source](/papers/trace/trace-latex-source.zip) · [BibTeX self-citation](/papers/trace/trace-citation.bib)
- [Cross-case record schema](/papers/trace/trace-records.schema.json)
- [Annotated reference registry](/papers/trace/references.json) · [Bibliography](/papers/trace/references.bib) · [Proposed protocol YAML](/papers/trace/proposed-evaluation-protocol.yaml)

**How to cite:** GTCode.com. (2026, November 15). *TRACE: Contrast-Guided Discovery from Conflicting Accounts* (Research proposal, version 0.1). https://gtcode.com/papers/trace/
