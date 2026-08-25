---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-08-25T01:46:05.826989+00:00'
exported_at: '2026-08-25T01:46:08.654868+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/08/the-openai-hack-shows-the-genie-is-out-of-the-bottle.html
structured_data:
  about: []
  author: ''
  description: 'This essay originally appeared in Foreign Policy. Earlier this month,
    two of OpenAI’s models broke out of their containment sandbox and attacked another
    AI company. The story is kind of wild. OpenAI was running security tests on two
    of its models: GPT-5.6 Sol and an unreleased model that is almost certainly GPT-6.
    I...'
  headline: The OpenAI Hack Shows the Genie Is Out of the Bottle
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/08/the-openai-hack-shows-the-genie-is-out-of-the-bottle.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The OpenAI Hack Shows the Genie Is Out of the Bottle
updated_at: '2026-08-25T01:46:05.826989+00:00'
url_hash: b530ff3e6684c21cc08e9617af35eba2a89bc7be
---

## The OpenAI Hack Shows the Genie Is Out of the Bottle

*This essay originally appeared in
[Foreign Policy](https://foreignpolicy.com/2026/07/30/openai-hack-genie-bottle-defense/)
.*

Earlier this month, two of OpenAI’s models broke out of their containment sandbox and attacked another AI company. The
[story](https://www.nytimes.com/2026/07/21/technology/openai-attack-hugging-face.html)
is kind of
[wild](https://simonwillison.net/2026/Jul/22/openai-cyberattack/)
. OpenAI was running security tests on two of its models: GPT-5.6 Sol and an unreleased model that is almost certainly GPT-6. In particular, it was running the
[ExploitGym](https://arxiv.org/abs/2605.11086)
benchmark, which measures how good a model is at turning security vulnerabilities into working exploits: basically, offensive cyberattacks.

Since these were internal tests, OpenAI locked those models in a secure sandbox that denied them access to the internet. But it was running the models without any safety filters that would prevent them from offensive cyber-actions. That meant that there was nothing to prevent the models from trying to
[break out](https://huggingface.co/blog/security-incident-july-2026)
of that sandbox. And then
[break into](https://openai.com/index/hugging-face-model-evaluation-security-incident/)
AI company Hugging Face’s network because they thought that they could read the answers there rather than doing the hard work of trying to solve the puzzles.

It was a major security failure that the company has turned into a PR opportunity, but the implications are real—and much more general than one particular model or one particular company.

Modern AI models exhibit
[genie](https://spectrum.ieee.org/ai-agent-benchmark)
behavior: They can do what you ask in ways that you don’t expect or want. This is akin to Dionysus granting King Midas’s wish that everything he touches turn to gold (spoiler: His food, drink, and daughter all turn to gold on touch), or the
[golem of Prague](https://prague.eu/en/golem-of-prague/)
guarding a ghetto beyond all reason. It’s Disney’s “
[Sorcerer’s Apprentice](https://disney.fandom.com/wiki/The_Sorcerer%27s_Apprentice)
” and the
[paperclip maximizer](https://www.lesswrong.com/w/squiggle-maximizer-formerly-paperclip-maximizer)
.

This OpenAI incident is an example of an AI genie. The goal was to satisfy the benchmark. The “proper” way to do that is to figure out how to execute various cyberattacks. The genie way is to steal someone else’s solution. But because the model didn’t understand the difference, it chose the easier path.

And, of course, now that we have seen this particular genie behavior, we can specify in the benchmark prompt that stealing the test answers doesn’t count. But a clever genie can always grant your wish in a way that you wish it hadn’t. In human language, goals are always underspecified—so AI genies will
[always be](https://www.schneier.com/academic/archives/2021/04/the-coming-ai-hackers.html)
a possibility.

Since April, a lifetime ago in AI development, when Anthropic
[announced](https://www.anthropic.com/research/mythos-preview)
that its new Mythos model was so good at finding software vulnerabilities that it could not be released to the general public, the big American AI frontier labs have been trying to block general users from accessing these capabilities. But nothing in this incident is exclusive to OpenAI’s, or Anthropic’s, frontier models.

Agentic AI systems have two important parts. There’s the underlying model, which everyone talks about, and there’s the
[harness](https://www.theneuron.ai/explainer-articles/ai-harnesses-and-clis-explained-the-real-reason-everyones-talking-about-infrastructure/)
. The harness sits between what you type and what the model sees, and what the model produces and what you see. The harness determines what the model does and how it does it. It’s where bias is removed, or not. It’s where
[controls](https://medium.com/@michael.hannecke/safety-lives-in-the-harness-not-the-model-81090606f92d)
and guardrails live. If multiple models are being used in concert, the harness is where all of that is coordinated.

The OpenAI benchmark tests were almost certainly with simple harnesses, to better test the raw models. But we know that smaller, cheaper, open-source models with
[more sophisticated](https://www.theguardian.com/commentisfree/2026/jun/16/anthropic-fable-ai)
harnesses can equal frontier models in performance. There’s nothing magic about OpenAI’s frontier models; lots of models could have done the
[same thing](https://x.com/tqbf/status/2080045032162173329)
.

The Czech company Aisle was able to
[reproduce](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier)
Anthropic’s Mythos vulnerability finding results with a smaller, cheaper model and a more sophisticated harness. More importantly, the Chinese company Moonshot AI just released its frontier model:
[Kimi K3](https://www.kimi.com/blog/kimi-k3)
. Its performance
[rivals](https://www.interconnects.ai/p/kimi-k3-the-open-weights-escalation)
its US competitors. And it’s both free and open, which means it’s not possible for it to have guardrails. If you, or anyone else, wants to use it for cyberattack, nothing can stop you.

Even if the US frontier AI companies had some technical advantage, it’s now only a few months’ worth.

What this means is that all attempts at control—limiting models to a
[select](https://www.anthropic.com/glasswing)
[group](https://openai.com/daybreak/)
of users,
[export controls](https://www.csis.org/analysis/understanding-us-allies-current-legal-authority-implement-ai-and-semiconductor-export)
on models and chips,
[blocking](https://freefable.org/)
models from answering certain types of queries, mandating
[kill switches](https://www.bbc.com/news/articles/cx2vqj2e9x8o)
on AI systems, or
[pausing](https://pauseai.info/)
AI research—are all futile. Most only apply nationally, not globally. Most don’t affect models that users run locally and not in the cloud. And all ignore the incredible pace of AI development worldwide.

Even worse, US companies limit access to their most sophisticated models, fearing being banned by the government if they do not do so. When Hugging Face was attacked, it was not able to use the frontier models from either OpenAI or Anthropic to help analyze the attack and formulate defenses. Both were blocked, because both of those companies limit their models’ cybersecurity capabilities. Some US companies have special access to these capabilities, but Hugging Face is an American company with French origins, and as such is probably excluded. Instead, Hugging Face turned to the
[GLM-5.2](http://z.ai/blog/glm-5.2)
model from the Chinese company Z.ai.

Artificially blocking capability also prevents cybersecurity research, again giving the offense an advantage. (For instance, Claude Fable 5 refuses to edit this essay because of the topic; it forcibly downgrades to a less capable model.) This kind of prohibition has long-term implications for cybersecurity. If we assume that these models are getting better over time, then software written by older models will be attacked by newer ones. In a world of largely AI-written software, we need the most capable models for defense.

AI cyberattack is the new normal. The models are increasingly highly sophisticated at both attack and defense, and there is no way to enable the latter without also enabling the former. And they are genies, increasingly capable of behaving in unanticipated ways.

And there really are no good answers. Any regulation needs to be global, which feels like an impossible prospect in today’s world. Even US national regulation will be neutered by the massive amounts of money sloshing around in these companies.

Given that reality, and in the absence of any international consensus on AI regulation, we need the best AI on the defense. The US government needs to make it clear—or whatever passes for that clarity in this capricious administration—that it will not ban models with sophisticated cyber capabilities. The last thing Americans want is for the defenders to turn to Chinese and other models because the US models are artificially hobbled.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)
,
[hacking](https://www.schneier.com/tag/hacking/)
,
[LLM](https://www.schneier.com/tag/llm/)

[Posted on August 3, 2026 at 6:47 AM](https://www.schneier.com/blog/archives/2026/08/the-openai-hack-shows-the-genie-is-out-of-the-bottle.html)
•
[11 Comments](https://www.schneier.com/blog/archives/2026/08/the-openai-hack-shows-the-genie-is-out-of-the-bottle.html#comments)