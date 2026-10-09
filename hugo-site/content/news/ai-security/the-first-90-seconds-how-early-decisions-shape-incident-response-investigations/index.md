---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-04T12:15:14.724901+00:00'
exported_at: '2026-02-04T12:15:17.050815+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/the-first-90-seconds-how-early.html
structured_data:
  about: []
  author: ''
  description: Early incident response decisions—evidence preservation, execution
    analysis, and logging visibility—determine investigation success.
  headline: 'The First 90 Seconds: How Early Decisions Shape Incident Response Investigations'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/the-first-90-seconds-how-early.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'The First 90 Seconds: How Early Decisions Shape Incident Response Investigations'
updated_at: '2026-02-04T12:15:14.724901+00:00'
url_hash: 4db01cd3d61e99c31818a0e9a479020eb40b735c
---

Many incident response failures do not come from a lack of tools, intelligence, or technical skills. They come from what happens immediately after detection, when pressure is high, and information is incomplete.

I have seen IR teams recover from sophisticated intrusions with limited telemetry. I have also seen teams lose control of investigations they should have been able to handle. The difference usually appears early. Not hours later, when timelines are built, or reports are written, but in the first moments after a responder realizes something is wrong.

Those early moments are often described as the first 90 seconds. However, taken too literally, that framing misses the point. This is not about reacting faster than an attacker or rushing to action. It is about establishing direction before assumptions harden and options disappear.

Responders make quiet decisions right away, like what to look at first, what to preserve, and whether to treat the issue as a single system problem or the beginning of a larger pattern. Once those early decisions are made, they shape everything that follows. Understanding why those choices matter (and getting them right) requires rethinking what the “first 90 seconds” of a real investigation represents.

## **The First 90 Seconds Are a Pattern, Not a Moment**

One of the most common mistakes I see is treating the opening phase of an investigation as a single, dramatic event. The alert fires, the clock starts, and responders either handle it well or they do not. That is not how real incidents unfold.

The “first 90 seconds” happens every time the scope of an intrusion changes.

You are notified about a system believed to be involved in an intrusion. You access it. You decide what matters, what to preserve, and what this system might reveal about the rest of the environment. That same decision window opens again when you identify a second system, then a third. Each one resets the clock.

This is where teams often feel overwhelmed. They look at the size of their environment and assume they are facing hundreds or thousands of machines at once. In reality, they are facing a much smaller set of systems at a time. Scope grows incrementally. One machine leads to another, then another, until a pattern starts to emerge.

Strong responders do not reinvent their approach each time that happens. They apply the same early discipline every time they touch a new system. What was executed here? When did it execute? What happened around it? Who or what interacted with it? That consistency is what allows scope to grow without control being lost.

This is also why early decisions matter so much. If responders treat the first affected system as an isolated problem and rush to “fix” it, they close a ticket instead of investigating an intrusion. If they fail to preserve the right artifacts early, they spend the rest of the investigation guessing. Those mistakes can compound as the scope expands.

## **How Investigations are Hindered**

When early investigations go wrong, it is tempting to blame training, hesitation, or poor communication. Those issues do show up, but they are usually symptoms, not root causes. The more consistent failure is that teams do not understand their own environment well enough when the incident begins.

Responders are forced to answer basic questions under pressure. Where does data leave the network? What logging exists on critical systems? How far back does the data go? Was it preserved or overwritten? Those questions should already have answers. When they do not, responders end up learning the critical components of their environment after it’s too late.

This is why logging that starts following a detection is so damaging. Forward visibility without backward context limits what can be proven. You may still reconstruct parts of the attack, but every conclusion becomes weaker. Gaps turn into assumptions, and assumptions turn into mistakes.

Another common failure is evidence prioritization. Early on, everything feels important, so teams jump between artifacts without a clear anchor. That creates activity without progress. In most investigations, the fastest way to regain clarity is to focus on
**evidence of execution**
. Nothing meaningful happens on a system without something running. Malware executes. PowerShell runs. Native tools get abused. Living off the land still leaves traces. If you understand what was executed and when, you can start to understand intent, access, and movement.

From there, context matters. That could mean what system was accessed around that time, who connected to the system, or where the activity moved next. Those answers do not exist in isolation. They form a chain, and that chain points outward into the environment.

The final failure is premature closure. In the interest of time, teams often reimage a system, restore services, and move on. Except that incomplete investigations can leave behind small, unnoticed pieces of access. Secondary implants. Alternate credentials. Quiet persistence. A subtle indicator of compromise does not always reignite immediately, which creates the illusion of success. If it does resurface, the incident feels new when, in reality, it is not. It is the same one that was never fully remediated.

## **Join us at SANS DC Metro 2026**

Teams that can get the opening moments right enable difficult investigations to become more manageable. Effective incident response is about discipline under uncertainty, applied the same way every time a new intrusion comes into scope. However, it is important to give yourself grace. No one starts out good at this. Every responder you trust today learned by making mistakes, then learning how not to repeat them the next time.

The goal is not to avoid incidents entirely. That is unrealistic. The goal is to avoid making repetitive mistakes under stress. That only happens when teams are prepared before an incident forces the issue. Because when they understand their environments, they can practice identifying execution, preserving evidence, and expanding scope deliberately while the stakes are still low.

When investigations are handled with that level of discipline, the first 90 seconds feel familiar rather than frantic. The same questions get asked, and the same priorities guide the work. That consistency is what allows teams to move faster later, with confidence instead of guesswork.

For responders who experience these challenges in their own investigations, this is exactly the mindset and methodology taught in our
[SANS FOR508: Advanced Incident Response, Threat Hunting, and Digital Forensics class](https://www.sans.org/cyber-security-courses/advanced-incident-response-threat-hunting-training?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_DCMetroMarch26_Feb_EZ_Organic_Article_508&utm_campaign=SANS_DC_Metro_March_2026)
. I will be teaching FOR508 at
*SANS DC Metro*
on March 2-7, 2026, for teams that want to practice this discipline and turn insights into action.

Note: This article has been expertly written and contributed by
[Eric Zimmerman](https://www.sans.org/profiles/eric-zimmerman?utm_medium=Sponsored_Content&utm_source=Hacker_News&utm_rdetail=NA&utm_goal=Orders&utm_type=Live_Training_Events&utm_content=THN_DCMetroMarch26_Feb_EZ_Organic_Article_Bio&utm_campaign=SANS_DC_Metro_March_2026)
, Principal Instructor at SANS Institute.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.