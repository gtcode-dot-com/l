---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-03T00:17:37.254856+00:00'
exported_at: '2026-03-03T00:17:42.271453+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/parking-aware-navigation-could-prevent-frustration-and-emissions-0219
structured_data:
  about: []
  author: ''
  description: By minimizing the need to drive around looking for a parking spot,
    this technique can save drivers up to 35 minutes — and give them a realistic estimate
    of total travel time.
  headline: Parking-aware navigation system could prevent frustration and emissions
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/parking-aware-navigation-could-prevent-frustration-and-emissions-0219
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Parking-aware navigation system could prevent frustration and emissions
updated_at: '2026-03-03T00:17:37.254856+00:00'
url_hash: aedb98148dcf415600c56f5d99615dc16ccfcf0d
---

It happens every day — a motorist heading across town checks a navigation app to see how long the trip will take, but they find no parking spots available when they reach their destination. By the time they finally park and walk to their destination, they’re significantly later than they expected to be.

Most popular navigation systems send drivers to a location without considering the extra time that could be needed to find parking. This causes more than just a headache for drivers. It can worsen congestion and increase emissions by causing motorists to cruise around looking for a parking spot. This underestimation could also discourage people from taking mass transit because they don’t realize it might be faster than driving and parking.

MIT researchers tackled this problem by developing a system that can be used to identify parking lots that offer the best balance of proximity to the desired location and likelihood of parking availability. Their adaptable method points users to the ideal parking area rather than their destination.

In simulated tests with real-world traffic data from Seattle, this technique achieved time savings of up to 66 percent in the most congested settings. For a motorist, this would reduce travel time by about 35 minutes, compared to waiting for a spot to open in the closest parking lot.

While they haven’t designed a system ready for the real world yet, their demonstrations show the viability of this approach and indicate how it could be implemented.

“This frustration is real and felt by a lot of people, and the bigger issue here is that systematically underestimating these drive times prevents people from making informed choices. It makes it that much harder for people to make shifts to public transit, bikes, or alternative forms of transportation,” says MIT graduate student Cameron Hickert, lead author on a paper describing the work.

Hickert is joined on the paper by Sirui Li PhD ’25; Zhengbing He, a research scientist in the Laboratory for Information and Decision Systems (LIDS); and senior author Cathy Wu, the Class of 1954 Career Development Associate Professor in Civil and Environmental Engineering (CEE) and the Institute for Data, Systems, and Society (IDSS) at MIT, and a member of LIDS. The research
[appears today in
*Transactions on Intelligent Transportation Systems*](https://arxiv.org/abs/2601.00521)
.

**Probable parking**

To solve the parking problem, the researchers developed a probability-aware approach that considers all possible public parking lots near a destination, the distance to drive there from a point of origin, the distance to walk from each lot to the destination, and the likelihood of parking success.

The approach, based on dynamic programming, works backward from good outcomes to calculate the best route for the user.

Their method also considers the case where a user arrives at the ideal parking lot but can’t find a space. It takes into the account the distance to other parking lots and the probability of success of parking at each.

“If there are several lots nearby that have slightly lower probabilities of success, but are very close to each other, it might be a smarter play to drive there rather than going to the higher-probability lot and hoping to find an opening. Our framework can account for that,” Hickert says.

In the end, their system can identify the optimal lot that has the lowest expected time required to drive, park, and walk to the destination.

But no motorist expects to be the only one trying to park in a busy city center. So, this method also incorporates the actions of other drivers, which affect the user’s probability of parking success.

For instance, another driver may arrive at the user’s ideal lot first and take the last parking spot. Or another motorist could try parking in another lot but then park in the user’s ideal lot if unsuccessful. In addition, another motorist may park in a different lot and cause spillover effects that lower the user’s chances of success.

“With our framework, we show how you can model all those scenarios in a very clean and principled manner,” Hickert says.

**Crowdsourced parking data**

The data on parking availability could come from several sources. For example, some parking lots have magnetic detectors or gates that track the number of cars entering and exiting.

But such sensors aren’t widely used, so to make their system more feasible for real-world deployment, the researchers studied the effectiveness of using crowdsourced data instead.

For instance, users could indicate available parking using an app. Data could also be gathered by tracking the number of vehicles circling to find parking, or how many enter a lot and exit after being unsuccessful.

Someday, autonomous vehicles could even report on open parking spots they drive by.

“Right now, a lot of that information goes nowhere. But if we could capture it, even by having someone simply tap ‘no parking’ in an app, that could be an important source of information that allows people to make more informed decisions,” Hickert adds.

The researchers evaluated their system using real-world traffic data from the Seattle area, simulating different times of day in a congested urban setting and a suburban area. In congested settings, their approach cut total travel time by about 60 percent compared to sitting and waiting for a spot to open, and by about 20 percent compared to a strategy of continually driving to the next closet parking lot.

They also found that crowdsourced observations of parking availability would have an error rate of only about 7 percent, compared to actual parking availability. This indicates it could be an effective way to gather parking probability data.

In the future, the researchers want to conduct larger studies using real-time route information in an entire city. They also want to explore additional avenues for gathering data on parking availability, such as using satellite images, and estimate potential emissions reductions.

“Transportation systems are so large and complex that they are really hard to change. What we look for, and what we found with this approach, is small changes that can have a big impact to help people make better choices, reduce congestion, and reduce emissions,” says Wu.

This research was supported, in part, by Cintra, the MIT Energy Initiative, and the National Science Foundation.