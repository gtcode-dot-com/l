---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-02T14:15:14.405680+00:00'
exported_at: '2026-02-02T14:15:16.729183+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/weekly-recap-proxy-botnet-office-zero.html
structured_data:
  about: []
  author: ''
  description: This week’s cybersecurity recap highlights key attacks, zero-days,
    and patches to keep you informed and secure.
  headline: '⚡ Weekly Recap: Proxy Botnet, Office Zero-Day, MongoDB Ransoms, AI Hijacks
    & New Threats'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/weekly-recap-proxy-botnet-office-zero.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: '⚡ Weekly Recap: Proxy Botnet, Office Zero-Day, MongoDB Ransoms, AI Hijacks
  & New Threats'
updated_at: '2026-02-02T14:15:14.405680+00:00'
url_hash: 8380739b9d6f1e124ff9174244e208eb2cd283c9
---

**

Ravie Lakshmanan
**

Feb 02, 2026

Hacking News / Cybersecurity

Every week brings new discoveries, attacks, and defenses that shape the state of cybersecurity. Some threats are stopped quickly, while others go unseen until they cause real damage.

Sometimes a single update, exploit, or mistake changes how we think about risk and protection. Every incident shows how defenders adapt — and how fast attackers try to stay ahead.

This week's recap brings you the key moments that matter most, in one place, so you can stay informed and ready for what's next.

## **⚡ Threat of the Week**

**[Google Disrupts IPIDEA Residential Proxy Network](https://thehackernews.com/2026/01/google-disrupts-ipidea-one-of-worlds.html)**
— Google has crippled IPIDEA, a massive residential proxy network consisting of user devices that are being used as the last-mile link in cyberattack chains. According to the tech giant, not only do these networks permit bad actors to conceal their malicious traffic, but they also open up users who enroll their devices to further attacks. Residential IP addresses in the U.S., Canada, and Europe were seen as the most desirable. Google pursued legal measures to seize or sinkhole domains used as command‑and‑control (C2) for devices enrolled in the IPIDEA proxy network, cutting off operators' ability to route traffic through compromised systems. The disruption is assessed to have reduced IPIDEA's available pool of devices by millions. The proxy software is either pre-installed on devices or may be willingly installed by users, lured by the promise of monetizing their available internet bandwidth. Once devices are registered in the residential proxy network, operators sell access to it to their customers. Numerous proxy and VPN brands, marketed as separate businesses, were controlled by the same actors behind IPIDEA. The proxy network also promoted several SDKs as app monetization tools, quietly turning user devices into proxy exit nodes without their knowledge or consent once embedded. IPIDEA has also been linked to
[large-scale brute-forcing attacks](https://thehackernews.com/2024/04/cisco-warns-of-global-surge-in-brute.html)
targeting VPN and SSH services as far back as early 2024. The team from Device and Browser Info has since
[released](https://deviceandbrowserinfo.com/learning_zone/articles/inside-ipidea-residential-proxy-network)
a list of all IPIDEA-linked proxy exit IPs.

## **🔔 Top News**

* **[Microsoft Patches Exploited Office Flaw](https://thehackernews.com/2026/01/microsoft-issues-emergency-patch-for.html)**
  — Microsoft issued out-of-band security patches for a high-severity Microsoft Office zero-day vulnerability exploited in attacks. The vulnerability, tracked as CVE-2026-21509, carries a CVSS score of 7.8 out of 10.0. It has been described as a security feature bypass in Microsoft Office. "Reliance on untrusted inputs in a security decision in Microsoft Office allows an unauthorized attacker to bypass a security feature locally," the tech giant said in an advisory. "This update addresses a vulnerability that bypasses OLE mitigations in Microsoft 365 and Microsoft Office, which protect users from vulnerable COM/OLE controls." Microsoft has not shared any details about the nature and the scope of attacks exploiting CVE-2026-21509.
* **[Ivanti Patches Exploited EPMM Flaws](https://thehackernews.com/2026/01/two-ivanti-epmm-zero-day-rce-flaws.html)**
  — Ivanti rolled out security updates to address two security flaws impacting Ivanti Endpoint Manager Mobile (EPMM) that have been exploited in zero-day attacks. The vulnerabilities, tracked as CVE-2026-1281 and CVE-2026-1340, relate to code injection, allowing attackers to achieve unauthenticated remote code execution. "We are aware of a very limited number of customers whose solution has been exploited at the time of disclosure," Ivanti said in an advisory, adding it does not have enough information about the threat actor tactics to provide "reliable atomic indicators." As of January 30, 2026, a public working proof-of-concept exploit is available. "As EPMM is an endpoint management solution for mobile devices, the impact of an attacker compromising the EPMM server is significant," Rapid7
  [said](https://www.rapid7.com/blog/post/etr-critical-ivanti-endpoint-manager-mobile-epmm-zero-day-exploited-in-the-wild-eitw-cve-2026-1281-1340/)
  . "An attacker may be able to access Personally Identifiable Information (PII) regarding mobile device users, such as their names and email addresses, but also their mobile device information, such as their phone numbers, GPS information, and other sensitive unique identification information."
* **[Poland Links Cyber Attack on Power System to Static Tundra](https://thehackernews.com/2026/01/poland-attributes-december-cyber.html)**
  — The Polish computer emergency response team revealed that coordinated cyber attacks targeted more than 30 wind and photovoltaic farms, a private company from the manufacturing sector, and a large combined heat and power plant (CHP) supplying heat to almost half a million customers in the country. CERT Polska said the incident took place on December 29, 2025, describing the attacks as destructive. The agency attributed the attacks to a threat cluster dubbed Static Tundra, which is also tracked as Berserk Bear, Blue Kraken, Crouching Yeti, Dragonfly, Energetic Bear, Ghost Blizzard (formerly Bromine), and Havex. Static Tundra is assessed to be linked to Russia's Federal Security Service's (FSB) Center 16 unit. Prior reports from ESET and Dragos linked the attack with moderate confidence to a group that shares tactical overlaps with a cluster referred to as Sandworm. The group exhibits a deep understanding of electrical grid equipment and operations, strong proficiency in the industrial protocols used in power systems, and the ability to develop custom malware and wiper tools across IT and OT environments. The activity also reflects the adversary's grasp of substation operations and the operational dependencies within electrical systems. "Taking over these devices requires capabilities beyond simply understanding their technical flaws," Dragos said. "It requires knowledge of their specific implementation. The adversaries demonstrated this by successfully compromising RTUs at approximately 30 sites, suggesting they had mapped common configurations and operational patterns to exploit systematically."
* **[LLMJacking Campaign Targets Exposed AI Endpoints](https://thehackernews.com/2026/01/researchers-find-175000-publicly.html)**
  — Cybercriminals are searching for, hijacking, and monetizing exposed LLM and MCP endpoints at scale. The campaign, dubbed Operation Bizarre Bazaar, targets exposed or unprotected AI endpoints to hijack system resources, resell API access, exfiltrate data, and move laterally to internal systems. "The threat differs from traditional API abuse because compromised LLM endpoints can generate significant costs (inference is expensive), expose sensitive organizational data, and provide lateral movement opportunities," Pillar Security said. Organizations running self-hosted LLM infrastructure (Ollama, vLLM, local AI implementations) or deploying MCP servers for AI integrations face active targeting. Common misconfigurations that are under active exploitation include Ollama running on port 11434 without authentication, OpenAI-compatible APIs on port 8000, MCP servers accessible without access controls, development/staging AI infrastructure with public IPs, and production chatbot endpoints that lack authentication or rate limits. Access to the infrastructure is advertised on a marketplace that offers access to over 30 LLMs. Called silver[.]inc, it is hosted on bulletproof infrastructure in the Netherlands, and marketed on Discord and Telegram, with payments made via cryptocurrency or PayPal.
* **[Chinese Threat Actors Use PeckBirdy Framework](https://thehackernews.com/2026/01/china-linked-hackers-have-used.html)**
  — China-aligned threat actors have been using a cross-platform, multifunction JScript framework called PeckBirdy to conduct cyber espionage attacks since 2023, augmenting their activities with modular backdoors in two separate campaigns targeting gambling sites and government entities. The command-and-control (C2) framework, written in Microsoft's JScript legacy language, is aimed at flexible deployment by enabling execution across multiple environments, including web browsers, MSHTA, WScript, Classic ASP, Node JS, and .NET (ScriptControl).

## **‎️‍🔥 Trending CVEs**

New vulnerabilities surface daily, and attackers move fast. Reviewing and patching early keeps your systems resilient.

Here are this week's most critical flaws to check first —
[CVE-2026-24423](https://thehackernews.com/2026/01/smartermail-fixes-critical.html)
(SmarterTools SmarterMail),
[CVE-2026-1281, CVE-2026-1340](https://thehackernews.com/2026/01/two-ivanti-epmm-zero-day-rce-flaws.html)
(Ivanti Endpoint Manager Mobile),
[CVE-2025-40536, CVE-2025-40537, CVE-2025-40551, CVE-2025-40552, CVE-2025-40553](https://thehackernews.com/2026/01/solarwinds-fixes-four-critical-web-help.html)
(SolarWinds Web Help Desk),
[CVE-2026-22709](https://thehackernews.com/2026/01/critical-vm2-nodejs-flaw-allows-sandbox.html)
(vm2),
[CVE-2026-1470, CVE-2026-0863](https://thehackernews.com/2026/01/two-high-severity-n8n-flaws-allow.html)
(n8n),
[CVE-2026-24858](https://thehackernews.com/2026/01/fortinet-patches-cve-2026-24858-after.html)
(Fortinet FortiOS, FortiManager, FortiAnalyzer, FortiProxy, and FortiWeb),
[CVE-2026-21509](https://thehackernews.com/2026/01/microsoft-issues-emergency-patch-for.html)
(Microsoft Office),
[CVE-2025-30248](https://www.westerndigital.com/support/product-security/wdc-25008-wd-discovery-desktop-app-version-5-3)
,
[CVE-2025-26465](https://www.westerndigital.com/support/product-security/wdc-25009-western-digital-my-cloud-os-5-firmware-5-32-102)
(Western Digital),
[CVE-2025-56005](https://github.com/bohmiiidd/Undocumented-RCE-in-PLY)
(PLY),
[CVE-2026-23864](https://github.com/facebook/react/security/advisories/GHSA-83fc-fqcc-2hmg)
(React Server Components),
[CVE-2025-14756](https://www.tp-link.com/us/support/faq/4916/)
(TP-Link),
[CVE‑2026‑0755](https://blog.amberwolf.com/blog/2026/january/advisory---check-point-harmony-local-privilege-escalation-cve-2025-9142/)
(Google gemini-mcp-tool),
[CVE-2025-9142](https://support.checkpoint.com/results/sk/sk184557)
(Check Point Harmony SASE),
[CVE-2026-1504](https://chromereleases.googleblog.com/2026/01/stable-channel-update-for-desktop_27.html)
(Google Chrome),
[CVE-2025-12556](https://claroty.com/team82/research/new-architecture-new-risks-one-click-to-pwn-idis-ip-cameras)
(IDIS IP cameras),
[CVE-2026-0818](https://www.mozilla.org/en-US/security/advisories/mfsa2026-07/)
(Mozilla Thunderbird),
[CCVE-2025-52598, CVE-2025-52599, CVE-2025-52600, CVE-2025-52601, CVE-2025-8075](https://www.nozominetworks.com/blog/smile-youre-being-hacked-nozomi-networks-labs-finds-five-new-flaws-in-hanwha-wisenet-cameras)
(Hanwha Wisenet cameras),
[CVE-2025-33217, CVE-2025-33218, CVE-2025-33219, CVE-2025-33220](https://nvidia.custhelp.com/app/answers/detail/a_id/5747)
(NVIDIA GPU Display Drivers),
[CVE-2025-0921](https://unit42.paloaltonetworks.com/iconics-suite-cve-2025-0921/)
(Iconics Suite),
[CVE-2025-26385](https://www.cisa.gov/news-events/ics-advisories/icsa-26-027-04)
(Johnson Controls), and
[SRC-2025-0001, SRC-2025-0002](https://srcincite.io/blog/2026/01/28/samstung-part-1-remote-code-execution-in-magicinfo-server.html)
,
[SRC-2025-0003, SRC-2025-0004](https://srcincite.io/blog/2026/01/28/samstung-part-2-remote-code-execution-in-magicinfo-server.html)
(Samsung MagicINFO 9 Server).

## **📰 Around the Cyber World**

* **Exposed C2 Server Reveals BYOB Infrastructure**
  — Cybersecurity researchers have discovered an open directory on a command-and-control (C2) server at IP address 38.255.43[.]60 on port 8081, which has been found serving malicious payloads associated with the Build Your Own Botnet (
  [BYOB](https://hunt.io/malware-families/byob)
  ) framework. "The open directory contained a complete deployment of the BYOB post-exploitation framework, including droppers, stagers, payloads, and multiple post-exploitation modules," Hunt.io
  [said](https://hunt.io/blog/exposed-byob-c2-infrastructure-multi-stage-malware-deployment)
  . "Analysis of the captured samples reveals a modular multi-stage infection chain designed to establish persistent remote access across Windows, Linux, and macOS platforms." The first stage is a dropper that implements multiple layers of obfuscation to evade signature-based detection, while fetching and executing an intermediate loader, which performs a series of security checks of its own before deploying the main remote access trojan (RAT) payload for reconnaissance and persistence. It also comes with capabilities to escalate privileges, log keystrokes, terminate processes, harvest emails, and inspect network traffic. Additional infrastructure linked to the threat actor has been found to host cryptocurrency mining payloads, indicating a two-pronged approach to compromising endpoints with different payloads.
* **Phantom Enigma Resurfaces with New Tactics**
  — The threat actors behind the
  [Operation Phantom Enigma](https://thehackernews.com/2025/06/malicious-browser-extensions-infect-722.html)
  campaign, which targeted Brazilian users in order to steal bank accounts in early 2025,
  [resurfaced](https://ptsecurity.com/research/pt-esc-threat-intelligence/phantom-in-the-flesh-new-attacks-by-phantom-enigma/)
  with similar attacks in fall 2025. The attacks, per Positive Technologies, involve sending phishing emails bearing invoice-related themes to trick ordinary users into clicking on malicious links to download a malicious MSI installer that installs a malicious Google Chrome extension dubbed EnigmaBanker on the victim's browser to collect credentials and transmit them to the attacker's server. The malware is designed to execute JavaScript code that imports a malicious extension via Chrome DevTools Protocol (
  [CDP](https://chromedevtools.github.io/devtools-protocol/)
  ) after launching the browser in debugging mode. On the other hand, the attacks aimed at enterprises drop an installer for legitimate remote access software like PDQ Connect, MeshAgent, ScreenConnect, or Syncro RMM. The threat actors behind the campaign are suspected to be operating out of Latin America.
* **Attackers Exploit Stolen AWS Credentials to Target AWS WorkMail**
  — Threat actors are leveraging compromised Amazon Web Services (AWS) credentials to deploy phishing and spam infrastructure using AWS WorkMail, bypassing the anti-abuse controls normally enforced by AWS Simple Email Service (SES). "This allows the threat actor to leverage Amazon's high sender reputation to masquerade as a valid business entity, with the ability to send email directly from victim-owned AWS infrastructure," Rapid7
  [said](https://www.rapid7.com/blog/post/dr-threat-actors-aws-workmail-phishing-campaigns/)
  . "Generating minimal service-attributed telemetry also makes threat actor activity difficult to distinguish from routine activity. Any organization with exposed AWS credentials and permissive Identity and Access Management (IAM) policies is potentially at risk, particularly those without guardrails or monitoring around WorkMail and SES configuration."
* **Malicious VS Code Extension Delivers Stealer Malware**
  — A malicious Visual Studio Code (VS Code) extension has been identified in Open VSX ("Angular-studio.ng-angular-extension") masquerading as a tool for the Angular web development framework, but harbors functionality that's activated when any HTML or TypeScript file is opened. It's designed to run encrypted JavaScript responsible for fetching the next-stage payload from a URL embedded into the memo field of a
  [Solana wallet](https://solscan.io/account/BjVeAjPrSKFiingBn4vZvghsGj9KCE8AJVtbc9S8o8SC)
  using a technique called
  [EtherHiding](https://thehackernews.com/2025/10/self-spreading-glassworm-infects-vs.html)
  by constructing an RPC request to the Solana mainnet. The infection chain is also engineered such that execution is skipped on systems matching Russian locale indicators. "This pattern is commonly observed in malware originating from or affiliated with Russian-speaking threat actors, implemented to avoid domestic prosecution," Secure Annex
  [said](https://annex.security/blog/worms-lurking/)
  . This architecture offers several advantages: blockchain immutability ensures configuration data persists indefinitely, and attackers can update payload URLs without modifying the published extension. The final payload deployed as part of the attack is a stealer malware that can siphon credentials from developer machines, conduct cryptocurrency theft, establish persistence, and exfiltrate the data to a server retrieved from a Google Calendar event.
* **Threat Actors Exploit Critical Adobe Commerce Flaw**
  — Threat actors are continuing to exploit a critical flaw in Adobe Commerce and Magento Open Source platforms (
  [CVE-2025-54236](https://thehackernews.com/2025/10/over-250-magento-stores-hit-overnight.html)
  , CVSS score: 9.1) to compromise 216 websites worldwide in one campaign, and deploy web shells on Magento sites in Canada and Japan to enable persistent access in another. "While the cases are not assessed to be part of a single coordinated campaign, all incidents demonstrate that the vulnerability is being actively abused for authentication bypass, full system compromise, and, in some cases, web shell deployment and persistent access," Oasis Security
  [said](https://oasis-security.io/blog/260128-Magento-CVE)
  .
* **Malicious Google Ads Leads to Stealer Malware**
  — Sponsored ads on Google when searching for "Mac cleaner" or "clear cache macOS" are being used to
  [redirect](https://mackeeper.com/blog/suspicious-ads-on-google-which-contain-harmful-content-for-mac-users/)
  unsuspecting users to sketchy sites hosted on Google Docs and Medium to trick them into following
  [ClickFix-style instructions](https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html#ai-chat-guides-spread-stealers)
  to deliver stealer malware. In a related development, DHL-themed phishing emails containing ZIP archives are
  [being used](https://medium.com/@mk7912/from-xloader-to-phantom-stealer-a-dhl-themed-multi-stage-infection-chain-5d552eee828d)
  to launch
  [XLoader](https://thehackernews.com/2025/02/cybercriminals-use-eclipse-jarsigner-to.html)
  using DLL side-loading, which then uses process hollowing techniques to load Phantom Stealer.
* **U.S. Authorities Investigated Meta Contractors' Claims that WhatsApp Chats Aren't Private**
  — U.S. law enforcement has been investigating allegations by former Meta contractors that employees at the company can access WhatsApp messages, despite the company's statements that the chat service is private and encrypted. The contractors claimed that some Meta staff had "unfettered" access to WhatsApp messages, content that should be off-limits, Bloomberg
  [reported](https://www.bloomberg.com/news/articles/2026-01-29/us-has-investigated-claims-that-whatsapp-chats-aren-t-private)
  . The report stands in stark contrast to WhatsApp encryption foundations, which prevent third parties, including the company, from accessing the chat contents. "What these individuals claim is not possible because WhatsApp, its employees, and its contractors, cannot access people's encrypted communications," Meta was quoted as saying to Bloomberg. It's worth noting that when a
  [user reports a user or group](https://faq.whatsapp.com/414631957536067/)
  , WhatsApp receives up to five of the last messages sent to them, along with their metadata. This is akin to taking a screenshot of the last few messages, as they are already on the device and in a decrypted state because the device has the "key" to read them. However, these allegations suggest much broader access to the platform.
* **New PyRAT Malware Spotted**
  — A new Python-based remote access trojan (RAT) called PyRAT has been found to demonstrate cross-platform capabilities, persistent infection methods, and extensive remote access features. It supports features like system command execution, file system operations, file enumeration, file upload/download, and archive creation to facilitate bulk exfiltration of stolen data. The malware also comes fitted with self-cleanup capabilities to uninstall itself from the victim machine and wipe all persistence components. "This Python‑based RAT poses a notable risk to organizations because of its cross‑platform capability, broad functionality, and ease of deployment," K7 Security Labs
  [said](https://labs.k7computing.com/index.php/the-pyrat-code-python-based-rat-and-its-internals/)
  . "Even though it is not associated with highly sophisticated threat actors, its effectiveness in real‑world attacks and observed detection rates indicate that it is actively used by cybercriminals and deserves attention." It's currently not known how it's distributed.
* **New Exfil Out&Look Attack Technique Detailed**
  — Cybersecurity researchers have discovered a new technique named Exfil Out&Look that abuses Outlook add-ins to steal data from organizations. "An add-in installed via OWA [Outlook Web Access can be abused to silently extract email data without generating audit logs or leaving any forensic footprint — a stark contrast to the behavior observed in Outlook Desktop," Varonis
  [said](https://www.varonis.com/blog/outlook-add-in-exfiltration)
  . "In organizations that rely heavily on Unified Audit Logs for detection and investigation, this blind spot can allow malicious or overly permissive add-ins to operate undetected for extended periods of time." An attacker could exploit this behavior to trigger an add-in's core functionality when a victim sends an email, allowing it to intercept outgoing messages and send the data to a third-party server. Following responsible disclosure to Microsoft on September 30, 2025, the company categorized the issue as low-severity with no immediate fix.
* **Exposed MongoDB Servers Exploited for Extortion Attacks**
  — Almost half of all internet-exposed MongoDB servers have been compromised and are being held for ransom. An unidentified threat actor has targeted misconfigured instances to drop ransom notes on more than 1,400 databases demanding a Bitcoin payment to restore the data. Flare's analysis found more than 208,500 publicly exposed MongoDB servers, out of which 100,000 expose operational information, and 3,100 could be accessed without authentication. What's more, nearly half (95,000) of all internet-exposed MongoDB servers run older versions that are vulnerable to N-day flaws. "Threat actors demand payment in Bitcoin (often around 0.005 BTC, equivalent today to $500-600 USD) to a specified wallet address, promising to restore the data," the cybersecurity company
  [said](https://flare.io/learn/resources/blog/mongodb-ransom/)
  . "However, there is no guarantee the attackers have the data, or will provide a working decryption key if paid."
* **Deep Dive into Dark Web Forums**
  — Positive Technologies has taken a deep-dive look into modern dark web forums, noting how they are in a constant state of flux due to ramping up of law enforcement operations, even as they embrace anonymity and protection technologies like Tor, I2P, coupled with anti-bot guardrails, anti-scraping mechanisms, closed moderation, and a strict trust system to escape scrutiny and block suspicious activity. "However, the results of these interventions are rarely final: the elimination of one forum usually becomes the starting point for the emergence of a new, more sustainable and secure one," it
  [said](https://ptsecurity.com/research/analytics/trust-infrastructure-the-evolution-of-dark-forum-security-and-its-economics/#id3)
  . "And an important feature of such forums is the high level of development of technical means of protection. If the early generations of dark web forums were primitive web platforms that often existed in the public part of the internet, modern forums are complex distributed systems with multi-level infrastructure, APIs, moderator bots, built-in verification tools and a multi-stage access system."
* **TA584 Campaign Drops XWorm and Tsundere Bot**
  — A prolific initial access broker known as TA584 (aka
  [Storm-0900](https://thehackernews.com/2025/12/threatsday-bulletin-wi-fi-hack-npm-worm.html#phishing-blitz-blocked)
  ) has been observed using the
  [Tsundere Bot](https://thehackernews.com/2025/11/tsundere-botnet-expands-using-game.html)
  alongside
  [XWorm](https://thehackernews.com/2025/10/xworm-60-returns-with-35-plugins-and.html)
  remote access trojan to gain network access for likely follow-on ransomware attacks. The XWorm malware uses a configuration called "P0WER" to enable its execution. "In the second half of 2025, TA584 demonstrated multiple attack chain changes, including adopting
  [ClickFix](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)
  social engineering, expanded targeting to more consistently target specific geographies and languages, and recently delivering a new malware called Tsundere Bot," Proofpoint
  [said](https://www.proofpoint.com/us/blog/threat-insight/cant-stop-wont-stop-ta584-innovates-initial-access)
  . The threat actor is assessed to be active since at least 2020, but has exhibited an increased operational tempo since March 2025. Organizations in North America, the U.K., Ireland, and Germany are the main targets. Emails sent by TA584 impersonate various organizations associated with healthcare and government entities, as well as leverage well-designed and believable lures to get people to engage with malicious content. These messages are sent via compromised accounts or third-party services like SendGrid and Amazon Simple Email Service (SES). "The emails usually contain unique links for each target that perform geofencing and IP filtering," Proofpoint said. "If these checks were passed, the recipient is redirected to a landing page aligning with the lure in the email." Early iterations of the campaign delivered macro-enabled Excel documents dubbed EtterSilent to facilitate malware installation. The end goal of the attack is to initiate a redirect chain involving third-party traffic direction systems (TDS) like Keitaro to a CAPTCHA page, followed by a ClickFix page that instructs the victim to run a PowerShell command on their system. Some of the other payloads distributed by TA584 in the past include Ursine, TA584, WARMCOOKIE, Xeno RAT, Cobalt Strike, and DCRat.
* **South Korea to Notify Citizens of Data Leaks**
  — The South Korean government
  [will notify](https://koreajoongangdaily.joins.com/news/2026-01-28/national/socialAffairs/Govt-to-notify-people-of-possible-data-leaks-not-just-confirmed-cases/2510657)
  citizens when their data was exposed in a security breach. The new notification system will cover confirmed breaches, but also alert people who may be involved in a data breach, even if the case has not been confirmed. These alerts will also include information on how to seek compensation for damages.
* **Details About Critical Apache bRPC Flaw**
  — CyberArk has published details about a recently patched critical vulnerability in Apache bRPC (CVE-2025-60021, CVSS score: 9.8) that could allow an attacker to inject remote commands. The problem resides in the "/pprof/heap" profiler endpoint. "The heap profiler service /pprof/heap did not validate the user-provided extra\_options parameter before incorporating it into the jeprof command line,' CyberArk
  [said](https://www.cyberark.com/resources/threat-research-blog/cve-2025-60021-cvss-9-8-command-injection-in-apache-brpc-heap-profiler)
  . "Prior to the fix, extra\_options was appended directly to the command string as –<user\_input>. Because this command is later executed to generate the profiling output, shell special characters in attacker-controlled input could alter the executed command, resulting in command injection." As a result, an attacker could exploit a reachable "/pprof/heap" endpoint to execute arbitrary commands with the privileges of the Apache bRPC process, resulting in remote code execution. There are about 181 publicly reachable /pprof/heap endpoints and 790 /pprof/\* endpoints, although it's not known how many of them are susceptible to this flaw.
* **Threat Actors Use New Unicode Trick to Evade Detection**
  — Threat actors are using the Unicode character for math division (∕) instead of a standard forward slash (/) in malicious links to evade detection. "The barely noticeable difference between the divisional and forward slashes causes traditional automated security systems and filters to fail, allowing the links to bypass detection," email security firm Barracuda
  [said](https://blog.barracuda.com/2026/01/22/email-threat-radar-january-2026)
  . "As a result, victims are redirected to default or random pages."
* **China Executes 11 Members of Myanmar Scam Mafia**
  — The Chinese government has
  [executed](https://www.bbc.com/news/articles/cd6wegndnjlo)
  11 members of the Ming family who ran cyber scam compounds in Myanmar. The suspects were sentenced in September 2025 following their arrest in 2023. In November 2025, five members of a Myanmar crime syndicate were
  [sentenced to death](https://thehackernews.com/2025/11/threatsday-bulletin-ai-tools-in-malware.html#china-delivers-harsh-verdict-in-cross-border-scam-crackdown)
  for their roles in running industrial-scale scamming compounds near the border with China. The Ming mafia's scam operations and gambling dens brought in more than $1.4 billion between 2015 and 2023, BBC News
  [reported](https://www.bbc.com/news/articles/cx2gdrvy9gjo)
  , citing China's highest court.
* **FBI Urges Organizations to Improve Cybersecurity**
  — The U.S. Federal Bureau of Investigation (FBI) launched Operation Winter SHIELD (short for "Securing Homeland Infrastructure by Enhancing Layered Defense"), outlining ten actions which organizations should implement to improve cyber resilience. This includes adopting phishing-resistant authentication, implementing a risk-based vulnerability management program, retiring end-of-life technology, managing third-party risk, preserving security logs, maintaining offline backups, inventorying internet-facing systems and services, strengthening email authentication, reducing administrator privileges, and executing incident response plans with all stakeholders. "Winter SHIELD provides industry with a practical roadmap to better secure information technology (IT) and operational technology (OT) environments, hardening the nation's digital infrastructure and reducing the attack surface," the FBI
  [said](https://www.fbi.gov/investigate/cyber/wintershield)
  . "Our goal is simple: to move the needle on resilience across industry by helping organizations understand where adversaries are focused and what concrete steps they can take now (and build toward in the future) to make exploitation harder."
* **Only 26% of Vulnerability Attacks Blocked by Hosts**
  — A new study by website security firm PatchStack has revealed that a significant majority of common WordPress-specific vulnerabilities are not mitigated by hosting service providers. In a test using 30 vulnerabilities that were known to be exploited in real-world attacks, the company found that 74% of all attacks resulted in a successful site takeover. "Of the high-impact vulnerabilities, Privilege Escalation attacks were blocked only 12% of the time," Patchstack
  [said](https://patchstack.com/articles/myth-of-secure-hosting-only-24-percent-of-vulnerability-exploits-blocked-by-hosts/)
  . "The biggest problem isn't that hosts don't care about vulnerability attacks – it's that they think their existing solutions have got them covered."
* **Cyber Attacks Became More Distributed in 2025**
  — Forescout's Threat Roundup report for 2025 has found that cyber attacks became more globally distributed and cloud-enabled. "In 2025, the top 10 countries accounted for 61% of malicious traffic - a 22% decrease compared to 2024 – and a reversal of a trend observed since 2022, when that figure was 73%," Forescout
  [said](https://www.forescout.com/blog/2025-threat-report-exploitation-grows-across-it-iot-and-ot/)
  . "In other words, attacks are more distributed and attackers are using IP addresses from less common countries more frequently." The U.S., India, and Germany were the most targeted countries, with 59% of the attacks originating from ISP-managed IPs, 17% from business and government networks, and 24% from hosting or cloud providers. The vast majority of the attacks originated from China, Russia, and Iran. Attacks using OT protocols surged by 84%, led by Modbus. The development comes as Cisco Talos
  [revealed](https://blog.talosintelligence.com/ir-trends-q4-2025/)
  that threat actors are increasingly exploiting public-facing applications, overtaking phishing in the last quarter of 2025.
* **Google Agrees to Settle Privacy Lawsuit for $68M**
  — Google has
  [agreed](https://www.reuters.com/sustainability/boards-policy-regulation/google-settles-google-assistant-privacy-lawsuit-68-million-2026-01-26/)
  to pay $68 million to settle a class-action lawsuit alleging its voice-activated assistant illegally recorded and shared the private conversations with third parties without their consent. The case revolved around "false accepts," where Google Assistant is said to have activated and recorded the user's communications even in scenarios where the actual trigger word, "Ok Google," was not used. Google has denied any wrongdoing. Apple reached a
  [similar $95 million settlement](https://thehackernews.com/2025/01/apple-to-pay-siri-users-20-per-device.html)
  in December 2024 over Siri recordings. Separately, Google has agreed to
  [pay $135 million](https://www.reuters.com/sustainability/boards-policy-regulation/google-pay-135-million-settle-android-data-transfer-lawsuit-2026-01-28/)
  to settle a proposed class-action lawsuit that accused the company of illegally using users' cellular data to
  [transmit system information to its servers](https://thehackernews.com/2025/07/google-ordered-to-pay-314m-for-misusing.html)
  without the user's knowledge or consent since November 12, 2017. As part of the settlement, Google will not transfer data without obtaining consent from Android users when they set up their phones. It will also make it easier for users to stop the transfers, and will disclose the transfers in its Google Play terms of service. The development follows a U.S. Supreme Court
  [decision](https://www.supremecourt.gov/docket/docketfiles/html/public/25-459.html)
  to hear a case stemming from the use of a Facebook tracking pixel to monitor the streaming habits of users of a sports website.
* **Security Flaws in Google Fast Pair protocol**
  — More than a dozen headphone and speaker models have been found vulnerable to a new vulnerability (CVE-2025-36911, CVSS score: 7.1) in the Google Fast Pair protocol. Called
  [WhisperPair](https://whisperpair.eu)
  , the
  [attack](https://www.wired.com/story/google-fast-pair-bluetooth-audio-accessories-vulnerability-patches/)
  allows threat actors to hijack a user's accessories without user interaction. In certain scenarios, the attackers can also register as the owners of those accessories and track the movement of the real owners via the Google Find Hub. Google awarded the researchers $15,000 following responsible disclosure in August 2025. "WhisperPair enables attackers to forcibly pair a vulnerable Fast Pair accessory (e.g., wireless headphones or earbuds) with an attacker-controlled device (e.g., a laptop) without user consent," researchers at the COSIC group of KU Leuven said. "This gives an attacker complete control over the accessory, allowing them to play audio at high volumes or record conversations using the microphone. This attack succeeds within seconds (a median of 10 seconds) at realistic ranges (tested up to 14 metres) and does not require physical access to the vulnerable device." In related news, an information leak vulnerability (CVE-2025-13834) and a denial-of-service (DoS) vulnerability (CVE-2025-13328) have been uncovered in Xiaomi Redmi Buds versions 3 Pro through 6 Pro. "An attacker within Bluetooth radio range can send specially crafted RFCOMM protocol interactions to the device's internal channels without prior pairing or authentication, enabling the exposure of sensitive call-related data or triggering repeatable firmware crashes," CERT Coordination Center (CERT/CC)
  [said](https://kb.cert.org/vuls/id/472136)
  .

## **🎥 Cybersecurity Webinars**

* **[Your SOC Stack Is Broken — Here's How to Fix It Fast](https://thehacker.news/modern-soc?source=recap)
  :**
  Modern SOC teams are drowning in tools, alerts, and complexity. This live session with AirMDR CEO Kumar Saurabh and SACR CEO Francis Odum cuts through the noise—showing what to build, what to buy, and what to automate for real results. Learn how top teams design efficient, cost-effective SOCs that actually work. Join now to make smarter security decisions.
* **[AI Is Rewriting Cloud Forensics — Learn How to Investigate Faster](https://thehacker.news/forensics-reimagined?source=recap)
  :**
  Cloud investigations are getting harder as evidence disappears fast and systems change by the minute. Traditional forensics can't keep up. Join Wiz's experts to see how AI and context-aware forensics are transforming cloud incident response—helping teams capture the right data automatically, connect the dots faster, and uncover what really happened in minutes instead of days.
* **[Build Your Quantum-Safe Defense: Get Guidance for IT Leaders](https://thehacker.news/post-quantum-cryptography?source=recap)
  :**
  Quantum computers could soon break the encryption that protects today's data. Hackers are already stealing encrypted information now to decrypt it later. Join this Zscaler webinar to learn how post-quantum cryptography keeps your business safe—using hybrid encryption, zero trust, and quantum-ready security tools built for the future.

## **🔧 Cybersecurity Tools**

* [Vulnhalla](https://github.com/cyberark/Vulnhalla)
  : CyberArk open-sources a new tool that automates vulnerability triage by combining CodeQL analysis with AI models like GPT-4 or Gemini. It scans public code repositories, runs CodeQL queries to find potential issues, and then uses AI to decide which ones are real security flaws versus false positives. This helps developers and security teams quickly focus on genuine risks instead of wasting time sorting through noisy scan results.
* [OpenClaw](https://github.com/cloudflare/moltworker)
  : A personal AI assistant running in Cloudflare Workers, connecting to Telegram, Discord, and Slack with secure device pairing. It uses Claude via Anthropic API and optional R2 storage for persistence—showcasing how AI agents can run safely in a sandboxed, serverless Cloudflare setup.

*Disclaimer: These tools are provided for research and educational use only. They are not security-audited and may cause harm if misused. Review the code, test in controlled environments, and comply with all applicable laws and policies.*

## **Conclusion**

Cybersecurity keeps moving fast. This week's stories show how attacks, defenses, and discoveries keep shifting the balance. Staying secure now means staying alert, reacting fast, and knowing what's changing around you.

The past few days proved that no one is too small to be a target and no system is ever fully safe. Every patch, every update, every fix counts — because threats don't wait.

Keep learning, stay cautious, and keep your guard up. The next wave of attacks is already forming.