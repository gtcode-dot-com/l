---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-06-27T03:35:18.662048+00:00'
exported_at: '2026-06-27T03:35:21.296256+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
structured_data:
  about: []
  author: ''
  description: DirtyClone, tracked as CVE-2026-43503, lets local users gain root by
    corrupting file-backed memory through cloned network packets.
  headline: New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned
    Packets
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New DirtyClone Linux Kernel Flaw Lets Local Users Gain Root via Cloned Packets
updated_at: '2026-06-27T03:35:18.662048+00:00'
url_hash: e38fba2af3c4998e506cee9ce690259cfe0af7e8
---

**

Swati Khandelwal
**

Jun 26, 2026

Linux / Vulnerability

**DirtyClone**
is a new Linux kernel privilege escalation in the
**DirtyFrag**
family. JFrog Security Research published a working exploit walkthrough for the flaw on June 25, the first public demonstration for this variant.

Tracked as
[CVE-2026-43503](https://ubuntu.com/security/CVE-2026-43503)
(CVSS 8.8), it lets a local user corrupt file-backed memory through a cloned network packet and gain root. The patch landed in mainline on May 21; if your kernel does not have it, update now.

When the kernel copies a network packet internally, two helper functions drop a safety flag that marks the packet's memory as shared with a file on disk. That missing flag is the entire vulnerability.

The attacker loads a privileged binary like /usr/bin/su into memory, wires those memory pages into a network packet, and forces the kernel to clone it. The cloned packet passes through an IPsec tunnel that the attacker controls, and the decryption step overwrites the binary's login checks with attacker-chosen bytes. The next time anyone runs su, it hands over root.

The file on disk never changes. The modification lives only in the kernel's in-memory copy, so file-integrity tools miss it, the attack leaves no audit trail, and a reboot restores the original binary. The attacker already has root by the time anyone might think to check.

Exploitation requires
**CAP\_NET\_ADMIN**
to configure the loopback IPsec tunnel. On Debian and Fedora, unprivileged user namespaces are enabled by default, so a local user can obtain that capability inside a new namespace.

Ubuntu 24.04 and later restrict namespace creation via AppArmor, blocking the default exploit path. Page cache is shared at the host level, so modifications made inside a namespace affect every process on the machine.

The exposed systems are multi-tenant servers, CI runners, container hosts, and Kubernetes clusters where untrusted users can create namespaces. JFrog
[confirmed the exploit](https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/)
on Debian, Ubuntu, and Fedora systems with default namespace configurations.

## Fourth in a Series

This is the fourth recent privilege escalation with the same failure mode: file-backed memory gets treated as packet data, then an in-place network operation writes where it should have copied.

* [Copy Fail](https://thehackernews.com/2026/04/new-linux-copy-fail-vulnerability.html)
  (CVE-2026-31431) came first in late April, exploiting the algif\_aead module for a four-byte page-cache write.
* [DirtyFrag](https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html)
  (CVE-2026-43284 and CVE-2026-43500) followed on May 7, chaining IPsec ESP and RxRPC paths for a full write primitive.
* [Fragnesia](https://thehackernews.com/2026/05/new-fragnesia-linux-kernel-lpe-grants.html)
  (CVE-2026-46300) appeared on May 13, bypassing the DirtyFrag patch through a flag-dropping bug in skb\_try\_coalesce().

Each fix closed one code path and left others open. DirtyClone's demonstrated exploit centers on \_\_pskb\_copy\_fclone(), with skb\_shift() also affected; the broader CVE fix covers additional frag-transfer helpers where the same flag could be lost.

The underlying problem is not one bad helper function. It is a contract problem: every code path that moves skb fragments has to preserve the shared-frag bit, every time.

The kernel's zero-copy networking lets file-backed memory serve as packet data, and a single dropped flag anywhere in the chain turns a performance optimization into a write primitive. Each variant found a path where the contract was not honored.

The original DirtyFrag researcher, Hyunwoo Kim, had submitted a broader
[multi-site patch](https://lore.kernel.org/netdev/ageeJfJHwgzmKXbh@v4bel/)
covering several remaining frag-transfer helpers on May 16. The combined fix was merged on May 21 (commit 48f6a5356a33), assigned CVE-2026-43503 on May 23, and shipped in Linux v7.1-rc5 on May 24.

## What to Do

Install your distribution's kernel update. The fix landed upstream in v7.1-rc5 and has been backported to stable and LTS branches.
[Ubuntu](https://ubuntu.com/security/notices/USN-8373-1)
,
[Debian](https://security-tracker.debian.org/tracker/CVE-2026-43503)
, and
[SUSE](https://www.suse.com/security/cve/CVE-2026-43503.html)
have published advisories;
[Red Hat has a Bugzilla tracking entry](https://bugzilla.redhat.com/show_bug.cgi?id=2480902)
.

If you cannot patch today, two workarounds reduce the attack surface. Restrict unprivileged user namespaces: on Debian and Ubuntu, set kernel.unprivileged\_userns\_clone=0 (other distributions use different mechanisms).

Alternatively, blacklist the esp4, esp6, and rxrpc kernel modules, though that breaks IPsec and AFS and only works when those features are loadable modules rather than compiled into the kernel. Both are temporary controls, not fixes.

The DirtyFrag class is probably not done. Any function that moves fragment descriptors without propagating the shared-frag flag is a potential new CVE, and auditing should cover every path that touches skb\_shinfo()-&gt;flags during fragment transfer.