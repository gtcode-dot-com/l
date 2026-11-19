---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-19T01:23:35.222134+00:00'
exported_at: '2026-11-19T01:23:37.026176+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
structured_data:
  about: []
  author: ''
  description: NGINX fixes five CVSS 9.2 flaws, including a decade-old HTTP/2 vulnerability
    demonstrated to allow unauthenticated code execution.
  headline: 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code
    on Servers
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/10-year-old-nginx-http2-flaw-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 10-Year-Old NGINX HTTP/2 Flaw Lets Unauthenticated Attackers Execute Code on
  Servers
updated_at: '2026-11-19T01:23:35.222134+00:00'
url_hash: fb8b318a049ee574dbf15c8b1ef46bfd4de76b5f
---

A flaw in
**NGINX**
's HTTP/2 support can allow an attacker to run code on servers with HTTP/2 enabled, without needing to log in.

The decade-old flaw,
**CVE-2026-123007,**
dubbed "
**nginx2root**
," has been present in NGINX's open-source code since version 1.9.5, released on September 22, 2015. Fixed versions 1.31.9 and 1.30.7 came out today.

**F5**
, the company behind NGINX, says attackers can run code where ASLR is turned off or can be bypassed. Security researchers at
**Wiz**
said they bypassed ASLR and ran code through the flaw in tests. Xint's researchers said they ran code through it with nothing more than a reachable HTTP/2 port.

Code run this way gets the permissions of an NGINX worker process. Getting root on the host takes a second way to raise privileges, according to CIRCL, the Computer Incident Response Center Luxembourg.

In Xint's tests, code running as a worker could get root on the host through a separate bug in the Linux kernel's SCTP code, even when NGINX ran inside a Docker container.

Neither the vendor nor the Wiz and Rapid7 researchers have reported any attacks exploiting the flaw so far. CISA's Known Exploited Vulnerabilities catalog did not list it as of today.

[Proof-of-concept code](https://github.com/sfewer-r7/CVE-2026-123007)
for the flaw is publicly available on GitHub, but its notes state it is suitable only for demonstrating the attack against a freshly started Docker container on the same machine.

Every open-source release from 1.9.5 through 1.31.8 is vulnerable, according to NGINX's
[security advisories](https://nginx.org/en/security_advisories.html)
. That includes 1.31.8 from October 21, as well as the October 14
[security releases](https://thehackernews.com/2026/10/nginx-fixes-5-flaws-including-possible.html)
1.31.7 and 1.30.6.

|  |
| --- |
|  |
| Wiz PoC |

NGINX Plus is affected too, in 37.x releases before the fixed builds and in R34 to R36, according to the
[vendor advisory](https://my.f5.com/manage/s/article/K000163926)
.

Today's releases also fix four more flaws that the vendor says can lead to code execution under the same ASLR condition. It scores all five 9.2 out of 10 on CVSS 4.0.

Each flaw can be reached only in a particular setup:

| Flaw | What it needs |
| --- | --- |
| CVE-2026-123007 | HTTP/2 turned on |
| CVE-2026-123633 | HTTP/2, with requests passed to a backend server while the worker is running low on `worker_connections` |
| CVE-2026-123634 | A proxied server name built from variables, plus a server-side include (SSI) or `mirror` subrequest to a location that looks up the same name |
| CVE-2026-121810 | HTTP/3 turned on |
| CVE-2026-113425 | NGINX used as a mail proxy |

HTTP/2 is on where a
`listen`
directive includes
`http2`
, or where
`http2 on`
is set. Running
`openssl s_client`
with
`-alpn h2`
against a server shows whether it accepts HTTP/2: the output reads
`ALPN protocol: h2`
if it does. Behind a CDN, test the NGINX origin itself, because an origin that accepts only HTTP/1.1 cannot be attacked through HTTP/2.

### Fixes, Workarounds and Signs of Attack

These releases fix CVE-2026-123007, according to F5:

* NGINX Open Source 1.31.0 to 1.31.8 (mainline): fixed in 1.31.9
* NGINX Open Source 1.9.5 to 1.30.6, including older branches such as 1.28: fixed in 1.30.7
* NGINX Plus 37.1.0 to 37.2.0.1: fixed in 37.3.0.1
* NGINX Plus 37.0.0 to 37.0.7.1: fixed in 37.0.8.1
* NGINX Plus R34 to R36: no fix listed

Versions 1.31.9 and 1.30.7 fix all five flaws, according to NGINX's
[release notes](https://nginx.org/en/CHANGES)
. On NGINX Plus, 37.3.0.1 and 37.0.8.1 fix four of the flaws, and the CVE-2026-123633 fix was introduced in the earlier builds 37.2.0.1 and 37.0.7.1.

After upgrading, restart NGINX fully or use its live binary upgrade. A reload alone leaves the old executable running, and existing connections can stay on old worker processes.

The
[official Docker images](https://hub.docker.com/_/nginx/tags?name=1.31.9)
for NGINX had 1.31.9 and 1.30.7 tags as of today, including Alpine variants.

Ubuntu and Debian had not shipped fixed packages as of today. Ubuntu's
[CVE status page](https://ubuntu.com/security/CVE-2026-123007)
listed nginx as vulnerable on its releases from 16.04 to 26.10, and Debian's
[security tracker](https://security-tracker.debian.org/tracker/CVE-2026-123007)
listed it as vulnerable in bookworm, trixie, forky and sid. A distribution package can carry a fix without changing the version number that
`nginx -v`
reports, so compare the full package version with the distribution's own advisory.

|  |
| --- |
|  |
| Xint PoC |

The vendor lists workarounds for only two of the five flaws. For the resolver flaw, CVE-2026-123634, avoid SSI and
`mirror`
directives, and do not build a proxied server name from variables. For the mail proxy flaw, CVE-2026-113425, limit listeners to trusted networks.

CIRCL's
[response guidance](https://www.circl.lu/pub/tr-105/)
lists turning off HTTP/2 as a temporary mitigation until you can upgrade. That blocks CVE-2026-123007 and CVE-2026-123633, but not the other three flaws. Turning off HTTP/3 where it is used removes the setup that CVE-2026-121810 needs.

On NGINX 1.25.1 and later, set
`http2 off;`
in each affected
`server`
block and remove
`http2`
from its
`listen`
directives. On 1.9.5 through 1.25.0, remove
`http2`
from the
`listen`
directive, so
`listen 443 ssl http2;`
becomes
`listen 443 ssl;`
. Then restart NGINX where needed and rerun the
`openssl`
check to confirm the server no longer accepts HTTP/2.

Until the Linux kernel's SCTP bug is fixed, the same guidance advises that hosts not using SCTP, a network transport protocol like TCP, block its kernel module from loading. One way is to add the line
`install sctp /bin/false`
to a
`.conf`
file in
`/etc/modprobe.d/`
. That does not unload a module already loaded or turn off SCTP built into the kernel.

For signs of an attack, CIRCL suggests looking for NGINX workers that start unexpected programs, workers that exit abnormally or leave core dumps, long-lived HTTP/2 connections with heavy incoming traffic but few logged requests, and unusual outbound connections or DNS lookups. A clean access log does not rule out an attack, because HTTP/2 control frames do not normally show up there as requests. None of these signs is proof on its own.

Rapid7's version of the attack needs about 128 GB of HTTP/2 traffic, according to its
[technical analysis](https://www.rapid7.com/blog/post/ve-cve-2026-123007-critical-nginx-http-2-integer-underflow-leads-to-rce-fixed/)
. The attack took two and a half minutes in its demonstration. On links slower than about 300 Mbit/s, the transfer would run past NGINX's default one-hour connection limit, and the attack would fail.

The method also depends on a glibc memory-copy routine that is chosen on x86-64 CPUs with the
`avx512f`
and
`avx512vl`
features.

Wiz ran its tests on official NGINX 1.31.7 and 1.31.8 builds, using HTTP/2 over TLS on 64-bit systems, according to its
[disclosure post](https://www.wiz.io/blog/nginx-http2-rce-vulnerabilities)
.

Xint's attack worked against its test servers on AWS, GCP and Azure, including over a public IP address, according to its
[research report](https://xint.io/blog/nginx2root-remote-code-execution)
.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.