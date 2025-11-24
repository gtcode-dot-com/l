---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2025-11-22T12:00:08.267886+00:00'
exported_at: '2025-11-22T12:00:10.862732+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html
structured_data:
  about: []
  author: ''
  description: Matrix Push C2 abuses browser notifications for fileless, cross-platform
    phishing, while Velociraptor misuse rises after a Windows Server flaw.
  headline: Matrix Push C2 Uses Browser Notifications for Fileless, Cross-Platform
    Phishing Attacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2025/11/matrix-push-c2-uses-browser.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: Matrix Push C2 Uses Browser Notifications for Fileless, Cross-Platform Phishing
  Attacks
updated_at: '2025-11-22T12:00:08.267886+00:00'
url_hash: b58a47d3efafff2131d33b5f20636fa9c64a10cc
---

Bad actors are leveraging browser notifications as a vector for phishing attacks to distribute malicious links by means of a new command-and-control (C2) platform called Matrix Push C2.

"This browser-native, fileless framework leverages push notifications, fake alerts, and link redirects to target victims across operating systems," Blackfog researcher Brenda Robb
[said](https://www.blackfog.com/new-matrix-push-c2-deliver-malware/)
in a Thursday report.

In these attacks, prospective targets are tricked into allowing browser notifications through social engineering on malicious or legitimate-but-compromised websites.

Once a user agrees to receive notifications from the site, the attackers take advantage of the
[web push notification mechanism](https://developer.mozilla.org/en-US/docs/Web/API/Push_API/Best_Practices)
built into the web browser to send alerts that look like they have been sent by the operating system or the browser itself, leveraging trusted branding, familiar logos, and convincing language to maintain the ruse.

These include alerts about, say, suspicious logins or browser updates, along with a handy "Verify" or "Update" button that, when clicked, takes the victim to a bogus site.

What makes this a clever technique is that the entire process takes place through the browser without the need for first infecting the victim's system through some other means. In a way, the attack is like
[ClickFix](https://thehackernews.com/2025/08/clickfix-malware-campaign-exploits.html)
in that users are lured into following certain instructions to compromise their own systems, thereby effectively bypassing traditional security controls.

That's not all. Since the attack plays out via the web browser, it's also a cross-platform threat. This effectively turns any browser application on any platform that subscribes to the malicious notifications to be enlisted to the pool of clients, giving adversaries a persistent communication channel.

Matrix Push C2 is offered as a malware-as-a-service (MaaS) kit to other threat actors. It's sold directly through crimeware channels, typically via Telegram and cybercrime forums, under a tiered subscription model: about $150 for one month, $405 for three months, $765 for six months, and $1,500 for a full year.

"Payments are accepted in cryptocurrency, and buyers communicate directly with the operator for access," Dr. Darren Williams, founder and CEO of BlackFog, told The Hacker News. "Matrix Push was first observed at the beginning of October and has been active since then. There's no evidence of older versions, earlier branding, or long-standing infrastructure. Everything indicates this is a newly launched kit."

The tool is accessible as a web-based dashboard, allowing users to send notifications, track each victim in real-time, determine which notifications the victims interacted with, create shortened links using a built-in URL shortening service, and even record installed browser extensions, including cryptocurrency wallets.

"The core of the attack is social engineering, and Matrix Push C2 comes loaded with configurable templates to maximize the credibility of its fake messages," Robb explained. "Attackers can easily theme their phishing notifications and landing pages to impersonate well-known companies and services."

Some of the supported notification verification templates are associated with well-known brands like MetaMask, Netflix, Cloudflare, PayPal, and TikTok. The platform also includes an "Analytics & Reports" section that allows its customers to measure the effectiveness of their campaigns and refine them as required.

"Matrix Push C2 shows us a shift in how attackers gain initial access and attempt to exploit users," BlackFog said. "Once a user's endpoint (computer or mobile device) is under this kind of influence, the attacker can gradually escalate the attack."

"They might deliver additional phishing messages to steal credentials, trick the user into installing a more persistent malware, or even leverage browser exploits to get deeper control of the system. Ultimately, the end goal is often to steal data or monetize the access, for example, by draining cryptocurrency wallets or exfiltrating personal information."

### Attacks Misusing Velociraptor on the Rise

The development comes as Huntress said it
[observed](https://www.huntress.com/blog/velociraptor-misuse-part-one-wsus-up)
a "significant uptick" in attacks weaponizing the legitimate
[Velociraptor](https://thehackernews.com/2025/10/hackers-turn-velociraptor-dfir-tool.html)
digital forensics and incident response (DFIR) tool over the past three months.

On November 12, 2025, the cybersecurity vendor said threat actors deployed Velociraptor after obtaining initial access through exploitation of a flaw in Windows Server Update Services (
[CVE-2025-59287](https://thehackernews.com/2025/10/microsoft-issues-emergency-patch-for.html)
, CVSS score: 9.8), which was patched by Microsoft late last month.

Subsequently, the attackers are said to have launched discovery queries with the goal of conducting reconnaissance and gathering details about users, running services, and configurations. The attack was contained before it could progress further, Huntress added.

The discovery shows that threat actors are not just
[using](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
[custom C2 frameworks](https://thehackernews.com/2025/11/researchers-detail-tuoni-c2s-role-in.html)
, but are also employing readily available offensive cybersecurity and incident response tools to their advantage.

"We've seen threat actors use legitimate tools long enough to know that Velociraptor won't be the first dual-use, open-source tool that will pop up in attacks – nor will it be the last," Huntress researchers said.