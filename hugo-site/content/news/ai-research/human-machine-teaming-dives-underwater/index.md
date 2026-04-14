---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-14T14:15:46.298164+00:00'
exported_at: '2026-04-14T14:15:48.733440+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/human-machine-teaming-dives-underwater-0414
structured_data:
  about: []
  author: ''
  description: MIT Lincoln Laboratory researchers are developing hardware and algorithms
    for underwater navigation and perception to improve collaboration between divers
    and autonomous underwater vehicles engaged in maritime missions.
  headline: Human-machine teaming dives underwater
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/human-machine-teaming-dives-underwater-0414
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Human-machine teaming dives underwater
updated_at: '2026-04-14T14:15:46.298164+00:00'
url_hash: 84d4323cc0dac0cf74f92115eacfca9e0abcc013
---

The electricity to an island goes out. To find the break in the underwater power cable, a ship pulls up the entire line or deploys remotely operated vehicles (ROVs) to traverse the line. But what if an autonomous underwater vehicle (AUV) could map the line and pinpoint the location of the fault for a diver to fix?

Such underwater human-robot teaming is the focus of an MIT Lincoln Laboratory project funded through an internally administered R&D portfolio on autonomous systems and carried out by the
[Advanced Undersea Systems and Technology Group](https://www.ll.mit.edu/r-d/air-missile-and-maritime-defense-technology/advanced-undersea-systems-and-technology)
. The project seeks to leverage the respective strengths of humans and robots to optimize maritime missions for the U.S. military, including critical infrastructure inspection and repair, search and rescue, harbor entry, and countermine operations.

"Divers and AUVs generally don't team at all underwater," says principal investigator Madeline Miller. "Underwater missions requiring humans typically do so because they involve some sort of manipulation a robot can't do, like repairing infrastructure or deactivating a mine. Even ROVs are challenging to work with underwater in very skilled manipulation tasks because the manipulators themselves aren't agile enough."

Beyond their superior dexterity, humans excel at recognizing objects underwater. But humans working underwater can't perform complex computations or move very quickly, especially if they are carrying heavy equipment; robots have an edge over humans in processing power, high-speed mobility, and endurance. To combine these strengths, Miller and her team are developing hardware and algorithms for underwater navigation and perception — two key capabilities for effective human-robot teaming.

As Miller explains, divers may only have a compass and fin-kick counts to guide them. With few landmarks and potentially murky conditions caused by a lack of light at depth or the presence of biological matter in the water column, they can easily become disoriented and lost. For robots to help divers navigate, they need to perceive their environment. However, in the presence of darkness and turbidity, optical sensors (cameras) cannot generate images, while acoustic sensors (sonar) generate images that lack color and only show the shapes and shadows of objects in the scene. The historical lack of large, labeled sonar image datasets has hindered training of underwater perception algorithms. Even if data were available, the dynamic ocean can obscure the true nature of objects, confusing artificial intelligence. For instance, a downed aircraft broken into multiple pieces, or a tire covered in an overgrowth of mussels, may no longer resemble an aircraft or tire, respectively.

"Ultimately, we want to devise solutions for navigation and perception in expeditionary environments," Miller says. "For the missions we're thinking about, there is limited or no opportunity to map out the area in advance. For the harbor entry mission, maybe you have a satellite map but no underwater map, for example."

On the navigation side, Miller's team picked up on work started by the
[MIT Marine Robotics Group](https://marinerobotics.mit.edu/)
, led by
[John Leonard](https://meche.mit.edu/people/faculty/JLEONARD@MIT.EDU)
, to develop diver-AUV teaming algorithms. With their navigation algorithms, Leonard's group ran simulations under optimal conditions and performed field testing in calm waters using human-paddled kayaks as proxies for both divers and AUVs. Miller's team then integrated these algorithms into a mission-relevant AUV and began testing them under more realistic ocean conditions, initially with a support boat acting as a diver surrogate, and then with actual divers.

"We quickly learned that you need more sensing capabilities on the diver when you factor in ocean currents," Miller explains. "With the algorithms demonstrated by MIT, the vehicle only needed to calculate the distance, or range, to the diver at regular intervals to solve the optimization problem of estimating the positions of both the vehicle and diver over time. But with the real ocean forces pushing everything around, this optimization problem blows up quickly."

On the perception side, Miller's team has been developing an AI classifier that can process both optical and sonar data mid-mission and solicit human input for any objects classified with uncertainty.

"The idea is for the classifier to pass along some information — say, a bounding box around an image — to the diver and indicate, "I think this is a tire, but I'm not sure. What do you think?" Then, the diver can respond, "Yes, you've got it right, or no, look over here in the image to improve your classification," Miller says.

This feedback loop requires an underwater acoustic modem to support diver-AUV communication. State-of-the-art data rates in underwater acoustic communications would require tens of minutes to send an uncompressed image from the AUV to the diver. So, one aspect the team is investigating is how to compress information into a minimum amount to be useful, working within the constraints of the low bandwidth and high latency of underwater communications and the low size, weight, and power of the commercial off-the-shelf (COTS) hardware they're using. For their prototype system, the team procured mostly COTS sensors and built a sensor payload that would easily integrate into an AUV routinely employed by the U.S. Navy, with the goal of facilitating technology transition. Beyond sonar and optical sensors, the payload features an acoustic modem for ranging to the diver and several data processing and compute boards.

Miller's team has tested the sensor-equipped AUV and algorithms around coastal New England — including in the open ocean near Portsmouth, New Hampshire, with the University of New Hampshire's (UNH)
[Gulf Surveyor](https://marine.unh.edu/facility/rv-gulf-surveyor)
and
[Gulf Challenger](https://marine.unh.edu/facility/rv-gulf-challenger)
coastal research vessels as diver surrogates, and on the Boston-area Charles River, with an MIT Sailing Pavilion skiff as the surrogate.

"The UNH boats are well-equipped and can access realistic ocean conditions. But pretending to be a diver with a large boat is hard. With the skiff, we can move more slowly and get the relative motion in tune with how a diver and AUV would navigate together."

Last summer, the team started testing equipment with human divers at Michigan Technological University's
[Great Lakes Research Center](https://www.mtu.edu/greatlakes/)
. Although the divers lacked an interface to feed back information to the AUV, each swam holding the team's tube-shaped prototype tablet, dubbed a "tube-let." The tube-let was equipped with a pressure and depth sensor, inertial measurement unit (to track relative motion), and ranging modem — all necessary components for the navigation algorithms to solve the optimization problem.

"A challenge during testing was coordinating the motion of the diver and vehicle, because they don't yet collaborate," Miller says. "Once the divers go underwater, there is no communication with the team on the surface. So, you have to plan where to put the diver and vehicle so they don't collide."

The team also worked on the perception problem. The water clarity of the Great Lakes at that time of year allowed for underwater imaging with an optical sensor. Caroline Keenan, a Lincoln Scholars Program PhD student jointly working in the laboratory's Advanced Undersea Systems and Technology Group and Leonard's research group at MIT, took the opportunity to advance her work on knowledge transfer from optical sensors to sonar sensors. She is exploring whether optical classifiers can train sonar classifiers to recognize objects for which sonar data doesn't exist. The motivation is to reduce the human operator load associated with labeling sonar data and training sonar classifiers.

With the internally funded research program coming to an end, Miller's team is now seeking external sponsorship to refine and transition the technology to military or commercial partners.

"The modern world runs on undersea telecommunication and power cables, which are vulnerable to attack by disruptive actors. The undersea domain is becoming increasingly contested as more nations develop and advance the capabilities of autonomous maritime systems. Maintaining global economic security and U.S. strategic advantage in the undersea domain will require leveraging and combining the best of AI and human capabilities," Miller says.