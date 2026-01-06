---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-20T07:15:18.424649+00:00'
exported_at: '2025-11-20T07:15:20.686757+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/cost-of-thinking-1119
structured_data:
  about: []
  author: ''
  description: 'MIT McGovern Institute researchers find a surprising parallel in the
    ways humans and new AI models solve complex problems.

    '
  headline: The cost of thinking
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/cost-of-thinking-1119
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: The cost of thinking
updated_at: '2025-11-20T07:15:18.424649+00:00'
url_hash: 9db0f0079cd92cdaef589ea14610dcce8cd23164
---

Large language models (LLMs) like ChatGPT can write an essay or plan a menu almost instantly. But until recently, it was also easy to stump them. The models, which rely on language patterns to respond to users’ queries, often failed at math problems and were not good at complex reasoning. Suddenly, however, they’ve gotten a lot better at these things.

A new generation of LLMs known as reasoning models are being trained to solve complex problems. Like humans, they need some time to think through problems like these — and remarkably, scientists at MIT’s McGovern Institute for Brain Research have found that the kinds of problems that require the most processing from reasoning models are the very same problems that people need take their time with. In other words, they
[report today in the journal
*PNAS*](https://www.pnas.org/doi/10.1073/pnas.2520077122)
, the “cost of thinking” for a reasoning model is similar to the cost of thinking for a human.

The researchers, who were led by
[Evelina Fedorenko](https://mcgovern.mit.edu/profile/ev-fedorenko/)
, an associate professor of brain and cognitive sciences and an investigator at the McGovern Institute, conclude that in at least one important way, reasoning models have a human-like approach to thinking. That, they note, is not by design. “People who build these models don’t care if they do it like humans. They just want a system that will robustly perform under all sorts of conditions and produce correct responses,” Fedorenko says. “The fact that there’s some convergence is really quite striking.”

**Reasoning models**

Like many forms of artificial intelligence, the new reasoning models are artificial neural networks: computational tools that learn how to process information when they are given data and a problem to solve. Artificial neural networks have been very successful at many of the tasks that the brain’s own neural networks do well — and in some cases, neuroscientists have discovered that those that perform best do share certain aspects of information processing in the brain. Still, some scientists argued that artificial intelligence was not ready to take on more sophisticated aspects of human intelligence.

“Up until recently, I was among the people saying, ‘These models are really good at things like perception and language, but it’s still going to be a long ways off until we have neural network models that can do reasoning,” Fedorenko says. “Then these large reasoning models emerged and they seem to do much better at a lot of these thinking tasks, like solving math problems and writing pieces of computer code.”

Andrea Gregor de Varda, a
[K. Lisa Yang ICoN Center](https://yangtan.mit.edu/icon/)
Fellow and a postdoc in Fedorenko’s lab, explains that reasoning models work out problems step by step. “At some point, people realized that models needed to have more space to perform the actual computations that are needed to solve complex problems,” he says. “The performance started becoming way, way stronger if you let the models break down the problems into parts.”

To encourage models to work through complex problems in steps that lead to correct solutions, engineers can use reinforcement learning. During their training, the models are rewarded for correct answers and penalized for wrong ones. “The models explore the problem space themselves,” de Varda says. “The actions that lead to positive rewards are reinforced, so that they produce correct solutions more often.”

Models trained in this way are much more likely than their predecessors to arrive at the same answers a human would when they are given a reasoning task. Their stepwise problem-solving does mean reasoning models can take a bit longer to find an answer than the LLMs that came before — but since they’re getting right answers where the previous models would have failed, their responses are worth the wait.

The models’ need to take some time to work through complex problems already hints at a parallel to human thinking: if you demand that a person solve a hard problem instantaneously, they’d probably fail, too. De Varda wanted to examine this relationship more systematically. So he gave reasoning models and human volunteers the same set of problems, and tracked not just whether they got the answers right, but also how much time or effort it took them to get there.

**Time versus tokens**

This meant measuring how long it took people to respond to each question, down to the millisecond. For the models, Varda used a different metric. It didn’t make sense to measure processing time, since this is more dependent on computer hardware than the effort the model puts into solving a problem. So instead, he tracked tokens, which are part of a model’s internal chain of thought. “They produce tokens that are not meant for the user to see and work on, but just to have some track of the internal computation that they’re doing,” de Varda explains. “It’s as if they were talking to themselves.”

Both humans and reasoning models were asked to solve seven different types of problems, like numeric arithmetic and intuitive reasoning. For each problem class, they were given many problems. The harder a given problem was, the longer it took people to solve it — and the longer it took people to solve a problem, the more tokens a reasoning model generated as it came to its own solution.

Likewise, the classes of problems that humans took longest to solve were the same classes of problems that required the most tokens for the models: arithmetic problems were the least demanding, whereas a group of problems called the “ARC challenge,” where pairs of colored grids represent a transformation that must be inferred and then applied to a new object, were the most costly for both people and models.

De Varda and Fedorenko say the striking match in the costs of thinking demonstrates one way in which reasoning models are thinking like humans. That doesn’t mean the models are recreating human intelligence, though. The researchers still want to know whether the models use similar representations of information to the human brain, and how those representations are transformed into solutions to problems. They’re also curious whether the models will be able to handle problems that require world knowledge that is not spelled out in the texts that are used for model training.

The researchers point out that even though reasoning models generate internal monologues as they solve problems, they are not necessarily using language to think. “If you look at the output that these models produce while reasoning, it often contains errors or some nonsensical bits, even if the model ultimately arrives at a correct answer. So the actual internal computations likely take place in an abstract, non-linguistic representation space, similar to how humans don’t use language to think,” he says.