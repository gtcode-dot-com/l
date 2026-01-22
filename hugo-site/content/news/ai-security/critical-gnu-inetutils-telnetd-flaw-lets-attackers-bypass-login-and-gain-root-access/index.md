---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-22T18:15:12.782864+00:00'
exported_at: '2026-01-22T18:15:15.027539+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html
structured_data:
  about: []
  author: ''
  description: A 9.8-severity flaw (CVE-2026-24061) in GNU InetUtils telnetd allows
    remote authentication bypass and root access in versions 1.9.3 to 2.7.
  headline: Critical GNU InetUtils telnetd Flaw Lets Attackers Bypass Login and Gain
    Root Access
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/critical-gnu-inetutils-telnetd-flaw.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Critical GNU InetUtils telnetd Flaw Lets Attackers Bypass Login and Gain Root
  Access
updated_at: '2026-01-22T18:15:12.782864+00:00'
url_hash: 506db78ab2205b3d4749821aa07ce13282e3105b
---

**

Ravie Lakshmanan
**

Jan 22, 2026

Vulnerability / Linux

A critical security flaw has been disclosed in the GNU InetUtils telnet daemon (
[telnetd](https://linux.die.net/man/8/telnetd)
) that went unnoticed for nearly 11 years.

The vulnerability, tracked as
**[CVE-2026-24061](https://nvd.nist.gov/vuln/detail/CVE-2026-24061)**
, is rated 9.8 out of 10.0 on the CVSS scoring system. It affects all versions of GNU InetUtils from version 1.9.3 up to and including version 2.7.

"Telnetd in GNU Inetutils through 2.7 allows remote authentication bypass via a '-f root' value for the USER environment variable," according to a description of the flaw in the NIST National Vulnerability Database (NVD).

In a
[post](https://seclists.org/oss-sec/2026/q1/89)
on the oss-security mailing list, GNU contributor Simon Josefsson said the vulnerability can be exploited to gain root access to a target system -

*The telnetd server invokes /usr/bin/login (normally running as root) passing the value of the USER environment variable received from the client as the last parameter.*

*If the client supply [sic] a carefully crafted USER environment value being the string "-f root", and passes the telnet(1) -a or --login parameter to send this USER environment to the server, the client will be automatically logged in as root bypassing normal authentication processes.*

*This happens because the telnetd server do [sic] not sanitize the USER environment variable before passing it on to login(1), and login(1) uses the -f parameter to by-pass normal authentication.*

Josefsson also noted that the vulnerability was introduced as part of a
[source code commit](https://codeberg.org/inetutils/inetutils/commit/fa3245ac8c288b87139a0da8249d0a408c4dfb87)
made on March 19, 2015, which eventually made it to version 1.9.3 release on May 12, 2015. Security researcher Kyu Neushwaistein (aka Carlos Cortes Alvarez) has been credited with discovering and reporting the flaw on January 19, 2026.

As mitigations, it's advised to apply the latest patches and restrict network access to the telnet port to trusted clients. As temporary workarounds, users can disable telnetd server, or make the InetUtils telnetd use a custom login(1) tool that does not permit use of the '-f' parameter, Josefsson added.

Data gathered by threat intelligence firm GreyNoise shows that
[21 unique IP addresses](https://viz.greynoise.io/tags/inetutils-telnetd--f-auth-bypass-attempt?days=1)
have been observed attempting to execute a remote authentication bypass attack by leveraging the flaw over the past 24 hours. All the IP addresses, which
[originate](https://viz.greynoise.io/query/tags:%22Inetutils%20Telnetd%20-f%20Auth%20Bypass%20Attempt%22%20last_seen:1d)
from Hong Kong, the U.S., Japan, the Netherlands, China, Germany, Singapore, and Thailand, have been flagged as malicious.