---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-20T22:15:25.801333+00:00'
exported_at: '2026-01-20T22:15:28.013020+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/why-its-critical-to-move-beyond-overly-aggregated-machine-learning-metrics-0120
structured_data:
  about: []
  author: ''
  description: MIT researchers have identified significant examples of machine learning
    model failure when those models are applied to data other than what they were
    trained on, raising questions about the need to test whenever a model is deployed
    in a new setting.
  headline: Why it’s critical to move beyond overly aggregated machine-learning metrics
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/why-its-critical-to-move-beyond-overly-aggregated-machine-learning-metrics-0120
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Why it’s critical to move beyond overly aggregated machine-learning metrics
updated_at: '2026-01-20T22:15:25.801333+00:00'
url_hash: cac57eb8febb8cf4e86acf272e13a036410a44c7
---

MIT researchers have identified significant examples of machine-learning model failure when those models are applied to data other than what they were trained on, raising questions about the need to test whenever a model is deployed in a new setting.

“We demonstrate that even when you train models on large amounts of data, and choose the best average model, in a new setting this ‘best model’ could be the worst model for 6-75 percent of the new data,” says Marzyeh Ghassemi, an associate professor in MIT’s Department of Electrical Engineering and Computer Science (EECS), a member of the Institute for Medical Engineering and Science, and principal investigator at the Laboratory for Information and Decision Systems.

In a
[paper](https://arxiv.org/pdf/2510.24884)
that was presented at the Neural Information Processing Systems (NeurIPS 2025) conference in December, the researchers point out that models trained to effectively diagnose illness in chest X-rays at one hospital, for example, may be considered effective in a different hospital, on average. The researchers’ performance assessment, however, revealed that some of the best-performing models at the first hospital were the worst-performing on up to 75 percent of patients at the second hospital, even though when all patients are aggregated in the second hospital, high average performance hides this failure.

Their findings demonstrate that although spurious correlations — a simple example of which is when a machine-learning system, not having “seen” many cows pictured at the beach, classifies a photo of a beach-going cow as an orca simply because of its background — are thought to be mitigated by just improving model performance on observed data, they actually still occur and remain a risk to a model’s trustworthiness in new settings. In many instances — including areas examined by the researchers such as chest X-rays, cancer histopathology images, and hate speech detection — such spurious correlations are much harder to detect.

In the case of a medical diagnosis model trained on chest X-rays, for example, the model may have learned to correlate a specific and irrelevant marking on one hospital’s X-rays with a certain pathology. At another hospital where the marking is not used, that pathology could be missed.

Previous research by Ghassemi’s group has shown that models can spuriously correlate such factors as age, gender, and race with medical findings. If, for instance, a model has been trained on more older people’s chest X-rays that have pneumonia and hasn’t “seen” as many X-rays belonging to younger people, it might predict that only older patients have pneumonia.

“We want models to learn how to look at the anatomical features of the patient and then make a decision based on that,” says Olawale Salaudeen, an MIT postdoc and the lead author of the paper, “but really anything that’s in the data that’s correlated with a decision can be used by the model. And those correlations might not actually be robust with changes in the environment, making the model predictions unreliable sources of decision-making.”

Spurious correlations contribute to the risks of biased decision-making. In the NeurIPS conference paper, the researchers showed that, for example, chest X-ray models that improved overall diagnosis performance actually performed worse on patients with pleural conditions or enlarged cardiomediastinum, meaning enlargement of the heart or central chest cavity.

Other authors of the paper included PhD students Haoran Zhang and Kumail Alhamoud, EECS Assistant Professor Sara Beery, and Ghassemi.

While previous work has generally accepted that models ordered best-to-worst by performance will preserve that order when applied in new settings, called accuracy-on-the-line, the researchers were able to demonstrate examples of when the best-performing models in one setting were the worst-performing in another.

Salaudeen devised an algorithm called OODSelect to find examples where accuracy-on-the-line was broken. Basically, he trained thousands of models using in-distribution data, meaning the data were from the first setting, and calculated their accuracy. Then he applied the models to the data from the second setting. When those with the highest accuracy on the first-setting data were wrong when applied to a large percentage of examples in the second setting, this identified the problem subsets, or sub-populations. Salaudeen also emphasizes the dangers of aggregate statistics for evaluation, which can obscure more granular and consequential information about model performance.

In the course of their work, the researchers separated out the “most miscalculated examples” so as not to conflate spurious correlations within a dataset with situations that are simply difficult to classify.

The NeurIPS paper releases the researchers’ code and some identified subsets for future work.

Once a hospital, or any organization employing machine learning, identifies subsets on which a model is performing poorly, that information can be used to improve the model for its particular task and setting. The researchers recommend that future work adopt OODSelect in order to highlight targets for evaluation and design approaches to improving performance more consistently.

“We hope the released code and OODSelect subsets become a steppingstone,” the researchers write, “toward benchmarks and models that confront the adverse effects of spurious correlations.”