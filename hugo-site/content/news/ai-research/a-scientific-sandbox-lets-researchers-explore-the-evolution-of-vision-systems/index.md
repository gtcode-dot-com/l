---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-18T12:03:30.414906+00:00'
exported_at: '2025-12-18T12:03:34.099540+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/scientific-sandbox-lets-researchers-explore-evolution-vision-systems-1217
structured_data:
  about: []
  author: ''
  description: 'Researchers developed a computational framework that enables them
    to explore and probe the evolution of vision systems over millions of years using
    embodied AI agents. This work could help scientists develop better sensors and
    cameras for robots, drones, and wearable devices. '
  headline: A “scientific sandbox” lets researchers explore the evolution of vision
    systems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/scientific-sandbox-lets-researchers-explore-evolution-vision-systems-1217
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: A “scientific sandbox” lets researchers explore the evolution of vision systems
updated_at: '2025-12-18T12:03:30.414906+00:00'
url_hash: 9188b6c14113b112c73ff2106698059c3263cf29
---

Why did humans evolve the eyes we have today?

While scientists can’t go back in time to study the environmental pressures that shaped the evolution of the diverse vision systems that exist in nature, a new computational framework developed by MIT researchers allows them to explore this evolution in artificial intelligence agents.

The framework they developed, in which embodied AI agents evolve eyes and learn to see over many generations, is like a “scientific sandbox” that allows researchers to recreate different evolutionary trees. The user does this by changing the structure of the world and the tasks AI agents complete, such as finding food or telling objects apart.

This allows them to study why one animal may have evolved simple, light-sensitive patches as eyes, while another has complex, camera-type eyes.

The researchers’ experiments with this framework showcase how tasks drove eye evolution in the agents. For instance, they found that navigation tasks often led to the evolution of compound eyes with many individual units, like the eyes of insects and crustaceans.

On the other hand, if agents focused on object discrimination, they were more likely to evolve camera-type eyes with irises and retinas.

This framework could enable scientists to probe “what-if” questions about vision systems that are difficult to study experimentally. It could also guide the design of novel sensors and cameras for robots, drones, and wearable devices that balance performance with real-world constraints like energy efficiency and manufacturability.

“While we can never go back and figure out every detail of how evolution took place, in this work we’ve created an environment where we can, in a sense, recreate evolution and probe the environment in all these different ways. This method of doing science opens to the door to a lot of possibilities,” says Kushagra Tiwary, a graduate student at the MIT Media Lab and co-lead author of a paper on this research.

He is joined on the paper by co-lead author and fellow graduate student Aaron Young; graduate student Tzofi Klinghoffer; former postdoc Akshat Dave, who is now an assistant professor at Stony Brook University; Tomaso Poggio, the Eugene McDermott Professor in the Department of Brain and Cognitive Sciences, an investigator in the McGovern Institute, and co-director of the Center for Brains, Minds, and Machines; co-senior authors Brian Cheung, a postdoc in the  Center for Brains, Minds, and Machines and an incoming assistant professor at the University of California San Francisco; and Ramesh Raskar, associate professor of media arts and sciences and leader of the Camera Culture Group at MIT; as well as others at Rice University and Lund University. The research
[appears today in
*Science Advances*](https://doi.org/10.1126/sciadv.ady2888)
.

**Building a scientific sandbox**

The paper began as a conversation among the researchers about discovering new vision systems that could be useful in different fields, like robotics. To test their “what-if” questions, the researchers decided to
[use AI to explore the many evolutionary possibilities](https://mit-genai.pubpub.org/pub/bcfcb6lu/release/3)
.

“What-if questions inspired me when I was growing up to study science. With AI, we have a unique opportunity to create these embodied agents that allow us to ask the kinds of questions that would usually be impossible to answer,” Tiwary says.

To build this evolutionary sandbox, the researchers took all the elements of a camera, like the sensors, lenses, apertures, and processors, and converted them into parameters that an embodied AI agent could learn.

They used those building blocks as the starting point for an algorithmic learning mechanism an agent would use as it evolved eyes over time.

“We couldn’t simulate the entire universe atom-by-atom. It was challenging to determine which ingredients we needed, which ingredients we didn’t need, and how to allocate resources over those different elements,” Cheung says.

In their framework, this evolutionary algorithm can choose which elements to evolve based on the constraints of the environment and the task of the agent.

Each environment has a single task, such as navigation, food identification, or prey tracking, designed to mimic real visual tasks animals must overcome to survive. The agents start with a single photoreceptor that looks out at the world and an associated neural network model that processes visual information.

Then, over each agent’s lifetime, it is trained using reinforcement learning, a trial-and-error technique where the agent is rewarded for accomplishing the goal of its task. The environment also incorporates constraints, like a certain number of pixels for an agent’s visual sensors.

“These constraints drive the design process, the same way we have physical constraints in our world, like the physics of light, that have driven the design of our own eyes,” Tiwary says.

Over many generations, agents evolve different elements of vision systems that maximize rewards.

Their framework uses a genetic encoding mechanism to computationally mimic evolution, where individual genes mutate to control an agent’s development.

For instance, morphological genes capture how the agent views the environment and control eye placement; optical genes determine how the eye interacts with light and dictate the number of photoreceptors; and neural genes control the learning capacity of the agents.

**Testing hypotheses**

When the researchers set up experiments in this framework, they found that tasks had a major influence on the vision systems the agents evolved.

For instance, agents that were focused on navigation tasks developed eyes designed to maximize spatial awareness through low-resolution sensing, while agents tasked with detecting objects developed eyes focused more on frontal acuity, rather than peripheral vision.

Another experiment indicated that a bigger brain isn’t always better when it comes to processing visual information. Only so much visual information can go into the system at a time, based on physical constraints like the number of photoreceptors in the eyes.

“At some point a bigger brain doesn’t help the agents at all, and in nature that would be a waste of resources,” Cheung says.

In the future, the researchers want to use this simulator to explore the best vision systems for specific applications, which could help scientists develop task-specific sensors and cameras. They also want to integrate LLMs into their framework to make it easier for users to ask “what-if” questions and study additional possibilities.

“There’s a real benefit that comes from asking questions in a more imaginative way. I hope this inspires others to create larger frameworks, where instead of focusing on narrow questions that cover a specific area, they are looking to answer questions with a much wider scope,” Cheung says.

This work was supported, in part, by the Center for Brains, Minds, and Machines and the Defense Advanced Research Projects Agency (DARPA) Mathematics for the Discovery of Algorithms and Architectures (DIAL) program.