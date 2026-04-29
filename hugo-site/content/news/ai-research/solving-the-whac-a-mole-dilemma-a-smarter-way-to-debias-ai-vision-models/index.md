---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-29T22:15:35.868901+00:00'
exported_at: '2026-04-29T22:15:38.057074+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/smarter-way-to-debias-ai-vision-models-0429
structured_data:
  about: []
  author: ''
  description: A new debiasing approach called WRING resolves the &quot;Whac-a-Mole
    dilemma&quot; of existing debiasing approaches that can create or amplify existing
    biases.
  headline: 'Solving the “Whac-a-mole dilemma”: A smarter way to debias AI vision
    models'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/smarter-way-to-debias-ai-vision-models-0429
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Solving the “Whac-a-mole dilemma”: A smarter way to debias AI vision models'
updated_at: '2026-04-29T22:15:35.868901+00:00'
url_hash: 23debd91bcd707a329e3ecdabd258c2a347d9f27
---

In today’s hospitals and clinics, a dermatologist may use an artificial intelligence model for classifying skin lesions to assess if the lesion is at risk of developing into a cancer or if it is benign. But if the model is biased toward certain skin tones, it could fail to identify a high-risk patient.

Perhaps one of the best known and most persistent challenges that AI research continues to reckon with is bias. Bias is often discussed in relation to training data, but model architecture can also contain and amplify bias, negatively influencing model performance in real-world settings. In high-stakes medical scenarios, the very real consequences of poor performance have made bias into a quintessential safety issue.

[A new paper](https://openreview.net/pdf?id=tkE29O0jzF)
from researchers at MIT, Worcester Polytechnic Institute, and Google that was accepted to the 2026 International Conference for Learning Representations proposes a novel debiasing approach called “Weighted Rotational DebiasING” (i.e., WRING) that can be applied to vision language models (VLMs), like OpenAI’s OpenCLIP.

VLMs are multi-modal models that can understand and interpret different data modalities like video, image, and text simultaneously. While debiasing approaches for VLMs do exist, the most commonly used approach is known as “projection debiasing,” which leads to what has been termed the
[“Whac-A-Mole dilemma”](https://arxiv.org/abs/2212.04825)
, an empirical observation that was formally introduced to AI research in 2023.

Projection debiasing is a post-processing approach that removes the undesirable, biased information from model embeddings by “projecting” the subspace out of a representation space of relationships, thereby cutting out the bias. But this approach has its drawbacks.

“When you do that, you inadvertently squish everything around,” says Walter Gerych, the paper’s first author, who conducted this research last year as a postdoc at MIT. “All the other relationships that the model learns change when you do that.”

Gerych, who is now an assistant professor of computer science at Worcester Polytechnic Institute, is joined on the paper by MIT graduate students Cassandra Parent and Quinn Perian; Google’s Rafiya Javed; and MIT associate professors of electrical engineering Justin Solomon and
[Marzyeh Ghassemi](https://jclinic.mit.edu/team-member/marzyeh-ghassemi/)
, who is an affiliate of the
[Abdul Latif Jameel Clinic for Machine Learning and Health](https://jclinic.mit.edu/)
and the Laboratory for Information and Decision Systems.

While projection debiasing stops the model from acting upon the bias that’s been projected out of the subspace, it can end up amplifying and creating other biases, hence the Whac-A-Mole dilemma. According to Ghassemi, the unintended amplification of model biases is “both a technical and practical challenge. For instance, when debiasing a VLM that retrieves images of clinical staff — if racial bias is removed — it could have the unintended consequence of amplifying gender bias.”

WRING works by moving certain coordinates within the high-dimensional space of a model — the ones that appear to be responsible for bias — to a different angle, so the model can no longer distinguish between different groups within a certain concept. This changes the representation within a specific space while leaving the model’s other relationships intact. And like projection debiasing, WRING is a post-processing approach, which means it can be applied “on the fly” to a pre-trained VLM.

“People already spent a lot of resources, a lot of money, training these huge models, and we don’t really want to go in and modify something during training because then you have to start from scratch,” Gerych explains. “[WRING is] very efficient. It doesn’t require more training of the model and it’s minimally invasive.”

In their results, the researchers found that WRING significantly reduced bias for a target concept without increasing bias in other areas. But for now, the approach is somewhat limited to Contrastive Language-Image Pre-training (CLIP) models, a type of VLM that connects images to language for search or classification.

“Extending this for ChatGPT-style, generative language models, is the reasonable next step for us,” says Gerych.

This work was supported, in part, by a National Science Foundation CAREER Award, AI2050 Award Early Career Fellowship, Sloan Research Fellow Award, the Gordon and Betty Moore Foundation Award, and MIT-Google Computing Innovation Award.