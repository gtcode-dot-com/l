---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-22T20:29:24.766322+00:00'
exported_at: '2026-10-22T20:29:26.530702+00:00'
feed: https://deepmind.google/blog/rss.xml
language: en
source_url: https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types
structured_data:
  about: []
  author: ''
  description: 'Explore Forest Typology (ForTy) 2020: a global 10-meter map categorizing
    Earth''s land into six distinct forest and land-use types, plus an annual time
    series.'
  headline: 'Beyond tree cover: mapping the world’s forest types'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://deepmind.google/blog/beyond-tree-cover-mapping-the-worlds-forest-types
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Beyond tree cover: mapping the world’s forest types'
updated_at: '2026-10-22T20:29:24.766322+00:00'
url_hash: 655df0fb22ace8918dccb9cedab8a4d53b00e1dc
---

October 22, 2026

Research

# Beyond tree cover: mapping the world’s forest types

Maxim Neumann and Charlotte Stanton

Copied

A new 10-meter resolution map shows which of the world's forests are natural, planted, or farmed, and how they are changing over time

Protecting the planet's forests starts with a simple question: what type of forest are we looking at? From space, an old-growth rainforest, a eucalyptus plantation, and an oil palm estate can look like the same patch of green. But they hold very different amounts of carbon and biodiversity. Telling them apart, and knowing how each patch has changed over time, shows us where conservation is working and where natural forests are being converted into plantations and farms.

Today, Google DeepMind and Google Research, together with the World Resources Institute (WRI) and the International Institute for Applied Systems Analysis (IIASA), are releasing
[Forest Typology (ForTy) 2020](https://www.nature.com/articles/s41597-026-08299-5)
, a global map that categorizes every 10-by-10-meter patch of land on Earth into six distinct forest and land-use types, a key baseline for the EU's deforestation regulation. Alongside it, we're sharing an early time series that tracks how these forests changed each year from 2017 to 2025, including where natural forests were replaced by plantations or farms. For the first time, users can see at 10-meter detail worldwide, year by year, not just where forest was lost, but what replaced it: a timber plantation, a tree-crop farm or other land.

## Why "tree cover" isn't enough

All forests store carbon and, together, forests are home to most of the world's land-based plant and animal species. But a forest’s ecological value also depends on its history: a primary forest that has never been cleared holds far more carbon and biodiversity than a single-species timber plantation that is harvested every decade or two.

Most global maps only indicate whether trees are present. That's a challenge for those trying to protect natural forests. The European Union's regulation on deforestation-free products (EUDR), for example, requires that products like coffee, cocoa or palm oil do not originate from land that was forest in 2020 and has since been converted to agriculture. Similarly, wood products, such as furniture, must also be free of forest degradation: they can't come from primary forests that have since been converted into plantation or planted forests, or from naturally regenerating forests that have since been converted into plantation forests. As a result, companies and regulators need to know not just where trees are, but what kind of forest they form (primary or regrowing, planted or plantation, forest or farm) and what replaces that forest after a harvest.

Last year, we jointly released
[Natural Forests of the World 2020](https://research.google/blog/separating-natural-forests-from-other-tree-cover-with-ai-for-deforestation-free-supply-chains/)
, a 10-meter resolution global map that separated natural forests from all other tree cover. It offered a starting point to help companies and regulators implement the EU Deforestation Regulation, and to support commodity producers in meeting their commitments not to convert natural forest. That map answered one question for every patch of land: was it natural forest in 2020 or not? ForTy goes further, showing what kind of forest is there, from primary forest to timber plantation to tree crops, and, with the new time series, how that changes each year.

## How ForTy classifies the world's forests

Specifically, ForTy sorts land into six categories based on definitions from the UN Food and Agriculture Organization (FAO):

1. Primary forest: native forest with no visible signs of human disturbance.
2. Naturally regenerating forest: forest that grew back on its own, for example after logging or fire.
3. Planted forest: forest that people planted or seeded, and managed over long cycles.
4. Plantation forest: fast-growing, intensively managed tree farms, often of one species.
5. Tree crops and agroforestry: farms that grow things other than wood, like oil palm, rubber, cocoa, or fruit.
6. Other land: everything else, from grassland and cropland to cities and water.

The Forest Typology map for 2020. Each color shows the most common forest or land type in each square kilometer. Explore it at 10-meter detail in our
[Earth Engine app](https://nature-trace.projects.earthengine.app/view/forest-typology-2020)
.

Training our ForTy model was challenging because these categories depend in part on how land is used, not just how it looks. To teach our model the difference, we built a large-scale collection of forest-type examples with about 1.7 million labeled locations drawn from expert surveys, national and regional datasets, and targeted reviews of places where the model struggled. The model uses a custom architecture designed for the challenges of remote sensing data, and takes as a key input
[AlphaEarth Foundations embeddings](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_SATELLITE_EMBEDDING_V1_ANNUAL)
, data-compact summaries of years of satellite observations for each 10-meter pixel, so it can spot subtle clues like planting patterns, growth cycles and harvest rhythms.

From above, the five forest and tree-crop classes can look alike. ForTy is able to identify the subtle differences in structure and seasonal patterns that set them apart, accurately categorizing them in a global map database. Imagery © Google Earth, Maxar Technologies, Airbus.

## Putting the map to the test

A map is only useful if people can trust it. So, with IIASA and WRI, we validated ForTy against more than 9,000 randomly chosen sites around the world. At each site, two trained experts studied high-resolution imagery and years of satellite records to determine which type of land was really there. ForTy picked the right forest type 90% of the time, and told forest apart from non-forest land 95% of the time, outperforming other global forest maps.

Beyond accuracy, we know that global conservation is not one-size-fits-all. Instead of giving a yes-or-no label for a specific patch of land, ForTy provides a probability score for each class, enabling users to adapt the classification to regional contexts and application-specific precision trade-offs. For example, a company assessing deforestation risk under EUDR might set a strict threshold, only accepting pixels the model is highly certain about to avoid regulatory risks. Meanwhile, a researcher estimating total forest extent might use the full spectrum of probabilities to get a fuller picture of the potential landscape.

## From a single snapshot in time to a story of change

A map of a single year is a useful baseline, but forests change. Our
[new early-release time series](https://nature-trace.projects.earthengine.app/view/forest-typology)
applies a similar approach to every year from 2017 to 2025. It shows not only where forests disappear and where they grow back, but also what kind of change happened: a natural forest turned into a timber plantation, for example, or abandoned land slowly regenerating into forest.

This differentiation matters because some of the most important changes are hard to see from space. When a natural forest is logged and replanted as a plantation, the land soon looks green again, so standard tree-cover maps might not pick up the change. ForTy's time series makes these hidden changes visible, both losses and gains.

## What's next

The Forest Typology 2020 map [described in Scientific Data] and the new time series are now freely available on Google Earth Engine under an open license. We hope governments, companies, conservation groups and scientists will use them to help build deforestation-free supply chains, direct forest finance where it’s needed, and protect the natural forests that matter most. Over the coming months, we'll keep improving the time series with our partners and users, and we'd love to hear how you use it. ForTy is part of our
[portfolio](https://developers.google.com/earth-engine/datasets/publisher/nature-trace)
of research on
[AI for Nature](https://deepmind.google/blog/mapping-modeling-and-understanding-nature-with-ai/)
, which includes mapping the drivers of forest loss, forecasting deforestation risk, modelling global species distributions, and monitoring biodiversity in the field. FortTy is also the latest addition to
[Google Earth AI](https://ai.google/earth-ai/)
, Google’s collection of geospatial models and datasets designed to help tackle the planet's most critical environmental challenges.

## Acknowledgements

This work was co-developed by Google DeepMind and Google Research, with the World Resources Institute and the International Institute for Applied Systems Analysis. We'd like to thank our co-authors Anton Raichuk, Peter Potapov, Myroslava Lesiv, Matthew Overlan, Mélanie Rey, Ravindran Rajakumar, Michelangelo Conserva, Radost Stanimirova, Michelle Sims, Sarah Carter, Elizabeth Goldman, Yuchang Jiang, Linus Scheibenreif, Ivelina Georgieva, Maria Shchepashchenko, Steffen Fritz, Nicholas Clinton, Dan Morris and Drew Purves, as well as the trusted testers who helped improved the map.

### AlphaEarth Foundations helps map our planet in unprecedented detail