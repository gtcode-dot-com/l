---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:51:08.502381+00:00'
exported_at: '2026-06-23T03:51:10.697014+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
structured_data:
  about: []
  author: ''
  description: Squidbleed CVE-2026-47729 can expose cleartext HTTP credentials from
    users sharing the same Squid proxy.
  headline: 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/29-year-old-squid-proxy-bug-squidbleed.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 29-Year-Old Squid Proxy Bug 'Squidbleed' Can Leak Cleartext HTTP Requests
updated_at: '2026-06-23T03:51:08.502381+00:00'
url_hash: 726cc507af6d690a889780c44907f6f18fa19737
---

**

Swati Khandelwal
**

Jun 22, 2026

Vulnerability / Server Security

A heap over-read in the Squid web proxy can leak another user's cleartext HTTP request, including any credentials or session tokens it carries, to anyone already allowed to send traffic through the same proxy.

The bug traces to a
[1997 FTP-parsing change](https://github.com/squid-cache/squid/commit/bb97dd37a)
and is still live in Squid's default configuration. Researchers at Calif.io
[disclosed it in June](https://blog.calif.io/p/squidbleed-cve-2026-47729)
and named it
**Squidbleed**
(
**CVE-2026-47729**
), after Heartbleed, which leaked memory the same way.

Squid describes this as an attack by a
[trusted client](https://seclists.org/oss-sec/2026/q2/896)
: someone already permitted to use the proxy, not any random host on the internet. That matches Squid's usual home, shared networks like schools, offices, and public Wi-Fi. In those setups, the attacker is just another user of the same proxy.

The leak also only reaches traffic that Squid can read. Normal HTTPS rides an opaque CONNECT tunnel, so Squid never sees inside it; the exposed traffic is cleartext HTTP, plus TLS-terminating setups where Squid decrypts and inspects.

The attacker also needs the proxy to reach an FTP server they control on port 21. Both FTP and that port are on by default.

## How the leak works

The bug sits in Squid's FTP directory-listing parser. To handle old NetWare servers that padded listings with extra spaces, the code skips whitespace with a loop: while (strchr(w\_space, \*copyFrom)) ++copyFrom;.

If the attacker's FTP server sends a listing line that ends right after the timestamp, with no filename, copyFrom lands on the string's null terminator. strchr treats that terminating NUL as part of the string it searches, so it returns a pointer instead of NULL, and the loop never stops. It walks off the end of the buffer, and xstrdup copies whatever follows back to the attacker as a filename.

VIDEO

The leaked bytes are the useful part. Squid reuses freed memory buffers without zeroing them, so a 4KB buffer that recently held a victim's HTTP request still holds most of it. A short FTP line overwrites only the first few bytes; the over-read returns the rest.

Calif's demo pulls an Authorization header from a victim sharing the same proxy, enough to act as that user.
[Proof-of-concept code is public](https://github.com/califio/publications/tree/main/MADBugs/squidbleed)
, and no in-the-wild exploitation has been reported as of writing.

## What to do

If you patch, verify the fix, not just the version. Confirm the guard is in FtpGateway.cc, or check your distribution's backport, since distros ship their own builds (Debian packages Squid 5.7).

The public thread is still inconsistent: maintainer Amos Jeffries first said Squid 7.6 carried the fix, then
[corrected that to 7.7](https://seclists.org/oss-sec/2026/q2/930)
, and on June 22 Debian's Salvatore Bonaccorso
[noted the referenced commit](https://seclists.org/oss-sec/2026/q2/995)
looks like it is already in 7.6.

The fix is small, a
[null-terminator check before the vulnerable strchr calls](https://github.com/squid-cache/squid/commit/865a131c7d557e68c965043d98c2eccae26deef8)
, merged to the development branch in April and v7 in May. Squid 7.6 does separately patch CVE-2026-50012, an unrelated cache\_digest heap overflow.

The cleaner move is the one the researchers recommend anyway: turn FTP off. Chromium dropped FTP years ago, and most networks carry almost none of it, so disabling it removes this attack surface for free, whatever build you run.

The risk is real but bounded. SUSE rates it moderate,
[CVSS 6.5](https://www.suse.com/security/cve/CVE-2026-47729.html)
, and the vector explains the score: the attacker needs proxy access (low privileges), and the only impact is confidentiality, nothing on integrity or availability.

Calif credits Anthropic's Claude Mythos Preview, the model behind
[Project Glasswing](https://thehackernews.com/2026/04/anthropics-claude-mythos-finds.html)
, with catching the strchr quirk almost at once, the same kind of buried parser bug
[AI agents have been surfacing elsewhere](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)
, including in FFmpeg. Calif hints Squid's FTP code may not be the last place it forgot to stop reading.