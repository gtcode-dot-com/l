---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-22T20:29:23.898164+00:00'
exported_at: '2026-10-22T20:29:26.537770+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/giving-ai-crystal-clear-view-of-materials-world-1018
structured_data:
  about: []
  author: ''
  description: MIT researchers created an AI model that can identify optimal crystalline
    materials for various applications. The model combines 3D atomic structures with
    natural language descriptions to characterize crystal structures from research
    papers and computational databases.
  headline: Giving AI a “crystal clear” view of the materials world
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/giving-ai-crystal-clear-view-of-materials-world-1018
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Giving AI a “crystal clear” view of the materials world
updated_at: '2026-10-22T20:29:23.898164+00:00'
url_hash: 631c78f18e2760a26f4b329959c0ec9f428b8c5e
---

New research can help AI models understand crystalline materials in 3D and reason about their properties.

In principle, artificial intelligence could make finding the right material for an application as simple as ordering dinner: Scientists would tell a large language model what they want, and it would serve them the perfect material for the job.

Unfortunately, that approach doesn’t work well yet, and the problem comes down to data: Most materials consist of 3D arrangements of crystals, not the text streams that today’s large language models are trained on. The experimental literature is also heavily biased toward a few popular classes of crystals, making AI outputs skew toward those materials.

Now MIT researchers have created a multimodal AI model that tackles these problems. The model combines 3D atomic structures with natural language descriptions to create rich linguistic descriptions about the structures from experimental research papers and first-principles computational databases. The unified description outlines not just the chemical composition and structure, but also its properties, processing considerations, and potential applications, helping AI learn more about what makes materials impactful.

In a
[new paper in
*Nature Communications*](https://www.nature.com/articles/s41467-026-76378-7)
, the researchers showed their system could identify better material designs than models trained on text streams alone by allowing the model to “see” the atomic arrangements and bonding patterns. For example, when the researchers asked the model to identify materials suited for solid-state lithium-ion battery electrolytes, its top results included materials that had been independently identified as promising candidates. The researchers also showed their model learned geometric representations of material structures in ways text-only models could not.

“Structure is really at the heart of the materials science field,” says Ju Li, the Carl Richard Soderberg Professor in Power Engineering in the departments of Materials Science and Engineering and Nuclear Science and Engineering. “If you understand the structure, you can infer quite a lot about the properties and performance of materials. We wanted to build the connection between a material’s atomic structure and its properties and processing for the model.”

Joining Li on a paper about the model are Yang Jeong Park, first author and former MIT postdoc; Mayank Kumaran, a recent University of Illinois Urbana-Champaign computer engineering graduate; Chia-Wei Hsu SM ’26; and Elsa Olivetti, the Jerry McAfee (1940) Professor in Engineering in DMSE.

**Getting models to see in 3D**

Materials scientists are always on the hunt for new crystals that will lead to the products of the future. Over the last decade, AI has reshaped that process, proposing and designing new crystalline structures, which have highly ordered atomic structures and make up more than 90 percent of solid materials on Earth.
Most of those models treat solid crystalline materials as 3D graphs.

The rise of large language models has given researchers another tool for innovation. But existing large language models rely heavily on text from published papers and books, limiting their knowledge of the physical world, since many potential crystal structures are stored in computational databases. Text-based models also lack understanding of visual geometry.

To overcome those challenges, the researchers decided to create a vision-language model for crystalline materials.

They trained a language model to create textual descriptions of crystal structures using an approach known as contrastive learning, in which models compare similar and dissimilar examples of structures and textual descriptions to achieve a unified understanding. This is similar to aligning the visual and language regions of the brain.

Following training, the researchers compared the predictions of two versions of the model: one trained on a dataset containing the AI-generated descriptions and the other trained on a dataset containing text from papers only. They found that the model trained on AI-generated descriptions successfully learned how to align geometric structures with text descriptions while the other did not.

“We wanted to create an AI model that works broadly across materials,” Li says. “That’s why we decided to synthesize narratives rather than rely solely on existing papers. We found when we used that narrative dataset, the models are better at predicting the function.”

**Accelerating materials science**

The researchers then showed their model could be given a natural language query describing a property and identify crystalline materials with that property, outperforming a baseline.

“There are sometimes these step changes within materials science around algorithmic integration toward useful tools, which the community uses to further advance the field,” Olivetti says. “This approach helps us see more deeply into three-dimensional structures and link structures to property and processing. I hope this can be one of those step changes.”

Li compares the model to AlphaFold, an AI model that links protein structures with function that has helped advance biological research and drug development.

The researchers believe their new approach can work with many crystalline materials, and they hope other material scientists will use it to accelerate their work.

“Being able to see a three-dimensional crystal and how its atoms are connected is super foundational,” Li says. “I think this will be useful to anyone who practices materials science.”

The work was supported, in part, by the U.S. Defense Threat Reduction Agency through the University Research Alliance; the U.S. Defense Advanced Research Projects Agency; and the National Research Foundation of Korea.