---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-13T18:15:21.044183+00:00'
exported_at: '2026-04-13T18:15:23.236711+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html
structured_data:
  about: []
  author: ''
  description: The cybersecurity industry is obsessing over Anthropic’s new model,
    Claude Mythos Preview, and its effects on cybersecurity. Anthropic said that it
    is not releasing it to the general public because of its cyberattack capabilities,
    and has launched Project Glasswing to run the model against a whole slew of public
    dom...
  headline: On Anthropic’s Mythos Preview and Project Glasswing
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: On Anthropic’s Mythos Preview and Project Glasswing
updated_at: '2026-04-13T18:15:21.044183+00:00'
url_hash: 445c023feec65ceb1d73aad1efc52d818d20290e
---

## On Anthropic’s Mythos Preview and Project Glasswing

The cybersecurity industry is obsessing over Anthropic’s new model, Claude Mythos Preview, and its effects on cybersecurity. Anthropic said that it is
[not releasing it](https://red.anthropic.com/2026/mythos-preview/)
to the general public because of its cyberattack capabilities, and has launched
[Project Glasswing](https://www.anthropic.com/glasswing)
to run the model against a whole slew of public domain and proprietary software, with the aim of finding and patching all the vulnerabilities before hackers get their hands on the model and exploit them.

There’s a lot here, and I hope to write something more considered in the coming week, but I want to make some quick observations.

One: This is very much a PR play by Anthropic—and it worked. Lots of reporters are
[breathlessly](https://www.nytimes.com/2026/04/07/opinion/anthropic-ai-claude-mythos.html)
[repeating](https://www.axios.com/2026/04/08/anthropic-mythos-model-ai-cyberattack-warning)
Anthropic’s
[talking](https://www.nytimes.com/2026/04/07/technology/anthropic-claims-its-new-ai-model-mythos-is-a-cybersecurity-reckoning.html)
[points](https://www.understandingai.org/p/why-anthropic-believes-its-latest)
, without engaging with them critically. OpenAI, presumably pissed that Anthropic’s new model has gotten so much positive press and wanting to grab some of the spotlight for itself, announced its model is
[just as scary](https://www.msn.com/en-us/technology/artificial-intelligence/scoop-openai-plans-staggered-rollout-of-new-model-over-cybersecurity-risk/ar-AA20usvp)
, and won’t be released to the general public, either.

Two: These models do demonstrate an increased sophistication in their cyberattack capabilities. They write effective exploits—taking the vulnerabilities they find and operationalizing them—without human involvement. They can find more complex vulnerabilities: chaining together several memory corruption bugs, for example. And they can do more with one-shot prompting, without requiring orchestration and agent configuration infrastructure.

Three: Anthropic might have a good PR team, but the problem isn’t with Mythos Preview. The security company Aisle was able to
[replicate](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)
the vulnerabilities that Anthropic found, using older, cheaper, public models. But there is a difference between finding a vulnerability and turning it into an attack. This points to a current advantage to the defender. Finding for the purposes of fixing is easier for an AI than finding plus exploiting. This advantage is likely to shrink, as ever more powerful models become available to the general public.

Four: Everyone who is panicking about the ramifications of this is correct about the problem, even if we can’t predict the exact timeline. Maybe the sea change just happened, with the new models from Anthropic and OpenAI. Maybe it happened six months ago. Maybe it’ll happen in six months. It will happen—I have no doubt about it—and sooner than we are ready for. We can’t predict how much more these models will improve in general, but software seems to be a specialized language that is optimal for AIs.

A couple of weeks ago, I
[wrote about](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html)
security in what I called “the age of instant software,” where AIs are superhumanly good at finding, exploiting, and patching vulnerabilities. I stand by everything I wrote there. The urgency is now greater than ever.

I was also part of a large team that wrote a “
[what to do now](https://labs.cloudsecurityalliance.org/mythos-ciso/)
” report. The guidance is largely correct: We need to prepare for a world where zero-day exploits are dime-a-dozen, and lots of attackers suddenly have offensive capabilities that far outstrip their skills.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)
,
[cybersecurity](https://www.schneier.com/tag/cybersecurity/)
,
[exploits](https://www.schneier.com/tag/exploits/)
,
[vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on April 13, 2026 at 12:52 PM](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html)
•
[1 Comments](https://www.schneier.com/blog/archives/2026/04/on-anthropics-mythos-preview-and-project-glasswing.html#comments)