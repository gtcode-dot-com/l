---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-02T02:15:14.916459+00:00'
exported_at: '2026-05-02T02:15:17.761635+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html
structured_data:
  about: []
  author: ''
  description: China-linked hackers exploit Exchange flaws since Dec 2024 across 8
    countries, enabling espionage and credential theft operations.
  headline: China-Linked Hackers Target Asian Governments, NATO State, Journalists,
    and Activists
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/china-linked-hackers-target-asian.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: China-Linked Hackers Target Asian Governments, NATO State, Journalists, and
  Activists
updated_at: '2026-05-02T02:15:14.916459+00:00'
url_hash: 5807671cf89d10f7290510c07c34a976a3eeb45f
---

Cybersecurity researchers have disclosed details of a new China-aligned espionage campaign targeting government and defense sectors across South, East, and Southeast Asia, along with one European government belonging to NATO.

Trend Micro has attributed the activity to a threat activity cluster it tracks under the temporary designation
**SHADOW-EARTH-053**
. The adversarial collective is assessed to be active since at least December 2024, while sharing some level of network overlap with
[CL-STA-0049, Earth Alux, and REF7707](https://thehackernews.com/2025/12/china-linked-ink-dragon-hacks.html)
.

"The group exploits N-day vulnerabilities in internet-facing Microsoft Exchange and Internet Information Services (IIS) servers (e.g.,
[ProxyLogon](https://thehackernews.com/2021/03/proxylogon-exchange-poc-exploit.html)
chain), then deploys web shells (
[Godzilla](https://thehackernews.com/2024/01/apache-activemq-flaw-exploited-in-new.html)
) for persistent access and stages
[ShadowPad](https://thehackernews.com/2025/11/shadowpad-malware-actively-exploits.html)
implants via DLL sideloading of legitimate signed executables," security researchers Daniel Lunghi and Lucas Silva
[said](https://www.trendmicro.com/en_us/research/26/d/inside-shadow-earth-053.html)
in an analysis.

Targets of the campaigns include Pakistan, Thailand, Malaysia, India, Myanmar, Sri Lanka, and Taiwan. The lone European country that features in the threat actor's victimology footprint is Poland.

The cybersecurity vendor said it observed nearly half the SHADOW-EARTH-053 targets, particularly those in Malaysia, Sri Lanka, and Myanmar, also compromised earlier by a related intrusion set dubbed SHADOW-EARTH-054, although no evidence of direct operational coordination has been observed.

The starting point of the attacks is the exploitation of known security flaws to breach unpatched systems and drop web shells like Godzilla to facilitate persistent remote access. The web shells function as a delivery vehicle for command execution, enabling reconnaissance and ultimately resulting in the deployment of the ShadowPad backdoor via AnyDesk. The malware is launched using DLL side-loading.

In at least one case, the weaponization of the
[React2Shell](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html)
(CVE-2025-55182) is said to have facilitated the distribution of a Linux version of
[Noodle RAT](https://thehackernews.com/2024/06/new-cross-platform-malware-noodle-rat.html)
(aka ANGRYREBEL and Nood RAT). It's worth mentioning here that the Google Threat Intelligence Group (GTIG) linked this attack chain to a group known as UNC6595.

Also put to use are
[open-source tunneling tools](https://thehackernews.com/2026/02/asian-state-backed-group-tgr-sta-1030.html)
like the IOX, GO Simple Tunnel (GOST), and Wstunnel, as well as
[RingQ](https://thehackernews.com/2024/08/new-windows-backdoor-bitsloth-exploits.html)
to pack malicious binaries and evade detection. To facilitate privilege escalation, SHADOW-EARTH-053 has been found to use Mimikatz, while lateral movement is accomplished using a custom remote desktop protocol (RDP) launcher and C# implementation of SMBExec known as
[Sharp-SMBExec](https://github.com/checkymander/Sharp-SMBExec/)
.

"The primary entry vector used in this campaign were vulnerabilities in internet-facing IIS applications," Trend Micro said. "Organizations should prioritize applying the latest security updates and cumulative patches to Microsoft Exchange and any web applications hosted on IIS."

"In scenarios where immediate patching is not feasible, we strongly recommend deploying Intrusion Prevention Systems (IPS) or Web Application Firewalls (WAF) with rulesets specifically tuned to block exploit attempts against these known CVEs (Virtual Patching)."

### GLITTER CARP and SEQUIN CARP Go After Activists and Journalists

The disclosure comes as the Citizen Lab flagged a new phishing campaign undertaken by two distinct China-affiliated threat actors targeting and impersonating journalists and civil society, including Uyghur, Tibetan, Taiwanese, and Hong Kong diaspora activists. The wide-ranging campaigns were first detected in April and June 2025, respectively.

The clusters have been codenamed
**GLITTER CARP**
, which has singled out the International Consortium of Investigative Journalists (ICIJ), and
**SEQUIN CARP**
, whose main target was ICIJ journalist Scilla Alecci and other international journalists writing about topics of critical interest to the Chinese government.

"The actor employs well-thought-out digital impersonation schemes in phishing emails, including impersonation of known individuals and tech company security alerts," the Citizen Lab
[said](https://citizenlab.ca/research/how-chinese-actors-use-impersonation-and-stolen-narratives-to-perpetuate-digital-transnational-repression/)
. "Although the targeted groups vary, this activity employs the same infrastructure and tactics across all cases, frequently reusing the same domains and same impersonated individuals across multiple targets."

GLITTER CARP, besides conducting broad-scale phishing attacks, has been tied to phishing campaigns targeting the Taiwanese semiconductor industry. Some aspects of these efforts were
[previously documented](https://thehackernews.com/2025/07/chinese-hackers-target-taiwans.html)
by Proofpoint in July 2025 under the name UNK\_SparkyCarp. SEQUIN CARP, on the other hand, shares similarities with a group tracked by Volexity as
[UTA0388](https://thehackernews.com/2025/10/from-healthkick-to-govershell-evolution.html)
and an intrusion set detailed by Trend Micro as
[TAOTH](https://thehackernews.com/2025/08/abandoned-sogou-zhuyin-update-server.html)
.

The end goal of the campaigns is to obtain initial access to email-based accounts via credential harvesting, phishing pages, or by socially engineering the target into granting access to a third-party OAuth token. GLITTER CARP's phishing emails also involve the use of 1x1 tracking pixels that point to a URL on the attacker's domain to gather device information and confirm if they were opened by the recipients.

The Citizen Lab said it "observed concurrent targeting of specific organizations using both the AiTM phishing kit (GLITTER CARP, UNK\_SparkyCarp) and the delivery of HealthKick using different phishing tactics by a separate group (UNK\_DropPitch)." This indicates some level of overlap between these groups, it added, although the precise nature of the relationship remains unknown.

"Our analysis of the GLITTER CARP and SEQUIN CARP attacks shows that digital transnational repression increasingly operates through a distributed network of actors," the research unit said. "The targets we identified in both GLITTER CARP and SEQUIN CARP align with the intelligence priorities of the Chinese government."

"The breadth of targeting documented in this report and by others, combined with the available information on China's past and current use of contractors which mirrors the activity we have observed, suggests with a medium level of confidence that commercial entities hired by the Chinese state may have been behind both clusters of activity described here."