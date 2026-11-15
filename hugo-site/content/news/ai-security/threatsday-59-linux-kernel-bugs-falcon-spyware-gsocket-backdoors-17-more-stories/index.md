---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T04:10:44.687668+00:00'
exported_at: '2026-11-15T04:10:46.959615+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
structured_data:
  about: []
  author: ''
  description: This week's ThreatsDay Bulletin covers AI-powered cyberattacks, ransomware,
    stolen credentials, Linux flaws, browser espionage, and emerging security
  headline: 'ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors +
    17 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/threatsday-59-linux-kernel-bugs-falcon.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay: 59 Linux Kernel Bugs, Falcon Spyware, GSocket Backdoors + 17 More
  Stories'
updated_at: '2026-11-15T04:10:44.687668+00:00'
url_hash: 0215fb6873aed2b71ad66634eef8200ce9a0de67
---

**

Ravie Lakshmanan
**

Nov 12, 2026

Hacking News / Cybersecurity News

A search result isn't always safe. An access request isn't always harmless. And a familiar account doesn't always mean a familiar person is using it. Simple things to remember. Yet a surprising amount of this week's trouble starts right there.

Attackers are using fake websites, stolen access, and trusted tools to get into places they shouldn't be. AI is helping them build attacks faster, while also giving them new systems to target. Some intruders are staying hidden even after security holes are fixed. Others are moving stolen money through a maze of transactions. And researchers keep finding small coding mistakes that can cause much bigger problems. Different stories, but much of the trouble comes down to making something dangerous look normal.

There is some good news, too. Criminal servers have been seized, and a few defenses are getting stronger. Still, plenty of things are going wrong in ways that shouldn't be this easy. Here's what turned up this week.

The threats change every week.
Subscribe, and we’ll alert you
when each new ThreatsDay Bulletin is out.

1. North Korea's crypto laundering network

   [How North Korea Is Laundering $6.4B Stolen from Binance](https://www.elliptic.co/insights/how-north-korea-is-laundering-the-6-4-billion-stolen-from-binance/)

   The North Korean threat actors linked to the
   [record-breaking theft of $6.43 billion](https://thehackernews.com/2026/11/binance-reveals-how-fake-job-interviews.html)
   from Binance are using a highly complex and clearly automated method to launder the illicit proceeds. "Since the theft it has used more than 20,000 wallets on 16 blockchains, at least 36 services and at least 65,000 transactions," Dr. Tom Robinson, Elliptic's founder and chief scientist,
   [said](https://www.elliptic.co/insights/how-north-korea-is-laundering-the-6-4-billion-stolen-from-binance/)
   . "Around $3.0 billion remains in addresses linked to the theft, mostly as ETH and BTC. A negligible amount has likely been cashed out." The attackers have also been observed
   [creating six meme coins](https://www.elliptic.co/insights/north-korea-meme-coins-binance-hack/)
   on the NEAR blockchain network (FUK, OLCCL, MEILI, MMLI, DABI, and SINU) to launder a slice of the ill-gotten funds, passing through about $430,000 of the stolen cryptocurrency. The goal is to disguise the path of money and make it harder to trace where the assets eventually end up. Other tactics used to make funds tracing more difficult include moving between blockchains through bridges and cross-chain swap services, swapping between assets on DEXs, hopping through lending vaults and liquid-staking services, and mixing bitcoin through coinjoins, and ETH and SOL through the Privacy Cash privacy pool. The Binance breach is by no means the first to affect a major cryptocurrency exchange, but it is the biggest ever by magnitude. North Korean spokesperson Kim Yo Jong
   [denied](https://kcnawatch.org/newstream/1793655240-736016532/press-statement-of-kim-yo-jong-department-director-of-c-c-wpk/)
   the country's role in the attack, calling it an "absurd" effort to "damage the international image of the DPRK."

   [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQl2mj4ZaDqjSfeRZqNw5CHDIIW4zqatYMtChfMxybdcNrZJgSihO0Mvs6jbraOYdHcGhYe7tY3dYAiEO5KuW3pmqkE_ur62woJRIFczinZ3GSx71PEwskKyNjWdgkSf2RprrQQ7a9TBz18oBGaVtD8AaHgd02kXXgR0dU22dzOg3lrnKprJHWtAcj8PkT/s1600/stolen.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgQl2mj4ZaDqjSfeRZqNw5CHDIIW4zqatYMtChfMxybdcNrZJgSihO0Mvs6jbraOYdHcGhYe7tY3dYAiEO5KuW3pmqkE_ur62woJRIFczinZ3GSx71PEwskKyNjWdgkSf2RprrQQ7a9TBz18oBGaVtD8AaHgd02kXXgR0dU22dzOg3lrnKprJHWtAcj8PkT/s1600/stolen.jpg)
2. GSocket detections surge 356%

   [Attacks Leveraging GSocket Spike in 2026](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)

   Microsoft said it has observed multiple incidents in which threat actors deployed
   [GSocket](https://github.com/hackerschoice/gsocket)
   , an open-source remote access tool, on internet-facing Linux servers to maintain access after the original vulnerabilities were addressed, turning a single web application compromise into persistent access. "Because GSocket relays traffic through a shared public network, there is no threat actor-owned IP address or domain to block," Microsoft
   [said](https://www.microsoft.com/en-us/security/blog/2026/11/11/global-socket-how-threat-actors-weaponizing-gsocket-stealthy-c2/)
   . "Defenders should look for GSocket deployment, persistence, privilege escalation, and outbound connections on affected hosts, not treat application patching alone as complete remediation." According to telemetry data, devices with GSocket-related detections increased 356.2% from March through August 2026, with most of them associated with PHP web applications, cPanel hosts, and Apache. The majority of targets of GSocket activity are in the education and research sector, followed by technology and communications, manufacturing, and government entities.
3. 235 servers seized in Europol takedown

   [Europol Operation Dismantles GootLoader, CastleRAT, and StealC Infrastructure](https://www.europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks)

   Europol, along with global partners, has disrupted the criminal infrastructure behind
   [GootLoader](https://thehackernews.com/2022/01/gootloader-hackers-targeting-employees.html)
   ,
   [CastleRAT](https://thehackernews.com/2025/09/tag-150-develops-castlerat-in-python.html)
   , and
   [StealC](https://thehackernews.com/2023/02/researchers-discover-dozens-samples-of.html)
   malware, seizing 235 servers and 257 domains as part of an
   [ongoing effort](https://www.justice.gov/opa/pr/gootloader-malware-disrupted-international-cyber-operation)
   called
   [Operation Endgame](https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html)
   . Since 2018, GootLoader has infected at least 25,000 computers globally, and has been used in ransomware attacks of at least 44 U.S. based victims, leading to approximately $28.8 million in losses. Of the seized infrastructure, 120 servers and 39 domains are linked to CastleRAT. "The operation targeted 'cybercrime-as-a-service' models, where these tools enabled further crimes like ransomware attacks and data theft," Europol
   [said](https://www.europol.europa.eu/media-press/newsroom/news/64-million-victim-datasets-secured-in-international-operation-against-malware-networks)
   . As part of the operation, authorities have identified over 6 million victim credentials. "The suspects were using these credentials, stolen from the victims after they infected them, to sell them and later be used for other cyber-attacks such as ransomware," Europol added.
4. Browser-based espionage targets governments

   [Hackers Deploy Falcon Browser Spyware to Monitor Government Emails and Steal Passwords](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)

   A command and control (C2) framework called Falcon (aka XG or Xiàng Gē) has been found compromising victims' browsers by running malicious JavaScript. Falcon shares near-identical URL structures, payload delivery mechanisms and communication protocols with
   [PeckBirdy](https://thehackernews.com/2026/01/china-linked-hackers-have-used.html)
   , another JavaScript C2 framework that came to light early this year. It's assessed that Falcon and PeckBirdy represent variants of the same core framework. "An actor leveraged Falcon to compromise visitors of webmail portals and government web applications by placing malicious JavaScript directly within these sites," Palo Alto Networks Unit 42
   [said](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)
   . "Operating entirely inside the browser context, attackers have used the framework to sideload malicious Chrome extensions and steal the following information: passwords, emails, session cookies, [and] communications." Falcon has also been used to deliver an implant dubbed Antino, which uses Microsoft OneDrive as a C2 channel. The activity has targeted government entities in one Middle Eastern country and four Southeast Asian countries between March and May 2026. "The campaigns we observed targeted ministries of foreign affairs, defense and interior, and law enforcement agencies, consistent with strategic intelligence collection objectives," Unit 42 said.
5. 59 Linux kernel bugs uncovered

   [Microsoft Flags 59 Linux Kernel Bugs](https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/)

   Microsoft said its scan of a subset of Linux kernel subsystems from late May to mid-June 2026 unearthed 26,502 raw findings using
   [MDASH](https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html)
   , which subsequently formed the basis for 59 public upstream reports and 33 assigned CVEs. This includes working root privilege-escalation exploits for eight of those CVEs, such as CVE-2026-64563. "CVE-2026-64563 is a one-line state-reset bug in rhashtable, the Linux kernel's shared resizable hash table," Microsoft
   [said](https://www.microsoft.com/en-us/security/blog/2026/11/11/lessons-from-59-linux-kernel-bug-reports/)
   . "Because callers trust the object pointers returned by a table walk, this small library flaw enabled a stable local privilege escalation on Linux -- and affected Android with SELinux enforcing -- without requiring special kernel configurations or user namespaces."
6. AI-assisted espionage in Central Asia

   [Silent Lynx Hackers Use AI Agent to Steal 2,000+ Tajik Government Documents](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server)

   An exposed
   [Silent Lynx](https://thehackernews.com/2026/10/silent-lynx-exploits-winrar-flaw-to.html)
   server has uncovered
   [cyber espionage operations](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html#silent-lynx-exploits-diplomacy-themes-to-breach-targets)
   targeting Central Asian governments and critical infrastructure from April to October 2026. "The directory held the group's tooling alongside data from active intrusions into government and critical infrastructure organisations across the region, and the AI agent the operator relied on to run them," CloudSEK
   [said](https://www.cloudsek.com/blog/off-the-rails-inside-an-exposed-silent-lynx-server)
   . "We assess with medium confidence that the operator has a Kazakhstan nexus: the operation runs in Russian, and the operator's own test traffic came from a residential Kazakh connection, which supports existing vendor assessments. The collection priorities, spanning transport, defence correspondence and resource ministries in neighbouring states, point to regional intelligence gathering rather than financial motive."
7. Contractor access fuels ransomware attacks

   [Citrus Ransomware Hackers Abuse Contractor Access, VLESS Tunnels, and AI-Generated Scripts](https://securelist.com/citrus-ransomware/121879/)

   A new Russian-speaking ransomware group called
   [Citrus](https://securelist.com/citrus-ransomware/121879/)
   is targeting Windows systems in corporate environments. The attackers have been found to gain access through compromised contractor accounts and leverage AI-generated PowerShell scripts, batch files, and commands during later stages of the intrusion. In an attempt to reduce visibility, the threat actor removes tools and output files after execution, clears command history, and deletes event logs. The group also disguises tools and related artifacts with benign-looking names to make them appear legitimate by using a trusted brand name. The ransomware is a Sn00py-family ransomware variant written in Go. On Windows systems, the malware encrypts user files and appends the .citrus extension, while taking steps to hinder recovery and incident response. Kaspersky said the activity shares several similarities with
   [Toy Ghouls](https://thehackernews.com/2026/09/three-threat-groups-target-russian.html)
   . "Citrus stands out for the way AI-generated content appears to support hands-on intrusion activity on compromised systems," said Stanislav Larinsky, Kaspersky Security Services expert. "In the cases we investigated, the attackers combined third-party account access, privilege-escalation attempts and domain-wide deployment techniques. These incidents show how limited contractor access can become a path to broader compromise if it is not tightly controlled and continuously monitored."
8. Malicious AI agents exploit OAuth consent

   [New BluePhishing Attack Tricks Microsoft Entra Users Into Granting AI Agents Cloud Access](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)

   Proofpoint has disclosed details of a new technique called BluePhishing that's described as the "next evolution of OAuth consent abuse," enabling bad actors to leverage agent identities like Microsoft Entra Agent ID for initial access. BluePhishing "socially engineer[s] victims into granting consent to a malicious agent blueprint for initial access," it
   [said](https://www.proofpoint.com/us/blog/threat-insight/BluePhishing-Initial-Access-via-Third-Party-Agent-Blueprint-Consent)
   . "Analogous to app consent phishing where attackers use client credentials to gain initial access to a tenant, BluePhishing extends this technique to the agent ecosystem. By exploiting gaps in visibility and governance around emerging AI agent adoption, attackers can abuse one-time consent links to create agent identities in target tenants, obtain access tokens, and operate with the privileges assigned to those agents."
9. AI age checks expand worldwide

   [Meta Expands Teen Account Protections Globally](https://about.fb.com/news/2026/11/expanding-teen-account-protections-to-teens-around-the-world/)

   Meta has announced that it's expanding its AI age-estimation technology globally to automatically place millions of teens in Teen Account protections on Instagram. "We use AI technology to find people we suspect to be teens, even if they use an adult birthday, and place them in Teen Account protections," Meta
   [said](https://about.fb.com/news/2026/11/expanding-teen-account-protections-to-teens-around-the-world/)
   . "As a result, millions more teens across the world who use Instagram will receive these built-in protections, even if they've misrepresented their age." In Australia, Meta has opted to use Apple's age-range signal as another method to help understand age.
10. OAuth support for Exchange migrations

    [Microsoft Supports OAuth Authentication for On-Premises Exchange Mailbox Migrations](https://techcommunity.microsoft.com/blog/exchange/now-available-oauth-authentication-for-on-premises-exchange-mailbox-migrations-t/4571777)

    Microsoft 365 Mailbox Replication Service (MRS) has added support for OAuth as an authentication method when migrating mailboxes between Microsoft 365 and an on-premises Exchange environment. "Once OAuth for MRS is configured, tenant administrators can create an OAuth migration endpoint and use it in migration batches or in onboarding and offboarding move jobs," Microsoft
    [said](https://techcommunity.microsoft.com/blog/exchange/now-available-oauth-authentication-for-on-premises-exchange-mailbox-migrations-t/4571777)
    . "You can use this method in both hybrid and non-hybrid organizations."
11. NTLM signing hardened against relay attacks

    [Microsoft Enables NTLM Signing by Default in Windows to Reduce Relay Attacks](https://support.microsoft.com/en-us/servicing/os/windows/docs/2026/11/kb5135557-ntlm-signing-security-improvements)

    In more Microsoft-related news, the tech giant has incorporated additional protections into Windows starting
    [November 10, 2026,](https://thehackernews.com/2026/11/microsoft-patches-1259-flaws-including.html)
    that address
    [CVE-2026-118737](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-118737)
    (CVSS score: 8.1), a critical remote code execution flaw in Remote Procedure Call Runtime that could allow an unauthorized attacker to execute code over a network. "These updates represent the first phase of improvements to NTLM message signing," Microsoft
    [said](https://support.microsoft.com/en-us/servicing/os/windows/docs/2026/11/kb5135557-ntlm-signing-security-improvements)
    . "These changes help ensure that authenticated NTLM sessions always establish a cryptographic session key and negotiate real message signing, reducing exposure to relay attacks." To that end, Windows servers will begin requiring NTLM signing by default starting May 2027.
12. Exposed cloud credentials lingered 18 months

    [Entra ID Issue Impacting Planning Inspectorate Disclosed](https://control-plane.io/resources/publications/planning-inspectorate-entra-id-security-issue)

    Details have emerged about a now-patched security flaw affecting the Planning Inspectorate, an executive agency of the United Kingdom's Ministry of Housing, Communities and Local Government (MHCLG). The issue involved a complete Microsoft Entra ID application credential that was committed in plaintext to a GitHub repository. "Although removed from the branch, the commit was orphaned via a force push and remained retrievable via GitHub's raw object CDN for 18 months," ControlPlane
    [said](https://control-plane.io/resources/publications/planning-inspectorate-entra-id-security-issue)
    . The client secret was deleted about 20 minutes after responsible disclosure on August 26, 2026.
13. Fake software sites spread infostealer

    [SEO Poisoning Campaign Delivers Armorsteal](https://www.zscaler.com/blogs/security-research/seo-poisoning-campaign-delivers-new-armorsteal-malware)

    An SEO poisoning campaign is using fake websites impersonating the Chocolatey package manager and the Microsoft Activation Scripts (MAS) tool to distribute a Python-based malware called
    [Armorsteal](https://www.seqrite.com/blog/armorsteal-unpacked-breaking-down-a-python-malware-kit-that-steals-data-and-mines-crypto/)
    . "The installer deployed a Python 3.11 runtime environment and three main components providing remote access, surveillance, and information stealing capabilities, with the Python code protected by Pyarmor," Zscaler
    [said](https://www.zscaler.com/blogs/security-research/seo-poisoning-campaign-delivers-new-armorsteal-malware)
    . "The remote access component communicates with a command-and-control (C2) server, downloads additional modules, and executes remote tasks. The surveillance component logs keystrokes, monitors the clipboard, captures screenshots, and displays fake cryptocurrency wallet notifications. The information stealing component targets browser data, Discord tokens, cryptocurrency wallets, seed phrases, saved passwords, SSH keys, and Steam data."
14. Localized phishing delivers banking trojan

    [Grandoreiro Campaign Targets LATAM](https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202611-grandoreiro-targets-latam)

    A new
    [Grandoreiro](https://thehackernews.com/2024/05/grandoreiro-banking-trojan-resurfaces.html)
    banking malware campaign is targeting users across Argentina, Chile, Colombia, Mexico, and Peru through country-specific phishing lures that are tailored to each region. "The campaign uses localized phishing lures, primarily in Spanish, with some observed using Portuguese even when targeting Spanish-speaking countries," Arctic Wolf
    [said](https://github.com/rtkwlf/wolf-tools/tree/main/pack_alerts/202611-grandoreiro-targets-latam)
    . "The phishing chain relies on recently registered domains and layered redirection to hinder detection. The final payload is retrieved through a Domain Generation Algorithm (DGA) seeded with the current date. The downloaded ZIP archive uses a deeply nested folder structure populated with two legitimate PE files and two benign PDF documents. A VBScript file located in the archive's root directory acts as the primary payload, employing junk code and multiple layers of obfuscation before reconstructing and launching a Delphi-based loader." The loader masquerades as a PDF reader and is used to fetch and run the banking trojan.
15. AI search results targeted by scam sites

    [Indirect Prompt Injection Campaign for Investment Scam Sites](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt)

    Palo Alto Networks Unit 42 said it detected an indirect prompt injection (IDPI) campaign across 26 domains. "These are attempting black-hat Generative Engine Optimization (GEO) to game AI-powered search results," Unit 42
    [said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt)
    . "Almost all of the 26 pages have very similar content, presenting as AI-powered digital asset trading platforms. These sites appear to be scam sites designed to collect user information. The injected prompt is set to be hidden from a regular web user but likely visible to an AI agent. These attacks intend to poison SEO and manipulate AI agents to eventually get users to visit these sites."
16. PyPI adds release verification signals

    [PyPI Announces Redesigned Project Pages with New Security Tab](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/#the-new-security-tab)

    The Python Package Index (PyPI) has added a security tab to its project pages, giving developers easy access to security signals. "The new security tab communicates release provenance states and displays per-file attestations, giving you a dedicated place to verify where the release files came from," PyPI
    [said](https://blog.pypi.org/posts/2026-11-06-ui-updates-complete/#the-new-security-tab)
    . "PyPI calculates each release's provenance state by checking whether each release file has an attestation."
17. 100+ domains spread credential stealer

    [REVSTEALER's Growing Distribution Ecosystem](https://akatsukilegion.com/post.php?slug=inside-revstealer-s-growing-distribution-ecosystem)

    The information stealer known as
    [RevStealer](https://thehackernews.com/2026/09/weekly-recap-chrome-0-day-router.html#:~:text=RevStealer%20Spreads%20via%20Game%20Cheats%20and%20Fake%20Claude%20Desktop%20App)
    is being propagated as part of an "industrial-scale, financially motivated campaign" that uses game cheats and AI tools as lures. The payload is distributed through more than 100 interconnected domains, trojanized Electron applications masquerading as Anthropic's Claude Opus 5, and hijacked YouTube distribution channels, per Akatsuki Legion. "Once executed, the malware performs a ten-point weighted sandbox-evasion scoring routine, decrypts an AES-256-CBC in-memory payload, and leverages fourteen indirect syscall wrappers and FNV-1a API hashing to bypass user-mode hooks before systematically harvesting credentials from browsers, password managers, cryptocurrency wallets, Steam, Roblox, Battle.net, EA Desktop, and Minecraft; then exfiltrating the loot as streamed, encrypted typed records over HTTPS, with a resilient Polygon blockchain dead-drop resolver standing by as a fallback command-and-control channel," the independent adversary research group
    [said](https://akatsukilegion.com/post.php?slug=inside-revstealer-s-growing-distribution-ecosystem)
    .
18. AI infrastructure becomes an attack target

    [Threat Actors Target AI Infrastructure](https://www.sekoia.com/blog/a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure)

    Threat actors have increasingly targeted AI orchestration platforms over the past few months, according to Sekoia. This is because "they concentrate API keys, enterprise data, and access to external tools," it
    [added](https://www.sekoia.com/blog/a-honeypots-tale-deconstructing-an-attack-on-genai-infrastructure)
    . This includes Flowise, which has been affected by multiple security flaws like CVE-2025-59528 and CVE-2026-41264. In one exploitation attempt recorded in August 2026, a suspected Chinese-speaking actor abused legitimate Flowise functionality to conduct automated reconnaissance and attempted to hijack the LLM agent to serve as an offensive analysis vector against external targets. "The attacker attempted to turn the AI agent into an interactive offensive assistant, submitting real-world reconnaissance data (Nightingale/Redis infrastructure) to generate custom exploitation playbooks and target analysis," Sekoia said.
19. AI-built phishing kits multiply

    [Vibe-Coded Phishing Kits Emerge](https://www.levelblue.com/blogs/spiderlabs-blog/blackapex-spy-and-counting-the-emerging-wave-of-vibe-coded-phishing-kits)

    LevelBlue has disclosed details of a family of phishing kits named BlackApex, DarkApex, SPY, XXX101-TOKEN, OGPARKER1, W1-TOKEN, and ALIBOBO-TOKEN that are used to facilitate
    [device code phishing](https://thehackernews.com/2026/09/microsoft-takes-down-eviltokens-device.html)
    attacks using shared document lures. The findings once again demonstrate how AI can speed up the development of a convincing multi-brand phishing kit. "Across all of its lures, the source shows traits we associate with AI-generated code, whether from direct prompts to a language model or from a person working alongside an AI coding assistant," LevelBlue
    [said](https://www.levelblue.com/blogs/spiderlabs-blog/blackapex-spy-and-counting-the-emerging-wave-of-vibe-coded-phishing-kits)
    . "The code, endpoints, and interface are the same across all of them. We cannot say whether these names reflect separate operators, resellers or customers of a single kit, but the pattern is consistent with a shared product being rebranded and redeployed."
20. AI verifies Signal security properties

    [DeepMind's AlphaProof Code Proves the Signal Protocol Is Secure](https://google-deepmind.github.io/code-verification/)

    Google's DeepMind has introduced
    [AlphaProof Code](https://deepmind.google/blog/introducing-alphaproof-code/)
    , which brings together human experts and AI agents to verify software and mathematically demonstrate that it works as intended. The multi-agent AI framework has been used to
    [prove key security properties of libsignal](https://www.wired.com/story/a-new-ai-tool-from-google-deepmind-formally-verified-the-signal-protocol/)
    , the Signal protocol's reference implementation, at the machine-code level. "AlphaProof Code consists of a human-guided agent for writing Lean specifications of code, a formal semantics of AArch64 machine code, and a team of autonomous prover agents whose proofs are accepted only if Lean’s kernel checks them against the approved specification," DeepMind
    [said](https://google-deepmind.github.io/code-verification/)
    . "Applied to libsignal, our agents generated about 6.5 million lines of machine-checked Lean proof code, resting on about 26,000 lines of trusted specifications and AArch64 semantics. The proofs cover Signal’s post-quantum PQXDH handshake and Triple Ratchet, establishing forward secrecy, authentication, post-compromise security, and handshake secrecy."

    [![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf3gyWCahnpbLHFuZkj6sS6mi7qDAxBnGn3B46dO5cAqTcQAhWqIhb7HEQJMpFyWw37hn_VfDafzmVGjjq5Q0EA9XEKrd2J9-HzZQ_j9ESOqo2lblXazjsWLJAjPwgQCNpfYmlQM-c-5_uwQy11qSbHbrf5J9KIX0AM63gImcuRaqp18XBQfGSV8I3slhn/s1600/nn.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgf3gyWCahnpbLHFuZkj6sS6mi7qDAxBnGn3B46dO5cAqTcQAhWqIhb7HEQJMpFyWw37hn_VfDafzmVGjjq5Q0EA9XEKrd2J9-HzZQ_j9ESOqo2lblXazjsWLJAjPwgQCNpfYmlQM-c-5_uwQy11qSbHbrf5J9KIX0AM63gImcuRaqp18XBQfGSV8I3slhn/s1600/nn.jpg)

That's the lot for this week. Some attacks were carefully planned. Others relied on old mistakes, trusted accounts, or someone clicking the wrong thing. AI is showing up on both sides, making attacks easier to build while helping researchers find problems faster. The tools keep changing, but attackers still seem happy to use whatever works.

The good news is that some of these threats are being stopped, and defenses are slowly catching up. The bad news is that fixing a bug, removing a file, or blocking an attacker doesn't always mean the problem is gone. Sometimes the damage sticks around longer than anyone expects. Worth keeping in mind before the next batch of headlines arrives.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.