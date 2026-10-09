---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-01T21:28:23.076692+00:00'
exported_at: '2025-12-01T21:28:25.780275+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html
structured_data:
  about: []
  author: ''
  description: A fast, no-BS look at this week’s biggest security hits, what they
    mean for your team, and where to tighten up first.
  headline: '⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid
    & More'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/weekly-recap-hot-cves-npm-worm-returns.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: '⚡ Weekly Recap: Hot CVEs, npm Worm Returns, Firefox RCE, M365 Email Raid &
  More'
updated_at: '2025-12-01T21:28:23.076692+00:00'
url_hash: 3066f86a089bf20d2b8ed7ce3d2438c50ecc96f8
---

**

Dec 01, 2025
**

Ravie Lakshmanan

Hacking News / Cybersecurity

Hackers aren't kicking down the door anymore. They just use the same tools we use every day — code packages, cloud accounts, email, chat, phones, and "trusted" partners — and turn them against us.

One bad download can leak your keys. One weak vendor can expose many customers at once. One guest invite, one link on a phone, one bug in a common tool, and suddenly your mail, chats, repos, and servers are in play.

Every story below is a reminder that your "safe" tools might be the real weak spot.

## **⚡ Threat of the Week**

**Shai-Hulud Returns with More Aggression**
— The npm registry was
[targeted](https://entro.security/blog/shai-hulud-2-0-banks-gov-tech-breach/)
a
[second time](https://securitylabs.datadoghq.com/articles/shai-hulud-2.0-npm-worm/)
by a self-replicating worm that went by the moniker "Sha1-Hulud: The Second Coming," affecting over 800 packages and 27,000 GitHub repositories. Like in the previous iteration, the
[main objective](https://www.trendmicro.com/en_us/research/25/k/shai-hulud-2-0-targets-cloud-and-developer-systems.html)
was to steal sensitive data like API keys, cloud credentials, and npm and GitHub authentication information, and facilitate deeper supply chain compromise in a worm-like fashion. The malware also created GitHub Actions workflows that allow for command-and-control (C2) and injected GitHub Actions workflow mechanisms to steal repository secrets. Additionally, the malware
[backdoored](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
every npm package maintained by the victim, republishing them with malicious payloads that run during package installation. "Rather than relying solely on Node.js, which is more heavily monitored, the malware dynamically installs Bun during package installation, benefiting from its high performance and self-contained architecture to execute large payloads with improved stealth," Endor Labs
[said](https://www.endorlabs.com/learn/shai-hulud-2-malware-campaign-targets-github-and-cloud-credentials-using-bun-runtime)
. "This shift likely helps the malware evade traditional defenses tuned specifically to observe Node.js behavior." GitGuardian's analysis
[revealed](https://blog.gitguardian.com/shai-hulud-2/)
a total of 294,842 secret occurrences, which correspond to 33,185 unique secrets. Of these, 3,760 were valid as of November 27, 2025. These included GitHub access tokens, Slack webhook URLs, GitHub OAuth tokens, AWS IAM keys, OpenAI Project API keys, Slack bot tokens, Claude API keys, Google API Keys, and GitLab tokens. Trigger.dev, which had one of its engineers installing a compromised package on their development machine,
[said](https://trigger.dev/blog/shai-hulud-postmortem)
the incident led to credential theft and unauthorized access to its GitHub organization. The Python Package Index (PyPI) repository
[said](https://blog.pypi.org/posts/2025-11-26-pypi-and-shai-hulud/)
it was not impacted by the supply chain incident.

[![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8Xw8AAoMBgDTD2qgAAAAASUVORK5CYII=)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjxccbWJ-vDSqI16EW7ZePzdrN3msD8Y3I0OTsvj1um0AaRoYcyvX3eLFo-sBB0eYAJo4eAWSx6sD1CzE5eg8VyNf78Q3VT_rTNZnr4eRvv3yMkwnSzSHiOn2h2qJQ8R8lrBil_sKk2qB13O5gndDatKecuFz_HWw_qneqKBpSGsaEV3A9u84byU_xXgELI/s2600/tm.png)

## **🔔 Top News**

* **[ToddyCat Steals Outlook Emails and Microsoft 365 Access Tokens](https://thehackernews.com/2025/11/toddycats-new-hacking-tools-steal.html)**
  — Attackers behind the ToddyCat advanced persistent threat (APT) toolkit have evolved to stealing Outlook mail data and Microsoft 365 Access tokens. The APT group has refined its toolkit in late 2024 and early 2025 to capture not only browser credentials, as previously seen, but also victims' actual email archives and access tokens. The activity marks the second major shift in ToddyCat's tooling this year, following an April 2025 campaign where the group abused a vulnerability in ESET's security scanner to deliver a previously undocumented malware codenamed TCESB.
* **[Qilin Attack Breaches MSP to Hack into Dozens of Financial Firms](https://thehackernews.com/2025/11/qilin-ransomware-turns-south-korean-msp.html)**
  — South Korea's financial sector has been targeted by what has been described as a sophisticated supply chain attack that led to the deployment of Qilin ransomware. "This operation combined the capabilities of a major Ransomware-as-a-Service (RaaS) group, Qilin, with potential involvement from North Korean state-affiliated actors (Moonstone Sleet), leveraging Managed Service Provider (MSP) compromise as the initial access vector," Bitdefender said. Korean Leaks took place over three publication waves, resulting in the theft of over 1 million files and 2 TB of data from 28 victims. To pull off these attacks, the Qilin affiliate is said to have breached a single upstream managed service provider (MSP), leveraging the access to compromise several victims at once.
* **[CISA Warns of Spyware Campaigns Using Spyware and RATs](https://thehackernews.com/2025/11/cisa-warns-of-active-spyware-campaigns.html)**
  — The U.S. Cybersecurity and Infrastructure Security Agency (CISA) issued an alert warning of bad actors actively leveraging commercial spyware and remote access trojans (RATs) to target users of mobile messaging applications. The cyber actors use social engineering techniques to deliver spyware and gain unauthorized access to a victim's messaging app, facilitating the deployment of additional malicious payloads that can further compromise the victim's mobile device, the agency said. The activity focuses on high-value individuals, primarily current and former high-ranking government, military, and political officials, along with civil society organizations and individuals across the United States, the Middle East, and Europe.
* **[Attack Exploits WSUS Flaw to Deploy ShadowPad](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html)**
  — Unknown threat actors exploited a recently patched security flaw in Microsoft Windows Server Update Services (CVE-2025-59287) to distribute malware known as ShadowPad. The attackers have been found to weaponize the vulnerability to launch Windows utilities like "curl.exe" and "certutil.exe," to contact an external server ("149.28.78[.]189:42306") to download and install ShadowPad. It's not clear who is behind the attack, but ShadowPad is a privately sold malware widely shared by Chinese hacking groups.
* **[A Blindspot in Microsoft Teams Guest Access](https://thehackernews.com/2025/11/ms-teams-guest-access-can-remove.html)**
  — Cybersecurity researchers shed light on a "fundamental architectural gap" that allows attackers to bypass Microsoft Defender for Office 365 protections via the guest access feature in Teams. The issue is essentially that when users operate as guests in another tenant, their protections are determined entirely by that hosting environment, not by their home organization. Microsoft began rolling out guest access last month. "These advancements increase collaboration opportunities, but they also widen the responsibility for ensuring those external environments are trustworthy and properly secured," Ontinue said.

## **‎️‍🔥 Trending CVEs**

Hackers act fast. They can use new bugs within hours. One missed update can cause a big breach. Here are this week's most serious security flaws. Check them, fix what matters first, and stay protected.

This week's list includes —
[CVE-2025-12972, CVE-2025-12970, CVE-2025-12978, CVE-2025-12977, CVE-2025-12969](https://thehackernews.com/2025/11/new-fluent-bit-flaws-expose-cloud-to.html)
(Fluent Bit),
[CVE-2025-13207, CVE-2024-24481](https://kb.cert.org/vuls/id/521113)
(Tenda),
[CVE-2025-62164](https://nvd.nist.gov/vuln/detail/CVE-2025-62164)
(vLLM),
[CVE-2025-12816](https://nvd.nist.gov/vuln/detail/CVE-2025-12816)
(Forge),
[CVE-2025-59373](https://www.asus.com/security-advisory/)
(ASUS MyASUS),
[CVE-2025-59366](https://www.asus.com/security-advisory/)
(ASUS routers)
[CVE-2025-65998](https://nvd.nist.gov/vuln/detail/CVE-2025-65998)
(Apache Syncope),
[CVE-2025-13357](https://dbugs.ptsecurity.com/vulnerability/PT-2025-47785)
(HashiCorp Vault Terraform Provider),
[CVE-2025-33183, CVE-2025-33184](https://nvidia.custhelp.com/app/answers/detail/a_id/5725)
(NVIDIA Isaac-GR00T),
[CVE-2025-33187](https://nvidia.custhelp.com/app/answers/detail/a_id/5720)
(NVIDIA DGX Spark),
[CVE-2025-12571, CVE-2024-9183](https://about.gitlab.com/releases/2025/11/26/patch-release-gitlab-18-6-1-released/)
(GitLab CE/EE),
[CVE-2025-66035](https://nvd.nist.gov/vuln/detail/CVE-2025-66035)
(Angular HttpClient), and an
[unauthenticated DoS vulnerability](https://www.harmonyintelligence.com/taking-down-next-js-servers)
in Next.js (no CVE).

## **📰 Around the Cyber World**

* **Poland Detains Russian Citizen Over Hack**
  — Polish authorities
  [detained](https://www.gov.pl/web/po-krakow/tymczasowe-aresztowanie-obywatela-federacji-rosyjskiej-podejrzanego-o-nieuprawnione-ingerencje-w-systemy-teleinformatyczne)
  a Russian citizen suspected of hacking into the IT systems of local companies, marking the latest case that Warsaw has linked to Moscow's sabotage and espionage efforts. The suspect allegedly broke into an online retailer's systems without authorization and tampered with its databases so as to potentially disrupt operations. The identity of the suspect has not been disclosed.
* **FCC Urges Broadcasters to Ensure Security of Networks**
  — The U.S. Federal Communications Commission (FCC) has urged broadcasters to ensure the security of their broadcast networks and systems in response to a recent string of cyber attacks that led to the broadcast of obscene materials and the misuse of the Emergency Alert System (EAS) Attention Signal (Attention Signal). "It appears that these recent hacks were caused by a compromised studio-transmitter link (STL) – the broadcast equipment that carries program content from the studio to remote transmitters – with threat actors often accessing improperly secured Barix equipment and reconfiguring it to receive attacker-controlled audio in lieu of station programming," the FCC
  [said](https://www.fcc.gov/document/fcc-urges-broadcasters-follow-cybersecurity-best-practices)
  . "Affected stations broadcast to the public an attacker-inserted audio stream that includes an actual or simulated Attention Signal and EAS alert tones, as well as obscene language, and other inappropriate material."
* **Firefox WebAssembly Flaw Detailed**
  — AISLE published technical details on CVE-2025-13016 (CVSS score: 7.5), a high-severity vulnerability in Firefox's WebAssembly engine that could lead to remote code execution. "A single line of template code, mixing uint8\_t\* and uint16\_t\* pointers in a std::copy operation created a memory corruption vulnerability that could allow attackers to execute arbitrary code," security researcher Stanislav Fort
  [said](https://aisle.com/blog/a-high-severity-webassembly-boundary-condition-vulnerability-in-firefox-cve-2025-13016)
  . The vulnerable code was introduced to the browser in April 2025, but remained unnoticed until October. It was patched in Firefox 145.
* **New Operation Shuts Down Cryptomixer**
  — Europol, alongside authorities from Switzerland and Germany, shut down a hybrid cryptocurrency mixing service known as Cryptomixer, which is suspected of facilitating cybercrime and money laundering. The
  [operation](https://www.eurojust.europa.eu/news/cryptocurrency-mixing-service-used-launder-money-taken-down)
  , named
  [Olympia](https://www.operation-olympia.com)
  , took place between November 24 and 28, 2025. The effort also led to over 12 terabytes of data and more than €25 million ($29.05 million) worth of Bitcoin. Since its creation in 2016, over €1.3 billion in Bitcoin is estimated to have been mixed through the service. "It facilitated the obfuscation of criminal funds for ransomware groups, underground economy forums, and dark web markets," Europol
  [said](https://www.europol.europa.eu/media-press/newsroom/news/europol-and-partners-shut-down-cryptomixer)
  . "It's software blocked the traceability of funds on the blockchain, making it the platform of choice for cybercriminals seeking to launder illegal proceeds from a variety of criminal activities, such as drug trafficking, weapons trafficking, ransomware attacks, and payment card fraud." The development came as Dutch police officials
  [seized](https://www.politie.nl/nieuws/2025/november/14/02---duizenden-servers-in-beslaggenomen-in-omvangrijk-cybercrime-onderzoek.html)
  250 servers linked to an unnamed bulletproof hosting provider on November 12, 2025.
* **South Korea Sentenced Man to 1 Year in Prison for Buying Hacking Tools From North Korea**
  — A 39-year-old businessman, referred to as Mr. Oh, was sentenced to one year in prison for repeatedly contacting a North Korean hacker named Eric via the QQ messenger and purchasing hacking programs to neutralize security software for operating illegal private servers for Lineage, The Chosun Daily
  [reported](https://www.chosun.com/english/national-en/2025/11/14/N6UAAHPAJBAJNJMIWFCSSZSADM/)
  .
* **AI Company Spots Fraud Campaign**
  — Artificial intelligence (AI)-driven agentic coding platform Factory said it disrupted a highly automated cyber operation abusing its free tiers to automate cyber attacks using its Droid AI development agent. "The goal of this attack was to exploit free compute at scale by chaining together free usage from multiple AI products and reselling that access and using it to mask a broad range of activity, including cyber crime," the company
  [said](https://factory.ai/news/droid-neutralizing-fraud)
  . "The infrastructure supported automated creation of accounts and organizations across multiple providers, redemption of trials and promotions as soon as they became available, health checking and key rotation when a provider banned or throttled a key, and routing logic that could shift traffic away from Droid moment‑to‑moment as our defenses tightened." The attack was conducted by a large, China‑based operation, it added, stating at least one state‑linked actor was involved.
* **Fake Battlefield 6 Game Used to Deliver Stealers and C2 Agents**
  — Threat actors are
  [capitalizing](https://www.bitdefender.com/en-us/blog/labs/fake-battlefield-6-pirated-games-trainers)
  on the popularity of Electronic Arts' Battlefield 6 game to distribute pirated versions, game installers, and fake game trainers across torrent websites that deploy stealers and C2 agents. One of the payloads, once executed, steals Discord credentials, cryptocurrency wallet, and cookies from Chrome, Edge, Firefox, Opera, Brave, Vivaldi, and Wave Browser. Another stealer malware, distributed as "Battlefield 6.GOG-InsaneRamZes," incorporates evasive features that stop execution if it finds that it's being run in a sandboxed environment or in a computer that geolocates to Russia or Commonwealth of Independent States (CIS) countries.
* **Nation-State Threat Actors Begin to Collaborate**
  — Cooperation within national state-sponsored ecosystems has become increasingly common, Gen Digital said, with overlaps in infrastructure (216.219.87[.]41) observed between North Korean threat actors, Lazarus Group's Contagious Interview, and Kimsuky. The cybersecurity company also said it identified a DoNot Team-attributed payload executing a known SideWinder loader in an attack targeting a victim located in Pakistan. But in a more interesting twist, an IP address previously used by Gamaredon as C2 was flagged as hosting an obfuscated version of InvisibleFerret, a Python backdoor linked to the Contagious Interview campaign. "While the IP could represent a proxy or VPN endpoint, the temporal proximity of both groups' activity and the shared hosting pattern indicate probable infrastructure reuse, with moderate confidence of operational collaboration," it
  [said](https://www.gendigital.com/blog/insights/research/apt-cyber-alliances-2025)
  . "Whether Lazarus leveraged a Gamaredon-controlled server or both actors shared the same client instance remains unclear, but the overlap is too close to ignore."
* **Anthropic Says Claude Opus is More Robust Against Prompt Injections**
  — AI company Anthropic, which released its coding model Claude Opus 4.5 last week, said it has substantial progress in robustness against prompt injection attacks that aim to smuggle in deceptive instructions to fool the model into harmful behavior. "Opus 4.5 is harder to trick with prompt injection than any other frontier model in the industry," it
  [said](https://www.anthropic.com/news/claude-opus-4-5)
  , beating Claude Haiku 4.5, OpenAI GPT-5.1, and Google Gemini 3 Pro. Anthropic said it added new external and internal evaluations for malicious uses and prompt injection attacks related to coding, computer use, and browser use environments, finding that Opus 4.5 refused 100% of the 150 malicious coding requests in an agentic coding evaluation. When tested to see whether it would comply with "malware creation, writing code for destructive DDoS attacks, and developing non-consensual monitoring software," the model refused about 78% of requests. It also refused just over 88% of requests related to surveillance, data collection, and generating and spreading harmful content.
* **Security Flaws in Uhale Android Photo Frames**
  — Multiple critical security issues and insecure behaviors have been disclosed in Uhale Android-based digital picture frames that could allow attackers to take complete control of the devices, potentially leading to malware infections, data exfiltration, botnet recruitment, lateral movement to other systems on the network, and other malicious actions. According to Quokka researchers Ryan Johnson, Doug Bennett, and Mohamed Elsabagh, the shortcomings
  [include](https://www.quokka.io/resources/technical-paper/uhale-digital-picture-frame-security-assessment)
  automatic malware delivery on boot on some devices, remote code execution (RCE) flaws due to insecure trust managers and unsanitized shell execution, arbitrary file write due to unauthenticated and unsanitized file transfers, and improperly configured file providers, SQL injection, and use of weak cryptography. Of the 17 issues, 11 have been assigned CVE identifiers. The most concerning finding is that the Uhale app (version 4.2.0) downloads suspicious artifacts, which are then executed by a service that shares package prefix similarities with a malware codenamed Mzmess that's delivered by the
  [Vo1d botnet](https://thehackernews.com/2025/03/vo1d-botnets-peak-surpasses-159m.html)
  . Uhale said a majority of the flaws have been fixed in version 4.2.1, with additional fixes being planned in version 5.1.0. The
  [current version](https://play.google.com/store/apps/details?hl=en&id=com.zeasn.technical.phone.frames)
  of the app is 4.33.
* **Operation South Star Leverages ZipperDown in China Attacks**
  — A now-patched
  [vulnerability](https://www.bitdefender.com/en-us/blog/hotforsecurity/zipperdown-programming-vulnerability-could-let-hackers-execute-code-in-ios-apps)
  known as
  [ZipperDown](https://zimperium.com/blog/zipperdown-vulnerability-100-million-ios-users-not-using-zimperium-risk-exploit)
  is said to have been exploited in the wild by nation-state actors in attacks targeting mobile devices in China, QiAnXin said. The activity has been named Operation South Star. "The attacker sends an email containing the exploit to the target's mobile email application," it
  [said](https://ti.qianxin.com/blog/articles/operation-south-star-en/)
  . "When the victim clicks on the email on their phone, ZipperDown is triggered instantly, unpacking a carefully crafted DAT file and releasing malicious SO and APK files to overwrite the target application components. Attackers exploited a logic vulnerability in the IMG image processing of a certain email Android app version, carefully constructing a DAT file that meets the format, ultimately triggering Zipperdown to overwrite the app's related library files." The malicious component is designed to establish a shell connection and execute second-stage commands. Recent cases observed in 2024 and 2025 have leveraged the modified SO file to act as a downloader for an APK file and load it. The malware, in turn, contacts a C2 server to periodically poll for new commands and execute them, allowing it to gather device and file information, read files, and start a reverse shell.
* **Threat Actors Continue to Advertise Malicious LLMs**
  — Bad actors have been
  [observed](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/the-devil-reviews-xanthorox-a-criminal-focused-analysis-of-the-latest-malicious-llm-offering)
  marketing malicious large language models (LLMs) like WormGPT 4, KawaiiGPT, and Xanthorox that are designed to generate phishing emails, write polymorphic malware, and automate reconnaissance by expressly removing ethical constraints and safety filters during their foundational training or fine-tuning process. Some of these tools, like Xanthorox, are advertised for $2,500 per year. While the code generated by these tools does not introduce hugely novel capabilities and requires additional human tweaking to enhance operational effectiveness for criminal tasks, these unrestricted models seek to further lower the barrier to entry for less-skilled actors and script kiddies, thereby democratizing cybercrime. As a result, attacks that once required certain expertise in coding could be pulled off at scale within a short span of time by anyone with access to the internet and a basic understanding of prompts. "The line between a benign research tool and a powerful threat creation engine is dangerously thin," Palo Alto Networks Unit 42
  [said](https://unit42.paloaltonetworks.com/dilemma-of-ai-malicious-llms/)
  . "The two are often separated only by the developer's intent and the absence of ethical guardrails." While safeguards built into the model are the first line of defense against such attacks, an increasingly common approach to bypass those defenses is for attackers to claim that they are a security researcher or participating in a capture-the-flag (CTF) tournament and need the offensive code for their exercise. As a case in point, new research from Netskope Threat Labs has
  [found](https://www.netskope.com/blog/the-future-of-malware-is-llm-powered)
  that OpenAI's GPT-4's built-in safeguards can be circumvented through role-based prompt injection to generate malicious code. Simply telling the model to assume the persona of a penetration testing automation script focused on defense evasion was enough to create a Python script that can inject itself into svchost.exe and terminate all antivirus-related processes. Furthermore, Microsoft, which is rolling out agentic AI features to Windows 11,
  [acknowledged](https://support.microsoft.com/en-us/windows/experimental-agentic-features-a25ede8a-e4c2-4841-85a8-44839191dfb3)
  that such applications introduce novel security risks, such as cross-prompt injection (XPIA), that can result in data exfiltration or malware installation. As threat actors increasingly resort to incorporating such tools, it's imperative that developers of foundation models implement mandatory, robust alignment techniques and adversarial stress testing before public release. "Addressing the security challenges of AI agents requires adherence to a strong set of security principles to ensure agents act in alignment with user intent and safeguard their sensitive information," Microsoft
  [said](https://learn.microsoft.com/en-us/windows/security/book/operating-system-agentic-security)
  .

## **🎥 Cybersecurity Webinars**

* [How to Detect Hidden Risks in AWS, AI, and Kubernetes — Before Attackers Do](https://thehacker.news/code-to-cloud-detection?source=recap)
  : Cloud threats are getting smarter—and harder to see. Join our experts to learn how code-to-cloud detection reveals hidden risks across identities, AI, and Kubernetes, helping you stop attacks before they reach production.
* [Learn How Top Teams Secure Cloud Infrastructure While Staying Fully Compliant](https://thehacker.news/securing-cloud-workloads?source=recap)
  : Securing cloud workloads isn't just defense — it's about enabling innovation safely. Learn practical, proven ways to strengthen access control, maintain compliance, and protect infrastructure without slowing agility.
* [How to Patch Faster and Safer: The Guardrail Framework That Actually Works](https://thehacker.news/resilient-patching?source=recap)
  : Community patching is fast, flexible, and easy to get wrong. This session shows how to build guardrails, spot repo risks early, and balance speed with security using proven, field-tested methods.

## **🔧 Cybersecurity Tools**

* [LUMEN](https://github.com/Koifman/LUMEN)
  — It is a browser-based Windows Event Log analyzer that runs entirely on your machine. It lets analysts upload multiple EVTX files, run SIGMA detections, correlate events into storylines, extract IOCs, and export findings—all without data leaving the device. Designed for secure, offline investigations, it supports curated and custom SIGMA rules, dashboards, and local session storage for efficient, privacy-focused log analysis.
* [Pi-hole](https://github.com/pi-hole/pi-hole)
  — It is a network-wide DNS sinkhole that blocks ads, trackers, and unwanted domains before they reach your devices. Installed on local hardware or servers, it filters all network traffic without client software and provides a dashboard and CLI for monitoring, custom blocklists, and DNS control.

*Disclaimer: These tools are for learning and research only. They haven't been fully tested for security. If used the wrong way, they could cause harm. Check the code first, test only in safe places, and follow all rules and laws.*

## **Conclusion**

If there's one theme this week, it's this: nobody is "too small" or "too boring" to be a target anymore. The weak link is usually something simple — a package no one checked, a vendor no one questioned, a "temporary" token that never got revoked, a guest account nobody owns. Attackers love that stuff because it works.

So don't just close this tab and move on. Pick one thing from this recap you can act on today — rotate a set of keys, tighten access for one vendor, review guest accounts, lock down an update path, or fix one high-risk bug. Then share this with the people who can break things and fix things with you. The gap between "we should do this" and "we actually did" is where most breaches live.