---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-21T08:15:12.950213+00:00'
exported_at: '2026-01-21T08:15:15.212402+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html
structured_data:
  about: []
  author: ''
  description: A flaw in the binary-parser npm package before version 2.3.0 lets attackers
    execute arbitrary JavaScript via unsanitized parser input.
  headline: CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/certcc-warns-binary-parser-bug-allows.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: CERT/CC Warns binary-parser Bug Allows Node.js Privilege-Level Code Execution
updated_at: '2026-01-21T08:15:12.950213+00:00'
url_hash: cb4211165e31caf635d4a5cd4c96156e24f6c429
---

**

Ravie Lakshmanan
**

Jan 21, 2026

Open Source / Vulnerability

A security vulnerability has been disclosed in the popular
[binary-parser npm library](https://github.com/keichi/binary-parser)
that, if successfully exploited, could result in the execution of arbitrary JavaScript.

The vulnerability, tracked as
**[CVE-2026-1245](https://www.cve.org/CVERecord?id=CVE-2026-1245)**
(CVSS score: N/A), affects all versions of the module prior to
[version 2.3.0](https://www.npmjs.com/package/binary-parser?activeTab=versions)
, which addresses the issue. Patches for the flaw were released on November 26, 2025.

Binary-parser is a widely used parser builder for JavaScript that allows developers to parse binary data. It supports a wide range of common data types, including integers, floating-point values, strings, and arrays. The package attracts approximately 13,000 downloads on a weekly basis.

According to an
[advisory](https://kb.cert.org/vuls/id/102648)
released by the CERT Coordination Center (CERT/CC), the vulnerability has to do with a
[lack of sanitization](https://github.com/keichi/binary-parser/pull/283)
of user-supplied values, such as parser field names and encoding parameters, when the JavaScript parser code is dynamically generated at runtime using the "Function" constructor.

It's worth noting that the npm library builds JavaScript source code as a string that represents the parsing logic and compiles it using the Function constructor and caches it as an executable function to parse buffers efficiently.

However, as a result of CVE-2026-1245, an attacker-controlled input could make its way to the generated code without adequate validation, causing the application to parse untrusted data, resulting in the execution of arbitrary code. Applications that use only static, hard-coded parser definitions are not affected by the flaw.

"In affected applications that construct parser definitions using untrusted input, an attacker may be able to execute arbitrary JavaScript code with the privileges of the Node.js process," CERT/CC said. "This could allow access to local data, manipulation of application logic, or execution of system commands depending on the deployment environment."

Security researcher Maor Caplan has been credited with discovering and reporting the vulnerability. Users of binary-parser are advised to upgrade to version 2.3.0 and avoid passing user-controlled values into parser field names or encoding parameters.