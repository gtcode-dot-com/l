---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-09T20:15:14.661599+00:00'
exported_at: '2026-04-09T20:15:16.891598+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html
structured_data:
  about: []
  author: ''
  description: EngageLab SDK flaw exposed 50M+ Android installs after April 2025 disclosure,
    risking crypto wallet data until November 2025 patch.
  headline: EngageLab SDK Flaw Exposed 50M Android Users, Including 30M Crypto Wallets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/engagelab-sdk-flaw-exposed-50m-android.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: EngageLab SDK Flaw Exposed 50M Android Users, Including 30M Crypto Wallets
updated_at: '2026-04-09T20:15:14.661599+00:00'
url_hash: f06c713635f2d793ff7e5104b1399f9a4b4dddc4
---

**

Ravie Lakshmanan
**

Apr 09, 2026

Vulnerability / Mobile Security

Details have emerged about a now-patched security vulnerability in a widely used third-party Android software development kit (SDK) called
[EngageLab SDK](https://www.engagelab.com/docs/essentials/developer-guide/client-sdk/android-sdk)
that could have put millions of cryptocurrency wallet users at risk.

"This flaw allows apps on the same device to bypass Android security sandbox and gain unauthorized access to private data," the Microsoft Defender Security Research Team
[said](https://www.microsoft.com/en-us/security/blog/2026/04/09/intent-redirection-vulnerability-third-party-sdk-android/)
in a report published today.

EngageLab SDK offers a
[push notification service](https://www.engagelab.com/app-push)
, which, according to its website, is designed to deliver "timely notifications" based on user behavior already tracked by developers. Once integrated into an app, the SDK offers a way to send personalized notifications and drive real-time engagement.

The tech giant said a significant number of apps using the SDK are part of the cryptocurrency and digital wallet ecosystem, and that the affected wallet apps accounted for more than 30 million installations. When non‑wallet apps built on the same SDK are included, the installation count surpasses 50 million.

Microsoft did not reveal the names of the apps, but noted that all those detected apps using vulnerable versions of the SDK have been removed from the Google Play Store. Following responsible disclosure in April 2025, EngageLab released
[version 5.2.1](https://mvnrepository.com/artifact/com.engagelab/engagelab/5.2.1)
in November 2025 to address the vulnerability.

The issue, identified in version 4.5.4, has been described as an intent redirection vulnerability. Intents in Android refer to
[messaging objects](https://developer.android.com/guide/components/intents-filters)
that are used to request an action from another app component.

Intent redirection occurs when the contents of an intent that a vulnerable app sends are manipulated by taking advantage of its trusted context (i.e., permissions) to gain unauthorized access to protected components, expose sensitive data, or escalate privileges within the Android environment.

An attacker could exploit this vulnerability by means of a malicious app installed on the device through some other means to access internal directories associated with an app that has the SDK integrated, resulting in unauthorized access to sensitive data.

There is no evidence that the vulnerability was ever exploited in a malicious context. That said, developers who integrate the SDK are recommended to update to the latest version as soon as possible, especially given that even trivial flaws in upstream libraries can have cascading impacts and impact millions of devices.

"This case shows how weaknesses in third‑party SDKs can have large‑scale security implications, especially in high‑value sectors like digital asset management," Microsoft said. "Apps increasingly rely on third‑party SDKs, creating large and often opaque supply‑chain dependencies. These risks increase when integrations expose exported components or rely on trust assumptions that aren’t validated across app boundaries."