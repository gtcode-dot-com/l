---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T06:15:16.777816+00:00'
exported_at: '2026-04-02T06:15:19.134321+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html
structured_data:
  about: []
  author: ''
  description: Claude Code 2.1.88 leak exposed 512,000 lines via npm error, fueling
    supply chain risks and typosquatting attacks.
  headline: Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Claude Code Source Leaked via npm Packaging Error, Anthropic Confirms
updated_at: '2026-04-02T06:15:16.777816+00:00'
url_hash: 965dbcee4ca3147bfe4c8cdd1169de3571690b18
---

**

Ravie Lakshmanan
**

Apr 01, 2026

Data Breach / Artificial Intelligence

Anthropic on Tuesday confirmed that internal code for its popular artificial intelligence (AI) coding assistant, Claude Code, had been inadvertently released due to a human error.

"No sensitive customer data or credentials were involved or exposed," an Anthropic spokesperson
[said](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html)
in a statement shared with CNBC News. "This was a release packaging issue caused by human error, not a security breach. We’re rolling out measures to prevent this from happening again."

The discovery came after the AI upstart released
[version 2.1.88](https://www.npmjs.com/package/@anthropic-ai/claude-code?activeTab=versions)
of the Claude Code npm package, with users spotting that it contained a source map file that could be used to access Claude Code's source code – comprising nearly 2,000 TypeScript files and more than 512,000 lines of code. The version is no longer available for download from npm.

Security researcher Chaofan Shou was the first to
[publicly flag](https://x.com/Fried_rice/status/2038894956459290963)
it on X, stating "Claude code source code has been leaked via a map file in their npm registry!" The X post has since amassed more than 28.8 million views. The leaked codebase remains accessible via a
[public GitHub repository](https://github.com/instructkr/claw-code)
, where it has surpassed 84,000 stars and 82,000 forks.

A source code leak of this kind is significant, as it gives software developers and Anthropic's competitors a blueprint for how the popular coding tool works. Users who have
[dug into the code](https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/)
have published details of its
[self-healing memory architecture](https://x.com/himanshustwts/status/2038924027411222533)
to overcome the model's
[fixed context window constraints](https://x.com/troyhua/status/2039052328070734102)
, as well as other internal components.

These
[include](https://dev.to/gabrielanhaia/claude-codes-entire-source-code-was-just-leaked-via-npm-source-maps-heres-whats-inside-cjo)
a tools system to facilitate various capabilities like file read or bash execution, a query engine to handle LLM API calls and orchestration, multi-agent orchestration to spawn "sub-agents" or swarms to carry out complex tasks, and a bidirectional communication layer that connects IDE extensions to Claude Code CLI.

The leak has also shed light on a feature called
[KAIROS](https://x.com/itsolelehmann/status/2039018963611627545)
that allows Claude Code to operate as a persistent, background agent that can periodically fix errors or run tasks on its own without waiting for human input, and even send push notifications to users. Complementing this proactive mode is a
[new "dream" mode](https://x.com/AlexFinn/status/2039005703160172723)
that will allow Claude to constantly think in the background to develop ideas and iterate existing ones.

Perhaps the most intriguing detail is the tool's Undercover Mode for making "stealth" contributions to open-source repositories. "You are operating UNDERCOVER in a PUBLIC/OPEN-SOURCE repository. Your commit messages, PR titles, and PR bodies MUST NOT contain ANY Anthropic-internal information. Do not blow your cover," reads the system prompt.

Another fascinating finding involves Anthropic's attempts to covertly fight
[model distillation attacks](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html)
. The system has
[controls in place](https://x.com/nyk_builderz/status/2039004963943133589)
that inject fake tool definitions into API requests to poison training data if competitors attempt to scrape Claude Code's outputs.

### Typosquat npm Packages Pushed to Registry

With Claude Code's internals now laid bare, the development risks providing bad actors with ammunition to bypass guardrails and trick the system into performing unintended actions, such as running malicious commands or exfiltrating data.

"Instead of brute-forcing jailbreaks and prompt injections, attackers can now study and fuzz exactly how data flows through Claude Code's four-stage context management pipeline and craft payloads designed to survive compaction, effectively persisting a backdoor across an arbitrarily long session," AI security company Straiker
[said](https://www.straiker.ai/blog/claude-code-source-leak-with-great-agency-comes-great-responsibility)
.

The more pressing concern is the fallout from the
[Axios supply chain attack](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
, as users who installed or updated Claude Code via npm on March 31, 2026, between 00:21 and 03:29 UTC may have pulled with it a trojanized version of the HTTP client that contains a cross-platform remote access trojan. Users are advised to immediately downgrade to a safe version and rotate all secrets.

What's more, attackers are already capitalizing on the leak to typosquat internal npm package names in an attempt to target those who may be trying to compile the leaked Claude Code source code and stage
[dependency confusion attacks](https://thehackernews.com/2021/02/dependency-confusion-supply-chain.html)
. The names of the packages, all published by a user named "
[pacifier136](https://www.npmjs.com/~pacifier136)
," are listed below -

* audio-capture-napi
* color-diff-napi
* image-processor-napi
* modifiers-napi
* url-handler-napi

"Right now they're empty stubs (`module.exports = {}`), but that's how these attacks work – squat the name, wait for downloads, then push a malicious update that hits everyone who installed it," security researcher Clément Dumas
[said](https://x.com/Butanium_/status/2039079715823128964)
in a post on X.

The incident is the second major blunder for Anthropic within a week. Details about the company's
[upcoming AI model](https://fortune.com/2026/03/26/anthropic-leaked-unreleased-model-exclusive-event-security-issues-cybersecurity-unsecured-data-store/)
, along with other internal data, were left accessible via the company's content management system (CMS) last week. Anthropic subsequently acknowledged it's been testing the model with early access customers, stating it's "most capable we've built to date," per
[Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/)
.