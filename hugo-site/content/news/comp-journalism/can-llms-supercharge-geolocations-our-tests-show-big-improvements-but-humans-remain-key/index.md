---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-11-08T05:00:07.031016+00:00'
exported_at: '2026-11-08T05:00:08.778109+00:00'
feed: https://www.bellingcat.com/feed/
language: en
source_url: https://www.bellingcat.com/resources/2026/10/22/can-llms-supercharge-geolocations-our-tests-show-big-improvements-but-humans-remain-key
structured_data:
  about: []
  author: ''
  description: In September, the AI company Anthropic claimed its models were approaching
    “superhuman capabilities for geolocating outdoor photos”. Bellingcat put that
    claim to the test.
  headline: Can LLMs Supercharge Geolocations? Our Tests Show Big Improvements But
    Humans Remain Key
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.bellingcat.com/resources/2026/10/22/can-llms-supercharge-geolocations-our-tests-show-big-improvements-but-humans-remain-key
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Can LLMs Supercharge Geolocations? Our Tests Show Big Improvements But Humans
  Remain Key
updated_at: '2026-11-08T05:00:07.031016+00:00'
url_hash: 2917e7e2a11f2e86b6dd762140c1aa623ba0ce6d
---

*Sign up
[here](https://bellingcat-investigations.beehiiv.com/)
to receive Bellingcat’s biggest investigations by email as soon as they are published*
.

In September, the AI company Anthropic published a blog post that claimed its models were approaching “
[superhuman capabilities](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)
for geolocating outdoor photos”. Anthropic made this claim by comparing its models’ performance to that of players of the popular online game GeoGuessr, which challenges users to geolocate Google Street View images.

Bellingcat has been running its own benchmark tests on AI
[models](https://www.bellingcat.com/resources/how-tos/2025/06/06/have-llms-finally-mastered-geolocation/)
since June 2025, right around the time when Large Language Models (LLMs) began to challenge reverse image searches for assisting with geolocation tasks. In our first round, GPT 4o-mini from OpenAI appeared to be the best tool for geolocating, a title which was taken by Google AI mode when we performed
[our second round](https://www.bellingcat.com/resources/2025/08/14/llms-vs-geolocation-gpt-5-performs-worse-than-other-ai-models/)
of tests a few months later in August 2025.

This time, we significantly upped the ante for the models, providing increasingly challenging photos and asking for only one set of coordinates. We tasked not only closed-weight models from
[Claude](https://platform.claude.com/docs/en/models/overview)
,
[Grok](https://docs.x.ai/developers/models)
,
[Gemini](https://ai.google.dev/gemini-api/docs/models)
,
[ChatGPT](https://developers.openai.com/api/docs/models)
, and
[Mistral](https://docs.mistral.ai/models)
, but also
[open-weight](https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model)
models from Moonshot AI’s
[Kimi](https://platform.kimi.ai/docs/models)
, commercial provider
[GeoSeer](https://geoseeer.com/)
and the non-generative geolocation model
[GeoClip](https://github.com/VicenteVivan/geo-clip)
. In total, we fed each model 52 photos that had not been published anywhere on the internet before.

The results showed that the current generation of models have markedly improved geolocation capabilities. Anthropic’s Opus and Fable, as well as Google’s recent Gemini 4 Argon model, performed the best on geolocation tasks, narrowing down locations from images faster than a human could under specific conditions. Preliminary tests of a set of agentic skills and tools being developed internally by Bellingcat also showed promising results in further improving the geolocation performance of generic-use AI agents.

But crucially, the tests also showed why humans remain necessary for accurate and trustworthy geolocation work, as no models were foolproof. This is particularly important given the increased use of AI in military contexts. The Anthropic blog post focused specifically on geolocating photos for military and intelligence purposes such as targeting, a historically labour-intensive process requiring significant human expertise.

While our tests showed some models performed extremely well at narrowing down results to the correct general area, none were close to being perfect at finding the exact spot a picture was taken. That accuracy is extremely important in geolocation, especially in military contexts where the cost of incorrect information
[can be life or death](https://www.bloomberg.com/graphics/2026-iran-school-attack/)
. It is also important for organisations like Bellingcat whose reputation relies on pinpoint factual accuracy.

## Our Methods

To compare model results, we used two metrics built on the distance in kilometres between a prediction and the real location.
*GeoGuessr Score*
was used to assess whether models could systematically identify the general area, while the
*Mean Log Score*
(explained below) measured which models most accurately pinpointed the correct location in the final few kilometres.

The
*GeoGuessr Score*
metric is based on the online
[game](https://www.geoguessr.com/)
of the same name, whose scoring system Stanford University academics
[reverse-engineered](https://arxiv.org/pdf/2307.05845)
in a 2024 study. This system rewards answers close to the general area an image was taken, but does not strongly distinguish between guesses close to the precise location. For example, an answer 200km from the correct location with more points than one 2,000km away. However, an answer 500m from where a picture was taken and another 5km away achieve a similar score. For real-world geolocations, that distance matters a great deal.

For more precision, we introduced a custom metric that grades models higher if they narrow down the search in the last few kilometres. This metric, the
*Mean Log Score,*
assigns a value from 0 (completely inaccurate) to 100 (perfect model) and works on a logarithmic scale instead of a linear one like GeoGuessr score.



Therefore, a 10-fold improvement in distance means the same whether it is from 5km to 500m or from 500km to 50km. You can compare both metrics
[here](https://public.flourish.studio/visualisation/30578383/)
.

Below are the model results sorted by either metric, showing how many photos each model geolocated within distance bands from the true location.

Several models placed at least 10 out of the 52 photos correctly within one kilometre, and the top-performing models placed over 50 percent of the photos within 25 kilometres.

*NOTE: Geoseer-fast refused to answer on four of the 52 photos, claiming “This image is not suitable for geolocation”, while Mistral-large-4 refused once with “insufficient information in image to identify location”. Kimi-k2.6 also failed to provide a set of coordinates on one photo, and Gemini 4 Argon timed out repeatedly on one photo.*

## Our Test

To independently assess the models, we sought to give them very specific instructions and some images that were harder to geolocate than those provided in our past tests. The prompt asked for a single set of coordinates reflecting the photographer’s location. The purpose of restricting the response in this way was to prevent hedging, such as multiple guesses or confidence scores, and make the grading more uniform across different models. Models were allowed to use their providers’ built-in tools: search, code execution and page fetch. We capped their token output at 64,000 and ran each model under its default effort setting with a maximum time of 15 minutes per photo. If a model did not return coordinates on the first prompt, we also allowed a single rescue prompt asking it to do so using its previous reasoning and without using any tools.


The images provided were unique, from around the world, not published on the internet before, scrubbed of metadata and provided without any context. They did not contain significant landmarks. We also included images in snowy, foggy and nighttime conditions.


The results show that the LLMs tested could, in many circumstances, successfully narrow down a location much faster than a human can geolocate even without any context. This is not limited to Google Street View-style images. Take, for example, this image of vegetation and a very small part of a rooftop.

An example of a photo used for testing, with annotation added after the test to highlight the only man-made object visible. Credit: Bellingcat.

For an average person, identifying the country this photo was taken in without any context could take a significant amount of time. However, multiple models quickly narrowed it down to Kenya. You can navigate their answers in the map below. Notice how several correctly inferred enough vegetation details to narrow down the exact part of the world and the park itself, but also that for many, the final response was a best guess only. It is important to note that even though some models were correct, others were significantly off.

The full model results for all 52 photos can be seen in the table below.

Of the models tested, Gemini 4 Argon scored highest on the Mean Log Score, and Claude’s models (Opus and Fable) were at the top of the table regardless of the score metric. Even Claude Sonnet, the weakest of its lineup, consistently came close to the real location while being the fastest to answer across all models.


This was followed by GPT-6 Astra and GPT-6.1 Sol, as well as other Claude and Gemini models, and then the geolocation-specific model, GeoSeer Fast, which provided good results but also timed out frequently. We tested GeoSeer’s more competent Agent model, but it refused to answer on eight photos and regularly timed out.

For secondary factors like time and cost, Claude also performed well on both metrics, and Gemini Argon, while much slower, came at a similar cost to Opus. Based on API rates, Argon and Opus models offered the best balance of accuracy and cost, especially compared to Fable and Grok. Grok was the most expensive option and had an underwhelming bottom-half performance. Meanwhile, GeoClip was freely available but only outperformed Claude Haiku.

## Model Limitations

While we sought to analyse the most prominent models, there was one that we could not include as it has yet to be fully released.

## Support Bellingcat

Your donations directly contribute to our ability to publish groundbreaking investigations and uncover wrongdoing around the world.

In its
[blog post](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)
, Anthropic claimed its Mythos model beats “even the strongest human baseline on median distance error, scoring 37.0km and 47.2km across 6,000 photos (placing 23.7 percent and 23.1 percent within 1km).“ But Nuno Moniz, Associate Research Professor at the Lucy Family Institute for Data &amp; Society at the University of Notre Dame, told Bellingcat that “the median represents a strong simplification of what would be acceptable to compare AI-based system performance with regards to humans”.

Anthropic compared its models to competitive GeoGuessr players and their success in identifying the location of Google Street View images. The entire set of test images was online and there was no guarantee the models were processing the imagery for the first time.

While Anthropic has been relatively open about these methods, not all developers have been as forthcoming. It is therefore difficult to assess whether the same limitations will impact all other models, or whether there will be further caveats that we are simply not aware of.

Moniz said that “the increasing availability of benchmarking tools and datasets has made it somewhat difficult to measure reliability in test results such as these”. Specifically, due to the ”uncertainty as to whether that data was included in its training”. This is why we ran our Bellingcat tests with non-published photos sourced from Bellingcat staff and the Bellingcat Volunteer Community.


A further limitation of any models comparing performance to GeoGuessr scores is that the game uses images from Google Street View, which is limited to a select number of countries, and within these, a limited number of roads. Street View is also intentionally skewed to feature clear, high-quality photos taken during daytime that are useful for navigation, and users can pan around their view. There are also some well-known tricks that allow GeoGuessr players to bypass actual geolocation to correctly guess the location of photos: for example, Google is known to use a
[black car](https://geometas.com/metas/countries/jordan/)
in Jordan and a white car in the UAE to capture imagery. While this wouldn’t necessarily impact model performance, it is a drawback of measuring against GeoGuessr score as the game has a set of workarounds that can bypass geolocation skill.


Anthropic’s data consisted of thousands of social media photos of various scenes. Once again, though, these photos were online and may have featured in the model’s training data. Anthropic’s
[blog post](https://www.anthropic.com/research/intelligence-targeting-conventional-weapons-capabilities)
contained four images as an example of this dataset.

Images used as part of Anthropic’s dataset. Credit: Anthropic.

The examples Anthropic shared are relatively easy to geolocate as they feature recognisable buildings and signs. But footage that requires geolocation often comes from regions where access is limited and which do not feature on social media or Street View.


Specifically, in a military and intelligence context, footage often involves low-resolution material and intentionally obscured details recorded in remote or inaccessible areas. Context that could be found online can be uncertain or plain wrong, especially during a developing situation, such as the image below that Bellingcat investigators geolocated when
[verifying](https://www.bellingcat.com/news/2026/03/08/video-shows-us-tomahawk-missile-strike-next-to-girls-school-in-iran/)
a US strike on a school in the city of Minab in Iran that killed at least 120 children earlier this year.

*An example of*
[*footage*](https://www.bellingcat.com/news/2026/03/08/video-shows-us-tomahawk-missile-strike-next-to-girls-school-in-iran/)
*geolocated by Bellingcat.*
Screen shot from Mehr News.

Anthropic researchers acknowledge this caveat, writing that it “does not as clearly emulate the task of precisely pinning down a location in near-real-time in a less populated battlefield setting; that is a task for future research.”

As noted, it is also possible that similar caveats need to be applied to other models when seeking to understand and interpret any geolocation-related benchmarking.

## Supercharged Models

In parallel to the above models, we also tested a set of agentic skills and tools being developed internally by Bellingcat. These are researcher-informed instructions and code that can equip generic-use AI agents to augment their geolocation ability. For instance, we designed skills such as allowing it to download
[Environmental Systems Research Institute (ESRI](https://www.esri.com/en-us/capabilities/imagery-remote-sensing/capabilities/content)
) satellite imagery tiles. We also designed another skill that enabled direct access to data from Bellingcat’s
[OpenStreetMaps search tool](https://www.bellingcat.com/resources/how-tos/2023/05/08/finding-geolocation-leads-with-bellingcats-openstreetmap-search-tool/)
, which aims to assist geolocation efforts by comparing items identified in imagery (like the position of a pylon compared to a nearby railway line) to OpenStreetMaps data.
[GeoSleuth](https://github.com/Oldcircle/geo-sleuth)
is a similar project that has already been published, which we used for comparison. We picked Claude’s Opus 5.5 model to run both skills customisations because of its strong performance and reasonable pricing, and ran all the photos through the supercharged models under the same conditions – except that they had no timeout enforced as the supercharged models required more time to utilise their extra skills.

The different timeout conditions and expanded toolset do not allow for a direct comparison of the customised models to the previous off-the-shelf models’ results, even if they both outperformed the barebones Opus model they were based on, and all other models on
*GeoGuessr Score,*
with only Argon ranking above Bellingcat’s agent in
*Mean Log Score*
.

Still, this test allows us to showcase why skill customisations can bring value. Take the following photo.

An image captured at the Global Campus of Human Rights in Venice. Credit: Bellingcat.

This is not an exceptionally hard geolocation, and 11 of 17 models answered within 5km of the actual capture
[location](https://www.google.com/maps/place/Venice,+Metropolitan+City+of+Venice,+Italy/@45.4275458,12.3815659,107m/data=!3m1!1e3!4m6!3m5!1s0x477eb1daf1d63d89:0x7ba3c6f0bd92102f!8m2!3d45.440379!4d12.3159547!16zL20vMDdfcGY?entry=ttu&amp;g_ep=EgoyMDI2MTAxOC4wIKXMDSoASAFQAw%3D%3D)
in Venice, Italy. GPT-Sol answered with the correct monastery, but only Bellingcat’s agent and GeoSleuth answered with the exact camera position coordinates. This was possible because both model customisations can download and compare satellite imagery tiles, which allows them to validate not just which monastery the photo was taken at but also the correct courtyard position and orientation from visual cues. You can click the buttons in the list below to audit each model’s final answer.

While in this instance the supercharged models got the exact spot, there were other instances where they did not, as the scores in the
[results table above](https://www.bellingcat.com/resources/2026/10/22/can-llms-supercharge-geolocations-our-tests-show-big-improvements-but-humans-remain-key/#:~:text=GeoGuessr%20Score%2C%20with%20only%20Argon%20ranking%20above%20Bellingcat%E2%80%99s%20agent%20in%20Mean%20Log%20Score.)
show. This again emphasises that even with extra skill sets added, these models were still far from infallible.

## Tests Conclusions

Despite increased model improvement, our analysis shows that important caveats remain and it is important to keep a human in the loop when seeking to guarantee a geolocation is precise and correct.


Our tests show that the coordinates models provide as answers are rarely an exact match, even with supercharged models. Invariably, even the best models, with the best tools, can confidently claim a wrong position. Anthropic says its Mythos model was able to pinpoint less than a quarter of its social media photos dataset within a 1km radius. But narrowing down a location is rarely the trickiest part of geolocation work. A large part of important geolocation work is in the final stretch: finding specific coordinates from a general area. This level of specificity is needed because a general area is not a match. Matching features and perspective are necessary for an accurate geolocation, and in many cases that is done on very low-quality images or even by cross-referencing multiple sources.

This level of precision is essential for investigations where it matters what building a person could be found at, what lines of sight individuals might have had, or what impact an air strike might have led to.

Since LLMs can still confidently get things wrong, as our analysis shows, all results still have to be verified independently. Strong human geolocation skills therefore remain crucial, as the more one understands about geolocations, the better one can verify or take to completion an automated result.

Though it can speed up geolocation work significantly, especially in narrowing down an area of interest, AI models remain a useful assistant rather than a tool we can blindly delegate geolocations to.

---

*Bellingcat is a non-profit and the ability to carry out our work is dependent on the kind support of individual donors. If you would like to support our work, you can do so*
[*here*](https://www.bellingcat.com/donate/)
*. You can also subscribe to our*
[*Newsletter*](https://bellingcat-newsletter.beehiiv.com/?modal=signup)
*and follow us on Bluesky*
[*here*](https://bsky.app/profile/bellingcat.com)
*, Instagram*
[*here*](https://www.instagram.com/bellingcatofficial/)
*, Reddit*
[*here*](https://www.reddit.com/r/bellingcat/)
*and YouTube*
[*here*](https://www.youtube.com/@bellingcatofficial/videos)
*.*