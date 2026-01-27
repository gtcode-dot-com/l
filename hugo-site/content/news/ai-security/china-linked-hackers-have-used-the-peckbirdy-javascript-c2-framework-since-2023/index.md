---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-27T12:15:13.657138+00:00'
exported_at: '2026-01-27T12:15:15.951598+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/china-linked-hackers-have-used.html
structured_data:
  about: []
  author: ''
  description: Experts details PeckBirdy, a JavaScript C2 framework used since 2023
    by China-aligned attackers to spread malware via fake updates & web injections.
  headline: China-Linked Hackers Have Used the PeckBirdy JavaScript C2 Framework Since
    2023
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/china-linked-hackers-have-used.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: China-Linked Hackers Have Used the PeckBirdy JavaScript C2 Framework Since
  2023
updated_at: '2026-01-27T12:15:13.657138+00:00'
url_hash: 9ef79f5c83d3f961093156d10b70cf1e11c01607
---

**

Ravie Lakshmanan
**

Jan 27, 2026

Web Security / Malware

Cybersecurity researchers have discovered a
[JScript](https://en.wikipedia.org/wiki/JScript)
-based command-and-control (C2) framework called
**PeckBirdy**
that has been put to use by China-aligned APT actors since 2023 to target multiple environments.

The flexible framework has been put to use against Chinese gambling industries and malicious activities targeting Asian government entities and private organizations, according to Trend Micro.

"PeckBirdy is a script-based framework which, while possessing advanced capabilities, is implemented using JScript, an old script language," researchers Ted Lee and Joseph C Chen
[said](https://www.trendmicro.com/en_us/research/26/a/peckbirdy-script-framework.html)
. "This is to ensure that the framework could be launched across different execution environments via LOLBins (living-off-the-land binaries)."

The cybersecurity company said it identified the PeckBirdy script framework in 2023 after it observed multiple Chinese gambling websites being injected with malicious scripts, which are designed to download and execute the primary payload in order to facilitate the remote delivery and execution of JavaScript.

The end goal of this routine is to serve fake software update web pages for Google Chrome so as to trick users into downloading and running bogus update files, thereby infecting the machines with malware in the process. This activity cluster is being tracked as SHADOW-VOID-044.

SHADOW-VOID-044 is one of the two temporary intrusion sets detected using PeckBirdy. The second campaign, observed first in July 2024 and referred to as SHADOW-EARTH-045, involves targeting Asian government entities and private organizations -- including a Philippine educational institution -- injecting PeckBirdy links into government websites to likely serve scripts for credential harvesting on the website.

"In one case, the injection was on a login page of a government system, while in another incident, we noticed the attacker using MSHTA to execute PeckBirdy as a remote access channel for lateral movement in a private organization," Trend Micro said. "The threat actor behind the attacks also developed a .NET executable to launch PeckBirdy with ScriptControl. These findings demonstrate the versatility of PeckBirdy's design, which enables it to serve multiple purposes."

What makes PeckBirdy notable is its flexibility, allowing it to run with varying capabilities across web browsers, MSHTA, WScript, Classic ASP, Node JS, and .NET (ScriptControl). The framework's server is configured to support multiple APIs that make it possible for clients to obtain landing scripts for different environments via an HTTP(S) query.

The API paths include an "ATTACK ID" value -- a random but predefined string with 32 characters (e.g., o246jgpi6k2wjke000aaimwбe7571uh7) -- that determines the PeckBirdy script to be retrieved from the domain. Once launched, the PeckBirdy determines the current execution context and then proceeds to generate a unique victim ID and persist it for subsequent executions.

The initialization step is followed by the framework attempting to figure out what communication methods are supported in the environment. PeckBirdy uses the WebSocket protocol to communicate with the server by default. However, it can also employ Adobe Flash ActiveX objects or Comet as a fallback mechanism.

After a connection has been initiated with the remote server, passing along the ATTACK ID and victim ID values, the server responds with a second-stage script, one of which is capable of stealing website cookies. One of PeckBirdy's servers associated with the SHADOW-VOID-044 campaign has been found to host additional scripts -

* An exploitation script for a Google Chrome flaw in the V8 engine (
  [CVE-2020-16040](https://chromereleases.googleblog.com/2020/12/stable-channel-update-for-desktop.html)
  , CVSS score: 6.5) that was patched in December 2020
* Scripts for social engineering pop-ups that are designed to trick victims into downloading and executing malicious files
* Scripts for delivering backdoors that are executed via Electron JS
* Scripts to establish reverse shells via TCP sockets

Further infrastructure analysis has led to the identification of two backdoors dubbed HOLODONUT and MKDOOR -

* HOLODONUT, a .NET-based modular backdoor that's launched using a simple downloader named NEXLOAD and is capable of loading, running, or removing different plugins received from the server
* MKDOOR, a modular backdoor that's capable of loading, running, or uninstalling different modules received from the server

It's suspected that SHADOW-VOID-044 and SHADOW-EARTH-045 could be linked to different China-aligned nation-state actors. This assessment is based on the following clues -

* The presence of
  [GRAYRABBIT](https://www.virusbulletin.com/conference/vb2024/abstracts/down-grayrabbit-hole-exposing-unc3569-and-its-mastermind/)
  , a backdoor previously deployed by
  [UNC3569](https://thehackernews.com/2024/04/researchers-identify-multiple-china.html)
  alongside DRAFTGRAPH and
  [Crosswalk](https://thehackernews.com/2024/06/chinese-cyber-espionage-group-exploits.html)
  following the exploitation of N-day security flaws, on a server operated by SHADOW-VOID-044
* HOLODONUT is said to share links to another backdoor,
  [WizardNet](https://thehackernews.com/2025/04/chinese-hackers-abuse-ipv6-slaac-for.html)
  , which is attributed to TheWizards
* A Cobalt Strike artifact hosted on the SHADOW-VOID-044 server that's signed using a certificate that was also used in a
  [2021 BIOPASS RAT campaign](https://thehackernews.com/2021/07/hackers-spread-biopass-malware-via.html)
  aimed at online gambling companies in China via a watering hole attack
* Similarities between BIOPASS RAT and MKDOOR, both of which open an HTTP server on a high-numbered port on the local host to listen (The BIOPASS RAT is attributed to a threat actor known as Earth Lusca, aka Aquatic Panda or RedHotel)
* SHADOW-EARTH-045's use of 47.238.184[.]9 – an IP address previously linked to
  [Earth Baxia](https://thehackernews.com/2024/09/chinese-hackers-exploit-geoserver-flaw.html)
  and
  [APT41](https://thehackernews.com/2025/07/china-linked-hackers-launch-targeted.html)
  – to downloaded files

"These campaigns make use of a dynamic JavaScript framework, PickBirdy, to abuse living-off-the-land binaries and deliver modular backdoors such as MKDOOR and HOLODONUT," Trend Micro concluded. "Detecting malicious JavaScript frameworks remains a significant challenge due to their use of dynamically generated, runtime-injected code and the absence of persistent file artifacts, enabling them to evade traditional endpoint security controls."