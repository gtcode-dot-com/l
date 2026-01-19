---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-01-19T14:15:14.280308+00:00'
exported_at: '2026-01-19T14:15:16.581952+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/01/new-stackwarp-hardware-flaw-breaks-amd.html
structured_data:
  about: []
  author: ''
  description: StackWarp is a hardware flaw affecting AMD Zen 1–5 CPUs that allows
    privileged hosts to execute code inside SEV-SNP confidential virtual machines.
  headline: New StackWarp Hardware Flaw Breaks AMD SEV-SNP Protections on Zen 1–5
    CPUs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/01/new-stackwarp-hardware-flaw-breaks-amd.html
  publisher:
    logo: /favicon.ico
    name: gtcode.com
title: New StackWarp Hardware Flaw Breaks AMD SEV-SNP Protections on Zen 1–5 CPUs
updated_at: '2026-01-19T14:15:14.280308+00:00'
url_hash: 56aec2cf0f79061a1544659968dd287ab6040d62
---

**

Ravie Lakshmanan
**

Jan 19, 2026

Hardware Security / Vulnerability

A team of academics from the CISPA Helmholtz Center for Information Security in Germany has disclosed the details of a new hardware vulnerability affecting AMD processors.

The security flaw, codenamed
**StackWarp**
, can allow bad actors with privileged control over a host server to run malicious code within confidential virtual machines (CVMs), undermining the integrity guarantees provided by AMD Secure Encrypted Virtualization with Secure Nested Paging (
[SEV-SNP](https://thehackernews.com/2025/10/rmpocalypse-single-8-byte-write.html)
). It impacts AMD Zen 1 through Zen 5 processors.

"In the context of SEV-SNP, this flaw allows malicious VM [virtual machine] hosts to manipulate the guest VM's
[stack pointer](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)#Hardware_stack)
," researchers Ruiyi Zhang, Tristan Hornetz, Daniel Weber, Fabian Thomas, and Michael Schwarz
[said](https://stackwarpattack.com/)
. "This enables hijacking of both control and data flow, allowing an attacker to achieve remote code execution and privilege escalation inside a confidential VM."

AMD, which is tracking the vulnerability as
[CVE-2025-29943](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3027.html)
(CVSS v4 score: 4.6), characterized it as a medium-severity, improper access control bug that could allow an admin-privileged attacker to alter the configuration of the CPU pipeline, causing the stack pointer to be corrupted inside an SEV-SNP guest.

The issue affects the following product lines -

* AMD EPYC 7003 Series Processors
* AMD EPYC 8004 Series Processors
* AMD EPYC 9004 Series Processors
* AMD EPYC 9005 Series Processors
* AMD EPYC Embedded 7003 Series Processors
* AMD EPYC Embedded 8004 Series Processors
* AMD EPYC Embedded 9004 Series Processors
* AMD EPYC Embedded 9005 Series Processors

While SEV is designed to encrypt the memory of protected VMs and is intended to isolate them from the underlying hypervisor, the new findings from CISPA show that the safeguard can be bypassed without reading the VM's plaintext memory by instead targeting a microarchitectural optimization called stack engine, responsible for accelerated stack operations.

"The vulnerability can be exploited via a previously undocumented control bit on the hypervisor side," Zhang said in a statement shared with The Hacker News. "An attacker running a hyperthread in parallel with the target VM can use this to manipulate the position of the stack pointer inside the protected VM."

This, in turn, enables redirection of program flow or manipulation of sensitive data. The StackWarp attack can be used to expose secrets from SEV-secured environments and compromise VMs hosted on AMD-powered cloud environments. Specifically, it can be exploited to recover an RSA-2048 private key from a single faulty signature, effectively getting around OpenSSH password authentication and sudo's password prompt, and attain kernel-mode code execution in a VM.

The chipmaker released microcode updates for the vulnerability in July and October 2025, with AGESA patches for EPYC Embedded 8004 and 9004 Series Processors scheduled for release in April 2026.

The development builds upon a prior study from CISPA that detailed
[CacheWarp](https://thehackernews.com/2023/11/cachewarp-attack-new-vulnerability-in.html)
(CVE-2023-20592, CVSS v3 score:m 6.5), a software fault attack on AMD SEV-SNP, which permits attackers to hijack control flow, break into encrypted VMs, and perform privilege escalation inside the VM. It's worth noting that both are hardware architectural attacks.

"For operators of SEV-SNP hosts, there are concrete steps to take: First, check whether hyperthreading is enabled on the affected systems. If it is, plan a temporary disablement for CVMs that have particularly high integrity requirements," Zhang said. "At the same time, any available microcode and firmware updates from the hardware vendors should be installed. StackWarp is another example of how subtle microarchitectural effects can undermine system-level security guarantees."