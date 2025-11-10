---
ai_agent_meta:
  content_digest: 88dd98d5a978848d3bdce732ce5fd17d67876bab
  generated_at: '2025-11-10T02:35:50.725362+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
ai_agent_note: 'ATTN AI Agent: Produce a concise, neutral summary suitable for a research
  dashboard. If any key claims need citation, flag them for sourcing. No speculative
  data beyond stated IPCC guidance.'
ai_commentary:
- body: Forests store substantial carbon and harbor most of Earth’s terrestrial biodiversity;
    estimates of yearly CO2 uptake remain uncertain due to model resolution.
  title: Context
- body: IPCC emphasizes carbon removal as essential for staying within 1.5°C and identifies
    forest management as a pivotal strategy to enhance the terrestrial carbon sink.
  title: Key finding
- body: The coarse resolution of global carbon models contributes to uptake uncertainties;
    improving model granularity can support more reliable planning for forest-based
    climate solutions.
  title: Modeling gaps and policy implications
ai_commentary_meta:
  content_digest: 88dd98d5a978848d3bdce732ce5fd17d67876bab
  generated_at: '2025-11-10T02:35:50.725326+00:00'
  model: gpt-5-nano-2025-08-07
  prompt_version: v2025-11-09
  provider: openai
category: ai-research
date: '2025-11-09T05:13:27.985431+00:00'
exported_at: '2025-11-09T05:30:20.806623+00:00'
feed: https://research.facebook.com/feed
meta_description: A concise briefing on forests’ role in the carbon cycle, the importance
  of carbon removal per IPCC guidance, and forest management as a policy lever to
  limit warming to 1.5°C, amid modeling uncertainties.
meta_keywords:
- forests
- carbon removal
- carbon sink
- IPCC
- climate change
- biodiversity
- forest management
- 1.5°C
- global carbon models
- terrestrial carbon cycle
source_url: https://research.facebook.com/blog/2023/4/every-tree-counts-large-scale-mapping-of-canopy-height-at-the-resolution-of-individual-trees
structured_data:
  about: &id001
  - Climate change
  - Forests and carbon sequestration
  - IPCC findings
  - Carbon removal
  - Forest management and biodiversity
  description: Forests capture carbon dioxide and support biodiversity, yet estimates
    of how much carbon they remove each year remain uncertain due to coarse modeling.
    The IPCC emphasizes that carbon removal is essential to limit warming to 1.5°C,
    and forest management is among the most important strategies to enhance the terrestrial
    carbon sink while preserving biodiversity.
  headline: 'Every tree counts: forests as a key to limiting warming'
  keywords: *id001
title: Every tree counts
updated_at: '2025-11-09T05:13:27.985431+00:00'
url_hash: 548a28a59b11ee32b93d10bfb2068900ec69683d
---

![](https://scontent.fhnl3-1.fna.fbcdn.net/v/t39.8562-6/341167001_531719905825011_2520132867068275390_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=f537c7&_nc_ohc=m7Cok2u_mOIQ7kNvwFw1Dv9&_nc_oc=AdkY7ccTkSJ8fOYhh8r5gTRpVzB1dQ9Usf2-gKwobEEyYoMBvx6R1JmgxNVmFeRAj2M&_nc_zt=14&_nc_ht=scontent.fhnl3-1.fna&_nc_gid=4pau6oB87q8dkfvyKEPXTg&oh=00_AfiubaH6ovPy-BVHFFVzVaK74MixgsBbnAqpODx9th2WaA&oe=6915F09B)

The increase in atmospheric carbon dioxide levels and associated climate change has had a dramatic impact on the Earth’s biosphere, ranging from drought and wildfires to the loss of biodiversity. Forests play a central role in the carbon dioxide cycle, pulling carbon dioxide from the atmosphere and storing the carbon in their biomass. Forests also contain the majority of Earth’s terrestrial biodiversity. Despite this central role, the magnitude of the carbon dioxide absorbed every year by forests around the world is still largely unclear, due in part to the coarse resolution of global carbon models.

The
[United Nations Intergovernmental Panel on Climate Change](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.ipcc.ch%2F&h=AT1knhjAa-wlgoX3FJIwwUWDvASegWjcEcZJ-r1la58HkYyKcZ7B5vKQ7utzRta8SFUNN6yXzk5XSeKznUAPI3ZAmr1bI6avurPsgthMEaTcfMUNzO5BbLm2Fjy9a1ASbOkjOQzeQDkgpiq0)
(IPCC) has clarified that carbon removal is a crucial part of limiting global warming to levels of 1.5º C in comparison with pre-industrial temperatures. Forest management is recognized by the IPCC as one of the most important ways to achieve carbon removal at scale, and over the past decade, forest management has become the main source of carbon offsets in the voluntary market.

In 2020, Meta set a goal to
[reach net zero emissions](https://l.facebook.com/l.php?u=https%3A%2F%2Fsustainability.fb.com%2Fclimate%2F&h=AT0irIv7AfboGwtfDHO5KfBLHuCBjErAyCjv7z9FrdwF6knnPmU1E_VR2_8Sn_HoPLpLAsd-ixsrMxtCZ05n1VzzfnfvzoCZ9hZOucCVn7aV_T85AWENXijrNn_Z02NL6cMXGQ0z55gSw7dz)
across our value chain in 2030. As part of this, we are developing new technology solutions to mitigate our own carbon footprint and making these openly available to enable a broader impact on climate change (for example, read more on
[how we use AI to reduce concrete’s carbon footprint](https://tech.facebook.com/engineering/2022/04/sustainable-concrete/)
). In this article, we describe how we leveraged internal
[state-of-the-art AI technology](https://ai.facebook.com/blog/dino-v2-computer-vision-self-supervised-learning/)
and collaborated with the
[World Resources Institute](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.wri.org%2F&h=AT11M9f7tQxwJhvbkxdVMkrQN2PuEjSdT661GeoE4ZIWO8uegnDYkord3ePPvlDw_BFHHhQJq_o5eKc-bSG3QuwJ4yg1OKexoXU071KLgNtSi1kbNGo32uCjZBY1-rEkrkaYedzxVzvToX7M)
(WRI) to develop a method to map forests, tree by tree, across areas the size of continents. As an example, we mapped the U.S. state of California and São Paulo, Brazil, and are making the data public and freely available.

## How improved mapping helps achieve net zero

To achieve net zero emissions, Meta is focused on reducing our emissions by prioritizing efficiency and circularity in our business decisions, embracing low-carbon technology, and engaging with our suppliers to help them set climate targets. Some emissions from hard-to-abate sectors will remain difficult to completely eliminate by the end of this decade. For those emissions we cannot avoid, we will remove an equivalent amount of carbon dioxide by purchasing credits from carbon removal projects, including nature-based solutions that can be deployed now, as well as emerging technologies that need our support to scale. Forests are critical to achieving the global scale of carbon removal needed as outlined by the IPCC, and the market for high-quality, forest-based carbon removal needs to grow significantly to achieve this scale.

We believe that by improving measurement, reporting, and verification (MRV) of forest-based carbon removal projects, we can improve the quality and accelerate the growth of nature-based climate solutions. First, by lowering the barrier to forest monitoring solutions, we can enable small landowners to access carbon markets and increase the number of community-led carbon removal projects. Smaller, distributed tree growth (e.g., in agroforestry) lacks affordable and scalable monitoring solutions, which can hamper the development of such projects in smaller communities. Second, nature-based solutions can use more reliable data of the carbon stock in forests for both the baselining and the monitoring of forest carbon. Improved, freely available high-resolution data could potentially be used in standardized verification methodologies for certain projects. Both of these challenges can be addressed by improving fine-grained knowledge of forests at a global scale and making the data publicly available.

**Figure 1:**
Canopy Height Map (CHM) for California, with inset showing zoomed-in region with input RGB imagery and LIDAR ground truth

## Description of our method

In order to make our mapping methodology useful for MRV of carbon projects, we set the following criteria: detect single trees (as small trees as possible) and be globally applicable. We also require that the method be applicable to different sources of imagery to allow for frequent updates of the canopy height maps.

Leveraging recent advances in self-supervised learning, namely the
[DINOv2 model we announced today](https://ai.facebook.com/blog/dino-v2-computer-vision-self-supervised-learning/)
, and our expertise in AI-based global mapping from high-resolution imagery, we have developed a machine learning approach that can detect canopy height with high fidelity from RGB imagery with a resolution of 0.5 m. We describe our model in detail in the preprint (
[link](https://l.facebook.com/l.php?u=https%3A%2F%2Farxiv.org%2Fabs%2F2304.07213&h=AT0NMycSZO9SYyVMJAkSUdokwNa_lrQwIX5uSABi2OlZu6GyEc9MyrMR9ifyaWXsa_NOjZVX4QtK8t5MI8v2IRzMIF4ykT-R1ocoso_RszdF3fDGEOvhjyWF85xvQmO3MWosYkeTw3YHKFN5)
), which has been submitted for peer review. DINOv2 provides a self-supervised framework that’s trainable on any collection of licensed photos without needing any associated metadata. In this work, a DINOv2 model is trained on high-resolution (0.5 m) RGB satellite imagery from
[MAXAR Technologies](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.maxar.com%2F&h=AT3H7g8WapANXoIup7j5tz7pNNaUCq-nNos9t5ewXcqn99qflZL6JRtYihAmzOlSK7llPkEXRcyWd_R9IOPJ_x-3hTSmMLCTCpI-hUz7YYiyIP4K4clkJBgh8s1pblwJbNaxQtPFfoX_YxLx)
in a self-supervised fashion. We then use aerial LIDAR data as a ground truth to learn canopy height maps (CHM). Since our ground truth is in North America and high-quality aerial LIDAR imagery is not globally available, we use spaceborne LIDAR data as a low-resolution and sparse but global data source to calibrate our model for global applicability.

Choosing the DINOv2’s self-supervised neural network learning allows for universal and generalizable features, which we believe facilitates global applicability of the model. The 0.5 m resolution allows us to map the canopy height of individual trees regardless of sparsity, undergrowth type, or species, which is crucial in achieving accurate biomass estimates. Leveraging our model, we create canopy height maps of California and São Paulo, Brazil (download the data
[here](https://l.facebook.com/l.php?u=https%3A%2F%2Fregistry.opendata.aws%2Fdataforgood-fb-forests%2F&h=AT1cpHXnDxT4K-OeLz6iwIJ_FvuLEI_B8yXKDc5-KOmHqRTPrLD78SqOYMwCz-AJ8fta2iwDUXPt2YccOlKdHIp74sw_L52yBgp4oVGkPIjQ2lsQKeNGpycgh801pvdkyWYLjjVtUwfGPsGe)
and view map
[here](https://l.facebook.com/l.php?u=https%3A%2F%2Fwri-datalab.earthengine.app%2Fview%2Fsubmeter-canopyheight&h=AT1A1NEd6HVPC6fVLFmTlRovxL9IAWBic_us4ogEfnb4rT80wJE8QbGubb-ovqh59wgnj8g-9tR6Sr3IHOL87GEinMXwTvyA4T7Tcan0MSu2nATTflbY_fesL3tTr1nq0AJBf5mxKr5z-xtu)
). We find that the model performs qualitatively well in Brazil, even though the high-resolution training data was from North America.

**Figure 2:**
Canopy Height Map (CHM) for the state of São Paulo, with inset showing zoomed-in region with input RGB imagery

Since the model is trained on RGB imagery, it allows the analysis of generic RGB imagery resampled to the same 0.5 m resolution that the model has been trained on, so imagery collected by planes or drones, rather than by satellites, can also be used as input. This is particularly important since aerial RGB data is more widely available and allows for simple, cost-effective tracking of changes in canopy height over time.

As an example, we demonstrate that our model performs well on the aerial imagery of the NEON dataset, as shown in the figure below.

**Figure 3:**
Even if the model is trained on satellite images, inference on airborne images does not seem to suffer from a domain shift

## Conclusion

Our method enables large-scale analysis of high-resolution imagery, determining forest canopy height with sub-meter resolution. Accurate forest mapping in space and time will lead to more accountable forest-based carbon offsets and enable the development of more carbon projects, especially those on smaller pieces of land — two requirements for nature-based carbon offsets to achieve the scale and quality needed to meet net zero goals at a global scale.

---

###### Acknowledgements

##### Our team consists of researchers from a wide range of backgrounds, from computer vision to physical modeling and sustainability. From the Physical Modeling group (Infrastructure): Eric Yang, Ben Nosarzewski, Janaki Vamaraju, Brian White, Tobias Tiecke, and Jamie Tolan. From Fundamental AI Research (FAIR): Guillaume Couairon, Huy Vo, Daniel Haziza, Theo Moutakani, Piotr Bojanowski, and Camille Couprie. From Net-Zero (Sustainability): Tracy Johns. For this work, we’ve had the pleasure of collaborating with the World Resources Institute’s John Brandt, Justine Spore, Dow Martin, and Sean DeWitt, and Sayantan Majumdar (Colorado State University) during an internship. We thank Andi Gros and Saikat Basu for their technical advice. We thank Shmulik Eisenmann, Patrick Louis, Lee Francisco, Leah Harwell, Eric Alamillo, Sylvia Lee, Patrick Nease, Alex Pompe, and Shawn Mcguire for their project support.