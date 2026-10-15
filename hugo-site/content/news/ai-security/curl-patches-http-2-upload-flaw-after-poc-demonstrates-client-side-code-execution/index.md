---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-15T04:02:38.513843+00:00'
exported_at: '2026-10-15T04:02:39.839401+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html
structured_data:
  about: []
  author: ''
  description: curl 8.23.0 fixes an HTTP/2 upload use-after-free that a malicious
    server can trigger; code execution was demonstrated under strict conditions.
  headline: curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code
    Execution
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/curl-patches-http2-upload-flaw-after.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: curl Patches HTTP/2 Upload Flaw After PoC Demonstrates Client-Side Code Execution
updated_at: '2026-10-15T04:02:38.513843+00:00'
url_hash: 01ccdefefe75bf15fd34c2ef2966af9f73168cf3
---

A flaw in how curl handles HTTP/2 uploads lets a malicious server receiving an upload corrupt the client's memory, and the researcher who reported it turned that into code execution on the uploading machine.

The curl project fixed it on October 14 in
[curl 8.23.0](https://daniel.haxx.se/blog/2026/10/14/curl-8-23-0/)
. Taking over a client needs exact knowledge of its build and memory layout, and curl expects a real attack to end in a crash instead.

The flaw, a use-after-free tracked as
[CVE-2026-92392](https://curl.se/docs/CVE-2026-92392.html)
, affects curl and libcurl 8.12.0 through 8.22.0, both the command-line tool and the library that many other programs use for transfers. curl rates it High on its own four-level scale, its first High-severity flaw since the
[SOCKS5 heap overflow of October 2023](https://thehackernews.com/2023/10/two-high-risk-security-flaws-discovered.html)
. The project cut its release cycle by two weeks to ship the fix.

The attack runs from the server side. The client has to upload a file of roughly 135KB over HTTP/2 to a server controlled by the attacker, and the server's certificate must pass the client's checks. libcurl negotiates HTTP/2 by default for https:// URLs when the server offers it, and the library was built with HTTP/2 support.

The flaw has shipped in every curl release since 8.12.0 in February 2025. No source reports attacks that use it. The
[reporter's HackerOne write-up](https://hackerone.com/reports/4030333)
, with the malicious server script and a Docker container described as reproducing the code execution, became public on October 14 with the advisory.

### What to Install, and What to Do Until Then

Upgrade to 8.23.0 or apply the
[fix commit](https://github.com/curl/curl/commit/8b0744af5b1b631da5b938ca31c3f9895ad5a321)
to a local build. curl's
[machine-readable advisory](https://curl.se/docs/CVE-2026-92392.json)
also lists fixed versions on three older branches, and the project said it would ship updated
[Rock-solid curl](https://rock-solid.curl.dev/)
releases, its long-term-support line for customers with support contracts, in step with 8.23.0:

* curl and libcurl 8.12.0 through 8.22.0: upgrade to 8.23.0
* 8.14.x branch: 8.14.3
* 8.16.x branch: 8.16.2
* 8.20.x branch: 8.20.2
* Debian 13 (trixie): 8.14.1-2+deb13u7 through DSA-6558-1, per
  [Debian's tracker](https://security-tracker.debian.org/tracker/CVE-2026-92392)
  . Debian 12 (bookworm) does not carry the vulnerable code.

The release fixes 24 CVEs in all. The other 23 are rated Low.

If you cannot update yet, curl's advice is not to use HTTP/2. The
[--http1.1](https://curl.se/docs/manpage.html#--http11)
option asks the tool for HTTP/1.1, and applications set
[CURLOPT\_HTTP\_VERSION](https://curl.se/libcurl/c/CURLOPT_HTTP_VERSION.html)
to CURL\_HTTP\_VERSION\_1\_1. curl's documentation calls that setting a request, because an existing connection on another version may be reused.

HTTP/2 support in libcurl is a
[build option](https://curl.se/docs/manpage.html#--http2)
. A build without it cannot negotiate HTTP/2, so it cannot reach the upload path the advisory describes.

### How a Hostile Server Turns the Bug Into Code Execution

Daniel Stenberg, curl's lead developer,
[explained the bug](https://daniel.haxx.se/blog/2026/10/14/a-uaf-turned-rce/)
in a post published with the release, and the public report lays out the code path. HTTP/2 carries several transfers over one connection, and libcurl tracks each transfer with an object it calls an easy handle.

During an upload, the server stalls the transfer by setting the HTTP/2 window to zero, returning part of the response, and then resetting the stream while keeping the connection open. curl treats the reset as a reason to retry.

In cleanup, curl first tells the HTTP/2 layer that the transfer is finished, then flushes the rest of the unsent upload into the same connection. With no transfer registered, those leftover bytes are read as a new request. The line pattern the reporter includes in the uploaded file makes them look like request lines. When they do, a new stream is opened that stores a pointer to the easy handle.

The retry completes on a new HTTP/1.1 connection, and the application frees the handle. The old connection still holds the pointer and uses it when the server sends a frame on that stream, which can happen as the program exits.

In the reporter's exploit, data the server sends lands in the memory the freed handle had used. A request that goes out leaks local addresses, which the server needs to defeat address space layout randomization (ASLR). A function pointer in that memory is overwritten with bytes from the server, and curl then calls it.

Code execution needs the attacker to know the target's exact curl version, architecture, libc allocator and heap layout, to keep two parallel transfers on the right timing, and to fit the payload into about 23 bytes, according to curl's advisory. "The most likely outcome of an attempted attack is rather just a crash," Stenberg wrote, putting the chance of success as slim. That is why curl graded the flaw High rather than Critical.

curl uses four severity levels and publishes no
[CVSS score](https://curl.se/dev/vuln-disclosure.html)
. The National Vulnerability Database had not analyzed the record as of October 14.

The fix is a six-line reorder in lib/multi.c by Stefan Eissing. The HTTP/2 layer now gives up its references to the handle after the leftover upload data has been flushed, not before.

The report reached curl on September 15 through HackerOne, and the security team confirmed it within hours, according to Stenberg. On
[October 7](https://daniel.haxx.se/blog/2026/10/07/twenty-two-pending-curl-vulnerabilities/)
, the project pre-announced a High-severity fix for the next release, shortening its cycle from eight weeks to six.

curl credits the finding to "Luna with Claude, Anthropic." Stenberg names the reporter as Luna Tong of Anthropic, says the finding came through the company's new OSS Scanner, and presumes its AI models were involved.

Anthropic opened
[OSS Scanner](https://thehackernews.com/2026/10/anthropic-launches-free-ai.html)
on October 8 as an opt-in service that scans enrolled open-source projects with its models and emails the results
[without human review](https://red.anthropic.com/oss-scanner)
, each report with a reproducer and, where available, a candidate patch. The curl report came three weeks before that public launch. Anthropic's
[launch post](https://www.anthropic.com/research/launching-opt-in-vuln-finding-service-for-open-source)
quoted Stenberg saying the scanner had turned up "one of the worst curl vulnerabilities reported in the last few years," without naming one.

The same maintainer wrote in
[July 2025](https://daniel.haxx.se/blog/2025/07/14/death-by-a-thousand-slops/)
that about a fifth of curl's security submissions that year were what he called AI slop, and that only about one in twenty had proved genuine.

curl has spent several years reducing the number of internal pointers to handles in favor of identifiers it looks up when needed, Stenberg wrote, and that is no guarantee against another use-after-free. curl calls the bug a mistake that a memory-safe language would likely have avoided, and the project does not plan to rewrite curl in one.