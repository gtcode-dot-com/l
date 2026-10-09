---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-02T12:15:13.177109+00:00'
exported_at: '2026-01-02T12:15:15.590918+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/the-roi-problem-in-attack-surface.html
structured_data:
  about: []
  author: ''
  description: Attack surface management ROI improves when ownership, exposure duration,
    and risky endpoints decline—not when asset counts rise.
  headline: The ROI Problem in Attack Surface Management
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/the-roi-problem-in-attack-surface.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: The ROI Problem in Attack Surface Management
updated_at: '2026-01-02T12:15:13.177109+00:00'
url_hash: b358cb0ff700e0fae7617a13ed49ecb184d4b5b1
---

Attack Surface Management (ASM) tools promise reduced risk. What they usually deliver is more information.

Security teams deploy ASM, asset inventories grow, alerts start flowing, and dashboards fill up. There is visible activity and measurable output. But when leadership asks a simple question, "
*Is this reducing incidents?*
" the answer is often unclear.

This gap between effort and outcome is the core ROI problem in attack surface management, especially when ROI is measured primarily through asset counts instead of risk reduction.

## **The Promise vs. The Proof**

Most ASM programs are built around a reasonable idea: you can't protect what you don't know exists. As a result, teams focus on discovery: domains and subdomains, IPs and cloud resources, third-party infrastructure, and transient or short-lived assets.

Over time, counts increase. Dashboards are trending upward. Coverage improves.

But none of those metrics directly answer whether the organization is actually safer. In many cases, teams end up busier without feeling less exposed.

## **Why ASM Feels Busy but Not Effective**

ASM tends to optimize for coverage because coverage is easy to measure: more assets discovered, more changes detected, and more alerts generated. Each of those feels like progress.

But they mostly measure inputs, not outcomes.

In practice, teams experience:

* Alert fatigue
* Long backlogs of "known but unresolved" assets
* Repeated ownership confusion
* Exposure that lingers for months

The work is real. The risk reduction is harder to see.

## **The Measurement Gap**

[One reason ASM ROI](https://www.sprocketsecurity.com/blog/attack-surface-management-asm-what-youre-missing-and-why-it-matters?utm_campaign=14984749-Paid%20Content&utm_source=Hacker%20News&utm_medium=Expert%20Article&utm_term=Hacker%20News%20Expert%20Article&utm_content=The%20ROI%20Problem%20in%20Attack%20Surface%20Management)
is hard to prove is that most attack surface metrics focus on what the system can see, not what the organization actually improves.

Common attack surface management metrics include:

* Number of assets
* Number of changes

More meaningful attack surface metrics are rarely tracked:

* How fast risky assets get owned
* How long dangerous exposure persists
* Whether attack paths actually shrink over time

Asset inventory remains foundational to measuring the external attack surface. Without broad discovery, it's impossible to understand exposure at all. The gap appears when discovery metrics aren't paired with measurements that show whether risk is actually being reduced.

Without outcome-oriented measurements, ASM becomes difficult to defend during budget reviews, even when everyone agrees that asset visibility is necessary.

## **What Would Meaningful ROI Look Like?**

Instead of asking, "
*How many assets did we discover?*
" a more useful question is, "
*How much faster and safer did we get at handling exposure?*
"

That reframing shifts ROI from visibility to response quality and exposure duration. Things that correlate much more closely with real-world risk.

### **Three Outcome Metrics That Actually Matter**

####

#### **1. Mean Time to Asset Ownership**

How long does it take to answer the basic question: "
*Who owns this?*
"

Assets without clear ownership:

* Linger longer
* Get patched later
* Are more likely to be forgotten entirely

Reducing time-to-ownership shortens the window where exposure exists without accountability. It's one of the clearest signals that ASM findings are turning into action.

#### **2. Reduction in Unauthenticated, State-Changing Endpoints**



Not all assets matter equally.

Tracking how many external endpoints can change state, how many require authentication, and how those numbers change over time provides a much stronger signal of whether the attack surface is shrinking where it counts.

An environment with thousands of static assets but few unauthenticated, state-changing paths is meaningfully safer than one with fewer assets but many risky entry points.

#### **3. Time to Decommission After Ownership Loss**



Exposure often persists after:

* Team changes
* Application deprecation
* Vendor migrations
* Reorgs

Measuring how quickly assets are retired once ownership disappears is one of the strongest indicators of long-term hygiene and one of the least commonly tracked.

If abandoned assets stick around indefinitely, discovery alone isn't reducing risk.

## **What This Looks Like in Practice**

Abstract metrics are easy to agree with and hard to operationalize. The goal isn't a new dashboard or a different set of alerts, but a shift in what's made visible: ownership gaps, exposure duration, and unresolved risk that would otherwise blend into asset counts.

Rather than emphasizing total asset count, this view surfaces:

* Which assets are owned
* Which are unresolved
* How long ownership has been unclear

The goal isn't more alerts but faster resolution.

### **Turning ASM into a Control**

ASM doesn't struggle because teams aren't working hard enough. It struggles because effort isn't consistently tied to outcomes that leadership cares about.

Reframing ROI around speed, ownership, and exposure duration makes it possible to show real progress. Even if the raw asset count never changes. In many cases, the most meaningful wins come from making the attack surface boring again.

### **A Concrete Starting Point**

One way to pressure-test outcome-based ASM metrics is to make asset visibility broadly accessible across teams, not gated behind tooling silos. We've found that when engineering, security, and infrastructure teams can all see ownership gaps and exposure duration, resolution speeds up without adding more alerts.

That thinking led us to release a
**[community edition of our ASM platform](https://portal.sprocketsecurity.com/users/sign_up?utm_campaign=14984749-Paid%20Content&utm_source=Hacker%20News&utm_medium=Expert%20Article&utm_term=Hacker%20News%20Expert%20Article&utm_content=The%20ROI%20Problem%20in%20Attack%20Surface%20Management)**
that exposes asset discovery and ownership visibility without cost or limits. The goal isn't to replace existing tools, but to give teams a way to measure whether exposure is actually shrinking over time.

If you want to pressure-test the ROI of your ASM program, try this: Ignore how many assets you have.

Instead, ask:

* How long do risky assets stay unowned?
* How many unauthenticated, state-changing paths exist today vs last quarter?
* How quickly do abandoned assets disappear?

If those answers aren't improving, more discovery won't change the outcome.

## **Conclusion: Measure What Actually Changes Risk**

Attack surface management becomes defensible when it's measured by what changes, not just what accumulates. Discovery will always matter. Visibility will always matter when measuring the attack surface. But neither guarantees that exposure is being reduced, only that it's being observed.

Attack surface management ROI shows up when risky assets get confirmed as owned faster, when dangerous paths disappear sooner, and when abandoned infrastructure doesn't linger indefinitely. Asset inventory provides the necessary breadth; outcome-oriented metrics provide the depth needed to understand real risk reduction.

At Sprocket Security, we try to think about
[attack surface management](https://www.sprocketsecurity.com/solutions/attack-surface-management?utm_campaign=14984749-Paid%20Content&utm_source=Hacker%20News&utm_medium=Expert%20Article&utm_term=Expert%20Article%20Hacker%20News&utm_content=The%20ROI%20Problem%20in%20Attack%20Surface%20Management)
not only in terms of how many assets exist, but also how long meaningful exposure persists and how quickly it gets resolved. What matters most is that attack surface metrics make progress visible, not just inventory growth.

If an attack surface management program can't answer whether exposure is shrinking over time, it's hard to argue that it's doing more than reporting the problem.

**Note:**
*This article was expertly written and contributed by Topher Lyons, Solutions Engineer at Sprocket Security.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.