---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-10T03:11:58.515140+00:00'
exported_at: '2026-06-10T03:12:00.209708+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html
structured_data:
  about: []
  author: ''
  description: 'Your weekly cybersecurity recap: a GitHub supply chain worm, an exploited
    Android flaw, Instagram account takeovers, and a five-month mailbox spy.'
  headline: '⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm
    and More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/weekly-recap-instagram-account-hacks.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: Instagram Account Hacks, Android Zero-Day, GitHub Worm and
  More'
updated_at: '2026-06-10T03:11:58.515140+00:00'
url_hash: 91386ca5f56a0a3dbe77d49b09125e7302af6019
---

**

Ravie Lakshmanan
**

Jun 08, 2026

Cybersecurity / Hacking

Monday again. The weekend was meant to be quiet. It wasn't. Last week had poisoned packages, a broken AI helper, and a worm tearing through repos. The ugly part: basic tricks still worked.

A chatbot got fooled. A bot token got leaked inside the malware. The same old mistakes showed up again. And while everyone chased the loud stuff, quieter attackers sat in inboxes for months, reading mail and stealing it bit by bit.

Lots to cover. Grab coffee. Read up.

## **⚡ Threat of the Week**

**[Miasma Worm Hits 73 Microsoft GitHub Repositories in Supply Chain Attack](https://thehackernews.com/2026/06/miasma-worm-hits-73-microsoft-github.html)**
- Microsoft's GitHub repositories became the latest to fall victim to the ongoing Miasma self-replicating supply chain attack campaign. The incident impacted 73 Microsoft repositories across four of its GitHub organizations, including Azure, Azure-Samples, Microsoft, and MicrosoftDocs. The development prompted GitHub to disable access to those repositories. Miasma is assessed to be a variant of the Mini Shai-Hulud worm that TeamPCP publicly released in mid-May 2026.

## **🔔 Top News**

* **[Google Fixes Android Framework Flaw Under Exploitation](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)**
  - Google released patches for 124 security vulnerabilities impacting its Android operating system for the month of June 2026, including one high-severity flaw in the Framework component that has come under active exploitation. Tracked as CVE-2025-48595 (CVSS score: 8.4), the security flaw has been described as a case of privilege escalation without requiring any user interaction. The vulnerability impacts devices running Android versions 14, 15, 16, and 16 QPR2 (Quarterly Platform Release 2). Google has acknowledged there are indications that CVE-2025-48595 may be under "limited, targeted exploitation." As is typically the case, the tech giant did not reveal any specifics about who may have been behind the activity, the targets affected, and the scale of such efforts.
* **[U.S. Action Disrupts Investment Fraud Schemes](https://thehackernews.com/2026/06/doj-disrupts-southeast-asia-crypto.html)**
  - The U.S. Department of Justice announced the results of a sweeping action undertaken by government authorities and private sector companies to combat cyber-enabled and cryptocurrency fraud targeting Americans. The "Disruption Week" operation led to the takedown of millions of social media, email, and internet access accounts used by transnational cybercrime groups in Southeast Asia to defraud victims. Private sector entities voluntarily froze over $3.8 million in cryptocurrency involved in the laundering of funds stolen from Americans. The efforts are part of an ongoing U.S. government initiative called Scam Center Strike Force, which aims to dismantle transnational criminal organizations running cyber-enabled fraud and "pig butchering" (aka romance baiting) scams from compounds in Southeast Asia, along with the human trafficking and money laundering operations that fuel the illicit enterprise.
* **[China-Linked TA4922 Broadens Focus to Europe, Africa](https://thehackernews.com/2026/06/china-linked-ta4922-expands-phishing.html)**
  - A new Chinese-speaking cybercrime group has expanded its reach from East Asia into Europe and Africa, while rapidly overhauling the malware it employs to hack into corporate networks. The actor, tracked as TA4922, is financially motivated and focused on gaining remote access to victim systems for data theft, fraud, and the resale of access. Some elements of the threat actor's tactics overlap with Silver Fox and Void Arachne. Its operations are unusually varied, leveraging malware delivery, credential phishing, and credit card theft across different campaigns. While historical attacks targeted Japan, the actor has also targeted organizations in Taiwan, Korea, Singapore, and India, the U.K., Germany, Italy, and South Africa. The lures are localized, impersonating tax authorities, finance departments and human resources teams in the target's own language to distribute Atlas RAT, RomulusLoader, and SilentRunLoader through DLL side-loading techniques.
* **[OP-512 Targets Microsoft IIS Servers with Custom Web Shell Framework](https://thehackernews.com/2026/06/new-threat-cluster-op-512-targets.html)**
  - A previously unreported threat cluster dubbed OP-512 has been observed targeting Microsoft Internet Information Services (IIS) servers to deploy a bespoke web shell framework. The espionage-focused activity has been assessed as originating from China. "OP-512 was highly likely conducting espionage through a compromised Internet Information Services (IIS) web server on an organization whose sector and geography align with China-linked intelligence priorities," ReliaQuest said. The web shell framework facilitates file management and authenticated command execution.
* **[Hackers Spied on a Stock Exchange Executive's Outlook Mailbox for 5 Months](https://thehackernews.com/2026/06/hackers-spied-on-stock-exchange.html)**
  - Unknown threat actors managed to spy on a senior member of an unnamed global stock exchange for at least five months. There are still several unanswered questions, like who was behind it and how they obtained initial access. However, what's evident is that the attacker spent several months inside the Outlook mailbox and likely accessed sensitive information. The goal of the operation was most likely cyber espionage, but details are scant on which stock exchange was targeted. The earliest sign of malicious activity was observed on October 10, 2025. The attack led to the deployment of a mailbox stealer that ran in 2-4 week intervals to hoover up email data. The captured information was exfiltrated via Dropbox and Microsoft OneDrive Personal, transferring only small batches at a time to avoid raising any red flags. The data exfiltration runs lasted through March 2026.

## **‎️🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first -
[CVE-2026-28318](https://thehackernews.com/2026/06/cisa-adds-actively-exploited-solarwinds.html)
(SolarWinds Serv-U),
[from CVE-2026-39210 through CVE-2026-39217](https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)
(FFmpeg),
[CVE-2026-20245](https://thehackernews.com/2026/06/cisco-catalyst-sd-wan-manager-cve-2026.html)
(Cisco Catalyst SD-WAN Manager),
[CVE-2026-20230](https://thehackernews.com/2026/06/cisco-patches-cve-2026-20230-in-unified.html)
(Cisco Unified Communications Manager),
[CVE-2026-3300](https://thehackernews.com/2026/06/hackers-exploit-critical-everest-forms.html)
(Everest Forms Pro plugin),
[CVE-2025-48595](https://thehackernews.com/2026/06/google-june-2026-android-update-patches.html)
(Google Android)
[CVE-2026-8501](https://kb.cert.org/vuls/id/158530)
(PCTCore64.sys),
[CVE-2026-10629](https://kb.cert.org/vuls/id/615987)
(Verizon IMS network),
[CVE-2026-7299](https://kb.cert.org/vuls/id/265691)
(Appsmith),
[CVE-2026-10621, CVE-2026-10622](https://kb.cert.org/vuls/id/873170)
(Collibra Agent),
[CVE-2026-0826](https://www.rapid7.com/blog/post/ve-cve-2026-0826-critical-unauthenticated-stack-buffer-overflow-hp-poly-vvx-trio-voip-phones-fixed/)
(
[HP Poly Voice](https://www.rapid7.com/blog/post/ve-cve-2026-0826-how-an-old-bug-can-feed-ai-powered-impersonation/)
),
[CVE-2026-8206](https://www.wordfence.com/blog/2026/06/unauthenticated-privilege-escalation-vulnerability-patched-in-kirki-wordpress-plugin/)
(
[Themeum Kirki - Freeform Page Builder, Website Builder &amp; Customizer plugin](https://aretiq.ai/research/vul260602-cve-2026-8206-themeum-kirki-wordpress-plugin-password-reset-email-redirect-privilege-escalation/)
),
[CVE-2026-23479](https://www.zeroday.cloud/blog/redis-cve-2026-23479-deep-dive)
,
[CVE-2026-23631](https://www.zeroday.cloud/blog/redis-cve-2026-23631-dark-replica)
aka DarkReplica,
[CVE-2026-25243](https://www.zeroday.cloud/blog/redis-cve-2026-25243-deep-dive)
,
[CVE-2026-25588, CVE-2026-25589](https://www.zeroday.cloud/blog/redis-five-cves-overview)
(Redis),
[CVE-2026-49200, CVE-2026-49201](https://community.acer.com/en/kb/articles/19673)
(Acer Wave 7 routers),
[CVE-2026-8874, CVE-2026-8876, CVE-2026-8878, CVE-2026-8879, CVE-2026-8881, CVE-2026-8888, CVE-2026-8889](https://kb.cert.org/vuls/id/595768)
(Securly),
[CVE-2026-10881, CVE-2026-10882, CVE-2026-10883](https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop.html)
(Google Chrome),
[CVE-2026-41722, CVE-2026-41723, CVE-2026-41724](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/37513)
(Broadcom VMware Cloud Foundation Operations),
[CVE-2026-34908, CVE-2026-34909](https://bishopfox.com/blog/popping-root-on-unifi-os-server-unauthenticated-rce-chain-detection-analysis)
(UniFi OS Server),
[CVE-2026-4372](https://pluto.security/blog/unauthenticated-remote-code-execution-in-huggingface-transformers-via-config-injection/)
(Hugging Face),
[CVE-2026-45495](https://www.zerodayinitiative.com/advisories/ZDI-26-331/)
(Microsoft Edge),
[CVE-2026-42253](https://lists.apache.org/thread/j9vmlc410ht5f28fc98gx75jcbq62j00)
(Apache ActiveMQ),
[CVE-2026-9614](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Neurons-for-ITSM-CVE-2026-9614?language=en_US)
(Ivanti ISTM),
[CVE-2026-48019](https://github.com/laravel/framework/security/advisories/GHSA-5vg9-5847-vvmq)
(laravel/framework),
[CVE-2026-5386](https://www.cisa.gov/news-events/ics-advisories/icsa-26-148-06)
(KMW CCTV security cameras),
[CVE-2026-5509](https://www.tp-link.com/us/support/faq/5102/)
(TP-Link Archer BE450 v1 and Archer BE7200 v1),
[CVE-2026-4387](https://specterops.io/blog/2026/06/01/cve-2026-4387-strongdm-state-file-reuse/)
(StrongDM),
[CVE-2026-8633](https://www.ibm.com/support/pages/node/7274072)
(IBM WebSphere), and
[CVE-2026-9739](https://nvd.nist.gov/vuln/detail/CVE-2026-9739)
(MCP Toolbox).

## **🎥 Cybersecurity Webinars**

* [Learn How to Validate What Your SIEM, EDR, and SOC Catch](https://thehacker.news/validate-automated-pentesting)
  → Automated pentesting finds flaws. It doesn't prove your defenses caught them. Join Picus experts to learn where testing falls short, why "clean" reports can mislead, and how validation shows what your SIEM, EDR, and SOC actually detect.
* [Stop AI-Powered Attacks Before They Spread](https://thehacker.news/outpacing-mythos-cyberattacks)
  → AI is making cyberattacks faster, harder to spot, and easier to scale. This webinar shows why old defenses fail against threats like Mythos-and how Zero Trust helps block movement, limit damage, and stop attacks before they grow.
* [Learn How to Detect and Stop Risky AI Use in Real Time](https://thehacker.news/securing-ai-use)
  → AI tools are spreading through the workplace faster than security teams can control. Every pasted file, prompt, or piece of code can expose sensitive data to systems that the business never approved. This webinar shows how to detect risky AI use, stop leaks in real time, and keep company data out of uncontrolled AI tools.

## **📰 Around the Cyber World**

* **Five Eyes Warns of China Exploiting LinkedIn to Target Security Personnel**
  - Chinese military intelligence services are using LinkedIn and other professional networking sites like Indeed and Upwork to recruit people with access to government, military, foreign policy, or sensitive economic information, the U.S. and its Five Eyes intelligence partners
  [said](https://www.mi5.gov.uk/five-eyes-joint-bulletin-safeguarding-our-secrets)
  in an advisory. The aim is to acquire privileged military, political and economic intelligence that can provide China with a strategic and tactical advantage over the Five Eyes, per the advisory. "These actors use an aggressive online recruitment strategy whereby intelligence officers or their affiliates pose as employees of private consultancies, think tanks, or human resources firms, and place online job advertisements for foreign policy and defense analysts," the agencies said. Bloomberg
  [reported](https://www.bloomberg.com/news/articles/2026-06-03/us-and-five-eyes-allies-warn-of-linkedin-china-spying-threat)
  that China has been
  [targeting](https://www.washingtonpost.com/world/2026/06/03/us-allies-say-china-is-using-job-platforms-target-security-personnel/)
  Five Eyes nationals with security clearance, particularly those working in foreign affairs, security, and intelligence, and military personnel, including people stationed in the Asia-Pacific region, as well as journalists, academics, and think-tank employees with knowledge of unclassified information. Targets are offered payments in exchange for increasingly privileged information. Payments may arrive through a number of online platforms, including reputable services like PayPal, Zelle, and Wise, or via Western Union and cryptocurrency.
* **Over 20K Accounts Likely Impacted in Instagram Attack Campaign**
  - Meta has
  [revealed](https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/686120c8-63be-4e3c-b7ed-466d65b672f5.html)
  that 20,225 Instagram accounts may have been impacted in a recent attack abusing an AI-powered support tool. The attacks involved compromising the accounts simply by asking Meta's chatbot to link their own email address to the targeted account. This enabled unauthorized third parties to reset the account password and take control of it. Many of the high-profile accounts were then sold on the dark web. The exploitation of the High Touch Support (HTS) tool was discovered on May 31, 2026. The filing published on Maine's Attorney General website lists April 17 as the date when the breach occurred, indicating the first unauthorized access may have occurred weeks before it was discovered. It's currently what personal information, if any, the threat actors may have accessed. The use of the tool has since been disabled. The development comes as a vulnerability was
  [disclosed](https://x.com/vxunderground/status/2063360297247572365?ref_src=twsrc%5Etfw)
  in Instagram's web-based password reset flow that exposed unredacted email addresses and phone numbers associated with user accounts when providing a user name as input.
* **Hola Browser for Windows Compromised to Deliver Cryptocurrency Miner**
  - Sophos discovered an XMRig cryptocurrency miner binary bundled within a certified version of the Hola Browser installer for Windows. Hola attributed the anomaly to a supply chain compromise affecting its "update distribution pipeline," which allowed the unauthorized payload to evade detection. "This was a supply chain compromise, and critically, no user data was accessed, exfiltrated, or compromised at any point during this incident affecting 0.1% of users," Hola said. "We have since completely rebuilt our distribution pipeline, implemented advanced code-signing verification, and introduced tighter access controls and continuous monitoring across our infrastructure."
* **Malicious npm Packages Target Trusted Brands**
  - A threat actor has been deploying dozens of malicious packages to npm targeting AI companies, luxury brands, and venture capital firms. These packages drop a new malware strain that impersonates an AI coding tool. The malicious code is launched by means of a post-install hook. "When the binary payloads are run, a terminal window pops up and prompts the user for user information and OpenAI or Anthropic API keys," OpenSourceMalware
  [said](https://opensourcemalware.com/blog/stardrop-attack)
  . "Meanwhile, in the background, the malware is already harvesting ~/.local/share/stardrop/auth.json and other files for credentials."
* **2 npm Packages Deliver Epsilon Stealer**
  - Two malicious npm packages, turbo-axios and faster-axios, targeted developers searching for the popular axios HTTP client. "Both are trojanized copies of the real axios source with a single addition: a postinstall hook that fetches and eval()s remote JavaScript," SafeDep
  [said](https://safedep.io/malicious-faster-axios-npm-epsilon-stealer/)
  . "The chain terminates in
  [Epsilon Stealer](https://thehackernews.com/2023/11/lummac2-malware-deploys-new.html)
  , a malware-as-a-service (MaaS) Electron infostealer that harvests browser credentials, crypto wallets, and messaging sessions, then opens a persistent WebSocket channel for arbitrary command execution."
* **Malicious npm Package Leaks Own Telegram Bot Token**
  - In a related development, OX Security flagged a malicious npm package named cms-store-ren that exfiltrates data to Telegram, while leaking its own bot API token in the process. "cms-store-ren is a malicious npm package that collects data from developers' machines and then sends them to a Telegram channel," OX Security
  [said](https://www.ox.security/blog/malware-slop-2-malicious-npm-package-leaks-its-own-bots-telegram-private-token/)
  . "It also downloads a potentially malicious JavaScript file from a remote server and tries to execute it, although this behavior wasn't yet weaponized. The package acts as a downloader/loader whose primary purpose is to fetch and execute a second-stage payload while reporting successful infections back to the malicious actor."
* **Fake Document Factory Taken Down in Spain**
  - French and Spanish authorities, with support from Europol, dismantled an online marketplace selling fake identity documents to migrant smuggling rings operating in Europe to evade border controls, fraudulently obtain residence rights, and facilitate secondary movements within the region. The counterfeit document production facility, located in Alicante, Spain, led to one arrest and the seizure of approximately 800 forged European documents, document-production equipment, digital devices, a vehicle, and €1,580 in cash. "The search of the apartment, rented under a false name, uncovered a fully operational counterfeit document workshop, highlighting the industrial-scale production methods increasingly used by organised crime groups involved in document fraud," Europol
  [said](https://www.europol.europa.eu/media-press/newsroom/news/fake-document-factory-dismantled-in-spain-around-800-ids-seized)
  .
* **Former IBM Executive Accuses Company of Covering Up Hacks**
  - A former IBM cybersecurity executive
  [accused](https://www.bloomberg.com/news/articles/2026-06-04/ibm-at-t-accused-by-whistleblower-of-covering-up-foreign-hacks)
  the company of getting hacked three times in the previous decade by foreign governments and then covering up the breaches. William Barlow, who was IBM's vice president of threat intelligence until August 2019, said IBM concluded Chinese hackers breached its core network between 2013 and 2016, but that the software company went on to conceal the incidents and never publicly disclosed them. Breaches at two other IBM subsidiaries were also covered up in a similar manner, a lawsuit unsealed last week revealed.
* **Gafgyt Botnet Variant Targets DD-WRT Router**
  - A new variant of the
  [Gafgyt](https://thehackernews.com/2024/08/new-gafgyt-botnet-variant-targets-weak.html)
  botnet called C0XMO is now targeting DD-WRT router firmware by exploiting a stack buffer overflow vulnerability (CVE-2021-27137). "Unlike earlier versions, this malware separates its lateral movement into a standalone Python script," Fortinet FortiGuard Labs
  [said](https://www.fortinet.com/blog/threat-research/inside-cross-platform-propagation-of-new-gafgyt-variant-c0xmo)
  . "This approach helps the attacker target various system architectures and device types more efficiently." The activity was discovered in March 2026 in connection with an attack targeting a Japanese technology firm. Once C0XMO is delivered and executed on the victim host, it sets up persistence, terminates competing processes and red teaming utilities, and then establishes a connection with a remote server to accept DDoS attack commands against specific targets. It also comes with a scanner to facilitate lateral movement via SSH, Telnet, Android Debug Bridge (ADB), and other HTTP-based exploits (e.g., CVE-2025-34054, CVE-2016-15047, CVE-2015-2051, CVE-2022-35914, and CVE-2021-27137).
* **Malicious PyPI Package Drops Backdoor**
  - Parsimonius, a malicious typosquat of the parsimonious Python package, "incorporated the legitimate parsimonious parsing functionality to avoid suspicion while simultaneously deploying a Telegram-based backdoor," Zscaler
  [said](https://x.com/threatlabz/status/2062651665598337319)
  . "Once installed, the backdoor provided attackers with remote access capabilities and facilitated the theft of sensitive data, including .env files and bot authentication tokens." The package racked up 2,474 downloads, prior to it being removed.
* **VECT Ransomware Suffers From New Flaws**
  - A new analysis of the Windows version of
  [VECT ransomware](https://thehackernews.com/2026/04/vect-20-ransomware-irreversibly.html)
  has uncovered additional vulnerabilities that "can leave files renamed, partially encrypted, inconsistently modified, or damaged in ways the attacker's own decryptor cannot reliably reverse," Morphisec
  [revealed](https://www.morphisec.com/blog/vect-ransomware-that-cant-decrypt/)
  . "These bugs change the recovery picture. A VECT incident does not necessarily produce one clean class of encrypted files. The same .vect suffix can represent several outcomes: a file that was only renamed, a file encrypted in a single pass, a large file with only selected regions modified, or a file left inconsistent by failed writes or shared-state races."
* **Handala Brand Used for Physical and Influence Operations**
  - Recorded Future has revealed that Iran's Ministry of Intelligence (MOIS) has likely expanded the use of its Handala persona to include external physical and influence operations targeting U.S. and Israeli interests, bringing cyber, physical, and influence personas under a single umbrella. The threat intelligence company said it observed significant overlaps in the online activities of Handala Hack Team, a new Handala-branded persona named "Handala Popular Resistance Front," and three influence operations networks dubbed VIPEmployment, MOISIRAN, and Brave Israel. "Notably, the HPRF and the three influence operations networks all almost certainly share a modus operandi: their administrators solicit individuals to conduct physical attacks and espionage targeting U.S. and Israeli entities, on behalf of Iranian intelligence agencies, for a financial reward," Recorded Future
  [said](https://www.recordedfuture.com/research/iran-handala-physical-threats)
  . "By encompassing these groups under the Handala brand, MOIS likely seeks to take advantage of Handala's global recognition to amplify its solicitation efforts."
* **New Android Trojan OverlayPhantom Spotted**
  - A new Android banking trojan referred to as OverlayPhantom has been observed targeting more than 180 apps across 10 countries via malicious URLs, aiming to steal credentials via fake overlays and real-time screen sharing. "The malware employs a two-stage infection chain, using a dropper application that impersonates trusted platforms, including the official Austrian government identity application, ID Austria, and the widely used consumer platform TikTok, to deceive victims into installing it," Cyble
  [said](https://cyble.com/blog/overlayphantom-android-banking-trojan/)
  . "Once deployed, OverlayPhantom masquerades as 'Google Play Services' and abuses Android's accessibility service to gain persistent, elevated control of the infected device." The malware is equipped to run over 30 remote commands to enable automated gestures, clipboard manipulation, credential theft, and data exfiltration. Targets of the malware include financial and cryptocurrency apps serving users in the U.S., Australia, Germany, France, Belgium, Finland, the Netherlands, Italy, Spain, and the U.K.
* **Fake Copyright Infringement Notice Emails Lead to Credential Theft**
  - Threat actors are using
  [official-looking copyright removal requests](https://www.malwarebytes.com/blog/threat-intel/2026/06/these-convincing-copyright-notices-are-designed-to-steal-google-logins)
  to target Chrome extension developers, warning them of imminent removal and urging them to appeal by clicking on a link ("dmca-chrome-extensions[.]click") within 48 hours. "After you enter your extension's ID to 'verify' it, the page pulls in your extension's real name and icon," Malwarebytes said. "But it's all part of a phishing attack designed to steal your Google username and password." Other campaigns have been found to use
  [pirated PC games and modified installers](https://www.malwarebytes.com/blog/threat-intel/2026/06/pirated-pc-games-are-delivering-password-stealing-malware)
  for franchises like Far Cry, Need for Speed, FIFA, and Assassin's Creed to distribute a Windows
  [password-stealing malware](https://www.malwarebytes.com/blog/threat-intel/2026/06/infostealers-are-becoming-the-go-to-phishing-payload)
  ; fake
  [payment invoices](https://www.malwarebytes.com/blog/threat-intel/2026/06/we-found-this-fake-invoice-campaign-while-scammers-were-still-building-it)
  that trick recipients into calling a bogus customer support agent as part of refund scams; counterfeit websites impersonating
  [BlueWallet](https://www.malwarebytes.com/blog/threat-intel/2026/06/fake-bluewallet-steals-passwords-accounts-and-crypto-from-macs)
  and
  [OpenAI ChatGPT](https://www.malwarebytes.com/blog/threat-intel/2026/05/fake-chatgpt-download-site-infects-windows-and-mac-users-with-malware)
  to deliver a macOS stealer and
  [clipper](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)
  . For Windows systems, the website mimicking ChatGPT is used to deliver a credential-stealing malware loader, while Mac users get Odyssey Stealer, a fork of Atomic Stealer (AMOS).
* **Bypassing Malicious Skill Scanners**
  - Trail of Bit said it was able to bypass
  [ClawHub's malicious skill detector](https://github.com/openclaw/clawhub/blob/c3c885ec10161ad35fbe78678ccc3f8c34e03ffd/convex/lib/securityPrompt.ts)
  ,
  [Cisco's agent skill scanner](https://github.com/cisco-ai-defense/skill-scanner)
  , and scanners integrated into skills.sh to push rogue skills to public skill marketplaces and steal sensitive data from developer systems. One of the malicious skills used prompt injection to "convince the guard model that the malicious payload is nothing to worry about," the company
  [said](https://blog.trailofbits.com/2026/06/03/the-sorry-state-of-skill-distribution/)
  . "The skill tells the agent to configure its package managers (npm and yarn) to use an attacker-controlled registry, but dresses the subterfuge up in the language of corporate environment configurations and virtual private network access to convince the LLM analyzer the change is innocuous." The takeaway here is that trust can never be outsourced to a third-party scanner and that they cannot reliably detect malicious content in agent skills. To counter the risks, organizations are recommended to curate skill marketplaces for their employees and agents using trustworthy open-source collections.
* **Phishing Campaigns Drop Remcos RAT**
  - Payment slip-themed phishing emails are being used to
  [distribute](https://www.jumpsec.com/guides/blacktoad-network-manipulation-in-an-autoit-payload/)
  a link pointing an external file-hosting service like MediaFire, which triggers the download of a screen saver (.SCR) file, which kicks off a multi-stage chain that ends in the deployment of Remcos RAT by means of an AutoIt script after performing anti-analysis checks. The activity has been attributed by JUMPSEC to a threat group called BlackToad, which is likely an affiliate of the broader Nigerian e-crime ecosystem that's tracked as
  [SilverTerrier](https://thehackernews.com/2022/05/interpol-arrest-leader-of-silverterrier.html)
  with its own set of targeting lures and tradecraft. It also exhibits some infrastructure overlap with a cluster documented by Agoda Engineering as
  [BoredFluff](https://medium.com/agoda-engineering/strengthening-cybersecurity-a-multi-layered-approach-to-prevent-advanced-threats-in-travel-49fe6e28d23c)
  , which targeted hotel staff in 2024 through fake guest enquiries to deliver Remcos RAT through a malware loader named GuLoader.
* **Pink, a New Com-Affiliated Actor**
  - A new cybercrime brand called Pink (aka CL-CRI-1147), is leveraging vishing for initial access with the primary objective of data theft and extortion. It's assessed to be part of the broader
  [Com ecosystem](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)
  , embracing techniques similar to those of ShinyHunters and CL-CRI-1116 (Blackfile/Redact). The group's data leak site went live on May 31, 2026. "The threat actor leverages vishing for initial access, impersonating internal IT personnel to convince a user to input credentials into a phishing site, allowing the actor to gain access to the victim's account and MFA," Palo Alto Networks Unit 42
  [said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-06-03-Pink-Extortion-Brand-Activity.txt)
  . "After gaining access to the victim's account, the actor rapidly identifies and exfiltrates data from platforms like SharePoint and OneDrive, similar to other Com-affiliated groups." The threat actor has also been found to make use of compromised victim accounts to send their initial extortion email as well as internal Teams messages. According to
  [Google](https://www.theregister.com/cyber-crime/2026/06/04/pink-is-the-latest-goon-squad-to-use-fake-helpdesk-calls-to-steal-creds/5251434)
  , the activity maps to a threat group it calls
  [UNC6671](https://thehackernews.com/2026/01/mandiant-finds-shinyhunters-using.html)
  .

## **🔧 Cybersecurity Tools**

* [CAI](https://github.com/aliasrobotics/cai)
  → It is an open-source framework for building AI agents that help with cybersecurity work, from security testing and vulnerability discovery to defense automation. It supports 300+ AI models and includes built-in tools for tasks like reconnaissance, exploitation, privilege escalation, and security assessment.
* [PMG](https://github.com/safedep/pmg)
  → It is a free, open-source tool that blocks malicious open-source packages before they install. It sits in front of package managers like npm, pip, and Poetry, checks packages with SafeDep threat intelligence, and helps protect developers and AI coding agents from supply-chain attacks.

*Disclaimer: This is strictly for research and learning. It hasn't been through a formal security audit, so don't just blindly drop it into production. Read the code, break it in a sandbox first, and make sure whatever you're doing stays on the right side of the law.*

## **Conclusion**

That's the week. Nothing here is new. Same tricks. Same shortcuts. Same open inboxes. That's what makes it worse. Patch what matters first. Warn the people who click everything. Back up the important stuff.

Then log off for a bit. It'll be messy again by next Monday.