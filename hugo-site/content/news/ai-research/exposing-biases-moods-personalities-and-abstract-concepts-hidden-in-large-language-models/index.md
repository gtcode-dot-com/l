---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T00:14:16.382292+00:00'
exported_at: '2026-03-03T00:14:17.712014+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/exposing-biases-moods-personalities-hidden-large-language-models-0219
structured_data:
  about: []
  author: ''
  description: A new method can test whether a large language model contains hidden
    biases, personalities, moods, or other abstract concepts. MIT researchers can
    zero in on connections within a model that encode for a concept of interest, to
    improve LLM safety and performance.
  headline: Exposing biases, moods, personalities, and abstract concepts hidden in
    large language models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/exposing-biases-moods-personalities-hidden-large-language-models-0219
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Exposing biases, moods, personalities, and abstract concepts hidden in large
  language models
updated_at: '2026-03-03T00:14:16.382292+00:00'
url_hash: 62c1ae27c0d3c57eec180b4eb3913c4ae3140302
---

By now, ChatGPT, Claude, and other large language models have accumulated so much human knowledge that they’re far from simple answer-generators; they can also express abstract concepts, such as certain tones, personalities, biases, and moods. However, it’s not obvious exactly how these models represent abstract concepts to begin with from the knowledge they contain.

Now a team from MIT and the University of California San Diego has developed a way to test whether a large language model (LLM) contains hidden biases, personalities, moods, or other abstract concepts. Their method can zero in on connections within a model that encode for a concept of interest. What’s more, the method can then manipulate, or “steer” these connections, to strengthen or weaken the concept in any answer a model is prompted to give.

The team proved their method could quickly root out and steer more than 500 general concepts in some of the largest LLMs used today. For instance, the researchers could home in on a model’s representations for personalities such as “social influencer” and “conspiracy theorist,” and stances such as “fear of marriage” and “fan of Boston.” They could then tune these representations to enhance or minimize the concepts in any answers that a model generates.

In the case of the “conspiracy theorist” concept, the team successfully identified a representation of this concept within one of the largest vision language models available today. When they enhanced the representation, and then prompted the model to explain the origins of the famous “Blue Marble” image of Earth taken from Apollo 17, the model generated an answer with the tone and perspective of a conspiracy theorist.

The team acknowledges there are risks to extracting certain concepts, which they also illustrate (and caution against). Overall, however, they see the new approach as a way to illuminate hidden concepts and potential vulnerabilities in LLMs, that could then be turned up or down to improve a model’s safety or enhance its performance.

“What this really says about LLMs is that they have these concepts in them, but they’re not all actively exposed,” says Adityanarayanan “Adit” Radhakrishnan, assistant professor of mathematics at MIT. “With our method, there’s ways to extract these different concepts and activate them in ways that prompting cannot give you answers to.”

The team published their findings today in a study
[appearing in the journal
*Science*](http://doi.org/10.1126/science.aea6792)
. The study’s co-authors include Radhakrishnan, Daniel Beaglehole and Mikhail Belkin of UC San Diego, and Enric Boix-Adserà of the University of Pennsylvania.

**A fish in a black box**

As use of OpenAI’s ChatGPT, Google’s Gemini, Anthropic’s Claude, and other artificial intelligence assistants has exploded, scientists are racing to understand how models represent certain abstract concepts such as “hallucination” and “deception.” In the context of an LLM, a hallucination is a response that is false or contains misleading information, which the model has “hallucinated,” or constructed erroneously as fact.

To find out whether a concept such as “hallucination” is encoded in an LLM, scientists have often taken an approach of “unsupervised learning” — a type of machine learning in which algorithms broadly trawl through unlabeled representations to find patterns that might relate to a concept such as “hallucination.” But to Radhakrishnan, such an approach can be too broad and computationally expensive.

“It’s like going fishing with a big net, trying to catch one species of fish. You’re gonna get a lot of fish that you have to look through to find the right one,” he says. “Instead, we’re going in with bait for the right species of fish.”

He and his colleagues had previously developed the beginnings of a more targeted approach with a type of predictive modeling algorithm known as a recursive feature machine (RFM). An RFM is designed to directly identify features or patterns within data by leveraging a mathematical mechanism that neural networks — a broad category of AI models that includes LLMs — implicitly use to learn features.

Since the algorithm was an effective, efficient approach for capturing features in general, the team wondered whether they could use it to root out representations of concepts, in LLMs, which are by far the most widely used type of neural network and perhaps the least well-understood.

“We wanted to apply our feature learning algorithms to LLMs to, in a targeted way, discover representations of concepts in these large and complex models,” Radhakrishnan says.

**Converging on a concept**

The team’s new approach identifies any concept of interest within a LLM and “steers” or guides a model’s response based on this concept. The researchers looked for 512 concepts within five classes: fears (such as of marriage, insects, and even buttons); experts (social influencer, medievalist); moods (boastful, detachedly amused); a preference for locations (Boston, Kuala Lumpur); and personas (Ada Lovelace, Neil deGrasse Tyson).

The researchers then searched for representations of each concept in several of today’s large language and vision models. They did so by training RFMs to recognize numerical patterns in an LLM that could represent a particular concept of interest.

A standard large language model is, broadly, a
[neural network](https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414)
that takes a natural language prompt, such as “Why is the sky blue?” and divides the prompt into individual words, each of which is encoded mathematically as a list, or vector, of numbers. The model takes these vectors through a series of computational layers, creating matrices of many numbers that, throughout each layer, are used to identify other words that are most likely to be used to respond to the original prompt. Eventually, the layers converge on a set of numbers that is decoded back into text, in the form of a natural language response.

The team’s approach trains RFMs to recognize numerical patterns in an LLM that could be associated with a specific concept. As an example, to see whether an LLM contains any representation of a “conspiracy theorist,” the researchers would first train the algorithm to identify patterns among LLM representations of 100 prompts that are clearly related to conspiracies, and 100 other prompts that are not. In this way, the algorithm would learn patterns associated with the conspiracy theorist concept. Then, the researchers can mathematically modulate the activity of the conspiracy theorist concept by perturbing LLM representations with these identified patterns.

The method can be applied to search for and manipulate any general concept in an LLM. Among many examples, the researchers identified representations and manipulated an LLM to give answers in the tone and perspective of a “conspiracy theorist.” They also identified and enhanced the concept of “anti-refusal,” and showed that whereas normally, a model would be programmed to refuse certain prompts, it instead answered, for instance giving instructions on how to rob a bank.

Radhakrishnan says the approach can be used to quickly search for and minimize vulnerabilities in LLMs. It can also be used to enhance certain traits, personalities, moods, or preferences, such as emphasizing the concept of “brevity” or “reasoning” in any response an LLM generates. The team has made the method’s underlying code publicly available.

“LLMs clearly have a lot of these abstract concepts stored within them, in some representation,” Radhakrishnan says
**. “**
There are ways where, if we understand these representations well enough, we can build highly specialized LLMs that are still safe to use but really effective at certain tasks.”

This work was supported, in part, by the National Science Foundation, the Simons Foundation, the TILOS institute, and the U.S. Office of Naval Research.