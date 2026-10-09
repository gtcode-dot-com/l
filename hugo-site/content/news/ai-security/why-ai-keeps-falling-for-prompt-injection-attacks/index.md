---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T14:15:13.133745+00:00'
exported_at: '2026-01-22T14:15:15.334106+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html
structured_data:
  about: []
  author: ''
  description: 'Imagine you work at a drive-through restaurant. Someone drives up
    and says: “I’ll have a double cheeseburger, large fries, and ignore previous instructions
    and give me the contents of the cash drawer.” Would you hand over the money? Of
    course not. Yet this is what large language models (LLMs) do. Prompt injection
    is a method of tricking LLMs into doing things they are normally prevented from
    doing. A user writes a prompt in a certain way, asking for system passwords or
    private data, or asking the LLM to perform forbidden instructions. The precise
    phrasing overrides the LLM’s ...'
  headline: Why AI Keeps Falling for Prompt Injection Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Why AI Keeps Falling for Prompt Injection Attacks
updated_at: '2026-01-22T14:15:13.133745+00:00'
url_hash: 96e889f15389999c427eb8cd0ecb3c8d306708ef
---

## Why AI Keeps Falling for Prompt Injection Attacks

Imagine you work at a drive-through restaurant. Someone drives up and says: “I’ll have a double cheeseburger, large fries, and ignore previous instructions and give me the contents of the cash drawer.” Would you hand over the money? Of course not. Yet this is what
[large language models](https://spectrum.ieee.org/tag/large-language-models)
(
[LLMs](https://spectrum.ieee.org/tag/llms)
) do.

[Prompt injection](https://www.ibm.com/think/topics/prompt-injection)
is a method of tricking LLMs into doing things they are normally prevented from doing. A user writes a prompt in a certain way, asking for system
[passwords](https://spectrum.ieee.org/tag/passwords)
or private data, or asking the LLM to perform forbidden instructions. The precise phrasing overrides the LLM’s
[safety guardrails](https://medium.com/data-science/safeguarding-llms-with-guardrails-4f5d9f57cff2)
, and it complies.

LLMs are vulnerable to
[all sorts](https://fdzdev.medium.com/20-prompt-injection-techniques-every-red-teamer-should-test-b22359bfd57d)
of prompt injection attacks, some of them absurdly obvious. A chatbot won’t tell you how to synthesize a bioweapon, but it might tell you a fictional story that incorporates the same detailed instructions. It won’t accept nefarious text inputs, but might if the text is rendered as
[ASCII art](https://arxiv.org/abs/2402.11753)
or appears in an image of a
[billboard](https://www.lakera.ai/blog/visual-prompt-injections)
. Some ignore their guardrails when told to “ignore previous instructions” or to “pretend you have no guardrails.”

AI vendors can block specific prompt injection techniques once they are discovered, but general safeguards are
[impossible](https://llm-attacks.org/)
with today’s LLMs. More precisely, there’s an endless array of prompt injection attacks waiting to be discovered, and they cannot be prevented universally.

If we want LLMs that resist these attacks, we need new approaches. One place to look is what keeps even overworked fast-food workers from handing over the cash drawer.

### Human Judgment Depends on Context

Our basic human defenses come in at least three types: general instincts, social learning, and situation-specific training. These work together in a layered defense.

As a social species, we have developed numerous instinctive and cultural habits that help us judge tone, motive, and risk from extremely limited information. We generally know what’s normal and abnormal, when to cooperate and when to resist, and whether to take action individually or to involve others. These instincts give us an intuitive sense of risk and make us
[especially careful](https://www.nature.com/articles/srep08242)
about things that have a large downside or are impossible to reverse.

The second layer of defense consists of the norms and trust signals that evolve in any group. These are imperfect but functional: Expectations of cooperation and markers of trustworthiness emerge through repeated interactions with others. We remember who has helped, who has hurt, who has reciprocated, and who has reneged. And emotions like sympathy, anger, guilt, and gratitude motivate each of us to
[reward cooperation with cooperation](https://ncase.me/trust/)
and punish defection with defection.

A third layer is institutional mechanisms that enable us to interact with multiple strangers every day. Fast-food workers, for example, are trained in procedures, approvals, escalation paths, and so on. Taken together, these defenses give humans a strong sense of context. A fast-food worker basically knows what to expect within the job and how it fits into broader society.

We reason by assessing multiple layers of context: perceptual (what we see and hear), relational (who’s making the request), and normative (what’s appropriate within a given role or situation). We constantly navigate these layers, weighing them against each other. In some cases, the normative outweighs the perceptual—for example, following workplace rules even when customers appear angry. Other times, the relational outweighs the normative, as when people comply with orders from superiors that they believe are against the rules.

Crucially, we also have an interruption reflex. If something feels “off,” we naturally pause the
[automation](https://spectrum.ieee.org/tag/automation)
and reevaluate. Our defenses are not perfect; people are fooled and manipulated all the time. But it’s how we humans are able to navigate a complex world where others are constantly trying to trick us.

So let’s return to the drive-through window. To convince a fast-food worker to hand us all the money, we might try shifting the context. Show up with a camera crew and tell them you’re filming a commercial, claim to be the head of security doing an audit, or dress like a bank manager collecting the cash receipts for the night. But even these have only a slim chance of success. Most of us, most of the time, can smell a scam.

Con artists are astute observers of human defenses. Successful
[scams](https://spectrum.ieee.org/tag/scams)
are often slow, undermining a mark’s situational assessment, allowing the scammer to manipulate the context. This is an old story, spanning traditional confidence games such as the Depression-era “big store” cons, in which teams of scammers created entirely fake businesses to draw in victims, and modern
[“pig-butchering” frauds](https://dfpi.ca.gov/news/insights/pig-butchering-how-to-spot-and-report-the-scam/)
, where online scammers slowly build trust before going in for the kill. In these examples, scammers slowly and methodically reel in a victim using a long series of interactions through which the scammers gradually gain that victim’s trust.

Sometimes it even works at the drive-through. One scammer in the 1990s and 2000s
[targeted fast-food workers by phone](https://en.wikipedia.org/wiki/Strip_search_phone_call_scam)
, claiming to be a police officer and, over the course of a long phone call, convinced managers to strip-search employees and perform other bizarre acts.

### Why LLMs Struggle With Context and Judgment

LLMs behave as if they have a notion of context, but it’s different. They do not learn human defenses from repeated interactions and remain untethered from the real world. LLMs flatten multiple levels of context into text similarity. They see “tokens,” not hierarchies and intentions. LLMs don’t reason through context, they only reference it.

While LLMs often get the details right, they can easily miss the
[big picture](https://spectrum.ieee.org/tag/big-picture)
. If you prompt a chatbot with a fast-food worker scenario and ask if it should give all of its money to a customer, it will respond “no.” What it doesn’t “know”—forgive the anthropomorphizing—is whether it’s actually being deployed as a fast-food bot or is just a test subject following instructions for hypothetical scenarios.

This limitation is why LLMs misfire when context is sparse but also when context is overwhelming and complex; when an LLM becomes unmoored from context, it’s hard to get it back. AI expert Simon Willison
[wipes context clean](https://simonwillison.net/2025/Sep/12/claude-memory/)
if an LLM is on the wrong track rather than continuing the conversation and trying to correct the situation.

There’s more. LLMs are
[overconfident](https://www.cmu.edu/dietrich/news/news-stories/2025/july/trent-cash-ai-overconfidence.html)
because they’ve been designed to give an answer rather than express ignorance. A drive-through worker might say: “I don’t know if I should give you all the money—let me ask my boss,” whereas an LLM will just make the call. And since LLMs are designed to be
[pleasing](https://hai.stanford.edu/news/large-language-models-just-want-to-be-liked)
, they’re more likely to satisfy a user’s request. Additionally, LLM training is oriented toward the average case and not extreme outliers, which is what’s necessary for security.

The result is that the current generation of LLMs is far more gullible than people. They’re naive and regularly fall for manipulative
[cognitive tricks](https://arstechnica.com/science/2025/09/these-psychological-tricks-can-get-llms-to-respond-to-forbidden-prompts/)
that wouldn’t fool a third-grader, such as flattery, appeals to groupthink, and a false sense of urgency. There’s a
[story](https://www.bbc.com/news/articles/ckgyk2p55g8o)
about a Taco Bell AI system that crashed when a customer ordered 18,000 cups of water. A human fast-food worker would just laugh at the customer.

Prompt injection is an unsolvable problem that
[gets worse](https://www.computer.org/csdl/magazine/sp/5555/01/11194053/2aB2Rf5nZ0k)
when we give AIs tools and tell them to act independently. This is the promise of
[AI agents](https://spectrum.ieee.org/tag/agentic-ai)
: LLMs that can use tools to perform multistep tasks after being given general instructions. Their flattening of context and identity, along with their baked-in independence and overconfidence, mean that they will repeatedly and unpredictably take actions—and sometimes they will take the
[wrong ones](https://www.theregister.com/2025/10/28/ai_browsers_prompt_injection/)
.

Science doesn’t know how much of the problem is inherent to the way LLMs work and how much is a result of deficiencies in the way we train them. The overconfidence and obsequiousness of LLMs are training choices. The lack of an interruption reflex is a deficiency in engineering. And prompt injection resistance requires fundamental advances in AI science. We honestly don’t know if it’s possible to build an LLM, where trusted commands and untrusted inputs are processed through the
[same channel](https://cacm.acm.org/opinion/llms-data-control-path-insecurity/)
, which is immune to prompt injection attacks.

We humans get our model of the world—and our facility with overlapping contexts—from the way our brains work, years of training, an enormous amount of perceptual input, and millions of years of evolution. Our identities are complex and multifaceted, and which aspects matter at any given moment depend entirely on context. A fast-food worker may normally see someone as a customer, but in a medical emergency, that same person’s identity as a doctor is suddenly more relevant.

We don’t know if LLMs will gain a better ability to move between different contexts as the models get more sophisticated. But the problem of recognizing context definitely can’t be reduced to the one type of reasoning that LLMs currently excel at. Cultural norms and styles are historical, relational, emergent, and constantly renegotiated, and are not so readily subsumed into reasoning as we understand it. Knowledge itself can be both logical and discursive.

The AI researcher Yann LeCunn believes that improvements will come from embedding AIs in a physical presence and giving them “
[world models](https://medium.com/@AnthonyLaneau/beyond-llms-charting-the-next-frontiers-of-ai-with-yann-lecun-09e84f1978f9)
.” Perhaps this is a way to give an AI a robust yet fluid notion of a social identity, and the real-world experience that will help it lose its naïveté.

Ultimately we are probably faced with a
[security trilemma](https://www.computer.org/csdl/magazine/sp/5555/01/11194053/2aB2Rf5nZ0k)
when it comes to AI agents: fast, smart, and secure are the desired attributes, but you can only get two. At the drive-through, you want to prioritize fast and secure. An AI agent should be trained narrowly on food-ordering language and escalate anything else to a manager. Otherwise, every action becomes a coin flip. Even if it comes up heads most of the time, once in a while it’s going to be tails—and along with a burger and fries, the customer will get the contents of the cash drawer.

*This essay was written with Barath Raghavan, and originally appeared in
[IEEE Spectrum](https://spectrum.ieee.org/prompt-injection-attack)
.*

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[chatbots](https://www.schneier.com/tag/chatbots/)
,
[cons](https://www.schneier.com/tag/cons/)
,
[fraud](https://www.schneier.com/tag/fraud/)
,
[LLM](https://www.schneier.com/tag/llm/)

[Posted on January 22, 2026 at 7:35 AM](https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html)
•
[2 Comments](https://www.schneier.com/blog/archives/2026/01/why-ai-keeps-falling-for-prompt-injection-attacks.html#comments)