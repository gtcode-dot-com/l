---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-08-25T01:36:50.028315+00:00'
exported_at: '2026-08-25T01:36:54.607203+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/determining-playoff-clinching-scenarios-in-the-nhl-using-constraint-programming
structured_data:
  about: []
  author: ''
  description: The AWS Generative AI Innovation Center built an automated system that
    uses constraint programming and custom tree search to determine, with mathematical
    certainty, when and how an NHL team clinches a playoff spot. The approach was
    validated against four full NHL seasons of officially published results.
  headline: Determining playoff clinching scenarios in the NHL using constraint programming
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/determining-playoff-clinching-scenarios-in-the-nhl-using-constraint-programming
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Determining playoff clinching scenarios in the NHL using constraint programming
updated_at: '2026-08-25T01:36:50.028315+00:00'
url_hash: 00ec4857b4b36b61a297f453f00a13f837a345f9
---

As the National Hockey League (NHL) regular season enters its final stretch each spring, one question dominates the minds of hockey fans: has my team clinched the playoffs? The answer is often surprisingly hard to discern. With 32 teams, complex tie-breaking rules, and hundreds of remaining games, determining whether a team is mathematically guaranteed a playoff spot is a serious combinatorial challenge.

In this post, we describe how the
[AWS Generative AI Innovation Center](/ai/generative-ai/innovation-center/)
created an automated system that determines NHL playoff clinching scenarios. Our approach uses constraint programming (CP) and custom tree search to produce these scenarios, and we validated the results against those officially published by the NHL. For more details, see our
[scientific paper](https://arxiv.org/abs/2605.13142)
.

## Background: what it means to clinch the playoffs

A team has
*clinched the playoffs*
(or simply “clinched”) if it is guaranteed to make the playoffs regardless of the outcomes of any remaining games. As the season progresses, usually starting in March, the NHL publishes daily clinching scenarios for teams that could clinch based on that evening’s games. These scenarios take the form of statements like:

&gt; The Minnesota Wild will clinch the playoffs if any of the following holds: they get at least one point against the Anaheim Ducks, the St. Louis Blues lose to the Utah Hockey Club in any fashion, or the Calgary Flames lose to the Vegas Golden Knights in any fashion.

Producing such scenarios manually has become increasingly time-consuming and error-prone as the league’s tie-breaking rules have grown more elaborate. Our work contributes an automated, mathematically rigorous alternative that is efficient for daily use.

## The NHL playoff structure

The NHL’s 32 teams are divided into two conferences (Eastern and Western), each split into two divisions. Sixteen teams qualify for the playoffs: in each conference, the top three teams from each division qualify directly, and two additional “wild card” teams fill the remaining spots.

Each game must produce a winner. If a game is tied after regulation, it goes to overtime, and then to a shootout if necessary. Games therefore have six possible outcomes from a given team’s perspective: regulation win (RW), overtime win (OTW), shootout win (SOW), shootout loss (SOL), overtime loss (OTL), and regulation loss (RL). Wins award 2 points, overtime/shootout losses award 1 point, and regulation losses award 0 points.

When teams are tied on points, the NHL applies a cascade of seven tie-breakers:

1. Point percentage (that is, fewer games played).
2. Regulation wins.
3. Regulation wins plus Overtime wins.
4. Total wins.
5. Head-to-head points.
6. Goal differential, including shootout-deciding goals.
7. Goals scored, including shootout-deciding goals.

These complex tie-breakers are a major reason why determining playoff clinch scenarios is computationally challenging.

## Our approach

Our solution has two key components: the 0-day solver and the n-day lookahead solver.

**0-day solver:**
The foundation of our approach is a constraint programming (CP) model that answers the question:
*given the current standings, has a team already clinched the playoffs?*

We formulate this as a feasibility problem: can we find outcomes to all remaining games such that the team in question misses the playoffs? If no such scenario exists, the team has clinched. This model is solved using the CP-SAT solver from Google OR-Tools, and accounts for the full complexity of the NHL’s tie-breaking rules.

**n-day lookahead:**
With the 0-day solver in hand, we then ask:
*which outcomes of the games of the next n days would cause a given team to clinch?*

We answer this with a custom tree search, where each layer represents a game that occurs in the next n days, and each node represents a specific outcome of that game (see Figure 1). The tree search calls the 0-day solver at each node to determine if the accumulated outcomes are sufficient for clinching. Preprocessing, pruning strategies, and node-ordering heuristics keep the search tractable.

For example, in Figure 1, the 0-day solver deduces that a team clinches the playoffs with a shootout win (SOW) in their next game, denoted with an ‘X’. That team then also clinches for any stronger result of that game (OTW or RW), as well as for any result of any other relevant game in the next n days. Green shading indicates nodes for which a clinch is proven without explicit evaluation.

![Tree search diagram where a shootout win and stronger results for team k are shaded green as proven playoff clinches](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/04/ML-21367-1.jpg)

Figure 1: Tree search for the n-day lookahead, where green nodes are proven clinches without explicit evaluation

## Results

We validated the clinch scenarios produced by our approach on four NHL regular seasons (2021–22 through 2024–25) using data from the NHL’s public API. All scenarios produced by our system matched exactly with those published by the NHL.

![Box plot of elapsed solve time per date in seconds on a log scale across the 2021-2022 through 2024-2025 NHL seasons](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/04/ML-21367-2.jpg)

Figure 2: Elapsed solve time per date across four NHL seasons

Determining 1-day clinch scenarios required a median runtime on the order of minutes, offering significant speedups over manual approaches (see Figure 2). This efficiency comes from pruning: with the right pre-processing strategies, node ordering heuristics, and inference algorithms, most of the search tree does not need to be explored. In Figure 3, we demonstrate pruning efficiency values near 100% for most instances.

![Box plot of pruning efficiency from 0 to 1 across the 2021-2022 through 2024-2025 NHL seasons, with medians near 1.0](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/08/04/ML-21367-3.jpg)

Figure 3: Pruning efficiency across four NHL seasons

## Practical value

These methods have direct practical applications:

* **For the NHL and media:**
  Automated, provably correct clinching scenarios that can be generated daily without manual effort, yielding significant time savings.
* **For fans:**
  Richer engagement as the postseason approaches, with scenarios that explain exactly what needs to happen for their team to clinch the playoffs.
* **For sports analytics:**
  A rigorous framework that can be extended to other milestones (division titles, elimination, specific seeds) and potentially adapted to other leagues.

This work is part of the broader set of
[mathematical optimization solutions](/blogs/machine-learning/better-decisions-at-scale-how-mathematical-optimization-delivers-where-intuition-fails/)
delivered by AWS to customers across industries. From routing and scheduling to sports analytics, these techniques quickly deliver definitive answers where manual approaches would take significant time, effort, and specialized expertise.

## Conclusion

Determining NHL playoff clinching scenarios is a computationally hard problem. The league’s layered qualification structure and tie-breaking rules create a combinatorial challenge that is difficult to solve manually. Our approach combines constraint programming with custom tree search to crack it efficiently and correctly, validated against four seasons of real NHL data.

The framework is extensible: future work could extend the approach to other clinching and elimination scenarios within the NHL, or adapt it to other sports leagues with different structures and rules.

If you have complex combinatorial problems and want to understand how optimization techniques could apply to your use case, reach out to your account manager to begin exploring with the
[AWS Generative AI Innovation Center](/ai/generative-ai/innovation-center/)
.

---

## About the authors

### Gili Rosenberg

Gili is a Sr. Applied Scientist at the Amazon Advanced Solutions Lab. Prior to joining AWS, Gili co-led the optimization team at 1QBit where he worked as a client-facing senior researcher for over 8 years. Gili has worked on many customer projects, predominantly in finance, materials, and automotives.

### Kyle Booth

Kyle is a Senior Applied Scientist at the Amazon Advanced Solutions Lab. He received his PhD in Operations Research from the University of Toronto. His research focuses on constraint programming and integer programming approaches to combinatorial optimization problems.

### Kyle Brubaker

Kyle was a Principal Applied Scientist at the Amazon Advanced Solutions Lab. He received an MSc in Biomedical Engineering from NYU, focusing on brain machine interfaces. He has an industry background in machine learning and ML engineering. (Affiliated with Amazon at time of contributions.)

### Ruben Andrist

Ruben is a Principal Applied Scientist in the Amazon Advanced Solutions Lab. He received a PhD in theoretical physics from ETH Zurich working on topological quantum error correction. Today his research is focused on quantum computing and heuristic optimization methods.