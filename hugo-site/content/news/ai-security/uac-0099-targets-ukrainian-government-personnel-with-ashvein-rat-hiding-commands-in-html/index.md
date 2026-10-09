---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-08T16:27:05.224923+00:00'
exported_at: '2026-10-08T16:27:07.809940+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html
structured_data:
  about: []
  author: ''
  description: TrendAI links UAC-0099 to ASHVEIN, a .NET stealer and RAT used in attacks
    targeting Ukrainian government personnel.
  headline: UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding
    Commands in HTML
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/uac-0099-targets-ukrainian-government.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: UAC-0099 Targets Ukrainian Government Personnel With ASHVEIN RAT Hiding Commands
  in HTML
updated_at: '2026-10-08T16:27:05.224923+00:00'
url_hash: 597dc1488663d6c1c77cf7cead5b859c037dc2f5
---

The Russia-aligned threat actor known as
**[UAC-0099](https://thehackernews.com/2023/12/uac-0099-using-winrar-exploit-to-target.html)**
has been attributed to a previously undocumented .NET infostealer and remote access trojan (RAT) codenamed
**ASHVEIN**
.

According to TrendAI, the malware has been put to use in attacks targeting Ukrainian government personnel. The cybersecurity company is tracking the cluster under the name
**Earth Sirrush**
(previously SHADOW-EARTH-065).

ASHVEIN, which its developers internally refer to as "TelemetryBrowser," brings together credential theft, surveillance, and remote-control capabilities. Its functionality includes credential theft from Chrome and Firefox, GDI-based screenshot capture, file enumeration and retrieval, PowerShell remote shell execution, system fingerprinting, and encrypted command-and-control (C2) communications.

"ASHVEIN also hides tasking inside invisible HTML elements," TrendAI
[said](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/earth-sirrush-russia-aligned-intrusion-set-4-years-evolving-espionage-tooling)
. "Some variants use a GitHub-based dead drop resolver as a fallback mechanism, while delivery methods include DLL sideloading, VHD containers, and dedicated .NET droppers."

UAC-0099 was first documented by the Computer Emergency Response Team of Ukraine (CERT-UA) in June 2023. It has a history of targeting Ukrainian government, defense, border guard, and logistics entities since at least mid-2022, emerging in the wake of Russia's full-scale invasion of Ukraine.

ESET, in its APT Activity Report
[published](https://thehackernews.com/2025/11/trojanized-eset-installers-drop.html)
in November 2025, said the cyber espionage crew can serve as an initial access broker for
[Sandworm](https://thehackernews.com/2026/08/sandworm-linked-uac-0145-uses-fake-job.html)
, a Russian advanced persistent threat (APT) group best known for its destructive attacks against Ukraine.

In the intervening time period, the threat actor has steadily expanded its malware arsenal, while shifting from PowerShell- and Go-based tools to compiled C# and .NET Reactor-protected binaries concealed within steganographic image files.

Some of the malware families deployed by the threat actor over the years are listed below -

* 2022 - 2024:
  [LONEPAGE](https://thehackernews.com/2023/12/uac-0099-using-winrar-exploit-to-target.html)
  (PowerShell-based loader),
  [THUMBCHOP](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html)
  (C#-based browser stealer),
  [CLOGFLAG](https://thehackernews.com/2023/07/picassoloader-malware-used-in-ongoing.html)
  (keylogger), SEAGLOW, and OVERJAM (Go-based backdoors for interactive access and reverse-proxy, respectively)
* 2024 – 2025:
  [MATCHBOIL](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html)
  (C#-based loader),
  [MATCHWOK](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html)
  (C#-based backdoor), and
  [DRAGSTARE](https://thehackernews.com/2025/08/cert-ua-warns-of-hta-delivered-c.html)
  aka
  [NordDragonScan](https://thehackernews.com/2025/07/researchers-uncover-batavia-windows.html)
  (C#-based information stealer)
* October 2025: ASHVEIN aka TelemetryBrowser
* February – April 2026:
  [BadPaw aka CINDERBLOT](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html)
  (.NET-based loader) and
  [MeowMeow](https://thehackernews.com/2026/03/apt28-linked-campaign-deploys-badpaw.html)
  (backdoor)
* April – July 2026:
  [LUNCHPOKE](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html)
  (.NET DLL that masquerades as a Notepad++ plugin),
  [BURNYBEAR](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html)
  (.NET-based loader), and
  [MATCHBOIL.V2](https://thehackernews.com/2026/07/fake-notepad-plugin-delivers.html)
  (updated version of MATCHBOIL)

"Five builds were compiled between October 8 and October 23, 2025, across three distinct packing variants," TrendAI said. "ASHVEIN overlaps functionally with DRAGSTARE in credential theft, screenshots, file collection, and WMI fingerprinting, but key differences separate them."

"DRAGSTARE was compiled by the NordDragon developer account, targets both Chrome and Firefox, and includes anti-VM checks and subnet scanning. ASHVEIN, compiled by the dev account, uses a different packing approach. The functional overlap, combined with separate build environments, indicates parallel tool development under different developer accounts for the same operational requirement."

UAC-0099 makes use of multiple delivery methods for ASHVEIN, including DLL sideloading (aka FORGECLAMP), VHD containers, and purpose-built .NET droppers. One such .NET executable is AnswerFromPolice, which embeds a Microsoft Word document that purports to be a response from the National Police of Ukraine.

AnswerFromPolice displays the decoy document impersonating the National Police of Ukraine while deploying the malware in the background. "This combination of institutional impersonation and credible decoy content is designed to increase the likelihood that recipients will open and trust the file," TrendAI said.

Another malware family that has undergone extensive evolution over the past year is MATCHBOIL. ESET's research indicates that the C# downloader has been under active development since at least April 2024. MATCHBOIL's primary responsibility is to download, install, and persist another payload.

Recently observed iterations of MATCHBOIL have taken the form of a DLL file that's executed by a custom C# loader. The malware also checks to determine if it's running in a virtual environment and aborts execution if the installation date of the operating system is 10 or more days older than the date on which the artifact is being executed.

"This demonstrates a keen interest by UAC-0099 operators in improving their downloader, not only to avoid detection by security solutions, but also to use it as a key part of their toolset in future attacks," ESET researcher Fernando Tavella
[said](https://www.welivesecurity.com/en/eset-research/matchboil-new-tricks-same-old-evil-intentions/)
in a report shared with The Hacker News.

In what appears to be yet another evolution of the threat actor's tradecraft, the Slovak cybersecurity company said it
[observed](https://thehackernews.com/2026/09/russia-aligned-uac-0099-plants-nuclear.html)
the use of a technique called GuardBreaker against a Ukrainian target to undermine artificial intelligence (AI)-assisted analysis.

Specifically, a malicious Visual Basic Script (VBScript) deployed by the adversary has been found to embed a prompt asking for instructions to make a nuclear weapon in an attempt to deliberately trigger a large language model's (LLM) safety mechanisms and prevent it from analyzing the rest of the code. The VBScript serves as a conduit for MATCHBOIL.

"Available evidence suggests that the targeting has expanded beyond government and military organizations to include civilian logistics and infrastructure operators that keep Ukraine supplied," TrendAI said. "That drift tracks the war: As the conflict continues, the value of understanding Ukraine's logistics networks rises, and the cyber effort follows the same logic as the kinetic one."