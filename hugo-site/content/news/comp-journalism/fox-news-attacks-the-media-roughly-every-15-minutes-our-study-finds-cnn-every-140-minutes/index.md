---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2026-10-09T01:35:42.030025+00:00'
exported_at: '2026-10-09T01:35:45.491481+00:00'
feed: http://feeds.feedburner.com/NiemanJournalismLab
language: en
source_url: https://www.niemanlab.org/2026/10/fox-news-attacks-the-media-roughly-every-15-minutes-our-study-finds-cnn-every-140-minutes
structured_data:
  about: []
  author: ''
  description: '"Disparaging journalism is a far more central part of Fox News programming
    than it is of either MSNBC or CNN programming."'
  headline: Fox News attacks the media roughly every 15 minutes, our study finds.
    (CNN? Every 140 minutes.)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.niemanlab.org/2026/10/fox-news-attacks-the-media-roughly-every-15-minutes-our-study-finds-cnn-every-140-minutes
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fox News attacks the media roughly every 15 minutes, our study finds. (CNN?
  Every 140 minutes.)
updated_at: '2026-10-09T01:35:42.030025+00:00'
url_hash: dceae994b7a13c5f7fc9835eafd448fc612ce2a5
---

In 2025, trust in journalism reached a
[record low](https://news.gallup.com/poll/695762/trust-media-new-low.aspx)
. According to
[Gallup,](https://news.gallup.com/poll/695762/trust-media-new-low.aspx)
only 8% of Republicans expressed trust in the news media, compared with 51% of Democrats. New data show an
[uptick](https://news.gallup.com/poll/714938/trust-news-media-edges-slightly-higher.aspx)
among Republicans, but overall trust remains near this record low, and the gap between Republicans and Democrats remains substantial.

One of the key drivers of this lopsided decline in trust in journalism may be the extent to which news outlets spend time bashing other news outlets, or bashing the news media in general — a phenomenon we call
*inter-journalism disparagement*
. Our research team at Duke University’s
[DeWitt Wallace Center for Media &amp; Democracy](https://dewitt.sanford.duke.edu/)
recently completed a study of the prominence of this phenomenon on each of the “big three” cable news networks (CNN, Fox News, MSNBC/MS NOW); whether it has increased or decreased over time; and whether there are significant differences in the rate of disparagement across networks.

The results were stark. Fox News far exceeds the other networks, with inter-journalism disparagement taking place once every 14.5 minutes. In contrast, CNN engages in inter-journalism disparagement roughly every 140 minutes, and MSNBC every 61 minutes.

To conduct this analysis, we gathered 15 years of cable news transcripts (2011-2025) for each network. We gathered a random sample of one week’s worth of programming for each year.
With this approach, we ended up with 3,543 transcripts and almost 19 million words across the three networks, which equates to roughly 62,000 pages of text.

Given the volume of text to be analyzed, we trained OpenAI’s
[GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)
to identify attacks against the news media. We developed a 20-page instruction document to help the model code instances of disparagement. GPT-5.5 consistently achieved 99.5% accuracy at identifying inter-journalism disparagement and 100% accuracy for avoiding false negatives, compared to human-coded samples. (You can read more details about the entire training and analytical process
[here](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7525940)
.)

We defined inter-journalism disparagement as negative statements about the conduct or content of an explicitly identified journalism target (such as a specific news organization, or the news media in general). Our definition, which is described in greater depth in the
[full paper,](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7525940)
needed to be quite detailed in order for ChatGPT to produce accurate results. Examples of inter-journalism disparagement include:

* CNN’s Dan Pfeiffer describing “political journalism writ large” as “bad,” “problematic” and “failing massively.”
* MSNBC’s Rachel Maddow describing The Washington Post’s editorial page as “rabid” and “foaming,” and “super right-wing,” noting: “I can’t believe this is in this real newspaper.”
* Fox News’ Mark Levin telling viewers that “MSNBC and CNN…have been lying and lying and lying to you for years.”

What we found when comparing the three networks tells us a lot about the dynamics of contemporary cable news and partisan journalism.

First, Figure 1 shows the rate of journalism disparagement across each of the big three networks. Because the volume of text that we analyzed varies across each network, our primary metric was the rate of disparagement per 1,000 words of transcript text. In this figure, we show not only the rate per 1,000 words, but we also convert that rate into a time-based frequency, using the industry standard of 1,000 words equaling approximately six minutes of air time.

![](https://www.niemanlab.org/images/1_overall_rate.jpg)

In Figure 2, we graph the frequency of inter-journalism disparagement over time. Here, we see that the massive difference between Fox News and CNN/MSNBC persists over the 15-year time period. Still, we do see some dips in the volume of disparagement on Fox News in the two-year periods leading up to the 2016 and 2024 elections, with journalism disparagement levels on Fox News rebounding to near-peak levels in 2025. We haven’t figured out yet what to make of this pattern.

![](https://www.niemanlab.org/images/2_rate_by_year.jpg)

CNN and MSNBC seem to converge in their disparagement activity starting around 2017, with MSNBC’s disparagement rate decreasing somewhat, and CNN’s disparagement rate increasing somewhat. This pattern aligns with recent
[research](https://doi.org/10.1073/pnas.2202197119)
that has shown, in other contexts, that CNN and MSNBC programming are converging in ways that suggest diminished differences between the more “centrist” CNN and the more left-leaning MSNBC.

A key takeaway here is that we should not think about Fox News and MSNBC as flip sides of the same partisan journalism coin. At least in relation to inter-journalism disparagement, these left- and right-leaning cable networks behave very differently. Disparaging journalism is a far more central part of Fox News programming than it is of either MSNBC or CNN programming.

In order to get a deeper understanding of these differences, we also identified the targets of the disparagement. These results are presented in Figures 3 through 5.

![](https://www.niemanlab.org/images/3_targets_chart_a.jpg)

Figure 3 presents a breakdown of the most common targets of disparagement on Fox News. By far the most frequent target of disparagement on Fox News is “the media.” Following in a distant second is CNN, with the “mainstream media” rounding out the top three targets. Other relatively frequent targets include The New York Times, MSNBC, and The Washington Post.

As should be clear, Fox News devotes far more attention to disparaging journalism as an institution than it does to attacking individual news sources. This stands in stark contrast to what we see when we look at the results for CNN and MSNBC. Looking first at CNN, Figure 4 shows that the network’s most frequent target is Fox News (though with a frequency that wouldn’t crack the top three of the Fox News list).

![](https://www.niemanlab.org/images/4_targets_chart_b.jpg)

Similarly, as Figure 5 shows, Fox News is also the number one target on MSNBC. Both CNN and MSNBC have the same top three, with Fox News followed by “the media” and the “right-wing media.” These instances of institutional disparagement happen far less frequently on CNN or MSNBC than they do on Fox News.

![](https://www.niemanlab.org/images/5_targets_chart_c.jpg)

Finally, we were also able to identify which hosts or anchors were the most frequent disparagers of their fellow journalists. Those results can be seen in Figure 6. Given the lopsided amount of inter-journalism disparagement on Fox News, it is not surprising that this graph is dominated by Fox News personalities, with Sean Hannity taking the top spot, followed by Greg Gutfeld and Tucker Carlson (note: our graph for Howard Kurtz reflects his move from CNN to Fox in 2013).

![](https://www.niemanlab.org/images/6_top_individuals.jpg)

This study didn’t distinguish further in terms of the nature of the disparagement across the three networks (for example, in terms of severity or legitimacy). This is something we are exploring in the next stage of this work. Nor did we examine whether viewer exposure to inter-journalism disparagement reduces trust in specific outlets or the institution of journalism. That certainly seems like a reasonable assumption, given the dramatically lower levels of trust in journalism among Republicans that we noted at the outset. We plan to investigate this relationship directly in future research.

But what we do see in this research is that disparagement of the institution of journalism, and of particular news outlets, is a much more prominent component of Fox News programming than it is of either CNN or MSNBC. Some
[researchers](https://ijoc.org/index.php/ijoc/article/view/24536)
have proposed that this kind of high-volume disparagement of news sources that don’t tow the same partisan line takes us beyond traditional notions of partisan journalism and into the realm of “anti-media media.” The goal of anti-media media is to “weaponize the facade of journalism against the roles assigned to journalism” in a democracy. Based on our findings, Fox News fits this characterization.

[Philip M. Napoli](https://sanford.duke.edu/profile/philip-michael-napoli/)
is the James R. Shepley Professor of Public Policy, director of the DeWitt Wallace Center for Media &amp; Democracy, and director of undergraduate studies for the journalism and media minor in the Sanford School of Public Policy at Duke University.
[Adam Meskouri](https://www.linkedin.com/in/adam-meskouri-2b2923196/)
is a politics researcher at Harvard and Duke.
[Anjini Mani](https://www.linkedin.com/in/anjinimani/)
is an undergraduate at Duke.
[Grant Socol](https://www.linkedin.com/in/grant-socol-a15766192/)
is a graduate research assistant at Duke.
[Harrison Walley](https://www.linkedin.com/in/harrison-walley/)
is an undergraduate at Duke.