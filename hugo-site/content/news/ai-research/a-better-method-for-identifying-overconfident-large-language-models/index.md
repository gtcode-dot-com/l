---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-26T22:51:51.301767+00:00'
exported_at: '2026-03-26T22:51:56.075100+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319
structured_data:
  about: []
  author: ''
  description: A new technique for assessing the reliability of a large language model’s
    predictions is better at identifying when the model is confident, but wrong. This
    more accurate method for uncertainty quantification could help users know whether
    to trust the model’s outputs.
  headline: A better method for identifying overconfident large language models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A better method for identifying overconfident large language models
updated_at: '2026-03-26T22:51:51.301767+00:00'
url_hash: 6afbee7e967a89c10efce84a66a273041ca9736f
---

Large language models (LLMs) can generate credible but inaccurate responses, so researchers have developed uncertainty quantification methods to check the reliability of predictions. One popular method involves submitting the same prompt multiple times to see if the model generates the same answer.

But this method measures self-confidence, and even the most impressive LLM might be confidently wrong. Overconfidence can mislead users about the accuracy of a prediction, which might result in devastating consequences in high-stakes settings like health care or finance.

To address this shortcoming, MIT researchers introduced a new method for measuring a different type of uncertainty that more reliably identifies confident but incorrect LLM responses.

Their method involves comparing a target model’s response to responses from a group of similar LLMs. They found that measuring cross-model disagreement more accurately captures this type of uncertainty than traditional approaches.

They combined their approach with a measure of LLM self-consistency to create a total uncertainty metric, and evaluated it on 10 realistic tasks, such as question-answering and math reasoning. This total uncertainty metric consistently outperformed other measures and was better at identifying unreliable predictions.

“Self-consistency is being used in a lot of different approaches for uncertainty quantification, but if your estimate of uncertainty only relies on a single model’s outcome, it is not necessarily trustable. We went back to the beginning to understand the limitations of current approaches and used those as a starting point to design a complementary method that can empirically improve the results,” says Kimia Hamidieh, an electrical engineering and computer science (EECS) graduate student at MIT and lead author of a
[paper on this technique](https://openreview.net/pdf?id=lOoRJo8xWy)
.

She is joined on the paper by Veronika Thost, a research scientist at the MIT-IBM Watson AI Lab; Walter Gerych, a former MIT postdoc who is now an assistant professor at Worcester Polytechnic Institute; Mikhail Yurochkin, a staff research scientist at the MIT-IBM Watson AI Lab; and senior author Marzyeh Ghassemi, an associate professor in EECS and a member of the Institute of Medical Engineering Sciences and the Laboratory for Information and Decision Systems.

**Understanding overconfidence**

Many popular methods for uncertainty quantification involve asking a model for a confidence score or testing the consistency of its responses to the same prompt. These methods estimate aleatoric uncertainty, or how internally confident a model is in its own prediction.

However, LLMs can be confident when they are completely wrong. Research has shown that epistemic uncertainty, or uncertainty about whether one is using the right model, can be a better way to assess true uncertainty when a model is overconfident.

The MIT researchers estimate epistemic uncertainty by measuring disagreement across a similar group of LLMs.

“If I ask ChatGPT the same question multiple times and it gives me the same answer over and over again, that doesn’t mean the answer is necessarily correct. If I switch to Claude or Gemini and ask them the same question, and I get a different answer, that is going to give me a sense of the epistemic uncertainty,” Hamidieh explains.

Epistemic uncertainty attempts to capture how far a target model diverges from the ideal model for that task. But since it is impossible to build an ideal model, researchers use surrogates or approximations that often rely on faulty assumptions.

To improve uncertainty quantification, the MIT researchers needed a more accurate way to estimate epistemic uncertainty.

**An ensemble approach**

The method they developed involves measuring the divergence between the target model and a small ensemble of models with similar size and architecture. They found that comparing semantic similarity, or how closely the meanings of the responses match, could provide a better estimate of epistemic uncertainty.

To achieve the most accurate estimate, the researchers needed a set of LLMs that covered diverse responses, weren’t too similar to the target model, and were weighted based on credibility.

“We found that the easiest way to satisfy all these properties is to take models that are trained by different companies. We tried many different approaches that were more complex, but this very simple approach ended up working best,” Hamidieh says.

Once they had developed this method for estimating epistemic uncertainty, they combined it with a standard approach that measures aleatoric uncertainty. This total uncertainty metric (TU) offered the most accurate reflection of whether a model’s confidence level is trustworthy.

“Uncertainty depends on the uncertainty of the given prompt as well as how close our model is to the optimal model. This is why summing up these two uncertainty metrics is going to give us the best estimate,” Hamidieh says.

TU could more effectively identify situations where an LLM is hallucinating, since epistemic uncertainty can flag confidently wrong outputs that aleatoric uncertainty might miss. It could also enable researchers to reinforce an LLM’s confidently correct answers during training, which may improve performance.

They tested TU using multiple LLMs on 10 common tasks, such as question-answering, summarization, translation, and math reasoning. Their method more effectively identified unreliable predictions than either measure on its own.

Measuring total uncertainty often required fewer queries than calculating aleatoric uncertainty, which could reduce computational costs and save energy.

Their experiments also revealed that epistemic uncertainty is most effective on tasks with a unique correct answer, like factual question-answering, but may underperform on more open-ended tasks.

In the future, the researchers could adapt their technique to improve its performance on open-ended queries. They may also build on this work by exploring other forms of aleatoric uncertainty.

This work is funded, in part, by the MIT-IBM Watson AI Lab.