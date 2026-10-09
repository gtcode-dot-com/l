---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-24T04:49:11.537316+00:00'
exported_at: '2026-03-24T04:49:13.775856+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/generative-ai-improves-wireless-vision-system-sees-through-obstructions-0319
structured_data:
  about: []
  author: ''
  description: Wave-Former is a new system that can complete the shape of a hidden
    3D object or reconstruct the scene of an entire interior room using reflected
    wireless signals.
  headline: Generative AI improves a wireless vision system that sees through obstructions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/generative-ai-improves-wireless-vision-system-sees-through-obstructions-0319
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Generative AI improves a wireless vision system that sees through obstructions
updated_at: '2026-03-24T04:49:11.537316+00:00'
url_hash: 04cc98f40b234ba0ab1924872a4650ebaa7dae67
---

MIT researchers have spent more than a decade studying techniques that enable robots to find and manipulate hidden objects by “seeing” through obstacles. Their methods utilize surface-penetrating wireless signals that reflect off concealed items.

Now, the researchers are leveraging generative artificial intelligence models to overcome a longstanding bottleneck that limited the precision of prior approaches. The result is a new method that produces more accurate shape reconstructions, which could improve a robot’s ability to reliably grasp and manipulate objects that are blocked from view.

This new technique builds a partial reconstruction of a hidden object from reflected wireless signals and fills in the missing parts of its shape using a specially trained generative AI model.

The researchers also introduced an expanded system that uses generative AI to accurately reconstruct an entire room, including all the furniture. The system utilizes wireless signals sent from one stationary radar, which reflect off humans moving in the space.

This overcomes one key challenge of many existing methods, which require a wireless sensor to be mounted on a mobile robot to scan the environment. And unlike some popular camera-based techniques, their method preserves the privacy of people in the environment.

These innovations could enable warehouse robots to verify packed items before shipping, eliminating waste from product returns. They could also allow smart home robots to understand someone’s location in a room, improving the safety and efficiency of human-robot interaction.

“What we’ve done now is develop generative AI models that help us understand wireless reflections. This opens up a lot of interesting new applications, but technically it is also a qualitative leap in capabilities, from being able to fill in gaps we were not able to see before to being able to interpret reflections and reconstruct entire scenes,” says Fadel Adib, associate professor in the Department of Electrical Engineering and Computer Science, director of the Signal Kinetics group in the MIT Media Lab, and senior author of two papers on these techniques. “We are using AI to finally unlock wireless vision.”

Adib is joined on the
[first paper](https://arxiv.org/pdf/2511.14152)
by lead author and research assistant Laura Dodds; as well as research assistants Maisy Lam, Waleed Akbar, and Yibo Cheng; and on the
[second paper](https://arxiv.org/pdf/2511.14019)
by lead author and former postdoc Kaichen Zhou; Dodds; and research assistant Sayed Saad Afzal. Both papers will be presented at the IEEE Conference on Computer Vision and Pattern Recognition.

**Surmounting specularity**

The Adib Group previously demonstrated the use of millimeter wave (mmWave) signals to
[create accurate reconstructions](https://news.mit.edu/2025/new-imaging-technique-reconstructs-hidden-object-shapes-0701)
of 3D objects that are hidden from view, like a lost wallet buried under a pile.

These waves, which are the same type of signals used in Wi-Fi, can pass through common obstructions like drywall, plastic, and cardboard, and reflect off hidden objects.

But mmWaves usually reflect in a specular manner, which means a wave reflects in a single direction after striking a surface. So large portions of the surface will reflect signals away from the mmWave sensor, making those areas effectively invisible.

“When we want to reconstruct an object, we are only able to see the top surface and we can’t see any of the bottom or sides,” Dodds explains.

The researchers previously used principles from physics to interpret reflected signals, but this limits the accuracy of the reconstructed 3D shape.

In the new papers, they overcame that limitation by using a generative AI model to fill in parts that are missing from a partial reconstruction.

“But the challenge then becomes: How do you train these models to fill in these gaps?” Adib says.

Usually, researchers use extremely large datasets to train a generative AI model, which is one reason models like Claude and Llama exhibit such impressive performance. But no mmWave datasets are large enough for training.

Instead, the researchers adapted the images in large computer vision datasets to mimic the properties in mmWave reflections.

“We were simulating the property of specularity and the noise we get from these reflections so we can apply existing datasets to our domain. It would have taken years for us to collect enough new data to do this,” Lam says.

The researchers embed the physics of mmWave reflections directly into these adapted data, creating a synthetic dataset they use to teach a generative AI model to perform plausible shape reconstructions.

The complete system, called Wave-Former, proposes a set of potential object surfaces based on mmWave reflections, feeds them to the generative AI model to complete the shape, and then refines the surfaces until it achieves a full reconstruction.

Wave-Former was able to generate faithful reconstructions of about 70 everyday objects, such as cans, boxes, utensils, and fruit, boosting accuracy by nearly 20 percent over state-of-the-art baselines. The objects were hidden behind or under cardboard, wood, drywall, plastic, and fabric.

**Seeing “ghosts”**

The team used this same approach to build an expanded system that fully reconstructs entire indoor scenes by leveraging mmWave reflections off humans moving in a room.

Human motion generates multipath reflections. Some mmWaves reflect off the human, then reflect again off a wall or object, and then arrive back at the sensor, Dodds explains.

These secondary reflections create so-called “ghost signals,” which are reflected copies of the original signal that change location as a human moves. These ghost signals are usually discarded as noise, but they also hold information about the layout of the room.

“By analyzing how these reflections change over time, we can start to get a coarse understanding of the environment around us. But trying to directly interpret these signals is going to be limited in accuracy and resolution.” Dodds says.

They used a similar training method to teach a generative AI model to interpret those coarse scene reconstructions and understand the behavior of multipath mmWave reflections. This model fills in the gaps, refining the initial reconstruction until it completes the scene.

They tested their scene reconstruction system, called RISE, using more than 100 human trajectories captured by a single mmWave radar. On average, RISE generated reconstructions that were about twice as precise than existing techniques.

In the future, the researchers want to improve the granularity and detail in their reconstructions. They also want to build large foundation models for wireless signals, like the foundation models GPT, Claude, and Gemini for language and vision, which could open new applications.

This work is supported, in part, by the National Science Foundation (NSF), the MIT Media Lab, and Amazon.