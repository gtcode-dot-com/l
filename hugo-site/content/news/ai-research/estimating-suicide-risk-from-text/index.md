---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-10-06T21:50:47.646744+00:00'
exported_at: '2026-10-06T21:50:49.230479+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/estimating-suicide-risk-from-text-0924
structured_data:
  about: []
  author: ''
  description: A new language processing tool from MIT&#039;s McGovern Institute could
    help identify individuals at risk for suicide from natural language in texts,
    enabling swifter interventions.
  headline: Estimating suicide risk from text
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/estimating-suicide-risk-from-text-0924
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Estimating suicide risk from text
updated_at: '2026-10-06T21:50:47.646744+00:00'
url_hash: 2d3921d846c7373924569d0dedfad707818f433c
---

When people reach out during a mental health crisis, a top priority for counselors is identifying those with a high risk of suicide. The distressed person’s language holds critical clues, and a new tool developed by scientists at MIT’s McGovern Institute for Brain Research is designed to pick up on and rapidly evaluate those signals.

The language-processing tool was developed by Daniel Low, a former graduate student in Senior Research Scientist
[Satra Ghosh](https://mcgovern.mit.edu/profile/satrajit-ghosh/)
’s
[Senseable Intelligence Group](https://sensein.group/)
who is now a research scientist at the
[Child Mind Institute](https://childmind.org/ "https://childmind.org/")
, where he leads its
[AI, Risk, and Contemplative Science Lab](https://childmind.org/science/advancing-methods/dair/arc-lab/ "https://childmind.org/science/advancing-methods/dair/arc-lab/")
, as well as a visiting scholar at Harvard University. It uses a custom-built list of words and phrases linked to 49 suicide risk factors, searching text for these and using them to estimate an individual’s risk.

Ghosh, Low, and colleagues
[report today in the
*Journal of Psychopathology and Clinical Scienc*
e](https://psycnet.apa.org/fulltext/2028-28243-001.html)
that their tool accurately predicts suicide risk from text conversations with crisis counselors. It is already helping to clarify which suicide risk factors matter most in times of crisis. With more validation, it could help with risk assessment in clinical settings and crisis-support situations.

**Identifying key risk factors**

Suicide attempts are notoriously difficult to predict. Dozens of risk factors have been linked to suicide, and even trained clinicians struggle to identify who will make an attempt among those who have some form of suicidal ideation. Among the factors that can make suicidal thoughts and behaviors more likely are certain psychiatric symptoms and disorders, like depression, borderline personality disorder, and post-traumatic stress disorder, as well as environmental and social stressors, like poverty, incarceration, discrimination, and loneliness.

“You see all these 50 risk factors, and they're all interacting in ways we don't really understand,” Low says. “Many different pathways could lead to someone feeling they want to escape their internal pain,” he says — and it’s challenging to know whose path will lead to a suicide attempt or death.

Ghosh and Low wanted to understand which risk factors counselors and clinicians should most look out for during a mental health crisis. To do that, they collaborated with the Crisis Text Line, whose trained volunteers provide confidential text-based support to people in distress.

Crisis Text Line, a global mental health nonprofit that provides free, 24/7, confidential mental health support for people in need, provided specialized training and controlled access to this restricted dataset. The researchers analyzed de-identified texts from approximately 16,000 conversations with Crisis Text Line’s volunteer crisis counselors. Based on Crisis Text Line’s assessments, those conversations were grouped into three different risk levels: non-suicidal, suicidal ideation without imminent risk, and imminent risk. It was this imminent risk group — those with a plan for suicide, or who have an intent to die within the next 48 hours — that the researchers most wanted to understand.

“We wanted to know what type of symptoms predict the highest suicide risk,” Low says. This question has been studied before, he says — but typically through epidemiological surveys that ask a person to recall their symptoms and experiences, often after their mental health crisis has passed. In contrast, he says, “Crisis Text Line gives us an opportunity to assess many different symptoms and potential risk factors as people are having the crises.”

**Reading between the lines**

Before analyzing the crisis line texts, the research team built a suicide-risk lexicon. They turned to artificial intelligence to generate a preliminary list of words and phrases tied to established suicide risk factors, including factors associated with suicidal ideation, suicide attempt, and suicide death. Then they manually reviewed and curated that list. Their final lexicon includes about 60 words or phrases for each of 49 risk factors, with the relevance of each one confirmed by expert clinicians.

Then they trained a machine learning model to search the crisis conversations for words and phrases in their lexicon and use these to predict suicide risk. Because the lexicon links each word or phrase to a specific risk factor, they could use these data to determine which risk factors are most closely tied to imminent risk among people in crisis.

What they found was consistent with patterns found in previous research, although not always intuitive. For example, depression is a well-known risk factor for suicidal ideation, but their model found that mentions of lethal means and substance use were more likely to be expressed by the highest-risk group than depressed mood or fatigue. Expressions of active suicidal ideation and self-injury were also strong predictors. Intermediate predictors included anxiety, post-traumatic stress disorder, and emotional pain.

The predictive model assigns a weight to each risk factor based on its contribution to risk. For example, mentions of lethal means for suicide, like “cut” or “pills,” are weighed heavily, whereas terms related to hopelessness, like “don’t know what to do” or “hopeless,” contribute to a lesser degree. After training their model, the team found they could use it to accurately predict risk severity in new conversations the model had not previously seen.

One limitation of lexicons, the researchers note, is that they do not consider the context of terms, and they can miss terms that are similar to those in the lexicon, but not explicitly included. Large language models have reasoning abilities, and Low and colleagues have developed ways of using large language models to detect suicide risk in other projects. However, they say they often use their lexicon in parallel to guarantee flagging certain terms, as well as to maintain data privacy.

Low stresses that while the team used the power of a large language model to develop its lexicon, its prediction model is a simpler, “lightweight” model. Unlike large language models, which require massive computational power, it can be run easily on a personal computer, reducing both cost and privacy concerns. Just as importantly, it is interpretable: Rather than merely generating a risk estimate like some deep learning models can do more effectively, it tells users how it got there. Words of concern can be flagged so users understand the basis for each assessment and act on that information. They are working on similar explainability approaches with large language models.

That’s critical, because the stakes are so high. “This is such a complex space that having a human in the loop is, I think, going to be critical for a long, long time,” says Ghosh, who is the director of the Open Data in Neuroscience Initiative at the McGovern Institute. Likewise, the researchers add that any predictive model must be thoroughly validated before clinical use, and might need to be continually refined to keep up with changes in language use or target populations.

Because a reliable lexicon opens doors to new ways of understanding mental health, Ghosh and Low are widely sharing not just their suicide risk lexicon, but also the software package they developed to build it. Researchers can use that tool to efficiently build lexicons for other mental health conditions. Meanwhile, Low says, the suicide risk lexicon is already being used to explore how text data from a variety of sources, from social media to electronic health records, might help researchers and clinicians better estimate risk.