---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-12T21:44:10.187499+00:00'
exported_at: '2026-06-12T21:44:12.852462+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html
structured_data:
  about: []
  author: ''
  description: Sygnia says Velvet Ant modified Linux PAM and OpenSSH components to
    steal credentials and maintain stealthy access since 2016.
  headline: China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly
    a Decade
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade
updated_at: '2026-06-12T21:44:10.187499+00:00'
url_hash: d0b8c9fa3de3a6fc5d76a4d2725091e752fc45d4
---

**

Swati Khandelwal
**

Jun 12, 2026

Linux / Network Security

Instead of hiding on the laptops and servers defenders watch most closely, a China-nexus group spent close to a decade hidden inside the Linux login system itself.

Sygnia, which tracks the group as
**Velvet Ant**
, says it backdoored the PAM and OpenSSH components that decide who is allowed to sign in, planting its access where ordinary cleanup could not reach it. The network it targeted had no direct internet access, so the group first staged through internet-facing systems to get there.

The earliest traces go back to 2016. Instead of dropping new malware that a scanner might catch, the attacker changed the trusted login programs themselves. Nothing obvious appeared, and no exploit was needed, so the activity looked like normal administration.

On many machines, the attacker replaced the main PAM login module with backdoored copies. Some let them in with a secret password; others quietly recorded real usernames and passwords as people logged in.

Researchers found nine separate versions. The OpenSSH programs were altered the same way, logging credentials and every command typed, with a hidden switch to turn that logging off when needed.

Reaching the isolated network at all took extra work. The attacker used other disguised tools and an internet-facing web server as a bridge, passing commands through it to open remote sessions deep inside the segment that had no direct internet access.

Because the login system itself was compromised, normal containment did little. Password resets and killed sessions do not help when the thing that checks those credentials is working for the attacker.

This is not new for the group. Each time defenders find one foothold, Velvet Ant moves to gear they watch less and sets up there. In a
[2024 case](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)
, Sygnia found the same actor turning internet-exposed
[F5 BIG-IP appliances](https://thehackernews.com/2024/06/china-linked-hackers-infiltrate-east.html)
into internal command servers.

Later that year, it reported the group exploiting a Cisco NX-OS flaw,
[CVE-2024-20399](https://nvd.nist.gov/vuln/detail/CVE-2024-20399)
, to
[plant a backdoor on the switches](https://thehackernews.com/2024/07/chinese-hackers-exploiting-cisco.html)
. That bug needs admin access first, so it is a persistence tool, not a remote break-in. Cisco patched it in July 2024, and CISA flagged it as exploited the next day.

[Operation Highland](https://www.sygnia.co/blog/operation-highland-velvet-ant/)
is the same idea, one level deeper. Load balancers, switches, and the login software itself are trusted by default and rarely checked, which is exactly why a patient attacker hides inside them.

Operation Highland is not a one-CVE problem. The attacker changed trusted programs after getting in, so the fix is verification, not patching, and cleanup is delicate: a wrong replacement can lock admins out of a live system.

* **Watch the login files**
  . Monitor the PAM and OpenSSH programs and their key files for any change, and alert when they change.
* **Hunt by checking what changed**
  , not by waiting for an alert. Compare these programs against known-good copies, because nothing will flag them for you.
* **Remove the backdoor before resetting passwords**
  , or the new ones get stolen the same way. Test any replacement in a lab first.

The earlier F5 and Cisco cases have their own checks: patch CVE-2024-20399 on Cisco Nexus gear, and watch F5 boxes for unexpected outbound connections.

The wider lesson is plain: infrastructure that sits outside normal monitoring still needs integrity checks, and that now includes the login layer.