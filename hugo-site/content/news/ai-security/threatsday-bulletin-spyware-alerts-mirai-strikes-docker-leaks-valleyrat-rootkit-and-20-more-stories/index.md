---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-12-12T00:03:07.426602+00:00'
exported_at: '2025-12-12T00:03:10.258219+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html
structured_data:
  about: []
  author: ''
  description: The latest ThreatsDay Bulletin breaks down the week’s biggest stories
    — rootkits evading Windows, Docker leaks, AI risks and global surveillance moves
  headline: 'ThreatsDay Bulletin: Spyware Alerts, Mirai Strikes, Docker Leaks, ValleyRAT
    Rootkit — and 20 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/12/threatsday-bulletin-spyware-alerts.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: 'ThreatsDay Bulletin: Spyware Alerts, Mirai Strikes, Docker Leaks, ValleyRAT
  Rootkit — and 20 More Stories'
updated_at: '2025-12-12T00:03:07.426602+00:00'
url_hash: 1d1f2671374a8cb8809c8cde0933b6bf9eb73732
---

**

Dec 11, 2025
**

Ravie Lakshmanan

This week's cyber stories show how fast the online world can turn risky. Hackers are sneaking malware into movie downloads, browser add-ons, and even software updates people trust. Tech giants and governments are racing to plug new holes while arguing over privacy and control. And researchers keep uncovering just how much of our digital life is still wide open.

The new Threatsday Bulletin brings it all together—big hacks, quiet exploits, bold arrests, and smart discoveries that explain where cyber threats are headed next.

It's your quick, plain-spoken look at the week's biggest security moves before they become tomorrow's headlines.

1. Maritime IoT under siege

   A new Mirai botnet variant dubbed Broadside has been exploiting a critical-severity vulnerability in TBK DVR (
   [CVE-2024-3721](https://nvd.nist.gov/vuln/detail/CVE-2024-3721)
   ) in attacks targeting the maritime logistics sector. "Unlike previous Mirai variants, Broadside employs a custom C2 protocol, a unique 'Magic Header; signature, and an advanced 'Judge, Jury, and Executioner' module for exclusivity," Cydome
   [said](https://cydome.io/cydome-identifies-broadside-a-new-mirai-botnet-variant-targeting-maritime-iot/)
   . "Technically, it diverges from standard Mirai by utilizing Netlink kernel sockets for stealthy, event-driven process monitoring (replacing noisy filesystem polling), and employing payload polymorphism to evade static defenses." Specifically, it tries to maintain exclusive control over the host by terminating other processes that match specific path patterns, fail internal checks, or have already been classified as hostile. Broadside extends beyond denial-of-service attacks, as it attempts to harvest system credential files (/etc/passwd and /etc/shadow) with an aim to establish a strategic foothold into compromised devices. Mirai is a formidable botnet that has spawned several variants since its source code was leaked in 2016.
2. LLM flaws persist indefinitely

   The U.K. National Cyber Security Centre
   [said](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
   prompt injections – which refer to flaws in generative artificial intelligence (GenAI) applications that allow them to parse malicious instructions to generate content that's otherwise not possible – "will never be properly mitigated" and that it's important to raise awareness about the class of vulnerability, as well as designing systems that "constrain the actions of the system, rather than just attempting to prevent malicious content reaching the LLM."
3. VaaS crackdown nets 193 arrests

   Europol's Operational Taskforce (OTF) GRIMM has arrested 193 individuals and disrupted criminal networks that have fueled the growth of violence-as-a-service (VaaS). The task force was launched in April 2025 to combat the threat, which involves recruiting young, inexperienced perpetrators to commit violent acts. "These individuals are groomed or coerced into committing a range of violent crimes, from acts of intimidation and torture to murder," Europol
   [said](https://www.europol.europa.eu/media-press/newsroom/news/operational-taskforce-grimm-193-arrests-in-6-months-tackling-violence-service-networks)
   . Many of the criminals involved in the schemes are alleged to be members of The Com, a loosely-knit collective comprising primarily English speakers who are involved in cyber attacks, SIM swaps, extortion, and physical violence.
4. Hack tools seized in Poland

   Polish law enforcement arrested three Ukrainian nationals for allegedly attempting to damage IT systems in the country using specialized hacking equipment after their vehicle was stopped and inspected. They have been charged with fraud, computer fraud, and acquiring computer equipment and software adapted to commit crimes, including damage to computer data of particular importance to the country's defense. "Officers thoroughly searched the vehicle's interior. They found suspicious items that could even be used to interfere with the country's strategic IT systems, breaking into IT and telecommunications networks," authorities
   [said](https://srodmiescie.policja.gov.pl/rs/aktualnosci/145521,Podrozowali-po-Europie-z-detektorem-urzadzen-szpiegowskich-i-sprzetem-hakerskim.html)
   . "During the investigation, officers seized a spy device detector, advanced Flipper hacking equipment, antennas, laptops, a large number of SIM cards, routers, portable hard drives, and cameras." The three men, of ages between 39 and 43, claimed to be computer scientists and "were visibly nervous," but did not give reasons as to why they were carrying such tools in the first place, and pretended not to understand what was being said to them, officials said.
5. Teen data thief caught

   The National Police in Spain have arrested a suspected 19-year-old hacker in Barcelona, for allegedly stealing and attempting to sell 64 million records obtained from breaches at nine companies. The defendant is said to have used six online accounts and five pseudonyms to advertise and sell the stolen databases. The teen faces charges related to involvement in cybercrime, unauthorized access, and disclosure of private data, and privacy violations. "The cybercriminal accessed nine different companies where he obtained millions of private personal records that he later sold online," authorities
   [alleged](https://www.policia.es/_es/comunicacion_prensa_detalle.php?ID=16737)
   . In a related development, Ukrainian police officials
   [announced](https://cyberpolice.gov.ua/news/policzejski-bukovyny-vykryly-arbitra-xakerskogo-forumu-yakyj-prodavav-vkradeni-akaunty-korystuvachiv-8323/)
   the arrest of a 22-year-old cybercriminal who used a custom malware he independently created to automatically hack user accounts on social networks and other platforms. The compromised accounts were then sold on hacker forums. Most of the victims were based in the U.S. and various European countries. The Bukovyn resident is also accused of administering a bot farm with more than 5,000 profiles in various social networks in order to implement various shadow schemes and transactions.
6. Millions lost via fake banking apps

   Russian police
   [said](https://t.me/IrinaVolk_MVD/5933)
   they have dismantled a criminal enterprise that stole millions from bank customers in the country using malware built on
   [NFCGate](https://thehackernews.com/2024/11/ghost-tap-hackers-exploiting-nfcgate-to.html)
   , a legitimate open-source tool increasingly exploited by cybercriminals worldwide. To that end, three suspects have been arrested for distributing NFC-capable malware through WhatsApp and Telegram, disguising it as software from legitimate banks. Victims were first approached via phone and persuaded to install a fraudulent banking app. During the fake "authorization" process, they were guided to hold their bank card to the back of their smartphone and enter their PIN — a step that enabled the attackers to harvest card credentials and withdraw funds from ATMs anywhere in the country without the cardholder's involvement. Preliminary losses exceed 200 million rubles (about $2.6 million).
7. Botnets exploit React flaw

   The recently disclosed React security flaw (
   [React2Shell](https://thehackernews.com/2025/12/react2shell-exploitation-delivers.html)
   , aka CVE-2025-55182) has come under widespread exploitation, including targeting smart home devices, according to
   [Bitdefender](https://www.bitdefender.com/en-us/blog/labs/cve-2025-55182-exploitation-hits-the-smart-home)
   . These include smart plugs, smartphones, NAS devices, surveillance systems, routers, development boards, and smart TVs. These attacks have been found to deliver Mirai and RondoDox botnet payloads. Significant probing activity has been detected from Poland, the U.S., the Netherlands, Ireland, France, Hong Kong, Singapore, China, and Panama. This indicates "broad global participation in opportunistic exploitation," the company said. Threat intelligence firm GreyNoise
   [said](https://www.greynoise.io/blog/cve-2025-55182-react2shell-opportunistic-exploitation-in-the-wild-what-the-greynoise-observation-grid-is-seeing-so-far)
   it observed 362 unique IP addresses across ~80 countries attempting exploitation as of December 8, 2025. "Observed payloads fall into distinct groups: miners, dual-platform botnets, OPSEC-masked VPN actors, and recon-only clusters," it added.
8. Linux malware evades detection

   Cybersecurity researchers have discovered a previously undocumented Linux backdoor named GhostPenguin. A multi-thread backdoor written in C++, it can collect system information, including IP address, gateway, OS version, hostname, and username, and send it to a command-and-control (C&C) server during a registration phase. "It then receives and executes commands from the C&C server. Supported commands allow the malware to provide a remote shell via '/bin/sh,' and perform various file and directory operations, including creating, deleting, renaming, reading, and writing files, modifying file timestamps, and searching for files by extension," Trend Micro
   [said](https://www.trendmicro.com/en_us/research/25/l/ghostpenguin.html)
   . "All C&C communication occurs over UDP port 53." The discovery comes as Elastic detailed a new syscall hooking technique called
   [FlipSwitch](https://www.elastic.co/security-labs/flipswitch-linux-rootkit)
   that has been devised in the aftermath of fundamental changes introduced to the Linux kernel 6.9 to allow malware to hide its presence on infected hosts. "Traditional rootkit techniques relied on direct syscall table manipulation, but modern kernels have moved to a switch-statement based dispatch mechanism," security researcher Remco Sprooten
   [said](https://github.com/1337-42/FlipSwitch-dev/)
   . "Instead of modifying the syscall table, it locates and patches specific call instructions inside the kernel's dispatch function. This approach allows for precise and reliable hooking, and all changes are fully reverted when the module is unloaded."
9. Crypto laundering plea deal

   Evan Tangeman, a 22-year-old California resident, pleaded guilty to RICO conspiracy charges after being accused of buying homes and laundering $3.5 million on behalf of a criminal gang that stole cryptocurrency through social engineering schemes. "The enterprise began no later than October 2023 and continued through at least May 2025. It grew from friendships developed on online gaming platforms and consisted of individuals based in California, Connecticut, New York, Florida, and abroad," the Justice Department (DoJ)
   [said](https://www.justice.gov/usao-dc/pr/guilty-plea-and-superseding-indictment-announced-social-engineering-scheme-stole-263)
   . "Tangeman was a money launderer for the group that also included database hackers, organizers, target identifiers, callers, and residential burglars targeting hardware virtual currency wallets." Members of the group were
   [previously charged](https://thehackernews.com/2025/05/weekly-recap-zero-day-exploits-insider.html#:~:text=DoJ%20Charges%2012%20More%20in%20RICO%20Conspiracy)
   with stealing more than $263 million worth of cryptocurrency from a victim in Washington, D.C.
10. Spyware warnings go global

    Apple and Google have sent a new round of spyware notifications to users in nearly 80 countries, according to a
    [report](https://www.reuters.com/technology/apple-sent-new-round-cyber-threat-notifications-users-84-countries-2025-12-05)
    from Reuters. There are currently no details about what kind of spyware the victims were targeted with. Neither company provided information on the number of users targeted or who they thought was behind the surveillance efforts.
11. EU greenlights Meta's ad model

    The European Commission has given its stamp of approval to a Meta proposal to give Instagram and Facebook users an option to share less personal data and see fewer personalized ads. The new option goes into effect in January 2026. "Meta will give users the effective choice between consenting to share all their data and seeing fully personalized advertising, and opting to share less personal data for an experience with more limited personalized advertising," the Commission
    [said](https://digital-markets-act.ec.europa.eu/meta-commits-give-eu-users-choice-personalised-ads-under-dma-2025-12-08_en)
    . The move comes after the social media giant was
    [fined €200 million](https://thehackernews.com/2025/07/google-ordered-to-pay-314m-for-misusing.html)
    in April 2025 (then $227 million) for violating the bloc's Digital Markets Act (DMA) over the
    [binary choice](https://thehackernews.com/2024/07/meta-given-deadline-to-address-eu.html)
    it gives E.U. users to either pay to access ad-free versions of the platforms or agree to being tracked in exchange for targeted ads. In a post last week, Austrian non-profit None of Your Business (noyb)
    [published](https://noyb.eu/en/pay-or-okay-study-users-prefer-tracking-free-third-option)
    a survey that said "when there's a 'pay,' a 'consent,' and an 'advertising, but no tracking' option, [...] 7 out of 10 people then choose the 'advertising, but no tracking' option."
12. Mass alert for Lumma victims

    New Zealand's National Cyber Security Centre (NCSC) said it's notifying around 26,000 users who have been infected with
    [Lumma Stealer](https://thehackernews.com/2025/07/hackers-use-leaked-shellter-tool.html)
    , in what it described as the first large-scale public outreach. "The malicious software is designed to steal sensitive information, like email addresses and passwords, from devices typically for the purposes of fraud or identity theft," it
    [said](https://www.ncsc.govt.nz/news/nz-cyber-agency-alerts-thousands-to-malware-infection/)
    . "The use of Lumma Stealer and other similar malware by cyber criminals is an ongoing international issue."
13. Update closes hijack flaw

    Notepad++ has released version 8.8.9 to fix a critical flaw in the open-source text and source code editor for Windows. This bug, according to security researcher Kevin Beaumont, was being
    [abused](https://doublepulsar.com/small-numbers-of-notepad-users-reporting-security-woes-371d7a3fd2d9)
    by threat actors in China to
    [hijack traffic](https://bsky.app/profile/doublepulsar.com/post/3m7li7hqvks26)
    from WinGUp (the Notepad++ updater), redirect it to malicious servers, and then trick people into downloading malware. "Verify certificate and signature on downloaded update installer," reads the
    [release notes](https://community.notepad-plus-plus.org/topic/27298/notepad-v8-8-9-vulnerability-fix)
    for version 8.8.9. "The review of the reports led to the identification of a weakness in the way the updater validates the integrity and authenticity of the downloaded update file," Notepad++ maintainers
    [said](https://notepad-plus-plus.org/news/v889-released/)
    . "In case an attacker is able to intercept the network traffic between the updater client and the Notepad++ update infrastructure, this weakness can be leveraged by an attacker to prompt the updater to download and execute an unwanted binary (instead of the legitimate Notepad++ update binary)."
14. Telegram tightens cyber controls

    A new report from Kaspersky examining more than 800 blocked Telegram channels that existed between 2021 and 2024 has
    [revealed](https://securelist.com/goodbye-dark-telegram/118286/)
    that the "median lifespan of a shadow Telegram channel increased from five months in 2021-2022 to nine months in 2023-2024" The messaging app also appears to be increasingly blocking cybercrime-focused channels since October 2024, prompting threat actors to migrate to other platforms.
15. UK targets info warfare actors

    The U.K. has imposed new sanctions against several
    [Russian](https://www.gov.uk/government/publications/new-uk-action-against-foreign-information-warfare/new-uk-action-against-foreign-information-warfare)
    and
    [Chinese](https://www.gov.uk/government/news/uk-clamps-down-on-china-based-companies-for-reckless-and-irresponsible-activity-in-cyberspace)
    organizations accused of undermining the West through cyber attacks and influence operations. The actions target two Chinese entities,
    [I-Soon](https://thehackernews.com/2025/12/chinese-hackers-have-started-exploiting.html)
    and the
    [Integrity Technology Group](https://thehackernews.com/2025/10/chinese-hackers-exploit-arcgis-server.html)
    (aka Flax Typhoon), as well as a Telegram channel Ryber and its co-owner, Mikhail Zvinchuk, an organization called
    [Pravfond](https://www.lrt.lt/en/news-in-english/19/2570212/leaked-files-reveal-lawyers-politicians-in-lithuania-on-kremlin-s-payroll-investigation)
    that's believed to be a front for the GRU, and the Centre for Geopolitical Expertise, a Moscow-based think tank founded by Aleksandr Dugin. "I-Soon and Integrity Tech are examples of the threat posed by the cyber industry in China, which includes information security companies, data brokers (that collect and sell personal data), and 'hackers for hire,'" the U.K. government said. "Some of these companies provide cyber services to the Chinese intelligence services."
16. Millions still using Log4Shell

    A new analysis from Sonatype has revealed that about 13% of all Log4j downloads in 2025 are susceptible to Log4Shell. "In 2025 alone, there were nearly 300 million total Log4j downloads," the supply chain security company
    [said](https://www.sonatype.com/whitepapers/the-persistence-of-open-source-vulnerabilities)
    . "Of those, about 13% – roughly 40 million downloads — were still vulnerable versions. Given that safe alternatives have been available for nearly four years, every one of those vulnerable downloads represents risk that could have been avoided." China, the United States, India, Japan, Brazil, Germany, the United Kingdom, Canada, South Korea, and France accounted for a huge chunk of the vulnerable downloads.
17. India weighs constant tracking

    The Indian government is reportedly reviewing a telecom industry proposal to force smartphone firms to enable satellite location tracking that is always activated for better surveillance, with no option for users to disable it, Reuters
    [revealed](https://www.reuters.com/sustainability/boards-policy-regulation/india-weighs-greater-phone-location-surveillance-apple-google-samsung-protest-2025-12-05/)
    . The idea is to get precise locations when legal requests are made to telecom firms during investigations, the news agency added. The move has been opposed by Apple, Google, and Samsung. Amnesty International has
    [called](https://www.reuters.com/sustainability/society-equity/amnesty-says-indias-review-location-tracking-plan-deeply-concerning-2025-12-08/)
    the plan "deeply concerning."
18. GlobalProtect scans spike

    A "concentrated spike" comprising more than 7,000 IP addresses has been observed attempting to log into Palo Alto Networks GlobalProtect portals. The activity, which originated from infrastructure operated by 3xK GmbH, was observed on December 2, 2025. GreyNoise
    [said](https://www.greynoise.io/blog/hidden-pattern-credential-based-attacks-palo-alto-sonicwall)
    the December wave shares three identical client fingerprints with a
    [prior wave](https://thehackernews.com/2025/10/scanning-activity-on-palo-alto-networks.html)
    observed between late September and mid-October. The threat intelligence firm said it also recorded a surge in scanning against SonicWall SonicOS API endpoints a day later. Both the attack waves have been attributed to the same threat actor.
19. OpenAI warns of AI misuse

    Artificial intelligence (AI) company OpenAI said there is a need for strengthening resilience as cyber capabilities in AI models advance rapidly, posing dual-use risks. To that end, the firm said it's investing in safeguards to help ensure these capabilities mainly benefit defensive uses and limit their use for malicious purposes. This includes: (1) Training the model to refuse or safely respond to harmful requests, (2) Maintaining system-wide monitoring across products that use frontier models to detect malicious cyber activity, and (3) End-to-end red teaming. "As these capabilities advance, OpenAI is investing in strengthening our models for defensive cybersecurity tasks and creating tools that enable defenders to more easily perform workflows such as auditing code and patching vulnerabilities," the company
    [said](https://openai.com/index/strengthening-cyber-resilience/)
    . "Our goal is for our models and products to bring significant advantages for defenders, who are often outnumbered and under-resourced."
20. Android malware fakes ransomware

    Spanish Android users have become the target of a new malware called DroidLock that propagates via dropper apps hosted on phishing websites. "It has the ability to lock device screens with a ransomware-like overlay and illegally acquire app lock credentials, leading to a total takeover of the compromised device," Zimperium
    [said](https://zimperium.com/blog/total-takeover-droidlock-hijacks-your-device)
    . "It employs deceptive system update screens to trick victims and can stream and remotely control devices via VNC. The malware also exploits device administrator privileges to lock or erase data, capture the victim's image with the front camera, and silence the device." In all, it supports 15 distinct commands. While the malware does not actually have the ability to encrypt files, it displays a scary overlay that instructs victims to contact a Proton email address within 24 hours or risk getting their files destroyed. Like other Android malware of its kind, it leverages accessibility services to carry out its malicious activities, including changing the device lock screen PIN or password, effectively locking users out. It also serves traditional WebView overlays atop targeting apps to capture credentials.
21. Google tightens HTTPS validation

    Google has announced that the Chrome Root Program and the CA/Browser Forum have taken steps to sunset 11 legacy methods for Domain Control Validation, a security-critical process designed to ensure certificates are only issued to the legitimate domain operator. "By retiring these outdated practices, which rely on weaker verification signals like physical mail, phone calls, or emails, we are closing potential loopholes for attackers and pushing the ecosystem toward automated, cryptographically verifiable security," the company
    [said](https://security.googleblog.com/2025/12/https-certificate-industry-phasing-out.html)
    . The deprecation is expected to be carried out in phases and completed by March 2028.
22. Torrent hides Agent Tesla

    Cybersecurity researchers have warned of a new campaign that uses a fake torrent for the Leonardo DiCaprio starrer One Battle After Another as a launchpad for a complex infection chain that drops
    [Agent Tesla](https://thehackernews.com/2025/08/hackers-using-new-quirkyloader-malware.html)
    malware. "Instead of the expected video file, users unknowingly download a compilation of PowerShell scripts and image archives that build into a memory-resident command-and-control (C2) agent, also known as a trojan (RAT – Remote Access Trojan) under the name of Agent Tesla," Bitdefender
    [said](https://www.bitdefender.com/en-us/blog/labs/fake-leonardo-dicaprio-movie-torrent-agent-tesla-powershell)
    . "This type of malware is designed with a single purpose: to provide attackers with unfettered access to the victim's Windows computer." The attack is part of a growing trend of embedding malware in bogus multimedia files. Earlier this May, a lure for Mission: Impossible – The Final Reckoning was used to
    [spread](https://www.bitdefender.com/en-us/blog/hotforsecurity/fake-mission-impossible-lumma-stealer-torrent)
    Lumma Stealer.
23. Leaked secrets flood Docker Hub

    A new study from Flare has found that more than 10,000 Docker Hub container images are exposing credentials to production systems, CI/CD databases, or large language model (LLM) keys. "42% of exposed images contained five or more secrets each, meaning a single container could unlock an entire cloud environment, CI/CD pipeline, and database," the company
    [said](https://flare.io/learn/resources/docker-hub-secrets-exposed/)
    . "AI LLM model keys were the most frequently leaked credentials, with almost 4,000 exposed, revealing how fast AI adoption has outpaced security controls." The exposure represents severe risks, as it enables full access to cloud environments, Git repositories, CI/CD systems, payment integrations, and other core infrastructure components.
24. VS Code trojans disguised as PNGs

    As many as 19 Microsoft Visual Studio Code (VS Code) extensions have been identified on the official Marketplace, with most of them embedding a malicious file that masquerades as a PNG image. The campaign, active since February 2025, was discovered last week. "The malicious files abused a legitimate npm package [path-is-absolute] to avoid detection and crafted an archive containing malicious binaries that posed as an image: A file with a PNG extension," ReversingLabs researcher Petar Kirhmajer
    [said](https://www.reversinglabs.com/blog/malicious-vs-code-fake-image)
    . "For this latest campaign, the threat actor modified it by adding a few malicious files. However, it's important to note that these changes to the package are only available when it is installed locally through the 19 malicious extensions, and they are not actually part of the package hosted on npm." The net effect is that the weaponized package is used to launch the attack as soon as one of the malicious extensions is used and VS Code is launched. The main purpose of the malicious code is to decode what appears to be a PNG file ("banner.png"), but, in reality, is an archive containing two binaries that are executed using the "cmstp.exe" living-off-the-land binary (LOLBin) by means of a JavaScript dropper. "One of these binaries is responsible for closing the LOLBin by emulating a key press, while the other binary is a more complicated Rust trojan," ReversingLabs said. The extensions have since been removed by Microsoft from the Marketplace.
25. ValleyRAT builder dissected

    Check Point Research said it was able to reverse engineer the ValleyRAT (aka Winos or Winos4.0) backdoor and its plugins by examining a publicly leaked builder and its development structure. "The analysis reveals the advanced skills of the developers behind ValleyRAT, demonstrating deep knowledge of Windows kernel and user-mode internals, and consistent coding patterns suggesting a small, specialized team," the cybersecurity company
    [said](https://research.checkpoint.com/2025/cracking-valleyrat-from-builder-secrets-to-kernel-rootkits/)
    . "The 'Driver Plugin' contains an embedded kernel-mode rootkit that, in some cases, retains valid signatures and remains loadable on fully updated Windows 11 systems, bypassing built-in protection features." Specifically, the plugin facilitates stealthy driver installation, user-mode shellcode injection via APCs, and forceful deletion of AV/EDR drivers. The rootkit is based on the publicly available open-source project Hidden. One of the other plugins is a login module that is designed to load additional components from an external server. ValleyRAT is attributed to a Chinese cybercrime group known as
    [Silver Fox](https://thehackernews.com/2025/12/silver-fox-uses-fake-microsoft-teams.html)
    . Approximately 6,000 ValleyRAT-related samples have been detected in the wild between November 2024 and November 2025, in addition to 30 distinct variants of the ValleyRAT builder and 12 variants of the rootkit driver.
26. AI chat guides spread stealers

    In a
    [new campaign](https://www.kroll.com/en/publications/cyber/new-amos-infection-vector-highlights-risks-around-ai-adoption)
    , threat actors are abusing the ability to share chats on OpenAI ChatGPT and Grok to surface them in search results, either via malvertising or search engine optimization (SEO) poisoning, to trick users into installing stealers like AMOS Stealer when searching for "sound not working on macOS," "clear disk space on macOS," or ChatGPT Atlas on search engines like Google. The
    [chat sessions](https://www.kaspersky.com/blog/share-chatgpt-chat-clickfix-macos-amos-infostealer/54928/)
    are shared under the guise of troubleshooting or installation guides and include ClickFix-style instructions to launch the terminal and paste a command to address issues faced by the user. "Attackers are systematically weaponizing multiple AI platforms with SEO poisoning, and that it is not isolated to a single AI platform, page, or query, ensuring victims encounter poisoned instructions regardless of which tool they trust," Huntress
    [said](https://www.huntress.com/blog/amos-stealer-chatgpt-grok-ai-trust)
    . "Instead, multiple AI-style conversations are being surfaced organically through standard search terms, each pointing victims toward the same multi-stage macOS stealer." The development comes as platforms like itch.io and Patreon are being used by threat actors to distribute Lumma Stealer. "Newly created Itch.io accounts spam comments in different legitimate games, with templated text messages that show Patreon links to supposed game updates," G DATA
    [said](https://www.gdatasoftware.com/blog/2025/12/38310-lumma-stealer-itchio-patreon)
    . These links direct to ZIP archives containing a malicious executable that's compiled with
    [nexe](https://github.com/nexe/nexe)
    and runs a six-levels of anti-analysis checks before dropping the stealer malware.

Cybersecurity isn't just a tech issue anymore—it's part of daily life. The same tools that make work and communication easier are the ones attackers now use to slip in unnoticed. Every alert, patch, or policy shift connects to a bigger story about how fragile digital trust has become.

As threats keep evolving, staying aware is the only real defense. The
**Threatsday Bulletin**
exists for that reason—to cut through the noise and show what actually matters in cybersecurity right now. Read on for this week's full rundown of breaches, discoveries, and decisions shaping the digital world.