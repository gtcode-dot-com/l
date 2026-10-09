---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-26T12:15:12.365654+00:00'
exported_at: '2026-01-26T12:15:14.702083+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/winning-against-ai-based-attacks.html
structured_data:
  about: []
  author: ''
  description: AI-powered attacks are evading EDR via steganography, AV abuse, and
    automation, forcing a shift toward combined NDR and EDR defenses.
  headline: Winning Against AI-Based Attacks Requires a Combined Defensive Approach
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/winning-against-ai-based-attacks.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Winning Against AI-Based Attacks Requires a Combined Defensive Approach
updated_at: '2026-01-26T12:15:12.365654+00:00'
url_hash: 7e411833b1b085b9d731c8b0f596dc5007c5de10
---

**

The Hacker News
**

Jan 26, 2026

Endpoint Security / Artificial Intelligence

If there's a constant in cybersecurity, it's that adversaries are always innovating. The rise of offensive AI is transforming attack strategies and making them harder to detect.
[Google's Threat Intelligence Group](https://cloud.google.com/blog/topics/threat-intelligence/threat-actor-usage-of-ai-tools)
, recently reported on adversaries using Large Language Models (LLMs) to both conceal code and generate malicious scripts on the fly, letting malware shape-shift in real-time to evade conventional defenses. A deeper look at these novel attacks reveals both unprecedented sophistication and deception.

In November 2025,
[Anthropic reported on](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
what it described as the first known "AI-orchestrated cyber espionage campaign." This operation featured AI integrated throughout the stages of attack, from initial access to exfiltration, which was executed largely autonomously by the AI itself.

Another recent trend concerns
[ClickFix-related attacks](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
using steganography techniques (hiding malware within image files) that slipped past signature-based scans. Skillfully disguised as legitimate software update screens or CAPTCHAs, these attacks deceived users into deploying remote access trojans (RATs), info-stealers, and other malware payloads on their own devices.

Adversaries are also exploiting ways to trigger and then compromise anti-virus (AV) exclusion rules by using a combination of social engineering, attack-in-the-middle, and SIM swapping techniques. Based on research from
[Microsoft's threat team from October 2025](https://www.microsoft.com/en-us/security/blog/2023/10/25/octo-tempest-crosses-boundaries-to-facilitate-extortion-encryption-and-destruction)
, the threat actor they call Octo Tempest convinced its victims to disable various security products and automatically delete email notifications. These steps allowed their malware to spread across an enterprise network without tripping endpoint alerts. Actors are also easily deploying dynamic and adaptive
[tools that specialize in detecting and disabling AV software on endpoints](https://thehackernews.com/2024/10/hackers-abuse-edrsilencer-tool-to.html)
.

All these techniques share a common thread: the ability to evade legacy defenses such as endpoint detection and response (EDR), exposing
[the limitations of relying solely on EDR](https://corelight.com/blog/edr-evasion?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2)
. Their success illustrates where EDR, acting alone and without additional defensive measures, can be vulnerable. These are new attacks in every sense of the word, using AI automation and intelligence to subvert digital defenses. This moment signals a fundamental shift in the cyber threat landscape, and it's rapidly driving a change in defensive strategy.

## **NDR and EDR, working together**

[Network detection and response (NDR) and EDR both bring different protective benefits](https://corelight.com/blog/10-reasons-why-ndr-is-essential-alongside-edr?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2)
. EDR, by its nature, is focused on what is happening inside each specific endpoint, whereas NDR continuously monitors the network environment, detecting threats as they traverse the organization. It excels at picking up what EDR does not, identifying behavioral anomalies and deviations from typical network patterns.

In the age of AI-based threats, there is a need for both kinds of systems to work together, especially as these attacks can operate at higher speeds and greater scale. Some EDR systems weren't designed for the speed and scale of AI-fueled attacks. NDR can pick up these network anomalies and strengthen defenses and gain deeper insights from this network data, leveraging the additional protection this complementary technology can provide.

Compounding the challenge is that today's attack surface is expanding and growing more complex. Sophisticated threat actors now
**combine threats that move across a variety of domains**
, compromising identity, endpoint, cloud and on-premises infrastructure in a lethal mix. This means the corresponding security systems in each of these focus areas need to work together, sharing metadata and other signals, to find and stop these threats. The bad actors hide behind this complexity so as to maximize their reach, increase their blast radius, and provide cover while they use different hacking tools to assume various roles and focus on different intermediate targets.

[Blockade Spider](https://www.crowdstrike.com/en-us/blog/defeating-blockade-spider-how-crowdstrike-stops-cross-domain-attacks/)
, a group active since April 2024, uses these mixed domains for ransomware attacks. After gaining access through finding unmanaged systems, they move laterally across a network, searching for a file collection to encrypt to try to extract a ransom. The full breadth of their approach was discovered by using NDR to obtain visibility into the virtual systems and cloud properties, and then using EDR as soon as the attack moved across the network into managed endpoints.

One of the more infamous variants is what was used in the
[Volt Typhoon attack](https://thehackernews.com/2024/08/chinese-volt-typhoon-exploits-versa.html)
observed by Microsoft in 2023. It's attributed to Chinese state-sponsored actors using living off the land (LoTL) techniques that helped them avoid endpoint detection. Its targets were unmanaged network edge devices, such as SOHO routers and other Internet of Things (IoT) hardware. The actors were able to alter the originating packets to appear to be coming from a cable modem in Texas, rather than a direct link to a Chinese IP address. What gave the game away was the network traffic. While they were successful in avoiding EDR, variations in network traffic volume detected by NDR indicated the originating cable modem traffic was actually hiding something far more nefarious. In this case, NDR served as a security safety net by detecting malicious activity that slipped past EDR systems.

Rising remote work also adds vulnerability. As VPNs have become more widely used to support remote workforces, they pose new opportunities for exploitation. A lack of visibility on remote networks means a compromised endpoint on a trusted connection can introduce damage to the organization's environment. If an EDR doesn't detect that a local machine running the VPN is already infected with malware, it can easily spread across an enterprise once the machine connects to the corporate network. Compromised VPNs can also hide lateral network movement that disguises itself amongst typical network operations and management tools. For example,
[two recent breaches of Salesforce supply chains](https://thehackernews.com/2025/11/salesforce-flags-unauthorized-data.html)
were accomplished by using AI to harvest OAuth credentials to gain unauthorized access to various customer accounts. NDR can identify weak entry and transit points, helping identify the riskiest areas to fix first, and EDR can share the evidence of a compromised account being used as a pivot point.

These and other exploits highlight the benefits of continuous monitoring with EDR and NDR working in tandem, enabling defenders to spot innovative adversary techniques and respond quickly and decisively to emerging threats. Adversaries will grow more capable as AI evolves, making this combined approach essential for reducing risk and improving your organization's ability to respond quickly and decisively.

[Corelight's Open NDR Platform](https://corelight.com/products/open-ndr/?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2)
enables SOCs to detect novel attack types, including those leveraging AI techniques. Its multi-layered detection approach includes behavioral and anomaly detections that can identify a range of unique and unusual network activity. As adversaries develop new methods of evading EDR systems, security teams that deploy NDR can strengthen their enterprise's defensive game. Visit
[corelight.com/elitedefense](https://corelight.com/cp/elitedefense?utm_source=thehackernews&utm_medium=article-1&utm_campaign=awareness-wave-2)
to learn more.

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.