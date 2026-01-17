---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-17T14:15:26.054574+00:00'
exported_at: '2026-01-17T14:15:28.649428+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/japan-science-technology-agency-develops-moonshot-robot
structured_data:
  about: []
  author: ''
  description: Using NVIDIA Isaac Sim and RTX GPUs, humanoid robot research will automate
    cooking, cleaning, repositioning and other caregiving tasks.
  headline: Japan Science and Technology Agency Develops NVIDIA-Powered Moonshot Robot
    for Elderly Care
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/japan-science-technology-agency-develops-moonshot-robot
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Japan Science and Technology Agency Develops NVIDIA-Powered Moonshot Robot
  for Elderly Care
updated_at: '2026-01-17T14:15:26.054574+00:00'
url_hash: 1ccd6bba9db0804cefac8d171cff6441e03b1fe0
---

The next universal technology since the smartphone is on the horizon — and it may be a little less pocket friendly.

The
[Moonshot](https://www.jst.go.jp/moonshot/en/index.html)
research program, funded by the Japan Science and Technology Agency and accelerated by NVIDIA AI and robotics technologies, is working to create a world by 2050 where AI-powered, autonomously learning robots are integrated into Japanese citizens’ everyday lives.

That’s just
[goal No. 3](https://www.jst.go.jp/moonshot/en/program/goal3/)
of the broader Moonshot initiative, which includes researchers from across Japan’s universities and comprises 10 ambitious technology goals — from ultra-early disease prediction to sustainable resource circulation.

In light of Japan’s rising elderly population, many of the research projects underway center on how robots can aid in senior care. This includes designing a robot that’s capable of caregiving tasks like cooking, cleaning and hygiene care.

## **NVIDIA Architecture Powers On Moonshot Robots**

NVIDIA technologies are integrated into every level of the Moonshot project’s senior care robots known as AI-Driven Robot for Embrace and Care, or AIREC.

Dry-AIREC robot, the larger and more mobile member of the Moonshot family, has two NVIDIA GPUs onboard. For AIREC-Basic, primarily used for data collection for the motion foundation model, three
[NVIDIA Jetson Orin NX](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)
modules power AI processing at the edge.

![Pictured are two Moonshot robots AIREC-Basic (left) and AIREC-Basic (right). ](https://blogs.nvidia.com/wp-content/uploads/2026/01/thumbnail_image.png)


Pictured is AIREC-Basic (left) and AIREC-Basic (right).

Plus,
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)
, an open-source
[robotic simulation](https://www.nvidia.com/en-us/use-cases/robotics-simulation/)
framework, was used to train the
[AIREC](https://airec-waseda.jp/en/toppage_en/)
robots to perform specific tasks, such as estimating the forces between objects.

VIDEO

The integration of NVIDIA technologies and AI into the robot development process has allowed this project to go from a far-fetched dream to reality faster than imagined.

“Five years ago, before generative AI, few people believed that this application was possible,” said Tetsuya Ogata, professor and director of the Institute for AI and Robotics at Waseda University. “Now, the atmosphere surrounding this technology has changed, so we can seriously think about this kind of application.”

## **Building a Full Set of Caregiving Capabilities**

Additional research projects are underway to develop the Moonshot robot’s elderly-care capabilities.

“We’re focusing on things like changing diapers, helping patients take baths and providing meal assistance, so those actions can be supported by the robots, and caregivers can focus on improving the patients’ lives,” said Misa Matsumura, a bioengineering master’s student at the University of Tokyo.

A recent paper by Matsumura — presented at the IEEE/RSJ International Conference on Intelligent Robots and Systems — focused on repositioning, an essential action in elderly care to prevent bed sores and enable diaper changing.

Automating repositioning with a
[humanoid robot](https://www.nvidia.com/en-us/glossary/humanoid-robot/)
— while considering the elderly care patients’ personal states and bodily needs — is no easy feat.

VIDEO

To train the Dry-AIREC robots for this research endeavor, Matsumura’s team used laptops powered by NVIDIA RTX GPUs.

Matsumura used 3D posture estimation, trajectory calculations and force estimation to further develop the robots’ capabilities.

Dry-AIREC’s fisheye and depth cameras helped assess the movements required to reposition patients. The exact repositioning method needed for a patient is found through trajectory calculations based on movement data from skilled caregivers.

The robot must also use the right amount of force in repositioning to complete the action without causing the patient pain. By predicting the pressure required to press the shoulders and knees, it determines the appropriate timing for movement — enabling actions with the ideal applied force.

Preliminary experiments were done using mannequins, and Matsumura’s research has now advanced to incorporate humans testing the robots. Matsumura is conducting ongoing research to further improve this action for Dry-AIREC.

![Three illustrations of Moonshot robots performing caregiving activities including folding laundry, cooking food and washing a patient. ](https://blogs.nvidia.com/wp-content/uploads/2026/01/Copy-of-Blog-1280x680.pptx-1.jpg)


Milestone images for goal No. 3 for the Japan Science and Technology Agency.

Among the many projects within the Moonshot program, developing robots for elderly care has particular significance for some of the researchers due to the project’s social and personal implications.

“Although my study focus is on medical robotics, I decided to join this project because my mother is growing older, and that experience has given me an appreciation for the importance of personal care,” said Etsuko Kobayashi, professor of bioengineering at the University of Tokyo and Matsumura’s graduate advisor. “I found that my experience in medical robotics can be meaningfully extended to care robotics, contributing to the development of safe and reliable robotic systems for human-centered applications.”

The Moonshot team for goal No. 3 will showcase their progress at the
[2026 International Symposium on System Integration](https://sice-si.org/SII2026/)
in January.

*Learn more about*
[*NVIDIA Isaac Sim*](https://developer.nvidia.com/isaac/sim)
*.*