---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-17T06:18:59.057572+00:00'
exported_at: '2026-09-17T06:19:02.076828+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html
structured_data:
  about: []
  author: ''
  description: WordlistLoader delivers Amatera via ClearFake ClickFix attacks, while
    SynkLoader uses Teams phishing to steal Windows login credentials.
  headline: WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows
    Passwords
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/wordlistloader-delivers-amatera-via.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: WordlistLoader Delivers Amatera via ClickFix, SynkLoader Phishes Windows Passwords
updated_at: '2026-09-17T06:18:59.057572+00:00'
url_hash: ed974b7e9a642d07e0db940f65bee0d6dd544bbf
---

Cybersecurity researchers have flagged two new malware families called
**WordlistLoader**
and
**SynkLoader**
that's used to deliver next-stage payloads and likely sell access to ransomware groups.

According to findings from Gen Digital, WordlistLoader is being used to deliver Amatera Stealer (aka ACR Stealer or AcridRain Stealer) via
[ClearFake](https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html)
campaigns, which employ the ClickFix (aka FakeCaptcha) technique to dupe victims into running malicious commands under the pretext of completing CAPTCHA verification checks.

"Once the visitor clicks on the 'I'm not a robot' checkbox, they're walked through the well-known ClickFix flow, where a malicious command is copied into their clipboard and the victim is instructed to paste it into the Windows Run dialog and execute it, leading to the download of WordlistLoader that ultimately results in the execution of Amatera," security researcher Vojtěch Krejsa
[said](https://www.gendigital.com/blog/insights/research/wordlistloader-delivering-amatera-via-clearfake-campaigns)
.

The ClickFix prompts are displayed on real websites that have been compromised with malicious JavaScript that's injected in the form of a Base64-encoded blob. The blob, for its part, fetches another JavaScript from a smart contract stored on the blockchain, an approach known as EtherHiding, and dynamically executes the retrieved code. Some of the compromised websites serving ClickFix prompts are below -

* abogadosrosarinos[.]com
* aptisweb[.]com
* avene-hebergement[.]com
* https-xhamster[.]com
* www.caesarjaco.co[.]id
* skybap[.]shop

In recent months, ClearFake campaigns have been revamped to use "cdn.jsdelivr[.]net" to host the threat actor's malicious JavaScript, highlighting the abuse of a legitimate Content Delivery Network (CDN) to stage rogue payloads.

"Although the CDN is meant for hosting JavaScript, the threat actors are actually using it to host their malicious PowerShell script," Expel
[noted](https://expel.com/blog/clearfake-new-lotl-techniques/)
earlier this January. "While jsDelivr appears to be taking down the actor's malicious repositories fairly quickly, the first stage's use of EtherHiding allows them to easily swap out burned URLs for fresh working ones."

The ClickFix command uses "conhost" to launch a hidden "cmd.exe" process, then map a remote WebDAV share using pushd, and finally launch the loader via "rundll32.exe." It's worth noting this WebDAV-based approach
[overlaps](https://www.microsoft.com/en-us/security/blog/2026/07/16/acr-stealer-two-observed-intrusion-chains-amid-increased-threat-activity/)
with a similar campaign recently highlighted by Microsoft.

In this campaign, a ClickFix prompt instructs the target to run a command that launches "cmd.exe," which subsequently invokes "rundll32.exe" to load a DLL from a remote WebDAV share accessed over HTTPS. Three different versions of the command have been recorded -

* Direct rundll32 invocation
* pushd-Mounted WebDAV Share followed by rundll32.exe invocation
* Headless and obfuscated pushd execution followed by rundll32.exe invocation (which matches the WordlistLoader infection chain)

"In the more advanced variant, threat actors further enhance stealth by launching commands through conhost.exe –headless, suppressing visible console windows, and employing environment variable obfuscation with delayed variable expansion to conceal critical execution components such as pushd, rundll32, and the remote host name," Microsoft said.

"Combined with minimized or headless execution, these techniques reduce user visibility, complicate static analysis and detection, and enable the infection chain to execute with minimal indication to the victim."

The primary difference is that the Python-based loaders observed by Microsoft between late April 2026 and mid-June 2026 in connection with the ACR Stealer intrusion chain have been replaced by WordlistLoader. ACR Stealer has also been propagated via ClickFix prompts that trigger a command spawning MSHTA to retrieve and execute remote HTA content from a threat actor-controlled domain.

This leads to the execution of a VBScript loader that decodes and runs PowerShell designed to fetch a JPEG image from an image-hosting service and extract it from the stealer payload in memory to minimize on-disk artifacts and complicate detection and analysis.

"The primary purpose of WordlistLoader, an intermediate stage in the Amatera infection chain, is to reconstruct a shellcode that serves as the entry point for subsequent stages," Gen Digital said. At the same time, it employs a hardware-breakpoint-based method to bypass Event Tracing for Windows (ETW) and avoid leaving traces of malicious activity.

WordlistLoader gets its name from the fact that the shellcode is stored in encoded form as a sequence of plain English words, with each word representing one byte. Gen said it also identified a variant that replaces the wordlist with an array of 16-byte UUID-encoded chunks.

The shellcode ultimately makes use of a reflective loader responsible for unpacking and loading Amatera 4.3.3-alpha1. The same reflective loader was
[observed](https://www.esentire.com/blog/amatera-stealer-4-0-2-beta-whats-new-in-this-variant)
in late April 2026 in connection with another ClickFix campaign delivering the stealer malware.

The latest version of the stealer comes with updated static obfuscation, hardened syscall invocation through the
[WoW64 transition](https://cloud.google.com/blog/topics/threat-intelligence/wow64-subsystem-internals-and-hooking-techniques)
, dynamically generated x64 indirect-syscall trampolines invoked through
[Heaven's Gate](https://www.huntress.com/cybersecurity-101/topic/what-is-heavens-gate)
, and a redesigned application-bound encryption (
[ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
) bypass that appears to be directly inspired by
[Remus Stealer](https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html#lumma-successor-adopts-evasive-tactics)
.

### SynkLoader Pushed via Microsoft Teams Phishing

The development comes as SynkLoader has been distributed via a
[Microsoft Teams phishing campaign](https://thehackernews.com/2026/08/twinloot-abuses-sharepoint-and-teams-to.html)
to siphon a victim's system login credentials by serving a fake lock screen. The activity was detected by Expel in mid-August 2025.

"Someone using a &lt;username&gt;@&lt;company&gt;.onmicrosoft.com email (Microsoft 365's default email domain for companies) reached out to the target using the name IT Service Desk (&lt;Fake Name&gt;)," Expel security researcher Marcus Hutchins
[said](https://expel.com/blog/synkloader-when-you-throw-in-everything-but-the-kitchen-sink/)
.

"The IT service desk convinced the user to download and install an MSI installer from a Microsoft Azure file storage endpoint (https://filereserve.blob.core.windows[.]net/vgnghuyk/331/331.msi), which gave the file the appearance of having come from Microsoft."

The MSI installer presents itself as a PowerShell Cleaner, which, when run, extracts a ZIP archive and a PowerShell script, the latter of which is automatically run in memory. The script is used to extract the contents of the archive and launch from it a Python-based loader that chooses one of three hard-coded command-and-control (C2) domains and checks in with the server at random, while sleeping for 90 to 120 seconds between requests.

The loader then decrypts and executes the responses from the server. At least seven different modules have been identified -

* **System Profiler**
  , a C# DLL to collect data about the target system.
* **Persistence Module**
  , a native DLL to create a randomly named scheduled task that launches SynkLoader every time the victim logs into the system and daily at 10 a.m.
* **PhishLocker**
  , a DLL to serve a fake Windows lock screen to capture the user's login password
* **TrafficRedirector**
  , a backconnect or reverse proxy that allows the attacker to reach the local network services or route internet traffic through the infected machine
* **Interactive Shell**
  , a remote access trojan (RAT) module to execute PowerShell commands and transmit the result
* **StreamMaster**
  , a Virtual Network Computing (VNC) module to stream the victim's desktop and enable remote mouse and keyboard control
* **Status Checker**
  , a Python script to report back the status of which modules are currently running on the system

It's not clear what the end goals of the operator are, but it's suspected that the toolkit may be part of a ransomware group or an initial access broker.

### Update

In a follow-up
[post shared](https://x.com/ReliaQuestTR/status/2091926469903589785)
on X, ReliaQuest said it observed the SynkLoader PowerShell loader being distributed through social-engineering campaigns involving vishing and Microsoft Teams messages impersonating IT support personnel.

"Despite variations in the initial contact method, the observed delivery chains lead victims to a fraudulent 'PowerShell Cleaner' MSI hosted on legitimate Azure Blob Storage," it said, mirroring findings from Expel. "SynkLoader decrypts its payload in memory and verifies its cryptographic hash before executing it. If the payload has been modified or improperly extracted, the loader fails silently rather than continuing execution."

The loader has also been found to deploy a modular Python backdoor named "ss[.]py" that dynamically fetches its operational capabilities from a C2 server at runtime, as opposed to embedding them directly in the payload. This, in turn, minimizes forensic visibility and allows the operator to expand their functionality at will.

"The campaign combines trusted cloud-hosting infrastructure, IT-support impersonation, in-memory PowerShell execution, and dynamically retrieved Python components to reduce visibility across traditional email, network, and sandbox-based controls," ReliaQuest added.

*(The story was updated after publication on August 26, 2026, to include additional insights from ReliaQuest.)*