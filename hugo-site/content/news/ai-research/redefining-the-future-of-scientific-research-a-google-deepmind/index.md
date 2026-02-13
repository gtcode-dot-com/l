---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T00:15:34.451533+00:00'
exported_at: '2026-02-13T00:15:37.382054+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think
structured_data:
  about: []
  author: ''
  description: Gemini Deep Think is accelerating discovery in maths, physics, and
    computer science by acting as a powerful scientific companion for researchers.
  headline: Accelerating Mathematical and Scientific Discovery with Gemini Deep Think
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/accelerating-mathematical-and-scientific-discovery-with-gemini-deep-think
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Accelerating Mathematical and Scientific Discovery with Gemini Deep Think
updated_at: '2026-02-13T00:15:34.451533+00:00'
url_hash: 3880f3dbfc7cf38e76a39e1e58c63463ade5bc69
---

Collaborating with experts on 18 research problems, an advanced version of Gemini Deep Think helped resolve long-standing bottlenecks across algorithms, ML and combinatorial optimization, information theory, and economics. Highlights from our
[âAccelerating Research with Geminiâ paper](http://arxiv.org/abs/2602.03837)
include (corresponding section numbers in paper):

1. **Crossing mathematical borders for network puzzles**
   : Progress on classic computer science problems like "Max-Cut" (efficiently splitting networks) and the "Steiner Tree" (connecting high-dimensional points) had slowed down. Gemini broke both deadlocks by thinking outside the box. It solved these discrete algorithmic puzzles by pulling advanced toolsâlike the Kirszbraun Theorem, measure theory, and the Stone-Weierstrass theoremâfrom entirely unrelated branches of continuous mathematics. See
   [Sections 4.1 and 4.2.](https://arxiv.org/pdf/2602.03837)
2. **Settling a decade-old conjecture in online submodular optimization**
   : A
   [2015 theory paper](https://research.google/pubs/online-submodular-welfare-maximization-greedy-beats-12-in-random-order/)
   proposed a seemingly obvious rule for data streams: making a copy of an arriving item is always less valuable than simply moving the original. Experts struggled for a decade to prove this. Gemini engineered a highly specific three-item combinatorial counterexample, rigorously proving the long-standing human intuition false. See
   [Section 3.1](https://arxiv.org/pdf/2602.03837)
   .
3. **Machine learning optimization:**
   Training AI to filter out noise usually requires engineers to manually tune a mathematical "penalty." Researchers created a new technique that did this automatically, but couldn't mathematically explain why. Gemini analyzed the equations and proved the method succeeds by secretly generating its own "adaptive penalty" on the fly. See
   [Section 8.3](https://arxiv.org/pdf/2602.03837)
   .
4. **Upgrading economic theory for AI:**
   A recent 'Revelation Principle' for auctioning AI generation tokens only worked mathematically when bids were restricted to rational numbers. Extending the domain to continuous real numbers invalidated the original proof. Gemini employed advanced topology and order theory to extend the theorem, accommodating real-world, continuous auction dynamics. See
   [Section 8.4](https://arxiv.org/pdf/2602.03837)
   .
5. **Physics of cosmic strings:**
   Calculating gravitational radiation from cosmic strings requires finding analytical solutions to tricky integrals containing "singularities." Gemini found a novel solution using Gegenbauer polynomials. This naturally absorbed the singularities, collapsing an infinite series into a closed form, finite sum. See
   [Section 6.1](https://arxiv.org/pdf/2602.03837)
   .

Spanning diverse fieldsâfrom information and complexity theory to cryptography and mechanism designâthe results demonstrate how AI is fundamentally shifting research. For details, see
[our paper](https://arxiv.org/pdf/2602.03837)
.

Given computer science's fluid, conference-driven publication pipeline, we describe these results by academic trajectory rather than a rigid taxonomy. About half target strong conferencesâincluding an ICLR â26 acceptanceâwhile most remaining findings will form future journal submissions. Even when course-correcting the field by identifying errors (
[Section 3.2](https://arxiv.org/pdf/2602.03837)
) or refuting conjectures (
[Section 3.1](https://arxiv.org/pdf/2602.03837)
), these outcomes highlight AIâs value as a high-level scientific collaborator.

## The Future of Human-AI Collaboration

Building on Googleâs previous breakthroughs (
[1](https://deepmind.google/blog/exploring-the-beauty-of-pure-mathematics-in-novel-ways/)
,
[2](https://deepmind.google/blog/funsearch-making-new-discoveries-in-mathematical-sciences-using-large-language-models/)
,
[3](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)
,
[4](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
,
[5](https://research.google/blog/gemini-provides-automated-feedback-for-theoretical-computer-scientists-at-stoc-2026/)
), this work demonstrates that general foundation models - leveraged with agentic reasoning workflows - can act as a powerful scientific companion.

Under direction from expert mathematicians, physicists, and computer scientists, Gemini Deep Think mode is proving its utility across fields where complex math, logic and reasoning are core.

We are witnessing a fundamental shift in the scientific workflow. As Gemini evolves, it acts as "force multiplier" for human intellect, handling knowledge retrieval and rigorous verification so scientists can focus on conceptual depth and creative direction. Whether refining proofs, hunting for counterexamples, or linking disconnected fields, AI is becoming a valuable collaborator in the next chapter of scientific progress.

## Acknowledgements

We thank the community of expert mathematicians, physicists, and computer scientists for their help and advice on this project

This project was a large-scale collaboration across Google and its success is due to the combined efforts of many individuals and teams. Thang Luong and Vahab Mirrokni led the overall research directions with deep technical expertises from Tony Feng and David Woodruff.

Authors of the first paper âTowards Autonomous Mathematics Researchâ include: Tony Feng, Trieu H. Trinh, Garrett Bingham, Dawsen Hwang, Yuri Chervonyi, Junehyuk Jung, Joonkyung Lee, Carlo Pagano, Sang-hyun Kim, Federico Pasqualotto, Sergei Gukov, Jonathan N. Lee, Junsu Kim, Kaiying Hou, Golnaz Ghiasi, Yi Tay, YaGuang Li, Chenkai Kuang, Yuan Liu, Hanzhao (Maggie) Lin, Evan Zheran Liu, Nigamaa Nayakanti, Xiaomeng Yang, Heng-Tze Cheng, Demis Hassabis, Koray Kavukcuoglu, Quoc V. Le, Thang Luong. We thank the following experts for feedback and discussions on the work: ââJarod Alper, Kevin Barreto, Thomas Bloom, Sourav Chatterjee, Otis Chodosh, Michael Hutchings, Seongbin Jeon, Youngbeom Jin, Aiden Yuchan Jung, Jiwon Kang, Jimin Kim, Vjekoslav KovaÄ, Daniel Litt, Ciprian Manolescu, Mona Merling, Agustin Moreno, Carl Schildkraut, Johannes Schmitt, Insuk Seo, Jaehyeon Seo, Terence Tao, Cheng-Chiang Tsai, Ravi Vakil, Zhiwei Yun, Shengtong Zhang, Wei Zhang, Yufei Zhao.

Authors of the second paper âAccelerating Scientific Research with Gemini: Case Studies and Common Techniquesâ include David P. Woodruff, Vincent Cohen-Addad, Lalit Jain, Jieming Mao, Song Zuo, MohammadHossein Bateni, Simina Branzei, Michael P. Brenner, Lin Chen, Ying Feng, Lance Fortnow, Gang Fu, Ziyi Guan, Zahra Hadizadeh, Mohammad T. Hajiaghayi, Mahdi JafariRaviz, Adel Javanmard, Karthik C. S., Ken-ichi Kawarabayashi, Ravi Kumar, Silvio Lattanzi, Euiwoong Lee, Yi Li, Ioannis Panageas, Dimitris Paparas, Benjamin Przybocki, Bernardo Subercaseaux, Ola Svensson, Shayan Taherijam, Xuan Wu, Eylon Yogev, Morteza Zadimoghaddam, Samson Zhou, Yossi Matias, Jeff Dean, James Manyika, Vahab Mirrokni. This list includes Google researchers building the agentic reasoning on top of Gemini, and our academic expert collaborators verifying and collaborating with Gemini. We also thank Corinna Cortes for her careful review of the paper.

We are grateful for the foundational support from the rest of the DeepThink team: Anirudh Baddepudi, Michael Brenner, Irene Cai, Kristen Chiafullo, Paul Covington, Rumen Dangovski, Chenjie Gu, Huan Gui, Vihan Jain, Rajesh Jayaram, Melvin Johnson, Rosemary Ke, Maciej Kula, Nate Kushman, Jane Labanowski, Steve Li, Pol Moreno, Sidharth Mudgal, William Nelson, ââAda Maksutaj Oflazer, Sahitya Potluri, Navneet Potti, Shubha Raghvendra, Siamak Shakeri, Archit Sharma, Xinying Song, Mukund Sundararajan, Qijun Tan, Zak Tsai, Theophane Weber, Winnie Xu, Zicheng Xu, Junwen Yao, Shunyu Yao, Adams Yu, Lijun Yu, and Honglei Zhuang.

We thank Quoc Le, Koray Kavukcuoglu, Demis Hassabis, James Manyika, Yossi Matias, and Jeff Dean for sponsoring this project.

Last but not least, we thank Divy Thakkar, Adam Brown, Vinay Ramasesh, Alex Davies, Thomas Hubert, EugÃ©nie Rives, Pushmeet Kohli, Benoit Schillings for feedback and support of the project.