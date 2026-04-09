---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-09T14:15:37.890908+00:00'
exported_at: '2026-04-09T14:15:40.619666+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/new-technique-makes-ai-models-leaner-faster-while-still-learning-0409
structured_data:
  about: []
  author: ''
  description: CompreSSM, an algorithm from MIT CSAIL, trims dead weight from AI models,
    shedding unnecessary complexity while also making them faster as they continue
    to learn. It helps the model find its own efficient structure while cutting compute
    costs.
  headline: New technique makes AI models leaner and faster while they’re still learning
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/new-technique-makes-ai-models-leaner-faster-while-still-learning-0409
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New technique makes AI models leaner and faster while they’re still learning
updated_at: '2026-04-09T14:15:37.890908+00:00'
url_hash: 30a4fd5b0bd225f79803c3ad672aea6d32368099
---

Training a large artificial intelligence model is expensive, not just in dollars, but in time, energy, and computational resources. Traditionally, obtaining a smaller, faster model either requires training a massive one first and then trimming it down, or training a small one from scratch and accepting weaker performance.

Researchers at MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL), Max Planck Institute for Intelligent Systems, European Laboratory for Learning and Intelligent Systems, ETH, and Liquid AI have now developed a new method that sidesteps this trade-off entirely, compressing models during training, rather than after.

The technique, called
[CompreSSM](https://arxiv.org/abs/2510.02823)
, targets a family of AI architectures known as state-space models, which power applications ranging from language processing to audio generation and robotics. By borrowing mathematical tools from control theory, the researchers can identify which parts of a model are pulling their weight and which are dead weight, before surgically removing the unnecessary components early in the training process.

"It's essentially a technique to make models grow smaller and faster as they are training," says Makram Chahine, a PhD student in electrical engineering and computer science, CSAIL affiliate, and lead author of the paper. "During learning, they're also getting rid of parts that are not useful to their development."

The key insight is that the relative importance of different components within these models stabilizes surprisingly early during training. Using a mathematical quantity called Hankel singular values, which measure how much each internal state contributes to the model's overall behavior, the team showed they can reliably rank which dimensions matter and which don't after only about 10 percent of the training process. Once those rankings are established, the less-important components can be safely discarded, and the remaining 90 percent of training proceeds at the speed of a much smaller model.

"What's exciting about this work is that it turns compression from an afterthought into part of the learning process itself,” says senior author Daniela Rus, MIT professor and director of CSAIL. “Instead of training a large model and then figuring out how to make it smaller, CompreSSM lets the model discover its own efficient structure as it learns. That's a fundamentally different way to think about building AI systems.”

The results are striking. On image classification benchmarks, compressed models maintained nearly the same accuracy as their full-sized counterparts while training up to 1.5 times faster. A compressed model reduced to roughly a quarter of its original state dimension achieved 85.7 percent accuracy on the CIFAR-10 benchmark, compared to just 81.8 percent for a model trained at that smaller size from scratch. On Mamba, one of the most widely used state-space architectures, the method achieved approximately 4x training speedups, compressing a 128-dimensional model down to around 12 dimensions while maintaining competitive performance.

"You get the performance of the larger model, because you capture most of the complex dynamics during the warm-up phase, then only keep the most-useful states," Chahine says. "The model is still able to perform at a higher level than training a small model from the start."

What makes CompreSSM distinct from existing approaches is its theoretical grounding. Conventional pruning methods train a full model and then strip away parameters after the fact, meaning you still pay the full computational cost of training the big model. Knowledge distillation, another popular technique, requires training a large "teacher" model to completion and then training a second, smaller "student" model on top of it, essentially doubling the training effort. CompreSSM avoids both of these costs by making informed compression decisions mid-stream.

The team benchmarked CompreSSM head-to-head against both alternatives. Compared to Hankel nuclear norm regularization, a recently proposed spectral technique for encouraging compact state-space models, CompreSSM was more than 40 times faster, while also achieving higher accuracy. The regularization approach slowed training by roughly 16 times because it required expensive eigenvalue computations at every single gradient step, and even then, the resulting models underperformed. Against knowledge distillation on CIFAR-10, CompressSM held a clear advantage for heavily compressed models: At smaller state dimensions, distilled models saw significant accuracy drops, while CompreSSM-compressed models maintained near-full performance. And because distillation requires a forward pass through both the teacher and student at every training step, even its smaller student models trained slower than the full-sized baseline.

The researchers proved mathematically that the importance of individual model states changes smoothly during training, thanks to an application of Weyl's theorem, and showed empirically that the relative rankings of those states remain stable. Together, these findings give practitioners confidence that dimensions identified as negligible early on won't suddenly become critical later.

The method also comes with a pragmatic safety net. If a compression step causes an unexpected performance drop, practitioners can revert to a previously saved checkpoint. "It gives people control over how much they're willing to pay in terms of performance, rather than having to define a less-intuitive energy threshold," Chahine explains.

There are some practical boundaries to the technique. CompreSSM works best on models that exhibit a strong correlation between the internal state dimension and overall performance, a property that varies across tasks and architectures. The method is particularly effective on multi-input, multi-output (MIMO) models, where the relationship between state size and expressivity is strongest. For per-channel, single-input, single-output architectures, the gains are more modest, since those models are less sensitive to state dimension changes in the first place.

The theory applies most cleanly to linear time-invariant systems, although the team has developed extensions for the increasingly popular input-dependent, time-varying architectures. And because the family of state-space models extends to architectures like linear attention, a growing area of interest as an alternative to traditional transformers, the potential scope of application is broad.

Chahine and his collaborators see the work as a stepping stone. The team has already demonstrated an extension to linear time-varying systems like Mamba, and future directions include pushing CompreSSM further into matrix-valued dynamical systems used in linear attention mechanisms, which would bring the technique closer to the transformer architectures that underpin most of today's largest AI systems.

"This had to be the first step, because this is where the theory is neat and the approach can stay principled," Chahine says. "It's the stepping stone to then extend to other architectures that people are using in industry today."

"The work of Chahine and his colleagues provides an intriguing, theoretically grounded perspective on compression for modern state-space models (SSMs)," says Antonio Orvieto, ELLIS Institute Tübingen principal investigator and MPI for Intelligent Systems independent group leader, who wasn't involved in the research. "The method provides evidence that the state dimension of these models can be effectively reduced during training and that a control-theoretic perspective can successfully guide this procedure. The work opens new avenues for future research, and the proposed algorithm has the potential to become a standard approach when pre-training large SSM-based models."

The work, which was accepted as a
[conference paper](https://arxiv.org/abs/2510.02823)
at the International Conference on Learning Representations 2026, will be presented later this month. It was supported, in part, by the Max Planck ETH Center for Learning Systems, the Hector Foundation, Boeing, and the U.S. Office of Naval Research.