---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-15T04:28:51.697923+00:00'
exported_at: '2026-11-15T04:28:53.269591+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
structured_data:
  about: []
  author: ''
  description: Google Cloud says AMD Turin VMs need OS patches and a stop-start cycle
    to mitigate three CPU side-channel flaws that could expose process data.
  headline: Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes
    in VMs
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/11/google-cloud-warns-three-amd-turin-cpu.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Google Cloud Warns Three AMD Turin CPU Flaws Could Leak Data Across Processes
  in VMs
updated_at: '2026-11-15T04:28:51.697923+00:00'
url_hash: 5af74d5ce665225df419dc5f091137a50fa1bd22
---

**

Swati Khandelwal
**

Nov 12, 2026

Vulnerability / Cloud Security

Google Cloud VMs on AMD Turin chips need a guest OS patch and a stop-and-start to protect against three CPU side-channel flaws, Google said this week.

The company has already applied mitigations against attacks between VMs, and between VMs and the host. Inside a VM, the flaws may let an attacker with code on the same processor core infer data from other processes or the kernel.

The affected machine series are C4D, N4D, H4D, Z4D,, and G4, including bare-metal instances of C4D and Z4D. Turin is the code name for fifth-generation AMD EPYC processors.

All three flaws are Transient Scheduler Attacks (TSA). Two of them, TSA-SQ (CVE-2024-36350) and TSA-L1 (CVE-2024-36357), were first disclosed on July 8, 2025, for earlier EPYC processors.

AMD now says its Zen 5 processors, which include Turin, are "impacted differently from previously characterized AMD processors." The third flaw, CVE-2026-0004, is new. It may let an attacker who can run code on a system infer data in the processor's L1 data cache.

The Xen Project, which maintains the Xen hypervisor, calls the new flaw TSA-Fill. It also says an earlier statement has been corrected: "AMD had previously said that Zen5 CPUs were not vulnerable to TSA-SQ and TSA-L1."

Google rates the issue Medium. AMD classifies all three as local attacks with high attack complexity that require only low privileges, according to its
[Zen 5 bulletin](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7073.html)
and
[CVE-2026-0004 advisory](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3055.html)
.

As of today, none of the three is in the KEV catalog of exploited flaws kept by the U.S. Cybersecurity and Infrastructure Security Agency. Neither company reports any exploitation in its bulletins.

### What Google Cloud Customers Need to Do

Google's
[security bulletin](https://docs.cloud.google.com/support/bulletins#gcp-2026-081)
gives these steps for each service:

* **VMs:**
  Install your OS vendor's fix when it ships. Starting this week, the company will update the CPU information that VMs report, so a patched guest kernel can turn on its mitigations. After that update reaches a VM, stop and start it. As the company puts it: "Rebooting the guest OS isn't enough."
* **Bare metal instances:**
  If you run your own OS or hypervisor on a C4D or Z4D bare metal instance, apply your vendor's fixes when they are available.
* **Hypervisors inside a VM:**
  The same CPU information update applies, so patched guest kernels can turn on their mitigations. Stop and start the VM once the update arrives.
* **GKE:**
  Updated node images for Turin-based bare metal instances will be made available, and upgrading nodes picks up the CPU information update. As of today, the bulletin does not yet list them as available.
* **Cloud Run:**
  No action is needed.

Customers on older Rome, Milan, and Genoa processors got the same stop-and-start instruction in an
[earlier bulletin](https://docs.cloud.google.com/support/bulletins#gcp-2025-037)
at the time of the
[original disclosure](https://thehackernews.com/2025/07/amd-warns-of-new-transient-scheduler.html)
on July 8, 2025.

The company lists nothing to do in the meantime for VMs whose OS vendor has not yet shipped a fix. It also does not say how to tell when the CPU information update has reached a VM.

A
[kernel commit](https://git.kernel.org/linus/cf27412f19c9cc5909b9107cd1b3f4ab7608e362)
that mitigates TSA on Zen 5, including the new variant, is in the Linux kernel source tree. As of today, Debian has fixed CVE-2026-0004 in its Linux kernel only in its unstable branch. Its
[security tracker](https://security-tracker.debian.org/tracker/CVE-2026-0004)
still lists the kernels in bookworm, trixie, and forky as vulnerable.

For Turin servers on your own hardware, AMD says both platform firmware and OS updates are needed to mitigate the flaws fully. The mitigation may affect performance, and administrators should weigh the risk to their own workloads, according to its
[technical guidance](https://www.amd.com/content/dam/amd/en/documents/resources/bulletin/technical-guidance-for-mitigating-transient-scheduler-attacks.pdf)
.

The Xen Project has published hypervisor patches in its
[Xen advisory](https://xenbits.xen.org/xsa/advisory-525.html)
. It says microcode for all TSA flaws on Zen 5 has been in linux-firmware since September 23.

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.