---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-11T18:15:14.535583+00:00'
exported_at: '2026-03-11T18:15:16.910659+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/researchers-trick-perplexitys-comet-ai.html
structured_data:
  about: []
  author: ''
  description: Researchers show GAN-trained phishing pages can trick Perplexity’s
    Comet AI browser in under four minutes, exposing a new AI-targeted attack surface.
  headline: Researchers Trick Perplexity's Comet AI Browser Into Phishing Scam in
    Under Four Minutes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/researchers-trick-perplexitys-comet-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Researchers Trick Perplexity's Comet AI Browser Into Phishing Scam in Under
  Four Minutes
updated_at: '2026-03-11T18:15:14.535583+00:00'
url_hash: 7e18efe30bb766d86b4e9a71a81768030b955b9c
---

**

Ravie Lakshmanan
**

Mar 11, 2026

Artificial Intelligence / Browser Security

Agentic web browsers that leverage artificial intelligence (AI) capabilities to autonomously execute actions across multiple websites on behalf of a user could be trained and tricked into falling prey to phishing and scam traps.

The attack, at its core, takes advantage of AI browsers' tendency to reason their actions and use it against the model itself to lower their security guardrails, Guardio
[said](https://guard.io/labs/agenticblabbering---how-ai-browsers-verbose-reasoning-fuels-the-ultimate-scamming-machine)
in a report shared with The Hacker News ahead of publication.

"The AI now operates in real time, inside messy and dynamic pages, while continuously requesting information, making decisions, and narrating its actions along the way. Well, 'narrating' is quite an understatement - It blabbers, and way too much!," security researcher Shaked Chen said.

"This is what we call
**Agentic Blabbering**
: the AI Browser exposing what it sees, what it believes is happening, what it plans to do next, and what signals it considers suspicious or safe."

By intercepting this traffic between the browser and the AI services running on the vendor's servers and feeding it as input to a Generative Adversarial Network (
[GAN](https://en.wikipedia.org/wiki/Generative_adversarial_network)
), Guardio said it was able to make Perplexity's Comet AI browser fall victim to a phishing scam in under four minutes.

The research builds on prior techniques like
[VibeScamming](https://thehackernews.com/2025/04/lovable-ai-found-most-vulnerable-to.html)
and
[Scamlexity](https://thehackernews.com/2025/08/experts-find-ai-browsers-can-be-tricked.html)
, which found that vibe-coding platforms and AI browsers could be coaxed into generating scam pages or carrying out malicious actions via hidden prompt injections. In other words, with the AI agent handling the tasks without constant human supervision, there arises a shift in the attack surface wherein a scam no longer has to deceive a user. Rather, it aims to trick the AI model itself.

"If you can observe what the agent flags as suspicious, hesitates on, and more importantly, what it thinks and blabbers about the page, you can use that as a training signal," Chen explained. "The scam evolves until the AI Browser reliably walks into the trap another AI set for it."

The idea, in a nutshell, is to build a "scamming machine" that iteratively optimizes and regenerates a phishing page until the agentic browser stops complaining and proceeds to carry out the threat actor's bidding, such as entering a victim's credentials on a bogus web page designed for carrying out a refund scam.

What makes this attack interesting and dangerous is that once the fraudster iterates on a web page until it works against a specific AI browser, it works on all users who rely on the same agent. Put differently, the target has shifted from the human user to the AI browser.

"This reveals the unfortunate near future we are facing: scams will not just be launched and adjusted in the wild, they will be trained offline, against the exact model millions rely on, until they work flawlessly on first contact," Guardio said. "Because when your AI Browser explains why it stopped, it teaches attackers how to bypass it."

The disclosure comes as Trail of Bits
[demonstrated](https://blog.trailofbits.com/2026/02/20/using-threat-modeling-and-prompt-injection-to-audit-comet/)
four
[prompt injection techniques](https://arxiv.org/abs/2511.20597)
against the Comet browser to extract users' private information from services like Gmail by exploiting the browser's AI assistant and exfiltrating the data to an attacker’s server when the user asks to summarize a web page under their control.

Last week, Zenity Labs also detailed two zero-click attacks affecting Perplexity's Comet that use
[indirect prompt injection](https://thehackernews.com/2025/12/google-adds-layered-defenses-to-chrome.html)
seeded within meeting invites to exfiltrate local files to an external server (aka
[PerplexedComet](https://labs.zenity.io/p/perplexedbrowser-perplexity-s-agent-browser-can-leak-your-personal-pc-local-files)
) or
[hijack a user's 1Password account](https://labs.zenity.io/p/perplexedbrowser-how-attackers-can-weaponize-comet-to-takeover-your-1password-vault)
if the
[password manager extension](https://1password.com/blog/security-advisory-for-ai-assisted-browsing-with-the-1password-browser)
is installed and unlocked. The issues, collectively codenamed PerplexedBrowser, have since been addressed by the AI company.

This is achieved by means of a prompt injection technique referred to as intent collision, which occurs "when the agent merges a benign user request with attacker-controlled instructions from untrusted web data into a single execution plan, without a reliable way to distinguish between the two," security researcher Stav Cohen said.

Prompt injection attacks remain a fundamental security challenge for large language models (LLMs) and for integrating them into organizational workflows, largely because completely eliminating these vulnerabilities may not be feasible. In December 2025, OpenAI
[noted](https://thehackernews.com/2026/01/weekly-recap-iot-exploits-wallet.html#:~:text=OpenAI%20Says%20Prompt%20Injections%20May%20Never%20Go%20Away%20in%20Browser%20Agents)
that such weaknesses are "unlikely to ever" be fully resolved in agentic browsers, although the associated risks could be reduced through automated attack discovery, adversarial training, and new system-level safeguards.