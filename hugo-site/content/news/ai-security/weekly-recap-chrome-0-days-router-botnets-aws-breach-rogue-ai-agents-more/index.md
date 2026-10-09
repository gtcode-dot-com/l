---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-18T03:15:27.270829+00:00'
exported_at: '2026-03-18T03:15:30.503976+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/weekly-recap-chrome-0-days-router.html
structured_data:
  about: []
  author: ''
  description: Catch up on the latest cyber threats, attack trends, security research,
    botnets, phishing, and critical vulnerabilities.
  headline: '⚡ Weekly Recap: Chrome 0-Days, Router Botnets, AWS Breach, Rogue AI Agents
    & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/weekly-recap-chrome-0-days-router.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: Chrome 0-Days, Router Botnets, AWS Breach, Rogue AI Agents
  & More'
updated_at: '2026-03-18T03:15:27.270829+00:00'
url_hash: d9b94684f75e66b2c483b168508d62893afec374
---

**

Ravie Lakshmanan
**

Mar 16, 2026

Cybersecurity / Hacking

Some weeks in security feel normal. Then you read a few tabs and get that immediate “ah, great, we’re doing this now” feeling.

This week has that energy. Fresh messes, old problems getting sharper, and research that stops feeling theoretical real fast. A few bits hit a little too close to real life, too. There’s a good mix here: weird abuse of trusted stuff, quiet infrastructure ugliness, sketchy chatter, and the usual reminder that attackers will use anything that works.

Scroll on. You’ll see what I mean.

## **⚡ Threat of the Week**

**[Google Patches 2 Actively Exploited Chrome 0-Days](https://thehackernews.com/2026/03/google-fixes-two-chrome-zero-days.html)**
— Google released security updates for its Chrome web browser to address two high-severity vulnerabilities that it said have been exploited in the wild. The vulnerabilities related to an out-of-bounds write vulnerability in the Skia 2D graphics library (CVE-2026-3909) and an inappropriate implementation vulnerability in the V8 JavaScript and WebAssembly engine (CVE-2026-3910) that could result in out-of-bounds memory access or code execution, respectively. Google did not share additional details about the flaws, but acknowledged that there exist exploits for both of them. The issues were addressed in Chrome versions 146.0.7680.75/76 for Windows and Apple macOS, and 146.0.7680.75 for Linux.

## **🔔 Top News**

* **[Meta to Discontinue Instagram E2EE in May 2026](https://thehackernews.com/2026/03/meta-to-shut-down-instagram-end-to-end.html)**
  — Meta announced plans to discontinue support for end-to-end encryption (E2EE) for chats on Instagram after May 8, 2026. In a statement shared with The Hacker News, a Meta spokesperson said, "Very few people were opting in to end-to-end encrypted messaging in DMs, so we're removing this option from Instagram in the coming months. Anyone who wants to keep messaging with end-to-end encryption can easily do that on WhatsApp."
* **[Authorities Disrupt SocksEscort Service](https://thehackernews.com/2026/03/authorities-disrupt-socksescort-proxy.html)**
  — A court-authorized international law enforcement operation dismantled a criminal proxy service named SocksEscort that enslaved thousands of residential routers worldwide into a botnet for committing large-scale fraud. "The malware allowed SocksEscort to direct internet traffic through the infected routers. SocksEscort sold this access to its customers," the U.S. Justice Department said. The main thing to note here is that SocksEscort was powered by AVrecon, a malware written in C to explicitly target MIPS and ARM architectures via known security flaws in edge network devices. The malware also featured a novel persistence mechanism that involved flashing custom firmware, which intentionally disables future updates, permanently transforming SOHO routers into SocksEscort proxy nodes to blindside corporate monitoring.
* **[UNC6426 Exploits nx npm Supply Chain Attack to Gain AWS Admin Access in 72 Hours](https://thehackernews.com/2026/03/unc6426-exploits-nx-npm-supply-chain.html)**
  — A threat actor known as UNC6426 leveraged keys stolen following the supply chain compromise of the nx npm package in August 2025 to completely breach a victim's AWS environment within 72 hours. UNC6426 used the access to abuse the GitHub-to-AWS OpenID Connect (OIDC) trust and create a new administrator role in the cloud environment, Google said. Subsequently, this role was abused to exfiltrate files from the client's Amazon Web Services (AWS) Simple Storage Service (S3) buckets and perform data destruction in their production cloud environments.
* **[KadNap Enslaves Network Devices to Fuel Illegal Proxy](https://thehackernews.com/2026/03/kadnap-malware-infects-14000-edge.html)**
  — A takedown-resistant botnet comprising more than 14,000 routers and other network devices has been conscripted into a proxy network that anonymously ferries traffic used for cybercrime. The botnet, named KadNap, exploits known vulnerabilities in Asus routers (among others), leveraging the initial access to drop shell scripts that reach out to a peer-to-peer network based on Kademlia for decentralized control. Infected devices are being used to fuel a proxy service named Doppelganger that, for a fee, tunnels customers' internet traffic through residential IP addresses, offering a way for attackers to blend in and make it harder to differentiate malicious traffic from legitimate activity.
* **[APT28 Strikes with Sophisticated Toolkit](https://thehackernews.com/2026/03/apt28-uses-beardshell-and-covenant.html)**
  — The Russian threat actor known as APT28 has been observed using a bespoke toolkit in recent cyber espionage campaigns targeting Ukrainian cyber assets. The primary components of the toolkit are two implants, one of which employs techniques from a malware framework the threat actor used in 2010s, while the other is a heavily modified version of the COVENANT framework for long-term spying. COVENANT is used in concert with BEARDSHELL to facilitate data exfiltration, lateral movement, and execution of PowerShell commands. Also alongside these tools is a malware named SLIMAGENT that shares overlaps with XAgent.

## **‎️‍🔥 Trending CVEs**

New vulnerabilities show up every week, and the window between disclosure and exploitation keeps getting shorter. The flaws below are this week's most critical — high-severity, widely used software, or already drawing attention from the security community.

Check these first, patch what applies, and don't wait on the ones marked urgent —
[CVE-2026-3909, CVE-2026-3910](https://thehackernews.com/2026/03/google-fixes-two-chrome-zero-days.html)
,
[CVE-2026-3913](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_10.html)
(Google Chrome),
[CVE-2026-21666, CVE-2026-21667, CVE-2026-21668, CVE-2026-21672, CVE-2026-21708, CVE-2026-21669, CVE-2026-21671](https://thehackernews.com/2026/03/veeam-patches-7-critical-backup.html)
(Veeam Backup & Replication),
[CVE-2026-27577, CVE-2026-27493, CVE-2026-27495, CVE-2026-27497](https://thehackernews.com/2026/03/critical-n8n-flaws-allow-remote-code.html)
(n8n),
[CVE-2026-26127, CVE-2026-21262](https://thehackernews.com/2026/03/microsoft-patches-84-flaws-in-march.html)
(Microsoft Windows),
[CVE-2019-17571, CVE-2026-27685](https://thehackernews.com/2026/03/dozens-of-vendors-patch-security-flaws.html)
(SAP),
[CVE-2026-3102](https://www.kaspersky.com/blog/exiftool-macos-picture-vulnerability-mitigation-cve-2026-3102/55362/)
(ExifTool for macOS),
[CVE-2026-27944](https://github.com/0xJacky/nginx-ui/security/advisories/GHSA-g9w5-qffc-6762)
(Nginx UI),
[CVE-2025-67826](https://blog.quarkslab.com/k7-antivirus-named-pipe-abuse-registry-manipulation-and-privilege-escalation.html)
(K7 Ultimate Security),
[CVE-2026-26224](https://blog.quarkslab.com/intego_lpe_macos_1.html)
,
[CVE-2026-26225](https://blog.quarkslab.com/intego_lpe_macos_2.html)
(Intego X9),
[CVE-2026-29000](https://www.codeant.ai/security-research/pac4j-jwt-authentication-bypass-public-key)
(
[pac4j-jwt](https://www.pac4j.org/blog/security-advisory-pac4j-jwt-jwtauthenticator.html)
),
[CVE-2026-23813](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05027en_us&docLocale=en_US)
(HPE Aruba Networking AOS-CX),
[CVE-2025-12818](https://swarm.ptsecurity.com/attack-arithmetic-how-an-integer-overflow-in-postgresql-libpq-leads-to-denial-of-service/)
(
[PostgreSQL](https://www.postgresql.org/support/security/CVE-2025-12818/)
),
[CVE-2026-2413](https://www.wordfence.com/blog/2026/03/400000-wordpress-sites-affected-by-unauthenticated-sql-injection-vulnerability-in-ally-wordpress-plugin/)
(Ally WordPress plugin),
[CVE-2026-0953](https://www.wordfence.com/blog/2026/03/30000-wordpress-sites-affected-by-authentication-bypass-vulnerability-in-tutor-lms-pro-wordpress-plugin/)
(Tutor LMS Pro WordPress plugin),
[CVE-2026-25921](https://github.com/gogs/gogs/security/advisories/GHSA-cj4v-437j-jq4c)
(Gogs),
[CVE-2026-2833, CVE-2026-2835, CVE-2026-2836](https://blog.cloudflare.com/pingora-oss-smuggling-vulnerabilities/)
(Cloudflare Pingora),
[CVE-2026-24308](https://zookeeper.apache.org/security.html)
(Apache ZooKeeper),
[CVE-2026-3059, CVE-2026-3060, CVE-2026-3989](https://kb.cert.org/vuls/id/665416)
(SGLang),
[CVE-2026-0231](https://security.paloaltonetworks.com/CVE-2026-0231)
(Palo Alto Networks Cortex XDR Broker VM),
[CVE-2026-20040, CVE-2026-20046](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-iosxr-privesc-bF8D5U4W)
(Cisco IOS XR Software),
[CVE-2025-65587](https://kb.cert.org/vuls/id/907705)
(graphql-upload-minimal),
[CVE-2026-3497](https://seclists.org/oss-sec/2026/q1/299)
(OpenSSH),
[CVE-2026-26123](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26123)
(Microsoft Authenticator for Android and iOS), and
[CVE-2025-61915](https://www.levelblue.com/blogs/spiderlabs-blog/cve-2025-61915-buffer-underflow-vulnerability-leads-to-memory-corruption-in-cups)
(CUPS).

## **🎥 Cybersecurity Webinars**

* [Stop Guessing: Automate Your Defense Against Real-World Attacks](https://thehacker.news/automate-testing-security-posture?source=recap)
  → Learn how to move beyond basic security checklists by using automation to test your defenses against real-world attacks. Experts will show you why traditional testing often fails and how to use continuous, data-driven tools to find and fix gaps in your protection. You will learn how to prove your security actually works without increasing your manual workload.
* [Fix Your Identity Security: Closing the Gaps Before Hackers Find Them](https://thehacker.news/identity-maturity-2026?source=recap)
  → This webinar covers a new study about why many companies are struggling to keep their user accounts and digital identities safe. Experts share findings from the Ponemon Institute on the biggest security gaps, such as disconnected apps and the new risks created by AI. You will learn simple, practical steps to fix these problems and get better control over who has access to your company's data.
* [The Ghost in the Machine: Securing the Secret Identities of Your AI Agents](https://thehacker.news/ghost-in-the-machine?source=recap)
  → As artificial intelligence (AI) begins to act on its own, businesses face a new challenge: how to give these "AI agents" the right digital IDs. This webinar explains why current security for humans doesn't work for autonomous bots and how to build a better system to track what they do. You will learn simple, real-world steps to give AI agents secure identities and clear rules, ensuring they don't accidentally expose your private company data.

## **📰 Around the Cyber World**

* **Fake Google Security Check Drops Browser RAT**
  — A web page mimicking a Google Account security page has been spotted delivering a fully featured browser-based surveillance toolkit that takes the form of a Progressive Web App (PWA). "Disguised as a routine security checkup, it walks victims through a four-step flow that grants the attacker push notification access, the device's contact list, real-time GPS location, and clipboard contents—all without installing a traditional app," Malwarebytes
  [said](https://www.malwarebytes.com/blog/privacy/2026/02/inside-a-fake-google-security-check-that-becomes-a-browser-rat)
  . "For victims who follow every prompt, the site also delivers an Android companion package introducing a native implant that includes a custom keyboard (enabling keystroke capture), accessibility-based screen reading capabilities, and permissions consistent with call log access and microphone recording."
* **Forbidden Hyena Delivers BlackReaperRAT**
  — A hacktivist group known as
  [Forbidden Hyena](https://bi.zone/eng/expertise/blog/forbidden-hyena-atakuet-s-novym-troyanom-udalennogo-dostupa-blackreaperrat/)
  (aka 4B1D) has distributed RAR archives in December 2025 and January 2026 in attacks targeting Russia that led to the deployment of a previously undocumented remote access trojan called BlackReaperRAT and an updated version of the Blackout Locker ransomware, referred to as
  [Milkyway](https://securelist.ru/sovmestnye-ataki-4bid-bo-team-red-likho/114124/)
  by the threat actors. BlackReaperRAT is capable of running commands via "cmd.exe," uploading/downloading files, spawning an HTTP shell to receive commands, and spreading the malware to connected removable media. "It carries out destructive attacks against organizations across various sectors located within the Russian Federation," BI.ZONE said. "The group publishes information regarding successful attacks on its Telegram channel. It collaborates with the groups Cobalt Werewolf and Hoody Hyena."
* **Chinese Hackers Target the Persian Gulf region with PlugX**
  — A China-nexus threat actor, likely suspected to be
  [Mustang Panda](https://thehackernews.com/2026/01/mustang-panda-deploys-updated.html)
  , has targeted countries in the Persian Gulf region. The activity took place within the first 24 hours of the ongoing conflict in the Middle East late last month. The campaign used a multi-stage attack chain that ultimately deployed a PlugX backdoor variant. "The shellcode and PlugX backdoor used obfuscation techniques such as control flow flattening (CFF) and mixed boolean arithmetic (MBA) to hinder reverse engineering," Zscaler
  [said](https://www.zscaler.com/blogs/security-research/china-nexus-threat-actor-targets-persian-gulf-region-plugx)
  . "The PlugX variant in this campaign supports HTTPS for command-and-control (C2) communication and DNS-over-HTTPS (DOH) for domain resolution."
* **Phishing Campaign Uses SEO Poisoning to Steal Data**
  — A phishing campaign has employed SEO poisoning to direct search engine results to fake traffic ticket portals that impersonate the Government of Canada and specific provincial agencies. "The campaign lures victims to a fake 'Traffic Ticket Search Portal' under the pretense of paying outstanding traffic violations," Palo Alto Networks Unit 42
  [said](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-01-30-IOCs-for-traffic-ticket-search-portal-themed-phishing.txt)
  . "Submitted data includes license plates, address, date of birth, phone/email, and credit card numbers." The phishing pages utilize a "waiting room" tactic where the victim's browser polls the server every two seconds and triggers redirects based on specific status codes.
* **Roundcube Exploitation Toolkit Discovered**
  — Hunt.io said it discovered a Roundcube exploitation toolkit on an internet-exposed directory on 203.161.50[.]145. It's worth noting that Russian threat actors like APT28, Winter Vivern, and TAG-70 have repeatedly targeted Roundcube vulnerabilities to breach Ukrainian organizations. "The directory included development and production XSS payloads, a Flask-based command-and-control server, CSS-injection tooling, operator bash history, and a Go-based implant deployed on a compromised Ukrainian web application," the company said, attributing it with medium to high confidence to APT28, citing overlaps with
  [Operation RoundPress](https://thehackernews.com/2025/05/russia-linked-apt28-exploited-mdaemon.html)
  . The toolkit, dubbed Roundish, supports credential harvesting, persistent mail forwarding, bulk email exfiltration, address book theft, and two-factor authentication (2FA) secret extraction, mirroring a feature present in MDAEMON. One of the primary targets of the attack is mail.dmsu.gov[.]ua, a Roundcube webmail instance associated with Ukraine's State Migration Service (DMSU). Besides the possibility of a shared development lineage, Roundish introduces four new components not previously documented in APT28 webmail activity, including a CSS-based side-channel module, browser credential stealer, and a Go-based backdoor that provides persistence via cron, systemd, and SELinux. The CSS injection component is designed to progressively extract characters from Roundcube's document object model (DOM) without injecting any JavaScript into the victim's page. The technique is likely used for targeting Cross-Site Request Forgery (CSRF) tokens or email UIDs. Central to the Roundish toolkit is an XSS payload that's engineered to steal the victim's email address, harvest account credentials, redirect all incoming emails to a Proton Mail address, export mailbox data from the victim's Inbox and Sent folders, and gather the victim's complete address book. "The combination of hidden autofill credential harvesting, server-side mail forwarding persistence, bulk mailbox exfiltration, and browser credential theft reflects a modular approach designed for sustained access," Hunt.io
  [said](https://hunt.io/blog/operation-roundish-apt28-roundcube-exploitation)
  . "From a defensive perspective, password resets alone are not sufficient in cases like this. Mail forwarding rules, Sieve filters, and multi-factor authentication secrets must be audited and reset."
* **Phishing Campaign Targeting AWS Console Credentials**
  — An active adversary-in-the-middle (AiTM) phishing campaign is using fake security alert emails to steal AWS Console credentials, per Datadog. "The phishing kit proxies authentication to the legitimate AWS sign-in endpoint in real time, validating credentials before redirecting victims and likely capturing one-time password (OTP) codes," the company
  [said](https://securitylabs.datadoghq.com/articles/behind-the-console-aws-aitm-phishing-campaign/)
  . "This campaign does not exploit AWS vulnerabilities or abuse AWS infrastructure." Post-compromise console access has been observed within 20 minutes of credential submission. These efforts originated from Mullvad VPN infrastructure.
* **Malicious npm Packages Deliver Cipher stealer**
  — Two new malicious npm packages, bluelite-bot-manager and test-logsmodule-v-zisko, were found to deliver via Dropbox a Windows executable designed to siphon sensitive data, including Discord totems, credentials from Chrome, Edge, Opera, Brave, and Yandex browsers, and seed files from cryptocurrency wallet apps like Exodus. from compromised hosts using a stealer named Cipher stealer. "The stealer also uses an embedded Python script and a secondary payload downloaded from GitHub," JFrog
  [said](https://research.jfrog.com/post/solara-cipher-npm/)
  .
* **GIBCRYPTO Ransomware Detailed**
  — A new ransomware called
  [GIBCRYPTO](https://labs.k7computing.com/index.php/gibcrypto-the-destructive-ransomware-with-a-snake-keylogger-connection/)
  comes with the ability to capture keystrokes and corrupt the Master Boot Record (MBR) so that any attempt to restart the system will cause the system to run into an error. The ransomware uses the Salsa20 algorithm for encryption. It's suspected to be part of
  [Snake Keylogger](https://thehackernews.com/2025/02/new-snake-keylogger-variant-leverages.html)
  , indicating the malware authors' attempts to diversify beyond information theft. The development comes as Sygnia highlighted SafePay's OneDrive-based data exfiltration technique during a ransomware attack after breaching a victim by leveraging a FortiGate firewall flaw and a misconfigured administrative account. "SafePay gained initial access by exploiting a firewall misconfiguration, which enabled them to obtain local administrative credentials," the company
  [said](https://www.sygnia.co/blog/safepay-onedrive-exfiltration-technique/)
  . "They rapidly escalated discovery and enumeration activities to identify high-value targets for lateral movement, demonstrating a structured and methodical approach to mapping the environment. Within a matter of hours, SafePay escalated to domain administrator access." The attack culminated in the deployment of ransomware, encrypting more than 60 servers.
* **Fraudulent Account Registration Activity Originating from Vietnam**
  — A sprawling cybercrime ecosystem based in Vietnam has been linked to a cluster of fraudulent account registration activity on platforms like LinkedIn, Instagram, Facebook, and TikTok. In these attacks, attributed to
  [O-UNC-036](https://www.okta.com/blog/threat-intelligence/opportunistic-sms-pumping-attacks-target-customer-sign-up-pages/)
  , the threat actors rely on disposable email addresses in order to execute SMS pumping attacks, also called International Revenue Sharing Fraud (IRSF). "In this scheme, malicious actors automate the creation of puppet accounts in a targeted service provider," Okta
  [said](https://www.okta.com/blog/threat-intelligence/vietnamese-cybercrime-operation-enables-fraudulent-account-signups/)
  . "Fraudsters use these account registrations to trigger SMS messages to premium rate phone numbers and profit from charges incurred. This activity can prove costly for service providers who use SMS to verify registration information in customer accounts or to send multi-factor authentication (MFA) security codes." O-UNC-036 has also been linked to a cybercrime-as–a-service (CaaS) ecosystem that provides paid infrastructure and services to facilitate online fraud. The web-based storefronts are hosted in Vietnam and specialize in the sales of web-based accounts.
* **Hijacked AppsFlyer SDK Distributes Crypto Clipper**
  — The AppsFlyer Web SDK was briefly hijacked to serve malicious code to steal cryptocurrency in a supply chain attack. The clipper malware payload came with capabilities to intercept cryptocurrency wallet addresses entered on websites and replace them with attacker-controlled addresses to divert funds to the threat actor. "The AppsFlyer Web SDK was observed serving obfuscated malicious JavaScript instead of the legitimate SDK from websdk.appsflyer[.]com," Profero
  [said](https://profero.io/blog/hijacked-at-the-source-a-trusted-marketing-appsflyers-sdk-distributes-a-crypto-stealer)
  . "The malicious payload appears to have been designed for stealth and compatibility, preserving legitimate SDK functionality while adding hidden browser hooks and wallet-hijacking logic." The
  [incident](https://statusfield.com/services/appsflyer/incidents)
  has since been resolved by AppsFlyer.
* **Operation CamelClone Targets Government and Defense Entities**
  — A new cyber espionage campaign dubbed Operation CamelClone has targeted governments and defense entities in Algeria, Mongolia, Ukraine, and Kuwait using malicious ZIP archives that contain a Windows shortcut (LNK) file, which, when executed, delivers a JavaScript loader named HOPPINGANT. The loader then delivers additional payloads for establishing C2 and exfiltrating data to the MEGA cloud storage service. "One interesting aspect of this campaign is that the threat actor does not rely on traditional command-and-control infrastructure," Seqrite Labs
  [said](https://www.seqrite.com/blog/operation-camelclone-multi-region-espionage-campaign-targets-government-and-defense-entities-amidst-regional-tensions/)
  . "Instead, the payloads are hosted on a public file-sharing service, filebulldogs[.]com, while stolen data is uploaded to MEGA storage using the legitimate tool Rclone." The activity has not been attributed to any known threat group.
* **How Threat Actors Exfiltrate Credentials Using Telegram Bots**
  — Threat actors are abusing the
  [Telegram Bot API](https://core.telegram.org/bots/api)
  to exfiltrate data via text messages or arbitrary file uploads, highlighting how legitimate services can be weaponized to evade detection. Agent Tesla Keylogger is by far the most prominent example of a malware family that uses Telegram for C2. "In general, Telegram C2s appear to be most popular among information stealers, possibly due to Telegram's technically legitimate nature and because information stealers typically only need to exfiltrate data passively rather than provide complex communications beyond simple message or file transfers," Cofense
  [said](https://cofense.com/blog/weaponizing-telegram-bots-how-threat-actors-exfiltrate-credentials)
  .
* **Microsoft Launches Copilot Health**
  — Microsoft has become the latest company after
  [OpenAI](https://thehackernews.com/2026/01/openai-launches-chatgpt-health-with.html)
  and
  [Anthropic](https://thehackernews.com/2026/01/anthropic-launches-claude-ai-for.html)
  to launch a dedicated "secure space" called Copilot Health that integrates medical records, biometric data from wearables, and lab test results to give personalized advice in the U.S. "Copilot Health brings together your health records, wearable data, and health history into one place, then applies intelligence to turn them into a coherent story," the company
  [said](https://microsoft.ai/news/introducing-copilot-health/)
  . Like OpenAI and Anthropic, Microsoft emphasized that Copilot Health isn't meant to replace professional medical care.
* **Rogue AI Agents Can Work Together to Engage in Offensive Behaviors**
  — According to a new report from artificial intelligence (AI) security company Irregular, agents can work together to hack into systems, escalate privileges, disable endpoint protection, and steal sensitive data while evading pattern-matching defenses. What's notable is that the experiment did not rely on adversarial prompting or deliberately unsafe system design. "In one case, an agent convinced another agent to carry out an offensive action, a form of inter-agent collusion that emerged with no external manipulation," Irregular
  [said](https://www.irregular.com/publications/emergent-offensive-cyber-behavior-in-ai-agents)
  . "This scenario demonstrates two compounding risks: inter-agent persuasion can erode safety boundaries, and agents can independently develop techniques to circumvent security controls. When an agent is given access to tools or data, particularly but not exclusively shell or code access, the threat model should assume that the agent will use them, and that it will do so in unexpected and possibly malicious ways."

## **🔧 Cybersecurity Tools**

* [Dev Machine Guard](https://github.com/step-security/dev-machine-guard)
  → It is a free, open-source tool that scans your computer to show you exactly what developer tools and scripts are running. It creates a simple list of your AI coding assistants, code editor extensions, and software packages to help you find anything suspicious or outdated. It is a single script that works in seconds to give you better visibility into the security of your local coding environment.
* [Trajan](https://github.com/praetorian-inc/trajan)
  → It is an automated security tool designed to find hidden vulnerabilities in "service meshes," which are the systems that manage how different parts of a large software application talk to each other. Because these systems are complex, it is easy for engineers to make small mistakes in the settings that allow hackers to bypass security or steal data. Trajan works by scanning these configurations to spot those specific errors and helping developers fix them before they can be exploited.

*Disclaimer: For research and educational use only. Not security-audited. Review all code before use, test in isolated environments, and ensure compliance with applicable laws.*

## **Conclusion**

There’s a lot packed in here, and not in a neat way. Some of it is the usual recycled chaos, some of it feels a little more deliberate, and some of it has that nasty “this is going to show up everywhere by next week” energy.

Anyway — enough throat-clearing. Here’s the stuff worth your attention.