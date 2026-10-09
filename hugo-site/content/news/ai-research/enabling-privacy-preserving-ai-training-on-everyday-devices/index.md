---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-29T04:15:43.302967+00:00'
exported_at: '2026-04-29T04:15:45.547472+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/enabling-privacy-preserving-ai-training-everyday-devices-0429
structured_data:
  about: []
  author: ''
  description: MIT researchers developed a technique that accelerates a privacy-preserving
    approach for training AI models on edge devices. Their new framework could enable
    more accurate, efficient, and secure AI models to be used in under-resourced settings.
  headline: Enabling privacy-preserving AI training on everyday devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/enabling-privacy-preserving-ai-training-everyday-devices-0429
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Enabling privacy-preserving AI training on everyday devices
updated_at: '2026-04-29T04:15:43.302967+00:00'
url_hash: 9ea2870941c951c4bc71e432afacc99fa198391a
---

A new method developed by MIT researchers can accelerate a privacy-preserving artificial intelligence training method by about 81 percent. This advance could enable a wider array of resource-constrained edge devices, like sensors and smartwatches, to deploy more accurate AI models while keeping user data secure.

The MIT researchers boosted the efficiency of a technique known as federated learning, which involves a network of connected devices that work together to train a shared AI model.

In federated learning, the model is broadcast from a central server to wireless devices. Each device trains the model using its local data and then transfers model updates back to the server. Data are kept secure because they remain on each device.

But not all devices in the network have enough capacity, computational capability, and connectivity to store, train, and transfer the model back and forth with the server in a timely manner. This causes delays that worsen training performance.

The MIT researchers developed a technique to overcome these memory constraints and communication bottlenecks. Their method is designed to handle a heterogenous network of wireless devices with varied limitations.

This new approach could make it more feasible for AI models to be used in high-stakes applications with strict security and privacy standards, like health care and finance.

“This work is about bringing AI to small devices where it is not currently possible to run these kinds of powerful models. We carry these devices around with us in our daily lives. We need AI to be able to run on these devices, not just on giant servers and GPUs, and this work is an important step toward enabling that,” says Irene Tenison, an electrical engineering and computer science (EECS) graduate student and lead author of a
[paper on this technique](https://arxiv.org/pdf/2510.03165)
.

Her co-authors include Anna Murphy ’25, a machine-learning engineer at Lincoln Laboratory; Charles Beauville, a visiting student from Ecole Polytechnique Fédérale de Lausanne (EPFL) in Switzerland and a machine-learning engineer at Flower Labs; and senior author Lalana Kagal, a principal research scientist in the Computer Science and Artificial Intelligence Laboratory (CSAIL) at MIT. The research will be presented at the IEEE International Joint Conference on Neural Networks.

**Reducing lag time**

Many federated learning approaches assume all devices in the network have enough memory to train the full AI model, and stable connectivity to transmit updates back to the server quickly.

But these assumptions fall short with a network of heterogenous devices, like smartwatches, wireless sensors, and mobile phones. These edge devices have limited memory and computational power, and often face intermittent network connectivity.

The central server usually waits to receive model updates from all devices, then averages them to complete the training round. This process repeats until training is complete.

“This lag time can slow down the training procedure or even cause it to fail,” Tenison says.

To overcome these limitations, the MIT researchers developed a new framework called FTTE (Federated Tiny Training Engine) that reduces the memory and communication overhead needed by each mobile device.

Their framework involves three main innovations.

First, rather than broadcasting the entire model to all devices, FTTE sends a smaller subset of model parameters instead, reducing the memory requirement for each device. Parameters are internal variables the model adjusts during training.

FTTE uses a special search procedure to identify parameters that will maximize the model’s accuracy while staying within a certain memory budget. That limit is set based on the most memory-constrained device.

Second, the server updates the model using an asynchronous approach. Rather than waiting for responses from all devices, the server accumulates incoming updates until it reaches a fixed capacity, then proceeds with the training round.

Third, the server weights updates from each device based on when it received them. In this way, older updates don’t contribute as much to the training process. These outdated data can hold the model back, slowing the training process and reducing accuracy.

“We use this semi-asynchronous approach because want to involve the least powerful devices in the training process so they can contribute their data to the model, but we don’t want the more powerful devices in the network to stay idle for a long time and waste resources,” Tenison says.

**Achieving acceleration**

The researchers tested their framework in simulations with hundreds of heterogeneous devices and a variety of models and datasets. On average, FTTE enabled the training procedure to reach completing 81 percent faster than standard federated learning approaches.

Their method reduced the on-device memory overhead by 80 percent and the communication payload by 69 percent, while attaining near the accuracy of other techniques.

“Because we want the model to train as fast as possible to save the battery life of these resource-constrained devices, we do have a tradeoff in accuracy. But a small drop in accuracy could be acceptable in some applications, especially since our method performs so much faster,” she says.

FTTE also demonstrated effective scalability and delivered higher performance gains for larger groups of devices.

In addition to these simulations, the researchers tested FTTE on a small network of real devices with varying computational capabilities.

“Not everyone has the latest Apple iPhone. In many developing countries, for instance, users might have less powerful mobile phones. With our technique, we can bring the benefits of federated learning to these settings,” she says.

In the future, the researchers want to study how their method could be used to increase the personalized performance of AI models on each device, rather than focusing on the average performance of the model. They also want to conduct larger experiments on real hardware.

This work was funded, in part, by a Takeda PhD Fellowship.