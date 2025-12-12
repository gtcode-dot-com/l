---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-12T12:03:29.583508+00:00'
exported_at: '2025-12-12T12:03:32.499303+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2025/new-method-improves-reliability-statistical-estimations-1212
structured_data:
  about: []
  author: ''
  description: MIT researchers developed a method that generates more accurate uncertainty
    measures for certain types of estimation. This could help improve the reliability
    of data analyses in areas like economics, epidemiology, and environmental sciences.
  headline: New method improves the reliability of statistical estimations
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2025/new-method-improves-reliability-statistical-estimations-1212
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New method improves the reliability of statistical estimations
updated_at: '2025-12-12T12:03:29.583508+00:00'
url_hash: 77b48a589d1111163bd9f89736fa9a1255926fee
---

Let’s say an environmental scientist is studying whether exposure to air pollution is associated with lower birth weights in a particular county.

They might train a machine-learning model to estimate the magnitude of this association, since machine-learning methods are especially good at learning complex relationships.

Standard machine-learning methods excel at making predictions and sometimes provide uncertainties, like confidence intervals, for these predictions. However, they generally don’t provide estimates or confidence intervals when determining whether two variables are related. Other methods have been developed specifically to address this association problem and provide confidence intervals. But, in spatial settings, MIT researchers found these confidence intervals can be completely off the mark.

When variables like air pollution levels or precipitation change across different locations, common methods for generating confidence intervals may claim a high level of confidence when, in fact, the estimation completely failed to capture the actual value. These faulty confidence intervals can mislead the user into trusting a model that failed.

After identifying this shortfall, the researchers developed a new method designed to generate valid confidence intervals for problems involving data that vary across space. In simulations and experiments with real data, their method was the only technique that consistently generated accurate confidence intervals.

This work could help researchers in fields like environmental science, economics, and epidemiology better understand when to trust the results of certain experiments.

“There are so many problems where people are interested in understanding phenomena over space, like weather or forest management. We’ve shown that, for this broad class of problems, there are more appropriate methods that can get us better performance, a better understanding of what is going on, and results that are more trustworthy,” says Tamara Broderick, an associate professor in MIT’s Department of Electrical Engineering and Computer Science (EECS), a member of the Laboratory for Information and Decision Systems (LIDS) and the Institute for Data, Systems, and Society, an affiliate of the Computer Science and Artificial Intelligence Laboratory (CSAIL), and senior author of this
[study](https://arxiv.org/pdf/2502.06067)
.

Broderick is joined on the paper by co-lead authors David R. Burt, a postdoc, and Renato Berlinghieri, an EECS graduate student; and Stephen Bates an assistant professor in EECS and member of LIDS. The research was recently presented at the Conference on Neural Information Processing Systems.

**Invalid assumptions**

Spatial association involves studying how a variable and a certain outcome are related over a geographic area. For instance, one might want to study how tree cover in the United States relates to elevation.

To solve this type of problem, a scientist could gather observational data from many locations and use it to estimate the association at a different location where they do not have data.

The MIT researchers realized that, in this case, existing methods often generate confidence intervals that are completely wrong. A model might say it is 95 percent confident its estimation captures the true relationship between tree cover and elevation, when it didn’t capture that relationship at all.

After exploring this problem, the researchers determined that the assumptions these confidence interval methods rely on don’t hold up when data vary spatially.

Assumptions are like rules that must be followed to ensure results of a statistical analysis are valid. Common methods for generating confidence intervals operate under various assumptions.

First, they assume that the source data, which is the observational data one gathered to train the model, is independent and identically distributed. This assumption implies that the chance of including one location in the data has no bearing on whether another is included. But, for example, U.S. Environmental Protection Agency (EPA) air sensors are placed with other air sensor locations in mind.

Second, existing methods often assume that the model is perfectly correct, but this assumption is never true in practice. Finally, they assume the source data are similar to the target data where one wants to estimate.

But in spatial settings, the source data can be fundamentally different from the target data because the target data are in a different location than where the source data were gathered.

For instance, a scientist might use data from EPA pollution monitors to train a machine-learning model that can predict health outcomes in a rural area where there are no monitors. But the EPA pollution monitors are likely placed in urban areas, where there is more traffic and heavy industry, so the air quality data will be much different than the air quality data in the rural area.

In this case, estimates of association using the urban data suffer from bias because the target data are systematically different from the source data.

**A smooth solution**

The new method for generating confidence intervals explicitly accounts for this potential bias.

Instead of assuming the source and target data are similar, the researchers assume the data vary smoothly over space.

For instance, with fine particulate air pollution, one wouldn’t expect the pollution level on one city block to be starkly different than the pollution level on the next city block. Instead, pollution levels would smoothly taper off as one moves away from a pollution source.

“For these types of problems, this spatial smoothness assumption is more appropriate. It is a better match for what is actually going on in the data,” Broderick says.

When they compared their method to other common techniques, they found it was the only one that could consistently produce reliable confidence intervals for spatial analyses. In addition, their method remains reliable even when the observational data are distorted by random errors.

In the future, the researchers want to apply this analysis to different types of variables and explore other applications where it could provide more reliable results.

This research was funded, in part, by an MIT Social and Ethical Responsibilities of Computing (SERC) seed grant, the Office of Naval Research, Generali, Microsoft, and the National Science Foundation (NSF).