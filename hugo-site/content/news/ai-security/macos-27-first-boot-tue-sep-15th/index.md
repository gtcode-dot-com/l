---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T04:42:52.468936+00:00'
exported_at: '2026-10-03T04:42:55.913422+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33340
structured_data:
  about: []
  author: ''
  description: 'MacOS 27 - First Boot, Author: Johannes Ullrich'
  headline: MacOS 27 - First Boot, (Tue, Sep 15th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33340
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MacOS 27 - First Boot, (Tue, Sep 15th)
updated_at: '2026-10-03T04:42:52.468936+00:00'
url_hash: 4446531aa2d4f55c7e9d6000124317cdbfa01a52
---

I have not done this type of diary in a while: What traffic will you see from a system on boot, before a user logs in? I just took a quick look at macOS 27 "Golden Gate" to see what traffic you should expect. Here are some of the highlights:

I captured about 300 packets. This was likely inflated for this particular system as it connected via Wi-Fi and wired network interfaces. Each network interface will do its own DHCP/IP discovery during boot. I only used router advertisements for IPv6, not DHCPv6.

### IPv6 Neighbor Discovery - Duplicate Address Discovery

As it is supposed to, macOS 27 does standard compliant duplicate address discovery before accepting an IPv6 address. It does use ICMPv6 nonces to prevent some spoofing DoS attacks:

&gt; `:: &gt; ff02::1:ff8f:bd1c ICMPv6 86  Neighbor Solicitation for fe80::14e5:ff56:308f:bd1c
&gt;
&gt; Internet Control Message Protocol v6
&gt;
&gt; Type: Neighbor Solicitation (135)
&gt;
&gt; Code: 0
&gt;
&gt; Checksum: 0xd8bb [correct]
&gt;
&gt; [Checksum Status: Good]
&gt;
&gt; Reserved: 00000000
&gt;
&gt; Target Address: fe80::14e5:ff56:308f:bd1c
&gt;
&gt; ICMPv6 Option (Nonce)
&gt;
&gt; Type: Nonce (14)
&gt;
&gt; Length: 1 (8 bytes)
&gt;
&gt; Nonce: 30480a0a9b7c`

### DNS Traffic

macOS 27 resolved these hostnames during boot:

* `_dns.resolver.arpa (SVCB)`

  Discover secre (DNS over HTTPS...) DNS resolvers
* `1-courier.push.apple.com`
  ???????,
  `1-courier.sandbox.push.apple.com`

  Used for Apple push messaging
* `126.2.5.10.in-addr.arpa`

  reverse resolve the local IP address
* `albert.apple.com`

  This hostname is used by Apple for device activation (do not block it, and it does certificate pinning, so do not TLS intercept it)
* `appleid.apple.com`

  verifying Apple ID associated with the system
* `ipv4only.arpa`

  For IPv6-only networks, this record resolves to a NAT64 IPv6 prefix that can be used to reach IPv4-only services. (RFC 7050 and RFC 8880)
* `www.apple.com`

  Used to discover captive portals.

### TCP Options

TCP options have not changed for a few years now in macOS. macOS 27 still uses the somewhat more conservative window scale of "6". It also still uses ECN and random timestamps.

I recorded four TCP connection during boot:

1. TLS to "albert.apple.com" (HTTPS on port 443, IPv4).
2. OCSP connection to ocsp.digicert.com to verify the "albert.apple.com" certificate (HTTP on port 80, IPv6)
3. TLS to "init.push.apple.com" (port 443)
4. TLS connection to courier.push.apple.com (port 5223)

### Multicast DNS

Just like prior macOS versions, macOS 27 does advertise any services via multicast DNS on port 5353/udp

### User Agents

During boot, the only visible user-agent is contained in the OCSP request: com.apple.trustd/3.0. The user agent is the same as prior versions of macOS. The user agent for Safari is:

Mozilla/5.0 (Macintosh; Intel Mac OS X 10\_15\_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0 Safari/605.1.15

The version of Safari is indicated as "27.0", but oddly enough, the OS version states "Intel Mac OS X 10\_15\_7" (this was collected from a Mac with "M" CPU).

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|