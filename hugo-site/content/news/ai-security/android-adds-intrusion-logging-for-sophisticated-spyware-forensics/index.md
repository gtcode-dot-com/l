---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T22:05:22.865484+00:00'
exported_at: '2026-05-14T22:05:26.073440+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html
structured_data:
  about: []
  author: ''
  description: Android Intrusion Logging stores encrypted forensic logs for 12 months,
    helping experts investigate spyware attacks on high-risk users.
  headline: Android Adds Intrusion Logging for Sophisticated Spyware Forensics
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/android-adds-intrusion-logging-for.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Android Adds Intrusion Logging for Sophisticated Spyware Forensics
updated_at: '2026-05-14T22:05:22.865484+00:00'
url_hash: 463638b65223054b6a816263877eba73fad4c2da
---

Google on Tuesday
[unveiled](https://blog.google/security/whats-new-in-android-security-privacy-2026/)
a new opt-in Android feature called
**Intrusion Logging**
for storing forensic logs to better analyze sophisticated spyware attacks.

Intrusion Logging, available as part of
[Advanced Protection Mode](https://support.google.com/android/answer/16339980)
, enables "persistent and privacy-preserving forensics logging to allow for investigation of devices in the event of a suspected compromise," the company said.

The feature, it added, was developed in partnership with Amnesty International and Reporters Without Borders. According to a
[help document](https://support.google.com/android/answer/16927813)
shared by Google, it logs device and network activities on a daily basis, including information about device behavior and the various applications that run on it.

The kinds of activities recorded are listed below -

* App activity (e.g., when an app process starts)
* App installations, updates, and uninstalls
* Network connections like starting and stopping Wi-Fi, Bluetooth, DNS lookups, and IP addresses
* File transfers to or from the device over USB
* Changes to system certificates
* When the device is locked or unlocked

Google also noted that the log data is end-to-end encrypted by the device and stored on Google servers. The encryption keys are secured by Google Account password and screen lock credentials, meaning the logs cannot be accessed by any third-party, including Google itself, apart from the device owner.

"By storing the data on a secure server, even malware installed on the smartphone cannot access, delete, or manipulate it," Reporters Without Borders
[said](https://www.reporter-ohne-grenzen.de/en/artikel/blog/4242/new-protection-feature-against-sophisticated-spyware-advanced-protection-mode-for-android)
. "End-to-end encryption also ensures that neither Google nor state actors can access the data. The Intrusion Logging function in particular enables detection and forensic analysis of even highly sophisticated and previously difficult-to-detect attacks."

The encrypted logs are stored for a period of 12 months, after which they are automatically wiped. Once Intrusion Logging is enabled, a user cannot delete the logs before the 12-month expiration window, even if the account is closed or the feature is turned off. Users have the option to download the logs offline, should they prefer to keep them for longer periods.

That said, Google has emphasized that once the logs are downloaded and decrypted, users are responsible for their security. "In certain legal or regulatory environments, you may be required by law to provide access to your decrypted data or your security credentials," it pointed out.

Another thing to keep in mind when enabling the feature is that it also records network events generated during Chrome Incognito browsing, such as DNS lookups and IP connections, as it operates at the system level and does not distinguish between the browsing modes. In other words, anybody with access to the decrypted logs can glean what websites were visited, but cannot infer specific pages on those sites.

The motivation behind Intrusion Logging is that a high-risk individual, who suspects they may have been targeted by advanced surveillance tools because of who they are and what they do, can share the activity log with trusted security experts for detailed examination.

The logs can be downloaded by navigating to the Settings app, and then tapping Security & privacy -> Advanced Protection -> Intrusion Logging -> Access logs. The feature is currently rolling out to all devices running the Android 16 December update and newer.

"With Intrusion Logging, Google is the first major vendor to proactively address the challenge of detecting advanced attacks on devices," Donncha Ó Cearbhaill, head of Security Lab at Amnesty International,
[said](https://securitylab.amnesty.org/latest/2026/05/android-intrusion-logging-as-a-new-source-of-data-for-consensual-forensic-analysis/)
in a statement. "By making more consensual forensic data available for researchers, we can make life more difficult for attackers and help civil society seek accountability when their devices are unlawfully targeted by spyware and mobile data extraction tools."

### Other Privacy and Security Features Coming to Android

Besides Intrusion Logging, Google has announced a raft of privacy and security improvements, including verified financial calls, a new phone call spoofing protection feature to combat attacks where scammers impersonate banks to trick users into revealing sensitive data or transferring funds.

When users receive a call that appears to be from a participating bank, Android asks the installed online banking app to confirm if they are actually attempting to reach the customer. If the app confirms no such is being made, the call is automatically ended by the system.

"Your bank or financial institution may also designate numbers as inbound-only, meaning they never use them to call customers," Google said. "Incoming calls from these numbers will be ended directly." The feature is expected to go live on Android 11+ devices with Revolut, Itaú, and Nubank in the coming weeks, before expanding to more banks later this year.

Other notable changes are listed below -

* Expanding
  [Live Threat Detection](https://thehackernews.com/2024/05/android-15-introduces-new-features-to.html)
  to issue warnings about suspicious app behavior, including SMS forwarding and
  [accessibility overlays](https://thehackernews.com/2025/06/new-android-malware-surge-hits-devices.html)
  that are typically used by Android banking trojans to steal credentials.
* Evaluating downloaded APK files via Chrome on Android for known malware when Safe Browsing is enabled before it's installed.
* Removing access to the accessibility services API from all apps that are not labeled as accessibility tools.
* Disabling device-to-device unlocking and Chrome WebGPU support.
* Adding scam detection for chat notifications.
* Enhancing Find Hub's Mark as lost feature with the ability to lock a phone with biometric authentication, blocking thieves from turning off device tracking if a device is marked as lost. Triggering Mark as lost also turns on additional protections like hiding Quick Settings and disabling new Wi-Fi and Bluetooth connections.
* Reducing the number of times a third-party with physical access to a device can guess the PIN or password, in addition to implementing longer wait times between failed attempts.
* Improving device recovery by making a device's IMEI number accessible via the lock screen on devices running Android 12 or higher.
* Better privacy controls that allow users to share their precise location temporarily for specific tasks while a specific app is open, and provide access to specific contacts to a third-party app, as opposed to sharing the entire address book.
* Introducing AISeal with pKVM for hardware-backed, on-device isolation of artificial intelligence (AI)-related data processing.
* Expanding
  [Binary Transparency in Android](https://thehackernews.com/2026/05/android-apps-get-public-verification.html)
  to ensure integrity through verification of official builds and a public ledger for authentic Google apps and foundational GMS APIs.
* Hiding SMS one-time passwords (OTPs) from most apps for three hours to block OTP theft by malicious apps that have been granted the SMS permission.
* Giving carriers the ability to disable 2G by default to shield customers from
  [legacy technology vulnerabilities](https://thehackernews.com/2024/10/android-14-adds-new-security-features.html)
  .
* Hardening data protection by introducing
  [post-quantum cryptography](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html)
  to safeguard against future threats.
* Incorporating
  [explicit user controls](https://blog.google/security/android-gemini-intelligence-security-privacy/)
  to opt-in and out of entire features, security guardrails, and transparency when using Gemini on Android.

"By improving protections against banking scams, and extending powerful protections like Live Threat Detection and Android Advanced Protection, we are ensuring that Android remains the most secure platform," Eugene Liderman, director of Android security and privacy, said.