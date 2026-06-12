---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:44:10.921209+00:00'
exported_at: '2026-06-12T21:44:12.842058+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/rethinking-mdr-as-attackers-and.html
structured_data:
  about: []
  author: ''
  description: Analysis of 25M alerts shows MDR leaves many alerts unreviewed, while
    AI SOCs can investigate every alert with faster triage.
  headline: Rethinking MDR as Attackers and Defenders Embrace AI
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/rethinking-mdr-as-attackers-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Rethinking MDR as Attackers and Defenders Embrace AI
updated_at: '2026-06-12T21:44:10.921209+00:00'
url_hash: cd830758282c85ab64dcafee68de3665768d21d5
---

For most of the past decade, managed detection and response was the answer to a real problem. Security teams couldn't staff around the clock, couldn't hire enough analysts, and needed someone else to handle the alert queue. MDR stepped in. It worked well enough. Until now.

The threat landscape has changed faster than the MDR model can adapt. Attackers are using AI to move faster, generate more convincing phishing at scale, automate reconnaissance, and create malware variants that evade signature-based detection. The attack surface has expanded from endpoint to cloud, identity, and network simultaneously. And yet MDR is still doing what it always did. Routing alerts to human analysts who triage what they can, in the order they can get to it.

That is no longer enough. The data we share below proves it and
[security leaders might consider exploring whether they have outgrown their MDR](https://intezer.com/mdr-renewal-checklist-2026/?utm_source=thehackernews&amp;utm_medium=referral)
.

## MDR's 24/7 promise doesn't cover 60% of your alerts

MDR promised 24/7 human coverage. What it delivered was a 24/7 human capacity to triage high-severity alerts. Those are not the same thing.

Across the industry, approximately 60% of alerts go unreviewed. That's not a performance failure. Human teams, whether in-house or outsourced to an MDR, cannot process the volume of alerts that modern environments generate. So they do what any rational person does. They prioritize. P1s and P2s get worked. P3s and P4s pile up.

But this is exactly where attackers hide.

[Analysis of 25 million alerts across global enterprises in 2025](https://intezer.com/2026-ai-soc-report-for-cisos/?utm_source=thehackernews&amp;utm_medium=referral)
found that nearly 1% of real threats originate in low-severity and informational alerts. In an enterprise generating 450,000 alerts annually, that translates to roughly 54 real incidents per year, about one per week, sitting in the deprioritized queue where no one is looking.

The breaches hiding in that backlog are not theoretical. They are happening right now, in organizations that believe they have coverage.

**Note:**
The math behind the above statement assumes 450K annual alerts, of which 60% are not investigated and of those, 2% are real incidents. Of those real incidents, 1% originate in low-severity alerts.

## Investigation quality varies by who is on shift

Even for alerts that do get reviewed, MDR investigation quality is not consistent. It is bounded by the experience of the analyst on duty, the queue depth at that moment, the time of day, and whether the team is fully staffed. A P1 at 3 am gets a different investigation than the same alert at 10 am.

This is not a criticism of MDR analysts. It is a description of what happens when any human-executed process runs at high volume, under pressure, around the clock. Variance is unavoidable.

The consequences are real. When an investigation is shallow, threats get classified as noise. When follow-through is inconsistent, early-stage lateral movement looks like routine behavior. The attacker who got in on a low-severity alert keeps moving undetected because no one had the time or context to connect the signals.

## Detection engineering is not a closed loop

In most MDR deployments, detection engineering is a periodic exercise. Rules get tuned when customers complain about alert volume. New coverage gets added when a major CVE makes news. Otherwise, the detection posture drifts.

The core problem is architectural. MDR investigation and detection engineering operate in separate silos. When an analyst investigates an alert and closes it as a false positive, that insight rarely feeds back into the detection system. Broken rules stay broken. Noisy rules keep generating noise. New attacker techniques arrive without matching detections.

The result is a detection posture that degrades faster than it improves. Real coverage, measured against the MITRE ATT&amp;CK framework, can be far lower than teams assume.

## You can't audit what you can't see

Most MDR services are a black box. Customers receive escalations and summaries. They do not get to see the investigation logic, inspect the evidence trail, verify the verdict, or audit what the analyst actually reviewed before closing a case.

In an era where accountability and transparency are security requirements, this is a genuine liability. When an incident is missed, you cannot diagnose why. When a verdict is wrong, you cannot trace the reasoning. When regulators ask what was investigated and how, there is no answer.

## The AI savings are going to the vendor, not to you

AI is reducing the operational cost of MDR. Providers are using it to automate portions of triage, reduce analyst hours, and increase margins. Those efficiency gains do not flow through to customers as lower prices or expanded coverage. The buyer still pays the same rate, or more. The provider keeps the savings.

But the coverage gap stays the same. The human scaling constraint stays the same. Only the provider's cost structure has improved.

## You don't own what was built in your name

Detection rules, triage logic, case history, and investigation learnings accumulate inside the MDR vendor's platform over the life of the contract. When the contract ends, that knowledge does not move with you. The years of tuning, the accumulated context about your environment, and the detection improvements built from your data all stay with the vendor.

This creates two problems. First, organizations that switch providers start from scratch, rebuilding institutional knowledge that took years to develop. Second, organizations that want to bring security operations in-house, a trend that is accelerating as AI SOC tools mature, find themselves starting with no foundation.

MDR providers, for obvious reasons, are not incentivized to help customers build internal capability. Their model depends on retaining the work.

## Your MDR contract may block you from using Claude for your SOC

The above-mentioned knowledge lock-in is no longer just a switching-cost problem. It's also an AI readiness problem. When you try to deploy an AI agent for SOC work, it needs a knowledge foundation to reason over. Detection rules, case history, behavioral baselines, and forensic verdicts. If those live in your MDR vendor's platform, your agent is starting from near zero.

## Additional MDR gaps worth noting

Aside from the above, MDR has a set of smaller gaps that compound over time. Every customer gets the same generic playbook regardless of their specific risk profile, compliance obligations, or data sensitivity. Integration tools like SOAR, which were supposed to streamline MDR findings into internal workflows, largely failed to deliver on that promise because human-driven investigation doesn't produce the structured, consistent outputs that automation requires. And when a real incident surfaces and a customer needs to talk to someone who understands their environment, they often reach an AI chatbot or a ticketing queue instead of a person.

## What the AI-powered attacker era actually requires

The attackers of 2026 are not waiting for alert queues to clear. AI-generated phishing campaigns hit inboxes at a volume and quality that bypass conventional gateways. Credential stealers like Agent Tesla and LummaC2 move fast. EDR tools are being actively evaded, with research showing that
[more than half of confirmed compromised endpoints had already been marked as "mitigated" by the EDR vendor](https://intezer.com/2026-ai-soc-report-for-cisos/?utm_source=thehackernews&amp;utm_medium=referral)
. The attacker has already won a round that the defender didn't know was being played.

Meeting this moment requires a different operating model. One where investigation speed is measured in seconds, not hours. Where every alert gets examined, regardless of severity or time of day. Where the output is an evidence-backed verdict, not an analyst's judgment call under pressure.

This is what an AI SOC is designed to deliver.

## An operating model shift where AI executes and humans supervise

The core idea behind an AI SOC is simple. Move investigative execution out of the human queue and into AI, so that humans can focus on decisions rather than discovery.

In practice, this means 100% of alerts, including endpoint, identity, cloud, network, phishing, and SIEM, are triaged and investigated automatically. Not sampled. Not filtered by severity. All of them. The AI applies the same forensic depth to a P4 alert at 3 am that a senior analyst would apply to a P1 in the afternoon.

Intezer's platform data across 25 million alerts shows this is achievable. Less than 2% of alerts required human escalation. The over 98% that resolved autonomously did so with sub-minute median triage time and 98% verdict accuracy. For a large enterprise with 450K annual alerts, that means roughly 441K alerts per year are fully investigated and resolved without human intervention and 54 genuine threats that would have been missed under traditional MDR coverage are now caught with actional remediation recommendations.

## Forensic depth is what makes AI autonomy trustworthy

AI can summarize an alert. That's useful. AI can enrich with threat intelligence. Also useful. But neither of those activities is investigation. They are pre-processing.

Genuine AI-driven investigation requires forensic-level interrogation. When an alert fires, the question is not "does this look suspicious?" It is, what actually executed, where did it originate, what did it do, and is there evidence of compromise in memory that the alert itself didn't surface?

This matters because the most dangerous threats are specifically designed to evade surface-level detection. Fileless malware lives entirely in memory and writes nothing to disk. Code injection hides inside legitimate processes. Early-stage credential theft looks like normal authentication. Without memory forensics, binary analysis, and code reuse detection, an AI investigation is only as deep as the alert data it was handed.

Forensic depth is also what creates the trust threshold, the point at which AI verdicts are accurate and evidence-backed enough to act on without human validation. Below that threshold, AI assists analysts. Above it, AI can safely take on the full investigative workload and escalate only when evidence warrants it.

## Closed-loop detection engineering changes everything

One of the most significant structural advantages of a true AI SOC is the closed loop between investigation and detection. Every alert investigation surfaces information about detection quality. Which rules are firing accurately, which are generating noise, and which attacker techniques have no coverage at all?

When this feedback flows continuously into detection engineering, the posture improves without waiting for an annual audit or a customer complaint. Noisy rules get tuned. Broken telemetry gets flagged. New coverage for emerging techniques gets deployed in days, not months. The detection system gets smarter alongside the investigation system.

This is how MITRE ATT&amp;CK coverage moves from a static baseline to a dynamic, improving map of what an organization can actually detect. It is the difference between coverage that reflects what was set up two years ago and coverage that reflects what attackers are doing today.

## Pricing that aligns with full coverage

The economics of an AI SOC should match the coverage it provides. Per-alert pricing, still common among AI copilot tools that rely heavily on LLMs, forces customers to be selective about which alerts to send. The result is the same cherry-picking problem that MDR created. High-severity alerts get the attention, low-severity alerts accumulate in a deprioritized queue.

Per-endpoint pricing changes this entirely. The cost is fixed to the number of monitored endpoints, not to alert volume. There is no economic penalty for investigating every alert. Full coverage becomes the default, not a premium option.

This also matters for budget predictability. Alert volumes spike unpredictably during active incidents or when new detections deploy. Endpoint counts are stable. For finance teams trying to plan security spend, the difference is significant.

## What ownership looks like under an AI SOC

Detection rules, investigation history, and organizational context should belong to the organization, not to the vendor. This means every detection deployed to a customer's SIEM is the customer's rule. Investigation evidence is available for audit at any time. If the organization decides to expand internal capability, build its own AI agents, or switch tools, they take everything with it.

This is not just a contract term. It is a prerequisite for security maturity and for broader adoption of AI tools like Claude for your security team. Organizations that want to eventually supervise AI systems rather than outsource to vendors need a knowledge foundation to build on. That foundation cannot exist if it lives inside a vendor's platform.

## The transition from MDR to AI SOC

Moving from MDR to an AI SOC is not necessarily a rip-and-replace decision for most organizations. The practical path might be augmentation first. Bring in an AI investigation alongside the existing MDR contract, observe what the AI surfaces that the MDR was missing, and let the comparison build the case for a clean transition at renewal.

By the time the MDR contract is up for renewal, the organization typically has months of evidence showing what full alert coverage looks like, what the escalation rate was under AI triage, and what it would cost to maintain the old model versus the new one. The decision is no longer theoretical.

## The question security leaders need to answer

The MDR model was designed for a world where attackers operated at human speed, and the primary challenge was staffing coverage. That world is gone. Attackers are running AI-assisted campaigns, moving through environments faster than human triage queues can respond, and specifically targeting the low-severity signal space where MDR leaves blind spots.

The question for every CISO and security leader evaluating their current operations is straightforward. Of the 60% of alerts your team isn't reviewing, how confident are you that none of them contain a real threat?

The answer, informed by Intezer's analysis of 25 million real alerts, is that roughly 54 of them do. Every year. One per week. In the pile that no one is looking at.

The AI SOC doesn't promise to eliminate all threats. No platform does. But it closes the coverage gap that the MDR model structurally cannot. Every alert, every severity, every hour of the day, is investigated with forensic depth, in under a minute. That is what security operations in the AI era look like.

**Found this article interesting? See the
[2026 MDR renewal checklist by Intezer](https://intezer.com/mdr-renewal-checklist-2026/?utm_source=thehackernews&amp;utm_medium=referral)
.**

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.