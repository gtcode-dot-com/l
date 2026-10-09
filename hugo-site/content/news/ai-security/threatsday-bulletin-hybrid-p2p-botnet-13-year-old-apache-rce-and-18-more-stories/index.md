---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-09T14:15:14.576490+00:00'
exported_at: '2026-04-09T14:15:16.915645+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html
structured_data:
  about: []
  author: ''
  description: '6:08 PM This week in cybersecurity: botnets, RCE flaws, AI-driven
    attacks, stealers, and more. Fast, no-fluff roundup.'
  headline: 'ThreatsDay Bulletin: Hybrid P2P Botnet, 13-Year-Old Apache RCE and 18
    More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/threatsday-bulletin-hybrid-p2p-botnet.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: Hybrid P2P Botnet, 13-Year-Old Apache RCE and 18 More
  Stories'
updated_at: '2026-04-09T14:15:14.576490+00:00'
url_hash: f15e2fdbed07045bddef5f0f7bb3c8f415bad69a
---

**

Ravie Lakshmanan
**

Apr 09, 2026

Hacking News / Cybersecurity News

Thursday. Another week, another batch of things that probably should've been caught sooner but weren't.

This one's got some range — old vulnerabilities getting new life, a few "why was that even possible" moments, attackers leaning on platforms and tools you'd normally trust without thinking twice. Quiet escalations more than loud zero-days, but the kind that matter more in practice anyway.

Mix of malware, infrastructure exposure, AI-adjacent weirdness, and some supply chain stuff that's... not great. Let's get into it.

1. Resilient hybrid botnet surge

   A new variant of the botnet known as
   [Phorpiex](https://thehackernews.com/2021/12/new-phorpiex-botnet-variant-steals-half.html)
   (aka Trik) has been observed, using a hybrid communication model that combines traditional C2 HTTP polling with a peer-to-peer (P2P) protocol over both TCP and UDP to ensure operational continuity in the face of server takedowns. The malware acts as a conduit for encrypted payloads, making it challenging for external parties to inject or modify commands. The primary goal of Phorpiex's Twizt variant is to drop a clipper that re-routes cryptocurrency transactions, as well as distribute high-volume sextortion email spam and facilitate
   [ransomware deployment](https://thehackernews.com/2025/02/ransomhub-becomes-2024s-top-ransomware.html)
   (e.g., LockBit Black, Global). It also exhibits worm-like behavior by propagating through removable and remote drives, and drop modules responsible for exfiltrating mnemonic phrases and scanning for Local File Inclusion (LFI) vulnerabilities. "Phorpiex has consistently demonstrated its capability to evolve, shifting from a pure spam operation to a sophisticated platform," Bitsight
   [said](https://www.bitsight.com/blog/ransomware-twizt-inside-phorpiex-botnet)
   . "The Phorpiex botnet remains a highly adaptive and resilient threat." There are about 125,000 infections daily on average, with the most affected countries being Iran, Uzbekistan, China, Kazakhstan, and Pakistan.
2. Chained flaws enable stealth RCE

   A remote code execution (RCE) vulnerability that lurked in Apache ActiveMQ Classic for 13 years could be chained with an older flaw (CVE-2024-32114) to bypass authentication. Tracked as CVE-2026-34197 (CVSS score: 8.8), the newly identified bug allows attackers to invoke management operations through the Jolokia API and trick the message broker into retrieving a remote configuration file and executing operating system commands. According to Horizon3.ai, the security defect is a bypass for CVE-2022-41678, a bug that allows authenticated attackers to trigger arbitrary code execution and write web shells to disk. "The vulnerability requires credentials, but default credentials (admin:admin) are common in many environments," Horizon3.ai researcher Naveen Sunkavally
   [said](https://horizon3.ai/attack-research/disclosures/cve-2026-34197-activemq-rce-jolokia/)
   . "On some versions (6.0.0 - 6.1.1), no credentials are required at all due to another vulnerability, CVE-2024-32114, which inadvertently exposes the Jolokia API without authentication. In those versions, CVE-2026-34197 is effectively an unauthenticated RCE." The newly discovered security defect was
   [addressed](http://activemq.apache.org/security-advisories.data/CVE-2026-34197-announcement.txt)
   in ActiveMQ Classic versions 5.19.4 and 6.2.3.
3. Cyber fraud losses hit record highs

   Cyber-enabled fraud cost victims over $17.7 billion during 2025, as financial losses to internet-enabled fraud continue to grow. The total loss exceeds $20.87 billion, up 26% from 2024. "Cyber-enabled fraud is responsible for almost 85% of all losses reported to IC3 [Internet Crime Complaint Center] in 2025," the U.S. Federal Bureau of Investigation (FBI)
   [said](https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf)
   . "Cryptocurrency investment fraud was the highest source of financial losses to Americans in 2025, with $7.2 billion reported in losses." In all investment scams led the pack with $8.6 billion in reported losses, followed by business email compromise ($3 billion) and tech support scams ($2.1 billion). Sixty-three new ransomware variants were identified last year, leading to more than $32 million in losses. Akira, Qilin, INC./Lynx/Sinobi, BianLian, Play, Ransomhub, Lockbit, Dragonforce, Safepay, and Medusa emerged as the top ten variants to hit critical manufacturing, healthcare, public health, and government entities.
4. AI-driven DDoS tactics escalate

   According to data from NETSCOUT, more than 8 million DDoS attacks were recorded across 203 countries and territories between July and December 2025. "The attack count remained stable compared to the first half of the year, but the nature and sophistication of attacks changed dramatically," the company
   [said](https://www.netscout.com/blog/how-botnet-driven-ddos-attacks-evolved-2h-2025)
   . "The TurboMirai class of IoT botnets, including AISURU and Eleven11 (RapperBot), emerged as a major force. DDoS-for-hire platforms are now integrating dark-web LLMs and conversational AI, lowering the technical barrier for launching complex, multi-vector attacks. Even unskilled threat actors can now orchestrate sophisticated campaigns using natural-language prompts, increasing risk for all industries."
5. Insider breach exposes private photos

   A former Meta employee in the U.K. is under investigation over allegations that he illegally downloaded about 30,000 private photos from Facebook. According to
   [The Guardian](https://www.theguardian.com/uk-news/2026/apr/07/meta-worker-london-accused-downloading-private-facebook-images)
   , the accused developed a software program to evade Facebook's internal security systems and access users' private images. Meta uncovered the breach more than a year ago, terminated the employee, and referred the case to law enforcement. The company said it also notified affected users, although it's not clear how many were impacted.
6. Help desk attacks enable enterprise breaches

   Google said it's tracking a financially motivated threat cluster called UNC6783 that's tied to the "Raccoon" persona and is targeting dozens of high-profile organizations across multiple sectors by compromising business process outsourcing (BPO) providers and help desk staff for later data extortion. "The campaign relies on live chat social engineering to direct employees to spoofed Okta logins using [org].zendesk-support[##].com domains," Austin Larsen, Google Threat Intelligence Group (GITG) principal threat analyst,
   [said](https://x.com/AustinLarsen_/status/2041376265907601529)
   . "Their phishing kit steals clipboard contents to bypass MFA and enroll their own devices for persistent access. We also observed them using fake security updates (ClickFix) to drop remote access malware." Organizations are advised to prioritize FIDO2 hardware keys for high-risk roles, monitor live chat for suspicious links, and regularly audit newly enrolled MFA devices.
7. Magecart skimmer hides in SVG

   A large-scale Magecart campaign is using invisible 1x1 pixel SVG elements to inject a fake checkout overlay on 99 Magento e-commerce stores, exfiltrating payment data to six attacker-controlled domains. "In the early hours of April 7th, nearly 100 Magento stores got mass-infected with a 'double-tap' skimmer: a credit card stealer hidden inside an invisible SVG element," Sansec
   [said](https://sansec.io/research/svg-onload-magecart-skimmer)
   . "The likely entry vector is the
   [PolyShell vulnerability](https://thehackernews.com/2026/03/webrtc-skimmer-bypasses-csp-to-steal.html)
   that continues to affect unprotected Magento stores." Like other attacks of this kind, the skimmer shows victims a convincing "Secure Checkout" overlay, complete with card validation and billing fields. Once the payment details are captured, it silently redirects the shopper to the real checkout page. Adobe has yet to release a security update to address the PolyShell flaw in production versions of Magento.
8. Emoji-coded signals evade detection

   Cybercriminals are
   [using emojis](https://www.yeoandyeo.com/resource/emoji-smuggling-the-cyberattack-hiding-in-plain-sight)
   across illicit communities to signal financial activity, access and account compromise, tooling and service offerings, represent targets or regions, and communicate momentum or importance. Using emojis allows bad actors to bypass security controls. "Emojis provide a shared visual layer that allows actors to communicate core concepts without relying entirely on text," Flashpoint
   [said](https://flashpoint.io/blog/the-language-of-emojis-in-threat-intelligence/)
   . "This is particularly valuable in: large Telegram channels with international membership, cross-border fraud operations, [and] decentralized marketplaces. This ability to compress meaning into visual shorthand helps scale operations and coordination across diverse actor networks."
9. Stealth RAT delivered via MSI

   A ClickFix campaign targeting Windows users is leveraging malicious MSI installers to deliver a Node.js-based information stealer. "This Windows payload is a highly adaptable remote access Trojan (RAT) that minimizes its forensic footprint by using dynamic capability loading," Netskope
   [said](https://www.netskope.com/blog/from-clickfix-to-maas-exposing-a-modular-windows-rat-and-its-admin-panel)
   . "The core stealing modules and communication protocols are never stored on the victim’s disk. Instead, they are delivered in-memory only after a successful C2 connection is established. To further obfuscate the attacker’s infrastructure, the malware routes gRPC streaming traffic over the Tor network, providing a persistent and masked bidirectional channel."
10. macOS attack bypasses Terminal safeguards

    More ClickFix, this time targeting macOS. According to Jamf, a ClickFix-style macOS attack is abusing the "applescript://" URL scheme to launch Script Editor and deliver an Atomic Stealer infostealer payload, thereby bypassing Terminal entirely. The attack leverages fake Apple-themed web pages that include instructions to "reclaim disk space on your Mac" by clicking on an "Execute" button that triggers the "applescript://" URL scheme. The new approach is likely a response to a
    [new security feature](https://thehackernews.com/2026/03/weekly-recap-telecom-sleeper-cells-llm.html#:~:text=Apple%20Tests%20Ways%20to%20Block%20Malicious%20Copy%2DPastes%20in%20macOS)
    introduced by Apple in macOS 26.4 that scans commands pasted into Terminal before they're executed. "It's a meaningful friction point, but as this campaign illustrates, when one door closes, attackers find another," security researcher Thijs Xhaflaire said.
11. PyPI package exfiltrates AI prompts

    A malicious PyPI package named hermes-px has been advertised as a "Secure AI Inference Proxy" but contains functionality to steal users' prompts. "The package actually hijacks a Tunisian university's private AI endpoint, bundles a stolen and rebranded Anthropic Claude Code system prompt, launders all responses to hide the true upstream source, and exfiltrates every user message directly to the attacker's Supabase database, bypassing the very Tor anonymity it promises," JFrog
    [said](https://research.jfrog.com/post/hermes-px-pypi/)
    .
12. Exposed PLCs targeted by state actors

    Data from Censys has revealed that there are 5,219 internet-exposed hosts that self-identify as Rockwell Automation/Allen-Bradley devices. "The United States accounts for 74.6% of global exposure (3,891 hosts), with a disproportionate share on cellular carrier ASNs indicative of field-deployed devices on cellular modems," it
    [said](https://censys.com/blog/iranian-affiliated-apt-targeting-rockwell-allen-bradley-plcs/)
    . "Spain (110), Taiwan (78), and Italy (73) represent the largest non-Anglosphere concentrations. Iceland's presence (36 hosts) is disproportionate to its population and warrants attention, given its geothermal energy infrastructure." The disclosure follows a
    [joint advisory](https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html)
    from U.S. agencies that warned of ongoing exploitation of internet-facing Rockwell Automation/Allen-Bradley programmable logic controllers (PLCs) by Iranian-affiliated nation-state actors since March 2026 to breach U.S. critical infrastructure sectors, causing operational disruption and financial loss in some cases. The agencies said the attacks are reminiscent of similar attacks on PLCs by Cyber Av3ngers in late 2023.
13. Code leak weaponized for malware spread

    In late March 2026, Anthropic inadvertently
    [exposed internal Claude Code source material](https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html)
    via a misconfigured npm package, which included approximately 512,000 lines of internal TypeScript. While the exposure lasted only about three hours, it triggered rapid mirroring of the source code across GitHub, prompting Anthropic to
    [issue takedown notices](https://github.com/github/dmca/blob/master/2026/03/2026-03-31-anthropic.md)
    (and later a
    [partial retraction](https://github.com/github/dmca/blob/master/2026/04/2026-04-01-anthropic-retraction.md)
    ). Needless to say, threat actors wasted no time and
    [took advantage](https://www.trendmicro.com/en_us/research/26/d/claude-code-remains-a-lure-what-defenders-should-do.html)
    of the topical nature of the leak to distribute Vidar Stealer, PureLogs Stealer, and GhostSocks proxy malware through fake leaked Claude Code GitHub repositories. "The campaign abuses GitHub Releases as a trusted malware delivery channel, using large trojanized archives and disposable accounts to repeatedly evade takedowns," Trend Micro
    [said](https://www.trendmicro.com/en_us/research/26/d/weaponizing-trust-claude-code-lures-and-github-release-payloads.html)
    . "The combined functionality of the malware payloads enables credential theft, cryptocurrency wallet exfiltration, session hijacking, and residential proxy abuse across Windows, giving the operators multiple monetization paths from a single infection."
14. Lumma successor adopts evasive tactics

    A new 64-bit version of Lumma Stealer called Remus (historically called Tenzor) has emerged in the wild following Lumma's takedown and the doxxing of its alleged core members. "The first Remus campaigns date back to February 2026, with the malware switching from Steam/Telegram dead drop resolvers to
    [EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)
    and employing new anti-analysis checks," Gen researchers
    [said](https://www.gendigital.com/blog/insights/research/remus-64bit-variant-of-lumma-stealer)
    . Besides using identical code, direct syscalls/sysenters, and the same string obfuscation technique, another detail linking the two is the use of an application-bound encryption method, only observed in Lumma Stealer to date.
15. Court rulings split on AI risk label

    In a setback for Anthropic, a Washington, D.C., federal appeals court declined to block the U.S. Department of Defense's national security designation of the AI company as a
    [supply chain risk](https://thehackernews.com/2026/02/pentagon-designates-anthropic-supply.html)
    . The development comes after another appeals court in San Francisco came to the opposite conclusion in a separate legal challenge by Anthropic, granting it a
    [preliminary injunction](https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html#court-halts-ai-risk-label)
    that bars the Trump administration from enforcing a ban on the use of AI chatbot Claude.The company has said the designation could cost the company billions of ⁠dollars in lost business and reputational harm. As Reuters
    [notes](https://www.reuters.com/world/us-court-declines-block-pentagons-anthropic-blacklisting-now-2026-04-08/)
    , the lawsuit is one of two that Anthropic filed over the Trump administration's unprecedented move to classify it as a supply chain risk after it refused to allow the military to use Claude for domestic mass surveillance or autonomous weapons.
16. Trojanized tools deliver crypto clipper

    In a
    [new campaign](https://securelist.com/clipbanker-malware-distributed-via-trojanized-proxifier/119341/)
    observed by Kaspersky, unwitting users searching for proxy clients like Proxifier on search engines like Google and Yandex are being directed to malicious GitHub repositories that host an executable, which acts as a wrapper around the legitimate Proxifier installer.Once launched, it configures Microsoft Defender Antivirus exclusions, launches the real Proxifier installer, sets up persistence, and runs a PowerShell script that reaches out to Pastebin to retrieve a next-stage payload. The downloaded PowerShell script is responsible for retrieving another script containing the Clipper malware from GitHub. The malware substitutes cryptocurrency wallet addresses copied to the clipboard with an attacker-controlled wallet with the intention of rerouting financial transactions. Since the start of 2025, more than 2,000 Kaspersky users – most of them in India and Vietnam – have encountered the threat.
17. SaaS platforms abused for phishing delivery

    Threat actors are leveraging notification pipelines in popular collaboration platforms to deliver spam and phishing emails. Because these emails are dispatched from the platform's own infrastructure (e.g., Jira's Invite Customers feature), they are unlikely to be blocked by email security tools. "These emails are transmitted using the legitimate mail delivery infrastructure associated with GitHub and Jira, minimizing the likelihood that they will be blocked in transit to potential victims," Cisco Talos
    [said](https://blog.talosintelligence.com/weaponizing-saas-notification-pipelines/)
    . "By taking advantage of the built-in notification functionality available within these platforms, adversaries can more effectively circumvent email security and monitoring solutions and facilitate more effective delivery to potential victims." The development coincides with a phishing campaign targeting multiple organizations with invitation lures sent from compromised email accounts that lead to the
    [deployment](https://redcanary.com/blog/threat-intelligence/phishing-rmm-tools/)
    of legitimate remote monitoring and management (RMM) tools like LogMeIn Resolve. The campaign, tracked as
    [STAC6405](https://www.sophos.com/en-us/blog/incident-responders-s-il-vous-plait)
    , has been ongoing since April 2025. In one case, the threat actor has been found to leverage a pre-existing installation of ScreenConnect to download a HeartCrypt-protected ZIP file that ultimately leads to the installation of malware that's consistent with
    [ValleyRAT](https://www.picussecurity.com/resource/blog/dissecting-valleyrat-from-loader-to-rat-execution-in-targeted-campaigns)
    . Other campaigns have leveraged
    [procurement-themed emails](https://www.forcepoint.com/blog/x-labs/dropbox-pdf-phishing-cloud-storage)
    to direct users to cloud-hosted PDFs containing embedded links that, when clicked, take victims to Dropbox credential harvesting pages. Threat actors have also
    [distributed executable files](https://www.trendmicro.com/en_us/research/26/c/copyright-lures-mask-a-multistage-purelog-stealer-attack.html)
    disguised as copyright violation notices to trick them into installing
    [PureLogs Stealer](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html)
    as part of a multi-stage campaign. What's more, Reddit posts advertising the premium version of TradingView have acted as a conduit for Vidar and Atomic Stealer to steal valuable data from both Windows and macOS systems. "The threat actor actively comments on their own posts with different accounts, creating the illusion of a busy and helpful community," Hexastrike
    [said](https://hexastrike.com/resources/blog/threat-intelligence/reddit-tradingview-lures-leading-to-vidar-and-amos-stealers/)
    . "More concerning, any comments from real users pointing out that the downloads are malware get deleted within minutes. The operation is hands-on and closely monitored."
18. Linux SMB flaw leaks crypto keys

    A high-severity security flaw has been disclosed in the Linux kernel's
    [ksmbd](https://docs.kernel.org/filesystems/smb/ksmbd.html)
    SMB3 server. Tracked as
    [CVE-2026-23226](https://nvd.nist.gov/vuln/detail/CVE-2026-23226)
    (CVSS score: 8.8), it falls under the same bug class as
    [CVE-2025-40039](https://nvd.nist.gov/vuln/detail/CVE-2025-40039)
    , which was patched in October 2025. "When two connections share a session over SMB3 multichannel, the kernel can read a freed channel struct – exposing the per-channel AES-128-CMAC signing key and causing a kernel panic," Orca
    [said](https://orca.security/resources/blog/cve-2026-23226-ksmbd-smb3-linux-kernel-uaf/)
    . "An attacker needs valid SMB credentials and network access to port 445." Alternatively, the vulnerability can be exploited by an attacker to leak the per-channel AES-128-CMAC key used to sign all SMB3 traffic, enabling them to forge signatures, impersonate the server, or bypass signature verification. It has been fixed in the commit "e4a8a96a93d."
19. Prompt injection turns AI into attack tool

    New research has demonstrated it's possible to trick Anthropic's vibe coding tool Claude Code into performing a full-scope penetration attack and credential theft by modifying a project's "CLAUDE.md" file to bypass the coding agent's safety guardrails. The instructions explicitly tell Claude Code to help the developer complete a penetration testing assessment against their own website and assist them in their tasks. "Claude Code should scan CLAUDE.md before every session, flagging instructions that would otherwise trigger a refusal if attempted directly within a prompt," LayerX
    [said](https://layerxsecurity.com/blog/vibe-hacking-claude-code-can-be-turned-into-a-nation-state-level-attack-tool-with-no-coding-at-all/)
    . "When Claude detects instructions that appear to violate its safety guardrails, it should present a warning and allow the developer to review the file before taking any actions."
20. AI exploit silently leaks enterprise data

    Grafana has patched a security vulnerability that could have enabled attackers to trick its artificial intelligence (AI) capabilities into leaking sensitive data by means of an indirect prompt injection and without requiring any user interaction. The attack has been codenamed GrafanaGhost by Noma Security. "By bypassing the client-side protections and security guardrails that restrict external data requests, GrafanaGhost allows an attacker to bridge the gap between your private data environment and an external server," the cybersecurity company
    [said](https://noma.security/blog/grafana-ghost/)
    . "Because the exploit ignores model restrictions and operates autonomously, sensitive enterprise data can be leaked silently in the background." GrafanaGhost is stealthy, as it requires no login credentials and does not depend on a user clicking a malicious link. The attack is another example of how AI-assisted features integrated into enterprise environments can be abused to access and extract critical data assets while remaining entirely invisible to defenders.

    [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlB7Ig3nKhgkeRj0BQk8-vdB2TsQYCEdjklYEfcIm-nWgrnimHZATEdz6D6ZHfHTp2-eh6hNnWy3txddkA8LBypEK-3eFb4tkwPnJTv7VU-7dPzNZrZUkSPoWvy7Hzn53C0hTrSvaLDiJ1fScn40GkCOhfqrMiy4__Ara0sEwxZRsbTsaLWj4OJyZD3rgx/s1600/system.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjlB7Ig3nKhgkeRj0BQk8-vdB2TsQYCEdjklYEfcIm-nWgrnimHZATEdz6D6ZHfHTp2-eh6hNnWy3txddkA8LBypEK-3eFb4tkwPnJTv7VU-7dPzNZrZUkSPoWvy7Hzn53C0hTrSvaLDiJ1fScn40GkCOhfqrMiy4__Ara0sEwxZRsbTsaLWj4OJyZD3rgx/s1600/system.png)
21. Android framework abused for payment fraud

    [LSPosed](https://github.com/LSPosed/Lsposed)
    is a powerful framework for rooted Android devices that allows users to modify the behavior of the system and apps in real-time without actually making any modifications to APK files. According to CloudSEK, threat actors are now weaponizing the tool to remotely inject fraudulent SMS messages and spoof user identities in modern payment ecosystems via a malicious module called "Digital Lutera." The attack effectively undermines
    [SIM-binding restrictions](https://thehackernews.com/2025/12/india-orders-messaging-apps-to-work.html)
    applied to banking and instant payment apps in India. However, for this approach to work, the threat actor requires a victim to install a Trojan that can intercept SMS messages sent to/from the device. While the attack previously combined a trojanized mobile device (the victim) and a modified mobile payment APK (on the attacker's device) to trick bank servers into believing the victim's SIM card is physically present in the attacker's phone, the latest iteration leans on LSPosed to achieve the same goals. A key requisite to this attack is that the attacker must have a rooted Android device with the LSPosed module installed. "This new attack vector allows threat actors to hijack legitimate, unmodified payment applications by 'gaslighting' the underlying Android operating system," CloudSEK
    [said](https://www.cloudsek.com/blog/weaponizing-lsposed-remote-sms-injection-and-identity-spoofing-in-modern-payment-ecosystems-2)
    . "By using LSPosed, the threat actor ensures the payment app's signature remains valid, making it invisible to many standard integrity checks."

That's the week. A lot of ground covered — old problems with new angles, platforms being abused in ways they weren't designed for, and a few things that are just going to keep getting worse before anyone seriously addresses them.

Patch what you can. Audit what you've trusted by default. And maybe double-check anything that touches AI right now — that space is getting messy fast.

Same time next Thursday.