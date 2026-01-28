---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-28T16:15:13.225519+00:00'
exported_at: '2026-01-28T16:15:16.108928+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html
structured_data:
  about: []
  author: ''
  description: A critical vm2 Node.js vulnerability (CVE-2026-22709, CVSS 9.8) allows
    sandbox escape via Promise handler bypass.
  headline: Critical vm2 Node.js Flaw Allows Sandbox Escape and Arbitrary Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Critical vm2 Node.js Flaw Allows Sandbox Escape and Arbitrary Code Execution
updated_at: '2026-01-28T16:15:13.225519+00:00'
url_hash: 6eee740db8795e9c3561ccd97d6dd2b1c305031e
---

**

Ravie Lakshmanan
**

Jan 28, 2026

Vulnerability / Open Source

A critical sandbox escape vulnerability has been disclosed in the popular vm2 Node.js library that, if successfully exploited, could allow attackers to run arbitrary code on the underlying operating system.

The vulnerability, tracked as
**CVE-2026-22709**
, carries a CVSS score of 9.8 out of 10.0 on the CVSS scoring system.

"In vm2 for version 3.10.0, Promise.prototype.then Promise.prototype.catch callback sanitization can be bypassed," vm2 maintainer Patrik Simek
[said](https://github.com/patriksimek/vm2/security/advisories/GHSA-99p7-6v5w-7xg8)
. "This allows attackers to escape the sandbox and run arbitrary code."

[vm2](https://github.com/patriksimek/vm2)
is a Node.js library used to run untrusted code within a secure sandboxed environment by intercepting and
[proxying JavaScript objects](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
to prevent sandboxed code from accessing the host environment.

The newly discovered flaw stems from the library's improper sanitization of
[Promise handlers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
, which creates an escape vector that results in the execution of arbitrary code outside the sandbox boundaries.

"The critical insight is that async functions in JavaScript return `globalPromise` objects, not `localPromise` objects. Since `globalPromise.prototype.then` and `globalPromise.prototype.catch` are not properly sanitized (unlike `localPromise`)," Endor Labs researchers Peyton Kennedy and Cris Staicu
[said](https://www.endorlabs.com/learn/cve-2026-22709-critical-sandbox-escape-in-vm2-enables-arbitrary-code-execution)
.

While CVE-2026-22709 has been addressed in vm2 version 3.10.2, it's the latest in a steady stream of sandbox escapes that have plagued the library in recent years. This includes
[CVE-2022-36067](https://thehackernews.com/2022/10/researchers-detail-critical-rce-flaw.html)
,
[CVE-2023-29017](https://thehackernews.com/2023/04/researchers-discover-critical-remote.html)
,
[CVE-2023-29199, CVE-2023-30547](https://thehackernews.com/2023/04/critical-flaws-in-vm2-javascript.html)
,
[CVE-2023-32314](https://github.com/patriksimek/vm2/security/advisories/GHSA-whpj-8f3w-67p5)
,
[CVE-2023-37466](https://github.com/patriksimek/vm2/security/advisories/GHSA-cchq-frgv-rjh5)
, and
[CVE-2023-37903](https://github.com/patriksimek/vm2/security/advisories/GHSA-g644-9gfx-q4q4)
.

The discovery of CVE-2023-37903 in July 2023 also led Simek to announce that the project was
[being discontinued](https://github.com/patriksimek/vm2/blob/b51d33c49b61e03cf67a075741790e9b938dd80f/README.md)
. However, these references have since been removed from the latest README file available on its GitHub repository. The
[Security page](https://github.com/patriksimek/vm2/blob/main/SECURITY.md)
has also been updated as of October 2025 to mention that vm2 3.x versions are being actively maintained.

However, vm2's maintainer has also acknowledged that new bypasses will likely be discovered in the future, urging users to make sure that they keep the library up to date and consider other robust alternatives, such as
[isolated-vm](https://github.com/laverdet/isolated-vm)
, for stronger isolation guarantees.

"Instead of relying on the problematic vm model, the successor to vm2, isolated-vm relies on V8's native Isolate interface, which offers a more solid foundation, but even then, the maintainers of vm2 stress the importance of isolation and actually recommend Docker with logical separation between components," Semgrep
[said](https://semgrep.dev/blog/2026/calling-back-to-vm2-and-escaping-sandbox/)
.

In light of the criticality of the flaw, users are recommended to update to the most recent version (
[3.10.3](https://github.com/patriksimek/vm2/releases/tag/v3.10.3)
), which comes with fixes for additional sandbox escapes.