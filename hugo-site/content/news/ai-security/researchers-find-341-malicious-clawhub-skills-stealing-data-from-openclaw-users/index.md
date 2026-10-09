---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T20:15:14.375762+00:00'
exported_at: '2026-02-02T20:15:16.878280+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
structured_data:
  about: []
  author: ''
  description: A security audit found 341 malicious ClawHub skills abusing OpenClaw
    to spread Atomic Stealer and steal credentials on macOS and Windows.
  headline: Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw
    Users
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/researchers-find-341-malicious-clawhub.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Researchers Find 341 Malicious ClawHub Skills Stealing Data from OpenClaw Users
updated_at: '2026-02-02T20:15:14.375762+00:00'
url_hash: 83616ea2c387d7f75eb367101cd7db1be6fa3b8e
---

A security audit of 2,857 skills on ClawHub has found 341 malicious skills across multiple campaigns, according to
[new findings](https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting)
from Koi Security, exposing users to new supply chain risks.

[ClawHub](https://www.clawhub.ai/skills)
is a marketplace designed to make it easy for
[OpenClaw](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
users to find and install third-party skills. It's an extension to the OpenClaw project, a self-hosted artificial intelligence (AI) assistant formerly known as both Clawdbot and Moltbot.

The analysis, which Koi conducted with the help of an OpenClaw bot named Alex, found that 335 skills use fake pre-requisites to install an Apple macOS stealer named
[Atomic Stealer](https://thehackernews.com/2025/06/new-atomic-macos-stealer-campaign.html)
(AMOS). This set has been codenamed
**ClawHavoc**
.

"You install what looks like a legitimate skill – maybe solana-wallet-tracker or youtube-summarize-pro," Koi researcher Oren Yomtov said. "The skill's documentation looks professional. But there's a 'Prerequisites' section that says you need to install something first."

This step involves instructions for both Windows and macOS systems: On Windows, users are asked to download a file called "openclaw-agent.zip" from a GitHub repository. On macOS, the documentation tells them to copy an installation script hosted at glot[.]io and paste it into the Terminal app. The targeting of macOS is no coincidence, as reports have
[emerged](https://www.businessinsider.com/clawdbot-ai-mac-mini-2026-1)
of people
[buying Mac Minis](https://mashable.com/article/jan-31-apple-mac-mini-deal)
to run the AI assistant 24x7.

Present within the password-protected archive is a trojan with keylogging functionality to capture API keys, credentials, and other sensitive data on the machine, including those that the bot already has access to. On the other hand, the glot[.]io script contains obfuscated shell commands to fetch next-stage payloads from an attacker-controlled infrastructure.

This, in turn, entails reaching out to another IP address ("91.92.242[.]30") to retrieve another shell script, which is configured to contact the same server to obtain a universal Mach-O binary that exhibits traits consistent with Atomic Stealer, a commodity stealer available for $500-1000/month that can harvest data from macOS hosts.

According to Koi, the malicious skills masquerade as

* ClawHub typosquats (e.g., clawhub, clawhub1, clawhubb, clawhubcli, clawwhub, cllawhub)
* Cryptocurrency tools like Solana wallets and wallet trackers
* Polymarket bots (e.g., polymarket-trader, polymarket-pro, polytrading)
* YouTube utilities (e.g., youtube-summarize, youtube-thumbnail-grabber, youtube-video-downloader)
* Auto-updaters (e.g., auto-updater-agent, update, updater)
* Finance and social media tools (e.g., yahoo-finance-pro, x-trends-tracker)
* Google Workspace tools claiming integrations with Gmail, Calendar, Sheets, and Drive
* Ethereum gas trackers
* Lost Bitcoin finders

In addition, the cybersecurity company said it identified skills that hide reverse shell backdoors inside functional code (e.g., better-polymarket and polymarket-all-in-one), or exfiltrate bot credentials present in "~/.clawdbot/.env" to a webhook[.]site (e.g., rankaj).

The development coincides with a report from OpenSourceMalware, which also flagged the same ClawHavoc campaign targeting OpenClaw users.

"The skills masquerade as cryptocurrency trading automation tools and deliver information-stealing malware to macOS and Windows systems," a security researcher who goes by the online alias 6mile
[said](https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto)
.

"All these skills share the same command-and-control infrastructure (91.92.242[.]30) and use sophisticated social engineering to convince users to execute malicious commands, which then steal crypto assets like exchange API keys, wallet private keys, SSH credentials, and browser passwords."

## OpenClaw Adds a Reporting Option

The problem stems from the fact that ClawHub is open by default and allows anyone to upload skills. The only restriction at this stage is that a publisher must have a GitHub account that's at least one week old.

The issue with malicious skills
[hasn't gone unnoticed](https://x.com/steipete/status/2018297794952651111)
by OpenClaw's creator Peter Steinberger, who has since rolled out a reporting feature that allows signed-in users to flag a skill. "Each user can have up to 20 active reports at a time," the documentation
[states](https://docs.openclaw.ai/tools/clawhub#security-and-moderation)
. "Skills with more than 3 unique reports are auto-hidden by default."

The findings underscore how open-source ecosystems continue to be abused by threat actors, who are now piggybacking on OpenClaw's sudden popularity to orchestrate malicious campaigns and distribute malware at scale.

In a report last week, Palo Alto Networks warned that OpenClaw represents what British programmer Simon Willison, who coined the term prompt injection, describes as a "
[lethal trifecta](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)
" that renders AI agents vulnerable by design due to their access to private data, exposure to untrusted content, and the ability to communicate externally.

The intersection of these three capabilities, combined with OpenClaw's persistent memory, "acts as an accelerant" and amplifies the risks, the cybersecurity company added.

"With persistent memory, attacks are no longer just point-in-time exploits. They become stateful, delayed-execution attacks," researchers Sailesh Mishra and Sean P. Morgan
[said](https://www.paloaltonetworks.com/blog/network-security/why-moltbot-may-signal-ai-crisis/)
. "Malicious payloads no longer need to trigger immediate execution on delivery. Instead, they can be fragmented, untrusted inputs that appear benign in isolation, are written into long-term agent memory, and later assembled into an executable set of instructions."

"This enables time-shifted prompt injection, memory poisoning, and logic bomb–style activation, where the exploit is created at ingestion but detonates only when the agent's internal state, goals, or tool availability align."