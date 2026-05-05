---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-05T14:15:17.186790+00:00'
exported_at: '2026-05-05T14:15:19.761533+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/the-back-door-attackers-know-about-and.html
structured_data:
  about: []
  author: ''
  description: OAuth tokens without expiry enable breaches like Drift attack on 700+
    firms, bypassing MFA and exposing sensitive data.
  headline: The Back Door Attackers Know About — and Most Security Teams Still Haven’t
    Closed
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/the-back-door-attackers-know-about-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: The Back Door Attackers Know About — and Most Security Teams Still Haven’t
  Closed
updated_at: '2026-05-05T14:15:17.186790+00:00'
url_hash: 0422c4bf71ebf7b08933a5b48b7cd6d2900b7872
---

Every AI tool, workflow automation, and productivity app your employees connected to Google or Microsoft this year left something behind: a persistent OAuth token with no expiration date, no automatic cleanup, and in most organizations, no one watching it. Your perimeter controls don't see it. Your MFA doesn't stop it. And when an attacker gets hold of one, they don't need a password.

OAuth grants don't expire when employees leave. They don't reset when passwords change. And in most organizations, nobody is watching them.

The model made sense when a handful of IT-approved apps needed calendar access. It doesn't hold up when every employee is independently wiring AI tools, workflow automations, and productivity apps directly into their Google or Microsoft environment — each one receiving a persistent, scoped token with no automatic expiration and no centralized visibility.

That's not a misconfiguration. It's how OAuth is designed to work. The gap is that most security programs weren't built to account for it at scale.

## CISOs know it's a problem. Most aren't solving it.

[New research from Material Security](https://material.security/resources/automating-oauth-grant-management-materials-research-shows-the-growing-gap-between-awareness-and-action?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news)
quantifies the gap between awareness and action. 80% of security leaders consider unmanaged OAuth grants a critical or significant risk. Most have said as much for years.

But awareness doesn't translate directly into capability.  A substantial portion of organizations (45%) are doing nothing to monitor OAuth grants at scale. Many of the rest (33%) are running manual processes — tracking grants in spreadsheets, reviewing permissions on an ad hoc basis, relying on employees to flag unusual app behavior.

Spreadsheets are not a threat response capability. They're a record of how much exposure an organization doesn't know it has.

## It's not theoreticalrisk

The argument for OAuth visibility often gets framed as employees piping sensitive information into third-party tools without IT visibility. That's a real problem, but it's the smaller one. The more pressing issue is that OAuth grants are an active attack vector. The
[Drift incident](https://material.security/resources/the-supply-chain-is-the-new-watering-hole?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news)
makes that concrete.

Drift, a sales engagement platform acquired by Salesloft, maintained OAuth integrations with Salesforce instances across hundreds of customer organizations. A threat actor tracked by Palo Alto Unit 42 as UNC6395 obtained valid OAuth refresh tokens — likely through prior phishing campaigns — and used them to access Salesforce environments belonging to more than 700 organizations.

The attack's structure is a warning: the tokens were legitimate, the integration was legitimate. From the perspective of any perimeter control, nothing was wrong. MFA was bypassed entirely because the attacker wasn't logging in — they were presenting a token that Drift had already been granted permission to use. Once inside, UNC6395 systematically exported data and combed through it for credentials: AWS access keys, Snowflake tokens, passwords.

Cloudflare, PagerDuty, and dozens of others were affected. The full scope is still being assessed.

The Drift incident wasn't an attack from a suspicious, unknown app. It was an attack
*through*
a trusted one. The lesson isn't that organizations should restrict OAuth integrations — it's that trusting an app at the time of installation doesn't mean it stays trustworthy, and that OAuth grants need active, continuous monitoring rather than passive acceptance.

## What monitoring actually needs to look like

The current generation of OAuth security tools addresses OAuth risk at the point of installation. They check whether a requested permission scope is excessive. They may flag apps from vendors with poor reputations. That's useful — but it's not sufficient. For the Drift scenario, a legitimate app whose credentials were later stolen and weaponized — it catches nothing.

To begin with, vendor trust levels and app scopes are important, but it only tells part of the story. Monitoring the actual behavior of the app–the API calls it makes, the actions it takes–is critical to understanding what the app is
*actually*
doing, not just what it could do. And even then, without deep visibility into the account(s) the app is linked to, you’re still operating half-blind. A risky app tied to an intern’s account is one thing–the same app being used by a VIP with access to countless sensitive emails, files, and systems is something else entirely.

The Drift attack didn't involve a suspicious app requesting unusual permissions at installation. It involved a legitimate app whose credentials were later compromised and weaponized. A tool that only evaluates the grant at the point of creation would have seen nothing wrong. The risk materialized later — when the token was stolen and used by a different actor entirely.

Effective OAuth security requires:

* **Continuous behavioral monitoring, not point-in-time review.**
  What is the app actually doing after it's been granted access? Monitoring the API calls an OAuth-connected app makes over time reveals anomalies that no static permission review can catch — sudden spikes in data access, queries for unusual data types, andaccess at unexpected hours.
* **Blast radius assessment.**
  An OAuth grant connected to an account with read access to thousands of sensitive documents and years of email history is categorically different from the same grant on a freshly provisioned account with limited exposure. The reach of the user's account determines the potential impact of a compromised or malicious OAuth connection. Risk scoring should reflect that.
* **Graduated response matched to organizational risk tolerance.**
  An obviously malicious app — unknown vendor, broad permissions, anomalous API behavior from day one — shouldn't sit in the environment while a ticket works through a queue. It should be revoked immediately. A mission-critical integration from a major vendor showing mild anomalies warrants human review before any action is taken. The response layer needs to be intelligent enough to tell the difference.

## Material's OAuth Threat Remediation Agent

Material Security's
[OAuth Threat Remediation Agent](https://material.security/resources/closing-the-back-door-introducing-materials-oauth-remediation-agent?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news)
is built around this more complete model of OAuth risk. The agent runs continuously across an organization's Google Workspace environment, monitoring every OAuth-connected application — not just new ones at the point of grant.

VIDEO

For each connected app, the agent evaluates three factors together:

* **Vendor trust and scope analysis**
  — the standard baseline that most tools stop at
* **Behavioral monitoring of actual API calls**
  made by the app over time, surfacing anomalies against expected behavior
* **Blast radius assessment**
  based on the access levels and data exposure of the accounts the app is connected to

These inputs combine into a risk signal that reflects both the probability of a problem and its potential impact. When the agent identifies a high-risk grant, it can act immediately — revoking the token before harm is done. For lower-certainty situations involving mission-critical applications, it surfaces the finding to the security team with full context: what the app is, what it's been doing, what it has access to, and what the risk score is.

Organizations configure their own thresholds: how much risk triggers automated remediation, and where the line is for requiring human sign-off. The agent is designed to keep security teams in the loop for the decisions that matter, and out of the loop for the ones that don't.

## Closing the back door

OAuth grants are the default way third-party apps and AI tools connect to the enterprise workspace. That's not changing. The number of grants in most environments will continue to grow as AI adoption accelerates. Telling employees they can't use AI tools isn't a viable security posture for most organizations — and it wouldn't address the threat posed by apps that are legitimate at installation and malicious later.

The answer isn't fewer OAuth grants. It's better visibility into the ones that exist, continuous monitoring of their behavior, and the operational capability to respond fast enough to matter and smart enough to avoid disrupting the integrations that keep the business running.

For security teams who want visibility into what's actually connected to their environment — and the ability to respond when something changes, reach out to
[Material Security](https://material.security/lp-cloud-office-security?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news)
for a demo of the
[OAuth Threat Remediation Agent](https://material.security/product/oauth-agent?utm_source=third-party&utm_medium=blog&utm_campaign=20260505-the-hacker-news)
.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.