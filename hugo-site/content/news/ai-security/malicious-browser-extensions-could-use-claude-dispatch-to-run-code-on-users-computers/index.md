---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-13T01:16:56.293496+00:00'
exported_at: '2026-11-13T01:16:57.367444+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
structured_data:
  about: []
  author: ''
  description: Researchers show how browser extensions can abuse Claude Dispatch to
    approve prompts and execute code through Claude Desktop.
  headline: Malicious Browser Extensions Could Use Claude Dispatch to Run Code on
    Users' Computers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/malicious-browser-extensions-could-use.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Malicious Browser Extensions Could Use Claude Dispatch to Run Code on Users'
  Computers
updated_at: '2026-11-13T01:16:56.293496+00:00'
url_hash: cea41b0360f6d3578779ae8c26263c160a49f1a5
---

**

Swati Khandelwal
**

Nov 06, 2026

Artificial Intelligence / Browser Security

A browser extension that can run scripts on claude.ai could make Claude Desktop run code on a person's computer, researchers at Forever Security, an endpoint security company, showed in a test.

The attack needs
**Dispatch**
, a Claude feature that lets people send tasks from their phone to Claude Desktop. The flaw that makes this possible can still be exploited, the researchers said earlier this week.

Claude Desktop is an AI agent that can run commands on the computer where it is installed. The researchers found that Dispatch also accepted an ordinary signed-in session on claude.ai, the Claude website, even though the site showed no link to it. That let an extension running on the site send Claude Desktop instructions as if the user had sent them.

The researchers say Anthropic, the company that makes Claude, told them on October 13 that Dispatch would be retired, with the end of October as the target. The Dispatch help page, last updated late last week, does not mention a retirement.

It says Dispatch is closed to new users and that people who already use it on some Pro, Max, and Ultra plans "can keep using it for now."

### How the Attack Worked

The attack needs two things, according to a
[technical write-up](https://forever.security/blog/thisbash-claude-dispatch-browser-extension-rce)
by Forever Security researcher Gal Weizman: an extension that can run scripts on claude.ai, and a person signed in to both claude.ai and Claude Desktop with Dispatch turned on.

The extension could be malicious, a legitimate one that received a compromised update, or a legitimate one with a security flaw. Dispatch itself only works while the computer is awake and the desktop app is open.

In the test, a script on the user's claude.ai page opened Dispatch and sent Claude four prompts as if it were the user. The prompts asked Claude to install an npm package.

Claude first hesitated over the unfamiliar package, but a follow-up message, delivered in the user's voice, got it to go ahead.

VIDEO

Claude asks before it acts, but those approval prompts appeared in the web page the extension controlled. The script clicked any "Allow" button every second, so no one had to be watching.

Claude then ran a global npm install, and the package's install script opened the Calculator app. No browser exploit was needed. The same step could have stolen files or installed a backdoor, given Claude's permissions on the computer, the researchers say.

The test was run with the browser and Claude Desktop on the same computer, and the researchers report no real attacks. Because Dispatch connects devices, the extension could also reach Claude Desktop on a different computer signed in to the same Claude account, they say. That case is described but not shown.

The same reach could link a home computer to a work laptop when someone uses a single personal Claude account on both devices, with Dispatch turned on. The researchers have seen personal Claude accounts with cross-device Dispatch turned on, on work computers at their customers.

The researchers reported the flaw to Anthropic on May 14. The company accepted it as valid on May 19 but closed the report as a duplicate of an issue it had already found internally, according to the researchers.

"Anthropic is retiring Dispatch, but not the design behind it," the researchers wrote, adding that two other Claude features, Claude Code Remote Control and Claude Cowork sessions, let extensions carry out the same attack. Their write-up does not include a test of those features, and they plan a follow-up post.

### What Dispatch Users Can Do

In Claude Desktop, Dispatch is part of Cowork and appears in the left-side panel. The
[Dispatch help page](https://support.claude.com/en/articles/13947068-assign-tasks-from-anywhere-in-claude-cowork)
says users should know how to quickly disconnect or revoke access before turning the feature on, but it does not explain how.

The researchers recommend these steps:

* Turn off cross-device Dispatch if you do not need it. If you do need it, review how devices are paired, approved, and removed.
* Treat browser extensions like other software on the computer: check their permissions, control what gets installed, and review updates that give them more access.
* Monitor what AI agents do on the computer, including unexpected package installations, setting changes, access to credentials, and external connections.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.