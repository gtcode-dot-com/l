---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-27T18:15:13.376938+00:00'
exported_at: '2026-01-27T18:15:15.812359+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/whatsapp-rolls-out-lockdown-style.html
structured_data:
  about: []
  author: ''
  description: Meta is rolling out Strict Account Settings on WhatsApp and using Rust-based
    media code to protect journalists and high-risk users from spyware attack
  headline: WhatsApp Rolls Out Lockdown-Style Security Mode to Protect Targeted Users
    From Spyware
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/whatsapp-rolls-out-lockdown-style.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: WhatsApp Rolls Out Lockdown-Style Security Mode to Protect Targeted Users From
  Spyware
updated_at: '2026-01-27T18:15:13.376938+00:00'
url_hash: 12c108c51c7e2cc522e54e574526f7859910b868
---

**

Ravie Lakshmanan
**

Jan 27, 2026

Mobile Security / Spyware

Meta on Tuesday
[announced](https://blog.whatsapp.com/whatsapps-latest-privacy-protection-strict-account-settings)
it's adding
**Strict Account Settings**
on WhatsApp to secure certain users against advanced cyber attacks because of who they are and what they do.

The feature, similar to
[Lockdown Mode](https://thehackernews.com/2022/07/apples-new-lockdown-mode-protects.html)
in Apple iOS and
[Advanced Protection](https://thehackernews.com/2025/05/google-rolls-out-on-device-ai.html)
in Android, aims to protect individuals, such as journalists or public-facing figures, from
[sophisticated spyware](https://thehackernews.com/2025/08/whatsapp-issues-emergency-update-for.html)
by trading some functionality for enhanced security.

Once this security mode is enabled, some of the account settings will be locked to the most restrictive options, while simultaneously blocking attachments and media from people not in a user's contacts.

"This lockdown-style feature bolsters your security on WhatsApp even further with just a few taps by locking your account to the most restrictive settings like automatically blocking attachments and media from unknown senders, silencing calls from people you don't know, and restricting other settings that may limit how the app works," Meta
[said](https://about.fb.com/news/2026/01/whatsapp-strict-account-settings-safeguarding-against-cyber-attacks/)
.

The feature can be enabled by navigating to Settings > Privacy > Advanced. Meta said the feature is rolling out gradually over the coming weeks.

In tandem, the social media giant said it's adopting the use of the
[Rust programming language](https://thehackernews.com/2025/11/rust-adoption-drives-android-memory.html)
in its media sharing functionality to help keep users' photos, videos, and messages safe from spyware attacks. It described the development as the "largest rollout globally of any library written in Rust."

The company also said the use of Rust made it possible to develop a secure, high-performance, cross-platform library ("wamedia") for media sharing in WhatsApp across devices, adding it's investing in a three-pronged approach to combat memory safety issues -

* Design the product to minimize unnecessary attack surface exposure
* Invest in security assurance for the remaining C and C++ code
* By default, the choice of memory-safe languages for new code

"WhatsApp has added protections like CFI, hardened memory allocators, safer buffer handling APIs, and more," the company
[said](https://engineering.fb.com/2026/01/27/security/rust-at-scale-security-whatsapp/)
. "This is an important step forward in adding additional security behind the scenes for users and part of our ongoing defense-in-depth approach."