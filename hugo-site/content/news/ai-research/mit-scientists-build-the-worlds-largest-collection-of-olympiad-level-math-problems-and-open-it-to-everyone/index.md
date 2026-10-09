---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-24T20:15:36.855462+00:00'
exported_at: '2026-04-24T20:15:38.997565+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/mit-scientists-build-worlds-largest-collection-olympiad-level-math-problems-open-0424
structured_data:
  about: []
  author: ''
  description: MIT CSAIL scientists have compiled the largest high-quality dataset
    of proof-based math problems ever created. It can help researchers test AI models’
    mathematical reasoning, while capturing the full range of mathematical perspectives
    and problem-solving traditions within the global math community.
  headline: MIT scientists build the world’s largest collection of Olympiad-level
    math problems, and open it to everyone
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/mit-scientists-build-worlds-largest-collection-olympiad-level-math-problems-open-0424
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MIT scientists build the world’s largest collection of Olympiad-level math
  problems, and open it to everyone
updated_at: '2026-04-24T20:15:36.855462+00:00'
url_hash: 44298595d321096ca8321ee7c4b6cba98fe13031
---

Every year, the countries competing in the International Mathematical Olympiad (IMO) arrive with a booklet of their best, most original problems. Those booklets get shared among delegations, then quietly disappear. No one had ever collected them systematically, cleaned them, and made them available, not for AI researchers testing the limits of mathematical reasoning, and not for the students around the world training for these competitions largely on their own.

Researchers at MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL), King Abdullah University of Science and Technology (KAUST), and the company HUMAIN have now done exactly that.

MathNet is the largest high-quality dataset of proof-based math problems ever created. Comprising more than 30,000 expert-authored problems and solutions spanning 47 countries, 17 languages, and 143 competitions, it is five times larger than the next-biggest dataset of its kind. The work will be presented at the International Conference on Learning Representations (ICLR) in Brazil later this month.

What makes MathNet different is not only its size, but its breadth. Previous Olympiad-level datasets draw almost exclusively from competitions in the United States and China. MathNet spans dozens of countries across six continents, covers 17 languages, includes both text- and image-based problems and solutions, and spans four decades of competition mathematics. The goal is to capture the full range of mathematical perspectives and problem-solving traditions that exist across the global math community, not just the most visible ones.

"Every country brings a booklet of its most novel and most creative problems," says Shaden Alshammari, an MIT PhD student and lead author on the paper. "They share the booklets with each other, but no one had made the effort to collect them, clean them, and upload them online."

Building MathNet required tracking down 1,595 PDF volumes totaling more than 25,000 pages, spanning digital documents and decades-old scans in more than a dozen languages. A significant portion of that archive came from an unlikely source: Navid Safaei, a longtime IMO community figure and co-author who had been collecting and scanning those booklets by hand since 2006. His personal archive formed much of the backbone of the dataset.

The sourcing matters as much as the scale. Where most existing math datasets pull problems from community forums like Art of Problem Solving (AoPS), MathNet draws exclusively from official national competition booklets. The solutions in those booklets are expert-written and peer-reviewed, and they often run to multiple pages, with authors walking through several approaches to the same problem. That depth gives AI models a far richer signal for learning mathematical reasoning than the shorter, informal solutions typical of community-sourced datasets. It also means the dataset is genuinely useful for students: Anyone preparing for the IMO or a national competition now has access to a centralized, searchable collection of high-quality problems and worked solutions from traditions around the world.

"I remember so many students for whom it was an individual effort. No one in their country was training them for this kind of competition," says Alshammari, who competed in the IMO as a student herself. "We hope this gives them a centralized place with high-quality problems and solutions to learn from."

The team has deep roots in the IMO community. Sultan Albarakati, a co-author, currently serves on the IMO board, and the researchers are working to share the dataset with the IMO foundation directly. To validate the dataset, they assembled a grading group of more than 30 human evaluators from countries including Armenia, Russia, Ukraine, Vietnam, and Poland, who coordinated together to verify thousands of solutions.

"The MathNet database has the potential to be an excellent resource for both students and leaders seeking new problems to work on or looking for the solution to a difficult question," says Tanish Patil, deputy leader of Switzerland's IMO. "Whilst other archives of Olympiad problems do exist (notably, the Contest Collections forums on AoPS), these resources lack standardized formatting system, verified solutions, and important problem metadata that topics and theory require. It will also be interesting to see how this dataset is used to improve the performance of reasoning models, and if we will soon be able to reliably answer an important issue when creating novel Olympiad questions: determining if a problem is truly original."

MathNet also functions as a rigorous benchmark for AI performance, and the results reveal a more complicated picture than recent headlines about AI math prowess might suggest. Frontier models have made extraordinary progress: Some have reportedly achieved gold-medal performance at the IMO, and on standard benchmarks they now solve problems that would stump most humans. But MathNet shows that progress is uneven. Even GPT-5, the top-performing model tested, averaged around 69.3 percent on MathNet's main benchmark of 6,400 problems, failing nearly one-in-three Olympiad-level problems. And when problems include figures, performance drops significantly across the board, exposing visual reasoning as a consistent weak point for even the most capable models.

Several open-source models scored 0 percent on Mongolian-language problems, highlighting another dimension where current AI systems fall short despite their overall strength.

"GPT models are equally good in English and other languages," Alshammari says. "But many of the open-source models fail completely at less-common languages, such as Mongolian."

The diversity of MathNet is also designed to address a deeper limitation in how AI models learn mathematics. When training data skews toward English and Chinese problems, models absorb a narrow slice of mathematical culture. A Romanian combinatorics problem or a Brazilian number theory problem may approach the same underlying concept from a completely different angle. Exposure to that range, the researchers argue, makes both humans and AI systems better mathematical thinkers.

Beyond problem-solving, MathNet introduces a retrieval benchmark that asks whether models can recognize when two problems share the same underlying mathematical structure, a capability that matters both for AI development and for the math community itself. Near-duplicate problems have appeared in real IMO exams over the years because finding mathematical equivalences across different notations, languages, and formats is genuinely hard, even for expert human committees. Testing eight state-of-the-art embedding models, the researchers found that even the strongest identified the correct match only about 5 percent of the time on the first try, with models frequently ranking structurally unrelated problems as more similar than equivalent ones.

The dataset also includes a retrieval-augmented generation benchmark, testing whether giving a model a structurally related problem before asking it to solve a new one improves performance. It does, but only when the retrieved problem is genuinely relevant. DeepSeek-V3.2-Speciale gained up to 12 percentage points with well-matched retrieval, while irrelevant retrieval degraded performance in roughly 22 percent of cases.

Alshammari wrote the paper with Safaei, HUMAIN AI engineer Abrar Zainal, KAUST Academy Director Sultan Albarakati, and MIT CSAIL colleagues: master's student Kevin Wen SB ’25; Microsoft Principal Engineering Manager Mark Hamilton SM ’22, PhD ‘25; and professors William Freeman and Antonio Torralba. Their work was funded, in part, by the Schwarzman College of Computing Fellowship and the National Science Foundation.


MathNet is publicly available at
[mathnet.csail.mit.edu](https://mathnet.csail.mit.edu)
.