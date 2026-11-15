---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T02:41:04.445497+00:00'
exported_at: '2026-11-15T02:41:06.803086+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/openai-says-new-gpt-6-cyber-model-hunts-flaws-without-crossing-the-line
structured_data:
  about: []
  author: ''
  description: GPT-6 Cyber scored 48.5% on ExploitGym, found 81 high-severity Firefox
    flaws and stayed in scope 99.93% of the time in OpenAI’s tests.
  headline: OpenAI Says New GPT-6 Cyber Model Hunts Flaws Without Crossing the Line
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/openai-says-new-gpt-6-cyber-model-hunts-flaws-without-crossing-the-line
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Says New GPT-6 Cyber Model Hunts Flaws Without Crossing the Line
updated_at: '2026-11-15T02:41:04.445497+00:00'
url_hash: c8d137c916001a924516e4255d24492586a99a12
---

**OpenAI on Thursday unveiled GPT-6 Cyber, a security model the company says is far more capable than its predecessor and more disciplined about respecting the limits researchers set for it.**

On ExploitGym, which checks whether an AI can exploit a given flaw in a remote target, the new model achieved 48.5%, up from 32.1% for GPT-5.6 Cyber.

OpenAI rated
[GPT-6 Cyber](https://openai.com/index/introducing-gpt-6-cyber/)
as Critical for cybersecurity under its Preparedness Framework, above the High designation given to GPT-5.6 Cyber.

In one alignment test, the model received an exploitation task alongside supporting services that were intentionally easy to hack but off-limits. Without deployment safety prompts, it refrained from exploiting them in 99.93% of cases, compared to 94.49% for GPT-5.6 Cyber. With the safety prompts, it never targeted the decoy services.

“This improvement in alignment reflects dedicated training to stay within authorized scope, respect restrictions, and report results accurately,” OpenAI said.

OpenAI researchers pointed the model at the Linux kernel, where it reproduced 1,724 vulnerabilities and built
[functional privilege escalation exploits for 948](https://www.securityweek.com/ai-agents-got-root-on-linux-via-948-kernel-flaws-in-openai-research/)
. GPT-5.6 Sol, tested with the same tooling, produced 166.

Advertisement. Scroll to continue reading.

OpenAI has reported 304 critical issues to maintainers with proposed fixes.

In Firefox, the model documented 81 new flaws that Mozilla deemed high severity, backing each with evidence and reproducible tests. Mozilla has begun rolling out patches.

New protections include monitoring that checks whether the model’s actions line up with what a user is permitted to do, and safeguards meant to stop OpenAI’s models from aiding efforts to compromise industrial controls and other safety-critical systems.

OpenAI refined these safeguards using feedback from industrial cybersecurity firm Dragos, which tested
[Daybreak Red](https://www.securityweek.com/openai-pledges-1-billion-to-bring-frontier-ai-to-critical-infrastructure-defenders/)
models in a controlled lab.

“The skill floor is dropping for the reconnaissance and vulnerability research needed before an attack,” said Dragos chief AI officer Rob T. Lee.

Access is currently limited to select approved customers of Daybreak Red, the part of OpenAI’s Daybreak program aimed at advanced exploit work and authorized testing. They can use GPT-6 Cyber through the API and Codex.

OpenAI plans to gradually open the model to all Daybreak Red customers, who are also getting GPT-5.6 Cyber. A dedicated Daybreak Red group for approved critical infrastructure defenders will permit sanctioned testing of critical systems.

**Related**
:
[OpenAI Finds GPT-6 Astra Quietly Holding Back on Internal Red-Teaming, Exploit Tasks](https://www.securityweek.com/openai-finds-gpt-6-astra-quietly-holding-back-on-internal-red-teaming-exploit-tasks/)

**Related**
:
[Meta Shares Top Muse Bug Bounty Findings as Payouts Reach $1.2 Million](https://www.securityweek.com/meta-shares-top-muse-bug-bounty-findings-as-payouts-reach-1-2-million/)

**Related**
:
[Google Touts Powerful Cybersecurity Capabilities in Gemini 4 Carbon Model](https://www.securityweek.com/google-says-gemini-4-carbon-leads-in-finding-exploiting-and-fixing-vulnerabilities/)