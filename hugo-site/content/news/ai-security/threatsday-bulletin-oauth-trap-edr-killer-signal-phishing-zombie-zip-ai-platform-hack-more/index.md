---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-12T22:15:15.728454+00:00'
exported_at: '2026-03-12T22:15:18.367900+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html
structured_data:
  about: []
  author: ''
  description: 'ThreatsDay: OAuth abuse, Signal hijacks, Zombie ZIP evasion, Teams
    malware, AI hack, RondoDox botnet, and more cyber stories.'
  headline: 'ThreatsDay Bulletin: OAuth Trap, EDR Killer, Signal Phishing, Zombie
    ZIP, AI Platform Hack & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/threatsday-bulletin-oauth-trap-edr.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: OAuth Trap, EDR Killer, Signal Phishing, Zombie ZIP,
  AI Platform Hack & More'
updated_at: '2026-03-12T22:15:15.728454+00:00'
url_hash: 06dc8e1b33e23fec3222974ef4bb5b661bebdca3
---

**

Ravie Lakshmanan
**

Mar 12, 2026

Cybersecurity / Hacking News

Another Thursday, another pile of weird security stuff that somehow happened in just seven days. Some of it is clever. Some of it is lazy. A few bits fall into that uncomfortable category of “yeah… this is probably going to show up in real incidents sooner than we’d like.”

The pattern this week feels familiar in a slightly annoying way. Old tricks are getting polished. New research shows how flimsy certain assumptions really are. A couple of things that make you stop mid-scroll and think, “wait… people are actually pulling this off?”

There’s also the usual mix of strange corners of the ecosystem doing strange things — infrastructure behaving a little too professionally for comfort, tools showing up where they absolutely shouldn’t, and a few cases where the weakest link is still just… people clicking stuff they probably shouldn’t.

Anyway. If you’ve got five minutes and a mild curiosity about what attackers, researchers, and the broader internet gremlins were up to lately, this week’s ThreatsDay Bulletin on The Hacker News has the quick hits. Scroll on.

1. OAuth consent abuse

   Cloud security firm Wiz has warned of the dangers posed by
   [malicious OAuth applications](https://thehackernews.com/2026/03/microsoft-warns-oauth-redirect-abuse.html)
   , highlighting how "consent fatigue" could open the door for attackers to gain access to a victim's sensitive data by giving their malicious apps a legitimate-looking name. By accepting the permissions requested by a rogue OAuth application, the user is "adding" the attacker's app into their company's tenant. "Once 'Accept' is clicked, the sign-in process is complete," Wiz
   [said](https://www.wiz.io/blog/detecting-malicious-oauth-applications)
   . "But instead of going to a normal landing page, the access token is sent to the attacker's Redirect URL. With that token, the attacker now has access to the user's files or emails without ever needing to know their password." The Google-owned company also said it detected a large-scale campaign active in early 2025 that involved 19 distinct OAuth applications impersonating well-known brands such as Adobe, DocuSign, and OneDrive, and targeted multiple organizations. Details of the activity were
   [documented](https://thehackernews.com/2025/08/attackers-use-fake-oauth-apps-with.html)
   by Proofpoint in August 2025.
2. Messaging account takeover

   Russian-linked hackers are trying to
   [break into](https://english.aivd.nl/documents/2026/03/09/cybersecurity-advisory.-phishing-via-messaging-apps-signal-and-whatsapp)
   the Signal and WhatsApp accounts of government officials, journalists, and military personnel globally with an aim to get unauthorized access – not by breaking encryption, but by simply tricking people into handing over the security verification codes or PINs. "The most frequently observed method used by the Russian hackers is to masquerade as a Signal Support chatbot in order to induce their targets to divulge their codes," the Netherlands Defence Intelligence and Security Service (MIVD) and the General Intelligence and Security Service (AIVD)
   [said](https://english.aivd.nl/latest/news/2026/03/09/russia-targets-signal-and-whatsapp-accounts-in-cyber-campaign)
   . "The hackers can then use these codes to take over the user's account. Another method used by the Russian actors takes advantage of the 'linked devices' function within Signal and WhatsApp." It's worth noting that a similar warning was
   [issued](https://thehackernews.com/2026/02/german-agencies-warn-of-signal-phishing.html)
   by Germany last month. "These attacks were executed via sophisticated phishing campaigns, designed to trick users into sharing information – SMS codes and/or Signal PIN – to gain access to users' accounts," Signal
   [said](https://x.com/i/status/2031038277604585785)
   . Google warned last year that Signal's widespread use among Ukrainian soldiers, politicians, and journalists had made it a frequent target for Russian espionage operations.
3. Cloud breach via software flaws

   Google has revealed that threat actors are increasingly exploiting vulnerabilities in third-party software to breach cloud environments. "The window between vulnerability disclosure and mass exploitation collapsed by an order of magnitude, from weeks to days," the tech giant's cloud division
   [said](https://cloud.google.com/security/report/resources/cloud-threat-horizons-report-h1-2026)
   . "While software-based exploits increased, initial access by threat actors using misconfiguration, which accounted for 29.4% of incidents in the first half of 2025, dropped to 21% in H2 2025. Similarly, exposed sensitive UI or APIs continued a downward trend, falling from 11.8% in H1 to 4.9% in H2. This decline suggests that automated guardrails are making identity and configuration errors harder to exploit and that threat actors are being driven toward more sophisticated and costly vectors that specifically target software vulnerabilities to gain a foothold." In most attacks investigated by Google, the actor's objective was silent exfiltration of high volumes of data without immediate extortion and long-term persistence.
4. Microcontroller debug bypass

   New research from Quarkslab has found that it's possible to bypass the 16-byte password protection required for debug access on several variants of the RH850 microcontroller family using voltage fault injection in under one minute. "Voltage glitching technique is performed by underpowering or overpowering the chip for a controlled amount of time to alter its behavior," the security company
   [said](https://blog.quarkslab.com/bypassing-debug-password-protection-on-the-rh850-family-using-fault-injection.html)
   . "The crowbar attack is a specific type of voltage glitch where the power supply is shorted to the ground instead of injecting a specific voltage, using a MOSFET, for example."
5. Solar Spider suspects arrested

   Two Nigerian nationals have been
   [arrested](https://www.amarujala.com/delhi-ncr/noida/two-nigerians-involved-in-international-cyber-fraud-module-arrested-in-greater-noida-2026-03-12)
   by authorities in the Indian state of Uttar Pradesh for their alleged involvement in an e-crime operation known as
   [Solar Spider](https://www.crowdstrike.com/en-us/adversaries/solar-spider/)
   . The suspects are believed to have been planning to siphon large amounts of money by leveraging security flaws in Indian cooperative banking systems. According to a
   [report](https://the420.in/solar-spider-cyber-fraud-nigerians-arrested-greater-noida/)
   from The420.in, the individuals have been identified as Okechukwu Imeka and Chinedu Okafor. The duo is suspected to be part of an international fraud syndicate involved in targeting financial institutions. Solar Spider has a history of targeting banking systems across India and the Middle East, often through spear-phishing campaigns. In a report published in July 2025, Tata Communications
   [revealed](https://tatacommunications.com/hubfs/47271964/TaCO-2024/threat-advisory/doc/threat-intelligence-advisory-22-july-2025.pdf)
   that threat actors leverage their initial access to steal credentials, tamper with NEFT/RTGS transactions, and focus on Structured Financial Messaging System (
   [SFMS](https://en.wikipedia.org/wiki/Structured_Financial_Messaging_System)
   ) and Host-to-Host (H2H) infrastructures. The group is also known for deploying a sophisticated attack framework dubbed
   [JSOutProx](https://thehackernews.com/2024/04/new-wave-of-jsoutprox-malware-targeting.html)
   since at least 2019.
6. PlugX malware campaign

   Check Point has disclosed targeted campaigns against entities in Qatar using conflict-related content as lures to deliver malware families like PlugX and Cobalt Strike. The attack chain uses Windows shortcut (LNK) files contained within ZIP archives, which, when opened, cause it to download a next-stage payload from a compromised server. The payload then displays the decoy document while using DLL side-loading to deploy PlugX. The activity, detected on March 1, 2026, has been attributed to
   [Mustang Panda](https://thehackernews.com/2025/09/china-linked-plugx-and-bookworm-malware.html)
   (aka Camaro Dragon). A second attack has been observed using a password-protected archive to execute a previously undocumented Rust loader that's responsible for deploying Cobalt Strike using DLL side-loading. "This loader exploits DLL hijacking of nvdaHelperRemote.dll, a component of the open-source screen reader NVDA. Abuse of this component has previously been observed in only a limited number of Chinese-nexus campaigns, including China-aligned activity associated with a campaign delivering
   [Voldemort](https://thehackernews.com/2024/08/cyberattackers-exploit-google-sheets.html)
   backdoor, as well as a wave of attacks targeting the Philippines and Myanmar back in 2025," Check Point
   [said](https://blog.checkpoint.com/research/china-nexus-activity-against-qatar-observed-amid-expanding-regional-tensions/)
   . While this attack is assessed as China-aligned, it has not been attributed to a specific threat actor. "The attackers leveraged the ongoing war in the Middle East to make their lures more credible and engaging, demonstrating the ability to rapidly adapt to major developments and breaking news," the company said.
7. Teen DDoS kit sellers

   Polish police have referred seven suspected minor cybercriminals to family court over an alleged scheme to sell distributed denial-of-service (DDoS) kits online. The suspects, aged between 12 and 16 at the time of the alleged offenses, face charges related to selling DDoS tools as part of a profit-driven scheme designed to target popular websites, including auction and sales portals, IT domains, hosting services, and accommodation booking sites. "Using the tools they administer, popular websites such as auction and sales portals, IT domains, hosting services, and accommodation booking services were attacked," Poland's Central Bureau for Combating Cybercrime (CBZC)
   [said](https://cbzc.policja.gov.pl/bzc/aktualnosci/849,Siedmiu-nastolatkow-sprzedawalo-narzedzia-do-atakow-DDoS.html)
   .
8. Phishing-resistant Windows login

   Microsoft is rolling out passkey support for Microsoft Entra on Windows devices, adding phishing-resistant passwordless authentication via Windows Hello. "We're introducing Microsoft Entra passkeys on Windows to enable phishing-resistant sign-in to Entra-protected resources. This update allows users to create device-bound passkeys stored in the Windows Hello container and authenticate using Windows Hello methods (face, fingerprint, or PIN)," Microsoft
   [said](https://mc.merill.net/message/MC1247893)
   . "It also expands passwordless authentication to Windows devices that aren't Entra-joined or registered, helping organizations strengthen security and reduce reliance on passwords."
9. Sysmon built into Windows

   Microsoft has natively integrated System Monitor (
   [Sysmon](https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/overview)
   ) functionality directly into Windows 11 and Windows Server 2025 as an optional built-in feature as of Windows 11's March feature update (
   [KB5079473](https://support.microsoft.com/en-us/topic/march-10-2026-kb5079473-os-builds-26200-8037-and-26100-8037-9c222a8e-cc02-40d4-a1f8-ad86be1bc8b6)
   ). It's disabled by default. The company
   [announced](https://techcommunity.microsoft.com/blog/windows-itpro-blog/native-sysmon-functionality-coming-to-windows/4468112)
   the integration in November 2025. "You no longer need to package it dynamically; you can simply
   [enable it programmatically via PowerShell](https://learn.microsoft.com/en-us/windows/security/operating-system-security/sysmon/how-to-enable-sysmon)
   ," Nick Carroll, cyber incident response manager at Nightwing, said. "Coupled with Microsoft's simultaneous announcement that Windows Intune will enable 'hotpatching' by default in May 2026, this drastically lowers the barrier to entry for deep endpoint visibility and represents a massive operational win for network defenders."
10. Canada phishing campaign

    An active phishing campaign is targeting Canadian residents (and possibly present in other countries) using fraudulent domains impersonating trusted institutions, including the Government of British Columbia and Hydro-Québec, with the goal of collecting personal information and credit card details, Flare
    [said](https://flare.io/learn/resources/blog/phishing-campaign-hosting-infrastructure-alleged-links-iranian-state-aligned-activity)
    . The hosting infrastructure behind this campaign is linked to
    [RouterHosting LLC](https://thehackernews.com/2023/08/iranian-company-cloudzy-accused-of.html)
    (aka Cloudzy), a provider that was publicly accused in 2023 of supplying services to at least 17 state-sponsored hacking groups from countries including Iran, China, Russia, and North Korea.
11. Private link safety in chats

    Meta has detailed the workings of Advanced Browsing Protection (
    [ABP](https://www.facebook.com/help/messenger-app/1147987549394223)
    ) in Messenger, which protects the privacy of the links clicked on within chats while still warning people about malicious links. "In its standard setting, Safe Browsing uses on-device models to analyze malicious links shared in chats," the company
    [said](https://engineering.fb.com/2026/03/09/security/how-advanced-browsing-protection-works-in-messenger/)
    . "But we've extended this further with an advanced setting called Advanced Browsing Protection (ABP) that leverages a continually updated watchlist of millions more potentially malicious websites." ABP leverages an approach called private information retrieval (PIR) to implement a privacy-preserving "URL-matching" scheme between the client's query and the server hosting the database, along with Oblivious HTTP, AMD SEV-SNP, and
    [Path ORAM](https://eprint.iacr.org/2013/280)
    for added privacy guarantees.
12. BlackSanta EDR killer

    A sophisticated attack campaign targeting HR departments and job recruiters has combined social engineering with advanced evasion techniques to stealthily compromise systems by avoiding analysis environments and leveraging a specialized module designed to kill antivirus and endpoint detection software. The attack begins with a resume-themed ISO file delivered likely through spam or phishing emails, which then drops next-stage payloads, including a DLL that's launched via DLL side-loading to gather basic system information, initiate communication with a remote server, run sandbox checks, employ geographic filtering to avoid running in restricted regions, and drop additional payloads, such as BlackSanta EDR that employs legitimate but vulnerable kernel drivers to impair system defenses, a known tactic referred to as Bring Your Own Vulnerable Driver (BYOVD). "Rather than functioning as a simple auxiliary payload, BlackSanta acts as a dedicated defense-neutralization module that programmatically identifies and interferes with protection and monitoring processes prior to the deployment of follow-on stages," Aryaka
    [said](https://www.aryaka.com/reports-and-guides/blacksanta-edr-killer-threat-report/)
    . "By targeting endpoint security engines alongside telemetry and logging agents, it directly reduces alert generation, limits behavioral logging, and weakens investigative visibility on compromised hosts." It's currently not known what the follow-on payloads are or how widespread the campaign is. Phishing campaigns don't just target HR teams, but also impersonate them in attacks. "Impersonating HR provides many benefits to threat actors. Tasks from HR are typically mandatory, so HR emails carry authority," Cofense
    [said](https://cofense.com/Blog/Seasonal-Surge-Why-HR-Phishing-Peaks-in-Q4-and-the-Seven-Themes-Behind-It)
    . "Legitimate HR tasks can also have strict deadlines, which a threat actor can use to impose urgency. Finally, regular HR tasks are expected by employees."
13. ZIP evasion technique

    A new technique dubbed
    [Zombie ZIP](https://github.com/bombadil-systems/zombie-zip)
    allows attackers to conceal payloads in specially crafted compressed files that can bypass security tools. "Malformed ZIP headers can cause antivirus and endpoint detection and response software (EDR) to produce false negatives," the CERT Coordination Center (CERT/CC)
    [said](https://kb.cert.org/vuls/id/976247)
    . "Despite the presence of malformed headers, some extraction software is still able to decompress the ZIP archive, allowing potentially malicious payloads to run upon file decompression." The vulnerability, tracked as CVE-2026-0866, has been codenamed Zombie Zip by researcher Christopher Aziz, who discovered it. The technique was demonstrated by Bombadil Systems security researcher Chris Aziz.
14. AI agent breaches platform

    Researchers at autonomous offensive security startup CodeWall
    [said](https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform)
    their AI agent hacked McKinsey's internal AI platform Lili and gained full read and write access to the chatbot platform in just two hours. This enabled access to the entire production database, including 46.5 million chat messages about strategy, mergers and acquisitions, and client engagements, all in plaintext, along with 728,000 files containing confidential client data, 57,800 user accounts, and 95 system prompts controlling the AI's behavior. The development is an indicator that agentic AI tools are becoming more effective for conducting cyber attacks. The agent said it found over 200 endpoints that were totally exposed, out of which 22 were unprotected. One of these endpoints, which wrote user search queries to the database, suffered from an SQL injection that could have made it possible to access sensitive data and rewrite the system prompts silently. McKinsey has since addressed the problem. There is no evidence that the issue was exploited in the wild.
15. Teams social engineering malware

    Hackers have contacted employees at financial and healthcare organizations over Microsoft Teams to trick them into granting remote access through Quick Assist and deploy a new piece of malware called
    [A0Backdoor](https://www.bluevoyant.com/blog/new-a0backdoor-linked-to-teams-impersonation-and-quick-assist-social-engineering)
    . The modus operandi, which aligns with the playbook of
    [Storm-1811](https://thehackernews.com/2026/03/fake-tech-support-spam-deploys.html)
    (aka STAC5777 or Blitz Brigantine), employs social engineering to gain the employee's trust by first flooding their inbox with spam and then contacting them over Teams, pretending to be the company's IT staff and offering assistance with the problem. To obtain access to the target machine, the threat actor instructs the user to start a Quick Assist remote session, which is used to deploy a malicious toolset that includes digitally signed MSI packages, some of which were hosted on Microsoft cloud storage tied to personal accounts. The installers serve as a conduit for launching a DLL that, in turn, decrypts and runs shellcode responsible for running anti-analysis checks and dropping A0Backdoor, which establishes contact to a remote server using DNS tunnelling to receive commands. The activity has been active since at least August 2025 through late February 2026.
16. Industrialized disinformation network

    The Russian influence operation known as
    [Doppelgänger](https://thehackernews.com/2024/11/ai-powered-fake-news-campaign-targets.html)
    has been described as industrialized and prioritizing infrastructure resilience, scalability, and operational continuity over short-term visibility. "Rather than functioning as a loose collection of spoofed websites or transient propaganda outlets, the network exhibits the hallmarks of a coordinated, professionally managed influence apparatus," DomainTools
    [said](https://dti.domaintools.com/research/doppelganger-rrn-disinformation-infrastructure-ecosystem)
    . "At its core, the ecosystem relies on systematic media brand impersonation executed at scale." Campaigns mounted as part of the operation exhibit deliberate geographic micro-targeting across European Union member states and the U.S.
17. Pentagon AI dispute

    Anthropic has
    [filed a lawsuit](https://www.courtlistener.com/docket/72379655/anthropic-pbc-v-us-department-of-war/)
    to block the Pentagon from placing it on a
    [national security blocklist](https://www.wsj.com/tech/ai/pentagon-formally-labels-anthropic-supply-chain-risk-escalating-conflict-ebdf0523)
    , stating the
    [supply chain risk designation](https://thehackernews.com/2026/02/pentagon-designates-anthropic-supply.html)
    was unlawful and violated its free speech and due process rights. The development comes after the Pentagon formally branded the artificial intelligence (AI) company a supply chain risk after it refused to remove guardrails against using its technology for autonomous weapons or domestic surveillance. In its own statement, Anthropic
    [said](https://www.anthropic.com/news/where-stand-department-war)
    "we had been having productive conversations with the Department of War over the last several days, both about ways we could serve the Department that adhere to our two narrow exceptions, and ways for us to ensure a smooth transition if that is not possible." However, the Pentagon
    [said](https://x.com/USWREMichael/status/2029754965778907493)
    there is no active negotiation happening with Anthropic. It also
    [reiterated](https://x.com/USWREMichael/status/2030704601444356542)
    that the department "does not do and will not do domestic mass surveillance." The development follows OpenAI's own deal with the U.S. Department of Defense, with CEO Sam Altman stating the defense contract would include protections against the same red lines that Anthropic had insisted on. The company has since
    [amended](https://openai.com/index/our-agreement-with-the-department-of-war/)
    its contract to ensure "the AI system shall not be intentionally used for domestic surveillance of U.S. persons and nationals." Anthropic's CEO Dario Amodei has
    [called](https://techcrunch.com/2026/03/04/anthropic-ceo-dario-amodei-calls-openais-messaging-around-military-deal-straight-up-lies-report-says/)
    OpenAI's messaging "safety theater" and "straight up lies."
18. GitHub SEO malware

    A new information stealer campaign distributing
    [BoryptGrab](https://www.trendmicro.com/en_us/research/26/c/boryptgrab-stealer-targets-users-via-deceptive-github-pages.html)
    is leveraging a network of more than 100 public GitHub repositories that claim to offer software tools for free, using search engine optimization (SEO) keywords to lure victims. The multi-stage infection chain begins when a ZIP file is downloaded from a fake GitHub download page. BoryptGrab can harvest browser data, cryptocurrency wallet information, and system information. It's also capable of capturing screenshots, collecting common files, and extracting Telegram information, Discord tokens, and passwords. Also delivered as part of the attack is a backdoor called TunnesshClient that establishes a reverse SSH tunnel to communicate with the attacker and acts as a
    [SOCKS5 proxy](https://censys.com/blog/unauth-socks)
    . The earliest ZIP file dates back to late 2025. Certain iterations of the campaign have been found to deliver Vidar Stealer or a Golang downloader dubbed HeaconLoad, which then downloads and runs additional payloads.
19. RAT campaign against India

    The Pakistan-aligned threat actor known as
    [Transparent Tribe](https://thehackernews.com/2026/03/transparent-tribe-uses-ai-to-mass.html)
    has been attributed to a fresh set of attacks targeting Indian government entities to infect systems with a RAT that enables remote command execution, process monitoring and termination, remote program execution, file upload/download, file enumeration, screenshot capture, and live screen monitoring capabilities. "The campaign primarily relies on social engineering techniques, distributing a malicious ZIP archive disguised as examination-related documents to persuade recipients to interact with the files," CYFIRMA
    [said](https://www.cyfirma.com/research/apt36-multi-vector-execution-malware-campaign-targeting-indian-government-entities/)
    . "Upon extraction, the archive delivers deceptive shortcut files along with a macro-enabled PowerPoint add-in, which collectively initiate the infection chain. The threat actors employ multiple layers of obfuscation and redundant execution mechanisms to enhance the probability of successful compromise while reducing the likelihood of user suspicion."
20. Signed phishing malware

    Microsoft is warning of multiple phishing campaigns using workplace meeting lures, PDF attachments, and abuse of legitimate binaries to deliver signed malware. The activity, observed in February 2026, has not been attributed to a specific threat actor or group. "Phishing emails directed users to download malicious executables masquerading as legitimate software," the company
    [said](https://www.microsoft.com/en-us/security/blog/2026/03/03/signed-malware-impersonating-workplace-apps-deploys-rmm-backdoors/)
    . "The files were digitally signed using an Extended Validation (EV) certificate issued to TrustConnect Software PTY LTD. Once executed, the applications installed remote monitoring and management (RMM) tools that enabled the attacker to establish persistent access on compromised systems." Some of the deployed RMM tools include ScreenConnect, Tactical RMM, and MeshAgent. The use of the TrustConnect branding was
    [disclosed](https://thehackernews.com/2026/03/threatsday-bulletin-redis-rce-ddr5-bot.html#fake-rmm-service-spreads-rat-via-phishing)
    by Proofpoint last week. Furthermore, the deployment of multiple RMM frameworks within a single intrusion indicates a deliberate strategy to ensure continuous access and ensure operational resilience even if one access mechanism is detected or removed. "These campaigns demonstrate how familiar branding and trusted digital signatures can be abused to bypass user suspicion and gain an initial foothold in enterprise environments," Microsoft added.
21. TikTok allowed in Canada

    Following a national security review of TikTok, Canada's Minister of Industry, Mélanie Joly, said the company can keep its business operational. "TikTok will implement enhanced protection for Canadians’ personal information, including new security gateways and privacy-enhancing technologies to control access to Canadian user data in order to reduce the risk of unauthorized or prohibited access," the government
    [said](https://www.canada.ca/en/innovation-science-economic-development/news/2026/03/minister-jolys-statement-on-the-outcome-of-the-further-national-security-review-of-tiktok-technology-canada-inc-under-the-investment-canada-act.html)
    . "TikTok will implement enhanced protections for minors." The development marks a complete 180 from a
    [2024 decision](https://thehackernews.com/2024/11/canada-orders-tiktok-to-shut-down.html)
    , when it was ordered to shut down its operations, citing unspecified "national security risks." However, that order was
    [paused in early 2025](https://www.bloomberg.com/news/articles/2026-03-09/tiktok-gets-green-light-to-stay-in-canada-reversing-earlier-ban)
    .
22. Vulnerabilities rise 12%

    Flashpoint
    [said](https://flashpoint.io/blog/global-threat-intelligence-report-2026/)
    it catalogued 44,509 vulnerability disclosures in 2025, a 12% increase year-over-year (YoY). Of those, 466 were confirmed as exploited in the wild. Nearly 33%, or 14,593 vulnerabilities, had publicly available exploit code. Ransomware attacks also increased 53% YoY in 2025, with 8,835 total attacks recorded. The top RaaS groups by attack volume in 2025 were Qilin at 1,213 attacks, Akira at 1,044, Cl0p at 529, Safepay at 452, and Play at 395. Manufacturing was the most targeted industry with 1,564 attacks, followed by technology at 987 and healthcare at 905. The U.S. accounted for approximately 53% of named victim organizations.
23. Botnet exploiting 174 flaws

    The
    [RondoDox](https://thehackernews.com/2026/01/rondodox-botnet-exploits-critical.html)
    DDoS botnet has been found to implement 174 different exploits between May 25, 2025, and February 16, 2026, peaking at 15,000 exploitation attempts in a single day between December 2025 and January 2026. It's believed that the threat actors are using compromised residential IP addresses as hosting infrastructure. "The operators of RondoDox have been using a shotgun approach, where they send multiple exploits to the same endpoint, hoping for one to work," Bitsight
    [said](https://www.bitsight.com/blog/rondodox-botnet-infrastructure-analysis)
    . Of the 174 different vulnerabilities, 15 have a public proof-of-concept (PoC), but no CVE, and 11 do not have PoC code at all. RondoDox is notable for its fast addition of recently disclosed vulnerabilities, in some cases incorporating the PoC even before the CVE was published (e.g.,
    [CVE-2025-62593](https://nvd.nist.gov/vuln/detail/CVE-2025-62593)
    ).
24. Memory-only keylogger attack

    Phishing emails bearing purchase order lures are being used to distribute an executable within RAR archives. Once launched, the binary extracts and runs
    [VIP Keylogger](https://thehackernews.com/2025/01/hackers-hide-malware-in-images-to.html)
    in memory without touching the disk. "This keylogger captures either browser cookies, logins, credit card details, autofills, visited URLs, downloads, or top sites from the appropriate files in each of the application's designated folders," K7 Labs
    [said](https://labs.k7computing.com/index.php/maas-vip_keylogger-campaign/)
    . It's also capable of targeting a wide range of web browsers, stealing the email accounts from Outlook, Foxmail, Thunderbird, and Postbox, and collecting Discord tokens.
25. Cloudflare-shielded phishing

    A new Microsoft 365 credential harvesting campaign has been observed abusing Cloudflare's services to delay detection and risk profiling. The gatekeeping is designed to ensure the visitor is a real target and not a security scanner or bot. "The campaign implemented multiple anti-detection techniques, including the use of CloudFlare human verification, hardcoded IP block lists, user agent checks, and multiple sites and redirects," DomainTools
    [said](https://dti.domaintools.com/securitysnacks/securitysnack-cloudflare-anti-security-for-phishing)
    .

Some of the stuff in this week’s list feels a little too practical. Not big flashy hacks — just simple tricks used in the right place at the right time. The kind of things that make defenders sigh because… yeah, that’ll probably work.

There’s also a bit of the usual theme: tools and features doing exactly what they were designed to do… just not for the people who built them. Add some creative thinking, and suddenly normal workflows start looking like attack paths.

Anyway — quick reads, strange ideas, and a few reminders that security problems rarely disappear… they just change shape. Scroll on.