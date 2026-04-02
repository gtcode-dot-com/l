---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T14:15:15.024305+00:00'
exported_at: '2026-04-02T14:15:17.311120+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html
structured_data:
  about: []
  author: ''
  description: 'Cybersecurity roundup: ShareFile RCE, Android rootkit, ImageMagick
    0-days, XLoader, phishing, and supply chain threats.'
  headline: 'ThreatsDay Bulletin: Pre-Auth Chains, Android Rootkits, CloudTrail Evasion
    & 10 More Stories'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/threatsday-bulletin-pre-auth-chains.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'ThreatsDay Bulletin: Pre-Auth Chains, Android Rootkits, CloudTrail Evasion
  & 10 More Stories'
updated_at: '2026-04-02T14:15:15.024305+00:00'
url_hash: 442d059e5c80be9dea86ab515e0e8ae0713f4d2a
---

**

Ravie Lakshmanan
**

Apr 02, 2026

Cybersecurity / Hacking News

The latest ThreatsDay Bulletin is basically a cheat sheet for everything breaking on the internet right now. No corporate fluff or boring lectures here, just a quick and honest look at the messy reality of keeping systems safe this week.

Things are moving fast. The list includes researchers chaining small bugs together to create massive backdoors, old software flaws coming back to haunt us, and some very clever new tricks that let attackers bypass security logs entirely without leaving a trace. We are also seeing sketchier traffic on the underground and the usual supply chain mess, where one bad piece of code threatens thousands of apps.

It is definitely worth a quick scan before you log off for the day, if only to make sure none of this is sitting in your own network. Let's get into it.

1. Pre-auth RCE chain exposed

   watchTower Labs has
   [disclosed](https://labs.watchtowr.com/youre-not-supposed-to-sharefile-with-everyone-progress-sharefile-pre-auth-rce-chain-cve-2026-2699-cve-2026-2701/)
   two security flaws in Progress ShareFile (CVE-2026-2699 and CVE-2026-2701) that could be chained to achieve pre-authenticated remote code execution. While CVE-2026-2699 is an authentication bypass via the "/ConfigService/Admin.aspx" endpoint, CVE-2026-2701 refers to a case of post-authenticated remote code execution. An attacker could combine the two vulnerabilities to sidestep authentication and upload web shells. Progress released fixes for the vulnerabilities with Storage Zone Controller 5.12.4 released on March 10, 2026. There are about 30,000 internet-facing instances, making patching against the flaws crucial.
2. Rootkit spreads via 50+ apps

   A new Android malware named NoVoice has been distributed via more than 50 apps that were downloaded at least 2.3 million times. While apps masqueraded as utilities, image galleries, and games, and offered the advertised functionality, the malware attempted to obtain root access on the device by exploiting 22 Android vulnerabilities that received patches between 2016 and 2021. "If the exploits succeed, the malware gains full control of the device," McAfee Labs
   [said](https://www.mcafee.com/blogs/other-blogs/mcafee-labs/new-research-operation-novoice-rootkit-malware-android/)
   . "From that moment onward, every app that the user opens is injected with attacker-controlled code. This allows the operators to access any app data and exfiltrate it to their servers." The malware avoids infecting devices in certain regions, like Beijing and Shenzhen in China, and implements more than a dozen checks for emulators, debuggers, and VPNs. It then contacts a remote server to send device information and fetch appropriate exploits to gain root access and disable SELinux. Upon gaining elevated access, the rootkit modifies system libraries to facilitate the execution of malicious code when specific apps are opened, install arbitrary apps, and enable persistence. NoVoice has been found to share some level of overlap with
   [Triada](https://thehackernews.com/2025/04/triada-malware-preloaded-on-counterfeit.html)
   . One of the targeted apps is WhatsApp, which enabled the malware to harvest data from the app as soon as it was launched. Google has since removed the apps. The highest concentration of infections has been reported in Nigeria, Ethiopia, Algeria, India, and Kenya.
3. FBI flags foreign app risks

   The U.S. Federal Bureau of Investigation (FBI) is warning of the data security risks associated with foreign-developed mobile applications. "As of early 2026, many of the most downloaded and top-grossing apps in the United States are developed and maintained by foreign companies, particularly those based in China," the FBI
   [said](https://www.ic3.gov/PSA/2026/PSA260331)
   . "The apps that maintain digital infrastructure in China are subject to China's extensive national security laws, enabling the Chinese government to potentially access mobile app users' data." The bureau also warned that these apps may harvest contact information under the pretext of inviting friends to use them, store personal data in Chinese servers, or contain malware that could collect data beyond what is authorized by the user. "This could include malicious code and hard-to-remove malware designed to exploit known vulnerabilities in various operating systems and insert a backdoor for escalated privileges, such as enabling the download and execution of additional malicious packages designed to provide unauthorized access to users' data," it added. The FBI did not name the apps, but TikTok, Shein, Temu, and DeepSeek fit the profile.
4. New bureau targets cyber threats

   The U.S. State Department has officially launched the
   [Bureau of Emerging Threats](https://www.state.gov/bureaus-offices/under-secretary-for-arms-control-and-international-security-affairs/bureau-of-emerging-threats/)
   , a new unit
   [tasked](https://abcnews.com/Politics/state-department-launches-effort-counter-cyberattacks-ai-risks/story?id=131265350)
   with protecting U.S. national security against cyber attacks against critical infrastructure, threats in the space domain, and misuse of artificial intelligence (AI) and other advanced technology risks from Iran, China, Russia, and North Korea.
5. Cybercrime kingpin extradited

   Li Xiong, the former chairman of a Cambodian financial conglomerate,
   [HuiOne](https://www.bloomberg.com/news/features/2025-08-01/huione-s-24-billion-hub-for-cybercrime-is-an-amazon-for-criminals)
   , has been extradited to China. He has been accused of operating gambling dens, fraud, unlawful business operations, and money laundering. According to
   [Xinhua](https://english.news.cn/20260401/ae7ef0da373145ceaaeb35170d1c9c2c/c.html)
   , Li is said to be a key member of the transnational cybercrime syndicate masterminded by
   [Chen Zhi](https://thehackernews.com/2026/03/weekly-recap-telecom-sleeper-cells-llm.html#:~:text=U%2EK%2E%20Sanctions%20Xinbi)
   , the chairman of Prince Group, who was
   [extradited](https://english.news.cn/20260108/cc5f710c876b4c8dbc4216a0b300d726/c.html)
   to China in January 2026 and has been
   [indicted](https://thehackernews.com/2026/01/tudou-guarantee-marketplace-halts.html)
   by the U.S. for operating large-scale, forced-labor "pig butchering" scam compounds in Southeast Asia. In May 2025, the U.S. Treasury's Financial Crimes Enforcement Network labeled Huione Group "a financial institution of primary money laundering concern."
6. Gmail username change arrives

   Google
   [said](https://blog.google/products-and-platforms/products/workspace/google-account-username-change/)
   it's rolling out the ability to change a username to Google Account users in the U.S. "Your previous Google Account email ending in gmail.com will become an alternate email address," Google
   [said](https://support.google.com/accounts/answer/19870)
   in a support document. "You'll receive emails to both your old and new addresses. The data saved in your account won’t be affected. This includes things like photos, messages, and emails sent to your previous email address." While users can change back to their previous email address at any time, it's not possible to create a new Google Account email ending in gmail.com for the next 12 months. The new email address cannot be deleted either.
7. Court halts AI risk label

   A U.S. federal judge has
   [temporarily blocked](https://www.axios.com/2026/03/26/judge-temporarily-blocks-pentagon-ban-anthropic)
   the Trump administration's designation of Anthropic as a
   [supply chain risk](https://thehackernews.com/2026/02/pentagon-designates-anthropic-supply.html)
   . The AI company had argued that the designation was causing immediate and irreparable harm. "Nothing in the governing statute supports the Orwellian notion that an American company may be branded a potential adversary and saboteur of the U.S. for expressing disagreement with the government," District Judge Rita Lin wrote in the ruling.
8. Phishing apps target mobile users

   Cybercriminals have set their sights on Android users through a new phishing scheme that disguises malicious applications as beta-testing opportunities for ChatGPT and Meta advertising tools. In these attacks, what appears to be an invitation to advertising apps turns out to be a carefully planned attempt to steal Facebook credentials and hijack control of user accounts. "These messages push malicious apps delivered through 'firebase-noreply@google.com' via Firebase App Distribution, a legitimate Google service for distributing pre-release apps to testers," LevelBlue
   [said](https://x.com/SpiderLabs/status/2036076835889418406)
   . "Once installed, these apps request Facebook credentials, leading to phishing and account takeover." A similar campaign has leveraged phishing emails impersonating ChatGPT and Gemini to push users into downloading malicious iOS apps from the Apple App Store. "Disguised as business or ad management tools, these apps prompt for Facebook credentials, leading to credential harvesting," the company
   [added](https://x.com/SpiderLabs/status/2029557536488038488)
   .
9. Drive adds ransomware defense

   Google has made ransomware detection and file restoration in Drive generally available after launching the feature in beta in September 2025 to help organizations minimize the impact of malware attacks on personal computers. Ransomware detection pauses file syncing, and file restoration allows users to bulk restore their files to a previous version in Drive. "Compared to when the feature was in beta, we are now able to detect even more types of ransomware encryption and are able to do it faster," Google
   [said](https://workspaceupdates.googleblog.com/2026/03/ransomware-detection-and-file-restoration-for-Google-Drive-now-generally-available.html)
   . "Our latest AI model is detecting 14x more infections, leading to even more comprehensive protection."
10. GhostSocks activity intensifies

    Cybersecurity company Darktrace
    [said](https://www.darktrace.com/blog/phantom-footprints-tracking-ghostsocks-malware)
    it has observed a steady increase in GhostSocks activity across its customer base since late 2025. "In one notable case from December 2025, Darktrace detected
    [GhostSocks](https://thehackernews.com/2025/10/polaredge-targets-cisco-asus-qnap.html)
    operating alongside Lumma Stealer, reinforcing that the partnership between Lumma and GhostSocks remains active despite recent attempts to disrupt Lumma's infrastructure," it said. Originally marketed on the Russian underground forum xss[.]is as a malware-as-a-service (MaaS), GhostSocks enables threat actors to turn compromised devices into residential proxies, leveraging the victim's internet bandwidth to route malicious traffic through it. It utilizes the SOCKS5 proxy protocol, creating a SOCKS5 connection on infected devices. It began to be widely adopted following its partnership with Lumma Stealer in 2024.
11. Open-source malware spikes 14x

    The number of malware advisories across open-source ecosystems has increased 13.6x since January 2024, as threat actors take control of trusted packages to poison the software supply chain. "Of the 1,011 npm ATO [Account takeover] advisories recorded in the OSV database over all time, 930 were filed in 2025, a roughly 12x year-over-year increase representing 92% of all ATOs reported on npm," Endor Labs
    [said](https://www.endorlabs.com/learn/new-research-malware-in-open-source-ecosystems-surges-14x-as-attackers-hijack-trusted-packages)
    . Among the 2025 npm ATO cases, 38.4% of affected packages had more than 1,000 monthly downloads, 18.5% exceeded 10,000, and 11.1% had more than 100,000. Attackers are deliberately targeting packages that are deeply embedded in production systems and automated CI/CD pipelines, maximizing the blast radius of each compromise."
12. XLoader boosts stealth tactics

    An updated version of the XLoader information-stealing malware (version 8.7) has been found to incorporate several changes to the code obfuscation to make automation and analysis more difficult. These include the use of encrypted strings that are decrypted at runtime, encrypted code blocks consisting of functions that are decrypted at runtime, and improved methods to conceal hard-coded values and specific functions, per Zscaler. XLoader also uses a combination of multiple encryption layers with different keys for encrypting network traffic. "XLoader continues to be a highly active information stealer that constantly receives updates," the company
    [said](https://www.zscaler.com/blogs/security-research/latest-xloader-obfuscation-methods-and-network-protocol)
    . "As a result of the malware's multiple encryption layers, decoy C2 servers, and robust code obfuscation, XLoader has been able to remain largely under the radar."
13. ImageMagick zero-days enable RCE

    Cybersecurity researchers have found multiple zero-day vulnerabilities in ImageMagick that could be chained to achieve remote code execution through a single image or PDF upload. According to
    [Pwn.ai](https://pwn.ai/blog/imagemagick-from-arbitrary-file-read-to-rce-in-every-policy-zeroday)
    , the attack works on the default configuration and the most restrictive "secure" configuration. The issue affects every major Linux distribution, as well as WordPress installations that process image uploads. It remains unpatched as of writing. In the interim, it's advised to process PDFs in an isolated sandbox with no network access, disable XML-RPC in WordPress, and block GhostScript.
14. Attackers evade CloudTrail logging

    Adversaries are
    [bypassing](https://www.abstract.security/blog/how-attackers-disable-cloudtrail-without-calling-stoplogging-or-deletetrail)
    traditional CloudTrail detections, like StopLogging or DeleteTrail, and instead using lesser-known AWS APIs to blind logging systems. This includes creating "invisible activity zones” using PutEventSelectors, using StopEventDataStoreIngestion and DeleteEventDataStore to halt or destroy long-term forensic visibility, disabling anomaly detection via PutInsightSelectors, neutralizing cross-account protections through DeleteResourcePolicy and DeregisterOrganizationDelegatedAdmin. "The real risk is in the sequence: individually, these API calls look like routine maintenance—but chained together, they allow attackers to erase evidence and evade detection entirely," Abstract Security said.
15. LofyGang deploys dual-payload RAT

    The threat actor known as
    [LofyGang](https://thehackernews.com/2022/10/lofygang-distributed-200-malicious-npm.html)
    resurfaced with a fake npm package ("undicy-http") that delivers a dual-payload attack: a Node.js-based Remote Access Trojan (RAT) with live screen streaming, and a native Windows PE binary that uses direct syscalls to inject into browser processes and steal credentials, cookies, credit cards, IBANs, and session tokens from more than 50 web browsers and 90 cryptocurrency wallet extensions. The session hijacking module targets Roblox, Instagram, Spotify, TikTok, Steam, Telegram, and Discord. "The Node.js layer independently operates as a full RAT with remote shell, screen capture, webcam/microphone streaming, file upload, and persistence capabilities, all controlled through a WebSocket C2 panel," JFrog
    [said](https://research.jfrog.com/post/lofygang-returns-a-dual-payload-npm-package/)
    . The Node.js layer also downloads a native PE binary to facilitate data exfiltration via a Discord webhook and a Telegram bot.

Nothing here looks huge on its own. That’s the point. Small changes, repeated enough times, start to matter. Things that used to be hard are getting easier. Things that were noisy are getting quiet. You stop seeing the obvious signs and start missing the subtle ones.

Read it like a pattern, not a list. Same ideas showing up in slightly different forms. Systems doing what they’re designed to do—just used differently. That gap is where most problems live now. That’s the recap.