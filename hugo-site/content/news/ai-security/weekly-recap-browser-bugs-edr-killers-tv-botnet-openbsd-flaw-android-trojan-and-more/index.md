---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-23T03:54:00.437742+00:00'
exported_at: '2026-06-23T03:54:03.335077+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/weekly-recap-browser-bugs-edr-killers.html
structured_data:
  about: []
  author: ''
  description: This week’s cybersecurity recap covers Firefox and Chrome bugs, EDR-killer
    tools, a TV botnet, an OpenBSD flaw, Android malware, Splunk exploitation,
  headline: '⚡ Weekly Recap: Browser Bugs, EDR Killers, TV Botnet, OpenBSD Flaw, Android
    Trojan, and More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/weekly-recap-browser-bugs-edr-killers.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: Browser Bugs, EDR Killers, TV Botnet, OpenBSD Flaw, Android
  Trojan, and More'
updated_at: '2026-06-23T03:54:00.437742+00:00'
url_hash: 862328431877a6fe28234ea99ee748732751c5f0
---

**

Ravie Lakshmanan
**

Jun 22, 2026

Cybersecurity / Hacking

It’s Monday again.

This week’s threat list looks painfully familiar: abused integrations, fake tools, poisoned websites, ransomware crews trying to shut down security tools, and mobile malware asking for way too much control.

The annoying part is how little of this feels new. Weak credentials, sketchy downloads, browser extensions with too much access, and WordPress sites are used to push more attacks. Nothing clever. Just sloppy, cheap, and effective.

Here’s the Monday recap. Let’s get into the week’s mess.

## **⚡ Threat of the Week**

**[FortiBleed Campaign Identifies Over 80K Targets](https://thehackernews.com/2026/06/cisa-warns-fortinet-customers-as.html)**
— A large-scale campaign codenamed FortiBleed has systematically targeted and compromised Fortinet FortiGate firewall and SSL VPN gateway devices worldwide. According to SOCRadar, it has been running since at least February 2026, with over 80,000 devices identified with working usernames and passwords that have been tested by suspected Russian-speaking threat actors using automated tools running around the clock. The U.S. Cybersecurity and Infrastructure Security Agency (CISA) urged Fortinet customers with FortiGate appliances to take steps to secure against ongoing malicious activity aimed at thousands of internet-accessible devices. Fortinet also said the campaign likely involves the threat actors reusing credentials from previous incidents, such as CVE-2026-24858, CVE-2025-59718, and CVE-2025-59719, along with employing brute-force techniques against devices with weak password hygiene and no multi-factor authentication (MFA).

## **🔔 Top News**

* **[Salesforce Disables Klue App Integration After New Extortion Campaign](https://thehackernews.com/2026/06/salesforce-disables-klue-app.html)**
  — Salesforce revealed that it disabled the Klue Battlecards app integration within its platform in response to a security incident impacting the competitive intelligence company on June 11, 2026. "Salesforce took this action because our security teams recently detected unusual activity involving the app that may have resulted in unauthorized access to a subset of customer data via the app's connection to Salesforce," the company said. "This issue is limited to Klue's app connection and does not arise from a vulnerability within the Salesforce platform." The development comes as an extortion group dubbed Icarus compromised and exfiltrated data from customers of Klue after obtaining access through a compromised legacy credential associated with an integration service. A number of companies have publicly acknowledged the incident, but noted the impact is limited.
* **[The Gentlemen RaaS Develops GentleKiller EDR Killer Suite](https://thehackernews.com/2026/06/the-gentlemen-raas-uses-gentlekiller.html)**
  — The Gentlemen ransomware-as-a-service (RaaS) operation is actively developing and maintaining a suite of endpoint detection and response (EDR) killers that it hands out to affiliates for shutting down endpoint detection and response (EDR) products before deploying the encryptor. The centerpiece of the group's EDR-disabling capability is GentleKiller, an in-house developed framework that comes in eight different variants, each one impersonating a different legitimate product and abusing a different vulnerable or malicious kernel driver. GentleKiller targets over 400 processes belonging to 48 security products, including CrowdStrike, SentinelOne, Microsoft Defender, Sophos, Kaspersky, and ESET itself.
* **[Splunk Flaw Actively Exploited in the Wild](https://thehackernews.com/2026/06/critical-splunk-enterprise-flaw-lets.html)**
  — Splunk's Product Security Incident Response Team (PSIRT) said it became aware of "limited exploitation" of CVE-2026-20253, a critical flaw in Splunk Enterprise that could be exploited to conduct unauthenticated file operations and even remote code execution. "In Splunk Enterprise versions below 10.2.4 and 10.0.7, an unauthenticated user could create or truncate arbitrary files through a PostgreSQL sidecar service endpoint," Splunk said. "The vulnerability exists because the PostgreSQL sidecar service endpoint lacks authentication controls, allowing any network-reachable user to invoke file operations without credentials." In an analysis of the flaw, Resecurity said it's "particularly dangerous" as it can be exploited remotely without authentication or user interaction. "By chaining multiple weaknesses together, an attacker can progress from unauthenticated access to arbitrary file operations and ultimately Remote Code Execution (RCE)," it
  [said](https://www.resecurity.com/blog/article/cve-2026-20253-splunk-enterprise-pre-authentication-remote-code-execution)
  . "A successful compromise may expose sensitive logs, credentials, security alerts, and operational data while providing attackers with a foothold for persistence, defense evasion, and lateral movement within the environment."
* **[Unpatchable 'usbliter8' Exploit Targets Apple A12 and A13 Chips](https://thehackernews.com/2026/06/unpatchable-usbliter8-exploit-breaks.html)**
  — Security researchers at Paradigm Shift released details of a working exploit dubbed usbliter8 that could be abused to achieve arbitrary code execution inside the SecureROM of Apple's A12 and A13 chips. The vulnerability is classified as a hardware bug residing in the Synopsys DWC2 USB controller, meaning the issue can never be patched. That said, a successful exploitation requires an attacker to have physical access to a vulnerable device. A proof-of-concept for usbliter8 has been made publicly available.
* **[Operation Endgame Disrupts SocGholish Servers](https://thehackernews.com/2026/06/operation-endgame-disrupts-socgholish.html)**
  — Dutch law enforcement authorities, along with counterparts from Canada, Germany, and the U.S., have disrupted malicious infrastructure associated with SocGholish and cleaned up nearly 15,000 infected WordPress websites. The takedown is part of Operation Endgame, an ongoing international law enforcement initiative to combat botnets and associated criminal infrastructures. It was launched in 2024. As part of the effort, 106 servers linked to SocGholish have been taken down, and 14,971 WordPress sites have been rid of the infections. Website owners have been notified to update their content management system (CMS), change their credentials, and delete any suspicious accounts.
* **[Malicious Campaign Fakes Popularity to Deliver Crypto Clipper](https://thehackernews.com/2026/06/crypto-clipper-campaign-abuses-fake.html)**
  — A cryptocurrency-stealing malware campaign has been targeting cryptocurrency asset holders and online gamblers by faking its own popularity, dressing up booby-trapped sniper bots and crash-game predictors with bogus GitHub stars, inflated download counts, and artificial intelligence (AI)-narrated YouTube tutorials. The activity has been traced to a Rust-based clipper malware targeting Windows and macOS users. The lures are "edge" tools that promise easy money, crypto sniper bots, and "predictors" that claim to forecast crash-gambling games, aimed at traders and gamblers chasing shortcuts, while a WordPress phishing page acts as the hub, funneling victims to the downloads.
* **[Rokarolla Android Trojan Combines Banking Fraud with Screen Surveillance](https://thehackernews.com/2026/06/new-rokarolla-android-malware-steals.html)**
  — A new "invasive" Android trojan dubbed Rokarolla is being distributed via malicious websites, while masquerading as popular applications like TikTok or Google Chrome. It's designed to target 217 distinct cryptocurrency and banking applications by serving fake overlay login screens, in addition to leveraging 137 commands that grant it complete control of a compromised device. It can harvest lock screen credentials, exfiltrate sensitive contact lists and SMS data, monitor the screen to capture WhatsApp data, take screenshots by abusing Android's accessibility services, redirect cryptocurrency transactions, and utilize keyloggers to continuously record user input. The malware also actively hides its presence from the launcher screen and disrupts user intervention by blocking incoming calls, deploying fraudulent screen overlays, suppressing device audio, and deactivating Google Play Protect. "The infection process begins when a dropper misleads users into installing a secondary payload containing the core malware," Zimperium said. "By masquerading as Google Play Protect, the dropper facilitates the installation of this payload. This strategy allows the malware to evade Android restrictions and exploit Accessibility services."

## **🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first —
[CVE-2026-20262](https://thehackernews.com/2026/06/cisco-releases-security-updates-for.html)
(Cisco SD-WAN Manager),
[CVE-2026-54420](https://thehackernews.com/2026/06/cisa-flags-litespeed-cpanel-plugin-flaw.html)
(LiteSpeed cPanel Plugin),
[CVE-2026-48907](https://thehackernews.com/2026/06/cisa-warns-of-actively-exploited-joomla.html)
(Widget Factory Joomla Content Editor),
[CVE-2026-4020](https://thehackernews.com/2026/06/hackers-exploit-gravity-smtp-wordpress.html)
(Gravity SMTP WordPress Plugin),
[CVE-2026-47101, CVE-2026-47102, CVE-2026-40217](https://www.obsidiansecurity.com/blog/litellm-privilege-escalation-rce)
,
[CVE-2026-49468](https://github.com/BerriAI/litellm/security/advisories/GHSA-4xpc-pv4p-pm3w)
(LiteLLM),
[CVE-2026-24190](https://www.levelblue.com/blogs/spiderlabs-blog/reversing-nvidias-cve-2026-24190-how-a-kernel-flaw-put-enterprise-ai-clusters-and-workstations-at-risk)
(NVIDIA Display Driver for Windows and Linux),
[CVE-2026-48558](https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/)
(SimpleHelp),
[CVE-2026-39449](https://patchstack.com/database/wordpress/plugin/contact-form-to-any-api/vulnerability/wordpress-contact-form-to-any-api-plugin-3-0-3-cross-site-scripting-xss-vulnerability)
(Contact Form to Any API WordPress plugin),
[CVE-2026-39849](https://github.com/pi-hole/FTL/security/advisories/GHSA-9cqv-839p-gpq2)
,
[CVE-2026-44693](https://github.com/pi-hole/FTL/security/advisories/GHSA-9ff5-f3v5-2xc7)
(Pi-hole FTL),
[CVE-2026-49980](https://github.com/rclone/rclone/security/advisories/GHSA-qw24-gh76-8rvv)
,
[CVE-2026-41179](https://github.com/rclone/rclone/security/advisories/GHSA-jfwf-28xr-xw6q)
,
[CVE-2026-41176](https://github.com/rclone/rclone/security/advisories/GHSA-25qr-6mpr-f7qx)
(Rclone),
[CVE-2026-54157](https://github.com/lobehub/lobehub/security/advisories/GHSA-xmwj-c75x-6346)
(@lobehub/lobehub),
[CVE-2026-48746](https://github.com/vllm-project/vllm/security/advisories/GHSA-94f4-hr76-p5j6)
(vllm),
[CVE-2026-48519](https://github.com/langflow-ai/langflow/security/advisories/GHSA-v5ff-9q35-q26f)
(Langflow),
[CVE-2026-38329](https://github.com/advisories/GHSA-9r27-c92g-8g7q)
(Bludit CMS),
[CVE-2026-39949](https://github.com/lukehebe/CVE-2026-39949/tree/main)
(Cacti),
[CVE-2026-8444](https://patchstack.com/database/wordpress/plugin/wp-review-slider-pro/vulnerability/wordpress-wp-review-slider-pro-plugin-12-6-8-authenticated-subscriber-sql-injection-vulnerability-2)
(WP Review Slider Pro WordPress plugin),
[CVE-2026-52697](https://patchstack.com/database/wordpress/plugin/taskbuilder/vulnerability/wordpress-taskbuilder-plugin-5-0-7-sql-injection-vulnerability)
(Taskbuilder WordPress plugin),
[CVE-2026-52700](https://patchstack.com/database/wordpress/plugin/wc-multishipping/vulnerability/wordpress-wcmultishipping-plugin-3-0-2-sql-injection-vulnerability)
(WCMultiShipping WordPress plugin),
[CVE-2026-3326](https://patchstack.com/database/wordpress/theme/xstore/vulnerability/wordpress-xstore-theme-9-7-3-unauthenticated-sqli-vulnerability)
(XStore WordPress theme),
[CVE-2026-2418](https://patchstack.com/database/wordpress/plugin/login-with-salesforce/vulnerability/wordpress-login-with-salesforce-plugin-1-0-2-unauthenticated-authentication-bypass-vulnerability)
(Login with Salesforce WordPress plugin),
[CVE-2026-6379](https://patchstack.com/database/wordpress/plugin/wp-photo-album-plus/vulnerability/wordpress-wp-photo-album-plus-plugin-9-1-11-001-unauthenticated-sql-injection-via-wppa-supersearch-parameter-vulnerability)
(WP Photo Album Plus WordPress plugin),
[CVE-2026-2446](https://patchstack.com/database/wordpress/plugin/powerpack-for-learndash/vulnerability/wordpress-powerpack-for-learndash-plugin-1-3-0-unauthenticated-arbitrary-option-update-vulnerability)
(PowerPack for LearnDash WordPress plugin),
[CVE-2025-15445](https://patchstack.com/database/wordpress/theme/restaurant-cafeteria/vulnerability/wordpress-restaurant-cafeteria-theme-0-4-6-subscriber-arbitrary-plugin-installation-activation-vulnerability)
(Restaurant Cafeteria WordPress theme),
[CVE-2026-8443](https://patchstack.com/database/wordpress/plugin/wp-review-slider-pro/vulnerability/wordpress-wp-review-slider-pro-plugin-12-6-8-authenticated-subscriber-sql-injection-vulnerability)
(WP Review Slider Pro WordPress plugin),
[CVE-2026-6933](https://patchstack.com/database/wordpress/plugin/premmerce-dev-tools/vulnerability/wordpress-premmerce-dev-tools-plugin-2-0-missing-authorization-to-authenticated-subscriber-remote-code-execution-vulnerability)
(Premmerce Dev Tools WordPress plugin),
[CVE-2026-9848](https://patchstack.com/database/wordpress/plugin/wp-ticket/vulnerability/wordpress-customer-support-ticket-system-helpdesk-plugin-6-0-4-unauthenticated-sql-injection-vulnerability)
(WP Ticket Customer Service Software &amp; Support Ticket System WordPress plugin),
[CVE-2026-52707](https://patchstack.com/database/wordpress/theme/kastell/vulnerability/wordpress-kastell-theme-2-0-local-file-inclusion-vulnerability)
(Kastell WordPress theme),
[CVE-2026-52703](https://patchstack.com/database/wordpress/plugin/fastdup/vulnerability/wordpress-fastdup-plugin-2-7-2-path-traversal-vulnerability)
(FastDup WordPress plugin),
[CVE-2026-52706](https://patchstack.com/database/wordpress/plugin/jet-engine/vulnerability/wordpress-jetengine-plugin-3-8-10-php-object-injection-vulnerability)
(JetEngine WordPress plugin),
[CVE-2026-27429](https://patchstack.com/database/wordpress/theme/nifty/vulnerability/wordpress-nifty-theme-1-4-1-php-object-injection-vulnerability)
(Nifty WordPress theme),
[CVE-2025-69129](https://patchstack.com/database/wordpress/plugin/wp_scraper/vulnerability/wordpress-wordpress-woocommerce-scraper-plugin-import-data-from-any-site-plugin-1-0-7-arbitrary-file-upload-vulnerability)
(WordPress &amp; WooCommerce Scraper WordPress plugin),
[CVE-2026-27400](https://patchstack.com/database/wordpress/plugin/ovabookpro/vulnerability/wordpress-bookpro-plugin-1-1-0-arbitrary-file-deletion-vulnerability)
(BookPro WordPress plugin),
[CVE-2026-8713](https://www.wordfence.com/blog/2026/06/critical-unauthenticated-arbitrary-file-deletion-vulnerability-patched-in-avada-builder-wordpress-plugin/)
(Avada Builder WordPress plugin),
[from CVE-2026-12437 through CVE-2026-12443](https://chromereleases.googleblog.com/2026/06/stable-channel-update-for-desktop_01750511403.html)
(Google Chrome),
[CVE-2026-12326, CVE-2026-12327, CVE-2026-12328](https://www.mozilla.org/en-US/security/advisories/mfsa2026-57/)
(Mozilla Firefox),
[CVE-2026-8049, CVE-2026-8050](https://kb.cert.org/vuls/id/380058)
(SignalRGB kernel driver),
[CVE-2026-20266](https://advisory.splunk.com/advisories/SVD-2026-0614)
(Splunk AI Toolkit),
[CVE-2026-41293, CVE-2026-43512, CVE-2026-42579, CVE-2026-42584, CVE-2026-43515](https://confluence.atlassian.com/security/security-bulletin-june-16-2026-1796309326.html)
(Atlassian Confluence Data Center and Server),
[CVE-2026-20181, CVE-2026-20190](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ise-multi-G5WP8vv)
(Cisco Identity Services Engine and ISE Passive Identity Connector),
[CVE-2026-48933, CVE-2026-48618](https://nodejs.org/en/blog/vulnerability/june-2026-security-releases)
(Node.js),
[CVE-2026-9862](https://www.fortra.com/security/advisories/product-security/fi-2026-007)
(Fortra Core Privileged Access Manager), and
[multiple vulnerabilities](https://github.com/unclecode/crawl4ai/security/advisories/GHSA-365w-hqf6-vxfg)
in Crawl4AI Docker API (no CVEs).

## **🎥 Cybersecurity Webinars**

* [Your Company Is Using More AI Than You Can See. Here’s How to Secure It](https://thehacker.news/securing-ai-use)
  → AI bots are actively accessing your company’s sensitive data—often without a clear human owner to hold accountable. Join this webinar to learn how to uncover hidden AI tools, lock down their permissions, and safely take back control of your network before a blind spot becomes a massive data breach.
* [Machine-Speed Attacks are Here: How to Stop AI-Powered Hackers](https://thehacker.news/outpacing-mythos-cyberattacks)
  → Hackers are now using AI to launch lightning-fast, highly convincing attacks that easily slip past traditional security. If your defenses rely on old, 'human-speed' tools, you're already falling behind. Join this critical webinar to see exactly how AI-powered threats operate—and get a clear, practical blueprint to lock down your network and stop machine-speed attacks in their tracks.

## **📰 Around the Cyber World**

* **Flaws in SiderAI and MaxAI**
  — Critical vulnerabilities have been disclosed in SiderAI (Spyder) and MaxAI (MaXSS) agentic side-panel Chrome extensions that can allow malicious websites to take screenshots of arbitrary websites or run arbitrary code by taking advantage of the add-ons' permissions. "Abusing these vulnerabilities allows attackers to compromise all browser sessions across any website, leading to the leakage of sensitive information, the invocation of arbitrary commands, and even account takeover," Rebora
  [said](https://rebora.io/blog/spyder-and-maxss-chrome-extension-vulnerabilities-put-millions-at-risk/)
  . "Furthermore, there was a potential risk of stealing files from the underlying operating system." Both extensions have a "Featured" badge and have been collectively installed nearly 7 million times. Given that the issues remain unpatched, users are recommended to remove them until fixes are in place.
* **Israeli Company Linked to Popa Android TV Box Botnet**
  — The Popa Android TV box botnet, which has been used for residential proxy traffic in ad fraud and website scraping, has been attributed to
  [NetNut](https://spur.us/blog/how-proxy-providers-co-opt-entire-networks)
  , operated by publicly traded Israeli company Alarum Technologies.
  [Qurium](https://www.qurium.org/forensics/finding-popa/)
  , along with the
  [Nokia Deepfield Emergency Response Team](https://github.com/deepfield/public-research/blob/main/reports/2026-06-18-robovpn-neunative.md)
  and
  [Synthient](https://synthient.com/blog/popa-from-sourcing-to-distribution)
  , has found that Popa is a "residential proxy software family that turns consumer devices into internet relay nodes" by means of a software development kit. It's worth noting that Popa was
  [first flagged by QiAnXin XLab](https://thehackernews.com/2025/03/vo1d-botnets-peak-surpasses-159m.html)
  in March 2025 as an Android component of the Vo1d botnet. "So Popa is not a traditional downloader or banking trojan, the ultimate goal of the code is just to implement a persistent communications layer capable of registering a device, maintaining long-lived encrypted connections, and opening tunnels on demand," according to the report. "Not differently from many other types of malware, Popa does not connect directly to a fixed command-and-control server. The compromised device starts by connecting a limited set of domain names to later learn where to register and tunnel the traffic." The botnet has impacted millions of consumer TV boxes over the last four years. Alarum, which also maintains RoboVPN, a commercial VPN service that includes a residential-proxy SDK that turns the user's machine into an exit node for third-party traffic. In a statement
  [shared](https://krebsonsecurity.com/2026/06/popa-botnet-linked-to-publicly-traded-israeli-firm/)
  with cybersecurity journalist Brian Krebs, NetNut and Alarum have disputed the allegations, calling them "demonstrably inaccurate assertions and flawed deductions rather than verified facts," adding "the SDKs at issue are designed to facilitate bandwidth-sharing functionality and do not transform user devices into malware-controlled systems or otherwise compromise the devices on which they operate." The development comes weeks after
  [another report from Include Security](https://thehackernews.com/2026/06/free-apps-are-quietly-turning-smart-tvs.html)
  found that an iOS SDK that Bright Data embeds in consumer apps can turn devices, including always-on smart TVs, into exit nodes that relay web-scraping traffic with users' consent.
* **Prinz Eugen Encrypts Recently Modified Files**
  — A new Go-based ransomware called Prinz Eugen has been observed targeting recently modified files for encryption. "It performs recursive encryption, prioritizes recently modified files, uses ChaCha20-Poly1305 with integrity checks, and leaves no ransom note on disk," Threatdown
  [said](https://www.threatdown.com/blog/prinz-eugen-ransomware-a-deep-dive-into-a-new-go-based-encryptor/)
  . It's suspected that the attackers gain initial access through compromised RDP credentials. The ransomware binary also takes steps to frustrate forensic analysis and recovery. The ransomware has been attributed to an actor called ROOTBOY, who has a track record of selling stolen data on cybercrime forums.
* **Okendo Reviews Widget Compromised in SmartApeSG Supply Chain Attack**
  — Okendo Reviews widget, a popular customer review platform used by more than 18,000 brands, is said to have been compromised as part of attacks designed to deploy malware via embedded malicious JavaScript code. The activity, detected on May 14, 2026, has been tied to SmartApeSG, which was previously observed using
  [ClickFix and FakeUpdates lures](https://www.blumira.com/blog/smartapesg-returns-with-unique-obfuscation-techniques)
  to distribute NetSupport Manager. "The injected JavaScript used obfuscation, environment checks, and staged execution," Zscaler
  [said](https://www.zscaler.com/blogs/security-research/smartapesg-launches-okendo-reviews-supply-chain-attack)
  . "The SmartApeSG injected JavaScript behaved as a staged loader, and did not attempt to execute every action immediately. Instead, the JavaScript focused on control, reconstruction, and retrieval, which reduced the visibility of the script and gave the operator more flexibility." The end goal of the attacks is to serve bogus ClickFix prompts that lead to malware deployment. In the past, SmartApeSG has also
  [relied](https://hunt.io/blog/russian-malicious-infrastructure-c2-servers-mapped)
  on command-and-control (C2) servers hosted on Russian infrastructure providers to communicate with hosts infected with Remcos RAT through fake CAPTCHA prompts injected into websites that instructed users to execute commands copied to the clipboard. Okendo has since addressed the issue and restored the widget script to a clean state.
* **AI-Generated Websites Used to Deliver SmartRAT**
  — Typosquatting domains hosting malicious content generated with AI-powered website creation tools are being used to deliver a PowerShell-based malware called SmartRAT (aka
  [Banana RAT](https://thehackernews.com/2026/05/threatsday-bulletin-linux-rootkits.html#brazilian-banking-rat)
  ). The web page impersonates a Brazilian bank and a
  [ClickFix lure](https://thehackernews.com/2026/06/clickfix-campaigns-expand-malware.html)
  to trick victims into running a PowerShell command that downloads the malware. "Threat actors are leveraging website builders to create convincing lures quickly and at scale, with capabilities ranging from basic credential theft to a ClickFix campaign that delivers remote access trojans (RATs)," Zscaler
  [said](https://www.zscaler.com/blogs/security-research/clickfix-campaign-generated-ai-delivers-smartrat)
  . "SmartRAT supports encrypted C2 communications, remote control (screen/keyboard/mouse), credential theft (keylogging and banking overlays), and persistence via scheduled tasks and a Windows service."
* **ClickFix Delivers GuLoader**
  — Another ClickFix has been observed using a combination of ClickFix and
  [EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)
  to deliver malware called
  [GuLoader](https://thehackernews.com/2022/12/guloader-malware-utilizing-new.html)
  using a compromised WordPress site as an entry point. "The attack chain combines four distinct components, compromised WordPress, EtherHiding via BSC Testnet, ClickFix social engineering, and GULoader delivery via UNC path, into a single intrusion sequence where every traditional defensive layer has a structural reason to remain silent," Sicuranext said.
* **UnregStealer Targets Brazilian Banks**
  — A new purpose-built trojan called UnregStealer has been targeting Latin America (LATAM) financial institutions. Described as a human-operated credential theft campaign, it was first discovered by IBM X-Force in May 2026. "Most LATAM banking trojans rely on automated infection chains and compiled malware, UnregStealer is different," the company
  [said](https://www.ibm.com/think/news/unregstealer-human-operated-browser-credential-theft-targeting-brazilian-banking)
  . "trojans rely on automated infection chains and compiled malware, UnregStealer is different. This trojan involves a real operator, who watches each victim's session live and pulls the trigger manually. This variation makes the campaign nearly invisible to sandboxes and behavioral detection systems that never see the payload activate." Attack chains begin with social engineering lures that masquerade as mandatory SSL certificate updates to deliver a PowerShell stager, ultimately resulting in the deployment of a malicious Chrome extension named "Certificado SSL Chrome" that's responsible for data theft and exfiltration. In recent months, LATAM financial institutions have been targeted by a JavaScript adversary-in-the-middle (AitM) framework called OverlordMX that also makes use of a human operator, who monitors victims in real time and manually triggers the necessary overlays to capture credentials. The campaign is assessed to be the work of a Spanish-speaking threat actor. "The attack operates in two stages: a web-inject layer that intercepts sensitive information from the victim, followed by a socially engineered RAT delivery that grants the operator full remote control of the victim’s device," IBM
  [said](https://www.ibm.com/think/news/overlordmx-new-social-engineering-campaign-targeting-latam)
  .
* **Pushka Android Malware Detailed**
  — An Android malware called Pushka is equipped to carry out on-device fraud, while granting remote access trojan (RAT) capabilities to the operators by abusing accessibility services. "Pushka can use fake overlay tactics to phish victims' credentials on their mobile devices and can further steal and exfiltrate data from their devices," IBM X-Force
  [said](https://www.ibm.com/think/news/pushka-malware-cannon-knows-how-fire-back)
  . "Pushka's RAT capabilities can perform actions on behalf of the user, including entering the user's login credentials, and clicking buttons." Pushka was first spotted in September 2025 across different European countries. It uses fake TV apps as decoys to trick users into installing them. The app acts as a dropper, and uses Android's PackageInstaller.Session API to silently install its main payload while bypassing Android 13’s Restricted Settings. "This method replaces the traditional use of Intent.ACTION\_INSTALL\_PACKAGE and is specifically used to mimic the legitimate installation flow used by the Play Store, allowing the malware to evade the OS-level restrictions introduced in newer Android versions," IBM said.
* **Ransomware Ecosystem Consolidates in Q1 2026**
  — Data from Flare
  [shows](https://flare.io/learn/resources/blog/ransomware-as-a-service-lockbit-alumni-launch-competing-programs-as-ecosystem-co)
  that the ransomware ecosystem is "reconsolidating around fewer, more capable operators after a fragmented stretch," led by brands like LockBit, Qilin, and The Gentlemen. The top 10 groups account for 71% of all Q1 2026 victims, with LockBit 5.0 logging 163 victims.
* **Australian Bank Accounts Targeted by Extension-Based Trojan**
  — A highly sophisticated browser extension-based banking is targeting Australian banking customers. "This is not a traditional virus designed to crash systems or cause visible disruption," IBM
  [said](https://www.ibm.com/think/news/invisible-thief-sophisticated-browser-extension-emptying-bank-accounts)
  . "Instead, it is specifically engineered to function as an invisible threat, embedding itself within the browser and operating directly inside the victim's trusted, authenticated session." It comes with capabilities to alter displayed balances, transaction history, and transfer limits; intercept one-time passwords (OTP) before submission; steal active banking session cookies; track visited pages and transaction patterns; and maintain a persistent WebSocket C2 connection for real-time commands. Exactly how the extension is distributed is unclear. "Because the attack runs within a legitimate, authenticated session, it inherits the user’s trust context and security controls, effectively neutralizing traditional protections," the company added.
* **Chinese and Russian Influence Operations Use AI to Bypass Bot Detection**
  — In a new report, Two Six Technologies said Russian and Chinese inauthentic accounts are likely using AI to enhance content quality rather than to increase content volume and exhibit fewer bot-like behaviours. "AI is enabling and motivating adversaries to craft better content and more human-like accounts," the company
  [said](https://twosixtech.com/blog/more-sophistication-less-slop-russian-and-chinese-malign-influence-actors-are-working-smarter-in-the-age-of-ai/)
  . "Inauthentic accounts are using AI to add visual appeal to their content. To reach broader audiences, they are probably also using it for translation. Pro-Russia and pro-China accounts now have slower posting speeds, and more pro-Russia accounts are inactive for a long stretch each day, mimicking a human who sleeps."
* **Operation Escaneo Targets Mexican Federal and Financial Orgs**
  — A sophisticated campaign targeting Latin American governments and financial institutions has come to light, thanks to an exposed attacker server ("62.171.185[.]97") that revealed the custom tools, exploitation chain, and persistence tactics adopted by the threat actors. "The campaign is characterised by a proprietary distributed reconnaissance engine (Kimera), a curated exploit armory targeting enterprise perimeter devices (Fortinet, Ivanti, Cisco), portable lateral movement toolkits, and layered command-and-control infrastructure using Neo-reGeorg webshells, Chisel reverse tunnels, and compromised Cisco routers with persistent GRE tunnels," CloudSEK
  [said](https://www.cloudsek.com/blog/operation-escaneo-mexican-government-financial-institutions-cyberattack)
  . "The threat actor demonstrated capability to operate across Windows and Linux environments, compromise SAP ERP and Oracle database systems for command execution, extract cryptographic material and Active Directory datasets, and maintain long-dwell access through multiple redundant persistence mechanisms." The activity has been attributed medium confidence to a group called PanchoVilla (aka MexicanMafia).
* **GNU Savannah Security Flaw Fixed**
  — The Free Software Foundation (FSF) said it has addressed an exploit demonstrated by Hacktron, alongside additional security issues. "After thorough review, we have found no reason to believe that sensitive project data or credentials were accessed, nor that there has been any compromise of Savannah's software supply chain," the FSF
  [said](https://www.fsf.org/news/statement-regarding-gnu-savannah-security-reports)
  . "Though the initial security issue was reported to us in early May, the vulnerabilities were discovered in software that was published approximately two years prior. We will be communicating directly with Savannah-hosted projects about steps they can take to review and strengthen the security of their projects."
* **27-Year-Old Authentication Bypass in OpenBSD**
  — Argus said it discovered a
  [27-year-old authentication bypass flaw](https://www.openwall.com/lists/oss-security/2026/06/16/9)
  in OpenBSD's PPP stack that could be used to sidestep Password Authentication Protocol (PAP) entirely. "OpenBSD's sppp\_pap\_input function used attacker-controlled length fields as the bcmp comparison length for credential validation," the company
  [said](https://blog.argus-systems.ai/blog/openbsd-pap-27-year-auth-bypass.html)
  . "Sending zero-length name and password fields caused bcmp to return 0 unconditionally, bypassing PAP authentication entirely." The flaw was introduced in July 1999. A fix was issued on June 14, 2026.
* **Abusing AI Features in SQL Server 2025 for C2**
  — SpecterOps has
  [revealed](https://specterops.io/blog/2026/06/10/oops-i-weaponized-the-database-abusing-ai-features-in-mssql-2025/#h-defensive-considerations)
  that it's possible to weaponize native AI features in Microsoft SQL Server 2025, such as sp\_invoke\_external\_rest\_endpoint, CREATE EXTERNAL MODEL, and AI\_GENERATE\_EMBEDDINGS as a practical channel for data exfiltration and C2, assuming an attacker has compromised an account with the sysadmin role in the database. To counter the threat, it's essential to review SQL Server database logins, audit and alert usage of xp\_cmdshell, SQL Agent Jobs, and CLR Assemblies, and set up notifications for any changes to sys.external\_models or when sp\_invoke\_external\_rest\_endpoint is enabled.
* **ErrTraffic TDS Exposed**
  — A traffic distribution system (TDS) known as
  [ErrTraffic](https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html)
  is being operated under a malware-as-a-service (MaaS) model for bad actors to direct users to ClickFix lures. ErrTraffic is a JavaScript framework that's injected into compromised WordPress sites. It employs the
  [EtherHiding](https://www.levelblue.com/blogs/spiderlabs-blog/err-hiding-and-seek-how-errtraffic-v3-leverages-etherhiding-in-clickfix-campaign)
  technique as a dead drop resolver to hide its C2 infrastructure within the blockchain. Sekoia's analysis of the framework has
  [identified](https://blog.sekoia.io/unveiling-errtraffic-inside-a-growing-clickfix-malware-distribution-framework/#h-backdoor)
  two distinct clusters of activity: Analytics and Beer. While Analytics interacts with the Polygon blockchain to fetch Vidar Stealer, the Beer cluster distributes several stealer families, including Vidar, Stealc, Remus and Salat. Alternatively, malvertising lures impersonating AI tools like Google Antigravity and OpenAI ChatGPT have also been used by the Analytics cluster to propagate DanaBot and Hijack Loader. A threat actor using the name LenAI has advertised and sold the ErrTraffic framework, with a one-month subscription costing $380. The attackers have also been found to use credential stuffing attacks to gain initial access to WordPress accounts and install PHP backdoors on the sites by masquerading as a
  [must-use plugin](https://thehackernews.com/2025/03/hackers-exploit-wordpress-mu-plugins-to.html)
  .
* **Malicious Resumes Lead to Xctdoor Malware**
  — AhnLab has disclosed details of a new campaign that uses malicious Windows Shortcut (LNK) files disguised as resumes that, upon execution, display decoy documents, while dropping additional scripts which then employ DLL side-loading to deploy
  [Xctdoor](https://thehackernews.com/2024/07/south-korean-erp-vendors-server-hacked.html)
  , a Go-based backdoor previously attributed to North Korean threat actors. "This attack is a method of executing an LNK file disguised as a normal document, using a task scheduler and a startup program to ensure persistence, and then exploiting the normal executable to execute backdoor malware," AhnLab
  [said](https://asec.ahnlab.com/ko/94163/)
  .
* **Bypassing Microsoft Entra Conditional Access Policies**
  — NetSPI said it found a way to bypass Microsoft Entra Conditional Access Policies by abusing Nested App Authentication to return access tokens for the Microsoft Graph API. "It was possible to use certain Nested App Authentication (or BroCI) flows to bypass any Conditional Access policy," security researcher Thomas Byrne
  [said](https://www.netspi.com/blog/technical-blog/cloud-pentesting/bypassing-microsoft-entra-conditional-access-policies-via-nested-app-authentication/)
  . "This vulnerability served mainly as a persistence mechanism as it would have required a successful phishing attack to return an initial refresh token before the vulnerable authentication flows could be carried out." A fix for the issue has since been rolled out by Microsoft.
* **Mexican Financial Sector Targeted by GitBait**
  — At least a dozen Mexican banks have been targeted by a modular phishing infrastructure dubbed GitBait that abuses GitHub-hosted Pages and employs obfuscated scripts and a centralized credential exfiltration via SheetBest API. Per
  [Group-IB](https://www.group-ib.com/blog/gitbait-phishing-mexico-banking-finance/)
  , the large-scale campaign has been active for three years. The activity is "built on a fully serverless architecture that abuses GitHub Pages for hosting and the SheetBest API for credential exfiltration — eliminating the need for any dedicated backend infrastructure." It's believed that victims are reached through common phishing delivery channels such as SMS, messaging apps, email, or social media platforms. In all cases, the victim receives a fraudulent URL that directs them to a phishing page impersonating a trusted financial institution. The phishing pages harvest user credentials, payment card details, client identifiers, and passwords through a multi-stage flow that mimics legitimate banking authentication workflows. In some cases, the captured data is exfiltrated to a Telegram bot, marking a deviation from the SheetBest-based mechanism. More than 100 domains associated with the campaign have been identified.
* **Email Bombing Leads to Deno-Based Proxy and RAT**
  — A large-scale
  [email flooding campaign](https://thehackernews.com/2026/03/fake-tech-support-spam-deploys.html)
  is being used as a pretext to target employees with bogus Microsoft Teams calls from an attacker impersonating internal IT support. Victims are then persuaded to download and execute a malicious archive from a fake self-service portal. The archive contains a modular Deno-based Remote Access Trojan and a TCP proxy framework spanning four different JavaScript files. "The JavaScript files implement a Deno-based remote access and tunneling agent," InfoGuard Labs
  [said](https://labs.infoguard.ch/posts/anatomy_deno_rat/)
  . "The main backdoor connects to a CloudFront-hosted WebSocket C2 endpoint, registers victim identity metadata, receives commands, and brokers traffic through local helper services." The proxy turns the compromised host into a pivot point for internal network access, allowing the attacker to route traffic through the victim machine.

## **🔧 Cybersecurity Tools**

* [Aether](https://github.com/0xsp-SRD/aether)
  → Because advanced malware often evades standard antivirus software by executing directly in a system's RAM, security teams need tools to inspect live memory. Aether is an open-source Windows threat-hunting tool that scans active, running processes for hidden payloads, code injections, and malicious behaviors, using a layered validation model to minimize false alarms during incident response.
* [AzureRedOps](https://github.com/Mr-Un1k0d3r/AzureRedOps)
  → It is an open-source offensive security toolkit designed to streamline Microsoft Entra ID and Azure red teaming. It unifies complex workflows—such as multi-flow token management, directory enumeration, and post-exploitation Microsoft Graph actions—into a single command-line interface.

*Disclaimer: This is strictly for research and learning. It hasn't been through a formal security audit, so don't just blindly drop it into production. Read the code, break it in a sandbox first, and make sure whatever you’re doing stays on the right side of the law.*

## **Conclusion**

This week’s lesson: most attacks do not need a genius move. They need one trusted app, one stale login, one noisy plugin, or one user chasing a shortcut.

The fix starts in the dull places. Cut access. Clean old sites. Question helper tools. Watch the small cracks, because that is where the week usually starts leaking.