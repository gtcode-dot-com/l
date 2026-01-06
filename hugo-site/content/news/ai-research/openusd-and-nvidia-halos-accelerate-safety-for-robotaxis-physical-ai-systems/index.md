---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-18T00:03:46.141168+00:00'
exported_at: '2025-12-18T00:03:49.576881+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/openusd-halos-safety-robotaxi-physical-ai
structured_data:
  about: []
  author: ''
  description: New NVIDIA safety frameworks and technologies are advancing how developers
    build safe physical AI.
  headline: 'Into the Omniverse: OpenUSD and NVIDIA Halos Accelerate Safety for Robotaxis,
    Physical AI Systems'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/openusd-halos-safety-robotaxi-physical-ai
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Into the Omniverse: OpenUSD and NVIDIA Halos Accelerate Safety for Robotaxis,
  Physical AI Systems'
updated_at: '2025-12-18T00:03:46.141168+00:00'
url_hash: 49f26a78eadb72ec35d5e02b79a8c584ae0dc70d
---

*Editor’s note: This post is part of*
[*Into the Omniverse*](https://www.nvidia.com/en-us/omniverse/news/)
*, a series focused on how developers, 3D practitioners and enterprises can transform their workflows using the latest advancements in*
[*OpenUSD*](https://www.nvidia.com/en-us/omniverse/usd/)
*and*
[*NVIDIA Omniverse*](https://www.nvidia.com/en-us/omniverse/usd/)
*.*

[Physical AI](https://www.nvidia.com/en-us/glossary/generative-physical-ai/)
is moving from research labs into the real world, powering intelligent robots and
[autonomous vehicles (AVs)](https://www.nvidia.com/en-us/glossary/autonomous-vehicles/)
— such as robotaxis — that must reliably sense, reason and act amid unpredictable conditions.

To safely scale these systems, developers need workflows that connect real-world data, high-fidelity simulation and robust AI models atop the common foundation provided by the
[OpenUSD](https://docs.nvidia.com/learn-openusd/latest/glossary.html)
framework.

The recently published
[OpenUSD Core Specification 1.0](https://aousd.org/uncategorized/core-spec-announcement/)
, OpenUSD — aka Universal Scene Description — now defines standard data types, file formats and composition behaviors, giving developers predictable, interoperable USD pipelines as they scale autonomous systems.

Powered by OpenUSD,
[NVIDIA Omniverse libraries](https://developer.nvidia.com/omniverse?sortBy=developer_learning_library%2Fsort%2Ffeatured_in.omniverse%3Adesc%2Ctitle%3Aasc&hitsPerPage=6)
combine
[NVIDIA RTX](https://developer.nvidia.com/rtx/ray-tracing?sortBy=developer_learning_library%2Fsort%2Ftitle%3Aasc)
rendering, physics simulation and efficient runtimes to create digital twins and simulation-ready (
[SimReady](https://www.nvidia.com/en-us/glossary/simready/)
) assets that accurately reflect real-world environments for synthetic data generation and testing.

[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)
world foundation models can run on top of these simulations to amplify data variation, generating new weather, lighting and terrain conditions from the same scenes so teams can safely cover rare and challenging edge cases.

*Learn more by watching the OpenUSD livestream today at 11 a.m. PT or in replay, part of the NVIDIA Omniverse OpenUSD Insiders series:*

VIDEO

In addition, advancements in
[synthetic data generation](https://www.nvidia.com/en-us/use-cases/synthetic-data-physical-ai/)
, multimodal datasets and SimReady workflows are now converging with the
[NVIDIA Halos](https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/)
framework for AV safety, creating a standards-based path to safer, faster, more cost-effective deployment of next-generation autonomous machines.

## **Building the Foundation for Safe Physical AI**

**Open Standards and SimReady Assets**

The OpenUSD
[Core Specification 1.0](https://aousd.org/uncategorized/core-spec-announcement/)
establishes the standard data models and behaviors that underpin SimReady assets, enabling developers to build interoperable simulation pipelines for AI factories and robotics on
[OpenUSD](https://developer.nvidia.com/usd)
.

Built on this foundation, SimReady 3D assets can be reused across tools and teams and loaded directly into
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)
, where USDPhysics colliders, rigid body dynamics and composition-arc–based variants let teams test robots in virtual facilities that closely mirror real operations.

**Open-Source Learning**

The
[Learn OpenUSD](https://docs.nvidia.com/learn-openusd/latest/index.html)
curriculum is now open source and available on GitHub, enabling contributors to localize and adapt templates, exercises and content for different audiences, languages and use cases. This gives educators a ready-made foundation to onboard new teams into OpenUSD-centric simulation workflows.​

**Generative Worlds as Safety Multiplier**

Gaussian splatting — a technique that uses editable 3D elements to render environments quickly and with high fidelity — and world models are accelerating simulation pipelines for safe robotics testing and validation.

At SIGGRAPH Asia, the
[NVIDIA Research](https://www.nvidia.com/en-us/research/)
team introduced
[Play4D](https://research.nvidia.com/publication/2025-12_play4d-accelerated-and-interactive-free-viewpoint-video-streaming-virtual)
, a streaming pipeline that enables 4D Gaussian splatting to accurately render dynamic scenes and improve realism.

Spatial intelligence company
[World Labs](https://www.worldlabs.ai/)
is using its
[Marble generative world model with NVIDIA Isaac Sim](https://developer.nvidia.com/blog/simulate-robotic-environments-faster-with-nvidia-isaac-sim-and-world-labs-marble/)
and
[Omniverse NuRec](https://docs.nvidia.com/nurec/index.html)
so researchers can turn text prompts and sample images into photorealistic, Gaussian-based physics-ready 3D environments in hours instead of weeks.

![](https://blogs.nvidia.com/wp-content/uploads/2025/12/WorldLabs_IsaacSim_Clip.gif)

Those worlds can then be used for physical AI training, testing and sim-to-real transfer. This high-fidelity simulation workflow expands the range of scenarios robots can practice in while keeping experimentation safely in simulation.

**Lightwheel Helps Teams Scale Robot Training With SimReady Assets**

Powered by OpenUSD,
[Lightwheel](https://www.nvidia.com/en-us/customer-stories/lightwheel/)
’s SimReady asset library includes a common scene description layer, making it easy to assemble high-fidelity digital twins for robots. The SimReady assets are embedded with precise geometry, materials and validated physical properties, which can be loaded directly into NVIDIA Isaac Sim and Isaac Lab for robot training. This allows robots to experience realistic contacts, dynamics and sensor feedback as they learn.

## **End-to-End Autonomous Vehicle Safety**

End-to-end autonomous vehicle safety advancements are accelerating with new research, open frameworks and inspection services that make validation more rigorous and scalable.

NVIDIA researchers, with collaborators at Harvard University and Stanford University, recently introduced the
[Sim2Val framework](https://www.arxiv.org/pdf/2506.20553)
to statistically combine real-world and simulated test results, reducing AV developers’ need for costly physical mileage while demonstrating how robotaxis and AVs can behave safely across rare and safety-critical scenarios.

Learn more by watching NVIDIA’s “Safety in the Loop” livestream:

VIDEO

These innovations are complemented by a new, open-source NVIDIA Omniverse NuRec Fixer, a Cosmos-based model trained on AV data that removes artifacts in neural reconstructions to produce higher-quality SimReady assets.

To align these advances with rigorous global standards, the
[NVIDIA Halos AI Systems Inspection Lab](https://www.nvidia.com/en-us/ai-trust-center/physical-ai/safety-certification/)
— accredited by ANAB — provides impartial inspection and certification of Halos elements across robotaxi fleets, AV stacks, sensors and manufacturer platforms through the
[Halos Certification Program](https://www.nvidia.com/en-us/ai-trust-center/physical-ai/safety-certification/)
.

**AV Ecosystem Leaders Putting Physical AI Safety to Work**

[Bosch](https://us.bosch-press.com/pressportal/us/en/press-release-28736.html)
,
[Nuro](https://www.nvidia.com/en-us/solutions/autonomous-vehicles/partners/nuro/)
and
[Wayve](https://wayve.ai/thinking/wayve-gen-3/)
are among the first participants in the NVIDIA Halos AI Systems Inspection Lab, which aims to accelerate the safe, large-scale deployment of robotaxi fleets. Onsemi, which makes sensor systems for AVs, industrial automation and medical applications, has recently become the first company to pass inspection for the NVIDIA Halos AI Systems Inspection Lab.

VIDEO

The open-source
[CARLA](https://carla.org/)
simulator integrates
[NVIDIA NuRec and Cosmos Transfer](https://developer.nvidia.com/blog/accelerating-av-simulation-with-neural-reconstruction-and-world-foundation-models/)
to generate reconstructed drives and diverse scenario variations, while
[Voxel51](https://voxel51.com/)
’s FiftyOne engine, linked to Cosmos Dataset Search, NuRec and Cosmos Transfer, helps teams curate, annotate and evaluate multimodal datasets across the AV pipeline.​

VIDEO

Mcity at the University of Michigan is enhancing the digital twin of its
[32-acre AV test facility](https://mcity.umich.edu/mcity-enhances-digital-twin-of-av-test-facility-with-nvidia-omniverse/)
using Omniverse libraries and technologies. The team is integrating the NVIDIA Blueprint for AV simulation and Omniverse Sensor RTX application programming interfaces to create physics-based models of camera, lidar, radar and ultrasonic sensors.

By aligning real sensor recordings with high-fidelity simulated data and sharing assets openly, Mcity enables safe, repeatable testing of rare and hazardous driving scenarios before vehicles operate on public roads.

## **Get Plugged Into the World of OpenUSD and Physical AI Safety**

Learn more about OpenUSD, NVIDIA Halos and physical AI safety by exploring these resources:

*Stay up to date by subscribing to*
[*NVIDIA news*](https://nvda.ws/3u5KPv1)
*, joining the*
[*community*](https://developer.nvidia.com/omniverse/community)
*and following NVIDIA Omniverse on*
[*Instagram*](https://www.instagram.com/nvidiaomniverse/)
*,*
[*LinkedIn*](https://www.linkedin.com/showcase/nvidia-omniverse/)
*,*
[*Medium*](https://medium.com/@nvidiaomniverse)
*and*
[*X*](https://twitter.com/nvidiaomniverse)
*.*