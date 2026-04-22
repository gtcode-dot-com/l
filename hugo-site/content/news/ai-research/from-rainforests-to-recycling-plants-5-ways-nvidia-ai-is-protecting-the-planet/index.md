---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-22T14:15:36.281436+00:00'
exported_at: '2026-04-22T14:15:38.749409+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing
structured_data:
  about: []
  author: ''
  description: Across climate, conservation, disaster monitoring and recycling, NVIDIA
    AI is enabling applications protecting the planet.
  headline: 'From Rainforests to Recycling Plants: 5 Ways NVIDIA AI Is Protecting
    the Planet'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'From Rainforests to Recycling Plants: 5 Ways NVIDIA AI Is Protecting the Planet'
updated_at: '2026-04-22T14:15:36.281436+00:00'
url_hash: 37698331a1ce8097b2c2cc042893dbc235b6a2a7
---

Protecting the planet has long been slow work — researchers wading through swamps to count endangered apes, forecasters painstakingly calculating the physics of weather, waste diversion facilities sorting recyclable material out of trash bound for landfills.

AI and accelerated computing are setting a new pace.

This Earth Day, NVIDIA is spotlighting five projects advancing climate science and sustainability. Read about:

## **NVIDIA Earth-2 Advances Climate Simulation [🔗](https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing/#earth-2)**

NVIDIA supports weather and climate understanding with the
[Earth-2](https://www.nvidia.com/en-us/high-performance-computing/earth-2/)

family of open AI models, libraries and frameworks — the world’s first fully open, accelerated weather AI software stack.

Earth-2 accelerates all stages of weather prediction, from processing initial observation data to generating 15-day global forecasts or local storm forecasts. It includes models like
[Earth-2 Nowcasting](https://research.nvidia.com/publication/2026-01_learning-accurate-storm-scale-evolution-observations)

, which uses generative AI to make country-scale forecasts into kilometer‑resolution, zero- to six-hour predictions of local storms and hazardous weather in just minutes.

Watch Mike Pritchard, director of climate simulation research at NVIDIA, discuss the technology at the recent NVIDIA GTC conference:

VIDEO

Another model, Earth-2 Global Data Assimilation, is now available to download from
[Earth2Studio](https://nvidia.github.io/earth2studio/)

and on
[Hugging Face](https://huggingface.co/nvidia/healda)

. Data assimilation is a massive undertaking for forecasters: For the National Weather Service, nearly half the compute needed to make predictions is used for preprocessing raw observations. Capable of running on a single GPU, Earth-2 Global Data Assimilation can within minutes turn this raw data into global snapshots of the current atmosphere, including the temperature, wind speed, humidity and air pressure.

The model architecture for Earth-2 Global Data Assimilation, HealDA, was developed in collaboration with the National Oceanic and Atmospheric Administration and MITRE.

## **AI Helps Primatologists Protect Critically Endangered Orangutans [🔗](https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing/#orangutans)**

AI is transforming wildlife conservation from a labor-intensive, costly process into efficient, automated systems that are helping great apes survive and thrive.

Two groundbreaking studies from the rainforests of Borneo and Sumatra recently demonstrated how GPU-accelerated AI can automate the detection of orangutan nests from aerial imagery, dramatically reducing the time and costs of population monitoring to better understand density and distribution of critically endangered orangutans.

Traditional orangutan surveys to count nests require teams to walk transects — straight paths used to systematically survey an area — through dense forests, peat swamps and mountainous terrain, a method that covers roughly 1 kilometer per hour.

Drone-based surveys, by contrast, can capture imagery across 18 kilometers in the same time frame. However, the bottleneck has always been manual image analysis — trained experts need approximately one minute per image to identify nests, meaning a single hour of drone flight generates up to 30 hours of tedious review work.

GPU-accelerated deep learning helps solve this challenge. Researchers for a
[study published in the
*American Journal of Primatology*](https://onlinelibrary.wiley.com/doi/10.1002/ajp.70100)

trained an AI model for automated nest detection that can process 1,800 images in under five minutes on a single GPU. The model was trained on a dataset of 800 high-resolution images using eight NVIDIA GPUs.

Similarly,
[researchers published in
*PeerJ*](https://peerj.com/articles/20333/)

trained four AI models on an NVIDIA GPU. One, based on the InceptionV3 architecture, demonstrated over 99% accuracy and precision in classifying aerial images as containing nests or not.

“Using NVIDIA-enabled deep learning, we can now train models that detect and count orangutan nests efficiently from aerial images,” said Song-Quan Ong, a computational ecologist at the Institute of Tropical Biology and Conservation at the Universiti Malaysia Sabah. “This significantly reduces the time and cost required for monitoring, while also enabling broader and more consistent coverage.”

All three orangutan species are classified as critically endangered, with populations declining more than 80% over the past 75 years. The threats they face are severe and mounting: Vast swaths of their forest habitat have been cleared for palm oil plantations, pulp and paper operations, and agricultural expansion. Forest fragmentation isolates populations, reducing genetic diversity and making survival increasingly precarious.

Illegal killing resulting from the wildlife trade, hunting and interactions in agricultural areas further decimates numbers. Compounding these pressures is the orangutan’s uniquely vulnerable life history: Females give birth only once every six to nine years, the longest inter-birth interval of any mammal, meaning populations cannot quickly recover from losses.

These challenges make rapid, scalable monitoring essential for guiding conservation interventions and measuring their effectiveness.

“We need to be really much faster with finding out where change occurs, and this really allows for that to happen,” said Serge Wich, a professor in primate biology at Liverpool John Moores University, whose mission is to translate this wealth of data into meaningful on-the-ground actions — and interactions. “This will allow people that would normally spend their time going through images to actually be working, for instance, with local communities to try to solve the real conservation issues.”

## **Smarter Sorting: AMP Diverts Billions of Pounds of Recyclables From Landfills With NVIDIA Physical AI [🔗](https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing/#amp)**

Recycling has a cost problem. Conventional sorting facilities can take up to $25 million to build and still miss a quarter of the recoverable material.

AMP

, a member of the
[NVIDIA Inception](https://www.nvidia.com/en-us/startups/)

startup program’s Sustainable Futures initiative, is using AI and robotics to change the math — and help the Earth.

Expanding beyond its hundreds of robots that already help sort materials at existing recycling sites, the company is now building AI-native recycling facilities from the ground up — including a fully automated plant in Denver and a waste-diversion project in Virginia that pulls recyclables and organics straight out of the trash.

The results are turning trash to treasure.

To date, AMP has diverted more than 2 billion pounds of material from landfills, preventing an estimated 739,000 metric tons of carbon-dioxide-equivalent emissions — a figure that also accounts for the cost of training and running its AI technologies.

AMP’s facilities are cost effective and achieve a 90% recovery rate — the percentage of total waste generated that’s successfully diverted from landfills through recycling, composting or energy recovery — compared with about 75% at conventional plants.

“If we use finite resources recklessly, it harms the planet,” said Joe Castagneri, director of software at AMP.  “When you don’t divert the plastics into recycling, oil-derived virgin plastics are used instead. When you don’t divert organic material from the landfill, it will break down anaerobically into methane. AI and automation bring efficient ways to sort through, reuse and ultimately get more out of our finite resources.”

Using
[NVIDIA Hopper GPUs](https://www.nvidia.com/en-us/data-center/technologies/hopper-architecture/)

, the company has cut AI inference energy consumption in half. In addition, thanks to AI and robotics making sorting much faster and more efficient, AMP uses roughly two-thirds the number of conveyor belts in traditional plants of the same size — meaning less steel, less power and a smaller energy footprint.

AMP trains its AI models on NVIDIA GPUs and runs inference at the edge using the open source
[NVIDIA TensorRT](https://developer.nvidia.com/tensorrt)

library and
[Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)

. The company is also exploring the
[NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim)

framework to develop and optimize its facilities in simulation before building in the real world.

“In the waste industry, AI and automation simply lower the costs of getting valuable stuff out of the trash,” Castagneri said. “That in turn increases how much trash we can pull out in the first place and how much of it we can pull out profitably. And if you can use resources more efficiently, it helps the environment.”

Other companies in NVIDIA Inception’s Sustainable Futures initiative are pioneering developments in fields such as green computing, sustainable infrastructure and wildlife conservation.

## **Before the Wave: Researchers Develop Tsunami Early Warning System [🔗](https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing/#tsunami-warning)**

Your browser does not support the video tag.

Artistic rendering of source data from the seafloor normal velocity and the acoustic–gravity model outputs, featured as part of SC25’s Art of HPC exhibit. Publication link: https://doi.org/10.1145/3712285.3771787

Video courtesy of Stefan Henneking, Sreeram Venkat, Veselin Dobrev, John Camier, Tzanio Kolev, Milinda Fernando, Alice-Agnes Gabriel, and Omar Ghattas.

Somewhere beneath the Pacific, along a 1,000-kilometer seam where the Juan de Fuca plate dives beneath North America, strain has been building since January 26, 1700, the last time the Cascadia fault ruptured. Paleoseismic evidence puts the recurrence interval at about 250 years. The math on that is uncomfortable.

When it goes, coastal Oregon and Washington will have as little as 15 minutes before waves as high as 30 meters arrive. Existing tsunami early warning systems are based on simplified assumptions and can lead to delayed, false or missed warnings.

A more accurate forecast can be achieved by solving what’s called an inverse problem: working backward from pressure readings at seafloor sensors to infer the seafloor motion that caused them, then forward again to predict where waves will strike and how high.

Omar Ghattas, a professor at UT Austin and his collaborator Stefan Henneking have spent years on this kind of problem. Their team — spanning UT Austin, UC San Diego and Lawrence Livermore —
[won the ACM Gordon Bell Prize](https://www.acm.org/media-center/2025/november/gordon-bell-prize-2025)

for doing it fast enough to matter.

The solution turns on a quiet mathematical fact: The physics of a Cascadia rupture doesn’t change depending on when it happens. That time-shift invariance enables precomputing the hard part — running the full-physics wave equations once per sensor, in advance — so that when sensors detect a real rupture, only a fast calculation remains. Running on GPUs, it finishes in under two-tenths of a second —
[a 10-billion-fold speedup over existing methods](https://www.acm.org/media-center/2025/november/gordon-bell-prize-2025)

— and returns not just a forecast but a measure of the uncertainty in that forecast.

That puts a warning in people’s hands within minutes of a rupture, leaving them closer to 10 minutes to reach higher ground than to none. The computation is no longer the constraint.

“We don’t have the 50 years it would take to solve the inverse problem by conventional algorithms,” Ghattas
[said at last month’s GTC conference](https://youtu.be/HwZDFUpx3kE?si=oG2eFkaQ33GBVqT2)

. “We have less than 15 minutes.”

## **By the Time You See It: Planet Applies AI to Earth Observation [🔗](https://blogs.nvidia.com/blog/earth-day-2026-ai-accelerated-computing/#planet)**

Planet operates the world’s largest constellation of Earth observation satellites. The company’s mission: image the entire globe every day, to make change actionable and visible. The Planet team has successfully launched nearly 650 satellites and produced more than 300 billion square kilometers of imagery, 50 petabytes of Earth data and a myriad of valuable insights for customers around the world.

However, what many may not know is that a raw satellite image isn’t actually an image. It’s a compressed array of bytes that must be decompressed, orthorectified — pinned precisely to the Earth’s surface and corrected for the physics of the sensor and the geometry of the orbit — and then processed. By the time a human sees it, the image may be hours old.

Kiruthika Devaraj, Planet’s vice president of spacecraft, framed it this way at last month’s NVIDIA
[GTC

conference](https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81732/?ncid=so-nvsh-262916-vt22)

: Earth observation has been modeled on astronomy, where the whole point is to peer into the distant past. What it needs to become, she argues, is more like biology: moving the “brains” of compute right next to the “eyes” of the sensor, thus expediting insights closer to the speed of collection.

A three-month collaboration with NVIDIA, presented at the conference, is an attempt to close that gap. Working GPU-native, the team built a pipeline that takes raw compressed satellite data and by comparison, traditional architectures, built when compute was expensive and storage was cheap, could take up to 100-300x longer to do the same job.

To put it in tangible terms: delivering wildfire insights in seconds, rather than hours. That gives first responders the rapid visibility needed to support active management.

*This Earth Day,*
[*tune into Devaraj’s discussion*](https://www.nvidia.com/gtc/session-catalog/sessions/gtc26-s81732/?ncid=so-nvsh-262916-vt22)
*of what’s possible with edge compute by Planet and NVIDIA.*