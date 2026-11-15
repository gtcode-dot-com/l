---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:10:06.691295+00:00'
exported_at: '2026-11-15T06:10:07.457259+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/apache-patches-critical-http-server-rce-found-by-anthropic-google
structured_data:
  about: []
  author: ''
  description: Apache fixed CVE-2026-119618, a critical HTTP/2 flaw reported by Anthropic
    and Google that could enable unauthenticated code execution.
  headline: Apache Patches Critical HTTP Server RCE Found by Anthropic, Google
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/apache-patches-critical-http-server-rce-found-by-anthropic-google
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apache Patches Critical HTTP Server RCE Found by Anthropic, Google
updated_at: '2026-11-15T06:10:06.691295+00:00'
url_hash: ef88bdf45c7769c62712779e4ad5213258fcff88
---

**Apache has patched a critical HTTP Server vulnerability that could allow unauthenticated remote code execution (RCE), following independent discoveries by Anthropic and Google researchers.**

Tracked as
[CVE-2026-119618](https://nvd.nist.gov/vuln/detail/cve-2026-119618)
, the flaw affects Apache HTTP Server versions 2.4.55 through 2.4.70. The issue was addressed on November 11 with the release of version 2.4.71. It resides in mod\_http2, the module responsible for handling HTTP/2 traffic.

The vulnerability involves a race condition in which multiple threads improperly access shared resources, potentially corrupting server memory.

According to
[Red Hat](https://access.redhat.com/security/cve/cve-2026-119618)
, an attacker could exploit the issue remotely without authentication to execute arbitrary commands and gain control of the server process. Red Hat assigned the vulnerability a CVSS score of 9.8 and explained that “only servers that have HTTP/2 enabled are affected; servers configured to serve only HTTP/1.1 are not vulnerable.”

[Apache credited](https://httpd.apache.org/security/vulnerabilities_24.html)
Anthropic’s OSS Scanner with reporting the flaw on October 26. Anthony Weems and Simon Scannell of Google Cloud Vulnerability Research independently reported the same vulnerability on November 3.

Cloud security firm Wiz
[reported](https://www.wiz.io/blog/cve-2026-119618-rce-apache-http-server-vulnerability)
that 64% of cloud environments in its data contained resources running affected Apache versions, while 51% had publicly exposed instances. The company cautioned that these figures do not account for server configuration, so they do not necessarily represent exploitable installations.

Advertisement. Scroll to continue reading.

Red Hat says public research has demonstrated a reliable exploit against a server with mod\_http2 enabled, but its advisory does not identify the research.

Wiz noted that when its blog was published on November 11, no exploit was available and there were no reports of exploitation in the wild.

A publicly available proof of concept (
[PoC](https://github.com/googlesky/CVE-2026-119618)
) on GitHub reports reproducing memory corruption and Apache process crashes, but does not demonstrate remote code execution.

Organizations are advised to install Apache HTTP Server 2.4.71 or vendor-supplied packages. Disabling HTTP/2 can temporarily prevent exploitation if updates cannot be deployed immediately.

Defiant also
[warned](https://www.wordfence.com/blog/2026/11/cve-2026-119618-apache-http2/)
that WordPress security updates cannot resolve the issue because it affects the underlying web server.

Apache HTTP Server 2.4.71 also fixes two other vulnerabilities: CVE-2026-106023, an important issue that can crash server processes, and CVE-2026-109163, a low-severity stack buffer overflow.

**Related**
:
[Hackers Target N-central Zero-Days as N-able Rushes Patches](https://www.securityweek.com/hackers-target-n-central-zero-days-as-n-able-rushes-patches/)

**Related**
:
[Attacker Targets 60,000 GitHub Repositories in Credential Theft Campaign](https://www.securityweek.com/attacker-targets-60000-github-repositories-in-credential-theft-campaign/)

**Related**
:
[Critical Red Hat Quay Vulnerability Could Expose Private Container Images](https://www.securityweek.com/critical-red-hat-quay-vulnerability-could-expose-private-container-images/)