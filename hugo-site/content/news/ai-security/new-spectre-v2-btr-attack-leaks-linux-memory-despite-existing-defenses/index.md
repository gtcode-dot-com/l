---
ai_commentary: []
ai_commentary_meta:
  content_digest: ''
  generated_at: ''
  model: ''
  prompt_version: ''
  provider: ''
category: ai-security
date: '2026-10-06T22:54:58.130021+00:00'
exported_at: '2026-10-06T22:55:00.031659+00:00'
feed: https://feeds.feedburner.com/TheHackersNews
language: en
source_url: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
structured_data:
  about: []
  author: ''
  description: Spectre BTR reuses stale JIT branch targets; Linux PoCs recover the
    root password hash within minutes on a fully patched Intel system.
  headline: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
  inLanguage: en
  keywords: []
  main_image: ''
  original_source: https://thehackernews.com/2026/09/new-spectre-v2-btr-attack-leaks-linux.html
  publisher:
    logo: /favicon.ico
    name: GTCode
title: New Spectre-v2 BTR Attack Leaks Linux Memory Despite Existing Defenses
updated_at: '2026-10-06T22:54:58.130021+00:00'
url_hash: 47cf7b5d49a9d48747bf353aac03665341877bf2
---

A group of academics from VUSec and Scuola Superiore Sant'Anna have disclosed details of a new
[Spectre](https://spectreattack.com/)
CPU vulnerability variant that affects Just-In-Time (
[JIT](https://en.wikipedia.org/wiki/Just-in-time_compilation)
) engines present in web browsers, language runtimes, and the operating system kernel, across multiple CPU vendors.

The new Spectre v2 variant has been codenamed
**[Branch Target Reuse (BTR)](https://www.vusec.net/projects/btr)**
.

"The key insight is that, while modern CPUs restore architectural code coherence after self-modification, they do not necessarily invalidate stale indirect branch prediction entries (i.e., branch targets)," researchers Sander Wiebing, Yuhui Zhu, Alessandro Biondi, and Cristiano Giuffrida said in an accompanying paper.

"In JIT engines, these stale targets can outlive the original code and later be reused when the code cache is repopulated, yielding a transient execute-after-free primitive. This allows attackers to hijack transient control flow to newly generated code at obsolete offsets, bypassing software hardening or reaching misaligned gadgets."

BTR was evaluated against SpiderMonkey (the JIT engine of Mozilla Firefox), GraalVM, and the Linux kernel's cBPF JIT, all of which have been found to be affected, although with "markedly different exploitability characteristics and leakage rates."

As a proof-of-concept, two end-to-end exploits have been devised against the Linux kernel that can be used to leak and recover the root password hash within minutes from a fully patched Intel system with default protections enabled.

Spectre
[refers](https://thehackernews.com/2024/03/ghostrace-new-data-leak-vulnerability.html)
to a class of CPU security vulnerabilities first discovered in 2017 that exploit speculative execution, a performance optimization technique that modern processors use to predict and execute instructions beforehand.

An attacker can exploit this loophole to trick a CPU into performing speculative operations that access sensitive data, and then infer that data through a cache timing side channel.

Spectre v2 is one
[specific type of the Spectre attack](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html)
that abuses indirect branch prediction in modern processors to achieve the same goals. Specifically, it poisons the CPU's branch prediction mechanism to cause a victim program to execute an indirect branch, which, in turn, causes the CPU to mispredict the branch and speculatively execute attacker-controlled code or a gadget.

Although the
[results of the misprediction](https://thehackernews.com/2025/01/new-slap-flop-attacks-expose-apple-m.html)
are discarded, an attacker can infer what the victim's speculative execution accessed by taking advantage of the cache state changes and measuring the cache changes.

VIDEO

"BTR targets JIT engines and arises from the interplay between Self-Modifying Code (SMC) and indirect branch prediction," the researchers said, adding, "JIT engines do expose exploitable transient-execution opportunities induced by SMC for the first time."

The attack presumes an attacker who is able to run unprivileged code in a JIT engine and is seeking to disclose sensitive data from the host environment. The entire sequence of actions is as follows -

* The attacker lures the JIT engine into allocating a training chunk and forces the victim branch to jump to it, thereby inserting a BTB entry referencing the current entry point.
* The attacker forces a deallocation of the training chunk and an allocation of the target chunk that partially reuses the same address.
* The attacker triggers the indirect branch again, the CPU uses the now-stale branch target buffer (BTB) entry and speculatively jumps to the old training-chunk entry point.
* The end result is control-flow hijacking and secret data disclosure.

"By redirecting control flow to an architecturally invalid entry point, the attacker can bypass Spectre hardening mitigations or execute misaligned instructions, ultimately disclosing secret data," the researchers explained.

However, a key aspect BTR hinges on is that the stale BTB entry must not be invalidated or replaced after the JIT engine frees the training chunk, and the branch predictor must select the stale BTB entry for prediction.

"This is the first example of a practical in-place Spectre-v2 attack – using the very same indirect branch for both training and testing," Giuffrida told The Hacker News via email.

"Common wisdom has always been this would be hard to pull off, because traditional Spectre-v2 attacks exploit "spatial" target violations (i.e., hijack an indirect branch target into another) and doing so for a single branch seems intuitively hard (given that you can only 'spatially' go from a valid indirect branch target to another of the same branch)."

"BTR shows this assumption is incorrect once one can mount "temporal" Spectre-v2 attacks like BTR, where the indirect branch and even the target stay the same, but the "meaning" of the target (i.e., the underlying code) changes."

The new Spectre v2 variant also undermines existing mitigations for this line of attack, including those of
[Training Solo](https://thehackernews.com/2025/05/researchers-expose-new-intel-cpu-flaws.html)
(CVE-2024-28956 and CVE-2025-24495). According to Giuffrida, the only caveat is that the scope is limited to JIT engines.

"BTR doesn't exploit any spatial violations at all," Giuffrida explained. "One indirect branch and one target is all you need for Spectre-v2 attacks, as long as the underlying code changes meaning in an attacker controlled way -- which happens to be feasible in common JIT engines out there."

"But since operating system kernels nowadays run JIT engines like cBPF, the reach in the end is similar to Training Solo and the like. More fundamentally, BTR exposes a flaw in the way modern CPUs handle self-modifying / JITted code. They all have support to resync microarchitectural structures such as instruction/data caches when code gets rewritten. BTR shows that this is insufficient and that leaving indirect branch prediction state stale has significant security implications as well."

Following responsible disclosure, mitigations for BTR have been released and merged into the Linux kernel (
[CVE-2026-64507](https://lore.kernel.org/linux-cve-announce/2026072554-CVE-2026-64507-5288@gregkh/)
and
[CVE-2026-64508](https://lore.kernel.org/linux-cve-announce/2026072554-CVE-2026-64508-fe26@gregkh/)
).

"GraalVM instead hinders region reuse by
[randomizing JIT code-cache locations](https://github.com/oracle/graal/pull/14261)
," the researchers said. "Mozilla considered
[IBPB](https://docs.kernel.org/admin-guide/hw-vuln/spectre.html)
[Indirect Branch Predictor Barrier]-based mitigations, but is currently prioritizing the completion and deployment of site isolation."

To sum up, the discovery of BTR has three major implications, the researchers said -

* *In-place Spectre-v2 attacks are practical in the "temporal" domain.*
* *JIT engines need to either deploy isolation mechanisms (à la site isolation) or deploy specific mitigations against BTR (e.g., cBPF's IBPB mitigation).*
* *Modern CPUs do not resync all the necessary microarchitectural state when code gets rewritten (and there is no easy way to address this, since syncing everything up is expensive), so other BTR-like problems may come to the surface in the future.*

The disclosure comes nearly two months after MIT CSAIL researchers Daniël Trujillo and Mengjia Yan disclosed a speculative execution attack technique called
[Interrupt Injection](https://thehackernews.com/2026/08/new-interrupt-injection-attack-can.html)
that can bypass Spectre v2 defenses and leak arbitrary kernel memory from Intel- and AMD-based Linux systems.

*(The story was updated after publication to include additional responses from VUSec.)*