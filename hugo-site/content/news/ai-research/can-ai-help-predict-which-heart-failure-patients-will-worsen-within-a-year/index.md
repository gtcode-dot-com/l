---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-13T00:15:38.942597+00:00'
exported_at: '2026-03-13T00:15:41.183222+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/can-ai-help-predict-which-heart-failure-patients-will-worsen-0312
structured_data:
  about: []
  author: ''
  description: A new deep learning model can predict a patient&#039;s heart failure
    trajectory up to a year in advance. The work was developed by researchers at MIT,
    Mass General Brigham, and Harvard Medical School.
  headline: Can AI help predict which heart-failure patients will worsen within a
    year?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/can-ai-help-predict-which-heart-failure-patients-will-worsen-0312
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Can AI help predict which heart-failure patients will worsen within a year?
updated_at: '2026-03-13T00:15:38.942597+00:00'
url_hash: 0520db8b21c3a8b1de19661cf89889d21fee83fc
---

Characterized by weakened or damaged heart musculature, heart failure results in the gradual buildup of fluid in a patient’s lungs, legs, feet, and other parts of the body. The condition is chronic and incurable, often leading to arrhythmias or sudden cardiac arrest. For many centuries, bloodletting and leeches were the treatment of choice, famously practiced by barber surgeons in Europe, during a time when physicians rarely operated on patients.

In the 21st century, the management of heart failure has become decidedly less medieval: Today, patients undergo a combination of healthy lifestyle changes, prescription of medications, and sometimes use pacemakers. Yet heart failure remains one of the leading causes of morbidity and mortality, placing a substantial burden on health-care systems across the globe.

“About half of the people diagnosed with heart failure will die within five years of diagnosis,” says Teya Bergamaschi, an MIT PhD student in the lab of Nina T. and Robert H. Rubin Professor
[Collin Stultz](https://jclinic.mit.edu/team-member/collin-stultz/)
and the co-first author of a new paper introducing a deep learning model for predicting heart failure. “Understanding how a patient will fare after hospitalization is really important in allocating finite resources.”

The paper,
[published in
*Lancet eClinical Medicine*](https://www.sciencedirect.com/science/article/pii/S2589537026000301?via%3Dihub)
by a team of researchers at MIT, Mass General Brigham, and Harvard Medical School, shares results from developing and testing PULSE-HF, which stands loosely for “Predict changes in left ventricULar Systolic function from ECGs of patients who have Heart Failure.” The project was conducted in Stultz’s lab, which is affiliated with the
[MIT Abdul Latif Jameel Clinic for Machine Learning in Health](https://jclinic.mit.edu/)
. Developed and retrospectively tested across three different patient cohorts from Massachusetts General Hospital, Brigham and Women’s Hospital, and MIMIC-IV (a publicly available dataset), the deep learning model accurately predicts changes in the left ventricular ejection fraction (LVEF), which is the percentage of blood being pumped out of the left ventricle of the heart.

A healthy human heart pumps out about 50 to 70 percent of blood from the left ventricle with each beat — anything less is considered a sign of a potential problem. “The model takes an [electrocardiogram] and outputs a prediction of whether or not there will be an ejection fraction within the next year that falls below 40 percent,” says Tiffany Yau, an MIT PhD student in Stultz’s lab who is also co-first author of the PULSE-HF paper. “That is the most severe subgroup of heart failure.”

If PULSE-HF predicts that a patient’s ejection fraction is likely to worsen within a year, the clinician can prioritize the patient for follow-up. Subsequently, lower-risk patients can reduce their number of hospital visits and the amount of time spent getting 10 electrodes adhered to their body for a 12-lead ECG. The model can also be deployed in low-resource clinical settings, including doctors offices in rural areas that don’t typically have a cardiac sonographer employed to run ultrasounds on a daily basis.

“The biggest thing that distinguishes [PULSE-HF] from other heart failure ECG methods is instead of detection, it does forecasting,” says Yau. The paper notes that to date, no other methods exist for predicting future LVEF decline among patients with heart failure.

During the testing and validation process, the researchers used a metric known as "area under the receiver operating characteristic curve" (AUROC) to measure PULSE-HF’s performance. AUROC is typically used to measure a model’s ability to discriminate between classes on a scale from 0 to 1, with 0.5 being random and 1 being perfect. PULSE-HF achieved AUROCs ranging from 0.87 to 0.91 across all three patient cohorts.

Notably, the researchers also built a version of PULSE-HF for single-lead ECGs, meaning only one electrode needs to be placed on the body. While 12-lead ECGs are generally considered superior for being more comprehensive and accurate, the performance of the single-lead version of PULSE-HF was just as strong as the 12-lead version.

Despite the elegant simplicity behind the idea of PULSE-HF, like most clinical AI research, it belies a laborious execution. “It’s taken years [to complete this project],” Bergamaschi recalls. “It’s gone through many iterations.”

One of the team’s biggest challenges was collecting, processing, and cleaning the ECG and echocardiogram datasets. While the model aims to forecast a patient’s ejection fraction, the labels for the training data weren’t always readily available. Much like a student learning from a textbook with an answer key, labeling is critical for helping machine-learning models correctly identify patterns in data.

Clean, linear text in the form of TXT files typically works best when training models. But echocardiogram files typically come in the form of PDFs, and when PDFs are converted to TXT files, the text (which gets broken up by line breaks and formatting) becomes difficult for the model to read. The unpredictable nature of real-life scenarios, like a restless patient or a loose lead, also marred the data. “There are a lot of signal artifacts that need to be cleaned,” Bergamaschi says. “It’s kind of a never-ending rabbit hole.”

While Bergamaschi and Yau acknowledge that more complicated methods could help filter the data for better signals, there is a limit to the usefulness of these approaches. “At what point do you stop?” Yau asks. “You have to think about the use case — is it easiest to have this model that works on data that is slightly messy? Because it probably will be.”

The researchers anticipate that the next step for PULSE-HF will be testing the model in a prospective study on real patients, whose future ejection fraction is unknown.

Despite the challenges inherent to bringing clinical AI tools like PULSE-HF over the finish line, including the possible risk of prolonging a PhD by another year, the students feel that the years of hard work were worthwhile.

“I think things are rewarding partially because they’re challenging,” Bergamaschi says. “A friend said to me, ‘If you think you will find your calling after graduation, if your calling is truly calling, it will be there in the one additional year it takes you to graduate.’ … The way we’re measured as researchers in [the ML and health] space is different from other researchers in ML space. Everyone in this community understands the unique challenges that exist here.”

“There’s too much suffering in the world,” says Yau, who joined Stultz’s lab after a health event made her realize the importance of machine learning in health care. “Anything that tries to ease suffering is something that I would consider a valuable use of my time.”