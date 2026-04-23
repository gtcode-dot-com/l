---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T12:15:13.465015+00:00'
exported_at: '2026-04-23T12:15:16.741849+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html
structured_data:
  about: []
  author: ''
  description: Mythos found decades-old vulnerabilities, yet fewer than 1% were patched,
    exposing a remediation gap.
  headline: Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/project-glasswing-proved-ai-can-find.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Project Glasswing Proved AI Can Find the Bugs. Who's Going to Fix Them?
updated_at: '2026-04-23T12:15:13.465015+00:00'
url_hash: 14b31915839958589c775873e38f9b3081a3ae0a
---

Last week, Anthropic announced Project Glasswing, an AI model so effective at discovering software vulnerabilities that they took the extraordinary step of postponing its public release. Instead, the company has given access to Apple, Microsoft, Google, Amazon, and a coalition of others to
**find and patch bugs before adversaries can**
.

Mythos Preview, the model that led to Project Glasswing,
**found vulnerabilities across every major operating system and browser.**
Some of these bugs had survived decades of human audits, aggressive fuzzing, and open-source scrutiny. One had been
**sitting for 27 years**
in
[OpenBSD,](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
generally considered to be one of the world’s most secure operating systems.

It's tempting to file this under "
**AI lab says their AI is too dangerous,**
" the same playbook OpenAI ran with GPT-2.

Not so fast; there's a material difference this time.

Mythos didn't just find individual CVEs.

* It
  **chained four independent bugs into an exploit sequence**
  that bypassed both the browser renderer and the OS sandboxing
* It performed local privilege escalation in Linux through race conditions
* It built a 20-gadget ROP chain targeting FreeBSD's NFS server, distributed across packets.

Claude Opus 4.6, Anthropic's previous frontier model, failed at autonomous exploit development almost entirely.
**Mythos hit a 72.4% success rate in the Firefox JS shell**
.

This isn't theoretical, nor some new three-to-five-year prediction. This is about to be a real-world engineering reality.

## **Why Project Glasswing Exposes the Real Cybersecurity Gap**

Here's the number that should keep security leaders awake at night:
**fewer than 1% of the vulnerabilities found by Mythos were patched**
.

Let that sink in for a moment.

The most powerful vulnerability discovery engine ever built ran against the world's most critical software, and the ecosystem couldn't absorb the output.

Glasswing solved the finding problem.

Nobody solved the problem of fixing.

### **Why Defenders Can't Keep Up: Calendar Speed vs. Machine Speed**

This is the structural issue the cybersecurity industry has been circling for years. AI just made it impossible to ignore.

Defenders operate on
**calendar speed**
. They:

* Gather intelligence
* Build a campaign
* Simulate the threats
* Mitigate
* Repeat

That cycle takes about
**four days on a good day**
. Attackers, especially those now leveraging LLMs at every stage of their operation, are
**moving at machine speed**
.

For an up-to-the-minute take, David B. Cross, CISO at Atlassian, will be speaking at the
[Autonomous Validation Summit on May 12](https://hubs.li/Q04cJdmF0)
about what this looks like from the inside, why periodic testing can't keep pace with adversaries that operate autonomously, and what defenders should be doing instead.

### **AI-Powered Attacks Are Already Autonomous**

Earlier this year, a threat actor deployed
**a custom MCP server hosting an LLM as part of their attack chain**
against FortiGate appliances.

The AI handled everything:

* Automated backdoor creation
* Internal infrastructure mapping fed directly to the model
* Autonomous vulnerability assessment, and
* AI-prioritized execution of offensive tools for domain admin access.

The result?
**2,516 organizations across 106 countries were compromised**
in parallel. The entire chain, from initial access through credential dumping to data exfiltration, was autonomous. The only human involvement was reviewing the results afterward.

### **AI-based Vulnerability Discovery Is Outpacing Remediation**

The gap between attacker speed and defender speed isn't new.

**What's new is that a small but worrisome gap just became a canyon.**

* Autonomous systems like AISLE
  [discovered](https://aisle.com/blog/aisle-discovered-12-out-of-12-openssl-vulnerabilities)
  13 out of 14 OpenSSL CVEs in recent coordinated releases, bugs that had survived years of human review.
* XBOW became the
  [top-ranked](https://xbow.com/blog/top-1-how-xbow-did-it)
  hacker on HackerOne in 2025, surpassing all human participants.
* The median time from disclosure to weaponized exploit
  [dropped](https://www.resilientcyber.io/p/the-zero-day-clock-is-ticking-why)
  from 771 days in 2018 to single-digit hours by 2024.
* By 2025, the majority of exploits will be weaponized
  *before*
  being publicly disclosed.

**Now add Mythos-class discovery to this picture.**

You don't get a safer world automatically. You get a
**tsunami of legitimate findings that still require human verification**
, organizational process, business continuity considerations, and patch cycles that haven't fundamentally changed in a decade.

## **How to Build a Mythos-Ready Security Program**

The instinct after Glasswing is to ask: "How do we find more bugs?"

That's actually the wrong question.

The right one is: "When thousands of exploitable vulnerabilities land on your desk tomorrow morning,
**can your program actually process them?**
"

For most organizations, the honest answer is no. And the reason isn't a lack of tools or talent; it's a structural
**dependency on periodic**
,
**human-initiated processes**
that were designed for a world where vulnerabilities trickled in, not one where they arrived in a tsunami.

We can't fix every vulnerability. We can't apply every hardening option.

> **That's not defeatism**
> , that’s the pragmatic starting point for any security program that actually works. The question that matters isn't "is this CVE critical?" but "
> **is this vulnerability exploitable in my environment, right now, given what I have deployed?**
> "

[A Mythos-ready security program](https://www.picussecurity.com/resource/report/surviving-the-post-mythos-era-12-actions-to-validate-your-defenses-before-july)
needs three fundamental pieces.

### **First: Signal-Driven Validation Over Scheduled Testing**

When a new threat emerges, when an asset changes, or when a configuration drifts, defenses need to be
**tested against that specific change in that moment.**
Not during the next quarterly pentest. Not when someone can find an open calendar slot.

The entire concept of "scheduled validation" assumes a stable threat landscape, and today, that
**assumption is dead on arrival**
.

### **Second: Environment-Specific Context Over Generic CVSS Scores**

Glasswing will produce an avalanche of CVEs.

Yet most vulnerability management programs are still prioritized by CVSS scores. This context-free metric tells you how bad a bug
*could be in theory*
, not whether
*it's exploitable in your specific infrastructure*
, given your controls and business risk.

When the volume of findings suddenly goes from
**hundreds to thousands**
, context-free prioritization won't just slow you down;
**it’ll break your process entirely**
.

### **Third: Closed-Loop Remediation Without a Manual Handoff**

The current model can’t survive in a world where adversaries exploit CVEs within hours of disclosure. You know the drill:

* Scanner finds a bug
* Analyst triages it
* The ticket goes to a different team
* Someone patches it weeks later
* Nobody re-validates

That chain of manual handoffs is exactly where the system disintegrates. If the cycle from finding to fix to re-validation can't run without humans shuttling tickets between queues, it clearly isn’t running anywhere near machine speed.

This isn't about buying more tools. It's about defenders leveraging their
**one asymmetric advantage**
: you know your organization’s topology,
**attackers don't**
.

That's a significant advantage,
**but only if you can act on it at machine speed.**

## **How Autonomous Exposure Validation Closes the Gap — and Where Picus Comes in**

This is the part where I’m going to be really transparent about who's writing this.

At Picus Security, we build a platform for
**Autonomous Exposure Validation**
. So, full disclosure, I have a perspective here that comes with an inherent bias. Take it accordingly.

What Glasswing crystallized for us, and for a lot of the CISOs we've been speaking with, is that the
**validation step**
within any
**exposure management program**
just became the most critical bottleneck.

* Finding vulnerabilities is about to get radically easier and more efficient
* Patching them is going to remain painfully slow.

The only lever you can pull in between is
**knowing which ones actually matter**
to your environment. That's validation.

### **From Four Days to Three Minutes: How Agentic Workflows Change the Cycle**

We built Picus Swarm, the AI team powering autonomous, real-time validation, to compress the traditional four-day cycle into minutes.

It's a set of AI agents that work together to do what used to require handoffs between four separate teams:

* A
  **researcher agent**
  ingests and vets threat intelligence.
* A
  **red teamer agent**
  maps it against your environment to generate a safety-checked attacker playbook.
* A
  **simulator agent**
  executes across your actual endpoints and cloud, gathering telemetry and proof data.
* A
  **coordinator agent**
  bridges findings to remediation, opening tickets, triggering SOAR playbooks, pushing indicators of attack to your EDR, and re-validating after fixes land.

Every action is traceable and auditable, andevery agent operates within guardrails you define.

The whole chain, from a new CISA alert to validated, remediation-ready findings, runs in about three minutes.

> When a
> **Mythos-class model drops thousands of findings**
> on your organization, you need something that can immediately tell you
> **which of these are exploitable in your environment.**
> Which controls would hold, which would fail, and what's the vendor-specific fix?

## **The Uncomfortable Truth**

Project Glasswing is going to be measured by one metric: how many vulnerabilities get patched before they get exploited. Not how many are found, not how impressive the exploit chains are, but whether the ecosystem can digest what AI is about to produce.

Visibility alone has never been enough, 83% of cybersecurity programs still show no measurable results. What’s changing the equation is
**closing the gap between seeing and proving:**
knowing whether a potential vulnerability
**would actually compromise your environment.**

That's validation.

And in a post-Glasswing world, it's the only thing standing between a flood of discoveries and a flood of breaches.

*We're hosting the Autonomous Validation Summit on May 12 & 14 with Frost & Sullivan, featuring practitioners from Kraft Heinz and Glow Financial Services, along with our CTO, Volkan Erturk. Together, we’ll be taking a deeper dive into this specific problem.*

*[>> Register here.](https://hubs.li/Q04cJdmF0)*

*Note: This article was written by
[Sıla Özeren Hacıoğlu](https://www.linkedin.com/in/silaozeren/)
, Security Research Engineer at Picus Security.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.