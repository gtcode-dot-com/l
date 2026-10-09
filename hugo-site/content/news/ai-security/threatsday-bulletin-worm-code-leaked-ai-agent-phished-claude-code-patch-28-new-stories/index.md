---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-11T19:51:48.589349+00:00'
exported_at: '2026-06-11T19:51:49.947419+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html
structured_data:
  about: []
  author: ''
  description: 'Cybersecurity roundup: supply chain threats, AI agent risks, browser-cloning
    malware, mule networks, endpoint bypasses, and key security updates.'
  headline: 'ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code
    Patch + 28 New Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/threatsday-bulletin-worm-code-leaked-ai.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: Worm Code Leaked, AI Agent Phished, Claude Code Patch
  + 28 New Stories'
updated_at: '2026-06-11T19:51:48.589349+00:00'
url_hash: 2ea1a39ca2835bb9205958d869f6e9a3b1370a52
---

**

Ravie Lakshmanan
**

Jun 11, 2026

Hacking News / Cybersecurity News

It's been one of those weeks. You expect the usual noise: recycled malware, sloppy attacks, another easy target getting hit. Instead, there's a supply chain attack kit in a public repo, a $5,000-a-month RAT that clones browsers, and research showing AI agents can be tricked into leaking real credentials.

The bigger problem is how polished this all looks now. Mule networks run like SaaS. Deepfake KYC bypass is sold as a feature. Endpoint tools can be quietly weakened using built-in OS settings, with no exploit needed.

Here's the full list of threats, tools, flaws, and updates worth knowing.

1. 3.3B identity records exposed

   A new analysis from Flashpoint has
   [revealed](https://flashpoint.io/blog/proactive-defender-guide-infostealers/)
   that "more than 11.1 million devices were infected with infostealers last year, fueling a supply of over 3.3 billion stolen credentials, session cookies, cloud tokens, and other forms of identity data now circulating across illicit markets." There are over 30 unique infostealer strains actively listed for sale across illicit marketplaces, forums, and underground communities, indicating the "scale and accessibility of the modern malware-as-a-service ecosystem." Lumma, Acreed, Rhadamanthys, Vidar, and StealC were the most prolific stealers in 2025. India, Brazil, Indonesia, Vietnam, the Philippines, and the U.S. were the top six countries affected by stealer malware during the same period.
2. MaaS RAT targets credentials

   A threat actor named "o1oo1" has advertised an advanced remote access trojan (RAT) named SilabRAT that's sold under a malware-as-a-service (MaaS) model for $5,000 a month on darknet forums since September 2025. "SilabRAT is heavily focused on financial gain through credential theft," Group-IB
   [said](https://www.group-ib.com/blog/silabrat-hijackloader-trojan-malware/)
   . "It offers stability and is capable of bypassing existing security measures." Delivered via
   [ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
   campaigns using
   [Hijack Loader](https://thehackernews.com/2024/05/hijack-loader-malware-employs-process.html)
   , the malware uses Hidden Virtual Network Computing (HVNC) to facilitate remote control capabilities, employs techniques like Browser Profile Cloning to replicate a user's browser profile (user agent, extensions, storage, and other fingerprinting attributes) to the attacker's system, and can identify wallet addresses or extract cryptocurrency-related artifacts. The Russian-speaking malware developer and vendor, "o1oo1," has been active since late 2020, previously launching a service called
   [AsmCrypt](https://thehackernews.com/2023/09/cybercriminals-using-new-asmcrypt.html)
   .
3. 47% of tech intrusions

   CrowdStrike has revealed that a North Korean threat actor known as
   [Famous Chollima](https://thehackernews.com/2024/08/north-korean-hackers-target-developers.html)
   , which is behind the long-running IT worker and Contagious Interview campaign, accounted for 47% of all state-sponsored hands-on-keyboard operations against the tech sector between April 2025 and March 2026. Hands-on intrusions refer to cyber attacks in which a human operator controls and interacts with a system rather than relying solely on malware. "In their IT worker infiltration campaigns, they sought fraudulent employment at tech companies across North America, Europe, and Asia," the cybersecurity company
   [said](https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-technology-threat-landscape-report/)
   .
4. 13 domains seized

   The U.S. Department of Justice has announced the seizure of 13 internet domains masquerading as consulting companies used to target U.S. persons, including current and former security clearance holders with access to classified and sensitive U.S. government information. "These domain seizures offer a glimpse at how foreign actors can use promises of easy money to lure Americans into revealing sensitive or classified information that they are duty-bound to protect,"
   [said](https://www.justice.gov/opa/pr/justice-department-fbi-disable-13-websites-backed-suspected-chinese-agents-sought-sensitive)
   Assistant Attorney General for National Security John A. Eisenberg. "Anyone approached online with offers of easy income for vague 'consulting' work should treat those overtures with extreme caution and remain vigilant for warning signs of malicious targeting." These sham companies advertised generic consulting or analyst jobs on platforms like Upwork, Expertia AI, Hubstaff Talent, Wellfound, and Post Job Free that sought to recruit current or former U.S. government and U.S. military employees to lend their expertise to unspecified clients. The recruiters then pressured candidates to part with confidential information and reports from "insider" sources in exchange for cryptocurrency payments. The announcement comes after the Five Eyes intelligence alliance countries
   [warned](https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html#:~:text=Five%20Eyes%20Warns%20of%20China%20Exploiting%20LinkedIn%20to%20Target%20Security%20Personnel)
   of China aggressively using job platforms to target people for information. In a statement shared with Reuters, the Chinese Embassy in Washington
   [condemned](https://www.reuters.com/legal/litigation/us-seizes-13-website-domains-tied-alleged-chinese-intelligence-collection-2026-06-10/)
   the allegations and called them fabricated.
5. Supply-chain toolkit exposed

   The
   [Miasma](https://thehackernews.com/2026/06/microsoft-restores-some-github-repos.html)
   credential-stealing attack framework was briefly made available for free on GitHub, after multiple repositories with the name "Miasma-Open-Source-Release" began appearing since June 8, 2026. According to SafeDep, the source code has been published through compromised developer accounts. "The
   [Miasma](https://www.ox.security/blog/600000-monthly-downloads-affected-miasma-supply-chain-attack-is-back-on-npm/)
   codebase appears to be larger than a supply chain worm," SafeDep
   [said](https://safedep.io/inside-the-miasma-supply-chain-attack-toolkit/)
   . "It is a full supply chain attack toolkit that allows the operator to execute various attacks via stolen credentials against arbitrary or targeted packages on public registries (PyPI, npm, RubyGems), JFrog Artifactory, GitHub repositories and GitHub Actions, AI coding tools config poisoning, SSH-based lateral movement, and other attack vectors." As opposed to relying on conventional command-and-control (C2) infrastructure, the malware employs three independent C2 channels using GitHub commit search, each with a different search string and crypto key: "DontRevokeOrItGoesBoom" to discover attacker-controlled personal access tokens (PATs) for data exfiltration, "TheBeautifulSandsOfTime" to deliver JavaScript, and "firedalazer" to deliver Python script URLs that act as a remote code execution backdoor. Miasma is assessed to be a variant of the Shai-Hulud worm. The campaign has since morphed into a Python variant called
   [Hades](https://www.endorlabs.com/learn/shai-hulud-hades-wave-hits-six-pypi-bioinformatics-packages)
   , which represents the latest evolution of the sustained software supply chain campaign. As of last week, a total of
   [304 components](https://www.sonatype.com/blog/new-shai-hulud-miasma-wave-hits-hundreds-of-npm-packages)
   have been impacted by Miasma.
6. Search uploads retained

   Google has
   [revealed](https://support.google.com/websearch/answer/17024959)
   that it intends to save the images, files, audio, and video users upload to Search under a new "Search Services History" setting. This can include images, files, and audio/video recordings, such as Google Lens images, content you upload, and recordings from Search Live, Translate speaking practice, and voice searches, per
   [Google](https://support.google.com/websearch/answer/17025248)
   . The tech giant said the Search Services History setting will be used to "provide, develop, and improve its services," including its AI models, as well as
   [offer personalized suggestions](https://support.google.com/websearch/answer/17026260)
   and ads if the new "
   [Personalized Recommendations](https://www.google.com/search-personalization/)
   " option is switched on. These two settings are separate from Google's Web &amp; App Activity.
7. Cross-platform RAT emerges

   Iru has analyzed a new cross-platform RAT called SStar Agent that's designed for both Windows and macOS systems. "The macOS builds are heavily instrumented surveillance tools focused on recon and exfiltration, while the Windows build layers on a keyboard hook, clipboard monitor, and remote mouse/keyboard control," the company
   [said](https://www.iru.com/blog/sstar-agent)
   . "Notably, the malware includes a large POST request via endpoint /api/telemetry/report that constantly monitors and exfiltrates the entire directory tree to monitor files of interest. The gap between the Windows and macOS versions indicates this is still a work in progress." The malware is delivered by means of a poisoned npm package named "tw-style-utils." The lure is a bogus Web3 engineering take-home assessment, a GitHub repository ("star45674/smart-contract-engineer-role") that's likely distributed to targets. While the repository itself is clean, the payload resides in the npm dependency. Although it's not clear who is behind the malware, the activity overlaps with previously observed social engineering attacks mounted by North Korean hacking groups.
8. Fake npm popularity

   Tenable has detailed a technique dubbed download pumping, where attackers artificially inflate npm package download counts in order to make malicious packages appear legitimate and trustworthy to developers. This approach has been observed in a package named "
   [ambar-src](https://www.tenable.com/blog/cybersecurity-research-faq-new-malicious-npm-package-ambar-src)
   ," which reached more than 50,000 downloads in three days after attackers published hundreds of benign versions of the package before introducing the actual malicious payload. "Every time a new version was published, automated systems like repository mirrors and analysis bots automatically downloaded it," Tenable
   [said](https://www.tenable.com/blog/how-cyberattackers-inflate-malicious-package-npm-download-counts)
   . "Because the attackers systematically uploaded hundreds of versions, they artificially generated a massive wave of automated traffic, inflating the package's download count to more than 50,000 downloads in just three days."
9. Exchange spoofing risk

   A weakness in certain configurations of Microsoft Exchange could be abused by attackers to send emails masquerading as any user to a vulnerable organization. The technique has been codenamed Ghost-Sender. "Using Exchange Online (or on-premises Exchange in hybrid mode) in combination with an external MX record, such as a third-party email server or spam protection solution, can allow the spoofing of emails from any sender to any recipient in the target tenant," InfoGuard Labs
   [said](https://labs.infoguard.ch/posts/ghost-sender/)
   . "This is regardless of the configured SPF, DKIM, and DMARC policies of the spoofed sender's domain, and the emails are delivered without any further warning. It is possible to send emails from anyone, including external and internal email addresses. For internal senders, Outlook even resolves the sender's profile picture."
10. Russia-focused phishing waves

    A previously unknown group known as
    [SiribClone](https://www.f6.ru/blog/siribclone/)
    has targeted Russian military personnel using bait applications for "safe photo exchange" to distribute malicious files for desktop and mobile devices. In some cases, members of the group have posed as women seeking romantic relationships to infect smartphones, computers, and Telegram accounts. The group has been active since early 2025. Attacks targeting Android devices lead to the deployment of a spyware called SafeLoveStealer that can steal photographs, videos, documents, and location data. Windows systems, on the other hand, are infected by a stealer known as SiribGrabber. The malware is distributed via phishing emails containing ZIP archives disguised as military-themed documents. In addition, the group operates phishing sites mimicking Telegram login pages to trick targets into entering their phone numbers, verification codes, and two-factor authentication passwords, allowing them to seize control of the accounts. Also linked to the threat actor is a tool called Kontur that stores stolen Telegram sessions and allows operators to review captured messages. Russian maritime universities, energy facilities, diplomatic missions, and government agencies have also been targeted through phishing campaigns by an
    [unidentified group](https://securelist.ru/unknown-group-targets-maritime-universities/115765/)
    since at least July 2024. Recent attack waves have employed a C2 framework called
    [Ravage](https://github.com/FL1GHT5/Ravage)
    , although two distinct phishing campaigns observed in 2024 have used Cobalt Strike. The third hacking group to single out Russia (along with Belarus) is
    [Cloud Atlas](https://thehackernews.com/2024/12/cloud-atlas-deploys-vbcloud-malware.html)
    , which has resorted to sending phishing emails with ZIP archives containing malicious shortcuts that launch PowerShell scripts, paving the way for malware like
    [VBShower and PowerShower](https://thehackernews.com/2024/12/cloud-atlas-deploys-vbcloud-malware.html)
    , the latter of which is used to drop a credential grabber. Lateral movement via RDP, SSH, and RevSocks is achieved via PAExec or PsExec as part of a framework known as PowerAdmin. Furthermore, the attacks involve two new tools: PowerCloud, which collects user data with administrator privileges and writes it to Google Sheets, and Browser checker, a PowerShell script that checks whether browser processes (Chrome, Edge, Firefox, and others) are running.
11. ClickFix backdoor expands

    A ransomware-related threat actor has put to use a new malware family called MLTBackdoor that's delivered via ClickFix. "MTLBackdoor supports a set of commands like downloading and uploading files from the victim's system," Zscaler ThreatLabz
    [said](https://www.zscaler.com/blogs/security-research/technical-analysis-mltbackdoor)
    . "However, one of the most powerful features is the ability to load Beacon Object Files (BOFs) to expand its capabilities." The malware was discovered in May 2026. In recent months, ransomware and data extortion attacks involving DragonForce and World Leaks have employed backdoors like
    [VIPERTUNNEL](https://labs.infoguard.ch/posts/slithering_through_the_noise/)
    , a
    [Python malware](https://thehackernews.com/2025/01/python-based-malware-powers-ransomhub.html)
    previously linked to RansomHub, and
    [RustyRocket](https://www.linkedin.com/posts/t-ryan-whelan-1156ab5_rusty-rocket-overview-ugcPost-7427362470236864512-CLdf/)
    , a custom-built Rust tool to facilitate covert data exfiltration and persistent access. "Once an attacker runs it, RustyRocket can securely connect back to an attacker-controlled server using heavily encrypted and layered traffic that blends in with normal internet activity, making it very hard for defenders to detect," Accenture's T. Ryan Whelan said. "This malware is an integrated communications architecture built for persistence and obfuscation."
12. WooCommerce card theft

    A new skimmer campaign is targeting WooCommerce sites to steal card details from checkout pages. "The skimmer impersonates the real Stripe payment element, validates cards in real time so the victim never suspects anything," CloudSEK
    [said](https://www.cloudsek.com/blog/woocommerce-payment-skimmer-card-data-theft-checkout-backdoor)
    . "The most 'professional' aspect of this sample is how hard it works to feel legitimate. It re-implements the same client-side checks a real checkout performs."
13. 33,000 users targeted

    A new Go-based loader named GoFlateLoader is being used to deliver multiple infostealers, including Amatera, Remus, Lumma, Vidar, StealC, and SvitStealer. "GoFlateLoader appears both in x86 (32-bit) and x86-64 (64-bit) variants, matching the bitness of the payload it is supposed to execute," Gen Digital's Avast
    [said](https://www.gendigital.com/blog/insights/research/goflateloader-delivers-multiple-infostealers)
    . "The loader is designed for in-memory payload execution and is deliberately inflated with a massive PE overlay to hinder detection." The malware is delivered via cracked software and a malicious
    [Traffic Distribution System](https://thehackernews.com/2026/06/fake-sites-mimicking-open-source-tools.html)
    (TDS) that has been used to deliver Remus Stealer, AnimateClipper, and the SessionGate framework. Since the beginning of April 2026, more than 33,000 unique users have been targeted, with the most affected countries including Brazil, India, Argentina, Mexico, Turkey, and Spain.
14. $862K damage case

    [Maxwell Schultz](https://thehackernews.com/2025/11/weekly-recap-fortinet-exploit-chrome-0.html#:~:text=Ohio%20Contractor%20Pleads%20Guilty%20to%20Hacking%20Former%20Employer)
    , 36, of Columbus, Ohio, has been
    [sentenced](https://www.justice.gov/usao-sdtx/pr/former-contractor-sent-federal-prison-hacking-employers-network-retaliation)
    to 24 months in federal prison for hacking into his employer's network after his contract was terminated in May 2021. Impersonating another contractor, Schultz obtained login credentials, accessed the former employer's systems, and executed a malicious PowerShell script that reset roughly 2,500 passwords, locking out employees and contractors and causing more than $862,000 in losses. Schultz pleaded guilty to the crime in November 2025.
15. Fake banking updates

    A new phishing campaign impersonating
    [Italian and European banking brands](https://www.d3lab.net/nfcshare-evolves-from-a-banking-phishing-apk-to-a-github-hosted-android-nfc-fraud-campaign/)
    is being used to distribute an Android malware called
    [NFCShare](https://www.d3lab.net/nfcshare-android-trojan-nfc-card-data-theft-via-malicious-apk/)
    . The attacks use phishing sites that aim to trick users into entering their credentials, after which they are prompted to update the banking application by downloading an APK file hosted on GitHub ("antoniocastaldo1998/app-scuola"). The end goal is to guide the user through a fake card verification flow: bring the card near the phone, keep it close while "authenticating," and enter the card PIN. Under the hood, the app reads NFC card data (ISO-DEP) and exfiltrates it to a remote WebSocket endpoint. The activity shares tactical overlaps with other NFC relay malware, such as
    [SuperCardX and RelayNFC](https://thehackernews.com/2025/12/brazil-hit-by-banking-trojan-spread-via.html)
    . The presence of Chinese text suggests a China-linked operator or tooling lineage.
16. AI agent phishing risk

    Four phishing simulations on an
    [OpenClaw](https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
    email agent codenamed Pinchy have revealed it to be susceptible to tactics commonly used to deceive human users. "In some cases, Pinchy not only failed at spotting the phishing attacks, it also performed risky actions that could potentially compromise a real-world organization," Varonis
    [said](https://www.varonis.com/blog/openclaw-phishing)
    . "In one notable case, a casual email from 'Dan' asking the agent to share staging credentials was enough to forward AWS IAM keys, database passwords, and SSH access to an external Gmail." This agent phishing is different from indirect prompt injection. While the latter embeds malicious instructions inside data the model consumes to trigger unintended actions or responses, agent phishing operates above the application surface. "A believable request arrives through a normal communication channel, reads like a legitimate business message, and succeeds when the agent acts on it before verifying who asked," Varonis added.
17. AI fixes weak passwords

    Apple has revealed that its upcoming version of Apple Intelligence, the company's generative artificial intelligence (AI) system, will support capabilities to update its weak and compromised passwords with a single tap via the Passwords app. "Building on its ability to alert users about weak and compromised passwords, Passwords can now automatically fix these for users with just a tap," Apple
    [said](https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/)
    . "Using Apple Intelligence and Safari to agentically take action on a user's behalf, Passwords securely navigates through websites to sign in and upgrade their accounts to strong passwords."
18. EDR telemetry throttled

    A new technique called EDRChoker that interferes with the client-server connection of Endpoint Detection and Response (EDR) software to sidestep defenses. "EDRChoker uses policy-based Quality of Service (QoS) to throttle EDR agents to the lowest bandwidth; when agents attempt to connect, they will consistently time out due to the extremely low bandwidth," a security researcher who goes by the name Zero Salarium
    [said](https://www.zerosalarium.com/2026/06/edrchoker-choking-telemetry-stream-block-edr.html)
    . "It takes a list of common EDR process names and creates QoS policies that limit those processes to 8 bits per second. At that bandwidth, an EDR agent becomes effectively isolated from its server." Earlier this January, the researcher also demonstrated EDRStartupHinder, which prevents an EDR program from starting. "EDRStartupHinder aims to exploit Windows Bindlink to redirect a DLL from System32 to another location, alongside taking advantage of the function that only loads DLLs signed by a program protected with Protected Process Light (PPL) to prevent AV/EDR services from starting," the researcher
    [said](https://www.zerosalarium.com/2026/01/edrstartuphinder-edr-startup-process-blocker.html)
    . Another technique
    [devised](https://binarydefense.com/resources/blog/windows-defender-acl-blocking-a-silent-technique-with-serious-impact)
    by Binary Defense involves disabling critical security services, such as Windows Defender and Sysmon, without triggering traditional malware alerts. It modifies Windows Access Control Lists (ACLs) to add "Deny" Access Control Entries (ACEs) against core system libraries like "kernel32.dll." Because these services rely on the DLL to function, the dependency chain is broken. Upon a system reboot, the protected services fail to start, leaving the endpoint without any defenses.
19. STX RAT supply chain grows

    The supply chain attack
    [targeting CPUID to deliver STX RAT](https://thehackernews.com/2026/04/cpuid-breach-distributes-stx-rat-via.html)
    is broader in scope than previously thought, with a new analysis from Cyderes uncovering seven additional trojanized packages tied to the same campaign. "All packages follow the same delivery mechanism," the cybersecurity company
    [said](https://www.cyderes.com/howler-cell/cpuid-hwmonitor-xvpn-dll-sideloading-stx-rat)
    . "The actor, operating under the alias Leda Elacoate (pufferfish11@firemail[.]cc), built and maintained a Bitbucket repository of trojanized installers over approximately one month, targeting a wide range of user demographics." Among the impacted packages is X-VPN, a consumer VPN with over 100 million reported users. Users who installed X-VPN from official channels are not affected. "The actor began with cryptocurrency exchange and trading software as lures, targeting users with likely access to financial accounts, and progressively expanded that lure portfolio across a social engineering decoy and VPN software," Cyderes added.
20. Agent Tesla via ZIP lures

    Phishing emails masquerading as legitimate payment advice messages are being used to deliver ZIP archives, opening which triggers a multi-stage infection chain that leads to the deployment of
    [Agent Tesla](https://thehackernews.com/2025/08/hackers-using-new-quirkyloader-malware.html)
    . "In simple terms, the victim opens what looks like a harmless file, but behind the scenes, a heavily obfuscated Batch script silently launches PowerShell, which then pulls and executes additional malicious code directly in memory," Point Wild
    [said](https://www.pointwild.com/threat-intelligence/from-phishing-email-to-process-injection-inside-a-multi-stage-agent-tesla-infection-chain/)
    . "From there, the attack escalates into a staged execution chain involving shellcode decoding, persistence setup, and process injection into legitimate Windows applications like charmap.exe." Agent, Tesla is designed to steal browser credentials, log keystrokes, capture screenshots, and extract sensitive data from the system. The collected information is then exfiltrated using SMTP-based communication, allowing malicious traffic to blend with normal-looking email activity.
21. AI video lures spread malware

    Two social engineering campaigns are using AI-generated TikTok videos and Instagram Reels to direct users to sketchy sites that deploy Vidar Stealer and other dubious programs. "One methodology involves fake tutorials for software installs, with professional-sounding voice-overs and clean graphics," ReversingLabs
    [said](https://www.reversinglabs.com/blog/social-media-attacks-phishing)
    . "The second approach relies on posts demonstrating how to use premium software for free, spanning multiple videos, with a centralized tutorial being introduced after the account gains traction."
22. Routers turned into C2 nodes

    A suspected China-nexus intrusion set has been identified conducting a large-scale campaign targeting edge network devices across Southeast Asia. "The adversary deploys a custom Linux ELF implant (router.elf) directly onto compromised border routers, establishing persistent command-and-control (C2) via DNS over HTTPS (DoH) while simultaneously weaponizing the router's iptables subsystem to hijack downstream DNS traffic at scale," a security researcher named Y4er
    [said](https://qiita.com/Y4er/items/0b6071745e4b7b240b3e)
    . "Correlated Windows-side tradecraft leverages a cracked Cobalt Strike 4.4 Beacon delivered via DLL sideloading (version.dll), sharing identical C2 infrastructure and malleable C2 profiles with the router implant - confirming unified operational control.
23. RMM abused in Brazil

    An active phishing campaign has been observed targeting Brazilian organizations with fake business-document lures, resulting in the download of a NinjaOne Remote Monitoring and Management (RMM) agent. "The campaign begins with phishing emails that redirect victims to Portuguese-language landing pages impersonating familiar Brazilian workflows, including SEFAZ-related fiscal documents, Reclame Aqui-style complaint processes, and secure document-delivery portals," Cato Networks
    [said](https://www.catonetworks.com/blog/cato-ctrl-previously-undocumented-ninjaone-rmm-abuse-chain/)
    . "After completing a fake verification process, victims are prompted to download what appears to be a protected business document. Instead, the download delivers a legitimate NinjaOne RMM agent configured to provide remote access to attacker-controlled infrastructure, highlighting a previously undocumented abuse of NinjaOne in the Brazilian threat Landscape." The development once again highlights how threat actors no longer need to rely on bespoke malware to infiltrate organizations.
24. Money laundering goes MaaS

    Cybersecurity company KELA has shed light on money mule networks, which play a crucial role in modern cybercrime and financial fraud ecosystems, enabling threat actors to launder and monetize proceeds through ransomware, scams, and Business Email Compromise (BEC), and other illicit schemes. "In recent years, traditional mule recruitment has increasingly evolved into professionalized Mule-as-a-Service (MaaS) ecosystems that provide scalable laundering infrastructure to cybercriminals," KELA
    [said](https://www.kelacyber.com/blog/mule-as-a-service-money-laundering/)
    , adding "mule operations increasingly rely on stolen identities, synthetic identities, compromised accounts, and AI-assisted onboarding techniques rather than solely recruiting human participants." Threat actors have also been found to rely on forged documentation, deepfake-enabled KYC bypass methods, account takeover techniques, and automated account "warming" activity to set up resilient laundering infrastructures across multiple financial platforms.
25. AI chats exposed

    G DATA said it has
    [witnessed](https://blog.gdatasoftware.com/2026/06/38428-browser-addons-spy-on-ai-chats)
    a growing number of Google Chrome extensions that impersonate legitimate productivity tools while stealthily hijacking users' conversations with AI chatbots. Some of these include
    [Urban VPN](https://thehackernews.com/2025/12/featured-chrome-browser-extension.html)
    ,
    [Smart Sidebar: ChatGPT, Claude &amp; DeepSeek](https://thehackernews.com/2026/01/two-chrome-extensions-caught-stealing.html)
    , and Chat AI, the last of which exhibits traits consistent with a campaign dubbed
    [AiFrame](https://thehackernews.com/2026/02/malicious-chrome-extensions-caught.html#fake-ai-chrome-extensions-steal-credentials-emails)
    . "User data generated through AI conversations may still be vulnerable to theft by threat actors utilizing plug-ins that pose as legitimate tools," G DATA said.
26. 507 Meta repos exposed

    A public Meta IP address running an open Grafana instance acted as a pathway for read-write access to 507 private Meta repositories, netting the Sectricity Security Team a bug bounty of $157,000. "The pivot was a wildcard SAN on the TLS certificate: \*.llm-playground.aws.metafb.cloud, which exposed a quiet shadow estate behind metafb.cloud," the cybersecurity company
    [said](https://sectricity.com/blog/misconfigured-grafana-507-private-meta-repos/)
    . "By parsing JavaScript bundles across that estate, we uncovered references to a previously unseen domain: api.haloworld.xyz, which became the next pivot point. Slight (AI built wordlist given JS bundles, context, etc) fuzzing against api.haloworld.xyz then exposed /\_api/gcp-token, an unauthenticated endpoint that handed out a valid GCP OAuth2 token." The GCP token, in turn, granted read access to the project's Secret Manager that contained a Vercel token. The Vercel token exposed 85 environment variables across Meta's projects, including multiple GitHub personal access tokens (PATs) and other secrets. One of those GitHub tokens had read/write access to 507 private repositories.
27. 7M seniors’ data sold

    Troy Murray, 57, of Hickory, North Carolina, has been sentenced to more than 10 years in prison for selling the personal information of over 7 million elderly Americans to Jamaican lottery fraud scammers. He has also been ordered to pay a forfeiture in the amount of $5,214,688.48. Murray "devised a scheme where he organized, maintained, and sold lists containing the names, phone numbers, physical addresses, and, in some cases, ages and email addresses, of elderly Americans to individuals in Jamaica involved in lottery fraud schemes," the U.S. Justice Department
    [said](https://www.justice.gov/opa/pr/fraudster-who-sold-personal-information-over-7-million-elderly-americans-jamaican-scammers)
    . "From 2016 to 2023, Murray sold these lists to Jamaican scammers, who perpetrated lottery fraud on elderly American consumers, earning Murray hundreds of thousands of dollars each year." Each of these lists was sold for $500.
28. One-packet crash bug

    Security researcher Marcus Hutchins has released details and a proof-of-concept (PoC) exploit for ComoDoS, an integer underflow vulnerability residing in Comodo Internet Security's firewall driver, Inspect.sys (
    [CVE-2026-49494](https://nvd.nist.gov/vuln/detail/CVE-2026-49494)
    , CVSS score: 7.5). "Although the vulnerability can be used to remotely trigger both an out-of-bounds (OOB) read and out-of-bounds write in the Windows kernel, the limitations on both primitives lead me to believe it's unlikely this bug could be weaponized into RCE," Hutchins
    [said](https://malwaretech.com/2026/06/exploiting-a-remote-kernel-vulnerability-in-comodo-internet-security.html)
    . "The bug does, however, enable you to remotely crash the target system with a single TCP/IP packet, even if the firewall is configured to block all ports." The vulnerability remains unpatched as of writing.
29. CI/CD secrets exposed

    Microsoft said it discovered an issue in the Claude Code GitHub Action that could be exploited to expose CI/CD workflow secrets when AI agents process untrusted GitHub content, including issue bodies, pull request descriptions, and comments. "While Claude Code Action supported environment scrubbing for subprocess execution paths such as Bash, the Read tool was not subject to the same sandboxing model," the Windows maker
    [said](https://www.microsoft.com/en-us/security/blog/2026/06/05/securing-ci-cd-in-agentic-world-claude-code-github-action-case/)
    . "It was eventually authorized to access /proc/self/environ, reading the workflow's ANTHROPIC\_API\_KEY and potentially other credentials available to the runner." Following responsible disclosure on April 29, 2026, the issue was fixed on May 5 with the release of Claude Code version 2.1.128. The patch strengthens the Read tool by unconditionally rejecting a number of files in /proc/ in order to protect those files from exfiltration.
30. Fake $200K job lure

    The Iranian hacking group known as
    [Nimbus Manticore](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)
    approached an employee via LinkedIn by impersonating a headhunter, luring them with a salary offer of $200,000 per year. Per Nextron Systems, the interaction is said to have redirected the victim to a fake hiring portal branded as Ebix Recruitment that prompted them to enter temporary credentials received from the recruiter to log in to the website. "After authentication, the portal prompted the victim to download a two-factor authentication application for 'additional security,'" the company
    [said](https://www.nextron-systems.com/2026/06/01/detecting-nimbus-manticore-and-their-sideloading-infection-chains/)
    . "The advertised 2FA application was delivered as a ZIP archive and contained the malware payload." The attack culminates with the deployment of a
    [custom implant](https://thehackernews.com/2026/05/iranian-hackers-deploy-minifast-and.html)
    with data exfiltration and remote control capabilities.
31. Backdoor with wiper modules

    Cybersecurity researchers have flagged a new Golang backdoor called BLUERABBIT that routes C2 through RabbitMQ for tasking, Redis for state management, and MinIO for S3-compatible data exfiltration. "It is a full-spectrum intrusion tool: remote access, system profiling, file encryption with a .candy extension, and two distinct disk-wiping modules capable of rendering systems permanently unrecoverable," Binary Defense
    [said](https://binarydefense.com/resources/blog/bluerabbit-a-golang-based-backdoor-with-ransomware-and-destructive-capabilities)
    . The backdoor is assessed to be the work of an Iran-nexus threat actor. It was first observed in mid-to-late March 2026, and is likely used for targeting entities in Israel. BLUERABBIT is "related to the same likely Iran-nexus activity cluster that previously leveraged BLUEWIPE and SEWERGOO in June 2025," it added.

The throughline is simple: attackers do not always need exploits. They need patience, stolen credentials, trusted tools, and one policy setting nobody has checked since the last reorg. The perimeter is not the real problem anymore. The problem is everything inside it that still trusts by default.

Same old lesson: audit what your agents can access, treat every identity in the pipeline as a risk, and check what your browser extensions are sending home. See you Thursday.