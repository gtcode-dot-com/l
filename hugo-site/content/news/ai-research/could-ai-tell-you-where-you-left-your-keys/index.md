---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-23T04:07:43.463010+00:00'
exported_at: '2026-06-23T04:07:44.672623+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/could-ai-tell-you-where-you-left-your-keys-0617
structured_data:
  about: []
  author: ''
  description: A new memory framework known as DAAAM enables a robot to rapidly recall
    rich descriptions and precise locational information about objects it encountered
    while exploring its environment. This efficient approach could help an autonomous
    agent quickly answer complex queries about its environment in natural language.
  headline: Could AI tell you where you left your keys?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/could-ai-tell-you-where-you-left-your-keys-0617
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Could AI tell you where you left your keys?
updated_at: '2026-06-23T04:07:43.463010+00:00'
url_hash: 0dc90b9f15983adeb3f722bd2336406944309042
---

An auto factory worker can remember the storage bin where she left a partly assembled component the night before, and quickly return to that spot to pick it up. But robots that may work side-by-side with her would struggle to develop and access this same type of “spatiotemporal” memory.

Now, MIT researchers have developed a long-term memory framework that allows robots to rapidly form and recall a detailed mental model of complicated, large-scale environments.

In the future, this advance could allow the factory worker to send a robotic assistant to fetch the item, simply by asking it to “go and grab the component we started assembling last night.”

This new method combines advanced map representations with rich descriptions of the environment that the robot gathers as it travels over a long period of time. The robot can quickly access this memory to answer complex queries about its environment in plain language.

This memory framework, which answers questions more accurately than state-of-the-art methods, runs fast enough for a mobile robot to use in real-time.

In addition to its potential uses in robotics, this method could have applications in augmented reality systems that aid maintenance workers in anomaly detection or assist commuters in wayfinding.

“If we want robots to work side-by-side with humans and interact better with humans, they must speak the same language. The robot must be able to reason about time and space the same way humans do. That is essentially what our method is doing. It is turning a traditional map into a language-based map that is easier for the robot to think about and access using language,” says Luca Carlone, an associate professor in MIT’s Department of Aeronautics and Astronautics (AeroAstro), principal investigator in the Laboratory for Information and Decision Systems (LIDS), and director of the MIT SPARK Laboratory.

He is joined on the
[paper](https://arxiv.org/pdf/2512.00565)
by lead author Nicolas Gorlo, an MIT graduate student; and Lukas Schmid, a former research scientist at MIT and now professor at the University of Technology Nuremberg in Germany. The research was recently presented at the Conference on Computer Vision and Pattern Recognition (CVPR).

**Spatiotemporal memory**

Memory allows an artificial intelligence system, like a chatbot, to answer complex questions and reason about previous interactions with its user.

“We want to design a new type of memory, a spatiotemporal memory, that enables an AI-powered robot to remember real interactions and sensor observations. Like ChatGPT, but grounded in the real world and capable of answering any question about the environment, like ‘Where did I leave my wallet?’” Carlone says.

To develop such a memory framework, the MIT researchers bridged two lines of work: computer vision and robotic mapping.

Multimodal computer vision models can understand and richly describe the objects in a scene, but they often only process a single annotation at a time. On the other hand, robotic mapping frameworks create 3D maps of an environment, like an entire apartment or university campus, but usually lack detailed descriptions of objects or are computationally expensive.

The method the MIT researchers created, called Describe Anything, Anywhere, Anytime, at Any Moment (DAAAM), takes the best of both approaches.

Using DAAAM, as a robot traverses its environment, it attaches rich descriptions to objects it sees. For instance, the robot may note that a particular building on the MIT campus is called the Stata Center and is designed with a certain type of architecture, or that a bike rack holds five bicycles and the red one has a flat tire.

It stores this detailed information in a 3D map-based representation that is arranged spatially, so objects will be grouped into separate regions. In this way, the robot can remember that the red bicycle with the flat tire is in the bike rack outside the Stata Center.

But existing techniques that capture such rich descriptions typically take a few seconds to annotate a few objects. This is too slow for real-time performance, since a robot might see hundreds of objects during a few minutes of exploration.

“The faster the robot can form this spatial memory, the more efficient it will be performing actions in the environment,” Carlone adds.

**Streamlining the process**

To speed things up, DAAAM aggregates nearby objects as it travels and uses an optimization method to select key frames to annotate. These are images with the clearest view of multiple objects, allowing the system to thoroughly describe several items in parallel, speeding up computation tenfold.

As the robot explores the space, it attaches each batch of annotations to multiple objects in a particular location on the 3D map.

“We annotate every object only once, so our framework can run in very large-scale environments in real time. And by clustering objects into regions, it can answer a wide range of queries about objects and locations in the environment,” Gorlo explains.

Once the system builds this spatial memory, it must retrieve information from an enormous database of objects and descriptions in an efficient manner.

To enable this, the researchers used an LLM that calls on various tools, which can quickly retrieve specific information in a way that reduces hallucinations. This allows DAAAM to answer a user query accurately in only a few seconds.

For instance, if one asks a robot about a certain sculpture it saw near an MIT campus building, DAAAM can use a semantic search tool to retrieve information based on the word “sculpture” or a different tool to retrieve information based on the location of the building.

When tested and compared with other methods, DAAAM was between 21 percent and 53 percent more accurate, depending on the question type.

In the future, the researchers want to expand DAAAM so the system can capture significant events that happened in the environment. They are also working to incorporate confidence levels into the system’s responses.

“Ultimately, we want to have robots that can help with any sort of tasks. With this framework, we are trying to create the foundations to enable a generalist agent that can do anything you ask,” Gorlo says.

This research was funded, in part, by the U.S. Army Research Laboratory and the Office of Naval Research. Carlone is currently on sabbatical as an Amazon Scholar; this article describes work performed at MIT and is not associated with Amazon.