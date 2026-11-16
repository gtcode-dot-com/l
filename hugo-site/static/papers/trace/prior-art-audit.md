# TRACE v0.1: prior-art audit

Prepared 15 November 2026. This targeted audit evaluates overlap, not just citation relevance. It establishes no exhaustive priority claim, reproduces no competitor results, and does not certify that TRACE merits implementation.

## Search and inspection

Primary records: arXiv versioned HTML, official proceedings PDFs, publisher records, author project pages and author repositories. Searches combined `contradictory findings`, `hypothesis discovery`, `source conflict`, `scientific agents`, `condition differences`, `abduction`, and the exact supplied titles/identifiers. Exact-ID verification covered all eight supplied leads. Backward inspection of Contrastive Discovery identified AutoDiscovery; POPPER's and Claim Cards' references were inspected for adjacent discovery, verification and interpretation work. Follow-up title/topic searches also identified the 2024 clinical-evidence study below. These follow-ups are citation chasing and targeted discovery, not an exhaustive forward-citation-index search or systematic review.

The existing bibliography retains invariant learning and its negative results, source dependence, abduction, ILP, experimental design, HypoGeniC, rule induction, Causal Modelling Agents and scientific agents. It does not follow that all such papers have had their proofs or implementations audited. Reading depth is disclosed per record in references.json.

## Closest competitors

### R41 · Contrastive Discovery

[Versioned paper](https://arxiv.org/abs/2611.14514v1) · [Author page](https://www.biojameskim.me/contrastive-discovery/). Submitted 10 November 2026.

**Inputs/method:** data and metadata; competing explanations organized as a contrast set, elicited beliefs, evidence generation and discovery search. **Evidence:** evaluated discovery workflow, rather than an untested architectural sketch. Its resolution score is not TRACE's sealed novel-condition endpoint. **Inspected:** selected methods, evaluation framing, dataset and mechanical-audit appendices. **Implementation:** author page says code “soon”; no author release was located. A paper-based implementation would be a reproduction attempt, not the author system. No execution performed. **Overlap:** Stage C/D. **Decision:** contrastive discovery is attributed prior art. A faithful adaptation and a controlled localization intervention are required; an input-format difference alone does not establish novelty.

### R42 · POPPER

[Paper](https://arxiv.org/abs/2502.09858v1) · [Author repository](https://github.com/snap-stanford/POPPER).

**Inputs/method:** free-form hypothesis and accessible resources; proposed implication tests and sequential evidence aggregation. **Evidence:** implemented multi-domain validation; guarantees require correct implications and conditional test validity. **Inspected:** method, assumptions and validity argument; repository entry point and sequential-testing implementation at commit `59611864e09dd15d7528e240ad87c7ddbb4a701c`, without execution. The code has distinct p-to-e, Fisher and LLM-estimated likelihood-ratio modes; comparator configuration must identify the mode rather than treating guarantees as interchangeable. **Overlap:** Stage D. **Decision:** falsification is inherited. Compare faithfully in the later statistical-test-compatible study; a prompt or deterministic interval heuristic does not inherit its guarantee. Source-conflict generation is a distinct evaluation intervention, not automatically an original algorithm.

### R43 · Claim Cards

[Paper](https://arxiv.org/abs/2610.20457v1).

**Inputs/method:** scientific claim; nine interpretation fields marked stated, inferred or default before evidence gathering. **Evidence:** interpretation interventions affect verdicts; recording a card alone did not measurably improve label agreement. **Inspected:** card mechanism, experimental framing and selected consistency appendix. No implementation reproduced. **Overlap:** Stage A and attribution fields. **Decision:** explicit scope is inherited. TRACE must test incremental conflict localization; correctness cannot be inferred merely from providing a schema.

### R44 · ConfRAG

[ACL record and PDF](https://aclanthology.org/2026.acl-long.11/).

**Inputs/method:** questions with conflicting retrieved web passages; answer clustering, answer and reason coverage. **Evidence:** 1,814-question benchmark. **Inspected:** task construction, evaluation and limitations; no benchmark run. Supplied cluster count and generator-side focus constrain transfer. Code/data are linked in the paper, not reproduced here. **Overlap:** alignment and conflict organization. **Decision:** use as a diagnostic; do not claim a new conflict-QA benchmark from TRACE's proposal or treat clustering success as discovery.

### R45 · Failing to Falsify

[Versioned paper](https://arxiv.org/abs/2604.02485v2).

**Inputs/method:** interactive hidden-rule tasks and counterexample-oriented interventions. **Evidence:** evaluated prompting and distillation, rather than source-lineage discovery. **Inspected:** primary abstract, selected Wason/Blicket results and evaluation framing, version metadata and method/appendix navigation; detailed statistical implementation not audited. Code is linked by the authors; not run. **Overlap:** rival generation/investigation. **Decision:** include a simple counterexample-prompting control; a complex architecture must justify its cost beyond it.

### R46 · Perceive-Then-Adjudicate

[ACL record and PDF](https://aclanthology.org/2026.findings-emnlp.1445/).

**Inputs/method:** claim, parametric knowledge and external evidence; learned agent arbitration and reflective rejection. **Evidence:** fact-checking evaluations, not held-out condition discovery. **Inspected:** architecture, experimental framing and limitations. Authors link code; not run. **Overlap:** conflict adjudication and erroneous-consensus handling. **Decision:** these are inherited ideas; a separate reliability comparison is appropriate if that becomes TRACE's remaining contribution.

### R47 · Discovery Within Validation Logic

[Publisher article](https://doi.org/10.1287/orsc.2017.1193), Behfar and Okhuysen, 2018.

**Inputs/method:** methodological analysis of abductive inquiry into anomalies and discordant findings. **Evidence:** scholarly argument and examples, not an agent benchmark. **Inspected:** selected full publisher sections on abduction and theory development. No software implementation claimed. **Overlap:** motivating premise. **Decision:** discovering explanations from contradictory findings is attributed prior art; only a specified incremental computational advantage is under investigation.

### R48 · PARADOX

[Publisher record](https://doi.org/10.1007/s10822-026-00965-5), Fata and Rahmani, published 20 October 2026.

**Inputs/method:** pharmacological reports; relation mining, contradiction graph, and contextual analysis. **Evidence:** reported evaluated extraction plus condition/missing-metadata analysis. **Inspected:** publisher abstract, metadata and data-availability statement; official [repository](https://github.com/ali-ft/PARADOX/tree/10d7a04d50e72dc375cff4146e19a42c5b022dec), selected cells in all three notebooks, and CSV headers/counts. The release contains 18,595 candidate pairs and 39 contradiction-result rows. The pipeline uses binary GPT contradiction judgments; its evaluation notebook uses `gpt_label` as the reference. These labels do not independently establish scientific truth. No committed held-out condition-prediction workflow was found in the inspected notebooks. Subscription full text remains unavailable; implementation inspection is not full-article review or result reproduction. **Overlap:** directly threatens source-disagreement-to-condition framing. **Decision:** no priority claim for that idea. The released detection/graph workflow does not establish the same endpoint as TRACE's proposed sealed predictions. That observation is limited to inspected artifacts; full-method differentiation remains unresolved. Public pairs could inform development examples after source reconstruction and independent adjudication, not serve as ready-made ground truth for predictive discovery.

### R49 · Conflicting clinical evidence with ChatGPT

[Xie and colleagues, JAMIA 2024](https://doi.org/10.1093/jamia/ocae100) · [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11187493/).

**Inputs/method:** clinical literature and assertions; identify disagreement and summarize unresolved questions. **Evidence:** evaluated evidence synthesis, not prospective predictive-condition superiority. **Inspected:** workflow and selected error analysis. No implementation reproduced. **Overlap:** scientific-source conflict analysis. **Decision:** source-grounded disagreement handling predates TRACE; the proposed new endpoint requires its own evidence.

### R50 · AutoDiscovery

[NeurIPS record](https://proceedings.neurips.cc/paper_files/paper/2025/hash/23b127521af7ca7a42f5cdb7507be4f2-Abstract-Conference.html) · [Author implementation documentation](https://allenai.github.io/asta-autodiscovery/autodiscovery/overview/).

**Inputs/method:** dataset, generated hypotheses, executable analyses and surprise-guided search. **Evidence:** existing discovery research and software. **Inspected:** official abstract, method documentation, generator instructions, structured outputs and scoring path in the [released implementation](https://github.com/allenai/asta-autodiscovery/tree/30e080f4ecf50912bb0771abb4accbf1e67bb736). It already proposes contexts, derived variables, relationships and cross-dataset hypotheses. Current software defaults can differ from paper experiments; no execution or full repository audit was performed. **Overlap:** open-ended hypothesis/evidence loop. **Decision:** attribute contextual/variable discovery as well as the loop. Compare this capable generator with and without source-conflict localization while preserving native search/scoring; do not equate model surprise with independent predictive validity.

## Contribution decision

The broad concepts are already established. The surviving proposal is a comparison: does supplied conflict localization change measurable candidates and their sealed predictions relative to strong contrastive/refinement methods with identical facts and resources? This question may already have an operational answer in uninspected work. It is not licensed as a new method merely because the present targeted search did not find that answer.

Before a priority claim, obtain PARADOX's full article lawfully, extend inspection beyond the selected implementation paths and continue forward-citation searches. The inspected code narrows the access gap but neither reproduces results nor establishes exhaustive differentiation. Those access/coverage gaps prevent an exhaustive novelty conclusion; they do not prevent attributing the established overlap or publishing this narrow, explicitly unvalidated research question. If the method is redundant, remove the claim. If the pilot provides no useful localization signal, assess uncertainty before deciding whether fresh cases or a simpler method are warranted.
