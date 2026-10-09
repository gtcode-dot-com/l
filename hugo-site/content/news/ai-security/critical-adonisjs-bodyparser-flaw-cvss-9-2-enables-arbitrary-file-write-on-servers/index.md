---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-06T12:15:14.583652+00:00'
exported_at: '2026-01-06T12:15:17.188486+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/critical-adonisjs-bodyparser-flaw-cvss.html
structured_data:
  about: []
  author: ''
  description: A critical CVSS 9.2 flaw in AdonisJS bodyparser lets attackers write
    arbitrary files via path traversal when uploads are misconfigured.
  headline: Critical AdonisJS Bodyparser Flaw (CVSS 9.2) Enables Arbitrary File Write
    on Servers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/critical-adonisjs-bodyparser-flaw-cvss.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Critical AdonisJS Bodyparser Flaw (CVSS 9.2) Enables Arbitrary File Write on
  Servers
updated_at: '2026-01-06T12:15:14.583652+00:00'
url_hash: 9e79634feeab3b7360cb2e7cdfda2661ceee5b00
---

**

Jan 06, 2026
**

Ravie Lakshmanan

Vulnerability / Web Security

Users of the "
[@adonisjs/bodyparser](https://www.npmjs.com/package/@adonisjs/bodyparser)
" npm package are being advised to update to the latest version following the disclosure of a critical security vulnerability that, if successfully exploited, could allow a remote attacker to write arbitrary files on the server.

Tracked as CVE-2026-21440 (CVSS score: 9.2), the flaw has been described as a path traversal issue affecting the AdonisJS multipart file handling mechanism. "@adonisjs/bodyparser" is an npm package associated with AdonisJS, a Node.js framework for developing web apps and API servers with TypeScript. The library is used to
[process AdonisJS HTTP request body](https://docs.adonisjs.com/guides/basics/request)
.

"If a developer uses MultipartFile.move() without the second options argument or without explicitly sanitizing the filename, an attacker can supply a crafted filename value containing traversal sequences, writing to a destination path outside the intended upload directory," the project maintainers
[said](https://github.com/adonisjs/core/security/advisories/GHSA-gvq6-hvvp-h34h)
in an advisory released last week. "This can lead to arbitrary file write on the server."

However, successful exploitation hinges on a reachable upload endpoint. The problem, at its core, resides in a function named "
[MultipartFile.move(location, options)](https://api.adonisjs.com/classes/_adonisjs_bodyparser.index.MultipartFile#move)
" that allows a file to be moved to the specified location. The "options" parameter holds two values: the name of a file and an overwrite flag indicating "true" or "false."

The issue arises when the name parameter is not passed as input, causing the application to default to an unsanitized client filename that opens the door to path traversal. This, in turn, allows an attacker to choose an arbitrary destination of their liking and overwrite sensitive files, if the overwrite flag is set to "true."

"If the attacker can overwrite application code, startup scripts, or configuration files that are later executed/loaded, RCE [remote code execution] is possible," AdonisJS said. "RCE is not guaranteed and depends on filesystem permissions, deployment layout, and application/runtime behavior."

The issue, discovered and reported by Hunter Wodzenski (@
[wodzen](https://github.com/wodzen)
) impacts the following versions -

* <= 10.1.1 (Fixed in 10.1.2)
* <= 11.0.0-next.5 (Fixed in 11.0.0-next.6)

### Flaw in jsPDF npm Library

The development coincides with the disclosure of another path traversal vulnerability in an npm package named jsPDF (
[CVE-2025-68428](https://nvd.nist.gov/vuln/detail/CVE-2025-68428)
, CVSS score: 9.2) that could be exploited to pass unsanitized paths and retrieve the contents of arbitrary files in the local file system the node process is running.

The vulnerability has been patched in jsPDF version 4.0.0 released on January 3, 2026. As workarounds, it's advised to use the
[--permission flag](https://nodejs.org/api/permissions.html)
to restrict access to the file system. A researcher named Kwangwoon Kim has been acknowledged for reporting the bug.

"The file contents are included verbatim in the generated PDFs," Parallax, the developers of the JavaScript PDF generation library,
[said](https://github.com/parallax/jsPDF/security/advisories/GHSA-f8cm-6447-x5h2)
. "Only the node.js builds of the library are affected, namely the dist/jspdf.node.js and dist/jspdf.node.min.js files."