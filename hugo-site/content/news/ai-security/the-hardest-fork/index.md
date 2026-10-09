---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T03:11:58.902445+00:00'
exported_at: '2026-06-10T03:12:00.199887+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/the-hardest-fork.html
structured_data:
  about: []
  author: ''
  description: AI vulnerability chaining overwhelms open source disclosure; 6% upstreamed,
    forcing trusted forks.
  headline: The Hardest Fork
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/the-hardest-fork.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Hardest Fork
updated_at: '2026-06-10T03:11:58.902445+00:00'
url_hash: 26283d41a572967679c69adf900c943c56ee8bec
---

Mythos is real. I know a big chunk of the industry thinks it's a marketing stunt, and I get why. I get it. But I've seen the findings, and they're bad. These aren't "whoops, this line right here is wrong, and that's RCE." They're novel combinations of a few dozen issues out of thousands of things every SAST scanner already finds, chained together into something much worse. It's real creativity, like Move 37. That's not a better scanner. That's a different category of threat.

In some ways, it doesn't even matter. Even if this specific model were a hoax, the capability is coming regardless. Some days, I wish it were a hoax. We'd have more time. But you can believe me or not. The rest of this post is about what we do about it either way, and I'm getting started now.

Washington has been tracking this for a while, but you can't regulate something most of the industry thinks is made up. Now that every boardroom is in preparation mode (and they are), DC finally gets to start thinking through what steps they can take. It's clear they need to play a role, but it's not clear how or what it should be. And they're in a really tough spot.

Regulate too little, and you risk a US-based company accidentally creating a weapon that puts our critical infrastructure at risk. Regulate too much, and the same thing happens in China instead. The whole thing feels like gain-of-function research on viruses. Everyone knows you should wash your hands before leaving the lab, but just because we make it mandatory doesn't mean the rest of the world will. We've already seen how that story goes in Wuhan.

Here's the structural problem that limits what any government can do: despite Europe's best attempts with the CRA, open source isn't governable. Laws and executive orders don't apply to people around the world putting things on the internet for free. The US realizes this, so they're focusing where they can and where they should: on consumption. That's the right instinct, and it's exactly where the rest of this post is going.

## The open source ecosystem and consumption model is not ready for this

I've been working on this problem every day of my life for the last decade. I helped found the
[OpenSSF](https://openssf.org/)
and
[Alpha-Omega](https://alpha-omega.dev/)
while at Google. I created
[Sigstore](https://www.sigstore.dev/)
,
[Scorecards](https://openssf.org/projects/scorecard/)
, and the first open source malware scanners. I funded the grants that put Rust in the Linux kernel and MFA on PyPI. Then I started Chainguard to do all of this commercially, at scale. I'm telling you all of this not to brag, but because I need you to believe me when I say: the way the world consumes open source software is fundamentally broken, and no amount of incremental improvement is going to fix it in time.

Not in its current form. Maybe not ever. It's going to have to change.

Most companies have been consuming open source freely for years without really thinking about it. Modern apps are layers of dependencies, and when something goes wrong in one of them, fixing it can cascade through an entire stack. For large orgs with legacy codebases, that's not an afternoon fix. And moving fast has its own risks now. AI has supercharged supply chain attacks, too. Rush to patch a vulnerability without careful review, and you might install malware that's worse than the original problem.

The maintainer side is even harder. Especially for the massive chunk of maintainers who care and want to help. Many don't, and that's completely fine. They owe their downstreams nothing. Some of the most critical software on the internet is maintained by one or two people in their spare time. Automated scanners and AI-generated reports have already been burying them in low-quality noise for years. And unlike commercial software, open source maintainers don't have contracts or SLAs. There's no guarantee a patch gets written, merged, or that the person is even reachable.

Coordinated vulnerability disclosure was designed for a world where finding a serious vulnerability took weeks of expert work and the targets were a small set of well-known projects. A model can now find hundreds overnight in the long tail. The existing system is not going to keep up, and we all need a backup plan for the vulnerabilities that don't get patched.

## What actually needs to happen

We need a Plan A and a Plan B.

Plan A: coordinated disclosure that actually works at scale. A single, trusted group that routes fully vetted reports and patches upstream, and supports the maintainers who want help. Not a dozen competing groups filing noisy tickets. One coordinated effort that maintainers recognize and trust, so their reports get bubbled to the top of every inbox. Right now, Glasswing has managed to get about 6% of its findings upstreamed. This program will never reach 100%. That's not how the long tail of open source works. My best guess is that we can get normal coordinated disclosure working, under hard time crunches, for maybe 50% of projects at best. And it's going to take a lot of work to get there.

Plan B: how we deal with the rest. And it's not a clean split. There's a huge messy middle of projects where the maintainer responds but can't ship a fix in time, or where a patch exists but nobody downstream picks it up. For all of those, and for the projects where maintainers can't or won't patch at all, we need a maintainer of last resort. Open source gives you the right to fork. To take a project, assume stewardship, and keep it alive independently. Forking dead or unresponsive projects already happens every day. But in a world with hundreds of vulnerabilities being reported by dozens of groups, we need to centralize in one place to maintain those forks that end users can trust. It's going to involve hard calls and hurt feelings, but it's the only way we avoid fragmentation.

A year ago, this wouldn't have been possible at scale. Now it is. The same AI capabilities creating this crisis are what make a maintainer of last resort viable. That function needs to live somewhere sustainably funded, staffed, neutral, and trusted.

The best time to fix a dependency tree was 20 years ago. The next best time is now. And the saying goes: if you want to go fast, go alone. If you want to go far, go together. The problem is we need to do both.

## Three forks in the road

So what do we actually do? There are three ways this plays out, depending on how much of this problem you think is someone else's to solve, and how long it takes us to figure out no one is coming to save us and actually get our shit together.

The naive one: you do nothing and hope. Glasswing patches everything upstream, your vendor magically sandboxes every workload so nothing can escape, your team rewrites your legacy deployment pipeline to ship every sixty seconds, and your CISO sleeps through the night for the first time since 2014. Every maintainer responds to every disclosure within 24 hours. Every company updates every dependency the day a patch lands. Nobody introduces a regression. Nobody installs malware disguised as a patch. I want to live in this world. We do not live in this world.

The chaotic one: nobody centralizes. Every major cloud provider forks its own versions of critical libraries, each with its own patch sets. Three different security vendors ship competing forks of the same logging framework. Your team is left trying to figure out which version of which fork has which CVEs fixed, and whether any of them introduced new ones. This is the default if we do nothing.

The hard fork: a deliberate, coordinated, painful decision to build new trust infrastructure for open source consumption. One disclosure pipeline that works at scale. One trusted place for maintained forks. Hard calls about which projects get forked and which forks survive. This is the most difficult option, and it's the only real one.

Open source has always had a mechanism for this. When a project can't or won't adapt, you fork it. You take stewardship, you do the work, and you move forward. That's the deal. It's always been the deal.

What's different now is the scale. We're not talking about forking one project. We're talking about building the infrastructure to fork, maintain, and distribute thousands of them. Under time pressure, with real adversaries on the other side. That's the hardest fork any of us has ever had to make.

The same AI capabilities that created this crisis are the ones that make it possible. Software is going to change in ways that would have been unimaginable a year ago, and I think there's a brighter future on the other side.

Is any of this actually going to work? I honestly have no idea. But we have to start, and as the Programmer's Credo says, "We do this not because it is easy, but because we thought it would be easy when we started." This one doesn't even feel easy at the start.

*Get the latest on the
[Chainguard blog](https://www.chainguard.dev/unchained)
.*

**Note:**
*This article is expertly written and contributed by Dan Lorenc, CEO and Co-founder, Chainguard.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.