---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-07T05:59:27.127102+00:00'
exported_at: '2026-10-07T05:59:28.364598+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/instructmesh-tool-lets-users-repair-ai-3d-models-then-fabricate-them-1001
structured_data:
  about: []
  author: ''
  description: The InstructMesh generative AI tool helps users 3D print working, real-world
    items with ease by understanding how designs should look and which edits users
    truly want. You can prompt the system to produce a 3D model, then ask it to edit
    specific parts.
  headline: New tool lets users repair AI-generated 3D models, then fabricate them
    just the way they want
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/instructmesh-tool-lets-users-repair-ai-3d-models-then-fabricate-them-1001
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New tool lets users repair AI-generated 3D models, then fabricate them just
  the way they want
updated_at: '2026-10-07T05:59:27.127102+00:00'
url_hash: 487a3c06f8822544a2c0142d4c04d6270fee8486
---

What makes InstructMesh so adept at following such unique prompts? It pairs Microsoft’s
[TRELLIS](https://microsoft.github.io/TRELLIS.2/)
system, which creates 3D models from text and image prompts, with the large language model (LLM)
[GPT-4,](https://openai.com/index/gpt-4-research/)
which supports ChatGPT — in other words, visual and textual knowledge combined.

“We wanted to bring together the talents of 3D generators and the reasoning skills of LLMs in an interactive space to make objects that people actually want,” says Faraz Faruqi SM ’22, PhD ’26, lead author on a
[paper](https://arxiv.org/abs/2608.28534)
presenting the project, graduate of the Department of Electrical Engineering and Computer Science, and recent CSAIL affiliate. “Language models are great at text and images, while TRELLIS’s talent lies in its ability to create 3D models, since it’s seen so many.”

InstructMesh’s strengths come in handy in other, more surprising areas. MIT scientists used the program to fabricate a knee brace that looks like denim to match a patient’s jeans. InstructMesh can even help create robots — that is, clever enclosures that house wireless components. The researchers made a “bristle bot” that resembles a colorful shrimp to demonstrate this. It has a motor hidden inside, and when switched on, it can slide across surfaces, sort of like a wind-up toy.

Faruqi and his colleagues found that InstructMesh could easily make their desired items. But what would someone who’s never 3D modeled anything think of their program? And could they really detect design flaws before fabrication?

The team has TRELLIS recreate popular 3D models found on
[Thingiverse](https://www.thingiverse.com/)
, a platform home to millions of 3D printable models, to help them find out. Nearly 80 percent of the models it generated were structurally flawed in some way. CSAIL researchers then asked novices to identify and fix these issues in InstructMesh — and they were able to do both around 90 percent of the time, as reviewed by an expert. What these newcomers lacked in expertise, they made up for in intuition.

InstructMesh scaffolds the actual modeling process, which previously required domain expertise in 3D modeling tools. “With manipulation happening in the latent space of the generative model, InstructMesh supports natural language description of issues, and creates interpretive changes in the geometry for the user to evaluate and approve,” says Faruqi.

Users then created items resembling things like phone stands and vases, noting that InstructMesh was easy to use. They also found that InstructMesh enabled them to express a wide range of ideas, while the sliders gave them more precision to make certain tweaks, such as enlarging or extruding a particular part of the model.

“The users got what they prompted for and easily tweaked designs where needed,” adds Faruqi. “What they saw is what they got, and the items worked as advertised, so to speak.”

While users enjoyed using the InstructMesh, Faruqi has an even grander vision for the project. He now works at Google, where he may soon incorporate InstructMesh into an augmented reality (AR) platform. The idea: Prompt the system by explaining what you need using the context of your surroundings, then it’ll rapidly 3D print it (e.g., making a phone case that matches your wallet).

InstructMesh may also begin to incorporate physics simulations to model how your design may react to specific uses, such as whether a bowl breaks when dropped, and which materials would work best. The software might also integrate the more recent TRELLIS.2 to refine even smaller features in 3D models.

Stefanie Mueller, an associate professor of electrical engineering and computer science (EECS) and mechanical engineering at MIT, and a member of CSAIL, is a senior author on the paper. Faruqi and Mueller wrote the paper with Google researchers Ahmed Katary ’23; Fabian Manhardt; Vrushank Phadnis MEng ’13, PhD ’20; Ruofei Du; and Federico Tombari. Other co-authors were Northeastern University Assistant Professor Megan Hofmann along with several CSAIL colleagues: Demircan Tas SM ’24 and SMArchS ’24, a PhD student in EECS and architecture; former visiting researcher Theresa Hradilak; Ning Zhang ’25, a graduate student in EECS; postdoc Jiaji Li; and Martin Nisser SM ’19, PhD ’24.

The researchers’ work was supported, in part, by Google and the MIT-HPI Collaborative Research Program. They will present it at the ACM Symposium on User Interface Software and Technology in November.