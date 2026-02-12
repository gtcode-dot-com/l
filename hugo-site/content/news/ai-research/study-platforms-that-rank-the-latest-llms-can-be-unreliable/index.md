---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-12T22:15:43.078838+00:00'
exported_at: '2026-02-12T22:15:46.109997+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/study-platforms-rank-latest-llms-can-be-unreliable-0209
structured_data:
  about: []
  author: ''
  description: The results of popular LLM ranking platforms can be skewed by just
    a few data points, possibly providing an unreliable report about which LLM would
    perform best in real situations, according MIT researchers who also developed
    a way to test the rankings and identify these influential data points.
  headline: 'Study: Platforms that rank the latest LLMs can be unreliable'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/study-platforms-rank-latest-llms-can-be-unreliable-0209
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Study: Platforms that rank the latest LLMs can be unreliable'
updated_at: '2026-02-12T22:15:43.078838+00:00'
url_hash: 4884855d45250cc8ff42603526e3da06c62417a4
---

A firm that wants to use a large language model (LLM) to summarize sales reports or triage customer inquiries can choose between hundreds of unique LLMs with dozens of model variations, each with slightly different performance.

To narrow down the choice, companies often rely on LLM ranking platforms, which gather user feedback on model interactions to rank the latest LLMs based on how they perform on certain tasks.

But MIT researchers found that a handful of user interactions can skew the results, leading someone to mistakenly believe one LLM is the ideal choice for a particular use case. Their study reveals that removing a tiny fraction of crowdsourced data can change which models are top-ranked.

They developed a fast method to test ranking platforms and determine whether they are susceptible to this problem. The evaluation technique identifies the individual votes most responsible for skewing the results so users can inspect these influential votes.

The researchers say this work underscores the need for more rigorous strategies to evaluate model rankings. While they didn’t focus on mitigation in this study, they provide suggestions that may improve the robustness of these platforms, such as gathering more detailed feedback to create the rankings.

The study also offers a word of warning to users who may rely on rankings when making decisions about LLMs that could have far-reaching and costly impacts on a business or organization.

“We were surprised that these ranking platforms were so sensitive to this problem. If it turns out the top-ranked LLM depends on only two or three pieces of user feedback out of tens of thousands, then one can’t assume the top-ranked LLM is going to be consistently outperforming all the other LLMs when it is deployed,” says Tamara Broderick, an associate professor in MIT’s Department of Electrical Engineering and Computer Science (EECS); a member of the Laboratory for Information and Decision Systems (LIDS) and the Institute for Data, Systems, and Society; an affiliate of the Computer Science and Artificial Intelligence Laboratory (CSAIL); and senior author of this study.

She is joined on the
[paper](https://arxiv.org/pdf/2508.11847)
by lead authors and EECS graduate students Jenny Huang and Yunyi Shen as well as Dennis Wei, a senior research scientist at IBM Research. The study will be presented at the International Conference on Learning Representations.

**Dropping data**

While there are many types of LLM ranking platforms, the most popular variations ask users to submit a query to two models and pick which LLM provides the better response.

The platforms aggregate the results of these matchups to produce rankings that show which LLM performed best on certain tasks, such as coding or visual understanding.

By choosing a top-performing LLM, a user likely expects that model’s top ranking to generalize, meaning it should outperform other models on their similar, but not identical, application with a set of new data.

The MIT researchers previously studied generalization in areas like statistics and economics. That work revealed certain cases where dropping a small percentage of data can change a model’s results, indicating that those studies’ conclusions might not hold beyond their narrow setting.

The researchers wanted to see if the same analysis could be applied to LLM ranking platforms.

“At the end of the day, a user wants to know whether they are choosing the best LLM. If only a few prompts are driving this ranking, that suggests the ranking might not be the end-all-be-all,” Broderick says.

But it would be impossible to test the data-dropping phenomenon manually. For instance, one ranking they evaluated had more than 57,000 votes. Testing a data drop of 0.1 percent means removing each subset of 57 votes out of the 57,000, (there are more than 10
194
subsets), and then recalculating the ranking.

Instead, the researchers developed an efficient approximation method, based on their prior work, and adapted it to fit LLM ranking systems.

“While we have theory to prove the approximation works under certain assumptions, the user doesn’t need to trust that. Our method tells the user the problematic data points at the end, so they can just drop those data points, re-run the analysis, and check to see if they get a change in the rankings,” she says.

**Surprisingly sensitive**

When the researchers applied their technique to popular ranking platforms, they were surprised to see how few data points they needed to drop to cause significant changes in the top LLMs. In one instance, removing just two votes out of more than 57,000, which is 0.0035 percent, changed which model is top-ranked.

A different ranking platform, which uses expert annotators and higher quality prompts, was more robust. Here, removing 83 out of 2,575 evaluations (about 3 percent) flipped the top models.

Their examination revealed that many influential votes may have been a result of user error. In some cases, it appeared there was a clear answer as to which LLM performed better, but the user chose the other model instead, Broderick says.

“We can never know what was in the user’s mind at that time, but maybe they mis-clicked or weren’t paying attention, or they honestly didn’t know which one was better. The big takeaway here is that you don’t want noise, user error, or some outlier determining which is the top-ranked LLM,” she adds.

The researchers suggest that gathering additional feedback from users, such as confidence levels in each vote, would provide richer information that could help mitigate this problem. Ranking platforms could also use human mediators to assess crowdsourced responses.

For the researchers’ part, they want to continue exploring generalization in other contexts while also developing better approximation methods that can capture more examples of non-robustness.

“Broderick and her students’ work shows how you can get valid estimates of the influence of specific data on downstream processes, despite the intractability of exhaustive calculations given the size of modern machine-learning models and datasets,” says Jessica Hullman, the Ginni Rometty Professor of Computer Science at Northwestern University, who was not involved with this work.  “The recent work provides a glimpse into the strong data dependencies in routinely applied — but also very fragile — methods for aggregating human preferences and using them to update a model. Seeing how few preferences could really change the behavior of a fine-tuned model could inspire more thoughtful methods for collecting these data.”

This research is funded, in part, by the Office of Naval Research, the MIT-IBM Watson AI Lab, the National Science Foundation, Amazon, and a CSAIL seed award.