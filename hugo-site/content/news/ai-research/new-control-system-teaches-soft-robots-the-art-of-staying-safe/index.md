---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-03T00:03:20.359009+00:00'
exported_at: '2025-12-03T00:03:22.798246+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/new-control-system-teaches-soft-robots-art-staying-safe-1202
structured_data:
  about: []
  author: ''
  description: System developed by researchers at MIT CSAIL and LIDS uses rigorous
    mathematics to ensure robots flex, adapt, and interact with people and objects
    in a safe and precise way. It helps robots remain flexible and responsive while
    mathematically guaranteeing they won’t exceed safe force limits.
  headline: New control system teaches soft robots the art of staying safe
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/new-control-system-teaches-soft-robots-art-staying-safe-1202
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New control system teaches soft robots the art of staying safe
updated_at: '2025-12-03T00:03:20.359009+00:00'
url_hash: da5430278526d64099bc66e8c269f42502f7bc9b
---

Imagine having a continuum soft robotic arm bend around a bunch of grapes or broccoli, adjusting its grip in real time as it lifts the object. Unlike traditional rigid robots that generally aim to avoid contact with the environment as much as possible and stay far away from humans for safety reasons, this arm senses subtle forces, stretching and flexing in ways that mimic more of the compliance of a human hand. Its every motion is calculated to avoid excessive force while achieving the task efficiently. In MIT Computer Science and Artificial Intelligence Laboratory (CSAIL) and Laboratory for Information and Decisions Systems (LIDS) labs, these seemingly simple movements are the culmination of complex mathematics, careful engineering, and a vision for robots that can safely interact with humans and delicate objects.

Soft robots, with their deformable bodies, promise a future where machines move more seamlessly alongside people, assist in caregiving, or handle delicate items in industrial settings. Yet that very flexibility makes them difficult to control. Small bends or twists can produce unpredictable forces, raising the risk of damage or injury. This motivates the need for safe control strategies for soft robots.

“Inspired by advances in safe control and formal methods for rigid robots, we aim to adapt these ideas to soft robotics — modeling their complex behavior and embracing, rather than avoiding, contact — to enable higher-performance designs (e.g., greater payload and precision) without sacrificing safety or embodied intelligence,” says lead senior author and MIT Assistant Professor Gioele Zardini, who is a principal investigator in LIDS and the Department of Civil and Environmental Engineering, and an affiliate faculty with the Institute for Data, Systems, and Society (IDSS). “This vision is shared by recent and parallel work from other groups.”

**Safety first**

The team developed a new framework that blends nonlinear control theory (controlling systems that involve highly complex dynamics) with advanced physical modeling techniques and efficient real-time optimization to produce what they call “contact-aware safety.” At the heart of the approach are high-order control barrier functions (HOCBFs) and high-order control Lyapunov functions (HOCLFs). HOCBFs define safe operating boundaries, ensuring the robot doesn’t exert unsafe forces. HOCLFs guide the robot efficiently toward its task objectives, balancing safety with performance.

“Essentially, we’re teaching the robot to know its own limits when interacting with the environment while still achieving its goals,” says MIT Department of Mechanical Engineering PhD student Kiwan Wong, the lead author of a new paper describing the framework. “The approach involves some complex derivation of soft robot dynamics, contact models, and control constraints, but the specification of control objectives and safety barriers is rather straightforward for the practitioner, and the outcomes are very tangible, as you see the robot moving smoothly, reacting to contact, and never causing unsafe situations.”

“Compared with traditional kinematic CBFs — where forward-invariant safe sets are hard to specify — the HOCBF framework simplifies barrier design, and its optimization formulation accounts for system dynamics (e.g., inertia), ensuring the soft robot stops early enough to avoid unsafe contact forces,” says Worcester Polytechnic Institute Assistant Professor and former CSAIL postdoc Wei Xiao.

“Since soft robots emerged, the field has highlighted their embodied intelligence and greater inherent safety relative to rigid robots, thanks to passive material and structural compliance. Yet their “cognitive” intelligence — especially safety systems — has lagged behind that of rigid serial-link manipulators,” says co-lead author Maximilian Stölzle, a research intern at Disney Research and formerly a Delft University of Technology PhD student and visiting researcher at MIT LIDS and CSAIL. “This work helps close that gap by adapting proven algorithms to soft robots and tailoring them for safe contact and soft-continuum dynamics.”

The LIDS and CSAIL team tested the system on a series of experiments designed to challenge the robot’s safety and adaptability. In one test, the arm pressed gently against a compliant surface, maintaining a precise force without overshooting. In another, it traced the contours of a curved object, adjusting its grip to avoid slippage. In yet another demonstration, the robot manipulated fragile items alongside a human operator, reacting in real time to unexpected nudges or shifts. “These experiments show that our framework is able to generalize to diverse tasks and objectives, and the robot can sense, adapt, and act in complex scenarios while always respecting clearly defined safety limits,” says Zardini.

Soft robots with contact-aware safety could be a real value-add in high-stakes places, of course. In health care, they could assist in surgeries, providing precise manipulation while reducing risk to patients. In industry, they might handle fragile goods without constant supervision. In domestic settings, robots could help with chores or caregiving tasks, interacting safely with children or the elderly — a key step toward making soft robots reliable partners in real-world environments.

“Soft robots have incredible potential,” says co-lead senior author Daniela Rus, director of CSAIL and a professor in the Department of Electrical Engineering and Computer Science. “But ensuring safety and encoding motion tasks via relatively simple objectives has always been a central challenge. We wanted to create a system where the robot can remain flexible and responsive while mathematically guaranteeing it won’t exceed safe force limits.”

**Combining soft robot models, differentiable simulation, and control theory**

Underlying the control strategy is a differentiable implementation of something called the Piecewise Cosserat-Segment (PCS) dynamics model, which predicts how a soft robot deforms and where forces accumulate. This model allows the system to anticipate how the robot’s body will respond to actuation and complex interactions with the environment. “The aspect that I most like about this work is the blend of integration of new and old tools coming from different fields like advanced soft robot models, differentiable simulation, Lyapunov theory, convex optimization, and injury-severity–based safety constraints. All of this is nicely blended into a real-time controller fully grounded in first principles,” says co-author Cosimo Della Santina, who is an associate professor at Delft University of Technology.

Complementing this is the Differentiable Conservative Separating Axis Theorem (DCSAT), which estimates distances between the soft robot and obstacles in the environment that can be approximated with a chain of convex polygons in a differentiable manner. “Earlier differentiable distance metrics for convex polygons either couldn’t compute penetration depth — essential for estimating contact forces — or yielded non-conservative estimates that could compromise safety,” says Wong. “Instead, the DCSAT metric returns strictly conservative, and therefore safe, estimates while simultaneously allowing for fast and differentiable computation.” Together, PCS and DCSAT give the robot a predictive sense of its environment for more proactive, safe interactions.

Looking ahead, the team plans to extend their methods to three-dimensional soft robots and explore integration with learning-based strategies. By combining contact-aware safety with adaptive learning, soft robots could handle even more complex, unpredictable environments.

“This is what makes our work exciting,” says Rus. “You can see the robot behaving in a human-like, careful manner, but behind that grace is a rigorous control framework ensuring it never oversteps its bounds.”

“Soft robots are generally safer to interact with than rigid-bodied robots by design, due to the compliance and energy-absorbing properties of their bodies,” says University of Michigan Assistant Professor Daniel Bruder, who wasn’t involved in the research. “However, as soft robots become faster, stronger, and more capable, that may no longer be enough to ensure safety. This work takes a crucial step towards ensuring soft robots can operate safely by offering a method to limit contact forces across their entire bodies.”


The team’s work was supported, in part, by The Hong Kong Jockey Club Scholarships, the European Union’s Horizon Europe Program, Cultuurfonds Wetenschapsbeurzen, and the Rudge (1948) and Nancy Allen Chair. Their work was published earlier this month in the Institute of Electrical and Electronics Engineers’
*Robotics and Automation Letters*
.