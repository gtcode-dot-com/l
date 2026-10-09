---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T02:09:01.047166+00:00'
exported_at: '2026-06-11T02:09:05.964961+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html
structured_data:
  about: []
  author: ''
  description: Anthropic split Fable 5 and Mythos 5 by cyber safeguards, giving vetted
    defenders stronger capabilities while limiting public misuse.
  headline: Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber
    Safeguards
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/anthropic-releases-claude-fable-5-its.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Anthropic Releases Claude Fable 5, Its Most Powerful AI Yet, With Cyber Safeguards
updated_at: '2026-06-11T02:09:01.047166+00:00'
url_hash: 10bc727f9c093aec7ffe937cbdf90a15dde3ec02
---

On June 9, Anthropic
[released Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)
, the most capable model it has ever made, generally available. It also did something unusual: it shipped one model as two products, split not by capability but by a layer of safety classifiers.

Fable 5 goes to the public. Its twin, Claude Mythos 5, the same underlying model with the cyber safeguards lifted, stays locked to a vetted group of cyber defenders and critical infrastructure operators.

Anthropic calls Mythos 5 the strongest cybersecurity model in the world.

The practical difference is this: Fable 5 routes flagged cyber, biology, chemistry, and distillation requests to the weaker Claude Opus 4.8, while Mythos 5 keeps the cyber capabilities available for vetted users. Both models cost $10 per million input tokens and $50 per million output tokens, less than half the price of the earlier Mythos Preview, and Fable 5 is available through the Claude API now.

It is included on Pro, Max, Team, and seat-based Enterprise plans at no extra cost through June 22, then moves to usage credits.

## How Fable 5's cyber classifiers work

The split exists because Mythos-class models find and exploit software vulnerabilities well enough that, in Anthropic's framing, handing that capability to the general public without controls would give attackers serious uplift.

The mechanism is a set of
[classifiers](https://www.anthropic.com/news/claude-fable-5-mythos-5)
: separate AI systems that watch for misuse and jailbreak attempts. When a request trips one, Fable 5 does not refuse. The response is handed to Opus 4.8, and the user is told the handoff happened. Of the flagged categories, distillation is the odd one out: it means extracting a model's capabilities to train a competing model, which Anthropic blocks to stop near-frontier abilities leaking out without safeguards attached.

The cybersecurity classifier is the broad one. Anthropic designed it to block not just exploit development but offensive cyber tasks in general: reconnaissance, discovery, lateral movement, the agentic steps that make up a real attack.

In an internal evaluation run with Fable 5 set to block rather than fall back, and which did not attempt to evade the safeguards, the classifiers stopped the model from making any progress on those tasks. One external partner found Fable 5 complied with zero harmful single-turn requests on cyberattack planning, exploit development, or defense evasion, holding up against 30 different public jailbreak techniques.

The trade-off is false positives. Anthropic tuned the safeguards conservatively to ship fast, so they sometimes catch harmless requests. The company says fallback fires in under 5% of all sessions, so for more than 95%, Fable 5 behaves like the cyber-unrestricted Mythos 5. That figure covers every fallback, genuine blocks included, so it caps the total disruption rather than measuring the false-positive rate on its own. Anthropic says it will narrow the safeguards and cut false positives after launch.

On robustness, the numbers are specific. An external bug bounty ran over 1,000 hours and produced no universal jailbreak, a prompt, or a harness that strips the safeguards wholesale. External red teams found none on long-form agentic tasks either, with one caveat Anthropic states plainly: the UK's AI Security Institute made progress toward a universal jailbreak within a brief initial testing window. Anthropic concedes it is likely impossible to fully prevent universal jailbreaks, and its stated goal is to make any that remain slow and costly enough to catch before they are used at scale.

## Why is the capability a threat

The case for treating this model carefully was laid out in April, when Anthropic released
[Claude Mythos Preview](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
to a limited group through
[Project Glasswing](https://www.anthropic.com/glasswing)
. The
[technical write-up](https://red.anthropic.com/2026/mythos-preview/)
from Anthropic's red team is the part worth reading.

During testing, Mythos Preview identified and exploited zero-day vulnerabilities in every major operating system and every major web browser when a user directed it to. The oldest bug it found was a 27-year-old flaw in OpenBSD, an operating system known mainly for its security. It autonomously wrote a remote code execution exploit against FreeBSD's NFS server from a 17-year-old bug, triaged as
[CVE-2026-4747](https://nvd.nist.gov/vuln/detail/CVE-2026-4747)
.

Anthropic describes the result as full root for an unauthenticated attacker from anywhere on the internet; NVD's entry is more measured, noting the stack overflow itself does not require the client to authenticate, but frames kernel code execution as reachable by an attacker able to send packets to the NFS server while the kgssapi.ko module is loaded.

By Anthropic's own account, it did not explicitly train these capabilities in; they emerged as a side effect of general improvements in code, reasoning, and autonomy, the same gains that make the model better at patching. The red team's flat warning: mitigations whose security value comes from friction rather than hard barriers get much weaker against a model that grinds through tedious exploitation steps at scale.

Hard technical barriers like KASLR and W^X still raise the cost; the warning is narrower, aimed at defenses that lean on attacker patience or manual effort, and the model can now supply itself.

Mythos 5 carries those skills forward. Anthropic says users will find it comparable to or somewhat stronger than Mythos Preview.

## The defender's actual problem

The defensive case is not hypothetical. In the first weeks of Project Glasswing, Anthropic and roughly 50 partners
[used Mythos Preview to find more than ten thousand](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html)
high- or critical-severity vulnerabilities in systemically important software.

Cloudflare alone found 2,000 bugs, 400 of them high- or critical-severity. Mozilla found and fixed 271 in Firefox 150, more than ten times what it caught in Firefox 148 using the older Opus 4.6. Anthropic says the same pressure is visible beyond Glasswing, in vendors shipping unusually large security releases.

That flood is the catch. Finding bugs is now cheap and fast. Verifying, triaging, and patching them is not, and it still runs on human time.

Anthropic reports that open-source maintainers, already buried under low-quality AI-generated bug reports, have asked it to slow its disclosures because they cannot write patches fast enough. In Glasswing, it says a high- or critical-severity bug found by the model takes about two weeks to patch on average.

The bottleneck has moved from discovery to the fix, and the gap between a public disclosure and a deployed patch is where attackers live. The red team's N-day experiments sharpen the point: starting from nothing but a disclosed CVE and its patch, Mythos Preview built working Linux privilege-escalation exploits in under a day each, at a few thousand dollars or less in compute.

For defenders, the read is the same as ever, just on a shorter clock: assume a high-severity CVE can become a working exploit within hours of disclosure, not weeks. That means prioritizing auto-update paths for internet-facing systems and treating dependency bumps that carry CVE fixes as time-sensitive work rather than backlog.

MFA and comprehensive logging stay the baseline, so a single missed patch does not become the only thing standing between an attacker and the network. Anthropic has opened a
[Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude)
that lets vetted security professionals use its models for legitimate offensive work without the cyber safeguards.

## A new 30-day data retention requirement

Anthropic is also changing how it handles data for Mythos-class models.

It will require 30-day retention for all traffic on Fable 5, Mythos 5, and future models at this capability level, across both first- and third-party surfaces. The company says it will not use the data for training or any non-safety purpose, will log all human access, and will delete it after 30 days except where a safety investigation or legal obligation requires holding it longer.

The stated reason is defensive: the data helps detect novel attacks and jailbreaks that operate across many requests. Teams with strict data-handling requirements will want to factor that retention window in before routing sensitive traffic through these models.

Anthropic plans to widen Mythos 5 access through a trusted-access program, and says that once compute capacity catches up, it aims to fold Fable 5 back into subscription plans without the usage-credit premium that kicks in after June 22.

The larger question the launch raises is the one Anthropic has been circling since April: similarly capable models from other labs are coming, and not all of them will ship with a wall of classifiers in front. The defensive head start Glasswing was meant to buy only matters if the rest of the industry uses it.