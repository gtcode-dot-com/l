---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T21:16:51.381666+00:00'
exported_at: '2026-05-14T21:16:53.801843+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32976
structured_data:
  about: []
  author: ''
  description: 'Apple Patches Everything, Author: Johannes Ullrich'
  headline: Apple Patches Everything, (Mon, May 11th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32976
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple Patches Everything, (Mon, May 11th)
updated_at: '2026-05-14T21:16:51.381666+00:00'
url_hash: 551e7073ab1d7d6ea0d6b6d42617a7f0c89b2907
---

# [Apple Patches Everything](/forums/diary/Apple+Patches+Everything/32976/)

**Published**
: 2026-05-11.
**Last Updated**
: 2026-05-11 22:19:13 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Apple+Patches+Everything/32976/#comments)

Apple today released its typical feature update across it's operating systems (iOS, iPadOS, macOS, tvOS, watchOS, vision OS). With this update, Apple patched 84 different vulnerabilities. Updates are available for the "26" series of operating systems, as well as for the previous "18" version of iOS/iPadOS, and two versions back for macOS (version 14 and 15).

None of the vulnerabilities has been exploited. The number of addressed vulnerabilities is about average compared to similar Apple updates.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-05-11%20at%203_17_51%E2%80%AFPM.png)

Figure: Number of Vulnerabilities patched for each security update. Last one in red at the end.

| iOS 26.5 and iPadOS 26.5 | iOS 18.7.9 and iPadOS 18.7.9 | macOS Tahoe 26.5 | macOS Sequoia 15.7.7 | macOS Sonoma 14.8.7 | tvOS 26.5 | watchOS 26.5 | visionOS 26.5 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43524:** An app may be able to break out of its sandbox.   Affects Icons | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-28819:** An app may be able to execute arbitrary code with kernel privileges.   Affects Wi-Fi | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28840:** An app may be able to gain root privileges.   Affects PackageKit | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-28846:** A remote attacker may be able to cause unexpected app termination.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28848:** A remote attacker may be able to cause unexpected system termination.   Affects SMB | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-28870:** An app may be able to access sensitive user data.   Affects GeoServices | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28872:** A remote attacker may be able to cause a denial-of-service.   Affects Calendar | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28873:** An app may be able to circumvent App Privacy Report logging.   Affects Privacy | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28877:** An app may be able to access sensitive user data.   Affects Accounts | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28878:** An app may be able to enumerate a user's installed apps.   Affects Crash Reporter | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2026-28882:** An app may be able to enumerate a user's installed apps.   Affects libxpc | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28883:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-28894:** A remote attacker may be able to cause a denial-of-service.   Affects Calling Framework | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28897:** A local user may be able to cause unexpected system termination or read kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28901:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-28906:** An attacker may be able to track users through their IP address.   Affects Networking | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-28907:** Processing maliciously crafted web content may prevent Content Security Policy from being enforced.   Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28908:** An app may be able to modify protected parts of the file system.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28913:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-28914:** A maliciously crafted ZIP archive may bypass Gatekeeper checks.   Affects zip | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28915:** An app may be able to gain root privileges.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28917:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28918:** Parsing a maliciously crafted file may lead to an unexpected app termination.   Affects CoreSymbolication | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-28919:** An app may be able to gain root privileges.   Affects StorageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28920:** Visiting a maliciously crafted website may leak sensitive data.   Affects zlib | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28922:** An app may be able to access private information.   Affects CoreMedia | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28923:** A malicious app may be able to break out of its sandbox.   Affects GPU Drivers | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28924:** An app may be able to access Contacts without user consent.   Affects Sync Services | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28925:** An app may be able to cause unexpected system termination or write kernel memory.   Affects HFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28929:** Replying to an email could display remote images in Mail in Lockdown Mode.   Affects Mail Drafts | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28930:** An app may be able to access protected user data.   Affects Spotlight | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28936:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects CoreServices | | | | | | | |
| x | x | x |  | x |  |  | x |
| **CVE-2026-28940:** Processing a maliciously crafted image may corrupt process memory.   Affects Model I/O | | | | | | | |
| x | x | x | x |  | x |  | x |
| **CVE-2026-28941:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.   Affects Model I/O | | | | | | | |
|  | x | x | x |  |  |  |  |
| **CVE-2026-28942:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-28943:** An app may be able to determine kernel memory layout.   Affects IOHIDFamily | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-28944:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebRTC | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-28947:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-28951:** An app may be able to gain root privileges.   Affects Kernel | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-28952:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28953:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-28954:** A maliciously crafted disk image may bypass Gatekeeper checks.   Affects Kernel | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-28956:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.   Affects AppleJPEG | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-28957:** An app may be able to capture a user's screen.   Affects Status Bar | | | | | | | |
| x | x |  |  |  |  |  | x |
| **CVE-2026-28958:** An app may be able to access sensitive user data.   Affects WebKit | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-28959:** An app may be able to cause unexpected system termination.   Affects APFS | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28961:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Network Extensions | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28962:** Processing maliciously crafted web content may disclose sensitive user information.   Affects WebKit | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-28963:** An attacker with physical access may be able to use Visual Intelligence to access sensitive user data during iPhone Mirroring.   Affects Screenshots | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-28964:** An app may be able to access sensitive user data.   Affects CoreAnimation | | | | | | | |
| x |  |  |  |  |  |  | x |
| **CVE-2026-28965:** A user may be able to view restricted content from the lock screen.   Affects WidgetKit | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-28969:** An app may be able to cause unexpected system termination.   Affects IOKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28971:** A malicious iframe may use another website?s download settings.   Affects WebKit | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-28972:** An app may be able to cause unexpected system termination or write kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28974:** An app may be able to cause a denial-of-service.   Affects Spotlight | | | | | | | |
| x |  | x | x |  | x | x | x |
| **CVE-2026-28976:** An app may be able to gain root privileges.   Affects UserAccountUpdater | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28977:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28978:** A malicious app may be able to break out of its sandbox.   Affects Installer | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28983:** A remote attacker may be able to cause a denial of service.   Affects LaunchServices | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28985:** An attacker on the local network may be able to cause a denial-of-service.   Affects mDNSResponder | | | | | | | |
| x |  | x |  |  | x |  |  |
| **CVE-2026-28986:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-28987:** An app may be able to leak sensitive kernel state.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-28988:** An app may be able to bypass certain Privacy preferences.   Affects Accounts | | | | | | | |
| x |  | x |  |  |  | x | x |
| **CVE-2026-28990:** Processing a maliciously crafted image may corrupt process memory.   Affects ImageIO | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-28991:** An app may be able to cause a denial-of-service.   Affects Accelerate | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-28992:** An attacker may be able to cause unexpected app termination.   Affects IOHIDFamily | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28993:** An app may be able to access user-sensitive data.   Affects Shortcuts | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-28994:** An attacker in a privileged network position may be able to perform denial-of-service attack using crafted Wi-Fi packets.   Affects Wi-Fi | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-28995:** A malicious app may be able to break out of its sandbox.   Affects App Intents | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-28996:** An app may be able to access sensitive user data.   Affects Storage | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-39869:** Processing an audio stream in a maliciously crafted media file may terminate the process.   Affects Audio | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-39870:** Processing a maliciously crafted image may corrupt process memory.   Affects SceneKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-39871:** An app may be able to observe unprotected user data.   Affects TV App | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43652:** An app may be able to access protected user data.   Affects Sandbox | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43653:** An attacker on the local network may be able to cause a denial-of-service.   Affects mDNSResponder | | | | | | | |
| x | x | x |  | x | x |  |  |
| **CVE-2026-43654:** An app may be able to disclose kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-43655:** An app may be able to cause unexpected system termination or read kernel memory.   Affects IOSurfaceAccelerator | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-43656:** Parsing a maliciously crafted file may lead to an unexpected app termination.   Affects Quick Look | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-43658:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-43659:** An app may be able to access sensitive user data.   Affects FileProvider | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-43660:** Processing maliciously crafted web content may prevent Content Security Policy from being enforced.   Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-43661:** Processing a maliciously crafted image may corrupt process memory.   Affects ImageIO | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-43666:** An attacker on the local network may be able to cause a denial-of-service.   Affects mDNSResponder | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-43668:** A remote attacker may be able to cause unexpected system termination or corrupt kernel memory.   Affects mDNSResponder | | | | | | | |
| x | x | x | x | x | x | x | x |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[apple patches](/tag.html?tag=apple patches)

[0 comment(s)](/diary/Apple+Patches+Everything/32976/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32974)
* [next](/diary/32980)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)