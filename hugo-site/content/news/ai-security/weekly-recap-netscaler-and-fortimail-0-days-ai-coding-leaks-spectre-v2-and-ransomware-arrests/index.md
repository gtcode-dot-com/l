---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-07T04:41:28.720020+00:00'
exported_at: '2026-10-07T04:41:31.019061+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
structured_data:
  about: []
  author: ''
  description: Catch up on this week’s biggest cyber threats, including exploited
    zero-days, AI-related data leaks, Spectre attacks, phishing tricks, and ransomware
  headline: '⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre
    v2 and Ransomware Arrests'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/weekly-recap-netscaler-and-fortimail-0.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '⚡ Weekly Recap: NetScaler and FortiMail 0-Days, AI Coding Leaks, Spectre v2
  and Ransomware Arrests'
updated_at: '2026-10-07T04:41:28.720020+00:00'
url_hash: acb91d74c1ac878c143c97a83cc26a38bd0a1cfd
---

A blank field. A public repo. One reply to an email. A box left exposed. None of this sounds dramatic, which is partly the problem. This week’s threats keep finding leverage in small things that were easy to overlook.

There are actively exploited bugs in the mix, cleaner intrusion paths, smarter automation, and a long patch list waiting behind them. Some attacks are getting more capable. Others are still getting in because the basics gave way first.

Here’s what mattered this week.

## **⚡ Threat of the Week**

**[Citrix Warns of Newly Exploited NetScaler ADC and Gateway Flaw](https://thehackernews.com/2026/10/new-netscaler-zero-day-exploited-in.html)**
— Citrix released security updates for a high-severity security flaw in NetScaler ADC and NetScaler Gateway that has been exploited as part of targeted zero-day attacks. The vulnerability, tracked as CVE-2026-88779, carries a CVSS score of 8.7 out of 10.0. "CVE-2026-88779 is a memory overflow vulnerability in Citrix NetScaler ADC and Citrix NetScaler Gateway that can lead to denial-of-service under specific deployment conditions," Citrix said. "The issue affects customer-managed NetScaler deployments running affected supported versions when the required preconditions are met." Successful exploitation requires NetScaler ADC or NetScaler Gateway to be configured either as a SAML service provider (SP) or SAML identity provider(IdP).

## **🔔 Top News**

* **[Critical FortiMail Zero-Day Flaw Exploited in Attacks](https://thehackernews.com/2026/10/critical-fortimail-zero-day-flaw.html)**
  — The U.S. Cybersecurity and Infrastructure Security Agency (CISA) warned of active exploitation of a critical security flaw impacting Fortinet FortiMail. The flaw, CVE-2026-104286 (CVSS score: 9.8), allows unauthenticated attackers to write arbitrary files on the underlying system. According to Fortinet, the vulnerability "may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests."
* **[Two ShinyHunters Members Arrested](https://thehackernews.com/2026/10/shinyhunters-suspect-rey-reportedly.html)**
  — Law enforcement agencies have arrested two members associated with the ShinyHunters digital extortion group. One of them is a 24-year-old Amsterdam man, who is believed to be Pepijn van der Stap, while the second individual is Saif ‌al-Din Khader, who is said to have been detained by Jordanian authorities last week. ShinyHunters has drawn attention in recent weeks for hijacking the darknet website of Cl0p and its hack of the FBI's "apply.fbijobs[.]gov" portal.
* **[Authorities Arrest 16-Year-Old Mastermind Behind KillSec](https://thehackernews.com/2026/10/police-arrest-16-year-old-suspected-of.html)**
  — Police in Spain apprehended a 16-year-old who is suspected to be the leader of the
  [KillSec](https://www.halcyon.ai/threat-group/killsec)
  (aka Kill Security Ransomware Group) ransomware operation. According to Europol, authorities took control of KillSec's leak site on September 30, 2026, securing no less than 110 terabytes of data. As part of Operation KillSwitch, a total of three suspects were provisionally arrested and eight properties searched in Greece, Romania, Spain, and the U.K. One of the group’s accused members, Fouad Eltibrizi, was
  [arrested](https://www.justice.gov/usao-pr/pr/dutch-national-indicted-and-arrested-unauthorized-computer-access-conspiracy)
  in the U.K. and is awaiting extradition to the U.S. Since emerging in 2024, the group is estimated to have launched around 1,000 attacks, at least half of which were successful. "The group exploited software vulnerabilities and poorly secured access points, particularly to cloud storage, to gain access to organizations' systems," Europol
  [said](https://www.europol.europa.eu/media-press/newsroom/news/teenager-suspected-of-leading-killsec-ransomware-group-law-enforcement-seizes-servers-and-leak-site)
  . "Its members then copied sensitive internal data to infrastructure under their control. Victims were named on the group's dark web leak site and threatened with publication of their data unless paid." Per Group-IB, which identified 274 publicly claimed victims, out of which most were U.S., Indian, and Brazilian organizations. "The group also sold stolen data outright, with asking prices ranging from USD 5,000 for a single company's records to USD 500,000 for the data it claimed to have taken from the global insurer, making KillSec as much a data broker as a ransomware operator," Group-IB
  [said](https://www.group-ib.com/media-center/press-releases/operation-killswitch-killsec/)
  .
* **[New Spectre v2 Variant Leaks Linux Root Password Hash in Minutes](https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html)**
  — A new Spectre v2 attack variant called Branch Target Reuse (BTR) can recover root password hashes from Intel computers running Linux in just a few minutes. The attack exploits stale information in a processor's branch predictor after a just-in-time (JIT) engine reuses memory for new code. By tampering with this information, an attacker can trick the processor into temporarily executing wrong instructions and potentially expose sensitive data. "We evaluated the end-to-end exploit on both Raptor Cove and Lion Cove, and leaked the password within 3 and 5 minutes on average, respectively," researchers claimed. "Indirect branch prediction is inherent to modern CPUs, and BTR exploits the desynchronization between the branch predictor and the actual state of the code. No current CPU has a mechanism to keep the two in sync, so until vendors add one, your CPU is vulnerable."
* **[Star Blizzard Uses Fake Invites to Deploy CosmicPulse](https://thehackernews.com/2026/09/russias-star-blizzard-targets-100.html)**
  — The Russian state-sponsored threat actor known as Star Blizzard has employed a new malware delivery technique called RedFlick in attacks targeting Ukrainian individuals and institutions as well as international non-government organizations (NGOs), Western think tanks, governments, and other organizations associated with international policy. The end goal is to deploy a custom backdoor called CosmicPulse by setting up scheduled tasks using RedFlick through phishing emails masquerading as invitations. Once a victim responds to an initial phishing email, Star Blizzard typically sends a follow-up containing a password-protected archive that triggers the RedFlick chain. "This technique is a notable departure from the actor’s previous use of ClickFix-based infection chains which required victims to complete multiple actions before CosmicPulse could be installed," Microsoft said. "By contrast, the RedFlick infection flow only requires a single user interaction, reducing friction in the compromise process."
* **[NeedyMantis Malware Enables Persistent Network Access](https://thehackernews.com/2026/09/hackers-use-needymantis-to-maintain.html)**
  — A modular post-compromise malware family called NeedyMantis is being used by threat actors to maintain long-term stealth access and support post-compromise operations. Distributed by a two-stage loader and launched via DLL sideloading, the malware has been observed in a limited number of targeted operations affecting telecommunications organizations, universities, medical nonprofits, intergovernmental organizations, and government contractors. The activity aligns with operations that are associated with threat actors operating from China. The malware operation has been active since at least October 2025. "While NeedyMantis employs techniques commonly used by modern malware, its architecture combines multiple loaders, custom encrypted file archives, a custom executable file format, and modular components that enable operators to evade analysis and extend functionality through additional modules," Microsoft said. At least one threat actor has been linked to its use: Storm-3069, which is Microsoft's designation for the DAEMON Tools supply chain attack that took place in May 2026.
* **[RatHat Android Malware Console Uses Gemini to Identify Higher-Value Victims](https://thehackernews.com/2026/09/rathat-android-malware-console-uses.html)**
  — The Android malware known as RatHat has been observed using Google Gemini to estimate each victim's bank balance and sorts the device into high-value and mid-value groups. "Gemini is used on both sides of the operation: the malware asks an LLM where to tap when its automation fails on an unfamiliar phone, and the panel uses one to estimate victims' bank balances from their SMS," Cleafy said. Over the course of the operation, the threat actors behind RatHat changed its command-and-control (C2) panel entirely, moving from ackCat to Panda Workshop. "The panel works as a complete malware factory: it builds, signs, and publishes new samples from the console, rebuilds them on a schedule to evade hash-based detection, without the operator touching the hosting infrastructure," Cleafy added. "Account caps and role-gated sections exist to constrain the panel's own users, and pivoting on its frontend artifacts resolves the three generations to nearly 100 separate deployments since April 2026."
* **[AI Coding Agents Leaked 13K Internal Company Screenshots](https://thehackernews.com/2026/09/ai-coding-agents-exposed-13000-internal.html)**
  — A new report from Glow Labs found that AI coding agents posted more than 13,000 sensitive screenshots of corporate software projects from 343 companies to public GitHub repositories. The activity has been codenamed PixelLeak. About a third of the exposures came from developers who were using gitshot. "Each case investigated during our 'PixelLeak' research started with a developer asking an agent to prove that a visual change worked," researchers said. "The software was changed, for example with a fix to the user interface layout, and the reviewers needed to see the before and after. The agents figured out that they could make the image available to the human reviewer by hosting it in an adjacent public repo. They just didn't consider the security implications." These incidents show that AI creates new security risks even without having to facilitate cyber attacks.

## **‎️‍🔥 Trending CVEs**

Bugs drop weekly, and the gap between a patch and an exploit is shrinking fast. These are the heavy hitters for the week: high-severity, widely used, or already being poked at in the wild.

Check the list, patch what you have, and hit the ones marked urgent first —
[CVE-2026-88779](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697174)
(Citrix NetScaler ADC and NetScaler Gateway),
[CVE-2026-96419, CVE-2026-96421, CVE-2026-95391, CVE-2026-95389](https://www.wireshark.org/docs/relnotes/wireshark-4.6.9.html)
(Wireshark),
[CVE-2026-86857, CVE-2026-86858, CVE-2026-13016, CVE-2026-86859, CVE-2026-86860](https://support.servicenow.com/kb?id=kb_article_view&amp;sysparm_article=KB3159623)
(ServiceNow),
[CVE-2026-93485 aka Comment2Shell](https://github.com/DeathShotXD/Comment2Shell)
(WordPress),
[CVE-2026-76708, CVE-2026-76709, CVE-2026-76710](https://support.hpe.com/hpesc/public/docDisplay?docId=hpesbnw05137en_us&amp;docLocale=en_US)
(HPE Networking Analytics and Location Engine),
[CVE-2026-89078, CVE-2026-93577](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-1-released/)
(GitLab),
[CVE-2026-96512](https://bugzilla.redhat.com/show_bug.cgi?id=2539327)
(
[Sudo](https://github.com/sudo-project/sudo/commit/1820a349687522f51023d1ae5925125f59679a8c)
),
[CVE-2026-87022, CVE-2026-86350, CVE-2026-78437, CVE-2026-78383, CVE-2026-77791, CVE-2026-79677, CVE-2026-76183, CVE-2026-75973, CVE-2026-86248, CVE-2026-73581](https://tomcat.apache.org/security-11.html#Fixed_in_Apache_Tomcat_11.0.26)
(Apache Tomcat),
[CVE-2026-18163, CVE-2026-18162, CVE-2026-18169 CVE-2026-18177, CVE-2026-18132, CVE-2026-18872, CVE-2026-17635, CVE-2026-17645, CVE-2026-18137](https://www.ibm.com/support/pages/node/7288641)
(IBM Financial Transaction Manager),
[CVE-2026-94384](https://aws.amazon.com/security/security-bulletins/2026-115-aws/)
(AWS Connect Salesforce Lambda),
[CVE-2026-65127, CVE-2026-65113, CVE-2026-65128, CVE-2026-65114, CVE-2026-65121, CVE-2026-65130](https://nvidia.custhelp.com/app/answers/detail/a_id/5879)
(NVIDIA),
[CVE-2026-74849](https://www.manageengine.com/products/self-service-password/advisory/CVE-2026-74849.html)
(ManageEngine ADSelfService Plus),
[CVE-2026-75939](https://access.redhat.com/security/cve/cve-2026-75939)
(Red Hat OpenShift),
[GHSA-632h-h47v-g4x4](https://securitylabs.datadoghq.com/articles/opencode-upgrade-remote-code-execution/)
(OpenCode),
[CVE-2026-91765](https://github.com/php/php-src/security/advisories/GHSA-rgrp-mwpx-f6rm)
(PHP),
[CVE-2026-96760](https://kb.cert.org/vuls/id/762428)
(Authlib),
[CVE-2026-42542, CVE-2026-44639](https://ridgesecurity.ai/blog/one-packet-can-take-down-the-database-behind-industrial-operations-ridge-security-discovers-cve-2026-42542/)
(TDengine),
[CVE-2026-86553, CVE-2026-86555, CVE-2026-86552, CVE-2026-86554](https://minanagehsalalma.github.io/zte-smartlife-app-pwned/)
(ZTE SmartLife),
[CVE-2026-101891, CVE-2026-87969, CVE-2026-86102, CVE-2026-86131](https://psirt.watchguard.com)
(WatchGuard),
[GHSA-cpc9-c4h3-2jwx](https://github.com/geoserver/geoserver/security/advisories/GHSA-cpc9-c4h3-2jwx)
(geoserver/geoserver-cloud),
[CVE-2026-93302, CVE-2026-89102](https://github.com/wolfSSL/wolfssl/releases/tag/v5.9.4-stable)
(WolfSSL),
[CVE-2026-84782](https://openssl-library.org/news/vulnerabilities/index.html)
(OpenSSL),
[CVE-2026-12530, CVE-2026-16796](https://www.beyondtrust.com/blog/entry/amazon-bedrock-agentcore-python-sdk-rce-cves)
(Amazon Bedrock AgentCore Python SDK),
[CVE-2026-76504](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU)
(Cisco Catalyst SD-WAN Manager),
[CVE-2026-84411](https://www.cisa.gov/news-events/ics-advisories/icsa-26-272-06)
(MikroTik RouterOS),
[CVE-2026-19743, CVE-2026-92368, CVE-2026-92369, CVE-2026-92370, CVE-2026-92371](https://www.teamviewer.com/en-in/resources/trust-center/security-bulletins/tv-2026-1010/)
,
[CVE-2026-19042](https://www.teamviewer.com/en-in/resources/trust-center/security-bulletins/tv-2026-1009/)
,
[CVE-2026-16444](https://www.teamviewer.com/en-in/resources/trust-center/security-bulletins/tv-2026-1008/)
,
[CVE-2026-12703](https://www.teamviewer.com/en-in/resources/trust-center/security-bulletins/tv-2026-1007/)
(TeamViewer),
[CVE-2026-102331](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01807488085.html)
(Google Chrome),
[from CVE-2026-100756 through CVE-2026-100793](https://www.mozilla.org/en-US/security/advisories/mfsa2026-97/)
(Mozilla Firefox),
[CVE-2026-54154, CVE-2026-102147, CVE-2026-102149, CVE-2026-102102, CVE-2026-102103, CVE-2026-102104, CVE-2026-102105, CVE-2026-102106, CVE-2026-102115, CVE-2026-102095, CVE-2026-85066, CVE-2026-85065](https://github.com/kiteworks/security-advisories/security)
(Kiteworks),
[CVE-2026-102489, CVE-2026-102490](https://csirt.divd.nl/cases/DIVD-2026-00015/)
(Zammad),
[CVE-2026-63292, CVE-2026-42356, CVE-2026-42528](https://httpd.apache.org/security/vulnerabilities_24.html)
(Apache HTTP Server),
[CVE-2026-101898, CVE-2026-101901, CVE-2026-101909, CVE-2026-101906, CVE-2026-101903, CVE-2026-101907, CVE-2026-101905](https://github.com/axios/axios/security)
, (Axios),
[CVE-2026-72018](https://xbow.com/blog/no-time-to-pwn-cve-2026-72018)
(Linux kernel),
[CVE-2026-101169](https://advisories.octopus.com/post/2026/sa2026-10/)
(Octopus Server),
[CVE-2026-94545](https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j)
(Next.js),
[CVE-2026-73857, CVE-2026-73856](https://github.com/owasp-modsecurity/ModSecurity/security/advisories)
(ModSecurity),
[CVE-2026-12855](https://kb.cert.org/vuls/id/553437)
(InsydeH2O IHISI SMM),
[MTLVULN-1694](https://www.mitel.com/support/security-advisories/mitel-product-security-advisory-misa-2026-0006)
(Mitel MiCollab),
[CVE-2026-81963](https://www.coresecurity.com/blog/cve-2026-81963-public-cbs-session-system-code-execution)
(Microsoft Windows),
[CVE-2026-90970](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-19-4-1-released/)
,
[CVE-2026-1868](https://docs.gitlab.com/releases/patches/other-patches/patch-release-gitlab-ai-gateway-18-8-1-released/)
(GitLab AI Gateway),
[CVE-2026-79898, CVE-2026-12627, CVE-2026-79901](https://www.fortra.com/security/advisories/product-security)
(Fortra BoKS),
[CVE-2026-93698](https://support.cpanel.net/hc/en-us/articles/43845931719447-Security-CVE-2026-93698-Vulnerability-in-Multilang-Adminbin-September-29-2026)
,
[CVE-2026-93029](https://support.cpanel.net/hc/en-us/articles/43845929235351-Security-CVE-2026-93029-Stored-XSS-in-WHM-s-Manage-SSL-Hosts-Interface-September-29-2026)
,
[CVE-2026-93697](https://support.cpanel.net/hc/en-us/articles/43845930445207-Security-CVE-2026-93697-Stored-XSS-in-WHM-s-Account-Modification-Interfaces-September-29-2026)
(cPanel and WHM),
[CVE-2026-103922](https://github.com/ionic-team/capacitor/security/advisories/GHSA-rvm3-566m-v7fv)
(Capacitor),
[CVE-2026-13181, CVE-2026-13182, CVE-2026-13183, CVE-2026-13184](https://tantosec.com/blog/2026/09/telerik-padding-oracle-to-shell/)
(Telerik UI for ASP.NET AJAX),
[CVE-2026-84732, CVE-2026-84256, CVE-2026-84226, CVE-2026-82312, CVE-2026-78043, CVE-2026-81738](https://community.openvpn.net/Security%20Announcements/)
(OpenVPN),
[CVE-2026-75754](https://www.asus.com/security-advisory)
(ASUS Control Center Enterprise),
[CVE-2026-96659](https://access.redhat.com/security/cve/cve-2026-96659)
(Foreman),
[CVE-2026-61500](https://horizon3.ai/attack-research/disclosures/anthropic-mythos-rejetto-hfs-rce/)
(Rejetto HFS),
[CVE-2026-18167, CVE-2026-18330](https://www.tp-link.com/us/support/faq/5279/)
(TP-Link Archer AX55 v4),
[CVE-2026-63688, CVE-2026-63692, CVE-2026-67269, CVE-2026-54472, CVE-2026-61421, and CVE-2026-67273](https://www.dell.com/support/kbdoc/en-us/000515771/dsa-2026-448-security-update-for-dell-container-storage-modules-multiple-vulnerabilities)
(Dell Container Storage Modules).

## **🎥 Cybersecurity Webinars**

* **[How to Control AI Agents Before Access Sprawl Takes Over](https://thehacker.news/ai-agents-governance)**
  → AI agents are rapidly gaining access to sensitive systems, data, and workflows—but most security programs were never designed to govern non-human identities at this scale. This webinar breaks down how to discover AI agents, control their permissions, prevent excessive access, and build a governance model that keeps agent adoption from turning into the next major identity security problem.
* **[AI Attacks Move at Machine Speed. Can Your Identity Security Keep Up?](https://thehacker.news/runtime-identity-security)**
  → AI-powered attacks can now move from reconnaissance to privilege escalation faster than traditional security teams can investigate and respond. This webinar explains why identity is becoming the critical real-time control layer—and how runtime identity security can help organizations detect risky access, enforce decisions across cloud, SaaS, on-prem, and AI environments, and stop machine-speed attacks before they turn into breaches.

## **📰 Around the Cyber World**

* **Google Halts OSS VRP Submissions**
  — As of October 1, 2026, Google is
  [no longer accepting](https://x.com/GoogleVRP/status/2105689195180179605)
  OSS VRP product vulnerability submissions due to a "significant rise in automated submissions, the vast majority of which are not valid." The tech giant
  [added](https://bughunters.google.com/about/rules/open-source/google-open-source-software-vulnerability-reward-program-rules)
  : "For some Google Cloud repos impacting Google Cloud products, we may still accept reports covering product vulnerabilities through the Cloud VRP. We will continue to reformat and work on this aspect of the OSS VRP and commit to giving an update in Q1 2027."
* **Microsoft's X Account Briefly Hijacked**
  — Unknown attackers hijacked the official Microsoft account on X, which has over 13 million followers, in what appeared to be a pump-and-dump scheme promoting a crypto token. "We have confirmed unauthorized access to our account on X, including posts that did not come from Microsoft," a Microsoft spokesperson
  [told](https://www.theverge.com/news/1003892/microsoft-x-twitter-account-clippy)
  The Verge. "The account has been secured, and the unauthorized posts have been removed, and we are continuing to investigate the circumstances."
* **TIKTOUK, a WordPress Credential Collection Toolkit**
  — A new toolkit called TIKTOUK "brings together WordPress probing, collection of exposed configuration data, recovery of encrypted email credentials, and JavaScript secret scanning," LevelBlue
  [said](https://www.levelblue.com/blogs/spiderlabs-blog/tiktouk-tracing-a-wordpress-credential-collection-toolkit)
  . TIKTOUK features Python components and a Go-based Linux crawler that probes WordPress pages and REST batch routes, collects configuration and option values, and retrieves referenced JavaScript files, scans their contents, and reports matching secret patterns.
* **Google Details PageBreak**
  — Google has detailed an internal AI agent called PageBreak that aims to autonomously scale vulnerability discovery while minimizing manual work arising from hallucinated bug reports. "Rather than simply hypothesizing bugs based on code patterns, the system closes the loop by verifying potential flaws against running environments," Google
  [said](https://blog.google/security/agentic-hacks-real-proofs-inside-googles-pagebreak-project/)
  . "This approach results in a near-zero false positive rate, ensuring that we avoid overloading product teams with unverified vulnerability reports." Page has uncovered over 500 Cross-Site Scripting (XSS) vulnerabilities across Google first-party web applications.
* **Milk Dragon Phishing Kit Detailed**
  — Group-IB has shed light on an adversary-in-the-middle (AiTM) phishing kit called Milk Dragon (aka NaiLong) that has been active since October 2025. "Unlike conventional phishing tactics that rely on fear and urgency, Milk Dragon lures victims with big discounts on consumer goods distributed via Facebook and TikTok marketplace advertisements," Group-IB
  [said](https://www.group-ib.com/blog/milk-dragon-nailong-phishing-kit/)
  . "Phishing pages impersonate brands across multiple industries, including Retail &amp; Supermarket chains. Well-known brand names such as LEGO, Calvin Klein, Aeon Malaysia, and many others are exploited and used as lures." The attack is designed to steal financial information from victims. Actively sold on Telegram, Milk Dragon has claimed victims spanning 66 countries, with 258 phishing pages identified to date.
* **Iranian Hacker Extradited to the U.S.**
  — An Iranian hacker
  [accused](https://www.justice.gov/opa/pr/17-iranians-charged-conducting-massive-cyber-theft-campaign-behalf-islamic-revolutionary)
  of being behind a
  [cyber espionage campaign](https://thehackernews.com/2026/08/threatsday-gogs-100-rce-n8n-workflow-to.html#10-million-reward)
  targeting hundreds of universities, federal and state government agencies, private sector companies, and non-governmental organizations has been
  [extradited](https://edition.cnn.com/2026/10/01/politics/iranian-accused-hacking-scheme-extradited)
  to the U.S. Amir Barati, 40, is expected to face wire and computer fraud charges in the US Southern District of New York. The High Court in Podgorica
  [approved](https://www.iranintl.com/en/202609227447)
  his extradition last month.
* **New Variant of NodeStealer Emerges**
  — Netskope Threat Labs said it detected a new variant of
  [NodeStealer](https://thehackernews.com/2023/11/nodestealer-malware-hijacking-facebook.html)
  packing major updates that turn it into a full-blown spyware. The new features were likely written with AI assistance. "The latest Python NodeStealer variant incorporates new spyware features, including keylogging, clipboard monitoring, and screenshot capture," Netskope
  [said](https://www.netskope.com/blog/python-nodestealer-ai-assisted-to-full-spyware)
  . "In addition, it expands its theft targets to include Wi-Fi passwords, the victim’s Pictures folder, and two additional web browsers. Earlier NodeStealer variants queried only two Facebook Graph API endpoints. The latest variant queries more than 20 endpoints to construct a comprehensive dossier on the individual managing the account."
* **Bypassing Microsoft's RejectDirectSend**
  — ReliaQuest said an empty Simple Mail Transfer Protocol (SMTP) envelope sender can bypass RejectDirectSend, which is designed to block unauthenticated
  [Direct Send mail](https://thehackernews.com/2025/07/hackers-using-pdfs-to-impersonate.html)
  . "An external sender can omit the envelope domain while retaining an internal-looking address, making phishing messages more likely to be trusted. The message still carries an internal-looking address, increasing the likelihood that spearphishing reaches the recipient," ReliaQuest
  [said](https://reliaquest.com/blog/threat-spotlight-one-blank-field-bypasses-direct-send-control/)
  . "The technique requires only one empty field – no credentials, no registered lookalike domain, and no dedicated sending infrastructure – so organizations should expect continued use." The cybersecurity company said it observed attackers repeatedly using self-addressed messages and familiar business lures to target leadership and business-facing users.
* **Attackers Exploit PaperCut Flaws to Deliver AdaptixC2**
  — In late August 2026, threat actors exploited
  [CVE-2026-82078 and CVE-2026-81578](https://thehackernews.com/2026/09/papercut-replaces-emergency-patches.html)
  , two PaperCut MF vulnerabilities, as zero-days to load an in-memory Java loader, which in turn deployed a web shell. The web shell was then used to deploy a trojanized Microsoft Copilot binary carrying an AdaptixC2 implant. "AdaptixC2 is an open-source and highly modular post-compromise framework that provides a broad set of capabilities, including remote shell access, file management, reverse proxying, and modules for Active Directory attacks, credential harvesting, lateral movement, and more," eSentire
  [said](https://www.esentire.com/blog/papercut-mf-zero-day-intrusion-java-loader-web-shell-and-adaptixc2-via-cve-2026-82078-and-cve-2026-81578)
  . "In this intrusion, threat actors used the lateral movement module to steal a token from a process running under a domain-privileged service account and move laterally to a domain controller." Upon gaining access to the domain controller, the threat actors dumped credentials to obtain the service account's NTLM hash and enabled Windows Restricted Admin mode. Ultimately, the attackers dumped the domain's Active Directory NTDS.dit database in an attempt to collect password hashes for all domain accounts.
* **Anthropic Says GLM-5.3 Can Build Cyber Exploits**
  — Anthropic
  [revealed](https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities)
  that Zhipu AI's (aka Z.ai) GLM-5.3 model can autonomously build end-to-end cyber exploits, like Claude Mythos Preview, and that it has been released without "meaningful safeguards to limit misuse." The AI company said attackers can bypass the open-weight model's safeguards between 64% and 100% of the time with simple techniques, adding that these lax safeguards significantly increase the cyber capabilities available to malicious actors. "At the same time, these capabilities can also benefit defenders working to secure their systems," it added. "The funniest part is how Anthropic admitted self-reflectively that the lack of guardrails may actually be benefiting the defenders working to secure their systems," Evilginx creator Kuba Gretzky
  [said](https://x.com/mrgretzky/status/2105255947547345117)
  in an X post. "Something they never wanted to allow, because of possible misuse."

## **Conclusion**

This week was a useful reminder that attackers do not need one perfect path. A fresh exploit, an exposed secret, a weak mail control, or one careless workflow can all get them moving.

Patch what is exposed, review what is trusted by default, and keep an eye on the simple paths. The clever stuff matters, but plenty of trouble still starts with something ordinary being left open.