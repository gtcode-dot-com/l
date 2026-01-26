---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-26T16:15:27.034802+00:00'
exported_at: '2026-01-26T16:15:29.312091+00:00'
feed: https://huggingface.co/blog/feed.xml
source_url: https://huggingface.co/blog/nvidia/earth-2-open-models
structured_data:
  about: []
  author: ''
  description: A Blog post by NVIDIA on Hugging Face
  headline: '**NVIDIA Earth-2 Open Models Span the Whole Weather Stack**'
  keywords: []
  main_image: ''
  original_source: https://huggingface.co/blog/nvidia/earth-2-open-models
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: '**NVIDIA Earth-2 Open Models Span the Whole Weather Stack**'
updated_at: '2026-01-26T16:15:27.034802+00:00'
url_hash: 8482226600fdae35b4b2a5b40835f3cca39e97c5
---

# **NVIDIA Earth-2 Open Models Span the Whole Weather Stack**

NVIDIA is excited to announce three new open-source models as part of the NVIDIA Earth-2 family, making it easier than ever to build weather forecasting capabilities across the weather stack, including tasks such as data assimilation, forecasting, nowcasting, downscaling and more. In addition, developers can quickly get started building weather and climate simulations by using NVIDIA open source software:

[Earth2Studio](https://github.com/NVIDIA/earth2studio)

for creating inference pipelines and

[Physics Nemo](https://github.com/NVIDIA/physicsnemo)

for training models.

NVIDIA Earth-2 comprises a set of accelerated tools and models which enables developers to bring together typically disparate weather and climate AI capabilities. Because Earth-2 is completely open, developers can customize and fine-tune their simulations to their specific needs, using their own data and their own infrastructure to build sovereign weather and climate predictions they fully own and control. Earth-2:

* Is a suite of leading open weather and climate models
* Is easy-to-use thanks to an ecosystem of open source software
* Enables you to create your own sovereign capabilities

## **Earth-2 Nowcasting: Kilometer-Scale Severe Weather Prediction**

Out now on Hugging Face:
[Earth-2 Nowcasting](https://huggingface.co/nvidia/stormscope-goes-mrms)
, powered by a new model architecture called StormScope, using generative AI to make country-scale forecasts into kilometer‑resolution, zero- to six-hour predictions of local storms and hazardous weather in just minutes. Earth-2 Nowcasting can generate the first predictions that outperform traditional, physics-based weather-prediction models on short-term precipitation forecasting by simulating storm dynamics directly. It harnesses AI to directly predict satellite and radar data.

This version is trained directly on globally available geostationary satellite observations (GOES) over the contiguous US (CONUS). However, this method could be applied to train versions of the model over other regions with similar satellite coverage.

[

Your browser does not support the video tag.
](https://huggingface.co/datasets/MikePritchard/Media-Jan2026-Earth2Launch/resolve/main/Earth-2%20NowCasting%20StormScope%20Visible%20and%20Radar%20CONUS%201080p.mov)

[Research Paper: Learning Accurate Storm-Scale Evolution from Observations](https://research.nvidia.com/publication/2026-01_learning-accurate-storm-scale-evolution-observations)

## **Earth-2 Medium Range: Highly accurate 15-Day Global Forecasts**

Out now on Hugging Face:
[Earth-2 Medium Range](https://huggingface.co/nvidia/atlas-era5)
, powered by a new model architecture called Atlas, enabling high-accuracy weather prediction for medium-range forecasts — or forecasts of up to 15 days in advance — across 70+ weather variables including temperature, pressure, wind and humidity. It uses a latent diffusion transformer architecture to predict incremental changes in the atmosphere so as to preserve critical atmospheric structures and reduce forecasting errors. On standard benchmarks, it outperforms leading open models such as GenCast on the most common forecasting variables measured by the industry.

[

Your browser does not support the video tag.
](https://huggingface.co/datasets/MikePritchard/Media-Jan2026-Earth2Launch/resolve/main/Earth-2%20Medium%20Range%20Forecast%20Ensembles%201080p.mov)

[Research Paper: Demystifying Data-Driven Probabilistic Medium-Range
Weather Forecasting](https://research.nvidia.com/publication/2026-01_demystifying-data-driven-probabilistic-medium-range-weather-forecasting)

## **Earth-2 Global Data Assimilation: An End-to-End AI Pipeline**

Coming soon to Hugging Face: Earth-2 Global Data Assimilation, powered by a new model architecture called HealDA, which produces initial conditions for weather prediction — snapshots of the current atmosphere, including the temperature, wind speed, humidity and air pressure, at thousands of locations around the globe. Earth-2 Global Data Assimilation can generate initial conditions in seconds on GPUs instead of hours on supercomputers. When coupled with Earth-2 Medium Range, this results in the most skillful forecasting predictions produced by an open, entirely AI pipeline.

[

Your browser does not support the video tag.
](https://huggingface.co/datasets/MikePritchard/Media-Jan2026-Earth2Launch/resolve/main/Earth-2%20GlobalDataAssimilation_CombinedRotate-1080p.mov)

[Research Paper: HealDA: Highlighting the Importance of Initial Errors in
End-to-End AI Weather Forecasts](https://research.nvidia.com/publication/2026-01_healda-highlighting-importance-initial-errors-end-end-ai-weather-forecasts)

These models join established open NVIDIA weather and climate models such as FourcastNet3, CorrDiff, cBottle, DLESym and more.

# **Getting Started**

[NVIDIA Earth2Studio](https://github.com/NVIDIA/earth2studio)
is an open-source Python ecosystem for quickly creating powerful AI weather and climate simulations. It provides all the necessary inference tools to get started with the new model checkpoints on Hugging Face. It’s as easy as:

[Getting Started Video](https://www.google.com/url?q=https://www.youtube.com/watch?v%3DSog6aCapZeA&sa=D&source=docs&ust=1769437755239233&usg=AOvVaw1veoCUlxlb401k3DL-1vQP)

# **Resources**

[Hugging Face Package for Earth-2 Nowcasting](https://huggingface.co/nvidia/stormscope-goes-mrms)

[Research Paper: Learning Accurate Storm-Scale Evolution from Observations](https://research.nvidia.com/publication/2026-01_learning-accurate-storm-scale-evolution-observations)

[Hugging Face Package for Earth-2 Medium-Range](https://huggingface.co/nvidia/atlas-era5)

[Research Paper: Demystifying Data-Driven Probabilistic Medium-Range
Weather Forecasting](https://research.nvidia.com/publication/2026-01_demystifying-data-driven-probabilistic-medium-range-weather-forecasting)

[Research Paper: HealDA: Highlighting the Importance of Initial Errors in
End-to-End AI Weather Forecasts](https://research.nvidia.com/publication/2026-01_healda-highlighting-importance-initial-errors-end-end-ai-weather-forecasts)