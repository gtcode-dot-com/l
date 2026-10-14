---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-14T05:07:23.224857+00:00'
exported_at: '2026-10-14T05:07:27.728821+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/how-artificial-neural-networks-build-their-own-learning-machinery-1013
structured_data:
  about: []
  author: ''
  description: MIT neuroscientists have shown it possible for an artificial neural
    network to build its own learning machinery. With simple instructions about how
    and when connections should change, a group of randomly connected units can reshape
    itself into an effective information-processing network, learning from the data
    it is...
  headline: How artificial neural networks build their own learning machinery
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/how-artificial-neural-networks-build-their-own-learning-machinery-1013
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How artificial neural networks build their own learning machinery
updated_at: '2026-10-14T05:07:23.224857+00:00'
url_hash: 11e83311a7c54e72cd7e4877c0018ef9dd4374ef
---

As artificial intelligence becomes more and more powerful, its ability to handle human-like tasks is undeniable. Artificial neural networks can learn to recognize images, use language, or write computer code. Like the brain’s circuits, they reorganize themselves as they learn, adjusting the strengths of their connections to improve their performance.

The question for many neuroscientists is: What can these machine systems teach them about how the brain learns? And what kinds of models are likely to be the most informative?

In a
[paper published Oct. 9 in the journal
*PNAS*](https://www.pnas.org/doi/10.1073/pnas.2606245123)
, scientists at MIT’s
[McGovern Institute for Brain Research](https://mcgovern.mit.edu/)
and
[K. Lisa Yang Integrative Computational Neuroscience (ICoN) Center](https://yangtan.mit.edu/our-research/k-lisa-yang-icon-center/)
argue that a crucial metric for the biological plausibility of an artificial neural network’s approach to learning is the network’s ability to organize itself, without the guiding hand of a developer. They show that it is possible for an artificial neural network to build its own learning machinery. With some simple instructions about how and when connections should change, a group of randomly connected units can reshape itself into an effective information-processing network, learning from the data it is trained on.

**Biological learning**

“Current AI technology is working very well, but it doesn’t necessarily use a learning algorithm that is used by the brain,” says Qianli Liao, a K. Lisa Yang ICoN Center Postdoctoral Fellow in the labs of MIT professors and McGovern Institure members

[Tomaso Poggio](https://mcgovern.mit.edu/profile/tomaso-poggio/ "https://mcgovern.mit.edu/profile/tomaso-poggio/")

and

[Mark Harnett](https://mcgovern.mit.edu/profile/mark-harnett/ "https://mcgovern.mit.edu/profile/mark-harnett/")

, and co-first author of the

*PNAS*

paper with MIT Research Scientist Liu Ziyin and graduate student Yulu Gan. Liao explains that engineers design the rules about how connections change as an artificial neural network processes training data and receives feedback about its mistakes.

When it comes to training AI to do its job, the approach is powerful. But Liao and his colleagues caution that networks designed in this way may not offer much insight into biological learning. “The brain doesn't have an external designer or architect,” Liao says. “The brain has to organize itself. And we need to know how simple rules are going to make the brain organize.”

The rules that reshape neural connections as an animal learns may be different in different parts of the brain, or they may change as the brain becomes more mature. Neuroscientists are working to understand how those rules work and how they might be disrupted by aging or disease — a vital step toward developing new therapies and prevention strategies. Liao points to the development of brain-computer interfaces, which aim to restore communication when the brain’s language abilities are lost or let paralyzed patients control neuroprosthetic limbs, as one potential application.

“None of these can work without knowing the rules behind neuron-neuron interactions,” he says. “That’s not achievable by just designing a circuit that works very well.” An artificial neural network’s value to neuroscience should instead be judged by the extent to which it can organize itself — not just its connections, but also the machinery that adjusts those connections.

**Self-organized artificial learning**

Working with Poggio and Hartnett, Liao, Ziyin, and Gan set out to develop and validate a self-organizing computational network capable of learning. Liao explained that the network’s structure begins with multiple layers of randomly interconnected neuron-like units. Within each layer, every neuron-like component is subject to the same rules about how connections should be adjusted. “They just interact with each other using that rule, and they develop some type of behavior,” he says.

The team’s network implements the kind of simple rules thought to rewire brain circuits as humans and other animals learn from their experiences. In both the brain and the machine network, for example, “neurons that fire together wire together.” In other words, when two connected neurons are activated at the same time, the connection between them strengthens.

The team showed that a self-organizing network governed by rules like these can learn to recognize patterns and classify images. They explain that in their model, learning is enabled by self-assembling motifs that emerge according to simple rules, then serve as building blocks for functional circuits. As their network learned, these motifs reorganized themselves using an optimization strategy similar to the approach built into most modern machine learning systems, called gradient descent, in which connections are gradually adjusted in response to errors in order to improve performance.

Most modern AI implements gradient descent through some form of the back-propagation algorithm, which neuroscientists say is unlikely to be used by the brain. The team compared its self-organizing network to networks designed to learn in this way and found that it performed at a similar level.

**Connecting brains and machines**

Poggio says finding a biological parallel to back-propagation could trigger significant progress in both AI and neuroscience.

“If the synaptic motifs we propose are, in fact, used by the brain to do what backpropagation does for artificial neural networks, then we will have a strong connection at the level of fundamental mechanisms between artificial and natural networks — between machines and brains,” he says.

Liao says a self-organizing network does not necessarily learn the same way the brain does — but it’s a critical starting point for biological plausibility.

“Self-organization is the first high-level framework,” he says. “Once we are good with self-organization as a measure, then we can talk about next thing.”

While the group’s main objective is better understanding the brain, Liao says that knowledge could ultimately improve machine learning systems, too, enabling engineers to develop networks that perform better or in more human-like ways.