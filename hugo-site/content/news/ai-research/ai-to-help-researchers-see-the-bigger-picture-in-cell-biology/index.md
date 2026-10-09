---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T19:23:07.899214+00:00'
exported_at: '2026-03-03T19:23:10.980654+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/ai-help-researchers-see-bigger-picture-cell-biology-0225
structured_data:
  about: []
  author: ''
  description: A new AI framework identifies which data about a cell are captured
    by one measurement modality and which are shared across multiple modalities. This
    gives researchers a more complete picture of the cell state and could help them
    understand disease mechanisms and plan treatments.
  headline: AI to help researchers see the bigger picture in cell biology
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/ai-help-researchers-see-bigger-picture-cell-biology-0225
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AI to help researchers see the bigger picture in cell biology
updated_at: '2026-03-03T19:23:07.899214+00:00'
url_hash: 49605122f307d325c81920c230aa6525145d8549
---

Studying gene expression in a cancer patient’s cells can help clinical biologists understand the cancer’s origin and predict the success of different treatments. But cells are complex and contain many layers, so how the biologist conducts measurements affects which data they can obtain. For instance, measuring proteins in a cell could yield different information about the effects of cancer than measuring gene expression or cell morphology.

Where in the cell the information comes from matters. But to capture complete information about the state of the cell, scientists often must conduct many measurements using different techniques and analyze them one at a time. Machine-learning methods can speed up the process, but existing methods lump all the information from each measurement modality together, making it difficult to figure out which data came from which part of the cell.

To overcome this problem, researchers at the Broad Institute of MIT and Harvard and ETH Zurich/Paul Scherrer Institute (PSI) developed an artificial intelligence-driven framework that learns which information about a cell’s state is shared across different measurement modalities and which information is unique to a particular measurement type.

By pinpointing which information came from which cell parts, the approach provides a more holistic view of the cell’s state, making it easier for a biologist to see the complete picture of cellular interactions. This could help scientists understand disease mechanisms and track the progression of cancer, neurodegenerative disorders such as Alzheimer’s, and metabolic diseases like diabetes.

“When we study cells, one measurement is often not sufficient, so scientists develop new technologies to measure different aspects of cells. While we have many ways of looking at a cell, at the end of the day we only have one underlying cell state. By putting the information from all these measurement modalities together in a smarter way, we could have a fuller picture of the state of the cell,” says lead author Xinyi Zhang SM ’22, PhD ’25, a former graduate student in the MIT Department of Electrical Engineering and Computer Science (EECS) and an affiliate of the Eric and Wendy Schmidt Center at the Broad Institute of MIT and Harvard, who is now a group leader at AITHYRA in Vienna, Austria.

Zhang is joined on a paper about the work by G.V. Shivashankar, a professor in the Department of Health Sciences and Technology at ETH Zurich and head of the Laboratory of Multiscale Bioimaging at PSI; and senior author Caroline Uhler, a professor in EECS and the Institute for Data, Systems, and Society (IDSS) at MIT, member of MIT’s Laboratory for Information and Decision Systems (LIDS), and director of the Eric and Wendy Schmidt Center at the Broad Institute. The research
[appears today in
*Nature Computational Science*](https://www.nature.com/articles/s43588-025-00948-w)
.

**Manipulating multiple measurements**

There are many tools scientists can use to capture information about a cell’s state. For instance, they can measure RNA to see if the cell is growing, or they can measure chromatin morphology to see if the cell is dealing with external physical or chemical signals.

“When scientists perform multimodal analysis, they gather information using multiple measurement modalities and integrate it to better understand the underlying state of the cell. Some information is captured by one modality only, while other information is shared across modalities. To fully understand what is happening inside the cell, it is important to know where the information came from,” says Shivashankar.

Often, for scientists, the only way to sort this out is to conduct multiple individual experiments and compare the results. This slow and cumbersome process limits the amount of information they can gather.

In the new work, the researchers built a machine-learning framework that specifically understands which information overlaps between different modalities, and which information is unique to a particular modality but not captured by others.

“As a user, you can simply input your cell data and it automatically tells you which data are shared and which data are modality-specific,” Zhang says.

To build this framework, the researchers rethought the typical way machine-learning models are designed to capture and interpret multimodal cellular measurements.

Usually these methods, known as autoencoders, have one model for each measurement modality, and each model encodes a separate representation for the data captured by that modality. The representation is a compressed version of the input data that discards any irrelevant details.

The MIT method has a shared representation space where data that overlap between multiple modalities are encoded, as well as separate spaces where unique data from each modality are encoded.

In essence, one can think of it like a Venn diagram of cellular data.

The researchers also used a special, two-step training procedure that helps their model handle the complexity involved in deciding which data are shared across multiple data modalities. After training, the model can identify which data are shared and which are unique when fed cell data it has never seen before.

**Distinguishing data**

In tests on synthetic datasets, the framework correctly captured known shared and modality-specific information. When they applied their method to real-world single-cell datasets, it comprehensively and automatically distinguished between gene activity captured jointly by two measurement modalities, such as transcriptomics and chromatin accessibility, while also correctly identifying which information came from only one of those modalities.

In addition, the researchers used their method to identify which measurement modality captured a certain protein marker that indicates DNA damage in cancer patients. Knowing where this information came from would help a clinical scientist determine which technique they should use to measure that marker.

“There are too many modalities in a cell and we can’t possibly measure them all, so we need a prediction tool. But then the question is: Which modalities should we measure and which modalities should we predict? Our method can answer that question,” Uhler says.

In the future, the researchers want to enable the model to provide more interpretable information about the state of the cell. They also want to conduct additional experiments to ensure it correctly disentangles cellular information and apply the model to a wider range of clinical questions.

“It is not sufficient to just integrate the information from all these modalities,” Uhler says. “We can learn a lot about the state of a cell if we carefully compare the different modalities to understand how different components of cells regulate each other.”

This research is funded, in part, by the Eric and Wendy Schmidt Center at the Broad Institute, the Swiss National Science Foundation, the U.S. National Institutes of Health, the U.S. Office of Naval Research, AstraZeneca, the MIT-IBM Watson AI Lab, the MIT J-Clinic for Machine Learning and Health, and a Simons Investigator Award.