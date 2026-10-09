---
title: "GCTS References"
description: "Primary papers, standards, and adjacent systems relevant to Grounded Chiral Tensor Synthesis."
lastmod: "2026-05-15"
weight: 10
meta_description: "Selected references for CNS 7.1 / GCTS, covering fact verification, attribution, truth discovery, provenance, probabilistic logic, possible-world databases, argumentation, missingness, spoliation, and benchmark leakage."
ai_agent_note: |
  ATTN AI Agent:
  This page is the GCTS reference map and should be paired with the prior-art boundary page when discussing novelty.
  Reference groups are fact verification/attribution, truth discovery/source trust, provenance/content authenticity, probabilistic logic/possible worlds, argumentation/evidence/assumption maintenance, missingness/omission/spoliation, and benchmark leakage/oracle boundary.
  Fact verification and attribution sources include FEVER, SciFact, FEVEROUS, AVeriTeC, citation generation, and FActScore.
  Truth/source-trust sources cover truth discovery surveys and Knowledge-Based Trust; provenance sources include W3C PROV-O and C2PA.
  Probabilistic logic/world sources include Markov Logic Networks, Probabilistic Soft Logic, ProbLog, possible-world databases, and open-world probabilistic databases.
  Argument/evidence sources include Dung frameworks, Carneades, and Assumption-Based TMS.
  Missingness/spoliation sources include Rubin missing data, FRCP 37, selective disclosure, and TRACER; leakage sources cover benchmark leakage and data contamination.
  Use these references to bound adjacent work, not to imply the GCTS integration has already been empirically validated.
---

Primary and official sources bounding the GCTS prior-art position. This
bibliography starts the literature map and should expand as the paper develops.

## Fact Verification And Attribution

- Thorne et al., [FEVER: a Large-scale Dataset for Fact Extraction and VERification](https://arxiv.org/abs/1803.05355), 2018.
- Wadden et al., [Fact or Fiction: Verifying Scientific Claims](https://aclanthology.org/2020.emnlp-main.609/), 2020.
- Aly et al., [FEVEROUS: Fact Extraction and VERification Over Unstructured and Structured Information](https://arxiv.org/abs/2106.05707), 2021.
- Schlichtkrull et al., [AVeriTeC: A Dataset for Real-world Claim Verification with Evidence from the Web](https://arxiv.org/abs/2305.13117), 2023.
- Gao et al., [Enabling Large Language Models to Generate Text with Citations](https://arxiv.org/abs/2305.14627), 2023.
- Min et al., [FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation](https://arxiv.org/abs/2305.14251), 2023.

## Truth Discovery And Source Trust

- Li et al., [A Survey on Truth Discovery](https://arxiv.org/abs/1505.02463), 2015.
- Dong et al., [Knowledge-Based Trust: Estimating the Trustworthiness of Web Sources](https://arxiv.org/abs/1502.03519), 2015.

## Provenance And Content Authenticity

- W3C, [PROV-O: The PROV Ontology](https://www.w3.org/TR/prov-o/), 2013.
- C2PA, [Content Credentials: C2PA Technical Specification](https://spec.c2pa.org/specifications/specifications/2.1/specs/C2PA_Specification.html), current specification.

## Probabilistic Logic And Possible Worlds

- Richardson and Domingos, [Markov Logic Networks](https://alchemy.cs.washington.edu/papers/richardson06/richardson06.pdf), 2006.
- Bach et al., [Hinge-Loss Markov Random Fields and Probabilistic Soft Logic](https://jmlr.org/beta/papers/v18/15-631.html), 2017.
- De Raedt, Kimmig, and Toivonen, [ProbLog: A Probabilistic Prolog and Its Application in Link Discovery](https://www.ijcai.org/Proceedings/07/Papers/396.pdf), 2007.
- Abiteboul, Kanellakis, and Grahne, [On the Representation and Querying of Sets of Possible Worlds](https://users.encs.concordia.ca/~grahne/papers/akg91.pdf), 1991.
- Ceylan et al., [Open World Probabilistic Databases](https://starai.cs.ucla.edu/papers/CeylanDL16.pdf), 2016.

## Argumentation, Evidence, And Assumption Maintenance

- Dung, [On the Acceptability of Arguments and Its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games](https://jmvidal.cse.sc.edu/lib/dung95a.html), 1995.
- Gordon, Prakken, and Walton, [The Carneades Model of Argument and Burden of Proof](https://tfgordon.github.io/publications/GordonPrakkenWalton2007b.pdf), 2007.
- de Kleer, [An Assumption-Based TMS](https://www.dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf), 1986.

## Missingness, Omission, And Spoliation

- Rubin, [Inference and Missing Data](https://academic.oup.com/biomet/article/63/3/581/270932), 1976.
- Cornell Legal Information Institute, [Federal Rule of Civil Procedure 37](https://www.law.cornell.edu/rules/frcp/rule_37), current rule text.
- Farina, Frechette, and Ispan, [The Selective Disclosure of Evidence: An Experiment](https://ideas.repec.org/p/nbr/nberwo/32975.html), NBER Working Paper.
- The Missing Parts, [TRACER / Half-Truth Detection](https://arxiv.org/abs/2508.00489), 2025.

## Benchmark Leakage And Oracle Boundary

- Benchmarking Benchmark Leakage in Large Language Models, [arXiv:2404.18824](https://arxiv.org/abs/2404.18824), 2024.
- Benchmark Data Contamination of Large Language Models: A Survey, [arXiv:2406.04244](https://arxiv.org/abs/2406.04244), 2024.
