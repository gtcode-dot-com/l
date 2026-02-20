---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-20T08:15:16.649248+00:00'
exported_at: '2026-02-20T08:15:18.921460+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html
structured_data:
  about: []
  author: ''
  description: ThreatsDay Bulletin tracks active exploits, phishing waves, AI risks,
    major flaws, and cybercrime crackdowns shaping this week’s threat landscape.
  headline: 'ThreatsDay Bulletin: OpenSSL RCE, Foxit 0-Days, Copilot Leak, AI Password
    Flaws & 20+ Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/threatsday-bulletin-openssl-rce-foxit-0.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: OpenSSL RCE, Foxit 0-Days, Copilot Leak, AI Password
  Flaws & 20+ Stories'
updated_at: '2026-02-20T08:15:16.649248+00:00'
url_hash: 738a64dbfeb36a461e51e785c04fe9ff0b64339b
---

**

Ravie Lakshmanan
**

Feb 19, 2026

Cybersecurity / Hacking News

The cyber threat space doesn’t pause, and this week makes that clear. New risks, new tactics, and new security gaps are showing up across platforms, tools, and industries — often all at the same time.

Some developments are headline-level. Others sit in the background but carry long-term impact. Together, they shape how defenders need to think about exposure, response, and preparedness right now.

This edition of ThreatsDay Bulletin brings those signals into one place. Scan through the roundup for quick, clear updates on what’s unfolding across the cybersecurity and hacking landscape.

1. Privacy model hardening

   Google
   [announced](https://developer.android.com/about/versions/17/behavior-changes-17)
   the first beta version of
   [Android 17](https://android-developers.googleblog.com/2026/02/the-first-beta-of-android-17.html)
   , with two privacy and security enhancements: the deprecation of Cleartext Traffic Attribute and support for HPKE Hybrid Cryptography to enable secure communication using a combination of public key and symmetric encryption (AEAD). "If your app targets (Android 17) or higher and relies on
   [usesCleartextTraffic](https://developer.android.com/guide/topics/manifest/application-element#usesCleartextTraffic)
   ='true' without a corresponding Network Security Configuration, it will default to disallowing cleartext traffic," Google said. "You are encouraged to migrate to
   [Network Security Configuration files](https://developer.android.com/training/articles/security-config)
   for granular control."
2. RaaS expands cross-platform reach

   A new analysis of the LockBit 5.0 ransomware has revealed that the Windows version packs in various defense evasion and anti-analysis techniques, including packing, DLL unhooking, process hollowing, patching Event Tracing for Windows (ETW) functions, and log clearing. "What's notable among the multiple systems support is its proclaimed capability to 'work on all versions of Proxmox,'" Acronis
   [said](https://www.acronis.com/en/tru/posts/lockbit-strikes-with-new-50-version-targeting-windows-linux-and-esxi-systems/)
   . "Proxmox is an open-source virtualization platform and is being adopted by enterprises as an alternative to commercial hypervisors, which makes it another prime target of ransomware attacks." The latest version also introduces dedicated builds tailored for enterprise environments, highlighting the continued evolution of ransomware-as-a-service (RaaS) operations.
3. Mac users lured via nested obfuscation

   Cybersecurity researchers have detailed a new evolution of the
   [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
   social engineering tactic targeting macOS users. "Dubbed Matryoshka due to its nested obfuscation layers, this variant uses a fake installation/fix flow to trick victims into executing a malicious Terminal command," Intego
   [said](https://www.intego.com/mac-security-blog/matryoshka-clickfix-macos-stealer/)
   . "While the ClickFix tactic is not new, this campaign introduces stronger evasion techniques — including an in-memory, compressed wrapper and API-gated network communications — designed to hinder static analysis and automated sandboxes." The campaign primarily targets users attempting to visit software review sites, leveraging typosquatting in the URL name to redirect them to fake sites and activate the infection chain.
4. Loader pipeline drives rapid domain takeover

   Another new
   [ClickFix](https://thehackernews.com/2026/02/microsoft-discloses-dns-based-clickfix.html)
   campaign detected in February 2026 has been observed delivering a malware-as-a-service (MaaS) loader known as
   [Matanbuchus 3.0](https://thehackernews.com/2025/07/hackers-leverage-microsoft-teams-to.html)
   . Huntress, which
   [dissected](https://www.huntress.com/blog/clickfix-matanbuchus-astarionrat-analysis)
   the attack chain, said the ultimate objective of the intrusion was to deploy ransomware or exfiltrate data based on the fact that the threat actor rapidly progressed from initial access to lateral movement to domain controllers via PsExec, rogue account creation, and Microsoft Defender exclusion staging. The attack also led to the deployment of a custom implant dubbed AstarionRAT that supports 24 commands to facilitate credential theft, SOCKS5 proxy, port scanning, reflective code loading, and shell execution. According to data from the cybersecurity company,
   [ClickFix fueled 53% of all malware loader activity](https://www.huntress.com/press-release/huntress-cyber-threat-report-exposes-the-playbook-for-organized-cybercrime)
   in 2025.
5. Typosquat chain targets macOS credentials

   In yet another ClickFix campaign, threat actors are relying on the "reliable trick" to host malicious instructions on fake websites disguised as Homebrew ("homabrews[.]org") to trick users into pasting them on the Terminal app under the pretext of installing the macOS package manager. In the attack chain documented by Hunt.io, the commands in the typosquatted Homebrew domain are used to deliver a credential-harvesting loader and a second-stage macOS infostealer dubbed Cuckoo Stealer. "The injected installer looped on password prompts using '
   [dscl . -authonly](https://ss64.com/mac/dscl.html)
   ,' ensuring the attacker obtained working credentials before deploying the second stage," Hunt.io
   [said](https://hunt.io/blog/fake-homebrew-clickfix-cuckoo-stealer-macos)
   . "Cuckoo Stealer is a full-featured macOS infostealer and RAT: It establishes LaunchAgent persistence, removes quarantine attributes, and maintains encrypted HTTPS command-and-control communications. It collects browser credentials, session tokens, macOS Keychain data, Apple Notes, messaging sessions, VPN and FTP configurations, and over 20 cryptocurrency wallet applications." The use of "dscl . -authonly" has been
   [previously observed](https://www.cloudsek.com/blog/amos-variant-distributed-via-clickfix-in-spectrum-themed-dynamic-delivery-campaign-by-russian-speaking-hackers)
   in attacks deploying Atomic Stealer.
6. Phobos affiliate detained in Europe

   Authorities from Poland's Central Bureau for Combating Cybercrime (CBZC) have detained a 47-year-old man over suspected ties to the Phobos ransomware group. He faces a potential prison sentence of up to five years. The CBZC
   [said](https://cbzc.policja.gov.pl/bzc/aktualnosci/823,47-latek-zwiazany-z-grupa-Phobos-zatrzymany-przez-policjantow-CBZC.html)
   the "47-year-old used encrypted messaging to contact the Phobos criminal group, known for conducting ransomware attacks," adding the suspect's devices contained logins, passwords, credit card numbers, and server IP addresses that could have been used to launch "various attacks, including ransomware." The arrest is part of Europol's
   [Operation Aether](https://thehackernews.com/2025/02/8base-ransomware-data-leak-sites-seized.html)
   , which targets the 8Base ransomware group, believed to be linked to Phobos. It has been almost exactly a year since international law enforcement dismantled the 8Base crew. More than 1,000 organizations around the world have been targeted in Phobos ransomware attacks, and the cybercriminals are believed to have obtained over $16 million in ransom payments.
7. Industrial ransomware surge accelerates

   There has been a sharp rise in the number of ransomware groups targeting industrial organizations as cybercriminals continue to exploit vulnerabilities in operational technology (OT) and industrial control systems (ICS), Dragos
   [warned](https://www.dragos.com/blog/dragos-2026-ot-cybersecurity-year-in-review)
   . A total of 119 ransomware groups targeting industrial organizations were tracked during 2025, a 49% increase from the 80 tracked in 2024. 2025 saw 3,300 industrial organizations around the world hit by ransomware, compared with 1693 in 2024. The most targeted sector was manufacturing, followed by transportation. In addition, a hacking group tracked as Pyroxene has been observed conducting "supply chain-leveraged attacks targeting defense, critical infrastructure, and industrial sectors, with operations expanding from the Middle East into North America and Western Europe." It often leverages initial access provided by PARISITE, to enable movement from IT into OT networks. Pyroxene overlaps with activity attributed to
   [Imperial Kitten](https://thehackernews.com/2023/11/iran-linked-imperial-kitten-cyber-group.html)
   (aka APT35), a threat actor affiliated with the cyber arm of the Islamic Revolutionary Guard Corps (IRGC).
8. Copilot bypassed DLP safeguards

   Microsoft
   [confirmed](https://admin.microsoft.com/#/MessageCenter/:/messages/CW1226324)
   a bug (
   [CW1226324](https://mailservices.isc.upenn.edu/computing/email/penno365/alerts/ms-incidents.html#:~:text=CW1226324%20%2D%20Users%27%20email%20messages%20with%20a%20confidential%20label%20applied%20are%20being%20incorrectly%20processed%20by%20Microsoft%20365%20Copilot%20chat)
   ) that let Microsoft 365 Copilot summarize confidential emails from Sent Items and Drafts folders since January 21, 2026, without users' permission, bypassing data loss prevention (DLP) policies put in place to safeguard sensitive data. A fix was deployed by the company on February 3, 2026. However, the company did not disclose how many users or organizations were affected. "Users' email messages with a confidential label applied are being incorrectly processed by Microsoft 365 Copilot chat," Microsoft said. "The Microsoft 365 Copilot "work tab" Chat is summarizing email messages even though these email messages have a sensitivity label applied, and a DLP policy is configured. A code issue is allowing items in the sent items and draft folders to be picked up by Copilot even though confidential labels are set in place."
9. Jira trials weaponized for spam

   Threat actors are abusing the trust and reputation associated with Atlassian Jira Cloud and its connected email system to run automated spam campaigns and bypass traditional email security. To accomplish this, the operators created Atlassian Cloud trial accounts using randomized naming conventions, allowing them to generate disposable Jira Cloud instances at scale. "Emails were tailored to target specific language groups, targeting English, French, German, Italian, Portuguese, and Russian speakers — including highly skilled Russian professionals living abroad," Trend Micro
   [said](https://www.trendmicro.com/en_us/research/26/b/spam-campaign-abuses-atlassian-jira.html)
   . "These campaigns not only distributed generic spam, but also specifically targeted sectors such as government and corporate entities." The attacks, active from late December 2025 through late January 2026, primarily targeted organizations using Atlassian Jira. The goal was to get recipients to open the emails and click on malicious links, which would initiate a redirect chain powered by the Keitaro Traffic Distribution System (TDS) and then finally lead them to pages peddling investment scams and online casino landing sites, suggesting that financial gain was likely the main objective.
10. GitLab SSRF now federally mandated patch

    The U.S. Cybersecurity and Infrastructure Security Agency (CISA), on February 18, 2026,
    [added](https://www.cisa.gov/news-events/alerts/2026/02/18/cisa-adds-two-known-exploited-vulnerabilities-catalog)
    CVE-2021-22175 to its Known Exploited Vulnerabilities (
    [KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
    ) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to apply the patch by March 11, 2026. "GitLab contains a server-side request forgery (SSRF) vulnerability when requests to the internal network for webhooks are enabled," CISA said. In March 2025, GreyNoise
    [revealed](https://thehackernews.com/2026/02/cisa-flags-four-security-flaws-under.html)
    that a cluster of about 400 IP addresses was actively exploiting multiple SSRF vulnerabilities, including CVE-2021-22175, to target susceptible instances in the U.S., Germany, Singapore, India, Lithuania, and Japan.
11. Telegram bots fuel Fortune 500 phishing

    An elusive, financially motivated threat actor dubbed GS7 has been targeting Fortune 500 companies in a new phishing campaign that leverages trusted company branding with lookalike websites aimed at harvesting credentials via Telegram bots. The campaign, codenamed
    [Operation DoppelBrand](https://socradar.io/resources/whitepapers/operation-doppelbrand-fortune-500-access/)
    , targets top financial institutions, including Wells Fargo, USAA, Navy Federal Credit Union, Fidelity Investments, and Citibank, as well as technology, healthcare, and telecommunications firms worldwide. Victims are lured through phishing emails and redirected to counterfeit pages where credentials are harvested and transmitted to Telegram bots controlled by the attacker. According to SOCRadar, the group itself, however, has a history stretching back to 2022. The threat actor is said to have registered more than 150 malicious domains in recent months using registrars such as NameCheap and OwnRegistrar, and routing traffic through Cloudflare to evade detection. GS7's end goals include not only harvesting credentials, but also downloading remote management and monitoring (RMM) tools like LogMeIn Resolve on victim systems to enable remote access or the deployment of malware. This has raised the possibility that the group may even act as an initial access broker (IAB), selling the access to ransomware groups or other affiliates.
12. Remcos shifts to live C2 surveillance

    Phishing emails disguised as invoices, job offers, or government notices are being used to distribute a new variant of Remcos RAT to facilitate comprehensive surveillance and control over infected systems. "The latest Remcos variant has been observed exhibiting a significant change in behaviour compared to previous versions," Point Wild
    [said](https://www.pointwild.com/threat-intelligence/remcos-revisited-inside-the-rats-evolving-command-and-control-techniques/)
    . "Instead of stealing and storing data locally on the infected system, this variant establishes direct online command-and-control (C2) communication, enabling real-time access and control. In particular, it leverages the webcam to capture live video streams, allowing attackers to monitor targets remotely. This shift from local data exfiltration to live, online surveillance represents an evolution in Remcos’ capabilities, increasing the risk of immediate espionage and persistent monitoring."
13. China-made vehicles restricted on bases

    Poland's Ministry of Defence has banned Chinese cars, and other motor vehicles equipped with technology to record position, images, or sound, from entering protected military facilities due to national security concerns and to "limit the risk of access to sensitive data." The ban also extends to connecting work phones to infotainment systems in motor vehicles produced in China. The ban isn't permanent: the Defence Ministry has called for the development of a vetting process to allow carmakers to undergo a security assessment that, if passed, can allow their vehicles to enter protected facilities. "Modern vehicles equipped with advanced communication systems and sensors can collect and transmit data, so their presence in protected zones requires appropriate safety regulations," the Polish Army
    [said](https://www.wojsko-polskie.pl/sgwp/articles/aktualnosci-w/zakazu-wjazdu-pojazdow-mechanicznych-wyprodukowanych-w-chinskiej-republice-ludowej-na-tereny-chronionych-obiektow-wojskowych/)
    . The measures introduced are preventive and comply with the practices of NATO countries and other allies to ensure the highest standards of defense infrastructure protection. They are part of a wider process of adapting security procedures to the changing technological environment and current requirements for the protection of critical infrastructure."
14. DKIM replay fuels invoice scams

    Bad actors are abusing legitimate invoices and dispute notifications from trusted vendors, such as PayPal, Apple, DocuSign, and Dropbox Sign (formerly HelloSign), to bypass email security controls. "These platforms often allow users to enter a 'seller name' or add a custom note when creating an invoice or notification," Casey-owned INKY
    [said](https://www.kaseya.com/blog/dkim-replay-attacks-apple-paypal-invoice-abuse/)
    . "Attackers abuse this functionality by inserting scam instructions and a phone number into those user-controlled fields. They then send the resulting invoice or dispute notice to an email address they control, ensuring the malicious content is embedded in a legitimate, vendor-generated message." Because these emails originate from a legitimate company, they bypass checks like Domain-based Message Authentication, Reporting and Conformance (DMARC). As soon as the legitimate email is received, the attacker proceeds to forward it to the intended targets, allowing the "authentic looking" message to land in the victims' inboxes. The attack is known as a DKIM replay attack.
15. RMM abuse surges 277%

    A new report from Huntress has revealed that the abuse of Remote Monitoring and Management (RMM) software surged 277% year-over-year, accounting for 24% of all observed incidents. Threat actors have begun to increasingly favor these tools because they are ubiquitous in enterprise environments, and the trusted nature of the RMM software allows malicious activity to blend in with legitimate usage, making detection harder for defenders. They also offer increased stealth, persistence, and operational efficiency. "As cybercriminals built entire playbooks around these legitimate, trusted tools to drop malware, steal credentials, and execute commands, the use of traditional hacking tools plummeted by 53%, while remote access trojans and malicious scripts dropped by 20% and 11.7%, respectively," the company
    [said](https://www.huntress.com/press-release/huntress-cyber-threat-report-exposes-the-playbook-for-organized-cybercrime)
    .
16. Texas targets China-linked tech firms

    Texas Attorney General Ken Paxton has
    [sued](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-sues-tp-link-allowing-ccp-access-americans-devices-first-several-lawsuits)
    TP-Link for "deceptively marketing its networking devices and allowing the Chinese Communist Party ('CCP') to access American consumers' devices in their homes." Paxton's lawsuit alleges that TP Link's products have been
    [used by Chinese hacking groups](https://thehackernews.com/2023/05/chinas-mustang-panda-hackers-exploit-tp.html)
    to launch cyber attacks against the U.S. and that the company is subject to Chinese data laws, which it said require firms operating in the country to support its intelligence services by "divulging Americans' data." TP-Link
    [told](https://therecord.media/texas-sues-tp-link-china-allegations)
    The Record that these allegations are "without merit" and that neither the Chinese government nor the Chinese Communist Party (CCP) exercises control over the company, its products, or user data. It also added that all U.S. user data is stored on domestic Amazon Web Services (AWS) servers. In a second lawsuit, Paxton also
    [accused](https://www.texasattorneygeneral.gov/news/releases/attorney-general-paxton-files-second-major-lawsuit-against-ccp-aligned-company-week-new-action)
    Anzu Robotics of misleading Texas consumers about the "origin, data practices, and security risks of its drones." Paxton's office described the company's products as "21st century Trojan horse linked to the CCP."
17. MetaMask backdoor expands DPRK campaign

    The North Korea-linked campaign known as
    [Contagious Interview](https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html)
    is designed to target IT professionals working in cryptocurrency, Web3, and artificial intelligence sectors to steal sensitive data and financial information using malware such as BeaverTail and InvisibleFerret. However, recent iterations of the campaign have expanded their data theft capabilities by tampering with the MetaMask wallet extension (if it's installed) through a lightweight JavaScript backdoor that shares the same functionality as InvisibleFerret, according to security researcher Seongsu Park. "Through the backdoor, attackers instruct the infected system to download and install a fake version of the popular MetaMask cryptocurrency wallet extension, complete with a dynamically generated configuration file that makes it appear legitimate," Park
    [said](https://sp4rk.medium.com/beyond-the-backdoor-how-contagious-interview-is-surgically-tampering-with-metamask-wallets-0314ae901d85)
    . "Once installed, the compromised MetaMask extension silently captures the victim's wallet unlock password and transmits it to the attackers’ command-and-control server, giving them complete access to cryptocurrency funds."
18. Booking.com kits hit hotels, guests

    Bridewell has warned of a resurgence in malicious activity targeting the hotel and retail sector. "The primary motivation driving this incident is financial fraud, targeting two victims: hotel businesses and hotel customers, in sequential order," security researcher Joshua Penny
    [said](https://www.bridewell.com/insights/blogs/detail/the-booking.com-phishing-campaign-targeting-hotels-and-customers)
    . "The threat actor(s) utilize impersonation of the Booking.com platform through two distinct phishing kits dedicated to harvesting credentials and banking information from each victim, respectively." It's worth noting that the activity shares overlap with a prior activity wave
    [disclosed](https://thehackernews.com/2025/11/large-scale-clickfix-phishing-attacks.html)
    by Sekoia in November 2025, although the use of a dedicated phishing kit is a new approach by either the same or new operators.
19. EPMM exploits enable persistent access

    The recently disclosed security flaws in Ivanti Endpoint Manager Mobile (EPMM) have been exploited by bad actors to establish a reverse shell, deliver JSP web shells, conduct reconnaissance, and download malware, including
    [Nezha](https://thehackernews.com/2025/10/chinese-hackers-weaponize-open-source.html)
    , cryptocurrency miners, and backdoors for remote access. The two critical vulnerabilities,
    [CVE-2026-1281 and CVE-2026-1340](https://thehackernews.com/2026/02/83-of-ivanti-epmm-exploits-linked-to.html)
    , allow unauthenticated attackers to remotely execute arbitrary code on target servers, granting them full control over mobile device management (MDM) infrastructure without requiring user interaction or credentials. According to Palo Alto Networks Unit 42, the campaign has affected state and local government, healthcare, manufacturing, professional and legal services, and high technology sectors in the U.S., Germany, Australia, and Canada. "Threat actors are accelerating operations, moving from initial reconnaissance to deploying dormant backdoors designed to maintain long-term access even after organizations apply patches," the cybersecurity company
    [said](https://unit42.paloaltonetworks.com/ivanti-cve-2026-1281-cve-2026-1340/)
    . In a related development, Germany's Federal Office for Information Security (BSI) has
    [reported](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-221601-1032.pdf)
    evidence of exploitation since the summer of 2025 and has urged organizations to audit their systems for indicators of compromise (IoCs) as far back as July 2025.
20. AI passwords lack true randomness

    New research by Irregular has
    [found](https://www.irregular.com/publications/vibe-password-generation)
    that passwords generated directly by a large language model (LLM) may appear strong but are fundamentally insecure, as "LLMs are designed to predict tokens – the opposite of securely and uniformly sampling random characters." The artificial intelligence (AI) security company said it detected LLM-generated passwords in the real world as part of code development tasks instead of leaning on traditional secure password generation methods. "People and coding agents should not rely on LLMs to generate passwords," the company said. "LLMs are optimized to produce predictable, plausible outputs, which is incompatible with secure password generation. AI coding agents should be directed to use secure password generation methods instead of relying on LLM-output passwords. Developers using AI coding assistants should review generated code for hardcoded credentials and ensure agents use cryptographically secure methods or established password managers."
21. PDF engine flaws enable account takeover

    Cybersecurity researchers have discovered more than a dozen vulnerabilities (
    [CVE-2025-70401, CVE-2025-70402, and CVE-2025-66500](https://novee.security/blog/from-pdf-to-pwn-scalable-0day-discovery-in-pdf-engines-and-services-using-multi-agent-llms-2/)
    ) in popular PDF platforms from Foxit and Apryse, potentially allowing attackers to exploit them for account takeover, session hijacking, data exfiltration, and arbitrary JavaScript execution. "Rather than isolated bugs, the issues cluster around recurring architectural failures in how PDF platforms handle untrusted input across layers," Novee Security researchers Lidor Ben Shitrit, Elad Meged, and Avishai Fradlis
    [said](https://novee.security/blog/hacker-trained-ai-discovers-16-new-0-day-vulnerabilities-in-pdf-engines/)
    . "Several vulnerabilities were exploitable with a single request and affected trusted domains commonly embedded inside enterprise applications." The issues have been addressed by both Apryse and Foxit through product updates.
22. Training labs expose cloud backdoors

    A "widespread" security issue has been discovered where security vendors inadvertently expose deliberately vulnerable training applications, such as OWASP Juice Shop, DVWA, bWAPP, and Hackazon, to the public internet. This can open organizations to severe security risks when they are executed from a privileged cloud account. "Primarily deployed for internal testing, product demonstrations, and security training, these applications were frequently left accessible in their default or misconfigured states," Pentera Labs
    [said](https://pentera.io/resources/research/exposed-cloud-training-apps)
    . "These critical flaws not only allowed attackers full control over the compromised compute engine but also provided pathways for lateral movement into sensitive internal systems. Violations of the principle of least privilege and inadequate sandboxing measures further facilitated privilege escalation, endangering critical infrastructure and sensitive organizational data." Further analysis has determined that threat actors are exploiting this blind spot to plant web shells, cryptocurrency miners, and persistence mechanisms on compromised systems.
23. Evasion loader refines C2 stealth

    The malware loader known as
    [Oyster](https://thehackernews.com/2025/07/seo-poisoning-campaign-targets-8500.html)
    (aka Broomstick or CleanUpLoader) has continued to evolve into early 2026, fine-tuning its C2 infrastructure and obfuscation methods, per findings from Sekoia. The malware is distributed mainly through fake websites that distribute installers for legitimate software like Microsoft Teams, with the core payload often deployed as a DLL for persistent execution. "The initial stage leverages excessive legitimate API call hammering and simple anti-debugging traps to thwart static analysis," the company
    [said](https://blog.sekoia.io/oysterloader-unmasked-the-multi-stage-evasion-loader/)
    . "The core payload is delivered in a highly obfuscated manner. The final stage implements a robust C2 communication protocol that features a dual-layer server infrastructure and highly-customized data encoding."
24. Stealer taunts researchers in code

    [Noodlophile](https://thehackernews.com/2025/08/noodlophile-malware-campaign-expands.html)
    is the name given to an information-stealing malware that has been distributed via fake AI tools promoted on Facebook. Assessed to be the work of a threat actor based in Vietnam, it was first documented by Morphisec in May 2025. Since then, there have been other reports detailing various campaigns, such as
    [UNC6229](https://thehackernews.com/2025/10/weekly-recap-wsus-exploited-lockbit-50.html#:~:text=UNC6229%20Uses%20Fake%20Job%20Postings%20to%20Spread%20RATs)
    and
    [PXA Stealer](https://thehackernews.com/2025/08/vietnamese-hackers-use-pxa-stealer-hit.html)
    , orchestrated by
    [Vietnamese cybercriminals](https://auteqia.garden/posts/malware/pxastealer/)
    . Morphisec's latest analysis of Noodlophile has revealed that the threat actor "padded the malware with millions of repeats of a colorful Vietnamese phrase translating to 'f\*\*\* you, Morphisec,'" suggesting that the operators were not thrilled about getting exposed. "Not just to vent frustration over disrupted campaigns, but also to bloat the file and crash AI-based analysis tools that are based on the Python disassemble library – dis.dis(obj)," security researcher Michael Gorelik
    [said](https://www.morphisec.com/blog/noodlophile-stealer-when-cybercriminals-get-a-bit-salty/)
    .
25. Crypto library RCE risk patched

    The OpenSSL project has patched a stack buffer overflow flaw that can lead to remote code execution attacks under certain conditions. The vulnerability, tracked as
    [CVE-2025-15467](https://nvd.nist.gov/vuln/detail/CVE-2025-15467)
    , resides in how the library processes Cryptographic Message Syntax data. Threat actors can use CMS packets with maliciously crafted AEAD parameters to crash OpenSSL and run malicious code. CVE-2025-15467 is one of 12 issues that were
    [disclosed](https://aisle.com/blog/aisle-discovered-12-out-of-12-openssl-vulnerabilities)
    by AISLE late last month. Another high-severity vulnerability is
    [CVE-2025-11187](https://nvd.nist.gov/vuln/detail/CVE-2025-11187)
    , which could trigger a stack-based buffer overflow due to a missing validation.
26. Machine accounts expand delegation risk

    New research from Silverfort has cleared a "common assumption" that
    [Kerberos delegation](https://www.silverfort.com/glossary/kerberos-delegation/)
    -- which allows a service to request resources or perform actions on behalf of a user -- applies not just to human users, but also to machine accounts as well. In other words, a computer account can be delegated on behalf of highly privileged machine identities such as domain controllers. "That means a service trusted for delegation can act not just on behalf of other users, but also on behalf of machine accounts, the most critical non-human identities (NHIs) in any domain," Silverfort researcher Dor Segal
    [said](https://www.silverfort.com/blog/delegation-part-two-insensitive-accounts/)
    . "The risk is obvious. If an adversary can leverage delegation, it can act on behalf of sensitive machine accounts, which in many environments hold privileges equivalent to Domain Administrator." To counter the risk, it's advised to run "Set-ADAccountControl -Identity “HOST01$” -AccountNotDelegated $true" for each sensitive machine account.

Security news rarely breaks in isolation. One incident leads to another, new research builds on older findings, and attacker playbooks keep adjusting along the way. The result is a constant stream of signals that are easy to miss without a structured view.

This roundup pulls those signals together into a single, readable snapshot. Go through the full list to get quick clarity on the developments shaping defender priorities and risk conversations right now.