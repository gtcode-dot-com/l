---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-23T04:07:42.672313+00:00'
exported_at: '2026-06-23T04:07:44.695491+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/better-way-to-model-metal-alloys-behavior-0619
structured_data:
  about: []
  author: ''
  description: MIT researchers created a technique that captures chemical arrangements
    across materials to improve predictions of how metal alloys and other complex
    materials will behave.
  headline: A better way to model the behavior of metal alloys
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/better-way-to-model-metal-alloys-behavior-0619
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A better way to model the behavior of metal alloys
updated_at: '2026-06-23T04:07:42.672313+00:00'
url_hash: e0e8a60107c1d5a51019b03594471a3eb04b6355
---

Companies working at the frontier of aerospace, energy, and computing are constantly looking for new materials to improve performance. But in order to understand how those materials will actually behave once they’re inside rockets or on computer chips, companies first have to make the material and then test it. That’s because even the most powerful simulation techniques struggle to model the complex chemical arrangements in most of today’s solid materials. The problem adds costs and time to materials innovation.

Now a team of MIT researchers has created a way to accurately model the behavior of metals, regardless of the complexity of their chemical arrangement. At the center of the approach are machine-learning models that make simulations of materials faster and more accurate. The researchers improved those models by building training datasets that capture the diversity of atomic environments in chemically disordered materials.

In a
[new paper in
*Sciences Advances*](http://doi.org/10.1126/sciadv.aea9951)
, the researchers showed their approach could be used to accurately predict material properties for a diverse group of metal alloys under a range of conditions. They also showed how the approach could be used to develop new materials, especially in scenarios where experimentation is expensive.

“The focus of the paper is metallic alloys, which is the field I work in, but this could be adapted to other types of materials, like semiconductors,” says senior author Rodrigo Freitas, MIT’s TDK Career Development Professor in Materials Science and Engineering. “This is not specific to any one application — you could use this approach to create new sustainable steels, new materials for aerospace, and more. That’s what makes this exciting.”

Joining Freitas on the paper are first author Killian Sheriff PhD ’26; MIT PhD students Daniel Xiao and Yifan Cao; and University of Sheffield Senior Lecturer Lewis R. Owen.

**Modeling metals**

Material properties are mostly determined by the internal arrangement of their chemical elements. Even if two materials have the same mix of chemical elements, different chemical arrangements can make the difference between a brittle material and one that deforms without breaking.

Capturing that distinction requires simulating materials atom by atom. To do that, researchers rely on models that describe how atoms interact with each other. Over the last two decades, machine learning has become the most accurate way to build those models. Such models work well when the chemical arrangements inside materials follow highly ordered patterns, but that’s not the case with most solid materials, whose atomic chemical arrangements are disordered and vary from one region to another.

“The real challenge in our field is modelling these chemically disordered phases,” Freitas says. “Chemical disorder means there’s a huge variety of local chemical environments, which is hard for the machine-learning model to learn. This is a problem because every single metal we use in practice is chemically disordered.”

The problem comes down to a lack of representative training data for those atom-by-atom simulations. The current leading approach for creating such data works by brute force, often requiring more than 100,000 hours of computation to create the training data for a single material. Even then, it does not transfer well when researchers change the material’s composition.

In
[previous work](https://news.mit.edu/2024/machine-learning-unlocks-secrets-advanced-alloys-0718)
, Freitas’ group had developed a way to measure the chemical complexity of solid materials by analyzing the frequency and spacing of tiny groups of atoms. For this study, the researchers used that capability to build better training datasets. They used a mathematical approach known as information theory to generate training datasets that capture a wider variety of local chemical environments inside disordered materials. The method works by swapping out atoms from samples to reduce repetition and expose the model to chemical environments it might otherwise miss.

“We kept optimizing the training set so it captured as many different local environments as possible,” Freitas says. “If the same kind of environment showed up many times, we replaced redundant examples with ones the model hadn’t seen before. That makes the training set much more informative because each example adds something new.”

When trained on the researchers’ datasets, the models predicted material properties more accurately than models trained using random sampling or another popular sampling method.

“The starting point for all these atom-by-atom simulations is: Are you able to accurately describe the chemical bond between atoms?” Freitas explains. “If not, it can still teach you about materials in general, but it doesn’t tell you what will happen to specific materials in the real world. This approach makes the simulations high fidelity in terms of their chemistry, to better reflect what’s happening to materials.”

The researchers applied their technique to create machine-learning training datasets for a group of chemically diverse metal alloys. Using a set of machine-learning models, they showed the models trained on their datasets are more accurate than much larger models created by companies like Google and Microsoft.

“We got to a point where we were convinced it worked without using these expensive brute-force methods,” Freitas says. “I told Killian, ‘This is a good paper. But if you can show that simulations with these models can now accurately predict useful materials properties, then it becomes a very good paper.’ Killian took that to heart and tested this as widely as he could.”


Sheriff worked with Xiao and Cao to test the approach across different alloys and properties. The team also drew on Owen’s experimental data to compare the simulations against real measurements of atomic ordering in alloys.

**From the lab to industry**

The method works, in part, by capturing hidden patterns in the sample data. The researchers describe the patterns in the paper as “subtle energetic biases toward certain local chemical configurations.”

Those small energetic differences matter because they determine which phases form in an alloy, how those phases change with temperature and composition, and ultimately which properties the material will have. As one test, Daniel Xiao led simulations showing that the team’s models could predict phase diagrams that closely matched experimental data. Phase diagrams map which phases are stable across different temperatures and chemical compositions, and they are a central tool for designing and processing alloys.

“Phase diagrams are one of the main ways people connect materials modeling to real processing decisions,” Freitas says. “If you are welding, casting, or heat-treating an alloy, you need to know which phases are likely to form under different conditions. Our goal is to make these kinds of predictions accurate enough, and accessible enough, that they become part of how people design materials.”

The researchers are now using the approach to study how changing an alloy’s composition affects mechanical properties and radiation tolerance, with the goal of designing materials that remain strong and damage-tolerant in harsh environments. They are also working to make the method easier to use with the kinds of tools and workflows materials engineers already rely on.

“Industry isn’t going to change the way they do things if what you’re creating doesn’t fit into their existing operating procedures,” Freitas says. “The goal is to make these predictions useful in the places where materials decisions are actually made.”


The research was supported by the U.S. Air Force Office of Scientific Research.