---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-01T01:10:11.371933+00:00'
exported_at: '2026-06-01T01:10:13.512198+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html
structured_data:
  about: []
  author: ''
  description: 2,000+ AI-built corporate apps lacked access controls across 380,000
    public assets, exposing sensitive data and increasing enterprise risk.
  headline: What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security
    Stacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/what-2000-exposed-vibe-coded-apps.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: What 2,000 Exposed Vibe-Coded Apps Reveal About the Limits of Most Security
  Stacks
updated_at: '2026-06-01T01:10:11.371933+00:00'
url_hash: 8b4b43d89df19fb9f3d78df7f8cee3ea847977d0
---

Shadow AI used to mean employees pasting things they shouldn't into ChatGPT. It now means something bigger: employees building full applications with AI, wiring them into production systems, and publishing them on the open internet. Without Security or IT in the loop.

The artifact moved from a prompt to a product. The risk surface moved with it.

In
*The Shadow Builders*
report (
[get it here](https://info.redaccess.io/shadow-ai-builders-security-report)
), a new category-level investigation covered in May by Axios, WIRED, and VentureBeat, Red Access identified more than 380,000 publicly accessible web assets across the leading vibe-coding platforms.

Roughly 5,000 looked corporate. More than 2,000 of those held sensitive corporate, operational, or personal data - sitting on the open web, deployed without basic access controls, often granting admin access by default to anyone who reached the URL. Six continents. Every industry is examined. No exploitation required.

Inside organizations, passing their audits while these exposures were live.

## **The new Shadow AI isn't about prompts. It's about products.**

Vibe coding - the broader space of AI-driven development platforms where anyone can build a working application by describing what they want - has compressed what used to take engineering teams months into something a non-developer can ship before lunch.

A marketing manager builds a campaign tracker and connects it to the BI tool where the real numbers live. An operations manager builds a vendor-intake form and connects it to the ticketing system. A finance team builds a board-prep dashboard and pulls invoice data into it before Friday. Those applications get connected to sanctioned production systems - CRMs, ERPs, ticketing tools, BI platforms - and frequently published to the open internet, with whatever access controls the builder happened to configure. Often, none.

The people doing this aren't malicious. They are competent employees solving real problems faster than their organization could, doing exactly what the platforms invited them to do. The platforms aren't villains either - they're delivering what their original audience asked for. What hasn't kept pace is the guardrails, technical and behavioral, governing what happens after the build.

This isn't Shadow IT in the old sense. Shadow IT was bounded: when a team bought a Trello account on a corporate card without telling anyone, the data sat inside an unsanctioned SaaS vendor, but identity, audit logs, and a governance surface at least existed.
[Shadow Builders](https://redaccess.io/use-case-shadow-builders)
invert that. The application is custom-built, the data is custom-loaded, the integrations are direct connections to production systems of record, and the artifact is often published on the open internet. The platform underneath may be audited; the application built on it isn't. There is the builder, the platform, and the URL. IT? Mostly not in the room.

## **Why a mature security stack still misses this**

The reflex of a CISO reading the numbers above is to check the stack. EDR is running. DLP is configured. CASB is licensed. Firewall and SSE are in place. Some organizations have added an enterprise browser. Each of those tools is doing what it was designed to do. The category sits in the gaps between them.

EDR sees the browser process, not the build inside it. To an endpoint agent, a Shadow Builder using a vibe-coding platform looks like ordinary, non-malicious browser activity - the same shape of telemetry as someone reading the news. Where modern EDR or an enterprise browser does see deeper, it only does so on devices the organization owns and inside browsers it manages. Personal laptops, contractor machines, BYOD devices, and personal-browser tabs are invisible by definition.

DLP watches enumerated channels. It can flag a user pasting regulated data into a known AI chat. It can't see a vibe-coded application connecting programmatically to a sanctioned BI tool via API, moving data cloud-to-cloud, physically bypassing the endpoint entirely.

CASB was built for Shadow IT - for SaaS vendors with discoverable identities. It can't readily distinguish an unbounded population of custom applications hosted on a vibe-coding platform's subdomains from the platform itself. The whole population tends to register as one approved SaaS vendor.

Firewall and SSE see traffic to the platform's domain but lack the application-as-business-object context. And most SASE/SSE deployments are partial - even the mature ones leave
[the unmanaged-device problem](https://redaccess.io/use-case-byod/)
unsolved.

None of these tools is failing. The category just sits across the gaps the existing architecture leaves between layers, generating fragments of signal that never assemble into a single, governable picture.

## **Where visibility actually has to live**

End-to-end, vibe coding is a web-session event. The build is a browser event. The OAuth grant that ties the new application to a sanctioned enterprise system is a browser event. The data the application is built around moves through the session. The deployment is a browser event - the publish action that turns the build into a live application at a public URL is a click inside the same tab where everything else happened.

Every step happens at the session layer. Not adjacent to it. Inside it.

A control positioned at the session layer, therefore, sees the whole build path - not a fragment of it. The platform used. The corporate systems connected to it, and through what mechanism. The data is moving in and out. The publish event that puts the application on the open internet. Attributable to a specific person and a specific application instance, regardless of which browser was used or which network path the traffic took. And, critically, regardless of whether the device is a corporate-issued laptop or a contractor's personal machine.

## **What to do this week**

Four moves. None of them is a technology purchase.

Start with discovery. Ask employees directly what they've built. Most Shadow Builders are doing useful work and aren't hiding anything; the framing matters. A workforce-wide prompt -
*if you've built a tool using an AI development platform, please tell us about it. We're not auditing. We're inventorying*
- gets further on the first pass than a policy memo or a tooling deployment.

Then map. For each application surfaced, capture which corporate systems it's connected to, how (OAuth, API key, manual upload - different audit trails), and whether it's publicly reachable. Public reachability is the most actionable signal in the short term.

Establish a sanctioned path. Give Shadow Builders somewhere to tell you. Name the approved platforms, define acceptable data categories, and set a minimum authentication standard. Lower-friction than the alternative, which is them not telling you at all.

And then accept that the work isn't a one-time inventory. Vibe-coded applications keep getting created; the picture you build this month will be incomplete next month. The mature posture is continuous discovery at the layer where the activity actually happens.

The category will keep maturing. Platforms will keep recalibrating defaults. None of those adaptations is finished. The exposure exists in most enterprises right now.

Red Access is the agentless, session-layer security platform built for exactly this - SSE-grade visibility and governance at the session itself, across any browser, any device, including unmanaged ones. Deployable in hours.
**[Request your free audit.](https://info.redaccess.io/request-a-demo)**

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.