---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-10T00:15:35.531706+00:00'
exported_at: '2026-03-10T00:15:38.557859+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/improving-ai-models-ability-explain-predictions-0309
structured_data:
  about: []
  author: ''
  description: A new technique transforms any computer vision model into one that
    can explain its predictions using a set of concepts a human could understand.
    The method generates more appropriate concepts that boost the accuracy of the
    model.
  headline: Improving AI models’ ability to explain their predictions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/improving-ai-models-ability-explain-predictions-0309
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Improving AI models’ ability to explain their predictions
updated_at: '2026-03-10T00:15:35.531706+00:00'
url_hash: f1d4406c19da4154c3c46dfe8019a65a17fb7474
---

In high-stakes settings like medical diagnostics, users often want to know what led a computer vision model to make a certain prediction, so they can determine whether to trust its output.

Concept bottleneck modeling is one method that enables artificial intelligence systems to explain their decision-making process. These methods force a deep-learning model to use a set of concepts, which can be understood by humans, to make a prediction. In new research, MIT computer scientists developed a method that coaxes the model to achieve better accuracy and clearer, more concise explanations.

The concepts the model uses are usually defined in advance by human experts. For instance, a clinician could suggest the use of concepts like “clustered brown dots” and “variegated pigmentation” to predict that a medical image shows melanoma.

But previously defined concepts could be irrelevant or lack sufficient detail for a specific task, reducing the model’s accuracy. The new method extracts concepts the model has already learned while it was trained to perform that particular task, and forces the model to use those, producing better explanations than standard concept bottleneck models.

The approach utilizes a pair of specialized machine-learning models that automatically extract knowledge from a target model and translate it into plain-language concepts. In the end, their technique can convert any pretrained computer vision model into one that can use concepts to explain its reasoning.

“In a sense, we want to be able to read the minds of these computer vision models. A concept bottleneck model is one way for users to tell what the model is thinking and why it made a certain prediction. Because our method uses better concepts, it can lead to higher accuracy and ultimately improve the accountability of black-box AI models,” says lead author Antonio De Santis, a graduate student at Polytechnic University of Milan who completed this research while a visiting graduate student in the Computer Science and Artificial Intelligence Laboratory (CSAIL) at MIT.

He is joined on a
[paper about the work](https://openreview.net/pdf?id=gdEWoxhb70)
by Schrasing Tong SM ’20, PhD ’26; Marco Brambilla, professor of computer science and engineering at Polytechnic University of Milan; and senior author Lalana Kagal, a principal research scientist in CSAIL. The research will be presented at the International Conference on Learning Representations.

**Building a better bottleneck**

Concept bottleneck models (CBMs) are a popular approach for improving AI explainability. These techniques add an intermediate step by forcing a computer vision model to predict the concepts present in an image, then use those concepts to make a final prediction.

This intermediate step, or “bottleneck,” helps users understand the model’s reasoning.

For example, a model that identifies bird species could select concepts like “yellow legs” and “blue wings” before predicting a barn swallow.

But because these concepts are often generated in advance by humans or large language models (LLMs), they might not fit the specific task. In addition, even if given a set of pre-defined concepts, the model sometimes utilizes undesirable learned information anyway, which is a problem known as information leakage.

“These models are trained to maximize performance, so the model might secretly use concepts we are unaware of,” De Santis explains.

The MIT researchers had a different idea: Since the model has been trained on a vast amount of data, it may have learned the concepts needed to generate accurate predictions for the particular task at hand. They sought to build a CBM by extracting this existing knowledge and converting it into text a human can understand.

In the first step of their method, a specialized deep-learning model called a sparse autoencoder selectively takes the most relevant features the model learned and reconstructs them into a handful of concepts. Then, a multimodal LLM describes each concept in plain language.

This multimodal LLM also annotates images in the dataset by identifying which concepts are present and absent in each image. The researchers use this annotated dataset to train a concept bottleneck module to recognize the concepts.

They incorporate this module into the target model, forcing it to make predictions using only the set of learned concepts the researchers extracted.

**Controlling the concepts**

They overcame many challenges as they developed this method, from ensuring the LLM annotated concepts correctly to determining whether the sparse autoencoder had identified human-understandable concepts.

To prevent the model from using unknown or unwanted concepts, they restrict it to use only five concepts for each prediction. This also forces the model to choose the most relevant concepts and makes the explanations more understandable.

When they compared their approach to state-of-the-art CBMs on tasks like predicting bird species and identifying skin lesions in medical images, their method achieved the highest accuracy while providing more precise explanations.

Their approach also generated concepts that were more applicable to the images in the dataset.

“We’ve shown that extracting concepts from the original model can outperform other CBMs, but there is still a tradeoff between interpretability and accuracy that needs to be addressed. Black-box models that are not interpretable still outperform ours,” De Santis says.

In the future, the researchers want to study potential solutions to the information leakage problem, perhaps by adding additional concept bottleneck modules so unwanted concepts can’t leak through. They also plan to scale up their method by using a larger multimodal LLM to annotate a bigger training dataset, which could boost performance.

“I’m excited by this work because it pushes interpretable AI in a very promising direction and creates a natural bridge to symbolic AI and knowledge graphs,” says Andreas Hotho, professor and head of the Data Science Chair at the University of Würzburg, who was not involved with this work. “By deriving concept bottlenecks from the model’s own internal mechanisms rather than only from human-defined concepts, it offers a path toward explanations that are more faithful to the model and opens many opportunities for follow-up work with structured knowledge.”

This research was supported by the Progetto Rocca Doctoral Fellowship, the Italian Ministry of University and Research under the National Recovery and Resilience Plan, Thales Alenia Space, and the European Union under the NextGenerationEU project.