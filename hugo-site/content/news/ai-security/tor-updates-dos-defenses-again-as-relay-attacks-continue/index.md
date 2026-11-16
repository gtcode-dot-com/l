---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T20:00:51.454264+00:00'
exported_at: '2026-11-16T20:00:53.123426+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/tor-updates-dos-defenses-again-as-relay-attacks-continue
structured_data:
  about: []
  author: ''
  description: The Tor Project has released new security fixes as a DDoS attack continues
    to strain the volunteer-run relays.
  headline: Tor Updates DoS Defenses Again as Relay Attacks Continue
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/tor-updates-dos-defenses-again-as-relay-attacks-continue
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Tor Updates DoS Defenses Again as Relay Attacks Continue
updated_at: '2026-11-16T20:00:51.454264+00:00'
url_hash: 6f9201ed6dca072137d67ee7e6702314f1e77330
---

**The Tor Project has released new security fixes for its core software as a distributed denial-of-service (DDoS) attack continues to strain the volunteer-run relays that make up its network.**

[Tor 0.4.9.17](https://forum.torproject.org/t/security-release-0-4-9-17/22454)
, announced on November 13, patches several security issues. The project singled out one fix related to how relays’ built-in DoS protections deal with IPv6.

“This release comes in rapid response to the ongoing DDoS attack on the network, which has affected most relay operators. This is not an easy problem to address, as relays across the network are being overwhelmed by a massive flood of client circuits,” Tor developer David Goulet said in the announcement.

According to the project, more defenses are under consideration, and new versions should follow shortly. Anyone running a relay has been urged to update without delay.

The latest version comes less than three weeks after
[Tor 0.4.9.15](https://forum.torproject.org/t/security-release-0-4-9-15/22332)
, which introduced three DoS protections against what the project described as a “thunderstorm” of directory requests.

Writing to relay operators at the time, Goulet
[noted](https://lists.torproject.org/mailman3/hyperkitty/list/tor-relays@lists.torproject.org/thread/DO63TMBKGPNCUG2UBNBZ6PSJOXMP4VM4/)
that a single relay could be hit with hundreds of circuits per second. He cautioned that relays would remain under heavy load for as long as the attack lasted.

Advertisement. Scroll to continue reading.

Reports from relay operators suggest the latest update hasn’t ended the disruption. In a
[forum post](https://forum.torproject.org/t/tor-relays-update-on-attack-in-progress-post-0-4-17-upgrade/22464)
on November 14, one operator said two of their relays had lost HSDir status due to attacks before the update, and that another was being targeted when 0.4.9.17 was released and installed.

Roughly ten minutes after that relay was upgraded, the attack took on a new form, according to the operator. Its traffic plunged and it kept becoming unresponsive.

“Relay unresponsiveness ultimately caused loss of HSDIR. Attack ceased immediately on loss of HSDIR,” the operator wrote.

In the operator’s view, 0.4.9.17 does not do enough to shield HSDir relays, and the attacker changes techniques while an attack is underway.

The operator also warned that the attacker could be capable of deanonymizing and tracking onion services. The Tor Project has issued no such warning in its release announcements.

**Related**
:
[Firefox Vulnerability Allows Tor User Fingerprinting](https://www.securityweek.com/firefox-vulnerability-allows-tor-user-fingerprinting/)

**Related**
:
[CryptoBandits Malware Doubles as a Backdoor, Abuses Tor](https://www.securityweek.com/cryptobandits-malware-doubles-as-a-backdoor-abuses-tor/)

**Related**
:
[Tor Exit Relays Hijacked](https://www.securityweek.com/in-other-news-tor-exit-relays-hijacked-banks-spot-rogue-ai-agents-self-rebuilding-macos-ransomware/)