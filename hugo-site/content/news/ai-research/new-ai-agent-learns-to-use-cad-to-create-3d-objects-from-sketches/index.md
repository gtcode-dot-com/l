---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-19T12:00:17.210583+00:00'
exported_at: '2025-11-19T12:00:19.452834+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/new-ai-agent-learns-use-cad-create-3d-objects-sketches-1119
structured_data:
  about: []
  author: ''
  description: VideoCAD, a new AI model that uses CAD software much like a human would,
    lowers the barrier to entry for design, helping people without years of CAD training
    to create 3D models more easily. 
  headline: New AI agent learns to use CAD to create 3D objects from sketches
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/new-ai-agent-learns-use-cad-create-3d-objects-sketches-1119
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New AI agent learns to use CAD to create 3D objects from sketches
updated_at: '2025-11-19T12:00:17.210583+00:00'
url_hash: 5ff03bea54664bee5b2d9a673f8a58eaf693478a
---

Computer-Aided Design (CAD) is the go-to method for designing most of today’s physical products. Engineers use CAD to turn 2D sketches into 3D models that they can then test and refine before sending a final version to a production line. But the software is notoriously complicated to learn, with thousands of commands to choose from. To be truly proficient in the software takes a huge amount of time and practice.

MIT engineers are looking to ease CAD’s learning curve with an AI model that uses CAD software much like a human would. Given a 2D sketch of an object, the model quickly creates a 3D version by clicking buttons and file options, similar to how an engineer would use the software.

The MIT team has created a new dataset called VideoCAD, which contains more than 41,000 examples of how 3D models are built in CAD software. By learning from these videos, which illustrate how different shapes and objects are constructed step-by-step, the new AI system can now operate CAD software much like a human user.

With VideoCAD, the team is building toward an AI-enabled “CAD co-pilot.” They envision that such a tool could not only create 3D versions of a design, but also work with a human user to suggest next steps, or automatically carry out build sequences that would otherwise be tedious and time-consuming to manually click through.

“There’s an opportunity for AI to increase engineers’ productivity as well as make CAD more accessible to more people,” says Ghadi Nehme, a graduate student in MIT’s Department of Mechanical Engineering.

“This is significant because it lowers the barrier to entry for design, helping people without years of CAD training to create 3D models more easily and tap into their creativity,” adds Faez Ahmed, associate professor of mechanical engineering at MIT.

Ahmed and Nehme, along with graduate student Brandon Man and postdoc Ferdous Alam, will present their work at the Conference on Neural Information Processing Systems (NeurIPS) in December.

**Click by click**

The team’s new work expands on recent developments in AI-driven user interface (UI) agents — tools that are trained to use software programs to carry out tasks, such as automatically gathering information online and organizing it in an Excel spreadsheet. Ahmed’s group wondered whether such UI agents could be designed to use CAD, which encompasses many more features and functions, and involves far more complicated tasks than the average UI agent can handle.

In their new work, the team aimed to design an AI-driven UI agent that takes the reins of the CAD program to create a 3D version of a 2D sketch, click by click. To do so, the team first looked to an existing dataset of objects that were designed in CAD by humans. Each object in the dataset includes the sequence of high-level design commands, such as “sketch line,” “circle,” and “extrude,” that were used to build the final object.

However, the team realized that these high-level commands alone were not enough to train an AI agent to actually use CAD software. A real agent must also understand the details behind each action. For instance: Which sketch region should it select? When should it zoom in? And what part of a sketch should it extrude? To bridge this gap, the researchers developed a system to translate high-level commands into user-interface interactions.

“For example, let’s say we drew a sketch by drawing a line from point 1 to point 2,” Nehme says. “We translated those high-level actions to user-interface actions, meaning we say, go from this pixel location, click, and then move to a second pixel location, and click, while having the ‘line’ operation selected.”

In the end, the team generated over 41,000 videos of human-designed CAD objects, each of which is described in real-time in terms of the specific clicks, mouse-drags, and other keyboard actions that the human originally carried out. They then fed all this data into a model they developed to learn connections between UI actions and CAD object generation.

Once trained on this dataset, which they dub VideoCAD, the new AI model could take a 2D sketch as input and directly control the CAD software, clicking, dragging, and selecting tools to construct the full 3D shape. The objects ranged in complexity from simple brackets to more complicated house designs. The team is training the model on more complex shapes and envisions that both the model and the dataset could one day enable CAD co-pilots for designers in a wide range of fields.

“VideoCAD is a valuable first step toward AI assistants that help onboard new users and automate the repetitive modeling work that follows familiar patterns,” says Mehdi Ataei, who was not involved in the study, and is a senior research scientist at Autodesk Research, which develops new design software tools. “This is an early foundation, and I would be excited to see successors that span multiple CAD systems, richer operations like assemblies and constraints, and more realistic, messy human workflows.”