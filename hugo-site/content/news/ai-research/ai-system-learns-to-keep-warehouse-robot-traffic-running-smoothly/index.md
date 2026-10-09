---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:59:15.794177+00:00'
exported_at: '2026-04-02T04:59:19.848779+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/ai-system-keeps-warehouse-robot-traffic-running-smoothly-0326
structured_data:
  about: []
  author: ''
  description: A new system increases throughput in automated warehouses by adaptively
    determining which robots should go first to avoid congestion and collisions. The
    work was led by researchers from MIT and Symbotic.
  headline: AI system learns to keep warehouse robot traffic running smoothly
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/ai-system-keeps-warehouse-robot-traffic-running-smoothly-0326
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AI system learns to keep warehouse robot traffic running smoothly
updated_at: '2026-04-02T04:59:15.794177+00:00'
url_hash: 923c9ca3b3fc9e8e0a5e61264bdc89accf29d097
---

Inside a giant autonomous warehouse, hundreds of robots dart down aisles as they collect and distribute items to fulfill a steady stream of customer orders. In this busy environment, even small traffic jams or minor collisions can snowball into massive slowdowns.

To avoid such an avalanche of inefficiencies, researchers from MIT and the tech firm Symbotic developed a new method that automatically keeps a fleet of robots moving smoothly. Their method learns which robots should go first at each moment, based on how congestion is forming, and adapts to prioritize robots that are about to get stuck. In this way, the system can reroute robots in advance to avoid bottlenecks.

The hybrid system utilizes deep reinforcement learning, a powerful artificial intelligence method for solving complex problems, to figure out which robots should be prioritized. Then, a fast and reliable planning algorithm feeds instructions to the robots, enabling them to respond rapidly in constantly changing conditions.

In simulations inspired by actual e-commerce warehouse layouts, this new approach achieved about a 25 percent gain in throughput over other methods. Importantly, the system can quickly adapt to new environments with different quantities of robots or varied warehouse layouts.

“There are a lot of decision-making problems in manufacturing and logistics where companies rely on algorithms designed by human experts. But we have shown that, with the power of deep reinforcement learning, we can achieve super-human performance. This is a very promising approach, because in these giant warehouses even a 2 or 3 percent increase in throughput can have a huge impact,” says Han Zheng, a graduate student in the Laboratory for Information and Decision Systems (LIDS) at MIT and lead author of a paper on this new approach.

Zheng is joined on the paper by Yining Ma, a LIDS postdoc; Brandon Araki and Jingkai Chen of Symbotic; and senior author Cathy Wu, the Class of 1954 Career Development Associate Professor in Civil and Environmental Engineering (CEE) and the Institute for Data, Systems, and Society (IDSS) at MIT, and a member of LIDS. The research
[appears today](https://jair.org/index.php/jair/article/view/20611)
in the
*Journal of Artificial Intelligence Research*
.

**Rerouting robots**

Coordinating hundreds of robots in an e-commerce warehouse simultaneously is no easy task.

The problem is especially complicated because the warehouse is a dynamic environment, and robots continually receive new tasks after reaching their goals. They need to be rapidly redirected as they leave and enter the warehouse floor.

Companies often leverage algorithms written by human experts to determine where and when robots should move to maximize the number of packages they can handle.

But if there is congestion or a collision, a firm may have no choice but to shut down the entire warehouse for hours to manually sort the problem out.

“In this setting, we don’t have an exact prediction of the future. We only know what the future might hold, in terms of the packages that come in or the distribution of future orders. The planning system needs to be adaptive to these changes as the warehouse operations go on,” Zheng says.

The MIT researchers achieved this adaptability using machine learning. They began by designing a neural network model to take observations of the warehouse environment and decide how to prioritize the robots. They train this model using deep reinforcement learning, a trial-and-error method in which the model learns to control robots in simulations that mimic actual warehouses. The model is rewarded for making decisions that increase overall throughput while avoiding conflicts.

Over time, the neural network learns to coordinate many robots efficiently.

“By interacting with simulations inspired by real warehouse layouts, our system receives feedback that we use to make its decision-making more intelligent. The trained neural network can then adapt to warehouses with different layouts,” Zheng explains.

It is designed to capture the long-term constraints and obstacles in each robot’s path, while also considering dynamic interactions between robots as they move through the warehouse.

By predicting current and future robot interactions, the model plans to avoid congestion before it happens.

After the neural network decides which robots should receive priority, the system employs a tried-and-true planning algorithm to tell each robot how to move from one point to another. This efficient algorithm helps the robots react quickly in the changing warehouse environment.

This combination of methods is key.

“This hybrid approach builds on my group’s work on how to achieve the best of both worlds between machine learning and classical optimization methods. Pure machine-learning methods still struggle to solve complex optimization problems, and yet it is extremely time- and labor-intensive for human experts to design effective methods. But together, using expert-designed methods the right way can tremendously simplify the machine learning task,” says Wu.

**Overcoming complexity**

Once the researchers trained the neural network, they tested the system in simulated warehouses that were different than those it had seen during training. Since industrial simulations were too inefficient for this complex problem, the researchers designed their own environments to mimic what happens in actual warehouses.

On average, their hybrid learning-based approach achieved 25 percent greater throughput than traditional algorithms as well as a random search method, in terms of number of packages delivered per robot. Their approach could also generate feasible robot path plans that overcame congestion caused by traditional methods.

“Especially when the density of robots in the warehouse goes up, the complexity scales exponentially, and these traditional methods quickly start to break down. In these environments, our method is much more efficient,” Zheng says.

While their system is still far away from real-world deployment, these demonstrations highlight the feasibility and benefits of using a machine learning-guided approach in warehouse automation.

In the future, the researchers want to include task assignments in the problem formulation, since determining which robot will complete each task impacts congestion. They also plan to scale up their system to larger warehouses with thousands of robots.

This research was funded by Symbotic.