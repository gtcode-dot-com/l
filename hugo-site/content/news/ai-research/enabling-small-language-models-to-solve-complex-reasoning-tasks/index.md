---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-16T00:03:43.190283+00:00'
exported_at: '2025-12-16T00:03:46.602183+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/enabling-small-language-models-solve-complex-reasoning-tasks-1212
structured_data:
  about: []
  author: ''
  description: MIT CSAIL&#039;s “DisCIPL” uses an LLM to steer smaller language models
    to collaborate on complex reasoning tasks. These less-powerful systems are collectively
    more accurate than leading LLMs, almost as precise as top reasoning models, and
    more efficient than both.
  headline: Enabling small language models to solve complex reasoning tasks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/enabling-small-language-models-solve-complex-reasoning-tasks-1212
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Enabling small language models to solve complex reasoning tasks
updated_at: '2025-12-16T00:03:43.190283+00:00'
url_hash: 3e1377a47f113b60a6a79c09dd30710c5ec57feb
---

As language models (LMs) improve at tasks like image generation, trivia questions, and simple math, you might think that human-like reasoning is around the corner. In reality, they still trail us by a wide margin on complex tasks. Try playing Sudoku with one, for instance, where you fill in numbers one through nine in such a way that each appears only once across the columns, rows, and sections of a nine-by-nine grid. Your AI opponent will either fail to fill in boxes on its own or do so inefficiently, although it can verify if you’ve filled yours out correctly.

Whether an LM is trying to solve advanced puzzles, design molecules, or write math proofs, the system struggles to answer open-ended requests that have strict rules to follow. The model is better at telling users how to approach these challenges than attempting them itself. Moreover, hands-on problem-solving requires LMs to consider a wide range of options while following constraints. Small LMs can’t do this reliably on their own; large language models (LLMs) sometimes can, particularly if they’re optimized for reasoning tasks, but they take a while to respond, and they use a lot of computing power.

This predicament led researchers from MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) to develop a collaborative approach where an LLM does the planning, then divvies up the legwork of that strategy among smaller ones. Their method helps small LMs provide more accurate responses than leading LLMs like OpenAI’s
[GPT-4o](https://openai.com/index/hello-gpt-4o/)
, and approach the precision of top reasoning systems such as
[o1](https://openai.com/o1/)
, while being more efficient than both. Their framework, called “Distributional Constraints by Inference Programming with Language Models” (or “DisCIPL”), has a large model steer smaller “follower” models toward precise responses when writing things like text blurbs, grocery lists with budgets, and travel itineraries.


The inner workings of DisCIPL are much like contracting a company for a particular job. You provide a “boss” model with a request, and it carefully considers how to go about doing that project. Then, the LLM relays these instructions and guidelines in a clear way to smaller models. It corrects follower LMs’ outputs where needed — for example, replacing one model’s phrasing that doesn’t fit in a poem with a better option from another.

The LLM communicates with its followers using a language they all understand — that is, a programming language for controlling LMs called
[“LLaMPPL.”](https://arxiv.org/abs/2306.03081)
Developed by MIT's Probabilistic Computing Project in 2023, this program allows users to encode specific rules that steer a model toward a desired result. For example, LLaMPPL can be used to produce
[error-free code](https://news.mit.edu/2025/making-ai-generated-code-more-accurate-0418)
by incorporating the rules of a particular language within its instructions. Directions like “write eight lines of poetry where each line has exactly eight words” are encoded in LLaMPPL, queuing smaller models to contribute to different parts of the answer.

MIT PhD student Gabriel Grand, who is the lead author on a
[paper](https://openreview.net/pdf?id=XvCBtm5PgF)
presenting this work, says that DisCIPL allows LMs to guide each other toward the best responses, which improves their overall efficiency. “We’re working toward improving LMs’ inference efficiency, particularly on the many modern applications of these models that involve generating outputs subject to constraints,” adds Grand, who is also a CSAIL researcher. “Language models are consuming more energy as people use them more, which means we need models that can provide accurate answers while using minimal computing power.”

“It's really exciting to see new alternatives to standard language model inference,” says University of California at Berkeley Assistant Professor Alane Suhr, who wasn’t involved in the research. “This work invites new approaches to language modeling and LLMs that significantly reduce inference latency via parallelization, require significantly fewer parameters than current LLMs, and even improve task performance over standard serialized inference. The work also presents opportunities to explore transparency, interpretability, and controllability of model outputs, which is still a huge open problem in the deployment of these technologies.”


**An underdog story**


You may think that larger-scale LMs are “better” at complex prompts than smaller ones when it comes to accuracy and efficiency. DisCIPL suggests a surprising counterpoint for these tasks: If you can combine the strengths of smaller models instead, you may just see an efficiency bump with similar results.

The researchers note that, in theory, you can plug in dozens of LMs to work together in the DisCIPL framework, regardless of size. In writing and reasoning experiments, they went with GPT-4o as their “planner LM,” which is one of the models that helps ChatGPT generate responses. It brainstormed a plan for several
[“Llama-3.2-1B”](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/)
models (smaller systems developed by Meta), in which those LMs filled in each word (or token) of the response.

This collective approach competed against three comparable ones: a follower-only baseline powered by Llama-3.2-1B, GPT-4o working on its own, and the industry-leading o1 reasoning system that helps ChatGPT figure out more complex questions, such as coding requests and math problems.


DisCIPL first presented an ability to write sentences and paragraphs that follow explicit rules. The models were given very specific prompts — for example, writing a sentence that has exactly 18 words, where the fourth word must be “Glasgow,” the eighth should be “in”, and the 11th must be “and.” The system was remarkably adept at handling this request, crafting coherent outputs while achieving accuracy and coherence similar to o1.


**Faster, cheaper, better**

This experiment also revealed that key components of DisCIPL were much cheaper than state-of-the-art systems. For instance, whereas existing reasoning models like OpenAI’s o1 perform reasoning in text, DisCIPL “reasons” by writing Python code, which is more compact. In practice, the researchers found that DisCIPL led to 40.1 percent shorter reasoning and 80.2 percent cost savings over o1.

DisCIPL’s efficiency gains stem partly from using small Llama models as followers, which are 1,000 to 10,000 times cheaper per token than comparable reasoning models. This means that DisCIPL is more “scalable” — the researchers were able to run dozens of Llama models in parallel for a fraction of the cost.


Those weren’t the only surprising findings, according to CSAIL researchers. Their system also performed well against o1 on real-world tasks, such as making ingredient lists, planning out a travel itinerary, and writing grant proposals with word limits. Meanwhile, GPT-4o struggled with these requests, and with writing tests, it often couldn’t place keywords in the correct parts of sentences. The follower-only baseline essentially finished in last place across the board, as it had difficulties with following instructions.

“Over the last several years, we’ve seen some impressive results from approaches that use language models to ‘
[auto-formalize](https://news.mit.edu/2024/natural-language-boosts-llm-performance-coding-planning-robotics-0501)
’ problems in math and robotics by representing them with code,” says senior author Jacob Andreas, who is an MIT electrical engineering and computer science associate professor and CSAIL principal investigator. “What I find most exciting about this paper is the fact that we can now use LMs to auto-formalize text generation itself, enabling the same kinds of efficiency gains and guarantees that we’ve seen in these other domains.”

In the future, the researchers plan on expanding this framework into a more fully-recursive approach, where you can use the same model as both the leader and followers. Grand adds that DisCIPL could be extended to mathematical reasoning tasks, where answers are harder to verify. They also intend to test the system on its ability to meet users’ fuzzy preferences, as opposed to following hard constraints, which can’t be outlined in code so explicitly. Thinking even bigger, the team hopes to use the largest possible models available, although they note that such experiments are computationally expensive.

Grand and Andreas wrote the paper alongside CSAIL principal investigator and MIT Professor Joshua Tenenbaum, as well as MIT Department of Brain and Cognitive Sciences Principal Research Scientist Vikash Mansinghka and Yale University Assistant Professor Alex Lew SM ’20 PhD ’25. CSAIL researchers presented the work at the Conference on Language Modeling in October and IVADO’s “Deploying Autonomous Agents: Lessons, Risks and Real-World Impact” workshop in November.


Their work was supported, in part, by the MIT Quest for Intelligence, Siegel Family Foundation, the MIT-IBM Watson AI Lab, a Sloan Research Fellowship, Intel, the Air Force Office of Scientific Research, the Defense Advanced Research Projects Agency, the Office of Naval Research, and the National Science Foundation.