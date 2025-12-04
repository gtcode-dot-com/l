---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-04T00:03:19.514191+00:00'
exported_at: '2025-12-04T00:03:21.960172+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/mit-engineers-design-aerial-microrobot-fly-like-bumblebee-1203
structured_data:
  about: []
  author: ''
  description: MIT researchers developed an aerial microrobot that can fly with speed
    and agility comparable to real insects. The research opens the door to future
    bug-sized robots that could aid in search-and-rescue missions.
  headline: MIT engineers design an aerial microrobot that can fly as fast as a bumblebee
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/mit-engineers-design-aerial-microrobot-fly-like-bumblebee-1203
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MIT engineers design an aerial microrobot that can fly as fast as a bumblebee
updated_at: '2025-12-04T00:03:19.514191+00:00'
url_hash: b11cd3005f36f45784b7228b300b5a3eaa255f29
---

In the future, tiny flying robots could be deployed to aid in the search for survivors trapped beneath the rubble after a devastating earthquake. Like real insects, these robots could flit through tight spaces larger robots can’t reach, while simultaneously dodging stationary obstacles and pieces of falling rubble.

So far, aerial microrobots have only been able to fly slowly along smooth trajectories, far from the swift, agile flight of real insects — until now.

MIT researchers have demonstrated aerial microrobots that can fly with speed and agility that is comparable to their biological counterparts. A collaborative team designed a new AI-based controller for the robotic bug that enabled it to follow gymnastic flight paths, such as executing continuous body flips.

With a two-part control scheme that combines high performance with computational efficiency, the robot’s speed and acceleration increased by about 450 percent and 250 percent, respectively, compared to the researchers’ best previous demonstrations.

The speedy robot was agile enough to complete 10 consecutive somersaults in 11 seconds, even when wind disturbances threatened to push it off course.

![Animation of a flying, flipping microrobot](/sites/default/files/images/inline/MIT-Microrobot-demo-05-press.gif)


A microrobot flips 10 times in 11 seconds.


Credit: Courtesy of the Soft and Micro Robotics Laboratory

“We want to be able to use these robots in scenarios that more traditional quad copter robots would have trouble flying into, but that insects could navigate. Now, with our bioinspired control framework, the flight performance of our robot is comparable to insects in terms of speed, acceleration, and the pitching angle. This is quite an exciting step toward that future goal,” says Kevin Chen, an associate professor in the Department of Electrical Engineering and Computer Science (EECS), head of the Soft and Micro Robotics Laboratory within the Research Laboratory of Electronics (RLE), and co-senior author of a
[paper on the robot](http://doi.org/10.1126/sciadv.aea8716)
.

Chen is joined on the paper by co-lead authors Yi-Hsuan Hsiao, an EECS MIT graduate student; Andrea Tagliabue PhD ’24; and Owen Matteson, a graduate student in the Department of Aeronautics and Astronautics (AeroAstro); as well as EECS graduate student Suhan Kim; Tong Zhao MEng ’23; and co-senior author Jonathan P. How, the Ford Professor of Engineering in the Department of Aeronautics and Astronautics and a principal investigator in the Laboratory for Information and Decision Systems (LIDS). The research appears today in
*Science Advances*
.

**An AI controller**

Chen’s group has been building robotic insects for more than five years.

They recently developed a
[more durable version of their tiny robot](https://news.mit.edu/2025/fast-agile-robotic-insect-could-someday-aid-mechanical-pollination-0115)
, a microcassette-sized device that weighs less than a paperclip. The new version utilizes larger, flapping wings that enable more agile movements. They are powered by a set of squishy artificial muscles that flap the wings at an extremely fast rate.

But the controller — the “brain” of the robot that determines its position and tells it where to fly — was hand-tuned by a human, limiting the robot’s performance.

For the robot to fly quickly and aggressively like a real insect, it needed a more robust controller that could account for uncertainty and perform complex optimizations quickly.

Such a controller would be too computationally intensive to be deployed in real time, especially with the complicated aerodynamics of the lightweight robot.

To overcome this challenge, Chen’s group joined forces with How’s team and, together, they crafted a two-step, AI-driven control scheme that provides the robustness necessary for complex, rapid maneuvers, and the computational efficiency needed for real-time deployment.

“The hardware advances pushed the controller so there was more we could do on the software side, but at the same time, as the controller developed, there was more they could do with the hardware. As Kevin’s team demonstrates new capabilities, we demonstrate that we can utilize them,” How says.

For the first step, the team built what is known as a model-predictive controller. This type of powerful controller uses a dynamic, mathematical model to predict the behavior of the robot and plan the optimal series of actions to safely follow a trajectory.

While computationally intensive, it can plan challenging maneuvers like aerial somersaults, rapid turns, and aggressive body tilting. This high-performance planner is also designed to consider constraints on the force and torque the robot could apply, which is essential for avoiding collisions.

For instance, to perform multiple flips in a row, the robot would need to decelerate in such a way that its initial conditions are exactly right for doing the flip again.

“If small errors creep in, and you try to repeat that flip 10 times with those small errors, the robot will just crash. We need to have robust flight control,” How says.

They use this expert planner to train a “policy” based on a deep-learning model, to control the robot in real time, through a process called imitation learning. A policy is the robot’s decision-making engine, which tells the robot where and how to fly.

Essentially, the imitation-learning process compresses the powerful controller into a computationally efficient AI model that can run very fast.

The key was having a smart way to create just enough training data, which would teach the policy everything it needs to know for aggressive maneuvers.

“The robust training method is the secret sauce of this technique,” How explains.

The AI-driven policy takes robot positions as inputs and outputs control commands in real time, such as thrust force and torques.

**Insect-like performance**

In their experiments, this two-step approach enabled the insect-scale robot to fly 447 percent faster while exhibiting a 255 percent increase in acceleration. The robot was able to complete 10 somersaults in 11 seconds, and the tiny robot never strayed more than 4 or 5 centimeters off its planned trajectory.

“This work demonstrates that soft and microrobots, traditionally limited in speed, can now leverage advanced control algorithms to achieve agility approaching that of natural insects and larger robots, opening up new opportunities for multimodal locomotion,” says Hsiao.

The researchers were also able to demonstrate saccade movement, which occurs when insects pitch very aggressively, fly rapidly to a certain position, and then pitch the other way to stop. This rapid acceleration and deceleration help insects localize themselves and see clearly.

“This bio-mimicking flight behavior could help us in the future when we start putting cameras and sensors on board the robot,” Chen says.

Adding sensors and cameras so the microrobots can fly outdoors, without being attached to a complex motion capture system, will be a major area of future work.

The researchers also want to study how onboard sensors could help the robots avoid colliding with one another or coordinate navigation.

“For the micro-robotics community, I hope this paper signals a paradigm shift by showing that we can develop a new control architecture that is high-performing and efficient at the same time,” says Chen.

“This work is especially impressive because these robots still perform precise flips and fast turns despite the large uncertainties that come from relatively large fabrication tolerances in small-scale manufacturing, wind gusts of more than 1 meter per second, and even its power tether wrapping around the robot as it performs repeated flips,” says Sarah Bergbreiter, a professor of mechanical engineering at Carnegie Mellon University, who was not involved with this work.

“Although the controller currently runs on an external computer rather than onboard the robot, the authors demonstrate that similar, but less precise, control policies may be feasible even with the more limited computation available on an insect-scale robot. This is exciting because it points toward future insect-scale robots with agility approaching that of their biological counterparts,” she adds.

This research is funded, in part, by the National Science Foundation (NSF), the Office of Naval Research, Air Force Office of Scientific Research, MathWorks, and the Zakhartchenko Fellowship.