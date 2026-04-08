---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T16:15:14.383865+00:00'
exported_at: '2026-04-08T16:15:16.749081+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32878
structured_data:
  about: []
  author: ''
  description: 'More Honeypot Fingerprinting Scans, Author: Johannes Ullrich'
  headline: More Honeypot Fingerprinting Scans, (Wed, Apr 8th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32878
  publisher:
    logo: /favicon.ico
    name: GTCode
title: More Honeypot Fingerprinting Scans, (Wed, Apr 8th)
updated_at: '2026-04-08T16:15:14.383865+00:00'
url_hash: 1d0f6d9dd73fca03f58262105cca39d53e46d7f8
---

One question that often comes up when I talk about honeypots: Are attackers able to figure out if they are connected to a honeypot? The answer is pretty simple: Yes!

Most "medium interaction" honeypots, like the one we are using, are just simulating various systems. These simulations are incomplete. For example, we are using the "Cowrie" honeypot to emulate SSH and telnet servers. Once an attacker is connected, any package they are installing will appear to install. In the past, I have written about attackers attempting to install bogus packages. If the install appears to succeed, the attacker knows they are connected to a honeypot. Some attackers look for SSH artifacts, such as the number and types of ciphers supported by SSH.

Today, I noticed one attacker, (IP address
[45.135.194.48](/ipinfo.html?ip=45.135.194.48)
), using another common trick: Cowrie will often allow attackers to connect "randomly". The effect is that various username and password combinations appear to work. In this case, the attacker used usernames and passwords that are highly unlikely to work. If they succeed, they know they are connected to a honeypot. Here are some of the usernames and passwords used:

| username | password |
| --- | --- |
| admin | definitely\_not\_valid\_creds |
| honeypot | indexer |
| honeypotter | imaginegettingindexed |
| xXhoneypotXx | P@ssw0rd1337! |
| youjustgotindexed | getindexedretard |

Will we do anything to block these types of requests? Maybe... I am not sure it is important enough to "hide" honeypots. One advantage we have is that many of our honeypots are connected to home networks with dynamic IPs. As a result, any IP address list an attacker will create is somewhat ephemeral. Secondly, we are mostly interested in internet-wide scans. We are not going to detect targeted attacks or zero days.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|