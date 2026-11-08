---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-08T05:50:03.610122+00:00'
exported_at: '2026-11-08T05:50:07.278918+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity
structured_data:
  about: []
  author: ''
  description: Learn how Google Antigravity and our Cheminformatics Skills accelerate
    drug discovery workflows, search compounds, and propose novel rigidified macrocycles.
  headline: Agentic cheminformatics with Google Antigravity
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/agentic-cheminformatics-with-google-antigravity
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Agentic cheminformatics with Google Antigravity
updated_at: '2026-11-08T05:50:03.610122+00:00'
url_hash: adafdd4764cb9dbbcc8baf5f90eab559ee61ffdd
---

November 3, 2026

Science

# Agentic cheminformatics with Google Antigravity

Zoi Tsangalidou, Ruijie (Kelly) Zhang, Sukhdeep Singh and Michael V. LeVine

Copied

Designing new medicines requires curating complex data from charts, figures and literature, training predictive models, and proposing candidate molecules to synthesize â a workflow that typically takes multiple days for a single iteration.

Here we show how
[Google Antigravity](https://antigravity.google/use-cases/science)
, equipped with our new Cheminformatics Skills, accelerates drug discovery workflows. Using real-world lung cancer treatments, an agent searches through thousands of compounds, performs matched molecular pair analysis, and proposes novel rigidified macrocycles with synthetic routes in just an hour.

Chemistry is one of scienceâs richest public records
*â*
spanning millions of structures across journal articles and vendor catalogs. It provides a common representation that links physics and mathematics to the life and environmental sciences. Molecules and their transformations are ubiquitous and shape the everyday world.

Despite decades of progress in cheminformatics, chemists still spend too much time wrangling data, a process complicated by the fact that molecules can be represented in many ways: from text descriptions to images or data structures. The same molecule can appear as an
[IUPAC](https://en.wikipedia.org/wiki/IUPAC_nomenclature_of_organic_chemistry)
name in a paper, a
[Markush structure](https://en.wikipedia.org/wiki/Markush_structure)
in a patent, or a structure-data file (SDF) in a catalog. Advanced cheminformatics systems must be able to unify these sources and deal with the many ways errors can arise in them. This task has no margin for error â alter a single atom or bond and you have described a different compound altogether, rendering a promising inhibitor or catalyst inert.

To let scientists focus on hypotheses rather than data wrangling, we built a suite of
**Cheminformatics Skills**
for
[Google Antigravity](https://antigravity.google/use-cases/science)
, turning the surface into a collaborative science workbench with full access to local tooling for both computational chemists and experimental bench chemists.

The skills also create a division of labour where the underlying language model handles workflow orchestration, database navigation and scientific reasoning, while deterministic chemistry tools execute molecular calculations. Grounded in
[RDKit](https://www.rdkit.org/)
, the foundational open source cheminformatics toolkit developed over two decades by a global community of contributors, alongside connectors to curated resources from
[ChEMBL](https://www.ebi.ac.uk/chembl/)
and
[PubChem](https://pubchem.ncbi.nlm.nih.gov/)
, the skills encode domain best practices directly into the agentâs workflow.

## Rigidifying a floppy molecule

In this technical walkthrough, we highlight a classic medicinal chemistry technique to improve drug potency: rigidification.

Drug molecules can be complex, often linking multiple substructures through rotatable bonds. Those bonds let the molecule twist into many 3D shapes (conformations), making it âfloppyâ in solution. To bind its target, however, a floppy molecule must lock into a single active shape. Losing that freedom of motion carries an entropic penalty, which weakens binding affinity and lowers potency.

To solve this problem, medicinal chemists often rigidify molecules by adding new bonds. Two substructures linked by a single rotatable bond can twist into many conformations, but adding a second bond to tie them together sharply limits how they can move in three dimensional space. By placing that bond in the right spot, chemists can lock the molecule into the exact shape needed to bind its target. This strategy, often called âpaying the entropic cost in advanceâ, can dramatically boost potency.

Here, we will focus on a well-known case of successful rigidification. The drug crizotinib is a first-generation, small-molecule tyrosine kinase inhibitor (TKI) used to treat certain forms of non-small cell lung carcinoma. In crizotinib, there are five major rotatable bonds. Lorlatinib is a third-generation, small-molecule TKI that resembles crizotinib, but has been cyclized at its end to reduce the effective number of rotatable bonds to zero, leading to higher potency among other effects.

## Collaborative Intelligence

We will ask the agent to search through literature for these drugs and their analogues. With the Cheminformatics skills in Antigravity, the agent is able to extract molecules from these documents, associate them with the data reported, and prepare the compounds for downstream analysis.

Within minutes, the agent retrieves thousands of compounds, filters out irrelevant molecules (such as buffers and solvents), and documents their sources in a report. The report also provides an initial analysis of the retrieved compound set: highlighting, for example, that the macrocycles are largely predicted to be brain-penetrant, an important property given that the target lung cancer frequently metastasizes to the brain.

For deeper exploration, the agent launches an interactive viewer displaying the curated compounds, their associated data, and customizable scatter plots. For example, plotting potency against rotatable bonds, colored by macrocycle status, immediately reveals that macrocycles like lorlatinib tend to have fewer rotatable bonds and higher potency. Ultimately, we designed these skills to not only expand the agentâs chemistry capabilities, but also to make user-agent collaboration seamless.

In the interactive viewer, scientists can browse every compound retrieved from the literature, click individual molecules to inspect their metadata, and plot relationships across the dataset. For example, plotting cellular potency versus rotatable bonds,colored by macrocycle status, clearly shows that the highest potency compounds are the most rigid.

After downloading and curating all the data, the agent is able to perform more advanced analysis to support the work of a computational chemist. As a next step, we will perform matched molecular pair analysis, a technique used in medicinal chemistry to isolate the effects of small, discrete changes to a molecule, by comparing pairs of molecules that only differ by that change. The agent had also independently suggested this analysis, as we expect the dataset to include many informative pairs. We will also ask the agent to build a predictive model using its molecular machine learning capabilities.

The matched molecular pair analysis (MMPA) compared many pairs of molecules that differ by whether or not they are cyclized. The results of the analysis show that cyclization reduces the number of rotatable bonds while generally increasing potency, as expected. The agent also built a large number of potency models using varying feature sets and model architectures, and validated them on a held-out set. The skills provide the agent with guidance on how to best build molecular machine learning models - for example, the agent will often use chronological splits, training on older compounds to predict newer ones, when this information is available, but can fall back to scaffold splits to better estimate generalizability.

The agent benchmarks multiple machine learning architectures with differing feature sets across four different experimental read outs, using a scaffold split to better gauge out-of-distribution performance. A combination of statistical and visual outputs allow the scientist to assess model performance and then iterate with the agent.

Finally, we ask the agent to design new, improved macrocycles based on its learnings and it recommends multiple reactions and synthesis routes involving different compounds. The agent can prepare these compounds for further analysis with AlphaFold or physics-based techniques like molecular dynamics simulation.

The skill equips the agent with the tools required to manipulate and validate reactions, generate curved arrow electron pushing diagrams, and look up similar reactions from public databases. The agent generated some interesting designs using its own knowledge combined with the previously developed MMPA and potency prediction models, explained its medicinal chemistry rationale, and suggested potential syntheses routes consistent with documented procedures. It also used the models it trained in the previous turn to predict each designâs potency.

The agent is able to reason about chemistry as it proposes new synthesis plans. Here the agent proposes a cyclization reaction, providing the scientist with electron-pushing diagrams to demonstrate the mechanism.

Once we are done with our analysis, the results can be exported in various formats, ready to be loaded into many industry standard chemistry software packages.

At the same time, it is also important to know what these tools cannot do. Sparse data, inter-lab assay noise, and narrow dynamic ranges limit the predictive precision of even the most powerful models; computational designs are testable hypotheses, not finished drugs. With the Cheminformatics Skills in Antigravity, a drug discovery scientist can generate more strongly-supported design hypotheses faster, but every proposed design must be synthesized and validated experimentally.

The speed at which researchers can make meaningful scientific decisions is accelerating. Not long ago, the workflow demonstrated here would have taken multiple days and required significant computational expertise. Using Antigravity as a science workbench allows both computational and experimental chemists to accelerate their workflows and focus on the questions that really matter.

## Acknowledgements

The cheminformatics skills are available on Google Antigravity today. Download the Antigravity App and install the Science plugin to start using these skills. Explore Science use cases
[here](https://antigravity.google/use-cases/science)
.

You can also get started with cheminformatics on Antigravity today as an Enterprise user, by choosing âUse Business Accountâ and logging into the app with your Google Cloud credentials.

To further advance the pace of research, weâre offering 10,000 scientists the highest usage tier in Google Antigravity free of charge for 6 months (onboarded on a rolling basis), subject to eligibility, capacity, and selection. Applications are
[now open](http://forms.gle/WvmBbPvRbpKG1BPn9)
.

We would like to acknowledge the contributions of the following team members: Filip Radlinski, Artem Sobolev, Victoria Johnston, Hannah Kiely-Collins
**,**
Zachary Wu, Jue Wang, Jack Dunger, Adriana Fernandez Lara, NgÃ¢n VÅ©, Doug Fritz, Yunhan Xu, Sebastian Nowozin, Pushmeet Kohli.

### Accelerating the search for antimicrobial peptides with Google Antigravity

### Conversing with antiquity