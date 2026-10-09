---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-06T12:15:14.740649+00:00'
exported_at: '2026-01-06T12:15:17.187027+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/russia-aligned-hackers-abuse-viber-to.html
structured_data:
  about: []
  author: ''
  description: Russia-aligned UAC-0184 abuses Viber messages to deliver Hijack Loader
    and Remcos RAT in espionage attacks on Ukrainian military and government system
  headline: Russia-Aligned Hackers Abuse Viber to Target Ukrainian Military and Government
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/russia-aligned-hackers-abuse-viber-to.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Russia-Aligned Hackers Abuse Viber to Target Ukrainian Military and Government
updated_at: '2026-01-06T12:15:14.740649+00:00'
url_hash: a259942b394956c4d08f0ac958d3917ca84329e7
---

**

Jan 05, 2026
**

Ravie Lakshmanan

Cyber Espionage / Windows Security

The Russia-aligned threat actor known as
**UAC-0184**
has been observed targeting Ukrainian military and government entities by leveraging the Viber messaging platform to deliver malicious ZIP archives.

"This organization has continued to conduct high-intensity intelligence gathering activities against Ukrainian military and government departments in 2025," the 360 Threat Intelligence Center
[said](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247507757&idx=1&sn=cf6b118e88395af45a000aae80811264&poc_token=HNnfW2mjnOhb-9voW7EL-AX6wsrUBqSd4LXEFGMn)
in a technical report.

Also tracked as Hive0156, the hacking group is
[primarily known](https://thehackernews.com/2024/02/new-idat-loader-attacks-using.html)
for leveraging war-themed lures in
[phishing emails](https://thehackernews.com/2024/04/ukraine-targeted-in-cyberattack.html)
to deliver
[Hijack Loader](https://thehackernews.com/2025/07/cyber-espionage-campaign-hits-russian.html)
in attacks targeting Ukrainian entities. The malware loader subsequently acts as a pathway for Remcos RAT infections.

The threat actor was first documented by CERT-UA in early January 2024. Subsequent attack campaigns have been
[found](https://thehackernews.com/2024/10/pro-ukrainian-hackers-strike-russian.html)
to leverage messaging apps like Signal and Telegram as a delivery vehicle for malware. The latest findings from the Chinese security vendor points to a further evolution of this tactic.

The attack chain involves the use of Viber as an initial intrusion vector to distribute malicious ZIP archives containing multiple Windows shortcut (LNK) files disguised as official Microsoft Word and Excel documents to trick recipients into opening them.

The LNK files are designed to serve a decoy document to the victim to lower their suspicion, while silently executing Hijack Loader in the background by fetching a second ZIP archive ("smoothieks.zip") from a remote server by means of a PowerShell script.

The attack reconstructs and deploys Hijack Loader in memory through a multi-stage process that employs techniques like DLL side-loading and module stomping to evade detection by security tools. The loader then scans the environment for installed security software, such as those related to Kaspersky, Avast, BitDefender, AVG, Emsisoft, Webroot, and Microsoft, by calculating the CRC32 hash of the corresponding program.

Besides establishing persistence by means of scheduled tasks, the loader takes steps to subvert static signature detection before covertly executing Remcos RAT by injecting it into "chime.exe." The remote administration tool grants the attackers the ability to manage the endpoint, execute payloads, monitor activities, and steal data.

"Although marketed as legitimate system management software, its powerful intrusive capabilities make it frequently used by various malicious attackers for cyber espionage and data theft activities," the 360 Threat Intelligence Center said. "Through the graphical user interface (GUI) control panel provided by Remcos, attackers can perform batch automated management or precise manual interactive operations on the victim's host."