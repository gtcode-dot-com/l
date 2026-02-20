---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-20T12:15:15.095988+00:00'
exported_at: '2026-02-20T12:15:18.042903+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html
structured_data:
  about: []
  author: ''
  description: Attacks against modern generative artificial intelligence (AI) large
    language models (LLMs) pose a real threat. Yet discussions around these attacks
    and their potential defenses are dangerously myopic. The dominant narrative focuses
    on “prompt injection,” a set of techniques to embed instructions into inputs to
    LLM intended to perform malicious activity. This term suggests a simple, singular
    vulnerability. This framing obscures a more complex and dangerous reality. Attacks
    on LLM-based systems have evolved into a distinct class of malware execution mechanisms,
    which we term “promptware.” In a ...
  headline: The Promptware Kill Chain
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: The Promptware Kill Chain
updated_at: '2026-02-20T12:15:15.095988+00:00'
url_hash: 85a071f015ff9f2696a5dfcffac1850138154516
---

## The Promptware Kill Chain

[![The promptware kill chain: initial access, privilege escalation, reconnaissance, persistence, command & control, lateral movement, action on objective](https://www.schneier.com/wp-content/uploads/2026/02/promptware-kill-chain-660w.jpg)](https://www.schneier.com/wp-content/uploads/2026/02/promptware-kill-chain.jpg)

Attacks against modern generative artificial intelligence (AI) large language models (LLMs) pose a real threat. Yet discussions around these attacks and their potential defenses are dangerously myopic. The dominant narrative focuses on “
[prompt injection](https://simonwillison.net/2022/Sep/12/prompt-injection/)
,” a set of techniques to embed instructions into inputs to LLM intended to perform malicious activity. This term suggests a simple, singular vulnerability. This framing obscures a more complex and dangerous reality. Attacks on LLM-based systems have evolved into a distinct class of malware execution mechanisms, which we term “promptware.” In a
[new paper](https://arxiv.org/abs/2601.09625)
, we, the authors, propose a structured seven-step “promptware kill chain” to provide policymakers and security practitioners with the necessary vocabulary and framework to address the escalating AI threat landscape.

In our model, the promptware kill chain begins with
*Initial Access*
. This is where the malicious payload enters the AI system. This can happen directly, where an attacker types a malicious prompt into the LLM application, or, far more insidiously, through “indirect prompt injection.” In the indirect attack, the adversary embeds malicious instructions in content that the LLM retrieves (obtains in inference time), such as a web page, an email, or a shared document. As LLMs become multimodal (capable of processing various input types beyond text), this vector expands even further; malicious instructions can now be hidden inside an image or audio file, waiting to be processed by a vision-language model.

The fundamental issue lies in the architecture of LLMs themselves. Unlike traditional computing systems that strictly separate executable code from user data, LLMs process all input—whether it is a system command, a user’s email, or a retrieved document—as a single, undifferentiated sequence of tokens. There is no architectural boundary to enforce a distinction between trusted instructions and untrusted data. Consequently, a malicious instruction embedded in a seemingly harmless document is processed with the same authority as a system command.

But prompt injection is only the
*Initial Access*
step in a sophisticated, multistage operation that mirrors traditional malware campaigns such as Stuxnet or NotPetya.

Once the malicious instructions are inside material incorporated into the AI’s learning, the attack transitions to
*Privilege Escalation*
, often referred to as “jailbreaking.” In this phase, the attacker circumvents the safety training and policy guardrails that vendors such as OpenAI or Google have built into their models. Through techniques analogous to social engineering—convincing the model to adopt a persona that ignores rules—to sophisticated adversarial suffixes in the prompt or data, the promptware tricks the model into performing actions it would normally refuse. This is akin to an attacker escalating from a standard user account to administrator privileges in a traditional cyberattack; it unlocks the full capability of the underlying model for malicious use.

Following privilege escalation comes
*Reconnaissance*
. Here, the attack manipulates the LLM to reveal information about its assets, connected services, and capabilities. This allows the attack to advance autonomously down the kill chain without alerting the victim. Unlike reconnaissance in classical malware, which is performed typically before the initial access, promptware reconnaissance occurs after the initial access and jailbreaking components have already succeeded. Its effectiveness relies entirely on the victim model’s ability to reason over its context, and inadvertently turns that reasoning to the attacker’s advantage.

Fourth: the
*Persistence*
phase. A transient attack that disappears after one interaction with the LLM application is a nuisance; a persistent one compromises the LLM application for good. Through a variety of mechanisms, promptware embeds itself into the long-term memory of an AI agent or poisons the databases the agent relies on. For instance, a worm could infect a user’s email archive so that every time the AI summarizes past emails, the malicious code is re-executed.

The
*Command-and-Control (C2)*
stage relies on the established persistence and dynamic fetching of commands by the LLM application in inference time from the internet. While not strictly required to advance the kill chain, this stage enables the promptware to evolve from a static threat with fixed goals and scheme determined at injection time into a controllable trojan whose behavior can be modified by an attacker.

The sixth stage,
*Lateral Movement*
, is where the attack spreads from the initial victim to other users, devices, or systems. In the rush to give AI agents access to our emails, calendars, and enterprise platforms, we create highways for malware propagation. In a “self-replicating” attack, an infected email assistant is tricked into forwarding the malicious payload to all contacts, spreading the infection like a computer virus. In other cases, an attack might pivot from a calendar invite to controlling smart home devices or exfiltrating data from a connected web browser. The interconnectedness that makes these agents useful is precisely what makes them vulnerable to a cascading failure.

Finally, the kill chain concludes with
*Actions on Objective*
. The goal of promptware is not just to make a chatbot say something offensive; it is often to achieve tangible malicious outcomes through data exfiltration, financial fraud, or even physical world impact. There are examples of AI
[agents being manipulated](https://crypto.news/aixbt-agent-hacked-losing-55eth-aixbt-token-drops-2025/)
into selling cars for a single dollar or
[transferring cryptocurrency](https://crypto.news/aixbt-agent-hacked-losing-55eth-aixbt-token-drops-2025/)
to an attacker’s wallet. Most alarmingly, agents with coding capabilities can be tricked into executing arbitrary code, granting the attacker total control over the AI’s underlying system. The outcome of this stage determines the type of malware executed by promptware, including infostealer, spyware, and cryptostealer, among others.

The kill chain was already demonstrated. For example, in the research “
[Invitation Is All You Need](https://arxiv.org/abs/2508.12175)
,” attackers achieved initial access by embedding a malicious prompt in the title of a Google Calendar invitation. The prompt then leveraged an advanced technique known as delayed tool invocation to coerce the LLM into executing the injected instructions. Because the prompt was embedded in a Google Calendar artifact, it persisted in the long-term memory of the user’s workspace. Lateral movement occurred when the prompt instructed the Google Assistant to launch the Zoom application, and the final objective involved covertly livestreaming video of the unsuspecting user who had merely asked about their upcoming meetings. C2 and reconnaissance weren’t demonstrated in this attack.

Similarly, the “
[Here Comes the AI Worm](https://dl.acm.org/doi/10.1145/3719027.3765196)
” research demonstrated another end-to-end realization of the kill chain. In this case, initial access was achieved via a prompt injected into an email sent to the victim. The prompt employed a role-playing technique to compel the LLM to follow the attacker’s instructions. Since the prompt was embedded in an email, it likewise persisted in the long-term memory of the user’s workspace. The injected prompt instructed the LLM to replicate itself and exfiltrate sensitive user data, leading to off-device lateral movement when the email assistant was later asked to draft new emails. These emails, containing sensitive information, were subsequently sent by the user to additional recipients, resulting in the infection of new clients and a sublinear propagation of the attack. C2 and reconnaissance weren’t demonstrated in this attack.

The promptware kill chain gives us a framework for understanding these and similar attacks; the paper characterizes dozens of them. Prompt injection isn’t something we can fix in current LLM technology. Instead, we need an in-depth defensive strategy that assumes initial access will occur and focuses on breaking the chain at subsequent steps, including by limiting privilege escalation, constraining reconnaissance, preventing persistence, disrupting C2, and restricting the actions an agent is permitted to take. By understanding promptware as a complex, multistage malware campaign, we can shift from reactive patching to systematic risk management, securing the critical systems we are so eager to build.

*This essay was written with Oleg Brodt, Elad Feldman and Ben Nassi, and originally appeared in
[Lawfare](https://www.lawfaremedia.org/article/the-promptware-kill-chain)
.*

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[LLM](https://www.schneier.com/tag/llm/)
,
[malware](https://www.schneier.com/tag/malware/)

[Posted on February 16, 2026 at 7:04 AM](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html)
•
[11 Comments](https://www.schneier.com/blog/archives/2026/02/the-promptware-kill-chain.html#comments)