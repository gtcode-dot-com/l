---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-01-06T12:15:28.750803+00:00'
exported_at: '2026-01-06T12:15:31.981758+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/mit-scientists-investigate-memorization-risk-clinical-ai-0105
structured_data:
  about: []
  author: ''
  description: MIT Jameel Clinic scientists have designed a series of tests to ensure
    that foundation models trained on electronic health records don&#039;t leak sensitive
    patient information when prompted by a bad actor.
  headline: MIT scientists investigate memorization risk in the age of clinical AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/mit-scientists-investigate-memorization-risk-clinical-ai-0105
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: MIT scientists investigate memorization risk in the age of clinical AI
updated_at: '2026-01-06T12:15:28.750803+00:00'
url_hash: a2a49e695c0a63052c772d449d22bcaa6cd0c994
---

What is patient privacy for? The Hippocratic Oath, thought to be one of the earliest and most widely known medical ethics texts in the world, reads: “Whatever I see or hear in the lives of my patients, whether in connection with my professional practice or not, which ought not to be spoken of outside, I will keep secret, as considering all such things to be private.”

As privacy becomes increasingly scarce in the age of data-hungry algorithms and cyberattacks, medicine is one of the few remaining domains where confidentiality remains central to practice, enabling patients to trust their physicians with sensitive information.

But
[a paper](https://neurips.cc/virtual/2025/loc/san-diego/poster/118370)
co-authored by MIT researchers investigates how artificial intelligence models trained on de-identified electronic health records (EHRs) can memorize patient-specific information. The work, which was recently presented at the 2025 Conference on Neural Information Processing Systems (NeurIPS), recommends a rigorous testing setup to ensure targeted prompts cannot reveal information, emphasizing that leakage must be evaluated in a health care context to determine whether it meaningfully compromises patient privacy.

Foundation models trained on EHRs should normally generalize knowledge to make better predictions, drawing upon many patient records. But in “memorization,” the model draws upon a singular patient record to deliver its output, potentially violating patient privacy. Notably, foundation models are already known to be
[prone to data leakage](https://icml.cc/virtual/2025/workshop/39996)
.

“Knowledge in these high-capacity models can be a resource for many communities, but adversarial attackers can prompt a model to extract information on training data,” says Sana Tonekaboni, a postdoc at the Eric and Wendy Schmidt Center at the Broad Institute of MIT and Harvard and first author of the paper. Given the risk that foundation models could also memorize private data, she notes, “this work is a step towards ensuring there are practical evaluation steps our community can take before releasing models.”

To conduct research on the potential risk EHR foundation models could pose in medicine, Tonekaboni approached MIT Associate Professor
[Marzyeh Ghassemi](https://jclinic.mit.edu/team-member/marzyeh-ghassemi/)
, who is a principal investigator at the
[Abdul Latif Jameel Clinic for Machine Learning in Health](https://jclinic.mit.edu/)
(Jameel Clinic), a member of the Computer Science and Artificial Intelligence Lab. Ghassemi, a faculty member in the MIT Department of Electrical Engineering and Computer Science and Institute for Medical Engineering and Science, runs the
[Healthy ML group](https://healthyml.org/)
, which focuses on robust machine learning in health.

Just how much information does a bad actor need to expose sensitive data, and what are the risks associated with the leaked information? To assess this, the research team developed a series of tests that they hope will lay the groundwork for future privacy evaluations. These tests are designed to measure various types of uncertainty, and assess their practical risk to patients by measuring various tiers of attack possibility.

“We really tried to emphasize practicality here; if an attacker has to know the date and value of a dozen laboratory tests from your record in order to extract information, there is very little risk of harm. If I already have access to that level of protected source data, why would I need to attack a large foundation model for more?” says Ghassemi.

With the inevitable digitization of medical records, data breaches have become more commonplace. In the past 24 months, the U.S. Department of Health and Human Services has recorded
[747 data breaches](https://ocrportal.hhs.gov/ocr/breach/breach_report.jsf)
of health information affecting more than 500 individuals, with the majority categorized as hacking/IT incidents.

Patients with unique conditions are especially vulnerable, given how easy it is to pick them out. “Even with de-identified data, it depends on what sort of information you leak about the individual,” Tonekaboni says. “Once you identify them, you know a lot more.”

In their structured tests, the researchers found that the more information the attacker has about a particular patient, the more likely the model is to leak information. They demonstrated how to distinguish model generalization cases from patient-level memorization, to properly assess privacy risk.

The paper also emphasized that some leaks are more harmful than others. For instance, a model revealing a patient’s age or demographics could be characterized as a more benign leakage than the model revealing more sensitive information, like an HIV diagnosis or alcohol abuse.

The researchers note that patients with unique conditions are especially vulnerable given how easy it is to pick them out, which may require higher levels of protection. “Even with de-identified data, it really depends on what sort of information you leak about the individual,” Tonekaboni says. The researchers plan to expand the work to become more interdisciplinary, adding clinicians and privacy experts as well as legal experts.

“There’s a reason our health data is private,” Tonekaboni says. “There’s no reason for others to know about it.”

This work supported by the Eric and Wendy Schmidt Center at the Broad Institute of MIT and Harvard, Wallenberg AI, the Knut and Alice Wallenberg Foundation, the U.S. National Science Foundation (NSF), a Gordon and Betty Moore Foundation award, a Google Research Scholar award, and the AI2050 Program at Schmidt Sciences. Resources used in preparing this research were provided, in part, by the Province of Ontario, the Government of Canada through CIFAR, and companies sponsoring the Vector Institute.