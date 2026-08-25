---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-08-25T18:45:28.381114+00:00'
exported_at: '2026-08-25T18:45:29.829046+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/medical-ai-assistance-benefits-vary-based-on-user-expertise-0804
structured_data:
  about: []
  author: ''
  description: New research found non-experts deferred to AI-based assistance in diagnosing
    skin cancer, even when it was wrong, while clinicians were more likely to catch
    AI errors.
  headline: The benefits of medical AI assistance vary based on user expertise
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/medical-ai-assistance-benefits-vary-based-on-user-expertise-0804
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The benefits of medical AI assistance vary based on user expertise
updated_at: '2026-08-25T18:45:28.381114+00:00'
url_hash: e72169530bcddc1a05eadb7599091b885f8388a9
---

A one-size-fits-all approach likely isn’t the best strategy when designing artificial intelligence systems that assist users in disease diagnosis.

A new study by researchers at MIT and elsewhere found that, while AI assistance generally improved the accuracy of non-experts and clinicians in diagnosing skin diseases, AI explainability methods had different impacts depending on the users’ knowledge level.

Explainable AI methods help users know when to trust a model’s predictions by describing or validating the model’s decision-making. For instance, a model might use a heat map to highlight image regions that were most important in its diagnosis or a large language model (LLM) to explain the prediction in plain language.

In this study, researchers tested non-experts and primary care providers in skin disease diagnosis, with and without the help of different explainable AI systems.

They found that non-experts’ diagnostic accuracy improved, but it was largely due to deference to the AI system. Non-experts trusted LLM-based explanations whether they were right or wrong, and found explanations more convincing when they were vague or generic.

By contrast, clinicians were not tripped up by incorrect AI assistance and performed best when given only a model’s prediction, with no accompanying explanation.

“Good AI systems can improve performance in some health settings, but this has to be balanced carefully with algorithmic deference that can lead to more error. We know that both AI and explainability methods can engage automation bias in humans, and this anchoring effect is something that must be accounted for when we design AI systems,” says Marzyeh Ghassemi, an associate professor in MIT’s Department of Electrical Engineering and Computer Science (EECS), a member of the Institute for Medical Engineering and Science, and a principal investigator at the Laboratory for Information and Decision Systems and the Abdul Latif Jameel Clinic for Machine Learning in Health.

“These findings are important as patients increasingly turn to AI to help with their health care. Our findings show that those with the least medical knowledge are most likely to be led astray when explainable AI models give an erroneous output,” says Roxana Daneshjou, a co-author and assistant professor of biomedical data science and dermatology at Stanford University.

These results underscore the importance of building AI systems with users in mind and of developing explainability methods that encourage critical thinking rather than overreliance on the model, the researchers say.

“It’s getting obvious that we cannot just assume a good AI will solve all problems. We need to pay careful attention to the users who will be using the AI system, because the same explanation can help an expert and mislead a beginner. Often the people who could benefit most from AI are the ones most likely to be led astray by it, so how we present a recommendation matters as much as whether it’s correct,” says lead author Orson Xu, an assistant professor in the Department of Biomedical Informatics at Columbia University.

Ghassemi, Xu, and Daneshjou are joined on the paper by many authors, including MIT graduate student Haoran Zhang, undergraduate Reina Wang, and Luis Soenksen PhD ’20, a research affiliate at the Jameel Clinic, along with clinicians and researchers. A description of the work
[appears today in
*Nature Medicine*](https://link.springer.com/article/10.1038/s41591-026-04553-w)
.

**Exploring explanations**

Several FDA-approved AI interfaces are being used to help clinicians identify skin conditions in medical images, as a way to streamline early diagnosis. In addition to providing a prediction of whether disease is present in the image, these tools often use one of several methods that explain the model’s decision-making.

At the same time, non-experts can perform digital diagnosis on their own using AI-powered search engines that predict skin diseases based on user prompts. These systems often use LLMs to explain the model’s prediction in simpler terms.

The researchers explored the effects and potential benefits of these explainable AI tools on primary care physicians and non-experts in dermatological disease detection. They tested users by showing them medical images plus an AI prediction of skin disease, employing different explainable AI approaches.

These approaches included: an AI prediction and confidence level with no explanation, a method that provides similar images to reinforce its prediction, a heat map-based approach that highlights important image regions, and an LLM that explains the model’s reasoning in plain language.

Non-experts were tasked with deciding whether an image of a skin mole was cancerous, with and without the help of explainable AI. Clinicians were given the more challenging task of providing a differential diagnosis of dermatological disease.

The researchers found that all explainable AI approaches improved the accuracy of non-experts, mostly because the tools helped users diagnose non-cancerous moles.

In addition, when they employed a fairness-constrained model designed to combat bias against darker skin tones, the system significantly improved accuracy and reduced diagnostic disparities based on skin tone.

“But the reason non-expert users are better is because they are more reliant on the models. When the model is wrong, it hurts performance more than it helps performance when the model is right. We were just able to train very good AI models for this setting,” Ghassemi says.

This deference effect is largest with LLM explanations, and users were more confident about their wrong answers when aided by an LLM.

On the other hand, clinicians were resilient to incorrect AI explanations and, of all the explainability methods, LLMs boost their accuracy the least.

“It really comes down to how each group uses the explanation. A clinician already has a diagnosis in mind and checks the AI against their own training, so a bad explanation gets caught. Meanwhile, a non-expert can use that exact same explanation to form an opinion in the first place, so a plausible, confident-sounding rationale can pull them toward the wrong answer. The same tool ends up being an asset for one user and a liability for another,” Xu says.

**Overcoming the deference effect**

When the researchers dug deeper, they found that users who were most deferential to AI assistance were the worst performers on the task without the help of AI.

They also found that the time at which
users were presented with AI explanations influenced their behavior. If an explanation is given first, before the user can perform the diagnosis on their own, they tend to become more deferential to the model.

In addition, AI systems outperformed humans when the presentation of disease was subtle, but humans performed much better if there are atypical symptoms or unrelated features in an image.

Taken together, these results indicate that explainable AI can cause overreliance on models and lead users to blindly follow AI recommendations even when they are wrong.

Rather than using LLMs to generate more detailed explanations, it might be more effective to force users to give a diagnostic hypothesis first, then provide an AI-based suggestion to highlight other possible conditions for consideration.

“We really want AI to improve creativity and either upskill or fill in gaps where users are missing subtle presentations. Otherwise, we risk engaging automation bias and then, when the model is wrong, users can’t recover,” Ghassemi says.

This research was funded, in part, by the National Science Foundation, Schmidt Sciences, the National Bureau of Economic Research, and Columbia University.