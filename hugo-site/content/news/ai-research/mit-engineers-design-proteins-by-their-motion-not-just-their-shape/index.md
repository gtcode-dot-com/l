---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:21:54.169708+00:00'
exported_at: '2026-04-02T04:21:56.399874+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/mit-engineers-design-proteins-by-motion-not-just-shape-0326
structured_data:
  about: []
  author: ''
  description: VibeGen is a new generative AI model that designs proteins with dynamic
    vibration and movement. The model, developed at MIT, opens new possibilities for
    dynamic biomaterials and adaptive therapeutics.
  headline: MIT engineers design proteins by their motion, not just their shape
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/mit-engineers-design-proteins-by-motion-not-just-shape-0326
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MIT engineers design proteins by their motion, not just their shape
updated_at: '2026-04-02T04:21:54.169708+00:00'
url_hash: acdecc05da60c79c372633052181f2c546d4357f
---

Proteins are far more than nutrients we track on a food label. Present in every cell of our bodies, they work like nature’s molecular machines. They walk, stretch, bend, and flex to do their jobs, pumping blood, fighting disease, building tissue, and many other jobs too small for the eye to see. Their power doesn’t come from shape alone, but from how they move.

In recent years, artificial intelligence has allowed scientists to design entirely new protein structures not found in nature tailored for specific functions, such as binding to viruses, or mimicking the mechanical properties of silk for sustainable materials. But designing for structure alone is like building a car body without any control over how the engine performs. The subtle vibrations, shifts, and mechanical dynamics of a protein are just as critical to its functions as its form.

Now, MIT engineers have taken a major step toward closing the gap with the development of an AI model known as VibeGen. If vibe coding lets programmers describe what they want and then AI generates the software, VibeGen does the same for living molecules: specify the vibe — the pattern of motion you want — and the model writes the protein.

The new model allows scientists to target how a protein flexes, vibrates, and shifts between shapes in response to its environment, opening a new frontier in the design of molecular mechanics. VibeGen builds on a series of advances from the
[Buehler lab](https://lamm.mit.edu/)
in agentic AI for science — systems in which multiple AI models collaborate autonomously to solve problems too complex for any single model.

“The essence of life at fundamental molecular levels lies not just in structure, but in movement,” says Markus Buehler, the Jerry McAfee Professor of Engineering in the departments of Civil and Environmental Engineering and Mechanical Engineering. “Everything from protein folding to the deformation of materials under stress follows the fundamental laws of physics.”

Buehler and his former postdoc, Bo Ni, identified a critical need for what they call physics-aware AI: systems capable of reasoning about motion, not just snapshots of molecular structure. “AI must go beyond analyzing static forms to understanding how structure and motion are fundamentally intertwined,” Buehler adds.

The new approach,
[described in a paper March 24 in the journal
*Matter*](https://www.cell.com/matter/abstract/S2590-2385(26)00069-X)
*,*
uses generative AI to create proteins with tailor-made dynamics.

**Training AI to think about motion**


The revolution in AI-driven protein science has been, overwhelmingly, a revolution in structure. Tools like AlphaFold solved the decades-old problem of predicting a protein’s three-dimensional shape. Existing generative models learned to design new shapes from scratch. But in focusing on the folded snapshot — the protein frozen in place — the field largely set aside the property that makes proteins work: their motion. “Structure prediction was such a grand challenge that it absorbed the field’s attention,” Buehler says. “But a protein’s shape is just one frame of a much longer film, and the design space extends through space and time, where structure sits on a much broader manifold.” Scientists could design a protein with a particular architecture. They couldn’t yet specify how that protein would move, flex, or vibrate once it was built.

VibeGen does something no protein design tool has done before. It inverts the traditional problem. Rather than asking, “What shape will this sequence produce?” it asks, “What sequence will make a protein move in exactly this way?”

To build VibeGen, Buehler and Ni turned to a class of AI diffusion models, the same underlying technology that powers AI image generators capable of creating realistic pictures from pure noise. In VibeGen’s case, the model starts with a random sequence of amino acids and refines it, step by step, until it converges on a sequence predicted to vibrate and flex in a targeted way.

The system works through two cooperating agents that design and challenge each other. A “designer” proposes candidate sequences aimed at a target motion profile. A “predictor” evaluates those candidates, asking whether they’ll actually move the way the designer intended. The two models iterate back and forth like an internal dialogue, until the design stabilizes into something that meets the goal. By specifying this vibrational fingerprint as the design input, VibeGen inverts the usual logic: dynamics becomes the blueprint, and structure follows.

“It’s a collaborative system,” Ni

says. “The designer proposes, the predictor critiques, and the design improves through that tension.”

Most sequences VibeGen produces are entirely de novo, not borrowed from nature, not a variation on something evolution already made. To confirm the designs actually work, the team ran detailed physics-based molecular simulations, and the proteins behaved exactly as intended, flexing and vibrating in the patterns VibeGen had targeted.

One of the study’s most striking findings is that many different protein sequences and folds can satisfy the same vibrational target — a property the researchers call functional degeneracy. Where evolution converged on one solution, VibeGen reveals an entire family of alternatives: proteins with different structures and sequences that nonetheless move in the same way. “It suggests that nature explored only a fraction of what’s possible,” Buehler says. “For any given dynamic behavior, there may be a large, untapped space of viable designs."

**A new frontier in molecular engineering**

Controlling protein dynamics could have wide-ranging applications. In medicine, proteins that can change shape on cue hold enormous potential. Many therapeutic proteins work by binding to a target molecule — a virus, a cancer cell, a misfiring receptor. How well they bind often depends not just on their shape, but on how flexibly they can adapt to their target. A protein that is engineered with motion could grip more precisely, reduce unintended interactions, and ultimately become a safer, more effective drug.

In materials science, which is an area of Buehler’s research, mechanical properties at the molecular scale affect their performance. Biological materials like silk and collagen get their strength and resilience from the coordinated motion of their molecular building blocks. Designing proteins that are stiffer, flexible, or vibrate in a certain way could lead to new sustainable fibers, impact-resistant materials, or biodegradable alternatives to petroleum-based plastics.

Buehler envisions further possibilities: structural materials for buildings or vehicles incorporating protein-based components that heal themselves after mechanical stress, or that adjust in response to heavy load.

By enabling researchers to specify motion as a direct design parameter, VibeGen treats proteins less like static shapes and more like programmable mechanical devices. The advance bridges artificial intelligence, medicine, synthetic biology, and materials engineering — toward a future in which molecular machines can be designed with the same precision and intentionality as bridges, engines, or microchips.

*“*
VibeGen can venture into uncharted territory, proposing protein designs beyond the repertoire of evolution, tailored purely to our specifications. It’s as if we’ve invented a new creative engine that designs molecular machines on demand,” Buehler adds.

The researchers plan to refine the model further and validate their designs in the lab. They also hope to integrate motion-aware design with other AI tools, building toward systems that can design proteins to be not just dynamic, but multifunctional; machines that sense their environment, respond to signals, and adapt in real-time.

The word “vibe” comes from vibration, and Buehler sees the connection as more than wordplay. “We've turned 'vibe' into a metaphor, a feeling, something subjective,” he says. “But for a protein, the vibe is the physics. It is the actual pattern of motion that determines what the molecule can do, the very machinery of life.”

The research was supported by
the U.S. Department of Agriculture, the MIT-IBM Watson AI Lab, and MIT’s Generative AI Initiative.