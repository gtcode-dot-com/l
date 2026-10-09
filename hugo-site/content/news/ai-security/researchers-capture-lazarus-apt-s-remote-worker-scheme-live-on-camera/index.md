---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-03T00:03:07.933912+00:00'
exported_at: '2025-12-03T00:03:10.837017+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/researchers-capture-lazarus-apts-remote.html
structured_data:
  about: []
  author: ''
  description: Lazarus-linked IT operatives caught using fake hiring, identity theft
    tools, and ANY.RUN traps to infiltrate Western companies.
  headline: Researchers Capture Lazarus APT's Remote-Worker Scheme Live on Camera
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/researchers-capture-lazarus-apts-remote.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Capture Lazarus APT's Remote-Worker Scheme Live on Camera
updated_at: '2025-12-03T00:03:07.933912+00:00'
url_hash: 8e4de7ac9980dc49661ed6da8679badfddd03c57
---

**

Dec 02, 2025
**

The Hacker News

Identity Theft / Threat Intelligence

A joint investigation led by Mauro Eldritch, founder of
**[BCA LTD](https://bca.ltd)**
, conducted together with threat-intel initiative
**[NorthScan](https://northscan.co/)**
and
**[ANY.RUN](https://any.run)
,**
a solution for interactive malware analysis and threat intelligence, has uncovered one of North Korea's most persistent infiltration schemes: a network of remote IT workers tied to Lazarus Group's Famous Chollima division.

For the first time, researchers managed to watch the operators work
**live**
, capturing their activity on what they believed were real developer laptops. The machines, however, were fully controlled, long-running sandbox environments created by ANY.RUN.

## The Setup: Get Recruited, Then Let Them In

|  |
| --- |
|  |
| Screenshot of a recruiter message offering a fake job opportunity |

The operation began when NorthScan's
**Heiner García**
impersonated a U.S. developer targeted by a Lazarus recruiter using the alias "Aaron" (also known as "Blaze").

Posing as a job-placement "business," Blaze attempted to hire the fake developer as a frontman; a known Chollima tactic used to slip North Korean IT workers into Western companies, mainly in the
**finance, crypto, healthcare, and engineering**
sectors.

|  |
| --- |
|  |
| The process of interviews |

The scheme followed a familiar pattern:

* steal or borrow an identity,
* pass interviews with AI tools and shared answers,
* work remotely via the victim's laptop,
* funnel salary back to DPRK.

Once Blaze asked for full access, including SSN, ID, LinkedIn, Gmail, and 24/7 laptop availability, the team moved to phase two.

## The Trap: A "Laptop Farm" That Wasn't Real

|  |
| --- |
|  |
| A safe virtual environment provided by ANY.RUN's Interactive Sandbox |

Instead of using a real laptop, BCA LTD's Mauro Eldritch deployed the ANY.RUN Sandbox's virtual machines, each configured to resemble a fully active personal workstation with usage history, developer tools, and U.S. residential proxy routing.

The team could also force crashes, throttle connectivity, and snapshot every move without alerting the operators.

## What They Found Inside the Famous Chollima's Toolkit

The sandbox sessions exposed a lean but effective toolset built for identity takeover and remote access rather than malware deployment. Once their Chrome profile synced, the operators loaded:

* **AI-driven job automation tools**
  (Simplify Copilot, AiApply, Final Round AI) to auto-fill applications and generate interview answers.
* **Browser-based OTP generators**
  (OTP.ee / Authenticator.cc) for handling victims' 2FA once identity documents were collected.
* **Google Remote Desktop**
  , configured via PowerShell with a fixed PIN, providing persistent control of the host.
* Routine
  **system reconnaissance**
  (dxdiag, systeminfo, whoami) to validate the hardware and environment.
* Connections consistently routed through
  **Astrill VPN**
  , a pattern tied to previous Lazarus infrastructure.

In one session, the operator even left a Notepad message asking the "developer" to upload their ID, SSN, and banking details, confirming the operation's goal: full identity and workstation takeover without deploying a single piece of malware.

## A Warning for Companies and Hiring Teams

Remote hiring has become a quiet but reliable entry point for identity-based threats. Attackers often reach your organization by targeting individual employees with seemingly legitimate interview requests. Once they're inside, the risk goes far beyond a single compromised worker. An infiltrator can gain access to internal dashboards, sensitive business data, and manager-level accounts that carry real operational impact.

Raising awareness inside the company and giving teams a safe place to check anything suspicious can be the difference between stopping an approach early and dealing with a full-blown internal compromise later.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.