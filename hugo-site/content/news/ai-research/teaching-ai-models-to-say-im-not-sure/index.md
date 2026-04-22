---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-22T20:15:44.576508+00:00'
exported_at: '2026-04-22T20:15:46.822493+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/teaching-ai-models-to-say-im-not-sure-0422
structured_data:
  about: []
  author: ''
  description: MIT CSAIL&#039;s “Reinforcement Learning with Calibration Rewards”
    technique improves AI confidence estimates without sacrificing performance, addressing
    a root cause of hallucination in reasoning models.
  headline: Teaching AI models to say “I’m not sure”
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/teaching-ai-models-to-say-im-not-sure-0422
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Teaching AI models to say “I’m not sure”
updated_at: '2026-04-22T20:15:44.576508+00:00'
url_hash: e3d70b5606ee5291a68aed603bceb5d717eadf82
---

Confidence is persuasive. In artificial intelligence systems, it is often misleading.

Today's most capable reasoning models share a trait with the loudest voice in the room: They deliver every answer with the same unshakable certainty, whether they're right or guessing. Researchers at MIT's Computer Science and Artificial Intelligence Laboratory (CSAIL) have now traced that overconfidence to a specific flaw in how these models are trained, and developed a method that fixes it without giving up any accuracy.

The technique, called RLCR (Reinforcement Learning with Calibration Rewards), trains language models to produce calibrated confidence estimates alongside their answers. In addition to coming up with an answer, the model thinks about its uncertainty in that answer, and outputs a confidence score. In experiments across multiple benchmarks, RLCR reduced calibration error by up to 90 percent while maintaining or improving accuracy, both on the tasks the model was trained on and on entirely new ones it had never seen. The work will be presented at the International Conference on Learning Representations later this month.

The problem traces to a surprisingly simple source. The reinforcement learning (RL) methods behind recent breakthroughs in AI reasoning, including the training approach used in systems like OpenAI's o1, reward models for getting the right answer, and penalize them for getting it wrong. Nothing in between. A model that arrives at the correct answer through careful reasoning receives the same reward as one that guesses correctly by chance. Over time, this trains models to confidently answer every question they are asked, whether they have strong evidence or are effectively flipping a coin.

That overconfidence has consequences. When models are deployed in medicine, law, finance, or any setting where users make decisions based on AI outputs, a system that expresses high confidence regardless of its actual certainty becomes unreliable in ways that are difficult to detect from the outside. A model that says "I'm 95 percent sure" when it is right only half the time is more dangerous than one that simply gets the answer wrong, because users have no signal to seek a second opinion.

"The standard training approach is simple and powerful, but it gives the model no incentive to express uncertainty or say I don’t know," says Mehul Damani, an MIT PhD student and co-lead author on the
[paper.](https://arxiv.org/abs/2507.16806)
"So the model naturally learns to guess when it is unsure."

RLCR addresses this by adding a single term to the reward function: a Brier score, a well-established measure that penalizes the gap between a model's stated confidence and its actual accuracy. During training, models learn to reason about both the problem and their own uncertainty, producing an answer and a confidence estimate together. Confidently wrong answers are penalized. So are unnecessarily uncertain correct ones.

The math backs it up: the team proved formally that this type of reward structure guarantees models that are both accurate and well-calibrated. They then tested the approach on a 7-billion-parameter model across a range of question-answering and math benchmarks, including six datasets the model had never been trained on.

The results showed a consistent pattern. Standard RL training actively degraded calibration compared to the base model, making models worse at estimating their own uncertainty. RLCR reversed that effect, substantially improving calibration with no loss in accuracy. The method also outperformed post-hoc approaches, in which a separate classifier is trained to assign confidence scores after the fact. "What’s striking is that ordinary RL training doesn't just fail to help calibration. It actively hurts it," says Isha Puri, an MIT PhD student and co-lead author. "The models become more capable and more overconfident at the same time."

The team also demonstrated that the confidence estimates produced by RLCR are practically useful at inference time. When models generate multiple candidate answers, selecting the one with the highest self-reported confidence, or weighting votes by confidence in a majority-voting scheme, improves both accuracy and calibration as compute scales.

An additional finding suggests that the act of reasoning about uncertainty itself has value. The researchers trained classifiers on model outputs and found that including the model's explicit uncertainty reasoning in the input improved the classifier's performance, particularly for smaller models. The model's self-reflective reasoning about what it does and doesn’t know contains real information, not just decoration.

In addition to Damani and Puri, other authors on the paper are Stewart Slocum, Idan Shenfeld, Leshem Choshen, and senior authors Jacob Andreas and Yoon Kim.