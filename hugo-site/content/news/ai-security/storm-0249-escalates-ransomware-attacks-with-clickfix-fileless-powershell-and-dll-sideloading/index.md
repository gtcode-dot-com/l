---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-10T00:03:07.939036+00:00'
exported_at: '2025-12-10T00:03:10.589186+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html
structured_data:
  about: []
  author: ''
  description: Storm-0249 now employs ClickFix, fileless PowerShell, and DLL sideloading
    to gain stealthy access that enables ransomware operations.
  headline: Storm-0249 Escalates Ransomware Attacks with ClickFix, Fileless PowerShell,
    and DLL Sideloading
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/storm-0249-escalates-ransomware-attacks.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Storm-0249 Escalates Ransomware Attacks with ClickFix, Fileless PowerShell,
  and DLL Sideloading
updated_at: '2025-12-10T00:03:07.939036+00:00'
url_hash: a0aedb90976531326ac2077337120797d138c2b1
---

**

Dec 09, 2025
**

Ravie Lakshmanan

Ransomware / Endpoint Security

The threat actor known as
**Storm-0249**
is likely shifting from its role as an initial access broker to adopt a combination of more advanced tactics like domain spoofing, DLL side-loading, and fileless PowerShell execution to facilitate ransomware attacks.

"These methods allow them to bypass defenses, infiltrate networks, maintain persistence, and operate undetected, raising serious concerns for security teams," ReliaQuest
[said](https://reliaquest.com/blog/threat-spotlight-storm-0249-precision-endpoint-exploitation)
in a report shared with The Hacker News.

Storm-0249 is the moniker assigned by Microsoft to an initial access broker that has sold footholds into organizations to other cybercrime groups, including ransomware and extortion actors like
[Storm-0501](https://thehackernews.com/2024/09/microsoft-identifies-storm-0501-as.html)
. It was first highlighted by the tech giant in September 2024.

Then, earlier this year, Microsoft also
[revealed](https://thehackernews.com/2025/04/microsoft-warns-of-tax-themed-email.html)
details of a phishing campaign mounted by the threat actor that used tax-related themes to target users in the U.S. ahead of the tax filing season and infect them with Latrodectus and the BruteRatel C4 (BRc4) post-exploitation framework.

The end goal of these infections is to
[obtain persistent access](https://thehackernews.com/2025/08/storm-0501-exploits-entra-id-to.html)
to various enterprise networks and monetize them by selling them to ransomware gangs, providing them with a ready supply of targets, and accelerating the pace of such attacks.

The latest findings from ReliaQuest demonstrate a tactical shift, where Storm-0249 has resorted to using the infamous
[ClickFix](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html)
social engineering tactic to trick prospective targets into running malicious commands via the Windows Run dialog under the pretext of resolving a technical issue.

In this case, the command copied and executed leverages the legitimate "curl.exe" to fetch a PowerShell script from a URL that mimics a Microsoft domain to give victims a false sense of trust ("sgcipl[.]com/us.microsoft.com/bdo/") and execute it in a fileless manner via PowerShell.

This, in turn, results in the execution of a malicious MSI package with SYSTEM privileges, which drops a trojanized DLL associated with SentinelOne's endpoint security solution ("SentinelAgentCore.dll") into the user's AppData folder along with the legitimate "SentinelAgentWorker.exe" executable.

In doing so, the idea is to sideload the rogue DLL when the "SentinelAgentWorker.exe" process is launched, thereby allowing the activity to stay undetected. The DLL then establishes encrypted communication with a command-and-control (C2) server.

Storm-0249 has also been observed making use of legitimate Windows administrative utilities like reg.exe and findstr.exe to extract unique system identifiers like MachineGuid to lay the groundwork for follow-on ransomware attacks. The use of living-off-the-land (LotL) tactics, coupled with the fact that these commands are run under the trusted "SentinelAgentWorker.exe" process, means the activity is unlikely to raise any red flags.

The findings indicate a departure from mass phishing campaigns to precision attacks that weaponize the trust associated with signed processes for added stealth.

"This isn't just generic reconnaissance – it's preparation for ransomware affiliates," ReliaQuest said. "Ransomware groups like LockBit and ALPHV use MachineGuid to bind encryption keys to individual victim systems."

"By tying encryption keys to MachineGuid, attackers ensure that even if defenders capture the ransomware binary or attempt to reverse-engineer the encryption algorithm, they cannot decrypt files without the attacker-controlled key."