---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-26T12:00:18.799781+00:00'
exported_at: '2025-11-26T12:00:21.019579+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126
structured_data:
  about: []
  author: ''
  description: MIT researchers find large language models sometimes mistakenly link
    grammatical sequences to specific topics, then rely on these learned patterns
    when answering queries. This can cause LLMs to fail on new tasks and could be
    exploited by adversarial agents to trick an LLM into generating harmful content.
  headline: Researchers discover a shortcoming that makes LLMs less reliable
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/shortcoming-makes-llms-less-reliable-1126
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers discover a shortcoming that makes LLMs less reliable
updated_at: '2025-11-26T12:00:18.799781+00:00'
url_hash: d75e912f956414ffeea800760c87a533a4b86806
---

Large language models (LLMs) sometimes learn the wrong lessons, according to an MIT study.

Rather than answering a query based on domain knowledge, an LLM could respond by leveraging grammatical patterns it learned during training. This can cause a model to fail unexpectedly when deployed on new tasks.

The researchers found that models can mistakenly link certain sentence patterns to specific topics, so an LLM might give a convincing answer by recognizing familiar phrasing instead of understanding the question.

Their experiments showed that even the most powerful LLMs can make this mistake.

This shortcoming could reduce the reliability of LLMs that perform tasks like handling customer inquiries, summarizing clinical notes, and generating financial reports.

It could also have safety risks. A nefarious actor could exploit this to trick LLMs into producing harmful content, even when the models have safeguards to prevent such responses.

After identifying this phenomenon and exploring its implications, the researchers developed a benchmarking procedure to evaluate a model’s reliance on these incorrect correlations. The procedure could help developers mitigate the problem before deploying LLMs.

“This is a byproduct of how we train models, but models are now used in practice in safety-critical domains far beyond the tasks that created these syntactic failure modes. If you’re not familiar with model training as an end-user, this is likely to be unexpected,” says Marzyeh Ghassemi, an associate professor in the MIT Department of Electrical Engineering and Computer Science (EECS), a member of the MIT Institute of Medical Engineering Sciences and the Laboratory for Information and Decision Systems, and the senior author of the study.

Ghassemi is joined by co-lead authors Chantal Shaib, a graduate student at Northeastern University and visiting student at MIT; and Vinith Suriyakumar, an MIT graduate student; as well as Levent Sagun, a research scientist at Meta; and Byron Wallace, the Sy and Laurie Sternberg Interdisciplinary Associate Professor and associate dean of research at Northeastern University’s Khoury College of Computer Sciences. A
[paper describing the work](https://arxiv.org/pdf/2509.21155)
will be presented at the Conference on Neural Information Processing Systems.

**Stuck on syntax**

LLMs are trained on a massive amount of text from the internet. During this training process, the model learns to understand the relationships between words and phrases — knowledge it uses later when responding to queries.

In prior work, the researchers found that LLMs pick up patterns in the parts of speech that frequently appear together in training data. They call these part-of-speech patterns “syntactic templates.”

LLMs need this understanding of syntax, along with semantic knowledge, to answer questions in a particular domain.

“In the news domain, for instance, there is a particular style of writing. So, not only is the model learning the semantics, it is also learning the underlying structure of how sentences should be put together to follow a specific style for that domain,” Shaib explains.

But in this research, they determined that LLMs learn to associate these syntactic templates with specific domains. The model may incorrectly rely solely on this learned association when answering questions, rather than on an understanding of the query and subject matter.

For instance, an LLM might learn that a question like “Where is Paris located?” is structured as adverb/verb/proper noun/verb. If there are many examples of sentence construction in the model’s training data, the LLM may associate that syntactic template with questions about countries.

So, if the model is given a new question with the same grammatical structure but nonsense words, like “Quickly sit Paris clouded?” it might answer “France” even though that answer makes no sense.

“This is an overlooked type of association that the model learns in order to answer questions correctly. We should be paying closer attention to not only the semantics but the syntax of the data we use to train our models,” Shaib says.

**Missing the meaning**

The researchers tested this phenomenon by designing synthetic experiments in which only one syntactic template appeared in the model’s training data for each domain. They tested the models by substituting words with synonyms, antonyms, or random words, but kept the underlying syntax the same.

In each instance, they found that LLMs often still responded with the correct answer, even when the question was complete nonsense.

When they restructured the same question using a new part-of-speech pattern, the LLMs often failed to give the correct response, even though the underlying meaning of the question remained the same.

They used this approach to test pre-trained LLMs like GPT-4 and Llama, and found that this same learned behavior significantly lowered their performance.

Curious about the broader implications of these findings, the researchers studied whether someone could exploit this phenomenon to elicit harmful responses from an LLM that has been deliberately trained to refuse such requests.

They found that, by phrasing the question using a syntactic template the model associates with a “safe” dataset (one that doesn’t contain harmful information), they could trick the model into overriding its refusal policy and generating harmful content.

“From this work, it is clear to me that we need more robust defenses to address security vulnerabilities in LLMs. In this paper, we identified a new vulnerability that arises due to the way LLMs learn. So, we need to figure out new defenses based on how LLMs learn language, rather than just ad hoc solutions to different vulnerabilities,” Suriyakumar says.

While the researchers didn’t explore mitigation strategies in this work, they developed an automatic benchmarking technique one could use to evaluate an LLM’s reliance on this incorrect syntax-domain correlation. This new test could help developers proactively address this shortcoming in their models, reducing safety risks and improving performance.

In the future, the researchers want to study potential mitigation strategies, which could involve augmenting training data to provide a wider variety of syntactic templates. They are also interested in exploring this phenomenon in reasoning models, special types of LLMs designed to tackle multi-step tasks.

“I think this is a really creative angle to study failure modes of LLMs. This work highlights the importance of linguistic knowledge and analysis in LLM safety research, an aspect that hasn’t been at the center stage but clearly should be,” says Jessy Li, an associate professor at the University of Texas at Austin, who was not involved with this work.

This work is funded, in part, by a Bridgewater AIA Labs Fellowship, the National Science Foundation, the Gordon and Betty Moore Foundation, a Google Research Award, and Schmidt Sciences.