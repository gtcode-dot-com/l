---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-02-22T06:15:15.060486+00:00'
exported_at: '2026-02-22T06:15:18.756930+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
structured_data:
  about: []
  author: ''
  description: AI-augmented actor breached 600+ FortiGate devices in 55 countries
    using weak credentials and exposed ports, Amazon reports.
  headline: AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/02/ai-assisted-threat-actor-compromises.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: AI-Assisted Threat Actor Compromises 600+ FortiGate Devices in 55 Countries
updated_at: '2026-02-22T06:15:15.060486+00:00'
url_hash: 529f7ce16c06dda07945439f0f976426a0c4f4d5
---

A Russian-speaking, financially motivated threat actor has been observed taking advantage of commercial generative artificial intelligence (AI) services to compromise over 600 FortiGate devices located in 55 countries.

That's according to new findings from Amazon Threat Intelligence, which said it observed the activity between January 11 and February 18, 2026.

"No exploitation of FortiGate vulnerabilities was observed—instead, this campaign succeeded by exploiting exposed management ports and weak credentials with single-factor authentication, fundamental security gaps that AI helped an unsophisticated actor exploit at scale," CJ Moses, Chief Information Security Officer (CISO) of Amazon Integrated Security,
[said](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/)
in a report.

The tech giant described the threat actor as having limited technical capabilities, a constraint they overcame by relying on multiple commercial generative AI tools to implement various phases of the attack cycle, such as tool development, attack planning, and command generation.

While one AI tool served as the primary backbone of the operation, the attackers also relied on a second AI tool as a fallback to assist with pivoting within a specific compromised network. The names of the AI tools were not disclosed.

The threat actor is assessed to be driven by financial gain and not associated with any advanced persistent threat (APT) with state-sponsored resources. As recently
[highlighted](https://thehackernews.com/2026/02/google-reports-state-backed-hackers.html)
by Google, generative AI tools are being increasingly adopted by threat actors to scale and accelerate their operations, even if they don't equip them with novel uses of the technology.

If anything, the emergence of AI tools illustrates how capabilities that were once off-limits to novice or technically challenged threat actors are becoming increasingly feasible, further lowering the barrier to entry for cybercrime and enabling them to come up with attack methodologies.

"They are likely a financially motivated individual or small group who, through AI augmentation, achieved an operational scale that would have previously required a significantly larger and more skilled team," Moses said.

Amazon's investigation into the threat actor's activity has revealed that they have successfully compromised multiple organizations’ Active Directory environments, extracted complete credential databases, and even targeted backup infrastructure, likely in a lead-up to ransomware deployment.

What's interesting here is that rather than devising ways to persist within hardened environments or those that had employed sophisticated security controls, the threat actor chose to drop the target altogether and move to a relatively softer victim. This indicates the use of AI as a way to bridge their skill gap for easy pickings.

Amazon said it identified publicly accessible infrastructure managed by the attackers that hosted various artifacts pertinent to the campaign. This included AI-generated attack plans, victim configurations, and source code for custom tooling. The entire modus operandi is akin to an "AI-powered assembly line for cybercrime," the company added.

At its core, the attacks enabled the threat actor to breach FortiGate appliances, allowing it to extract full device configurations that, in turn, made it possible to glean credentials, network topology information, and device configuration information.

This involved systematic scanning of FortiGate management interfaces exposed to the internet across ports 443, 8443, 10443, and 4443, followed by attempts to authenticate using commonly reused credentials. The activity was sector-agnostic, indicating automated mass scanning for vulnerable appliances. The scans originated from the IP address
[212.11.64[.]250](https://www.virustotal.com/gui/ip-address/212.11.64.250/detection)
.

The stolen data was then used to burrow deeper into targeted networks and conduct post-exploitation activities, including reconnaissance for vulnerability scanning using Nuclei, Active Directory compromise, credential harvesting, and efforts to access backup infrastructure that align with typical ransomware operations.

Data gathered by Amazon shows that the scanning activity resulted in organizational-level compromise, causing multiple FortiGate devices belonging to the same entity to be accessed. The compromised clusters have been detected across South Asia, Latin America, the Caribbean, West Africa, Northern Europe, and Southeast Asia.

"Following VPN access to victim networks, the threat actor deploys a custom reconnaissance tool, with different versions written in both Go and Python," the company said.

"Analysis of the source code reveals clear indicators of AI-assisted development: redundant comments that merely restate function names, simplistic architecture with disproportionate investment in formatting over functionality, naive JSON parsing via string matching rather than proper deserialization, and compatibility shims for language built-ins with empty documentation stubs."

Some of the other steps undertaken by the threat actor following the reconnaissance phase are listed below -

* Achieve domain compromise via
  [DCSync attacks](https://www.semperis.com/blog/dcsync-attack/)
  .
* Move laterally across the network via pass-the-hash/pass-the-ticket attacks, NTLM relay attacks, and remote command execution on Windows hosts.
* Target Veeam Backup & Replication servers to deploy credential harvesting tools and programs aimed at exploiting known Veeam vulnerabilities (e.g.,
  [CVE-2023-27532](https://thehackernews.com/2024/07/new-ransomware-group-exploiting-veeam.html)
  and
  [CVE-2024-40711](https://thehackernews.com/2024/10/critical-veeam-vulnerability-exploited.html)
  ).

Another noteworthy finding is the threat actor's pattern of repeatedly running into failures when trying to exploit anything beyond the "most straightforward, automated attack paths," with their own documentation recording that the targets had either patched the services, closed the required ports, or had no vulnerable exploitation vectors.

With Fortinet appliances becoming an
[attractive target for threat actors](https://thehackernews.com/2026/01/fortinet-patches-cve-2026-24858-after.html)
, it's essential that organizations ensure management interfaces are not exposed to the internet, change default and common credentials, rotate SSL-VPN user credentials, implement multi-factor authentication for administrative and VPN access, and audit for unauthorized administrative accounts or connections.

It's also essential to isolate backup servers from general network access, ensure all software programs are up-to-date, and monitor for unintended network exposure.

"As we expect this trend to continue in 2026, organizations should anticipate that AI-augmented threat activity will continue to grow in volume from both skilled and unskilled adversaries," Moses said. "Strong defensive fundamentals remain the most effective countermeasure: patch management for perimeter devices, credential hygiene, network segmentation, and robust detection for post-exploitation indicators."