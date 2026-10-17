---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-17T22:03:54.016359+00:00'
exported_at: '2026-10-17T22:03:55.910948+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/ai-model-decodes-language-cells-use-communicate-1015
structured_data:
  about: []
  author: ''
  description: Researchers at the MIT Whitehead Institute developed a powerful computational
    approach to understand how cells communicate with each other to assemble into
    tissues and organs. Their framework has the potential to accelerate stem cell
    engineering, improve disease models, and even inform cancer treatments.
  headline: AI model decodes the language cells use to communicate
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/ai-model-decodes-language-cells-use-communicate-1015
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AI model decodes the language cells use to communicate
updated_at: '2026-10-17T22:03:54.016359+00:00'
url_hash: c0a2e19f9297635fd544e8982dc88365f071d192
---

A new computational approach reveals how cells communicate to assemble into tissues. This could accelerate stem cell engineering, improve disease models, and inform therapies.

As an embryo develops from a small cluster of stem cells, those once “blank slate” cells begin to take on more specialized roles like brain, liver, or muscle cells, and organize themselves into three-dimensional structures such as tissues and organs.

The fate of each cell — what type of specialized cell it will become — depends on which genes are turned on or off in the cell. These patterns of gene activity shape the cell’s structure and function, enabling it to take on a specific role in the body.

But this decision isn’t up to individual cells. They constantly send and receive chemical signals to and from neighboring cells, which help them understand where they are, what stage of development they are in, and what they should become. These messages spread through multi-step sequences called signaling pathways, which translate external signals into specific changes in gene activity in the cell.

For researchers, being able to retrace the sequence of instructions a cell has received would offer a powerful way to understand how tissues develop and how these processes go awry in disease.

But this has been difficult to achieve because scientists have long assumed that the effects of signaling pathways vary widely across cell types, meaning they would need to map each pathway separately in each cell type — an arduous and painstaking process.

Now, in a new study led by MIT assistant professor of biology and Whitehead Institute for Biomedical Research member Pulin Li and graduate student Nicholas Hutchins, researchers have discovered that each signaling pathway leaves behind a unique “fingerprint” — a distinctive pattern of gene activity that reflects the particular signals the cell has encountered.

Importantly, these fingerprints are consistent across different cell types for the same signaling pathway, which means that instead of mapping each cell type separately, scientists can reconstruct signaling histories across many cell types using these pathway-specific fingerprints.

This discovery was made possible through a machine learning model called IRIS. This model can detect fingerprints of different signaling pathways and pinpoint which signals a cell received at different stages of development inside an embryo, even for cell types it hasn’t encountered before.

This artificial intelligence-driven approach marks a major advance over traditional methods, which require researchers to experimentally test every pathway in every possible cell type, and opens up the possibility to comprehensively map the signaling histories of every cell inside a mouse or human embryo at an unprecedented scale.

“Think of voice recognition systems like Siri, which are trained mainly in English, but then use that training to help them recognize other languages,” says Li. “This is called transfer learning, and this is why IRIS can work across many different cell types.”

The researchers’ detailed open-access findings,
[published in the journal
*Nature Methods*](https://www.nature.com/articles/s41592-026-03213-8)
on Sept. 8, could accelerate stem cell engineering for regenerative medicine and improve the creation of organoids — miniature, 3D models that mimic real organs — for studying disease mechanisms and testing new drugs. This is because once researchers learn the pattern of signals that drives a stem cell to become a specific cell type, they can recreate those signals to control the fate of stem cells in a lab or medical setting.

IRIS is a neural network-based model, which, in essence, is an AI-driven system designed to recognize patterns in complex data, similar to how our brains spot patterns. It examines a cell’s overall gene activity and estimates which signaling pathways were likely “on” at specific times during development.

Li and Hutchins trained IRIS on a large experimental dataset that measured how thousands of human embryonic stem cells responded to dozens of combinations of six major signaling pathways at multiple stages of development. This created a comprehensive map, or atlas, of how signaling combinations influence cell behavior.

The team then tested IRIS using single cells from mouse embryos during gastrulation, a stage when cells are rapidly branching into different fates. IRIS could accurately predict when and where specific signaling pathways would activate in cells destined to become part of heart, gut, muscle, and spinal cord tissue. This variation in signaling molecules is what guides cells to form the right structures in the right places.

With this approach, scientists can not only begin to understand the fundamentals of cell-to-cell communication, but also gain a practical roadmap for guiding stem cells into specific, functional cell types in the lab.

When the researchers employed IRIS to identify signals needed to create a cell type critical for lung development, the model predicted that activating a specific signaling pathway would encourage lung-specific development. Experiments in mouse embryos confirmed the model’s prediction. By identifying the precise combinations of signals that drive lung cell development, they can more reliably generate accurate, lab-grown models of lung tissue.

“In these ways, IRIS is helping us decode the language cells use to talk to each other at a much faster rate than we could realistically achieve through experiments,” Hutchins says.

These improved models would allow researchers to study diseases like asthma, lung cancer, and pulmonary fibrosis, in which lung tissue becomes scarred, often without a known cause. They can then use these models to test potential therapies, and ultimately design regenerative treatments that can repair the damaged tissue.