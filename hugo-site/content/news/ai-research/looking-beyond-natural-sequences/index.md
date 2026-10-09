---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-03T02:49:25.021678+00:00'
exported_at: '2026-10-03T02:49:26.335207+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/looking-beyond-natural-sequences-0827
structured_data:
  about: []
  author: ''
  description: A machine-learning framework developed by MIT biologists aims to improve
    the success rate of computational protein design while moving away from results
    that reproduce sequences found in nature.
  headline: Looking beyond natural sequences
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/looking-beyond-natural-sequences-0827
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Looking beyond natural sequences
updated_at: '2026-10-03T02:49:25.021678+00:00'
url_hash: 9f44453224e486492fc591a845600498f3d986b9
---

A protein’s function is determined by its structure, and structure — the way a protein folds — is determined by its sequence of amino acids, the building blocks of proteins.

Many methods for designing novel proteins, including examples that could bind to a disease-causing molecule in our cells, involve a two-step process: The structure comes first, and then a machine-learning framework generates a repertoire of sequences that could potentially adopt that structure.

In nature, many different amino acid sequences can fold into the same structure. At the same time, one amino acid sequence can potentially adopt different structures depending on the protein’s flexibility or a functional trigger. Therefore, when researchers use artificial intelligence to design new proteins, the challenge is to guide AI to “see” that there are many potentially useful answers — that many sequences can adopt the same fold

“For years, the field has measured success by asking whether a model can reproduce the protein sequence that evolution happened to select — our work shows that this isn’t the best metric for protein design,” says
[Amy E. Keating](https://biology.mit.edu/profile/amy-e-keating/)
, Department of Biology head, Jay A. Stein (1968) Professor of Biology,
[professor of biological engineering](https://be.mit.edu/faculty/amy-e-keating/)
, and senior author of
[a paper recently published in
*PNAS*](https://pubmed.ncbi.nlm.nih.gov/42391398/)
.

PottsMPNN, a new machine-learning framework developed in the Department of Biology, incorporates the physical principles that govern protein structure and stability, improving sequence generation and the ability to predict how mutations will affect a protein’s stability. In other words, the model has a better understanding of the sequence-energy landscape, meaning the relationship between the identity of each amino acid and the stability of the protein.

Adding this framework to a protein design pipeline will allow researchers to design structurally feasible proteins with sequences that don’t resemble those of any native protein.

“If we’re thinking about a completely novel, designed structure, there would be no native sequence to compare it to,” says graduate student and lead author Foster Birnbaum. “What we actually care about is how likely the generated sequences are to fold into the desired structures, how well the model understands the sequence-energy landscape, and how well it can predict the effect of mutations on the stability of the protein.”

**Beyond the noise**

In the same way that AI has recently powered some dramatic social changes, so too has machine learning impacted the pace and breadth of fundamental biological research. Only recently has it become possible to reliably use a computational model to generate a protein structure or sequence. Perhaps the most widely used model today, however,
[was released in 2022](https://www.bakerlab.org/2022/09/16/proteinmpnn-excels-at-creating-new-proteins/)
.

“For a field that’s moving as fast as machine learning in biology, that model has not been surpassed — we’ve been trying to understand why that is, and what it is about that model that makes it so useful,” Birnbaum says.

Birnbaum was first interested in strategic applications of something researchers call “noise,” or adding variations to a protein structure during training. Noise decreases the tendency of the model to overly mimic native sequences, increasing the diversity of structures for which it’s able to generate sequences.

PottsMPNN also uses a pairwise distribution to capture interactions between amino acids. The ability to account for the physical interactions between all 20 possible sequence options at a pair of positions in the protein is a key reason that PottsMPNN more accurately models the sequence-energy landscape than other methods.

Finally, Birnbaum says, they introduced sets of evolutionarily related sequences into training the PottsMPNN framework to teach the model how different sequences can adopt the same folded structure.

Birnbaum acknowledges that in trying to shift away from adhering to native sequences, incorporating evolutionary information is, in some ways, still a reliance on them. But PottsMPNN succeeded in demonstrating that as the model depends less and less on native sequences, structural compatibility and energy prediction, including for novel proteins, improve.

**Protein design in the age of AI**

“Once we can design any protein we want, that enables us to do a potentially scary amount of biological engineering,” Birnbaum says. “It’s a difficult task, but I’m really optimistic about this century’s progress in biology.”

Birnbaum hopes that the model could be further improved and fine-tuned for a specific task, which has in the past led to better predictions, for example, on the outcome or consequence of a particular mutation.

Ultimately, according to Keating, “Our methods move the field toward designing useful new-to-nature proteins for diverse applications while providing a stronger foundation for future advances.”