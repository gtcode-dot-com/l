---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-23T05:48:08.744563+00:00'
exported_at: '2026-03-23T05:48:11.253690+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/build-robots-with-ai
structured_data:
  about: []
  author: ''
  description: The latest open models and frameworks from NVIDIA bring together simulation,
    robot learning and embedded compute to accelerate cloud-to-robot workflows.
  headline: 'From Simulation to Production: How to Build Robots With AI'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/build-robots-with-ai
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'From Simulation to Production: How to Build Robots With AI'
updated_at: '2026-03-23T05:48:08.744563+00:00'
url_hash: 274199774038a5e1ac1a3e18eca6462de4c3aa69
---

The next generation of robots will be generalist-specialists — capable of understanding instructions and learning broad skills while also trainable for specialized tasks.

Think of them as jacks of all trades that can also master specific jobs.

Building these robots requires integrated cloud-to-robot workflows that make it seamless to collect and generate data, train and evaluate control policies, and deploy them safely onto physical machines.​ These generalist-specialist systems depend on reasoning
[vision language action (VLA) models](https://www.nvidia.com/en-us/glossary/reasoning-vision-language-action/)

to perceive, understand and act intelligently across diverse tasks.

To accelerate this shift, the open
[NVIDIA Isaac](https://www.nvidia.com/en-us/industries/robotics/)

platform provides
[robotics developers](https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world)

with everything they need — models, data pipelines, simulation frameworks, runtime libraries — to build a robot and deploy it at scale with NVIDIA’s
[three-computer solution](https://blogs.nvidia.com/blog/three-computers-robotics/)

. NVIDIA even provides an open VLA model,
[NVIDIA Isaac GR00T N](https://developer.nvidia.com/isaac/gr00t)

, which gives developers a powerful foundation to bootstrap and post-train their own robotic intelligence.

These models, libraries and frameworks can run in the cloud or on edge AI infrastructure — and can now be further accelerated with the integration of long-running agents like OpenClaw.

With the latest agent-friendly NVIDIA Isaac GR00T models,
[Isaac robot simulation and learning frameworks](https://developer.nvidia.com/isaac)

, as well as edge AI systems announced this week at
[NVIDIA GTC](https://www.nvidia.com/gtc/)

, NVIDIA is giving developers new, powerful tools for the generalist-specialist era of autonomy.

These workflows are open and composable, so developers can mix and match components, bring their own tools and data, and accelerate their pipeline from prototype to real-world deployment.

*[Agility](https://www.agilityrobotics.com/content/agility-and-ai)
uses NVIDIA Isaac open frameworks to bring its robots from simulation to reality.*

It all starts with data.

## **Turning Compute Into Data**

Just a couple years ago, scaling a robotics pipeline depended on a developer’s ability to manually collect data: A robot’s learning depended on its exposure to different scenarios and real-world environments.

NVIDIA open libraries and frameworks change the equation by blending real-world signals — sensor logs and teleoperation demonstrations — with simulation-generated data to quickly turn cloud compute into large quantities of usable data.

Generating high-fidelity, physically accurate synthetic data helps robotics developers overcome the limitations of physical data collection, where it can be difficult or impossible to gather enough information about rare edge cases. These edge cases may be hard or unsafe to capture physically, but they’re essential for a robot to master before deploying at scale in unpredictable, real-world environments.

While synthetic data today makes up just 20% of AI training data for edge scenarios, it’s expected to constitute more than 90% of edge scenario data by 2030, according to a report by Gartner.

NVIDIA is propelling this shift with libraries and open frameworks that fuel an entire factory for realistic synthetic data based on the physical world.

[NVIDIA Omniverse NuRec](https://docs.nvidia.com/nurec/)

accelerated 3D Gaussian splatting libraries, now in general availability, turn real-world sensor data into OpenUSD-based interactive simulations in
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)

, an open source robotics simulation framework. This enables developers to scan and recreate real worlds from sensor data, making it easy to safely test robots in simulations based on real physical interactions.

*Using NVIDIA Omniverse NuRec and
[FieldAI](https://www.fieldai.com/news/fieldai-and-nvidia-omniverse-building-the-next-generation-of-industrial-ai)
’s world-class robot foundation models, FieldAI enables industrial customers to effortlessly deploy robotics and physical AI into their workflows.*

Real data can also be brought in from other devices using teleoperation.
[NVIDIA Isaac Teleop](https://nvidia.github.io/IsaacTeleop)

, also in general availability, enables developers to harness data collected through teleoperation devices — like extended-reality headsets, body trackers and gloves — to create demo data in the real world and in simulation that can be used to train robots in simulation environments like
[NVIDIA Isaac Lab](https://developer.nvidia.com/isaac/lab)

.

These datasets are then amplified using the new
[NVIDIA Physical AI Data Factory Blueprint](https://nvidianews.nvidia.com/news/nvidia-announces-open-physical-ai-data-factory-blueprint-to-accelerate-robotics-vision-ai-agents-and-autonomous-vehicle-development)

that unifies data augmentation, evaluation and orchestration into a single pipeline.

Powered by
[NVIDIA Cosmos](https://www.nvidia.com/en-us/ai/cosmos/)

open
[world foundation models](https://www.nvidia.com/en-us/glossary/world-models/)

and
[NVIDIA OSMO](https://developer.nvidia.com/osmo)

, an open source, agentic orchestrator, this reference workflow provides a scalable, production-ready data engine for robotics. Using the blueprint, developers can turn a single real-world scenario into new and varied synthetic possibilities in a fraction of the time it would take to collect similar data in the real world.

In addition to simulating the environment and data, robot builders need to simulate the robot itself. Using
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)

, developers can choose from an array of humanoids, autonomous mobile robots and robot arms, and rig the virtual model to real-world specifications.

*Isaac Sim integrates with*
[*PTC Onshape*](https://www.onshape.com/en/blog/robotics-development-cloud-native-cad-simulation-ptc-onshape-nvidia-isaac-sim)
*so developers can easily rig and modify their robots in simulation.*

The robot is rendered in
[OpenUSD](https://developer.nvidia.com/openusd)

, so it can seamlessly interact with the generated data and environment. Robot movements and trajectories can be recorded, replayed and used to train AI models — all safely in simulation before ever touching real hardware.

## **Putting AI Through Its Paces: Policy Training**

Once the teaching materials — the datasets — are gathered, it’s time for the robot to learn new tasks. This starts with the robot brain, powered by reasoning VLAs such as GR00T.

The VLA can be post-trained using data specific to its intended task. For example, a laundry-folding robot must be trained to grasp a clothing item, identify its shape, fold it correctly and stack it neatly atop other folded items. A cooking robot might need to become an expert at slicing, stirring and sauteeing ingredients. And a hospital care robot must learn how to navigate a hallway, find an elevator and hand items to clinicians or patients.

*A robot arm learns how to fold a shirt in NVIDIA Isaac Sim using simulation data from*
[*Lightwheel*](https://lightwheel.ai/media/simready)
*.*

Once the VLA is
[post-trained](https://blogs.nvidia.com/blog/ai-scaling-laws/#post-training-scaling)

, developers can then put the robot policy through its paces.

Training robots like these in the real world would be prohibitively slow, expensive and risky. So developers train in simulation with frameworks like the recently announced Isaac Lab 3.0, which gives robots thousands of lightweight, physically based simulation environments running in parallel so they can safely practice many scenarios at once — learning in days what would take years in the real world.

[*Hexagon Robotics’*](https://robotics.hexagon.com/industrial-autonomy-hexagon-robotics-nvidia-physical-ai)
*AEON humanoid learns to walk up and down stairs in parallel in NVIDIA Isaac Lab.*

Isaac Lab is integrated with
[Newton](https://developer.nvidia.com/newton-physics)

, an open source physics engine for robot learning. With Newton, developers can couple different types of physics solvers — which apply laws like gravity and inertia as well as collision constraints to compute how objects move, ensuring simulations behave realistically. These help developers simulate how a robot interacts with soft objects like cloth, or traverses through terrains like snow or gravel.

VIDEO

Robotics developers can also tap NVIDIA Isaac libraries and AI models that provide the core building blocks for manipulation and mobility tasks, optimized for runtime deployment at the edge.

* **Isaac for Manipulation**

  : Enables robots to perceive objects, understand their geometry and pose, and grasp them. Developers combine these perception models with GPU-accelerated motion generation so their robots can plan and replan quickly in cluttered, changing scenes.
* **Isaac for Mobility**

  : Provides the foundation for robots to localize, map and navigate safely. Developers use GPU-accelerated visual odometry and
  [SLAM](https://blogs.nvidia.com/blog/what-is-simultaneous-localization-and-mapping-nvidia-jetson-isaac-sdk/)

  for robust positioning, paired with real-time 3D reconstruction to navigate around obstacles and environment changes.

[*1X’*](http://1x.tech/discover/nvidia-gtc-2026)
*s NEO robots learn to walk across different types of terrain in NVIDIA Isaac Lab.*

To ensure that simulation-based lessons translate to the real world, Newton — as well as physics engines
[NVIDIA PhysX](https://www.nvidia.com/en-us/drivers/physx/physx-9-19-0218-driver/)

and Google DeepMind’s Mujoco — are supported in Isaac Sim and Isaac Lab. This makes it easy for developers to transition between frameworks without needing to adjust their robots.

Training on a single skill is not enough — developers need to be sure a robot’s skill can translate across environments and tasks. The latest
[Isaac Lab-Arena](https://developer.nvidia.com/isaac/lab-arena)

release unlocks large-scale task setup and policy evaluation, simplifying environment composition and accelerating complex task creation to help developers evaluate various tasks in parallel. Isaac Lab-Arena connects to industrial and academic benchmarks such as LIBERO, RoboTwin and NIST so developers can easily evaluate their progress.

## **Testing, Testing — A Critical Step Before Deployment**

Before they can be deployed, robots must test what they’ve learned repeatedly across diverse conditions. Every detail — from robot motion and manipulation to the way robot dynamics react to each task — must be evaluated before it operates in the real world.

[*Cyngn*](https://www.cyngn.com/pr/at-gtc-cyngn-advances-high-fidelity-forklift-simulation-through-fmu-integration)
*tests a forklift’s tire dynamics in NVIDIA Isaac Sim as it moves across various inclines.*

Comprehensive testing includes both software-in-the-loop, where just the robotics software stack is tested, and hardware-in-the-loop, which tests how the stack runs on a robotic brain (the edge compute).

Isaac Sim enables both hardware-in-the-loop and software-in-the-loop testing, so developers can easily flip between real and simulated environments as they test and iterate.

[*Wandelbots*](https://www.wandelbots.com/post/bringing-embodied-ai-to-life-simplifying-robotics-development-with-wandelbots-nova-and-nvidia-isaac)
*tests factory automation robots in high-fidelity simulation environments using NVIDIA Isaac Sim.*

The latest Isaac Sim release is designed to help developers move seamlessly between workflows. It supports NuRec rendering for easy data input, while multiple physics backends enable robots to go between Isaac Sim and Isaac Lab without major modifications.

It also connects directly to
[Mega](https://blogs.nvidia.com/blog/mega-omniverse-blueprint/)

, an NVIDIA Blueprint for developing, testing and optimizing physical AI and robot fleets at scale in a
[digital twin](https://www.nvidia.com/en-us/glossary/digital-twin/)

. This allows robotics developers to scale testing from one robot to a few or an entire fleet.

[*Idealworks*](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.idealworks.com%2Fen%2Fnews%2Fsick-idealworks-simulation-orchestration-nvidia-gtc&data=05%7C02%7Ckburke%40nvidia.com%7C819a5c191e484888058408de8323f8a1%7C43083d15727340c1b7db39efd9ccc17a%7C0%7C0%7C639092387771837452%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=mRQwAW%2BIHl5ocyCXAML4AL6n%2FhSgkQT66h6RT7GgSbo%3D&reserved=0)
*tests multiple robots at once in a physically based factory setting using NVIDIA Isaac Sim and Mega.*

## **Running in the Real World With NVIDIA Isaac Workflows, Jetson Modules**

Once ready to deploy, developers need high-performance compute that runs models seamlessly, processes diverse high-speed sensor data and supports a wide variety of robot shapes and sizes at the edge.

The
[NVIDIA Jetson](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/)

family — including Jetson Thor and Jetson Orin — supports the full range of AI-powered robots with real-time sensing and AI reasoning, from small manipulators to full-sized humanoids.

In addition, NVIDIA Isaac runtime libraries optimize how the robotics policy runs at the edge. The latest open source
[cuVSLAM library](https://github.com/nvidia-isaac/cuVSLAM)
helps robots see where they are and build a map in real time, using an embedded computer powered by Jetson to track movement accurately and reliably.

## **Researching New Frontiers**

As robots become generalist-specialists, researchers need evolvable workflows that make it easy to iterate on existing skills instead of needing to rebuild from scratch.

[SOMA-X](https://github.com/NVlabs/SOMA-X)

, a new open research framework from NVIDIA, helps by standardizing how skeletons, motion and identity are represented across AI, simulation and real robots.

With SOMA-X, teams can swap in different body models or robot platforms without constantly redoing rigging, motion retargeting or integration work — keeping Isaac Sim, Isaac Lab and GR00T-based pipelines stable as hardware and software advances.

As new body models, datasets or hardware show up, developers can plug into the same shared SOMA-X representation without breaking existing tools or long-running agents like OpenClaw that are constantly training, evaluating and deploying new behaviors.

On top of this shared body layer, a new foundation model called GEAR-SONIC, now available to researchers, delivers powerful capabilities for humanoids. Trained on large-scale human motion data in Isaac Lab, SONIC teaches robots a wide range of natural whole-body skills — like walking, crawling and manipulating objects — using a single unified policy instead of multiple task-specific controllers.

## **Safety Tools, Resources to Get Started**

The NVIDIA robotics stack is complemented by safety tooling and starter resources to help teams quickly move from experimentation to reliable systems deployed at scale.

* [**NVIDIA Halos**](https://www.nvidia.com/en-us/ai-trust-center/halos/autonomous-vehicles/)

  : This comprehensive, full-stack safety system is designed to ensure the safe development, training and deployment of robotics with end-to-end safety guardrails from the cloud to the robot.
* [**NVIDIA GR00T X-Embodiment**](https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-GR00T-X-Embodiment-Sim)

  : This dataset includes the same data used to post-train NVIDIA GR00T. It’s been downloaded more than 10 million times from Hugging Face.
* [Bones Studio](https://bones.studio/)
  is releasing
  [BONES-SEED](https://huggingface.co/datasets/bones-studio/seed)

  , a massive library of 140,000 human motion animations designed to train humanoid robots. Each motion is richly labeled with descriptions and timestamps, giving robotics teams a ready-to-use foundation to build smarter, more lifelike robots — available through the
  [**NVIDIA Physical AI Open Dataset collection**](https://huggingface.co/collections/nvidia/physical-ai)

  on Hugging Face.
* **Educational resources**

  : For new robotics developers,
  [Isaac Sim and Isaac Lab](https://www.nvidia.com/en-us/learn/learning-path/robotics/)

  learning paths are available to guide development. And the
  [NVIDIA Deep Learning Institute](https://www.nvidia.com/en-us/training/)

  offers self-paced and instructor-led courses to kickstart the robotics development journey.

*Watch the*
[*GTC keynote*](https://www.nvidia.com/gtc/keynote/)
*from NVIDIA founder and CEO Jensen Huang and explore*
[*physical AI*](https://www.nvidia.com/gtc/sessions/physical-ai-days/)
*,*
[*robotics*](https://www.nvidia.com/gtc/sessions/robotics/)
*and*
[*vision AI*](https://www.nvidia.com/gtc/sessions/computer-vision-and-video-analytics/)
*sessions.*