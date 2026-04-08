---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-08T10:15:16.651000+00:00'
exported_at: '2026-04-08T10:15:18.901749+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html
structured_data:
  about: []
  author: ''
  description: Over 1,700 malicious packages since Jan 2025 fuel cross-ecosystem supply
    chain attacks, enabling espionage and financial theft.
  headline: N. Korean Hackers Spread 1,700 Malicious Packages Across npm, PyPI, Go,
    Rust
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/n-korean-hackers-spread-1700-malicious.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: N. Korean Hackers Spread 1,700 Malicious Packages Across npm, PyPI, Go, Rust
updated_at: '2026-04-08T10:15:16.651000+00:00'
url_hash: 50beef3305ca5af06e3a818d01b44a93493ffd96
---

The North Korea-linked persistent campaign known as
**[Contagious Interview](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)**
has spread its tentacles by publishing malicious packages targeting the Go, Rust, and PHP ecosystems.

"The threat actor's packages were designed to impersonate legitimate developer tooling [...], while quietly functioning as malware loaders, extending Contagious Interview’s established playbook into a coordinated cross-ecosystem supply chain operation," Socket security researcher Kirill Boychenko
[said](https://socket.dev/blog/contagious-interview-campaign-spreads-across-5-ecosystems)
in a Tuesday report.

The complete list of identified packages is as follows -

* npm: dev-log-core, logger-base, logkitx, pino-debugger, debug-fmt, debug-glitz
* PyPI: logutilkit, apachelicense, fluxhttp, license-utils-kit
* Go: github[.]com/golangorg/formstash, github[.]com/aokisasakidev/mit-license-pkg
* Rust: logtrace
* Packagist: golangorg/logkit

These loaders are designed to fetch platform-specific second-stage payloads, which turn out to be a piece of malware with infostealer and remote access trojan (RAT) capabilities. It's primarily focused on gathering data from web browsers, password managers, and cryptocurrency wallets.

However, a Windows version of the malware delivered via "license-utils-kit" incorporates what's described by Socket as a "full post-compromise implant" that's equipped to run shell commands, log keystrokes, steal browser data, upload files, terminate web browsers, deploy AnyDesk for remote access, create an encrypted archive, and download additional modules.

"That makes this cluster notable not just for its cross-ecosystem reach, but for the depth of post-compromise functionality embedded in at least part of the campaign," Boychenko added.

What makes the latest set of libraries noteworthy is that the malicious code is not triggered during installation.Rather, it's embedded into seemingly legitimate functions that align with the package's advertised purpose. For instance, in the case of "logtrace," the code is concealed within "Logger::trace(i32)," a method that's unlikely to raise a developer's suspicion.

The expansion of Contagious Interview across five open-source ecosystems is a further sign that the campaign is a well-resourced and persistent supply chain threat engineered to systematically infiltrate these platforms as initial access pathways to breach developer environments for espionage and financial gain.

In all, Socket said it has identified
[more than 1,700 malicious packages](https://socket.dev/supply-chain-attacks/north-korea-s-contagious-interview-campaign)
linked to the activity since the start of January 2025.

The discovery is part of a broader software supply chain compromise campaign undertaken by North Korean hacking groups. This includes the
[poisoning](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html)
of the popular Axios npm package to distribute an implant called WAVESHAPER.V2 after taking control of the package maintainer's npm account via a tailored social engineering campaign.

The attack has been attributed to a financially motivated threat actor known as UNC1069, which overlaps with BlueNoroff, Sapphire Sleet, and Stardust Chollima. Security Alliance (SEAL), in a report published today, said it blocked 164 UNC1069-linked domains impersonating services like Microsoft Teams and Zoom between February 6 and April 7, 2026.

"UNC1069 operates multi-week, low-pressure social engineering campaigns across Telegram, LinkedIn, and Slack – either impersonating known contacts or credible brands or by leveraging access to previously compromised company and individual accounts – before delivering a fraudulent Zoom or Microsoft Teams meeting link," SEAL
[said](https://radar.securityalliance.org/advisory-on-dprk-unc1069-fake-microsoft-teams-and-zoom-calls/)
.

These fake meeting links are used to serve ClickFix-like lures, resulting in the execution of malware that contacts an attacker-controlled server for data theft and targeted post-exploitation activity across Windows, macOS, and Linux.

"Operators deliberately do not act immediately following initial access. The implant is left dormant or passive for a period following compromise," SEAL added. "The target typically reschedules the failed call and continues normal operations, unaware that the device is compromised. This patience extends the operational window and maximizes the value extracted before any incident response is triggered."

In a statement shared with The Hacker News, Microsoft said financially-driven North Korean threat actors are actively evolving their toolset and infrastructure, using domains masquerading as U.S.-based financial institutions and video conferencing applications for social engineering.

"What we are seeing consistently is ongoing evolution in how DPRK-linked, financially motivated actors operate, shifts in tooling, infrastructure, and targeting, but with clear continuity in behavior and intent," Sherrod DeGrippo, general manager for threat intelligence at Microsoft, said.