---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-04-13T08:15:14.101743+00:00'
exported_at: '2026-04-13T08:15:16.308736+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
structured_data:
  about: []
  author: ''
  description: OpenAI revoked its macOS signing certificate after a malicious Axios
    dependency incident on March 31, 2026, preventing potential software misuse.
  headline: OpenAI Revokes macOS App Certificate After Malicious Axios Supply Chain
    Incident
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/04/openai-revokes-macos-app-certificate.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: OpenAI Revokes macOS App Certificate After Malicious Axios Supply Chain Incident
updated_at: '2026-04-13T08:15:14.101743+00:00'
url_hash: 40d14a5d72ef5bca675c2bfcded803a492a73c14
---

OpenAI revealed a GitHub Actions workflow used to sign its macOS apps, which downloaded the malicious Axios library on March 31, but noted that no user data or internal system was compromised.

"Out of an abundance of caution, we are taking steps to protect the process that certifies our macOS applications are legitimate OpenAI apps," OpenAI
[said](https://openai.com/index/axios-developer-tool-compromise/)
in a post last week. "We found no evidence that OpenAI user data was accessed, that our systems or intellectual property were compromised, or that our software was altered."

The disclosure comes a little over a week after Google Threat Intelligence Group (GTIG) attributed the
[supply chain compromise](https://thehackernews.com/2026/04/google-attributes-axios-npm-supply.html)
of the popular npm package to a North Korean hacking group it tracks as
[UNC1069](https://thehackernews.com/2026/04/unc1069-social-engineering-of-axios.html)
.

The attack enabled the threat actors to hijack the package maintainer's npm account to push two poisoned versions 1.14.1 and 0.30.4 that came embedded with a malicious dependency named "plain-crypto-js," which deployed a cross-platform backdoor called WAVESHAPER.V2 to infect Windows, macOS, and Linux systems.

The artificial intelligence (AI) company said a GitHub Actions workflow it uses as part of its macOS app-signing process downloaded and executed Axios version 1.14.1. The workflow, it added, had access to a certificate and notarization material used for signing ChatGPT Desktop, Codex, Codex CLI, and Atlas.

"Our analysis of the incident concluded that the signing certificate present in this workflow was likely not successfully exfiltrated by the malicious payload due to the timing of the payload execution, certificate injection into the job, sequencing of the job itself, and other mitigating factors," the company said.

Despite finding no evidence of data exfiltration, OpenAI said it's treating the certificate as compromised and that it's revoking and rotating it. As a result, older versions of all its macOS desktop apps will no longer receive updates or support starting May 8, 2026.

This also means that apps signed with the previous certificate will be blocked by macOS security protections by default, preventing them from being downloaded or launched. The earliest releases signed with their updated certificate are listed below -

* ChatGPT Desktop - 1.2026.071
* Codex App - 26.406.40811
* Codex CLI - 0.119.0
* Atlas - 1.2026.84.2

As part of its remediation efforts, OpenAI is also working with Apple to ensure software signed with the previous certificate cannot be newly notarized. The 30-day window till May 8, 2026, is a way to minimize user disruption and give them enough time to make sure they are updated to the latest version, it pointed out.

"In the event that the certificate was successfully compromised by a malicious actor, they could use it to sign their own code, making it appear as legitimate OpenAI software," OpenAI said. "We have stopped new software notarizations using the old certificate, so new software signed with the old certificate by an unauthorized third-party would be blocked by default by macOS security protections unless a user explicitly bypasses them."

### Two Supply Chain Attacks Rock March

The breach of Axios, one of the most widely used HTTP client libraries, was one of the two major supply chain attacks that took place in March aimed at the open-source ecosystem. The
[other incident](https://ramimac.me/teampcp/)
targeted
[Trivy](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/)
, a vulnerability scanner maintained by Aqua Security, resulting in
[cascading impacts](https://snyk.io/articles/trivy-github-actions-supply-chain-compromise/)
across five ecosystems, affecting a number of other popular libraries depending on it.

The attack, the work of a cybercriminal group called
[TeamPCP](https://thehackernews.com/2026/03/teampcp-pushes-malicious-telnyx.html)
(aka UNC6780), deployed a credential stealer dubbed SANDCLOCK that facilitated the extraction of sensitive data from developer environments. Subsequently, the threat actors weaponized the stolen credentials to compromise npm packages and push a self-propagating worm named
[CanisterWorm](https://www.stepsecurity.io/blog/canisterworm-how-a-self-propagating-npm-worm-is-spreading-backdoors-across-the-ecosystem)
.

Days later, the crew used secrets pilfered from the Trivy intrusion to inject the same malware into two GitHub Actions workflows maintained by Checkmarx. The threat actors then followed it up by publishing malicious versions of
[LiteLLM](https://docs.litellm.ai/blog/security-update-march-2026)
and
[Telnyx](https://www.akamai.com/blog/security-research/telnyx-pypi-2026-teampcp-supply-chain-attacks)
to the Python Package Index (PyPI), both of which use Trivy in their CI/CD pipeline.

"The Telnyx compromise indicates a continued change in the techniques used in TeamPCP's supply chain activity, with adjustments to tooling, delivery methods, and platform coverage," Trend Micro
[said](https://www.trendmicro.com/en_us/research/26/c/teampcp-telnyx-attack-marks-a-shift-in-tactics.html)
in an
[analysis of the attack](https://www.trendmicro.com/en_us/research/26/c/your-ai-stack-just-handed-over-your-root-keys-inside-the-litellm-pypi-breach.html)
.

"In just eight days, the actor has pivoted across security scanners, AI infrastructure, and now telecommunications tooling, evolving their delivery from inline Base64 to .pth auto-execution, and ultimately to split-file WAV steganography, while also expanding from Linux-only to dual-platform targeting with Windows persistence."

On
[Windows systems](https://www.ox.security/blog/teampcps-telnyx-windows-malware-technical-analysis/)
, the hack of the
[Telnyx Python SDK](https://x.com/TheEnergyStory/status/2038238773721325996)
resulted in the deployment of an executable named "msbuild.exe" that employs several obfuscation techniques to evade detection and extracts DonutLoader, a shellcode loader, from a PNG image present within the binary to load a full-featured trojan and a
[beacon](https://www.threatlocker.com/blog/supply-chain-attack-security-scanner-compromise-leads-to-widespread-infostealer-and-ransomware-pivot)
associated with
[AdaptixC2](https://thehackernews.com/2025/10/russian-ransomware-gangs-weaponize-open.html)
, an open-source command-and-control (C2) framework.

Additional analyses of the campaign, now identified as CVE-2026-33634, have been published by various cybersecurity vendors -

TeamPCP's supply chain compromise rampage may have come to an end, but the group has since shifted its focus towards monetizing existing credential harvests by teaming up with other financially motivated groups like Vect, LAPSUS$, and ShinyHunters. Evidence indicates that the threat actor has also launched a proprietary ransomware operation under the name CipherForce.

These efforts have been complemented by TeamPCP's use of the stolen data to access cloud and software-as-a-service (SaaS) environments, marking a new-found escalation of the campaign. To that end, the cybercrime gang has been found to verify stolen credentials using TruffleHog, launch discovery operations within 24 hours of validation, exfiltrate more data, and attempt lateral movement to gain access to the broader network.

"The credentials and secrets stolen in the supply chain compromises were quickly validated and used to explore victim environments and exfiltrate additional data," Wiz researchers
[said](https://www.wiz.io/blog/tracking-teampcp-investigating-post-compromise-attacks-seen-in-the-wild)
. "While the speed at which they were used suggests that it was the work of the same threat actors responsible for the supply chain operations, we are not able to rule out the secrets being shared with other groups and used by them."

### Attacks Ripple Through Dependencies

Google has
[warned](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package)
that "hundreds of thousands of stolen secrets" could potentially be circulating as a result of the Axios and Trivy attacks, fueling more software supply chain attacks, SaaS environment compromises, ransomware and extortion events, and cryptocurrency theft over the near term.

Two organizations that have confirmed compromise through the Trivy supply chain attack are artificial intelligence (AI) data training startup
[Mercor](https://x.com/mercor_ai/status/2039101905675403306)
and the
[European Commission](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_748)
. While the company has not shared details on the impact, the LAPSUS$ extortion group listed Mercor on its leak site, claiming to have exfiltrated about 4TB of data. The Mercor breach has led Meta to pause its work with the company, according to a
[report](https://www.wired.com/story/meta-pauses-work-with-mercor-after-data-breach-puts-ai-industry-secrets-at-risk/)
from WIRED.

Earlier this month, CERT-EU
[revealed](https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain)
that the threat actors used the stolen AWS secret to exfiltrate data from the Commission's cloud environment. This included data relating to websites hosted for up to 71 clients of the Europa web hosting service and outbound email communications. The ShinyHunters group has since released the exfiltrated dataset publicly on its dark web leak site.

GitGuardian's
[analysis](https://blog.gitguardian.com/team-pcp-snowball-analysis/)
of the Trivy and LiteLLM supply chain attacks and their spread through dependencies and automation pipelines has found that 474 public repositories executed malicious code from the compromised "trivy-action" workflow, and 1,750 Python packages were configured in a way that would automatically pull the poisoned versions.

"TeamPCP is deliberately targeting security tools that run with elevated privileges by design. Compromising them gives the attacker access to some of the most sensitive environments in the organization, because security tools are typically granted broad access by design," Brett Leatherman, assistant director of Cyber Division at the U.S. Federal Bureau of Investigation (FBI),
[wrote](https://www.linkedin.com/posts/bleatherman_fbicyber-share-7442369430245826560-IA9x/?rcm=ACoAAA98Bu8BVZIE7tjrbfEgLetF8Wf_4bWQNHc&skipRedirect=true)
on LinkedIn.

The supply chain incidents are dangerous because they take aim at the inherent trust developers assume when downloading packages and dependencies from open-source repositories. "Trust was assumed where it should have been verified," Mark Lechner, chief information security officer at Docker,
[said](https://www.docker.com/blog/defending-your-software-supply-chain-what-every-engineering-team-should-do-now/)
.

"The organizations that came through these incidents with minimal damage had already begun replacing implicit trust with explicit verification at every layer of their stack: verified base images instead of community pulls, pinned references instead of mutable tags, scoped and short-lived credentials instead of long-lived tokens, and sandboxed execution environments instead of wide-open CI runners."

Both Docker and the Python Package Index (PyPI) maintainers have
[outlined](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/)
a long list of recommendations that developers can implement to counter such attacks -

* Pin packages by digest or commit SHA instead of mutable tags.
* Use Docker Hardened Images (DHI).
* Enforce minimum release age settings to delay adoption of new versions for dependency updates.
* Treat every CI runner as a potential breach point and avoid pull\_request\_targe triggers in GitHub Actions unless absolutely necessary.
* Use short-lived, narrowly scoped credentials.
* Use an internal mirror or artifact proxy.
* Deploy canary tokens to get alerted to potential exfiltration attempts.
* Audit environment for hard-coded secrets.
* Run AI coding agents in sandboxed environments.
* Use trusted publishing to push packages to
  [npm](https://docs.npmjs.com/trusted-publishers)
  and
  [PyPI](https://docs.pypi.org/trusted-publishers/)
  .
* Secure the open-source development pipeline with two-factor authentication (2FA).

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) has also
[added](https://www.cisa.gov/news-events/alerts/2026/03/26/cisa-adds-one-known-exploited-vulnerability-catalog)
CVE-2026-33634 to its Known Exploited Vulnerabilities (
[KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
) catalog, mandating that Federal Civilian Executive Branch (FCEB) agencies apply the necessary mitigations by April 9, 2026.

"The number of recent software supply chain attacks is overwhelming," Charles Carmakal, chief technology officer of Mandiant Consulting at Google,
[said](https://www.linkedin.com/posts/charlescarmakal_cybersecurity-threatintel-supplychain-activity-7444746390288789504-rHpT/?rcm=ACoAAAAHXmsBeL1ZrOKRT8g9rCLjiQfqDSJUjk4)
. "Defenders need to pay close attention to these campaigns. Enterprises should spin up dedicated projects to assess the existing impact, remediate, and harden against future attacks."