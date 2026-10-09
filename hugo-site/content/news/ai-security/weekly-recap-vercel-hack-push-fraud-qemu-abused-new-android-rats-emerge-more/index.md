---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-20T16:15:14.250780+00:00'
exported_at: '2026-04-20T16:15:16.708415+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html
structured_data:
  about: []
  author: ''
  description: Monday cybersecurity recap on evolving threats, trusted tool abuse,
    stealthy in-memory attacks, and shifting access patterns.
  headline: '⚡ Weekly Recap: Vercel Hack, Push Fraud, QEMU Abused, New Android RATs
    Emerge & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/weekly-recap-vercel-hack-push-fraud.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: Vercel Hack, Push Fraud, QEMU Abused, New Android RATs Emerge
  & More'
updated_at: '2026-04-20T16:15:14.250780+00:00'
url_hash: c74a7b343e3b729299adc9223b6f215f7fccf221
---

**

Ravie Lakshmanan
**

Apr 20, 2026

Cybersecurity / Hacking

Monday’s recap shows the same pattern in different places. A third-party tool becomes a way in, then leads to internal access. A trusted download path is briefly swapped to deliver malware. Browser extensions act normally while pulling data and running code. Even update channels are used to push payloads. It’s not breaking systems—it’s bending trust.

There’s also a shift in how attacks run. Slower check-ins, multi-stage payloads, andmore code kept in memory. Attackers lean on real tools and normal workflows instead of custom builds. Some cases hint at supply-chain spread, where one weak link reaches further than expected.

Go through the whole recap. The pattern across access, execution, and control only shows up when you see it all together.

## **⚡ Threat of the Week**

**[Vercel Discloses Data Breach](https://thehackernews.com/2026/04/vercel-breach-tied-to-context-ai-hack.html)**
—Web infrastructure provider Vercel has disclosed a security breach that allows bad actors to gain unauthorized access to "certain" internal Vercel systems. The incident originated from the compromise of Context.ai, a third-party artificial intelligence (AI) tool, which was used by an employee at the company, it added. "The attacker used that access to take over the employee's Vercel Google Workspace account, which enabled them to gain access to some Vercel environments and environment variables that were not marked as 'sensitive,'" the company said. It's currently not known who is behind the incident, but a threat actor using the ShinyHunters persona has claimed responsibility for the hack. Context.ai also disclosed a March 2026 incident involving unauthorized access to its AWS environment. However, it has since emerged that the attacker also likely compromised OAuth tokens for some of its consumer users. Furthermore, Hudson Rock uncovered that a Context.ai employee was compromised with Lumma Stealer in February 2026, raising the possibility that the infection may have triggered the "supply chain escalation."

## **🔔 Top News**

* **[Law Enforcement Operation Brings Down DDoS-for-Hire Operation](https://thehackernews.com/2026/04/operation-poweroff-seizes-53-ddos.html)**
  —Law enforcement agencies across Europe, the U.S., and other partner nations cracked down on the commercial DDoS-for-hire ecosystem, targeting both operators and customers of services used to target websites and knock them offline. As part of the effort, authorities took down 53 domains, arrested four people, and sent warning notifications to thousands of criminal users. The U.S. Justice Department said court-authorized actions were undertaken to disrupt Vac Stresser and Mythical Stress. The actions are a persistent cat-and-mouse game, as booted services often reappear under new names and domains despite repeated takedowns. While these disruptions tend to have short-term results, the resilience of the criminal activity indicates that arrests need to be combined with infrastructure seizures, financial disruption, and user deterrence for lasting impact.
* **[Newly Discovered PowMix Botnet Hits Czech Workers](https://thehackernews.com/2026/04/newly-discovered-powmix-botnet-hits.html)**
  —An active malicious campaign is targeting the workforce in the Czech Republic with a previously undocumented botnet dubbed PowMix since at least December 2025. "PowMix employs randomized command-and-control (C2) beaconing intervals, rather than persistent connection to the C2 server, to evade the network signature detections," Cisco Talos said. The never-before-seen botnet is designed to facilitate remote access, reconnaissance, and remote code execution, while establishing persistence by means of a scheduled task. At the same time, it verifies the process tree to ensure that another instance of the same malware is not running on the compromised host.
* **[AI-Driven Pushpaganda Exploits Google Discover to for Ad Fraud](https://thehackernews.com/2026/04/ai-driven-pushpaganda-scam-exploits.html)**
  —A novel ad fraud scheme has been found to leverage search engine poisoning (SEO) techniques and artificial intelligence (AI)-generated content to push deceptive news stories into Google's Discover feed and trick users into enabling persistent browser notifications that lead to scareware and financial scams. The Pushpaganda campaign has been found to target the personalized content feeds of Android and Chrome users. "This operation, named for push notifications central to the scheme, generates invalid organic traffic from real mobile devices by tricking users into subscribing to enabling notifications that presented alarming messages," HUMAN Security said. Google has since rolled out fixes and algorithmic updates to address the issue.
* **[Obsidian Plugin Abuse Delivers PHANTOMPULSE RAT](https://thehackernews.com/2026/04/obsidian-plugin-abuse-delivers.html)**
  —A social engineering campaign has abused Obsidian, a cross-platform note-taking application, as an initial access vector to distribute a previously undocumented Windows remote access trojan called PHANTOMPULSE in attacks targeting individuals in the financial and cryptocurrency sectors. Elastic Security Labs is tracking the activity under the name REF6598. It employs elaborate social engineering tactics through LinkedIn and Telegram to breach both Windows and macOS systems by tricking victims into opening a cloud-hosted vault in Obsidian. PHANTOMPULSE is an artificial intelligence (AI)-generated backdoor that uses the Ethereum blockchain for resolving its C2 server. On macOS, the attack is used to deliver an unspecified payload.
* **[CPUID Downloads Hijacked to Serve STX RAT](https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html)**
  —Unknown threat actors
  [hijacked](https://gist.github.com/N3mes1s/b5b0b96782b9f832819d2db7c6684f84)
  the official CPUID download page to serve trojanized installers that ultimately led to the deployment of STX RAT, a remote access trojan with infostealer capabilities. The attack did not compromise CPUID's original signed binaries, the threat actors served their own trojanized packages via redirect. "The threat actor compromised the official CPUID download page to serve a trojanized package, employing DLL sideloading as the initial execution vector followed by a layered, five-stage in-memory unpacking chain designed to evade detection," Cyderes
  [said](https://www.cyderes.com/howler-cell/how-cpuids-hwmonitor-supply-chain-was-hijacked-to-deploy-stx-rat)
  . "The use of a timestomped compilation timestamp, reflective PE loading, and exclusively in-memory payload execution demonstrates a deliberate effort to hinder forensic analysis and bypass traditional security controls."
* **[108 Malicious Chrome Extensions Steal Google and Telegram Data](https://thehackernews.com/2026/04/108-malicious-chrome-extensions-steal.html)**
  —A cluster of 108 Google Chrome extensions has been found to communicate with the same command-and-control (C2) infrastructure with the goal of collecting user data and enabling browser-level abuse by injecting ads and arbitrary JavaScript code into every web page visited. The extensions provide the expected functionality to avoid raising red flags, but malicious code running in the background connects to the threat actor's C2 server to perform the nefarious activities. At the center of the campaign is a backend hosted on a Contabo virtual private server (VPS), with multiple subdomains handling session hijacking, identity collection, command execution, and monetization operations. There is evidence indicating a Russian malware-as-a-service (MaaS) operation, based on the presence of a payment and monetization portal in its C2 infrastructure.
* **[OpenAI Launches GPT-5.4-Cyber](https://thehackernews.com/2026/04/openai-launches-gpt-54-cyber-with.html)**
  —OpenAI announced a new model, GPT-5.4-Cyber, specifically designed for use by digital defenders. Artificial intelligence (AI) companies have repeatedly warned that more capable AI models could create an opening for bad actors to exploit vulnerabilities and security gaps in software with new speed and intensity. Unlike Anthropic, which said its new Claude Mythos model is only being privately released to a small number of trusted organizations due to concerns that it could be exploited by adversaries, OpenAI said "the class of safeguards in use today sufficiently reduce cyber risk enough to support broad deployment of current models," but hinted at the need for more advanced protections in the long term. Defending critical software has long depended on the ability to find and fix vulnerabilities faster than attackers can exploit them. GPT-5.4-Cyber has a lower refusal boundary for legitimate cybersecurity work than standard GPT-5.4. It adds capabilities aimed at advanced defensive workflows, including binary reverse engineering. "We don't think it's practical or appropriate to centrally decide who gets to defend themselves," OpenAI stated. "Instead, we aim to enable as many legitimate defenders as possible, with access grounded in verification, trust signals, and accountability." The use of AI for vulnerability discovery and analysis means that the barrier to entry for attackers is collapsing. Bad actors could ask an AI model to analyze differences between two versions of a binary and generate an exploit at a faster rate. Rob T. Lee, chief of research at the SANS Institute,
  [said](https://x.com/robtlee/status/2044241744296820786)
  the debut of Mythos and GPT-5.4-Cyber is "nothing more than one vendor trying to one-up another," adding, "We need to start benchmarking how one AI model is able to find code vulnerabilities over another and how quickly they are doing it. There are real risks at stake here." At the same time, researchers from
  [AISLE](https://aisle.com/blog/system-over-model-zero-day-discovery-at-the-jagged-frontier)
  and
  [Xint](https://go.xint.io/xint-mythos-appsec-findings-report)
  found that it's possible to replicate Mythos's results with smaller, cheaper models. "The critical variable in AI vulnerability discovery is not the model alone," Xint said. "It is the structured system that decides where to look, validates that findings are real and exploitable, eliminates false positives, and delivers actionable remediation."

## **🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first —
[CVE-2026-20184](https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html)
(Cisco Webex Services),
[CVE-2026-20147](https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html)
(Cisco Identity Services Engine and ISE Passive Identity Connector),
[CVE-2026-20180, CVE-2026-20186](https://thehackernews.com/2026/04/cisco-patches-four-critical-identity.html)
(Cisco Identity Services Engine),
[CVE-2026-33032](https://thehackernews.com/2026/04/critical-nginx-ui-vulnerability-cve.html)
(nginx-ui),
[CVE-2026-32201](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html)
(Microsoft SharePoint Server),
[CVE-2026-27304](https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html)
(Adobe ColdFusion),
[CVE-2026-39813, CVE-2026-39808](https://thehackernews.com/2026/04/april-patch-tuesday-fixes-critical.html)
(Fortinet FortiSandbox),
[CVE-2026-40176, CVE-2026-40261](https://thehackernews.com/2026/04/new-php-composer-flaws-enable-arbitrary.html)
(Composer),
[CVE-2025-0520](https://thehackernews.com/2026/04/showdoc-rce-flaw-cve-2025-0520-actively.html)
(ShowDoc),
[CVE-2026-22039](https://github.com/kyverno/kyverno/security/advisories/GHSA-8p9x-46gm-qfx2)
(
[Kyverno](https://orca.security/resources/blog/kyverno-ssrf-vulnerability-cve-2026-4789/)
),
[CVE-2026-27681](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/april-2026.html)
(SAP Business Planning and Consolidation and Business Warehouse),
[CVE-2026-34486](https://www.striga.ai/research/tomcat-tribes-unauth-rce)
,
[CVE-2026-29146](https://lists.apache.org/thread/9510k5p5zdvt9pkkgtyp85mvwxo2qrly)
(Apache Tomcat),
[CVE-2026-40175](https://www.aikido.dev/blog/axios-cve-2026-40175-a-critical-bug-thats-not-exploitable)
(Axios),
[CVE-2026-32196](https://cymulate.com/blog/cve-2026-32196-one-click-rce-windows-admin-center/)
(Microsoft Windows Admin Center),
[CVE-2026-20204](https://advisory.splunk.com/advisories/SVD-2026-0403)
(Splunk Enterprise),
[CVE-2026-20205](https://advisory.splunk.com/advisories/SVD-2026-0407)
(Splunk MCP Server)
[CVE-2026-6296, CVE-2026-6297, CVE-2026-6298, CVE-2026-6299, CVE-2026-6358](https://chromereleases.googleblog.com/2026/04/stable-channel-update-for-desktop_15.html)
,
[CVE-2026-5873](https://www.hacktron.ai/blog/i-let-claude-opus-to-write-me-a-chrome-exploit)
(Google Chrome),
[CVE-2026-34078](https://tails.net/news/version_7.6.2/)
(Tails),
[CVE-2026-34622](https://helpx.adobe.com/security/products/acrobat/apsb26-44.html)
(Adobe Acrobat Reader),
[CVE-2026-33413](https://www.strix.ai/blog/where-others-missed-it-etcd-auth-bypass)
(etcd),
[CVE-2026-1492](https://www.cyfirma.com/research/cve-2026-1492-wordpress-user-registration-membership-authentication-bypass-flaw/)
(User Registration & Membership plugin),
[CVE-2026-23818](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05032en_us&docLocale=en_US)
(HPE Aruba Networking Private 5G Core On-Prem),
[CVE-2025-54236](https://oasis-security.io/blog/260128-Magento-CVE)
(Magento),
[CVE-2026-26980](https://github.com/TryGhost/Ghost/security/advisories/GHSA-w52v-v783-gw97)
(Ghost CMS),
[CVE-2026-40478](https://github.com/advisories/GHSA-xjw8-8c5c-9r79)
(
[Thymeleaf](https://www.endorlabs.com/learn/its-about-thyme-how-a-whitespace-character-broke-thymeleafs-expression-sandbox-cve-2026-40478)
),
[CVE-2026-41242](https://github.com/protobufjs/protobuf.js/security/advisories/GHSA-xq3m-2v4x-88gg)
(
[protobufjs](https://www.endorlabs.com/learn/the-dangers-of-reusing-protobuf-definitions-critical-code-execution-in-protobuf-js-ghsa-xq3m-2v4x-88gg)
),
[CVE-2026-40871](https://github.com/mailcow/mailcow-dockerized/security/advisories/GHSA-r8fq-wrfm-cj2q)
(
[Mailcow](https://github.com/lukehebe/Vulnerability-Disclosures/blob/main/CVE-2026-40871.md)
),
[CVE-2026-5747](https://aws.amazon.com/security/security-bulletins/2026-015-aws/)
(AWS Firecracker), and
[CVE-2025-50892](https://medium.com/workday-engineering/leveraging-raw-disk-reads-to-bypass-edr-f145838b0e6d)
(eudskacs.sys).

## **🎥 Cybersecurity Webinars**

* [The Force Awakens in AppSec: Rethinking Mythos & Organizational Defenses at AI Speed](https://thehacker.news/state-of-ai-security?source=recap)
  → This webinar explores how AI-powered hacking is making traditional security patching too slow to be effective. It focuses on the "patch gap"— the dangerous time between a bug being found and fixed—and offers a new way to prioritize vulnerabilities based on real-world risk. The session provides practical strategies for security leaders to defend against automated, high-speed attacks.
* [The Rise of the Agent: Moving to Autonomous Exposure Validation](https://thehacker.news/agentic-exposure-validation?source=recap)
  → This webinar explores how "agentic" AI is changing security testing by using autonomous AI agents to simulate real-world attacks. Unlike traditional scanners, these tools continuously find and validate which security gaps are actually reachable by hackers. The session focuses on moving from slow, manual checks to automated exposure validation to stay ahead of AI-driven threats.

## **📰 Around the Cyber World**

* **Vect Partners with BreachForums and TeamPCP**
  —Dataminr revealed that the Vect ransomware group has formalized partnerships with the BreachForums cybercrime marketplace and TeamPCP hacking group. The partnership will allow BreachForums members to deploy ransomware and will use the victims of
  [TeamPCP's supply chain attacks](https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html)
  to attack organizations that are in a vulnerable state. "Between the two partnerships, Vect will lower the barrier to entry for ransomware actors, incentivize group members to carry out attacks, and exploit pre-existing breaches to broaden impact," the company
  [said](https://www.dataminr.com/resources/intel-brief/vect-breachforums-teampcp-converge-in-unprecedented-affiliate-mobilizatio/)
  . "The convergence of large-scale supply chain credential theft, a maturing RaaS operation, and mass dark web forum mobilization represents an unprecedented model of industrialized ransomware deployment."
* **MuddyWater Targets Global Organizations via Microsoft Teams**
  —The Iranian hacking group known as MuddyWater has been observed using targeted social engineering to approach targets via Microsoft Teams by masquerading as IT support staff to trick them into running a botnet malware called
  [Tsundere](https://thehackernews.com/2026/04/iran-linked-hackers-disrupt-us-critical.html)
  (aka Dindoor). "A notable aspect of this intrusion was the abuse of Deno, a legitimate JavaScript and TypeScript runtime typically used for backend application development," CyberProof
  [said](https://www.cyberproof.com/blog/iranian-apt-seedworm-targets-global-organizations-via-microsoft-teams/)
  . "The attacker leveraged deno.exe to execute a highly obfuscated, Base64‑encoded payload -- tracked as DINODANCE -- directly in memory, minimizing on-disk artifacts and complicating detection." Once decoded, the malware establishes C2 communications with a remote server, exfiltrating basic host metadata such as username, hostname, and operating system details.
* **Multi-Stage Intrusion Drops Direct-Sys Loader and CGrabber Stealer**
  —An attack chain involving ZIP archives distributed through GitHub user attachment URLs is abusing DLL side-loading to deliver a malware loader called Direct-Sys Loader, which performs anti-analysis checks and then drops CGrabber. The malware, for its part, avoids infecting machines running in the Commonwealth of Independent States (CIS) countries and collects browser credentials, crypto wallet data, password manager data, and a broad range of application artifacts. "By skipping execution on machines in those regions, they reduce the risk of attracting attention from local law enforcement and avoid targeting their own infrastructure or allies," Cyderes
  [said](https://www.cyderes.com/howler-cell/direct-sys-loader-cgrabber-stealer-five-stage-malware-chain)
  . "The Direct-Sys Loader and CGrabber Stealer represent a cohesive, multi-stage, stealth-focused malware ecosystem engineered with advanced detection-evasion capabilities."
* **Russian Hackers Target Ukrainian Agencies**
  —Threat actors linked to Russia broke into more than 170 email accounts belonging to prosecutors and investigators across Ukraine in recent months," Reuters
  [reported](https://www.reuters.com/world/russia-linked-hackers-compromised-scores-ukrainian-prosecutors-email-accounts-2026-04-15/)
  , citing data from
  [Ctrl-Alt-Intel](https://ctrlaltintel.com/research/FancyBear/)
  . The espionage activity also targeted officials in Romania, Greece, Bulgaria, and Serbia. Speaking to The Record, Ukraine's State Service of Special Communications and Information Protection (SSSCIP)
  [confirmed](https://therecord.media/ukraine-confirms-suspected-apt28-campaign-targeting-prosecutors)
  that local government agencies were targeted in a long-running hacking campaign that it has been tracking since 2023, with the attacks weaponizing flaws in
  [Roundcube webmail software](https://thehackernews.com/2025/05/russia-linked-apt28-exploited-mdaemon.html)
  to run malicious code as soon as a specially crafted message is opened. The campaign is believed to be the work of
  [APT28](https://thehackernews.com/2026/04/russian-state-linked-apt28-exploits.html)
  (aka Fancy Bear).
* **Infostealer Lookup Services are Changing Cybercrime**
  —Hudson Rock revealed that infostealer lookup services, some accessible via a simple search on Google, are rapidly fueling a new era of initial access, shifting how cyber attacks begin and transforming a complex hacking process into a simple, automated transaction. "These platforms have effectively turned billions of compromised credentials and active session cookies into a highly searchable, low-cost commodity available to the masses," it
  [said](https://www.infostealers.com/article/the-new-era-of-initial-access-how-infostealer-lookup-services-are-changing-cybercrime/)
  . "Because this data is so easily accessible, organizations can no longer afford to be reactive."
* **AdaptixC2 Detailed**
  —Kaspersky has detailed the inner workings of an open-source command-and-control (C2) framework known as AdaptixC2, which has seen increased adoption by bad actors over the past year. Written in Go and C++, AdaptixC2 is designed for post-exploitation and stealthy interaction with its malicious agents deployed on compromised systems. It also employs diverse network communication and post-exploitation techniques to get around traffic monitoring tools and minimize its footprint. "Unlike many general-purpose C2 platforms, AdaptixC2 focuses on advanced agent-to-C2 communication and specific evasion techniques designed to bypass modern security tools, including EDR and NDR solutions," the company
  [said](https://securelist.com/tr/adaptixc2-network-and-host-detection/119424/)
  . "The framework provides the flexibility to develop custom agents while also including standard agent implementations in Go and C++ for Windows, macOS, and Linux. Additionally, it supports a modular approach to extending its functionality."
* **Adware Update Delivers EDR Killer**
  —In an unusual attack, a browser-hijacking adware family rolled out a multi-phase update that attempted to disable security software on infected hosts. The adware is signed by Dragon Boss Solutions LLC, a U.A.E.-based company that claims to conduct search monetization research and has promoted modified versions of the Chrome browser (e.g., Chromstera, Chromnius, and Artificius). "The signed software silently fetches and executes payloads capable of killing antivirus products, all while running with SYSTEM privileges," Huntress
  [said](https://www.huntress.com/blog/pups-grow-fangs)
  . The antivirus killing capability was observed starting in late March 2025, although the loader and updater components date back to late 2024. "The operation uses an off-the-shelf software update mechanism to deploy these MSI and PowerShell-based payloads. Establishing WMI persistence disables security applications and blocks reinstallation of protective software," it added. The MSI installer, downloaded from a fallback update server, performs reconnaissance, queries for installed security products, and runs a PowerShell script ("ClockRemoval.ps1") to terminate running processes, disable antivirus services by tampering with the Windows Registry, delete installation directories, and force deletion when uninstallers fail. What's significant is that the update mechanism can be modified to deploy any payload. To make matters worse, the primary update domain baked into the operation to retrieve the MSI installer – chromsterabrowser[.]com – was left unregistered, meaning any threat actor could have registered the domain for as little as $10 and push malicious updates, turning an adware infection into a potential supply chain compromise. The domain has since been sinkholed. That said, 23,565 unique IP addresses connected to the sinkhole during a 24-hour monitoring period. The infections are concentrated around the U.S., France, Canada, the U.K., and Germany. These included universities, OT networks, government entities, primary and secondary educational institutions, healthcare organizations, and multiple Fortune 500 companies.
* **India Will Not Require Smartphone Makers to Preload Aadhaar App**
  —The Indian government will no longer require smartphone makers like Apple and Samsung to preload devices with a state-owned biometric identification app, Reuters
  [reported](https://www.reuters.com/world/china/india-drops-proposal-mandate-national-id-app-aadhaar-smartphones-after-pushback-2026-04-17/)
  . India's IT ministry reviewed the proposal and "is not in favour of mandating the pre-installation of the Aadhaar App on smartphones," UIDAI said in a statement. The Aadhaar request was the sixth time in two years the government has sought pre-installation of state apps on phones, according to industry communications. Smartphone makers flagged concerns about device security and compatibility when they received the Aadhaar preload proposal, and also flagged higher production costs as they ‌would have ⁠been required to run separate manufacturing lines for India and export markets.
* **SQL Injection Campaign Targets Payment Services**
  —An active
  [SQL injection campaign](https://oasis-security.io/blog/260304-SQLi)
  is operating through attacker infrastructure located in Canada. The campaign has targeted 35 websites, with confirmed successful SQL injection exploitation and data exfiltration affecting three organizations operating in the payment, real estate, and developer service sectors. Attacker-side artifacts indicate coordinated and deliberate exploitation rather than opportunistic scanning.
* **QEMU Abused for Defense Evasion**
  —Threat actors are abusing
  [QEMU](https://thehackernews.com/2024/03/cybercriminals-utilize-qemu-emulator-as.html)
  , an open-source machine emulator and virtualizer, to hide malicious activity within virtualized environments. "Attackers are drawn to QEMU and more common hypervisor-based virtualization tools like Hyper-V, VirtualBox, and VMware because malicious activity within a virtual machine (VM) is essentially invisible to endpoint security controls and leaves little forensic evidence on the host itself," Sophos
  [said](https://www.sophos.com/en-us/blog/qemu-abused-to-evade-detection-and-enable-ransomware-delivery)
  . Two clusters of activity have been detected: STAC4713, which has used QEMU as a covert reverse SSH backdoor to deliver tooling and harvest domain credentials with the end goal of likely deploying
  [Payouts King ransomware](https://www.zscaler.com/blogs/security-research/payouts-king-takes-aim-ransomware-throne)
  (likely tied to former BlackBasta affiliates) after obtaining initial access via exploitation of known security flaws in SolarWinds Web Help Desk, and STAC3725, which exploits Citrix Bleed 2 (aka CVE-2025-5777) for obtaining a foothold and installs ScreenConnect for persistent remote access. The threat actors then deploy a QEMU VM to install additional tools for conducting enumeration and credential theft. "Follow-on activity differed across intrusions, suggesting that initial access brokers originally compromised the victims’ environments and then sold the access to other threat actors," Sophos said.
* **Fake Adobe Reader Site Drops ScreenConnect**
  —Threat actors are using fake Adobe Acrobat Reader website lures to lure victims into installing ConnectWise's ScreenConnect. The attack chain was detected in February 2026. "The attack uses .NET reflection to keep payloads in memory only, which helps it evade signature-based defenses and hinder forensic examination," Zscaler ThreatLabz
  [said](https://www.zscaler.com/blogs/security-research/memory-loader-drops-screenconnect)
  . "A VBScript loader dynamically reconstructs strings and objects at runtime to defeat static analysis and sandboxing. Auto-elevated Component Object Model (COM) objects are abused to bypass User Account Control (UAC) and run with elevated privileges without user prompts." The attack employs an in-memory .NET loader that's responsible for launching ScreenConnect.
* **Nearly 6M Hosts Use FTP**
  —Censys
  [said](https://censys.com/blog/ftp-exposure-brief/)
  it observed about 5,949,954 hosts running at least one internet-facing FTP service, down from over 10.1 million in 2024, which amounts to a decline of 40% in two years. Of these, nearly 2.45 million hosts had no evidence of encryption. "Over 150,000 IIS FTP services return a 534 response, indicating TLS was never set up," Censys said. "For most use cases, FTP can be replaced without significant disruption. If FTP must remain, enabling Explicit TLS is a configuration change, not a protocol upgrade, and both Pure-FTPd and vsftpd support it natively."
* **Malformed APKs Bypass Detections as New Android RATs Emerge**
  —Threat actors are
  [increasingly](https://www.cleafy.com/cleafy-labs/malformed-apks-as-an-anti-analysis-technique-malfixer-tool)
  using
  [malformed APKs](https://zimperium.com/blog/over-3000-android-malware-samples-using-multiple-techniques-to-bypass-detection)
  , which refer to Android packages that can be installed and run on Android but are intentionally broken by using unsupported compression methods, header manipulation, or false password protection, to bypass static analysis tools and delay detection. Cleafy has released an open-source tool called
  [Malfixer](https://github.com/Cleafy/Malfixer)
  to detect and fix malformed APKs. The development comes as Zimperium
  [flagged](https://zimperium.com/blog/android-bankers-4-campaigns-in-a-row)
  four new Android malware families, RecruitRat, SaferRat,
  [Astrinox](https://thehackernews.com/2026/04/mirax-android-rat-turns-devices-into.html)
  (aka Mirax), and
  [Massiv](https://thehackernews.com/2026/02/fake-iptv-apps-spread-massiv-android.html)
  , that are capable of harvesting sensitive information and facilitating unauthorized financial transactions. In all, campaigns distributing these malware families target over 800 applications across the banking, cryptocurrency, and social media sectors. RecruitRat leverages recruitment-related social engineering and fraudulent job-seeking platforms for initial access. SaferRat is distributed through fake websites that claim to offer free access to premium streaming platforms and legitimate video streaming software. All four banking trojans abuse the native Session Installation API to bypass Android's sideloading restrictions and request accessibility services permissions to carry out their malicious activities.
* **Over 200 PrestaShop Stores Expose Installer**
  —More than 200 PrestaShop online stores have left their installation folder exposed online, allowing attackers to abuse the behavior to overwrite database configuration, gain admin access, and execute arbitrary code on the server. According to
  [Sansec](https://sansec.io/research/prestashop-installer-takeover)
  , the affected stores span 27 countries, including France, Italy, Poland, and the Czech Republic. Another set of 15 stores has been found to expose the Symfony Profiler, which is enabled when PrestaShop runs in debug mode.
* **How to Contain a Domain Compromise via Predictive Shielding**
  —Microsoft
  [detailed](https://www.microsoft.com/en-us/security/blog/2026/04/17/domain-compromise-predictive-shielding-shut-down-lateral-movement/)
  an attack chain in which a threat actor targeted a public sector organization in June 2025, methodically progressing from one state of the attack lifecycle to the next, starting with dropping a web shell following the exploitation of a file-upload flaw in an internet-facing Internet Information Services (IIS) server. The attacker then performed reconnaissance, escalated their privileges, leveraged the compromised IIS service account to reset the passwords of high-impact identities, and deployed Mimikatz to harvest credentials. Then, the threat actor abused privileged accounts and remotely created a scheduled task on a domain controller to capture NTDS snapshots. The attacker also planted a Godzilla web shell on the Exchange Server and leveraged their privileged context to alter mailbox permissions, allowing them to read and manipulate all mailbox contents. The threat actor subsequently used Impacket to enumerate the role assignments and other activities that were flagged and blocked by Microsoft Defender. "The threat actor then launched a broad password spray from the initially compromised IIS server, unlocking access to at least 14 servers through password reuse," Microsoft said. "They also attempted remote credential dumping against a couple of domain controllers and an additional IIS server using multiple domain and service principals." After Microsoft Defender's
  [predictive shielding](https://learn.microsoft.com/en-us/defender-xdr/shield-predict-threats)
  was enabled in late July 2025, the attacker's attempts to sign in to Microsoft Entra Connect servers were blocked. The campaign stopped on July 28, 2025.
* **Cargo Theft Malware Actor Conducts Remote Access Campaigns**
  —In November 2025, Proofpoint
  [detailed](https://thehackernews.com/2025/11/cybercriminals-exploit-remote.html)
  a threat actor that used compromised load boards to gain access to trucking companies with the end goal of freight diversion and cargo theft. New research from the enterprise security company has revealed that the attacker abused multiple remote access tools like ScreenConnect, Pulseway, and SimpleHelp to establish persistence to a controlled decoy environment, with attempts made to identify financial access, payment platforms, and cryptocurrency assets to conduct freight fraud and broader financial theft. The actor maintained access for more than a month. At least one ScreenConnect instance is said to have leveraged a third‑party signing‑as‑a‑service provider to re-sign the installer with a valid but fraudulent code‑signing certificate. "This reconnaissance focused on identifying financial access – such as banking, accounting, tax software, and money transfer services – as well as transportation‑related entities, including fuel card services, fleet payment platforms, and load board operators," the company
  [said](https://www.proofpoint.com/us/blog/threat-insight/beyond-breach-inside-cargo-theft-actors-post-compromise-playbook)
  . "The latter activity was likely designed to support crimes against the transportation industry, including cargo theft and related financial fraud."
* **British National Pleads Guilty to Scattered Spider Campaign**
  —Tyler Robert Buchanan, who was
  [extradited](https://thehackernews.com/2025/08/scattered-spider-hacker-gets-10-years.html)
  from Spain to the U.S. last April following his arrest in the European nation in June 2024, pleaded guilty to hacking a dozen companies and stealing at least $8 million in digital assets. He pleaded guilty to one count of conspiracy to commit wire fraud and one count of aggravated identity theft. "From September 2021 to April 2023, Buchanan and other individuals conspired to conduct cyber intrusions and virtual currency thefts," the U.S. Justice Department
  [said](https://www.justice.gov/usao-cdca/pr/british-national-pleads-guilty-hacking-companies-and-stealing-least-8-million-virtual)
  . "The victims and intended victims included interactive entertainment companies, telecommunications companies, technology companies, business process outsourcing (BPO) and information technology (IT) suppliers, cloud communications providers, virtual currency companies, and individuals." Buchanan and his co-conspirators conducted SMS phishing attacks targeting a victim company's employees, tricking them into clicking on bogus links that exfiltrated their credentials via a phishing kit to an online Telegram channel under their control. The stolen data was then used to access the accounts, gather confidential company information, and siphon millions of dollars' worth of virtual currency after conducting SIM swapping attacks.

## **🔧 Cybersecurity Tools**

* [Cirro](https://github.com/bishopfox/cirro)
  → It is an open-source tool designed to help security experts find hidden risks in cloud environments. It works by collecting data about people, their permissions, and the digital resources they use, then turning that information into a visual map. By showing how these different pieces are connected, the tool makes it easier to spot "attack paths"—the step-by-step routes a hacker could take to move through a system and reach sensitive data. While it is currently focused on Azure, it is built to be flexible so users can add other platforms over time.
* [Janus](https://github.com/SpecterOps/Janus)
  → It is an open-source tool designed to help security teams track technical failures during operations. It automatically pulls logs from command-and-control (C2) platforms like Mythic and Cobalt Strike to identify where tools failed or commands were blocked. By organizing these "friction points" into reports, Janus helps teams see exactly where their workflow slows down and what tasks need to be improved or automated.

*Disclaimer: This is strictly for research and learning. It hasn't been through a formal security audit, so don't just blindly drop it into production. Read the code, break it in a sandbox first, and make sure whatever you’re doing stays on the right side of the law.*

## **Conclusion**

That wraps this week’s recap. Most of it isn’t loud, but it shows how easy it is for trusted paths to turn into entry points and for normal activity to hide real access.

Keep an eye on the basics. Check what you trust, watch how things run, and don’t ignore the small changes.