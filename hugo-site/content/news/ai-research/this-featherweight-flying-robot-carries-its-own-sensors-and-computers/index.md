---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-19T01:23:50.331705+00:00'
exported_at: '2026-11-19T01:23:52.035585+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118
structured_data:
  about: []
  author: ''
  description: MIT researchers designed a featherweight, flying robot that can carry
    the electronics it needs to perform onboard sensing and computation. This enables
    the robot to fly quickly and precisely without being attached to a laboratory
    motion-capture system.
  headline: This featherweight, flying robot carries its own sensors and computers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/featherweight-flying-robot-carries-its-own-sensors-and-computers-1118
  publisher:
    logo: /favicon.ico
    name: GTCode
title: This featherweight, flying robot carries its own sensors and computers
updated_at: '2026-11-19T01:23:50.331705+00:00'
url_hash: 62626f8cbcfd5bbe5448ca2b0cf147af0a704577
---

The speedy microrobot flies without an attached motion-capture system, moving it closer to applications like agriculture or industrial surveillance.

To bring this tiny robot closer to real-world applications, the researchers need it to carry the additional weight from electronics for onboard sensing and computation, while still being fast, maneuverable, and robust to collisions.

In this research, they developed a method to scale up the artificial muscles without hampering the robot’s performance. They carefully tuned the radius and length of the soft actuators, increasing their size by 50 percent while boosting the robot’s net lift forces by 46 percent.

“It is very difficult to scale up the actuators without causing the output power of the system to go down, which reduces the lift forces. We tuned the geometry of the robot very precisely so lift proportionally increases with the additional actuator weight,” Chen explains.

They were able to achieve a lift-to-weight ratio of 1.9, giving the robot more than enough lift force to carry the onboard electronics package they developed, which weighs only 244 milligrams.

The tiny electronics package contains the sensors, and microcontroller needed for onboard sensing and computation.

The researchers incorporated an inertial measurement unit to estimate attitude, an optical flow sensor to estimate lateral flight speed and position, and a time-of-flight sensor to measure height.

But without the precision of the attached motion capture system, the robot does not know its absolute position, causing it to drift off course.

**Speedy sensing**

To overcome this challenge, the team designed a sensing algorithm to calculate the robot orientation, angular velocity, and position extremely quickly, simplifying the calculations to reduce the computational cost.

They found that estimating position continuously at a faster rate yielded higher performance than a more accurate, slower estimation.

“We spent a lot of time optimizing the selection of the sensors and position estimators so the robot would have very low drift. Our robot can now fly with positional accuracy that is comparable to flying with offboard cameras,” says Hsiao.

They integrated the sensors and computing components into a tiny electronics package, which they attached to a fiberglass substrate so it wouldn’t be thrown off by vibrations of the robot.