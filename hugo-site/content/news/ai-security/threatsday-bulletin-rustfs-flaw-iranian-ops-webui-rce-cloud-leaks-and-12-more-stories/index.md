---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-08T21:44:02.145489+00:00'
exported_at: '2026-01-08T21:44:05.329307+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html
structured_data:
  about: []
  author: ''
  description: Weekly cybersecurity roundup covering exploited vulnerabilities, malware
    campaigns, legal actions, and nation-state attacks across cloud, AI, and infr
  headline: 'ThreatsDay Bulletin: RustFS Flaw, Iranian Ops, WebUI RCE, Cloud Leaks,
    and 12 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/threatsday-bulletin-rustfs-flaw-iranian.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: RustFS Flaw, Iranian Ops, WebUI RCE, Cloud Leaks, and
  12 More Stories'
updated_at: '2026-01-08T21:44:02.145489+00:00'
url_hash: a689747631a28c1cc9e14ff904ab5ec0f5836a7b
---

**

Jan 08, 2026
**

Ravie Lakshmanan

Cybersecurity / Hacking News

The internet never stays quiet. Every week, new hacks, scams, and security problems show up somewhere.

This week's stories show how fast attackers change their tricks, how small mistakes turn into big risks, and how the same old tools keep finding new ways to break in.

Read on to catch up before the next wave hits.

1. Honeypot Traps Hackers

   Cybersecurity company Resecurity revealed that it deliberately lured threat actors who claimed to be associated with Scattered LAPSUS$ Hunters (
   [SLH](https://thehackernews.com/2025/11/a-cybercrime-merger-like-no-other.html)
   ) into a trap, after the group claimed on Telegram that it had hacked the company and stolen internal and client data. The company said it set up a honeytrap account populated with fake data designed to resemble real-world business data and planted a fake account on an underground marketplace for compromised credentials after it uncovered a threat actor attempting to conduct malicious activity targeting its resources in November 2025 by probing various publicly facing services and applications. The threat actor is also said to have targeted one of its employees who had no sensitive data or privileged access. "This led to a successful login by the threat actor to one of the emulated applications containing synthetic data," it
   [said](https://www.resecurity.com/blog/article/synthetic-data-a-new-frontier-for-cyber-deception-and-honeypots)
   . "While the successful login could have enabled the actor to gain unauthorized access and commit a crime, it also provided us with strong proof of their activity. Between December 12 and December 24, the threat actor made over 188,000 requests attempting to dump synthetic data." As of January 4, 2025, the group removed the post announcing the hack from their Telegram channel. Resecurity said the exercise also allowed them to identify the threat actor and link one of their active Gmail accounts to a U.S.-based phone number and a Yahoo account. Regardless of the setback, new findings from CYFIRMA indicate that the loose-knit collective has resurfaced with scaled-up recruitment activity, seeking initial access brokers, insider collaborators, and corporate credentials. "Chatroom discussions repeatedly reference legacy threat brands such as LizardSquad, though these mentions remain unverified and are likely part of an intimidation or reputation-inflation strategy rather than proof of a formal alliance," it
   [said](https://www.cyfirma.com/research/resurgence-of-scattered-lapsus-hunters/)
   .
2. Crypto Miner via GeoServer

   Threat actors are exploiting a known flaw in GeoServer,
   [CVE-2024-36401](https://thehackernews.com/2025/12/cisa-flags-actively-exploited-geoserver.html)
   , to distribute an XMRig cryptocurrency miner by means of PowerShell commands. "Additionally, the same threat actor is also distributing a coin miner to WegLogic servers," AhnLab
   [said](https://asec.ahnlab.com/en/91724/)
   . "It appears that they are installing CoinMiner when they scan the systems exposed to the outside world and find vulnerable services." Two other threat actors have also benefited from abusing the flaw to deliver the miner, AnyDesk for remote access, and a custom-made downloader malware dubbed "systemd" from an external server whose exact function remains unknown. "Threat actors are targeting environments where GeoServer is installed and are installing various coin miners," the company said. "The threat actor can then use NetCat, which is installed together with the coin miner, to install other malware or steal information from the system."
3. KEV Catalog Expansion

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA)
   [added](https://cyble.com/blog/cisa-kev-2025-exploited-vulnerabilities-growth/)
   245 vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog in 2025, as the database grew to 1,484 software and hardware flaws at high risk of cyber attacks – an increase of about 20% from the previous year. In comparison, 187 vulnerabilities were added in 2023 and 185 in 2024. Of the 245 flaws, 24 were exploited by ransomware groups. Microsoft, Apple, Cisco, Fortinet, Google Chromium, Ivanti, Linux Kernel, Citrix, D-Link, Oracle, and SonicWall accounted for 105 of the total vulnerabilities added to the catalog. According to Cyble, the oldest vulnerability added to the KEV catalog in 2025 was CVE-2007-0671, a Microsoft Office Excel Remote Code Execution vulnerability. The oldest vulnerability in the catalog is CVE-2002-0367, a privilege escalation vulnerability in the Windows NT and Windows 2000 "smss.exe" debugging subsystem that has been known to be used in ransomware attacks.
4. AI Logs Dispute Deepens

   OpenAI has been
   [ordered](https://news.bloomberglaw.com/ip-law/openai-must-turn-over-20-million-chatgpt-logs-judge-affirms)
   to turn over 20 million anonymized ChatGPT logs in a consolidated AI copyright case in the U.S. after it failed to convince a federal judge to dismiss a magistrate judge's order, the company said insufficiently weighed privacy concerns. The high-profile lawsuit, which has major news publishers like the New York Times and Chicago Tribune as plaintiffs, is centred around the core argument that the data that powers ChatGPT has included millions of copyrighted works from the news organizations without consent or payment. OpenAI has
   [insisted](https://openai.com/new-york-times/)
   that AI training is fair use, adding "the data we are making accessible to comply with this order has undergone a de-identification process intended to remove or mask PII and other private information, and is being provided under tight access controls designed to prevent the Times from copying and printing data that isn't directly relevant to this case." The news plaintiffs have also alleged that OpenAI destroyed "relevant output log data" by failing to temporarily cease its deletion practices as soon as litigation started in an apparent effort to dodge copyright claims.
5. Taiwan Faces Surge Attacks

   The National Security Bureau in Taiwan said that China's attacks on the country's energy sector increased tenfold in 2025 compared to the previous year. Attackers targeted critical infrastructure in nine key sectors, and the total number of cyber incidents linked to China grew by 6%. The NSB recorded a total of 960,620,609 cyber intrusion attempts targeting Taiwan's critical infrastructure, allegedly coming from China's cyber army in 2025. "On average, China's cyber army launched 2.63 million intrusion attempts per day targeting Taiwan's CI across nine primary sectors, namely administration and agencies, energy, communications and transmission, transportation, emergency rescue and hospitals, water resources, finance, science parks and industrial parks, as well as food," the NSB
   [said](https://www.nsb.gov.tw/en/#/%E5%85%AC%E5%91%8A%E8%B3%87%E8%A8%8A/%E6%96%B0%E8%81%9E%E7%A8%BF%E6%9A%A8%E6%96%B0%E8%81%9E%E5%8F%83%E8%80%83%E8%B3%87%E6%96%99/2026-01-04/Analysis%20on%20China's%20Cyber%20Threats%20to%20Taiwan's%20Critical%20Infrastructure%20in%202025)
   . The energy and emergency rescue/hospitals sectors experienced the most significant year-on-year surge in cyber attacks from Chinese threat actors. The attacks have been attributed to five Chinese hacking groups, namely BlackTech (Canary Typhoon, Circuit Panda, and Earth Hundu), Flax Typhoon (aka Ethereal Panda and Storm-0919), HoneyMyte (aka Bronze President, Mustang Panda, and Twill Typhoon), APT41 (aka Brass Typhoon, Bronze Atlas, Double Dragon, Leopard Typhoon, and Wicked Panda), and UNC3886, which are said to have probed network equipment and industrial control systems of Taiwan's energy companies to plant malware. "China has fully integrated military, intelligence, industrial, and technological capabilities across both public and private sectors to enhance the depth of intrusion and operational stealth of its external cyberattacks through a wide range of cyberattack tactics and techniques," NSB said. China's cyber army is also said to have exploited vulnerabilities in the websites and systems of major hospitals in Taiwan to drop ransomware and conduct adversary-in-the-middle (AitM) attacks against communications companies to steal sensitive data.
6. Exchange Limit Canceled

   Microsoft
   [said](https://techcommunity.microsoft.com/blog/exchange/exchange-online-canceling-the-mailbox-external-recipient-rate-limit/4483498)
   it's indefinitely canceling earlier plans to enforce a Mailbox External Recipient Rate Limit in Exchange Online to combat abuse and prevent misuse of the service for bulk spam and other malicious email activity. "The Recipient Rate Limit and the Tenant-level External Recipient Rate Limit mentioned in Exchange Online limits remain unchanged by this announcement," the company said. The tech giant
   [first announced](https://techcommunity.microsoft.com/blog/exchange/exchange-online-to-introduce-external-recipient-rate-limit/4114733)
   the limit in April 2024, stating it would begin enforcing an external recipient rate limit of 2,000 recipients in 24 hours, effective April 2026.
7. Stalkerware Founder Guilty

   Bryan Fleming, the founder of
   [pcTattletale](https://thehackernews.com/2025/06/weekly-recap-apt-intrusions-ai-malware.html#:~:text=Stalkerware%20Apps%20Spyzie%2C%20Cocospy%2C%20and%20Spyic%20Go%20Offline)
   ,
   [pleaded](https://www.courtlistener.com/docket/68576045/searchseizure-warrant/)
   [guilty](https://www.courtlistener.com/docket/72109083/united-states-v-fleming/)
   to operating stalkerware from his home in the U.S. state of Michigan. In May 2024, the U.S.-based spyware company said it was "out of business and completely done" after an unknown hacker
   [defaced its website](https://web.archive.org/web/20240525052023/https://www.pctattletale.com/)
   and posted gigabytes of data to its homepage. The app, which covertly captured screenshots of hotel booking systems, suffered from a security flaw that allowed the screenshots to be available to anyone on the internet. The breach affected
   [more than 138,000 users](https://haveibeenpwned.com/Breach/pcTattletale)
   who had registered for the service. The U.S. Homeland Security Investigations (HSI) said it began investigating pcTattletale in June 2021 for "surreptitiously spying on spouses and partners." While the tool was
   [ostensibly marketed](https://web.archive.org/web/20231011165029/https://www.pctattletale.com/)
   as a parental control and employee monitoring software, pcTattletale also promoted its ability to snoop on spouses and domestic partners by tracking every click and screen tap. Fleming even had a
   [YouTube channel](https://web.archive.org/web/20260105175022/https://www.youtube.com/watch?v=SL5uCPlUg2s)
   to promote the spyware. He is expected to be sentenced later this year. The development marks a rare instance of criminal prosecution for purveyors of stalkerware, who often operate out in the open with impunity. The previous spyware conviction in the U.S.
   [occurred in 2014](https://www.justice.gov/archives/opa/pr/man-pleads-guilty-selling-stealthgenie-spyware-app-and-ordered-pay-500000-fine)
   when a Danish citizen, Hammad Akbar, pleaded guilty to operating the StealthGenie spyware.
8. Hardcoded Token Risk

   A critical security vulnerability has been
   [disclosed](https://github.com/rustfs/rustfs/security/advisories/GHSA-h956-rh7x-ppgj)
   in
   [RustFS](https://docs.rustfs.com/concepts/introduction.html)
   that stems from implementing gRPC authentication using a hard-coded static token that's publicly exposed in the source code repository, hard-coded on both client and server sides, non-configurable with no mechanism for token rotation, and universally valid across all RustFS deployments. "Any attacker with network access to the gRPC port can authenticate using this publicly known token and execute privileged operations, including data destruction, policy manipulation, and cluster configuration changes," RustFS said. The vulnerability, which does not have a CVE identifier, carries a CVSS score of 9.8. It affects versions alpha.13 through alpha.77, and has been patched in
   [1.0.0-alpha.78](https://github.com/rustfs/rustfs/releases/tag/1.0.0-alpha.78)
   released on December 30, 2025.
9. Malware via pkr\_mtsi

   A Windows packer and loader named pkr\_mtsi has been put to use in large-scale malvertising and SEO-poisoning campaigns to distribute trojanized installers for legitimate software such as PuTTY, Rufus, and Microsoft Teams, enabling initial access and flexible delivery of follow-on payloads. It's available in both executable (EXE) and dynamic-link library (DLL) forms. "In observed campaigns, pkr\_mtsi has been used to deliver a diverse set of malware families, including
   [Oyster](https://thehackernews.com/2024/06/oyster-backdoor-spreading-via.html)
   ,
   [Vidar Stealer](https://thehackernews.com/2023/06/vidar-malware-using-new-tactics-to.html)
   , Vanguard Stealer,
   [Supper](https://thehackernews.com/2025/11/gootloader-is-back-using-new-font-trick.html)
   , and more, underscoring its role as a general-purpose loader rather than a single-payload wrapper," ReversingLabs
   [said](https://www.reversinglabs.com/blog/unpacking-pkr_mtsi)
   . First observed in April 2025, the packer has witnessed a steady evolutionary trajectory in the intervening months, adding increasingly sophisticated obfuscation layers, anti-analysis and anti-debugging techniques, and evasive API resolution strategies.
10. Open WebUI RCE Risk

    A high-severity security flaw has been disclosed in Open WebUI in versions 0.6.34 and older (
    [CVE-2025-64496](https://github.com/open-webui/open-webui/security/advisories/GHSA-cm35-v4vp-5xvx)
    , CVSS score: 7.3) that affects the Direct Connections feature, which lets users connect to external AI model servers (e.g., OpenAI's API). "If a threat actor tricks a user into connecting to a malicious server, it can lead to an account takeover attack," Cato Networks
    [said](https://www.catonetworks.com/blog/cato-ctrl-vulnerability-discovered-open-webui-cve-2025-64496/)
    . "If the user also has workspace.tools permission enabled, it can lead to remote code execution (RCE). Which means that a threat actor can control the system running Open WebUI." The issue was addressed in version 0.6.35 released on November 7, 2025. The attack requires the victim to enable Direct Connections (disabled by default) and add the attacker's malicious model URL. At its core, the flaw stems from a trust failure between untrusted model servers and the user's browser session. A hostile server can send a crafted server-sent events message that triggers the execution of JavaScript code in the browser. This allows an attacker to steal authentication tokens stored in localStorage. Once obtained, those tokens grant full access to the victim's Open WebUI account. Chats, uploaded documents and API keys can all be exposed.
11. Iranian Group Evolves

    The Iranian nation-state group known as MuddyWater has been conducting phishing attacks designed to deliver known backdoors such as
    [Phoenix](https://thehackernews.com/2025/10/iran-linked-muddywater-targets-100.html)
    and
    [UDPGangster](https://thehackernews.com/2025/12/muddywater-deploys-udpgangster-backdoor.html)
    through executable files disguised as PDFs and DOC files with macro code. Both the implants come fitted with command execution and file upload/download capabilities. "It is worth noting that MuddyWater has gradually reduced the use of ready-made remote control programs such as RMM, and instead developed and deployed a variety of dedicated backdoors to implement penetration for specific targets," the 360 Threat Intelligence Center
    [said](https://mp.weixin.qq.com/s?__biz=MzUyMjk4NzExMA==&mid=2247507486&idx=1&sn=0dff4745b6c633dc05643744fcc62435&chksm=f9c1ed17ceb664014437bc93fc66feb95345648524896e03d8551bb2317107342312def355d3&scene=178&cur_album_id=1955835290309230595&search_click_id=#rd)
    . "The disguised content of the sample is Israeli, Azerbaijani, and English, and the sample is also uploaded by Israel, Azerbaijan, and other regions, which is in line with the attack target of the MuddyWater organization."
12. ownCloud MFA Alert

    File-sharing platform ownCloud has
    [warned](https://owncloud.com/security-advisories/security-advisory-credential-theft-incidents/)
    users to enable multi-factor authentication (MFA) to block malicious attempts that use compromised credentials to steal their data. The alert comes in the wake of a report from Hudson Rock, which flagged a threat actor named Zestix (aka Sentap) for auctioning data exfiltrated from the corporate file-sharing portals of about 50 major global enterprises. "Contrary to attacks involving sophisticated cookie hijacking or session bypasses, the Zestix campaign highlights a far more pedestrian – yet equally devastating – oversight: The absence of Multi-Factor Authentication (2FA)," Hudson Rock
    [said](https://www.infostealers.com/article/dozens-of-global-companies-hacked-via-cloud-credentials-from-infostealer-infections-more-at-risk/)
    . The attacks follow a well-oiled workflow: An employee inadvertently downloads a malicious file that leads to the deployment of information-stealing malware. Once the stolen information is made available for sale on darknet forums, the threat actor uses the valid usernames and passwords extracted from the stealer logs to sign into popular cloud file sharing services ShareFile, Nextcloud, and OwnCloud by taking advantage of the missing MFA protections. Zestix is believed to have been active in Russian-language closed forums since late 2024, primarily motivated by financial gain by selling access in exchange for Bitcoin payments. Assessed to be of
    [Iranian origin](https://www.darksignal.co/p/sentap-an-opportunistic-threat-actor)
    , the initial access broker has demonstrated ties with a ransomware group named
    [FunkSec](https://thehackernews.com/2025/01/ai-driven-ransomware-funksec-targets-85.html)
    .
13. Cross-Platform RAT Analysis

    ANY.RUN has
    [published](https://any.run/malware-trends/gravityrat/)
    a technical rundown of a sophisticated remote access trojan called
    [GravityRAT](https://thehackernews.com/2024/06/pakistan-linked-malware-campaign.html)
    that has been actively targeting organizations and government entities since 2016. A multi-platform malware, it's equipped to harvest sensitive data, including WhatsApp backups on Android devices, and boasts a wide range of anti-analysis features, including checking BIOS versions, searching for hypervisor artifacts, counting CPU cores, and querying CPU temperature through Windows Management Instrumentation (WMI). "This temperature check is particularly effective because most hypervisors, including Hyper-V, VMware Fusion, VirtualBox, KVM, and Xen, do not support temperature monitoring, causing them to return error messages that immediately reveal the presence of a virtual environment," ANY.RUN said. The use of GravityRAT is primarily attributed to a Pakistan-origin threat actor tracked as Transparent Tribe. On Windows, it's often spread via spear-phishing emails containing malicious Office documents with macros or exploits. On Android, it masquerades as a messaging platform and is distributed via third-party sites or social engineering. "The RAT operates through a multi-stage infection and command-and-control architecture," ANY.RUN added. "GravityRAT implements a modular architecture where different components handle specific functions."
14. Scam Empire Kingpin Caught

    Cambodian authorities have
    [arrested and extradited](https://www.bbc.com/news/articles/cy4q8e88n2vo)
    Chen Zhi, the alleged mastermind behind one of Asia's largest transnational scam networks, to China.
    [Chen](https://www.bbc.com/news/articles/c70jz8e00g1o)
    , 38, is the founder and chairman of Prince Group. He was among the three Chinese nationals arrested on January 6, 2026. His Cambodian nationality was "revoked by a Royal Decree" last month. In October 2025, the U.S. Department of Justice (DoJ)
    [unsealed](https://thehackernews.com/2025/10/threatsday-bulletin-15b-crypto-bust.html#crypto-empire-built-on-slavery)
    an indictment against Prince Group and Chen (in absentia) for operating illegal forced-labor scam compounds across Southeast Asia to conduct cryptocurrency fraud schemes, also known as romance baiting or pig butchering. Scamsters in such incidents begin by establishing fake relationships with unsuspecting users before coaxing them into investing their funds in bogus cryptocurrency platforms. The industrial scale of the operation notwithstanding, those conducting the scams are often trafficked foreign nationals, who are trapped and coerced to carry out online fraud under threat of torture. The U.K. and U.S. governments have also
    [sanctioned](https://www.gov.uk/government/news/uk-and-us-take-joint-action-to-disrupt-major-online-fraud-network)
    Prince Group, designating it as a transnational criminal organization. In a statement in November 2025, Prince Group
    [said](https://www.business-humanrights.org/en/latest-news/cambodia-prince-group-denies-allegations-linking-its-chairman-to-running-transnational-organised-crimes-including-scam-operations-after-sanctions-and-indictment-made-by-foreign-govts/)
    it "categorically rejects" the accusations. China's Ministry of Public Security
    [described](https://www.scmp.com/news/china/politics/article/3339118/alleged-scam-billionaire-chen-zhi-arrested-cambodia-and-extradited-china)
    Chen's arrest as "another great achievement under China-Cambodia law enforcement cooperation." Mao Ning, a spokesperson for China's Ministry of Foreign Affairs,
    [said](https://www.mfa.gov.cn/eng/xw/fyrbt/202601/t20260108_11808454.html)
    "for quite some time, China has been actively working with countries, including Cambodia, to crack down on crimes of online gambling and telecom fraud with notable outcomes." Beijing has also worked with Thailand and Myanmar to release thousands of people from scam compounds. Despite ongoing crackdowns, the United Nations Office on Drugs and Crime (UNODC) has said the criminal networks that run the scam hubs are evolving at an unprecedented scale. Scam victims worldwide lost between $18 billion and $37 billion in 2023, according to UNODC estimates.
15. Phishing Kits Double

    The number of phishing-as-a-service (PhaaS) toolkits doubled during 2025, with 90% of high-volume phishing campaigns leveraging such tools in 2025, according to an
    [analysis](https://blog.barracuda.com/2026/01/07/threat-spotlight-phishing-kits-evolved-2025)
    by Barracuda. Some of the notable PhaaS players were
    [Sneaky 2FA](https://thehackernews.com/2025/11/sneaky-2fa-phishing-kit-adds-bitb-pop.html)
    ,
    [CoGUI](https://thehackernews.com/2025/05/employees-searching-payroll-portals-on.html)
    ,
    [Cephas](https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html)
    ,
    [Whisper 2FA](https://thehackernews.com/2025/10/threatsday-bulletin-15b-crypto-bust.html)
    , and
    [GhostFrame](https://thehackernews.com/2025/12/new-advanced-phishing-kits-use-ai-and.html)
    . These kits incorporate advanced anti-analysis measures, MFA bypass, and stealth deployment that make it harder to detect using traditional measures. The main advantage of PhaaS kits is that they lower the barrier to entry, enabling even attackers with little technical expertise to mount large-scale, targeted phishing campaigns with minimal effort. The most common phishing themes observed during the year were fake payment, financial, legal, digital signature, and HR-related messages designed to deceive users into clicking on a link, scanning a QR code, or opening an attachment. Among the novel techniques used by phishing kits are obfuscations to hide URLs from detection and inspection, CAPTCHA for added authenticity, malicious QR codes, abuse of trusted, legitimate online platforms, and ClickFix, among others.
16. Zed IDE RCE Flaws

    Two high-severity security flaws have been disclosed in
    [Zed IDE](https://zed.dev/)
    that expose users to arbitrary code execution when loading or interacting with a maliciously crafted source code repository. "Zed automatically loaded
    [MCP](https://en.wikipedia.org/wiki/Model_Context_Protocol)
    [Model Context Protocol] settings from the workspace without requiring user confirmation," Mindguard
    [said](https://mindgard.ai/blog/zed-ide-vulnerabilities-coordinated-disclosure)
    about
    [CVE-2025-68433](https://github.com/zed-industries/zed/security/advisories/GHSA-cv6g-cmxc-vw8j)
    (CVSS score: 7.8). "A malicious project could use this to define MCP tools that execute arbitrary code on the developer's system without explicit permission." The second vulnerability (
    [CVE-2025-68432](https://github.com/zed-industries/zed/security/advisories/GHSA-29cp-2hmh-hcxj)
    , CVSS score: 7.8) has to do with the IDE implicitly trusting project-supplied Language Server Protocol (
    [LSP](https://en.wikipedia.org/wiki/Language_Server_Protocol)
    ) configurations, potentially opening the door to arbitrary command execution when a user opens any source code file in the repository. Following responsible disclosure on November 14, 2025, Zed released
    [version 0.218.2-pre](https://zed.dev/blog/secure-by-default)
    to address the issues last month.

That's the wrap for this week. These stories show how fast things can change and how small risks can grow big if ignored.

Keep your systems updated, watch for the quiet stuff, and don't trust what looks normal too quickly.

Next Thursday, ThreatsDay will be back with more short takes from the week's biggest moves in hacking and security.