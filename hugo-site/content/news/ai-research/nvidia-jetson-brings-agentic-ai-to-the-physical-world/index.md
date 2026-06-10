---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-06-10T03:12:30.646354+00:00'
exported_at: '2026-06-10T03:12:31.964339+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/jetson-agentic-ai-physical-world
structured_data:
  about: []
  author: ''
  description: With NVIDIA JetPack 7.2 and NVIDIA NemoClaw support, Jetson is agentic-ready,
    giving developers a production-grade stack to deliver next-level intelligence
    to robotics, inspection and industrial automation.
  headline: NVIDIA Jetson Brings Agentic AI to the Physical World
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/jetson-agentic-ai-physical-world
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NVIDIA Jetson Brings Agentic AI to the Physical World
updated_at: '2026-06-10T03:12:30.646354+00:00'
url_hash: 5f8cc1fb819277e09f320e2255f89916e5ea5ec2
---

Agentic AI is getting physical.

At COMPUTEX on Tuesday, NVIDIA announced
[NVIDIA JetPack 7.2](https://developer.nvidia.com/embedded/develop/software)
and
[NVIDIA NemoClaw](https://www.nvidia.com/en-us/ai/nemoclaw/)
support on
[NVIDIA Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)
.

JetPack 7.2 brings agentic AI skills,
[Yocto project](https://github.com/oe4t)
support,
[NVIDIA CUDA 13](https://developer.nvidia.com/cuda-13-0-0-download-archive)
on
[NVIDIA Jetson Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
, a substantial performance gain on Jetson AGX Orin 32GB module and Multi-Instance GPU (MIG) support on
[NVIDIA Jetson Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
.

![](https://blogs.nvidia.com/wp-content/uploads/2026/05/Picture2.png)

NVIDIA’s Asier Arrnaz shows how Build-a-Claw brings AI to the edge, a personalized, always-on assistant running right on NVIDIA Jetson.

The launch coincides with the GTC Taipei
[Build-a-Claw event](https://www.nvidia.com/en-us/ai/build-a-claw/#referrer=vanity)
, bringing the popular hands-on event from GTC San Jose to Taiwan, one of the world’s premier global technology hubs.

The release lands NemoClaw,
[NVIDIA’s agentic AI framework](https://www.nvidia.com/en-us/ai/)
, on the production-grade Jetson stack — taking agentic AI from servers and workstations into the physical world, across robotics, inspection and industrial automation.

“Agentic AI is here, and Jetson’s programmability and high performance enable developers to instantly deploy physical AI agents in production at the edge,” said Deepu Talla, vice president of robotics and edge computing at NVIDIA. “With purpose-built skills for agentic development and workflows, developers can accelerate time to market, cut total cost of ownership and deploy at scale — all on a memory-optimized platform.”

Jetson is already a multi-generation platform —
[Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
,
[Thor](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
and beyond — powering edge AI in robotics, autonomous systems, industrial inspection and medical devices. JetPack 7.2 builds on that foundation; NemoClaw extends it.

Three layers ship in this release. JetPack 7.2 at the base — operating system (OS), compute, deterministic performance. A new layer of agent skills in the middle, automating developer tasks. And NemoClaw at the top.

JetPack 7.2 brings major upgrades to the Jetson software foundation. Yocto-based OS support gives industrial customers a leaner, more customizable Linux foundation — important for memory-bound deployments. CUDA 13 on Jetson Orin brings the latest compute stack to existing devices. MIG plus real-time kernel on Jetson Thor lets developers reserve dedicated GPU resources for deterministic workloads, like robot perception systems that can’t pause for unrelated AI inference.
[Jetson AGX Orin](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
32GB also gets a performance boost to 241 TOPS of AI compute, up 20% above its original spec.

The middle layer — agent skills — accelerates the work of building a Jetson-based system itself. Jetson agent skills now include Linux customization, memory optimization, model benchmarking and similar developer tasks. These are now available as agent-deployable skills, developed from NVIDIA documentation and design guides. The result: a task that used to take weeks resolves in days.

At the top, NemoClaw deploys to Jetson with a single command. The pairing lands agentic AI on a production-grade robotics and vision AI stack, accelerating task automation for industrial systems. Developers can go further with
[NVIDIA Metropolis VSS blueprint skills](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization/tree/main/skills)
, adding visual reasoning agents that watch, interpret and act on what they see.

## Agentic AI already arriving with Jetson

The Jetson platform is already in deployment across fields such as robotics, industrial automation, drones, healthcare devices, agricultural machinery, humanoid systems and more.

![](https://blogs.nvidia.com/wp-content/uploads/2026/05/Picture-3.jpg)

Solomon uses NemoClaw to coordinate AI agents on a humanoid robot.

[Solomon](https://www.solomon-3d.com/news-events/press-releases/solomon-nvidia-nemoclaw-active-perception-humanoid-robots/)
uses NVIDIA NemoClaw to coordinate AI agents on a humanoid robot, integrating reasoning, perception, sensor fusion, locomotion and manipulation into a single workflow. With Solomon’s active perception technology, powered by NVIDIA’s open source foundation model, the robot can understand tasks, optimize positioning for picking and adapt dynamically. All this enables reliable and autonomous operations in complex environments.

[Advantech](https://www.advantech.com/en/resources/news/advantech-mic-ai-systems-enable-yocto-based-embedded-linux-with-nvidia-jetpack-72-support-for-flexible-edge-ai-deployment)
is building and deploying an agentic factory brain within its own manufacturing facilities to enable AI-native operations using NVIDIA NemoClaw,
[NVIDIA Nemotron 3](https://developer.nvidia.com/nemotron)
and NVIDIA Jetson Thor. The platform automates robot fleet management, intelligent defect detection and autonomous decision-making to drive next-generation industrial operations. Across industries, the builds are already shipping.

[Rebotnix](https://rebotnix.com/blog/nvidia_computex2026)
makes smart city cameras with agentic reasoning capabilities for faster city-level decision-making.

[Spingence](https://www.spingence.com/en/)
builds manufacturing defect agents to identify root causes and process improvement recommendations through analytics and knowledge reasoning.

And
[ANIWEAVE](https://www.aniweave.ai/spatial-touring)
and
[Avalanche Computing](https://www.avalanc.com/)
are partnering to transform real estate spaces into immersive 3D touring experiences with AI-powered conversational agents.

## More AI, less memory

![](https://blogs.nvidia.com/wp-content/uploads/2026/05/computex-jetson-vending.jpg)

Image courtesy of SandStar.

[SandStar](https://en.sandstar.com/blog/sandstar-to-deliver-global-low-cost-high-performance-ai-retail-solutions-using-nvidia-jetson-orin-nx.html)
uses NVIDIA Jetson Orin NX and NemoClaw to power AI vending machines and smart retail operations with AI vision, LLM-driven interaction, standard operating procedure monitoring and store optimization across 30+ countries. By achieving nearly 40% memory optimization, SandStar reports it migrated from 16GB to 8GB devices, significantly reducing deployment costs while maintaining high performance.

[NoTraffic](https://www.notraffic.com/)
develops AI-powered Intelligent Traffic Management Systems that analyze real-time traffic conditions and dynamically optimize signal operations. NoTraffic reports it optimized CUDA library overhead through static compilation and targeted kernel pruning. These optimizations reduced memory usage by 29%, improving efficiency and streamlining the perception stack for faster real-time inference.

[GROOVE X](https://groove-x.com/en/)
, maker of the LOVOT companion robot, is using a variety of AI accelerators on Jetson modules to offload CPU and GPU workload and reduce memory footprint.

## Yocto-based JetPack 7.2 in production

![](https://blogs.nvidia.com/wp-content/uploads/2026/05/computex-jetson-robot-front.jpg)

Hexagon Robotics integrates Jetson Thor for safer humanoid robots.

[Hexagon Robotics](https://hexagon.com/robotics)
is integrating NVIDIA Jetson Thor to power safer and more autonomous humanoid robots with real-time AI, high-speed sensor processing and multimodal data fusion. Combined with Yocto-based OS customization for better reproducibility and safety, these humanoid robots operate more reliably in demanding environments such as manufacturing, logistics and construction.

[Zipline](https://www.zipline.com/)
uses NVIDIA Jetson Orin NX in its autonomous delivery drones to enable real-time sensor fusion, environmental awareness and safe navigation for rapid medical, food and retail deliveries around the world. Zipline uses Yocto to build its custom operating system which is designed for high-performance onboard AI processing while optimizing for reliability, efficiency and a lower memory footprint.

[1X](https://www.1x.tech/discover/nvidia-gtc-2026)
(maker of the Neo Humanoid) and
[Universal Robots](https://www.universal-robots.com/)
are planning to adopt
[Yocto-based JetPack 7.2](https://developer.nvidia.com/blog/deploy-agentic-ready-ai-at-the-edge-with-memory-efficiency-in-nvidia-jetpack-7-2/)
in their production deployments.

## Yocto ecosystem partners

[Balena](https://blog.balena.io/balena-announces-remote-fleet-management-for-nvidia-jetpack-7-2-and-jetson-thor/)
,
[Konsulko Group](https://www.konsulko.com/orca-os-nvidia-jetson-live-tutorial)
,
[Neurealm](https://www.neurealm.com/press-release/neurealm-announces-day-one-support-for-nvidias-official-yocto-project-integration-on-jetson-platforms/)
,
[Peridio](https://www.peridio.com/nvidia-jetson-vision-ai-guide)
,
[RidgeRun](https://www.ridgerun.com/post/how-ridgerun-helps-bring-nvidia-jetson-based-products-to-market-faster-with-yocto)
and
[Wind River](https://www.aptiv.com/en/newsroom/article/aptiv-to-deliver-production-ready-edge-ai-with-long-term-support-with-nvidia)
provide Linux distro products, engineering services and long-term support that help customers ship production-grade Yocto-based deployments faster.

[AAEON](https://www.aaeon.com/en)
,
[ASUS](https://iot.asus.com/embedded-computers-edge-ai-systems/edge-ai-gpu-computers/filter?Series=Edge-AI-GPU-Computers&amp;Spec=2213)
,
[Avermedia](https://professional.avermedia.com/)
,
[Connect Tech](https://connecttech.com/jetpack-7-2-yocto/)
and
[YUAN](https://www.yuan.com.tw/newscontent/335)
have validated Yocto OS with their production edge computing systems to accelerate customer deployment.

## What’s next

NemoClaw started in the data center. Now it runs in a retail store, a humanoid robot on a factory floor, a traffic system at a busy intersection. The era of physical AI agents has just begun.

Developers can start their agentic AI journey from the
[Jetson software page](https://developer.nvidia.com/embedded/develop/software)
.

Watch NVIDIA founder and CEO Jensen Huang’s
[keynote](https://www.nvidia.com/en-tw/gtc/taipei/keynote/?nvid=nv-int-bnr-823296)
and learn more at
[NVIDIA GTC Taipei](https://www.nvidia.com/en-tw/gtc/taipei/)
.

See
[notice](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
regarding software product information.