---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-07T04:42:02.920405+00:00'
exported_at: '2026-10-07T04:42:06.988055+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/game-playing-ai-stratego-new-champ-0930
structured_data:
  about: []
  author: ''
  description: Researchers developed an AI system that beat human experts at the board
    wargame Stratego and outperformed more expensive models. This new system could
    someday help humans make strategic decisions in situations when some information
    is hidden.
  headline: This game-playing AI is the new champ at Stratego
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/game-playing-ai-stratego-new-champ-0930
  publisher:
    logo: /favicon.ico
    name: GTCode
title: This game-playing AI is the new champ at Stratego
updated_at: '2026-10-07T04:42:02.920405+00:00'
url_hash: ea039df066f8591ee37f231cf0dd8fa7c2a8a62b
---

A new AI system that excels at challenging games with hidden information could someday help human decision-makers select ideal strategies to outfox opponents in complicated situations like military maneuvers.

Using advances in machine-learning, researchers from MIT, Carnegie Mellon University, New York University, and Stanford University developed an AI that defeated top-ranked human players of the board wargame Stratego by a large margin — something no AI system had been able to achieve.

Stratego, a two-player game of imperfect information, in which the opponent’s piece identities remain hidden, is often used as a benchmark to test the strategic thinking abilities of powerful AI models.

To build their model, the researchers combined efficient training algorithms with new techniques tailored for calculated decision-making in hidden information settings.

The AI system achieved greater performance at Stratego than the next best models, while being far cheaper and less computationally demanding to train. The system also outperformed top human players in other strategic games with different rules and designs, demonstrating how it can be generalized for a variety of use-cases.

The AI system could be adapted to help humans tackle many real-world problems with hidden information, such as business negotiations or cybersecurity.

“In the kind of imperfect information tasks you would face in reality, you often don’t have the luxury of enumerating through all the possibilities. There are just too many. Having AI algorithms that are general purpose and can provably perform this challenging task so well is a big step forward,” says Gabriele Farina, an assistant professor in the Department of Electrical Engineering and Computer Science (EECS), principal investigator at the Laboratory for Information and Decision Systems (LIDS), and senior author of a paper on this AI system.

He is joined on the paper by lead author Samuel Sokota, a graduate student at Carnegie Mellon; Eugene Vinitsky, an assistant professor at NYU; Zico Kolter, a professor at Carnegie Mellon; Hengyuan Hu, a graduate student at Stanford; and Zhiyuan Fan, an EECS graduate student at MIT. The research
[appears today in
*Nature*](https://www.nature.com/articles/s41586-026-11036-y)
.

**Hidden information**

The world is full of imperfect information problems.

In these interactions, some parties possess information others do not. For instance, traders in financial markets may not know the rationale behind the trades of others, while military forces likely don’t have full knowledge of enemy positions.

With hidden information, the decisions parties make, as well as the decisions they choose not to make, are intertwined in such a way that it is extremely difficult to determine the best steps to take next.

“The more you bluff, the more your opponent expects it, and the less each bluff is worth. It’s not obvious how to reason about that,” Sokota explains. “It’s very different from a setting like chess, where the best move is still the best move no matter how often you’ve played it.”

Stratego is often used to model imperfect information situations. In this board wargame, which resembles military chess, players arrange 40 pieces on their side of a board and then move pieces across the board to capture their opponent’s flag.

But the identity of all pieces remains secret until they collide, and then the lower-ranking piece is eliminated.

The possible piece configurations number more than 10 to the 66th power — an exponentially greater number than in chess — making Stratego extremely difficult for an AI system to play well.

Past efforts, such as Google’s DeepMind, relied on sophisticated operations that were computationally demanding and costly. But even with millions of dollars in training costs, these models were still not strong enough to beat top human Stratego players.

“With Stratego, there is an explosion of possible universes you might have to deal with. AI techniques that were developed for games like poker definitely could not scale in this setting,” Farina says.

The MIT researchers set out to develop a full AI system that could achieve superhuman performance for less cost, which they called Ataraxos (a Greek word used to describe one who is unbothered or free from anxiety).

**A two-pronged approach**

To build Ataraxos, the researchers trained the model using a technique called self-play reinforcement learning. The model plays against itself many times to learn a strong “blueprint strategy” of how to excel at Stratego.

They designed especially efficient algorithms, which enabled Ataraxos to learn much faster than prior methods while ensuring it didn’t get stuck trying to predict every possible move. This reduces training costs and boosts performance.

“Our system reaches strictly higher playing strength than DeepNash (DeepMind’s system) while using less than one hundredth of the training examples and less than one thirtieth of the self-play games, indicating a massive improvement in efficiency,” says Farina.

During a game, Ataraxos uses the blueprint strategy as a starting point to set up the board and begin thinking about its next moves at each round of play.

But before acting, it refines its choices on the fly using a technique called decision-time planning. The system employs a generative model that uses probabilities to estimate the likely identities of the opponent’s hidden pieces, then evaluates future choices before selecting the next move.

“Rather than just guessing blindly, we use decision-time planning to find the most plausible state of the board. Using this generative model allows us to really zoom in on the specific board and opponent we are facing,” Farina says.

The innovative use of this generative model for decision-time planning was the missing piece that enabled Ataraxos to achieve superhuman performance.

Ataraxos beat the strongest Stratego player in the world by a record margin of 15-1-4 and achieved a 39-2 record against top human players at the Stratego world championship. “Ataraxos is good at calculating risk in a way that humans are not. A human might start freaking out if their most valuable piece is exposed, but the bot can be surprisingly composed. It doesn’t overcorrect and give away its secrets,” Farina says.

The researchers also adapted Ataraxos for other imperfect information games, including Barrage Stratego (a faster-paced variant with fewer pieces), Hanabi (a cooperative card game with many players), and Dou dizhu (a game in which two players cooperate against a third).

The system achieved superhuman performance in each instance, demonstrating the generality of this method.

In the future, the researchers want to build interpretability measures into Ataraxos so the system can explain its decision-making in a way that a human could understand.

“Humans must have the final say in whether a recommendation is followed, so before adoption can happen, we need a way to audit the model’s decisions. We still have a long way to go, but I hope these algorithms can be the foundation for a lot more work to come,” Farina says.

This research is funded, in part, by the Office of Naval Research, the New York University Department of Civil and Urban Engineering, the C2SMART Center, the National Science Foundation, and a Schmidt Sciences AI2050 Early Career Fellowship.