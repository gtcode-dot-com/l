---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-27T16:15:13.051496+00:00'
exported_at: '2026-01-27T16:15:15.289243+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html
structured_data:
  about: []
  author: ''
  description: ClickFix uses fake CAPTCHAs and a signed Microsoft App-V script to
    deploy Amatera stealer on enterprise Windows systems.
  headline: ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted
    Web Services
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/clickfix-attacks-expand-using-fake.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: ClickFix Attacks Expand Using Fake CAPTCHAs, Microsoft Scripts, and Trusted
  Web Services
updated_at: '2026-01-27T16:15:13.051496+00:00'
url_hash: c063206e75b8234f536d1a95f8e7da088c2a202c
---

Cybersecurity researchers have disclosed details of a new campaign that combines
[ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
-style fake CAPTCHAs with a signed Microsoft Application Virtualization (
[App-V](https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/app-v/appv-for-windows)
) script to distribute an information stealer called
[Amatera](https://thehackernews.com/2025/11/new-evalusion-clickfix-campaign.html)
.

"Instead of launching PowerShell directly, the attacker uses this script to control how execution begins and to avoid more common, easily recognized execution paths," Blackpoint researchers Jack Patrick and Sam Decker
[said](https://blackpointcyber.com/blog/novel-fake-captcha-chain-delivering-amatera-stealer/)
in a report published last week.

In doing so, the idea is to transform the App-V script into a living-off-the-land (LotL) binary that proxies the execution of PowerShell through a trusted Microsoft component to conceal the malicious activity.

The starting point of the attack is a fake CAPTCHA verification prompt that seeks to trick users into pasting and executing a malicious command on the Windows Run dialog. But here is where the attack diverges from traditional ClickFix attacks.

The supplied command, rather than invoking PowerShell directly, abuses "
[SyncAppvPublishingServer.vbs](https://lolbas-project.github.io/lolbas/Scripts/Syncappvpublishingserver/)
," a signed Visual Basic Script associated with App-V to retrieve and execute an in-memory loader from an external server using "wscript.exe."

It's worth noting that the misuse of "SyncAppvPublishingServer.vbs" is not new. In 2022, two different threat actors from China and North Korea, tracked as
[DarkHotel](https://thehackernews.com/2022/03/south-korean-darkhotel-hackers-targeted.html)
and
[BlueNoroff](https://thehackernews.com/2022/12/bluenoroff-apt-hackers-using-new-ways.html)
, were observed leveraging the LOLBin exploit to stealthily execute a PowerShell script. But this is the first time it has been observed in ClickFix attacks.

"Adversaries may abuse SyncAppvPublishingServer.vbs to bypass PowerShell execution restrictions and evade defensive counter measures by 'living off the land,'" MITRE
[notes](https://attack.mitre.org/techniques/T1216/002/)
in its ATT&CK framework. "Proxying execution may function as a trusted/signed alternative to directly invoking 'powershell.exe.'"

The use of an App-V script is also significant as the virtualization solution is built only into Enterprise and Education editions of Windows 10 and Windows 11, along with modern Windows Server versions. It's not available for Windows Home or Pro installations.

In Windows operating systems where App-V is either absent or not enabled, the execution of the command fails outright. This also indicates that enterprise managed systems are likely the primary targets of the campaign.

The obfuscated loader runs checks to ensure that it's not run within sandboxed environments, and then proceeds to fetch configuration data from a public Google Calendar (ICS) file, essentially turning a trusted third-party service into a
[dead drop resolver](https://attack.mitre.org/techniques/T1102/001/)
.

"By externalizing configuration in this way, the actor can rapidly rotate infrastructure or adjust delivery parameters without redeploying earlier stages of the chain, reducing operational friction and extending the lifespan of the initial infection vector," the researchers pointed out.

Parsing the calendar event file leads to the retrieval of additional loader stages, including a PowerShell script that functions as an intermediate loader to execute the next stage, another PowerShell script, directly in memory. This step, in turn, results in the retrieval of a PNG image from domains like "gcdnb.pbrd[.]co" and "iili[.]io" via WinINet APIs that conceals an encrypted and compressed PowerShell payload.

The resulting script is decrypted, GZip decompressed in memory, and run using Invoke-Expression, ultimately culminating in the execution of a shellcode loader that's designed to launch Amatera Stealer.

"What makes this campaign interesting isn't any single trick, but how carefully thought-out everything is when chained together," Blackpoint concluded. "Each stage reinforces the last, from requiring manual user interaction, to validating clipboard state, to pulling live configuration from a trusted third-party service."

"The result is an execution flow that only progresses when it unfolds (almost) exactly as the attacker expects, which makes both automated detonation and casual analysis significantly harder."

### The Evolution of ClickFix: JackFix, CrashFix, and GlitchFix

The disclosure comes as ClickFix has become one of the most widely used initial access methods in the last year, accounting for 47% of the attacks observed by Microsoft.

Recent ClickFix campaigns have
[targeted](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2025-12-18-phishing-for-authentication-tokens.txt)
social media content creators by claiming they are eligible for free verified badges, instructing them via videos to copy authentication tokens from their browser cookies into a fake form to complete the supposed verification process. The embedded video also informs the user to "not log out for at least 24 hours" to keep the authentication tokens valid.

The campaign, active since at least September 2025, is estimated to have used 115 web pages across the attack chain and eight exfiltration endpoints,
[per Hunt.io](https://hunt.io/blog/clickfix-facebook-session-hijacking)
. The main targets of the activity include creators, monetized pages, and businesses seeking verification, with the end goal being to facilitate account takeover following token theft.

"Defending against the ClickFix technique is uniquely challenging because the attack chain is built almost entirely on legitimate user actions and the abuse of trusted system tools," Martin Zugec, technical solutions director at Bitdefender,
[said](https://businessinsights.bitdefender.com/how-clickfix-cyberattack-technique-works)
in a report last month. "Unlike traditional malware, ClickFix turns the user into the initial access vector, making the attack look benign from an endpoint defense perspective."

ClickFix is also constantly evolving, utilizing variants like
[JackFix](https://thehackernews.com/2025/11/jackfix-uses-fake-windows-update-pop.html)
and
[CrashFix](https://thehackernews.com/2026/01/crashfix-chrome-extension-delivers.html)
to deceive the victim into infecting their own machines. While operators use several methods to attempt to convince a target to perform command execution, the growing popularity of the social engineering technique has paved the way for
[ClickFix builders](https://thehackernews.com/2025/08/cybercriminals-deploy-cornflakev3.html)
that are advertised on hacker forums for anywhere between $200 to $1,500 per month.

The latest entrant to this threat landscape is
[ErrTraffic](https://thehackernews.com/2026/01/threatsday-bulletin-ghostad-drain-macos.html#fake-glitch-scam-toolkit-exposed)
, a traffic distribution system (TDS) that's specifically designed for ClickFix-like campaigns by causing compromised websites injected with malicious JavaScript to glitch and then suggesting a fix to address the non-existent problem. This technique has been codenamed GlitchFix.

The malware-as-a-service (MaaS) supports three different file distribution modes that involve using fake browser update alerts, fake "system font required" dialogs, and bogus missing system font errors to trigger the execution of malicious commands. ErrTraffic is explicitly blocked from running on machines located in the Commonwealth of Independent States (CIS) countries.

"ErrTraffic doesn't just show a fake update prompt, it actively corrupts the underlying page to make victims believe something is genuinely wrong," Censys
[said](https://censys.com/blog/errtraffic-inside-glitchfix-attack-panel)
. "It also applies CSS transformations that make everything look broken."

ClickFix has also been adopted by threat actors behind the
[ClearFake](https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html)
campaign, which is known to infect sites with fake web browser update decoys on compromised WordPress to distribute malware. ClearFake's use of ClickFix was first recorded in May 2024, leveraging CAPTCHA challenges for delivering Emmenhtal Loader (aka PEAKLIGHT), which then drops Lumma Stealer.

The attack chain also makes use of another known technique referred to as
[EtherHiding](https://thehackernews.com/2025/10/north-korean-hackers-use-etherhiding-to.html)
to retrieve the next-stage JavaScript code using smart contracts on Binance's BNB Smart Chain (BSC) and eventually inject the ClickFix fake CAPTCHA obtained from a different smart contract into the web page. At the same time, the final stage avoids re-infecting already infected victims.

Like in the case of the Amatera Stealer attack, the ClickFix command copied to the clipboard abuses "SyncAppvPublishingServer.vbs" to obtain the final payload hosted on the jsDelivr content delivery network (CDN). Expel's analysis of the ClearFake campaign shows that as many as 147,521 systems have likely been infected since late August 2025.

"One of many factors security products use to decide if behavior is malicious or not is whether said behavior is being performed by a trusted application," security researcher Marcus Hutchins
[said](https://expel.com/blog/clearfake-new-lotl-techniques/)
. "In this case, 'SyncAppvPublishingServer.vbs' is a default Windows component, and the file can only be modified by TrustedInstaller (a highly privileged system account used internally by the operating system). Therefore, the file and its behavior alone would not normally be suspect."

"Organizations and EDR are unlikely to outright block 'SyncAppvPublishingServer.vbs' from launching PowerShell in hidden mode, as it would prevent the component from being used for its intended purpose. Consequently, by abusing the command line injection bug in 'SyncAppvPublishingServer.vbs,' attackers can execute arbitrary code via a trusted system component."

Expel also characterized the campaign as highly sophisticated and very evasive, owing to the use of in-memory PowerShell code execution, coupled with its reliance on blockchain and popular CDNs, thus ensuring that it does not communicate with any infrastructure that's not a legitimate service.

Censys has described the broader fake CAPTCHA ecosystem as a "fragmented, fast-changing abuse pattern that uses trusted web infrastructure as the delivery surface," wherein Cloudflare-style challenges act as a conduit for clipboard-driven execution of PowerShell commands, VB Scripts, MSI installers, and even hand-offs to browser-native frameworks like
[Matrix Push C2](https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html)
.

"This aligns with a broader shift toward Living Off the Web: systematic reuse of security-themed interfaces, platform-sanctioned workflows, and conditioned user behavior to deliver malware," the attack surface management firm
[said](https://censys.com/blog/living-off-the-web-how-trust-infrastructure-became-a-malware-delivery-interface)
. "Attackers do not need to compromise trusted services; they inherit trust by operating inside familiar verification and browser workflows that users and tooling are trained to accept."