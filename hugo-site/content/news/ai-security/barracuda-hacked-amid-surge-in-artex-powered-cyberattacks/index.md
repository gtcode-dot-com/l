---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-16T18:53:46.915546+00:00'
exported_at: '2026-11-16T18:53:48.573563+00:00'
feed: https://feeds.feedburner.com/securityweek
language: en
source_url: https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks
structured_data:
  about: []
  author: ''
  description: Barracuda falls victim to an Artex-powered attack as more Chinese threat
    actors adopt the agentic AI penetration testing framework.
  headline: Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Barracuda Hacked Amid Surge in Artex-Powered Cyberattacks
updated_at: '2026-11-16T18:53:46.915546+00:00'
url_hash: f9b57f5984ac24069dd731b246714acdfe64e892
---

**The Artex agentic AI penetration testing framework has become a common tool in Chinese threat actors’ arsenal, and Barracuda is one of its victims.**

Published on GitHub in July 2026, Artex relies on a planner to formulate an objective and create tasks based on it, and on agents to perform those tasks, while the platform itself records the progress, findings, and assets.

It reportedly used DeepSeek v4.1-flash as the initial model, but can use other LLMs as well, and GLM-5.3 and Grok 4.6 were observed in certain instances. Overall, however, its users mainly rely on Chinese models, which are more permissive compared to US-made ones.

Artex was designed for security testing, but threat actors have been using it as part of in-the-wild intrusions since at least August, and its occurrence in real-world attacks has increased significantly during the past several weeks.

“The framework enables threat actors with minimal technical expertise to conduct complex, multi-target operations simultaneously, fundamentally accelerating attack velocity and expanding operational scale,” the FBI warns in
[a new alert](https://www.ic3.gov/CSA/2026/261113.pdf)
(PDF).

Mentioning the framework’s use in attacks on South Korean financial firms and
[ConnectWise](https://www.securityweek.com/china-apt-uses-ai-pentest-tool-artex-in-connectwise-attacks/)
, the FBI warns of the risks Artex poses: faster attacks through automation, exploitation of neglected peripheral devices, and the ability to find and exploit supply chain attack vectors.

Advertisement. Scroll to continue reading.

The framework’s developer removed their GitHub repository in October, but Artex continues to proliferate through other channels. In early November,
[Censys](https://censys.com/blog/artex-agentic-asbestos/)
was seeing roughly 1,500 hosts running exposed Artex consoles.

In October, Artex was used by Chinese espionage group Vapor Panda in a campaign targeting over 200 organizations in 14 countries, including “foreign ministries, a European presidency, and US pharmaceutical, semiconductor, defense, and nuclear organizations,”
[SentinelOne](https://www.sentinelone.com/blog/artex-unmasked-the-rise-of-ai-powered-artex-in-cybercrime-espionage/)
reports.

Storm-0940 is another Chinese state-sponsored group using Artex, but evidence shows that financially motivated threat actors such as Storm-3358 have also adopted the framework, Cisco’s Talos
[notes](https://blog.talosintelligence.com/artex-and-beyond/)
.

Post-exploitation, the threat actors were seen abusing compromised credentials and keys, escalating privileges, deploying persistence, moving laterally, and stealing credentials and data.

“Observed impacts range from access to cloud secrets and mailbox data to the use of compromised applications to reach connected environments,” Talos says.

Amazon
[describes](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/)
similar observations, noting that one of the most prominent Artex campaigns was focused on large-scale theft of credentials to access AI models, while another targeted cryptocurrency exchanges.

[Barracuda](https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion)
, which fell victim to an Artex-powered intrusion, published similar findings: hackers used an exposed valid cloud access key to map its reach, then reused discovered secrets to access more systems and exfiltrate more credentials and secrets.

“In all, the attacker touched about 10 cloud accounts in roughly 44 hours. The work was methodical and tireless. The probe names, the other indicators we collected, the order in which the attacker worked through our systems, and its built-in routines for hunting credentials and wallets all match Artex,” Barracuda explains.

The attack unfolded between November 1 and November 2, targeted sensitive material across secret stores, configurations, Kubernetes service accounts, and server metadata services, and left a backdoor behind in a Kubernetes cluster.

On some servers, the attackers gained shell access and used it to search for Ethereum keystore files, seed phrase files, extended private keys, and other wallet-related information.

The attack, Barracuda says, was similar to the October intrusion at cloud application hosting platform
[Railway](https://blog.railway.com/p/incident-report-october-security-incident)
. Furthermore, it fits the previously reported wave of intrusions at
[dozens of AI developer platforms](https://www.securityweek.com/ai-linked-breaches-mount-as-workos-northflank-trigger-dev-disclose-hacks/)
.

Barracuda has not attributed the attack, noting that Artex is used by many groups.

Amazon’s
[analysis](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-observes-threat-actors-running-cybercrime-campaigns-with-artex-ai-agents/)
of two Artex-powered campaigns revealed that the attackers relied on long-known techniques, but operated at far greater speeds courtesy of AI.

“The agents succeeded where basic security hygiene was missing, including default or hardcoded credentials, keys left in code and public artifacts, unauthenticated interfaces and inference endpoints, and unpatched software. Getting those fundamentals right remains the most effective defense,” Amazon says.

“The reported Artex activity shows that autonomous attackers don’t need a zero-day. They can find exposed services, exploit authorization gaps, and keep adapting while defenders are still triaging alerts and approving a response. When every defensive action has to wait for a person, the attacker controls the pace. Defenders need to move from identifying exposure to verified protection at machine speed,” Miggo Security co-founder and CEO Daniel Shechter said.

**Related:**
[Is AI Making Us Worse at Cybersecurity?](https://www.securityweek.com/is-ai-making-us-worse-at-cybersecurity/)

**Related:**
[OpenAI Unveils Daybreak Red Team, Defense Factory Security Tools](https://www.securityweek.com/openai-unveils-daybreak-red-team-defense-factory-security-tools/)

**Related:**
[Notion Customer Data Compromised in Fireworks AI Hack](https://www.securityweek.com/notion-customer-data-compromised-in-fireworks-ai-hack/)

**Related:**
[Google Widens Gemini 4 Carbon Access After AI Agents Verify Signal Code](https://www.securityweek.com/google-widens-gemini-4-carbon-access-after-ai-agents-verify-signal-code/)