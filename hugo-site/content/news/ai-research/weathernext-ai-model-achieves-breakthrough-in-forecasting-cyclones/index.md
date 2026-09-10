---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-10T01:00:13.124440+00:00'
exported_at: '2026-09-10T01:00:18.302709+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones
structured_data:
  about: []
  author: ''
  description: WeatherNext enables accurate cyclone forecasts that can give an extra
    day of warning. Now we are open sourcing the model.
  headline: 'WeatherNext: AI model achieves breakthrough in forecasting cyclones'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/weathernext-ai-model-achieves-breakthrough-in-forecasting-cyclones
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'WeatherNext: AI model achieves breakthrough in forecasting cyclones'
updated_at: '2026-09-10T01:00:13.124440+00:00'
url_hash: f5f908b6ffe4ea666d96d2de696b56071776e443
---

Our model uses
[Functional Generative Networks (FGNs)](https://arxiv.org/pdf/2506.10772)
to efficiently produce ensembles of different predictions, which captures the inherent uncertainty of the weather. We can now generate a single 15-day forecast in less than a minute on a TPU, empowering forecasters to quickly evaluate the probability distribution of potentially devastating tail-risks. Last year, our system produced 50 predictions at a time, matching global physics models. This year we scaled our ensemble size to 1,000 members, capturing rare but consequential scenarios like rapid intensification events, as occurred during Hurricane Melissa in 2025.

Up until now, operating at very high spatial resolution has been considered the main driver for making accurate intensity forecasts. However, WeatherNext Cyclones only needs data with a resolution of 28x28km, 100x coarser than traditional models. A smaller version of the model, WeatherNext 2-mini, which operates at a coarser 111x111km resolution, also shows great performance. This has surprised scientists, and it remains an open research question to fully understand how our models produce such accurate predictions at this resolution. We hope that, together with the research community, we can find out.

## Opening up WeatherNext to the research community

Alongside our
*Nature*
paper, we are
[open sourcing](https://github.com/google-deepmind/weathernext)
the code and model weights, making them freely available for anyone to build on. This includes academic research, operational forecasting, or developing more specialized, localized models. We hope to accelerate progress across the global weather community and empower meteorological agencies, researchers, and nonprofits to better predict weather events of all kinds and make key decisions to protect lives and infrastructure.

We are also releasing two sets of similar models: WeatherNext Cyclones, which ran during the hurricane season (results can be seen in the paper); and WeatherNext 2, a later update that we operationalized in October. Additionally, we are releasing WeatherNext 2-mini, a compact version of the model that can run on a single TPU in a free public
[Colab notebook](https://colab.research.google.com/github/google-deepmind/weathernext/blob/master/docs/weathernext2/wn2_demo.ipynb)
.

You can explore our latest cyclone forecasts on
[Weather Lab](https://deepmind.google.com/science/weatherlab/)
, which we recently refreshed with a new interface and expanded to include global weather forecasts alongside cyclone tracks. Weather Lab now lets you visualize WeatherNext predictions for temperature, precipitation, wind speed, and more, all in a single view. Both Weather Lab and WeatherNext models are a part of
[Google Earth AI](https://ai.google/earth-ai/)
.

## Pushing the frontiers of AI for weather forecasting

We have achieved a historic breakthrough by gaining more than a full day of lead time for predicting cyclones â delivering an advance equivalent to a decade of meteorological progress. As we prepare for future storm seasons, we invite researchers, meteorological agencies, and experts to partner with us, build on our open source models, and explore our forecasts on Weather Lab. By combining advanced machine learning with the indispensable real-world expertise of human forecasters, we aim to create a collaborative weather forecasting ecosystem that can save lives and help communities adapt to a changing climate.

**Note: For official weather forecasts and warnings, refer to your local meteorological agency or national weather service.**