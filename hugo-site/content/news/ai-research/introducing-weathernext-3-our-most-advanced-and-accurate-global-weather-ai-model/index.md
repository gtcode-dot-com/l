---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-03T03:01:15.046002+00:00'
exported_at: '2026-10-03T03:01:18.409519+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model
structured_data:
  about: []
  author: ''
  description: WeatherNext 3, our most advanced global weather AI model, is now in
    Search, Gemini, Maps, Google Maps Platform, and Cloud.
  headline: Introducing WeatherNext 3, our most advanced and accurate global weather
    AI model
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/introducing-weathernext-3-our-most-advanced-and-accurate-global-weather-ai-model
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Introducing WeatherNext 3, our most advanced and accurate global weather AI
  model
updated_at: '2026-10-03T03:01:15.046002+00:00'
url_hash: d75554c78e0fe54a871a452ed74377e3e4786640
---

## Real-world data at continuous global scale

WeatherNext 3's biggest leap forward is what it learns from. Most AI weather models, including WeatherNext 2, are trained on data from numerical weather prediction (NWP) models. Although useful, NWP models are complex, supercomputer-driven physics simulations that carry a six-hour data lag. This lag can lead to biases for fast-changing variables like rain or surface temperature.

By ingesting a mosaic of live, global geostationary satellite data, our new model gains a rich, continuously updating view of the atmosphere. This allows the model to generate a new forecast every hour, each one grounded in the most recent satellite observations available, at up to 5-kilometer resolution.

This is important because critical weather develops fast. When storms, fronts, or precipitation systems materialize suddenly, our rapid update cycle and higher resolution provides earlier, more detailed insights needed to help drive an effective response.

Some variables, like temperature and humidity, can fluctuate dramatically over just a few kilometers, which is particularly relevant for communities near coastlines, valleys, or mountain ranges. Traditional models struggle here because they train on representations of the atmosphere that lack detail and miss extreme local variations.

To address this, WeatherNext 3 instead trains directly on sparse weather station observation data. This allows us to make global forecasts on a 5-kilometer grid that account for regional details like topography.

This breakthrough is particularly vital for regions across Latin America, Africa, and Asia-Pacific that have historically been underserved by high-resolution forecasting due to the immense supercomputing costs of traditional regional models. It brings localized, high-fidelity forecasting to billions of people and local businesses in these areas.

Beyond improved resolution and forecast frequency, our model introduces predictions specifically engineered for renewable energy production. The model forecasts 100-meter wind speeds (roughly at turbine-height) for precise wind-energy output, alongside high-resolution cloud cover and sun radiation levels to help solar farms estimate how much light they will receive on the ground.

This data is crucial for global clean energy planning, allowing grid operators and renewables developers to accurately predict how much power their clean energy assets will generate and match it with consumer demand.

## Precipitation forecasting at breakthrough accuracy

Global weather models notoriously struggle to accurately predict precipitation. Rain and snow systems are driven by fast-moving cloud processes on tiny scales that are hard to model accurately using traditional physics-based simulations. Consequently, AI forecasts often produce blurry estimates or miss the boundaries of severe storms entirely.

To solve this, we train our model on two exceptionally high-quality sources of precipitation data: NASA’s satellite-based Integrated Multi-satellite Retrievals for GPM (IMERG) and our own global precipitation reanalysis based on satellite radar.

The result is a significant leap in precipitation forecasting accuracy. In medium-range global forecasts, evaluations against baselines show a Continuous Ranked Probability Score (CRPS) improvement of up to 60% against IMERG, 30% for MRMS, and 10% against rain gauge measurements for early lead times.