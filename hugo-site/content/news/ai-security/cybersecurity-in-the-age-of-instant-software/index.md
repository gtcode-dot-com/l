---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-07T23:53:02.185112+00:00'
exported_at: '2026-04-07T23:53:04.616494+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html
structured_data:
  about: []
  author: ''
  description: 'AI is rapidly changing how software is written, deployed, and used.
    Trends point to a future where AIs can write custom software quickly and easily:
    “instant software.” Taken to an extreme, it might become easier for a user to
    have an AI write an application on demand—a spreadsheet, for example—and delete
    it when yo...'
  headline: Cybersecurity in the Age of Instant Software
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Cybersecurity in the Age of Instant Software
updated_at: '2026-04-07T23:53:02.185112+00:00'
url_hash: f5e0fb4dbb299dbddabeed6330a56a6e47488451
---

## Cybersecurity in the Age of Instant Software

AI is rapidly changing how software is written, deployed, and used. Trends point to a future where AIs can write custom software quickly and easily: “instant software.” Taken to an extreme, it might become easier for a user to have an AI write an application on demand—a spreadsheet, for example—and delete it when you’re done using it than to buy one commercially. Future systems could include a mix: both traditional long-term software and ephemeral instant software that is constantly being written, deployed, modified, and deleted.

AI is changing cybersecurity as well. In particular, AI systems are getting better at finding and patching vulnerabilities in code. This has implications for both attackers and defenders, depending on the ways this and related technologies improve.

In this essay, I want to take an optimistic view of AI’s progress, and to speculate what AI-dominated cybersecurity in an age of instant software might look like. There are a number of unknowns that will factor into how the arms race between attacker and defender might play out.

## How flaw discovery might work

On the attacker side, the ability of AIs to automatically find and exploit vulnerabilities has increased dramatically over the past few months. We are already seeing both
[government](https://www.anthropic.com/news/disrupting-AI-espionage)
and
[criminal](https://www.eset.com/us/about/newsroom/research/eset-discovers-promptlock-the-first-ai-powered-ransomware/)
hackers using AI to attack systems. The exploitation part is critical here, because it gives an unsophisticated attacker capabilities far beyond their understanding. As AIs get better, expect more attackers to automate their attacks using AI. And as individuals and organizations can increasingly run powerful AI models locally, AI companies
[monitoring and disrupting](https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/)
malicious AI use will become increasingly irrelevant.

Expect open-source software, including open-source libraries incorporated in proprietary software, to be the most targeted, because vulnerabilities are easier to find in source code. Unknown No. 1 is how well AI vulnerability discovery tools will work against closed-source commercial software packages. I believe they will soon be good enough to find vulnerabilities just by analyzing a copy of a shipped product, without access to the source code. If that’s true, commercial software will be vulnerable as well.

Particularly vulnerable will be software in IoT devices: things like internet-connected cars, refrigerators, and security cameras. Also industrial IoT software in our internet-connected power grid, oil refineries and pipelines, chemical plants, and so on. IoT software tends to be of much lower quality, and industrial IoT software tends to be legacy.

Instant software is differently vulnerable. It’s not mass market. It’s created for a particular person, organization, or network. The attacker generally won’t have access to any code to analyze, which makes it less likely to be exploited by external attackers. If it’s ephemeral, any vulnerabilities will have a short lifetime. But lots of instant software will live on networks for a long time. And if it gets uploaded to shared tool libraries, attackers will be able to download and analyze that code.

All of this points to a future where AIs will become powerful tools of cyberattack, able to automatically find and exploit vulnerabilities in systems worldwide.

## Automating patch creation

But that’s just half of the arms race. Defenders get to use AI, too. These same AI vulnerability-finding technologies are even more valuable for defense. When the defensive side finds an exploitable vulnerability, it can patch the code and deny it to attackers forever.

How this works in practice depends on another related capability: the ability of AIs to patch vulnerable software, which is closely related to their ability to write secure code in the first place.

AIs are not very good at this today; the instant software that AIs create is generally filled with vulnerabilities, both because AIs write insecure code and because the people vibe coding don’t understand security. OpenClaw is a
[good example](https://blog.barrack.ai/openclaw-security-vulnerabilities-2026/)
of this.

Unknown No. 2 is how much better AIs will get at writing secure code. The fact that they’re trained on massive corpuses of poorly written and insecure code is a handicap, but they are getting better. If they can reliably write vulnerability-free code, it would be an enormous advantage for the defender. And AI-based vulnerability-finding makes it
[easier](https://sergejepp.substack.com/p/winning-the-ai-cyber-race-verifiability)
for an AI to train on writing secure code.

We can
[envision](https://www.csoonline.com/article/4069075/autonomous-ai-hacking-and-the-future-of-cybersecurity.html)
a future where AI tools that find and patch vulnerabilities are part of the typical software development process. We can’t say that the code would be vulnerability-free—that’s an impossible goal—but it could be without any easily findable vulnerabilities. If the technology got really good, the code could become essentially vulnerability-free.

## Patching lags and legacy software

For new software—both commercial and instant—this future favors the defender. For commercial and conventional open-source software, it’s not that simple. Right now, the world is filled with legacy software. Much of it—like IoT device software—has no dedicated security team to update it. Sometimes it is incapable of being patched. Just as it’s harder for AIs to find vulnerabilities when they don’t have access to the source code, it’s harder for AIs to patch software when they are not embedded in the development process.

I’m not as confident that AI systems will be able to patch vulnerabilities as easily as they can find them, because patching often requires more holistic testing and understanding. That’s Unknown No. 3: how quickly AIs will be able to create reliable software updates for the vulnerabilities they find, and how quickly customers can update their systems.

Today, there is a time lag between when a vendor issues a patch and customers install that update. That time lag is even longer for large organizational software; the risk of an update breaking the underlying software system is just too great for organizations to roll out updates without testing them first. But if AI can help speed up that process, by writing patches faster and more reliably, and by testing them in some AI-generated twin environment, the advantage goes to the defender. If not, the attacker will still have a window to attack systems until a vulnerability is patched.

## Toward self-healing

In a truly optimistic future, we can imagine a self-healing network. AI agents continuously scan the ever-evolving corpus of commercial and custom AI-generated software for vulnerabilities, and automatically patch them on discovery.

For that to work, software license agreements will need to change. Right now, software vendors control the cadence of security patches. Giving software purchasers this ability has implications about compatibility, the right to repair, and liability. Any solutions here are the realm of policy, not tech.

If the defense can find, but can’t reliably patch, flaws in legacy software, that’s where attackers will focus their efforts. If that’s the case, we can imagine a continuously evolving AI-powered intrusion detection, continuously scanning inputs and blocking malicious attacks before they get to vulnerable software. Not as transformative as automatically patching vulnerabilities in running code, but nevertheless valuable.

The power of these defensive AI systems increases if they are able to coordinate with each other, and share vulnerabilities and updates. A discovery by one AI can quickly spread to everyone using the affected software. Again: Advantage defender.

There are other variables to consider. The relative success of attackers and defenders also depends on how plentiful vulnerabilities are, how easy they are to find, whether AIs will be able to find the more subtle and obscure vulnerabilities, and how much coordination there is among different attackers. All this comprises Unknown No. 4.

## Vulnerability economics

Presumably, AIs will clean up the obvious stuff first, which means that any remaining vulnerabilities will be subtle. Finding them will take AI computing resources. In the optimistic scenario, defenders pool resources through information sharing, effectively amortizing the cost of defense. If information sharing doesn’t work for some reason, defense becomes much more expensive, as individual defenders will need to do their own research. But instant software means much more diversity in code: an advantage to the defender.

This needs to be balanced with the relative cost of attackers finding vulnerabilities. Attackers already have an inherent way to amortize the costs of finding a new vulnerability and create a new exploit. They can vulnerability hunt cross-platform, cross-vendor, and cross-system, and can use what they find to attack multiple targets simultaneously. Fixing a common vulnerability often requires cooperation among all the relevant platforms, vendors, and systems. Again, instant software is an advantage to the defender.

But those hard-to-find vulnerabilities become more valuable. Attackers will attempt to do what the major intelligence agencies do today: find “
[nobody but us](https://en.wikipedia.org/wiki/NOBUS)
” zero-day exploits. They will either use them slowly and sparingly to minimize detection or quickly and broadly to maximize profit before they’re patched. Meanwhile, defenders will be both vulnerability hunting and intrusion detecting, with the goal of patching vulnerabilities before the attackers find them.

We can even imagine a market for vulnerability sharing, where the defender who finds a vulnerability and creates a patch is compensated by everyone else in the information-sharing/repair network. This might be a stretch, but maybe.

## Up the stack

Even in the most optimistic future, attackers aren’t going to just give up. They will attack the non-software parts of the system, such as the users. Or they’re going to look for
[loopholes](https://www.schneier.com/wp-content/uploads/2021/04/The-Coming-AI-Hackers.pdf)
in the system: things that the system technically allows but were unintended and unanticipated by the designers—whether human or AI—and can be used by attackers to their advantage.

What’s left in this world are attacks that don’t depend on finding and exploiting software vulnerabilities, like social engineering and credential stealing attacks. And we have already seen how AI-generated deepfakes make social engineering easier. But here, too, we can imagine defensive AI agents that monitor users’ behaviors, watching for signs of attack. This is another AI use case, and one that I’m not even sure how to think about in terms of the attacker/defender arms race. But at least we’re pushing attacks up the stack.

Also, attackers will attempt to infiltrate and influence defensive AIs and the networks they use to communicate, poisoning their output and degrading their capabilities. AI systems are vulnerable to all sorts of manipulations, such as prompt injection, and it’s unclear whether we will
[ever be able](https://spectrum.ieee.org/prompt-injection-attack)
to solve that. This is Unknown No. 5, and it’s a biggie. There might always be a “
[trusting trust problem](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf)
.”

No future is guaranteed. We truly don’t know whether these technologies will continue to improve and when they will plateau. But given the pace at which AI software development has improved in just the past few months, we need to start thinking about how cybersecurity works in this instant software world.

*This essay originally appeared in
[CSO](https://www.csoonline.com/article/4152133/cybersecurity-in-the-age-of-instant-software.html)
.*

EDITED TO ADD:
[Two](https://sockpuppet.org/blog/2026/03/30/vulnerability-research-is-cooked/)
[essays](https://lwn.net/Articles/1065620/)
published after I wrote this. Both are good illustrations of where we are re AI vulnerability discovery. Things are changing very fast.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[computer security](https://www.schneier.com/tag/computer-security/)
,
[cybersecurity](https://www.schneier.com/tag/cybersecurity/)
,
[LLM](https://www.schneier.com/tag/llm/)
,
[patching](https://www.schneier.com/tag/patching/)
,
[vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on April 7, 2026 at 1:07 PM](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html)
•
[3 Comments](https://www.schneier.com/blog/archives/2026/04/cybersecurity-in-the-age-of-instant-software.html#comments)