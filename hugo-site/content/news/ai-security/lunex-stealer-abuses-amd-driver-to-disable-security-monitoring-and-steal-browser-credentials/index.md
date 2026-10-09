---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-05T04:00:22.175298+00:00'
exported_at: '2026-10-05T04:00:23.345915+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html
structured_data:
  about: []
  author: ''
  description: Lunex uses BYOVD to disable kernel security callbacks before stealing
    browser credentials and cryptocurrency wallets.
  headline: Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal
    Browser Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/lunex-stealer-abuses-amd-driver-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Lunex Stealer Abuses AMD Driver to Disable Security Monitoring and Steal Browser
  Credentials
updated_at: '2026-10-05T04:00:22.175298+00:00'
url_hash: d0389279f56227f3aa2cc930c8000964f6bfcf8c
---

The
[Psychedelic Stealer](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html)
malware distributed via compromised Ukrainian websites using ClickFix-style Cloudflare verification checks is part of a wider malware-as-a-service (MaaS) platform called
**Lunex**
.

The new findings come from Ontinue, which described the activity as a four-stage attack chain aimed at targeting Ukrainian-speaking users.

"The attack chain begins with a fake CAPTCHA page and culminates in the deployment of a fully-featured C2 agent," Ontinue threat researcher Rhys Downing
[said](https://www.ontinue.com/resource/lunex-unmasked-a-new-information-stealer-deployed-through-byovd/)
in a technical report. "The stealer extracts credentials and data from seven Chromium-based browsers, exfiltrates cryptocurrency wallets, and establishes persistent remote filesystem access through a PowerShell-based Native Messaging Host installed within the victim's browser."

The infection makes use of bogus MSI installers delivered via ClickFix to trigger a series of actions, including delivering a loader dubbed LunexLoader that's designed to bypass User Account Control (UAC) on Windows using the CMSTPLUA COM object, leverage the bring your own vulnerable driver (
[BYOVD](https://thehackernews.com/2026/07/silverfox-targets-japanese-manufacturer.html)
) attack for defense evasion, and finally download the stealer payload.

The use of the BYOVD technique is significant, not least because it's rarely employed as a precursor to a final-stage payload like an information stealer. Lunex takes advantage of a vulnerable kernel-mode driver for AMD Radeon Software ("PDFWKRNL.sys"), which is
[susceptible](https://thehackernews.com/2023/11/researchers-find-34-windows-drivers.html)
to
[CVE-2023-20598](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-6009.html)
, to
[escalate privileges](https://github.com/unkvolism/pdfwkrnl)
and blind security-related processes while keeping them running.

Psychedelic Stealer was
[first documented](https://thehackernews.com/2026/09/hacked-ukrainian-sites-serve-fake.html)
earlier this week by Arctic Wolf Labs, detailing the threat actor's modus operandi of compromising legitimate websites belonging to a hair-treatment clinic, a scale-model manufacturer, a specialist bookseller, a psychological facility, a tool retailer, and an automotive retailer to inject an iframe element designed to serve the ClickFix lure.

"Our analysis of the attack chain found that, before the stealer is delivered, the malware is designed to use a legitimate but vulnerable driver to switch off security tools on the victim's machine. With those protections disabled, the information stealer is then deployed to take browser passwords, session cookies, and cryptocurrency wallet data," Downing told The Hacker News.

The earliest reference to Lunex in cybersecurity literature dates back to June 2026, when BlueTeamCoolTeam's Luke Wilkinson
[identified](https://blueteam.cool/posts/lunex-c2-osint/)
six active Lunex Stealer's command-and-control (C2) panels across the U.S., Finland, Germany, the Netherlands, and Ukraine.

|  |
| --- |
|  |
| LunexStealer (aka Psychedelic Stealer) C2 Panel | Source: BlueTeamCoolTeam |

It's worth noting that both Psychedelic Stealer and LunexStealer refer to the same component of the MaaS platform. "'Psychedelic' is the name of the malware file that runs on victims' devices, while Lunex is the underlying platform being sold to multiple criminal groups, which is the reason for the name 'Lunex' and 'LunexStealer,'" Downing explained.

Upon execution, LunexStealer communicates with the Lunex panel at 193.178.159[.]128 over HTTP to facilitate comprehensive information theft -

* Steal credentials from Google Chrome, Microsoft Edge, Brave, Yandex Browser, Opera, Opera GX, and Vivaldi.
* Enumerate five desktop cryptocurrency wallets, Bitcoin Core, Litecoin, Exodus, Atomic Wallet, and Electrum, and four browser extension wallets, MetaMask, MetaMask Legacy, OKX Wallet, and SafePal Wallet, and exfiltrate relevant data from them.
* Establish persistence using a Registry Run key, a hidden scheduled task named "psychedelicloveUtils," and register a
  [Chrome native-messaging bridge or host](https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging)
  (NMH) that allows the stealer to perform additional actions.

"The host is backed by a 13,200-byte PowerShell script embedded in the .rdata section that implements the Chrome Native Messaging protocol over standard input and output," Downing said. "The NMH operates within Chrome’s process context. It survives stealer binary deletion, system reboots, and browser restarts."

The PowerShell script supports six file system actions -

* **list\_drives**
  , to enumerate all drive letters C through Z
* **list\_dir**
  , to list directory contents with file sizes
* **read\_file**
  , to read arbitrary files in 512 KB chunks and those up to 524 MB
* **write**
  , to write arbitrary data to any file path
* **download**
  , to download files from the system
* **run**
  , to execute arbitrary programs

What's more, LunexStealer injects a malicious Chrome extension by manipulating Chrome Secure Preferences and declares extensive permissions for cookies, history, bookmarks, tabs, storage, proxy, scripting, declarativeNetRequest, and all HTTP and HTTPS URLs. This grants the extension complete visibility and control over a victim's browser activity.

Analysis of the Lunex panel points to a Russian-speaking developer or development team, with 28 unique panels identified across 13 countries, marking a major expansion from June 2026. These panels are hosted in Russia, the U.S., the U.K., the Netherlands, France, Germany, Turkey, and Bangladesh.

"That growth in just a few months shows the platform is actively expanding and being used by either one threat actor or sold for other actors, not just a single operator," Downing said.

One of the panels hosted in Turkey has been found to resolve to five phishing domains -

* account-sams-club[.]com
* teamwork-recover-password[.]com
* namshi-uae[.]com
* whatsappbusineses[.]com
* ibraq-perfumes[.]com

This indicates that the MaaS platform's feature set extends beyond credential theft to also enable brand impersonation and phishing.

"The BYOVD delivery chain, using PDB-guided kernel callback zeroing rather than process termination, represents a quieter approach to EDR neutralisation that leaves security products running but blind," Ontinue said.

"Validated testing demonstrated that neither HVCI nor the current Microsoft Vulnerable Driver Blocklist prevents the specific PDFWKRNL.sys variant used in this chain from loading, a gap that persists despite the driver hash being catalogued in the LOLDrivers project since March 2026."