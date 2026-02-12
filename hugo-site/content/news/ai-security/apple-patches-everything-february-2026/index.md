---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-12T22:15:24.311081+00:00'
exported_at: '2026-02-12T22:15:26.845989+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32706
structured_data:
  about: []
  author: ''
  description: 'Apple Patches Everything: February 2026, Author: Johannes Ullrich'
  headline: 'Apple Patches Everything: February 2026, (Wed, Feb 11th)'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32706
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'Apple Patches Everything: February 2026, (Wed, Feb 11th)'
updated_at: '2026-02-12T22:15:24.311081+00:00'
url_hash: cd6444f0f50fba529e802745cbb1d2efada8f161
---

# [Apple Patches Everything: February 2026](/forums/diary/Apple+Patches+Everything+February+2026/32706/)

**Published**
: 2026-02-11.
**Last Updated**
: 2026-02-11 19:36:59 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Apple+Patches+Everything+February+2026/32706/#comments)

Today, Apple released updates for all of its operating systems (iOS, iPadOS, macOS, tvOS, watchOS, and visionOS). The update fixes 71 distinct vulnerabilities, many of which affect multiple operating systems. Older versions of iOS, iPadOS, and macOS are also updated.

OF special note is CVE-2026-20700. This vulnerability has already been exploited in targeted attacks. It allows attackers who can write to memory to execute code. Two vulnerabilities patched in December are related to the same attack (CVE-2025-14174 and CVE-2025-43529).

Interesting are additional Siri/Voice Over vulnerabilities that allow access to some information on locked devices. This is a recurring issue, and you should probably turn off VoiceOver and Siri on locked devices. Another recurring and likely impossible to completely eliminate threat is applications being able to access data from other applications. To reduce the probability of exploitation, limit the Apps you install on your devices.

| iOS 26.3 and iPadOS 26.3 | iOS 18.7.5 and iPadOS 18.7.5 | macOS Tahoe 26.3 | macOS Sequoia 15.7.4 | macOS Sonoma 14.8.4 | tvOS 26.3 | watchOS 26.3 | visionOS 26.3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43338:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.   Affects ImageIO | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-43402:** An app may be able to cause unexpected system termination or corrupt process memory.   Affects WindowServer | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-43403:** An app may be able to access sensitive user data.   Affects Compression | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-43417:** An app may be able to access user-sensitive data.   Affects File Bookmark | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-43537:** Restoring a maliciously crafted backup file may lead to modification of protected system files.   Affects Books | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2025-46283:** An app may be able to access sensitive user data.   Affects CoreServices | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2025-46290:** A remote attacker may be able to cause a denial-of-service.   Affects Security | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2025-46305:** A malicious HID device may cause an unexpected process crash.   Affects Multi-Touch | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2025-46310:** An attacker with root privileges may be able to delete protected system files.   Affects PackageKit | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-20601:** An app may be able to monitor keystrokes without user permission.   Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20602:** An app may be able to cause a denial-of-service.   Affects WindowServer | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20603:** An app with root privileges may be able to access private information.   Affects Notification Center | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20605:** An app may be able to crash a system process.   Affects Voice Control | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-20606:** An app may be able to bypass certain Privacy preferences.   Affects UIKit | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-20608:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-20609:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.   Affects CoreMedia | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20610:** An app may be able to gain root privileges.   Affects Setup Assistant | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20611:** Processing a maliciously crafted media file may lead to unexpected app termination or corrupt process memory.   Affects CoreAudio | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20612:** An app may be able to access sensitive user data.   Affects Spotlight | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20614:** An app may be able to gain root privileges.   Affects Remote Management | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20615:** An app may be able to gain root privileges.   Affects CoreServices | | | | | | | |
| x |  | x |  | x |  |  | x |
| **CVE-2026-20616:** Processing a maliciously crafted USD file may lead to unexpected app termination.   Affects Model I/O | | | | | | | |
|  | x | x |  | x |  |  | x |
| **CVE-2026-20617:** An app may be able to gain root privileges.   Affects CoreServices | | | | | | | |
| x |  | x |  | x | x | x | x |
| **CVE-2026-20618:** An app may be able to access user-sensitive data.   Affects System Settings | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20619:** An app may be able to access sensitive user data.   Affects System Settings | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-20620:** An attacker may be able to cause unexpected system termination or read kernel memory.   Affects GPU Drivers | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20621:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Wi-Fi | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-20623:** An app may be able to access protected user data.   Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20624:** An app may be able to access sensitive user data.   Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20625:** An app may be able to access sensitive user data.   Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  | x |
| **CVE-2026-20626:** A malicious app may be able to gain root privileges.   Affects Kernel | | | | | | | |
| x |  | x | x |  |  |  | x |
| **CVE-2026-20627:** An app may be able to access sensitive user data.   Affects CoreServices | | | | | | | |
| x |  | x |  | x |  | x | x |
| **CVE-2026-20628:** An app may be able to break out of its sandbox.   Affects Sandbox | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20629:** An app may be able to access user-sensitive data.   Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20630:** An app may be able to access protected user data.   Affects LaunchServices | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20634:** Processing a maliciously crafted image may result in disclosure of process memory.   Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20635:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-20638:** A user with Live Caller ID app extensions turned off could have identifying information leaked to the extensions.   Affects Call History | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-20640:** An attacker with physical access to iPhone may be able to take and view screenshots of sensitive data from the iPhone during iPhone Mirroring with Mac.   Affects UIKit | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-20641:** An app may be able to identify what other apps a user has installed.   Affects StoreKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20642:** A person with physical access to an iOS device may be able to access photos from the lock screen.   Affects Photos | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-20645:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Accessibility | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20646:** A malicious app may be able to read sensitive location information.   Affects Weather | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20647:** An app may be able to access sensitive user data.   Affects Siri | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20648:** A malicious app may be able to access notifications from other iCloud devices.   Affects Siri | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20649:** A user may be able to view sensitive user information.   Affects Game Center | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-20650:** An attacker in a privileged network position may be able to perform denial-of-service attack using crafted Bluetooth packets.   Affects Bluetooth | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-20652:** A remote attacker may be able to cause a denial-of-service.   Affects WebKit | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-20653:** An app may be able to access sensitive user data.   Affects Shortcuts | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-20654:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-20655:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Live Captions | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20656:** An app may be able to access a user's Safari history.   Affects Safari | | | | | | | |
|  | x | x |  |  |  |  |  |
| **CVE-2026-20658:** An app may be able to gain root privileges.   Affects Security | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20660:** A remote user may be able to write arbitrary files.   Affects CFNetwork | | | | | | | |
| x | x | x |  | x |  |  | x |
| **CVE-2026-20661:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects VoiceOver | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20662:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Siri | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-20663:** An app may be able to enumerate a user's installed apps.   Affects LaunchServices | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20666:** An app may be able to access sensitive user data.   Affects NSOpenPanel | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20667:** An app may be able to break out of its sandbox.   Affects libxpc | | | | | | | |
| x |  | x | x | x |  | x |  |
| **CVE-2026-20669:** An app may be able to access sensitive user data.   Affects Admin Framework | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20671:** An attacker in a privileged network position may be able to intercept network traffic.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20673:** Turning off "Load remote content in messages? may not apply to all mail previews.   Affects Mail | | | | | | | |
|  | x | x | x | x |  |  |  |
| **CVE-2026-20674:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Accessibility | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-20675:** Processing a maliciously crafted image may lead to disclosure of user information.   Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-20676:** A website may be able to track users through Safari web extensions.   Affects WebKit | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-20677:** A shortcut may be able to bypass sandbox restrictions.   Affects Messages | | | | | | | |
| x | x | x |  | x |  |  | x |
| **CVE-2026-20678:** An app may be able to access sensitive user data.   Affects Sandbox Profiles | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20680:** A sandboxed app may be able to access sensitive user data.   Affects Spotlight | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-20681:** An app may be able to access information about a user's contacts.   Affects Contacts | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-20682:** An attacker may be able to discover a user's deleted notes.   Affects Screenshots | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-20700:** An attacker with memory write capability may be able to execute arbitrary code. **Apple is aware of a report that this issue may have been exploited in an extremely sophisticated attack against specific targeted individuals on versions of iOS before iOS 26. CVE-2025-14174 and CVE-2025-43529 were also issued in response to this report** ..   Affects dyld | | | | | | | |
| x |  | x |  |  | x | x | x |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:

[0 comment(s)](/diary/Apple+Patches+Everything+February+2026/32706/#comments)

My next class:

|  |  |  |
| --- | --- | --- |
| [Application Security: Securing Web Apps, APIs, and Microservices](https://www.sans.org/event/sans-2026/course/application-security-securing-web-apps-api-microservices) | Orlando | Mar 29th - Apr 3rd 2026 |

* [previous](/diary/32704)
* [next](/diary/32708)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)