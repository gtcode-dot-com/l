---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-16T00:03:43.006791+00:00'
exported_at: '2025-12-16T00:03:46.604036+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/adam-robot-vegas-golden-knights-thor
structured_data:
  about: []
  author: ''
  description: In Las Vegas’s T-Mobile Arena, fans of the Golden Knights are getting
    more than just hockey — they’re getting a taste of the future. ADAM, a robot developed
    with NVIDIA Isaac libraries, is pouring drinks and turning heads in one of the
    NHL’s most exciting venues. ADAM, short for Automated Dual Arm Mixologist, was
    developed  Read Article
  headline: 'Cheers to AI: ADAM Robot Bartender Makes Drinks at Vegas Golden Knights
    Game'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/adam-robot-vegas-golden-knights-thor
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Cheers to AI: ADAM Robot Bartender Makes Drinks at Vegas Golden Knights Game'
updated_at: '2025-12-16T00:03:43.006791+00:00'
url_hash: febc7fa7bf6e5ddc7bfc58b9e7f54e5782713e88
---

In Las Vegas’s T-Mobile Arena, fans of the Golden Knights are getting more than just hockey — they’re getting a taste of the future. ADAM, a robot developed with
[NVIDIA Isaac libraries](https://developer.nvidia.com/isaac)
, is pouring drinks and turning heads in one of the NHL’s most exciting venues.

ADAM, short for Automated Dual Arm Mixologist, was developed by Las-Vegas based Richtech Robotics. It’s not just a novelty — it’s a solution to real-world challenges in hospitality: labor shortages and demands for unique customer experiences.

“The hospitality industry faces significant labor challenges, and ADAM is our answer to meeting those needs while elevating the customer experience,” said Matt Casella, president of Richtech Robotics. “With NVIDIA’s Isaac platform, we’ve developed a solution that’s scalable, consistent, and frankly, creates memorable moments for fans. The response at T-Mobile Arena has been phenomenal—people love interacting with ADAM.”

VIDEO

## **Learning to Serve Drinks in Simulation**

Before ADAM ever poured a drink, it trained in a virtual bar. Richtech used
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)
, an open-source, reference robotic simulation framework built on
[NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)
, to build a high-fidelity and physically accurate simulation of ADAM’s workstation, complete with cups, utensils and lighting variations. The team generated
[synthetic data](https://www.nvidia.com/en-us/glossary/synthetic-data-generation/)
to teach ADAM how to recognize objects even in tricky conditions like glare or reflection.

VIDEO

ADAM’s skills such as pouring and shaking were refined in simulation using
[Isaac Lab](https://developer.nvidia.com/isaac/lab)
, NVIDIA’s open source robot learning framework. The result: a robot that doesn’t just follow instructions — it adapts to its environment with precision.

## **Running Real-Time AI at the Edge With Jetson**

ADAM runs on
[NVIDIA Jetson AGX Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
, the powerful edge AI platform capable of 275 TOPS of compute. Using
[Isaac ROS 2](https://developer.nvidia.com/isaac/ros)
libraries, ADAM captures camera feeds, detects objects and calibrates the workspace in real time. ADAM’s perception stack — built with
[TAO Toolkit](https://developer.nvidia.com/tao-toolkit)
and optimized with
[TensorRT](https://developer.nvidia.com/tensorrt)
— enables it to identify cups, measure liquid levels and adjust movements with less than 40 milliseconds of latency.

That means ADAM can spot a misplaced cup, detect when foam reaches the rim and correct a pour — all without missing a beat.

## **Creating Industrial Dexterity With NVIDIA Thor**

While ADAM is busy serving drinks at Golden Knights games, Richtech Robotics is also making major strides in industrial automation with Dex, a new mobile
[humanoid robot](https://www.nvidia.com/en-us/glossary/humanoid-robot/)
built for factory and warehouse environments.

Recently unveiled at
[GTC DC](https://www.nvidia.com/gtc/dc/)
, Dex combines the mobility of an autonomous wheeled platform with the precision of dual-arm dexterity. It’s designed to handle such light-to-medium industrial tasks as machine operation, parts sorting, material handling and packaging — all with the flexibility to  take on different tools and workflows.

Dex runs on
[NVIDIA Jetson Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
, a next-generation robotics processor that gives it the ability to deliver real-time sensor processing and AI reason in dynamic industrial settings.

Dex was trained from a blend of real world and synthetic data generated from Isaac Sim. This allowed Dex’s model to be generalized across a multitude of scenarios.

*Learn more about*
[*Jetson Thor*](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
*and about festive Jetson platform
[holiday prices](https://blogs.nvidia.com/blog/jetson-edge-ai-holiday-2025/)
.*