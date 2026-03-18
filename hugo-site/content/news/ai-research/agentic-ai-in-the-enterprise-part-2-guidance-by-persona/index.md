---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-research
date: '2026-03-18T03:01:43.891216+00:00'
exported_at: '2026-03-18T03:01:47.148117+00:00'
feed: https://aws.amazon.com/blogs/machine-learning/feed
language: en
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-ai-in-the-enterprise-part-2-guidance-by-persona
structured_data:
  about: []
  author: ''
  description: This is Part II of a two-part series from the AWS Generative AI Innovation
    Center. In Part II, we speak directly to the leaders who must turn that shared
    foundation into action. Each role carries a distinct set of responsibilities,
    risks, and leverage points. Whether you own a P&L, run enterprise architecture,
    lead...
  headline: 'Agentic AI in the Enterprise Part 2: Guidance by Persona'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://aws.amazon.com/blogs/machine-learning/agentic-ai-in-the-enterprise-part-2-guidance-by-persona
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Agentic AI in the Enterprise Part 2: Guidance by Persona'
updated_at: '2026-03-18T03:01:43.891216+00:00'
url_hash: bdc73d04f2c97545b21056bd33c4b17a0e394264
---

This is Part II of a two-part series from the AWS Generative AI Innovation Center. If you missed Part I, refer to
[Operationalizing Agentic AI Part 1: A Stakeholder’s Guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)
.

The biggest barrier to agentic AI isn’t the technology—it’s the operating model. In
[Part I](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)
, we established that organizations generating real value from agents share three traits: they define work in precise detail, they bound autonomy deliberately, and they treat improvement as a continuous habit rather than a one-time project. We also introduced the four ingredients of work that is truly “agent-shaped”: a clear start and end, judgment across tools, observable and measurable success, and a safe failure mode. Without these foundations, even the most sophisticated agent will stall in the lab.

**Now comes the harder question:**
***who*
makes it work, and
*how*
?**

In Part II, we speak directly to the leaders who must turn that shared foundation into action. Each role carries a distinct set of responsibilities, risks, and leverage points. Whether you own a P&L, run enterprise architecture, lead security, govern data, or manage compliance, this section is written in the language of your job—because that’s where agentic AI either succeeds or quietly dies.

## Part II – Guidance by persona

### For the line-of-business owner: put the agent on the hook for your KPIs.

If you own a P&L, you don’t need another technology toy. You need fewer open tickets, fewer days in your cash conversion cycle, fewer abandoned carts, fewer compliance exceptions. An agent is useful only if it can be tied directly to those numbers.

The first step is to write a job description for the agent the same way you would for a new hire. “This agent takes inbound X, checks Y, does Z, and hands off to this team when it’s done.” Include what
*done*
means in your operational terms: time to respond, quality threshold, escalation triggers, and customer-facing commitments.

The second step is to anchor the business case in numbers your own team already tracks. How many units per week pass through this workflow? What does each unit cost in labor, rework, and write-offs? How long does it spend waiting in queues? How often does it bounce back because something was missing or wrong? If you can’t answer these questions today, your first project isn’t an agent—it’s instrumenting the workflow.

The third step is sequencing. Early in the journey, the most useful agent is often the one that collapses handoffs: it reads the inbound request, gathers context from multiple systems, proposes a plan, and drops that plan into your team’s lap with everything pre-staged. It may not
*close the loop*
by itself, but it can remove hours or days of back-and-forth. Cost-saving wins like this help build credibility with the CFO and give you political capital to pursue more ambitious, revenue-focused use cases later.

The line-of-business owner doesn’t need to understand models or prompts. They need to own a small portfolio of agent jobs tied directly to their metrics, and they need to insist that every initiative starts with a written job contract, not a slide with a label.

![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/03/16/ml-20583-p2-1.jpg)

### For the CTO or chief architect: Decide whether you want ten agents or one hundred

If you’re the CTO, one of your biggest risks is success. Once the first agent lands well, other teams will want one. If each team builds its own stack—own framework, own connectors, own access model—you’ll end up with a zoo of agents that look different, are tested differently, and are impossible to monitor as a whole.

The architecture question is simple to state and hard to execute: do you want ten impressive one-off agents, or do you want a system that can support one hundred agents safely?

The system path asks you to do some hard work early. It means standardizing how tools are exposed so that every agent calls the same integration when it needs to read customer data, update a ticket, or book a payment. It means separating
*thinking*
from
*doing*
in your design: one component plans, another calls tools, another checks compliance, another explains decisions back to users. It means capturing decision traces in a consistent format so observability and debugging work across use cases.

It also asks you to think about agents as long-lived services, not short-lived scripts. They need identities, permissions, rotation, lifecycle management, and a way to be upgraded without breaking their consumers. That’s more work on day one, but it’s what allows you to say “Yes” to the tenth team that wants an agent without starting from scratch.

The CTO’s job isn’t to pick the best agent framework in a vacuum. It’s to build a sturdy floor—identity, policy enforcement, logging, connectors, and evaluation hooks—that allows many teams to ship agents safely, quickly, and consistently.

### For the CISO: Treat agents like colleagues, not code

If you’re responsible for security, you’re used to thinking in assets: systems, data stores, credentials. Agents add something new to your threat model: authorized entities that can make decisions and take actions at machine speed.

The mistake is to treat agents as just another application. They’re closer to colleagues. They have accounts. They have roles. They have tools they can use. They can make mistakes. They can be misconfigured.

The practical move is to set up non-human identities for agents with the same seriousness you apply to human identities. Each agent should have its own credentials, its own permissions, and its own audit trail. It shouldn’t inherit all the rights of the service account it happens to run under. When an agent reads sensitive data or calls a high-risk tool, that should be visible in your logs in a way your team recognizes.

You’ll also want ways to stop agents cleanly. That means kill switches that really work, not just a line in a design doc. It means policies that say, “This class of action always requires human approval,” and enforces that at the tool level, not just in the agent’s prompt. It means watching for behavior that drifts: an agent that suddenly calls a tool far more often than usual, or starts reading data it hasn’t needed before.

CISOs who adapt well to agentic AI don’t try to block autonomy entirely. They define where autonomy is acceptable, what evidence is needed to trust it, and what happens when that trust is broken. They join the design conversation early and make policy part of the agent’s shape, not a gate at the end.

### For the chief data officer: Make the data boring

Agents amplify whatever data foundation you already have. If your data is fragmented, stale, and undocumented, agents can make those problems visible to everyone quickly. If your data is consistent, well-governed, and straightforward to understand, agents can multiply its value.

The CDO’s job in the agentic era is to make the data boring, in the best possible way. That means when an agent asks, “Show me all open claims over this threshold,” it gets a consistent answer regardless of which region or line of business it operates in. It means one definition of “customer health score” exists and is documented well enough that people and agents can both use it. It means lineage is clear: when something goes wrong, you can trace the decision back through the metrics, through the features, all the way to the source system.

It also means being realistic about readiness. Some workflows simply aren’t ready for autonomous decisions because the data they rely on is too incomplete or too contradictory. The best CDOs lean into this. They don’t say, “We can’t support agents.” They say, “We can support this class of work today. If you want to automate that other class, here are the data improvements we need first.”

One of the most valuable contributions a CDO can make to the agent conversation is a map: which domains have production-grade data, which are in progress, and where the landmines are. That map helps everyone else pick their first jobs wisely, instead of discovering data debt mid-implementation.

### For the chief data science or AI officer: Evaluation is your real product

If you lead data science or AI, it’s tempting to focus on models: which foundation model, which fine-tune technique, which benchmark score. Those decisions matter, but in production, your real product is the evaluation system wrapped around the model.

Agents can fail in ways that benchmarks don’t measure. They get stuck in loops. They call tools incorrectly. They half-complete tasks in ways that look plausible but are wrong. They behave well on clean test data and fall apart on the edge cases no one thought to include. An effective evaluation system does three things.

First, it turns real work into tests. When an agent makes a mistake in production, that scenario becomes part of a growing evaluation suite. Over time, the hardest cases you encounter become guardrails that help protect you from regressing.

Second, it runs automatically. Changes to prompts, models, tools, or retrieval indexes trigger evaluation before that change goes live. That gives you the confidence to iterate quickly, because you’re not relying on a few spot checks and hope.

Third, it measures what the business cares about. That includes technical metrics like latency and tool success rate, but also task completion rate, escalation rate, cost per decision, and the share of work where humans accept the agent’s recommendation as-is. When those numbers are visible and improving, trust follows.

Teams that invest here early discover that model choices become simpler, not harder. Once you can see how a model behaves on your real tasks, the “which model is best?” debate becomes a grounded comparison instead of a philosophical discussion.

### For the compliance or legal officer: Design for audits before you face one

If you’re accountable for compliance or legal risk, agentic AI probably looks like a moving target. Regulations are evolving, and vendor marketing is ahead of regulatory clarity. You can’t freeze the organization until every standard settles, but you also can’t tolerate “We’ll figure out the governance later.”

A pragmatic approach is to work backwards from an audit. Imagine a regulator or internal audit committee asks, “On this date, why did this agent take this action?” Decide now what evidence you’d need to answer that question clearly and quickly.

That implies a few design choices. Every agent should leave a trail: what inputs it saw, what tools it called, what options it considered, what it chose, and what rules it applied. For high-stakes domains like credit decisions, insurance underwriting, and employment-related actions, humans must remain in the loop, and the agent’s role should be advisory or preparatory: collecting data, organizing evidence, proposing actions. The human’s approval becomes part of the record.

It also implies that not all agent ideas are allowed. Some use cases live squarely inside regulatory red zones until frameworks and controls mature. Your job is to make those lines visible early. When you can say “Yes” to some agents with clear conditions, “Yes later” to others with specific prerequisites, and “No” to a few with a clear rationale, you can become an enabler rather than a blocker.

One of the most helpful things you can do for the rest of the leadership team is to turn abstract concerns like “we need responsible AI” into a concrete checklist that can be applied to each proposed agent before work starts.

## Call to action

If the patterns in this post sound familiar, you’re not behind. You’re where most enterprises are. What separates those who move forward is the decision to treat agentic AI as an operating model challenge, not a technology experiment. Five moves you can make to get started:

**Convene the right room.**
Bring your LOB owner, CTO, CISO, CDO, AI/DS leader, and compliance lead together—not for a demo, but for a working session. Each person answers one question: “What’s the single biggest thing blocking us from putting an agent into production on a real workflow?”

**Pick one job, not one use case.**
Identify one concrete piece of work with a clear start, clear end, defined tools, and a success measure someone outside the team can verify. Write the agent’s job description together. If the room can’t agree on what
*done*
looks like, you’ve found your first problem to solve.

**Draw your readiness map.**
Have your CDO and CISO jointly sketch which data domains and systems are production-ready for autonomous decisions today, which need improvements first, and where the hard boundaries are. That one-page map can save you months of wasted effort.

**Commit to a cadence.**
Set a recurring weekly or biweekly review where the cross-functional team examines how the agent behaved, what worked, what broke, and what to adjust. If you only evaluate at launch, you are building a demo. If you evaluate continuously, you are building a capability.

**Make governance a design input, not a launch gate.**
Decide now what evidence you would need if an auditor asked “Why did this agent do this?” six months from today. Integrate that into the architecture before the first line of code is written.

The enterprises generating real value from agentic AI got there by doing the unglamorous work: defining jobs precisely, bounding autonomy deliberately, investing in evaluation relentlessly, and aligning stakeholders around a shared operating model.

**Partner with the Generative AI Innovation Center**

You don’t have to navigate this journey alone. Whether you are planning your first agentic pilot or scaling to an enterprise-wide capability, reach out to the
[Generative AI Innovation Center](https://aws.amazon.com/ai/generative-ai/innovation-center/)
team to start a conversation grounded in your workflows, your data, and your business outcomes.

---

## About the authors

### Nav Bhasin

Nav Bhasin is a Senior Data Science Manager at the AWS Generative AI Innovation Center, where he accelerates enterprise customers’ journey from Agentic AI concept to production deployment. With over a decade of experience building AI products across industrial, energy, and healthcare domains, Nav has spent six years at AWS leading worldwide teams of GenAI architects and scientists, playing a central role in bringing products like Amazon Bedrock, Amazon SageMaker, and AgentCore to production adoption. Before the Innovation Center, he led go-to-market architecture and data science teams for AWS’s core GenAI product portfolio. Prior to AWS, Nav served as Head of Data Science and Engineering at Utopus Insights and led Engineering and Architecture at Honeywell. Nav holds an MBA and a graduate degree in Electronics Engineering.

### Sri Elaprolu

Sri Elaprolu is Director of the AWS Generative AI Innovation Center, where he leads a global team implementing cutting-edge AI solutions for enterprise and government organizations. During his 13-year tenure at AWS, he has led ML science teams partnering with global enterprises and public sector organizations. Prior to AWS, he spent 14 years at Northrop Grumman in product development and software engineering leadership roles. Sri holds a Master’s in Engineering Science and an MBA.