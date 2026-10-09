---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-23T16:15:23.584423+00:00'
exported_at: '2026-04-23T16:15:25.761851+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html
structured_data:
  about: []
  author: ''
  description: 'ThreatsDay Bulletin: active exploits, supply chain attacks, AI abuse,
    and stealth data risks observed this week.'
  headline: 'ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM
    Farms +25 New Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/threatsday-bulletin-290m-defi-hack.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: $290M DeFi Hack, macOS LotL Abuse, ProxySmart SIM Farms
  +25 New Stories'
updated_at: '2026-04-23T16:15:23.584423+00:00'
url_hash: 87768c2b55d851d8bbcea226b56718d8333cd32f
---

**

Ravie Lakshmanan
**

Apr 23, 2026

Hacking News / Cybersecurity News

You scroll past one incident and see another that feels familiar, like it should have been fixed years ago, but it still works with small changes. Same bugs. Same mistakes.

The supply chain is messy. Packages you did not check are stealing data, adding backdoors, and spreading. Attacking the systems behind apps is easier than breaking the apps themselves. The exploits are simple but still work, giving attackers easy access.

AI tools are also part of the problem now. They trust bad input and take real actions, which makes the damage bigger. Then there are quieter issues. Apps take data they should not. Devices behave in strange ways. Attackers keep testing what they can get away with. No noise. Just ongoing damage.

Here is the list for this week’s ThreatsDay Bulletin.

1. State-backed crypto heist

   Inter-blockchain communication protocol LayerZero has
   [revealed](https://x.com/LayerZero_Core/status/2046081551574983137)
   that North Korean threat actors tracked TraderTraitor may have been behind the
   [recent hack](https://www.coindesk.com/tech/2026/04/20/kelp-dao-claims-layerzero-s-default-settings-are-what-actually-caused-the-usd290-million-disaster)
   of decentralized finance (DeFi) project KelpDAO, resulting in the theft of $290 million. "The attack was specifically engineered to manipulate or poison downstream RPC infrastructure by compromising a quorum of the RPCs the LayerZero Labs DVN relied upon to verify transactions," LayerZero said. KelpDAO, in a
   [post](https://x.com/KelpDAO/status/2046332070277091807)
   on X, said, "Two RPC nodes hosted by LayerZero were compromised. A simultaneous DDoS attack was launched against the third RPC node. This was an attack on LayerZero's infrastructure. Kelp's own systems were not involved in building or operating that infrastructure." Meanwhile, the Arbitrum Security Council has
   [temporarily frozen](https://x.com/arbitrum/status/2046435443680346189)
   the 30,766 ETH being held in the address on Arbitrum One that is connected to the KelpDAO exploit. It's worth noting that TraderTraiter was attributed to the mega
   [Bybit hack](https://thehackernews.com/2025/03/safewallet-confirms-north-korean.html)
   in early 2025 that led to the theft of $1.5 billion in digital assets. Recently, Lazarus Group was also
   [linked](https://thehackernews.com/2026/04/285-million-drift-hack-traced-to-six.html)
   to the $285 million theft from the Drift Protocol.
2. Active RCE exploits

   Separately, VulnCheck has warned of attacks attempting to exploit two flaws in MajorDoMo, a smart home automation platform. While
   [CVE-2026-27175](https://nvd.nist.gov/vuln/detail/CVE-2026-27175)
   is a critical command injection vulnerability that started seeing exploitation on April 13,
   [CVE-2026-27174](https://nvd.nist.gov/vuln/detail/CVE-2026-27174)
   allows unauthenticated remote code execution via the PHP console in the admin panel and was first detected on April 18. "CVE-2026-27175 was exploited to drop a PHP webshell that delivers persistent backdoor access," VulnCheck
   [said](https://www.linkedin.com/posts/ccondon_kevs-infosecurity-cybersecurity-share-7452329826373283840-CvRT/)
   . "CVE-2026-27174 saw exploitation that ended in a Metasploit php/meterpreter/reverse\_tcp staged payload." Other vulnerabilities that have witnessed exploitation efforts include
   [CVE-2025-22952](https://nvd.nist.gov/vuln/detail/CVE-2025-22952)
   , an SSRF in Elestio Memos, and
   [CVE-2024-57046](https://nvd.nist.gov/vuln/detail/cve-2024-57046)
   , an authentication bypass in NETGEAR DGN2200 routers.
3. Supply chain malware surge

   A number of malicious packages have been discovered in the npm registry:
   [ixpresso-core](https://safedep.io/malicious-ixpresso-core-npm-rat/)
   ,
   [forge-jsx](https://safedep.io/malicious-forge-jsx-npm-rat/)
   ,
   [@genoma-ui/components, @needl-ai/common, rrweb-v1](https://safedep.io/malicious-genoma-ui-npm-dependency-confusion-campaign/)
   ,
   [cjs-biginteger, sjs-biginteger, bjs-biginteger](https://safedep.io/malicious-sjs-biginteger-npm-ssh-theft/)
   ,
   [@fairwords/websocket, @fairwords/loopback-connector-es, @fairwords/encryption](https://safedep.io/malicious-fairwords-npm-credential-worm/)
   ,
   [js-logger-pack](https://safedep.io/malicious-js-logger-pack-npm-stealer/)
   , and
   [@kindo/selfbot](https://research.jfrog.com/post/astral-injection/)
   . These packages come with features to steal sensitive data from compromised hosts, perform system reconnaissance, andimplant an SSH backdoor by injecting the attacker's public key into ~/.ssh/authorized\_keys, deliver an information stealer, and spread the
   [XWorm](https://thehackernews.com/2025/10/xworm-60-returns-with-35-plugins-and.html)
   remote access trojan (RAT). The packages published under the "@fairwords" scope have also been found to self-propagate to all npm packages using the victim's token and attempt cross-ecosystem propagation to PyPI via .pth file injection. New versions of
   [js-logger-pack](https://research.jfrog.com/post/hugging-face-exfil/)
   have since been found to leverage the Hugging Face repository to poll for updates and use it as a data-theft destination. Also detected was the compromise of
   [@velora-dex/sdk](https://safedep.io/malicious-velora-dex-sdk-npm-compromised-rat/)
   (version 9.4.1) to decode and execute a Base64 payload that fetches a shell script from a remote server that, in turn, downloads and persists a Go-based remote access trojan called minirat on macOS systems. Another legitimate package to be compromised was
   [mgc](https://safedep.io/malicious-npm-mgc-compromised-rat/)
   (versions 1.2.1 through 1.2.4), which was injected with a dropper that detects the operating system and fetches a platform-specific RAT from a GitHub Gist to exfiltrate valuable data.
4. AI prompt injection surge

   Forcepoint has detected 10 new indirect prompt injection (IPI) payloads targeting artificial intelligence (AI) agents with malicious instructions designed to achieve financial fraud, data destruction, API key theft, and AI denial-of-service attacks. "Regardless of the specific payload technique or attacker intent, every case follows the same fundamental sequence: the attacker poisons web content, hides the payload from human view, waits for an AI agent to ingest the page, exploits the LLM's inability to distinguish trusted instructions from attacker-controlled content, and triggers a real-world action with a covert exfiltration return channel back to the attacker," the company
   [said](https://www.forcepoint.com/blog/x-labs/indirect-prompt-injection-payloads)
   .
5. Covert browser data access

   The Claude desktop app has been
   [found](https://www.thatprivacyguy.com/blog/anthropic-spyware/)
   granting itself permission to access web browser data, even if some browsers haven't even been installed on a user's computer, web privacy expert Alexander Hanff said. The app has been spotted placing configuration files in preset locations for Chromium-based browsers like Brave, Google Chrome, Microsoft Edge, and Vivaldi. The Native Messaging manifest files pre-authorize Claude to interact with the browser even before the user installs it. The issue has been described as a case of dark pattern that violates privacy laws in the E.U.
6. Hardware display protection

   The U.K. National Cyber Security Centre (NCSC) has unveiled a new technology called SilentGlass that's designed to protect video connections from cyber attacks. "SilentGlass, a plug-and-play device, actively blocks anything unexpected or malicious between HDMI and Display Port connections and screens," NCSC
   [said](https://www.ncsc.gov.uk/news/world-first-ncsc-engineered-device-secures-vulnerable-display-links)
   . "Already successfully deployed on Government estates, SilentGlass is now available for anyone to buy and use. It has been approved for use in the most high-threat environments."
7. Passkeys replace passwords

   In a related development, the NCSC also endorsed
   [passkeys](https://www.ncsc.gov.uk/passkeys)
   as the default authentication standard and the "first choice of login" for access to all digital services. "Passkeys are a newer method for logging into online accounts, which do much of the heavy lifting for users, only requiring user approval rather than needing to input a password," NCSC
   [said](https://www.ncsc.gov.uk/news/ncsc-leave-passwords-in-the-past-passkeys-are-the-future)
   . "This makes passkeys quicker and easier to use and harder for cyber attackers to compromise." It also said the majority of cyber harms to individuals begin with criminals stealing or compromising login details, which makes passkey adoption a "huge leap" in boosting resilience to phishing attacks. More than 50% of active Google services users in the U.K. are said to be already using passkeys.
8. Backdoor sabotage claims

   Reports from Iranian media have claimed that hardware made by Cisco, Juniper, Fortinet, and MikroTik either rebooted or disconnected during recent attacks on Iran, despite the country being cut off from the global internet. "The most striking and suspicious aspect of this incident is its precise timing and the lack of access to the international internet at that moment," Iranian news website Entekhab
   [said](https://www.entekhab.ir/003qie)
   . "This disruption occurred at a time when international gateways were effectively blocked or inaccessible; therefore, attributing this chain collapse to 'a simple cyber attack from beyond the borders' is not only unconvincing but also reveals the traces of deep-seated sabotage embedded within the equipment." The report hypothesizes the presence of hidden firmware backdoors or rogue implants within compromised devices, creating a dormant botnet that's activated when a certain event occurs without the need for internet access. The other possibility is a supply chain compromise. "If the chips or installation files of Cisco and Juniper products are compromised before entering the country, even replacing the operating system will not solve the problem, because the root of the problem is embedded in the hardware and read-only memory (ROM)," the report said. These arguments have found purchase in China, whose state media agency Xinhua
   [called](https://english.news.cn/20260417/7c6c61509f1e4f4c87f97ad9f7a20bf0/c.html)
   U.S.-made equipment the "real trojan horse." The disclosure comes as DomainTools
   [revealed](https://dti.domaintools.com/research/mois-linked-moist-grasshopper-homeland-justice-karmabelow80-handala-hackers-campaigns-and-evolution)
   that the various hacktivist personas adopted by Iran, such as
   [Homeland Justice, Karma, and Handala](https://thehackernews.com/2026/03/iran-linked-hackers-breach-fbi.html)
   , "constitute a coordinated, MOIS-aligned cyber influence ecosystem operating under multiple branded identities that serve distinct but complementary operational roles."
9. Ransomware infighting escalates

   The Krybit ransomware group has hacked the website of rival ransom group 0APT after the latter
   [threatened](https://x.com/AlvieriD/status/2043661269861904492)
   to dox Krybit's members. According to security firm
   [Barricade](https://barricadecyber.com/threat-intelligence-report-krybit-ransomware-panel-breach-by-0apt/)
   , 0APT leaked the complete database of the Krybit ransomware operation, including victim records, plaintext credentials, Bitcoin wallets, encryption tokens, and a 56MB exfiltration file inventory. In return, Krybit has hit back by compromising 0APT's server within 48 hours, defacing their data leak site, and publishing source code, bash history, Nginx logs, and system files. To rub salt into the wound, the group listed 0APT as victim #1 on their own leak site.
10. Stealth malware-as-a-service

    There is a new cryptor-as-a-service platform called FUD Crypt (fudcrypt[.]net). "For $800 to $2,000 per month, subscribers upload an arbitrary Windows executable and receive a multi-stage deployment package that attempts automatic DLL sideloading, in-memory AMSI and ETW interference, silent UAC elevation via CMSTPLUA, and Windows Defender tamper via Group Policy on Enterprise builds," Ctrl-Alt-Intel
    [said](https://ctrlaltintel.com/research/FudCrypt-analysis-1/)
    .
11. Formbook phishing surge

    Two different phishing campaigns targeting Greek, Spanish, Slovenian, Bosnian, Latin, and Central American companies are using different techniques to deliver
    [Formbook](https://thehackernews.com/2024/07/cybercriminals-target-polish-businesses.html)
    malware. "FormBook is a data-stealing malware that targets Windows systems, primarily distributed through phishing emails with malicious attachments," WatchGuard
    [said](https://www.watchguard.com/wgrd-security-hub/secplicity-blog/formbook-malware-analysis-phishing-campaigns-use-dll-side-loading)
    . “It collects sensitive information like login credentials, browser data, and screenshots, using advanced evasion techniques to avoid detection.”
12. Stealth .NET execution abuse

    A highly sophisticated, multi-stage post-exploitation framework has been observed targeting organizations in the Middle East and EMEA financial sectors. "The threat actor leverages a legitimate, digitally signed Intel utility (IAStorHelp.exe) by abusing the .NET AppDomainManager mechanism, effectively turning a trusted binary into a stealthy execution container," CYFIRMA
    [said](https://www.cyfirma.com/research/operation-phantomclr-stealth-execution-via-appdomain-hijacking-and-in-memory-net-abuse/)
    . "This approach allows malicious code to be executed within a trusted environment. It bypasses conventional security controls without modifying the original signed binary." Because AppDomainManager hijacking enables stealth execution within a trusted signed binary, it allows malicious code to run without modifying the original executable, effectively bypassing code-signing trust controls. The attack begins with a phishing email containing a ZIP archive, which contains an
    [LNK file](https://www.splunk.com/en_us/blog/security/lnk-phishing-analysis-simulation.html)
    masquerading as a PDF document to execute "IAStorHelp.exe." It's currently not known who is behind the campaign, but the level of sophistication, modular design, and operational discipline suggest capabilities consistent with advanced threat actors.
13. RAT plus adware bundle

    A new malware campaign is spreading both a remote access trojan and adware together, allowing attackers to establish persistent access and make financial profits. The attack has been found to leverage a loader to deliver
    [Gh0st RAT](https://thehackernews.com/2024/07/gh0st-rat-trojan-targets-chinese.html)
    [trojan](https://www.cyfirma.com/news/weekly-intelligence-report-20-february-2026/)
    and CloverPlus adware, an unwanted software designed to install advertising components and change browser behavior, such as startup pages and pop-up ads, per
    [Splunk](https://www.splunk.com/en_us/blog/security/detecting-ghost-rat-cloverplus-adware-loader-analysis.html)
    .
14. macOS stealth execution abuse

    In a new analysis, Cisco Talos revealed that bad actors can bypass security controls in Apple macOS by repurposing native features like Remote Application Scripting (RAS) for remote execution and abusing Spotlight metadata (Finder comments) to stage payloads in a way that evades static file analysis. "Because Finder is scriptable over RAE, the comment of a file on a remote machine can be set via the “eppc://” protocol. By Base64 encoding a payload locally, a multi-line script can be stored within this single string field. The make new file command handles the creation of the target file, ensuring that no pre-existing file is required," Talos
    [said](https://blog.talosintelligence.com/bad-apples-weaponizing-native-macos-primitives-for-movement-and-execution/)
    . "The payload resides entirely within the Spotlight metadata, a location that remains largely unexamined by standard endpoint detection and response (EDR) solutions. This creates a stealthy staging area where malicious code can persist on the disk without triggering alerts associated with suspicious file contents." In addition, attackers can move toolkits and establish persistence using built-in protocols such as SMB, Netcat, Git, TFTP, and SNMP operating entirely outside the visibility of standard SSH-based telemetry. In some cases, adversaries can also bypass built-in restrictions by using Terminal as a proxy for execution, encoding payloads in Base64 and deploying them in stages.
15. LLM agent testing framework

    A group of academics has released a hackable, modular, and configurable open-source framework called
    [Terrarium](https://github.com/umass-aisec/Terrarium)
    for studying and evaluating decentralized LLM-based multi-agent systems (MAS). "As the capabilities of agents progress (e.g., tool calling) and their state space expands (e.g., the internet), multi-agent systems will naturally arise in unique and unexpected scenarios," the researchers
    [said](https://arxiv.org/abs/2510.14312v1)
    , adding it acts as "an isolated playground for studying agent behavior, vulnerabilities, and safety. It enables full customization of the communication protocol, communication proxy, environment, tool usage, and agents."
16. AI data privacy purge

    According to
    [Reuters](https://www.reuters.com/legal/government/ai-company-deleted-okcupid-user-photos-data-after-ftc-scrutiny-2026-04-20/)
    , AI company Clarifai said it has deleted 3 million profile photos taken from dating site OkCupid in 2014. It follows a
    [settlement reached](https://thehackernews.com/2026/04/weekly-recap-axios-hack-chrome-0-day.html)
    last month between the U.S. Federal Trade Commission (FTC) and Match Group, OkCupid's owner. Clarifai is said to have certified the data deletion to the FTC on April 7, 2026, and deleted any models that trained on the data. The company also emphasized that it hadn't shared the data with third parties. The FTC opened the investigation in 2019, after The New York Times
    [reported](https://www.nytimes.com/2019/03/01/business/ethics-artificial-intelligence.html)
    that Clarifai had
    [built](https://www.nytimes.com/2019/07/13/technology/databases-faces-facial-recognition-technology.html)
    a training database using OkCupid dating profile photos. The behavior was a direct violation of OkCupid's privacy policy, although Clarifai was not accused of wrongdoing.
17. Zero-credential RCE chain

    VulnCheck said it's seeing active exploitation of the Apache ActiveMQ Jolokia remote code execution chain that strings together
    [CVE-2026-34197 and CVE-2024-32114](https://thehackernews.com/2026/04/apache-activemq-cve-2026-34197-added-to.html)
    . "CVE-2024-32114 removes authentication from the Jolokia endpoint entirely on ActiveMQ versions 6.0.0 through 6.1.1," VulnCheck's Jacob Baines
    [said](http://www.linkedin.com/posts/jacob-baines-1490a7189_the-vulncheck-canary-network-is-seeing-active-share-7452736851557380096-0VkW/)
    . "Combined with CVE-2026-34197, that is zero-credential RCE."
18. Stealth phishing lure

    There has been a surge in phishing emails utilizing empty subject lines as a way to lure users to actually click and open the email without the usual warning cues. Known as silent subject or null subject phishing, the technique is designed to exploit blind spots in email defenses, as it allows such emails to bypass security filters that rely on analyzing the subject lines for specific keywords that may indicate potential phishing or scam. "Emails with empty subject lines evade user suspicion by exploiting human curiosity," CyberProof
    [said](https://www.cyberproof.com/blog/silent-lures-the-rise-of-empty-subject-email-attacks/)
    . "The primary objective of a silent subject campaign is to gain initial access through social engineering, leading to credential compromise, unauthorized access, and potential lateral movement within targeted environments, especially focusing on high-value or VIP users."
19. Industrial-scale SIM farms

    A Belarus-based turnkey solution is assisting SIM farm operators in supporting cybercrime on an industrial scale. Infrawatch said that it identified 87 instances of ProxySmart control panels in 17 countries that are linked to at least 24 commercial proxy providers and 35 cellular providers. The footprint spans 94 phone farm locations, distributed across 19 U.S. states, as well as countries in Europe and South America. ProxySmart provides an end-to-end platform for operating and monetizing mobile proxy infrastructure, including farm management, device control, customer provisioning, retail proxy sales, and payment handling. It's accessible via a web-based control panel that's self-hosted by the farm operator. Devices in the farms are either physical Android phones or USB 4G/5G modems. The phones are enrolled via an unsigned Android APK package downloaded from the ProxySmart website, with SMS send and receive capability included. Modems are managed through ModemManager, an open-source USB dongle management tool. The ProxySmart service is written in Python and obfuscated using PyArmour. "ProxySmart is publicly associated with a Belarus-based vendor footprint and offers an end-to-end stack for operating and monetizing a physical farm, including device management, automated IP rotation, customer provisioning, plan enforcement, and anti-bot countermeasures," the company
    [said](https://infrawatch.com/blog/inside-the-mobile-farm-the-oem-stack-powering-us-4g-5g-proxy-networks#blogpost)
    . "Technical analysis indicates operator capabilities consistent with large-scale evasion enablement, including automated IP rotation, remote device control, and network fingerprint spoofing." SIM farms enable a range of cybercrime activity such as smishing, premium-rate number fraud, bot sign-ups, and one-time password interception. In response to the findings, ProxySmart
    [disputed](https://proxysmart.org/a-response-to-recent-third-party-research/)
    its characterization as a SIM farm, stating it's a "data-path proxy management platform" and that its mobile proxy infrastructure "underpins a wide range of legitimate commercial and research activity" including advertising verification, brand protection, price monitoring, and anti-fraud model training, among others.
20. Telegram under CSAM probe

    Ofcom, the U.K.'s independent communications regulator, has launched an investigation into Telegram under the country's Online Safety Act to examine whether the platform is being used to share child sexual abuse material (CSAM) and is doing enough to combat the threat. "We received evidence from the Canadian Centre for Child Protection regarding the alleged presence and sharing of child sexual abuse material on Telegram, and carried out our own assessment of the platform," Ofcom
    [said](https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/ofcom-investigates-telegram-and-teen-chat-sites)
    . "In light of this, we have decided to open an investigation to examine whether Telegram has failed, or is failing, to comply with its duties in relation to illegal content." In a statement
    [shared](https://therecord.media/uk-regulator-to-probe-telegram-over-csam-allegations)
    with The Record, Telegram said it "categorically denies Ofcom's accusations," adding it has "virtually eliminated the public spread of CSAM on its platform through world-class detection algorithms and cooperation with NGOs." Earlier this year, Ofcom also
    [commenced](https://www.bleepingcomputer.com/news/security/uk-probes-telegram-teen-chat-sites-over-csam-sharing-concerns/)
    a probe into X to determine whether the service is taking necessary steps to take down illegal content, including non-consensual intimate images and CSAM.
21. EU cracks disinfo ops

    The European Union
    [imposed sanctions](https://www.consilium.europa.eu/en/press/press-releases/2026/04/21/russian-hybrid-threats-eu-lists-two-entities-over-information-manipulation-activities/)
    on two pro-Russian organizations accused of spreading disinformation and supporting the Kremlin's hybrid influence operations against Europe and Ukraine. The measures target Euromore and the Foundation for the Support and Protection of the Rights of Compatriots Living Abroad (Pravfond). The move is part of the E.U.'s broader effort to counter Russian information and influence operations targeting Europe since the start of Moscow's full-scale invasion of Ukraine in 2022. The E.U. has imposed sanctions on 69 individuals and 19 entities linked to Russian hybrid warfare.
22. Bot farm dismantled

    Ukrainian authorities have
    [dismantled](https://t.me/SBUkr/17353)
    a bot farm that's alleged to have supplied thousands of fake social media accounts to Russian intelligence services for use in disinformation campaigns against Ukraine. The suspected organizer of the network has been detained in the northern city of Zhytomyr, and nearly 20,000 fraudulent online profiles that were used in information operations have been blocked. The suspect is believed to have sold more than 3,000 fake Telegram accounts each month to Russian clients. The accounts were created using Ukrainian mobile phone numbers and then advertised on online platforms used by pro-Russian actors. If convicted, the suspect faces up to six years in prison.
23. Malicious extensions surge

    More than 130,000 users have downloaded and installed malicious Chrome and Edge extensions that, while offering the promised functionality, also implement covert tracking, remote configuration capabilities, and data collection mechanisms.The 12 extensions posed as tools to download TikTok videos and were available through the official Chrome and Edge stores. The activity has been codenamed StealTok. The extensions have been found to use remote configuration to bypass store review. "Beyond privacy concerns, the use of remote configuration endpoints introduces a significant security risk, enabling post-installation behavior changes that bypass marketplace review mechanisms," LayerX
    [said](https://layerxsecurity.com/blog/stealtok-130k-users-compromised-by-data-stealing-tiktok-video-downloaders/)
    .
24. Joomla SEO spam backdoor

    In a new campaign spotted by Sucuri, threat actors are planting a new PHP-based backdoor on Joomla sites to inject SEO spam. The injected script acts as a remote loader to send information about the infected website and awaits further instructions from an attacker-controlled server. "Attackers inject malicious code that silently serves spam content to visitors and search engines, all without the site owner knowing," Sucuri
    [said](https://blog.sucuri.net/2026/04/joomla-seo-spam-injector-obfuscated-php-backdoor-hijacking-site-visitors.html)
    . "The goal is simple: abuse the site's reputation to push traffic towards products the attacker wants to promote."
25. Post-exfiltration data trade

    A new service called Leak Bazaar has been promoted on the Russian-speaking TierOne forum that claims to process data stolen from extortion and ransomware attacks and turn it into "something more legible, more selective and precise, and making it marketable for the general population to ingest." It's advertised by a user named Snow, who joined the forum on March 3, 2026. "What Leak Bazaar is really offering is not a DLS or Data or Dedicated Leak Site in the conventional sense, but a post-exfiltration service layer," Flare
    [said](https://flare.io/learn/resources/blog/leak-bazaar-inside-new-criminal-platform)
    . "It is trying to reassure both suppliers and buyers that the platform can solve the most frustrating part of data theft, which is that a large percentage of exfiltrated material is too noisy, too unstructured, or too cumbersome to use without additional labor."
26. RDP scanning concentration

    GreyNoise has
    [disclosed](https://www.greynoise.io/blog/ip-addresses-behind-nearly-half-rdp-internet-scanning)
    that a small cluster of 21 IP addresses is now responsible for generating nearly half of all the RDP scanning traffic on the public internet. The addresses are registered to ColocaTel (AS213438), a company based in the Seychelles. According to the threat intelligence firm, mass internet scanning activity is now
    [preceding vendor vulnerability disclosures](https://www.greynoise.io/blog/the-internet-changes-before-the-advisory-drops)
    more frequently than before, with 49% of surges arriving within 10 days of disclosure and 78% within 21 days.In a related development, security researcher Morgan Robertson revealed that almost three-quarters of Perforce P4 source code management servers connected to the internet are misconfigured and leaking source code and sensitive files. "The default Perforce settings allow unauthenticated users to create accounts, list existing users, access passwordless accounts, and, until version 2025.1, allowed syncing repositories remotely; potentially exposing intellectual property across more than a dozen sectors, including gaming, healthcare, automotive, finance, and government," Robertson
    [said](https://morganrobertson.net/p4wned/)
    . "Action is recommended for all Perforce administrators to ensure security hardening, including setting stronger authentication requirements, disabling automatic account creation, and raising security levels."
27. Emerging threat groups surge

    Various new hacktivist, data extortion, and ransomware crews have been spottedin the wild. These include
    [Harakat Ashab al-Yamin al-Islamia](https://www.darkowl.com/blog-content/harakat-ashab-al-yamin-al-islamia-a-new-group-or-part-of-a-broader-iranian-aligned-network/)
    ,
    [World Leaks](https://breachcache.com/cases/worldleaks-extortion/)
    ,
    [Lamashtu](https://cyberxtron.com/resources/blogs/lamashtu-threat-report-an-emerging-data-extortion-group-targeting-global-organizations-7623)
    ,
    [Payouts King](https://www.zscaler.com/blogs/security-research/payouts-king-takes-aim-ransomware-throne)
    ,
    [BravoX](https://labs.infoguard.ch/posts/bravox/bravox/)
    ,
    [Black Shrantac](https://marlink.com/resources/knowledge-hub/black-shrantac-inside-the-ransomware-group-weaponising-legitimate-tools-against-global-organisations/)
    ,
    [NBLOCK](https://www.cyfirma.com/news/weekly-intelligence-report-17-april-2026/)
    ,
    [Ndm448](https://www.cyfirma.com/news/weekly-intelligence-report-20-february-2026/)
    ,
    [Chip](https://www.cyfirma.com/news/weekly-intelligence-report-13-march-2026/)
    ,
    [Ransoomed](https://www.cyfirma.com/news/weekly-intelligence-report-13-february-2026/)
    , and
    [Zollo](https://www.cyfirma.com/news/weekly-intelligence-report-20-march-2026/)
    .

None of this is new. That is the problem. Old paths still open, basic checks still skipped, and trust still given where it should not be. Attackers are not doing anything magical, they are just faster and less careful because they do not need to be.

The fixes are known but ignored. Patch early, check what you install, limit access, and stop trusting inputs by default. Most of the damage comes from things that were easy to prevent. Same story next week.