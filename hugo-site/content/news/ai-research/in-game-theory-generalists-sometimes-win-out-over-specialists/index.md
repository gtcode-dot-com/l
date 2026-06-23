---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-23T04:07:43.156687+00:00'
exported_at: '2026-06-23T04:07:44.685784+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/game-theory-generalists-sometimes-win-out-over-specialists-0617
structured_data:
  about: []
  author: ''
  description: In a new paper, MIT LIDS researchers show that for certain kinds of
    games, an overlooked class of algorithms performs much better than expected against
    better-trained opponents.
  headline: In game theory, generalists sometimes win out over specialists
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/game-theory-generalists-sometimes-win-out-over-specialists-0617
  publisher:
    logo: /favicon.ico
    name: GTCode
title: In game theory, generalists sometimes win out over specialists
updated_at: '2026-06-23T04:07:43.156687+00:00'
url_hash: 7f14127c5ea0af0703b3d60a2161a09a7fbb1e34
---

Whether you’re playing poker against a single opponent or find yourself in a bidding war over a home purchase with another prospective buyer, you are operating under conditions of imperfect information. You know what cards you’re holding in the poker game, and you also know how much above the home’s asking price you can afford, but you don’t know your opponent’s hand in the card game or how high the other home buyer is willing to go.

A
[paper](https://openreview.net/pdf?id=vClBDezZUo)
co-authored by MIT researchers and presented in April at the International Conference on Learning Representations in Rio De Janeiro won’t tell you what to do in these situations, specifically. But it does offer new insights into so-called imperfect-information games that involve two contestants facing off in a “zero-sum” competition, where one player’s gain means the other player’s loss.

MIT researchers on the project include Sobhan Mohammadpour, a PhD student in MIT’s Department of Electrical Engineering and Computer Science (EECS) and the Laboratory for Information and Decision Systems (LIDS); and Gabriele Farina, an assistant professor in EECS and a principal investigator at LIDS. Additional co-authors include Max Rudolph of the University of Texas at Austin (UT), Nathan Lichtlé of the University of California at Berkeley (UCB), Alexandre Bayen of UCB, J. Zico Kolter of Carnegie Mellon University (CMU), Amy X. Zhang ’11, MNG ’12 of UT; Eugene Vinitsky of New York University; and Samuel Sokota of CMU.

The focus of the new work is on algorithms that could be used to train neural networks to participate in imperfect-information games. The assumption, long-held in the field, was that algorithms grounded in principles of game theory would, in this setting, clearly outcompete a general-purpose variety of algorithms called policy gradient methods, which came into use for decision-making in the 1990s. The term “policy” in this context basically means strategy, whereas “gradient” refers to a path that leads in the direction of greatest change — to the top (or bottom) of a hill, for example. Policy gradient methods are being used to train neural networks to make decisions that move — in small, sequential steps — toward a particular goal (like reaching a summit, metaphorically speaking), with continual adjustments and course corrections made along the way to bring the agent closer to the intended destination.

Although strategic games were not on the original agenda when policy gradient methods were conceived in the early 1990s, the authors of the new paper still wondered how this class of algorithms might fare in two-player games. These methods become more complicated to analyze in multi-agent settings, according to Farina. “There is still a direction you can move in to improve your circumstances, but, because of the other player’s actions, that direction can constantly change over the course of the game. And those shifts can be rapid.”

“It had been pretty much taken for granted that specialized game-theoretic algorithms were the right approach for this setting,” says Sokota. “Our study showed that policy gradient methods can work better than these specialized algorithms, and that the specialized algorithms may not work as well as people thought — which raises an interesting sociological question about why this went unnoticed for so long. Part of the answer is that the field hadn’t done the engineering work required to rigorously evaluate the algorithms, so it was hard to tell what worked and what didn’t.”

Consequently, a major contribution of this work has been to provide an even-handed way of appraising different algorithms that can teach agents — i.e., neural networks — how to compete in imperfect-information games. “We’re taking a different approach,” notes Rudolph. “Unlike many of the papers published in this field, we’re not proposing a new algorithm that can beat out other algorithms. We’re proposing a benchmark that can assess these algorithms.”

Simply put, a benchmark consists of software designed to rate the performance of algorithms. “What we’re offering is a testing grounds, or playing grounds, where people can take their algorithms, train them for a specific task, and see how well they do,” says Farina.

The group calculates a player’s performance in terms of a concept called exploitability, which measures how well a player does against the “worst-case adversary,” Sokota explains. “In a game like poker, this opponent wouldn’t know what my hand is, but would know how I would behave for any given hand.” Achieving a zero on this scale implies perfect play, whereas a high exploitability score indicates far-from-optimal play.

Five games were played in experiments carried out by the team: two versions of Phantom Tic-Tac-Toe, in which players can’t see what their opponent has done, along with two imperfect-information variants of a board game called Hex, and another game of deception called Liar’s Dice.

The biggest challenge faced by the researchers was getting the exploitability measure to work on games of this size, which may include as many as 30 billion states. A “state” in this case is not just all the possible board positions, but also encompasses the entire history of the game, including every step and misstep along the way.

“It’s like looking into a dark room that’s filled with objects you can’t see,” says Mohammadpour. “Somehow, you need to figure out where these objects are and exactly how they got there.” Previous researchers, Mohammadpour adds, have typically used exploitability for games that are 100,000 times smaller than the ones analyzed in their study.

In the experiments carried out on these five games, neural networks trained with policy gradient algorithms got better (lower) exploitability scores than networks trained on game theory-based algorithms. In head-to-head competitions, which took place in the next round, the policy gradient-trained networks again beat their game theory-trained opponents. “Those results were reassuring,” Rudolph says, “because they give us more confidence in our benchmarking approach.”

The team has made their benchmarking software freely available and convenient to use. “You don’t need a supercomputer,” Mohammadpour says. “You can run it on an ordinary laptop. And all you have to do is add a single line of code to a commonly used collection of benchmarking software called OpenSpiel.”

Although their experiments involved some fairly obscure games, Farina would like to put this work into a broader context. “Keep in mind that the term 'game' really applies to any multi-agent strategic interaction,” he says. “So the lessons we learn from this research are by no means limited to recreational games.”

Vinitsky agrees. “Hidden information is a very important property of the world,” he says. “It pervades a range of things — including military operations, trading scenarios, and negotiations — all of which are carried out under conditions of hidden information. The idea that we can improve on these games suggests that we can also do better in these other settings as well.”

Ian Gemp — a computer scientist and game theory expert at Google DeepMind who was not involved in this study — finds these results encouraging. “This work serves as a compelling reminder,” he says, “that modernizing classical tools [like policy gradient methods] remains a highly productive path for solving complex strategic problems.”