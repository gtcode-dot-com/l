---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-16T14:15:15.460932+00:00'
exported_at: '2026-04-16T14:15:18.333590+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html
structured_data:
  about: []
  author: ''
  description: This week's biggest hacks, zero-days, supply chain attacks, crypto
    theft, ransomware hits, and critical patches — all in one place.
  headline: 'ThreatsDay Bulletin: Defender 0-Day, SonicWall Brute-Force, 17-Year-Old
    Excel RCE and 15 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/threatsday-bulletin-17-year-old-excel.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: Defender 0-Day, SonicWall Brute-Force, 17-Year-Old Excel
  RCE and 15 More Stories'
updated_at: '2026-04-16T14:15:15.460932+00:00'
url_hash: 5020d062d99c9fd39d821d50b9944a598c5f43e7
---

**

Ravie Lakshmanan
**

Apr 16, 2026

Hacking News / Cybersecurity News

You know that feeling when you open your feed on a Thursday morning and it's just... a lot? Yeah. This week delivered. We've got hackers getting creative in ways that are almost impressive if you ignore the whole "crime" part, ancient vulnerabilities somehow still ruining people's days, and enough supply chain drama to fill a season of television nobody asked for.

Not all bad though. Some threat actors got exposed with receipts, a few platforms finally tightened things up, and there's research in here that's genuinely worth your time. Grab your coffee and keep scrolling.

1. Targeted wallet breach

   Cryptocurrency wallet service Zerion has
   [disclosed](https://x.com/zerion/status/2044167535231414727)
   that one of its team member's devices was compromised, resulting in the theft of approximately $100K in stolen funds from internal company hot wallets. The company noted that user funds, Zerion apps, or infrastructure were not impacted by the breach. The team member is said to have been the target of an artificial intelligence (AI)-enabled social engineering attack carried by a North Korean threat actor tracked as
   [UNC1069](https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html)
   . The hacking group was recently attributed to the poisoning of the popular Axios npm package. "This allowed the attacker to gain access to some of the team members' logged-in sessions and credentials as well as private keys to company hot wallets used for testing and internal purposes," Zerion said. "This was not an opportunistic attack. The actor is clearly sophisticated and well-resourced. They planned the attack thoroughly."
2. Anonymous age checks

   The European Union has announced that it will soon roll out a new online age verification app to allow users to prove their age when accessing online platforms. Users can set it up by downloading the app on their Android or iOS device using a passport or ID card. The Commission has emphasized that the app will respect users' privacy. "Users will prove their age without revealing any other personal information," President of the European Commission, Ursula von der Leyen,
   [said](https://ec.europa.eu/commission/presscorner/detail/en/statement_26_817)
   . "Put simply, it is completely anonymous: users cannot be tracked. Third, the app works on any device – phone, tablet, computer, you name it. And, finally, it is fully open source – everyone can check the code." The development comes as countries around the world are undertaking various stages of regulatory action to keep cyberspace a safer place for children and minors and protect them from serious harm.
3. New Defender zero-day

   A researcher using the alias "Chaotic Eclipse" released a zero-day exploit called
   [BlueHammer](https://thehackernews.com/2026/04/microsoft-issues-patches-for-sharepoint.html)
   earlier this month following Microsoft's handling of the vulnerability disclosure process. Although the issue appears to have been fixed as of this month's Patch Tuesday release (CVE-2026-33825), the researcher has since
   [disclosed](https://x.com/ChaoticEclipse0/status/2044550275692642782)
   a new unpatched
   [Microsoft Defender privilege escalation vulnerability](https://deadeclipse666.blogspot.com/2026/04/public-disclosure-response-for-cve-2026.html)
   . The exploit has been codenamed
   [RedSun](https://github.com/Nightmare-Eclipse/RedSun)
   . "This works 100% reliably to go from unprivileged user to SYSTEM against Windows 11 and Windows Server with April 2026 updates, as well as Windows 10, as long as you have Windows Defender enabled," security researcher Will Dormann
   [said](https://infosec.exchange/@wdormann/116412019416916182)
   .
4. Legacy Excel RCE active

   The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has
   [added](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog)
   an old remote code execution vulnerability impacting Microsoft Office to its Known Exploited Vulnerabilities (KEV) catalog, requiring Federal Civilian Executive Branch (FCEB) agencies to remediate the shortcoming by April 28, 2026. The vulnerability in question is CVE-2009-0238, which has a CVSS score of 8.8. "Microsoft Office Excel contains a remote code execution vulnerability that could allow an attacker to take complete control of an affected system if a user opens a specially crafted Excel file that includes a malformed object," CISA
   [said](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
   .
5. sudo now requires password

   Raspberry Pi has released version 6.2 of its Raspberry Pi OS, which introduces one significant change: it disables passwordless sudo by default. As a result, users who run a sudo command for administrator-level access will be prompted to enter the current user's password. The change affects only new installations; existing setups are untouched. "Given the ever-increasing threat of cybercrime, we continually review the security of Raspberry Pi OS to ensure it is sufficiently robust to withstand potential attacks," Raspberry Pi
   [said](https://www.raspberrypi.com/news/a-security-update-for-raspberry-pi-os/)
   . "This is always a tricky balance, as anything that makes the operating system more secure will invariably inconvenience legitimate users to some extent, so we try to keep such changes to a minimum. This particular security update is one that many users may not even notice, but it will affect some."
6. Stealth C2 frameworks uncovered

   A previously undocumented command-and-control (C2) framework dubbed ObsidianStrike has been deployed on infrastructure belonging to a Brazilian law firm. "Only two instances of ObsidianStrike exist on the entire internet," Breakglass Intelligence
   [said](https://intel.breakglass.tech/post/obsidianstrike-c2-compromised-brazilian-law-firm-9-months)
   . "The framework has zero presence on GitHub, zero samples on VirusTotal or MalwareBazaar, and near-zero vendor detection. This is a fully private, Portuguese-language C2 built for targeted Windows operations, hidden behind a victim organization's domain." Also discovered by the security vendor is
   [ArchangelC2](https://intel.breakglass.tech/post/archangelc2-innocreed-screenconnect-fraud)
   , a C2 panel behind an industrial-scale ScreenConnect remote-access fraud campaign that has been operational since November 2024.
7. Fake app drains $9.5M

   A fake Ledger app
   [managed](https://www.coindesk.com/business/2026/04/14/a-fake-ledger-app-on-the-apple-app-store-just-drained-usd9-5-million-in-crypto)
   to slip onto the Apple App Store,
   [draining $9.5 million in cryptocurrency](https://t.me/investigations/313)
   from more than 50 victims between April 7 and April 13, 2026. The app, named
   [Ledger Live](https://archive.ph/4RVLf)
   , was released by a developer, "SAS Software Company," and published under "Leva Heal Limited." Users who downloaded the fraudulent app were tricked into entering their seed phrases, giving attackers full access to their wallets and allowing them to send digital assets to external addresses under their control. While Apple has since removed the macOS app from the store, questions remain as to how it managed to pass the company's review process. In more Apple-related news, the company has also
   [removed](https://techcrunch.com/2026/04/14/how-the-rewards-app-freecash-scammed-its-way-to-the-top-of-the-app-stores/)
   a data harvesting app called Freecash from its App Store after it was
   [deceptively](https://www.wired.com/story/no-the-freecash-app-wont-pay-you-to-scroll-tiktok/)
   [advertised](https://www.malwarebytes.com/blog/news/2026/01/get-paid-to-scroll-tiktok-the-data-trade-behind-freecash-ads)
   as a way to "make money just by scrolling TikTok," while collecting sensitive information from users. This included details about a user's race, religion, sex life, sexual orientation, health, and other biometrics. Once installed, however, instead of the promised functionality, users were routed to a roster of mobile games where they are offered cash rewards for completing time-limited in-game challenges. The app continues to be available on the Google Play Store.
8. Localized ransomware campaign

   Cybercriminals are using a new ransomware strain called JanaWare to target people in Turkey, according to Acronis. The attack leverages phishing emails containing a Google Drive link that paves the way for the download and subsequent execution of a malicious JAR file via javaw.exe. The payload is a customized
   [Adwind](https://thehackernews.com/2024/06/warning-new-adware-campaign-targets.html)
   (aka AlienSpy, jRAT, or Sockrat) variant with polymorphic characteristics that's used to deliver the ransomware module. The malware implements geofencing and environment filtering to ensure that the compromised systems match the Turkish language and region. While none of these tricks are particularly novel or advanced, they continue to work against unprotected small targets. It's unclear how many people or businesses might have fallen prey to the scheme. The low-stakes, localized approach has allowed the campaign to persist since at least 2020 without any major disruption. "Victimology appears to primarily include home users and small to medium-sized businesses. Initial access is assessed to occur via phishing emails delivering malicious Java archives," the company
   [said](https://www.acronis.com/en/tru/posts/new-janaware-ransomware-targets-turkey-via-adwind-rat/)
   . "Ransom demands observed in analyzed samples range from $200–$400, consistent with a low-value, high-volume monetization approach."
9. Crackdown on navigation abuse

   Google said it's introducing a new spam policy for "back button hijacking," which occurs when a site interferes with a user's browser navigation and prevents them from using their back button to immediately get back to the page they came from. Instead, the hijack could redirect users to sketchy sites or other pages they have never visited before. "Back button hijacking interferes with the browser's functionality, breaks the expected user journey, and results in user frustration," Google
   [said](https://developers.google.com/search/blog/2026/04/back-button-hijacking)
   . "Pages that are engaging in back button hijacking may be subject to manual spam actions or automated demotions, which can impact the site's performance in Google Search results. To give site owners time to make any needed changes, we're publishing this policy two months in advance of enforcement on June 15, 2026."
10. Stealth cloud credential theft

    The China-linked hacking group known as
    [APT41](https://thehackernews.com/2025/09/china-linked-apt41-hackers-target-us.html)
    has been attributed to an undetectable, purpose-built ELF backdoor targeting Linux cloud workloads across Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Alibaba Cloud environments. "The implant uses SMTP port 25 as a covert command-and-control channel, harvests cloud provider credentials and metadata, and phones home to three Alibaba-themed typosquat domains hosted on Alibaba Cloud infrastructure in Singapore," Breakglass Intelligence
    [said](https://intel.breakglass.tech/post/apt41-winnti-elf-cloud-credential-harvester-alibaba-typosquat)
    . "A selective C2 handshake validation mechanism renders the server invisible to conventional scanning tools like Shodan and Censys."
11. RDP phishing hardening

    Starting with the April 2026 security update (
    [CVE-2026-26151](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-26151)
    ), Microsoft has introduced new Windows protections to defend against phishing attacks that abuse Remote Desktop connection (RDP) files, adding security warnings and turning off redirections by default. "Malicious actors misuse this capability by sending RDP files through phishing emails," Microsoft
    [said](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/remotepc/understanding-security-warnings)
    . "When a victim opens the file, their device silently connects to a server controlled by the attacker and shares local resources, giving the attacker access to files, credentials, and more." Russian hacking groups like APT29 have
    [weaponized](https://thehackernews.com/2024/12/apt29-hackers-target-high-value-victims.html)
    RDP configuration files to target Ukrainian government agencies, enterprises, and military entities in the past.
12. Plugin supply chain breach

    Unknown threat actors have staged a supply chain attack on a WordPress plug-in maker called Essential Plugin (formerly WP Online Support) after acquiring it in early 2025 from the original developers in a six-figure deal to plant a backdoor in August and subsequently weaponize it early this month to distribute malicious payloads to any website with the plug-ins installed. WordPress has since permanently closed all the plugins. "The plugin's wpos-analytics module had phoned home to analytics.essentialplugin.com, downloaded a backdoor file called wp-comments-posts.php (designed to look like the core file wp-comments-post.php), and used it to inject a massive block of PHP into wp-config.php," Anchor Hosting
    [said](https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/)
    . "The injected code was sophisticated. It fetched spam links, redirects, and fake pages from a command-and-control server. It only showed the spam to Googlebot, making it invisible to site owners." In addition, it resolved the command-and-control (C2) domain through an Ethereum smart contract to make it resilient to takedown efforts. Prior to their removal, the plugins collectively had more than 180,000 installs. "This is a classical case of supply chain compromise that happened because the original vendor sold their plugins to a third-party, which turned out to be a malicious threat actor," Patchstack
    [said](https://patchstack.com/articles/critical-supply-chain-compromise-on-20-plugins-by-essentialplugin/)
    .
13. Sanctioned crypto market persists

    Telegram has continued to host Xinbi Guarantee, an illicit marketplace that has
    [processed](https://thehackernews.com/2026/02/weekly-recap-ai-skill-malware-31tbps.html#:~:text=Xinbi%20Marketplace%20Accounts%20for%20%2417%2E9B%20in%20Total%20Volume)
    over $21 billion in total transaction volume, despite sanctions
    [issued](https://thehackernews.com/2026/03/weekly-recap-telecom-sleeper-cells-llm.html#:~:text=U%2EK%2E%20Sanctions%20Xinbi)
    by the U.K. last month. The development has raised questions about the platform's willingness to police its own ecosystem and suspend bad actors. The Chinese-language bazaar is
    [known to offer](https://thehackernews.com/2025/05/xinbi-telegram-market-tied-to-84b-in.html)
    money laundering solutions to cryptocurrency scammers, harassment services, and products like electrified batons and tasers that cater to investment scams operating out of Southeast Asia. "Xinbi is still going strong," Elliptic's cofounder and chief scientist, Tom Robinson,
    [told](https://www.wired.com/story/telegram-is-still-hosting-a-sanctioned-21-billion-crypto-scammer-black-market/)
    WIRED. "They're on track to become the largest market of this kind that has ever existed."
14. Malvertising leads to ransomware

    Orange Cyberdefense has
    [revealed](https://www.orangecyberdefense.com/global/blog/cert-news/smoking-out-an-affiliate-smokedham-qilin-a-few-google-ads-and-some-bossware)
    that threat actors used malvertising in three separate incidents observed between early February and early April 2026 to deliver the SmokedHam (aka Parcel RAT, SharpRhino, and WorkersDevBackdoor) backdoor by masquerading it as installers for RVTools or Remote Desktop Manager (RDM). The malware is assessed to be a modified version of the open-source trojan known as ThunderShell. In at least one case, the attack led to the deployment of Qilin ransomware, but not before dropping employee monitoring and remote desktop solutions like Controlio, TeraMind, and Zoho Assist for persistent access, exfiltrating KeePass password databases, and conducting discovery and lateral movement. The adoption of
    [legitimate dual-use tools](https://censys.com/blog/netsupport-manager-tracking-dual-use-remote-administration-infrastructure/)
    is a concerning trend as it allows attackers to blend their actions into legitimate activity and reduce the risk of detection. The activity has been attributed with medium confidence to
    [UNC2465](https://thehackernews.com/2021/05/colonial-pipeline-paid-nearly-5-million.html)
    , an affiliate of DarkSide, LockBit, and Hunters International. It also overlaps with a campaign detailed by
    [Synacktiv](https://www.synacktiv.com/en/publications/case-study-how-hunters-international-and-friends-target-your-hypervisors)
    and
    [Field Effect](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)
    in early 2025.
15. APT lineage link uncovered

    New research has discovered that the threat actor known as
    [Water Hydra](https://thehackernews.com/2024/02/darkme-malware-targets-traders-using.html)
    (aka DarkCasino) is still active in 2026, with new evidence uncovering a previously unreported connection between evilgrou-tech, a commodity operator, and the hacking group. "The handle 'evilgrou' is assessed with moderate confidence to be a deliberate reference to
    [EvilNum](https://thehackernews.com/2023/08/winrar-security-flaw-exploited-in-zero.html)
    (Evil + [num -> grou]p), the predecessor APT group from which WaterHydra/DarkCasino splintered in late 2022," Breakglass Intelligence
    [said](https://intel.breakglass.tech/post/multi-rat-operation-dismantled-waterhydra-apt-nexus-five-aes-keys-recovered-and-live-c2-infrastructure-mapped-across-three-continents)
    . The strongest attribution indicator is a shared developer workspace path embedded in binaries associated with EvilNum and Water Hydra: "C:\Users\Administrator\Desktop\vaeeva\shellrundll.tlb." These two artifacts are separated by two years, one in July 2022 and the other in January 2024.
16. Scientific software RCE risk

    Cybersecurity researchers have
    [disclosed](https://www.threatleap.com/publications/Finding-Critical-Security-Vulnerabilities-In-Widely-Used-Research-And-Scientific-Software-For-Fun-Not-Profit-HDF5-Story)
    security flaws in HDF5 software, a file format to manage, process, and store heterogeneous data, that could be exploited to compromise a vulnerable system. "The discovered vulnerabilities, based on a stack buffer overflow, could allow threat actors to overwrite memory and compromise target systems for stealing highly classified research data, industrial espionage, or a foothold into the internal network," ThreatLeap's co-founder, Leon Juranic, said. "In practice, this means the vulnerability could be exploited by a single specially crafted malicious input file and, as a result, an entire system could get compromised." The issues were addressed in October 2025 following responsible disclosure.
17. Brute-force surge on edge devices

    Security researchers have detected a "sharp rise" in brute-force attempts to hijack SonicWall and FortiGate devices between January and March 2026, with the vast majority (88%) appearing to originate from the Middle East. Most attempts were unsuccessful, either blocked outright by security tools or directed at invalid usernames. "Attackers are aggressively scanning and testing perimeter devices for weak or exposed credentials," Barracuda Networks
    [said](https://blog.barracuda.com/2026/04/14/soc-threat-radar-april-2026)
    . "Even when attacks fail, persistent probing raises the risk that a single weak password or misconfiguration could lead to compromise."
18. Fraud network evades sanctions

    Triad Nexus, a sprawling cybercrime ecosystem acting as the backbone of scams, money laundering, and illicit gambling operations since at least 2020, has been observed using geographic fencing and laundering its infrastructure through "clean" front companies to acquire accounts at major enterprise cloud providers (Amazon, Cloudflare, Google, and Microsoft) and
    [avoid sanctions](https://thehackernews.com/2025/05/us-sanctions-funnull-for-200m-romance.html)
    . Besides engaging in fraud, the group specializes in high-fidelity brand impersonation, weaponizing the digital identities of Global 2000 companies to dupe victims. "The network has industrialized brand theft on a global scale; its catalog includes 'pixel-perfect' clones of everything from high-end luxury goods to public services," Silent Push
    [said](https://www.silentpush.com/blog/triad-nexus-funnull-2026/)
    . "Despite federal sanctions in 2025, the group has reinstated its global fraud engine, shifting its focus toward emerging markets while maintaining a persistent threat to Western enterprise assets." Triad Nexus is estimated to be responsible for over $200 million in reported losses, primarily fueled by pig butchering and virtual currency scams.

That's a wrap for this week. If anything here made you pause, good. Go check your patches, side-eye your dependencies, and maybe don't trust that app just because it's sitting in an official store. The basics still matter more than most people want to admit.

We'll be back next Thursday with whatever fresh chaos the internet cooks up. Until then, stay sharp and keep your logs close. See you on the other side.