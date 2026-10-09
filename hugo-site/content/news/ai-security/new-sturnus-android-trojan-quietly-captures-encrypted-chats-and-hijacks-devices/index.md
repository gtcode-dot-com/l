---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-21T00:00:08.644024+00:00'
exported_at: '2025-11-21T00:00:10.879200+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/new-sturnus-android-trojan-quietly.html
structured_data:
  about: []
  author: ''
  description: Android banking trojan Sturnus enables screen-decrypted chat capture,
    device takeover, and targeted European financial fraud.
  headline: New Sturnus Android Trojan Quietly Captures Encrypted Chats and Hijacks
    Devices
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/new-sturnus-android-trojan-quietly.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New Sturnus Android Trojan Quietly Captures Encrypted Chats and Hijacks Devices
updated_at: '2025-11-21T00:00:08.644024+00:00'
url_hash: f43e39d8e8814057c603d6957d383f82ab79bf9a
---

**

Nov 20, 2025
**

Ravie Lakshmanan

Malware / Mobile Security

Cybersecurity researchers have disclosed details of a new Android banking trojan called
**Sturnus**
that enables credential theft and full device takeover to conduct financial fraud.

"A key differentiator is its ability to bypass encrypted messaging," ThreatFabric
[said](https://www.threatfabric.com/blogs/sturnus-banking-trojan-bypassing-whatsapp-telegram-and-signal)
in a report shared with The Hacker News. "By capturing content directly from the device screen after decryption, Sturnus can monitor communications via WhatsApp, Telegram, and Signal."

Another notable feature is its ability to stage overlay attacks by serving fake login screens atop banking apps to capture victims' credentials. According to the Dutch mobile security company, Sturnus is privately operated and is currently assessed to be in the evaluation stage. Artifacts distributing the banking malware are listed below -

* Google Chrome ("com.klivkfbky.izaybebnx")
* Preemix Box ("com.uvxuthoq.noscjahae")

The malware has been designed to specifically single out financial institutions across Southern and Central Europe with region-specific overlays.

The name Sturnus is a nod to its use of a mixed communication pattern blending plaintext, AES, and RSA, with ThreatFabric likening it to the
[European starling](https://www.allaboutbirds.org/guide/European_Starling/overview)
(binomial name: Sturnus vulgaris), which
[incorporates](https://www.allaboutbirds.org/guide/European_Starling/sounds)
a variety of whistles and is known to be a vocal mimic.

The trojan, once launched, contacts a remote server over WebSocket and HTTP channels to register the device and receive encrypted payloads in return. It also establishes a WebSocket channel to allow the threat actors to interact with the compromised Android device during Virtual Network Computing (VNC) sessions.

Besides serving fake overlays for banking apps, Sturnus is also capable of abusing Android's
[accessibility services](https://thehackernews.com/2025/03/new-android-trojan-crocodilus-abuses.html)
to capture keystrokes and record user interface (UI) interactions. As soon as an overlay for a bank is served to the victim and the credentials are harvested, the overlay for that specific target is disabled so as not to arouse the user's suspicion.

Furthermore, it can display a full-screen overlay that blocks all visual feedback and mimics the Android operating system update screen to give the impression to the user that software updates are in progress, when, in reality, it allows malicious actions to be carried out in the background.

Some of the malware's other features include support for monitoring device activity, as well as leveraging accessibility services to gather chat contents from Signal, Telegram, and WhatsApp when they are opened by the victim, and send details about every visible interface element on the screen.

This allows the attackers to reconstruct the layout at their end and remotely issue actions related to clicks, text input, scrolling, app launches, permission confirmations, and even enable a black screen overlay. An alternate remote control mechanism packed into Sturnus uses the system's display-capture framework to mirror the device screen in real-time.

"Whenever the user navigates to settings screens that could disable its administrator status, the malware detects the attempt through accessibility monitoring, identifies relevant controls, and automatically navigates away from the page to interrupt the user," ThreatFabric said.

"Until its administrator rights are manually revoked, both ordinary uninstallation and removal through tools like ADB are blocked, giving the malware strong protection against cleanup attempts."

The extensive environment monitoring capabilities make it possible to collect sensor information, network conditions, hardware data, and an inventory of installed apps. This device profile serves as a continuous feedback loop, helping attackers adapt their tactics to sidestep detection.

"Although the spread remains limited at this stage, the combination of targeted geography and high-value application focus implies that the attackers are refining their tooling ahead of broader or more coordinated operations," ThreatFabric said.