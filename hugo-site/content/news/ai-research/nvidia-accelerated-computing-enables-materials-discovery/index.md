---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-18T02:23:41.227269+00:00'
exported_at: '2025-11-18T02:23:42.216991+00:00'
feed: http://feeds.feedburner.com/nvidiablog
language: en
source_url: https://blogs.nvidia.com/blog/ai-science-materials-discovery-sc25
structured_data:
  about: []
  author: ''
  description: NVIDIA Holoscan drives breakthroughs in real-time nano-imaging and
    NVIDIA ALCHEMI boosts discovery of advanced materials and cooling technologies.
  headline: NVIDIA Accelerated Computing Enables Scientific Breakthroughs for Materials
    Discovery
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://blogs.nvidia.com/blog/ai-science-materials-discovery-sc25
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: NVIDIA Accelerated Computing Enables Scientific Breakthroughs for Materials
  Discovery
updated_at: '2025-11-18T02:23:41.227269+00:00'
url_hash: 1e59b1d2fe616fe8c2b58198bf82260ac066ca10
---

To power future technologies including liquid-cooled data centers, high-resolution digital displays and long-lasting batteries, scientists are searching for novel chemicals and materials optimized for factors like energy use, durability and efficacy.

New NVIDIA-accelerated data processing pipelines and AI microservices unveiled at the
[SC25](https://sc25.supercomputing.org/)
conference in St. Louis are advancing chemistry and material science to support this research, with potential applications in industries such as aerospace, energy and manufacturing.

A demo in the NVIDIA booth showcases work by the U.S. Department of Energy’s Brookhaven National Laboratory using the
[NVIDIA Holoscan](https://www.nvidia.com/en-us/edge-computing/holoscan/)
AI sensor processing platform to visualize materials at under 10 nanometer-resolution.

Another demo highlights a pair of microservices coming to
[NVIDIA NIM](https://developer.nvidia.com/nim)
that will provide efficient, high-throughput simulations for batched conformer search and batched molecular dynamics — processes necessary to predict and simulate the properties of materials at an atomic level. The NIM microservices are part of NVIDIA ALCHEMI, a suite of microservices and toolkits for chemistry and materials science.

Japanese energy company ENEOS and New Jersey-based OLED display technology company Universal Display Corporation are among the early-access users of the NVIDIA ALCHEMI NIM microservices.

VIDEO

## **Brookhaven National Laboratory** **Accelerates Nanoscale Imaging With NVIDIA Holoscan**

Brookhaven National Laboratory is driving materials science research with the National Synchrotron Light Source II (NSLS-II), a facility that houses dozens of
[beamlines](https://www2.lbl.gov/Science-Articles/Archive/tabl-wonder.html)
that help scientists investigate material properties using a powerful X-ray source.

NSLS-II is capable of imaging complex material systems like battery, microelectronic and nanoparticle superlattices at nanometer resolution. These experiments generate large volumes of data that must be processed using advanced computational methods before scientists can extract meaningful insights from them.

NSLS-II researchers are using the NVIDIA Holoscan platform for
[high-bandwidth, high-throughput edge processing](https://dl.acm.org/doi/10.1145/3731599.3767593)
of streaming data in real time. The Holoscan-accelerated processing pipeline enables researchers to receive near-instant feedback on their experiments, helping them run imaging workflows more efficiently.

“By collaborating with NVIDIA to integrate Holoscan into our pipeline, we can now see results right away as we conduct a scan, instead of waiting for each scan to finish,” said Hanfei Yan, lead beamline scientist for the
[Hard X-ray Nanoprobe](https://www.bnl.gov/nsls2/beamlines/highlights.php?q=3-ID)
at NSLS-II. “This capability enables us to identify regions of interest on the fly and to observe the evolution of properties during measurements, which is critical for decisionmaking in experiments.”

Boosting image processing efficiency is more than a time-saver for researchers — it helps optimize the operating costs of expensive instruments like the NSLS-II.

“If we can run our experiments more efficiently, we can support more users, which in turn means we can do more science,” said Daniel Allan, group leader of data engineering at NSLS-II. “We also see the potential to use this pipeline for AI-assisted operation — integrating AI models for both imaging tasks and controls to conduct autonomous experiments.”

## **ENEOS** **Innovates With Immersion Cooling Fluids, Catalysts for Energy Conversion**

ENEOS is applying NVIDIA ALCHEMI NIM microservices to two critical energy applications: discovering new liquids for immersion cooling in next-generation data centers, and identifying catalysts that can be used for processes like hydrogen fuel production.

NVIDIA ALCHEMI NIM microservices for conformer search and molecular dynamics enable ENEOS scientists to prescreen molecular candidates through computational experiments, narrowing down options so only the most promising materials are tested in real-world experiments. This optimization saves research and development costs while accelerating the path to commercialization.

By adopting ALCHEMI, the team found they could evaluate about 10 million liquid-immersion candidates and 100 million oxygen evolution reaction candidates within a few weeks — at least 10x more than they could with prior methods.

“We hadn’t considered running searches at the 10-100 million scale before, but NVIDIA ALCHEMI made it surprisingly easy to sample extensively and achieve more physically realistic results,” said Takeshi Ibuka, general manager of the AI innovation department at ENEOS Holdings, Inc. “Because the calculations finish so quickly, we can spend more time productively analyzing results instead of doing just calculation tasks.”

## **Universal Display Corporation** **Advances the Next Generation of OLED Screens**

Universal Display Corporation (UDC) invents, develops and commercializes energy-efficient organic light emitting diode (OLED) materials for displays in everyday products including watches, smartphones, laptops, computer monitors, televisions, cars and virtual-reality headsets.

With NVIDIA ALCHEMI, UDC’s scientists are predicting properties of potential new OLED materials to power displays with better performance, greater energy efficiency and more precise color tuning.

![](https://blogs.nvidia.com/wp-content/uploads/2025/11/Aurora-flexible-OLED-panel_2-1680x1200.jpg)


OLED panel image courtesy of UDC.

Finding the right OLED material involves searching a universe of possibilities: The number of possible molecules UDC could make for an OLED is vast, around 10 to the 100th power. With the ALCHEMI NIM microservice for AI-accelerated conformer search, UDC can evaluate billions of candidate molecules up to 10,000x faster than traditional computational methods.

“Early on, our work relied on conventional CPU machines that limited how broadly we could explore at any given time, and required us to prioritize the most promising areas of chemistry using our expertise and chemical intuition,” said Julie Brown, executive vice president and chief technical officer at UDC.

“By using GPU-accelerated computing and NVIDIA ALCHEMI together with our in-house expertise, we can completely change the scale and speed of discovery,” said Brown. “This  enables us to uncover opportunities and fast-track new materials quicker than we ever could before.”

The most promising compounds discovered in this initial search are next simulated using the ALCHEMI NIM for molecular dynamics, which accelerates the process by up to 10x for a single simulation. By running their workloads across multiple NVIDIA GPUs in parallel, the UDC team is further amplifying the speedup, reducing simulation time from days to seconds.

![](https://blogs.nvidia.com/wp-content/uploads/2025/11/UDC_OLED-1680x531.jpg)


Images courtesy of UDC.

UDC is applying NVIDIA ALCHEMI NIM microservices to research projects including the development of blue phosphorescent OLEDs that could meaningfully improve energy efficiency and device performance.

“The NVIDIA ALCHEMI microservices enable more creativity for individual scientists by removing any concerns that we have about capacity and throughput limitations, and giving us immediate feedback on new chemistry,” said Brown. “Through this collaboration with NVIDIA, we can amplify the impact of our scientific insight and significantly increase the pace at which new materials are discovered and developed. These efforts don’t just push the boundaries of what OLED can do — they set the stage for more sustainable and energy-efficient displays worldwide.”

NVIDIA ALCHEMI is among over 150
[NVIDIA CUDA-X](https://www.nvidia.com/en-us/technologies/cuda-x/)
libraries and frameworks speeding up real-world problem-solving across science and engineering.

VIDEO

*Learn more about*
[*NVIDIA Holoscan*](https://www.nvidia.com/en-us/edge-computing/holoscan/)
*and*
[*NVIDIA ALCHEMI*](https://developer.nvidia.com/blog/revolutionizing-ai-driven-material-discovery-using-nvidia-alchemi/)
*, and watch the*
[*SC25 fireside chat by Ian Buck*](https://nvevents.nvidia.com/sc25fireside)
*, vice president of hyperscale and high-performance computing at NVIDIA.*

*See*
[*notice*](https://www.nvidia.com/en-eu/about-nvidia/terms-of-service/)
*regarding software product information.*