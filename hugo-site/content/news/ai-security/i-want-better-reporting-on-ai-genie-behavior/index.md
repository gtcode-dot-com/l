---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T02:33:27.640107+00:00'
exported_at: '2026-10-07T02:33:32.164022+00:00'
feed: https://www.schneier.com/feed/atom/
language: en
source_url: https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html
structured_data:
  about: []
  author: ''
  description: AI systems are regularly completing tasks in ways that their prompters
    don’t want or intend. Some of them are disturbing, and some of them are dangerous.
    This is something I’ve been calling “genie behavior,” because I think that really
    gets at the core of what’s happening. I wish the popular press would report on
    th...
  headline: I Want Better Reporting on AI Genie Behavior
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: I Want Better Reporting on AI Genie Behavior
updated_at: '2026-10-07T02:33:27.640107+00:00'
url_hash: 70870b7268f95bbea66034604da3e531b85bd5c0
---

## I Want Better Reporting on AI Genie Behavior

AI systems are regularly completing tasks in ways that their prompters don’t want or intend. Some of them are disturbing, and some of them are dangerous. This is something I’ve been calling “
[genie](https://www.lawfaremedia.org/article/ais-as-modern-genies)
[behavior](https://www.theguardian.com/commentisfree/2026/jul/28/rogue-ai-agent-instructions)
,” because I think that really gets at the core of what’s happening.

I wish the popular press would report on this better. I don’t like the “going rogue” framing because it deflects the responsibility from the prompters—often the AI companies themselves. And now, pretty much anything off-script is being called “hacking.”

Take, for example, the recent stories of one of OpenAI’s models hacking into government systems. First,
*The New York Times*
[writes](https://www.nytimes.com/2026/09/25/technology/openais-ai-us-government-websites.html)
this headline: “OpenAI’s Systems Meddled With U.S. Government Sites After Going Rogue.”

Sounds scary, but this is from the body of the article:

&gt; With the Education Department, OpenAI’s technology tried to hack the website to gather data from the department’s civil rights office but failed, researchers from the A.I. research firm Transluce said. The A.I. also pulled data from the Census Bureau website, which is housed at the Commerce Department, using login credentials it found online. Separately, OpenAI’s agents shared public data from the S.E.C. website on an online forum.

[This](https://transluce.org/agent-activity)
is from the original Transluce report. It is explicit that the agents were trying to discover vulnerabilities:

&gt; The first hacking attempt was against the University of New Mexico’s Digital Library (nmdigital.unm.edu) from May 25-26 2026. Agents repeatedly tried to retrieve one photograph in UNM’s Valmora collection, both directly and through third-party relay services. They sent seven probes attempting to verify the existence of vulnerabilities, including SQL injection, command injection, and path traversals. In all cases, these tactics appear to have been unsuccessful. The agents also sent a self-described “flood: of 80 requests to the UNM server in an apparent attempt to access the image.

Transluce doesn’t talk about the other two anecdotes, and I don’t know where they come from. But one involves using Census Bureau credentials found online. (I know from a colleague that those are incredibly easy to create; all use you need is an email address.) And the other involves sharing publicly available data.

So no actual hacking. And certainly no “meddling.”

The other story making the rounds is about Australia, from the same Transluce report. The news stories have headlines like
[“An OpenAI Agent Hacked Australia’s Health Service”](https://archive.ph/uiUkC)
and
[“Rogue OpenAI agent ‘infiltrated’ Australian government website in world first.”](https://www.bbc.com/news/articles/c6vgy0333dppo)
And Prime Minister Anthony Albanese said: “There will obviously be legal consequences on it.”

Again from Transluce’s actual report:

&gt; On June 20-21, agents attempted to exploit vulnerabilities in the Australian Institute of Health and Welfare (AIHW), a government statistics agency). The agents were tasked with finding the
&gt; *January 2022 rolling-12-month-average government cost per person for Dermatologicals across Victorian LGAs.*
&gt;
&gt; Again, the agents ran into errors, including requests blocked by Cloudflare and issues with correctly identifying Tableau parameter names. As before, they then resorted to probing for exploitable vulnerabilities. Minutes after Cloudflare blocked the dataset download, an agent sent a reflected cross-site scripting probe to the same dashboard: a web address with code embedded in it, designed to test whether the site would run code supplied by an outsider. Cloudflare’s firewall blocked the probe before it reached the dashboard. When Cloudflare blocked the dataset download on AIHW’s main site, they fetched the file from AIHW’s pre-production server (pp.aihw.gov.au) instead, which served it in pieces over more than 100 scans. The file itself is public, so no non-public data was exposed, but the agent bypassed the site’s anti-bot controls.

Note the last sentence: “The file itself is public….”

I’m not saying that these AI systems aren’t incredibly sophisticated cyberattackers. I’m also not saying that they don’t occasionally autonomously attack other systems and networks. If we are ever going to get trustworthy AI—
[integrous AI](https://www.schneier.com/essays/archives/2025/12/building-trustworthy-ai-agents.html)
—we are going to need to figure out how to ensure that AI systems complete tasks in line with all sorts of implicit constraints and restrictions. But every instance of genie-like behavior isn’t a cyberattack.

I want to
[measure](https://spectrum.ieee.org/ai-agent-benchmark)
genie-like behavior in AIs, but I am much more worried about human hackers enhanced with this technology than I am about this technology acting autonomously.

Tags:
[AI](https://www.schneier.com/tag/ai/)
,
[cyberattack](https://www.schneier.com/tag/cyberattack/)

[Posted on September 30, 2026 at 7:05 AM](https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html)
•
[24 Comments](https://www.schneier.com/blog/archives/2026/09/i-want-better-reporting-on-ai-genie-behavior.html#comments)