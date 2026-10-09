---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-27T04:07:20.150983+00:00'
exported_at: '2026-06-27T04:07:22.258008+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/llms-help-robots-understand-vague-instructions-and-focus-key-details-0626
structured_data:
  about: []
  author: ''
  description: MIT CSAIL&#039;s “Masked IRL” algorithm helps a robot understand ambiguous
    instructions so it does chores safely. An LLM first elaborates on users&#039;
    prompts based on demonstration data, then another narrows down which details an
    algorithm should incorporate into a motion plan.
  headline: LLMs help robots understand vague instructions and focus on key details
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/llms-help-robots-understand-vague-instructions-and-focus-key-details-0626
  publisher:
    logo: /favicon.ico
    name: GTCode
title: LLMs help robots understand vague instructions and focus on key details
updated_at: '2026-06-27T04:07:20.150983+00:00'
url_hash: 58b19a63fcfa8078a88049a9b3aa41ff57838915
---

Imagine working at a warehouse or office sometime in the near future, and you’re asked to help a new trainee learn the basics of their job. The catch: It’s a robot. To teach them, you might want to play a game of “show and tell” — that is, physically showing how to do something a few different ways, while also explaining what you’re doing.

Let’s say you asked the robot to place some coffee on your desk without disturbing you during a Zoom call. You’ll prefer that the robot doesn’t get too close to you and the laptop so that it doesn’t interrupt your meeting. To enable this behavior, the robot should be trained with data that clearly demonstrates the full task. Computer scientists have attempted to explain manipulation tasks to robots by recording lots of physical demonstrations or writing extensive directions. But if you don’t have both, the machine is likely to misunderstand what it needs to do.


It’s laborious for humans to do all that showing and telling, so researchers at MIT’s Computer Science and Artificial Intelligence Laboratory (CSAIL) have automated the process of teaching a robot, while clarifying instructions automatically and using nearly five times less demonstration data. Their “Masked Inverse Reinforcement Learning” (Masked IRL) approach uses a large language model (LLM) to elaborate on ambiguous prompts based on the data collected from a user’s demo. Another LLM then narrows down which details an algorithm should incorporate into a motion plan, so that a robot can safely complete chores in homes, offices, and factories.


“Our approach could come in handy when a human interacts with a robot but doesn’t want to spell out all the details of a task,” says MIT PhD student and CSAIL researcher Minyoung Hwang, who is a lead author on a
[paper](https://arxiv.org/abs/2511.14565)
presenting the project. “We’re minimizing human effort by enabling machines to get to the bottom of what users really want.”

According to Hwang, Masked IRL can help robots safely maneuver in settings where there are elements a human might not describe in a prompt, but that are crucial nonetheless. For example, a machine grabbing you a snack from the kitchen may not know to avoid bumping into your laptop. Likewise, a factory robot placing items into different boxes must carefully navigate around shelves.

To learn new tasks in these situations, Masked IRL uses the robot’s sensors to capture information about its surroundings. These components also log each movement of a kinesthetic demonstration — a training approach where a human physically moves a robot to do a specific action. It’s sort of like being the machine’s physical therapist, bending joints in a particular direction to show a robot how to grab, move, and place objects.

MIT’s system then calls on an LLM to compare this sequence of motions (called a trajectory) to the shortest possible path. The model also elaborates on what might be unclear in a prompt, turning a request like “stay close” into “stay close to the surface of the table.” Using the trajectory comparison and clarified directions, the LLM begins to understand why the motions it was trained on are important to the task.


A second LLM then evaluates details of the environment, such as the position of obstacles and the shape of the robot’s target object. During this process, it “masks” (in other words, ignores) the elements it deems irrelevant to the task at hand, scoring each one as either a “1” (important) or “0” (not so much). For example, whether or not a user was leaning on a table during a demonstration would be a “0,” making it irrelevant. Any detail considered a “1” is incorporated into the final action plan by an algorithm.


These masks gave Masked IRL a key advantage over comparable baselines in both 3D and real-world demos because it taught a robot which information to prioritize. Thanks to the researchers’ system, virtual and real robots alike were able to skillfully maneuver objects around obstacles, such as moving a coffee mug around a laptop to different spots on a table. In these tasks, Masked IRL correctly identified users’ preferences, which they didn’t explicitly state in their prompts, up to 15 percent more often than comparable baselines.


During simulation experiments, CSAIL researchers also found that Masked IRL was a fast learner. It required fewer demos to understand how to move the mug than its baselines. They also found that the robots performed better when an LLM cleared up instructions, instead of having the machine try to follow a vague request.


This more focused approach also translated well to a real robotic arm, executing prompts the system hadn’t seen during its training phase. After being trained on 50 kinesthetic demonstrations, the robot carefully moved a cup toward a human while avoiding colliding with a user’s computer — an obstacle it learned to avoid by elaborating on a more general request to “stay away.” It also wiped a table down while “staying close” to it, and handed a user a bag of chips while “staying away” from both a human and a table.

Masked IRL senses and explains what users leave unsaid, but soon, it might “see” it too. CSAIL researchers plan to make their approach more dynamic by equipping it with cameras, allowing a robot to take images of its surroundings. Then it could highlight and focus on specific elements nearby. For example, if you asked the machine to pick up a toy, it might see some bananas nearby and ignore them before handling its target object.

Hwang wrote the paper with three CSAIL colleagues: PhD student Alexandra Forsey-Smerek ’20, SM ’22; postdoc Nathaniel Dennler; and MIT Assistant Professor Andreea Bobu, who is a member of the Department of Aeronautics and Astronautics and CSAIL. Their work was supported, in part, by the Tata Group via the MIT Generative AI Impact Consortium Award, and the Department of Defense. They’ll present the project at the 2026 IEEE International Conference on Robotics and Automation in June.