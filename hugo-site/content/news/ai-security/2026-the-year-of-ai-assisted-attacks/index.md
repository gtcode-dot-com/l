---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-04T12:15:13.811159+00:00'
exported_at: '2026-05-04T12:15:16.400384+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html
structured_data:
  about: []
  author: ''
  description: AI lowers attack barriers in 2025, enabling 7M-user breach and faster
    exploits, increasing scale and impact of cyber threats.
  headline: '2026: The Year of AI-Assisted Attacks'
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/2026-year-of-ai-assisted-attacks.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: '2026: The Year of AI-Assisted Attacks'
updated_at: '2026-05-04T12:15:13.811159+00:00'
url_hash: 86ea4b30666e4e39dfd446797472b848663515a9
---

On December 4, 2025, a 17-year-old was
[arrested in Osaka](https://www.japantimes.co.jp/news/2025/12/04/japan/crime-legal/police-arrest-cyberattack-net-cafe/)
under Japan’s Unauthorized Access Prohibition Act. The young man had run malicious code to extract the personal data of over 7 million users of
[Kaikatsu Club](https://www.immuniweb.com/blog/teen-arrested-for-the-internet-cafe-operator-hack.html)
, Japan's largest internet cafe chain. When asked, the young man shared his motivation for the hack: he wanted to buy Pokémon cards.

In a sense, this is a fairly conventional story. Since the 1990s, we’ve read about computing wunderkinds such as Kevin Mitnick, whose technical ability exceeded their judgment and who were drawn into high-profile cybercrimes in pursuit of status, profit, or excitement. But something is different in this story: the young man in question wasn’t technical.

## The rise of AI-assisted attacks

In 2025, LLM-backed chat and agent systems crossed a threshold, going from useful but error-prone coding assistants to end-to-end coding powerhouses. Throughout the year, several measures of cybercrime frequency and severity approximately doubled. Instances of
[malicious packages discovered on public repositories increased by 75%](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware)
,
[cloud intrusions increased by 35%](https://www.crowdstrike.com/global-threat-report/)
, and
[AI-generated phishing began outperforming human red teams](https://hoxhunt.com/blog/ai-vs-human-phishing-benchmark-2025)
entirely. A more qualitative difference, however, has been in the profiles of those conducting attacks.

In February 2025,
[three teenagers](https://japantoday.com/category/crime/3-teens-arrested-over-fraudulent-mobile-contracts-aided-by-chatgpt)
(ages 14, 15, and 16) with no coding background used
[ChatGPT](https://openai.com/index/chatgpt/)
to build a tool that hit
[Rakuten Mobile](https://mobileidworld.com/japanese-teens-arrested-for-using-chatgpt-to-hack-rakuten-mobile-contracts/)
’s system ~220,000 times, spending their proceeds on gaming consoles and online gambling. In July 2025, a single actor using Claude Code, a more sophisticated agentic coding platform,
[conducted an extortion campaign targeting 17 organizations](https://www.nbcnews.com/tech/security/hacker-used-ai-automate-unprecedented-cybercrime-spree-anthropic-says-rcna227309)
over the course of one month, using agentic AI to develop malicious code, organize stolen files, analyze financial records to calibrate demands, and draft extortion emails. In December 2025, another individual
[used Claude Code and ChatGPT to breach the Mexican government](https://www.securityweek.com/hackers-weaponize-claude-code-in-mexican-government-cyberattack/)
, targeting more than 10 agencies and stealing over 195 million taxpayer records.

While these attacks were possible before 2025, we are now seeing single-actor attacks that would have been characteristic of organized teams and smaller-scale attacks by nontechnical individuals that would have been more characteristic of attacks carried out by a talented hacker or engineer in the pre-AI era. In 2025, the barrier to entry for conducting a technically sophisticated attack has been significantly lowered.

## Bad numbers go up

Throughout 2025, measures of bot activity, malware, targeted compromise, and phishing exhibited dramatic increases. At the same time, measures of LLM capability on technical benchmarks leaped forward.

In 2022, there were 55,000 malicious packages in public repositories, according to
[Sonatype](https://www.sonatype.com/state-of-the-software-supply-chain/2026/open-source-malware)
. By 2025, that number had grown to 454,600. Notable leaps occurred in 2023 (the year GPT-4 was released) and 2025 (a marquee year for agentic coding).

Another practical measure of real-world attacker capability, time to exploit, is almost unrecognizable from the pre-AI era. Time to exploit measures the time from when a vulnerability is publicizeduntil an exploit for that vulnerability has been discovered in the wild.

This number has come down from
[over 700 days in 2020 to only 44 days in 2025](https://flashpoint.io/blog/n-day-vulnerability-trends/)
. This means attackers are developing exploits for known vulnerabilities in less than 2 months, rather than in almost 2 years. In fact, Mandiant’s
[M-Trends 2026 report](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026/)
found that time-to-exploit has effectively gone negative — exploits are now routinely arriving before patches, with
[28.3% of CVEs exploited within 24 hours](https://vulncheck.com/blog/exploitation-trends-2025)
of disclosure.

Throughout 2024, 2025, and early 2026, the performance of frontier models such as ChatGPT, Claude, and Gemini on benchmarks such as SWE-bench, a test of software development capability, rocketed through the roof. In August 2024, top models could resolve
[33% of real GitHub issues](https://epoch.ai/benchmarks/swe-bench-verified)
on the bench. By December 2025, that number had climbed to just under 81%.

In late 2024 and especially 2025, AI-assisted coding hit an inflection point. Supercharging coding, however, has also supercharged offensive capabilities, and the environment in 2026 reflects these changes, with attacks occurring more frequently, with greater severity, and with greater impact.

## Can’t patch the pain away

AI is speeding up both defenders and attackers. Unfortunately, based on data from 2025 and 2026, the arms race is favoring attackers. The average time to remediate a known high- or critical-severity CVE is now 74 days, according to the Edgescan 2025 Vulnerability Statistics Report. In addition, 45% of vulnerabilities in systems maintained by large companies (1000+ employees) never get remediated.

Organizations have also been feeling pressure from the increased malware found in public package repositories. In September 2025, the
[Shai-Hulud attack](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
targeting the npm ecosystem compromised over 500 packages. Over
[487 organizations had secrets compromised](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem)
, and
[$8.5m was stolen from Trust Wallet](https://www.bleepingcomputer.com/news/security/trust-wallet-links-85-million-crypto-theft-to-shai-hulud-npm-attack/)
after attackers used exposed credentials to poison its Chrome extension. Many organizations instituted code freezes following the attack.

The detection problem compounds this. In 2025, malicious npm packages posing as popular libraries like chalk and debug included documentation, unit tests, and code structured to appear as legitimate telemetry modules. Static analysis and signature scanners missed them entirely — because the code, likely AI-generated, looked like real software. As Chainguard CEO Dan Lorenc
[has observed](https://cyberscoop.com/dan-lorenc-chainguard-open-source-security/)
, “The complexity and scale of vulnerability management has outgrown the capabilities of most organizations to manage on their own.”

## Deleting categories of attack

The lesson of 2025 is that you can’t outrun these attacks. The exploit window is shrinking faster than patch cycles can compress, and AI-generated malware is slipping past the detection tools that organizations have relied on for decades. The Venn diagram of “willing to do attacks” and “has technical ability to do attacks” used to be a sliver, but it is growing every month. At the same time, we’re building more software, faster. And if the supply chain attacks are coming fast in 2026, what will 2027 look like with model capabilities dialed up to 10?

Thinking in terms of speed and outrunning attacks will only get teams so far in the current environment. Rather, the smart move is to hit delete on entire categories of vulnerability, freeing up teams to focus on the remaining areas. This is the approach behind
[Chainguard Libraries](https://www.chainguard.dev/libraries)
, which rebuilds every open source library from verified, attributable source code. The idea behind Libraries is to render whole categories of attacks structurally impossible, protecting users from CI/CD takeover, dependency confusion, long-lived token theft, or package distribution attacks. When
[tested against 8,783 malicious npm packages](https://www.chainguard.dev/unchained/mitigating-malware-in-the-python-npm-ecosystem)
, Chainguard Libraries blocked 99.7%. Against approximately 3,000 malicious Python packages, it blocked roughly 98%.

454,600 malicious packages last year. 394,877 in a single quarter. An amateur in Algeria
[built ransomware that hit 85 targets](https://research.checkpoint.com/2025/funksec-alleged-top-ransomware-group-powered-by-ai/)
in his first month. A 17-year-old exfiltrated 7 million records to buy Pokémon cards. The tools that enabled these attacks are getting cheaper, faster, and more accessible. Instead of scrambling when the next
[Axios](https://thehackernews.com/2026/03/axios-supply-chain-attack-pushes-cross.html)
or
[Shai-Hulud](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/)
hits next week or next month, you could just read about it over your cup of coffee while your organization populates production systems, artifact managers, and developer workstations from Chainguard Libraries.

**Note:**
This article was expertly written and contributed by Patrick Smyth, Principal Developer Relations Engineer,
*Chainguard.*

Found this article interesting?

This article is a contributed piece from one of our valued partners.

Follow us on

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)

,

[Twitter](https://twitter.com/thehackersnews)

and

[LinkedIn](https://www.linkedin.com/company/thehackernews/)

to read more exclusive content we post.