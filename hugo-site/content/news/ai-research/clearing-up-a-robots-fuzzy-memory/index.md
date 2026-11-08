---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-08T05:23:20.075002+00:00'
exported_at: '2026-11-08T05:23:21.131123+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/clearing-up-robot-fuzzy-memory-1105
structured_data:
  about: []
  author: ''
  description: MIT researchers developed a system that identifies and corrects the
    descriptions of mislabeled objects stored in a robot’s memory. The method could
    make household or industrial robots better able to perform complex, multistep
    tasks.
  headline: Clearing up a robot’s fuzzy memory
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/clearing-up-robot-fuzzy-memory-1105
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Clearing up a robot’s fuzzy memory
updated_at: '2026-11-08T05:23:20.075002+00:00'
url_hash: 16de4ca3c25d3eedbaa6b632b2a310c4b7a3d989
---

A new system identifies and corrects unreliable object descriptions stored in a robot’s memory, improving the robot’s ability to interact with its environment.

The researchers also employed a special technique to streamline this process so a mobile robot can continually update uncertain memory entries in real time.

When compared to baseline methods, UQ-DAAAM boosted the robot’s confidence and improved the accuracy of its answers to questions about objects, their locations, and when it saw them.

“Contrary to ChatGPT, when we think about physical AI, it is not enough to simply put a disclaimer cautioning that sometimes the robot might be wrong. Allowing a robot to know what it doesn’t know is going to be essential for this technology to be deployed safely and have a positive impact on society,” says Luca Carlone, an associate professor in MIT’s Department of Aeronautics and Astronautics (AeroAstro), principal investigator in the Laboratory for Information and Decision Systems (LIDS), director of the MIT SPARK Laboratory, and the senior author of the
[paper](https://arxiv.org/pdf/2606.08277)
presenting UQ-DAAAM.

He is joined on the paper by co-lead authors and MIT graduate students Harry Zhang and Nicolas Gorlo. The research will be presented at the Conference on Neural Information Processing Systems.

**Amending memory**

This new method builds on the researchers’ prior work,
[DAAAM](https://news.mit.edu/2026/could-ai-tell-you-where-you-left-your-keys-0617)
, a robot memory system that uses a vision-language model (VLM) to richly describe objects in scenes a robot captures with its onboard cameras. These descriptions are stored as detailed captions in a 3D map-based representation of the robot’s environment that it can call upon later to answer questions.

But the robot sometimes sees objects only partially or from far away, or its camera might capture blurry or poorly lit images. In these cases, DAAAM might describe these objects incorrectly, such as by mistaking a gray chimney for a squirrel perched on a rooftop.

“With no way to correct itself, this wrong memory would persist as the robot proceeds in its environment, which could impact downstream applications,” Zhang says.

UQ-DAAAM integrates uncertainty quantification into the DAAAM framework. It allows the robot to measure its confidence in the accuracy of object descriptions and fix incorrect captions as it travels through an environment.

While on the move, the robot constantly collects and stores images of the world around it. Many of these images show the same objects captured from different angles. UQ-DAAAM uses these additional viewpoints to identify and correct unreliable descriptions.

First, it calculates the VLM’s confidence level in the words it generated to describe a potentially mislabeled object. Then, it measures consistency by comparing this description to captions of images that describe the same object from different vantage points.

“We fuse both sources of uncertainty into a single number that captures how certain the VLM is in its overall understanding of the object,” Carlone explains.

If that number exceeds a certain threshold, the uncertainty is too high, and UQ-DAAAM will refine the caption by using additional images of the object.

It does this using a heuristic, or simple rule, that determines which additional viewpoints will reduce the robot’s uncertainty about the object. For instance, it might choose an image captured a few frames later that clearly shows smoke emanating from the chimney.

The researchers mathematically proved that this heuristic can identify the best frames to select without rerunning the VLM, dramatically reducing the amount of computation.

“The key challenge Nico and Harry had to overcome is how to combine VLMs with uncertainty quantification into something that is running in a fraction of a second on a robot that is moving,” Carlone says.

**Remembering with confidence**

Once it has identified additional captions that will reduce its uncertainty about the object, the system uses an LLM to fuse them into a single object description. To boost accuracy, the LLM puts more weight on new captions and those with less ambiguity.

This refinement step is able to resolve ambiguities for about 92 percent of the objects in the robot’s environment, while only requiring two additional captions per object. It increased the accuracy of object descriptions by 5 percent compared to the state of the art.

UQ-DAAAM also provided more accurate answers to questions about the objects it observed, where it saw them, and when it last encountered them than baseline methods.

“Performing this uncertainty quantification procedure across the entire map the robot generates allows it to improve its understanding of what it has observed,” Gorlo says.

Next, the researchers want to use UQ-DAAAM to guide different types of robots, like mobile robotic manipulators, and apply their uncertainty quantification techniques to other domains.

In addition, they are studying the use of UQ-DAAAM to identify areas of high uncertainty the robot could revisit to improve its understanding of the environment. They are also exploring uncertainty quantification in systems that predict the future state of a robot’s environment.

This research is supported, in part, by the U.S. Army Research Laboratory and the U.S. Office of Naval Research. Carlone is currently on sabbatical as an Amazon Scholar; this article describes work performed at MIT and is not associated with Amazon.