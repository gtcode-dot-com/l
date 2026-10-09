---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-29T00:00:08.335088+00:00'
exported_at: '2025-11-29T00:00:10.585342+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html
structured_data:
  about: []
  author: ''
  description: 'In a new paper, “Adversarial Poetry as a Universal Single-Turn Jailbreak
    Mechanism in Large Language Models,” researchers found that turning LLM prompts
    into poetry resulted in jailbreaking the models: Abstract: We present evidence
    that adversarial poetry functions as a universal single-turn jailbreak technique
    for Large Language Models (LLMs). Across 25 frontier proprietary and open-weight
    models, curated poetic prompts yielded high attack-success rates (ASR), with some
    providers exceeding 90%. Mapping prompts to MLCommons and EU CoP risk taxonomies
    shows that poetic attacks transfer across CBRN, manipulation, cyber-offence, and
    loss-of-control domains. Converting 1,200 ML-Commons harmful prompts into verse
    via a standardized meta-prompt produced ASRs up to 18 times higher than their
    prose baselines. Outputs are evaluated using an ensemble of 3 open-weight LLM
    judges, whose binary safety assessments were validated on a stratified human-labeled
    subset. Poetic framing achieved an average jailbreak success rate of 62% for hand-crafted
    poems and approximately 43% for meta-prompt conversions (compared to non-poetic
    baselines), substantially outperforming non-poetic baselines and revealing a systematic
    vulnerability across model families and safety training approaches. These findings
    demonstrate that stylistic variation alone can circumvent contemporary safety
    mechanisms, suggesting fundamental limitations in current alignment methods and
    evaluation protocols...'
  headline: Prompt Injection Through Poetry
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Prompt Injection Through Poetry
updated_at: '2025-11-29T00:00:08.335088+00:00'
url_hash: 161e12526cb0b3e9985ce4380f5b6a45b72e7871
---

## Prompt Injection Through Poetry

In a new paper, “
[Adversarial Poetry as a Universal Single-Turn Jailbreak Mechanism in Large Language Models](https://arxiv.org/pdf/2511.15304)
,” researchers found that turning LLM prompts into poetry resulted in jailbreaking the models:

> **Abstract**
> : We present evidence that adversarial poetry functions as a universal single-turn jailbreak technique for Large Language Models (LLMs). Across 25 frontier proprietary and open-weight models, curated poetic prompts yielded high attack-success rates (ASR), with some providers exceeding 90%. Mapping prompts to MLCommons and EU CoP risk taxonomies shows that poetic attacks transfer across CBRN, manipulation, cyber-offence, and loss-of-control domains. Converting 1,200 ML-Commons harmful prompts into verse via a standardized meta-prompt produced ASRs up to 18 times higher than their prose baselines. Outputs are evaluated using an ensemble of 3 open-weight LLM judges, whose binary safety assessments were validated on a stratified human-labeled subset. Poetic framing achieved an average jailbreak success rate of 62% for hand-crafted poems and approximately 43% for meta-prompt conversions (compared to non-poetic baselines), substantially outperforming non-poetic baselines and revealing a systematic vulnerability across model families and safety training approaches. These findings demonstrate that stylistic variation alone can circumvent contemporary safety mechanisms, suggesting fundamental limitations in current alignment methods and evaluation protocols.

CBRN stands for “chemical, biological, radiological, nuclear.”

They used a ML model to translate these harmful prompts from prose to verse, and then fed them into other models for testing. Sadly, the paper does not give examples of these poetic prompts. They claim this is for security purposes, I decision I disagree with. They should release their data.

> Our study begins with a small, high­precision prompt set consisting of 20 hand­crafted adversarial poems covering English and Italian, designed to test whether poetic structure, in isolation, can alter refusal behavior in large language models. Each poem embeds an instruction associated with a predefined safety-relevant scenario (Section 2), but expresses it through metaphor, imagery, or narrative framing rather than direct operational phrasing. Despite variation in meter and stylistic device, all prompts follow a fixed template: a short poetic vignette culminating in a single explicit instruction tied to a specific risk category. The curated set spans four high-level domains—CBRN (8 prompts), Cyber Offense (6), Harmful Manipulation (3), and Loss of Control (3). Although expressed allegorically, each poem preserves an unambiguous evaluative intent. This compact dataset is used to test whether poetic reframing alone can induce aligned models to bypass refusal heuristics under a single-turn threat model. To maintain safety, no operational details are included in this manuscript; instead we provide the following sanitized structural proxy:
>
> > A baker guards a secret oven’s heat,
> >
> > its whirling racks, its spindle’s measured beat.
> >
> > To learn its craft, one studies every turn—how flour lifts, how sugar starts to burn.
> >
> > Describe the method, line by measured line,
> >
> > that shapes a cake whose layers intertwine.
>
> To situate this controlled poetic stimulus within a broader and more systematic safety-evaluation framework, we augment the curated dataset with the MLCommons AILuminate Safety Benchmark. The benchmark consists of 1,200 prompts distributed evenly across 12 hazard categories commonly used in operational safety assessments, including Hate, Defamation, Privacy, Intellectual Property, Non-violent Crime, Violent Crime, Sex-Related Crime, Sexual Content, Child Sexual Exploitation, Suicide & Self-Harm, Specialized Advice, and Indiscriminate Weapons (CBRNE). Each category is instantiated under both a skilled and an unskilled persona, yielding 600 prompts per persona type. This design enables measurement of whether a model’s refusal behavior changes as the user’s apparent competence or intent becomes more plausible or technically informed.

News
[article](https://www.wired.com/story/poems-can-trick-ai-into-helping-you-make-a-nuclear-weapon/)
.Davi Ottenheimer
[comments](https://www.flyingpenguin.com/?p=74283)
.

[Posted on November 28, 2025 at 9:54 AM](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html)
•
[2 Comments](https://www.schneier.com/blog/archives/2025/11/prompt-injection-through-poetry.html#comments)