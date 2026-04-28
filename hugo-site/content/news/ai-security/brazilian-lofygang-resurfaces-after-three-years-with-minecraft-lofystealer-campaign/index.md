---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-28T18:15:14.627947+00:00'
exported_at: '2026-04-28T18:15:16.812449+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/brazilian-lofygang-resurfaces-after.html
structured_data:
  about: []
  author: ''
  description: LofyGang resurfaces with LofyStealer disguised as Minecraft hack, exfiltrating
    IBANs and passwords to 24.152.36[.]241, escalating gaming threats.
  headline: Brazilian LofyGang Resurfaces After Three Years With Minecraft LofyStealer
    Campaign
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/brazilian-lofygang-resurfaces-after.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Brazilian LofyGang Resurfaces After Three Years With Minecraft LofyStealer
  Campaign
updated_at: '2026-04-28T18:15:14.627947+00:00'
url_hash: cf6223895a14337227269fe309739a12ceb694d6
---

A cybercrime group of Brazilian origin has resurfaced after more than three years to orchestrate a campaign that targets Minecraft players with a new stealer called
**LofyStealer**
(aka GrabBot).

"The malware disguises itself as a Minecraft hack called 'Slinky,'" Brazil-based cybersecurity company ZenoX
[said](https://zenox.ai/en/lofystealer-malware-mirando-jogadores-de-minecraft/)
in a technical report. "It uses the official game icon to induce voluntary execution, exploiting the trust of young users in the gaming scene."

The activity has been attributed with high confidence to a threat actor known as
[LofyGang](https://thehackernews.com/2022/10/lofygang-distributed-200-malicious-npm.html)
, which was
[observed](https://thehackernews.com/2022/08/10-credential-stealing-python-libraries.html#malicious-npm-packages-steal-discord-tokens-and-bank-card-data)
leveraging typosquatted packages on the npm registry to push stealer malware in 2022, specifically with an intent to siphon credit card data and user accounts associated with Discord Nitro, gaming, and streaming services.

The group, believed to be active since late 2021, advertises their tools and services on platforms like GitHub and YouTube, while also contributing to an underground hacking community under the alias DyPolarLofy to leak thousands of Disney+ and  Minecraft accounts.

"Minecraft has been a LofyGang target since 2022," Acassio Silva, co-founder and head of threat intelligence at ZenoX, told The Hacker News. "They leaked thousands of Minecraft accounts under the DyPolarLofy alias on Cracked.io. The current campaign goes after Minecraft players directly through a fake 'Slinky' hack."

The attack begins with a Minecraft hack that, when launched, triggers the execution of a JavaScript loader that's ultimately responsible for the deployment of LofyStealer ("chromelevator.exe") on compromised hosts and execute it directly in memory with an aim to harvest a wide range of sensitive data spanning multiple web browsers, including Google Chrome, Chrome Beta, Microsoft Edge, Brave, Opera, Opera GX, Mozilla Firefox, and Avast Browser.

The captured data, which includes cookies, passwords, tokens, cards, and International Bank Account Numbers (IBANs), is exfiltrated to a command-and-control (C2) server located at 24.152.36[.]241.

"Historically, the group's primary vector was the JavaScript supply chain: NPM package typosquatting, starjacking (fraudulent references to legitimate GitHub repositories to inflate credibility), and payloads embedded in sub-dependencies to evade detection," ZenoX said.

"The focus was on Discord token theft, Discord client modification for credit card interception, and exfiltration via webhooks abusing legitimate services (Discord, Repl.it, Glitch, GitHub, and Heroku) as C2."

The latest development marks a departure from previously observed tradecraft and a shift towards a malware-as-a-service (MaaS) model with free and premium tiers, along with a bespoke builder called Slinky Cracked that's used as a delivery vehicle for the stealer malware.

The disclosure comes as threat actors are increasingly abusing the trust associated with a platform like GitHub to
[host bogus repositories](https://hexastrike.com/resources/blog/threat-intelligence/cloned-loaded-and-stolen-how-109-fake-github-repositories-delivered-smartloader-and-stealc/)
that act as lures for
[malware families](https://blog.intellibron.io/lua-jit-smartloader-analyzing-the-github-campaign-delivering-stealer/)
like
[SmartLoader, StealC Stealer](https://thehackernews.com/2026/02/smartloader-attack-uses-trojanized-oura.html)
, and Vidar Stealer. Unsuspecting users are directed to these repositories through techniques like SEO poisoning.

In some cases, attackers have been found to spread Vidar 2.0 through Reddit posts advertising fake Counter-Strike 2 game cheats, redirecting victims to a malicious website that delivers a ZIP archive containing the malware.

"This infostealer campaign highlights an ongoing security challenge where widely trusted platforms are abused to distribute malicious payloads," Acronis
[said](https://www.acronis.com/en/tru/posts/vidar-stealer-20-distributed-via-fake-game-cheats-on-github-and-reddit/)
in an analysis published last month. "By taking advantage of social trust and common download channels, threat actors are often able to bypass traditional security solutions."

The findings add to a growing list of campaigns that have leveraged GitHub in recent months -

* Targeting developers directly inside GitHub, using fake Microsoft Visual Studio Code (VS Code) security alerts posted through Discussions to trick users into installing malware by clicking on a link. "Because GitHub Discussions trigger email notifications for participants and watchers, these posts are also delivered directly to developers' inboxes," Socket
  [said](https://socket.dev/blog/widespread-github-campaign-uses-fake-vs-code-security-alerts-to-deliver-malware)
  . "This extends the reach of the campaign beyond GitHub itself and makes the alerts appear more legitimate."
* Targeting Argentina's judicial systems
  [using spear‑phishing emails](https://www.pointwild.com/threat-intelligence/covert-rat-phishing-campaign/)
  to distribute a compressed ZIP archive that uses an intermediate batch script to retrieve a
  [remote access trojan](https://thehackernews.com/2026/02/threatsday-bulletin-kali-linux-claude.html#judicial-spear-phish-drops-rat)
  (RAT) hosted on GitHub.
* Creating
  [GitHub accounts and OAuth applications](https://blog.atsika.ninja/posts/the-phishy-github-issue-case/)
  , followed by opening an issue that mentions a target developer, triggering an email notification that, in turn, tricks them into authorizing the OAuth app, effectively allowing the attacker to obtain their access tokens. The issues aim to induce a false sense of urgency, warning users of unusual access attempts.
* Using fraudulent GitHub repositories to distribute malicious batch script installers masquerading as legitimate IT and security software, leading to the deployment of the
  [TookPS](https://thehackernews.com/2025/04/cryptocurrency-miner-and-clipper.html)
  downloader, which then initiates a multi-stage infection chain to establish persistent remote access using SSH reverse tunnels and RATs like MineBridge RAT (aka TeviRAT). The activity has been attributed to
  [Rift Brigantine](https://www.bluevoyant.com/blog/rift-brigantines-github-lures-deploy-malware)
  (aka FIN11, Graceful Spider, and TA505).
* Using counterfeit GitHub repositories posing as AI tools, game cheats, Roblox scripts, phone number location trackers, and VPN crackers to distribute
  [LuaJIT payloads](https://www.netskope.com/blog/openclaw-trap-ai-assisted-lure-factory-targets-developers-gamers)
  that function as a generic trojan as part of a campaign dubbed TroyDen's Lure Factory.

"The breadth of the lure factory – gaming cheats, developer tools, phone trackers, Roblox scripts, VPN crackers – suggests an actor optimizing for volume across audiences rather than precision targeting," Netskope said.

"Defenders should treat any GitHub-hosted download that pairs a renamed interpreter with an opaque data file as a high-priority triage candidate, regardless of how legitimate the surrounding repository looks."