---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T07:13:59.907793+00:00'
exported_at: '2026-11-15T07:14:01.557531+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html
structured_data:
  about: []
  author: ''
  description: Mior and Skyfall attacks expose data in AMD SEV-SNP confidential VMs,
    with Mior also enabling memory changes and forged attestation reports.
  headline: New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From
    AMD SEV-SNP VMs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/new-mior-and-skyfall-attacks-let-rogue.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Mior and Skyfall Attacks Let Rogue Cloud Hosts Steal Secrets From AMD SEV-SNP
  VMs
updated_at: '2026-11-15T07:13:59.907793+00:00'
url_hash: fb5ac890be2a0d2100af01bb6e89f9f7695d4d4c
---

Two attacks made public this week allow a malicious host to read data inside AMD SEV-SNP-protected virtual machines (VMs), which are built to keep the server's operator out.

One of them,
**Mior**
, can also modify a VM's memory and fake the signed report confirming which software it runs. Both need control of the server's hypervisor, and Mior also needs control of the server's BIOS. Researchers showed both in lab tests on AMD EPYC server processors.

AMD, which makes the processors, lists SEV firmware for Mior and microcode for
**Skyfall**
, both dated August 12. It plans to give server makers platform firmware in November for Skyfall and in December for Mior, and fixes for embedded chips later. Customers are told to get the BIOS update from their server maker.

SEV-SNP brings confidential computing to AMD EPYC server processors. It uses hardware-enforced memory encryption and access control to protect a VM, even from the host's hypervisor.

The ETH Zurich team behind Mior attacked SEV-SNP while it was starting up. During start-up, a security co-processor on the chip, the Platform Security Processor (PSP), fills in a table called the Reverse Map Table (RMP). The RMP records who owns each page of memory and what they may do with it.

The team redirected the PSP's writes to the memory of a graphics card it controlled, instead of to main memory. The team used a card because it believes the PSP reads the values back to check them, and the card could return them. Start-up then finished without errors, but part of the real RMP, including the entry that protects the table itself, stayed uninitialized.

That let the hypervisor rewrite the RMP's protections. The team then enabled debugging on a confidential VM that had it disabled and used the PSP's own debug commands to read and write the VM's memory. This worked in all 1,000 attempts across both test runs.

SEV-SNP also measures a VM's software image when the VM starts, and the PSP signs attestation reports that include this measurement. In a second test, the team copied a harmless VM's measurement into a malicious VM, so the malicious VM's attestation reports described the harmless image instead.

The attack needs control of the hypervisor and the BIOS (also called UEFI), plus a PCIe device such as a graphics card, the
[Mior paper](https://xca-attacks.github.io/mior/mior_ccs26.pdf)
says. For the tests, the team modified the BIOS to leave the chip's memory-routing settings unlocked.

"We operate in AMD’s threat model defined for SEV-SNP. AMD explicitly distrusts the UEFI, thus an attacker can modify the UEFI," the researchers say.

Ordinary VMs already trust their host and its firmware, so Mior gives an attacker nothing new against them, the team says.

The team ran Mior on one EPYC 9135, a Zen 5 chip. It considers Zen 3 and Zen 4 chips potentially affected but did not test them because it had no setup that allowed it to change their BIOS.

The debugging and attestation tests both worked with ciphertext hiding turned on. That optional SEV-SNP feature stops the hypervisor from even reading encrypted VM memory.

Two earlier attacks by some of the same researchers, the
[Fabricked attack](https://xca-attacks.github.io/fabricked/)
and the
[RMPocalypse attack](https://thehackernews.com/2025/10/rmpocalypse-single-8-byte-write.html)
, also corrupted the RMP as SEV-SNP started up. Mior is a separate flaw, unrelated to Fabricked and to the fix for it, the team says. It also worked on older firmware from before that fix.

Skyfall comes from a team at ETH Zurich and Google. It builds on
[Transient Scheduler Attacks](https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html)
(TSA), a group of flaws in AMD processors that can leak data through instruction timing. TSA was first disclosed on July 8, 2025.

The team found that when a hypervisor intentionally causes a VM to fail to start, the processor has already cached part of the VM's saved state. That data is left behind without the usual cleanup, and the hypervisor can read it through TSA.

This way, the team recovered a VM's saved register values and a disk-encryption key from a test VM. For the key, it changed the VM's kernel to pause at the moment the key sat in registers. In a real attack, the team says, a hypervisor can instead use a technique called SEV-Step to step through the VM until the key reaches the registers.

Skyfall can also read VM memory, but only three fixed cache lines in a page it targets, at offsets 0x0c0, 0x380 and 0x3c0. The rest of the page stays out of reach.

The attack needs a malicious host or hypervisor, but no tampering with the hardware. The team tested it on an EPYC 7313, a Zen 3 chip, and on EPYC 9124 and 9334 chips, which are Zen 4. It did not show the leak on Zen 5 chips.

Beyond VMs, the Skyfall team read decrypted microcode updates on all three test chips. It also recovered register values stored in System Management Mode (SMM) memory, which even the operating system kernel normally cannot read. Both of these attacks need privileged software on the machine.

The program committee of the IEEE Symposium on Security and Privacy, which accepted the
[Skyfall paper](https://skyfall-attack.github.io/assets/skyfall.pdf)
, said it overlooks what a realistic attack on VMs would need. That includes a processor core free of other activity, failing VM starts and performance-counter reads at high speed, and a VM that does not crash or time out during the attack.

### Affected Processors and Fixes

AMD tracks Mior as CVE-2026-0462 and rates it 5.9 on the CVSS 4.0 scale in a
[security advisory](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3059.html)
. It tracks Skyfall's VM leak as CVE-2026-40671, rated 4.9, in a
[second advisory](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3061.html)
that describes the flaw as exposing VM register data.

For Mior, the company lists only SEV-SNP as affected, not the earlier SEV and SEV-ES versions.

It lists the same five EPYC server lines for both flaws, with these fixes:

As listed in the two advisories

| EPYC series | Mior platform firmware (target) | Mior SEV firmware (August 12) | Skyfall platform firmware (target) |
| --- | --- | --- | --- |
| 7003 | `MilanPI-SP3_1.0.0.L` (December) | `1.3A.03` | `MilanPI-SP3_1.0.0.L` (November) |
| 8004 | `GenoaPI_1.0.0.K` (December) | `1.3A.4` | `Genoa_100J Patch 3` (November) |
| 8005 | `TurinPI_1.0.0.C` (December) | `1.3A.0A` | `TurinPI_1.0.0.C` (November) |
| 9004 | `GenoaPI_1.0.0.K` (December) | `1.3A.4` | `Genoa_100J Patch 3` (November) |
| 9005 | `TurinPI_1.0.0.C` (December) | `1.3A.0A` | `TurinPI_1.0.0.C` (November) |

The two advisories give the same TurinPI\_1.0.0.C package different target months. Microcode for Skyfall is dated August 12 for each of these lines. The Instinct MI300A accelerator has a Skyfall patch dated September 21, and fixes for embedded EPYC models are due between January and April 2027.

The Mior team says updated firmware that mitigates the flaw is already out, and the Skyfall team says new microcode has been released. The advisories do not say whether those updates work on their own or only as part of the BIOS updates, and they list no workaround.

Supermicro, a server maker, has published a
[BIOS fix list](https://www.supermicro.com/en/support/security_AMD-SB-3059)
covering flaws in dozens of its H12, H13, and H14 motherboards. The same pages say the boards also need a BMC firmware update and that the company is still testing affected products.

Because the fixes are implemented in the host's firmware, customers who rent confidential VMs depend on their cloud provider to install them. The advisory covering Mior also lists TCB (trusted computing base) values for SNP attestation next to each fixed firmware version. It does not say how VM owners should check them.

Neither advisory says whether the flaws have been used in attacks. Both teams have published code, and the Mior
[proof-of-concept code](https://github.com/xca-attacks/mior)
needs a BIOS patched to leave the memory-routing settings unlocked.

The EDK II project assigned Skyfall's SMM leak CVE-2026-18448 and rates it 5.6. AMD's
[EDK II bulletin](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7072.html)
traces it to missing TSA mitigations in EDK II firmware code.

The bulletin lists EPYC and Ryzen chips, including embedded models, and recommends the company's earlier TSA mitigations plus an EDK II patch when one is available.

For the five EPYC server lines listed above, the bulletin lists only that patch, due in November. Platform firmware with the fix is already available for other chips, including the EPYC 4004 and 4005 models. The EDK II project's own advisory lists no patched version as of today.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.