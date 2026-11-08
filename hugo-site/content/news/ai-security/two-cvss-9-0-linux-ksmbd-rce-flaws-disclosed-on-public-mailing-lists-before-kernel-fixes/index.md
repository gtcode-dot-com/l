---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-11-08T05:29:43.391292+00:00'
exported_at: '2026-11-08T05:29:44.136900+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
structured_data:
  about: []
  author: ''
  description: Two CVSS 9.0 flaws in Linux KSMBD could enable remote code execution;
    one needs no authentication, and neither has a mainline fix.
  headline: Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before
    Kernel Fixes
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/10/two-cvss-90-linux-ksmbd-rce-flaws.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: Two CVSS 9.0 Linux KSMBD RCE Flaws Disclosed on Public Mailing Lists Before
  Kernel Fixes
updated_at: '2026-11-08T05:29:43.391292+00:00'
url_hash: eebdb3f4f6ae3ff939e7e17874e18477e315be74
---

Linux servers running KSMBD, the kernel's built-in SMB server, are exposed to two publicly reported remote code execution flaws rated 9.0 by
[Trend Micro's Zero Day Initiative](https://www.zerodayinitiative.com/advisories/upcoming)
, with no fix yet in the mainline kernel.

One of them, ZDI-CAN-33774, can be triggered before any network authentication. The other, ZDI-CAN-33549, requires the SMB Direct transport and an RDMA-capable network interface.

[ZDI-CAN-33549](https://lore.kernel.org/lkml/BYAPR01MB3830472B5702C089B0BBB77D80662@BYAPR01MB3830.prod.exchangelabs.com/)
is an integer underflow in KSMBD's SMB Direct path. A client can supply RDMA buffer descriptors in which the first is longer than the declared payload, causing the server's size counter to wrap and allowing a subsequent memory copy to overrun the end of an allocated buffer.

It requires three things: an RDMA-capable interface (hardware or the rxe software driver), a writable KSMBD share, and a client negotiating SMB Direct.

[ZDI-CAN-33774](https://lore.kernel.org/lkml/BYAPR01MB383076AC412E19C48CFBEAE980662@BYAPR01MB3830.prod.exchangelabs.com/)
requires no authentication, exposing any server running KSMBD on port 445. The flaw is a race in how KSMBD assigns its handler table: a burst of short SMB1 packets followed by an SMB2 packet in the same TCP write causes workers to handle SMB1 data with an SMB2 handler, reading past the end of the shorter buffer. A path to writing past the buffer also exists once an attacker has access to a share.

As of Thursday, neither flaw had a named fix in the mainline kernel or in
[linux-next](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/log/fs/smb)
, the integration tree that feeds it.
[Linux news site Phoronix](https://www.phoronix.com/news/LKML-New-Trend-Vulnerabilities)
said SMB Direct maintainer Stefan Metzmacher submitted a fix for ZDI-CAN-33549 targeting the next kernel development cycle, but this had not been confirmed elsewhere.

Fixes to mainline typically take weeks to reach stable branches and distribution kernels after that. Neither flaw has a CVE identifier, since the
[kernel project](https://docs.kernel.org/process/cve.html)
assigns those only after a stable-tree fix is available.

Running systemctl status ksmbd or lsmod | grep ksmbd confirms whether the module is active. Red Hat Enterprise Linux does not include KSMBD by default,
[according to Red Hat's support documentation](https://access.redhat.com/solutions/6991749)
.

The ZDI reports credit TrendAI, Trend Micro's AI scanner, as the finder. The Linux kernel's
[security documentation](https://docs.kernel.org/process/security-bugs.html)
, updated in May 2026 following
[guidance from Linus Torvalds](https://lwn.net/Articles/1073193/)
, states that bugs found by AI tools are, by definition, already public and should be sent to subsystem developer lists.

ZDI's routing appeared to follow that logic, copying public mailing lists alongside the private kernel security address without attaching patches to any of the reports.

Stable-kernel maintainer Greg Kroah-Hartman replied to three of the five kernel reports within minutes of each other. To the
[report on the VMware GPU driver](https://lore.kernel.org/dri-devel/2026102254-protector-seventy-6454@gregkh/)
, he wrote: "For some reason you sent this to public lists, and did not include a patch, so there's not much we can do with this." On the
[NVMe driver report](https://lore.kernel.org/all/2026102226-duly-imprison-a2c1@gregkh/)
, seventeen seconds later: "Again, no patch, and sent to a public list? Please fix your submission process."

| ZDI ID | Subsystem | Flaw class | CVSS | Affects KSMBD? |
| --- | --- | --- | --- | --- |
| [ZDI-CAN-33549](https://lore.kernel.org/lkml/BYAPR01MB3830472B5702C089B0BBB77D80662@BYAPR01MB3830.prod.exchangelabs.com/) | KSMBD SMB Direct | Remote code execution | 9.0 | Yes (SMB Direct and RDMA required) |
| [ZDI-CAN-33774](https://lore.kernel.org/lkml/BYAPR01MB383076AC412E19C48CFBEAE980662@BYAPR01MB3830.prod.exchangelabs.com/) | KSMBD protocol dispatch | Remote code execution | 9.0 | Yes (any KSMBD install) |
| [ZDI-CAN-33367](https://lore.kernel.org/lkml/BYAPR01MB3830CECF5D0871064C59BA0280662@BYAPR01MB3830.prod.exchangelabs.com/) | Networking (skb\_zerocopy) | Local privilege escalation | 7.8 | No |
| ZDI-CAN-34068 | VMware GPU driver (vmwgfx) | Local privilege escalation | 8.8 | No |
| ZDI-CAN-34076 | NVMe target driver (nvmet) | Information disclosure | 8.6 | No |

Three of the five kernel reports are not related to SMB.
[ZDI-CAN-33367](https://lore.kernel.org/lkml/BYAPR01MB3830CECF5D0871064C59BA0280662@BYAPR01MB3830.prod.exchangelabs.com/)
, discovered by researcher
**p1r0x**
, is a local privilege escalation in the kernel's networking stack that requires local access. ZDI-CAN-34068 is a local privilege escalation in the VMware virtual GPU driver, ZDI-CAN-34076 is an information disclosure in the NVMe target driver, and neither affects KSMBD servers.

A sixth ZDI report, ZDI-CAN-32005, is a
[buffer overflow in ConnMan](https://lore.kernel.org/all/BYAPR01MB383046745372577D8F5902D580672@BYAPR01MB3830.prod.exchangelabs.com/)
, a network daemon separate from the Linux kernel.

### Update: Public Exploit for ZDI-CAN-33367 Gains Root on Major Distributions

ZDI-CAN-33367, the lowest-rated of the five kernel reports, is the only one with public exploit code shown to reach root. The report was posted to the public lists together with the source code of a working proof-of-concept,
[according to AlmaLinux](https://almalinux.org/blog/2026-10-23-zdi-can-33367/)
, and
[CloudLinux](https://blog.cloudlinux.com/zdi-can-33367)
said its kernel team used that code to get root on AlmaLinux 8, 9 and 10, CloudLinux 9 and 10, Debian 12 and 13, and Ubuntu 24.04 and 26.04. CentOS 6 and 7 kernels are not affected.

The flaw lets an ordinary local user change the kernel's in-memory copy of files they are only allowed to read, such as setuid programs or /etc/passwd, which is enough to take over the machine. It works because skb\_zerocopy() drops a marker that tells the kernel's IPsec code not to decrypt shared memory pages in place. That marker was added by this year's fix for Dirty Frag (CVE-2026-43284), so kernels carrying that fix are still exposed, CloudLinux said.

The exploit needs unprivileged user namespaces, which let an ordinary account act as administrator of its own private network setup, and a set of networking modules that affected kernels ship. AlmaLinux allows such namespaces by default. Ubuntu's AppArmor restriction on them did not stop the exploit,
[Sysdig](https://www.sysdig.com/blog/detecting-and-mitigating-zdi-can-33367-and-five-other-linux-flaws)
reported.

An
[upstream fix](https://lore.kernel.org/all/20261022104217.1852191-1-pointerliu@126.com/)
written by Zizhen Liu and reviewed by netdev maintainer Eric Dumazet was posted on October 22. It had not been merged as of 14:59 UTC on Friday, October 23, according to CloudLinux, and Sysdig reported on Saturday that it was still unmerged and that none of the six reports had a CVE. AlmaLinux backported the fix ahead of a Red Hat update and placed patched kernels for AlmaLinux 8, 9 and 10 in its testing repository on Friday. CloudLinux released a KernelCare live patch, which applies without a reboot, for CloudLinux 10 and AlmaLinux 10 the same day, with CloudLinux 9 in review and CloudLinux 8 in progress.

Until fixed kernels arrive, CloudLinux and Sysdig advise setting user.max\_user\_namespaces to 0 on hosts that do not need unprivileged user namespaces. The setting applies without a reboot but stops rootless containers, Flatpak and some browser sandboxes from working for ordinary accounts, and CloudLinux said it had not yet tested the setting against the exploit. Running sysctl user.max\_user\_namespaces prints 0 when the path is closed. AlmaLinux recommends blocking the esp4 and esp6 kernel modules as a stopgap on systems that do not use IPsec. Sysdig said on Saturday that no exploitation in the wild had been reported.

### Update: Maintainers Point to Existing Fixes for Both KSMBD Flaws

KSMBD maintainer Namjae Jeon replied on the ZDI-CAN-33774 thread that the race is already fixed by commit 68f410faedaf, which he wrote on September 30 and credited to a different reporter. The commit sits in his ksmbd-for-next branch and had not reached a released kernel as of Saturday, Sysdig reported. For ZDI-CAN-33549, Metzmacher asked the reporter on October 21 to test his branch for Linux 7.5, saying he believes the flaw is already fixed there. That had not been confirmed as of Saturday.

The public proof-of-concept code for the two KSMBD flaws shows a kernel memory leak and crashes, not code execution, according to CloudLinux and Sysdig. The ZDI-CAN-33774 code leaks 28 bytes of kernel heap memory per attempt before authentication and can crash the kernel. ZDI's report also describes a path to writing past the buffer, but nothing public shows it leading to code execution, Sysdig said. KSMBD is not built into the AlmaLinux and CloudLinux 9 and 10 kernels, and on Debian and Ubuntu it runs only after an administrator installs ksmbd-tools and starts the service, CloudLinux said.

*(The story was updated after publication on October 26, 2026, to include the public exploit for ZDI-CAN-33367 and the maintainers' fix status for the two KSMBD flaws.)*

Found this article interesting? Follow us on
[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ)
,
[Twitter](https://twitter.com/thehackersnews)
and
[LinkedIn](https://www.linkedin.com/company/thehackernews/)
to read more exclusive content we post.