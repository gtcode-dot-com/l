---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T10:15:14.574934+00:00'
exported_at: '2026-04-23T10:15:16.783677+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/apple-patches-ios-flaw-that-stored.html
structured_data:
  about: []
  author: ''
  description: Apple fixes CVE-2026-28950 in iOS 26.4.2 after deleted notifications
    were retained, mitigating forensic data exposure.
  headline: Apple Patches iOS Flaw That Stored Deleted Signal Notifications in FBI
    Forensic Case
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/apple-patches-ios-flaw-that-stored.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple Patches iOS Flaw That Stored Deleted Signal Notifications in FBI Forensic
  Case
updated_at: '2026-04-23T10:15:14.574934+00:00'
url_hash: ed49d08cfdbb4939af4f487ed57c1935bef28680
---

**

Ravie Lakshmanan
**

Apr 23, 2026

Vulnerability / Encryption

Apple has rolled out a software fix for iOS and iPadOS to address a Notification Services flaw that stored notifications marked for deletion on the device.

The vulnerability, tracked as CVE-2026-28950 (CVSS score: N/A), has been described as a logging issue that has been addressed with improved data redaction.

"Notifications marked for deletion could be unexpectedly retained on the device," Apple said in an advisory.

The shortcoming affects the following devices -

* iPhone 11 and later, iPad Pro 12.9-inch 3rd generation and later, iPad Pro 11-inch 1st generation and later, iPad Air 3rd generation and later, iPad 8th generation and later, and iPad mini 5th generation and later - Fixed in
  [iOS 26.4.2 and iPadOS 26.4.2](https://support.apple.com/en-us/127002)
* iPhone XR, iPhone XS, iPhone XS Max, iPhone 11 (all models), iPhone SE (2nd generation), iPhone 12 (all models), iPhone 13 (all models), iPhone SE (3rd generation), iPhone 14 (all models), iPhone 15 (all models), iPhone 16 (all models), iPhone 16e, iPad mini (5th generation - A17 Pro), iPad (7th generation - A16), iPad Air (3rd - 5th generation), iPad Air 11-inch (M2 - M3), iPad Air 13-inch (M2 - M3), iPad Pro 11-inch (1st generation - M4), iPad Pro 12.9-inch (3rd - 6th generation), and iPad Pro 13-inch (M4) - Fixed in
  [iOS 18.7.8 and iPadOS 18.7.8](https://support.apple.com/en-us/127003)

The update comes weeks after a report from 404 Media that the U.S. Federal Bureau of Investigation (FBI)
[managed](https://thehackernews.com/2026/04/weekly-recap-fiber-optic-spying-windows.html#:~:text=FBI%20Extracts%20Signal%20Messages%20from%20iOS%20Notification%20History%20Database)
to forensically extract copies of incoming Signal messages
[from a defendant's iPhone](https://prairielanddefendants.com/court-notes/march-10-federal-trial-day-12/)
, even after the app was deleted, by taking advantage of the fact that copies of the content were saved in the device's push notification database.

It's not known why the notifications' content was logged in the device to begin with, but the latest update suggests it was a bug. That said, it's unclear when this issue was introduced, and if there have been prior cases where such data may have been captured by authorities using forensic tools.

While Signal already has an option to prevent the content of incoming messages from being displayed in notifications, the development highlighted how physical access to a device can facilitate the extraction of sensitive data from at-risk users.

"For most app notifications, there's no simple way to easily figure out what metadata might be gleaned from a notification, or if the notification is unencrypted or not," the Electronic Frontier Foundation (EFF)
[said](https://www.eff.org/deeplinks/2026/04/how-push-notifications-can-betray-your-privacy-and-what-do-about-it)
. "It's also good to reconsider whether any app should be sending you notifications to begin with."

To prevent the message content from showing in notifications, users can
[navigate](https://support.signal.org/hc/en-us/articles/360043273491-In-App-Notification-Options)
to their profile > Notifications > Show, and select one of the following: "Name only" or "No name or message."

"Note that no action is needed for this fix to protect Signal users on iOS," Signal
[said](https://x.com/signalapp/status/2047070518776356996)
in a post on X. "Once you install the patch, all inadvertently-preserved notifications will be deleted, and no forthcoming notifications will be preserved for deleted applications."

"We're grateful to Apple for the quick action here, and for understanding and acting on the stakes of this kind of issue. It takes an ecosystem to preserve the fundamental human right to private communication."