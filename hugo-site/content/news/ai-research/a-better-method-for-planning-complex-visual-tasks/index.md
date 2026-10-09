---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-11T04:15:40.694499+00:00'
exported_at: '2026-03-11T04:15:42.944704+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/better-method-planning-complex-visual-tasks-0311
structured_data:
  about: []
  author: ''
  description: A new AI-driven system generates plans for long-term, complex tasks
    about twice as well as some existing methods. The technique, developed at MIT,
    uses two vision-language models that work together to simulate actions and produce
    files for formal planning software.
  headline: A better method for planning complex visual tasks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/better-method-planning-complex-visual-tasks-0311
  publisher:
    logo: /favicon.ico
    name: GTCode
title: A better method for planning complex visual tasks
updated_at: '2026-03-11T04:15:40.694499+00:00'
url_hash: 767179d3df4a28a68e1e51c81a4a6efb468a9a11
---

MIT researchers have developed a generative artificial intelligence-driven approach for planning long-term visual tasks, like robot navigation, that is about twice as effective as some existing techniques.

Their method uses a specialized vision-language model to perceive the scenario in an image and simulate actions needed to reach a goal. Then a second model translates those simulations into a standard programming language for planning problems, and refines the solution.

In the end, the system automatically generates a set of files that can be fed into classical planning software, which computes a plan to achieve the goal. This two-step system generated plans with an average success rate of about 70 percent, outperforming the best baseline methods that could only reach about 30 percent.

Importantly, the system can solve new problems it hasn’t encountered before, making it well-suited for real environments where conditions can change at a moment’s notice.

“Our framework combines the advantages of vision-language models, like their ability to understand images, with the strong planning capabilities of a formal solver,” says Yilun Hao, an aeronautics and astronautics (AeroAstro) graduate student at MIT and lead author of an
[open-access paper](https://arxiv.org/pdf/2510.03182)
on this technique. “It can take a single image and move it through simulation and then to a reliable, long-horizon plan that could be useful in many real-life applications.”

She is joined on the paper by Yongchao Chen, a graduate student in the MIT Laboratory for Information and Decision Systems (LIDS); Chuchu Fan, an associate professor in AeroAstro and a principal investigator in LIDS; and Yang Zhang, a research scientist at the MIT-IBM Watson AI Lab. The paper will be presented at the International Conference on Learning Representations.

**Tackling visual tasks**

For the past few years, Fan and her colleagues have studied the use of generative AI models to perform complex reasoning and planning, often employing large language models (LLMs) to process text inputs.

Many real-world planning problems, like robotic assembly and autonomous driving, have visual inputs that an LLM can’t handle well on its own. The researchers sought to expand into the visual domain by utilizing vision-language models (VLMs), powerful AI systems that can process images and text.

But VLMs struggle to understand spatial relationships between objects in a scene and often fail to reason correctly over many steps. This makes it difficult to use VLMs for long-range planning.

On the other hand, scientists have developed robust, formal planners that can generate effective long-horizon plans for complex situations. However, these software systems can’t process visual inputs and require expert knowledge to encode a problem into language the solver can understand.

Fan and her team built an automatic planning system that takes the best of both methods. The system, called VLM-guided formal planning (VLMFP), utilizes two specialized VLMs that work together to turn visual planning problems into ready-to-use files for formal planning software.

The researchers first carefully trained a small model they call SimVLM to specialize in describing the scenario in an image using natural language and simulating a sequence of actions in that scenario. Then a much larger model, which they call GenVLM, uses the description from SimVLM to generate a set of initial files in a formal planning language known as the Planning Domain Definition Language (PDDL).

The files are ready to be fed into a classical PDDL solver, which computes a step-by-step plan to solve the task. GenVLM compares the results of the solver with those of the simulator and iteratively refines the PDDL files.

“The generator and simulator work together to be able to reach the exact same result, which is an action simulation that achieves the goal,” Hao says.

Because GenVLM is a large generative AI model, it has seen many examples of PDDL during training and learned how this formal language can solve a wide range of problems. This existing knowledge enables the model to generate accurate PDDL files.

**A flexible approach**

VLMFP generates two separate PDDL files. The first is a domain file that defines the environment, valid actions, and domain rules. It also produces a problem file that defines the initial states and the goal of a particular problem at hand.

“One advantage of PDDL is the domain file is the same for all instances in that environment. This makes our framework good at generalizing to unseen instances under the same domain,” Hao explains.

To enable the system to generalize effectively, the researchers needed to carefully design just enough training data for SimVLM so the model learned to understand the problem and goal without memorizing patterns in the scenario. When tested, SimVLM successfully described the scenario, simulated actions, and detected if the goal was reached in about 85 percent of experiments.

Overall, the VLMFP framework achieved a success rate of about 60 percent on six 2D planning tasks and greater than 80 percent on two 3D tasks, including multirobot collaboration and robotic assembly. It also generated valid plans for more than 50 percent of scenarios it hadn’t seen before, far outpacing the baseline methods.

“Our framework can generalize when the rules change in different situations. This gives our system the flexibility to solve many types of visual-based planning problems,” Fan adds.

In the future, the researchers want to enable VLMFP to handle more complex scenarios and explore methods to identify and mitigate hallucinations by the VLMs.

“In the long term, generative AI models could act as agents and make use of the right tools to solve much more complicated problems. But what does it mean to have the right tools, and how do we incorporate those tools? There is still a long way to go, but by bringing visual-based planning into the picture, this work is an important piece of the puzzle,” Fan says.

This work was funded, in part, by the MIT-IBM Watson AI Lab.