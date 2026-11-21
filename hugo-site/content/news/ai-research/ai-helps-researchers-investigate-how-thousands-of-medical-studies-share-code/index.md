---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-11-21T00:31:43.762563+00:00'
exported_at: '2026-11-21T00:31:46.089019+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/ai-helps-researchers-investigate-how-medical-studies-share-code-1119
structured_data:
  about: []
  author: ''
  description: Researchers using AI to examine nearly 4,000 studies and hundreds of
    code repositories found gaps in the information needed to scrutinize and reuse
    published studies, reducing the effectiveness of sharing prediction research.
  headline: AI helps researchers investigate how thousands of medical studies share
    code
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/ai-helps-researchers-investigate-how-medical-studies-share-code-1119
  publisher:
    logo: /favicon.ico
    name: GTCode
title: AI helps researchers investigate how thousands of medical studies share code
updated_at: '2026-11-21T00:31:43.762563+00:00'
url_hash: 4665289b81f88c7a2d1bf4b04c0072e02c837cfb
---

An MIT and Dana-Farber Institute-led team used large language models to examine nearly 4,000 studies and hundreds of code repositories, revealing gaps in the information needed to scrutinize and reuse published research.

The data and code that underpin a research study can tell us what was actually done, and how. In a medical study, for example, how were patients selected for inclusion? How were missing values handled? How were the results evaluated?

Access to a study's data and code help researchers to answer these questions, to examine the methods, and to build on the work.

“Studies involve many choices about how to prepare data, develop models, and evaluate performance. These are sometimes called ‘researcher degrees of freedom,’” says Tom Pollard, a research scientist at MIT's Laboratory for Computational Physiology and Computer Science and Artificial Intelligence Laboratory. “The choices we make affect the results, and a methods section in a paper can only capture so much detail.”

While sharing code can be a first step, in order for code to be understood and reused, it must be sufficiently structured and described. The problem is that, right now, there is little guidance for researchers on what constitutes a well-organized, well-described collection of code.

This is where an international team led by researchers at MIT and Dana-Farber Cancer Institute sought to help, by examining how code is currently shared in clinical prediction studies. Such studies develop or evaluate models to estimate patient outcomes, such as the risk of developing a disease. Because these models inform decisions about patient care, researchers need to be able to scrutinize how they were built and tested.

Using large language models (LLMs), the researchers examined nearly 4,000 papers to identify statements about shared code. They then followed the statements to assess hundreds of associated code repositories.

Their review revealed two key gaps: Code sharing remains uncommon, and making code public does not consistently mean providing the documentation and supporting information needed for reuse. The open-access findings, recently
[published in
*Nature Medicine*](https://www.nature.com/articles/s41591-026-04691-1)
, are informing
[TRIPOD-Code](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888484/)
, a reporting guideline being developed to clarify what researchers should share.

**Following the code**

TRIPOD-Code builds on TRIPOD and TRIPOD+AI, checklists that help researchers report how clinical prediction models were developed and evaluated. To understand current code-sharing practices, the team identified studies citing either guideline. The review included almost 4,000 studies that developed, updated, or validated prediction models, and whose full texts were available through PubMed Central’s open-access collection.

“The challenge was that the information was highly inconsistent. First, we had to identify whether or not a paper shared code” says Thomas Sounack, the study’s first author. He adds that authors “discuss and link to code from a paper in many different ways.”

The team used an LLM to help screen papers, identify statements about code availability, and extract links. Software then retrieved the linked repositories — online collections of code and related files — for further assessment.

The workflow went beyond checking whether a link existed. It also assessed repositories against characteristics such as completeness of documentation, software requirements, and terms of reuse.

“The real benefit of LLMs is their ability to process unstructured information such as text. These models helped us work with information that was scattered across papers and software repositories, rather than neatly organized in a table,” says Pollard, who is a senior author of the study. “That allowed us to examine how code was being shared in much more detail across a large collection of studies.”

Human reviewers evaluated the work of the LLMs. Two researchers independently checked 500 papers and a separate sample of repositories, resolving disagreements before comparing their assessments with the automated results.

Agreement was stronger for concrete characteristics, such as whether a license file was present, than for judgments about the adequacy of documentation. Because classification errors remain possible, the authors emphasize the overall patterns rather than treating every count as exact.

**Inconsistent code sharing**

Only about 1 in 8 studies reported sharing code. Where code was shared, the contents of repositories varied widely.

Some repositories were “extremely well-organized and -documented, while others gave almost no guidance at all,” Sounack says. Good code sharing, he explains, means “giving enough information to understand what the code does and be able to run it to reproduce the results reported in the paper.”

Practices also varied substantially across journals and countries. Among journals, the proportion of studies sharing code ranged from zero to more than 70 percent. Some journals with low sharing rates nevertheless had written code-sharing policies, suggesting that policies alone may not be enough to motivate code sharing.

The review also helped to identify examples of effective practice. Some researchers, for example, provided synthetic datasets to assist with code reuse where the original patient records could not be shared publicly.

**Setting a standard for code sharing**

Researchers who share code are already making an effort to make their work transparent. But clinical prediction research brings together people from medicine, statistics, and computer science, whose expectations for documenting and sharing code may differ.

TRIPOD-Code aims to establish a consensus. Through an expert review process, the team is developing guidance on which elements of shared analytical code should be considered essential.

“We want to give researchers practical guidance on how to share code, and give journals clearer expectations to communicate to authors,” Pollard says. “The review gives us evidence to inform those discussions."