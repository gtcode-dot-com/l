---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-11-12T22:51:26.339588+00:00'
exported_at: '2025-11-12T22:54:41.541946+00:00'
feed: http://feeds.feedburner.com/blogspot/gJZg
language: en
source_url: http://blog.research.google/2024/03/computer-aided-diagnosis-for-lung.html
structured_data:
  about: []
  author: ''
  description: Computer-aided diagnosis for lung cancer screening
  headline: Computer-aided diagnosis for lung cancer screening
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: http://blog.research.google/2024/03/computer-aided-diagnosis-for-lung.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Computer-aided diagnosis for lung cancer screening
updated_at: '2025-11-12T22:51:26.339588+00:00'
url_hash: 9b5b9c06475f0bd46ee8ef87dfc51548987d84b5
---

Lung cancer is the leading cause of cancer-related deaths globally with
[1.8 million deaths](https://www.who.int/news-room/fact-sheets/detail/cancer#:~:text=The%20most%20common%20causes%20of,rectum%20(916%20000%20deaths)%3B)
reported in 2020. Late diagnosis dramatically reduces the chances of survival.
[Lung cancer screening](https://www.cdc.gov/cancer/lung/basic_info/screening.htm)
via
[computed tomography](https://www.cancer.gov/about-cancer/diagnosis-staging/ct-scans-fact-sheet#:~:text=indicate%20real%20problems.-,Lung%20cancer,-Low%2Ddose%20CT)
(CT), which provides a detailed 3D image of the lungs, has been shown to reduce mortality in high-risk populations by at least 20% by detecting potential signs of cancers earlier. In the US, screening involves annual scans, with some countries or cases recommending more or less frequent scans.

The
[United States Preventive Services Task Force](https://www.uspreventiveservicestaskforce.org/uspstf/recommendation/lung-cancer-screening)
recently expanded lung cancer screening recommendations by
[roughly 80%](https://pubmed.ncbi.nlm.nih.gov/34636916/)
, which is expected to increase screening access for women and racial and ethnic minority groups. However, false positives (i.e., incorrectly reporting a potential cancer in a cancer-free patient) can cause anxiety and lead to unnecessary procedures for patients while increasing costs for the healthcare system. Moreover, efficiency in screening a large number of individuals can be challenging depending on healthcare infrastructure and radiologist availability.

At Google we have previously developed
[machine learning (ML) models for lung cancer detection](https://blog.google/technology/health/lung-cancer-prediction/)
, and have evaluated their ability to automatically detect and classify regions that show signs of potential cancer. Performance has been shown to be comparable to that of specialists in detecting possible cancer. While they have achieved high performance, effectively communicating findings in realistic environments is necessary to realize their full potential.

To that end, in “
[Assistive AI in Lung Cancer Screening: A Retrospective Multinational Study in the US and Japan](https://pubs.rsna.org/doi/10.1148/ryai.230079)
”, published in
[*Radiology AI*](https://pubs.rsna.org/journal/ai)
, we investigate how ML models can effectively communicate findings to radiologists. We also introduce a generalizable user-centric interface to help radiologists leverage such models for lung cancer screening. The system takes CT imaging as input and outputs a cancer suspicion rating using four categories (no suspicion, probably benign, suspicious, highly suspicious) along with the corresponding regions of interest. We evaluate the system’s utility in improving clinician performance through randomized reader studies in both the US and Japan, using the local cancer scoring systems (
[Lung-RADSs V1.1](https://www.acr.org/-/media/ACR/Files/RADS/Lung-RADS/LungRADSAssessmentCategoriesv1-1.pdf)
and
[Sendai Score](https://www.jscts.org/pdf/guideline/gls3rdfig_english130621.pdf)
) and image viewers that mimic realistic settings. We found that reader specificity increases with model assistance in both reader studies. To accelerate progress in conducting similar studies with ML models, we have
[open-sourced code](https://github.com/Google-Health/google-health/tree/master/ct_dicom)
to process CT images and generate images compatible with the
[picture archiving and communication system](https://en.wikipedia.org/wiki/Picture_archiving_and_communication_system)
(PACS) used by radiologists.

## Developing an interface to communicate model results

Integrating ML models into radiologist workflows involves understanding the nuances and goals of their tasks to meaningfully support them. In the case of lung cancer screening, hospitals follow various country-specific guidelines that are regularly updated. For example, in the US, Lung-RADs V1.1 assigns an
[alpha-numeric score](https://www.acr.org/-/media/ACR/Files/RADS/Lung-RADS/LungRADSAssessmentCategoriesv1-1.pdf)
to indicate the lung cancer risk and follow-up recommendations
*.*
When assessing patients, radiologists load the CT in their workstation to read the case, find lung nodules or lesions, and apply set guidelines to determine follow-up decisions.

Our first step was to improve the
[previously developed ML models](https://blog.google/technology/health/lung-cancer-prediction/)
through additional training data and architectural improvements, including
[self-attention](https://research.google/pubs/attention-is-all-you-need/)
. Then, instead of targeting specific guidelines, we experimented with a complementary way of communicating AI results independent of guidelines or their particular versions. Specifically, the system output offers a suspicion rating and localization (regions of interest) for the user to consider in conjunction with their own specific guidelines. The interface produces output images directly associated with the CT study, requiring no changes to the user’s workstation. The radiologist only needs to review a small set of additional images. There is no other change to their system or interaction with the system.

The assistive lung cancer screening system comprises 13 models and has a high-level architecture similar to the end-to-end system used in
[**prior work**](https://blog.google/technology/health/lung-cancer-prediction/)
. The models coordinate with each other to first segment the lungs, obtain an overall assessment, locate three suspicious regions, then use the information to assign a suspicion rating to each region. The system was deployed on Google Cloud using a
[**Google Kubernetes Engine**](https://cloud.google.com/kubernetes-engine)
(GKE) that pulled the images, ran the ML models, and provided results. This allows scalability and directly connects to servers where the images are stored in
[**DICOM stores**](https://cloud.google.com/healthcare-api/docs/concepts/dicom)
.

## Reader studies

To evaluate the system’s utility in improving clinical performance, we conducted two reader studies (i.e., experiments designed to assess clinical performance comparing expert performance with and without the aid of a technology) with 12 radiologists using pre-existing, de-identified CT scans. We presented 627 challenging cases to 6 US-based and 6 Japan-based radiologists. In the experimental setup, readers were divided into two groups that read each case twice, with and without assistance from the model. Readers were asked to apply scoring guidelines they typically use in their clinical practice and report their overall suspicion of cancer for each case. We then compared the results of the reader’s responses to measure the impact of the model on their workflow and decisions. The score and suspicion level were judged against the actual cancer outcomes of the individuals to measure sensitivity, specificity, and
[area under the ROC curve](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc#:~:text=AUC%20stands%20for%20%22Area%20under,across%20all%20possible%20classification%20thresholds.)
(AUC) values. These were compared with and without assistance.

The ability to conduct these studies using the same interface highlights its generalizability to completely different cancer scoring systems, and the generalization of the model and assistive capability to different patient populations. Our study results demonstrated that when radiologists used the system in their clinical evaluation, they had an increased ability to correctly identify lung images without actionable lung cancer findings (i.e.,
*specificity*
) by an absolute 5–7% compared to when they didn’t use the assistive system. This potentially means that for every 15–20 patients screened, one may be able to avoid unnecessary follow-up procedures, thus reducing their anxiety and the burden on the health care system. This can, in turn, help improve the sustainability of lung cancer screening programs, particularly as
[more people become eligible for screening](https://pubmed.ncbi.nlm.nih.gov/34636916/)
.

## Translating this into real-world impact through partnership

The system results demonstrate the potential for fewer follow-up visits, reduced anxiety, as well lower overall costs for lung cancer screening. In an effort to translate this research into real-world clinical impact, we are working with:
[DeepHealth](https://deephealth.com/)
, a leading AI-powered health informatics provider; and
[Apollo Radiology International](https://apolloradiologyintl.com/)
a leading provider of Radiology services in India to explore paths for incorporating this system into future products. In addition, we are looking to help other researchers studying how best to integrate ML model results into clinical workflows by
[open sourcing code](https://github.com/Google-Health/google-health/tree/master/ct_dicom)
used for the reader study and incorporating the insights described in this blog. We hope that this will help accelerate medical imaging researchers looking to conduct reader studies for their AI models, and catalyze translational research in the field.

## Acknowledgements

*Key contributors to this project include Corbin Cunningham, Zaid Nabulsi, Ryan Najafi‎, Jie Yang, Charles Lau, Joseph R. Ledsam, Wenxing Ye, Diego Ardila, Scott M. McKinney, Rory Pilgrim, Hiroaki Saito, Yasuteru Shimamura, Mozziyar Etemadi, Yun Liu, David Melnick, Sunny Jansen, Nadia Harhen, David P. Nadich, Mikhail Fomitchev, Ziyad Helali, Shabir Adeel, Greg S. Corrado, Lily Peng, Daniel Tse, Shravya Shetty, Shruthi Prabhakara, Neeral Beladia, and Krish Eswaran. Thanks to Arnav Agharwal and Andrew Sellergren for their open sourcing support and Vivek Natarajan and Michael D. Howell for their feedback. Sincere appreciation also goes to the radiologists who enabled this work with their image interpretation and annotation efforts throughout the study, and Jonny Wong and Carli Sampson for coordinating the reader studies.*