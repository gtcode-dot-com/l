---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:53:59.968607+00:00'
exported_at: '2026-06-23T03:54:03.340960+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/stop-your-legacy-infrastructure-from.html
structured_data:
  about: []
  author: ''
  description: AI agents inherit risk from legacy servers, AD, IAM, and cloud storage,
    creating attack paths that bypass model-level security.
  headline: Stop Your Legacy Infrastructure from Hijacking Your AI Agents
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/stop-your-legacy-infrastructure-from.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Stop Your Legacy Infrastructure from Hijacking Your AI Agents
updated_at: '2026-06-23T03:53:59.968607+00:00'
url_hash: 6867fc8dafccd650a4e13e518efd05207b1ead43
---

Earlier this month, I spoke at the
[Gartner Security &amp; Risk Management Summit](https://www.gartner.com/en/conferences/na/security-risk-management-us)
about a blind spot most security programs are still not accounting for - how attackers are circumventing AI security programs by using legacy infrastructure to hijack AI agents.

AI adoption is moving faster than security programs can account for. Roughly 71% of organizations are piloting AI agents across their enterprise applications, and 31% have already moved them into production workflows.

For this reason, organizations are legitimately pouring resources into securing AI workloads against model poisoning, prompt injection, data leakage, and other emerging threats. Yet this focus misses everything
*underneath*
the AI layer. Because an unpatched server, a misconfigured Active Directory permission, or a cached credential on a developer's machine are exposures that give attackers a direct route to everything your AI agents depend on - knowledge bases, cloud storage, Lambda functions, SaaS integrations, and the credentials that connect them.

This means that threat actors don’t really need to attack your AI head-on -
*they just need to reach what it connects to.*
In this article, I'll walk through how legacy infrastructure becomes the attack path into AI agent environments and what security teams can do to block those paths.

## **AI Agents Use What They Inherit**

Despite their novelty and power, in some ways AI agents operate like other assets in your environment. They authenticate through existing identity providers, store data in existing cloud buckets, execute tasks through existing Lambda functions, and inherit permissions from existing IAM roles. Every one of those dependencies carries whatever security debt the organization had before the AI deployment started.

What’s more, most organizations are inadvertently
*compounding*
that debt. According to
[Infosecurity Magazine](https://www.infosecurity-magazine.com/news/overprivileged-ai-45-times-higher/)
, 70% of organizations grant their AI systems
*more*
privileged access than a human in the same role. Not surprisingly, this comes with a painful price tag. Organizations with over-privileged AI reported a 76% incident rate, compared to just 17% for those enforcing least privilege.

All of those connections - identity providers, cloud buckets, Lambda functions, IAM roles - run through the infrastructure your teams have managed for years: Active Directory, cloud IAM, service accounts, stored credentials. Yet none of it was designed with AI agents in mind, and most of it was provisioned long before the first agent went into production. The result is that an attacker who finds their way in through any of those layers doesn't need to touch the AI. The agent's own permissions do the work for them.

## **How a CVE from 2025 Hijacks an AI Agent in 2026**

The diagram below shows a typical enterprise AI agent architecture. A customer success team uses an AI-powered Co-Pilot - hosted on AWS Bedrock - to query customer data exported from Salesforce into an S3 bucket. The Co-Pilot executes tasks through Lambda functions and integrates with business applications. John, a developer, builds and maintains the agent. Users across the organization interact with it daily.

Now here's what happens when an attacker finds a way in. The following diagram shows an attack path my team modeled in a real enterprise environment. None of these exposures are exotic - they exist, in some combination, in most enterprise networks right now. What makes them dangerous is how they connect. Here is how the attack developed, stage-by-stage.

* **Stage 1: An S3 bucket becomes a critical asset.**
  To feed the CSM Co-Pilot, the team exported Salesforce data into an S3 bucket. That export turned the bucket into a high-value target holding sensitive customer records. Multiple users across the AWS account received overly broad read access to production S3 buckets - including John, the Co-Pilot developer, who never needed access to production data. On its own, this is a simple permissions misconfiguration.
* **Stage 2: An unpatched server on the perimeter.**
  An external-facing server runs Apache Tomcat. That server is exposed to
  [CVE-2025-24813](https://nvd.nist.gov/vuln/detail/CVE-2025-24813)
  - a remote code execution flaw disclosed in March 2025 and added to CISA's Known Exploited Vulnerabilities catalog the same month. It was never patched. Because the server sits in the enterprise environment and is joined to Active Directory, an attacker who exploits the vulnerability can dump cached credentials from server memory and compromise an AD user account. In isolation, this is a known vulnerability on a single server - serious, but not critical.
* **Stage 3: Active Directory misconfiguration enables lateral movement.**
  That compromised AD account can abuse a Resource-Based Constrained Delegation misconfiguration to impersonate John and access his workstation. John uses AWS CLI to manage the Co-Pilot's cloud resources, and behind the scenes, CLI stores AWS access keys on his machine. The attacker harvests those keys. In isolation, this is an AD permissions issue - one of thousands that most environments carry.
* **Now connect the three stages.**
  The attacker exploits CVE-2025-24813 on the perimeter, dumps credentials, moves laterally through AD to John's workstation, harvests his AWS access keys, and reads every record in the production S3 bucket - the same bucket that feeds the Co-Pilot's knowledge base.
  *The Co-Pilot agent is now compromised.*
  The attacker controls what it reads, what it trusts, and what it returns to users. No part of the AI stack was directly attacked. Three moderate findings - an overprivileged cloud key, an unpatched web server, an AD misconfiguration - became one critical attack path.

## **What to Do About It**

The attack path I just described crosses four layers: network, identity, cloud, and AI. Most security programs assess each of those layers independently, and the exposures in each one may already be known. An EASM tool flags the Tomcat server. An AD security tool catches the delegation misconfiguration. A CSPM tool picks up the overprivileged S3 access. Each one reports a moderate finding which may not be remediated due to lower priority but in combination become a critical issue: a Tomcat vulnerability on the perimeter chains through AD into a developer's cloud credentials and ends at an AI agent's knowledge base.

Closing these paths starts with an exposure management approach that treats AI agent dependencies (knowledge bases, storage buckets, Lambda functions, etc) as critical assets themselves. From there, map backward: what identity relationships, permissions, and infrastructure connect to those assets, and which of those connections carry exploitable exposures in the context of your environment? When you map the full path, choke points emerge - places where a single fix will block multiple routes to your AI assets.

If your exposure management platform can trace that full path - from legacy server through AD and cloud infrastructure to an AI agent's knowledge base - you can fix the exposure before an attacker chains it. If it can't, no amount of guardrails on the AI layer will close it.

## **The Bottom Line**

AI agent adoption is accelerating across every enterprise department. And every new agent you deploy connects to infrastructure that is already exposed. That means that the attack surface compounds with every deployment.

The question for security leaders isn't whether your AI layer is protected. It's whether the environment in which those agents operate - including your bread-and-butter legacy infrastructure - is handing attackers the path to hijack them.

Because attackers don't need new techniques to compromise AI agents. They just need the old ones - and an environment that lets them use the old to exploit the new.

**Note:**
*This article was thoughtfully written and contributed for our audience*
by
[Zur Ulianitzky](https://www.linkedin.com/in/zur-ulianitzky-782020138/)
, SVP Product and Security Research, XM Cyber.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.