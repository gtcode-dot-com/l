---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-09-26T20:05:26.373478+00:00'
exported_at: '2026-09-26T20:05:28.331943+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/generating-scenarios-extreme-events-without-extreme-data-0824
structured_data:
  about: []
  author: ''
  description: MIT engineers developed a tool that predicts plausible extreme events
    and worst-case scenarios, such as an extreme storm’s likely duration, intensity,
    and area of impact. Importantly, the model doesn’t need to know about previous
    extreme events in order to generate plausible future extreme events.
  headline: Generating scenarios for extreme events, without extreme data
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/generating-scenarios-extreme-events-without-extreme-data-0824
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Generating scenarios for extreme events, without extreme data
updated_at: '2026-09-26T20:05:26.373478+00:00'
url_hash: e8e03f68c1bad10e87020c64da9cfa8729718172
---

Can a city’s seawall stand up to a blockbuster storm? Will a region’s power grid hold against record-breaking heat? And can a town’s fire-fighting resources contain a major wildfire?

To answer these questions, communities will first need to know how such extreme events could unfold. How far is a wildfire likely to spread? How much of a region might a storm impact? How long could a heat wave last?

But extreme events are notoriously difficult to anticipate. By their nature, they are outliers. In the history of record keeping, extreme events are sporadic and rare. Yet most methods that assess a region’s risk depend on extreme events of the past to characterize even more extreme, worst-case scenarios in the future.

Now, MIT engineers have developed a tool that generates plausible extreme events and worst-case scenarios, and maps their characteristics, such as an extreme storm’s likely duration, intensity, and area of impact. The key to their method is that it does not need to know about previous extreme events in order to generate plausible future extreme events.

Instead, the method, in the form of a machine-learning algorithm, learns from a dataset, such as a region’s daily weather records and maps. This record may or may not contain past extreme deviations, such as record-setting heat or rain. The team’s algorithm takes a statistical approach to learn from the available data, to exclude implausible weather scenarios. The method then generates plausible extreme events that are likely to occur in a region with a given frequency (such as once every 100 years), and projects how those extreme events might look in terms of their size, intensity, and duration.

“We are trying to model extreme, unprecedented events that no one has seen before, that are not in the dataset,” says Kai Chang SM ’25, a PhD student in the MIT Center for Computational Science and Engineering.

“An event like Hurricane Katrina is something that happens every 30 to 40 years,” adds Themis Sapsis, the William I. Koch Professor of Mechanical and Ocean Engineering at MIT, a core member of the Center for Computational Science and Engineering, and an affiliate of the MIT Institute for Data, Systems, and Society. “What will be the Katrina that happens every 100 years? How bad will it be? That’s exactly what we’re trying to quantify, to help planners prepare for plausible extreme scenarios.”

Beyond weather events, the approach, which the team has dubbed Extreme Event Aware, or “η-learning,” can be applied to other fields, such as robotic navigation and financial markets.

“Financial market crashes are extreme events that are a complicated combination of things, involving many different sectors,” Chang says. “What is the interaction that leads to a market crash? That is something that this method could explore.”

Sapsis and Chang detail their new method in an open-access paper that
[appeared on Aug. 20 in the journal
*Nature Communications*](https://www.nature.com/articles/s41467-026-76811-x)
*.*

**“Riskier than everything”**

To estimate a region’s risk of an extreme weather event, planners, policymakers, and insurance companies typically ask questions such as “What does a once-every-100-year storm look like for New York City?” For answers, they use computer simulations that must be trained on data that includes extreme, once-in-a-century events, in order to learn the conditions leading up to those events and generate scenarios of how those events might look in the future.

“These methods assume there are very disastrous events that we have seen in the dataset, and they build a method to either estimate the risk of those events, or they try to predict exactly the events that have happened,” Chang says. “We are trying to see: What do unprecedented extreme events look like that are riskier than everything that has happened before and yet are still plausible?”

For example, if the most extreme rainfall measurement ever recorded in New York City is 200 millimeters, what kind of storm would produce an even more extreme measurement, of 300 millimeters? Such an event has never been recorded before and yet could still be plausible. City planners would want to know where such a storm would hit, how big an area it would cover, and how intense it would be. A simulation of the storm could help them assess infrastructure and plan reinforcements.

“We want to predict maps of these worst-case scenarios,” Sapsis says. “There is no method that does this efficiently to predict events that happen rarely.”

**Extreme learning**

The team’s new algorithm generates plausible, unprecedented extreme scenarios, without needing to train on previous extreme event data. To do so, the algorithm combines and learns statistics, or probabilities, about the relationships between two types of data: point statistics and spatial maps.

To demonstrate, the researchers applied the method to generate maps of future extreme precipitation events over the continental United States. The researchers began with 25 years of hourly precipitation maps, which they pooled into daily maps. From the full record, they computed point statistics describing how often the maximum rainfall across a map reached a given level. They then trained the algorithm on paired low- and high-resolution spatial maps from just the first six months of the record, which contained few or no examples of the most extreme rainfall levels.

From these data, the algorithm learned how patterns in low-resolution maps correspond to detailed, high-resolution precipitation maps. It then used the point statistics to constrain the rainfall extremes represented in those maps. This combination enables the algorithm to generate plausible spatial patterns for events more extreme than those represented in the training data — for instance, the possible locations, sizes, and intensities of a once-in-a-century rainfall event with a maximum of 300 millimeters.

A user can prompt the trained algorithm with a question such as, “What could a once-in-a-century storm look like in New York City?” The algorithm then generates maps of statistically plausible storms that are likely to occur with that frequency, including characteristics such as the storm’s size, area of coverage, and intensity of rainfall.

“Someone can say, ‘I’m interested in building things to withstand the risk of an event that happens every 100 years,’” Chang says. “What we can do then is produce thousands of possible realizations that will happen with this sort of rare frequency.”

As long as relevant point statistics and spatial data are available, the method could be applied to visualize other unprecedented events such as extreme floods and wildfires.

“Extreme events have become a strategic concern, not just an environmental one — we’ve optimized global systems for efficiency, and the price of that efficiency is that there’s very little slack left anywhere. A single extreme event propagates through supply chains, energy markets, and food systems in weeks,” Sapsis says. “Being able to put a probability on an event that hasn’t happened yet is now a question of national and economic resilience.”

This research was supported, in part, by a Vannevar Bush Faculty Fellowship and the U.S. Air Force Office of Scientific Research.