---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:03:21.731424+00:00'
exported_at: '2026-04-02T04:03:24.675149+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/threatsday-bulletin-pqc-push-ai-vuln.html
structured_data:
  about: []
  author: ''
  description: ThreatsDay Bulletin covers stealthy attack trends, evolving phishing
    tactics, supply chain risks, and how familiar tools are being quietly abused.
  headline: 'ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing
    Kits & 20 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/threatsday-bulletin-pqc-push-ai-vuln.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: PQC Push, AI Vuln Hunting, Pirated Traps, Phishing Kits
  & 20 More Stories'
updated_at: '2026-04-02T04:03:21.731424+00:00'
url_hash: 1a1bb5cbacdaa9c573ca00fb45edc551eb2122eb
---

**

Ravie Lakshmanan
**

Mar 26, 2026

Cybersecurity / Hacking News

Some weeks in security feel loud. This one feels sneaky. Less big dramatic fireworks, more of that slow creeping sense that too many people are getting way too comfortable abusing things they probably shouldn’t even be touching.

There’s a little bit of everything in this one, too. Weird delivery tricks, old problems coming back in slightly worse forms, shady infrastructure doing shady infrastructure things, and the usual reminder that if criminals find a workflow annoying, they’ll just make a new one by Friday. Efficient little parasites. You almost have to respect the commitment.

A few of these updates have that nasty “yeah, that tracks” energy. Stuff that sounds niche right up until you picture it landing in a real environment with real users clicking real nonsense because they’re busy and tired and just trying to get through the day. Then it stops being abstract pretty fast.

So yeah, this week’s ThreatsDay Bulletin is a solid scroll-before-you-log-off kind of read. Nothing here needs a full panic spiral, but some of it definitely deserves a raised eyebrow and maybe a muttered: “Oh come on.” Let’s get into it.

1. PQC migration fast-tracked

   Google has unveiled a 2029 timeline to secure the quantum era with post-quantum cryptography (PQC) migration, urging other engineering teams to follow suit. "This new timeline reflects migration needs for the PQC era in light of progress on quantum computing hardware development, quantum error correction, and quantum factoring resource estimates," the tech giant
   [said](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/)
   . "Quantum computers will pose a significant threat to current cryptographic standards, and specifically to encryption and digital signatures. The threat to encryption is relevant today with store-now-decrypt-later attacks, while digital signatures are a future threat that require the transition to PQC prior to a Cryptographically Relevant Quantum Computer (CRQC). That's why we've adjusted our threat model to prioritize PQC migration for authentication services." As part of the effort, the company said Android 17 is integrating PQC digital signature protection using the Module-Lattice-Based Digital Signature Algorithm (
   [ML-DSA](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf)
   ). This
   [includes](https://security.googleblog.com/2026/03/post-quantum-cryptography-in-android.html)
   upgrading the Android Verified Boot (AVB) with support for ML-DSA to ensure that the software loaded during the boot sequence remains highly resistant to unauthorized tampering. The second PQC upgrade concerns the transition of Remote Attestation to a fully PQC-compliant architecture and updating Android Keystore to natively support ML-DSA.
2. AI finds hidden vulns

   GitHub said it's introducing AI-powered security detections in GitHub Code Security to expand application security coverage across more languages and frameworks. "These detections complement CodeQL by surfacing potential vulnerabilities in areas that are difficult to support with traditional static analysis alone," GitHub
   [said](https://github.blog/security/application-security/github-expands-application-security-coverage-with-ai-powered-detections/)
   . "This hybrid detection model helps surface vulnerabilities – and suggested fixes – directly to developers within the pull request workflow." The Microsoft subsidiary said the move is designed to uncover security issues "in areas that are difficult to support with traditional static analysis alone." The new hybrid model is expected to enter public preview in early Q2 2026.
3. Pirated apps spread backdoors

   The Russian threat actor known as Sandworm (aka APT-C-13) has been attributed with moderate confidence to an attack campaign that leverages pirated versions of legitimate software like Microsoft Office ("Microsoft.Office.2025x64.v2025.iso") as lures to deliver different backdoors tracked as Tambur,
   [Sumbur, Kalambur](https://thehackernews.com/2025/02/microsoft-uncovers-sandworm-subgroups.html)
   , and DemiMur to high-value targets. It's assessed that these attacks use Telegram as a distribution vector, using social engineering tactics to target Ukrainian users seeking software cracks. Tambur is designed to spawn SSH reverse tunnels to issue malicious commands, while Kalambur revolves around intranet penetration, remote desktop (RDP) takeover, and persistent communication. Sumbur is a successor to Kalambur with improved obfuscation techniques. DemiMur is mainly used to tamper with the trust chain and evade detection. "Attackers use this module to force the import of a forged DemiMurCA.crt root certificate into the operating system's trusted root certificate authority store," the 360 Advanced Threat Research Institute
   [said](https://mp.weixin.qq.com/s/QWe2m4qdp45u1cuA5rgLwQ)
   . "When subsequent scripts are executed, Windows automatically verifies the validity of the signature block and deems it 'trusted.'"
4. Fake extension drains wallets

   A cryptocurrency scam called ShieldGuard claimed to be a blockchain project that presented itself as a security tool aimed at protecting crypto wallets from phishing and harmful smart contracts through a browser extension. Ironically, further analysis revealed that it was built to drain digital assets from wallets. The scam was advertised via a dedicated website ("shieldguards[.]net"), as well as an X account (@ShieldGuardsNet) and a Telegram channel (@ShieldsGuard). "The project was promoted using a multi-level marketing campaign in which users would be rewarded for early use of the extension (via a cryptocurrency 'airdrop') and for promoting the capability to other users," Okta
   [said](https://www.okta.com/blog/threat-intelligence/disrupting-shieldguard--a-security-extension-primed-to-drain-cry/)
   . "ShieldGuard appears designed to harvest wallet addresses and other sensitive data for major cryptocurrency platforms including Binance, Coinbase, MetaMask, OpenSea, Phantom and Uniswap, as well as for users of Google services. The extension also extracts the full HTML of pages after a user signs into Binance, Coinbase, OpenSea or Uniswap via their browser." The threat actor behind the activity is assessed to be Russian-speaking.
5. Firmware backdoor spreads globally

   Sophos said it identified multiple detections on Android devices for malicious activity associated with the
   [Keenadu](https://thehackernews.com/2026/02/keenadu-firmware-backdoor-infects.html)
   backdoor. "Keenadu is a firmware infection embedded in the libandroid\_runtime.so (shared object library) that injects itself into the Zygote process," the company
   [said](https://www.sophos.com/en-us/blog/android-devices-ship-with-firmware-level-malware)
   . "As Zygote is the parent process for all Android apps, an attacker effectively gains total control over an infected device." Keenadu acts as a downloader for second-stage malware, with the infected devices containing two system-level APK files: PriLauncher.apk and PriLauncher3QuickStep.apk. Over 500 unique compromised Android devices across nearly 50 models have been detected as of March 4, 2026. The devices are mostly low-cost models produced by Allview, BLU, Dcode, DOOGEE, Gigaset, Gionee, Lava, and Ulefone. The identified infections were spread globally, with devices located in 40 countries.
6. Phishing service quickly rebounds

   In early March, Europol and Microsoft announced the seizure of 330 active
   [Tycoon2FA](https://thehackernews.com/2026/03/europol-led-operation-takes-down-tycoon.html)
   domains and legal action against multiple individuals linked to the PhaaS. According to CrowdStrike, the takedown effort left only a minor dent in Tycoon2FA's operations, which are now back to pre-disruption levels. On March 4 and 5, following the law enforcement operation, Tycoon2FA activity volume dropped to roughly 25%, but returned to previous levels shortly after, with "daily levels of cloud compromise active remediations returning to early 2026 levels," CrowdStrike
   [said](https://www.crowdstrike.com/en-us/blog/tycoon2fa-phishing-as-a-service-platform-persists-following-takedown/)
   . "Additionally, Tycoon2FA's TTPs have not changed following the takedown, indicating that the service's operations may persist beyond this disruption." These TTPs include phishing emails directing to malicious CAPTCHA pages, session cookie theft upon CAPTCHA validation, use of JavaScript payloads for email address extraction, credential proxying via malicious JavaScript files, and use of stolen credentials to access the victims' cloud environments. Post-disruption campaigns have leveraged malicious URLs, URL shortener services, links to legitimate presentation software that include malicious redirects to Tycoon2FA infrastructure, and attacker-controlled infrastructure impersonating construction entities, and compromised SharePoint infrastructure from known contacts that retrieves XLSX and PDF files. The short-lived disruption is proof that without arrests or physical seizures, it's easy for cybercriminals to recover and replace the impacted infrastructure.
7. Fake invites deliver remote access

   Phishing campaigns are weaponizing fake meeting invites for various video conference applications, including Zoom, Microsoft Teams, and Google Meet, to distribute remote access tools. "The attackers trick corporate users to execute the payload by claiming a mandatory software update is required to join the video call, redirecting victims to typo-squatted domains, such as zoom-meet.us," Netskope
   [said](https://www.netskope.com/blog/attackers-weaponize-signed-rmm-tools-via-zoom-meet-teams-lures)
   . "The payload, disguised as a software update, is a digitally signed remote monitoring and management (RMM) tool such as Datto RMM, LogMeIn, or ScreenConnect. These tools enable attackers to remotely access victims' machines and gain full administrative control over their endpoints, potentially leading to data theft or the deployment of more destructive malware."
8. Fileless stealer via phishing

   Attackers are using copyright-infringement notices in a fileless phishing campaign targeting healthcare and government organizations in Germany and Canada that delivers the
   [PureLogs](https://thehackernews.com/2025/05/purerat-malware-spikes-4x-in-2025.html)
   data-stealing malware. "The attack likely relies on phishing emails that lure victims into downloading a malicious executable tailored to the victim's local language," Trend Micro
   [said](https://www.trendmicro.com/en_us/research/26/c/copyright-lures-mask-a-multistage-purelog-stealer-attack.html)
   . "Once executed, the malware deploys a multistage infection chain designed for evasion. Notably, it downloads an encrypted payload disguised as a PDF file, then retrieves the decryption password remotely from attacker-controlled infrastructure. The extracted payload launches a Python-based loader that decrypts and executes the final .NET PureLogs stealer malware in memory." The Python dropper specifically leverages two .NET loaders to load the stealer malware, with one acting as a backup in case either of them is blocked or killed by an endpoint control. The routine also incorporates anti-virtual machine techniques to evade automated analysis environments, as well as employs in-memory execution to complicate detection efforts. "By disguising malicious executables as legal notices, using encrypted payloads masquerading as PDF files, remotely retrieving dynamic decryption keys, and leveraging a renamed WinRAR utility for extraction, the operators effectively minimize static indicators and hinder automated analysis," the company added. "The Python-based loader and dual .NET loaders introduce redundancy and fileless execution pathways, ensuring that the final PureLog Stealer payload is launched reliably and without leaving artifacts on disk."
9. MS-SQL attacks deploy scanner

   The Larva-26002 threat actor continues to target improperly managed MS-SQL servers. "In January 2024, the Larva-26002 threat actor attacked MS-SQL servers to install the Trigona and Mimic ransomware," AhnLab
   [said](https://asec.ahnlab.com/en/92988/)
   . In the latest attacks, the threat actors exploited the Bulk Copy Program (BCP) utility of MS-SQL servers to stage the malware locally and deploy a scanner malware named ICE Cloud Client. Written in Go, it functions as both a scanner and a brute-force tool to break into susceptible MS-SQL servers. "The strings contained in the binary are written in Turkish, and the emoticons used suggest that the author utilized generative AI," the company added.
10. Bug lets attackers fake rankings

    New research has flagged a critical vulnerability in ClawHub, a skills marketplace for OpenClaw, that an attacker could exploit to position their skill as the #1 skill. The flaw stems from the fact that a download counter function named "increment()," which is used to keep track of skill downloads, was exposed as a public mutation rather than an internal private function. Without authentication, rate limiting, or deduplication mechanisms in place, an attacker could continuously trigger the endpoint to artificially inflate the download metric for a given skill. "An attacker can call downloads:increment with a single curl request with any valid skill ID, bypassing every protection in the download flow and inflating any skill's downloads counter without limit," security researcher Noa Gazit
    [said](https://www.silverfort.com/blog/clawhub-vulnerability-enables-attackers-to-manipulate-rankings-to-become-the-number-one-skill/)
    . By gaming the rankings, the threat actor could device an unsuspecting developer into installing malicious skills. The issue has since been
    [mitigated by ClawHub](https://github.com/openclaw/clawhub/commit/ba9cdde7036214dfb2806fa045a10b002b56d9b7)
    following responsible disclosure by Silverfort on March 16, 2026.
11. npm packages steal crypto keys

    Five newly discovered malicious npm packages have been found to typosquat a legitimate cryptocurrency library and exfiltrate private keys to a single hard-coded Telegram bot. All the packages, ethersproject-wallet, base-x-64, bs58-basic, raydium-bs58, and base\_xd, were published under the account "galedonovan." According to
    [Socket](https://socket.dev/blog/5-malicious-npm-packages-typosquat-solana-and-ethereum-libraries-steal-private-keys)
    , "each package hooks a function that developers routinely pass private keys through. When that function is called at runtime, the package silently sends the key to a Telegram bot before returning the expected result. The user's code behaves normally, and there is no visible error or side effect."
12. Google Forms deliver malware

    A Google Forms campaign is using business-related lures, such as job interviews, project briefs, and financial documents, to distribute malware, including the PureHVNC remote access trojan (RAT). "Instead of the usual phishing email or fake download page, attackers are using Google Forms to kick off the infection chain," Malwarebytes
    [said](https://www.malwarebytes.com/blog/threat-intel/2026/03/that-job-brief-on-google-forms-could-infect-your-device)
    . "The attack typically begins when a victim downloads a business-themed ZIP file linked from a Google Form. Inside is a malicious file that sets off a multi-stage infection process, eventually installing malware on the system." Another campaign has been
    [observed](https://www.levelblue.com/blogs/spiderlabs-blog/tracing-a-multi-vector-malware-campaign-from-vbs-to-open-infrastructure)
    using obfuscated Visual Basic Script (VBScript) files to deliver
    [PhantomVAI Loader](https://thehackernews.com/2025/10/threatsday-bulletin-15b-crypto-bust.html#shipment-lures-drop-stealth-loaders)
    via PNG image files hosted on Internet Archive to ultimately install Remcos RAT and XWorm.
13. APT targets Web3 support teams

    A sophisticated, multi-stage malware campaign directed at customer support staff working for Web3 companies is
    [leveraging](https://www.zeroshadow.io/blog/malware-q27-customer-support/)
    suspicious links sent via customer support chat to initiate an attack chain that delivers a malicious executable disguised as a photograph, which then retrieves a second-stage loader from an AWS S3 dead drop. This loader proceeds to retrieve an implant named
    [Farfli](https://thehackernews.com/2023/12/chinese-hackers-using-sugargh0st-rat-to.html)
    (aka Gh0st RAT) that's launched via DLL side-loading to establish persistent communication with threat actor-controlled infrastructure. The campaign has been attributed to
    [APT-Q-27](https://thehackernews.com/2025/11/dragon-breath-uses-roningloader-to.html)
    (aka GoldenEyeDog), a
    [financially motivated threat group](https://ti.qianxin.com/blog/articles/tracking-the-recent-activities-of-the-apt-q-27-en/)
    suspected to be operating out of China since at least 2022. A similar campaign involving the distribution of sketchy links via Zendesk was
    [documented](https://cystack.net/research/malware-linked-apt-q-27)
    by CyStack last month. The techniques observed include staging payloads inside a directory designed to resemble a Windows Update cache, DLL side-loading, and in-memory execution of the final backdoor. The end goal is to reduce on-disk footprints, blend into normal system behaviour, and make retrospective detection harder.
14. Cloud phones fuel fraud economy

    Cloud phones are internet-based virtual phone systems powered by Android that allow users to send and receive voice calls, messages, and access features just like a physical device. While early fraud waves leveraged "virtual" Android devices hosted on physical phone farms for social media engagement manipulation, fake app reviews and installs, SMS spam, and ad fraud, subsequent iterations have evolved into cloud-based virtual mobile infrastructures that use emulators to mimic phone behavior. Along with it expanded the abuse of cloud phones – sold in the form of phone box devices – for
    [financial fraud](https://www.deloitte.com/us/en/insights/industry/financial-services/authorized-push-payment-fraud.html)
    expanded. Threat actors can buy, sell, and move cloud phones with pre-loaded e-wallets and pre-verified bank cards and accounts for use in Account TakeOver (ATO) and Authorized Push Payment (
    [APP](https://www.lseg.com/en/risk-intelligence/glossary/payment-fraud/authorised-push-payment-fraud)
    ) scams, Group-IB said. In this scheme, unsuspecting users are tricked into providing their personal banking credentials to fraudsters impersonating bank workers or government officials in order to complete the verification process on the fraudsters' cloud phone. These cloud phone devices with configured bank cards and accounts are then sold to other parties on darknet markets. "Major cloud phone platforms like LDCloud, Redfinger, and GeeLark offer device rentals for as little as $0.10-0.50 per hour, making fraud infrastructure accessible to anyone with minimal capital investment," the company
    [added](https://www.group-ib.com/blog/cloud-phones-invisible-threat/)
    . "Darknet markets actively trade pre-verified dropper accounts created on cloud phones, with Revolut and Wise accounts priced at $50-200 each, often including continued access to the cloud phone instance."
15. 500K+ IIS servers outdated

    The Shadowserver Foundation
    [said](https://x.com/Shadowserver/status/2036017138750861391)
    it's seeing over 511,000 end-of-life Microsoft IIS instances in its daily scans, out of which over 227,000 instances are beyond the official Microsoft Extended Security Updates (ESU) period. Most of them are located in China, the U.S., France, the U.K., Italy, Brazil, India, Japan, Australia, and Russia.
16. CCTV abuse triggers crackdown

    Indian authorities have
    [ordered](https://www.medianama.com/2026/03/223-india-cctv-audit-ghaziabad-spy-bust/)
    a comprehensive audit of CCTV systems across the nation following the exposure of a Pakistan-linked spy network that exploited surveillance cameras for espionage purposes. The solar-powered devices, installed at various railway stations and other important infrastructure, allegedly transmitted live footage to handlers linked to Pakistan's Inter-Services Intelligence (ISI). The Indian government has
    [outlined](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2245073&reg=3&lang=2)
    measures to strengthen the security of CCTV systems, such as mandatory documentation of the origin of critical components, testing of devices against vulnerabilities that could allow unauthorized remote access, and testing of devices for compliance. In tandem, at least 22 people have been
    [arrested](https://www.ndtv.com/india-news/massive-pakistan-linked-spy-network-conducted-pre-attack-recon-busted-in-up-ghaziabad-11254630)
    in connection with a Pakistan-linked network that engaged in reconnaissance activity. This included five men and a woman who have been accused of taking photos and videos of railway stations and military bases and sending them to handlers in Pakistan. These individuals were recruited through social media and encrypted messaging apps, luring them with payments ranging from ₹5,000 to ₹20,000 per "assignment." Compromised CCTV systems can facilitate military operations and intelligence gathering. During the U.S.–Israel–Iran conflict last month, Check Point Research found a sharp surge in exploitation attempts targeting IP cameras by Iran-affiliated threat actors.
17. TDS routes victims to scams

    A new traffic distribution (TDS) codenamed
    [TOXICSNAKE](https://themalwarefiles.com/threat-intelligence-dossier-toxicsnake-b3e954bd644b)
    has been used to route victims to phishing, scam funnels, or malware payloads. The attacks begin with a first-stage JavaScript loader that's capable of fingerprinting a site visitor, and either returns a redirect URL or a link to a malicious payload.
18. PowerShell ransomware evades EDR

    In a new report, Halcyon has revealed that the custom built Crytox PowerShell Encryptor is able to evade endpoint detection and response (EDR) solutions without the need for additional tooling like HRSword. "Crytox targeting continues to focus on virtual infrastructure (hypervisors, VM servers), entry via VPN exploitation, and manual hands-on-keyboard execution, which are all consistent with a deliberate, targeted operation rather than high-volume automated campaigns," the company
    [said](https://www.halcyon.ai/ransomware-research-reports/crytox-consistently-evades-endpoint-security-via-powershell)
    . The development comes as the INC ransomware group has claimed attacks against ten law firms and legal services organizations within a 48-hour period. "The volume, sector specificity, and timing of these postings suggest the possibility of a coordinated campaign or a shared upstream compromise, such as a supply chain event affecting a common legal technology provider or managed services vendor," Halcyon
    [noted](https://www.halcyon.ai/ransomware-alerts/inc-ransom-group-mounts-rapid-campaign-against-law-firms)
    .
19. Stealer exposes NK operator

    New research from Hudson Rock has
    [found](https://www.infostealers.com/article/infected-by-gta-5-cheats-how-an-infostealer-infection-unmasked-a-north-korean-agent/)
    a machine belonging to the North Korea IT worker scheme that was accidentally infected with the Lumma Stealer malware after the local user downloaded malicious payloads when searching for GTA V cheats. Interestingly, the exfiltrated stealer logs contained corporate CDN credentials for Funnull, a content delivery network (CDN) that has been leveraged by state-sponsored actors. The operator used a "massive matrix of synthetic identities" across Western freelance platforms and global hosting providers, while also using five distinct Chrome profiles and one Edge profile to compartmentalize their operations. It's believed that the machine owner was either a willing facilitator (i.e., a laptop farm host based out of Indonesia) or a North Korean operative.
20. Polyfill attack tied to DPRK

    The 2024
    [Polyfill[.]io supply chain attack](https://thehackernews.com/2024/07/polyfillio-attack-impacts-over-380000.html)
    has been linked to North Korean threat actors after a North Korean operative made a fatal operational security (OPSEC) blunder by downloading a fake software setup file and infected their own machine with the Lumma Stealer. While the attack was initially linked to Funnull, Hudson Rock
    [discovered](https://www.infostealers.com/article/how-one-infostealer-infection-solved-a-global-supply-chain-mystery-and-unmasked-dprk-spies-in-u-s-crypto/)
    that the threat actor downloaded a password-protected ZIP archive hosted on MediaFire that was deceptively named to appear as a legitimate software installer. The evidence collected by the malware from the North Korean hacker's endpoint included credentials for the Funnull DNS management portal, credentials for the Polyfill Cloudflare tenant (proving that the weaponized domain was under the threat actor's control), and conversations regarding the malicious domain configuration changes made during the peak of the attack. While the threat actor used the "Brian" persona to pull off the attack, they also mange other identities to conduct IT worker fraud by securing a gig at cryptocurrency exchange Gate and exploiting the access to obtain intelligence on their employer's security posture and understand blind spots in compliance systems. The same operative, under the "Wenyi Han" alias, is also said to have conducted strategic, state-sponsored data exfiltration, illustrating the severity of the IT worker threat.
21. Court dismisses WhatsApp case

    A U.S. judge granted a motion to
    [dismiss a case](https://thehackernews.com/2025/09/weekly-recap-bootkit-malware-ai-powered.html#:~:text=WhatsApp%20Former%20Security%20Chief%20Files%20Lawsuit)
    against tech giant Meta brought by a former WhatsApp employee, Attaullah Baig, who accused the company of ignoring privacy and security issues, and putting users' information in danger. According to
    [Courthouse News Service](https://www.courthousenews.com/meta-dodges-retaliation-claims-from-whatsapp-whistleblower/)
    , the judge said, "the complaint does not contain sufficient facts to show that the plaintiff reported violations of SEC rules or regulations, the plaintiff did not plead facts regarding the elements of securities fraud or wire fraud, and his reporting cybersecurity violations does not relate to rules governing internal accounting controls." Meta said, "Mr. Baig's allegations misrepresent the hard work of our security team. We're proud of our strong record of protecting people’s privacy and security, and will continue building on it."
22. Police gain password access powers

    Hong Kong police can now demand phone or computer passwords from those who are suspected of breaching the National Security Law (NSL). Those who refuse to share the passwords could face up to a year in jail and a fine of up to $12,700, and individuals who provide "false or misleading information" could face up to three years in jail. The amendments to the NSL ensure that "activities endangering national security can be effectively prevented, suppressed and punished, and at the same time the lawful rights and interests of individuals and organisations are adequately protected," authorities
    [said](https://www.bbc.com/news/articles/ce8j9yj52lro)
    . The move has prompted the U.S. Department of State Consular Affairs to issue an advisory, stating the legal change applies to everyone arriving or just transiting Hong Kong International Airport. "In addition, the Hong Kong government also has more authority to take and keep any personal devices, as evidence, that they claim are linked to national security offenses," it
    [noted](https://hk.usconsulate.gov/security-alert-2026032601/)
    .
23. Android RAT sold as MaaS

    A new Android RAT named
    [Oblivion RAT](https://thehackernews.com/2026/03/six-android-malware-families-target-pix.html)
    is being sold as a malware-as-a-service (MaaS) platform on cybercrime networks for $300/month. "The platform includes a web-based APK builder for the implant, a separate dropper builder that generates convincing fake Google Play update pages, and a C2 panel for real-time device control," iVerify
    [said](https://iverify.io/blog/oblivion-rat-android-spyware-analysis)
    . "Pricing runs $300/month, $700/3 months, $1,300/6 months, or $2,200 lifetime, with 7-day demo accounts available." Oblivion is distributed via dropper APKs sent to victims as part of social engineering attacks. Once installed, the dropper apps present a Google Play update flow to sideload the embedded RAT payload. As with other Android malware families, Oblivion abuses Android's accessibility services API to grant itself additional permissions and steal sensitive data. "The core of the social engineering is the Accessibility Page builder, which generates a pixel-perfect replica of Android's accessibility service settings screen," iVerify said. "Every text element is operator-controlled: page title, section headers, the Enable button, and a descriptive info message. When the victim taps Enable, they grant the implant's accessibility service full control over the device UI."

Disruptions don’t really stick anymore. Stuff gets taken down, shuffled around, then quietly comes back like nothing happened. Same tactics, slightly cleaner execution.

A lot of this leans on built-in trust. Familiar tools, normal flows, things people stop questioning. That gap between “looks fine” and “definitely not fine” is still doing most of the work.

Nothing here is shocking on its own. Put together, though, it’s a bit uncomfortable. Scroll on.