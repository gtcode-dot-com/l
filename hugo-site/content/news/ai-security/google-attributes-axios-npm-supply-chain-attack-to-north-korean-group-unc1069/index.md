---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T06:15:16.585973+00:00'
exported_at: '2026-04-02T06:15:19.136555+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html
structured_data:
  about: []
  author: ''
  description: Google links Axios npm supply chain attack to UNC1069 after trojanized
    versions 1.14.1 and 0.30.4 spread WAVESHAPER.V2, impacting multiple OS.
  headline: Google Attributes Axios npm Supply Chain Attack to North Korean Group
    UNC1069
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Attributes Axios npm Supply Chain Attack to North Korean Group UNC1069
updated_at: '2026-04-02T06:15:16.585973+00:00'
url_hash: d170707b4f614a38d20b6910589bb456dd2f7a78
---

Google has
[formally attributed](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)
the
[supply chain compromise](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
of the popular Axios npm package to a financially motivated North Korean threat activity cluster tracked as
**UNC1069**
.

"We have attributed the attack to a suspected North Korean threat actor we track as UNC1069," John Hultquist, chief analyst at Google Threat Intelligence Group (GTIG), told The Hacker News in a statement.

"North Korean hackers have deep experience with supply chain attacks, which they've historically used to steal cryptocurrency. The full breadth of this incident is still unclear, but given the popularity of the compromised package, we expect it will have far reaching impacts."

The development comes after
[threat actors seized control](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
of the package maintainer's npm account to push two trojanized versions 1.14.1 and 0.30.4 that introduced a malicious dependency named "plain-crypto-js" that's used to deliver a cross-platform backdoor capable of infecting Windows, macOS, and Linux systems.

Rather than introducing any code changes to Axios, the attack leverages a postinstall hook within the "package.json" file of the malicious dependency to achieve stealthy execution. Once the compromised Axios package is installed, npm automatically triggers the execution of malicious code in the background.

Specifically, the "plain-crypto-js" package functions as a "payload delivery vehicle" for an obfuscated JavaScript dropper dubbed SILKBELL ("setup.js"), which fetches the appropriate next-stage from a remote server based on the victim's operating system.

As previously detailed by The Hacker News, the Windows execution branch delivers PowerShell malware, a C++ Mach-O binary for macOS, and a Python backdoor for Linux systems. The dropper also performs a cleanup to remove itself and replace the "plain-crypto-js" package's "package.json" file with a clean version that does not have the postinstall hook.

|  |
| --- |
|  |
| Image Source: Elastic Security Labs |

The backdoor, codenamed WAVESHAPER.V2, is assessed to be an updated version of
[WAVESHAPER](https://thehackernews.com/2026/02/north-korea-linked-unc1069-uses-ai.html)
, a C++ backdoor deployed by UNC1069 in attacks aimed at the cryptocurrency sector. The threat actor has been operational since 2018. The supply chain attack's links to UNC1069 were first flagged by Elastic Security Labs, citing functionality overlaps.

The three WAVESHAPER.V2 variants support four different commands, while beaconing to the command-and-control (C2) server at 60-second intervals -

* **kill**
  , to terminate the malware's execution process.
* **rundir**
  , to enumerate directory listings, along with file paths, sizes, and creation/modification timestamps.
* **runscript**
  , to run AppleScript, PowerShell, or shell commands based on the operating system.
* **peinject**
  , to decode and execute arbitrary binaries.

"WAVESHAPER.V2 is a direct evolution of WAVESHAPER, a macOS and Linux backdoor previously attributed to UNC1069," Mandiant and GTIG said. "While the original WAVESHAPER uses a lightweight, raw binary C2 protocol and employs code packing, WAVESHAPER.V2 communicates using JSON, collects additional system information, and supports more backdoor commands."

"Despite these upgrades, both versions accept their C2 URL dynamically via command-line arguments, share identical C2 polling behaviors and an uncommon User-Agent string, and deploy secondary payloads to identical temporary directories (e.g., /Library/Caches/com.apple.act.mond)."

The links to North Korea are also bolstered by the fact that the macOS binary
[references](https://www.elastic.co/security-labs/axios-supply-chain-compromise-detections)
developer build paths like "Jain\_DEV/client\_mac/macWebT/macWebT," where "macWebT" links directly to
[BlueNoroff's "webT" module](https://www.sentinelone.com/blog/bluenoroff-how-dprks-macos-rustbucket-seeks-to-evade-analysis-and-detection/)
from
[RustBucket](https://thehackernews.com/2023/04/lazarus-subgroup-targeting-apple.html)
and
[Hidden Risk](https://thehackernews.com/2024/11/north-korean-hackers-target-crypto.html)
malware campaigns in 2023, according to researcher
[Giuseppe Massaro](https://gist.github.com/N3mes1s/0c0fc7a0c23cdb5e1c8f66b208053ed6)
.

To
[mitigate the threat](https://www.upwind.io/feed/from-nodes-to-snakes-npm-supply-chain)
, users are advised to audit dependency trees for compromised versions (and downgrade to a safe version, if found), pin Axios to a known safe version in the "package-lock.json" file to prevent accidental upgrades, check for presence of "plain-crypto-js" in "node\_modules," terminate malicious processes, block C2 domain ("sfrclak[.]com," IP address: 142.11.206[.]73), isolate affected systems, and rotate all credentials.

"The Axios attack should be understood as a template, not a one-time event. The level of operational sophistication documented here, including compromised maintainer credentials, pre-staged payloads built for three operating systems, both release branches hit in under 40 minutes, and built-in forensic self-destruction, reflects a threat actor that planned this as a scalable operation," ReversingLabs Chief Software Architect Tomislav Peričin told The Hacker News.

"If this campaign is now appearing in PyPI and NuGet, that's consistent with what the attack mechanics already suggest: the goal was maximum developer reach. Organizations need to audit not just their npm dependencies, but every package manager feeding their build pipelines, and treat any secrets exposed in affected environments as compromised, regardless of which registry they touched."