---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T04:59:16.163516+00:00'
exported_at: '2026-04-02T04:59:19.844447+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/wristband-enables-wearers-control-robotic-hand-with-own-movements-0325
structured_data:
  about: []
  author: ''
  description: MIT engineers designed an ultrasound wristband that precisely tracks
    a wearer’s hand movements in real time and communicates the information to a robot
    or a virtual environment.
  headline: Wristband enables wearers to control a robotic hand with their own movements
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/wristband-enables-wearers-control-robotic-hand-with-own-movements-0325
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Wristband enables wearers to control a robotic hand with their own movements
updated_at: '2026-04-02T04:59:16.163516+00:00'
url_hash: 49887e64b7caefeb1abc1cc41c39f24cecb25e81
---

The next time you’re scrolling your phone, take a moment to appreciate the feat: The seemingly mundane act is possible thanks to the coordination of 34 muscles, 27 joints, and over 100 tendons and ligaments in your hand. Indeed, our hands are the most nimble parts of our bodies. Mimicking their many nuanced gestures has been a longstanding challenge in robotics and virtual reality.

Now, MIT engineers have designed an ultrasound wristband that precisely tracks a wearer’s hand movements in real-time. The wristband produces ultrasound images of the wrist’s muscles, tendons, and ligaments as the hand moves, and is paired with an artificial intelligence algorithm that continuously translates the images into the corresponding positions of the five fingers and palm.

The researchers can train the wristband to learn a wearer’s hand motions, which the device can communicate in real-time to a robot or a virtual environment.

In demonstrations, the team has shown that a person wearing the wristband can wirelessly control a robotic hand. As the person gestures or points, the robot does the same. In a sort of wireless marionette interaction, the wearer can manipulate the robot to play a simple tune on the piano and shoot a small basketball into a desktop hoop. With the same wristband, a wearer can also manipulate objects on a computer screen, for instance pinching their fingers together to enlarge and minimize a virtual object.

The team is using the wristband to gather hand motion data from many more users with different hand sizes, finger shapes, and gestures. They envision building a large dataset of hand motions that can be plumbed, for instance, to train humanoid robots in dexterity tasks, such as performing certain surgical procedures. The ultrasound band could also be used to grasp, manipulate, and interact with objects in video games, design applications, or other virtual settings.


“We think this work has immediate impact in potentially replacing hand tracking techniques with wearable ultrasound bands in virtual and augmented reality,” says Xuanhe Zhao, the Uncas and Helen Whitaker Professor of Mechanical Engineering at MIT. “It could also provide huge amounts of training data for dexterous humanoid robots.”

Zhao, Gengxi Lu, and their colleagues present the wristband’s new design in a
[paper appearing today](https://www.nature.com/articles/s41928-026-01594-4)
in
*Nature Electronics.*
Their MIT co-authors are former postdocs Xiaoyu Chen, Shucong Li, and Bolei Deng; graduate students SeongHyeon Kim and Dian Li; postdocs Shu Wang and Runze Li; and Anantha Chandrakasan, MIT provost and the Vannevar Bush Professor of Electrical Engineering and Computer Science. Other co-authors are graduate students Yushun Zheng and Junhang Zhang, Baoqiang Liu, Chen Gong, and Professor Qifa Zhou from the University of Southern California.

**Seeing strings**

There are currently a number of approaches to capturing and mimicking human hand dexterity in robots. Some approaches use cameras to record a person’s hand movements as they manipulate objects or perform tasks. Others involve having a person wear a glove with sensors, which records the person’s hand movements and transmits the data to a receiving robot. But erecting a complex camera system for different applications is impractical and prone to visual obstacles. And sensor-laden gloves could limit a person’s natural hand motions and sensations.

A third approach uses the electrical signals from muscles in the wrist or forearm that scientists then correlate with specific hand movements. Researchers have made significant advances in this approach, however these signals are easily affected by noise in the environment. They are also not sensitive enough to distinguish subtle changes in movements. For instance, they may discern whether a thumb and index finger are pinched together or pulled apart, but not much of the in-between path.

Zhao’s team wondered whether ultrasound imaging might capture more dexterous and continuous hand movements. His group has been developing various forms of ultrasound stickers — miniaturized versions of the transducers used in doctor’s offices that are paired with hydrogel material that can safely stick to skin.

In their new study, the team incorporated the ultrasound sticker design into a wearable wristband to continuously image the muscles and tendons in the wrist.

“The tendons and muscles in your wrist are like strings pulling on puppets, which are your fingers,” Lu says. “So the idea is: Each time you take a picture of the state of the strings, you’ll know the state of the hand.”

**Mapping manipulation**

The team designed a wristband with an ultrasound sticker that is the size of a smartwatch, and added onboard electronics that are about as small as a cellphone. They attached the wristband to a volunteer’s wrist and confirmed that the device produced clear and continuous images of the wrist as the volunteer moved their fingers in various gestures.

The challenge then was to relate the black and white ultrasound images of the wrist to specific positions of the hand. As it turns out, the fingers and thumb are capable of 22 degrees of freedom, or different ways of extending or angling. The researchers found that they could identify specific regions in their ultrasound images of the wrist that correlate to each of these 22 degrees of freedom. For instance, changes in one region relate to thumb extension, while changes in another region correlate with movements of the index finger.

To establish these connections, a volunteer wearing the wristband would move their hand in various positions while the researchers recorded the gestures with multiple cameras surrounding the volunteer. By matching changes in certain regions of the ultrasound images with hand positions recorded by the cameras, the team could label wrist image regions with the corresponding degree of freedom in the hand. But to do this translation continuously, and in real-time, would be an impossible task for humans.

So, the team turned to artificial intelligence. They used an AI algorithm that can be trained to recognize image patterns and correlate them with specific labels and, in this case, the hand’s various degrees of freedom. The researchers trained the algorithm with ultrasound images that they meticulously labeled, annotating the image regions associated with a specific degree of freedom. They tested the algorithm on a new set of ultrasound images and found it correctly predicted the corresponding hand gestures.

Once the researchers successfully paired the AI algorithm with the wristband, they tested the device on more volunteers. For the new study, eight volunteers with different hand and wrist sizes wore the wristband while they formed various hand gestures and grasps, including making the signs for all 26 letters in American Sign Language. They also held objects such as a tennis ball, a plastic bottle, a pair of scissors, and a pencil. In each case, the wristband precisely tracked and predicted the position of the hand.

To demonstrate potential applications, the team developed a simple computer program that they wirelessly paired with the wristband. As a wearer went through the motions of pinching and grasping, the gestures corresponded to zooming in and out on an object on the computer screen, and virtually moving and manipulating it in a smooth and continuous fashion.

The researchers also tested the wristband as a wireless controller of a simple commercial robotic hand. While wearing the wristband, a volunteer went through the motions of playing a keyboard. The robot in turn mimicked the motions in real-time to play a simple tune on a piano. The same robot was also able to mimic a person’s finger taps to play a desktop basketball game.

Zhao is planning to further miniaturize the wristband’s hardware, as well as train the AI software on many more gestures and movements from volunteers with wider ranging hand sizes and shapes. Ultimately, the team is building toward a wearable hand tracker that can be worn by anyone, to wirelessly manipulate humanoid robots or virtual objects with high dexterity.

“We believe this is the most advanced way to track dexterous hand motion, through wearable imaging of the wrist,” Zhao says. “We think these wearable ultrasound bands can provide intuitive and versatile controls for virtual reality and robotic hands.”

This research was supported, in part, by MIT, the U.S. National Institutes of Health, the U.S. National Science Foundation, the U.S. Department of Defense, and Singapore National Research Foundation through the Singapore-MIT Alliance for Research and Technology.