---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-03-13T10:15:13.830344+00:00'
exported_at: '2026-03-13T10:15:16.160128+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/03/nine-crackarmor-flaws-in-linux-apparmor.html
structured_data:
  about: []
  author: ''
  description: Nine CrackArmor flaws in Linux AppArmor since 2017 enable root escalation
    and container bypass, putting 12.6M systems at risk.
  headline: Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass
    Container Isolation
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/03/nine-crackarmor-flaws-in-linux-apparmor.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Nine CrackArmor Flaws in Linux AppArmor Enable Root Escalation, Bypass Container
  Isolation
updated_at: '2026-03-13T10:15:13.830344+00:00'
url_hash: 4791d205271970dbf9947ac6cba53f2394668150
---

**

Ravie Lakshmanan
**

Mar 13, 2026

Linux / Vulnerability

Cybersecurity researchers have disclosed multiple security vulnerabilities within the Linux kernel's
[AppArmor](https://apparmor.net/)
module that could be exploited by unprivileged users to circumvent kernel protections, escalate to root, and undermine container isolation guarantees.

The nine confused deputy vulnerabilities have been collectively codenamed
**CrackArmor**
by the Qualys Threat Research Unit (TRU). The cybersecurity company said the issue has existed since 2017. No CVE identifiers have been assigned to the shortcomings.

AppArmor is a Linux security module that provides mandatory access control (MAC) and secures the operating system against external or internal threats by preventing known and unknown application flaws from being exploited. It has been included in the mainline Linux kernel since version 2.6.36.

"This 'CrackArmor' advisory exposes a
[confused deputy flaw](https://cwe.mitre.org/data/definitions/441.html)
allowing unprivileged users to manipulate security profiles via pseudo-files, bypass user-namespace restrictions, and execute arbitrary code within the kernel," Saeed Abbasi, senior manager of Qualys TRU,
[said](https://blog.qualys.com/vulnerabilities-threat-research/2026/03/12/crackarmor-critical-apparmor-flaws-enable-local-privilege-escalation-to-root)
.

"These flaws facilitate local privilege escalation to root through complex interactions with tools like Sudo and Postfix, alongside denial-of-service attacks via stack exhaustion and Kernel Address Space Layout Randomization (KASLR) bypasses via out-of-bounds reads."

[Confused deputy vulnerabilities](https://blog.qualys.com/vulnerabilities-threat-research/2025/07/24/fortifying-your-cloud-against-cross-service-confused-deputy-attacks)
occur when a privileged program is coerced by an unauthorized user into misusing its privileges to perform unintended, malicious actions. The problem essentially exploits the trust associated with a more-privileged tool to execute a command that leads to privilege escalation.

Qualys said an entity that doesn't have permissions to perform an action can manipulate AppArmor profiles to disable critical service protections or enforce deny-all policies, triggering denial-of-service (DoS) attacks in the process.

"Combined with kernel-level flaws inherent in profile parsing, attackers bypass user-namespace restrictions and achieve Local Privilege Escalation (LPE) to full root," it added.

"Policy manipulation compromises the entire host, while namespace bypasses facilitate advanced kernel exploits such as arbitrary memory disclosure. DoS and LPE capabilities result in service outages, credential tampering via passwordless root (e.g., /etc/passwd modification), or KASLR disclosure, which enables further remote exploitation chains."

To make matters worse, CrackArmor enables unprivileged users to create fully‑capable user namespaces, effectively getting around Ubuntu's
[user namespace restrictions](https://ubuntu.com/blog/ubuntu-23-10-restricted-unprivileged-user-namespaces)
implemented via AppArmor, as well as subvert critical security guarantees like container isolation, least‑privilege enforcement, and service hardening.

The cybersecurity company said it's withholding the release of proof-of-concept (PoC) exploits for the identified flaws to give users some time to prioritize patches and minimize exposure.

The problem affects all Linux kernels since version 4.11 on any distribution that integrates AppArmor. With more than 12.6 million enterprise Linux instances operating with AppArmor enabled by default in several major distributions, such as Ubuntu, Debian, and SUSE, immediate kernel patching is advised to mitigate these vulnerabilities.

"Immediate kernel patching remains the non-negotiable priority for neutralizing these critical vulnerabilities, as interim mitigation does not offer the same level of security assurance as restoring the vendor-fixed code path," Abbasi noted.