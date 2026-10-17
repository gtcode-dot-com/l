---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-17T22:10:49.704673+00:00'
exported_at: '2026-10-17T22:10:52.801008+00:00'
feed: http://bair.berkeley.edu/blog/feed.xml
language: en
source_url: http://bair.berkeley.edu/blog/2026/07/26/abbel
structured_data:
  about: []
  author: ''
  description: The BAIR Blog
  headline: Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://bair.berkeley.edu/blog/2026/07/26/abbel
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Teaching LLMs to Update Beliefs for Efficient Long-Horizon Interaction
updated_at: '2026-10-17T22:10:49.704673+00:00'
url_hash: 81a2e769e89fad81a669e731049475a312872729
---

![ABBEL overview](https://bair.berkeley.edu/static/blog/abbel/ABBEL%20main%20figure.png)
*Overview of ABBEL compared to traditional recursive summarization. Beliefs replace the full interaction history as the agentâs working context, and belief grading improves performance by
supervising the contents of each belief state..*

As task horizons grow, LLM contexts canât scale forever. Self-summarization enables concise, interpretable contexts, but at a significant performance cost, especially for human assistance domains where high quality data is scarce, e.g., collaborative code generation. We address this with
[ABBEL](https://arxiv.org/abs/2512.20111)
: a framework that isolates and supervises the information content of summaries in the form of natural-language belief states.

## Motivation: the cost of recursive summarization

For language models to effectively assist with increasingly complex tasks such as software development, they must be able to interact with us over hundreds or even thousands of steps. For such long tasks, it is impractical to keep the history of the entire interaction in context. The heuristic approach used so far has been summary generation, sometimes called context compaction. For example, Cursorâs latest model composer 2.5 uses compaction during training for improved performance (
[Cassano et al., 2026](https://cursor.com/blog/self-summarization)
). Alongside composer, Grandcode (
[DeepReinforce et al., 2026](https://arxiv.org/abs/2604.02721)
), the first system to consistently beat all human competitors in online coding competitions, despite using one of the newest efficient attention models (Qwen 3.5-397B),
still found it necessary to employ context summarization.

But compaction has a problem. Despite seemingly low performance gaps in benchmarks, model servers like Cursor continue to recommend that users avoid compaction with their coding assistants in the middle of a task (
[Heule et al., 2026](https://cursor.com/blog/continually-improving-agent-harness)
).

To understand why, see below the performance over RL fine-tuning of a Context summary model compared to full context models in Combination Lock, a Wordle-like game that allows up to 16 guesses.
Though both model types improve over the course of training, the summary model never closes the gap.

![Average attempts to guess target word with context summary vs full context policies over training](https://bair.berkeley.edu/static/blog/abbel/Average%20attempts%20to%20guess%20target%20word%20context%20summaries.png)
*Fig. 1: Average attempts to guess the target word on Combination Lock over RL fine-tuning (lower is better). Context-summary policies improve with training but do not close the gap to full-context policies.*

Making models self-summarize while completing a task increases the complexity of the learning problem. While this could typically be addressed by training with more data, the performance degradation observed in real world interactive settings likely arises from the difficulty we have in creating and using human simulators effectively to generate high quality training environments (
[Lin et al., 2025](https://jessylin.com/2025/07/10/user-simulators-1/)
,
[Tomlin et al., 2025](https://nickatomlin.github.io/blog/user-simulators-2.html)
). Thus, the better you can learn to summarize on the limited and messy multiturn interaction trajectories you can collect, the better off your model will be for downstream users.

## ABBEL: acting through belief bottlenecks

![ABBEL belief grading diagram](https://bair.berkeley.edu/static/blog/abbel/ABBEL%20belief%20grading%20diagram.png)
*Fig. 2: Autoencoder-inspired belief grading. The model encodes prior belief, action and observation (b
t
, a
t
, o
t
) into posterior belief b
t+1
and is rewarded for how well select information from the history can be reconstructed from that belief.*

To address poor learning efficiency, we isolate the summary generation task. Drawing inspiration from recursive Bayesian estimation, we formulate summaries as belief states, which we periodically prompt the model to update based on new information.

â¹ Prev

Pause

Next âº

1 / 16

*Fig. 3: ABBEL rollout. Belief updates from the latest observation alternate with action selection conditioned only on the current posterior belief.*

### Belief grading

We then extract and supervise the contents of the belief states (Fig. 2, Belief Grading). Belief grading can be thought of as adding an auxiliary RL task, using heuristics designed to capture what makes a good belief as the reward. An example heuristic for coding could be shorter is better, but closer to being able to reconstruct the git diff is also better, so balancing these would yield a good belief. In domains where good heuristics are hard to define, we propose a general autoencoding-inspired grading function, which treats the current language model Ï
Î¸
as both encoder and decoder of information from
the history, and the belief states as the codes. We grade each belief b
t+1
by how well it can be used by the current model Ï
Î¸
to reconstruct the most recent observation o
t
:

![Eq. 1: Reconstruction grading objective](https://bair.berkeley.edu/static/blog/abbel/Belief%20grading%20equation.png)
*Eq. 1: Reconstruction grading objective. Here b
t+1
is the updated belief, o
t
the latest observation, a
t
the action just taken, b
t
the prior belief, p
I
the task prompt, and Ï
Î¸
the current model. Higher grades reward beliefs that retain information needed to decode the latest observation.*

## What do we gain by grading beliefs?

### Collaborative coding on CollabBench

We demonstrate the utility of belief grading in our motivating domain of human-driven assistive coding, with the CollabBench environment from Sweet-RL (
[Zhou et al., 2025](https://arxiv.org/pdf/2503.15478)
).

![CollabBench collaborative coding environment](https://bair.berkeley.edu/static/blog/abbel/Collabbench.png)
*Fig. 4: CollabBench collaborative coding environment. The agent asks clarifying questions, then submits a function scored against hidden unit tests.*

We see that with the general reconstruction-based belief grading function we reduce the performance gap from full context models by about 50%, and train in 50% fewer steps compared to training models to summarize without belief grading (no BG). After training, ABBEL still uses significantly less memory than the full context setting, as measured by the peak context token length (Peak Tokens).

| Model | Test Pass Rate â | Success Rate â | Peak Tokens Ã 10Â² â | Training Steps â |
| --- | --- | --- | --- | --- |
| Full Context | 0.52Â±0.02 | 0.39Â±0.02 | 14.08Â±0.55 | 100 |
| ABBEL (no BG) | 0.46Â±0.02 | 0.31Â±0.02 | 4.20Â±0.37 | 100 |
| ABBEL-rec-BG | 0.48Â±0.01 | 0.36Â±0.01 | 6.01Â±0.33 | 50 |

*Fig. 5: CollabBench results. With reconstruction belief grading, ABBEL-rec-BG recovers about half the gap to full context while using fewer peak tokens, and trains in 50 steps instead of 100.*

### Combination Lock

Additionally, in CombinationLock, we demonstrate that ABBEL with a belief grader which leverages domain knowledge (by computing useful statistics over the history and checking that they can be reconstructed from the belief state), enables even higher learning efficiency than full context (FULL CTX) models.

![Average Attempts to guess target word ABBEL](https://bair.berkeley.edu/static/blog/abbel/Average%20Attempts%20to%20guess%20target%20word%20ABBEL.png)
*Fig. 6: Average attempts to guess the target word on Combination Lock (lower is better). With domain-knowledge belief grading, ABBEL approaches or exceeds FULL CTX in this setting; without belief grading, learning is slower.*

### Multi-objective question answering

In a third environment, multi-objective question answering (from MEM1
[Zhang et al., 2025](https://arxiv.org/pdf/2512.24601)
, a recent work which performed end-to-end optimization in a modified version of typical recursive summarization), we demonstrate the utility of isolating belief states from reasoning, by showing that a Peak Belief length Penalty (more details in paper) significantly reduces memory usage with minimal performance degradation, unlike is commonly observed when penalizing reasoning lengths (
[Arora et al., 2025](https://proceedings.neurips.cc/paper_files/paper/2025/file/579b5b84311e122584dedab1d3b7613f-Paper-Conference.pdf)
).

![Performance and memory usage in multi QA](https://bair.berkeley.edu/static/blog/abbel/Performance%20and%20memory%20usage%20in%20multi%20QA.png)
*Fig. 7: Exact-match score and peak memory versus number of objectives in multi-objective QA. ABBEL with a peak belief penalty (PBP) maintains comparable performance while using less memory than MEM1 and ABBEL without PBP in this evaluation.*

Alternative solutions to managing long contexts involve different tradeoffs, and are worth considering depending on the requirements of a deployed system. Context compression methods generate dense representations which, while computationally efficient, sacrifice human-understandability (
[Kontonis et al., 2026](https://arxiv.org/abs/2604.09852)
,
[Eyuboglu et al., 2025](https://arxiv.org/pdf/2506.06266)
,
[Gupta et al., 2025](https://arxiv.org/pdf/2510.19732)
,
[Chevalier et al., 2023](https://arxiv.org/pdf/2305.14788)
,
[Deng et al., 2025](https://aclanthology.org/2025.acl-long.241.pdf)
,
[Deng et al., 2025](https://proceedings.neurips.cc/paper_files/paper/2025/file/1c93b738747776f9d3fdd077a5a07114-Paper-Conference.pdf)
,
[Bulatov et al., 2022](https://arxiv.org/abs/2207.06881)
). Hand-designed summarization prompts (
[Wang et al., 2025](https://arxiv.org/pdf/2407.16741)
,
[Ãrwall et al., 2025](https://github.com/aorwall/moatless-tools)
,
[Starace et al., 2025](https://arxiv.org/pdf/2504.01848)
) and pruning strategies (
[Jiang et al., 2024](https://arxiv.org/pdf/2310.06839)
) specific to target environments require expert human knowledge and donât allow an agent to learn what to remember as part of its decision-making strategy. Methods that process long contexts into an external memory store (
[Packer et al., 2023](https://arxiv.org/pdf/2310.08560)
,
[Xu et al., 2025](https://arxiv.org/pdf/2502.12110)
) for the agents or subagents to query (
[Zhang et al., 2025](https://arxiv.org/pdf/2512.24601)
) are complementary, as they may benefit from better next context creation through summarization training. We would like to point out some exciting works in the space of general recursive summarization focused on math (
[Wu et al., 2026](https://arxiv.org/pdf/2602.03773)
), reasoning with belief generation (
[Zhou et al., 2025](https://arxiv.org/pdf/2506.15841)
), competitive coding with a distilled summarization module using similar autoencoding objectives to our general belief grader (
[DeepReinforce et al., 2026](https://arxiv.org/abs/2604.02721)
), and adding continuous features to summaries (
[Kontonis et al., 2026](https://arxiv.org/abs/2604.09852)
).

## Whatâs next for better memory?

Many more possibilities are enabled through using explicit belief states as information bottlenecks for multi-step interaction. You could reward actions based on their effect on the belief state to guide exploration, transmit the explicit belief states for better communication between agents, or even improve user controllability by directly modifying the memories on which the agentsâ decisions are based.

Some forms of information, e.g., what a person looks like, are not represented well by text alone. A continuously learning system will also have to capture such information. Additionally, if we want a system to learn to communicate in a brand new language or to play a brand new game better than any person in the world, the skills accumulated over the lifetime of conversations or games must be stored in a very compressed form, essentially taking on the role of the weights of the model itself.

More powerful systems will likely utilize a combination of multiple forms of memory, where the contents of the context may correspond to working memory while other approaches are used for short and long-term memory. How to instantiate these other forms of memory, for instance via test-time training, adapter memories, continuous context memories, or some combination thereof, presents an exciting challenge.

## Acknowledgements

Acknowledgements: We would like to thank
[Alane Suhr](https://www.alanesuhr.com/)
and
[Kartik Goyal](https://kartikgo.github.io/)
for advising this research as well as
[Ethan Mendes](https://ethanm88.github.io/)
,
[David He](https://davidhe137.github.io/)
,
[Jitesh Jain](https://praeclarumjj3.github.io/)
, and
[Nicholas Tomlin](https://nickatomlin.github.io/)
for comments on early drafts of this post. We would like to thank the MEM1 authors for their email correspondence and for sharing private reviewer feedback which we found particularly insightful.

---

## Citation

If abbel was inspiring for your future work, please cite us with this! And here is some
[advice](https://jakob-bjorner.github.io/abbel-advice.html)
for doing similar research!

```
@misc{lidayan2026abbellearningnaturallanguagebelief,
      title={ABBEL: Learning Natural-Language Belief States for Memory-Efficient Interaction},
      author={Aly Lidayan and Jakob Bjorner and Satvik Golechha and Kartik Goyal and Alane Suhr},
      year={2026},
      eprint={2512.20111},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.20111},
}
```

---



---