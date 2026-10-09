---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T17:57:48.938479+00:00'
exported_at: '2026-06-23T17:57:51.927256+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html
structured_data:
  about: []
  author: ''
  description: AIR says its fake AI skill passed scanner checks by using a mutable
    external link, exposing a blind spot in agent skill vetting.
  headline: Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000
    Agents
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/fake-ai-agent-skill-passed-security.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Fake AI Agent Skill Passed Security Scans and Reportedly Reached 26,000 Agents
updated_at: '2026-06-23T17:57:48.938479+00:00'
url_hash: 0b83c8e24935ba1965fe7318f614162734396f2e
---

Security firm AIR built a fake AI agent skill, pushed it through a popular skill marketplace and an Instagram ad, and says it reached roughly 26,000 agents, including some on corporate accounts.

Every skill security scanner the firm tested it against marked it safe. The payload was harmless by design: it collected the user's email address and did nothing else.

The point was to show that none of the signals people lean on to trust a skill caught it: not the scanners, not the GitHub stars, not the open-source reputation.

A skill is a bundle of instructions an agent loads into its own context and follows with roughly the authority of a user prompt. That trust is the whole problem, and it is the reason skill-scanning tools exist in the first place.

The skill, named
**brand-landingpage**
, claimed to build a landing page using Google's Stitch design tool, aimed squarely at non-technical users.

To make it look credible, AIR went after two trust signals: GitHub stars and a clean scanner verdict. For the stars, it opened a pull request to a skill marketplace repository with around 36,000 stars and 156 skills.

The pull request was merged after a few days, so the skill inherited the repo's count. Then it ran an Instagram ad aimed at marketers, salespeople, and designers, who installed it and put it to work.

## Why the scanners missed it

The scanners AIR tested analyze the package you hand them: the SKILL.md and the files shipped with it. That's
[Cisco's](https://github.com/cisco-ai-defense/skill-scanner)
,
[NVIDIA's](https://github.com/nvidia/skillspector)
, and the ones wired into skills.sh.

[AIR's skill](https://www.air.security/blog-posts/the-story-of-skills)
carried no setup instructions of its own. It told the agent to install the "Stitch SDK" by following the documentation at an external link, stitch-design.ai, a domain AIR controls, not Google (the real Stitch lives at stitch.withgoogle.com).

At first, the link led to the genuine Stitch docs, so the scanners, seeing a clean package that pointed at a plausible setup page, cleared it. The page the agent would actually fetch and follow sat outside the scan.

Once the skill was installed widely, AIR swapped the page behind that link. The new version told the agent to download and run a script.

In the demo, it only mailed the user's address back to AIR, which is how the firm counted the agents it reached. A real operator could have used that foothold to read files, move data, or hit internal systems, bounded only by what the agent could reach.

AIR is not the first to show this. Three weeks earlier,
[Trail of Bits](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/)
bypassed ClawHub's malicious-skill detector, Cisco's scanner, and all three scanners wired into skills.sh. Its conclusion was blunt: a scanner checks a fixed package, while an attacker can keep tweaking the payload until it passes.

Real campaigns have used the same
[trick](https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html)
for months, keeping the submitted skill clean and hosting the payload on a site the agent only fetches at install.

The problem is structural: the scan happens once, but the page a skill points the agent to can be rewritten at any time after. Anthropic's own
[docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
already warn that skills fetching external URLs are risky for exactly this reason, since the content can change after the skill is vetted.

Separate
[research this year](https://theweatherreport.ai/posts/skill-scanner-disagreement/)
found scanners often disagree, because each one judges a skill in isolation, blind to its external links and to what changes after review.

## What to do

The read for defenders is the same one researchers keep landing on, now with a sharper example behind it. Treat skills as software, not text. Vet what a skill points to, not just what ships inside it.

Most of these add-ons got installed with no review, so the first job is finding what is already running. Route new skills through a single source you control, and re-check them when anything changes, because a clean result at install does not stay clean if the skill phones out to a link someone else can edit.

Pin versions. Hold agents to the least privilege. Assume any external instruction an agent fetches runs with the agent's access.

The scale figures come from AIR alone, and they deserve a skeptical read. The firm is launching a managed skill marketplace and closes the write-up, pitching it, so the 26,000 number, the corporate-account detail, and the claim that it could have seized full control of every agent are the company's own and are not independently confirmed.

What holds up is the method. The named scanners really do judge only the submitted package, the external-link blind spot is real and has been independently demonstrated, and the trust signals AIR borrowed, stars, and a clean scan are exactly the ones the ecosystem still treats as proof.

The experiment does not expose a new bug so much as it lines up every weak trust signal around agent skills into one run: stars that can be borrowed, a scan that reads a snapshot, and a link that can be rewritten after the check clears.

Whether the real figure is 26,000 or a fraction of it, the gap it walks through is one that defenders still have not closed.