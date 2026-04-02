---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T08:15:42.413897+00:00'
exported_at: '2026-04-02T08:15:44.802495+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/mit-researchers-use-ai-uncover-atomic-defects-materials-0330
structured_data:
  about: []
  author: ''
  description: MIT researchers developed an AI model that can measure the types and
    concentrations of atomic defects used to improve materials’ strength, conductivity,
    and energy-conversion efficiency.
  headline: MIT researchers use AI to uncover atomic defects in materials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/mit-researchers-use-ai-uncover-atomic-defects-materials-0330
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MIT researchers use AI to uncover atomic defects in materials
updated_at: '2026-04-02T08:15:42.413897+00:00'
url_hash: 004527d33154e2be8ebaa6ee0557df301094b2e1
---

In biology, defects are generally bad. But in materials science, defects can be intentionally tuned to give materials useful new properties. Today, atomic-scale defects are carefully introduced during the manufacturing process of products like steel, semiconductors, and solar cells to help improve strength, control electrical conductivity, optimize performance, and more.

But even as defects have become a powerful tool, accurately measuring different types of defects and their concentrations in finished products has been challenging, especially without cutting open or damaging the final material. Without knowing what defects are in their materials, engineers risk making products that perform poorly or have unintended properties.

Now, MIT researchers have built an AI model capable of classifying and quantifying certain defects using data from a noninvasive neutron-scattering technique. The model, which was trained on 2,000 different semiconductor materials, can detect up to six kinds of point defects in a material simultaneously, something that would be impossible using conventional techniques alone.

“Existing techniques can’t accurately characterize defects in a universal and quantitative way without destroying the material,” says lead author Mouyang Cheng, a PhD candidate in the Department of Materials Science and Engineering. “For conventional techniques without machine learning, detecting six different defects is unthinkable. It’s something you can’t do any other way.”

The researchers say the model is a step toward harnessing defects more precisely in products like semiconductors, microelectronics, solar cells, and battery materials.

“Right now, detecting defects is like the saying about seeing an elephant: Each technique can only see part of it,” says senior author and associate professor of nuclear science and engineering Mingda Li. “Some see the nose, others the trunk or ears. But it is extremely hard to see the full elephant. We need better ways of getting the full picture of defects, because we have to understand them to make materials more useful.”

Joining Cheng and Li on the paper are postdoc Chu-Liang Fu, undergraduate researcher Bowen Yu, master’s student Eunbi Rha, PhD student Abhijatmedhi Chotrattanapituk ’21, and Oak Ridge National Laboratory staff members Douglas L Abernathy PhD ’93 and Yongqiang Cheng. The
[paper](https://www.cell.com/matter/abstract/S2590-2385(26)00091-3)
appears today in the journal
*Matter*
.

**Detecting defects**

Manufacturers have gotten good at tuning defects in their materials, but measuring precise quantities of defects in finished products is still largely a guessing game.

“Engineers have many ways to introduce defects, like through doping, but they still struggle with basic questions like what kind of defect they’ve created and in what concentration,” Fu says. “Sometimes they also have unwanted defects, like oxidation. They don’t always know if they introduced some unwanted defects or impurity during synthesis. It’s a longstanding challenge.”

The result is that there are often multiple defects in each material. Unfortunately, each method for understanding defects has its limits. Techniques like X-ray diffraction and positron annihilation characterize only some types of defects. Raman spectroscopy can discern the type of defect but can’t directly infer the concentration. Another technique known as transmission electron microscope requires people to cut thin slices of samples for scanning.

In a few previous papers, Li and collaborators applied machine learning to experimental spectroscopy data to characterize crystalline materials. For the new paper, they wanted to apply that technique to defects.

For their experiment, the researchers built a computational database of 2,000 semiconductor materials. They made sample pairs of each material, with one doped for defects and one left without defects, then used a neutron-scattering technique that measures the different vibrational frequencies of atoms in solid materials. They trained a machine-learning model on the results.

“That built a foundational model that covers 56 elements in the periodic table,” Cheng says. “The model leverages the multihead attention mechanism, just like what ChatGPT is using. It similarly extracts the difference in the data between materials with and without defects and outputs a prediction of what dopants were used and in what concentrations.”

The researchers fine-tuned their model, verified it on experimental data, and showed it could measure defect concentrations in an alloy commonly used in electronics and in a separate superconductor material.

The researchers also doped the materials multiple times to introduce multiple point defects and test the limits of the model, ultimately finding it can make predictions about up to six defects in materials simultaneously, with defect concentrations as low as 0.2 percent.

“We were really surprised it worked that well,” Cheng says. “It’s very challenging to decode the mixed signals from two different types of defects — let alone six.”

**A model approach**

Typically, manufacturers of things like semiconductors run invasive tests on a small percentage of products as they come off the manufacturing line, a slow process that limits their ability to detect every defect.

“Right now, people largely estimate the quantities of defects in their materials,” Yu says. “It is a painstaking experience to check the estimates by using each individual technique, which only offers local information in a single grain anyway. It creates misunderstandings about what defects people think they have in their material.”

The results were exciting for the researchers, but they note their technique measuring the vibrational frequencies with neutrons would be difficult for companies to quickly deploy in their own quality-control processes.

“This method is very powerful, but its availability is limited,” Rha says. “Vibrational spectra is a simple idea, but in certain setups it’s very complicated. There are some simpler experimental setups based on other approaches, like Raman spectroscopy, that could be more quickly adopted.”

Li says companies have already expressed interest in the approach and asked when it will work with Raman spectroscopy, a widely used technique that measures the scattering of light. Li says the researchers’ next step is training a similar model based on Raman spectroscopy data. They also plan to expand their approach to detect features that are larger than point defects, like grains and dislocations.

For now, though, the researchers believe their study demonstrates the inherent advantage of AI techniques for interpreting defect data.

“To the human eye, these defect signals would look essentially the same,” Li says. “But the pattern recognition of AI is good enough to discern different signals and get to the ground truth. Defects are this double-edged sword. There are many good defects, but if there are too many, performance can degrade. This opens up a new paradigm in defect science.”

The work was supported, in part, by the Department of Energy and the National Science Foundation.