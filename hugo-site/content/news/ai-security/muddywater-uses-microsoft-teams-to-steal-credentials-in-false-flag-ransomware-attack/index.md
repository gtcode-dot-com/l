---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-06T16:15:14.216074+00:00'
exported_at: '2026-05-06T16:15:16.586004+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html
structured_data:
  about: []
  author: ''
  description: MuddyWater used Teams phishing in 2026 to steal credentials, enabling
    stealthy data exfiltration and persistence without encryption.
  headline: MuddyWater Uses Microsoft Teams to Steal Credentials in False Flag Ransomware
    Attack
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/muddywater-uses-microsoft-teams-to.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: MuddyWater Uses Microsoft Teams to Steal Credentials in False Flag Ransomware
  Attack
updated_at: '2026-05-06T16:15:14.216074+00:00'
url_hash: e322187aad2c0442b8af7bd373a09e88438ac127
---

The Iranian state-sponsored hacking group known as
[MuddyWater](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)
(aka Mango Sandstorm, Seedworm, and Static Kitten) has been attributed to a ransomware attack in what has been described as a "false flag" operation.

The attack, observed by Rapid7 in early 2026, has been found to leverage social engineering techniques via Microsoft Teams to initiate the infection sequence. Although the incident initially appeared to be consistent with a ransomware-as-a-service (RaaS) group operating under the
[Chaos](https://thehackernews.com/2025/07/chaos-raas-emerges-after-blacksuit.html)
brand, evidence points to it being a targeted state-backed attack that masquerades as opportunistic extortion.

"The campaign was characterized by a high-touch
[social engineering phase conducted via Microsoft Teams](https://thehackernews.com/2026/04/unc6692-impersonates-it-helpdesk-via.html)
, where the attackers utilized interactive screen-sharing to harvest credentials and manipulate multi-factor authentication (MFA)," Rapid7 said in a
[report](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/)
shared with The Hacker News.

"Once inside, the group bypassed traditional ransomware workflows, forgoing file encryption in favor of data exfiltration and long-term persistence via remote management tools like DWAgent."

The findings indicate that MuddyWater is attempting to muddy attribution efforts by increasingly relying on off-the-shelf tools available in the cybercrime underground to conduct its attacks. This shift has also been
[documented](https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html)
by Ctrl-Alt-Intel, Broadcom, Check Point, and JUMPSEC in recent months, highlighting the adversary's use of CastleRAT and Tsundere.

With that said, this is not the first time MuddyWater has conducted ransomware attacks. In September 2020, the threat actor was
[attributed](https://thehackernews.com/2025/12/iran-linked-hackers-hits-israeli_2.html)
to a campaign targeting prominent Israeli organizations with a loader called PowGoop that deployed a variant of Thanos ransomware with destructive capabilities.

Then, in 2023, Microsoft
[disclosed](https://thehackernews.com/2023/04/iran-based-hackers-caught-carrying-out.html)
that the hacking group teamed up with DEV-1084, a threat actor known to use the DarkBit persona, to conduct destructive attacks under the pretext of deploying ransomware. As recently as October 2025, the attackers are believed to have
[used the Qilin ransomware](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
to target an Israeli government hospital.

"In this case, the emerging picture was that the attackers were likely Iranian-affiliated operators working through the cyber criminal ecosystem, using a criminal ransomware brand and methods associated with the broader extortion market, while serving a strategic Iranian objective," Check Point noted back in March.

"The use of Qilin, and participation in its affiliate program, likely serves not only as a layer of cover and plausible deniability, but also as a meaningful operational enabler, especially as earlier attacks appear to have heightened security measures and monitoring by Israeli authorities."

Chaos is a RaaS group that emerged in early 2025. Known for its double extortion model, the threat actor has advertised its affiliate program on cybercrime forums, like RAMP and RehubCom.

Attacks mounted by the e-crime gang leverage a combination of mail flooding and vishing using Teams, often by impersonating IT support personnel, to trick victims into installing remote access tools like Microsoft Quick Assist, and then abuse that foothold to burrow deeper into the victim's environment and deploy ransomware.

"The group has also demonstrated triple extortion by threatening distributed denial-of-service (DDoS) attacks against the victim's infrastructure," Rapid7 said. "These capabilities are reportedly offered to affiliates as part of bundled services, representing a notable feature of its RaaS model. Additionally, Chaos has been observed leveraging elements of quadruple extortion, including threats to contact customers or competitors to increase pressure on victims."

As of late March 2026, Chaos has claimed 36 victims on its data leak site, most of which are located in the U.S. Construction, manufacturing, and business services are some of the prominent sectors targeted by the group.

In the intrusion analyzed by Rapid7, the threat actor is said to have initiated external chat requests via Teams to engage with employees and obtain initial access through screen-sharing sessions, followed by using compromised user accounts to conduct reconnaissance, establish persistence using tools like DWAgent and AnyDesk, move laterally, and exfiltrate data. The victim was then contacted via email for ransom negotiations.

"While connected, the TA [threat actor] executed basic discovery commands, accessed files related to the victim’s VPN configuration, and instructed users to enter their credentials into locally created text files," Rapid7 explained. "In at least one instance, the TA also deployed a remote management tool (AnyDesk) to further facilitate access."

The threat actor has also been observed using RDP to download an executable ("ms\_upd.exe") from an external server ("172.86.126[.]208") using the curl utility. Upon execution, the binary kicks off a multi-stage infection chain that delivers more malicious components.

A brief description of the malware families is below -

* [ms\_upd.exe](https://www.virustotal.com/gui/file/24857fe82f454719cd18bcbe19b0cfa5387bee1022008b7f5f3a8be9f05e4d14)
  (aka
  [Stagecomp](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)
  ), which collects system information and reaches out to a command-and-control (C2) server to drop next-stage payloads (game.exe, WebView2Loader.dll, and visualwincomp.txt).
* [game.exe](https://www.virustotal.com/gui/file/1319d474d19eb386841732c728acf0c5fe64aa135101c6ceee1bd0369ecf97b6)
  (aka
  [Darkcomp](https://thehackernews.com/2026/03/iran-linked-muddywater-hackers-target.html)
  ), which is a bespoke remote access trojan (RAT) that masquerades as a legitimate
  [Microsoft WebView2](https://developer.microsoft.com/en-us/microsoft-edge/webview2/)
  application. It's a trojanized version of the official Microsoft
  [WebView2APISample project](https://github.com/MicrosoftEdge/WebView2Samples/tree/main/SampleApps/WebView2APISample)
  .
* [WebView2Loader.dll](https://www.virustotal.com/gui/file/a47cd0dc12f0152d8f05b79e5c86bac9231f621db7b0e90a32f87b98b4e82f3a)
  , a legitimate DLL downloaded by ms\_upd.exe. It's required by Microsoft Edge WebView2 to embed web content in Windows applications.
* [visualwincomp.txt](https://www.virustotal.com/gui/file/c86ab27100f2a2939ac0d4a8af511f0a1a8116ba856100aae03bc2ad6cb0f1e0)
  , an encrypted configuration used by the RAT to obtain the C2 information.

The RAT connects to the C2 server and enters an infinite loop to poll for new commands every 60 seconds, allowing it to run commands or PowerShell scripts, perform file operations, and spawn an interactive cmd.exe shell or PowerShell.

The campaign's links to MuddyWater stem from the use of a
[code-signing certificate](https://www.seqrite.com/blog/iran-us-israel-cyberwar-2026-analysis/)
attributed to "Donald Gay" to sign "ms\_upd.exe." The certificate has been
[previously put to use](https://thehackernews.com/2026/02/muddywater-targets-mena-organizations.html)
by the threat cluster to sign its malware, including a CastleLoader downloader called
[Fakeset](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
.

These findings underscore the growing convergence of state-sponsored intrusion activity and cybercriminal tradecraft to obscure attribution and delay appropriate defensive response.

"The use of a RaaS framework in this context may enable the actor to blur distinctions between state-sponsored activity and financially motivated cybercrime, thereby complicating attribution," Rapid7 said. "Furthermore, the inclusion of extortion and negotiation elements could serve to focus defensive efforts on immediate impact, likely delaying the identification of underlying persistence mechanisms established via remote access tools such as DWAgent or AnyDesk."

"Notably, the apparent absence of file encryption, despite the presence of Chaos ransomware artifacts, represents a deviation from typical ransomware behavior. This inconsistency may indicate that the ransomware component functioned primarily as a facilitating or obfuscation mechanism, rather than as the primary objective of the intrusion."

The development comes as Hunt.io revealed details of an Iranian-nexus operation targeting Omani government institutions to exfiltrate more than 26,000 Ministry of Justice user records, judicial case data, committee decisions, and SAM and SYSTEM registry hives.

"An open directory on 172.86.76[.]127, a RouterHosting VPS in the United Arab Emirates, surfaced an active intrusion campaign against the Omani government, with the toolkit, C2 code, session logs, and exfiltrated data all sitting in plain sight," the company
[said](https://hunt.io/blog/iranian-nexus-oman-government-intrusion)
. "The primary target was the Ministry of Justice and Legal Affairs (mjla.gov[.]om)."

The discovery also coincides with continued activity from pro-Iran-aligned hacktivist groups, such as Handala Hack, which has claimed to have published details on nearly 400 U.S. Navy personnel in the Persian Gulf and carried out an attack on the Port of Fujairah in the United Arab Emirates, enabling it to gain access to its internal systems and leak about 11,000 sensitive documents related to invoices, shipping records, and customs documents.

"A month ago, we documented a broad escalation in Iranian-linked cyber operations —
[surveillance via hacked cameras](https://research.checkpoint.com/2026/interplay-between-iranian-targeting-of-ip-cameras-and-physical-warfare-in-the-middle-east/)
, the leak of thousands of highly sensitive documents from Israel's former Military Chief of Staff, and a measurable rise in attack volume across the region. We said then that further escalation was likely," Sergey Shykevich, group manager at Check Point Research, told The Hacker News.

"The claimed attack on the Port of Fujairah is that escalation, if confirmed. What's changed is the nature of the threat: this is no longer about intelligence gathering or public embarrassment. Stolen port infrastructure data was allegedly used to enable physical missile targeting."

"The cyber and kinetic domains are now explicitly connected. This campaign is not slowing down. Every quiet period on the physical front has historically been followed by intensified cyber activity — and what we're seeing now is the most serious manifestation of that pattern to date."