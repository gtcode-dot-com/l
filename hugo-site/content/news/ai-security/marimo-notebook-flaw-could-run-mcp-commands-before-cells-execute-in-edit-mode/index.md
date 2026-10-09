---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-26T16:53:31.692170+00:00'
exported_at: '2026-09-26T16:53:33.557895+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html
structured_data:
  about: []
  author: ''
  description: Marimo fixes CVE-2026-75149, an 8.7-severity flaw that can launch an
    MCP command before notebook cells run in edit mode.
  headline: Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit
    Mode
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/marimo-notebook-flaw-could-run-mcp.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Marimo Notebook Flaw Could Run MCP Commands Before Cells Execute in Edit Mode
updated_at: '2026-09-26T16:53:31.692170+00:00'
url_hash: 6bcf831998050f129c03758fc9280655973d4a05
---

**

Swati Khandelwal
**

Aug 25, 2026

Vulnerability / AI Security

Marimo has addressed a high-severity security flaw in its notebook software that allowed an attacker to execute an attacker-supplied Model Context Protocol (MCP) command in a specially crafted notebook, according to VulnCheck's CVE Numbering Authority (CNA) record.

The CNA record says the command can run as a local subprocess when the notebook is opened in edit mode.

The vulnerability, tracked as
**CVE-2026-75149**
, is a code injection issue affecting versions prior to 0.23.15. VulnCheck's CVE Numbering Authority (CNA) record assigns it a CVSS v4 score of 8.7 and a CVSS v3.1 score of 8.8, with user interaction required and no attacker authentication required.

Marimo has addressed the issue in version 0.23.15. The CVE was published on August 19. Users running an affected release should move to a version outside the affected range.

According to
[OSV's CVE import](https://osv.dev/vulnerability/CVE-2026-75149)
, a crafted notebook can supply an attacker-controlled MCP server command through notebook configuration.

The victim opens the notebook in edit mode. The CNA record says the specified command is launched as a local subprocess before any notebook cell is executed.

Marimo's
[PEP 723 hardening patch](https://github.com/marimo-team/marimo/commit/1a21bd71e258438d2511136b5edacc94c08855f4)
treats notebook metadata as attacker-controlled and passes notebook-supplied configuration through an allowlist.

The following notebook-supplied configuration sections are removed -

* ai
* mcp
* completion
* secrets
* server

The patch's MCP regression case uses an attacker-controlled URL and verifies that the mcp section is removed. The CNA record supplies the separate command-to-subprocess behavior described for CVE-2026-75149.

The Hacker News confirmed on August 25 that the
[current PyPI release](https://pypi.org/project/marimo/0.24.0/)
is version 0.24.0, released August 17. Marimo's
[version 0.23.15 release](https://github.com/marimo-team/marimo/releases/tag/0.23.15)
was published on July 23, 2026. Marimo's
[security policy](https://github.com/marimo-team/marimo/security/policy)
says security patches are provided for the latest stable release and encourages users to stay current.

The CVE record credits Gregory Tan, who uses the handle Grg0rry, with discovering the flaw. The same handle also appears as a co-author on Marimo's PEP 723 hardening commit.

The same configuration boundary was addressed in VulnCheck's
[separate CVE-2026-67618 advisory](https://www.vulncheck.com/advisories/marimo-api-key-exfiltration-via-malicious-notebook-pep-723-metadata)
(CVSS score: 7.1), disclosed on August 4, 2026. That flaw affects Marimo versions before 0.23.15 and involves an attacker-controlled artificial intelligence (AI) base\_url supplied through notebook metadata.

For CVE-2026-67618, an operator opens the malicious notebook. The operator later makes an AI request. The configured endpoint then receives the operator's API key without requiring a notebook cell to be executed.

CVE-2026-75149 is separate from the
[earlier CVE-2026-39987 flaw](https://thehackernews.com/2026/04/marimo-rce-flaw-cve-2026-39987.html)
in Marimo.
[Marimo's advisory](https://github.com/marimo-team/marimo/security/advisories/GHSA-2679-6mx9-h9xc)
for that vulnerability states that versions 0.20.4 and earlier were affected by a missing authentication validation on the /terminal/ws endpoint.

Requests reaching that endpoint could obtain a full pseudo-terminal (PTY) shell. The shell could then execute arbitrary commands. Marimo lists version 0.23.0 as the patched version for the earlier flaw.