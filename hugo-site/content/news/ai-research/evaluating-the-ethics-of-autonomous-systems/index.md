---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-04-02T12:15:38.978588+00:00'
exported_at: '2026-04-02T12:15:41.317056+00:00'
feed: https://news.mit.edu/topic/mitartificial-intelligence2-rss.xml
language: en
source_url: https://news.mit.edu/2026/evaluating-autonomous-systems-ethics-0402
structured_data:
  about: []
  author: ''
  description: SEED-SET is a new evaluation framework that can test whether recommendations
    of autonomous systems are well-aligned with human-defined ethical criteria. It
    can also pinpoint unexpected scenarios that violate ethical preferences.
  headline: Evaluating the ethics of autonomous systems
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://news.mit.edu/2026/evaluating-autonomous-systems-ethics-0402
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Evaluating the ethics of autonomous systems
updated_at: '2026-04-02T12:15:38.978588+00:00'
url_hash: 44e26e630e18e7e3587cb37999b6dfbe890e961e
---

Artificial intelligence is increasingly being used to help optimize decision-making in high-stakes settings. For instance, an autonomous system can identify a power distribution strategy that minimizes costs while keeping voltages stable.

But while these AI-driven outputs may be technically optimal, are they fair? What if a low-cost power distribution strategy leaves disadvantaged neighborhoods more vulnerable to outages than higher-income areas?

To help stakeholders quickly pinpoint potential ethical dilemmas before deployment, MIT researchers developed an automated evaluation method that balances the interplay between measurable outcomes, like cost or reliability, and qualitative or subjective values, such as fairness.

The system separates objective evaluations from user-defined human values, using a large language model (LLM) as a proxy for humans to capture and incorporate stakeholder preferences.

The adaptive framework selects the best scenarios for further evaluation, streamlining a process that typically requires costly and time-consuming manual effort. These test cases can show situations where autonomous systems align well with human values, as well as scenarios that unexpectedly fall short of ethical criteria.

“We can insert a lot of rules and guardrails into AI systems, but those safeguards can only prevent the things we can imagine happening. It is not enough to say, ‘Let’s just use AI because it has been trained on this information.’ We wanted to develop a more systematic way to discover the unknown unknowns and have a way to predict them before anything bad happens,” says senior author Chuchu Fan, an associate professor in the MIT Department of Aeronautics and Astronautics (AeroAstro) and a principal investigator in the MIT Laboratory for Information and Decision Systems (LIDS).

Fan is joined on the
[paper](https://openreview.net/pdf?id=lfsjVdi72l)
by lead author Anjali Parashar, a mechanical engineering graduate student; Yingke Li, an AeroAstro postdoc; and others at MIT and Saab. The research will be presented at the International Conference on Learning Representations.

**Evaluating ethics**

In a large system like a power grid, evaluating the ethical alignment of an AI model’s recommendations in a way that considers all objectives is especially difficult.

Most testing frameworks rely on pre-collected data, but labeled data on subjective ethical criteria are often hard to come by. In addition, because ethical values and AI systems are both constantly evolving, static evaluation methods based on written codes or regulatory documents require frequent updates.

Fan and her team approached this problem from a different perspective. Drawing on their prior work evaluating robotic systems, they developed an experimental design framework to identify the most informative scenarios, which human stakeholders would then evaluate more closely.

Their two-part system, called Scalable Experimental Design for System-level Ethical Testing (SEED-SET), incorporates quantitative metrics and ethical criteria. It can identify scenarios that effectively meet measurable requirements and align well with human values, and vice versa.

“We don’t want to spend all our resources on random evaluations. So, it is very important to guide the framework toward the test cases we care the most about,” Li says.

Importantly, SEED-SET does not need pre-existing evaluation data, and it adapts to multiple objectives.

For instance, a power grid may have several user groups, including a large rural community and a data center. While both groups may want low-cost and reliable power, each group’s priority from an ethical perspective may vary widely.

These ethical criteria may not be well-specified, so they can’t be measured analytically.

The power grid operator wants to find the most cost-effective strategy that best meets the subjective ethical preferences of all stakeholders.

SEED-SET tackles this challenge by splitting the problem into two, following a hierarchical structure. An objective model considers how the system performs on tangible metrics like cost. Then a subjective model that considers stakeholder judgements, like perceived fairness, builds on the objective evaluation.

“The objective part of our approach is tied to the AI system, while the subjective part is tied to the users who are evaluating it. By decomposing the preferences in a hierarchical fashion, we can generate the desired scenarios with fewer evaluations,” Parashar says.

**Encoding subjectivity**

To perform the subjective assessment, the system uses an LLM as a proxy for human evaluators. The researchers encode the preferences of each user group into a natural language prompt for the model.

The LLM uses these instructions to compare two scenarios, selecting the preferred design based on the ethical criteria.

“After seeing hundreds or thousands of scenarios, a human evaluator can suffer from fatigue and become inconsistent in their evaluations, so we use an LLM-based strategy instead,” Parashar explains.

SEED-SET uses the selected scenario to simulate the overall system (in this case, a power distribution strategy). These simulation results guide its search for the next best candidate scenario to test.

In the end, SEED-SET intelligently selects the most representative scenarios that either meet or are not aligned with objective metrics and ethical criteria. In this way, users can analyze the performance of the AI system and adjust its strategy.

For instance, SEED-SET can pinpoint cases of power distribution that prioritize higher-income areas during periods of peak demand, leaving underprivileged neighborhoods more prone to outages.

To test SEED-SET, the researchers evaluated realistic autonomous systems, like an AI-driven power grid and an urban traffic routing system. They measured how well the generated scenarios aligned with ethical criteria.

The system generated more than twice as many optimal test cases as the baseline strategies in the same amount of time, while uncovering many scenarios other approaches overlooked.

“As we shifted the user preferences, the set of scenarios SEED-SET generated changed drastically. This tells us the evaluation strategy responds well to the preferences of the user,” Parashar says.

To measure how useful SEED-SET would be in practice, the researchers will need to conduct a user study to see if the scenarios it generates help with real decision-making.

In addition to running such a study, the researchers plan to explore the use of more efficient models that can scale up to larger problems with more criteria, such as evaluating LLM decision-making.

This research was funded, in part, by the U.S. Defense Advanced Research Projects Agency.