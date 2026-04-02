---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:58:55.047958+00:00'
exported_at: '2026-04-02T04:58:58.476761+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/32830
structured_data:
  about: []
  author: ''
  description: 'Apple Patches (almost) everything again. March 2026 edition., Author:
    Johannes Ullrich'
  headline: Apple Patches (almost) everything again. March 2026 edition., (Wed, Mar
    25th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/32830
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple Patches (almost) everything again. March 2026 edition., (Wed, Mar 25th)
updated_at: '2026-04-02T04:58:55.047958+00:00'
url_hash: 799b46146a18693f0ddc0ed1035024e9db4250ac
---

# [Apple Patches (almost) everything again. March 2026 edition.](/forums/diary/Apple+Patches+almost+everything+again+March+2026+edition/32830/)

**Published**
: 2026-03-25.
**Last Updated**
: 2026-03-25 21:29:57 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Apple+Patches+almost+everything+again+March+2026+edition/32830/#comments)

Apple released the next version of its operating system, patching 85 different vulnerabilities across all of them. None of the vulnerabilities are currently being exploited. The last three macOS "generations" are covered, as are the last two versions of iOS/iPadOS. For tvOS, watchOS, and visionOS, only the current version received patches. This update also includes the recently released Background Security Improvements. Some older watchOS versions received updates, but these updates do not address any security issues.

| iOS 26.4 and iPadOS 26.4 | iOS 18.7.7 and iPadOS 18.7.7 | macOS Tahoe 26.4 | macOS Sequoia 15.7.5 | macOS Sonoma 14.8.5 | tvOS 26.4 | watchOS 26.4 | visionOS 26.4 | Safari 26.4 | Xcode 26.4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2025-43376:** A remote attacker may be able to view leaked DNS queries with Private Relay turned on.   Affects WebKit | | | | | | | | | |
|  | x |  |  |  |  |  |  |  |  |
| **CVE-2025-43534:** A user with physical access to an iOS device may be able to bypass Activation Lock.   Affects iTunes Store | | | | | | | | | |
|  | x |  |  |  |  |  |  |  |  |
| **CVE-2026-20607:** An app may be able to access protected user data.   Affects libxpc | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20631:** A user may be able to elevate privileges.   Affects PackageKit | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20632:** An app may be able to access sensitive user data.   Affects Music | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20633:** An app may be able to access user-sensitive data.   Affects Archive Utility | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20637:** An app may be able to cause unexpected system termination.   Affects AppleKeyStore | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20639:** Processing a maliciously crafted string may lead to heap corruption.   Affects configd | | | | | | | | | |
|  |  |  | x | x |  |  |  |  |  |
| **CVE-2026-20643:** Processing maliciously crafted web content may bypass Same Origin Policy.   Affects WebKit | | | | | | | | | |
| x | x | x |  |  |  |  | x | x |  |
| **CVE-2026-20651:** An app may be able to access sensitive user data.   Affects Messages | | | | | | | | | |
|  |  |  | x |  |  |  |  |  |  |
| **CVE-2026-20657:** Parsing a maliciously crafted file may lead to an unexpected app termination.   Affects Vision | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20660:** A remote user may be able to write arbitrary files.   Affects CFNetwork | | | | | | | | | |
|  |  |  | x |  |  |  |  |  |  |
| **CVE-2026-20665:** Processing maliciously crafted web content may prevent Content Security Policy from being enforced.   Affects WebKit | | | | | | | | | |
| x | x | x |  |  | x | x | x | x |  |
| **CVE-2026-20668:** An app may be able to access sensitive user data.   Affects Focus | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-20684:** An app may bypass Gatekeeper checks.   Affects AppleScript | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-20687:** An app may be able to cause unexpected system termination or write kernel memory.   Affects Kernel | | | | | | | | | |
| x | x | x | x |  | x | x |  |  |  |
| **CVE-2026-20688:** An app may be able to break out of its sandbox.   Affects Printing | | | | | | | | | |
| x |  | x | x | x |  |  | x |  |  |
| **CVE-2026-20690:** Processing an audio stream in a maliciously crafted media file may terminate the process.   Affects CoreMedia | | | | | | | | | |
| x | x | x | x | x | x | x | x |  |  |
| **CVE-2026-20691:** A maliciously crafted webpage may be able to fingerprint the user.   Affects WebKit Sandboxing | | | | | | | | | |
| x |  | x |  |  |  | x | x | x |  |
| **CVE-2026-20692:** "Hide IP Address" and "Block All Remote Content" may not apply to all mail content.   Affects Mail | | | | | | | | | |
| x |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20693:** An attacker with root privileges may be able to delete protected system files.   Affects PackageKit | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20694:** An app may be able to access user-sensitive data.   Affects MigrationKit | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20695:** An app may be able to determine kernel memory layout.   Affects Kernel | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20697:** An app may be able to access sensitive user data.   Affects Spotlight | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20698:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | | | |
| x |  | x |  |  | x | x | x |  |  |
| **CVE-2026-20699:** An app may be able to access user-sensitive data.   Affects AppleMobileFileIntegrity | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-20701:** An app may be able to connect to a network share without user consent.   Affects NetAuth | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28816:** An app may be able to delete files for which it does not have permission.   Affects Notes | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28817:** A sandboxed process may be able to circumvent sandbox restrictions.   Affects Printing | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28818:** An app may be able to access sensitive user data.   Affects Spotlight | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28820:** An app may be able to access sensitive user data.   Affects StorageKit | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28821:** An app may be able to gain elevated privileges.   Affects CoreServices | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28822:** An attacker may be able to cause unexpected app termination.   Affects Audio | | | | | | | | | |
| x |  | x | x | x | x | x | x |  |  |
| **CVE-2026-28823:** An app with root privileges may be able to delete protected system files.   Affects Admin Framework | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28824:** An app may be able to access sensitive user data.   Affects AppleMobileFileIntegrity | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28825:** An app may be able to modify protected parts of the file system.   Affects SMB | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28826:** A malicious app may be able to break out of its sandbox.   Affects NSColorPanel | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28827:** An app may be able to break out of its sandbox.   Affects NetFSFramework | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28828:** An app may be able to access sensitive user data.   Affects TCC | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28829:** An app may be able to modify protected parts of the file system.   Affects WebDAV | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28831:** An app may be able to access sensitive user data.   Affects Printing | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28832:** An app may be able to disclose kernel memory.   Affects File System | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28833:** An app may be able to enumerate a user's installed apps.   Affects iCloud | | | | | | | | | |
| x |  | x |  |  |  |  | x |  |  |
| **CVE-2026-28834:** An app may be able to cause unexpected system termination.   Affects GPU Drivers | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28835:** Mounting a maliciously crafted SMB network share may lead to system termination.   Affects SMB | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28837:** An app may be able to access sensitive user data.   Affects System Settings | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28838:** An app may be able to break out of its sandbox.   Affects CoreServices | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28839:** An app may be able to access sensitive user data.   Affects NetAuth | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28841:** A buffer overflow may result in memory corruption and unexpected app termination.   Affects IOGraphics | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28842:** A buffer overflow may result in memory corruption and unexpected app termination.   Affects IOGraphics | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28844:** An attacker may gain access to protected parts of the file system.   Affects SystemMigration | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28845:** An app may be able to access protected user data.   Affects LaunchServices | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28852:** An app may be able to cause a denial-of-service.   Affects UIFoundation | | | | | | | | | |
| x | x | x | x |  | x | x | x |  |  |
| **CVE-2026-28856:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Siri | | | | | | | | | |
| x |  |  |  |  |  | x | x |  |  |
| **CVE-2026-28857:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | | | |
| x |  | x |  |  |  |  | x | x |  |
| **CVE-2026-28858:** A remote user may be able to cause unexpected system termination or corrupt kernel memory.   Affects Telephony | | | | | | | | | |
| x |  |  |  |  |  |  |  |  |  |
| **CVE-2026-28859:** A malicious website may be able to process restricted web content outside the sandbox.   Affects WebKit | | | | | | | | | |
| x |  | x |  |  | x | x | x | x |  |
| **CVE-2026-28861:** A malicious website may be able to access script message handlers intended for other origins.   Affects WebKit | | | | | | | | | |
| x | x | x |  |  |  |  | x | x |  |
| **CVE-2026-28862:** An app may be able to access user-sensitive data.   Affects Phone | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28863:** An app may be able to fingerprint the user.   Affects Sandbox Profiles | | | | | | | | | |
| x |  |  |  |  | x | x | x |  |  |
| **CVE-2026-28864:** A local attacker may gain access to user's Keychain items.   Affects Security | | | | | | | | | |
| x | x | x | x | x |  | x | x |  |  |
| **CVE-2026-28865:** An attacker in a privileged network position may be able to intercept network traffic.   Affects 802.1X | | | | | | | | | |
| x | x | x | x | x | x | x | x |  |  |
| **CVE-2026-28866:** An app may be able to access sensitive user data.   Affects Clipboard | | | | | | | | | |
| x | x | x | x | x |  |  |  |  |  |
| **CVE-2026-28867:** An app may be able to leak sensitive kernel state.   Affects Kernel | | | | | | | | | |
| x | x | x | x |  | x | x | x |  |  |
| **CVE-2026-28868:** An app may be able to disclose kernel memory.   Affects Kernel | | | | | | | | | |
| x | x | x | x | x |  | x | x |  |  |
| **CVE-2026-28870:** An app may be able to access sensitive user data.   Affects GeoServices | | | | | | | | | |
| x |  | x |  |  | x | x | x |  |  |
| **CVE-2026-28871:** Visiting a maliciously crafted website may lead to a cross-site scripting attack.   Affects WebKit | | | | | | | | | |
| x | x | x |  |  |  |  |  | x |  |
| **CVE-2026-28874:** A remote attacker may cause an unexpected app termination.   Affects Baseband | | | | | | | | | |
| x |  |  |  |  |  |  |  |  |  |
| **CVE-2026-28875:** A remote attacker may be able to cause a denial-of-service.   Affects Baseband | | | | | | | | | |
| x |  |  |  |  |  |  |  |  |  |
| **CVE-2026-28876:** An app may be able to access sensitive user data.   Affects DeviceLink | | | | | | | | | |
| x | x | x | x | x |  |  | x |  |  |
| **CVE-2026-28877:** An app may be able to access sensitive user data.   Affects Accounts | | | | | | | | | |
| x |  | x | x |  |  | x | x |  |  |
| **CVE-2026-28878:** An app may be able to enumerate a user's installed apps.   Affects Crash Reporter | | | | | | | | | |
| x | x | x |  | x | x | x | x |  |  |
| **CVE-2026-28879:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects Audio | | | | | | | | | |
| x | x | x | x | x | x | x | x |  |  |
| **CVE-2026-28880:** An app may be able to enumerate a user's installed apps.   Affects iCloud | | | | | | | | | |
|  | x |  | x | x |  |  |  |  |  |
| **CVE-2026-28881:** An app may be able to access sensitive user data.   Affects iCloud | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28882:** An app may be able to enumerate a user's installed apps.   Affects libxpc | | | | | | | | | |
| x |  | x |  |  | x | x | x |  |  |
| **CVE-2026-28886:** A user in a privileged network position may be able to cause a denial-of-service.   Affects CoreUtils | | | | | | | | | |
| x | x | x | x | x | x | x | x |  |  |
| **CVE-2026-28888:** An app may be able to gain root privileges.   Affects CUPS | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28889:** An app may be able to read arbitrary files as root.   Affects Simulator | | | | | | | | | |
|  |  |  |  |  |  |  |  |  | x |
| **CVE-2026-28890:** An app may be able to cause unexpected system termination.   Affects otool | | | | | | | | | |
|  |  |  |  |  |  |  |  |  | x |
| **CVE-2026-28891:** An app may be able to break out of its sandbox.   Affects NetAuth | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28892:** An app may be able to modify protected parts of the file system.   Affects Diagnostics | | | | | | | | | |
|  |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28893:** A document may be written to a temporary file when using print preview.   Affects CUPS | | | | | | | | | |
|  |  | x |  |  |  |  |  |  |  |
| **CVE-2026-28894:** A remote attacker may be able to cause a denial-of-service.   Affects Calling Framework | | | | | | | | | |
| x |  | x | x | x |  |  |  |  |  |
| **CVE-2026-28895:** An attacker with physical access to an iOS device with Stolen Device Protection enabled may be able to access biometrics-gated Protected Apps with the passcode.   Affects App Protection | | | | | | | | | |
| x |  |  |  |  |  |  |  |  |  |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[apple](/tag.html?tag=apple)
[ios](/tag.html?tag=ios)
[iPadOS](/tag.html?tag=iPadOS)
[macOS](/tag.html?tag=macOS)
[visionos](/tag.html?tag=visionos)
[watchos](/tag.html?tag=watchos)

[0 comment(s)](/diary/Apple+Patches+almost+everything+again+March+2026+edition/32830/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/32826)
* [next](/diary/32834)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)