---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T19:51:46.439978+00:00'
exported_at: '2026-06-11T19:51:49.974899+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
structured_data:
  about: []
  author: ''
  description: OpenClaw input flaws let hidden contacts and phishing emails trigger
    code execution and data leaks, exposing agent trust risks.
  headline: New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/new-attacks-trick-openclaw-ai-agent.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Attacks Trick OpenClaw AI Agent Into Running Code and Leaking Secrets
updated_at: '2026-06-11T19:51:46.439978+00:00'
url_hash: 11b624bb99a974df5c15e2326d3ee58261efbd7b
---

Two security teams have shown, in separate research published this week, that
[OpenClaw](https://github.com/openclaw/openclaw)
, the popular self-hosted AI agent, can be driven to run attacker-controlled code or hand over sensitive data through ordinary-looking inputs.

[Imperva](https://www.imperva.com/blog/compromise-openclaw-with-prompt-injections-in-message-objects/)
buried instructions inside shared contacts, vCards, and location pins that the agent executed without the victim ever seeing them.
[Varonis](https://www.varonis.com/blog/openclaw-phishing)
built a test agent on the platform, gave it a mailbox full of synthetic business data, and watched a single plain email talk it into forwarding mock AWS keys and a fake customer export to an outside address.

The flaw Imperva found is patched in OpenClaw 2026.4.23, so update if you run it. The phishing weakness Varonis found is not something a patch fixes; it comes down to limiting what the agent can do on its own.

Different doors into the same room: the agent trusts what reaches it, and its access becomes the attacker's.

## Hidden commands in a shared contact

Imperva researcher Yohann Sillam looked at how OpenClaw hands messaging data to the model behind it. The problem is in the plumbing.

When the agent passes a shared contact, vCard, or location to the LLM, it flattens the object into the prompt text inline, with no boundary marking it as untrusted. The content the agent fetches from the web gets wrapped in an untrusted-content marker. Message objects do not.

Only some fields travel to the model, and that is what the attack abuses. A shared contact sends just the name field, serialized as &lt;contact: name, number&gt;. The angle brackets are legal in a name, so the model cannot tell where the real name ends and an injected instruction begins. The contact name is truncated where it shows on screen, both on WhatsApp and in the receiving app, so the victim does not see the payload either.

The same trick works through a vCard's full-name field, which WhatsApp supports natively, and through the label on a shared location pin.

In Imperva's tests against Gemini 3.1 Pro (preview build), the hidden text told the agent to download and run a script from a server the researchers controlled. It did. A plain image with instructions buried in it failed, likely because that attack has been reported so often that models are now trained to resist it; the message-object route worked because models have seen far fewer examples of it.

With OpenClaw's memory on by default, Imperva warns, a single piece of widely shared content carrying a hidden instruction could quietly compromise the agents that ingest it, if they are not sandboxed.

Imperva disclosed the issue, and OpenClaw shipped a fix in version 2026.4.23 that moves contact names, vCard fields, and location labels out of the prompt body and into a separate untrusted-metadata channel. Imperva found the same flattening pattern in other personal AI assistants, so the underlying problem is not OpenClaw's alone.

## A normal email is enough

Varonis Threat Labs came at OpenClaw from the social angle. In research led by Itay Yashar, the team built an agent called
**Pinchy**
on the platform, wired it to a Gmail inbox stocked with realistic but synthetic business clutter and mock secrets, and ran it through four phishing simulations on Google Gemini 3.1 Pro and OpenAI Codex GPT-5.4.

They draw a line between prompt injection, which hides instructions in data, and what they call agent phishing: a believable request that arrives through a normal channel and works because the agent acts before checking who sent it.

The agent failed both exfiltration tests. In the first, a message posing as a team lead named Dan, sent from an outside Gmail address, asked for staging access during a fake production incident. Pinchy found the credentials and forwarded mock AWS IAM access keys, database connection strings, and SSH credentials in plaintext.

The second pretext was softer: a routine-sounding request for the weekly customer export, supposedly for a QBR deck. The agent shipped out a synthetic dataset of 247 enterprise customers, contacts, and contract values included. Both failures happened under a strict profile that told the agent to verify senders first. The rule existed. Urgency beat it once, routine beat it the second time.

The agent did better when the threat was technical rather than social. It interacted with a gift-card phishing page but withheld real credentials and eventually flagged it; the strict profile blocked the page outright. On a malicious OAuth consent screen dressed up as a timesheet app, it inspected the redirect target, judged it suspicious, and stopped before granting access.

That is the split Varonis draws out: the agent is better than many people at spotting bad URLs and fake login portals, and worse at the social judgment that makes a human pause when a colleague suddenly asks for credentials at an odd hour. The drive to be helpful is the attack surface.

Varonis says OpenAI Codex GPT-5.4 was more cautious than Gemini 3.1 Pro about entering or sending data to outside sites without confirmation, but both fell for the social pretexts.

## The weak spot behind both attacks

Varonis maps both attacks onto what Simon Willison calls the
[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
: an agent that can read private data, take in untrusted content, and send data back out. OpenClaw has all three, which is why a poisoned contact and a friendly email end in the same place.

That trust boundary is not only a prompt problem; it shows up in OpenClaw's code as well. A separate
[InfoSec Write-ups analysis](https://infosecwriteups.com/one-agent-five-zero-days-turning-past-cves-into-sast-rules-650c32b20032)
turned OpenClaw's past advisories into static-analysis rules, then used them to find five more flaws across the Slack, Discord, Matrix, Zalo, and Microsoft Teams channel extensions.

All five were the same bug: the startup code resolved each channel's allowlist by mutable display name instead of a stable ID, so an attacker who renamed themselves to match an allowed user could slip onto the list and steer the agent. OpenClaw has patched them.

OpenClaw ships with broad access to files, shells, and more than twenty messaging platforms, and it has drawn a steady run of
[earlier prompt-injection and data-exfiltration warnings](https://thehackernews.com/2026/03/openclaw-ai-agent-flaws-could-enable.html)
since it launched late last year.

The Dutch data protection authority took the strongest line: the
[Autoriteit Persoonsgegevens](https://www.autoriteitpersoonsgegevens.nl/en/current/ap-warns-of-major-security-risks-with-ai-agents-like-openclaw)
told users and organisations not to run OpenClaw on systems that hold sensitive data, citing data-breach and account-takeover risks.

## What to do about it

Anyone running OpenClaw should update to 2026.4.23 or later for the message-object fix. The rest is architecture, not prompt wording, and Varonis lays out four controls.

Treat the agent's instruction file as an enforced, version-controlled policy, not a suggestion. Outbound mail needs a gate: no first-time sends to unfamiliar addresses without approval, so a hijacked agent cannot relay phishing from a trusted account. Connector access should track the trust level of whatever triggered the task, so an inbox handling outside email cannot also read the whole CRM. And the riskiest actions, forwarding credentials or moving money, should wait for a human.

Both teams land on the same mental model. Varonis frames it as treating the agent like a junior employee with system access and no instinct for what looks off, not as a security tool. Imperva gets there from the other direction, calling it an authenticated executor that trusts its inputs.

The fixes on offer today are specific patches and guardrails. The harder problem is still open. An agent useful enough to act on your email and run your commands is, by design, one that trusts input and wants to help, and nobody has a general fix for that yet.