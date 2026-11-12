---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-12T21:38:03.783976+00:00'
exported_at: '2026-11-12T21:38:05.194046+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/new-research-could-lead-faster-trustworthy-ai-models-climate-prediction-1112
structured_data:
  about: []
  author: ''
  description: A new training technique streamlines the production of fast, trustworthy,
    and adaptable AI models for climate prediction, known as climate emulators. The
    technique, developed at MIT, boosts the performance and adaptability of a climate
    emulator while using only a fraction of the data typically required.
  headline: New research could lead to faster, trustworthy AI models for climate prediction
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/new-research-could-lead-faster-trustworthy-ai-models-climate-prediction-1112
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New research could lead to faster, trustworthy AI models for climate prediction
updated_at: '2026-11-12T21:38:03.783976+00:00'
url_hash: a865d7bae4f04a4d69341535d4b7f6624ed90858
---

MIT scientists developed a training method to generate models that simulate the effects of human activities on climate much more quickly than other approaches.

Accurate, up-to-date climate projections are essential for planning decisions that enhance the resilience of power grids, protect public health, maximize agricultural yields, and more.

Now, MIT researchers have developed a technique that streamlines the production of fast, trustworthy, and adaptable artificial intelligence models for climate prediction.

These specialized AI models, known as climate emulators, can rapidly simulate the effects of human activities onto a future climate, predicting impacts on temperatures or sea level, for example.

Because emulators run in a matter of seconds, scientists use them to efficiently test thousands of varied climate scenarios. This provides more reliable estimates and can identify unexpected outcomes of regional interventions.

The MIT researchers developed a training technique that boosts the performance and adaptability of a climate emulator while using only a fraction of the data typically required. This significantly cuts production time for these practical scientific tools.

They show that an emulator trained with a much smaller amount of carefully selected synthetic data accurately predicts outcomes of scenarios it did not see during training, while traditional emulators failed to adapt to new situations.

“Climate emulators are especially well-suited for modeling policy-relevant scenarios. By using our method to generate optimized training data for an emulator, we can speed up the production of much more reliable emulators, so we can better trust their outputs for making policy decisions,” says Christoher Womack PhD ’26, who is now a postdoc at ETH Zurich and lead author of a
[paper on this technique](https://www.pnas.org/doi/10.1073/pnas.2620731123)
.

He is joined on the paper by Shahine Bouabid, a postdoc in the MIT Department of Earth, Atmospheric and Planetary Sciences (EAPS); Andrei Sokolov, a research scientist in MIT’s Center for Sustainability Science and Strategy (CS3); Popat Salunke, a postdoc in CS3; Glenn Flierl, a professor of oceanography in EAPS; Sebastian D. Eastham, an associate professor at Imperial College London; and senior author Noelle E. Selin, a professor in the MIT Institute for Data, Systems, and Society (IDSS) and EAPS, and director of CS3. The research
[appears this week](https://www.pnas.org/doi/10.1073/pnas.2620731123)
in the
*Proceedings of the National Academy of Sciences.*

**Speedier surrogates**

Climate scientists typically use earth system models (ESMs) to make long-term projections about how global temperature or precipitation could change in response to varying greenhouse gas emissions.

These enormous, physics-based models capture the major components and interactions of the earth’s climate in extreme detail. While powerful, ESMs can take months to run on a cluster of supercomputers — and that’s only to project one possible future climate scenario.

Selin and her collaborators design climate emulators, which are fast AI surrogate models that mimic the behavior of full-scale ESMs. Emulators help scientists test many scenarios, make more accurate forecasts, and explore specific pollutants and regional effects.

“Climate emulators can run in just a few seconds, so it really expands what we can do in terms of exploring these future climate scenarios,” Womack says.

When scientists design a climate emulator, they often train the AI model using a set of six to eight future scenarios based on realistic future trajectories of emissions. They must run each scenario through a full-scale ESM, making these datasets costly and time-consuming to generate.

The MIT researchers recently found that using realistic future scenarios as training data can lead to underperforming emulators that fail to predict unfamiliar or novel scenarios.

In this work, they developed an algorithm that generates a synthetic dataset of optimized climate scenarios tailored to boost one emulator’s predictive performance.

“Our algorithm might generate some weird scenarios which look nothing like a realistic future, but we don’t care so much if the training scenarios are realistic. We are just trying to make the best possible dataset to train an emulator,” Womack says.

Importantly, rather than needing to run a full ESM six or eight times to generate training data, a user would only need to run that model once.

**Tuning the training data**

The researchers begin by generating an arbitrary climate scenario using a fast and simple climate model. They test how well their emulator can reproduce the results of that ESM, which gives them a measure of error.

Because of the programming technique they used to build the training pipeline, they can iteratively update the training data to increase the emulator’s predictive skill. For instance, the algorithm could increase CO
2
emissions dramatically in the year 2050 or rapidly decrease methane emissions in 2037.

Then the optimization updates the training data until the emulator’s error level reaches a certain threshold.

In the end, rather than resembling realistic scenarios in which emissions follow smooth trajectories, the synthetic data contain rapid variations.

“By introducing these high-frequency wiggles and oscillations, our data enable the emulator to extract a lot more information about the overall system,” Womack explains.

Their training algorithm outputs these emissions scenarios, which they can use to train an emulator that is more accurate and adaptable.

“In the future, we are definitely going to see climates and scenarios we haven’t seen before. If we can simulate these different scenarios more robustly, we can provide more reliable information to the stakeholders who need it,” Selin says.

For instance, an emulator trained with their technique can capture the effects of local pollutant control policies that reduce one pollutant while other emissions continue rising. The traditional emulators they evaluated failed this test.

In the long run, Womack hopes this work improves the usefulness of fast and adaptable climate emulators for policy formulation.

“This is such an important piece of the pipeline when it comes to creating useful tools that speak to stakeholder needs. Because the process of training an emulator can takes months or even years, the emulators we have are usually out-of-date. By cutting down that production time, I think this technique will be a game-changer in terms of getting updated tools into the hands of researchers and practitioners,” Selin adds.

In the future, the researchers want to test their technique using an emissions scenario generated by a full ESM. They also want to apply it to other types of climate models and explore its effectiveness in broader machine learning and computer vision applications.

This research was part of the Bringing Computation to the Climate Challenge (BC3) project and supported by Schmidt Sciences through the MIT Grand Challenges.