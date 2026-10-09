---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-02T10:15:29.271127+00:00'
exported_at: '2026-02-02T10:15:31.675091+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/how-generative-ai-can-help-scientists-synthesize-complex-materials-0202
structured_data:
  about: []
  author: ''
  description: DiffSyn, a computer model developed by MIT researchers, suggests promising
    ways to synthesize new materials for faster experimentation.
  headline: How generative AI can help scientists synthesize complex materials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/how-generative-ai-can-help-scientists-synthesize-complex-materials-0202
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: How generative AI can help scientists synthesize complex materials
updated_at: '2026-02-02T10:15:29.271127+00:00'
url_hash: ffb104c1fb1b63893890db991257b4bade529608
---

Generative artificial intelligence models have been used to create enormous libraries of theoretical materials that could help solve all kinds of problems. Now, scientists just have to figure out how to make them.

In many cases, materials synthesis is not as simple as following a recipe in the kitchen. Factors like the temperature and length of processing can yield huge changes in a material’s properties that make or break its performance. That has limited researchers’ ability to test millions of promising model-generated materials.

Now, MIT researchers have created an AI model that guides scientists through the process of making materials by suggesting promising synthesis routes. In a new paper, they showed the model delivers state-of-the-art accuracy in predicting effective synthesis pathways for a class of materials called zeolites, which could be used to improve catalysis, absorption, and ion exchange processes. Following its suggestions, the team synthesized a new zeolite material that showed improved thermal stability.

The researchers believe their new model could break the biggest bottleneck in the materials discovery process.

“To use an analogy, we know what kind of cake we want to make, but right now we don’t know how to bake the cake,” says lead author Elton Pan, a PhD candidate in MIT’s Department of Materials Science and Engineering (DMSE). “Materials synthesis is currently done through domain expertise and trial and error.”

The paper describing the work appears today in
*Nature Computational Science*
. Joining Pan on the paper are Soonhyoung Kwon ’20, PhD ’24; DMSE postdoc Sulin Liu; chemical engineering PhD student Mingrou Xie; DMSE postdoc Alexander J. Hoffman; Research Assistant Yifei Duan SM ’25; DMSE visiting student Thorben Prein; DMSE PhD candidate Killian Sheriff; MIT Robert T. Haslam Professor in Chemical Engineering Yuriy Roman-Leshkov; Valencia Polytechnic University Professor Manuel Moliner; MIT Paul M. Cook Career Development Professor Rafael Gómez-Bombarelli; and MIT Jerry McAfee Professor in Engineering Elsa Olivetti.

**Learning to bake**

Massive investments in generative AI have led companies like Google and Meta to create huge databases filled with material recipes that, at least theoretically, have properties like high thermal stability and selective absorption of gases. But making those materials can require weeks or months of careful experiments that test specific reaction temperatures, times, precursor ratios, and other factors.

“People rely on their chemical intuition to guide the process,” Pan says. “Humans are linear. If there are five parameters, we might keep four of them constant and vary one of them linearly. But machines are much better at reasoning in a high-dimensional space.”

The synthesis process of materials discovery now often takes the most time in a material’s journey from hypothesis to use.

To help scientists navigate that process, the MIT researchers trained a generative AI model on over 23,000 material synthesis recipes described over 50 years of scientific papers. The researchers iteratively added random “noise” to the recipes during training, and the model learned to de-noise and sample from the random noise to find promising synthesis routes.

The result is DiffSyn, which uses an approach in AI known as diffusion.

“Diffusion models are basically a generative AI model like ChatGPT, but more like the DALL-E image generation model,” Pan says. “During inference, it converts noise into meaningful structure by subtracting a little bit of noise at each step. In this case, the ‘structure’ is the synthesis route for a desired material.”

When a scientist using DiffSyn enters a desired material structure, the model offers some promising combinations of reaction temperatures, reaction times, precursor ratios, and more.

“It basically tells you how to bake your cake,” Pan says. “You have a cake in mind, you feed it into the model, the model spits out the synthesis recipes. The scientist can pick whichever synthesis path they want, and there are simple ways to quantify the most promising synthesis path from what we provide, which we show in our paper.”

To test their system, the researchers used DiffSyn to suggest novel synthesis paths for a zeolite, a material class that is complex and takes time to form into a testable material.

“Zeolites have a very high-dimensional synthesis space,” Pan says. “Zeolites also tend to take days or weeks to crystallize, so the impact [of finding the best synthesis pathway faster] is much higher than other materials that crystallize in hours.”

The researchers were able to make the new zeolite material using synthesis pathways suggested by DiffSyn. Subsequent testing revealed the material had a promising morphology for catalytic applications.

“Scientists have been trying out different synthesis recipes one by one,” Pan says. “That makes them very time-consuming. This model can sample 1,000 of them in under a minute. It gives you a very good initial guess on synthesis recipes for completely new materials.”

**Accounting for complexity**

Previously, researchers have built machine-learning models that mapped a material to a single recipe. Those approaches do not take into account that there are different ways to make the same material.

DiffSyn is trained to map material structures to many different possible synthesis paths. Pan says that is better aligned with experimental reality.

“This is a paradigm shift away from one-to-one mapping between structure and synthesis to one-to-many mapping,” Pan says. “That’s a big reason why we achieved strong gains on the benchmarks.”

Moving forward, the researchers believe the approach should work to train other models that guide the synthesis of materials outside of zeolites, including metal-organic frameworks, inorganic solids, and other materials that have more than one possible synthesis pathway.

“This approach could be extended to other materials,” Pan says. “Now, the bottleneck is finding high-quality data for different material classes. But zeolites are complicated, so I can imagine they are close to the upper-bound of difficulty. Eventually, the goal would be interfacing these intelligent systems with autonomous real-world experiments, and agentic reasoning on experimental feedback to dramatically accelerate the process of materials design.”

The work was supported by MIT International Science and Technology Initiatives (MISTI), the National Science Foundation, Generalitat Vaslenciana, the Office of Naval Research, ExxonMobil, and the Agency for Science, Technology and Research in Singapore.