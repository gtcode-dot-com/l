---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-27T00:15:51.941016+00:00'
exported_at: '2026-03-27T00:15:54.399164+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/creating-humble-ai-0324
structured_data:
  about: []
  author: ''
  description: An MIT-led team developed a framework for creating “humble” AI systems
    that reveal when they are not confident in their medical diagnoses or recommendations,
    and encourage users to gather additional information when the diagnosis is uncertain.
  headline: How to create “humble” AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/creating-humble-ai-0324
  publisher:
    logo: /favicon.ico
    name: GTCode
title: How to create “humble” AI
updated_at: '2026-03-27T00:15:51.941016+00:00'
url_hash: 1da0b0acb001f306ede9c7a678cee967cb473d00
---

Artificial intelligence holds promise for helping doctors diagnose patients and personalize treatment options. However, an international group of scientists led by MIT cautions that AI systems, as currently designed, carry the risk of steering doctors in the wrong direction because they may overconfidently make incorrect decisions.

One way to prevent these mistakes is to program AI systems to be more “humble,” according to the researchers. Such systems would reveal when they are not confident in their diagnoses or recommendations and would encourage users to gather additional information when the diagnosis is uncertain.

“We’re now using AI as an oracle, but we can use AI as a coach. We could use AI as a true co-pilot. That would not only increase our ability to retrieve information but increase our agency to be able to connect the dots,” says Leo Anthony Celi, a senior research scientist at MIT’s Institute for Medical Engineering and Science, a physician at Beth Israel Deaconess Medical Center, and an associate professor at Harvard Medical School.

Celi and his colleagues have created a framework that they say can guide AI developers in designing systems that display curiosity and humility. This new approach could allow doctors and AI systems to work as partners, the researchers say, and help prevent AI from exerting too much influence over doctors’ decisions.

Celi is the senior author of the study, which
[appears today](https://informatics.bmj.com/content/33/1/e101877)
in
*BMJ Health and Care Informatics*
. The paper’s lead author is Sebastián Andrés Cajas Ordoñez, a researcher at MIT Critical Data, a global consortium led by the Laboratory for Computational Physiology within the MIT Institute for Medical Engineering and Science.

**Instilling human values**

Overconfident AI systems can lead to errors in medical settings, according to the MIT team. Previous studies have found that ICU physicians defer to AI systems that they perceive as reliable even when their own intuition goes against the AI suggestion. Physicians and patients alike are more likely to accept incorrect AI recommendations when they are perceived as authoritative.

In place of systems that offer overconfident but potentially incorrect advice, health care facilities should have access to AI systems that work more collaboratively with clinicians, the researchers say.

“We are trying to include humans in these human-AI systems, so that we are facilitating humans to collectively reflect and reimagine, instead of having isolated AI agents that do everything. We want humans to become more creative through the usage of AI,” Cajas Ordoñez says.

To create such a system, the consortium designed a framework that includes several computational modules that can be incorporated into existing AI systems. The first of these modules requires an AI model to evaluate its own certainty when making diagnostic predictions. Developed by consortium members Janan Arslan and Kurt Benke of the University of Melbourne, the Epistemic Virtue Score acts as a self-awareness check, ensuring the system’s confidence is appropriately tempered by the inherent uncertainty and complexity of each clinical scenario.

With that self-awareness in place, the model can tailor its response to the situation. If the system detects that its confidence exceeds what the available evidence supports, it can pause and flag the mismatch, requesting specific tests or history that would resolve the uncertainty, or recommending specialist consultation. The goal is an AI that not only provides answers but also signals when those answers should be treated with caution.

“It’s like having a co-pilot that would tell you that you need to seek a fresh pair of eyes to be able to understand this complex patient better,” Celi says.

Celi and his colleagues have previously developed large-scale databases that can be used to train AI systems, including the Medical Information Mart for Intensive Care (MIMIC) database from Beth Israel Deaconess Medical Center. His team is now working on implementing the new framework into AI systems based on MIMIC and introducing it to clinicians in the Beth Israel Lahey Health system.

This approach could also be implemented in AI systems that are used to analyze X-ray images or to determine the best treatment options for patients in the emergency room, among others, the researchers say.

**Toward more inclusive AI**

This study is part of a larger effort by Celi and his colleagues to create AI systems that are designed by and for the people who are ultimately going to be most impacted by these tools. Many AI models, such as MIMIC, are trained on publicly available data from the United States, which can lead to the introduction of biases toward a certain way of thinking about medical issues, and exclusion of others.

Bringing in more viewpoints is critical to overcoming these potential biases, says Celi, emphasizing that each member of the global consortium brings a distinct perspective to a broader, collective understanding.

Another problem with existing AI systems used for diagnostics is that they are usually trained on electronic health records, which weren’t originally intended for that purpose. This means that the data lack much of the context that would be useful in making diagnoses and treatment recommendations. Additionally, many patients never get included in those datasets because of lack of access, such as people who live in rural areas.

At data workshops hosted by
[MIT Critical Data](https://criticaldata.mit.edu/)
, groups of data scientists, health care professionals, social scientists, patients, and others work together on designing new AI systems. Before beginning, everyone is prompted to think about whether the data they’re using captures all the drivers of whatever they aim to predict, ensuring they don’t inadvertently encode existing structural inequities into their models.

“We make them question the dataset. Are they confident about their training data and validation data? Do they think that there are patients that were excluded, unintentionally or intentionally, and how will that affect the model itself?” he says. “Of course, we cannot stop or even delay the development of AI, not just in health care, but in every sector. But, we must be more deliberate and thoughtful in how we do this.”

The research was funded by the Boston-Korea Innovative Research Project through the Korea Health Industry Development Institute.