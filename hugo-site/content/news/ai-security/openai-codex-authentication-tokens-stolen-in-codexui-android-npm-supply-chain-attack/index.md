---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-09T01:58:46.601350+00:00'
exported_at: '2026-06-09T01:58:49.012718+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
structured_data:
  about: []
  author: ''
  description: Codex tokens were exfiltrated via a popular npm package, affecting
    users since v0.1.82 and enabling persistent account access.
  headline: OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply
    Chain Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/openai-codex-authentication-tokens.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Codex Authentication Tokens Stolen in codexui-android npm Supply Chain
  Attack
updated_at: '2026-06-09T01:58:46.601350+00:00'
url_hash: fac583a743fb9f53f0dbf08030ec4b3e7f3ba119
---

Cybersecurity researchers have disclosed details of a new malicious supply chain campaign that's targeting developers using OpenAI Codex through a legitimate-looking remote web UI.

The tool, named
[codexui-android](https://www.npmjs.com/package/codexui-android)
, is advertised on GitHub and npm as a remote web UI for OpenAI Codex, attracting over 29,000 weekly downloads. The package is still available for download from the repository.

What makes this activity noteworthy is that it's not a traditional attack that uses a typosquat or throwaway package to trick developers. Rather, the malicious code is embedded into a functional npm package that has undergone active development. The associated GitHub repository remains clean.

"And for the past month, every single invocation has been quietly exfiltrating your Codex authentication tokens to an attacker-controlled server," Aikido Security researcher Charlie Eriksen
[said](https://www.aikido.dev/blog/codex-remote-ui-steals-ai-tokens)
.

The nefarious changes are said to have been introduced about a month after the package was published to the registry, likely in an effort to build user trust and expand its reach. The npm account associated with the package is "friuns" (aka Igor Levochkin).

Present within the package is code that extracts the contents of Codex's "~/.codex/auth.json" file and exfiltrates them to a remote server ("sentry.anyclaw[.]store") that masquerades as Sentry, a legitimate application monitoring and error tracking platform. The captured data includes the following details: access\_token, refresh\_token, id\_token, and account ID.

"The refresh\_token doesn't expire," Eriksen said. "An attacker holding it can silently impersonate you indefinitely. A stolen Codex refresh\_token goes beyond access to a chat interface -- it's persistent, silent access to whatever that account can do."

It's worth mentioning here that every time a user logs in to the Codex app, CLI, or IDE Extension using either ChatGPT or an API key, the login details are cached locally in a plaintext file at ~/.codex/auth.json or in the operating system-specific credential store.

"If you use file-based storage, treat ~/.codex/auth.json like a password: it contains access tokens," OpenAI
[warns](https://developers.openai.com/codex/auth)
in its support documentation. "Don't commit it, paste it into tickets, or share it in chat."

Interestingly, the npm package is far from the only delivery vector the threat actor uses to target Codex developers. Aikido said it observed an Android application named
[OpenClaw Codex Claude AI Agent](https://play.google.com/store/apps/details?id=gptos.intelligence.assistant)
(package name: "gptos.intelligence.assistant") that runs the npm package within its PRoot sandbox and sends the Codex credentials to the same endpoint.

"The APK itself is small (26 MB) and looks clean on a Play pre-publish scan," Eriksen explained. "On first run, it extracts a Termux-derived Linux userland into the app's private storage and runs Node.js inside it via PRoot."

"The version is not pinned, so the device pulls whatever is currently published on npm. The exfiltration has been in place since codexui-android@0.1.82. The package runs inside the app's PRoot sandbox, where the in-app Codex sign-in writes its auth.json. Once the user signs in, the package reads that file out of the sandbox and ships the full OAuth blob to sentry.anyclaw.store/startlog."

Released by an entity named "BrutalStrike," the Android app has more than 50,000 downloads. The same exfiltration chain has also been flagged in a second Android app linked to BrutalStrike: Codex (package name: "codex.app"), which has been downloaded over 10,000 times. The remaining three apps offered by the developer do not contain the functionality.

Upon
[reaching out](https://github.com/friuns2/codex-mobile/issues/198)
to the package author on GitHub, Aikido said they initially posted a comment stating they had lost access to their npm account, only to edit the response and post a different one in which they claimed they are "currently investigating this issue internally" and that they "have started removing the affected functionality and related data."

The author further claimed no credential data was shared with any third parties, without answering why this code was inserted only into the npm package build or why they needed access to the Codex tokens in the first place. The
[X profile](https://x.com/friuns2)
linked to the author includes the domain "anyclaw[.]store."

WHOIS records
[indicate](https://whois.domaintools.com/anyclaw.store)
that the domain was registered on April 12, 2026, just two days after the very first version of the npm package (version 0.1.72) was uploaded to npmjs[.]com.

The development comes as threat actors are increasingly targeting real artificial intelligence (AI) developer tooling and workflows to steal credentials and burrow deeper into the software supply chain.

Late last month, the Belgian security company also found that a deleted Google API key remains live for up to 23 minutes, a window that an attacker with access to a leaked key can take advantage of to gain access to user data and other APIs, including those related to Google Gemini. The median revocation window is around 16 minutes.

"An attacker holding your deleted key can keep sending requests until one reaches a server that has not caught up," researcher Joe Leon
[said](https://www.aikido.dev/blog/google-api-keys-deletion)
. "If Gemini is enabled on the project, they can dump files you have uploaded and exfiltrate cached conversations."

Although Google first opted not to fix the issue, stating it's a "known property of the system and not a security issue," the tech giant has since decided to treat it as a
[P0 bug](https://developers.google.com/issue-tracker/concepts/issues)
, making it a severe issue that "needs to be addressed immediately."

The findings, as with a
[similar 4-second exploitation window](https://www.offensai.com/blog/aws-iam-eventual-consistency-persistence)
previously observed with deleted Amazon Web Services (AWS) access keys, highlight how credential revocation delays are exploitable and can be used to gain unauthorized access to the cloud environments, while defenders assume the credentials have been revoked.