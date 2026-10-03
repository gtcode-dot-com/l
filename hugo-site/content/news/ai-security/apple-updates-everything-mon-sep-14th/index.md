---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T04:42:54.578080+00:00'
exported_at: '2026-10-03T04:42:55.902537+00:00'
feed: https://isc.sans.edu/rssfeed.xml
language: en
source_url: https://isc.sans.edu/diary/rss/33336
structured_data:
  about: []
  author: ''
  description: 'Apple Updates Everything, Author: Johannes Ullrich'
  headline: Apple Updates Everything, (Mon, Sep 14th)
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://isc.sans.edu/diary/rss/33336
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Apple Updates Everything, (Mon, Sep 14th)
updated_at: '2026-10-03T04:42:54.578080+00:00'
url_hash: 5822efeadc1a33660f9e59155e074be886246d6f
---

# [Apple Updates Everything](/forums/diary/Apple+Updates+Everything/33336/)

**Published**
: 2026-09-14.
**Last Updated**
: 2026-09-14 18:33:44 UTC

**by**
[Johannes Ullrich](https://plus.google.com/101587262224166552564?rel=author)
(Version: 1)

[0 comment(s)](/diary/Apple+Updates+Everything/33336/#comments)

Today, Apple released its annual update across all its operating systems. With that, Apple not only released new features but also patched 261 different vulnerabilities. This is the most vulnerabilities Apple has ever patched, but the increase is not as significant as other vendors' "post-AI" patch releases.

In addition to the major "27" version, Apple also released bug-fix-only releases for the 26 branch of its operating systems and for 15 (Sequioa) for macOS. None of the vulnerabilities is labeled as being exploited. Apple does not note a severity to individual vulnerabilities.

There are some reports about difficulties downloading iOS 27. Users instead see 26.7 downloaded, but iOS 27 may actually be installed. Also note that some security-relevant applications, such as Little Snitch, have recently released updates that must be applied before upgrading to macOS 27. The Objective-See utility BlockBlock released version 2.5.2 to improve macOS 27 compatiblity.

![](https://isc.sans.edu/diaryimages/images/Screenshot%202026-09-14%20at%202_23_35%E2%80%AFPM.png)

Figure: Number of patches for each update over the last 2 years.

| iOS 27 and iPadOS 27 | iOS 26.7 and iPadOS 26.7 | macOS Golden Gate 27 | macOS Tahoe 26.7 | macOS Sequoia 15.8 | tvOS 27 | watchOS 27 | visionOS 27 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **CVE-2022-3437:** A user in a privileged network position may be able to leak sensitive user information.   Affects Heimdal | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-20683:** An app may be able to use the Sign In With Apple authentication flow to access the user's Apple Account.   Affects Apple Account | | | | | | | |
| x |  | x | x | x |  |  | x |
| **CVE-2026-28899:** An app may bypass Gatekeeper checks.   Affects WebDAV | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28930:** An app may be able to access protected user data.   Affects Spotlight | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2026-28934:** Mounting a malicious disk image may cause unexpected system termination.   Affects HFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-28935:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-28937:** An app may be able to access sensitive user data.   Affects Terminal | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-28966:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects RealityKit | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-28968:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-28969:** An app may be able to cause unexpected system termination.   Affects IOKit | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-34979:** An attacker in a privileged network position may be able to cause a denial-of-service.   Affects CUPS | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43661:** Processing a maliciously crafted image may corrupt process memory.   Affects ImageIO | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-43664:** An app may be able to access sensitive user data.   Affects Accessibility | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-43674:** An attacker with physical access to an unlocked device may be able to view Wi-Fi passwords without authentication.   Affects Wi-Fi3 | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-43677:** Connecting to a malicious WebDAV server may lead to unexpected app termination.   Affects WebDAV | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43683:** An app may be able to cause unexpected process termination or disclose process memory.   Affects CoreDrag | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43684:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  | x | x |  | x |  |  |  |
| **CVE-2026-43686:** Connecting to a malicious NFS server may lead to kernel memory corruption.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-43687:** Connecting to a malicious NFS server may disclose kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x |  | x | x | x |
| **CVE-2026-43688:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects Filters | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-43689:** A malicious app may be able to gain root privileges.   Affects Kernel | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-43690:** A local user may be able to read kernel memory.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43691:** An app may be able to gain root privileges.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43692:** A remote user may cause an unexpected app termination or arbitrary code execution.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43695:** An app may be able to access sensitive user data.   Affects NetworkExtension | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-43696:** An app may be able to capture Touch Bar content without authorization.   Affects Touch Bar | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43697:** Processing a maliciously crafted 3D file may lead to an out-of-bounds read.   Affects SceneKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43698:** An app may be able to gain root privileges.   Affects CUPS | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-43702:** Processing a maliciously crafted video file may lead to unexpected app termination or corrupt process memory.   Affects CoreMedia Video Toolbox | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2026-43715:** Processing maliciously crafted web content may lead to memory corruption.   Affects WebKit | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-43719:** Mounting a maliciously crafted SMB network share may lead to system termination.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43737:** An app may be able to access motion data from headphones without user consent.   Affects CoreMotion | | | | | | | |
| x | x | x | x | x | x | x |  |
| **CVE-2026-43738:** Processing a maliciously crafted asset catalog may result in disclosure of process memory.   Affects CoreUI | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-43741:** An app may be able to access protected user data.   Affects Messages | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43743:** An app may be able to cause unexpected system termination.   Affects IOGPUFamily | | | | | | | |
|  | x |  | x |  |  |  |  |
| **CVE-2026-43760:** An app may be able to access user-sensitive data.   Affects Screen Sharing Server | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2026-43763:** An app may be able to read files outside of its sandbox.   Affects ATS | | | | | | | |
|  |  |  | x | x |  |  |  |
| **CVE-2026-43785:** An app may be able to modify a file it only had permission to read.   Affects File Bookmark | | | | | | | |
| x |  | x | x | x | x |  | x |
| **CVE-2026-43786:** An app may be able to gain root privileges.   Affects CoreServices | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43787:** An attacker in a privileged network position may be able to leak sensitive user information.   Affects Mail | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43788:** Processing a maliciously crafted file may lead to a denial-of-service or potentially disclose memory contents.   Affects Spotlight | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-43789:** An app may be able to access user-sensitive data.   Affects CoreMedia | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43790:** A remote attacker may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43791:** An app may be able to read arbitrary files.   Affects StorageKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-43794:** Processing maliciously crafted web content may lead to memory corruption.   Affects WebKit | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-64712:** An app may be able to gain root privileges.   Affects odproxyd | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-64714:** Processing a maliciously crafted image may lead to a denial-of-service.   Affects ImageIO | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-64715:** Processing maliciously crafted web content may lead to an unexpected process crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-64718:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit Canvas | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-64736:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects IOMobileFrameBuffer | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-64752:** Processing a maliciously crafted image may lead to arbitrary code execution.   Affects CoreMedia | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-64753:** Processing maliciously crafted web content may disclose sensitive user information.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-64756:** An app may be able to access user-sensitive data.   Affects Image Capture | | | | | | | |
| x |  | x | x | x |  |  |  |
| **CVE-2026-64758:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects ImageIO | | | | | | | |
|  | x |  |  | x |  |  |  |
| **CVE-2026-64760:** An app may be able to leak sensitive kernel state.   Affects IOSurfaceAccelerator | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-64761:** An app may be able to identify what other apps a user has installed.   Affects Accessibility | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-64778:** Visiting a maliciously crafted website may leak sensitive data.   Affects WebKit History | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-64779:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit Storage | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-64780:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-64781:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-64782:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-64784:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-64787:** Processing maliciously crafted web content may lead to an unexpected process termination.   Affects WebKit | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-64788:** Processing maliciously crafted web content may lead to memory corruption.   Affects IOGPUFamily | | | | | | | |
|  |  |  |  |  |  | x | x |
| **CVE-2026-64790:** An app may be able to gain elevated privileges.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65329:** An attacker in a privileged network position may be able to bypass IPSec authentication and intercept network traffic.   Affects Telephony | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-65331:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-65334:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-65338:** Processing maliciously crafted web content may lead to an unexpected Safari crash.   Affects WebKit | | | | | | | |
|  |  |  |  |  |  |  | x |
| **CVE-2026-65339:** An app may be able to leak sensitive user information.   Affects Audio | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-65341:** Processing maliciously crafted web content may lead to memory corruption.   Affects WebKit | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-65342:** An app may be able to access sensitive user data.   Affects ATS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65343:** A remote attacker may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-65344:** Processing a maliciously crafted video file may lead to unexpected app termination.   Affects CoreMedia | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-65345:** An app may be able to access user-sensitive data.   Affects Storage | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-65346:** Processing an image may lead to arbitrary code execution.   Affects ImageIO | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-65347:** Processing an image may lead to a denial-of-service.   Affects ImageIO | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-65348:** An app may be able to modify protected parts of the file system.   Affects Storage | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-65349:** An app may be able to cause unexpected system termination or read kernel memory.   Affects Kernel | | | | | | | |
|  |  |  |  | x | x | x | x |
| **CVE-2026-65354:** A malicious app may be able to break out of its sandbox.   Affects iWork | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-65358:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x |  | x |  | x | x | x | x |
| **CVE-2026-65359:** A local user may be able to cause unexpected system termination or read kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-65360:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  | x |  |  |  |  |  |  |
| **CVE-2026-65361:** An app may be able to access sensitive user data.   Affects SoftwareUpdate | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65362:** An app may be able to gain root privileges.   Affects Disk Images | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65364:** A remote attacker may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65365:** Connecting to a malicious SMB share may disclose kernel memory.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65369:** A malicious application may bypass Gatekeeper checks.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65371:** An app may be able to disclose kernel memory.   Affects Kernel | | | | | | | |
|  |  |  |  | x |  |  |  |
| **CVE-2026-65374:** Connecting to a malicious WebDAV server may result in code execution.   Affects WebDAV | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65375:** An app may be able to cause unexpected system termination.   Affects WebDAV | | | | | | | |
|  |  | x |  | x |  |  |  |
| **CVE-2026-65376:** An app may be able to cause unexpected system termination.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65377:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-65378:** An app may be able to access sensitive user data.   Affects Spotlight | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65380:** An app may be able to access protected user data.   Affects Sandbox | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-65381:** A malicious app may be able to break out of its sandbox.   Affects AppleMobileFileIntegrity | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65382:** An app may be able to access sensitive user data.   Affects LaunchServices | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65383:** An app may bypass Gatekeeper checks.   Affects System Settings | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-65390:** Processing maliciously crafted web content may lead to memory corruption.   Affects WebRTC | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-65391:** Processing maliciously crafted web content may lead to memory corruption.   Affects WebRTC | | | | | | | |
|  |  |  |  |  | x | x | x |
| **CVE-2026-65393:** An app may be able to access user-sensitive data.   Affects Xcode IDE | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-65395:** Processing a maliciously crafted image may result in memory corruption.   Affects ImageIO | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-65398:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects IOMobileFrameBuffer | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-65399:** An archive may be able to bypass Gatekeeper.   Affects copyfile | | | | | | | |
| x | x | x | x | x |  | x | x |
| **CVE-2026-65400:** An attacker on the network may be able to authenticate to Screen Sharing without valid credentials.   Affects Screen Sharing Server | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-65401:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  |  |  | x |  |  |  |  |
| **CVE-2026-65402:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-65403:** An app may be able to access sensitive user data.   Affects Reminders | | | | | | | |
| x | x | x | x | x |  | x | x |
| **CVE-2026-65404:** A malicious application may be able to bypass Privacy preferences.   Affects Accounts | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-65405:** An app may be able to determine kernel memory layout.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-65406:** An app may be able to access sensitive user data.   Affects BackgroundAssets | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-65407:** An app may be able to cause unexpected system termination.   Affects AppleAVD | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-65408:** An app may be able to cause unexpected system termination.   Affects Apple Neural Engine | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-65409:** An app may be able to cause a denial of service.   Affects Foundation | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-65410:** An app may be able to cause unexpected system termination.   Affects AVEVideoEncoder | | | | | | | |
| x | x | x | x |  | x | x | x |
| **CVE-2026-65411:** An app may be able to modify protected parts of the file system.   Affects MobileBackup | | | | | | | |
| x | x |  |  |  |  |  | x |
| **CVE-2026-65412:** Processing web content may lead to a denial-of-service.   Affects CoreText | | | | | | | |
| x | x | x | x | x |  | x | x |
| **CVE-2026-65413:** An app may be able to cause a denial of service.   Affects SceneKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-65415:** A local user may be able to cause unexpected system termination or read kernel memory.   Affects Kernel | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84487:** Processing a maliciously crafted file may result in disclosure of process memory.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84489:** An app may be able to cause a denial of service.   Affects CoreUI | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-84491:** An app may be able to access sensitive user data.   Affects Photos Storage | | | | | | | |
| x | x | x |  |  | x | x | x |
| **CVE-2026-84492:** An app may be able to cause unexpected system termination.   Affects Graphics | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84497:** Opening a maliciously crafted file may lead to unexpected process termination.   Affects Model I/O | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-84505:** An app may be able to gain root privileges.   Affects Directory Utility | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84506:** An app may be able to execute arbitrary code with kernel privileges.   Affects udf | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84507:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84509:** Connecting to a malicious SMB server may lead to unexpected system termination.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84510:** Mounting a maliciously crafted volume may lead to unexpected system termination.   Affects exFAT | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-84511:** Processing a maliciously crafted asset catalog may lead to unexpected process termination.   Affects CoreUI | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-84512:** Mounting a maliciously crafted disk image may cause unexpected system termination or corrupt kernel memory.   Affects Disk Images | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84513:** A malicious application may be able to determine a user's current location.   Affects Symptom Framework | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84514:** An app may be able to modify protected parts of the file system.   Affects Kext Management | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84515:** Connecting to a malicious SMB server may lead to kernel memory corruption.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84516:** Processing a maliciously crafted file may result in unexpected app termination or disclosure of process memory.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84517:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84518:** A malicious website may be able to determine what apps a user has installed.   Affects Safari | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-84519:** Mounting a disk image with maliciously crafted files may lead to unexpected system termination.   Affects AppleDouble | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-84520:** A local attacker may be able to cause unexpected system termination or corrupt kernel memory.   Affects AppleFDEKeyStore | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84521:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  | x |  | x | x |  |  |  |
| **CVE-2026-84522:** An app may be able to access sensitive user data.   Affects Archive Utility | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84523:** An app may be able to cause unexpected system termination or write kernel memory.   Affects APFS | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84524:** Processing a maliciously crafted font file may lead to unexpected app termination.   Affects FontParser | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84525:** An app may be able to access user-sensitive data.   Affects ATS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84526:** Processing a maliciously crafted 3D scene may lead to unexpected process termination.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84527:** An app may be able to access sensitive user data.   Affects TCC | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-84530:** An app may be able to disclose kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x |  | x | x | x |
| **CVE-2026-84531:** Processing maliciously crafted NTLM input may lead to unexpected app termination.   Affects Security | | | | | | | |
| x |  | x |  |  |  |  |  |
| **CVE-2026-84532:** Opening a maliciously crafted file may cause unexpected process termination or disclose process memory.   Affects RealityKit | | | | | | | |
| x | x | x | x | x | x |  | x |
| **CVE-2026-84533:** An attacker in a privileged network position may be able to modify network traffic.   Affects Heimdal | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-84534:** Extracting a maliciously crafted archive may allow an attacker to write arbitrary files.   Affects file\_cmds | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-84535:** An app may be able to break out of its sandbox.   Affects Automator | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84536:** Connecting to a malicious SMB server may lead to unexpected system termination.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84537:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84538:** A remote attacker may be able to cause a denial-of-service.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84540:** An app may be able to access sensitive user data.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84541:** An application may be able to access restricted files.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84543:** Connecting to a malicious SMB server may cause unexpected system termination or corrupt kernel memory.   Affects SMB | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84544:** Connecting to a malicious NFS server may cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84548:** Processing a maliciously crafted document may lead to an out-of-bounds read.   Affects Quick Look | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84549:** Connecting to a malicious NFS server may cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84550:** An app may be able to cause unexpected system termination.   Affects Disk Images | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84551:** An app may be able to bypass network restrictions.   Affects Sandbox | | | | | | | |
| x |  | x |  |  |  | x | x |
| **CVE-2026-84552:** An app may be able to cause unexpected system termination.   Affects Disk Images | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-84553:** A remote attacker may be able to cause a denial-of-service.   Affects smbx | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84554:** An attacker in a privileged network position may be able to cause a denial-of-service.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84555:** An app may be able to access sensitive user data.   Affects Sandbox | | | | | | | |
|  |  | x |  | x |  |  |  |
| **CVE-2026-84556:** An app may be able to access sensitive user data.   Affects Keychain Access | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84558:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84559:** A malicious application may be able to access restricted files.   Affects CoreServices | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84560:** An app may gain unauthorized access to Bluetooth.   Affects Bluetooth | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84561:** An app may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84563:** An app may be able to cause unexpected system termination.   Affects CUPS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84564:** Processing a maliciously crafted image may result in disclosure of process memory.   Affects ImageIO | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84565:** Processing a maliciously crafted disk image may lead to unexpected app termination.   Affects Disk Images | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84566:** A local attacker may be able to cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-84567:** An app may be able to cause unexpected system termination.   Affects cd9660 | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84568:** An attacker with control of a network directory server may be able to execute arbitrary code with root privileges.   Affects autofs | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84569:** An app may be able to access sensitive user data.   Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84570:** An app may be able to bypass Gatekeeper checks.   Affects autofs | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84571:** Processing a maliciously crafted image may lead to unexpected app termination.   Affects CoreUI | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84572:** An app may be able to cause unexpected system termination or read kernel memory.   Affects udf | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84573:** An app may be able to access sensitive user data.   Affects Mail | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84574:** An app may be able to bypass Privacy preferences.   Affects CoreServices | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84575:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects CoreUI | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-84576:** An app may be able to access sensitive user data.   Affects QuartzCore | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84577:** An app may be able to bypass sandbox restrictions.   Affects libxpc | | | | | | | |
|  |  | x | x |  |  |  |  |
| **CVE-2026-84578:** An app may be able to break out of its sandbox.   Affects quarantine | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84580:** An app may be able to break out of its sandbox.   Affects quarantine | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84581:** Mounting a maliciously crafted disk image may cause unexpected system termination or corrupt kernel memory.   Affects HFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84583:** A local app may be able to read a persistent account identifier.   Affects AuthKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84584:** An app may be able to break out of its sandbox.   Affects Archive Utility | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84585:** An app may be able to access local network devices without user consent.   Affects NetworkExtension | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84586:** A malicious application may be able to leak sensitive user information.   Affects Apple Account | | | | | | | |
|  |  | x |  |  |  | x |  |
| **CVE-2026-84587:** An app may be able to access protected user data.   Affects AppKit | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84588:** Mounting a maliciously crafted disk image may cause unexpected system termination or corrupt kernel memory.   Affects Kernel | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84589:** An app may be able to modify Privacy preferences.   Affects TCC | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84593:** An app may be able to cause unexpected system termination.   Affects AppleKeyStore | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-84596:** Processing a maliciously crafted font may result in the disclosure of process memory.   Affects CoreText | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84597:** Processing a maliciously crafted font may result in the disclosure of process memory.   Affects FontParser | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84598:** An attacker with physical access to a trust-paired device may be able to read and write arbitrary files.   Affects MobileBackup | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-84600:** A malicious shortcut may be able to send messages without user confirmation.   Affects Shortcuts | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84601:** An app may be able to bypass Apple Intelligence security prompts.   Affects Apple Intelligence | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84602:** An app may be able to cause unexpected system termination.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84603:** An app may be able to access sensitive user data.   Affects Sandbox Profiles | | | | | | | |
| x |  |  |  |  |  | x | x |
| **CVE-2026-84606:** An app may be able to identify a user across reinstalls.   Affects iCloud | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-84607:** A sandboxed app may be able to execute arbitrary code with kernel privileges.   Affects AVEVideoEncoder | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84609:** An app may be able to modify protected system files.   Affects Software Update | | | | | | | |
| x |  | x | x | x | x | x | x |
| **CVE-2026-84611:** Processing a maliciously crafted 3D model may lead to memory corruption.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84612:** An app may be able to read persistent device identifiers.   Affects DeviceCheck | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84615:** An app may be able to access sensitive user data.   Affects Music | | | | | | | |
| x | x |  |  |  | x |  | x |
| **CVE-2026-84616:** An app may be able to cause unexpected system termination.   Affects AVEVideoEncoder | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84617:** An app may be able to access sensitive user data.   Affects XPC | | | | | | | |
| x | x | x | x | x | x |  |  |
| **CVE-2026-84618:** An app may be able to access sensitive user data.   Affects Game Center | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84619:** An app may be able to cause unexpected system termination or write kernel memory.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-84620:** Processing a maliciously crafted 3D model may lead to memory corruption.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84621:** An app may be able to access sensitive user data.   Affects Spotlight | | | | | | | |
| x | x | x | x | x |  |  |  |
| **CVE-2026-84622:** An app with root privileges may be able to read uninitialized kernel memory.   Affects Kernel | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84623:** An app may be able to fingerprint the device.   Affects Power Management | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-84624:** A sandboxed app may be able to access restricted files.   Affects CoreML | | | | | | | |
| x | x | x | x | x |  |  | x |
| **CVE-2026-84625:** An app may be able to fingerprint the user.   Affects Sandbox Profiles | | | | | | | |
| x |  | x |  |  |  | x | x |
| **CVE-2026-84626:** An app may be able to identify what other apps a user has installed.   Affects NetworkExtension | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84628:** A sandboxed app may be able to access the System Keychain.   Affects MediaRemote | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84629:** An app may be able to fingerprint the user.   Affects Photos Storage | | | | | | | |
| x |  |  |  |  | x | x | x |
| **CVE-2026-84631:** An app may be able to gain root privileges.   Affects Bluetooth | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-84632:** Processing a maliciously crafted 3D model may lead to memory corruption.   Affects SceneKit | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-84635:** Processing maliciously crafted web content may lead to an unexpected process termination.   Affects WebKit | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-84636:** An app may be able to access sensitive user data.   Affects Wi-Fi Connectivity | | | | | | | |
| x |  |  |  |  | x | x | x |
| **CVE-2026-86869:** Processing a maliciously crafted image may lead to unexpected app termination.   Affects ImageIO | | | | | | | |
|  | x | x |  |  |  |  |  |
| **CVE-2026-86870:** Processing a maliciously crafted file may lead to unexpected app termination.   Affects libarchive | | | | | | | |
| x | x | x |  |  |  | x | x |
| **CVE-2026-86876:** A sandboxed process may be able to circumvent sandbox restrictions.   Affects CoreMedia | | | | | | | |
| x | x | x | x | x |  | x | x |
| **CVE-2026-86878:** An app may be able to access sensitive user data.   Affects Camera | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-86879:** A remote attacker may be able to cause a denial-of-service.   Affects Baseband | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-86881:** An attacker with a compromised intermediate certificate authority may be able to issue certificates with arbitrary extended key usages.   Affects Security | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-86882:** Processing a maliciously crafted image may lead to unexpected process termination.   Affects Accelerate Framework | | | | | | | |
| x | x | x | x | x | x | x | x |
| **CVE-2026-86883:** An app may be able to access sensitive user data.   Affects Managed Configuration | | | | | | | |
| x |  |  |  |  |  |  | x |
| **CVE-2026-86884:** An app may be able to access sensitive user data.   Affects Siri | | | | | | | |
| x |  | x |  |  | x | x |  |
| **CVE-2026-86885:** An attacker in radio range may be able to cause unexpected system termination.   Affects Baseband | | | | | | | |
| x |  |  |  |  |  |  |  |
| **CVE-2026-86886:** An app may be able to modify protected system files.   Affects TCC | | | | | | | |
| x | x |  |  |  |  | x |  |
| **CVE-2026-86887:** An app may be able to bypass certain Privacy preferences.   Affects Time Zone | | | | | | | |
| x | x |  |  |  |  |  | x |
| **CVE-2026-86888:** A local app may be able to read a persistent account identifier.   Affects App Store | | | | | | | |
| x |  | x | x |  | x | x | x |
| **CVE-2026-86889:** An attacker in a privileged network position may be able to intercept network traffic.   Affects Security | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-86890:** An attacker with physical access to a locked device may be able to view sensitive user information.   Affects Siri Suggestions | | | | | | | |
| x | x |  |  |  |  |  |  |
| **CVE-2026-86891:** An app may be able to access Bluetooth device information.   Affects Core Bluetooth | | | | | | | |
|  |  | x | x | x |  | x |  |
| **CVE-2026-86892:** An app may be able to cause a denial-of-service.   Affects SpringBoard | | | | | | | |
| x | x |  |  |  |  |  | x |
| **CVE-2026-86893:** An app may be able to read device name.   Affects CloudKit | | | | | | | |
| x |  |  |  |  | x | x | x |
| **CVE-2026-86894:** An app may be able to break out of its sandbox.   Affects libxpc | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86895:** A local app may be able to read a persistent account identifier.   Affects CloudKit | | | | | | | |
| x |  |  |  |  | x | x | x |
| **CVE-2026-86897:** An app may be able to access sensitive user data.   Affects Safe Browsing | | | | | | | |
| x | x | x |  |  |  |  | x |
| **CVE-2026-86898:** Opening a maliciously crafted webarchive file may lead to universal cross-site scripting.   Affects WebKit | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-86900:** Mounting a maliciously crafted exFAT volume may cause unexpected system termination or kernel memory disclosure.   Affects exFAT | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86901:** Mounting a maliciously crafted exFAT volume may cause unexpected system termination or kernel memory disclosure.   Affects exFAT | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86902:** An app may be able to access sensitive user data.   Affects NSDocument | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86903:** An app may be able to disclose kernel memory.   Affects Kernel | | | | | | | |
| x |  | x |  |  | x | x | x |
| **CVE-2026-86904:** An app may be able to track users across apps and websites without permission.   Affects Watch App | | | | | | | |
| x | x |  |  |  |  | x |  |
| **CVE-2026-86905:** An app may be able to delete credentials stored in Keychain.   Affects Authentication Services | | | | | | | |
| x |  | x |  |  |  |  | x |
| **CVE-2026-86909:** An app may be able to bypass Gatekeeper checks.   Affects System Settings | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86910:** An application may be able to access restricted files.   Affects APFS | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-86911:** A malicious app may be able to bypass clickjacking protections for secure prompts.   Affects Foundation | | | | | | | |
|  |  | x |  |  |  |  |  |
| **CVE-2026-86917:** An app may be able to gain root privileges.   Affects Kernel | | | | | | | |
|  |  | x | x | x |  |  |  |
| **CVE-2026-86924:** Connecting a malicious accessory may cause unexpected system termination.   Affects MobileAccessoryUpdater | | | | | | | |
| x | x | x | x |  |  |  |  |

--

Johannes B. Ullrich, Ph.D. , Dean of Research,
[SANS.edu](https://sans.edu)

[Twitter](https://jbu.me/164)
|

Keywords:
[apple](/tag.html?tag=apple)
[watchos macos ipad ios ipados visionos patches](/tag.html?tag=watchos macos ipad ios ipados visionos patches)

[0 comment(s)](/diary/Apple+Updates+Everything/33336/#comments)

Click
[HERE](https://www.sans.org/profiles/dr-johannes-ullrich)
to learn more about classes Johannes is teaching for SANS

* [previous](/diary/33332)
* [next](/diary/33340)

### Comments

[Login here to join the discussion.](/login)



[Top of page](#)

×

![modal content]()

[Diary Archives](/diaryarchive.html)