---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T00:15:33.157040+00:00'
exported_at: '2026-02-13T00:15:37.386816+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/helping-ai-agents-search-to-get-best-results-from-llms-0205
structured_data:
  about: []
  author: ''
  description: The EnCompass system runs AI agent programs by backtracking and making
    several attempts, finding an LLM’s best set of outputs. It lets programmers easily
    experiment with different search strategies so they can work with AI agents more
    efficiently. The work was led by researchers at MIT CSAIL and Asari AI.
  headline: Helping AI agents search to get the best results out of large language
    models
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/helping-ai-agents-search-to-get-best-results-from-llms-0205
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Helping AI agents search to get the best results out of large language models
updated_at: '2026-02-13T00:15:33.157040+00:00'
url_hash: a0fb3502cdd1307cb5f32154a10d1d1b602d52e4
---

Whether you’re a scientist brainstorming research ideas or a CEO hoping to automate a task in human resources or finance, you’ll find that artificial intelligence tools are becoming the assistants you didn’t know you needed. In particular, many professionals are
[tapping into the talents](https://www.globenewswire.com/news-release/2025/05/20/3084932/0/en/72-of-professionals-report-using-AI-at-work-compared-to-just-48-in-2024.html)
of semi-autonomous software systems called AI agents, which can call on AI at specific points to solve problems and complete tasks.


AI agents are particularly effective when they use large language models (LLMs) because those systems are powerful, efficient, and adaptable. One way to program such technology is by describing in code what you want your system to do (the “workflow”), including when it should use an LLM. If you were a software company trying to revamp your old codebase to use a more modern programming language for better optimizations and safety, you might build a system that uses an LLM to translate the codebase one file at a time, testing each file as you go.


But what happens when LLMs make mistakes? You’ll want the agent to backtrack to make another attempt, incorporating lessons it learned from previous mistakes. Coding this up can take as much effort as implementing the original agent; if your system for translating a codebase contained thousands of lines of code, then you’d be making thousands of lines of code changes or additions to support the logic for backtracking when LLMs make mistakes.

To save programmers time and effort, researchers with MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) and Asari AI have
[developed a framework called “EnCompass.”](https://arxiv.org/pdf/2512.03571)

With EnCompass, you no longer have to make these changes yourself. Instead, when EnCompass runs your program, it automatically backtracks if LLMs make mistakes. EnCompass can also make clones of the program runtime to make multiple attempts in parallel in search of the best solution. In full generality, EnCompass searches over the different possible paths your agent could take as a result of the different possible outputs of all the LLM calls, looking for the path where the LLM finds the best solution.


Then, all you have to do is to annotate the locations where you may want to backtrack or clone the program runtime, as well as record any information that may be useful to the strategy used to search over the different possible execution paths of your agent (the search strategy). You can then separately specify the search strategy — you could either use one that EnCompass provides out of the box or, if desired, implement your own custom search strategy.

“With EnCompass, we’ve separated the search strategy from the underlying workflow of an AI agent,” says lead author Zhening Li ’25, MEng ’25, who is an MIT electrical engineering and computer science (EECS) PhD student, CSAIL researcher, and research consultant at Asari AI. “Our framework lets programmers easily experiment with different search strategies to find the one that makes the AI agent perform the best.”


EnCompass was used for agents implemented as Python programs that call LLMs, where it demonstrated noticeable code savings. EnCompass reduced coding effort for implementing search by up to 80 percent across agents, such as an agent for translating code repositories and for discovering transformation rules of digital grids. In the future, EnCompass could enable agents to tackle large-scale tasks, including managing massive code libraries, designing and carrying out science experiments, and creating blueprints for rockets and other hardware.

**Branching out**

When programming your agent, you mark particular operations — such as calls to an LLM — where results may vary. These annotations are called “branchpoints.” If you imagine your agent program as generating a single plot line of a story, then adding branchpoints turns the story into a choose-your-own-adventure story game, where branchpoints are locations where the plot branches into multiple future plot lines.

You can then specify the strategy that EnCompass uses to navigate that story game, in search of the best possible ending to the story. This can include launching parallel threads of execution or backtracking to a previous branchpoint when you get stuck in a dead end.


Users can also plug-and-play a few common search strategies provided by EnCompass out of the box, or define their own custom strategy. For example, you could opt for Monte Carlo tree search, which builds a search tree by balancing exploration and exploitation, or beam search, which keeps the best few outputs from every step. EnCompass makes it easy to experiment with different approaches to find the best strategy to maximize the likelihood of successfully completing your task.

**The coding efficiency of EnCompass**

So just how code-efficient is EnCompass for adding search to agent programs? According to researchers’ findings, the framework drastically cut down how much programmers needed to add to their agent programs to add search, helping them experiment with different strategies to find the one that performs the best.


For example, the researchers applied EnCompass to an agent that translates a repository of code from the Java programming language, which is commonly used to program apps and enterprise software, to Python. They found that implementing search with EnCompass — mainly involving adding branchpoint annotations and annotations that record how well each step did — required 348 fewer lines of code (about 82 percent) than implementing it by hand. They also demonstrated how EnCompass enabled them to easily try out different search strategies, identifying the best strategy to be a two-level beam search algorithm, achieving an accuracy boost of 15 to 40 percent across five different repositories at a search budget of 16 times the LLM calls made by the agent without search.

“As LLMs become a more integral part of everyday software, it becomes more important to understand how to efficiently build software that leverages their strengths and works around their limitations,” says co-author Armando Solar-Lezama, who is an MIT professor of EECS and CSAIL principal investigator. “EnCompass is an important step in that direction.”

The researchers add that EnCompass targets agents where a program specifies the steps of the high-level workflow; the current iteration of their framework is less applicable to agents that are entirely controlled by an LLM. “In those agents, instead of having a program that specifies the steps and then using an LLM to carry out those steps, the LLM itself decides everything,” says Li. “There is no underlying programmatic workflow, so you can execute inference-time search on whatever the LLM invents on the fly. In this case, there’s less need for a tool like EnCompass that modifies how a program executes with search and backtracking.”

Li and his colleagues plan to extend EnCompass to more general search frameworks for AI agents. They also plan to test their system on more complex tasks to refine it for real-world uses, including at companies. What’s more, they’re evaluating how well EnCompass helps agents work with humans on tasks like brainstorming hardware designs or translating much larger code libraries. For now, EnCompass is a powerful building block that enables humans to tinker with AI agents more easily, improving their performance.

“EnCompass arrives at a timely moment, as AI-driven agents and search-based techniques are beginning to reshape workflows in software engineering,” says Carnegie Mellon University Professor Yiming Yang, who wasn’t involved in the research. “By cleanly separating an agent’s programming logic from its inference-time search strategy, the framework offers a principled way to explore how structured search can enhance code generation, translation, and analysis. This abstraction provides a solid foundation for more systematic and reliable search-driven approaches to software development.”

Li and Solar-Lezama wrote the paper with two Asari AI researchers: Caltech Professor Yisong Yue, an advisor at the company; and senior author Stephan Zheng, who is the founder and CEO. Their work was supported by Asari AI.


The team’s work was presented at the Conference on Neural Information Processing Systems (NeurIPS) in December.