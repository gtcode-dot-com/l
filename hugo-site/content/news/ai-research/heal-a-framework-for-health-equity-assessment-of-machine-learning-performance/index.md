---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-02-13T06:41:27.141031+00:00'
exported_at: '2026-02-13T06:41:31.732672+00:00'
feed: http://feeds.feedburner.com/blogspot/gJZg
language: en
source_url: http://blog.research.google/2024/03/heal-framework-for-health-equity.html
structured_data:
  about: []
  author: ''
  description: 'HEAL: A framework for health equity assessment of machine learning
    performance'
  headline: 'HEAL: A framework for health equity assessment of machine learning performance'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://blog.research.google/2024/03/heal-framework-for-health-equity.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'HEAL: A framework for health equity assessment of machine learning performance'
updated_at: '2026-02-13T06:41:27.141031+00:00'
url_hash: 1cd1772b195af5f43a7ae8b74aa363c1f1e7c0b4
---

Health equity is a major societal concern worldwide with disparities having many causes. These sources include limitations in access to healthcare, differences in clinical treatment, and even fundamental differences in the diagnostic technology. In dermatology for example, skin cancer outcomes are worse for populations such as minorities, those with lower socioeconomic status, or individuals with limited healthcare access. While there is great promise in recent advances in machine learning (ML) and artificial intelligence (AI) to help improve healthcare, this transition from research to bedside must be accompanied by a careful understanding of whether and how they impact health equity.

*Health equity*
is defined by public health organizations as fairness of opportunity for everyone to be as healthy as possible. Importantly, equity may be different from
*equality*
. For example, people with greater barriers to improving their health may require more or different effort to experience this fair opportunity. Similarly, equity is not
*fairness*
as defined in the AI for healthcare literature. Whereas AI fairness often strives for equal performance of the AI technology across different patient populations, this does not center the goal of prioritizing performance with respect to pre-existing health disparities.

In “
[Health Equity Assessment of machine Learning performance (HEAL): a framework and dermatology AI model case study](https://www.thelancet.com/journals/eclinm/article/PIIS2589-5370(24)00058-0/fulltext)
”, published in
[*The Lancet eClinicalMedicine*](https://www.thelancet.com/journals/eclinm/home)
, we propose a methodology to quantitatively assess whether ML-based health technologies perform equitably. In other words, does the ML model perform well for those with the worst health outcomes for the condition(s) the model is meant to address? This goal anchors on the principle that health equity should prioritize and measure model performance with respect to disparate health outcomes, which may be due to a number of factors that include structural inequities (e.g., demographic, social, cultural, political, economic, environmental and geographic).

## The health equity framework (HEAL)

The HEAL framework proposes a 4-step process to estimate the likelihood that an ML-based health technology performs equitably:

(1) Identify factors associated with health inequities and define tool performance metrics,

(2) Identify and quantify pre-existing health disparities,

(3) Measure the performance of the tool for each subpopulation,

(4) Measure the likelihood that the tool prioritizes performance with respect to health disparities.

The final step’s output is termed the HEAL metric, which quantifies how anticorrelated the ML model’s performance is with health disparities. In other words, does the model perform better with populations that have the worse health outcomes?

This 4-step process is designed to inform improvements for making ML model performance more equitable, and is meant to be iterative and re-evaluated on a regular basis. For example, the availability of health outcomes data in step (2) can inform the choice of demographic factors and brackets in step (1), and the framework can be applied again with new datasets, models and populations.

With this work, we take a step towards encouraging explicit assessment of the health equity considerations of AI technologies, and encourage prioritization of efforts during model development to reduce health inequities for subpopulations exposed to structural inequities that can precipitate disparate outcomes. We should note that the present framework does not model causal relationships and, therefore, cannot quantify the actual impact a new technology will have on reducing health outcome disparities. However, the HEAL metric may help identify opportunities for improvement, where the current performance is not prioritized with respect to pre-existing health disparities.

## Case study on a dermatology model

As an illustrative case study, we applied the framework to a dermatology model, which utilizes a convolutional neural network similar to that described in
[prior work](https://blog.research.google/2019/09/using-deep-learning-to-inform.html)
. This example dermatology model was trained to classify 288 skin conditions using a development dataset of 29k cases. The input to the model consists of three photos of a skin concern along with demographic information and a brief structured medical history. The output consists of a ranked list of possible matching skin conditions.

Using the HEAL framework, we evaluated this model by assessing whether it prioritized performance with respect to pre-existing health outcomes. The model was designed to predict possible dermatologic conditions (from a list of hundreds) based on photos of a skin concern and patient metadata. Evaluation of the model is done using a top-3 agreement metric, which quantifies how often the top 3 output conditions match the most likely condition as suggested by a dermatologist panel. The HEAL metric is computed via the anticorrelation of this top-3 agreement with health outcome rankings.

We used a dataset of 5,420 teledermatology cases, enriched for diversity in age, sex and race/ethnicity, to retrospectively evaluate the model’s HEAL metric. The dataset consisted of “store-and-forward” cases from patients of 20 years or older from primary care providers in the USA and skin cancer clinics in Australia. Based on a review of the literature, we decided to explore race/ethnicity, sex and age as potential factors of inequity, and used sampling techniques to ensure that our evaluation dataset had sufficient representation of all race/ethnicity, sex and age groups. To quantify pre-existing health outcomes for each subgroup we relied on measurements from
[public](https://www.who.int/data/gho/data/themes/mortality-and-global-health-estimates/global-health-estimates-leading-causes-of-dalys)
[databases](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(20)30925-9/fulltext)
endorsed by the World Health Organization, such as
[Years of Life Lost](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/4427)
(YLLs) and
[Disability-Adjusted Life Years](https://www.who.int/data/gho/indicator-metadata-registry/imr-details/158)
(DALYs; years of life lost plus years lived with disability).

Our analysis estimated that the model was 80.5% likely to perform equitably across race/ethnicity subgroups and 92.1% likely to perform equitably across sexes.

However, while the model was likely to perform equitably across age groups for cancer conditions specifically, we discovered that it had room for improvement across age groups for non-cancer conditions. For example, those 70+ have the poorest health outcomes related to non-cancer skin conditions, yet the model didn't prioritize performance for this subgroup.

## Putting things in context

For holistic evaluation, the HEAL metric cannot be employed in isolation. Instead this metric should be contextualized alongside many other factors ranging from computational efficiency and data privacy to ethical values, and aspects that may influence the results (e.g., selection bias or differences in representativeness of the evaluation data across demographic groups).

As an adversarial example, the HEAL metric can be artificially improved by deliberately reducing model performance for the most advantaged subpopulation until performance for that subpopulation is worse than all others. For illustrative purposes, given subpopulations A and B where A has worse health outcomes than B, consider the choice between two models: Model 1 (M1) performs 5% better for subpopulation A than for subpopulation B. Model 2 (M2) performs 5% worse on subpopulation A than B. The HEAL metric would be higher for M1 because it prioritizes performance on a subpopulation with worse outcomes. However, M1 may have absolute performances of just 75% and 70% for subpopulations A and B respectively, while M2 has absolute performances of 75% and 80% for subpopulations A and B respectively. Choosing M1 over M2 would lead to worse overall performance for all subpopulations because some subpopulations are worse-off while no subpopulation is better-off.

Accordingly, the HEAL metric should be used alongside a
[Pareto condition](https://en.wikipedia.org/wiki/Pareto_efficiency)
(discussed further in the paper), which restricts model changes so that outcomes for each subpopulation are either unchanged or improved compared to the status quo, and performance does not worsen for any subpopulation.

The HEAL framework, in its current form, assesses the likelihood that an ML-based model prioritizes performance for subpopulations with respect to pre-existing health disparities for specific subpopulations. This differs from the goal of understanding whether ML will reduce disparities in outcomes across subpopulations in reality. Specifically, modeling improvements in outcomes requires a causal understanding of steps in the care journey that happen both before and after use of any given model. Future research is needed to address this gap.

## Conclusion

The HEAL framework enables a quantitative assessment of the likelihood that health AI technologies prioritize performance with respect to health disparities. The case study demonstrates how to apply the framework in the dermatological domain, indicating a high likelihood that model performance is prioritized with respect to health disparities across sex and race/ethnicity, but also revealing the potential for improvements for non-cancer conditions across age. The case study also illustrates limitations in the ability to apply all recommended aspects of the framework (e.g., mapping societal context, availability of data), thus highlighting the complexity of health equity considerations of ML-based tools.

This work is a proposed approach to address a grand challenge for AI and health equity, and may provide a useful evaluation framework not only during model development, but during pre-implementation and real-world monitoring stages, e.g., in the form of health equity dashboards. We hold that the strength of the HEAL framework is in its future application to various AI tools and use cases and its refinement in the process. Finally, we acknowledge that a successful approach towards understanding the impact of AI technologies on health equity needs to be more than a set of metrics. It will require a set of goals agreed upon by a community that represents those who will be most impacted by a model.

## Acknowledgements

*The research described here is joint work across many teams at Google. We are grateful to all our co-authors: Terry Spitz, Malcolm Pyles, Heather Cole-Lewis, Ellery Wulczyn, Stephen R. Pfohl, Donald Martin, Jr., Ronnachai Jaroensri, Geoff Keeling, Yuan Liu, Stephanie Farquhar, Qinghan Xue, Jenna Lester, Cían Hughes, Patricia Strachan, Fraser Tan, Peggy Bui, Craig H. Mermel, Lily H. Peng, Yossi Matias, Greg S. Corrado, Dale R. Webster, Sunny Virmani, Christopher Semturs, Yun Liu, and Po-Hsuan Cameron Chen. We also thank Lauren Winer, Sami Lachgar, Ting-An Lin, Aaron Loh, Morgan Du, Jenny Rizk, Renee Wong, Ashley Carrick, Preeti Singh, Annisah Um'rani, Jessica Schrouff, Alexander Brown, and Anna Iurchenko for their support of this project.*