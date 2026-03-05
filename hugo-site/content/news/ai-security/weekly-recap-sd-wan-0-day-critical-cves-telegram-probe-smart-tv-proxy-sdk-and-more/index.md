---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-05T01:05:14.075092+00:00'
exported_at: '2026-03-05T01:05:15.424266+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/weekly-recap-sd-wan-0-day-critical-cves.html
structured_data:
  about: []
  author: ''
  description: Weekly cybersecurity recap covering active exploits, AI abuse, exposed
    cloud assets, critical CVEs, and evolving threat trends.
  headline: '⚡ Weekly Recap: SD-WAN 0-Day, Critical CVEs, Telegram Probe, Smart TV
    Proxy SDK and More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/weekly-recap-sd-wan-0-day-critical-cves.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: SD-WAN 0-Day, Critical CVEs, Telegram Probe, Smart TV Proxy
  SDK and More'
updated_at: '2026-03-05T01:05:14.075092+00:00'
url_hash: 30df4179a20e11c258efff11b5a2d6247512c0b8
---

**

Ravie Lakshmanan
**

Mar 02, 2026

Cybersecurity / Hacking

This week is not about one big event. It shows where things are moving. Network systems, cloud setups, AI tools, and common apps are all being pushed in different ways. Small gaps in access control, exposed keys, and normal features are being used as entry points.

The pattern becomes clear only when you see everything together. Faster scans, smarter misuse of trusted services, and steady targeting of high-value sectors. Each story adds context. Reading them all gives a fuller picture of how today’s threat landscape is evolving.

## **⚡ Threat of the Week**

**[Cisco SD-WAN Zero-Day Exploited](https://thehackernews.com/2026/02/cisco-sd-wan-zero-day-cve-2026-20127.html)**
— A newly disclosed maximum-severity security flaw in Cisco Catalyst SD-WAN Controller (formerly vSmart) and Catalyst SD-WAN Manager (formerly vManage) has come under active exploitation in the wild as part of malicious activity that dates back to 2023. The vulnerability, tracked as CVE-2026-20127 (CVSS score: 10.0), allows an unauthenticated remote attacker to bypass authentication and obtain administrative privileges on an affected system by sending a crafted request. Cisco credited the Australian Signals Directorate's Australian Cyber Security Centre (ASD-ACSC) for reporting the vulnerability. The networking equipment major is tracking the exploitation and subsequent post-compromise activity under the moniker UAT-8616, describing the cluster as a "highly sophisticated cyber threat actor."

## **🔔 Top News**

* **[Anthropic Accuses 3 Chinese Firms of Distillation Attacks](https://thehackernews.com/2026/02/anthropic-says-chinese-ai-firms-used-16.html)**
  — Anthropic accused three Chinese AI firms of engaging in concerted "industrial-scale" distillation attack campaigns aimed at extracting information from its model, making it the latest American tech firm to level such claims after OpenAI issued similar complaints. DeepSeek, Moonshot AI, and MiniMax are said to have flooded Claude with large volumes of specially-crafted prompts to elicit responses to train their own proprietary models. Last month, OpenAI submitted an open letter to U.S. legislators, claiming to have observed activity "indicative of ongoing attempts by DeepSeek to distill frontier models of OpenAI and other U.S. frontier labs, including through new, obfuscated methods." The disclosure renewed a debate over training data sources and distillation techniques, with some criticizing the company for training its own systems using copyrighted material without permission. "Anthropic is guilty of stealing training data at a massive scale and has had to pay multibillion-dollar settlements for their theft," xAI CEO Elon Musk said.
* **[Google Disrupts UNC2814 GRIDTIDE Campaign](https://thehackernews.com/2026/02/google-disrupts-unc2814-gridtide.html)**
  — Google disclosed that it worked with industry partners to disrupt the infrastructure of a suspected China-nexus cyber espionage group tracked as UNC2814 that breached at least 53 organizations across 42 countries. The tech giant described UNC2814 as a prolific, elusive actor that has a history of targeting international governments and global telecommunications organizations across Africa, Asia, and the Americas. Central to the hacking group's operations is a novel backdoor dubbed GRIDTIDE that abuses Google Sheets API as a communication channel to disguise C2 traffic and facilitate the transfer of raw data and shell commands. Chinese cyber espionage groups have consistently prioritized the telecommunication sector as a target precisely because of the access their networks provide to sensitive data and lawful intercept infrastructure.
* **[Thousands of Public Google Cloud API Keys Exposed with Gemini Access](https://thehackernews.com/2026/02/thousands-of-public-google-cloud-api.html)**
  — New research has found that Google Cloud API keys, typically designated as project identifiers for billing purposes, could be abused to authenticate to sensitive Gemini endpoints and access private data. The problem occurs when users enable the Gemini API on a Google Cloud project (i.e., Generative Language API), causing the existing API keys in that project, including those accessible via the website JavaScript code, to gain surreptitious access to Gemini endpoints without any warning or notice. With a valid key, an attacker can access uploaded files, cached data, and even rack up LLM usage charges, Truffle Security said. The issue has since been plugged by Google.
* **[UAT-10027 Targets U.S. Education and Healthcare Sectors](https://thehackernews.com/2026/02/uat-10027-targets-us-education-and.html)**
  — A previously undocumented threat activity cluster known as UAT-10027 has been attributed to an ongoing malicious campaign targeting education and healthcare sectors in the U.S. since at least December 2025. The end goal of the attacks is to deliver a never-before-seen backdoor codenamed Dohdoor. "Dohdoor utilizes the DNS-over-HTTPS (DoH) technique for command-and-control (C2) communications and has the ability to download and execute other payload binaries reflectively," Cisco Talos said. Analysis of the campaign has revealed no evidence of data exfiltration to date. Although no final payloads have been observed other than what appears to be the Cobalt Strike Beacon to backdoor into the victim's environment, it's believed that UAT-10027's actions are likely driven by financial gain based on the victimology pattern.
* **[Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration](https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html)**
  — Security vulnerabilities in Anthropic Claude Code could have allowed attackers to remotely execute code on users' machines and steal API keys by injecting malicious configurations into repositories, and then waiting for an unsuspecting developer to clone and open an untrustworthy project. The vulnerabilities were addressed between September 2025 and January 2026. "The ability to execute arbitrary commands through repository-controlled configuration files created severe supply chain risks, where a single malicious commit could compromise any developer working with the affected repository," Check Point said. "The integration of AI into development workflows brings tremendous productivity benefits, but also introduces new attack surfaces that weren't present in traditional tools."

## **‎️‍🔥 Trending CVEs**

New vulnerabilities surface daily, and attackers move fast. Reviewing and patching early keeps your systems resilient.

Here are this week’s most critical flaws to check first —
[CVE-2025-40538, CVE-2025-40539, CVE-2025-40540, CVE-2025-40541](https://thehackernews.com/2026/02/solarwinds-patches-4-critical-serv-u.html)
(SolarWinds Serv-U),
[CVE-2026-20127](https://thehackernews.com/2026/02/cisco-sd-wan-zero-day-cve-2026-20127.html)
,
[CVE-2026-20122, CVE-2026-20126, CVE-2026-20128](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-authbp-qwCX8D4v)
(Cisco Catalyst SD-WAN),
[CVE-2026-25755](https://github.com/ZeroXJacks/CVEs/blob/main/2026/CVE-2026-25755.md)
(jsPDF),
[CVE-2025-12543](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05011en_us&docLocale=en_US#hpesbnw05011-rev-1-telco-service-activator-imprope-0)
(HPE Telco Service Activator),
[CVE-2026-22719, CVE-2026-22720, CVE-2026-22721](https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/36947)
(Broadcom VMware Aria Operations),
[CVE-2026-3061, CVE-2026-3062, CVE-2026-3063](https://chromereleases.googleblog.com/2026/02/stable-channel-update-for-desktop_23.html)
(Google Chrome),
[CVE-2025-10010](https://sec-consult.com/vulnerability-lab/advisory/multiple-vulnerabilities-in-cpsd-cryptopro-secure-disk-for-bitlocker/)
(CryptoPro Secure Disk for BitLocker),
[CVE-2025-13942, CVE-2025-13943, CVE-2026-1459](https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-null-pointer-dereference-and-command-injection-vulnerabilities-in-certain-4g-lte-5g-nr-cpe-dsl-ethernet-cpe-fiber-onts-security-routers-and-wireless-extenders-02-24-2026)
(Zyxel),
[CVE-2025-71210, CVE-2025-71211](https://success.trendmicro.com/en-US/solution/KA-0022458)
(Trend Micro Apex One),
[CVE-2026-0542](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB2693566)
(ServiceNow AI Platform),
[CVE-2026-24061](https://seclists.org/oss-sec/2026/q1/199)
(telnetd),
[CVE-2026-21902](https://supportportal.juniper.net/s/article/2026-02-Out-of-Cycle-Security-Bulletin-Junos-OS-Evolved-PTX-Series-A-vulnerability-allows-a-unauthenticated-network-based-attacker-to-execute-code-as-root-CVE-2026-21902)
(Juniper Networks Junos OS),
[CVE-2025-29631, CVE-2025-1242](https://www.cisa.gov/news-events/ics-advisories/icsa-26-055-03)
(Gardyn Home Kit),
[CVE-2025-15576](https://www.freebsd.org/security/advisories/FreeBSD-SA-26:04.jail.asc)
(FreeBSD),
[CVE-2026-26365](https://www.akamai.com/blog/security-research/2026/feb/cve-2026-26365-incorrect-processing-connection-transfer-encoding)
(Akamai),
[CVE-2026-27739](https://github.com/angular/angular-cli/security/advisories/GHSA-x288-3778-4hhx)
(Angular), and
[SVE-2025-50109](https://bishopfox.com/blog/samsung-tizen-os-version-through-9-0)
(Samsung Tizen OS).

## **🎥 Cybersecurity Webinars**

* [Automating Real-World Security Testing to Prove What Actually Works](https://thehacker.news/automate-testing-security-posture?source=recap)
  → This webinar explains why one-time security assessments are no longer enough and shows how organizations can automate continuous, real-world testing of their defenses to uncover gaps and measure how well controls hold up against actual attack techniques.
* [When AI Agents Become Your New Attack Surface](https://thehacker.news/ai-agents-attack-surface?source=recap)
  → This webinar explains that as AI tools turn into autonomous agents that can browse, call APIs, and access internal systems, the security risk expands beyond the model to the entire environment they operate in, requiring stricter access controls, monitoring, and system-level safeguards rather than model testing alone.
* [Quantum Is Coming: Preparing for the End of Today’s Encryption](https://thehacker.news/post-quantum-cryptography?source=recap)
  → This webinar explains how future quantum computers could break today’s encryption, why “harvest now, decrypt later” attacks are a real risk, and what practical steps organizations can take now to begin shifting to post-quantum cryptography.

## **📰 Around the Cyber World**

* **UNC6384 Drops New PlugX Variant**
  —
  [IIJ-SECT](https://sect.iij.ad.jp/blog/2026/02/plugx-executed-via-staticplugin/)
  and
  [LAB52](https://lab52.io/blog/plugx-meeting-invitation-via-msbuild-and-gdata/)
  have detailed new activity from the Chinese cyber espionage group
  [UNC6384](https://thehackernews.com/2025/08/unc6384-deploys-plugx-via-captive.html)
  . The attacks follow a known modus operandi of using STATICPLUGIN, a digitally signed downloader, to deliver updated versions of PlugX using DLL side-loading. The malicious payloads are distributed via phishing emails with meeting invitation lures or through fake software updates.
* **OpenAI Takes Action Against ChatGPT Accounts Used for Harmful Purposes**
  — OpenAI said it took down ChatGPT accounts used for influence operations, phishing, and malware development. This included a possible Chinese intelligence operation in which an individual associated with Chinese law enforcement used the AI tool for covert influence operations against domestic and foreign adversaries. The company also acted against clusters conducting reconnaissance about U.S. persons and federal building locations, online romance scams, and Russian influence operations across Africa by generating social media posts and long-form commentary articles. "Unusually, this scam network combined manual ChatGPT prompting and an automated AI chatbot to try to entrap its targets," OpenAI
  [said](https://openai.com/index/disrupting-malicious-ai-uses/)
  about the scam operation running out of Cambodia. Some of these scams targeted Indonesian loveseekers. Other scams used ChatGPT to create content that purported to come from fictitious law firms, as well as impersonate real attorneys and U.S. law enforcement as part of a recovery scam targeting fraud victims.
* **AI-Induced Lateral Movement**
  — New research from Orca Security has highlighted how AI can become a "third dimension" in the world of lateral movement, after network and identity, allowing attackers to expand their reach. "By injecting prompt injections in overlooked fields that are fetched by AI agents, hackers can trick LLMs, abuse Agentic tools, and carry out significant security incidents," Orca
  [said](https://orca.security/resources/blog/ai-induced-lateral-movement-ailm/)
  . "LLMs don’t truly understand the difference between data and instructions, and when tool output is fed back into the model, it can be interpreted as something to act on. Which opens a window to AI-induced Lateral Movement (AILM) activities."
* **Russia Launches Probe into Telegram CEO**
  — Russian authorities launched a criminal investigation of Telegram founder and CEO Pavel Durov. He is allegedly charged with promoting and facilitating terrorist activity on the messaging platform by failing to respond to law enforcement takedown requests. Russian officials have accused Durov of choosing a "path of violence and permissiveness" by not cooperating with its law enforcement agencies, according to
  [the Rossiyskaya Gazeta](https://rg.ru/2026/02/24/telegram-ot-simvolov-cifrovoj-svobody-k-instrumentu-gibridnyh-ugroz-1.html)
  . The move comes after Russia began restricting access to Telegram in the country in favor of MAX. Last month, Durov
  [called](https://t.me/durov/470)
  it an "attempt to force its citizens to switch to a state-controlled app built for surveillance and political censorship."
* **Hacked Prayer App Sends Surrender Messages**
  — According to reports from
  [The Wall Street Journal](https://www.wsj.com/livecoverage/iran-strikes-2026/card/israel-hacked-popular-iranian-prayer-app-to-urge-defections-resistance-wtYyb29CmKrTXoJBIV3C)
  and
  [WIRED](https://www.wired.com/story/hacked-prayer-app-sends-surrender-messages-to-iranians-amid-israeli-strikes/)
  , unidentified hackers seized control of an Iranian prayer app during a joint U.S.-Israeli attack to send messages urging the Iranian military to lay down their weapons and promising amnesty if they surrendered. The messages were sent in the form of push notifications to the BadeSaba Calendar app. It's currently not clear who is behind the hack. The app has been downloaded more than 5 million times from the Google Play Store. Following the U.S.-Israel war on Iran, the government
  [shut down all internet access](https://bsky.app/profile/netblocks.org/post/3mg2qsdqyss2j)
  in the country.
* **Smart TVs Turned Into AI Content Scrapers**
  — Several smart TV app makers are deploying a new SDK named
  [Bright SDK](https://www.theverge.com/column/885244/smart-tv-web-crawler-ai)
  that lets users see fewer ads but also stealthily turns their TV into a node in a global proxy network that crawls and scrapes the web. Bright Data, the company behind the SDK, claims to operate more than 150 million residential proxy IP addresses spanning 195 countries.
* **Multiple Stealer Malware Families Detected**
  — Multiple information stealer families have been detected in the wild. This includes
  [Arkanix](https://securelist.com/arkanix-stealer/119006/)
  ,
  [CharlieKirk GRABBER](https://www.cyfirma.com/research/charliekirk-grabber-a-python-based-infostealer/)
  ,
  [ComSuon](https://x.com/GenThreatLabs/status/2025958414833066132)
  ,
  [DarkCloud](https://flashpoint.io/blog/understanding-darkcloud-infostealer/)
  ,
  [MawaStealer](https://gist.github.com/shavitush/9ae98e9ae70c4772c91d7bec1a138fb3)
  , and
  [MioLab](https://g0njxa.medium.com/approaching-stealers-devs-a-brief-interview-with-miolab-novastealer-35589d651ffd)
  (NovaStealer). Kaspersky's analysis of Arkanix has revealed that it was likely developed as an LLM-assisted experiment, shrinking development time and costs. While Arkanix was promoted on underground forums in October 2025, the malware-as-a-service (MaaS) appears to have been taken down towards the end of 2025. The findings demonstrate continued demand for off-the-key stealer malware, creating an ecosystem that enables other threat actors to purchase stealer logs for obtaining initial access to targets. "Raw Infostealer logs are meticulously filtered by corporate domain, packaged, and sold to initial access brokers and attackers specifically looking for frictionless entry points into high-value corporate networks," Hudson Rock
  [said](https://www.infostealers.com/article/how-infostealers-industrialize-the-brute-forcing-of-corporate-sso-gateways/)
  . The development has been complemented by underground networks turning into cybercrime marketplaces, complete with reputation systems, escrow, and specialist vendors, Varonis added. "One operator runs infostealers across thousands of machines. Another extracts and sorts the credentials. A third sells curated access," security researcher Daniel Kelley
  [said](https://www.varonis.com/blog/how-hackers-buy-access)
  . "A fourth deploys the ransomware. Each person focuses on what they do best, and the ecosystem has become ruthlessly efficient."
* **Chilean National Extradited to U.S. to Face Financial Fraud Crimes**
  — Alex Rodrigo Valenzuela Monje (aka VAL4K), a 24-year-old Chilean national, has been extradited to the U.S. over his alleged role in running a cybercrime operation that involved the trafficking of payment card data. The defendant is accused of trafficking stolen credit card numbers and information for over 26,500 credit cards. "From at least May 2021 to August 2023, Valenzuela Monje operated an illegal online card shop, selling dumps of unauthorized access devices through Telegram channels," the U.S. Justice Department
  [said](https://www.justice.gov/usao-ut/pr/chilean-national-extradited-us-face-financial-fraud-crimes-district-utah)
  . "He allegedly operated the channels known as MacacoCC Collective and Novato Carding, offering payment card data for virtually all U.S. payment cards."
* **New FUNNULL Infrastructure Discovered**
  — QiAnXin has
  [flagged](https://blog.xlab.qianxin.com/exposing-funnull-how-ringh23-maccms-are-poisoning-the-web/)
  new infrastructure associated with
  [FUNNULL](https://thehackernews.com/2025/05/us-sanctions-funnull-for-200m-romance.html)
  , a Philippines-based content delivery network (CDN) sanctioned last year by the U.S. Treasury for facilitating cyber scam operations. "Previously, their main method was to poison existing public CDN services; now they have evolved to independently develop complete server-side attack suites (RingH23), actively infiltrating CDN nodes, demonstrating a significant improvement in control and technical sophistication," QiAnXin XLab said. Two independent supply chain infection channels have been identified: the compromise of maccms.la to distribute a malicious PHP backdoor through its update channel, and the compromise of the GoEdge CDN management node to implant an infection module, and deploy the proprietary RingH23 attack suite to all edge nodes via SSH remote commands. The campaign has compromised 10,748 unique IP addresses, predominantly video streaming sites.
* **Spike in Scans for SonicWall Devices**
  — GreyNoise said it detected a spike in scans for SonicWall devices originating from the infrastructure of a known proxy provider. The activity started on February 22, 2026, and scanned for exposed SonicWall SSL VPNs. A total of 84,142 scanning sessions targeting SonicWall SonicOS infrastructure were observed between February 22 and February 25, 2026. The scanning came from 4,305 unique IP addresses across 20 autonomous systems. "Ninety-two percent of sessions probed a single API endpoint to determine whether SSL VPN is enabled — the prerequisite check before credential attacks," GreyNoise
  [said](https://www.greynoise.io/blog/active-reconnaissance-campaign-targets-sonicwall-firewalls-through-commercial-proxy-infrastructure)
  . "A commercial proxy service delivered 32% of campaign volume through 4,102 rotating exit IPs in two surgical bursts totaling 16 hours."
* **Google Removes 115 Android Apps Tied to Ad Fraud**
  — A new ad fraud operation dubbed
  [Genisys](https://integralads.com/insider/inside-genisys-the-25-million-device-fraud-network-built-with-ai/)
  involved hijacking Android devices to run malicious activity in the background. The activity leveraged a set of
  [115 apps](https://integralads.com/insider/inside-arcade-the-gaming-web-that-plays-itself/)
  that stealthily opened websites inside hidden browser windows to generate ad display revenue for their creators. More than 500 domains were generated using AI tools to serve the ads. "They appear as generic blogs, news-style sites, and informational properties produced at scale, built not to attract real audiences but to receive and monetize fraudulent traffic," Integral Ads said. The apps have since been removed by Google. The findings build on another mobile ad fraud scheme called
  [Arcade](https://go.integralads.com/rs/469-VBI-606/images/Genisys_Threat_IOC_Apps_List_IAS.pdf)
  in which mobile apps generated hidden in-app browser activity to load websites in the background and convert mobile-origin activity into web traffic.
* **Zerobot Exploits Flaws in n8n and Tenda Routers**
  — A Mirai-based IoT botnet named
  [Zerobot](https://thehackernews.com/2022/12/zerobot-botnet-emerges-as-growing.html)
  has been observed exploiting vulnerabilities in the n8n AI automation platform (
  [CVE-2025-68613](https://thehackernews.com/2025/12/critical-n8n-flaw-cvss-99-enables.html)
  ) and Tenda routers (
  [CVE-2025-7544](https://nvd.nist.gov/vuln/detail/CVE-2025-7544)
  ) to expand its reach. The activity was first detected in January 2026. "Targeting of the n8n vulnerability is particularly interesting: Botnets typically exploit Internet of Things (IoT) devices, such as security cameras, DVRs, and routers, but n8n falls into an entirely different category," Akamai
  [said](https://www.akamai.com/blog/security-research/2026/feb/zerobot-malware-targets-n8n-automation-platform)
  . "Although this isn’t entirely new behavior for botnets, this sort of targeting presents a greater danger to organizations by exposing more critical infrastructure to compromise as the n8n exploit could enable lateral movement for a threat actor."
* **Various ClickFix Campaigns Spotted**
  — Threat hunters disclosed multiple ClickFix campaigns, including one leading to a hands-on-keyboard attack that deployed the Termite ransomware. The
  [attack](https://blog.deception.pro/blog/clickfix-hok-velvet-tempest-termite)
  has been attributed to a group known as Velvet Tempest (DEV-0504). Another ClickFix campaign, codenamed
  [OCRFix](https://www.cyjax.com/resources/blog/ocrfix-botnet-trojan-delivered-through-clickfix-and-etherhiding)
  , used websites impersonating the Tesseract OCR tool as a launchpad for delivering malware that uses
  [EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)
  to retrieve the C2 server, send system information, and await further instructions. A third campaign has been found employing
  [fake GitHub repositories](https://securitylabs.datadoghq.com/articles/tech-impersonators-clickfix-and-macos-infostealers/)
  impersonating software companies and leveraging ClickFix to social-engineer victims into installing infostealers, such as SHub Stealer v2.0.
* **GTFire Phishing Scheme Detailed**
  — A phishing campaign dubbed GTFire is abusing Google Firebase to host phishing pages and Google Translate to disguise the malicious URLs and bypass email and web security filters. "By chaining these services together, the attackers create phishing links that appear benign, leverage Google’s reputation, and dynamically redirect victims to brand‑impersonating login pages," Group-IB
  [said](https://www.group-ib.com/blog/gtfire-phishing-scheme/)
  . "Once credentials are submitted and harvested, victims are often redirected back to the legitimate website of the targeted organization, reducing suspicion and delaying incident response." The campaign is estimated to have harvested thousands of stolen credentials associated with more than a thousand organizations, spanning over a hundred countries and hundreds of industries. The threat actor behind the operation has been active since at least January 1, 2022. Mexico, the U.S., Spain, India, and Argentina are among the prominent targets.
* **C77L Ransomware Targets Russia**
  — A ransomware operation called C77L has been tied to at least 40 attacks on Russian and Belarusian enterprises since March 2025. The group is assessed to be operating out of Iran. Initial access to target networks is accomplished via weak passwords for publicly available RDP and VPN endpoints. "The targets of attacks are Windows systems due to their overwhelming predominance in the IT infrastructures of medium and small businesses," F6
  [said](https://www.f6.ru/blog/c77l-ransomware/)
  .
* **RESURGE Malware Can Be Dormant on Infected Ivanti Devices**
  — The U.S. Cybersecurity and Infrastructure Security Agency (CISA)
  [updated](https://www.cisa.gov/news-events/analysis-reports/ar25-087a)
  its original alert for
  [RESURGE](https://thehackernews.com/2025/03/resurge-malware-exploits-ivanti-flaw.html)
  , a piece of malware deployed as part of exploitation activity targeting a now-patched security flaw in Ivanti Connect Secure (ICS) appliances. The agency said "RESURGE has sophisticated network-level evasion and authentication techniques, leveraging advanced cryptographic methods and forged TLS certificates to facilitate covert communications," adding "RESURGE can remain latent on systems until a remote actor attempts to connect to the compromised device."
* **30 Members of The Com Arrested**
  — A coordinated law enforcement operation led by Europol
  [detained](https://www.europol.europa.eu/media-press/newsroom/news/project-compass-first-operational-results-against-com-network)
  30 individuals connected to an underground online community known as
  [The Com](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)
  . The operation, launched in January 2025, has been codenamed Project Compass. An additional 179 members were also identified as part of the investigation. The Com is the name assigned to a loose-knit cybercrime collective that has been linked to online doxxing, harassment, threats of violence, extortion, sexual exploitation, phishing, SIM swapping, ransomware, and other digital crimes. Europol described The Com as a decentralized extremist network.
* **U.K. Government Cuts Cyber Attack Fix Times by 84%**
  — The U.K. government has
  [claimed](https://www.gov.uk/government/news/government-cuts-cyber-attack-fix-times-by-84-and-launches-new-profession-to-protect-public-services)
  it has reduced its backlog of critical vulnerabilities by 75% and reduced cyber attack fix times by 87%. Serious security weaknesses in public sector websites are fixed six times faster, cutting the average time from nearly two months to just over a week, the U.K. government said in an update published on 26 February.
* **Poland Dismantles Organized Crime Group**
  — Poland's Central Bureau for Combating Cybercrime (CBZC)
  [dismantled](https://cbzc.policja.gov.pl/bzc/aktualnosci/832,Funkcjonariusze-CBZC-zabezpieczyli-ponad-100-000-wyludzonych-loginow-i-hasel-do-.html)
  an organized group that used phishing to take control of Facebook accounts and extract BLIK payment codes from victims. Eleven members of an organized criminal group operating in Poland and Germany between May 2022 and May 2024 were identified. Six suspects have been placed in pretrial detention as part of the investigation, and over 100,000 credentials were seized. The group used "phishing techniques to obtain login details for Facebook accounts, and then gained access to them and used instant messaging to extort BLIK codes from other users of the portal," CBZC said.
* **Hacker Exploits Clade to Target Mexican Government Sites**
  — An unknown hacker
  [exploited](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data)
  Anthropic's Claude chatbot to carry out attacks against Mexican government agencies, according to a report by Gambit Security. "Within a month of the initial compromise, ten government bodies and one financial institution were affected, approximately 195 million identities exposed, and roughly 150GB of data exfiltrated: tax records, civil registry files, voter data," the company
  [said](https://www.morningstar.com/news/accesswire/1139788msn/gambit-security-raises-61m-to-set-the-standard-for-enterprise-resilience)
  . "The attacker even built an automated system that forges official government tax certificates using live data. It was orchestrated by an individual actor directing AI to operate as a nation-state-level team of operators and analysts." The operation ran on more than 1,000 prompts and regularly passed information to OpenAI's GPT-4.1 for analysis. The breach began in late December 2025 and continued for about a month. Anthropic has since disrupted the activity and banned all of the accounts involved. The attacks haven't been attributed to a specific group.

## **🔧 Cybersecurity Tools**

* [Titus](https://github.com/praetorian-inc/titus)
  → It is an open-source tool from Praetorian that scans code, files, repositories, and traffic to find leaked credentials like API keys and tokens. It uses hundreds of pattern rules and can check whether a detected secret is actually active. You can run it as a command-line tool, use it inside other tools as a Go library, or use it as extensions in Burp Suite or a browser to uncover credential leaks in different workflows.
* [Sirius](https://github.com/SiriusScan/Sirius)
  → It is an open-source vulnerability scanning platform on GitHub that automates network and system security checks to find weaknesses and risks in infrastructure. It combines community-driven security data with automated tests, runs within containers, and gives operators a unified view of vulnerabilities to prioritize remediation.

*Disclaimer: These tools are provided for research and educational use only. They are not security-audited and may cause harm if misused. Review the code, test in controlled environments, and comply with all applicable laws and policies.*

## **Conclusion**

Viewed one by one, these incidents seem contained. Seen together, they show how risk now flows across connected systems that organizations rely on daily. Infrastructure, AI platforms, cloud services, and third-party tools are deeply intertwined, and strain in one area often exposes another.

The takeaway is clarity, not alarm. Adversaries are improving efficiency, scaling access, and operating inside normal processes. Reading through each report helps map that shift and understand how the broader environment is changing.