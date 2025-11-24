---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: comp-journalism
date: '2025-11-21T00:07:30.235174+00:00'
exported_at: '2025-11-21T00:07:32.784542+00:00'
feed: https://thedispatch.com/feed/
language: en
source_url: https://thedispatch.com/article/ai-911-call-centers
structured_data:
  about: []
  author: ''
  description: More and more emergency dispatch centers are using AI to field non-emergency
    calls.
  headline: What Happens When AI Answers Your 911 Call?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thedispatch.com/article/ai-911-call-centers
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: What Happens When AI Answers Your 911 Call?
updated_at: '2025-11-21T00:07:30.235174+00:00'
url_hash: 1a3991515454cace1e0178e5a3f775fae8a56b13
---

If you call the non-emergency line in Grant County, Washington, just east of Seattle, you’ll hear an unusual voice on the other end of the phone. It is firm, calm, and female-sounding with a slight robotic clipping, though not overly stilted. The voice belongs to Ava. If you call the non-emergency line in Hamilton County, Tennessee, where Chattanooga is located, you’ll have a similar experience with Evelyn.

Neither Ava nor Evelyn is human. Both are AI-powered agents, which have been deployed in more than a dozen 911 centers across the United States to help dispatchers field non-emergency calls on dedicated phone lines. More 911 centers are considering similar moves. As they do so, questions about the safety, accuracy, and oversight of these AI agents used to answer the calls will become more prevalent.
*The Dispatch*
spoke with agencies already using these systems, the companies building them, and experts in AI security and threat modeling to understand why this technology may be used and where it may fall short.

D.T. Donaldson, the director of the unified dispatch center for Grant County, Washington, known as MACC 911, told
*The Dispatch*
he had been looking at the role AI could play in non-emergency calls—with lackluster findings—for more than three years by November 2022. Donaldson and his team were introduced to AI vendor
[Aurelian](https://www.aurelian.com/product)
, which uses a number of generative models (e.g., ChatGPT and Llama) to automate call answering, specifically for non-emergency 911 calls. On Memorial Day weekend in 2024, MACC 911 rolled out its AI-powered agent, known as Ava, to the general public.

Ava asks callers to press 1 if they’d like to speak in Spanish. Then, in either Spanish or English, Ava talks to the caller in real time and will either route the call to a human if it is an emergency, respond to the caller to resolve the issue, or gather information and create a summary for a dispatcher to review and resolve later.

Donaldson said that around 5 percent of calls to non-emergency lines are actually emergencies, making Ava’s ability to accurately understand what constitutes an emergency crucial. Donaldson cited a caller complaining of chest pain as the “archetypal example.” While Hamilton County never adopted a phone tree system, they looked into it to see whether it would be suitable. “In the old [phone tree] system, if you said, ‘It feels like an elephant sitting on my chest,’ it wouldn’t know what to do with that because it’s looking for the word ‘elephant’ in the table [of keywords], " Donaldson told
*The Dispatch*
. “The generative AI completely understands that that’s likely a medical condition, and likely chest pain.”

The reasons for 911 centers to turn toward AI are obvious. Lee Ann Magoski, the director of emergency communications for Monterey County, California, has worked in public safety communications for nearly 30 years. Her center uses a different AI system for answering non-emergency lines called
[AWS Connect](https://aws.amazon.com/blogs/publicsector/supporting-911-centers-non-emergency-response-solutions-architecture-guidance/)
, which she describes as “like a large phone tree … it directs traffic where it needs to go.” She said the system handles about 35 percent of her center’s calls on a monthly basis, saving her dispatchers—who often work more than 100 hours in a two-week stretch—precious time. “They are working four 12-hour days, and then there is still mandatory overtime on top of that to keep everyone safe,” she said. Her center also uses AI tools to monitor compliance, transcribe calls, and train future dispatchers. At any one time, dispatchers are “managing eight, 10, or more incidents,” often in
[life-and-death](https://thecurrentga.org/2023/09/20/911-call-takers-are-demoralized-overwhelmed-and-dealing-with-their-own-mental-health-woes/)
circumstances, Magoski said. Emergency call centers have one of the
[highest turnover rates](https://www.iaedjournal.org/keeping-them-in-the-profession#:~:text=Despite%20obstacles%20(as%20highlighted%20in,with%20the%20highest%20turnover%20rates.)
of any industry given the psychological stress dispatchers are subject to.

“Switching [between emergency and non-emergency calls] is very costly on a psyche,” Donaldson said. Barbara Loveless, the director of operations in Hamilton County, Tennessee, points to this as a key benefit of using AI to handle non-emergency calls: “It gave staff that necessary time to be ready for when the next bad call hits.”

Yet some AI security experts are raising concerns when it comes to using AI to answer non-emergency calls. They pointed to a number of inherent issues with generative AI systems, including
[hallucinations](https://www.computerworld.com/article/4059383/openai-admits-ai-hallucinations-are-mathematically-inevitable-not-just-engineering-flaws.html)
,
[biases](https://carnegieendowment.org/research/2025/01/the-world-according-to-generative-artificial-intelligence?lang=en)
,
[edge cases](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know)
,
[error rates](https://www.eweek.com/news/ai-hallucinations-increase/)
, and security weaknesses.

Tim Marple leads Maiden Labs, a nonprofit focusing on using emerging technologies for public good. He previously served as a lead analyst in the intelligence and investigations team at OpenAI. Marple described AI used in 911 dispatch centers as “categorically unsettling.”

“It’s sugar when you’re hungry,” he told
*The Dispatch*
. “What this boils down to is in potential instances of emergency, we are delegating the responsibility to adjudicate on what could be life or death conditions to a machine that has known biases and known problems that include hallucination outside of the realm of reality.”

Richard Bird, the chief security officer for Singulr AI, an enterprise platform for AI security and governance, agreed. He worries that these systems are not being properly and scientifically tested for accuracy rates, despite having known issues such as
[hallucinations](https://openai.com/index/why-language-models-hallucinate/)
. “People that are unapologetic about AI today go, ‘Oh, well, it’s just the beginning, it’ll get better,’ which is true,” he said. He likened it to boarding an experimental aircraft on which the pilot says, “‘Hey, I’ve got bad news for you today. This flight’s not going to make it. But good news, it’ll get better over time, right?’ This idea of improving by continuously testing production AI systems in real life situations has already proven to be a very bad idea.”

Back at MACC 911 in Grant County, Washington, Technical Services Manager Garrett Klein said that a friend flagged one such issue with the system there: When they tried to report a mental health concern, the call was handled by the AI instead of being routed immediately to a dispatcher. Klein described how after he reported the problem along, Aurelian fixed it within 15 minutes.

But it’s impossible to know how many other cases are not being flagged or escalated appropriately.

*The Dispatch*
tested the Ava AI agent on a staging line. In many cases, it was able to accurately follow protocols and escalate calls appropriately. But in some more challenging scenarios, it struggled to follow what might be the right protocols. For example, when told of an odd smell in a basement similar to moldy eggs, it did not escalate the call as a possible gas leak.

Using AI agents poses unique security risks, including prompt injections (where a malicious caller embeds hidden commands into their speech to manipulate the AI’s behavior) and data or model poisoning (where attackers insert falsified or misleading information into the system’s training data to distort how it interprets real calls). Were these AI agents to be attacked, serious problems could include real emergencies being misrouted or personal data being leaked.

Bird described using AI agents to answer 911 calls as “kind of emblematic of the classic tech bro statement of ‘build fast, break things’ … except ‘build fast, break things’ is a really irresponsible way to address technology solutions in things like public safety emergency services.”

Ryan Rowcliffe, the field chief technology officer at Legion Security, a company that automates security analyst workflows, emphasized the particular “caution and responsibility” companies using AI agents should take. “Anything which isn’t what the whole training sets historically have been trained on will inject bias, which then means the performance of the system is going to degrade … they’re tokenized text and they’re going to be fallible,” Rowcliffe told
*The Dispatch.*

When asked to respond to such criticisms, Aurelian CEO Max Keenan told
*The Dispatch*
a safeguard on Ava is running additional AI programs in the background while it fields calls to check for biases and hallucinations. But some experts worried that both models may have similar biases or would fail to catch the same hallucinations.

When asked about error rates, Keenan told
*The Dispatch*
that defining “error” is difficult, since the range of acceptable outcomes is large in non-emergencies. He said that “true errors” (which he defined as a call that generates an objectively wrong outcome that’s not what the caller intended) occur in less than 1 percent of calls. But they declined to share data from their reviews in assessing the error rate.

Many of those running 911 dispatch centers maintain that the AI agents are saving human dispatchers valuable time. “Would you rather the dispatcher work on your parking problem or work on the baby not breathing?” Donaldson said.

“With the introduction of any new tool … there is a lot of concern from our call-taking staff,” Klein said. “The thought of maybe a computer bungling up a call—really it’s kind of an unconscionable thought to them because it reflects on them. So there was, I think, concern initially.” That concern has abated, Klein said. Ava is now seen as part of the team.

“She is very much a member of the team to the point where if a caller is abusive to her, our call-takers are calling them back and [saying], ‘Hey, what’s your problem?’” Klein added. “It’s been quite the evolution … she’s on staff, she has a name, they refer to her in the proper.”

When Ava hit the milestone of taking her 10,000th call, staff at MACC 911 thought so much of it that they made Ava a cake to celebrate.