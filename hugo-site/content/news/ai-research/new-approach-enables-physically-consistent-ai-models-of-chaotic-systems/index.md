---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-21T00:02:15.976159+00:00'
exported_at: '2026-11-21T00:02:16.888490+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/new-approach-enables-physically-consistent-ai-models-chaotic-systems-1120
structured_data:
  about: []
  author: ''
  description: MIT researchers developed a physics-constrained machine learning approach
    that guarantees bounded predictions for chaotic systems, enabling reliable AI
    models for weather forecasting, climate modeling, and the study of turbulent flows.
  headline: New approach enables physically consistent AI models of chaotic systems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/new-approach-enables-physically-consistent-ai-models-chaotic-systems-1120
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New approach enables physically consistent AI models of chaotic systems
updated_at: '2026-11-21T00:02:15.976159+00:00'
url_hash: 480a8b723958aa8ddaf27c32a22857fe53a1893c
---

Enforcing physics-based constraints prevents AI models from generating unreliable predictions for complex nonlinear systems in weather, climate, and turbulent flows.

Modeling of complex, chaotic processes such as weather and climate patterns and turbulent flows in aviation or in ocean currents has advanced enormously in recent years. However, such models are still prone to drift into physically impossible predictions over time.

Now, researchers with MIT’s Laboratory for Information and Decision Systems (LIDS) have found a way to introduce physics-based restrictions on machine learning models that can ensure that such models never exceed realistic bounds, based on what is actually possible in the real world. This new approach, using information that is now being made freely available by the team, could significantly improve the usefulness and reliability of such models, which besides climate and weather are also used in a wide range of industrial processes, aeronautics, and hydrology.

The new findings are
[published](https://www.pnas.org/doi/10.1073/pnas.2533077123)
in the
*Proceedings of the National Academy of Sciences (PNAS)*
in a paper by MIT graduate student Sunbochen Tang and MIT professors Navid Azizan and Themistoklis Sapsis.

“Lack of guarantees for a bounded response has always been a major obstacle on formulating data-driven models for complex nonlinear systems,” says Sapsis, a professor of mechanical engineering and LIDS affiliate. The approach the team has developed, he says, “paves the way for applying the most advanced machine-learning architectures for prediction and control in a plethora of real-world problems, even those characterized by intrinsic instabilities.”

Developing reliable models for complex dynamical systems is important across many domains. In fluid dynamics, turbulent flows can disrupt air travel, reduce the efficiency of wind turbines, and affect fuel economy of vehicles. Similarly, in weather forecasting, the chaotic nature of atmospheric dynamics makes accurate long-term predictions difficult.

“Tiny differences in the starting conditions can lead to dramatically different outcomes in a chaotic system,” Azizan says. “That makes predicting its behavior far into the future extremely difficult.” And yet, there are always physical constraints on the kinds of changes that are possible in the real world.

“Chaos does not mean anything can happen. These systems often remain bounded, and their models should, too.” But how to introduce those boundaries into the models has been a thorny problem, says Azizan, the Hayes Associate Professor in the Department of Mechanical Engineering and the Institute for Data, Systems, and Society, and a principal investigator in LIDS.

“A model can match the data over a short period and still fail when you let it run for a long time,” he says. “Small errors can accumulate until the simulation produces values that grow without limit,” producing predictions that could never actually occur in real systems.

“It’s a fundamental problem with many of the existing machine learning models,” he says. “It’s a question that comes up frequently in different domains: how can we embed physical constraints into these models in a way that preserves their flexibility, but ensures physically meaningful outputs?”

“We want to preserve the chaos without the artificial runaway behavior that the real system does not have,” he says. “Our approach gives the model room to learn complex dynamics while guaranteeing that its trajectories stay bounded.” This is the first work that establishes such formal guarantees for machine learning models of chaos.

Previous attempts to prevent unrealistic results from such models have often been based on “imposing penalties or incentives during training,” says Tang, a doctoral student in the Department of Aeronautics and Astronautics and LIDS, using functions that are often designed based on privileged information about the system. But as these only apply during the training process for the model, “there’s no guarantee that the model will satisfy the underlying constraints intended by such incentives at test time” once it is dealing with new inputs when it is actually used. “The model could still produce unbounded predictions,” he says.

To illustrate why simply imposing arbitrary limits would not be a satisfactory solution to the prediction stability issue, Tang explains, “you can cap the predictions, for example, by setting an arbitrary limit on physical quantities, such as 100 degrees for temperature. That’s one possible way to keep predictions bounded, but it could restrict the model from representing complex and nontrivial features that should be learned directly from the data.”

He says that “what sets our approach apart is that we formulate energy-based constraints. We let the model learn an energy-like function,” based on real-world chaotic systems, where energy dissipation helps keep trajectories bounded despite their complex behaviors. “Specifically, the model learns an energy-like function, along with a boundary where its chaotic behavior should be confined to. We then add a projection layer, a component that adjusts how the model predicts the system will evolve, to enforce energy dissipation as a hard constraint. Outside this boundary, the energy-like quantity must decrease, so the simulated system is drawn toward the bounded region. That way, we can establish theoretical guarantees that the model prediction remains bounded over arbitrarily long forecast windows.”

The team tested their approach on a variety of different well-known physical systems, ranging from simple textbook cases to highly complex multidimensional systems, and found that their approach closely matched the true outcomes, while conventional approaches soon deviated into impossible predictions.

Azizan adds that “the fundamental difference between our approach and the existing approaches is what we call hard constraining versus soft constraining.” While many of the current approaches “try to incentivize the model to satisfy the constraints, they’re not treated as hard constraints. Our approach is based on the concept of hard-constrained neural networks,” so that what comes out “is always physically consistent, even if it’s a completely new case the model hasn’t seen.”

“AI models shine in scenarios where there’s a large amount of data available,” Azizan says, for example with images or with text, both of which are abundantly available on the internet. However, he says, “for a lot of physical systems, data is not as abundant.” For such cases where the data is limited, he says, “these physics-constrained approaches can help a lot, because the physics of the problem is another source of information.”

The new approach is broadly useful for any chaotic systems. “This is readily applicable to a wide range of neural network architectures,” Tang says. They plan to continue testing it on ever-larger systems. “We’re trying to see how well this would work on data-driven models of realistic weather systems.”

“The projection layer is modular: it is model-agnostic and can work with different neural network architectures,” Azizan says. “We hope other researchers and practitioners will build on it and test it on larger and even more complex problems.” The paper, along with open-source code, is
[now accessible online at PNAS](https://www.pnas.org/doi/10.1073/pnas.2533077123)
.

A
[follow-up work](https://proceedings.mlr.press/v331/goertzen26a.html)
this year by members of the team was presented at the Learning for Dynamics and Control conference. The paper won the conference’s Best Paper Award.

“Trustworthy and reliable AI needs more than just evidence that a model usually works,” Azizan says. “For high-stakes applications, you need guarantees about the properties that must always hold. In this work, we established one such guarantee: boundedness. Our broader goal is to make principles part of how AI models are built, not just how they are tested.”