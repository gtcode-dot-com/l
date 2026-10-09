---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-21T12:15:14.265324+00:00'
exported_at: '2026-04-21T12:15:16.720651+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/ngate-campaign-targets-brazil.html
structured_data:
  about: []
  author: ''
  description: NGate abuses HandyPay in Brazil since Nov 2025, stealing NFC data and
    PINs to enable ATM fraud and unauthorized payments.
  headline: NGate Campaign Targets Brazil, Trojanizes HandyPay to Steal NFC Data and
    PINs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/ngate-campaign-targets-brazil.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: NGate Campaign Targets Brazil, Trojanizes HandyPay to Steal NFC Data and PINs
updated_at: '2026-04-21T12:15:14.265324+00:00'
url_hash: d4a8d13feaf9a7cee4a367162921f441d9e4ade4
---

**

Ravie Lakshmanan
**

Apr 21, 2026

Mobile Security / Artificial Intelligence

Cybersecurity researchers have discovered a new iteration of an Android malware family called
**NGate**
that has been found to abuse a legitimate application called
[HandyPay](https://handypay.app/)
instead of NFCGate.

"The threat actors took the app, which is used to relay NFC data, and patched it with malicious code that appears to have been AI-generated," ESET security researcher Lukáš Štefanko
[said](https://www.welivesecurity.com/en/eset-research/new-ngate-variant-hides-in-a-trojanized-nfc-payment-app/)
in a report shared with The Hacker News. "As with previous iterations of NGate, the malicious code allows the attackers to transfer NFC data from the victim's payment card to their own device and use it for contactless ATM cash-outs and unauthorized payments."

In addition, the malicious payload is capable of capturing the victim's payment card PIN and exfiltrating it to the threat actor's command-and-control (C2) server.

NGate, also known as NFSkate, was
[first publicly documented](https://thehackernews.com/2024/08/new-android-malware-ngate-steals-nfc.html)
by the Slovakian cybersecurity vendor in August 2024, detailing its ability to carry out relay attacks to siphon victims' contactless payment data with an aim to conduct fraudulent transactions.

A year later, Dutch mobile security company ThreatFabric
[detailed](https://thehackernews.com/2025/09/raton-android-malware-detected-with-nfc.html)
a threat codenamed RatOn that used dropper apps impersonating adult-friendly versions of TikTok to deploy NGate to carry out
[NFC relay attacks](https://thehackernews.com/2025/08/new-android-malware-wave-hits-banking.html)
.

The latest version of NGate detected by ESET has primarily targeted users in Brazil, marking the first such campaign to single out the South American nation. The trojanized HandyPay application is distributed via websites masquerading as Rio de Prêmios, a lottery run by the Rio de Janeiro state lottery organization, and a Google Play Store listing page for a purported card protection app.

The fake lottery website seeks to convince a user to tap a button to send a WhatsApp message to claim the prize money, at which point they are directed to likely download the poisoned version of the HandyPay app.Regardless of the method used, the app asks to be set as the default payment app following installation.

Then, the victim is asked to enter the payment card PIN into the app and tap their card on the back of the NFC-enabled smartphone. As soon as this step is carried out, the malware abuses HandyPay to capture and relay the NFC card data to an attacker-controlled device, thereby allowing them to use the stolen information to make cash withdrawals from ATMs.

The active campaign is assessed to have begun around November 2025. The malicious version of HandyPay has never been made available on the Google Play Store, meaning attackers are using the aforementioned methods as delivery mechanisms to trick unsuspecting users into downloading them. HandyPay has since launched an internal investigation into the matter.

ESET noted that the cheaper subscription prices for HandyPay may have caused the operators of the campaign to switch as opposed to sticking with existing turnkey solutions that cost north of $400 per month. "In addition to the price, HandyPay natively does not require any permissions, only to be made the default payment app, helping the threat actors avoid raising suspicion," the company pointed out.

An analysis of the artifact has revealed the presence of emojis in debug and toast messages, highlighting the possible use of a large language model (LLM) to generate or modify the source code. While conclusive proof remains elusive, the development aligns with a broader trend of cybercriminals latching on to generative artificial intelligence (AI) to produce malware even with little to no technical expertise.

"With the appearance of yet another NGate campaign on the scene, it can be plainly seen that NFC fraud is on the rise," ESET said. "This time, instead of using an established solution such as NFCGate or a MaaS on offer, the threat actors decided to trojanize HandyPay, an application with existing NFC relay functionality."