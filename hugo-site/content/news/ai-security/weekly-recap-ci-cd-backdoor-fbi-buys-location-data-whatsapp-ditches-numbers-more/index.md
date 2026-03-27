---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-27T00:15:17.196810+00:00'
exported_at: '2026-03-27T00:15:19.755108+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/weekly-recap-cicd-backdoor-fbi-buys.html
structured_data:
  about: []
  author: ''
  description: Trivy backdoored, FBI buys location data, iOS DarkSword kit, WhatsApp
    usernames, Langflow RCE, Cisco FMC zero-day & critical CVEs to patch.
  headline: '⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches
    Numbers & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/weekly-recap-cicd-backdoor-fbi-buys.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: CI/CD Backdoor, FBI Buys Location Data, WhatsApp Ditches Numbers
  & More'
updated_at: '2026-03-27T00:15:17.196810+00:00'
url_hash: 36acbbb403efbc3699ffe5a14782b5921648b744
---

**

Ravie Lakshmanan
**

Mar 23, 2026

Cybersecurity / Hacking

Another week, another reminder that the internet is still a mess. Systems people thought were secure are being broken in simple ways, showing many still ignore basic advisories.

This edition covers a mix of issues: supply chain attacks hitting CI/CD setups, long-abused IoT devices being shut down, and exploits moving quickly from disclosure to real attacks. There are also new malware tricks showing attackers are becoming more patient and creative.

It’s a mix of old problems that never go away and new methods that are harder to detect. There are quiet state-backed activities, exposed data from open directories, growing mobile threats, and a steady stream of zero-days and rushed patches.

Grab a coffee, and at least skim the CVE list. Some of these are the kind you don’t want to discover after the damage is done.

## **⚡ Threat of the Week**

**[Trivy Vulnerability Scanner Breached in for Supply Chain Attack](https://thehackernews.com/2026/03/trivy-hack-spreads-infostealer-via.html)**
— Attackers have
[backdoored](https://labs.boostsecurity.io/articles/20-days-later-trivy-compromise-act-ii/)
the widely used open-source Trivy vulnerability scanner, injecting credential-stealing malware into official releases and GitHub Actions used by thousands of CI/CD workflows. The breach has triggered a cascade of additional supply-chain compromises stemming from impacted projects and organizations not rotating their secrets, resulting in the distribution of a self-propagating worm referred to as CanisterWorm. Trivy, developed by Aqua Security, is one of the most widely used open-source vulnerability scanners, with over 32,000 GitHub stars and more than 100 million Docker Hub downloads. The Trivy compromise is the latest in a growing pattern of attacks targeting GitHub Actions and developers in general. GitHub
[changed](https://github.blog/changelog/2025-11-07-actions-pull_request_target-and-environment-branch-protections-changes/)
the default behavior of pull\_request\_target workflows in December 2025 to reduce the risk of exploitation.

## **🔔 Top News**

* **[DoJ Takes Down DDoS Botnets](https://thehackernews.com/2026/03/doj-disrupts-3-million-device-iot.html)**
  — A cluster of IoT botnets behind some of the largest DDoS attacks ever recorded --
  [AISURU](https://www.cloudflare.com/threat-intelligence/research/report/aisuru-botnet/)
  ,
  [Kimwolf](https://www.cloudflare.com/learning/ddos/glossary/aisuru-kimwolf-botnet/)
  , JackSkid, and Mossad -- were wiped as part of a broad law enforcement operation. The botnets largely spread across routers, IP cameras, and digital video recorders that are often shipped with weak credentials and rarely patched. Authorities removed the command-and-control servers used to commandeer the infected nodes. Together, operators of the four botnets had amassed more than 3 million devices, which they then sold access to other criminal hackers, who then used them to target victims with DDoS attacks to knock websites and internet services offline or mask other illicit activity. Some of these DDoS attacks were aimed at U.S. Department of Defense systems and other high-value targets. No arrests were announced, but two suspects associated with AISURU/Kimwolf are said to be based in Canada and Germany. All four botnets disrupted by the operation are variants of Mirai, which had its source code leaked in 2016 and has served as the starting point for other botnets. The U.S. Justice Department said some victims of the DDoS attacks lost hundreds of thousands of dollars through remediation expenses or ransom demands from hackers who would only stop overloading websites for a price.
* **[Google Debuts New Advanced Flow for Sideloading on Android](https://thehackernews.com/2026/03/google-adds-24-hour-wait-for-unverified.html)**
  — Google's advanced flow for Android changes how apps from unverified developers are installed, adding friction to combat scams and malware. The feature is aimed at experienced users and allows sideloading through a one-time setup. The advanced flow adds a 24-hour delay and verification steps intended to disrupt coercive pressure and give users time to make decisions. It’s designed to address scenarios where attackers pressure individuals to install unsafe software and play on the urgency of the operation to push them to bypass security warnings and disable protections before they can pause or seek help.
* **[Critical Langflow Flaw Comes Under Attack](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html)**
  — A critical security flaw impacting Langflow has come under active exploitation within 20 hours of public disclosure, highlighting the speed at which threat actors weaponize newly published vulnerabilities. The security defect, tracked as CVE-2026-33017 (CVSS score: 9.3), is a case of missing authentication combined with code injection that could result in remote code execution. Cloud security firm Sysdig said that the attacks weaponize the vulnerability to steal sensitive data from compromised systems. "The real-world proof is definitive: threat actors exploited it in the wild within 20 hours of the advisory going public, with no public PoC code available," Aviral Srivastava, who discovered the vulnerability, told The Hacker News. "They built working exploits just from reading the advisory description. That's the hallmark of trivial exploitation when multiple independent attackers can weaponize a vulnerability from a description alone, within hours."
* **[Interlock Ransomware Exploited Cisco FMC Flaw as 0-Day](https://thehackernews.com/2026/03/interlock-ransomware-exploits-cisco-fmc.html)**
  — An Interlock ransomware campaign exploited a critical security flaw in Cisco Secure Firewall Management Center (FMC) Software as a zero-day well over a month before it was publicly disclosed. The vulnerability in question is CVE-2026-20131 (CVSS score: 10.0), a case of insecure deserialization of user-supplied Java byte stream, which could allow an unauthenticated, remote attacker to bypass authentication and execute arbitrary Java code as root on an affected device. "This wasn't just another vulnerability exploit; Interlock had a zero-day in their hands, giving them a week's head start to compromise organizations before defenders even knew to look," Amazon, which spotted the activity, said.
* **[Yet Another iOS Exploit Kit Comes to Light](https://thehackernews.com/2026/03/darksword-ios-exploit-kit-uses-6-flaws.html)**
  — A new watering hole attack against iPhone users has been found to deliver a previously undocumented iOS exploit kit codenamed DarkSword. While some of the attacks targeted users in Ukraine, the kit has also been put to use by two other clusters that singled out Saudi Arabian users in November 2025, as well as users in Turkey and Malaysia. It's worth noting that these exploits would not be effective on devices where Lockdown Mode is active or on the iPhone 17 with Memory Integrity Enforcement (MIE) enabled. The kit used a total of six exploits in iOS to deliver various malware families designed for surveillance and intelligence gathering. Apple has since addressed all of them. "Completely written in JavaScript, DarkSword comprises six vulnerabilities across two exploit chains that were patched in stages ending with iOS 26.3," iVerify said. "Starting in WebKit and moving down to the kernel, it achieves full iPhone compromise with elegant techniques never publicly seen before." The discovery of DarkSword makes it the
  [second mass attack](https://arstechnica.com/security/2026/03/hundreds-of-millions-of-iphones-can-be-hacked-with-a-new-tool-found-in-the-wild/)
  targeting iOS devices. What's more, the Russian threat actor that deployed DarkSword demonstrated poor operational security. They left the full JavaScript code unobfuscated, unprotected, and easily accessible. The findings also point to a secondary market where such exploits are being acquired by threat actors of varied motivations to actively infect unpatched iOS users on a large scale.
* **[Perseus Banking Malware Targets Android](https://thehackernews.com/2026/03/new-perseus-android-banking-malware.html)**
  — A newly discovered Android malware is masking itself within television streaming apps in order to steal users' passwords and banking data and spy on their personal notes, researchers have found. The malware, dubbed Perseus by researchers at ThreatFabric, is being actively distributed in the wild and primarily targets users in Turkey and Italy. To infect devices, attackers disguise the malware inside apps that appear to offer IPTV services — platforms that stream television content over the internet. These apps are also widely used to stream pirated content and are often downloaded outside official marketplaces like Google Play, making users more accustomed to installing them manually and less likely to view the process as suspicious. Once installed, Perseus can monitor nearly everything a user does in real time. It uses overlay attacks — placing fake login screens over legitimate apps — and keylogging capabilities to capture credentials as they are entered. The malware's most unusual feature is its focus on personal note-taking applications. "Notes often contain sensitive information such as passwords, recovery phrases, financial details, or private thoughts, making them a valuable target for attackers," ThreatFabric said.

## **‎️‍🔥 Trending CVEs**

New vulnerabilities show up every week, and the window between disclosure and exploitation keeps getting shorter. The flaws below are this week's most critical — high-severity, widely used software, or already drawing attention from the security community.

Check these first, patch what applies, and don't wait on the ones marked urgent —
[CVE-2026-21992](https://thehackernews.com/2026/03/oracle-patches-critical-cve-2026-21992.html)
(Oracle),
[CVE-2026-33017](https://thehackernews.com/2026/03/critical-langflow-flaw-cve-2026-33017.html)
(Langflow),
[CVE-2026-32746](https://thehackernews.com/2026/03/critical-telnetd-flaw-cve-2026-32746.html)
(GNU InetUtils telnetd),
[CVE-2026-32297, CVE-2026-32298](https://thehackernews.com/2026/03/9-critical-ip-kvm-flaws-enable.html)
(Angeet ES3 KVM),
[CVE-2026-3888](https://thehackernews.com/2026/03/ubuntu-cve-2026-3888-bug-lets-attackers.html)
(Ubuntu),
[CVE-2026-20643](https://thehackernews.com/2026/03/apple-fixes-webkit-vulnerability.html)
(Apple WebKit),
[CVE-2026-4276](https://kb.cert.org/vuls/id/624941)
(LibreChat RAG API),
[CVE-2026-24291](https://www.mdsec.co.uk/2026/03/rip-regpwn/)
aka RegPwn (Microsoft Windows),
[CVE-2026-21643](https://bishopfox.com/blog/cve-2026-21643-pre-authentication-sql-injection-in-forticlient-ems-7-4-4)
(Fortinet FortiClient),
[CVE-2026-3864](https://github.com/kubernetes/kubernetes/issues/137797)
(Kubernetes),
[CVE-2026-32635](https://github.com/angular/angular/security/advisories/GHSA-g93w-mfhg-p222)
(Angular),
[CVE-2026-25769](https://hakaisecurity.io/cve-2026-25769-rce-via-insecure-deserialization-in-wazuh-cluster-remote-command-execution-through-cluster-protocol/research-blog/)
(
[Wazuh](https://github.com/wazuh/wazuh/security/advisories/GHSA-3gm7-962f-fxw5)
),
[CVE-2026-3564](https://www.connectwise.com/company/trust/security-bulletins/2026-03-17-screenconnect-bulletin)
(ConnectWise ScreenConnect),
[CVE-2026-22557, CVE-2026-22558](https://community.ui.com/releases/Security-Advisory-Bulletin-062-062/c29719c0-405e-4d4a-8f26-e343e99f931b)
(Ubiquiti),
[CVE-2025-14986](https://depthfirst.com/post/the-masked-namespace-vulnerability-in-temporal-cve-2025-14986)
(Temporal),
[CVE-2026-31381, CVE-2026-31382](https://www.rapid7.com/blog/post/ve-cve-2026-31381-cve-2026-31382-gainsight-assist-information-disclosure-xss-fixed/)
(Gainsight Assist),
[CVE-2026-26189](https://github.com/aquasecurity/trivy-action/security/advisories/GHSA-9p44-j4g5-cfx5)
(Trivy),
[CVE-2026-4439, CVE-2026-4440, CVE-2026-4441](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_18.html)
(Google Chrome),
[CVE-2026-33001, CVE-2026-33002](https://www.jenkins.io/security/advisory/2026-03-18/)
(Jenkins),
[CVE-2026-21570](https://confluence.atlassian.com/security/security-bulletin-march-17-2026-1721271371.html)
(Atlassian Bamboo Center), and
[CVE-2026-21884](https://confluence.atlassian.com/security/security-bulletin-march-17-2026-1721271371.html)
(Atlassian Crowd Data Center).

**🎥 Cybersecurity Webinars**

* [Learn How to Automate Exposure Management with OpenCTI & OpenAEV](https://thehacker.news/automate-testing-security-posture?source=recap)
  → Discover how to automate continuous, threat-informed testing using open-source tools like OpenCTI and OpenAEV to validate your security controls against real attacker behavior without increasing your budget. See a live demo on how to verify your security works, identify real gaps, and integrate it into your SOC workflow at no extra cost.
* [Identity Maturity Cracking in 2026: See the New Data + How to Catch Up Fast](https://thehacker.news/identity-maturity-2026?source=recap)
  → Identity programs are under massive pressure in 2026 - disconnected apps, AI agents, and credential sprawl are creating real risks and audit challenges. Join this webinar for new Ponemon Institute 2026 research from over 600 leaders, showing the scale of the problem and practical steps to close gaps, reduce friction, and catch up quickly.

## **📰 Around the Cyber World**

* **WhatsApp Tests Usernames Instead of Phone Numbers**
  — WhatsApp is planning to introduce usernames and unique IDs instead of phone numbers, allowing users to send messages and make voice or video calls without sharing numbers. The optional privacy feature is expected to roll out globally by June 2026, with users and businesses able to reserve unique handles. "We're excited to bring usernames to WhatsApp in the future to help people connect with new friends, groups, and businesses without having to share their phone numbers," the company
  [said](https://economictimes.indiatimes.com/tech/technology/whatsapp-to-introduce-usernames-by-mid-2026-allowing-messaging-without-phone-numbers/articleshow/129685847.cms)
  in a statement shared with The Economic Times. The feature has been under test since early January 2026. Signal
  [introduced](https://thehackernews.com/2024/02/signal-introduces-usernames-allowing.html)
  a similar feature in early 2024.
* **FBI Details SE Asia Scam Centers**
  — The U.S. Federal Bureau of Investigation (FBI) detailed its work with Thai authorities to shut down
  [scam centers](https://www.secretservice.gov/newsroom/behind-the-shades/2026/01/inside-our-nationwide-crackdown-card-skimming-and-fraud)
  proliferating in Southeast Asia. The schemes, which primarily target retirees, small-business owners, and people seeking companionship, have been described as a blend of cyber fraud, money laundering, and human trafficking, causing billions of dollars in annual losses. These scam centers operate in a manner that's similar to how legitimate corporations do. "Recruiters advertise high-paying jobs abroad. Workers are flown to foreign countries only to discover that the positions do not exist," the FBI
  [said](https://www.fbi.gov/news/stories/fbi-in-thailand-working-with-partners-to-shut-down-regions-scam-centers-that-target-americans)
  . "Passports are confiscated. Armed guards patrol the grounds. Under threat of violence, workers are forced to pose as potential romantic partners or savvy investment advisers, cultivating trust with victims over weeks or months." Recent crackdowns in countries like Cambodia have freed thousands of workers from scam compounds, but the FBI warned that these breakthroughs can be temporary, as criminal networks always tend to relocate, rebrand, or shift tactics in response to law enforcement actions.
* **APT28 Exposed Server Leaks SquirrelMail XSS Payload**
  — A second exposed open directory discovered on a server ("
  [203.161.50[.]145](https://thehackernews.com/2026/03/weekly-recap-chrome-0-days-router.html#:~:text=Roundcube%20Exploitation%20Toolkit%20Discovered)
  ") associated with APT28 (aka Fancy Bear) has offered insights into the threat actor's espionage campaigns targeting government and military organizations across Ukraine, Romania, Bulgaria, Greece, Serbia, and North Macedonia. According to
  [Ctrl-Alt-Intel](https://ctrlaltintel.com/threat%20research/FancyBear/)
  , the directory contained command-and-control (C2) source code, scripts to steal emails, credentials, address books, and 2FA tokens from Roundcube mailboxes, telemetry logs, and exfiltrated data. The stolen data consists of 2,870 emails from government and military mailboxes, 244 sets of stolen credentials, 143 Sieve forwarding rules (to silently forward every incoming email to an attacker-controlled mailbox), and 11,527 contact email addresses. One of the newly identified tools is an XSS payload targeting the SquirrelMail webmail software, highlighting the threat actor's continued focus on leveraging XSS flaws to steal data from email inboxes. It's worth noting that the server was
  [attributed](https://thehackernews.com/2024/10/cert-ua-identifies-malicious-rdp-files.html)
  to APT28 by the Computer Emergency Response Team of Ukraine (CERT-UA) as far back as September 2024. "Fancy Bear developed a modular, multi-platform exploitation toolkit where a victim simply opening a malicious email – with no further clicks – could result in their credentials stolen, their 2FA bypassed, emails within their mailbox exfiltrated, and a silent forwarding rule established that persists indefinitely," Ctrl-Alt-Intel said.
* **Analysis of a Beast Ransomware Server**
  — An
  [analysis](https://www.team-cymru.com/post/beast-ransomware-server-toolkit-analysis)
  of an open directory on a server ("5.78.84[.]144") associated with Beast, a ransomware-as-a-service (RaaS) that's suspected to be the successor to Monster ransomware, has uncovered the various tools used by the threat actors and the different stages of their attack lifecycle. These included Advanced IP Scanner and Advanced Port Scanner to map internal networks and find open remote desktop protocol (RDP) or server message block (SMB) ports. Also identified were programs to locate sensitive files for exfiltration and flag which servers hold the most data, as well as Mimikatz, LaZagne, and Automim (for credential harvesting), AnyDesk (for persistence), PsExec (for lateral movement), and MEGASync (for data exfiltration). Beast ransomware operations paused in November 2025 and resumed in January 2026.
* **GrapheneOS Opposes the Unified Attestation Initiative**
  — GrapheneOS has come out strongly against
  [Unified Attestation](https://uattest.net/)
  , stating it "serves no truly useful purpose beyond giving itself an unfair advantage while pretending it has something to do with security." The Unified Attestation initiative is an open-source, decentralized alternative to the Google Play Integrity API to provide device and app integrity checks for custom ROMs without requiring Google Play Services. "We strongly oppose the Unified Attestation initiative and call for app developers supporting privacy, security, and freedom on mobile to avoid it," GraphenseOS said. "Companies selling phones should not be deciding which operating systems people are allowed to use for apps."
* **VoidStealer Uses Chrome Debugger to Steal Secrets**
  — An information stealer known as VoidStealer has observed using a novel debugger-based Application-Bound Encryption (
  [ABE](https://thehackernews.com/2024/08/google-chrome-adds-app-bound-encryption.html)
  ) bypass technique that leverages hardware breakpoints to extract the "v20\_master\_key" directly from browser memory and use it to decrypt sensitive data stored in the browser. VoidStealer is a malware-as-a-service (MaaS) infostealer that began being marketed on several dark web forums in mid-December 2025. The ABE bypass technique was introduced in version 2.0 of the stealer announced on March 13, 2026. "The bypass requires neither privilege escalation nor code injection, making it a stealthier approach compared to alternative ABE bypass methods," Gen Digital
  [said](https://www.gendigital.com/blog/insights/research/voidstealer-abe-bypass)
  . VoidStealer is assessed to have adopted the technique from the open-source
  [ElevationKatz](https://github.com/Meckazin/ChromeKatz/tree/main/ElevationKatz)
  project.
* **FBI Says it is Buying Americans' location Data**
  — FBI director Kash Patel admitted that the agency is buying location data that can be used to track people's movements without a warrant. "We do purchase commercially available information that’s consistent with the Constitution and the laws under the Electronic Communications Privacy Act, and it has led to some valuable intelligence for us," Patel
  [said](https://www.politico.com/news/2026/03/18/fbi-buying-data-track-people-patel-00834080)
  at a hearing before the Senate Intelligence Committee.
* **Iranian Botnet Exposed via Open Directory**
  — An Open Directory on "185.221.239[.]162:8080" has been found to contain several payloads, including a Python-based botnet script, a compiled DDoS binary, multiple C-language denial-of-service files, and IP addresses associated with SSH credentials. "A Python script called ohhhh.py reads credentials in a host:port|username|password format and opens 500 concurrent SSH sessions, compiling and launching the bot client on each host automatically," Hunt.io
  [said](https://hunt.io/blog/iran-botnet-operation-open-directory)
  . "The exposed .bash\_history captured three distinct phases of work: standing up the tunnel network, building and testing DDoS tooling against live targets, and iterative botnet development across multiple script versions." The activity has not been linked to any state-directed campaign.
* **OpenClaw Developers Targeted in Phishing Attack**
  — OpenClaw's combination of flexibility, local control, and a fast-growing ecosystem has made it popular among developers in a very short time. While that unprecedented adoption speed has exposed organizations to new security risks of its own (i.e., vulnerabilities and the presence of malicious skills on ClawHub and SkillsMP), threat actors are also capitalizing on the brand name and reputation to set up fake GitHub accounts for a phishing campaign that lures unsuspecting developers with promises of free $CLAW tokens and trick them into connect their cryptocurrency wallet. "The threat actor creates fake GitHub accounts, opens issue threads in attacker-controlled repositories, and tags dozens of GitHub developers," OX Security researchers Moshe Siman Tov Bustan and Nir Zadok
  [said](https://www.ox.security/blog/openclaw-github-phishing-crypto-wallet-attack/)
  . "The posts claim that recipients have won $5,000 worth of CLAW tokens and can collect them by visiting a linked site and connecting their crypto wallet." The linked site ("token-claw[.]xyz") is a near-identical clone of openclaw.ai rigged with a wallet-draining "Connect your wallet" button designed to conduct cryptocurrency theft.
* **New Campaign Targets Energy Operations Personnel in Pakistan**
  — A targeted campaign against operations personnel at energy firms linked to projects in Pakistan has leveraged phishing emails mimicking invitations to the upcoming Pakistan Energy Exhibition & Conference (PEEC). The messages, sent from compromised accounts from a Pakistani university and a government organization, aim to deceive victims into opening PDF attachments with a fake Adobe Acrobat Reader update prompt. Clicking the update leads to the download of a ClickOnce application resource that drops the Havoc Demon C2 framework. "The redirect chain was also wrapped in geofencing and browser fingerprinting, limiting access to intended targets," Proofpoint
  [said](https://x.com/threatinsight/status/2035023649330348370)
  . "That likely reduced the exposure to automated analysis while keeping the delivery path tightly scoped." The activity has been codenamed UNK\_VaporVibes. It's assessed to share overlaps with activity publicly associated with
  [SloppyLemming](https://thehackernews.com/2026/03/sloppylemming-targets-pakistan-and.html)
  .
* **Over 373K Dark Web Sites Down**
  — International law enforcement agencies
  [announced](https://www.europol.europa.eu/media-press/newsroom/news/global-cybercrime-crackdown-over-373-000-dark-web-sites-shut-down)
  the takedown of one of the largest known networks of fraudulent platforms on the dark web, uncovering hundreds of thousands of fake websites used to scam users seeking child sexual abuse content. A 10-day international operation led by German authorities and supported by Europol shut down more than 373,000 dark web domains run by a 35-year-old man based in China, who had been operating a sprawling network of fraudulent platforms since at least 2021. While the sites advertised child abuse material and cybercrime-as-a-service offerings, nothing was actually delivered after victims made a payment in Bitcoin. The fraudulent scheme netted the operator an estimated €345,000 from around 10,000 people. Authorities from 23 countries participated in the operation, and have since identified 440 customers whose purchases are now under active investigation.
* **Malicious npm Packages Steal Secrets**
  — Two malicious npm packages, sbx-mask and touch-adv, have been found to steal secrets from victims' computers. While one invokes the malicious code via the postinstall script, the other executes it when application code is invoked by the developer after importing it. "The evidence strongly suggests account takeover of a legitimate publisher, rather than intentional malicious activity," Sonatype
  [said](https://www.sonatype.com/blog/sonatype-discovers-two-malicious-npm-packages)
  . "Hijacked publisher accounts are particularly concerning as, over time, maintainers build trust with the users of their components. Attackers aim to take advantage of that trust in order to steal valuable, or profitable, information."
* **China to Have Its Own Post-Quantum Cryptography in 3 Years**
  — China is reportedly planning to develop its own national post-quantum cryptography standards within the next three years, according to a
  [report](https://www.reuters.com/world/asia-pacific/china-likely-have-standards-post-quantum-crytography-3-years-expert-says-2026-03-19/)
  from Reuters. The U.S. finalized ​its first set of post-quantum cryptography standards in 2024 and is aiming to achieve full industry migration by 2035.
* **What's Next for Tycoon2FA?**
  — A recent law enforcement operation dismantled the infrastructure associated with the
  [Tycoon2FA](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html)
  phishing-as-a-service (PhaaS) platform. However, a new analysis from Bridewell has revealed that some of the 2FA phishing CAPTCHA pages are still live. The lingering activity, the cybersecurity company noted, stems from the fact that these pages operate on a massive network of compromised third-party sites, legitimate SaaS platforms, and thousands of disposable domains. "Operators and affiliates are highly agile and will attempt to rebuild, migrate to new infrastructure, or pivot to competing PhaaS platforms," it
  [added](https://www.bridewell.com/insights/blogs/detail/the-rise-and-fall-of-tycoon-2fa-inside-the-mfa-bypassing-phishing-empire)
  . "The live CAPTCHA pages we are seeing may belong to surviving criminal affiliates attempting to keep their individual campaigns breathing on secondary proxy networks."

## **🔧 Cybersecurity Tools**

* [MESH](https://github.com/BARGHEST-ngo/MESH)
  → It is an open-source tool from BARGHEST that enables remote mobile forensics and network monitoring over an encrypted, peer-to-peer mesh network resistant to censorship. It connects Android/iOS devices behind firewalls or CGNAT using a modified Tailscale-like protocol (no central servers needed), supports ADB wireless debugging, libimobiledevice, PCAP capture, and Suricata IDS—allowing secure, direct access for live logical acquisitions in restricted or hostile environments.
* [enject](https://github.com/GreatScott/enject)
  → It is a lightweight Rust tool that protects .env secrets from AI assistants like Copilot or Claude. It replaces real values in your .env file with placeholders (e.g., en://api\_key). Secrets stay encrypted in a per-project store (AES-256-GCM, master password protected). When you run enject run -- <command>, it decrypts them only in memory at runtime, then wipes them—never leaving plaintext on disk. Open-source, macOS/Linux, perfect for safe local development.

*Disclaimer: For research and educational use only. Not security-audited. Review all code before use, test in isolated environments, and ensure compliance with applicable laws.*

## **Conclusion**

And that’s the week. The real pattern isn’t any one story; it’s the gap. The gap between a flaw and detection. Between a patch and a deployment. Between knowing and doing. Most of this week’s damage happened in that gap, and it’s not new.

Before you move on: update your mobile devices, review anything touching your CI/CD pipeline, and don’t store crypto wallet recovery phrases in notes apps.