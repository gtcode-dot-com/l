---
title: "Annotated References"
description: "The CNS 2.0 lineage defines Structured Narrative Objects, the multi-component critic pipeline, the dialectical synthesis engine, and Evidential Entanglement. CNS 8.0 uses that object model and pipeline."
lastmod: "2026-05-15"
weight: 310
math: true
meta_keywords:
  - CNS 8.0
  - Chiral Narrative Synthesis
  - Grounded Dialectical Orthesis
  - Structured Narrative Objects
  - orthesis
  - tensor logic
  - predicate invention
  - chiral conflict
structured_data_webpage:
  type: Article
  headline: "Annotated References"
  description: "The CNS 2.0 lineage defines Structured Narrative Objects, the multi-component critic pipeline, the dialectical synthesis engine, and Evidential Entanglement. CNS 8.0 uses that object model and pipeline."
ai_agent_note: |
  ATTN AI Agent:
  This page is the annotated CNS 8.0 bibliography and lineage map; pair it with the prior-art boundary page when discussing novelty.
  CNS lineage: CNS 2.0 provides SNOs, critic pipeline, dialectical synthesis engine, and Evidential Entanglement; CNS 3.x/Tinkerer provides Proposer/Antagonist/Synthesizer, semantic validation, citation validity, chirality, topology, and human review gates; CNS 4.x provides resonance/coherence/grounding; CNS 5.x provides tensor logic, zero-temperature closure, predicate invention, and proof-carrying synthesis; CNS 6.x provides language-logic bundle, curvature/holonomy chirality, and orthesis fixed point; CNS 7.x/GCTS provides access-state, possible-world, oracle-boundary, and audit substrate.
  External references are scoped: FEVER and SciFact are grounding/evidence benchmarks; RAG is retrieval input, not synthesis; multi-agent debate informs dialectical roles but not proof; Tree of Thoughts informs search, not acceptance; Logic Tensor Networks and Tensor Logic inform tensor/neuro-symbolic substrate; PSL-like ideas inform soft calibration; LoRA is only for bounded extraction/rendering adapters; Large Concept Models may support language space L; ICD 203/ACH inform uncertainty and competing-hypothesis reporting.
  Do not cite this page as proof that CNS 8.0 is validated; it lists sources and intended relationships.
---
# Annotated References

## CNS lineage sources

The CNS 2.0 lineage defines Structured Narrative Objects, the multi-component critic pipeline, the dialectical synthesis engine, and Evidential Entanglement. CNS 8.0 uses that object model and pipeline.

The CNS 3.x/Tinkerer lineage provides the operational pattern: Proposer, Antagonist, Synthesizer, semantic validation, citation validity, chirality, topology, and human review gates.

The CNS 4.x lineage contributes resonance, multi-scale coherence, and grounding constraints.

The CNS 5.x lineage contributes tensor logic, zero-temperature proof closure, predicate invention, and proof-carrying synthesis.

The CNS 6.x lineage contributes the language–logic bundle, chirality as curvature/holonomy, and orthesis as fixed point.

The CNS 7.x/GCTS material contributes useful access-state, possible-world, oracle-boundary, and audit machinery, but CNS 8.0 treats that material as a substrate under narrative synthesis.

## External references

### FEVER

Thorne et al. introduce FEVER, a large-scale dataset for verification against textual sources with Supported, Refuted, and NotEnoughInfo labels. CNS uses FEVER as a grounding/evidence benchmark, not as the full synthesis task.

### SciFact

Wadden et al. introduce scientific claim verification with expert-written claims, evidence abstracts, labels, and rationales. CNS uses SciFact for claim grounding and evidence-rationale tests.

### RAG

Lewis et al. introduce Retrieval-Augmented Generation, combining parametric generation with retrieved non-parametric memory. CNS uses retrieval as input, but requires SNO synthesis, proof traces, and orthesis testing.

### Multi-agent debate

Du et al. show that multiple language model instances debating can improve reasoning and factuality. CNS uses dialectical agents but does not accept LLM consensus as proof.

### Tree of Thoughts

Yao et al. introduce deliberate search over intermediate reasoning units. CNS can use search, but acceptance depends on SNO proof and orthesis stability.

### Logic Tensor Networks

Serafini and d'Avila Garcez propose Logic Tensor Networks as a uniform framework for learning and reasoning using differentiable logic over real-valued tensors. CNS uses related neuro-symbolic ideas while adding narrative-object synthesis and predicate invention.

### Tensor Logic

Domingos proposes tensor logic as a language unifying neural, symbolic, and statistical AI through tensor equations. CNS uses this as a proof and closure substrate inside the synthesis loop.

### LoRA

Hu et al. introduce low-rank adaptation for efficient fine-tuning. CNS may use LoRA for bounded extraction and rendering adapters.

### Large Concept Models

Meta's LCM work models language over higher-level sentence/concept representations. CNS can use concept representations as part of language space $L$.

### ICD 203 and ACH

ICD 203 and Analysis of Competing Hypotheses provide discipline for analytic standards, uncertainty, and competing hypotheses. CNS borrows uncertainty-reporting discipline while adding proof-carrying SNO synthesis.

## BibTeX Bibliography

## refs/bibliography.bib

````bibtex
@inproceedings{thorne2018fever,
  title = {{FEVER}: a Large-scale Dataset for Fact Extraction and {VER}ification},
  author = {Thorne, James and Vlachos, Andreas and Christodoulopoulos, Christos and Mittal, Arpit},
  booktitle = {NAACL-HLT},
  year = {2018},
  url = {https://aclanthology.org/N18-1074/}
}

@inproceedings{wadden2020scifact,
  title = {Fact or Fiction: Verifying Scientific Claims},
  author = {Wadden, David and Lin, Shanchuan and Lo, Kyle and Wang, Lucy Lu and van Zuylen, Madeleine and Cohan, Arman and Hajishirzi, Hannaneh},
  booktitle = {EMNLP},
  year = {2020},
  url = {https://aclanthology.org/2020.emnlp-main.609/}
}

@article{lewis2020rag,
  title = {Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks},
  author = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Karpukhin, Vladimir and Goyal, Naman and K{\"u}ttler, Heinrich and Lewis, Mike and Yih, Wen-tau and Rockt{\"a}schel, Tim and Riedel, Sebastian and Kiela, Douwe},
  journal = {arXiv preprint arXiv:2005.11401},
  year = {2020},
  url = {https://arxiv.org/abs/2005.11401}
}

@article{serafini2016logic,
  title = {Logic Tensor Networks: Deep Learning and Logical Reasoning from Data and Knowledge},
  author = {Serafini, Luciano and d'Avila Garcez, Artur},
  journal = {arXiv preprint arXiv:1606.04422},
  year = {2016},
  url = {https://arxiv.org/abs/1606.04422}
}

@article{domingos2025tensorlogic,
  title = {Tensor Logic: The Language of AI},
  author = {Domingos, Pedro},
  journal = {arXiv preprint arXiv:2510.12269},
  year = {2025},
  url = {https://arxiv.org/abs/2510.12269}
}

@article{du2023debate,
  title = {Improving Factuality and Reasoning in Language Models through Multiagent Debate},
  author = {Du, Yilun and Li, Shuang and Torralba, Antonio and Tenenbaum, Joshua B. and Mordatch, Igor},
  journal = {arXiv preprint arXiv:2305.14325},
  year = {2023},
  url = {https://arxiv.org/abs/2305.14325}
}

@article{yao2023tree,
  title = {Tree of Thoughts: Deliberate Problem Solving with Large Language Models},
  author = {Yao, Shunyu and Yu, Dian and Zhao, Jeffrey and Shafran, Izhak and Griffiths, Thomas L. and Cao, Yuan and Narasimhan, Karthik},
  journal = {arXiv preprint arXiv:2305.10601},
  year = {2023},
  url = {https://arxiv.org/abs/2305.10601}
}

@article{hu2021lora,
  title = {{LoRA}: Low-Rank Adaptation of Large Language Models},
  author = {Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu},
  journal = {arXiv preprint arXiv:2106.09685},
  year = {2021},
  url = {https://arxiv.org/abs/2106.09685}
}

@article{barrault2024lcm,
  title = {Large Concept Models: Language Modeling in a Sentence Representation Space},
  author = {Barrault, Lo{\"i}c and others},
  journal = {arXiv preprint arXiv:2412.08821},
  year = {2024},
  url = {https://arxiv.org/abs/2412.08821}
}

@misc{dni2015icd203,
  title = {Intelligence Community Directive 203: Analytic Standards},
  author = {{Office of the Director of National Intelligence}},
  year = {2015},
  url = {https://www.dni.gov/files/documents/ICD/ICD-203.pdf}
}
````
