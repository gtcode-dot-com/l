---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T03:24:15.887487+00:00'
exported_at: '2026-06-27T03:24:18.678793+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html
structured_data:
  about: []
  author: ''
  description: Russian intelligence phishing now seeks Signal Backup Recovery Keys
    to restore message backups and take over Signal accounts.
  headline: FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/fbi-warns-russian-intelligence-hackers.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: FBI Warns Russian Intelligence Hackers Target Signal Backup Recovery Keys
updated_at: '2026-06-27T03:24:15.887487+00:00'
url_hash: 20c00d895ed3a9110e06d6d54f8ae1337be27f78
---

**

Swati Khandelwal
**

Jun 26, 2026

Secure Messaging / Social Engineering

The FBI and CISA have updated
[their March warning](https://thehackernews.com/2026/03/fbi-warns-russian-hackers-target-signal.html)
about Russian intelligence phishing Signal accounts, and the operators have added a step: they now coax targets into handing over their Signal Backup Recovery Key.

Hand it over once, and the attacker can restore the account's backup, read the private and group message history, and take over the account. Worse, the key keeps working. Make a new account on the same phone number, and the old key can still be used against it, the advisory warns.

The fix is blunt: generate a new key in Settings, which kills the old one for future backup downloads, and accept that anything the attacker already pulled is gone.

The updated advisory,
[PSA I-062626-PSA](https://www.ic3.gov/PSA/2026/PSA260626)
, adds two public tracking names the
[March notice](https://www.ic3.gov/PSA/2026/PSA260320)
lacked: UNC5792 and UNC4221. The FBI ties the activity to multiple Russian Intelligence Services (RIS) groups, including FSB officers embedded with the FSB Border Guards and others working for the Russian military services. The campaign hits Signal and WhatsApp accounts; the new recovery-key tactic the advisory describes is specific to Signal.

The targets are individuals of high intelligence value: current and former U.S. and international government officials, military personnel, political figures, journalists, and officials in Ukraine. The March notice said the broader campaign had already compromised thousands of accounts worldwide.

The phishing message poses as Signal support. Earlier waves asked for SMS verification codes and account PINs, or used doctored "group invite" links that silently
[linked an attacker's device](https://thehackernews.com/2025/02/hackers-exploit-signals-linked-devices.html)
to the account.

The updated version walks the target through turning on Signal backups, opening the Recovery Key, and pasting it into the chat. The advisory prints two sample messages: one dressed up as a mandatory two-factor rollout, the other as an urgent "data recovery" fix for messages supposedly at risk of loss.

As in March, the agencies are clear that none of these breaks Signal's encryption or the app itself. The actors compromise individual accounts through social engineering, then walk in through a legitimate feature.

Alongside the update, the State Department's
[Rewards for Justice](https://rewardsforjustice.net/rewards/unc5792/)
program is offering up to $10 million for information on UNC5792.

The activity overlaps with warnings from Dutch intelligence (AIVD and MIVD),
[Germany's BfV and BSI](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html)
, and France's ANSSI earlier this year. Google's Threat Intelligence Group
[first documented](https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger/)
UNC5792 abusing Signal's linked-device feature in early 2025, and saw the same tradecraft turn up against WhatsApp and Telegram.

## What to do now

* Treat any in-app message from "Signal support" as hostile. Real support does not message you inside the app to ask for codes, PINs, or your Recovery Key.
* Never paste your Backup Recovery Key, verification code, or PIN into a chat. Nothing legitimate asks for them that way.
* Open Settings, check Linked Devices, and remove anything you do not recognize.
* If you think you handed over your Recovery Key, generate a new one in Settings now, and assume any backup made before that is already in someone else's hands.

The March notice warned the tactics would shift. They have, from chasing one-time codes to taking the key that opens the entire archive. The encryption holds. The account is the weak point, and the person holding it is the target.