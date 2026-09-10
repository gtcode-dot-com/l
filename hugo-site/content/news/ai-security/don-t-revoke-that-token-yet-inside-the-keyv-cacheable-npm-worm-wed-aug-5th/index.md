---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-10T00:59:22.121450+00:00'
exported_at: '2026-09-10T00:59:23.004674+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33218
structured_data:
  about: []
  author: ''
  description: 'Don''t Revoke That Token Yet: Inside the keyv/cacheable npm Worm,
    Author: Renato Marinho'
  headline: 'Don''t Revoke That Token Yet: Inside the keyv/cacheable npm Worm, (Wed,
    Aug 5th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33218
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Don''t Revoke That Token Yet: Inside the keyv/cacheable npm Worm, (Wed, Aug
  5th)'
updated_at: '2026-09-10T00:59:22.121450+00:00'
url_hash: d233e46c2fe333f3c55fb0a41f59e49312563c6b
---

When you learn that a compromised package executed on one of your build hosts, muscle memory takes over: revoke the npm token, rotate the GitHub PAT, cycle the cloud keys. That reflex has been correct in almost every supply-chain incident I have worked. In the
**`keyv`
/
`cacheable`**
compromise that has been unfolding since yesterday, it is the one thing you should not do first — because revoking the stolen token is exactly what arms the payload.

Let me back up.

**What happened**

On August 4, 2026, an attacker took over the maintainer account behind the widely used
`keyv`
and
`cacheable`
npm namespaces — caching libraries that sit near the bottom of a very large number of dependency trees — and published trojanized releases. Socket's Threat Research team, which did the primary analysis, places the first malicious release,
`[email protected]`
, at 09:35 UTC. The poisoned versions ship a
`preinstall`
hook:

```
"scripts": { "preinstall": "node setup.mjs" }
```

`setup.mjs`
downloads a standalone Bun runtime, runs an obfuscated second stage (
`Math_Symbol.js`
, ~728 KB), and harvests whatever it can reach: AWS instance metadata, cloud keys, Vault tokens, Kubernetes service-account tokens, GitHub Actions secrets, npm tokens, plus a generic regex sweep for private keys and bearer tokens on disk. Then — and this is why the campaign grew from roughly ten packages to several hundred within hours — it uses the stolen npm token to inject the same hook into other packages the compromised identity can publish, recomputes the integrity hashes, and republishes. It is a worm. The public IOC lists now cover more than 440 packages across two thousand-plus versions, and they are still moving.

Two properties make this one worth a closer look than the average typosquat.

**It does not need npm install**

Most teams scope this kind of incident to "who ran
`npm install`
in the exposure window." That misses half the population. The source repository also received IDE and agent autostart hooks — a
`SessionStart`
entry in
`.claude/settings.json`
and a
`folderOpen`
task in
`.vscode/tasks.json`
— that run the loader
**when the cloned folder is simply opened**
. No install, nothing built.

Sit with who that includes. It includes the security engineer who cloned the repository
*to investigate the incident after reading about it*
. It includes the AI coding agent that opened the directory to "take a look." I do not think we have seen AI-agent configuration files used as a first-class supply-chain execution vector at this scale before, and it is worth internalizing: a checked-out repository is now an execution surface, and
`.claude/`
,
`.cursor/`
, and
`.vscode/`
are part of it.

**It punishes remediation**

Here is the part that should change how you respond. Alongside the credential theft, the payload installs a host-level dead-man's switch. It writes the stolen GitHub token and an attacker-supplied handler command to
`~/.config/gh-token-monitor/`
, then persists itself as a macOS LaunchAgent or a Linux
`systemd`
user service with
`loginctl enable-linger`
so it survives logout. The systemd unit describes itself, helpfully, as a "GitHub Token Validity Monitor," so at a glance it reads like a developer convenience.

A watcher script polls the GitHub API with the stolen token every 60 seconds. While the token works, nothing happens. The moment the token stops working — an HTTP 4xx, which is precisely what your revocation produces — it
`eval`
s the remote-supplied handler string, then deletes its own state and exits. It is single-shot and self-clearing, and it also self-destructs after a 24-hour TTL.

What is in the handler? Public analysis cannot say, because it is attacker-controlled text pulled at runtime and can be changed remotely. It could be data destruction, re-implant, or nothing at all. That is the whole problem:
**the risk is not that the trap does something specific and known — it is that you cannot assess it, and it fires at the exact moment your team believes it is containing the incident and starts to relax.**

One consequence is counterintuitive but load-bearing:
**isolating the host from the network is safe.**
With no connectivity there is no HTTP response, so there is no 4xx, so the switch does not fire — and exfiltration stops at the same time. Isolate first. Do not power off; volatile memory is evidence.

**Why the usual checks miss it**

* **"The signature was valid."**
  `[email protected]`
  shipped with a passing SLSA attestation. Provenance attests to build integrity, not source integrity — the legitimate workflow faithfully built already-trojanized code.
* **"The diff was clean."**
  The library itself was not modified. The malice lives in
  `package.json`
  and two added files. A
  `dist/`
  comparison shows nothing.
* **"We don't use keyv."**
  You almost certainly do, transitively. The common path is
  `eslint → file-entry-cache → flat-cache → keyv`
  . Very few victims installed any of these directly.
* **"Nobody ran
  `npm install`
  ."**
  See the second section.

**What to actually do**

The order matters more than the individual steps:

1. **Isolate**
   the host from the network. Safe, for the reason above. Do not shut it down.
2. **Preserve**
   evidence before you delete anything — the watcher self-clears in ~24 hours. Copy
   `~/.config/gh-token-monitor/{handler,token,started_at}`
   , the payloads, the plist/unit, and record hashes. Do not execute the handler; treat it as inert text.
   `started_at`
   bounds your exposure window.
3. **Eradicate**
   : kill the watcher, unload the LaunchAgent / disable the systemd unit, drop
   `loginctl`
   linger, remove the files and the
   `.claude`
   /
   `.vscode`
   hooks, and clear the package caches.
4. **Rotate**
   — now, and only now. npm token first, to stop propagation; then GitHub, cloud, Vault, Kubernetes, CI secrets, and anything that was sitting in a file, because there was a regex sweep. Revoke, do not merely rotate.
5. **Audit**
   what was done in your name: repositories freshly described "Shai-Hulud: Here We Go Again," unexpected npm publishes under your accounts, and credential use in your cloud logs during the
   `started_at`
   window.

CI runners and any host with confirmed execution should be rebuilt, not cleaned. Arbitrary code ran; the list of known artifacts is not a completeness guarantee.

**A small tool to help with the triage**

Enumerating this by hand across a fleet is tedious, and the moving IOC list makes a hardcoded grep obsolete within hours. I wrote a scanner to help with the triage: it checks lockfiles and
`node_modules`
for the compromised name/version set (with the transitive chain, so "we don't use keyv" gets answered on the spot), flags the host persistence and the dead-man's switch, and prints the response order above so nobody rotates before cleaning.

It is built to be easy to trust during exactly this kind of incident: one auditable file you can read in fifteen minutes, zero dependencies, zero egress (it never phones home;
`--update`
is the only network call and it is explicit), and read-only. It runs offline. It is MIT-licensed and open source, and — disclosure — it comes out of my work at Securest8; the IOC data is not mine but the public research of Socket, Wiz, and Kodem, credited in the repository.

If you only take the tool, take the response order with it. The scanner finds the problem; the order in which you touch credentials is what keeps a bad day from getting worse.

**Bottom line**

The novel part of this campaign is not the credential theft — it is the two design choices around it: an execution path that does not require installing anything, and a switch that turns your remediation reflex into the trigger. Scope the second vector, isolate before you revoke, and clean the host before you touch a single token.

**References**

- Socket, "Popular npm Packages in the keyv and Cacheable Namespaces Compromised in Active Supply Chain Attack," August 4, 2026. https://socket.dev/blog/popular-npm-packages-in-the-keyv-and-cacheable-namespaces-compromised-in-active-supply-chain

- Wiz Research, public IOC feed (keyv/cacheable). https://github.com/wiz-sec-public/wiz-research-iocs/blob/main/reports/keyv-packages.csv

- Wiz, "keyv and cacheable npm supply chain attack." https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack

- Kodem Security, keyv supply-chain attack IOCs and first-hour runbook. https://www.kodemsecurity.com/resources/keyv-supply-chain-attack-shai-hulud-npm-worm-affected-versions-iocs-and-first-hour-response-runbook

--

Renato Marinho

[LinkedIn](http://ow.ly/Nst730dJ6X3)
|
[Twitter](http://ow.ly/uXqT30dJ6Tp)