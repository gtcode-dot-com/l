---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T06:54:23.609791+00:00'
exported_at: '2026-11-15T06:54:27.328392+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33506
structured_data:
  about: []
  author: ''
  description: 'Apple Patches Everyting: November 2026 Edition, Author: Johannes Ullrich'
  headline: 'Apple Patches Everyting: November 2026 Edition, (Tue, Nov 10th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33506
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Apple Patches Everyting: November 2026 Edition, (Tue, Nov 10th)'
updated_at: '2026-11-15T06:54:23.609791+00:00'
url_hash: 4197e6ee024c931fe812e18aa5ffe63ec4d48b7f
---

On Monday, Apple released updates for iOS/iPadOS, macOS, watchOS, and visionOS. These updates fix nine different vulnerabilities. One of the vulnerabilities, CVE-2026-113971, applies only to iOS/iPadOS version 26. Several of the vulnerabilities apply to Bluetooth issues that may weaken the device pairing process.

The number of vulnerabilities Apple patches remains small, but Apple has increased the cadence of its updates.

| iOS 27.2.1 and iPadOS 27.2.1 | iOS 26.7.3 and iPadOS 26.7.3 | iOS 18.7.12 and iPadOS 18.7.12 | macOS Golden Gate 27.2.1 | macOS Tahoe 26.7.3 | macOS Sequoia 15.8.3 | watchOS 27.2.1 | watchOS 26.6.1 | visionOS 27.2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2026-113960:** A user added to an iMessage group may be able to access messages sent before they joined.   Affects Messages | | | | | | | | |
| x | x |  | x | x | x | x |  | x |
| **CVE-2026-113961:** A remote attacker may be able to join an iMessage group chat and receive its messages.   Affects Messages | | | | | | | | |
| x | x |  | x | x | x | x |  | x |
| **CVE-2026-113963:** An app may be able to access sensitive user data.   Affects App Intents | | | | | | | | |
| x |  |  |  |  |  | x |  | x |
| **CVE-2026-113964:** An attacker in Bluetooth range may be able to bypass the rate limit on pairing code attempts and pair with a device without user interaction.   Affects CoreUtils | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113965:** A malicious Bluetooth device may be able to establish a pairing without user interaction.   Affects CoreUtils | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113968:** An attacker in Bluetooth range may be able to bypass the rate limit on pairing code attempts.   Affects AirPlay | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113969:** An attacker on the same network may be able to bypass the rate limit on AirPlay pairing code attempts.   Affects rapportd | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113970:** An attacker in Bluetooth range may be able to corrupt process memory.   Affects Bluetooth | | | | | | | | |
| x | x | x | x | x | x | x | x | x |
| **CVE-2026-113971:** An attacker with physical access may be able to pair a device with an AirPlay receiver from the lock screen.   Affects MediaRemote | | | | | | | | |
|  |  | x |  |  |  |  |  |  |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|