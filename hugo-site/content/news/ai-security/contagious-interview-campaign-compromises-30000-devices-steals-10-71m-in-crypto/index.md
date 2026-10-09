---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-03T23:18:31.877911+00:00'
exported_at: '2026-10-03T23:18:33.397961+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/contagious-interview-campaign.html
structured_data:
  about: []
  author: ''
  description: North Korean Contagious Interview campaign compromised 30,000 devices
    and stole at least $10.71 million in cryptocurrency.
  headline: Contagious Interview Campaign Compromises 30,000 Devices, Steals $10.71M
    in Crypto
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/contagious-interview-campaign.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Contagious Interview Campaign Compromises 30,000 Devices, Steals $10.71M in
  Crypto
updated_at: '2026-10-03T23:18:31.877911+00:00'
url_hash: 1dcb430bc406c3fd538b77b714b3c675b88f0585
---

The North Korean threat actors behind the
**[Contagious Interview](https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html)**
campaign have compromised at least 30,000 devices located in more than 100 countries and siphoned funds or account credentials from over 7,000 cryptocurrency wallets, according to a new
[joint cybersecurity advisory](https://www.ic3.gov/CSA/2026/260918.pdf)
.

The primary targets of the campaign are individual web designers, engineers, and specialists in cryptocurrency, blockchain, and Web3 technologies. In all, the threat actors are estimated to have plundered at least $10.71 million worth of cryptocurrency from victims.

The alert comes courtesy of cybersecurity and intelligence agencies from Japan, the U.S., Australia, and Germany. The activity is tracked by the broader cybersecurity community under the monikers CL-STA-0240, DeceptiveDevelopment, DEV#POPPER, Famous Chollima, Gwisin Gang, PurpleBravo, Tenacious Pungsan, UNC5342, Void Dokkaebi, and WaterPlum.

The cyber threat group "conducts cyber attacks by infiltrating unsuspecting job seekers' computer networks, harvesting sensitive information, and stealing cryptocurrency," the alert said.

It's suspected that both WaterPlum and
[some North Korean IT workers](https://thehackernews.com/2026/08/north-korean-job-fraud-expands-beyond.html)
(aka PurpleDelta or Wagemole) operate under the 313 General Bureau of the Munitions Industry Department, corroborating a
[June 2025 assessment](https://thehackernews.com/2025/06/us-seizes-774m-in-crypto-tied-to-north.html)
from DTEX. What's more, the two clusters are said to be deeply intertwined, in some cases using the same IP addresses when accessing laptop farms and applying for positions at Japanese cryptocurrency exchanges.

Contagious Interview, first
[exposed](https://thehackernews.com/2026/07/dprk-linked-macos-malvertising-uses.html)
by Palo Alto Networks Unit 42, is a long-running campaign that has been underway since at least 2022, targeting software developers and IT professionals across the wild by posing as prospective employers and recruiters, and approaching them on social media platforms like LinkedIn under the pretext of lucrative job offers.

Once initial rapport is established, the threat actors instruct targets to complete a job assessment or coding test, triggering a multi-step infection chain that leads to the deployment of various malware families, including
[BeaverTail, InvisibleFerret](https://thehackernews.com/2024/07/north-korean-hackers-update-beavertail.html)
,
[FlexibleFerret](https://thehackernews.com/2026/01/north-korean-purplebravo-campaign.html)
,
[GolangGhost, PylangGhost](https://thehackernews.com/2025/06/bluenoroff-deepfake-zoom-scam-hits.html)
,
[OtterCookie](https://thehackernews.com/2026/07/north-korea-linked-hackers-hide.html)
,
[RATatouille, OtterCandy](https://thehackernews.com/2025/10/north-korean-hackers-combine-beavertail.html)
, and
[StoatWaffle](https://thehackernews.com/2026/03/north-korean-hackers-abuse-vs-code-auto.html)
.

The backdoor access afforded is then abused by the adversary to deliver remote access trojans for enabling persistent access and data exfiltration.

"Some WaterPlum actors also operate as North Korean IT workers performing web system design and development tasks on corporate web systems for clients," the agencies said, adding a laptop farm operated by a facilitator in Japan has been identified and dismantled.

Furthermore, WaterPlum has been observed using online chat platforms to communicate with U.S. and Japanese developers, while employing enablers in Japan, the U.S., and other countries to set up and manage laptop farms for remote device management.

"Beyond immediate credential theft, successful infections provide WaterPlum actors opportunities to infiltrate organizations employing targeted developers, enabling espionage, intellectual property theft, and additional lateral movement in corporate environments," the agencies noted. "Stolen ID images can also be used by North Korean IT workers to impersonate victims and generate foreign currency."

### IT Worker Threat Expands to Discord for Recruiting Proxies

Complementing North Korea's offensive cyber capabilities is the
[infamous IT worker scheme](https://www.npa.go.jp/bureau/security/northkorea_IT/NK_IT_202607.html)
, which is tasked with generating illicit revenue for the regime by landing jobs in Western companies and elsewhere under false identities. The operation is also known for increasingly relying on artificial intelligence (AI) to craft fictitious identities and expand its activities globally.

|  |
| --- |
|  |
| IT workers' recruitment process |

Sekoia, in its
[overview](https://www.sekoia.com/blog/beyond-lazarus-organization-of-dprk-cyber-capabilities)
of North Korea's cyber operations, described the IT worker program as an adaptation of an established practice that involved the "dispatch of North Korean labor abroad to earn foreign currency dates to the 1960s and 1970s, beginning with logging in the Soviet Far East before broadening into construction, textiles and restaurant services across Russia, China, the Gulf, and Africa."

According to infrastructure findings published in July 2026 by Kudelski Security, primary targeting is focused on the U.S. and Japan, with the threat actors utilizing commercial VPN providers, specifically Astrill VPN and Mullvad, to establish exit nodes within those targeted regions.

In a report published last week, Silent Push said it identified a North Korean IT worker spreading a fake job recruitment scam via a Discord server named "Mouse Review," specifically hiring individuals based in the U.S., the E.U., and Latin America to act as proxies and attend job interviews so as to get around sanctions, geographic blocks, and compliance checks.

The AI-generated job advertisement claims: "YOUR ROLE IS SIMPLE, BUT CRUCIAL. You handle communications and interviews. I handle all technical work behind the scenes. You get paid consistently for your communication."

Highlighting financial incentives of $3,000 to $5,000 for facilitators who land a job, the ad reveals a real-time technical proxying and remote desktop control strategy for the interview process: "For live coding challenges, I can remotely access your screen and complete coding tasks while you continue the conversation smoothly."

"The North Korean IT worker's primary goal is proxy hiring, using Western or Latin American (LATAM) citizens as the 'face' and legal identity to bypass sanctions, KYC (identity verification) controls, and regional hiring restrictions," Silent Push
[said](https://www.silentpush.com/blog/nk-it-worker/)
. "The job ad scam offers a financial incentive split (35% to the proxy, 65% to the North Korean IT Worker) to incentivize foreign nationals to serve as financial and identity mules."