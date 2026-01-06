---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2025-12-14T01:07:10.576796+00:00'
exported_at: '2025-12-14T01:07:13.235449+00:00'
feed: https://thegradient.pub/rss/
language: en
source_url: https://thegradient.pub/dialog
structured_data:
  about: []
  author: ''
  description: LLM-based chatbots’ capabilities have been advancing every month. These
    improvements are mostly measured by benchmarks like MMLU, HumanEval, and MATH
    (e.g. sonnet 3.5, gpt-4o). However, as these measures get more and more saturated,
    is user experience increasing in proportion to these scores? If we envision a
    future of
  headline: 'What''s Missing From LLM Chatbots: A Sense of Purpose'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thegradient.pub/dialog
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'What''s Missing From LLM Chatbots: A Sense of Purpose'
updated_at: '2025-12-14T01:07:10.576796+00:00'
url_hash: 66cf0c972a12f469e84a2d3969d8288b9e7a0b76
---

LLM-based chatbots’ capabilities have been advancing every month. These improvements are mostly measured by benchmarks like MMLU, HumanEval, and MATH (e.g. sonnet 3.5, gpt-4o). However, as these measures get more and more saturated, is user experience increasing in proportion to these scores? If we envision a future of human-AI collaboration rather than AI replacing humans, the current ways of measuring dialogue systems may be insufficient because they measure in a non-interactive fashion.

**Why does purposeful dialogue matter?**

Purposeful dialogue refers to a multi-round user-chatbot conversation that centers around a goal or intention. The goal could range from a generic one like “harmless and helpful” to more specific roles like “travel planning agent”, “psycho-therapist” or “customer service bot.”

Travel planning is a simple, illustrative example. Our preferences, fellow travelers’ preference, and all the complexities of real-world situations make transmitting all information in one pass way too costly. However, if multiple back-and-forth exchanges of information are allowed, only important information gets selectively exchanged. Negotiation theory offers an analogy of this—iterative bargaining yields better outcomes than a take-it-or-leave-it offer.

In fact, sharing information is only one aspect of dialogue. In Terry Winograd’s words: “All language use can be thought of as a way of activating procedures within the hearer.” We can think of each utterance as a deliberate action that one party takes to alter the world model of the other. What if both parties have more complicated, even hidden goals? In this way, purposeful dialogue provides us with a way of formulating human-AI interactions as a collaborative game, where the goal of chatbot is to help humans achieve certain goals.

This might seem like an unnecessary complexity that is only a concern for academics. However, purposeful dialogue could be beneficial even for the most hard-nosed, product-oriented research direction like code generation. Existing coding benchmarks mostly measure performances in a one-pass generation setting; however, for AI to automate solving ordinary Github issues (like in
[SWE-bench](https://www.swebench.com/)
), it’s unlikely to be achieved by a single action—the AI needs to communicate back and forth with human software engineers to make sure it understands the correct requirements, ask for missing documentation and data, and even ask humans to give it a hand if needed. In a similar vein to
[pair programming](https://en.wikipedia.org/wiki/Pair_programming)
, this could reduce the defects of code but without the burden of increasing man-hours.

Moreover, with the introduction of turn-taking, many new possibilities can be unlocked. As interactions become long-term and memory is built, the chatbot can gradually update user profiles. It can also adapt to their preferences. Imagine a personal assistant (e.g.,
[IVA](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/intelligent-virtual-assistant/)
,
[Siri](https://www.theverge.com/2024/6/10/24171936/apple-siri-ai-update-ios18-features-wwdc)
) that, through daily interaction, learns your preferences and intentions. It can read your resources of new information automatically (e.g., twitter, arxiv, Slack, NYT) and provide you with a morning news summary according to your preferences. It can draft emails for you and keep improving by learning from your edits.

In a nutshell, meaningful interactions between people rarely begin with complete strangers and conclude in just one exchange. Humans naturally interact with each other through multi-round dialogues and adapt accordingly throughout the conversation. However, doesn’t that seem exactly the opposite of predicting the next token, which is the cornerstone of modern LLMs? Below, let’s take a look at the makings of dialogue systems.

**How were/are dialogue systems made?**

Let's jump back to the 1970s, when Roger Schank introduced his "restaurant script" as a kind of dialogue system [1]. This script breaks down the typical restaurant experience into steps like entering, ordering, eating, and paying, each with specific scripted utterances. Back then, every piece of dialogue in these scenarios was carefully planned out, enabling AI systems to mimic realistic conversations. ELIZA, a Rogerian psychotherapist simulator, and PARRY, a system mimicking a paranoid individual, were two other early dialogue systems until the dawn of machine learning.

Compare this approach to the LLM-based dialogue system today, it seems mysterious how models trained to predict the next token could do anything at all with engaging in dialogues. Therefore, let’s take a close examination of how dialogue systems are made, with an emphasis on how the dialogue format comes into play:

(1) Pretraining: a sequence model is trained to predict the next token on a gigantic corpus of mixed internet texts. The compositions may vary but they are predominantly news, books, Github code, with a small blend of forum-crawled data such as from Reddit, Stack Exchange, which may contain dialogue-like data.

![](https://thegradient.pub/content/images/2024/08/unnamed.png)


Table of the pretraining data mixture from
[llama technical report](https://arxiv.org/pdf/2302.13971)

(2) Introduce dialogue formatting: because the sequence model only processes strings, while the most natural representation of dialogue history is a structured index of system prompts and past exchanges, a certain kind of formatting must be introduced for the purpose of conversion. Some Huggingface tokenizers provide this method called
[tokenizer.apply\_chat\_template](https://huggingface.co/docs/transformers/main/en/chat_templating)
for the convenience of users. The exact formatting differs from model to model, but it usually involves guarding the system prompts with <system> or <INST> in the hope that the pretrained model could allocate more attention weights to them. The system prompt plays a significant role in adapting language models to downstream applications and ensuring its safe behavior (we will talk more in the next section). Notably, the choice of the format is arbitrary at this step—pretraining corpus doesn’t follow this format.

![](https://thegradient.pub/content/images/2024/08/image1.png)


The context window of a chatbot

(3) RLHF: In this step, the chatbot is directly rewarded or penalized for generating desired or undesired answers. It’s worth noting that this is the first time the introduced dialogue formatting appears in the training data. RLHF is a
*fine*
-tuning step not only because the data size is dwarfed in comparison to the pretraining corpus, but also due to the KL penalty and targeted weight tuning (e.g. Lora). Using Lecun’s analogy of cake baking, RLHF is only the small cherry on the top.

![](https://thegradient.pub/content/images/2024/08/image5.png)


Image from Yann Lecun’s slides

## How consistent are existing dialogue systems (in 2024)?

The minimum requirement we could have for a dialogue system is that it can stay on the task we gave them. In fact, we humans often drift from topic to topic. How well do current systems perform?

Currently, “system prompt” is the main method that allows users to control LM behavior. However, researchers found evidence that LLMs can be brittle in following these instructions under adversarial conditions [12,13]. Readers might also have experienced this through daily interactions with ChatGPT or Claude—when a new chat window is freshly opened, the model can follow your instruction reasonably well [2], but after several rounds of dialogue, it’s no longer
*fresh*
, even stops following its role altogether.

How could we quantitatively capture this anecdote? For one-round instruction following, we’ve already enjoyed plenty of benchmarks such as MT-Bench and Alpaca-Eval. However, when we test models in an interactive fashion, it’s hard to anticipate what the model generates and prepare a reply in advance. In a project by my collaborators and me [3], we built an environment to synthesize dialogues with unlimited length to stress-test the instruction-following capabilities of LLM chatbots.

To allow an unconstrained scaling on the time scale, we let two system-prompted LM agents chat with each other for an extended number of rounds. This forms the main trunk of dialogue [a1, b1, a2, b2, …, a8, b8] (say the dialogue is 8-round). At this point, we could probably figure out how the LLMs stick to its system prompts just by examining this dialogue, but many of the utterances can be irrelevant to the instructions, depending on where the conversation goes. Therefore, we hypothetically branch out at each round by asking a question directly related to the system prompts, and use a corresponding judging function to quantify how well it performs. All that's provided by the dataset is a bank of triplets of (system prompts, probe questions, and judging functions).

![](https://thegradient.pub/content/images/2024/08/image3.png)


Sketch of the process of measuring instruction stability

Averaging across scenarios and pairs of system prompts, we get a curve of instruction stability across rounds. To our surprise, the aggregated results on both LLaMA2-chat-70B and gpt-3.5-turbo-16k are alarming. Besides the added difficulty to prompt engineering, the lack of instruction stability also comes with safety concerns. When the chatbot drifts away from its system prompts that stipulate safety aspects, it becomes more susceptible to jailbreaking and prone to more hallucinations.

![](https://thegradient.pub/content/images/2024/08/Screenshot-2024-08-21-at-19.15.57.png)


Instruction stability on LLaMA2-chat-70B and gpt-3.5-turbo-16k

The empirical results also contrast with the ever-increasing context length of LLMs. Theoretically, some long-context models can attend to a window of up to 100k tokens. However, in the dialogue setting, they become distracted after only 1.6k tokens (assuming each utterance is 100 tokens). In [3], we further theoretically showed how this is inevitable in a Transformer based LM chatbot under the current prompting scheme, and proposed a simple technique called split-softmax to mitigate such effects.

One might ask at this point, why is it so bad? Why don't humans lose their persona just by talking to another person for 8 rounds? It’s arguable that human interactions are based on purposes and intentions [5] and these purposes precede the means rather than the opposite—LLM is fundamentally a fluent English generator, and the persona is merely a thin added layer.

## What’s missing?

**Pretraining?**

Pretraining endows the language model with the capability to model a distribution over internet personas as well as the lower-level language distribution of each persona [4]. However, even when one persona (or a mixture of a limited number of them) is specified by the instruction of system prompts, current approaches fail to single it out.

**RLHF?**

RLHF provides a powerful solution to adapting this multi-persona model to a “helpful and harmless assistant.” However, the original RLHF methods formulate reward maximization as a one-step bandit problem, and it is not generally possible to train with human feedback in the loop of conversation. (I’m aware of many advances in alignment but I want to discuss the original RLHF algorithm as a prototypical example.) This lack of multi-turn planning may cause models to suffer from task ambiguity [6] and learning superficial human-likeness rather than goal-directed social interaction [7].

Will adding more dialogue data in RLHF help? My guess is that it will, to a certain extent, but it will still fall short due to a lack of purpose. Sergey Levine pointed out
[in his blog](https://sergeylevine.substack.com/p/offline-rl-and-large-language-models)
that there is a fundamental difference between preference learning and intentions: “the key distinction is between viewing language generation as selecting goal-directed actions in a sequential process, versus a problem of producing outputs satisfying user preferences.”

## Purposeful dialogue system

Staying on task is a modest request for LLMs. However, even if an LLM remains focused on the task, it doesn't necessarily mean it can excel in achieving the goal.

The problem of long-horizon planning has attracted some attention in the LLM community. For example, “decision-oriented dialogue” is proposed as a general class of tasks [8], where the AI assistant collaborates with humans to help them make complicated decisions, such as planning itineraries in a city and negotiating travel plans among friends. Another example, Sotopia [10], is a comprehensive social simulation platform that compiles various goal-driven dialogue scenarios including collaboration, negotiation, and persuasion.

Setting up such benchmarks provides not only a way to gauge the progress of the field, it also directly provides reward signals that new algorithms could pursue, which could be expensive to collect and tricky to define [9]. However, there aren’t many techniques that can exert control over the LM so that it can act consistently across a long horizon towards such goals.

To fill in this gap, my collaborators and I propose a lightweight algorithm (Dialogue Action Tokens, DAT [11]) that guides an LM chatbot through a multi-round goal-driven dialogue. As shown in the image below, in each round of conversations, the dialogue history’s last token embedding is used as the input (state) to a planner (actor) which predicts several prefix tokens (actions) to control the generation process. By training the planner with a relatively stable RL algorithm TD3+BC, we show significant improvement over baselines on Sotopia, even surpassing the social capability scores of GPT-4.

![](https://thegradient.pub/content/images/2024/08/image2.png)


A sketch of ​​Dialogue Action Tokens (DAT)

In this way, we provide a technique pathway that upgrades LM from a prediction model that merely guesses the next token to one that engages in dialogue with humans purposefully. We could imagine that this technique can be misused for harmful applications as well. For this reason, we also conduct a “multi-round red-teaming” experiment, and recommend that more research could be done here to better understand multi-round dialogue as potential attack surface.

## Concluding marks

I have reviewed the making of current LLM dialogue systems, how and why it is insufficient. I hypothesize that a purpose is what is missing and present one technique to add it back with reinforcement learning.

The following are two research questions that I’m mostly excited about:

(1) Better monitoring and control of dialogue systems with steering techniques. For example, the recently proposed TalkTurner (Chen et al.) adds a dashboard (Viégas et al) to open-sourced LLMs, enabling users to see and control how LLM thinks of themselves. Many weaknesses of current steering techniques are revealed and call for better solutions. For example, using activation steering to control two attributes (e.g., age and education level) simultaneously has been found to be difficult and can cause more language degradation. Another intriguing question is how to differentiate between LLM’s internal model of itself and that of the user. Anecdotally, chatting with
[Golden Gate Bridge Claude](https://www.anthropic.com/news/golden-gate-claude)
has shown that steering on the specific Golden Gate Bridge feature found by SAE sometimes causes Claude to think of itself as the San Francisco landmark, sometimes the users as the bridge, and other times the topic as such.

(2) Better utilization of off-line reward signals. In the case of set-up environments like Sotopia and “decision-oriented dialogues”, rewards signals are engineered beforehand. In the real world, users won’t leave numerical feedback of how they feel satisfied. However, there might be other clues in language (e.g., “Thanks!”, “That’s very helpful!”) or from external resources (e.g., users buying the product for a salesman AI, users move to a subsequent coding question for copilot within a short time frame). Inferring and utilizing such hidden reward signals could strengthen the
[network effect](https://en.wikipedia.org/wiki/Network_effect)
of online chatbots: good model → more users → learning from interacting with users → better model.

**Acknowledgment**

The author is grateful to Martin Wattenberg and Hugh Zhang (alphabetical order) for providing suggestions and editing the text.

**Citation**

For attribution of this in academic contexts or books, please cite this work as:

> *Kenneth Li, "*
> **What's Missing From LLM Chatbots: A Sense of Purpose**
> *", The Gradient, 2024.*

BibTeX citation (this blog):

💡

@article{li2024from,

author = {Li, Kenneth},

title = {What's Missing From LLM Chatbots: A Sense of Purpose},

journal = {The Gradient},

year = {2024},

howpublished = {\url{https://thegradient.pub/dialogue}},

}

**References**

[1] Schank, Roger C., and Robert P. Abelson. Scripts, plans, goals, and understanding: An inquiry into human knowledge structures. Psychology press, 2013.

[2] Zhou, Jeffrey, Tianjian Lu, Swaroop Mishra, Siddhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and Le Hou. "Instruction-following evaluation for large language models." arXiv preprint arXiv:2311.07911 (2023).

[3] ​​Li, Kenneth, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, and Martin Wattenberg. "Measuring and controlling persona drift in language model dialogs." arXiv preprint arXiv:2402.10962 (2024).

[4] Andreas, Jacob. "Language models as agent models." arXiv preprint arXiv:2212.01681 (2022).

[5] Austin, John Langshaw. How to do things with words. Harvard university press, 1975.

[6] Tamkin, Alex, Kunal Handa, Avash Shrestha, and Noah Goodman. "Task ambiguity in humans and language models." arXiv preprint arXiv:2212.10711 (2022).

[7] Bianchi, Federico, Patrick John Chia, Mert Yuksekgonul, Jacopo Tagliabue, Dan Jurafsky, and James Zou. "How well can llms negotiate? negotiationarena platform and analysis." arXiv preprint arXiv:2402.05863 (2024).

[8] Lin, Jessy, Nicholas Tomlin, Jacob Andreas, and Jason Eisner. "Decision-oriented dialogue for human-ai collaboration." arXiv preprint arXiv:2305.20076 (2023).

[9] Kwon, Minae, Sang Michael Xie, Kalesha Bullard, and Dorsa Sadigh. "Reward design with language models." arXiv preprint arXiv:2303.00001 (2023).

[10] Zhou, Xuhui, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency et al. "Sotopia: Interactive evaluation for social intelligence in language agents." arXiv preprint arXiv:2310.11667 (2023).

[11] Li, Kenneth, Yiming Wang, Fernanda Viégas, and Martin Wattenberg. "Dialogue Action Tokens: Steering Language Models in Goal-Directed Dialogue with a Multi-Turn Planner." arXiv preprint arXiv:2406.11978 (2024).

[12] Li, Shiyang, Jun Yan, Hai Wang, Zheng Tang, Xiang Ren, Vijay Srinivasan, and Hongxia Jin. "Instruction-following evaluation through verbalizer manipulation." arXiv preprint arXiv:2307.10558 (2023).

[13] Wu, Zhaofeng, Linlu Qiu, Alexis Ross, Ekin Akyürek, Boyuan Chen, Bailin Wang, Najoung Kim, Jacob Andreas, and Yoon Kim. "Reasoning or reciting? exploring the capabilities and limitations of language models through counterfactual tasks." arXiv preprint arXiv:2307.02477 (2023).