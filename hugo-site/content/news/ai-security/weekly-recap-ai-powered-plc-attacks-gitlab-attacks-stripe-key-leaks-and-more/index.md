---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-09-17T06:10:41.104361+00:00'
exported_at: '2026-09-17T06:10:42.407178+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html
structured_data:
  about: []
  author: ''
  description: AI-powered PLC attacks, GitLab exploits, npm backdoors, cloud leaks,
    auth abuse, and payment fraud lead this week’s cybersecurity recap.
  headline: '⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks
    and More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/08/weekly-recap-ai-powered-plc-attacks.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: AI-Powered PLC Attacks, GitLab Attacks, Stripe Key Leaks and
  More'
updated_at: '2026-09-17T06:10:41.104361+00:00'
url_hash: 931eb972dbc1a65eea4dadae7dc2c45ec48f2b8e
---

**

Ravie Lakshmanan
**

Aug 24, 2026

Cybersecurity / Hacking

A package gets installed. A login prompt opens. A box sits exposed to the internet. Nothing looks unusual yet.

That’s roughly the mood this week. Trusted tools turn hostile, old weak spots get fresh attention, AI makes exploit work cheaper, and researchers keep finding attacks that sound harder than they actually are.

Plenty to clean up. Here’s the short version.

## **⚡ Threat of the Week**

**[U.S. Warns of AI-Powered Attacks on Siemens PLCs](https://thehackernews.com/2026/08/ai-generated-exploit-scripts-target.html)**
— Threat actors are using AI to write exploit scripts targeting internet-exposed Siemens S7 Series programmable logic controllers (PLCs) used across water, energy, manufacturing, and other critical infrastructure sectors, according to the U.S. government. The agencies warned: "This is not a theoretical risk—it is an active threat." The exploitation of poorly secured PLCs could result in disruption of critical industrial processes, safety incidents, downtime or equipment damage, compromise of sensitive data, and compliance violations, not to mention have cascading impacts across interconnected systems. Threat actors have been observed using legitimate scanning services, such as Censys and ZoomEye, to identify Internet-exposed or insufficiently segmented Siemens S7 Series PLCs. Once vulnerable systems have been identified, AI-generated scripts masquerading as legitimate monitoring tools are deployed to find exploits. For capability development, actors are testing and refining their exploitation techniques against specific PLC models to improve their ability to compromise the PLCs," the agencies said. "To prepare for operational effects, actors are leveraging read access to understand target environments, enabling preparation and positioning for future write operations to cause disruption or other operational impacts." It's currently not known who is behind the activity.

## **🔔 Top News**

* **[GitLab Flaw Comes Under Attack](https://thehackernews.com/2026/08/gitlab-cve-2026-19478-comes-under.html)**
  — A newly disclosed security flaw in GitLab came under active exploitation within days of public disclosure, according to watchTowr. The vulnerability in question is CVE-2026-19478 (CVSS score: 9.4), a case of code injection that allows an unauthenticated attacker to modify or delete publicly accessible GitLab projects and rewrite their data under certain conditions without requiring credentials, user interaction, or obscure configuration.
* **[14 Trojanized npm Packages Drop RedC2 4.0 Linux Backdoor](https://thehackernews.com/2026/08/14-trojanized-npm-packages-drop-redc2.html)**
  — A set of 14 trojanized npm packages were found to masquerade as functional calendar and streak utilities but are engineered to stealthily deliver an artificial intelligence (AI)-powered Linux implant dubbed RedC2 4.0. RedC2 4.0, marketed on cybercrime forums as a cross-platform toolkit for Windows, macOS, and Linux, offers surveillance, credential theft, payload loading, and mass-operation capabilities. The version was advertised by a threat actor named "MarlboroMan" on Hack Forums in early June 2026, describing it as a command-and-control (C2 or C&amp;C) framework "built for evasion."
* **[Zombie Card Attack Can Revive Expired Visa Cards for Contactless Payment Fraud](https://thehackernews.com/2026/08/zombie-card-attack-can-revive-expired.html)**
  — Academic researchers demonstrated a new Zombie Card attack that bypasses cryptographic checks to complete contactless payments using physically expired Visa credit cards. By taking advantage of a smartphone relay setup to alter the expiration date fed to the point-of-sale (PoS) terminal without breaking the card's cryptography, it's possible to make real in-store purchases. Raja Hasnain Anwar, the lead author, told The Hacker News that transactions succeeded at most of those banks when the team modified the Consumer Device Cardholder Verification Method (CDCVM) flag. There is no evidence the technique has been exploited in the wild.
* **[Suspected Russian Hackers Abuse Legitimate Authentication Workflows](https://thehackernews.com/2026/08/suspected-russian-hackers-abuse-google.html)**
  — Three distinct suspected Russian cyber espionage threat clusters, viz., UNC6293, UNC7005, and UNC5976, have been observed leveraging legitimate authentication flows to single out individuals working in academia, aerospace and defense, governments, and think tanks across Europe, as well as academia and think tanks within the U.S. "These clusters engage in persistent, adaptive phishing campaigns, using sophisticated social engineering tactics to compromise personal accounts across multiple platforms," Google said. UNC7005 has also been attributed to CaptiveCrunch, which targets captive Wi-Fi portals in locations such as hotels, conference centers, and airports in the U.S. and elsewhere to stealthily redirect users to attacker-controlled infrastructure to steal credentials. A new report from Lumen Black Lotus Labs has found that the threat actor likely compromised three Managed Service Providers (MSPs) to conduct the captive portal hijack via a supply chain attack.
* **[Cloudflare Workers Spectre Attack Leaks JWT](https://thehackernews.com/2026/08/cloudflare-workers-spectre-attack-leaks.html)**
  — A remote Spectre attack against Cloudflare Workers has been found to leak a JSON Web Token (JWT) from a co-located Worker in the production environment at up to 12 bits per second, 360 times the rate of a previous attack demonstrated in 2021. "Cloudflare Workers is one of the top three edge-computing solutions and handles millions of HTTP requests per second worldwide across tens of thousands of websites every day," researchers said in a study. "We demonstrate a remote Spectre attack using amplification techniques in combination with a remote timing server, which is capable of leaking 120 bit/h."
* **[Cl0p Deploys Bespoke Web Shell in PTC Windchill Attacks](https://thehackernews.com/2026/08/clop-linked-windchill-web-shell.html)**
  — A JavaServer Pages (JSP) web shell deployed following the exploitation of a critical security flaw in PTC Windchill and FlexPLM servers is specifically designed for the enterprise Product Lifecycle Management (PLM) software. Per ReliaQuest, the web shell is a fully equipped extortion platform capable of mapping sensitive vault data, decrypting every credential in the Windchill keystore, and running additional code by means of a custom Java class loader. This is not the first time the Clop gang has deployed custom web shells. The e-crime group was previously observed dropping DEWMODE and LEMURLOOT after exploiting SQL injection flaws in Accellion (CVE-2021-27101) and MOVEit Transfer (CVE-2023-34362) file transfer software, respectively. As of August 12, 2026, the ransomware gang started releasing alleged victims' full names. Over 40 organizations are said to have been targeted by the prolific e-crime group. The development continues Cl0p's trend of targeting zero-days in popular SaaS platforms for mass exploitation and extortion.
* **[Security Flaw in Unisoc](https://thehackernews.com/2026/08/unisoc-volte-video-call-exploit-chain.html)**
  — Researchers disclosed a new unpatched flaw in Unisoc T612 modem firmware that, when combined with a
  [previously disclosed](https://ssd-disclosure.com/unisoc-t612-rce/)
  remote code execution (RCE) vulnerability (also unpatched), could allow a threat to obtain elevated access to the Android kernel on affected devices. The exploit can be triggered by first delivering a malicious payload to the phone's modem via the RCE vulnerability and then placing a video call to the device, which the victim would need to answer. "A critical vulnerability has been identified in the Unisoc modem firmware that allows arbitrary code execution with kernel privileges from the modem context," SSD Secure Disclosure said. "By disabling protections on the first memory region (ID 0) of the Memory Protection Unit (MPU), an attacker can gain unrestricted read and write access to physical memory. This can ultimately lead to local privilege escalation, including the ability to modify kernel code."

## **🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first —
[CVE-2026-15748](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)
(Forminator Forms),
[CVE-2026-15826](https://thehackernews.com/2026/08/forminator-wordpress-flaw-can-enable.html)
(User Profile Builder),
[CVE-2026-73570](http://h)
(Zimbra),
[CVE-2026-32475](https://thehackernews.com/2026/08/elementor-pro-flaw-could-let.html)
(Elementor Pro),
[CVE-2026-64849](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)
(MLflow),
[CVE-2026-25895](https://thehackernews.com/2026/08/attackers-exploit-mlflow-ssrf-flaw-to.html)
(FUXA),
[CVE-2026-20030, CVE-2026-20357, CVE-2026-20358, CVE-2026-20359, CVE-2026-20231, CVE-2026-20315, CVE-2026-20317, CVE-2026-20318, CVE-2026-20319](https://thehackernews.com/2026/08/cisco-patches-nine-crosswork-and-secure.html)
(Cisco),
[CVE-2026-19478](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-2-4-released/)
(GitLab),
[CVE-2026-65346](https://support.apple.com/en-us/100100)
(Apple),
[CVE-2026-19505, CVE-2026-19506, CVE-2026-19507, CVE-2026-19508, CVE-2026-19509](https://kb.cert.org/vuls/id/874418)
(RDK Central RDK-B WebUI), CVE-2026-75874, CVE-2026-74934, CVE-2026-74935, from CVE-2026-74936 through CVE-2026-74949 (Mozilla
[Firefox](https://www.mozilla.org/en-US/security/advisories/mfsa2026-74/)
and
[Thunderbird](https://www.mozilla.org/en-US/security/advisories/mfsa2026-78/)
),
[CVE-2026-76034, CVE-2026-76036](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0826575033.html)
,
[CVE-2026-76017](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0404570826.html)
(Google Chrome),
[CVE-2026-14682, CVE-2026-12143](https://confluence.atlassian.com/security/security-bulletin-august-18-2026-1821999768.html)
(Atlassian Bamboo Data Center),
[CVE-2026-76404, CVE-2026-76389, CVE-2026-76395, CVE-2026-76310, CVE-2026-76311, CVE-2026-76312](https://advisory.splunk.com/advisories/)
(Splunk),
[CVE-2026-69106, CVE-2026-65922](https://docs.jfrog.com/releases/docs/artifactory-self-managed-releases)
(JFrog Artifactory),
[CVE-2026-6837](https://minanagehsalalma.github.io/CVE-2026-6837-zyxel-export-cgi-command-injection/)
(Zyxel),
[CVE-2026-18051](https://wpscan.com/vulnerability/dc56cdd2-419b-4a64-9d2a-29dc7e79cb6d/)
(W3 Total Cache),
[CVE-2026-63093](https://nvd.nist.gov/vuln/detail/CVE-2026-63093)
(Cursor),
[CVE-2026-40144, CVE-2026-40145](https://www.beyondtrust.com/trust-center/security-advisories/bt26-04)
(BeyondTrust Endpoint Privilege Management for Windows),
[CVE-2026-57580](https://oblique.security/blog/hacking-saml/)
(Authentik),
[CVE-2026-63182](https://oblique.security/blog/hacking-saml/)
(PHP litesaml/lightsaml),
[CVE-2026-41473, CVE-2026-41472](https://pentera.io/resources/research/pre-auth-rce-chain-cyberpanel/)
(CyberPanel),
[CVE-2026-66794](https://access.redhat.com/security/cve/cve-2026-66794)
(Multicluster Engine for Kubernetes),
[CVE-2026-69502, CVE-2026-69555, CVE-2026-65816, CVE-2026-65801, CVE-2026-65770, CVE-2026-69836, CVE-2026-24301](https://msrc.microsoft.com/update-guide/vulnerability)
(Microsoft),
[CVE-2026-15580](https://amibeingpwned.com/blog/solar-winds-part-2-avoided)
(N-Able Passportal),
[CVE-2026-59270, CVE-2026-47836, CVE-2026-47841](https://spring.io/security)
(Spring Security UnboundID LDAP server),
[CVE-2026-75501](https://kb.cert.org/vuls/id/756733)
(Calix GS7 XGS GS5239XG router),
[CVE-2026-18963](https://access.redhat.com/security/cve/cve-2026-18963)
(Keycloak), and
[GHSA-p9r8-2q67-fp86](https://github.com/NASA-AMMOS/AIT-GUI/security/advisories/GHSA-p9r8-2q67-fp86)
(AMMOS Instrument ToolkiT-GUI).

**(Update on August 28, 2026:**
"We conducted our own investigation immediately upon becoming aware of the public report and have determined through testing and analysis that existing network security controls in deployed systems prevent exploitation of the reported attack scenario," a spokesperson for Calix told The Hacker News regarding CVE-2026-75501.)

## **🎥 Cybersecurity Webinars**

* **[AI Coding Is Creating Remediation Debt. See What 300 Enterprise Leaders Found](https://thehacker.news/ai-coding-risk)
  →**
  AI coding is accelerating development, but it’s also pushing more unvetted open source into production and expanding the backlog security teams must manage. See what 300 enterprise security and engineering leaders revealed about the growing risk, and which governance approaches are actually helping teams regain control.
* **[AI Attacks Can Move in Minutes. Can Your Security Operations Keep Up?](https://thehacker.news/ai-threat-readiness)**
  → AI is compressing vulnerability discovery, exploit development, and attack chaining into much shorter windows. Learn a practical AI threat-readiness framework for improving attack-surface visibility and accelerating investigation, validation, and remediation before machine-speed threats outpace existing security operations.

## **📰 Around the Cyber World**

* **Live Stripe keys for 659 merchants leaked**
  — A dataset published on a data-trading forum on August 18, 2026, contains live Stripe API keys for 659 merchant accounts, along with roughly 35 GB of customer and payment data pulled from them. "A Stripe secret key is not a password to a dashboard," Ransomnews
  [said](https://ransomnews.com/stripe-merchant-api-keys-leak-2026/)
  . "It is full programmatic access to the account. Anyone holding one can read every customer record, create charges, issue refunds, and change where payouts are sent. The 519 accounts in that bottom row could, on the collector’s own record, both take money in and move it out."
* **CISA Releases Guidance for Improving Operational Standards**
  — The U.S. Cybersecurity and Infrastructure Security Agency (CISA) published the Logging Reference Architecture for federal agencies to establish logging, visibility, and operational standards in an Agency Logging Plan. The guidance implements a practical, risk-based, prioritized logging approach that improves agency network monitoring. "Cyber defense begins with insight. Robust logs provide the critical visibility needed to counter daily threats targeting federal systems. CISA is enhancing agency logging strategies to ensure security teams can rapidly detect and respond to cyber incidents,"
  [said](https://cisa.gov/resources-tools/resources/logging-reference-architecture)
  CISA Acting Executive Assistant Director for Cybersecurity Chris Butera. "The Logging Reference Architecture guides agencies away from fragmented practices, establishing a mature enterprise capability that maximizes the operational value of their data."
* **U.S. Court Partially Overturns Ex-Google Engineer's Conviction**
  —
  [Linwei Ding](https://thehackernews.com/2026/01/ex-google-engineer-convicted-for.html)
  , a former Google software engineer who was convicted earlier this year for allegedly stealing thousands of the company's confidential documents to build a startup in China, had part of the ruling overturned by a U.S. federal judge last week. According to
  [Reuters](https://www.reuters.com/legal/government/ex-google-engineers-conviction-stealing-ai-secrets-partially-overturned-2026-08-20/)
  , U.S. District Court Judge Vince Chhabria in San Francisco ruled there was not enough evidence that the defendant intended or knew his conduct would benefit the government of China. Ding is scheduled to be sentenced on September 1, 2026.
* **How Threat Actors Abuse ScreenConnect**
  — Threat actors are using various methods, ranging from phishing lures and SEO-poisoned balenaEtcher downloads to malvertising redirects and an already-resident SimpleHelp agent, to deploy ScreenConnect via PowerShell and msiexec. "In the one case that reached full hands-on control, the operator rotated domains, deployed multiple ScreenConnect instances disguised as Microsoft services, layered persistence across services, SafeBoot, and credential providers, and ran scripts to evict rival RMM tools before forcing a reboot," Trend Micro
  [said](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/screenconnect-abuse)
  .
* **DCRat in 2026**
  — Judicial‑themed phishing lures are being used to propagate
  [DCRat](https://thehackernews.com/2024/09/new-html-smuggling-campaign-delivers.html)
  , per Trellix. "Every stage of the attack required human interaction, from opening the phishing email to extracting the archive to executing the malicious components alongside trusted libraries by using DLL sideloading," the cybersecurity company
  [said](https://www.trellix.com/blogs/research/signed-sealed-injected-dcrat-mechanics-2026/)
  . "In its final stage, the malware employed process hollowing to inject malicious code into a trusted system process, effectively evading detection. The end payload was DCRat, granting attackers full remote access and control. This campaign is particularly notable for a legitimate, signed utility to bypass traditional security perimeters."
* **Using Apple's Find My to Track Live Location**
  — A security researcher who goes by the name Zerotistic has
  [devised](https://zerotistic.blog/posts/find-my-people-linux/)
  a way to enroll a Linux-based machine into Apple's Find My network and read live location data from it for those who have opted to share their locations with the Apple account owner.
* **WebAudio Fingerprinting on Alibaba**
  — Developer Matt Callaghan has
  [accused](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html)
  Alibaba's AliExpress of trying to track web users by playing sounds through browsers vulnerable to audio fingerprinting. The software engineer discovered the issue late last week after investigating why his Bluetooth headphones stopped playing music whenever he visited the AliExpress website. "Shortly after loading the AliExpress homepage, audio from my phone would stop playing," Callaghan said. "Closing the AliExpress tab fixes it immediately. Muting the tab/Firefox/Windows does not help, and there is no visible video, music, or other media playing on the page." Firefox
  [issued](https://x.com/firefox/status/2090589371049087177)
  a statement on X saying its anti-fingerprinting technology blocks Alibaba's tracking technique. Tom Ritter, who leads security efforts for Mozilla Firefox,
  [said](https://ritter.vg/blog-webaudio_alibaba.html)
  : "We made the WebAudio constant in Firefox 118 three years ago as part of our initial round of Fingerprinting Protection features. This eliminated most of the differences."
* **Anthropic Expands Claude Mythos 5 Access**
  — Anthropic said it's working with cybersecurity technology and services partners to integrate Claude Mythos 5 into their products and services to secure their software. "Customers on Claude Enterprise plans can now run our most capable model in Claude Security, using it to scan their codebases for security vulnerabilities and suggest patches," it
  [said](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)
  . "Our new Defender Advantage Fund (0xDAF) will provide $35 million in credits to organizations working to patch vulnerabilities in open-source projects, automate parts of the process of scanning and patching open-source software, and experiment with new security approaches."
* **Agentic Source Code Review**
  — Google
  [said](https://cloud.google.com/blog/topics/threat-intelligence/staying-ahead-of-adversarial-ai-through-agentic-source-code-review/)
  it uses what's called the Agentic Vulnerability Discovery Harness (AVDH) to "rapidly analyze code and find exploit paths during proactive reviews, penetration tests, red team operations, and incident response engagements." The development comes amid increasing adversarial misuse of AI. The tech giant said its use of AVDH over the past 10 months has led to the discovery of over 100 true-positive critical vulnerabilities, including critical flaws in Drupal (CVE-2026-13242 and CVE-2026-55803). The system outlined by Google is very similar to Microsoft's
  [MDASH](https://thehackernews.com/2026/05/microsofts-mdash-ai-system-finds-16.html)
  .

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnCynJxLV6lP5OuvQRYutvrgfK2lpDM1k0FJjfyQybtRVbNu6MI6EogDWRYtItw2RGDRlxIXBc1ez4E54O8PUxxWvtSNdq4AysHZV0Xm0x-24myrhitBMjdBSFCGtOPqrQ8bii8JiP7XPvbtDN-OWBX2fgMMjv3CHmeV00o0xNc4BLgSVN8UcvTc2pu5q1/s1600/google.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgnCynJxLV6lP5OuvQRYutvrgfK2lpDM1k0FJjfyQybtRVbNu6MI6EogDWRYtItw2RGDRlxIXBc1ez4E54O8PUxxWvtSNdq4AysHZV0Xm0x-24myrhitBMjdBSFCGtOPqrQ8bii8JiP7XPvbtDN-OWBX2fgMMjv3CHmeV00o0xNc4BLgSVN8UcvTc2pu5q1/s1600/google.png)

* **768 Leaked Corporate AWS Keys Hold Full Admin Rights**
  — Truffle Security's scan has
  [verified](https://trufflesecurity.com/blog/leaked-corporate-aws-keys-held-full-admin-rights)
  64,024 unique AWS key pairs across 431,875 public findings, including git history, Hugging Face datasets, Docker images, package registries, CI logs. These keys surfaced publicly between August 2022 and August 2026. Of these pairs, 10,616 came with complete credentials. According to Truffle Security: ""88% still authenticate. 768 of the live ones belong to a company and carry full control of its AWS account: 526 root keys plus 242 IAM users holding AdministratorAccess. The median live leaked key is five years old and has never been rotated."

## **Conclusion**

This week’s useful reminder: attackers rarely need everything to fail. One exposed service, one trusted shortcut, or one overlooked dependency can be enough to get started.

So the better question is not “what’s the next big threat?” It’s “what are we still assuming is safe?” That usually finds the problem sooner.