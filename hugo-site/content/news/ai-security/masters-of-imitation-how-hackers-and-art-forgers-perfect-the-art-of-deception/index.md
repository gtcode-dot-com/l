---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-02T04:03:21.479304+00:00'
exported_at: '2026-04-02T04:03:24.678945+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/masters-of-imitation-how-hackers-and.html
structured_data:
  about: []
  author: ''
  description: 81% of attacks are malware-free as AI-driven mimicry hides threats
    in trusted systems, increasing detection difficulty and risk.
  headline: 'Masters of Imitation: How Hackers and Art Forgers Perfect the Art of
    Deception'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/masters-of-imitation-how-hackers-and.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: 'Masters of Imitation: How Hackers and Art Forgers Perfect the Art of Deception'
updated_at: '2026-04-02T04:03:21.479304+00:00'
url_hash: 463221cb96dc91a62ade6bc6b42bd3e73c490afa
---

Unmasking impostors is something the art world has faced for decades, and there are valuable lessons from the works of Elmyr de Hory that can apply to the world of defensive cybersecurity. During the 1960s, de Hory gained infamy as a premier forger, passing off counterfeit masterworks of Picasso, Matisse, and Renoir to unsuspecting collectors and renowned museums. Over the next several decades, more than a thousand of his works slipped past experts who relied on trusted signatures, familiar patterns, and reputable provenance.

It’s not unlike the challenges SOCs are facing now. We’re firmly in the Age of Imitation. Cyberattackers, equipped with AI, are mastering the art of imitating the familiar, posing as trusted users and masking their activity within legitimate processes and ordinary network traffic. As history shows, it’s often easier to identify impostors when you know what to look for.

## **Key takeaways for defenders:**

* Mimicry is the new normal:
  [81% of attacks are malware-free](https://go.crowdstrike.com/2026-global-threat-report.html)
* Agentic AI is helping attackers hide more effectively within innocent network traffic and behaviors
* Layered defense now requires more layers to extend protection across software supply chains and federated identities
* [NDR](https://www.corelight.com/cp/elitedefense)
  enhances visibility to detect and neutralize “fakes”

### **The rise of mimicry in modern attacks**

Just as de Hory reused old canvases and pigments to make his paintings appear more authentic, attackers employ similar methods in the digital realm, leveraging trusted tools and credentials to make their malicious activity blend in. And while mimicry-based techniques have long been a staple of the attacker’s playbook, over the past couple of years, they have gotten more sophisticated. Living-off-the-Land (LotL) attacks and AI-augmented attack tooling have raised the bar for fakery.
[CrowdStrike’s 2026 Global Threat Report](https://go.crowdstrike.com/2026-global-threat-report.html)
states that 81% of attacks are now malware-free, relying instead on legitimate tools and techniques, which is the hallmark of LotL tactics. Spotting these fakes quickly isn’t just an option: it’s one of the best chances to disrupt an attack before it causes real harm.

## **A field guide to network fakery:**

### **Agentic AI-assisted actors**

*Autonomous or semi-autonomous, these generate fake identities, code, and mimic behaviors at scale.*

de Hory had a complex support network to sell his paintings, involving art dealers and other representatives across many countries and cities. When some potential buyers became suspicious, he started selling his works under a variety of pseudonyms. This is similar to what is now happening with the use of inexpensive AI agents. These aren’t just used to
[forge believable identities](https://news.usps.com/2026/03/02/theres-a-new-way-scammers-are-targeting-victims/)
to conduct fraud, but are now used to produce
[exploit code to exfiltrate secrets](https://www.theverge.com/tech/879088/dji-romo-hack-vulnerability-remote-control-camera-access-mqtt)
and scripts to infect endpoints, forming the basis of a larger-scale attack. Sophisticated, self-learning agents observe network behavior and continuously tune their own traffic, mirroring their patterns to fool anomaly detections. They shift C2 traffic into bursts that coincide with legitimate spikes and manipulate their signals just enough to avoid standing out. And legitimate agents are being used as orchestrators of other exploit tools to automate and scale up attacks.

### **Supply chain and cloud impostors**

*Counterfeit or compromised components that masquerade as trusted software, updates, or cloud services.*

Attackers use malicious AI agents to create a layer of complexity for software supply chains. The agents substitute malicious software and masquerade this code as just another benign update, making the exploit origins and root causes harder to figure out. These types of exploits mean that attackers don’t need to fool network defenders or software developers directly. This is what
[Microsoft researchers found with the Shai Hulud v2 worm](https://www.microsoft.com/en-us/security/blog/2025/12/09/shai-hulud-2-0-guidance-for-detecting-investigating-and-defending-against-the-supply-chain-attack/)
. Attackers modified hundreds of software packages to provide a coordinated ecosystem to harvest developer credentials and API secrets, then boosted its potency by propagating through trusted internal network shares, all while impersonating legitimate software updates. While supply chain attacks have been around for many years (
[think SolarWinds](https://thehackernews.com/2020/12/new-evidence-suggests-solarwinds.html)
), AI agents have made them faster to produce and distribute.

Cloud-based deception has also accelerated. For years, attackers have used fake login pages and spoofed cloud repositories that mimic the design and branding of legitimate services to trick users into handing over credentials. AI-powered tools have the potential to intensify the creation of these convincing fakes, enabling attackers to generate fraudulent sites more quickly and at greater scale.

### **Cloaked tunnels**

*Techniques that cloak malicious traffic inside allowed protocols or encrypted channels*

de Hory widened his network by using galleries and other representatives to mask his transactions and sell his forgeries. Today’s attackers do something similar, cloaking their network conversations using IP tunnels to hide malicious activity inside legitimate-looking traffic. Another cloaking mechanism uses purposely mismatched requests and replies, such as requesting confidential web data from a previously unknown destination to evade detection. Attackers also use these methods to disable security protections, then lie dormant inside a corporate network for months, waiting for the right moment to strike. Add to these methods are mobile app stores, which have been plagued for years with fake apps containing malware, such as this more recent example of a
[visual search tool that hides a remote execution exploit](https://annex.security/blog/pixel-perfect/)
.

### **Rogue infrastructure**

*Attacker-controlled servers, domains, or services designed to imitate legitimate infrastructure.*

de Hory evaded detection by moving frequently, from city to city, around the globe. Cyberattackers employ a similar strategy, spinning up lookalike servers, domains, and services under their control that impersonate trusted infrastructure. Recent
[Microsoft research](https://www.microsoft.com/en-us/security/blog/2026/03/02/oauth-redirection-abuse-enables-phishing-malware-delivery/)
shows threat actors luring users with fake Teams meeting messages that led to credential harvesting sites disguised as legitimate login pages. Fake connections like this can be a precursor to a series of moves to take control of your network resources and data. Fake servers can then be employed to compromise and extract sensitive data, later leveraging the information to launch a ransomware campaign.

### **Finally, phishing**

And fakery lies at the heart of any phishing campaign. Today’s campaigns make use of all kinds of fakery, including using fake email addresses that appear to be part of your domain but are part of
[homoglyph or homograph attacks](https://www.malwarebytes.com/blog/news/2017/10/out-of-character-homograph-attacks-explained)
. These attacks can spoof legitimate domains with substitute lookalike characters to redirect conversations under a hacker’s control or be used as part of subsequent phishing campaigns. de Hory would be pleased, since he took so much effort to copy the brushwork, color choices, and styles of the masters in his fakes.

## **How NDR can expose the fakes**

The parallels between de Hory's forgeries and modern cyberattacks are striking. Both rely on mimicry, movement, and exploiting trusted systems. de Hory was eventually exposed when experts compared multiple works and spotted the stylistic fingerprints he couldn't hide. Network detection and response (NDR) can catch attackers the same way, by watching for behavioral patterns and anomalies that betray what's really happening on the network.

Here are a few of the ways NDR helps expose malicious activity hiding in plain sight:

* **Detecting behavioral anomalies:**
  Identifying deviations from established network baselines, such as unusual login times, atypical data transfers, or unexpected lateral movement that may signal an impostor is at work, even when credentials appear legitimate.
* **Revealing protocol and metadata inconsistencies:**
  Spotting mismatches that attackers can't easily hide, such as odd protocol combinations, traffic to newly registered or homograph domains, or encrypted sessions with suspicious certificate details.
* **Providing context:**
  Enriching raw traffic with metadata that explains the wider picture, such as where connections originate, how they behave over time, and whether they fit normal patterns, so analysts can quickly separate real threats from noise, such as
  [this example, which shows how a SOC analyst can test various hypotheses](https://www.youtube.com/watch?v=jSYkVitRwVA)
  to figure out an attack.

As attackers grow more sophisticated and leverage AI to scale their deception, defenders need tools that can see through the noise. NDR, working alongside other security products, gives SOCs the visibility to catch these threats early, before they cause real damage.

[Corelight’s Open NDR Platform](https://corelight.com/elitedefense?utm_source=feedly&utm_medium=retail-march&utm_campaign=awareness-wave-2)
enables SOCs to detect emerging threats, including those leveraging AI techniques. Its multi-layered detection approach includes behavioral and anomaly detections that can identify a range of unique and unusual network activity. As adversaries develop new methods of attack, security teams that deploy NDR can strengthen their enterprise’s defensive game. Visit
[corelight.com/elitedefense](https://corelight.com/elitedefense?utm_source=feedly&utm_medium=retail-march&utm_campaign=awareness-wave-2)
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