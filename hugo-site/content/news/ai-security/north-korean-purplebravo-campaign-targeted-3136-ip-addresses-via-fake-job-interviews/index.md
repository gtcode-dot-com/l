---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-21T18:15:12.933710+00:00'
exported_at: '2026-01-21T18:15:15.162720+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html
structured_data:
  about: []
  author: ''
  description: North Korean PurpleBravo hackers targeted 3,136 IPs and 20 companies
    using fake interviews, malicious VS Code projects, and BeaverTail malware.
  headline: North Korean PurpleBravo Campaign Targeted 3,136 IP Addresses via Fake
    Job Interviews
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: North Korean PurpleBravo Campaign Targeted 3,136 IP Addresses via Fake Job
  Interviews
updated_at: '2026-01-21T18:15:12.933710+00:00'
url_hash: 8d9ea51cea4ab9a465546d60f3ffee17d5d7c224
---

As many as 3,136 individual IP addresses linked to likely targets of the Contagious Interview activity have been identified, with the campaign claiming 20 potential victim organizations spanning artificial intelligence (AI), cryptocurrency, financial services, IT services, marketing, and software development sectors in Europe, South Asia, the Middle East, and Central America.

The
[new findings](https://www.recordedfuture.com/research/purplebravos-targeting-it-software-supply-chain)
come from Recorded Future's Insikt Group, which is tracking the North Korean threat activity cluster under the moniker
**PurpleBravo**
. First
[documented](https://thehackernews.com/2023/11/north-korean-hackers-pose-as-job.html)
in late 2023, the
[campaign](https://thehackernews.com/2025/10/north-korean-hackers-combine-beavertail.html)
is also known as CL-STA-0240, DeceptiveDevelopment, DEV#POPPER, Famous Chollima, Gwisin Gang, Tenacious Pungsan, UNC5342, Void Dokkaebi, and WaterPlum.

The 3,136 individual IP addresses, primarily concentrated around South Asia and North America, are assessed to have been targeted by the adversary from August 2024 to September 2025. The 20 victim companies are said to be based in Belgium, Bulgaria, Costa Rica, India, Italy, the Netherlands, Pakistan, Romania, the United Arab Emirates (U.A.E.), and Vietnam.

"In several cases, it is likely that job-seeking candidates executed malicious code on corporate devices, creating organizational exposure beyond the individual target," the threat intelligence firm said in a new report shared with The Hacker News.

The disclosure comes a day after Jamf Threat Labs
[detailed](https://thehackernews.com/2026/01/north-korea-linked-hackers-target.html)
a significant iteration of the Contagious Interview campaign wherein the attackers abuse malicious Microsoft Visual Studio Code (VS Code) projects as an attack vector to distribute a backdoor, underscoring continued exploitation of trusted developer workflows to achieve their twin goals of cyber espionage and financial theft.

The Mastercard-owned company said it detected four LinkedIn personas potentially associated with PurpleBravo that masqueraded as developers and recruiters and claimed to be from the Ukrainian city of Odesa, along with several malicious GitHub repositories that are designed to deliver known malware families like BeaverTail.

PurpleBravo has also been observed managing two distinct sets of command-and-control (C2) servers for BeaverTail, a JavaScript infostealer and loader, and a Go-based backdoor known as
[GolangGhost](https://thehackernews.com/2025/11/north-korean-hackers-deploy-197-npm.html)
(aka FlexibleFerret or WeaselStore) that is based on the HackBrowserData open-source tool.

The C2 servers, hosted across 17 different providers, are administered via Astrill VPN and from IP ranges in China. North Korean threat actors'
[use of Astrill VPN](https://spur.us/astrill-vpn-and-remote-worker-fraud/)
in cyber attacks has been
[well-documented](https://www.silentpush.com/blog/astrill-vpn/)
over the years.

It's worth pointing out that Contagious Interview complements a second, separate campaign referred to as Wagemole (aka PurpleDelta), where IT workers from the Hermit Kingdom actors seek unauthorized employment under fraudulent or stolen identities with organizations based in the U.S. and other parts of the world for both financial gain and espionage.

While the two clusters are treated as disparate sets of activities, there are significant
[tactical and infrastructure overlaps](https://thehackernews.com/2025/09/north-korean-hackers-use-new-akdoortea.html)
between them despite the fact that the IT worker threat has been ongoing since 2017.

"This includes a likely PurpleBravo operator displaying activity consistent with North Korean IT worker behavior, IP addresses in Russia linked to North Korean IT workers communicating with PurpleBravo C2 servers, and administration traffic from the same Astrill VPN IP address associated with PurpleDelta activity," Recorded Future said.

To make matters worse, candidates who are approached by PurpleBravo with fictitious job offers have been found to take the coding assessment on company-issued devices, effectively compromising their employers in the process. This highlights that the IT software supply chain is "just as vulnerable" to infiltration from North Korean adversaries other than the IT workers.

"Many of these [potential victim] organizations advertise large customer bases, presenting an acute supply-chain risk to companies outsourcing work in these regions," the company noted. "While the North Korean IT worker employment threat has been widely publicized, the PurpleBravo supply-chain risk deserves equal attention so organizations can prepare, defend, and prevent sensitive data leakage to North Korean threat actors."