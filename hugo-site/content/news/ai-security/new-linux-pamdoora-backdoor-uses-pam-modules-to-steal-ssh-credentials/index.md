---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-05-14T02:28:39.449193+00:00'
exported_at: '2026-05-14T02:28:42.927552+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
structured_data:
  about: []
  author: ''
  description: PamDOORa Linux backdoor abuses PAM modules for SSH persistence and
    credential theft, increasing Linux server compromise risks.
  headline: New Linux PamDOORa Backdoor Uses PAM Modules to Steal SSH Credentials
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/05/new-linux-pamdoora-backdoor-uses-pam.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Linux PamDOORa Backdoor Uses PAM Modules to Steal SSH Credentials
updated_at: '2026-05-14T02:28:39.449193+00:00'
url_hash: ebf40297105237f0441f16ef1c4acdfd46fcfa80
---

**

Ravie Lakshmanan
**

May 08, 2026

Malware / Threat Intelligence

Cybersecurity researchers have disclosed details of a new Linux backdoor named
**PamDOORa**
that's being advertised on the Rehub Russian cybercrime forum for $1,600 by a threat actor called "darkworm."

The backdoor is designed as a Pluggable Authentication Module (
[PAM](https://www.redhat.com/en/blog/pluggable-authentication-modules-pam)
)-based post-exploitation toolkit that enables persistent SSH access by means of a magic password and specific TCP port combination. It's also capable of harvesting credentials from all legitimate users who authenticate through the compromised system.

"The tool, called PamDOORa, is a new PAM-based backdoor, designed to serve as a post-exploitation backdoor, enabling authentication to servers via OpenSSH," Flare.io researcher Assaf Morag
[said](https://flare.io/learn/resources/blog/pamdoora-new-linux-pam-based-backdoor-sale-dark-web)
in a technical report. "Allegedly this would remain persistent on Linux systems (x86\_64)."

PamDOORa is the second Linux backdoor after
[Plague](https://thehackernews.com/2025/08/new-plague-pam-backdoor-exposes.html)
to be discovered targeting the PAM stack over the past year. PAM is a security framework in Unix/Linux operating systems that grants system administrators the ability to incorporate multiple authentication mechanisms or update them (e.g., switching from passwords to biometrics) into an existing system through the use of pluggable modules without the need for rewriting existing applications.

Because PAM modules typically run with
[root privileges](https://www.cyberark.com/resources/endpoint-privilege-security/plague-malware-exploits-pluggable-authentication-module-to-breach-linux-systems)
, a compromised, misconfigured, or malicious module can introduce significant security risks and open the door to credential harvesting and unauthorized access.

"Despite its strengths, the Pluggable Authentication Module's (PAM) modularity introduces risks, as malicious modifications to PAM modules can create backdoors or steal user credentials, especially since PAM does not store passwords but transmits values in plaintext," Group-IB
[noted](https://www.group-ib.com/blog/pluggable-authentication-module/)
in September 2024.

"The pam\_exec module, which allows the execution of external commands, can be exploited by attackers to gain unauthorized access or establish persistent control by injecting malicious scripts into PAM configuration files."

The Singaporean security vendor also detailed how it's possible to manipulate PAM configuration for SSH authentication to execute a script via pam\_exec, effectively allowing a bad actor to obtain a privileged shell on a host and facilitate stealthy persistence.

The latest findings from Flare.io show that PamDOORa, besides enabling credential theft, incorporates anti-forensic capabilities to methodically tamper with authentication logs to erase traces of malicious activity.

Although there is no evidence that the malware has been put to use in real-world attacks, infection chains distributing the malware are likely to involve the adversary first obtaining root access to the host through some other means and deploying the PamDOORa PAM module to capture credentials and establish persistent access over SSH.

Morag told The Hacker News that PamDOORa was compared with several similar PAM-based backdoors, including Plague. Although they share a similar approach of altering the PAM behavior to enable credential capture, the "small differences in the design" indicate that the backdoor does not overlap with any of them. "But without comparing the two binaries, we cannot completely rule out," Morag added.

After an initial asking price of $1,600 on March 17, 2026, the "darkworm" persona has since reduced it by almost 50% to $900 as of April 9, indicating either a lack of buyer interest or an intent to accelerate a sale.

"PamDOORa represents an evolution over existing open-source PAM backdoors," Morag explained. "While the individual techniques (PAM hooks, credential capture, log tampering) are well-documented, the integration into a cohesive, modular implant with anti-debugging, network-aware triggers, and a builder pipeline places it closer to operator-grade tooling than the crude proof-of-concept scripts found in most public repositories."