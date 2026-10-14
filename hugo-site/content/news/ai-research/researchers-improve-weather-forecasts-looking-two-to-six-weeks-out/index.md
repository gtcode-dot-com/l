---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-14T23:35:08.069469+00:00'
exported_at: '2026-10-14T23:35:09.784938+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/researchers-improve-weather-forecasts-looking-two-six-weeks-out-1014
structured_data:
  about: []
  author: ''
  description: A new technique significantly improves weather forecasting beyond two
    weeks. Researchers developed a machine-learning model that learns to correct errors
    in existing forecasting models to make their output more accurate over the two-to-six-week
    time frame, a key window for emergency planning.
  headline: Researchers improve weather forecasts looking two to six weeks out
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/researchers-improve-weather-forecasts-looking-two-six-weeks-out-1014
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers improve weather forecasts looking two to six weeks out
updated_at: '2026-10-14T23:35:08.069469+00:00'
url_hash: 378737ffe80d7a1a1f25101f171f1b314367d29d
---

In 2021, Texas suffered the worst energy infrastructure failure in state history, following three severe winter storms in February. At least 246 people were killed as a result of the disruptions, which led to food, water, heat and electricity shortages.

If energy officials had had more time to prepare for the storms, for example by bringing in more trucks of natural gas to disrupted areas, damage from the event could have been mitigated. Unfortunately, weather forecasts beyond two weeks are notoriously unreliable, making for a tighter window for energy operators, farmers, and emergency response officials around the globe.

A new technique by a team including researchers at MIT significantly improves weather forecasting beyond two weeks. The researchers developed a machine-learning model that learns to correct errors in existing forecasting models to improve their output over the two-to-six-week time frame. When applied to a gold-standard forecasting model, it doubled forecasting accuracy over that time frame, placing first in a prominent international forecasting competition.

In a
[new paper in
*Nature*](https://www.nature.com/articles/s41586-026-11126-x)
, the researchers describe their approach and show how it enables forecasts that for the first time beat climatologic averages between two and six weeks.

“Not only does this do better on time averaged forecasts for this range, which is already very useful for farmers and members of the energy industry trying to match supply with demand, but it also improves predictions of extreme weather events, whether it’s flooding or cold spells or something else,” co-author and MIT Research Scientist Judah Cohen says. “It’s really important to predict both, but extreme events might be the most impactful part of this for society.”

Joining Cohen on the paper are lead authors Hannah Guan, a Harvard College undergraduate; Soukayna Mouatadid, a University of Toronto postdoc; Genevieve Flaspohler SM ’18, PhD ’22; Paulo Orenstein, an associate professor at Brazil’s National Institute for Pure and Applied Mathematics; Jeremy Berman of the data company DTN; Jakob Schloer and Joshua Talib, researchers with the European Center for Medium-Range Weather Forecasts; and Alex Lu, Haiyu Dong, Jonathan Weyn, Zekun Ni, and Lester Mackey, all researchers at Microsoft.


**Longer forecasts**

In the 1970s, longtime MIT Professor Edward Lorenz came up with the idea of chaos theory to describe how tiny changes in initial weather conditions lead to completely different outcomes.

“He came up with this theoretical two-week limit where beyond that, we just can’t predict weather because the noise in the system grows so much that it overwhelms any signal you start with,” Cohen says. “That had a strong influence on the field that may have held people back from exploring forecasting beyond the two-week range. I never really believed that completely. In theory the atmosphere can create an infinite number of patterns, but it likes to fall into these favorite patterns over and over again. Once one thing happens, I think you can predict the domino that will fall after that, and the domino that will fall after that.”

Today, the best weather forecasts come from either dynamical models, which numerically simulate how the atmosphere and oceans evolve over time, or artificial intelligence models, which learn to make predictions from historical weather data. AI models have shown improvements in predicting weather at short ranges, but they’re even worse than dynamical models at longer time ranges.

Cohen, who is based in the MIT Department of Civil and Environmental Engineering, focuses on forecasting weather two to six weeks in advance, which is known as subseasonal forecasting. “That range is referred to as the ‘predictability desert,’ because in the short range you can capitalize on the initial conditions in the climate system and the atmosphere, and on the longer term you have these slow, varying boundary forces, like the super El Niño everyone’s focused on this winter,” Cohen says. “The subseasonal range can’t take advantage of either of those. In most cases forecasting in the subseasonal ranges is no different than going to a casino and rolling the dice.”

Cohen credits his co-author Lester Mackey, whom he has been collaborating with for more than a decade, with the initial idea of using machine learning to reduce errors in forecasting models.

“We built this wrapper — Lester calls it postprocessing,” Cohen says. “We know AI models have a lot of errors, so we thought maybe we can quantify those errors and remove them.”

While other forecasting systems do more simplistic error correction, the research team’s postprocessing layer uses AI to learn from a forecasting system’s mistakes based on historic data and shifts its forecasts. In that time range, forecasters use so-called probabilistic forecasts, where the likelihood of a range of possibilities if given.

“As more forecasts and data become available, our model adaptively improves its correction,” Cohen says.

To build the model, the researchers used MIT Engaging, a supercomputing cluster hosted by MIT’s Office of Research Computing and Data, but the resulting model does not require a supercomputer to run.

To put their model to the test, last year the research team submitted three models that included their post-processing layer to the European Center for Medium-Range Weather Forecasts (ECMWF), which is considered the best forecasting center in the world. Each season ECMWF holds forecasting competitions between models.

The submission that won first place combined ECMWF’s forecasting model with another, and then applied the postprocessing correction on top. That approach ended up doubling the original model’s predictive power in the subseasonal range. For the first time, the model offered an improvement over relying on climatologic averages.

“Up until now, no one had been able to show a model predicts weather better than long term averages for these subseasonal forecasts,” Cohen says. “They’ve pretty much all been worse than that — you could literally flip a coin and do better. People have questioned if it’s even worth investing in models at all for this time range. We consistently beat climatology averages with our models.”

The model also showed a statistically significant improvement in the ability to predict extreme weather.

“That’s one of the more important findings, because it’s so difficult to accomplish,” Cohen says. “When the ECMWF developed their own, non-AI, error-correction to their model, it got worse at predicting extreme weather. I think that’s because traditional error, or bias, correction is always trying to get to the mean, whereas extreme weather is on the fringe of probabilities.”

**Preparing for disaster**

In the
*Nature*
paper, the team showed their technique could be used to improve land forecasts in most regions across the globe. They also applied their bias correction technique to other models and showed it improved those as well, putting even lesser models on par with the ECMWF’s forecasts.

“What’s nice about our model is it’s an add-on wrapper,” Cohen explains. “We used it with the ECMWF’s dynamical model because that was considered the best, but it can be used with any model. It even improves models that are already bias corrected using another AI algorithm. So it shows a robust improvement. And it’s open source and low cost.”

Cohen says the meteorological office for the Republic of Kenya has already reached out about implementing the model to improve forecasting of the annual monsoon season to improve agricultural yields this winter. He hopes other groups will also use the model.

“This could help you decide when to fertilize around rain, when there’s a freeze coming to protect crops during winter harvests, or help you avoid droughts,” Cohen says. “It could also be useful for energy and emergency management. I’ve talked to energy officials who say, ‘If I’m told two days before that an ice storm’s coming, I don’t have enough time, but if I had two weeks, that could be enough to make adequate preparations.”

The work was supported, in part, by the U.S. National Science Foundation, the Carlos Chagas Filho Foundation for Research Support, and the European Union.