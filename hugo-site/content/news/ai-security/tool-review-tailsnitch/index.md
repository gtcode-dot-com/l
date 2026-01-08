---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:48:37.341448+00:00'
exported_at: '2026-01-08T21:48:39.696511+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32602
structured_data:
  about: []
  author: ''
  description: 'Tool Review: Tailsnitch, Author: Johannes Ullrich'
  headline: 'Tool Review: Tailsnitch, (Tue, Jan 6th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32602
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Tool Review: Tailsnitch, (Tue, Jan 6th)'
updated_at: '2026-01-08T21:48:37.341448+00:00'
url_hash: 21693e0a096757df566deb22492b2f6b972ab51d
---

In yesterday's podcast, I mentioned "tailsnitch", a new tool to audit Tailscale configurations. Tailscale is an easy-to-use overlay to Wireguard. It is probably best compared to STUN servers in VoIP in that it allows devices behind NAT to connect directly to each other. Tailscale just helps negotiate the setup, and once the connection is established, data will flow directly between the connected devices. I personally use it to provide remote assistance to family members, and it has worked great for this purpose. Tailscale uses a "Freemium" model. For my use case, I do not need to pay, but if you have multiple users or a large number of devices, you may need to pay a monthly fee. There are also a few features that are only available to paid accounts.

Tailscale, like all VPN solutions, does, however, come with risks. You are exposing internal network assets, and misconfigurations can lead to unintentionally exposed hosts. I found Tailscale to be relatively straightforward to configure, but as things get more complex, it is easy to overlook some gaps in your configuration. Tailscale also offers some advanced security features that are not enabled by default.

Tailsnitch is supposed to solve this problem. Tailsnitch is open source software and can be found on GitHub (
<https://github.com/Adversis/tailsnitch>
). It was created by security consulting company Adversis (
<https://www.adversis.io>
). To test it, I used the binary distribution for my ARM-based Mac. Tailsnitch can use OAUTH credentials to authenticate to Tailscale. To run it:

> `./tailsnitch --tailscale-path /Applications/Tailscale.app/Contents/MacOS/Tailscale`

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-01-06%20at%209_05_17%E2%80%AFAM.png)

This is the default configuration. I only specified the "tailscale-path". Without it, tailsnitch wasn't able to identify my copy of the tailscale binary (it is not in my path). Other options include different output formats (JSON, verbose), filtering findings by severity, and an option to automatically fix any problems, which I did not test (I am not brave enough :) ).

My first test run identified one "medium", two "low", and 13 "info" suggestions:

Medium

This was actually a nice find: Two of my systems ran out-of-date versions of Tailscale. Something I will have to fix after finishing writing this diary :)

Low

Two of my devices use keys without expiration. This isn't a great thing, but intentional in this case. These are family member systems that I need to access only rarely (a couple of times a year), and I do not want to have to maintain rotating keys. So this is a risk I am willing to accept. I appreciate the reasonable rating from tailsnitch.

Another "low" issue was that I had no ACL tests defined. This is a feature I wasn't aware of, and nice of tailsnitch to point this out to me. I need to look into what these tests can do for me (I am the only user of this Tailscale network, so different user restrictions are not an issue)

Info

The "Info" sections of the results pointed out some other features I wasn't aware of. But for a single-user Tailscale net, many of them are irrelevant (for example, setting up Groups for better access control). Some of the features, like more advanced logging, are only available for paid plans.

In my quick test, I found tailsnitch to be a great tool to not only identify problems with your tailscale configuration, but also to learn more about additional hardening options that are available. The tool is easy to run, and the results are presented with the necessary detail to learn more about the identified issues.

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|